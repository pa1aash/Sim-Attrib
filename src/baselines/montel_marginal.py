"""Anau Montel, Alvey & Weniger (2025)'s trials-corrected global-null test (their Section
II.3), run against this project's own simulator instead of asserted as "not run here".

WHY THIS EXISTS (W16-2)
------------------------
`paper/main.tex` Section 2 calls this paper's method a "baseline" and then states, in its
own closing sentence, that the comparison on this project's own six-column confound "was
not run here" -- asserted, not measured. This module runs it, on the real simulator, and
`results/montel_marginal_test.yaml` is the number the paper's prose is rewritten to report.

THE CONSTRUCTION, AS THEY STATE IT (Section II.3, read in full via the vault note
`research/notes/tests-for-model-misspecification-in-simulation-based-inference.md`)
-----------------------------------------------------------------------------------
For a set of N_t "localized" test statistics t_i(x), each with a Monte-Carlo p-value

    p_i(x_obs) = P_{x ~ p_sim}( t_i(x) >= t_i(x_obs) )                       (their eq. 6/7)

they do NOT stop at the per-test p-values, because doing so ignores the multiple-testing
"look-elsewhere effect". Their global (trials-corrected) p-value is obtained by:

  1. drawing N_mc samples from the null/base model;
  2. computing all N_t p-values for each of those N_mc samples;
  3. taking the MINIMUM p-value across the N_t tests, for each of the N_mc samples --
     this is what "accounts for their correlation": the minima are drawn from whatever
     joint dependence the N_t tests actually have, not from an independence assumption;
  4. comparing the observed minimum p-value against that empirical null distribution of
     minima. The global p-value is the fraction of null minima at least as extreme.

That is implemented here exactly: :func:`calibrate_global_null` performs steps 1-3,
:func:`evaluate` performs step 4. Nothing about the trials-correction is approximated.

WHAT IS SIMPLIFIED, STATED PRECISELY (S8 / W16-2's "do not approximate without saying so")
--------------------------------------------------------------------------------------------
Their localized test statistics t_i(x) = -2 ln[p_sim(x) / p_dist(x|i)] are log-likelihood
RATIOS against a specific alternative, estimated by a trained neural network (their
Appendix A) because their setting is general SBI: p_sim and p_dist are intractable
densities over a high-dimensional x, so a classifier-based density-ratio estimate is the
only way to get t_i(x) at all.

That machinery is not needed here and is NOT reimplemented. This project's summary set
`S_B` is ten deterministic, low-dimensional coordinates of the simulator's output (binned
reported incidence), each with a directly Monte-Carlo-computable null distribution. So the
localized test statistic used here is the exact standardised-deviation statistic

    t_i(x) = ((s_i(x) - mu_i) / sigma_i) ** 2                                    (*)

with mu_i, sigma_i the null (H0, eta=0) mean and standard deviation of summary coordinate
i, estimated directly from simulator draws -- large when coordinate i deviates from its
null-predicted value, exactly the property their t_i is built to have. (*) is EXACT given
mu_i, sigma_i (no neural approximation); mu_i, sigma_i are themselves Monte Carlo estimates,
whose own Monte Carlo error is controlled by using a large, independent reference batch
(N_NORM below) and reported nowhere as more precise than it is.

The object under test in W16-2 -- whether the paper's baseline's global-null test and its
arg-min analysis resolve the six-column equivalence-class ambiguity -- is a property of the
TRIALS-CORRECTION MACHINERY applied to per-summary-coordinate tests, not of how any one
t_i is computed. Substituting an exact per-summary statistic for their neural one changes
nothing about what is being asked, and removes a source of approximation error (a trained
classifier) that this project has no need to introduce.

THE SIMULATOR CANNOT EXPRESS A SIX-COLUMN DISTORTION AS ONE FORWARD CALL
---------------------------------------------------------------------------
`src/simulators/sir3.py`'s `simulate` takes ONE `families` flag ("base" or "adversarial")
applied to all three components in that one call -- there is no per-component family
selection. The six-column object in `results/robustness/k6_spectrum.yaml` is a LINEAR
object: six one-parameter Jacobian columns (three per family set) stacked side by side,
built from six separate small-eta finite differences, never as one jointly-mixed nonlinear
trajectory. Generating a single "observed dataset" that is simultaneously base-family in
one component and adversarial-family in another is therefore not something `simulate` can
produce, and extending it to do so is out of this session's scope.

What IS directly simulatable, and what the confound's own prose in `audit/FINAL_CLAIMS.md`
names, is the WITHIN-one-family-set version of the confound: "a drifting removal hazard is
nearly indistinguishable from a constant hazard change combined with a drifting reporting
rate." Both halves of that sentence are single-family-set scenarios --
  * "a drifting removal hazard"                         -> families="base",    eta=(0, e, 0)
  * "constant hazard change + drifting reporting rate"  -> families="adversarial", eta=(0, e, e)
-- and comparing the global test's arg-min pattern between them is a direct test of whether
Montel et al.'s per-summary-coordinate local tests can tell these two mechanisms apart, which
is exactly the equivalence-class ambiguity `results/robustness/k6_spectrum.yaml`'s near-null
directions v5/v6 name (both load on progression AND observation, negligibly on transmission).

CASES RUN
----------
  BBB              families="base",       eta = ETA_SCALE * (1, 1, 1)   -- the declared base
                                                                            corner, genuinely
                                                                            misspecified in
                                                                            all three components
  AAA              families="adversarial", eta = ETA_SCALE * (1, 1, 1)   -- the declared
                                                                            adversarial corner
  confound_progression_only        families="base",       eta = (0, ETA_SCALE, 0)
  confound_progression_and_observation  families="adversarial", eta = (0, ETA_SCALE, ETA_SCALE)
  null_control     families="base",       eta = (0, 0, 0)   -- H0 TRUE. The S5 vacuous-flag
                                                                 check: the global test must be
                                                                 able to NOT reject.

Every eta above uses ETA_SCALE (0.1 native units, THRESHOLDS' own definition of "one
distortion unit" = a 10% relative deformation) -- a real, finite, non-infinitesimal
misspecification, not the infinitesimal steps the rank diagnostic uses for its Jacobian.

    python -m src.baselines.montel_marginal
"""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from ..provenance import header, now_iso
from ..runlock import check_pidfile, write_pidfile
from ..simulators import sir3
from ..simulators.sir3 import BASE, ETA_SCALE, with_params
from ..simulators.summaries import SUMMARY_LABELS, SUMMARY_SETS

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results"

