"""What does the spectrum look like when the component list is longer than three?

WHY THIS EXISTS
---------------
``audit/R2_THREAT_CHECK.md`` §1.3 records the sharpest objection to the rank diagnostic:
Gutenkunst et al. (2007) find sensitivity spectra for models of this class spread over **many
decades with no gap**, which would make "numerical rank at tolerance tau" a statement about
where the analyst put tau.

Session G4's finding 1 measures the recorded spectra and finds them **under about one decade
wide** — so the objection as literally stated does not describe them. That answer is only half
of one, and the missing half is the obvious one: **Gutenkunst et al. study models with dozens
of parameters, and this Jacobian has three columns because the project declared three
components.** A three-column matrix cannot exhibit a decades-wide gapless decay no matter how
badly conditioned the underlying model is. The narrow spectrum may therefore be a property of
`K = 3`, not evidence about the simulator.

This script tests that directly and cheaply. The two distortion family sets are **both**
exactly the identity at ``eta = 0``, are normalised by the **same** prior-predictive standard
deviations, and share the **same** ``eta_scale`` — so their columns live in one space and can
simply be placed side by side. That gives a ``d x 6`` Jacobian over six distortion directions
of the same simulator, at no modelling cost and no new assumption.

**What it can and cannot show.** Six columns is not dozens, and this is one simulator. If the
six-column spectrum is still narrow, that is weak evidence; if it is wide and smooth, that is
strong evidence that the three-column narrowness was an artefact of ``K``, and that the rank
verdict's tolerance-insensitivity does not survive a longer component list. **The asymmetry is
deliberate: the test is set up so that the informative outcome is the one against the
project.**

``S_A`` has ``d = 4``, so a six-column Jacobian is structurally rank-deficient there and two of
its singular values are exactly zero for reasons that have nothing to do with the question.
``S_B`` (``d = 10``) is the informative case; ``S_A`` is reported anyway, with the structural
zeros visible rather than dropped.

    python -m src.diagnostics.wide_spectrum_check
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from ..provenance import header, now_iso
from ..simulators.sir3 import ETA_SCALE, K, prior_predictive_stats, simulate, with_params
from ..simulators.summaries import SUMMARY_LABELS, SUMMARY_SETS
from .jacobian_rank import KAPPA_MAX, TAU

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results" / "robustness"

SEED = 20260820
R = 128
R_NORM = 2000
REP_H = 1e-4  # the representative h recorded in results/jacobian_rank.*.yaml

COLUMN_LABELS = [
    "base:transmission (saturating incidence)",
    "base:progression (mean-centred hazard drift)",
    "base:observation (reporting-fraction multiplier)",
    "adv:transmission (constant beta multiplier)",
    "adv:progression (constant gamma multiplier)",
    "adv:observation (reporting trend)",
]


def _columns(family_set: str, sd_map: dict[str, np.ndarray]) -> dict[str, list[np.ndarray]]:
    params = with_params(families=family_set)
    step = REP_H * ETA_SCALE
    cols: dict[str, list[np.ndarray]] = {n: [] for n in SUMMARY_SETS}
    for k in range(K):
        acc: dict[str, list] = {n: [] for n in SUMMARY_SETS}
        for r in range(R):
            ep, em = np.zeros(K), np.zeros(K)
            ep[k], em[k] = step, -step
            op = simulate(ep, seed=SEED + r, params=params)
            om = simulate(em, seed=SEED + r, params=params)
            for n, fn in SUMMARY_SETS.items():
                acc[n].append((fn(op) - fn(om)) / (2.0 * REP_H))
        for n in SUMMARY_SETS:
            cols[n].append(np.mean(np.asarray(acc[n]), axis=0) / sd_map[n])
        print(f"  {family_set} column {k} done")
    return cols


def _spectrum(J: np.ndarray) -> dict[str, Any]:
    n_cols = J.shape[1]
    _u, s_raw, _vt = np.linalg.svd(J, full_matrices=True)
    s = np.zeros(n_cols)
    s[: len(s_raw)] = s_raw
    pos = [x for x in s if x > 0]
    ratios = [float(x / s[0]) for x in s]
    adj = [float(s[i] / s[i + 1]) if s[i + 1] > 0 else math.inf for i in range(len(s) - 1)]
    rank = int(sum(1 for x in s if x >= TAU * s[0]))
    kappa = float(s[0] / s[-1]) if s[-1] > 0 else math.inf
    # Spread over the strictly positive part: a structural zero (d < n_cols) is not evidence
    # about decay, it is evidence about dimension, and mixing them would flatter the argument.
    spread = float(math.log10(pos[0] / pos[-1])) if len(pos) > 1 else None
    return {
        "n_columns": int(n_cols),
        "singular_values": [float(x) for x in s],
        "n_structurally_zero": int(n_cols - len(pos)),
        "sigma_i_over_sigma_1": ratios,
        "adjacent_ratios": adj,
        "spread_decades_over_positive_singular_values": spread,
        "largest_adjacent_ratio": float(max(a for a in adj if math.isfinite(a))) if adj else None,
        "largest_adjacent_ratio_falls_after_index": (
            int(np.argmax([a if math.isfinite(a) else -1 for a in adj]) + 1) if adj else None
        ),
        "rank_at_tau": rank,
        "condition_number": kappa,
        "full_column_rank": bool(rank == n_cols),
        "verdict_at_pre_registered_thresholds": (
            "separable" if (rank == n_cols and kappa <= KAPPA_MAX) else "INSEPARABLE"
        ),
    }


def main() -> int:
    started = now_iso()
    print(f"prior-predictive sd (R_norm={R_NORM}) ...")
    stats = prior_predictive_stats(SUMMARY_SETS, n_replicates=R_NORM, seed0=SEED + 900_000)
    sd_map = {n: sd for n, (_m, sd) in stats.items()}

    print("base columns ...")
    base_cols = _columns("base", sd_map)
    print("adversarial columns ...")
    adv_cols = _columns("adversarial", sd_map)

    out_sets: dict[str, Any] = {}
    for n in SUMMARY_SETS:
        J3b = np.column_stack(base_cols[n])
        J3a = np.column_stack(adv_cols[n])
        J6 = np.column_stack(base_cols[n] + adv_cols[n])
        out_sets[n] = {
            "d": int(J6.shape[0]),
            "coordinate_labels": list(SUMMARY_LABELS[n]),
            "three_columns_base": _spectrum(J3b),
            "three_columns_adversarial": _spectrum(J3a),
            "six_columns_both_family_sets": _spectrum(J6),
        }
        six = out_sets[n]["six_columns_both_family_sets"]
        print(f"\n{n} (d={J6.shape[0]}): 6-column spectrum "
              f"{['%.4g' % x for x in six['singular_values']]}")
        print(f"  spread over positive sigma: {six['spread_decades_over_positive_singular_values']}")
        print(f"  rank at tau {six['rank_at_tau']}/6, kappa {six['condition_number']:.4g} "
              f"-> {six['verdict_at_pre_registered_thresholds']}")

    doc = {
        "provenance": header(script="src/diagnostics/wide_spectrum_check.py",
                             command="python -m src.diagnostics.wide_spectrum_check",
                             seed=SEED, started=started),
        "what_this_is": (
            "Session G4 adversarial pass, finding 1, second half. Places the base and "
            "adversarial distortion columns side by side to see what the spectrum does when the "
            "component list is longer than three. Does not modify anything in results/. See "
            "audit/G3_ADVERSARIAL_REVIEW.md."
        ),
        "why_the_columns_are_comparable": (
            "Both family sets are exactly the identity at eta = 0, so both Jacobians are "
            "linearisations about the SAME point; both are divided by the SAME prior-predictive "
            "standard deviations; and both use the same common eta_scale, so one normalised "
            "unit means the same fractional deformation in every column."
        ),
        "what_this_cannot_show": (
            "Six columns is not the dozens of parameters the sloppy-models literature studies, "
            "and this is one simulator. A still-narrow six-column spectrum is weak evidence. A "
            "wide, smoothly decaying one is strong evidence that the three-column narrowness was "
            "a property of K = 3 rather than of the simulator."
        ),
        "settings": {"seed": SEED, "R": R, "R_norm": R_NORM, "representative_h": REP_H,
                     "eta_scale": ETA_SCALE, "tau": TAU, "kappa_max": KAPPA_MAX},
        "column_labels_for_the_six_column_jacobian": COLUMN_LABELS,
        "summary_sets": out_sets,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "wide_spectrum_check.yaml"
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, width=100)
    print(f"\nwrote {path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
