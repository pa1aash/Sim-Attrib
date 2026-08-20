"""Re-apply the rank verdict under alternative tolerances, from the recorded results files.

WHY THIS EXISTS
---------------
``audit/R2_THREAT_CHECK.md`` §1.3 records the sharpest objection found against the rank
diagnostic, and it is not a novelty objection. Gutenkunst et al. (2007) report that
sensitivity spectra for models of this class are spread over many decades **with no gap**; if
that holds here, then "numerical rank at tolerance tau" reports where the analyst put tau
rather than a structural property of the model.

That is an empirical question about the numbers G3 produced, and this script answers it
**from those numbers**, without re-simulating anything. It reads ``results/jacobian_rank.*.yaml``
and:

  1. tabulates the full singular-value spectrum and every adjacent ratio, so a reader can see
     whether a gap exists and where;
  2. re-applies the pre-registered decision rule at a range of alternative tolerances;
  3. computes the EXACT tolerance at which each summary set's verdict flips, and expresses it
     as a multiple of the pre-registered value -- which is a sharper statement than a table of
     sampled thresholds, because it does not depend on which alternatives happened to be tried.

THE RULE IS NOT RE-INVENTED HERE, AND THE SCRIPT CHECKS THAT
------------------------------------------------------------
The decision rule below is transcribed from the rule each results file states in its own
``numerical_rank.rule`` field, and from ``docs/THRESHOLDS.md`` §1.3. Transcription can be
wrong, so the script **asserts that its own re-application at the pre-registered thresholds
reproduces the verdict recorded in the file**. If the transcription were wrong, that assertion
fails and no table is written. A re-analysis that cannot reproduce the original result at the
original settings has not earned the right to report what happens at other settings.

    python -m src.diagnostics.threshold_sensitivity
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import yaml

from ..provenance import header, now_iso
from .jacobian_rank import KAPPA_MAX, TAU

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "results"
OUT = RESULTS / "robustness"

#: Alternative tolerances, spanning the range the G4 brief names -- half, double, and an order
#: of magnitude in each direction around the pre-registered value. Stated as multipliers of the
#: pre-registered tau so the table cannot silently drift from it.
TAU_MULTIPLIERS: tuple[float, ...] = (0.1, 0.5, 1.0, 2.0, 10.0)


def _verdict(sv: list[float], resolved: list[bool], tau: float, kappa_max: float) -> dict[str, Any]:
    """The pre-registered rule, transcribed. See the module docstring for why it is checked."""
    kk = len(sv)
    sv1 = sv[0]
    above = [s >= tau * sv1 for s in sv]
    rank_certain = sum(1 for i, a in enumerate(above) if a and resolved[i])
    rank_possible = sum(1 for i, a in enumerate(above) if a or not resolved[i])
    determined = rank_certain == rank_possible
    kappa = (sv1 / sv[-1]) if sv[-1] > 0 else math.inf
    full_rank = determined and rank_certain == kk
    inseparable = (not determined) or (rank_certain < kk) or (kappa > kappa_max)
    return {
        "tau": tau,
        "kappa_max": kappa_max,
        "rank_certain": rank_certain,
        "full_column_rank": bool(full_rank),
        "condition_number": kappa,
        "kappa_within_ceiling": bool(kappa <= kappa_max),
        "verdict": "INSEPARABLE" if inseparable else "separable",
    }


def main() -> int:
    started = now_iso()
    doc: dict[str, Any] = {
        "provenance": header(script="src/diagnostics/threshold_sensitivity.py",
                             command="python -m src.diagnostics.threshold_sensitivity",
                             seed=0, started=started),
        "what_this_is": (
            "RE-ANALYSIS of results/jacobian_rank.*.yaml under alternative rank tolerances. No "
            "simulation was run. Nothing in results/ is modified. Written for session G4's "
            "adversarial pass; see audit/G3_ADVERSARIAL_REVIEW.md finding 1."
        ),
        "seed_field_is_zero_because": (
            "no random number was drawn. The seed of the run being re-analysed is recorded in "
            "the file this reads, not here."
        ),
        "source_files": [],
        "pre_registered": {"tau": TAU, "kappa_max": KAPPA_MAX,
                           "note": "docs/THRESHOLDS.md §1.2 and §1.3, unrevised"},
        "summary_sets": {},
    }

    for name in ("S_A", "S_B", "S_C"):
        path = RESULTS / f"jacobian_rank.{name}.yaml"
        rec = yaml.safe_load(path.read_text(encoding="utf-8"))
        doc["source_files"].append(str(path.relative_to(REPO)))
        r = rec["results"]
        sv = [float(x) for x in r["singular_values_at_representative_h"]]
        resolved = [bool(x) for x in r["resolved"]]

        # --- the self-check: reproduce the recorded verdict before reporting any other -----
        check = _verdict(sv, resolved, TAU, KAPPA_MAX)
        recorded = "INSEPARABLE" if r["inseparable"] else "separable"
        if check["verdict"] != recorded:
            raise AssertionError(
                f"{name}: re-applied rule gives {check['verdict']!r} at the pre-registered "
                f"thresholds but the results file records {recorded!r}. The transcription of "
                f"the rule is wrong; no sensitivity table is trustworthy until it is fixed."
            )
        if abs(check["condition_number"] - float(r["condition_number"])) > 1e-9 * max(
            1.0, abs(float(r["condition_number"]))
        ) and math.isfinite(float(r["condition_number"])):
            raise AssertionError(f"{name}: recomputed kappa disagrees with the recorded value")

        ratios = [s / sv[0] for s in sv]
        gaps = [(sv[i] / sv[i + 1]) if sv[i + 1] > 0 else math.inf for i in range(len(sv) - 1)]
        finite_gaps = [g for g in gaps if math.isfinite(g)]
        largest_gap_after = (gaps.index(max(finite_gaps)) + 1) if finite_gaps else None

        # tau* is the tolerance at which the smallest singular value stops counting toward the
        # rank. Because the rule is sigma_K >= tau*sigma_1, that is exactly sigma_K/sigma_1 --
        # and because kappa = sigma_1/sigma_K, it is also exactly 1/kappa. The two
        # pre-registered criteria are therefore the SAME criterion; see §1.3 of THRESHOLDS.
        tau_star = ratios[-1]

        doc["summary_sets"][name] = {
            "d": int(r["dimensions"]["d"]),
            "K": int(r["dimensions"]["K"]),
            "representative_h": float(r["plateau"]["representative_h"]),
            "singular_values": sv,
            "sigma_i_over_sigma_1": ratios,
            "adjacent_ratios_sigma_i_over_sigma_i_plus_1": gaps,
            "largest_adjacent_ratio_falls_after_index": largest_gap_after,
            "spectrum_spread_decades_log10_sigma1_over_sigmaK": (
                math.log10(sv[0] / sv[-1]) if sv[-1] > 0 else None
            ),
            "recorded_verdict": recorded,
            "flip_point": {
                "tau_star": tau_star,
                "tau_star_as_multiple_of_pre_registered_tau": (tau_star / TAU),
                "kappa_star": check["condition_number"],
                "kappa_star_as_fraction_of_pre_registered_kappa_max": (
                    check["condition_number"] / KAPPA_MAX
                    if math.isfinite(check["condition_number"]) else None
                ),
                "meaning": (
                    "the verdict flips to INSEPARABLE for any tau > tau_star, equivalently for "
                    "any kappa_max < kappa_star. Both are the same statement: sigma_K/sigma_1 = "
                    "1/kappa exactly, so tau and 1/kappa_max are one threshold with two names."
                ),
            },
            "sensitivity": [
                _verdict(sv, resolved, TAU * m, 1.0 / (TAU * m))
                for m in TAU_MULTIPLIERS
            ],
            "sensitivity_note": (
                "Each row moves tau and kappa_max TOGETHER, holding kappa_max = 1/tau, because "
                "docs/THRESHOLDS.md §1.2 derives them from one another (tau = 1/kappa). Moving "
                "one alone would test a threshold pair the project never registered."
            ),
        }

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "threshold_sensitivity.yaml"
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, width=100)
    print(f"wrote {path.relative_to(REPO)}")

    for name, blk in doc["summary_sets"].items():
        print(f"\n{name}: sigma = {['%.4g' % s for s in blk['singular_values']]}")
        print(f"  sigma_i/sigma_1        = {['%.4g' % s for s in blk['sigma_i_over_sigma_1']]}")
        print(f"  adjacent ratios        = {['%.4g' % s for s in blk['adjacent_ratios_sigma_i_over_sigma_i_plus_1']]}")
        print(f"  spread (decades)       = {blk['spectrum_spread_decades_log10_sigma1_over_sigmaK']}")
        print(f"  flips at tau* = {blk['flip_point']['tau_star']:.4g} "
              f"= {blk['flip_point']['tau_star_as_multiple_of_pre_registered_tau']:.3g}x pre-registered tau")
        for row in blk["sensitivity"]:
            print(f"    tau={row['tau']:<8.4g} kappa_max={row['kappa_max']:<8.4g} "
                  f"rank={row['rank_certain']} -> {row['verdict']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
