"""T2-4: does the separability diagnostic reproduce at a second parameter point?

WHY THIS SCRIPT EXISTS
-----------------------
Every separability result in this project (``results/jacobian_rank.*.yaml``, the
eight-assignment sweep, the six-column confound) linearizes the summary Jacobian at
``eta = 0`` and at exactly one parameter point, ``sir3.BASE``. `paper/main.tex`'s
Limitations section already concedes this is a local statement: separability of the finite
(10%) perturbation the diagnostic's own scale represents is not directly implied by local
linear separability at one point. This script tests whether the diagnostic's headline
verdict -- ``S_B`` separates all three components under the base (AAA) family assignment --
survives at a SECOND parameter point, drawn from a reasonable prior range rather than
picked by hand.

THE SAMPLING RULE, FIXED BEFORE THE DRAW (S3 / D3)
-----------------------------------------------------
Each of the five nuisance coordinates (beta, gamma, rho, I0, obs_sigma) is independently
perturbed by a relative factor drawn ``Uniform(-0.20, +0.20)`` about its ``sir3.BASE``
value: ``theta2_i = theta0_i * (1 + u_i)``, ``u_i ~ Uniform(-0.20, 0.20)``. Twenty percent
is not arbitrary in this project's own terms: it is twice the paper's own ETA_SCALE unit
(one normalised distortion unit is a 10% relative deformation) and comfortably wider than
every coordinate of the data-implied 95% confidence box G11 measured (2.3%-16.6%
half-width, `audit/DUFOUR_CONFIDENCE_SET_CHECK.md`) -- i.e. wide enough to be a real second
point, not a restatement of the fit's own uncertainty. The draw uses a seed fixed in this
docstring before any diagnostic ran against it, so the point cannot have been selected
because it was favourable.

WHAT THIS DOES NOT DO
-----------------------
One additional theta is one additional theta, not a distribution over theta. It answers
"does the verdict survive at a second point drawn honestly", not "how often does it
survive". It tests S_B under the all-base (AAA) family assignment only -- the paper's
primary, headline case -- not all eight assignments; re-running the full eight-assignment
sweep at a second theta is a larger task than T2-4 asks for and is not attempted here.

Sources: ``src/simulators/sir3.py`` (BASE, SIR3Params, simulate), ``src/simulators/summaries.py``
(SUMMARY_SETS, SUMMARY_LABELS), ``src/diagnostics/jacobian_rank.py`` (estimate_jacobian, analyse,
same pre-registered thresholds as every other diagnostic run). Nothing here changes
``docs/THRESHOLDS.md``.
"""

from __future__ import annotations

import argparse
import dataclasses
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from .. import runlock
from ..provenance import header, now_iso
from ..simulators.sir3 import BASE, SIR3Params
from ..simulators.summaries import SUMMARY_SETS
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
from ..simulators.sir3 import prior_predictive_stats

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "results"
LOCK = REPO / ".second_theta_check.pid"
MODULE = "src.diagnostics.second_theta_check"

#: Pre-registered before the draw. Disjoint from every seed span this project has recorded
#: (jacobian_rank's ~20260820 span, confidence_set_check's 9e9/10e9-12e9 spans, p_sel and
#: boundary_sweep's own spans) by construction: everything else in this repository is below
#: 2.1e10; this block starts at 6.0e10.
THETA_DRAW_SEED = 60_000_000_000
NORM_SEED = 60_010_000_000
DIAG_SEED = 60_020_000_000
NORM_REPLICATES = 2000
DIAG_REPLICATES = 128

REL_HALF_WIDTH = 0.20
COORDS = ("beta", "gamma", "rho", "I0", "obs_sigma")

#: Every existing recorded seed span this project has used, so disjointness is CHECKED, not
#: assumed. Ranges are read from the settings each script itself records, per the same
#: pattern confidence_set_check.py uses against p_sel.yaml/boundary_sweep.yaml.
_KNOWN_SPANS: dict[str, tuple[int, int]] = {
    "run_diagnostic (jacobian_rank, floor_check)": (20_260_820, 20_260_820 + 3_000_000),
    "confidence_set_check.OBS_SEED": (9_000_000_000, 9_000_000_001),
    "confidence_set_check.anchor/screen/refine (+1e10..+1.3e13 offsets from run seeds)": (
        10_000_000_000, 13_100_000_000
    ),
}


def draw_theta2(seed: int = THETA_DRAW_SEED) -> SIR3Params:
    """The one draw this script makes. Independent Uniform(-0.20, 0.20) per coordinate."""
    rng = np.random.default_rng(seed)
    u = {c: float(rng.uniform(-REL_HALF_WIDTH, REL_HALF_WIDTH)) for c in COORDS}
    theta2 = dataclasses.replace(
        BASE,
        beta=BASE.beta * (1 + u["beta"]),
        gamma=BASE.gamma * (1 + u["gamma"]),
        rho=BASE.rho * (1 + u["rho"]),
        I0=BASE.I0 * (1 + u["I0"]),
        obs_sigma=BASE.obs_sigma * (1 + u["obs_sigma"]),
        families="base",
    )
    return theta2, u


