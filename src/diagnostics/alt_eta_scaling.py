"""Is separability an artifact of the flat 10% ETA_SCALE convention? -- session G11, T2-3.

WHY THIS EXISTS
---------------
Every separability verdict in this project is measured in one unit: each distortion
``eta_k`` normalised by a single, common ``ETA_SCALE = 0.1`` (a flat 10% relative
deformation, ``docs/THRESHOLDS.md`` Section 0). An external adversarial review of the drafted
paper asked the natural question a flat, arbitrary unit choice invites: do the separability
verdicts survive under a *different* per-column scaling, or are they a property of this
particular convention?

THE ALTERNATIVE SCALING, AND WHY IT IS NOT ANOTHER ARBITRARY CHOICE
---------------------------------------------------------------------
Rather than invent a second flat convention (which would only replace one arbitrary choice
with another), this script uses a scaling with an independent source: the per-coordinate
relative standard errors ``results/confidence_set_mmc.yaml`` reports for the simulator's
native parameters (beta, gamma, rho), from the session G11 maximum-likelihood fit to one
realised dataset. Each distortion family targets one native parameter most directly
(transmission -> beta, progression -> gamma, observation -> rho), so this substitutes
"one native-parameter standard error" for "one flat 10%" as the unit each eta_k is measured
in -- a scaling motivated by the data rather than chosen for convenience, and one this project
had not used for this purpose before this session.

WHAT THIS SCRIPT DOES, AND WHAT IT DOES NOT DO
-------------------------------------------------
It re-derives condition numbers from the Jacobian columns ``results/robustness/k6_spectrum.yaml``
already stores at every swept step size -- **no new simulator draws**. Rescaling column j of an
already-estimated Jacobian by a constant factor is exact linear algebra, not a new measurement;
the representative step size for each triple is identified the same way
``src/diagnostics/p_sel.py::load_jacobian`` does, by finding the h whose spectrum best
reproduces the recorded condition number.

It does not re-run the diagnostic's pipeline, does not change ETA_SCALE anywhere in
``src/simulators/sir3.py`` (which remains the paper's primary, pre-registered convention), and
does not claim the alternative scaling is *more correct* -- only that it is a second,
independently-motivated scaling under which the separability verdicts can be checked.

    python -m src.diagnostics.alt_eta_scaling
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from ..provenance import header, now_iso
from ..simulators.sir3 import COMPONENTS
from .jacobian_rank import KAPPA_MAX, TAU
from .k6_spectrum import triple_columns

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results" / "robustness" / "alt_eta_scaling.yaml"

ETA_SCALE = 0.1  # docs/THRESHOLDS.md Section 0 -- the primary, pre-registered convention

#: Relative standard error of the MLE for each native parameter a distortion family targets,
#: from results/confidence_set_mmc.yaml's fisher_information.standard_errors and
#: mle_fit.theta_hat (session G11, commit a91131a). Recorded here as literals rather than
#: re-read at runtime, because this script's job is to show what a THIRD PARTY'S already-
#: published number implies for the diagnostic, not to re-fit the model.
ALT_RELATIVE_SCALE: dict[str, float] = {
    "transmission": 0.0032369499298674615 / 0.35509229586932795,   # beta:   SE / theta_hat
    "progression": 0.004000716595537015 / 0.14754451276515815,     # gamma:  SE / theta_hat
    "observation": 0.009524492210426639 / 0.404992777556476,       # rho:    SE / theta_hat
}


def _find_representative_h(cols: dict, keys: list[str], hs: list[float],
                           recorded_kappa: float) -> int:
    best_rel, best_hi = float("inf"), None
    for hi in range(len(hs)):
        J = np.column_stack([np.asarray(cols[k]["columns_by_h"][hi], dtype=float) for k in keys])
        sv = np.linalg.svd(J, compute_uv=False)
        kappa = float(sv[0] / sv[-1])
        rel = abs(kappa - recorded_kappa) / recorded_kappa
        if rel < best_rel:
            best_rel, best_hi = rel, hi
    assert best_hi is not None
    return best_hi


def _kappa_rank(J: np.ndarray, tau: float) -> tuple[float, int]:
    sv = np.linalg.svd(J, compute_uv=False)
    kappa = float(sv[0] / sv[-1]) if sv[-1] > 0 else float("inf")
    rank = int(np.sum(sv >= tau * sv[0]))
    return kappa, rank


def main(argv: list[str] | None = None) -> int:
    started = now_iso()
    command = "python -m src.diagnostics.alt_eta_scaling"

    src_path = REPO / "results" / "robustness" / "k6_spectrum.yaml"
    k6 = yaml.safe_load(src_path.read_text(encoding="utf-8"))
    block = k6["summary_sets"]["S_B"]
    cols = block["raw_columns_normalised"]
    hs = cols["base:transmission"]["h_values"]

    triples: dict[str, Any] = {}
    for code in ("AAA", "BBB"):
        triple = triple_columns(code)
        keys = [f"{fs}:{COMPONENTS[k]}" for fs, k in triple]
        recorded_kappa = float(block["mixed_triples"][code]["condition_number"])
        hi = _find_representative_h(cols, keys, hs, recorded_kappa)
        J = np.column_stack([np.asarray(cols[k]["columns_by_h"][hi], dtype=float) for k in keys])
        kappa_flat, rank_flat = _kappa_rank(J, TAU)
        factors = np.array([ALT_RELATIVE_SCALE[COMPONENTS[k]] / ETA_SCALE for _fs, k in triple])
        J_alt = J * factors[np.newaxis, :]
        kappa_alt, rank_alt = _kappa_rank(J_alt, TAU)
        triples[code] = {
            "columns": keys,
            "representative_h": float(hs[hi]),
            "flat_10pct": {"kappa": kappa_flat, "rank_at_tau": rank_flat,
                          "separable": bool(rank_flat == 3 and kappa_flat <= KAPPA_MAX)},
            "mle_se_based": {"per_column_relative_scale": {COMPONENTS[k]: float(factors[i])
                                                            for i, (_fs, k) in enumerate(triple)},
                             "kappa": kappa_alt, "rank_at_tau": rank_alt,
                             "separable": bool(rank_alt == 3 and kappa_alt <= KAPPA_MAX)},
        }

    six_keys = [f"{fs}:{COMPONENTS[k]}" for fs in ("base", "adversarial") for k in range(3)]
    recorded_kappa_6 = float(block["six_columns"]["condition_number"])
    hi6 = _find_representative_h(cols, six_keys, hs, recorded_kappa_6)
    J6 = np.column_stack([np.asarray(cols[k]["columns_by_h"][hi6], dtype=float) for k in six_keys])
    kappa6_flat, rank6_flat = _kappa_rank(J6, TAU)
    factors6 = np.array([ALT_RELATIVE_SCALE[k.split(":")[1]] / ETA_SCALE for k in six_keys])
    J6_alt = J6 * factors6[np.newaxis, :]
    kappa6_alt, rank6_alt = _kappa_rank(J6_alt, TAU)
    six_column = {
        "columns": six_keys,
        "representative_h": float(hs[hi6]),
        "flat_10pct": {"kappa": kappa6_flat, "rank_at_tau": rank6_flat,
                      "separable": bool(rank6_flat == 6 and kappa6_flat <= KAPPA_MAX)},
        "mle_se_based": {"per_column_relative_scale": {k: float(f) for k, f in
                                                       zip(six_keys, factors6)},
                         "kappa": kappa6_alt, "rank_at_tau": rank6_alt,
                         "separable": bool(rank6_alt == 6 and kappa6_alt <= KAPPA_MAX)},
    }

    doc = {
        "provenance": header(script="src/diagnostics/alt_eta_scaling.py", command=command,
                             seed=0, started=started),
        "what_this_is":
            "Session G11, T2-3. Re-derives condition number and rank under a second, "
            "data-motivated per-column eta scaling (relative standard error of the "
            "corresponding native parameter's MLE, from results/confidence_set_mmc.yaml) "
            "instead of the flat 10% ETA_SCALE convention, to check the separability "
            "verdicts are not an artifact of one arbitrary unit choice. No new simulator "
            "draws: derived from the Jacobian columns results/robustness/k6_spectrum.yaml "
            "already stores at every swept step size.",
        "eta_scale_primary": ETA_SCALE,
        "alt_relative_scale_source": "results/confidence_set_mmc.yaml fisher_information."
                                     "standard_errors / mle_fit.theta_hat, commit a91131a",
        "tau": TAU, "kappa_max": KAPPA_MAX,
        "eight_assignment_triples": triples,
        "six_column": six_column,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(yaml.safe_dump(doc, sort_keys=False, width=100), encoding="utf-8")
    print(f"wrote {OUT}")
    for code, t in triples.items():
        print(f"  {code}: flat kappa={t['flat_10pct']['kappa']:.3f} -> "
              f"alt kappa={t['mle_se_based']['kappa']:.3f}, "
              f"separable flat={t['flat_10pct']['separable']} "
              f"alt={t['mle_se_based']['separable']}")
    print(f"  six-column: flat kappa={six_column['flat_10pct']['kappa']:.3f} rank="
          f"{six_column['flat_10pct']['rank_at_tau']}/6 -> alt kappa="
          f"{six_column['mle_se_based']['kappa']:.3f} rank={six_column['mle_se_based']['rank_at_tau']}/6")
    return 0


if __name__ == "__main__":
    sys.exit(main())