SUMMARY_NAME = "S_B"
ALPHA = 0.05

#: Independent batch sizes for the three null-distribution roles. Kept SEPARATE (distinct
#: seed blocks) so that no batch is used both to define a quantity and to evaluate it against
#: itself, which would understate the test's own Monte Carlo error.
N_NORM = 3000   #: estimates mu_i, sigma_i in (*)
N_REF = 3000    #: reference null batch for the per-summary p_i lookup (step 1-2's "N_mc" role
                #: for the LOCAL tests; kept apart from N_CALIB below)
N_CALIB = 1500  #: null draws whose per-summary p-values (looked up against N_REF) are minimised
                #: to build the empirical null distribution of the minimum p-value -- their
                #: "N_mc" for the GLOBAL test


def local_test_statistics(s: np.ndarray, mu: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    """``t_i(x)`` of the module docstring's equation (*). Larger = more deviant."""
    z = (np.asarray(s, dtype=float) - mu) / sigma
    return z * z


def summary_batch(n: int, seed0: int, *, eta: tuple[float, float, float],
                   params: sir3.SIR3Params) -> np.ndarray:
    """``n`` independent draws of :data:`SUMMARY_NAME`, shape ``(n, d)``."""
    fn = SUMMARY_SETS[SUMMARY_NAME]
    rows = []
    for r in range(n):
        out = sir3.simulate(eta, seed=seed0 + r, params=params)
        rows.append(fn(out))
    return np.asarray(rows, dtype=float)


def local_p_values(t_obs: np.ndarray, t_ref: np.ndarray) -> np.ndarray:
    """Per-summary upper-tail Monte Carlo p-values (their footnote 5, eq. 6/7).

    ``t_ref`` is ``(N_ref, d)`` -- one column per summary coordinate's null distribution of
    the local test statistic. The ``+1 / (n+1)`` form is the standard finite-sample-correct
    Monte Carlo p-value (Davison & Hinkley 1997 Alg. 4.1): it never reports exactly zero,
    which a raw ``count/n`` would for any p smaller than ``1/n`` and which would misreport a
    global test as impossibly certain rather than as "below this batch's resolution".
    """
    n = t_ref.shape[0]
    ge = (t_ref >= t_obs[None, :]).sum(axis=0)
    return (1.0 + ge) / (n + 1.0)


def calibrate_global_null(t_ref: np.ndarray, t_calib: np.ndarray) -> np.ndarray:
    """The null distribution of the MINIMUM p-value across summary coordinates.

    For each of the ``N_calib`` null draws, compute its ``d`` local p-values against
    ``t_ref`` (so the calibration set and the reference set are DIFFERENT batches -- neither
    ``t_ref`` nor ``t_calib`` is compared against itself), then take the minimum over
    coordinates. This is steps 1-3 of the module docstring's construction; the resulting
    array of ``N_calib`` minima IS the trials-corrected null the observed minimum is judged
    against, so it is what "accounts for correlation" among the ten summary coordinates --
    whatever dependence the ten local tests actually have, it is baked into these minima by
    construction, not assumed away.
    """
    p_calib = np.array([local_p_values(t_calib[j], t_ref) for j in range(t_calib.shape[0])])
    return p_calib.min(axis=1)


def cp_upper_bound_zero_count(n: int, alpha: float = ALPHA) -> float:
    """Exact Clopper-Pearson upper confidence bound when zero of ``n`` trials succeed.

    ``1 - alpha**(1/n)``, the exact binomial upper limit at zero successes (equivalent to
    the standard "rule of three" for large ``n``: ``approx -ln(alpha)/n``). Used to report a
    global p-value as an upper bound, not as a literal zero, when it falls below what
    ``N_CALIB`` null draws can resolve.
    """
    return float(1.0 - alpha ** (1.0 / n))


def evaluate(eta: tuple[float, float, float], params: sir3.SIR3Params, seed_obs: int, *,
             mu: np.ndarray, sigma: np.ndarray, t_ref: np.ndarray, m_calib: np.ndarray,
             labels: list[str]) -> dict[str, Any]:
    """Run the full test on ONE observed dataset drawn under ``(eta, params)``."""
    s_obs = summary_batch(1, seed_obs, eta=eta, params=params)[0]
    t_obs = local_test_statistics(s_obs, mu, sigma)
    p_obs = local_p_values(t_obs, t_ref)
    m_obs = float(p_obs.min())
    argmin_idx = int(np.argmin(p_obs))

    n_calib = len(m_calib)
    n_at_least_as_extreme = int(np.sum(m_calib <= m_obs))
    global_p = (1.0 + n_at_least_as_extreme) / (n_calib + 1.0)
    global_p_is_upper_bound = n_at_least_as_extreme == 0

    # arg-min TIES: report every coordinate within one N_REF resolution unit of the minimum
    # p-value, not only the single smallest-index argmin, since a resolved ambiguity should
    # show as a genuinely narrow arg-min and a confound should show as a broad one.
    resolution = 1.0 / (t_ref.shape[0] + 1.0)
    near_min_idx = [i for i in range(len(p_obs)) if p_obs[i] <= m_obs + resolution]

    return {
        "eta": [float(x) for x in eta],
        "families": params.families,
        "seed_obs": seed_obs,
        "summary_values": [float(x) for x in s_obs],
        "local_test_statistics": [float(x) for x in t_obs],
        "local_p_values": [float(x) for x in p_obs],
        "min_local_p_value": m_obs,
        "argmin_coordinate_index": argmin_idx,
        "argmin_coordinate_label": labels[argmin_idx],
        "near_min_coordinate_labels": [labels[i] for i in near_min_idx],
        "n_coordinates_within_resolution_of_the_minimum": len(near_min_idx),
        "global_p_value": global_p,
        "global_p_value_is_upper_bound": global_p_is_upper_bound,
        "global_p_value_upper_bound_if_zero_count": (
            cp_upper_bound_zero_count(n_calib) if global_p_is_upper_bound else None
        ),
        "n_calib_minima_at_least_as_extreme": n_at_least_as_extreme,
        "n_calib": n_calib,
        "verdict": "REJECT H0" if global_p < ALPHA else "DO NOT REJECT H0",
        "alpha": ALPHA,
    }


CASES: dict[str, dict[str, Any]] = {
    "BBB": {
        "families": "base",
        "eta_units": (1.0, 1.0, 1.0),
        "what_this_is": (
            "The declared base corner (docs/THRESHOLDS.md / results/robustness/k6_spectrum.yaml "
            "'BBB'), genuinely misspecified in all three components at one native distortion "
            "unit."
        ),
    },
    "AAA": {
        "families": "adversarial",
        "eta_units": (1.0, 1.0, 1.0),
        "what_this_is": "The declared adversarial corner, same magnitude, all three components.",
    },
    "confound_progression_only": {
        "families": "base",
        "eta_units": (0.0, 1.0, 0.0),
        "what_this_is": (
            "'A drifting removal hazard' (audit/FINAL_CLAIMS.md C3): only the progression "
            "component is distorted, under the base family."
        ),
    },
    "confound_progression_and_observation": {
        "families": "adversarial",
        "eta_units": (0.0, 1.0, 1.0),
        "what_this_is": (
            "'A constant hazard change combined with a drifting reporting rate' "
            "(audit/FINAL_CLAIMS.md C3): progression AND observation distorted together, "
            "under the adversarial family -- the mechanism combination the paper's own prose "
            "says is nearly indistinguishable from confound_progression_only above."
        ),
    },
    "null_control": {
        "families": "base",
        "eta_units": (0.0, 0.0, 0.0),
        "what_this_is": (
            "S5 vacuous-flag check: H0 is TRUE here (eta = 0 exactly). The global test must "
            "be able to NOT reject under this case, or its verdict carries no information -- "
            "a test that rejects regardless of input is as suspect as a flag that is always "
            "true."
        ),
    },
    "strong_misspecification_control": {
        "families": "adversarial",
        "eta_units": (3.0, 3.0, 3.0),
        "what_this_is": (
            "Positive-power check: a much larger, unambiguous distortion (3x the declared "
            "corners). The global test should reject here with a smaller p-value than at the "
            "declared corners, confirming the test's power scales with the actual size of the "
            "misspecification rather than being a fixed artefact of the machinery."
        ),
    },
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Anau Montel et al. global-null test (W16-2)")
    ap.add_argument("--seed", type=int, default=20260826)
    args = ap.parse_args(argv)

    command = f"python -m src.baselines.montel_marginal --seed {args.seed}"
    started = now_iso()

    out_path = OUT / "montel_marginal_test.yaml"
    lock = Path(tempfile.gettempdir()) / "sim-attrib-runs" / "montel_marginal_test.json"
    prior = check_pidfile(lock)
    if prior["alive"]:
        raise SystemExit(
            f"REFUSING TO START: pid {prior['pid']} is already running "
            f"{prior['command']!r} and will write {prior.get('outputs')}. "
            f"Standing constraint S3. Kill it deliberately or wait."
        )
    write_pidfile(lock, module="src.baselines.montel_marginal",
                  outputs=[str(out_path.relative_to(REPO))])
    print(f"pidfile {lock} (pid {__import__('os').getpid()})", flush=True)

    labels = list(SUMMARY_LABELS[SUMMARY_NAME])
    d = len(labels)

    print(f"mu/sigma: {N_NORM} null draws (seed0={args.seed})", flush=True)
    norm_batch = summary_batch(N_NORM, args.seed, eta=(0.0, 0.0, 0.0), params=BASE)
    mu = norm_batch.mean(axis=0)
    sigma = norm_batch.std(axis=0, ddof=1)

    seed_ref = args.seed + 1_000_000
    print(f"local p-value reference: {N_REF} null draws (seed0={seed_ref})", flush=True)
    ref_batch = summary_batch(N_REF, seed_ref, eta=(0.0, 0.0, 0.0), params=BASE)
    t_ref = np.array([local_test_statistics(ref_batch[i], mu, sigma) for i in range(N_REF)])

    seed_calib = args.seed + 2_000_000
    print(f"global-null calibration: {N_CALIB} null draws (seed0={seed_calib})", flush=True)
    calib_batch = summary_batch(N_CALIB, seed_calib, eta=(0.0, 0.0, 0.0), params=BASE)
    t_calib = np.array([local_test_statistics(calib_batch[i], mu, sigma)
                        for i in range(N_CALIB)])
    m_calib = calibrate_global_null(t_ref, t_calib)

    n_simulator_runs = N_NORM + N_REF + N_CALIB

    results: dict[str, Any] = {}
    for case_index, (name, spec) in enumerate(CASES.items()):
        # A deterministic per-case offset, NOT Python's hash() -- str hashing is randomised
        # per process (PYTHONHASHSEED) unless disabled, which would silently make x_obs's
        # seed, and therefore the reported numbers, non-reproducible run to run even at a
        # fixed --seed.
        eta = tuple(float(u) * ETA_SCALE for u in spec["eta_units"])
        params = with_params(families=spec["families"])
        seed_obs = args.seed + 3_000_000 + case_index * 1_000
        r = evaluate(eta, params, seed_obs, mu=mu, sigma=sigma, t_ref=t_ref, m_calib=m_calib,
                    labels=labels)
        r["what_this_is"] = spec["what_this_is"]
        results[name] = r
        n_simulator_runs += 1
        print(f"  {name:38s} global_p={r['global_p_value']:.5g}"
              f"{'  (upper bound)' if r['global_p_value_is_upper_bound'] else ''} "
              f"-> {r['verdict']:16s} argmin={r['argmin_coordinate_label']}", flush=True)

    # S5 vacuous-flag test, made explicit rather than left implicit in the case table above.
    vacuous_flag_check = {
        "claim": "the global test can produce DO NOT REJECT under some input, not only REJECT",
        "null_control_verdict": results["null_control"]["verdict"],
        "null_control_global_p": results["null_control"]["global_p_value"],
        "passes": results["null_control"]["verdict"] == "DO NOT REJECT H0",
    }
    if not vacuous_flag_check["passes"]:
        print("\nWARNING: null_control REJECTED. The test may be vacuously rejecting "
              "regardless of input -- see vacuous_flag_check in the output file.", flush=True)

    # Does the arg-min analysis resolve the confound? Compare the two confound sub-cases'
    # flagged-coordinate sets directly, rather than leaving the reader to infer it from two
    # separate blocks.
    a = set(results["confound_progression_only"]["near_min_coordinate_labels"])
    b = set(results["confound_progression_and_observation"]["near_min_coordinate_labels"])
    argmin_a = results["confound_progression_only"]["argmin_coordinate_label"]
    argmin_b = results["confound_progression_and_observation"]["argmin_coordinate_label"]
    confound_resolution = {
        "question": (
            "does the arg-min analysis distinguish 'drifting removal hazard alone' from "
            "'constant hazard change + drifting reporting rate', the two mechanisms "
            "results/robustness/k6_spectrum.yaml's near-null directions v5/v6 confound?"
        ),
        "confound_progression_only_argmin": argmin_a,
        "confound_progression_and_observation_argmin": argmin_b,
        "argmins_identical": argmin_a == argmin_b,
        "confound_progression_only_near_min_set": sorted(a),
        "confound_progression_and_observation_near_min_set": sorted(b),
        "near_min_set_jaccard_overlap": (
            len(a & b) / len(a | b) if (a | b) else None
        ),
        "resolves_the_ambiguity": not (argmin_a == argmin_b or (len(a & b) / len(a | b) > 0.5
                                                                 if (a | b) else False)),
    }

    doc: dict[str, Any] = {
        "provenance": header(script="src/baselines/montel_marginal.py", command=command,
                             seed=args.seed, started=started),
        "what_this_is": (
            "W16-2: Anau Montel, Alvey & Weniger (2025)'s trials-corrected minimum-per-"
            "summary-statistic global-null test (their Section II.3), run against this "
            "project's own simulator and summary set S_B. Replaces the paper's prior 'not "
            "run here' sentence with a measured result. See the module docstring in "
            "src/baselines/montel_marginal.py for the exact construction and the one stated "
            "simplification (exact per-summary test statistics in place of their neural "
            "local tests; the trials-corrected aggregation itself is implemented exactly)."
        ),
        "summary_set": SUMMARY_NAME,
        "coordinate_labels": labels,
        "d": d,
        "settings": {
            "seed": args.seed, "n_norm": N_NORM, "n_ref": N_REF, "n_calib": N_CALIB,
            "alpha": ALPHA, "eta_scale": ETA_SCALE, "n_simulator_runs": n_simulator_runs,
        },
        "mu": [float(x) for x in mu],
        "sigma": [float(x) for x in sigma],
        "cases": results,
        "vacuous_flag_check": vacuous_flag_check,
        "confound_resolution": confound_resolution,
    }

    OUT.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, width=100)
    print(f"\nwrote {out_path.relative_to(REPO)}", flush=True)
    print(f"\nvacuous-flag check passes: {vacuous_flag_check['passes']}", flush=True)
    print(f"confound resolves: {confound_resolution['resolves_the_ambiguity']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