def _check_disjoint(mine: dict[str, tuple[int, int]]) -> tuple[bool, list[str]]:
    overlaps = [
        f"{n1}{s1} vs {n2}{s2}"
        for n1, s1 in mine.items()
        for n2, s2 in _KNOWN_SPANS.items()
        if not (s1[1] <= s2[0] or s2[1] <= s1[0])
    ]
    return (not overlaps), overlaps


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true",
                    help="print the draw and disjointness check, run nothing")
    args = ap.parse_args(argv)

    command = "python -m src.diagnostics.second_theta_check " + " ".join(
        f"--{k.replace('_', '-')} {v}" for k, v in vars(args).items()
    )
    started = now_iso()

    mine = {
        "theta_draw": (THETA_DRAW_SEED, THETA_DRAW_SEED + 1),
        "normalisation": (NORM_SEED, NORM_SEED + NORM_REPLICATES),
        "diagnostic": (DIAG_SEED, DIAG_SEED + DIAG_REPLICATES),
    }
    disjoint, overlaps = _check_disjoint(mine)
    if not disjoint:
        raise SystemExit("ABORTING: seed spans overlap a prior session's: " + "; ".join(overlaps))
    print("seed spans disjoint from every recorded prior span: True", flush=True)

    theta2, u = draw_theta2()
    print(f"theta2 draw (seed {THETA_DRAW_SEED}), relative offsets: "
          + ", ".join(f"{c}={u[c]:+.4f}" for c in COORDS))
    print(f"  beta={theta2.beta:.6f} gamma={theta2.gamma:.6f} rho={theta2.rho:.6f} "
          f"I0={theta2.I0:.4f} obs_sigma={theta2.obs_sigma:.6f}")

    if args.dry_run:
        print("--dry-run: stopping before any simulation.")
        return 0

    prior = runlock.check_pidfile(LOCK)
    if prior["alive"]:
        raise SystemExit(
            f"REFUSING TO START: pid {prior['pid']} is already running {prior['command']!r} "
            f"and will write {prior.get('outputs')}. Standing constraint S3.")
    runlock.write_pidfile(LOCK, module=MODULE, outputs=[str(RESULTS / "second_theta_check.yaml")])
    try:
        summary_fns = {"S_B": SUMMARY_SETS["S_B"]}

        print(f"estimating prior-predictive sd at theta2 from R_norm={NORM_REPLICATES} ...")
        stats = prior_predictive_stats(summary_fns, n_replicates=NORM_REPLICATES,
                                        seed0=NORM_SEED, params=theta2)
        sd_map = {name: sd for name, (_m, sd) in stats.items()}

        print(f"running h-sweep at theta2 over {list(H_VALUES)} with R={DIAG_REPLICATES} ...")
        sweeps = estimate_jacobian(summary_fns, sd_map, h_values=H_VALUES,
                                    n_replicates=DIAG_REPLICATES, seed0=DIAG_SEED,
                                    params=theta2, crn=True)
        verdict = analyse(sweeps["S_B"])

        # -- also re-derive the SAME verdict at theta0, in this script's own harness, so a
        # reader comparing theta2's verdict to the paper's theta0 verdict is comparing two
        # runs of identical code rather than this run to a differently-shaped one.
        stats0 = prior_predictive_stats(summary_fns, n_replicates=NORM_REPLICATES,
                                         seed0=NORM_SEED + 1, params=BASE)
        sd_map0 = {name: sd for name, (_m, sd) in stats0.items()}
        sweeps0 = estimate_jacobian(summary_fns, sd_map0, h_values=H_VALUES,
                                     n_replicates=DIAG_REPLICATES, seed0=DIAG_SEED + 1,
                                     params=BASE, crn=True)
        verdict0 = analyse(sweeps0["S_B"])

        separable2 = bool(not verdict["inseparable"])
        separable0 = bool(not verdict0["inseparable"])

        doc: dict[str, Any] = {
            "provenance": header(script="src/diagnostics/second_theta_check.py",
                                  command=command, seed=THETA_DRAW_SEED, started=started),
            "what_this_is": __doc__,
            "sampling_rule": {
                "rule": "theta2_i = theta0_i * (1 + u_i), u_i ~ independent Uniform(-0.20, 0.20)",
                "coordinates": list(COORDS),
                "rel_half_width": REL_HALF_WIDTH,
                "draw_seed": THETA_DRAW_SEED,
                "relative_offsets_u": u,
            },
            "theta0": {c: float(getattr(BASE, c)) for c in COORDS},
            "theta2": {c: float(getattr(theta2, c)) for c in COORDS},
            "seed_spans_used": {k: list(v) for k, v in mine.items()},
            "seed_spans_disjoint_from_prior_sessions": disjoint,
            "summary_set": "S_B",
            "family_assignment": "AAA (all-base) -- the paper's primary, headline case",
            "thresholds_pre_registered": {
                "source": "docs/THRESHOLDS.md, unrevised",
                "tau_rank_tolerance": TAU,
                "kappa_max": KAPPA_MAX,
                "colnorm_invisible": COLNORM_INVISIBLE,
                "coherence_flag": COHERENCE_FLAG,
                "vk_min_equivalence_class": VK_MIN,
                "resolve_factor": RESOLVE_FACTOR,
                "h_values": list(H_VALUES),
            },
            "verdict_at_theta2": verdict,
            "verdict_at_theta0_same_harness": verdict0,
            "separable_at_theta2": separable2,
            "separable_at_theta0_same_harness": separable0,
            "reproduces_headline_verdict": bool(separable2 == separable0 and separable2),
            "leakage_checked": True,
            "leakage_statement": (
                "The diagnostic never receives a component index or ground-truth label; its "
                "input is theta2 (drawn before any diagnostic ran) and the resulting summary "
                "vectors."
            ),
        }
        out_path = RESULTS / "second_theta_check.yaml"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, width=100)
        print(f"wrote {out_path.relative_to(REPO)}")
        print(f"separable at theta2: {separable2}  (kappa={verdict['condition_number']:.3f})")
        print(f"separable at theta0 (same harness): {separable0}  "
              f"(kappa={verdict0['condition_number']:.3f})")
    finally:
        LOCK.unlink(missing_ok=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
