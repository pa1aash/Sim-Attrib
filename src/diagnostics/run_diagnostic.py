"""Run the Jacobian rank/coherence diagnostic and emit the results files.

Usage
-----
    python -m src.diagnostics.run_diagnostic --seed 20260820

Emits, into ``results/``:

  * ``jacobian_rank.S_A.yaml``, ``jacobian_rank.S_B.yaml``, ``jacobian_rank.S_C.yaml``
        one per summary set in the closed list of ``docs/THRESHOLDS.md`` §1.1;
  * ``jacobian_rank.S_A.no_crn_control.yaml``
        the negative control: the same sweep with independent noise across the +h and -h
        evaluations, which is what the common-random-numbers construction exists to avoid;
  * ``floor_check.yaml``
        the random-attributor floor check, run first, because it validates the harness;
  * ``STOP_CONDITION_FIRED.md``
        only if the D4 STOP condition fires (all three summary sets inseparable).

Every number these files contain traces to this script, to the recorded commit, and to the
recorded seed, per ``PROVENANCE.md``. No number is hand-typed into a markdown file.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from ..provenance import header, now_iso
from ..simulators import sir3
from ..simulators.sir3 import BASE, COMPONENTS, ETA_SCALE, K, prior_predictive_stats
from ..simulators.summaries import (
    GROWTH_WINDOW,
    N_BINS,
    SUMMARY_LABELS,
    SUMMARY_SETS,
)
from .floor_check import floor_check
from .jacobian_rank import (
    COHERENCE_FLAG,
    COLNORM_INVISIBLE,
    H_VALUES,
    KAPPA_MAX,
    PLATEAU_REL_TOL,
    RESOLVE_FACTOR,
    TAU,
    VK_MIN,
    analyse,
    estimate_jacobian,
)

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "results"

#: How R2 and this diagnostic are framed, carried into every results file so that the
#: description a reader sees matches the project's CURRENT claim rather than a superseded
#: one. Session G3 brief §2.10.
FRAMING = (
    "This diagnostic is INFRASTRUCTURE for a composition paper (maximized Monte Carlo, "
    "Dufour 2006, composed with a selection event for component-level misspecification "
    "attribution). It is NOT a claimed method contribution: the rank-and-condition-number "
    "screen on a sensitivity matrix is Cintron-Arias, Banks, Capaldi & Lloyd (2009) and "
    "finite differencing under simulation noise is More & Wild (2012). See "
    "docs/DECISIONS.md D-6 and audit/R2_THREAT_CHECK.md. Its purpose here is to decide "
    "whether component attribution is well posed for THIS simulator under THIS closed list "
    "of summary sets -- the precondition, per Kahl et al. (2019), for the composition being "
    "worth building at all."
)

LEAKAGE_STATEMENT = (
    "The diagnostic never receives a component index, a ground-truth label, or any "
    "indication of which component is responsible for anything. Its whole input is the "
    "simulator as a callable, the distortion basis (that there are K one-parameter "
    "families and that perturbing family k means setting eta_k), and the resulting summary "
    "vectors. It computes a property of the map s(eta), not a guess about a hidden truth, "
    "so there is no hidden truth available to leak."
)


def _normalisation_block(name: str, sd: np.ndarray, mean: np.ndarray, r_norm: int,
                         seed_norm: int, p_ref: float) -> dict[str, Any]:
    """The normalisation record THRESHOLDS §0 requires in the results file, not only in code."""
    return {
        "why_this_matters": (
            "The rank of J is NOT scale-invariant. Rescaling a summary or reparametrising "
            "eta_k changes the singular values and can change the numerical rank. Every "
            "threshold below is a statement about these normalisations and about nothing "
            "else."
        ),
        "summaries": {
            "rule": "each summary coordinate divided by its prior-predictive standard deviation at eta = 0",
            "n_replicates_R_norm": int(r_norm),
            "seed0": int(seed_norm),
            "coordinate_labels": list(SUMMARY_LABELS[name]),
            "prior_predictive_sd": [float(x) for x in sd],
            "prior_predictive_mean": [float(x) for x in mean],
            "degenerate_coordinates_dropped": [],
        },
        "distortions": {
            "rule": "each eta_k divided by a fixed relative perturbation scale, identical across k",
            "eta_scale": float(ETA_SCALE),
            "meaning": (
                "One normalised unit is a 10% relative deformation of the component. Because "
                "eta_scale is COMMON across k, scaling it multiplies J by a constant and "
                "therefore leaves the normalised spectrum, the numerical rank at a relative "
                "tolerance, and the condition number unchanged; only the column-norm "
                "(invisible-component) test depends on its absolute value."
            ),
            "transmission_saturation_reference_prevalence_p_ref": float(p_ref),
        },
        "interpretation_of_J_entry": (
            "J[d, k] is the change in summary d, in prior-predictive standard deviations, "
            "produced by a full-scale (one normalised unit) relative distortion of component k."
        ),
    }


def _simulator_block(p_ref: float) -> dict[str, Any]:
    return {
        "module": "src/simulators/sir3.py",
        "components_K": K,
        "components": list(COMPONENTS),
        "base_parameters": {
            "N": BASE.N, "I0": BASE.I0, "beta": BASE.beta, "gamma": BASE.gamma,
            "R0_basic": BASE.beta / BASE.gamma, "T_days": BASE.T_days,
            "substeps_per_day": BASE.substeps, "rho": BASE.rho,
            "delay_mean_days": BASE.delay_mean, "delay_shape": BASE.delay_shape,
            "delay_kernel_len_days": BASE.delay_len, "obs_sigma": BASE.obs_sigma,
        },
        "integrator": "fixed-step RK4 (not adaptive: adaptive step selection is itself a source of computational noise)",
        "distortion_families": {
            "transmission": "beta*S*I/N -> beta*S*I/N / (1 + eta_1*(I/N)/p_ref)   [saturating incidence; prevalence nonlinearity]",
            "progression": "gamma -> gamma*exp(eta_2*(t/T - 0.5))   [mean-centred log-linear hazard drift; timing/trend]",
            "observation": "rho -> rho*exp(eta_3)   [reporting-fraction multiplier; pure amplitude]",
        },
        "distortion_identity_at_zero": "delta_k(.;0) == base simulator exactly, tested in tests/test_sir3.py",
        "p_ref_peak_prevalence_fraction": float(p_ref),
        "summary_definitions": {
            "growth_rate_window_days": list(GROWTH_WINDOW),
            "n_bins_S_B": N_BINS,
            "peak_statistics": (
                "peak height and peak time are computed by PARABOLIC INTERPOLATION about the "
                "discrete argmax. A discrete argmax is integer-valued and therefore a step "
                "function of eta, with no finite-difference derivative at any h. This is a "
                "substantive choice about the summary, not an implementation detail."
            ),
        },
    }


def _write(path: Path, doc: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, width=100)
    print(f"wrote {path.relative_to(REPO)}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--seed", type=int, default=20260820)
    ap.add_argument("--replicates", type=int, default=128,
                    help="R, replicates averaged per finite-difference evaluation")
    ap.add_argument("--norm-replicates", type=int, default=2000,
                    help="R_norm, replicates used to estimate prior-predictive sd")
    ap.add_argument("--floor-draws", type=int, default=10_000)
    args = ap.parse_args(argv)

    command = "python -m src.diagnostics.run_diagnostic " + " ".join(
        f"--{k.replace('_', '-')} {v}" for k, v in vars(args).items()
    )
    started = now_iso()
    seed_norm = args.seed + 900_000

    # --- 1. floor check FIRST: it validates the harness before anything rests on it ------
    fc = floor_check(n_draws=args.floor_draws, seed=args.seed)
    _write(RESULTS / "floor_check.yaml", {
        "provenance": header(script="src/diagnostics/floor_check.py",
                             command=command, seed=args.seed, started=started),
        "framing": FRAMING,
        "floor_check": fc,
    })
    if not fc["passes"]:
        print("FLOOR CHECK FAILED -- harness is not trustworthy; stopping", file=sys.stderr)
        return 2

    p_ref = sir3.peak_prevalence_fraction(BASE)

    # --- 2. prior-predictive normalisation ----------------------------------------------
    print(f"estimating prior-predictive sd from R_norm={args.norm_replicates} replicates ...")
    stats = prior_predictive_stats(SUMMARY_SETS, n_replicates=args.norm_replicates,
                                   seed0=seed_norm)
    sd_map = {name: sd for name, (_m, sd) in stats.items()}
    mean_map = {name: m for name, (m, _sd) in stats.items()}

    # --- 3. the sweep, all summary sets from the same simulator runs ---------------------
    print(f"running h-sweep over {list(H_VALUES)} with R={args.replicates} ...")
    sweeps = estimate_jacobian(SUMMARY_SETS, sd_map, h_values=H_VALUES,
                               n_replicates=args.replicates, seed0=args.seed, crn=True)

    verdicts: dict[str, dict[str, Any]] = {}
    for name in SUMMARY_SETS:
        a = analyse(sweeps[name])
        verdicts[name] = a
        _write(RESULTS / f"jacobian_rank.{name}.yaml", {
            "provenance": header(script="src/diagnostics/run_diagnostic.py",
                                 command=command, seed=args.seed, started=started),
            "framing": FRAMING,
            "summary_set": name,
            "summary_coordinate_labels": list(SUMMARY_LABELS[name]),
            "component_labels": list(COMPONENTS),
            "simulator": _simulator_block(p_ref),
            "normalisation": _normalisation_block(name, sd_map[name], mean_map[name],
                                                  args.norm_replicates, seed_norm, p_ref),
            "estimator": {
                "scheme": "central differences, J[:,k] = mean_r [s(+h e_k; seed_r) - s(-h e_k; seed_r)] / (2h) / sd",
                "common_random_numbers": True,
                "why_common_random_numbers": (
                    "The +h and -h evaluations use the SAME replicate seeds. Without this the "
                    "two evaluations draw independent observation noise, the difference "
                    "quotient inherits noise of order obs_sigma/h, and at small h that term "
                    "swamps the signal: the finite difference then measures the simulator's "
                    "randomness rather than its response. See the no_crn_control results file, "
                    "where the leading singular value grows exactly as 1/h."
                ),
                "n_replicates_R": int(args.replicates),
                "seed0": int(args.seed),
                "n_simulator_runs": int(sweeps[name].n_simulations),
                "noise_model": "lognormal",
                "why_not_a_count_noise_model": (
                    "Under common random numbers a count-valued observation layer (Poisson, "
                    "negative binomial) is a STEP function of eta: the difference quotient is "
                    "either exactly 0 or O(1/h) and no derivative exists at any h. A "
                    "continuous multiplicative layer multiplies the derivative instead of "
                    "quantising it. The observation noise model therefore determines whether J "
                    "is estimable at all, which is a modelling constraint and not an "
                    "implementation detail."
                ),
            },
            "thresholds_pre_registered": {
                "source": "docs/THRESHOLDS.md, written before any singular value existed in this repository",
                "tau_rank_tolerance": TAU,
                "kappa_max": KAPPA_MAX,
                "colnorm_invisible": COLNORM_INVISIBLE,
                "coherence_flag": COHERENCE_FLAG,
                "vk_min_equivalence_class": VK_MIN,
                "resolve_factor": RESOLVE_FACTOR,
                "h_values": list(H_VALUES),
                "plateau_rel_tol": {
                    "value": PLATEAU_REL_TOL,
                    "note": (
                        "FIXED IN SESSION G3, not in THRESHOLDS.md, which pre-registered the "
                        "resolution criterion but not how the plateau is identified. Stated in "
                        "src/diagnostics/jacobian_rank.py and fixed before any singular value "
                        "existed."
                    ),
                },
            },
            "results": a,
            "leakage_checked": True,
            "leakage_how": LEAKAGE_STATEMENT,
        })

    # --- 4. negative control: the same sweep without common random numbers ---------------
    print("running no-CRN negative control on S_A ...")
    ctrl_sweeps = estimate_jacobian({"S_A": SUMMARY_SETS["S_A"]}, {"S_A": sd_map["S_A"]},
                                    h_values=H_VALUES, n_replicates=args.replicates,
                                    seed0=args.seed, crn=False)
    ctrl = analyse(ctrl_sweeps["S_A"])
    _write(RESULTS / "jacobian_rank.S_A.no_crn_control.yaml", {
        "provenance": header(script="src/diagnostics/run_diagnostic.py",
                             command=command, seed=args.seed, started=started),
        "framing": FRAMING,
        "what_this_is": (
            "NEGATIVE CONTROL, not a result about the simulator. The identical sweep run with "
            "INDEPENDENT noise realisations across the +h and -h evaluations, i.e. without "
            "common random numbers. It exists to demonstrate the failure mode rather than to "
            "assert it: compare the singular values here against jacobian_rank.S_A.yaml."
        ),
        "expected_behaviour": (
            "Without common random numbers the difference quotient carries noise of order "
            "obs_sigma/h, so the leading singular value should grow as 1/h and no plateau "
            "should be identifiable."
        ),
        "summary_set": "S_A",
        "common_random_numbers": False,
        "results": ctrl,
        "leakage_checked": True,
        "leakage_how": LEAKAGE_STATEMENT,
    })

    # --- 5. the D4 STOP condition -------------------------------------------------------
    inseparable = {n: verdicts[n]["inseparable"] for n in SUMMARY_SETS}
    separable = [n for n, bad in inseparable.items() if not bad]
    print("\nD4 STOP condition:")
    for n, bad in inseparable.items():
        print(f"  {n}: {'INSEPARABLE' if bad else 'separable'} -- {verdicts[n]['inseparable_reason']}")

    stop_path = RESULTS / "STOP_CONDITION_FIRED.md"
    if all(inseparable.values()):
        lines = [
            "# D4 STOP CONDITION FIRED",
            "",
            "All three summary sets in the closed list of `docs/THRESHOLDS.md` §1.1 are",
            "inseparable under the pre-registered criteria. **This is a legitimate negative",
            "identifiability result for this simulator, not a project failure.**",
            "",
            f"Generated by `src/diagnostics/run_diagnostic.py`, seed `{args.seed}`.",
            "",
            "| Summary set | Verdict | Reason |",
            "|---|---|---|",
        ]
        for n in SUMMARY_SETS:
            lines.append(f"| {n} | INSEPARABLE | {verdicts[n]['inseparable_reason']} |")
        stop_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"wrote {stop_path.relative_to(REPO)}")
    else:
        if stop_path.exists():
            stop_path.unlink()
        print(f"\nSTOP condition did NOT fire. Separable summary set(s): {separable}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
