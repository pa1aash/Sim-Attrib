"""Generate session G4's tables from the robustness results files.

Same contract as ``report_tables.py``: no number is hand-typed into a markdown file (S11,
``PROVENANCE.md``). ``audit/G3_ADVERSARIAL_REVIEW.md`` quotes this file verbatim.

    python -m src.diagnostics.report_robustness
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "results"
ROB = RESULTS / "robustness"
SETS = ("S_A", "S_B", "S_C")
COMPONENTS = ("transmission", "progression", "observation")


def _fmt(x: Any, sig: int = 4) -> str:
    if x is None:
        return "—"
    if isinstance(x, bool):
        return "yes" if x else "no"
    if not isinstance(x, (int, float)):
        return str(x)
    if x != x:
        return "nan"
    if x == float("inf"):
        return "inf"
    return f"{x:.{sig}g}"


def _load(p: Path) -> dict | None:
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else None


def build() -> str:
    L: list[str] = []
    L.append("# Robustness tables — GENERATED, not typed")
    L.append("")
    L.append("Produced by `src/diagnostics/report_robustness.py` from `results/robustness/*.yaml`.")
    L.append("Do not edit by hand. `audit/G3_ADVERSARIAL_REVIEW.md` quotes this file verbatim.")
    L.append("")
    L.append("**Nothing here replaces `results/jacobian_rank.*.yaml`.** Those files record what")
    L.append("session G3 ran and are untouched.")
    L.append("")

    # ---------------------------------------------------------------- 1. thresholds -----
    ts = _load(ROB / "threshold_sensitivity.yaml")
    if ts:
        L.append("---")
        L.append("")
        L.append("## 1. The spectrum, and how far the tolerance can move before the verdict does")
        L.append("")
        L.append(f"Re-analysis of the recorded singular values. No simulation. "
                 f"Pre-registered `tau = {_fmt(ts['pre_registered']['tau'])}`, "
                 f"`kappa_max = {_fmt(ts['pre_registered']['kappa_max'])}`.")
        L.append("")
        L.append("| Summary set | singular values | sigma_i/sigma_1 | adjacent ratios | spread (decades) | largest gap after |")
        L.append("|---|---|---|---|---|---|")
        for n in SETS:
            b = ts["summary_sets"][n]
            L.append(
                f"| {n} | {', '.join(_fmt(x) for x in b['singular_values'])} "
                f"| {', '.join(_fmt(x, 3) for x in b['sigma_i_over_sigma_1'])} "
                f"| {', '.join(_fmt(x, 3) for x in b['adjacent_ratios_sigma_i_over_sigma_i_plus_1'])} "
                f"| {_fmt(b['spectrum_spread_decades_log10_sigma1_over_sigmaK'], 3)} "
                f"| sigma_{b['largest_adjacent_ratio_falls_after_index']} |")
        L.append("")
        L.append("**Spread** is `log10(sigma_1/sigma_K)`. Gutenkunst et al. report spectra spread over")
        L.append("*many decades without a gap*; the number above is the like-for-like quantity.")
        L.append("")
        L.append("### 1.1 Flip points — the exact tolerance at which each verdict changes")
        L.append("")
        L.append("| Summary set | recorded verdict | tau* | as a multiple of pre-registered tau | kappa* | as a fraction of kappa_max |")
        L.append("|---|---|---|---|---|---|")
        for n in SETS:
            b = ts["summary_sets"][n]
            f = b["flip_point"]
            L.append(
                f"| {n} | {b['recorded_verdict']} | {_fmt(f['tau_star'])} "
                f"| {_fmt(f['tau_star_as_multiple_of_pre_registered_tau'], 3)}x "
                f"| {_fmt(f['kappa_star'])} "
                f"| {_fmt(f['kappa_star_as_fraction_of_pre_registered_kappa_max'], 3)} |")
        L.append("")
        L.append("`tau* = sigma_K/sigma_1 = 1/kappa` exactly, so the two pre-registered criteria are")
        L.append("one threshold under two names (`docs/THRESHOLDS.md` §1.3 says so).")
        L.append("")
        L.append("### 1.2 The verdict at alternative tolerances")
        L.append("")
        head = "| tau | kappa_max | " + " | ".join(f"{n} rank" for n in SETS) + " | " + \
               " | ".join(f"{n} verdict" for n in SETS) + " |"
        L.append(head)
        L.append("|---" * (2 + 2 * len(SETS)) + "|")
        n_rows = len(ts["summary_sets"]["S_A"]["sensitivity"])
        for i in range(n_rows):
            rows = [ts["summary_sets"][n]["sensitivity"][i] for n in SETS]
            L.append(f"| {_fmt(rows[0]['tau'])} | {_fmt(rows[0]['kappa_max'])} | "
                     + " | ".join(str(r["rank_certain"]) for r in rows) + " | "
                     + " | ".join(r["verdict"] for r in rows) + " |")
        L.append("")

    # ------------------------------------------------- 2. adversarial + seed re-runs ----
    labels = [("adversarial", "adversarial family set"),
              ("seed_20260821", "base families, seed 20260821"),
              ("seed_20260822", "base families, seed 20260822")]
    present = [(lab, desc) for lab, desc in labels
               if (ROB / f"jacobian_rank.{lab}.S_A.yaml").exists()]
    if present:
        L.append("---")
        L.append("")
        L.append("## 2. Re-runs: a different family set, and different seeds")
        L.append("")
        L.append("Same diagnostic code, same pre-registered thresholds, same `h` sweep, same")
        L.append("normalisation rule, same replicate count. Only the family set and the seed differ.")
        L.append("")
        L.append("| Run | Summary set | d | rank at tau | kappa | plateau found | verdict |")
        L.append("|---|---|---|---|---|---|---|")
        base = {n: _load(RESULTS / f"jacobian_rank.{n}.yaml") for n in SETS}
        for n in SETS:
            r = base[n]["results"]
            L.append(f"| **G3 as recorded** | {n} | {r['dimensions']['d']} "
                     f"| {r['numerical_rank']['rank_certain']} | {_fmt(r['condition_number'])} "
                     f"| {_fmt(r['plateau']['found'])} "
                     f"| {'INSEPARABLE' if r['inseparable'] else 'separable'} |")
        for lab, desc in present:
            for n in SETS:
                d = _load(ROB / f"jacobian_rank.{lab}.{n}.yaml")
                r = d["results"]
                L.append(f"| {desc} | {n} | {r['dimensions']['d']} "
                         f"| {r['numerical_rank']['rank_certain']} | {_fmt(r['condition_number'])} "
                         f"| {_fmt(r['plateau']['found'])} "
                         f"| {'INSEPARABLE' if r['inseparable'] else 'separable'} |")
        L.append("")
        L.append("### 2.1 Singular values and pairwise coherence, per run")
        L.append("")
        L.append("| Run | Summary set | singular values | sigma_3/sigma_1 | "
                 "mu(tra,pro) | mu(tra,obs) | mu(pro,obs) | flagged |")
        L.append("|---|---|---|---|---|---|---|---|")

        def _row(tag: str, n: str, doc: dict) -> str:
            r = doc["results"]
            sv = r["singular_values_at_representative_h"]
            coh = r["pairwise_coherence"]
            flagged = ", ".join(f"{COMPONENTS[i]}–{COMPONENTS[j]}"
                                for i, j in r["coherence_flagged_pairs"]) or "none"
            ratio = sv[-1] / sv[0] if sv[0] else float("nan")
            return (f"| {tag} | {n} | {', '.join(_fmt(x) for x in sv)} | {_fmt(ratio, 3)} "
                    f"| {_fmt(coh[0][1], 3)} | {_fmt(coh[0][2], 3)} | {_fmt(coh[1][2], 3)} "
                    f"| {flagged} |")

        for n in SETS:
            L.append(_row("**G3 as recorded**", n, base[n]))
        for lab, desc in present:
            for n in SETS:
                L.append(_row(desc, n, _load(ROB / f"jacobian_rank.{lab}.{n}.yaml")))
        L.append("")
        L.append("### 2.2 Column norms — is any component invisible?")
        L.append("")
        L.append("| Run | Summary set | " + " | ".join(f"‖J·{c}‖" for c in COMPONENTS)
                 + " | invisible (<0.1) |")
        L.append("|---|---|---|---|---|---|")

        def _cn(tag: str, n: str, doc: dict) -> str:
            r = doc["results"]
            inv = ", ".join(COMPONENTS[i] for i in r["invisible_components"]) or "none"
            return (f"| {tag} | {n} | " + " | ".join(_fmt(x) for x in r["column_norms"])
                    + f" | {inv} |")

        for n in SETS:
            L.append(_cn("**G3 as recorded**", n, base[n]))
        for lab, desc in present:
            for n in SETS:
                L.append(_cn(desc, n, _load(ROB / f"jacobian_rank.{lab}.{n}.yaml")))
        L.append("")

        adv = ROB / "jacobian_rank.adversarial.S_A.yaml"
        if adv.exists():
            L.append("### 2.3 Where the adversarial run's near-null direction points")
            L.append("")
            any_nn = False
            for n in SETS:
                d = _load(ROB / f"jacobian_rank.adversarial.{n}.yaml")
                for nn in d["results"]["near_null_directions"]:
                    any_nn = True
                    members = ", ".join(COMPONENTS[k] for k in nn["equivalence_class_members"]) or "none"
                    border = ", ".join(COMPONENTS[k] for k in nn["borderline_members"]) or "none"
                    v = ", ".join(_fmt(x, 4) for x in nn["right_singular_vector_at_representative_h"])
                    L.append(f"**{n}**, direction {nn['index']} — `sigma = {_fmt(nn['singular_value'])}`, "
                             f"`sigma/sigma_1 = {_fmt(nn['sigma_ratio_to_sigma1'])}`, "
                             f"**{nn['degeneracy_kind']}** degeneracy")
                    L.append("")
                    L.append(f"- right singular vector: ({v}) over ({', '.join(COMPONENTS)})")
                    L.append(f"- equivalence-class members (|v_k| >= 0.3 across the plateau): {members}")
                    L.append(f"- borderline: {border}")
                    L.append("")
            if not any_nn:
                L.append("No near-null direction was reported under the adversarial family set.")
                L.append("")

    # -------------------------------------------------------- 3. summary smoothness ----
    sm = _load(ROB / "summary_smoothness_check.yaml")
    if sm:
        L.append("---")
        L.append("")
        L.append("## 3. Does the argmax inside S_A's peak statistics contaminate its Jacobian?")
        L.append("")
        L.append("### 3.1 Fine eta sweep at one fixed seed — what happens at a real argmax switch")
        L.append("")
        L.append("| Component | eta range | points | switches found | largest step in peak_time | largest step in peak_height | median step, peak_time | median step, peak_height |")
        L.append("|---|---|---|---|---|---|---|---|")
        for comp, b in sm["fine_eta_sweeps"].items():
            L.append(f"| {comp} | [{_fmt(b['eta_range'][0], 3)}, {_fmt(b['eta_range'][1], 3)}] "
                     f"| {b['n_points'] - b['n_points_outside_the_family_domain_and_skipped']} "
                     f"| {b['n_argmax_switches']} "
                     f"| {_fmt(b['largest_step_in_peak_time'])} | {_fmt(b['largest_step_in_peak_height'])} "
                     f"| {_fmt(b['median_step_in_peak_time'])} | {_fmt(b['median_step_in_peak_height'])} |")
        L.append("")
        L.append("Steps are between adjacent eta grid points, in native summary units. A step much")
        L.append("larger than the median is the signature of a discontinuity being crossed.")
        L.append("")
        L.append("### 3.2 Census at the estimator's own settings — how often is a switch actually straddled?")
        L.append("")
        L.append("| h | component | replicates | straddling an argmax switch | boundary fallbacks | peak_height difference quotient: mean | sd | max abs |")
        L.append("|---|---|---|---|---|---|---|---|")
        for row in sm["argmax_switch_census"]:
            L.append(f"| {_fmt(row['h'])} | {COMPONENTS[row['component_k']]} | {row['n_replicates']} "
                     f"| {row['n_replicates_straddling_an_argmax_switch']} "
                     f"| {row['n_replicates_with_a_boundary_argmax_fallback']} "
                     f"| {_fmt(row['peak_height_difference_quotient_mean'])} "
                     f"| {_fmt(row['peak_height_difference_quotient_sd'])} "
                     f"| {_fmt(row['peak_height_difference_quotient_max_abs'])} |")
        L.append("")
        L.append("### 3.3 Leave-one-coordinate-out — does S_A's verdict rest on the peak statistics?")
        L.append("")
        L.append("| S_A computed with | singular values | rank at tau | kappa | verdict |")
        L.append("|---|---|---|---|---|")
        for key, v in sm["leave_one_coordinate_out_S_A"].items():
            L.append(f"| {key.replace('_', ' ')} | {', '.join(_fmt(x) for x in v['singular_values'])} "
                     f"| {v['rank_at_tau']} | {_fmt(v['condition_number'])} | {v['verdict']} |")
        L.append("")

    # ------------------------------------------------------------- 4. count coupling ---
    cc = _load(ROB / "crn_count_check.yaml")
    if cc:
        L.append("---")
        L.append("")
        L.append("## 4. Count observations under common random numbers — degeneracy or artefact?")
        L.append("")
        L.append("Test statistic `final_size`, which is linear, so the target derivative is available")
        L.append("in closed form from the deterministic mean with no Monte Carlo error.")
        L.append("")
        L.append("### 4.1 The pathwise map, walked finely at one fixed seed")
        L.append("")
        cen = cc["pathwise_step_census"]
        L.append(f"`eta` walked over [{_fmt(cen['eta_range'][0], 3)}, {_fmt(cen['eta_range'][1], 3)}] "
                 f"in {cen['n_points']} steps.")
        L.append("")
        L.append("| Coupling | distinct values | jumps | adjacent pairs exactly equal | largest jump | total variation | net change across the range |")
        L.append("|---|---|---|---|---|---|---|")
        for kind in ("lognormal", "poisson_numpy", "poisson_inversion"):
            b = cen[kind]
            L.append(f"| {kind} | {b['n_distinct_values']} / {b['n_points']} | {b['n_jumps']} "
                     f"| {_fmt(b['fraction_of_adjacent_pairs_exactly_equal'], 4)} "
                     f"| {_fmt(b['largest_jump'])} | {_fmt(b['total_variation'])} "
                     f"| {_fmt(b['endpoint_change'])} |")
        L.append("")
        L.append("### 4.2 The difference quotient across the pre-registered h sweep")
        L.append("")
        L.append("`R_small` is the replicate count the reported diagnostic used; `R_large` is large")
        L.append("enough to separate bias from variance.")
        L.append("")
        for kind in ("lognormal", "poisson_numpy", "poisson_inversion"):
            L.append(f"**{kind}**")
            L.append("")
            L.append("| h | exact derivative of the mean | estimate at R_small | relative error at R_small | mean at R_large | relative bias at R_large | sd of one replicate | fraction of replicates exactly zero | sample sd at R_small exactly zero |")
            L.append("|---|---|---|---|---|---|---|---|---|")
            for row in cc["difference_quotients"]:
                b = row[kind]
                L.append(f"| {_fmt(row['h'])} | {_fmt(row['exact_derivative_of_the_mean'], 6)} "
                         f"| {_fmt(b['estimate_at_R_small'], 6)} "
                         f"| {_fmt(b['relative_error_at_R_small'], 3)} "
                         f"| {_fmt(b['mean_over_R_large'], 6)} "
                         f"| {_fmt(b['relative_bias_over_R_large'], 3)} "
                         f"| {_fmt(b['sd_of_one_replicate'])} "
                         f"| {_fmt(b['fraction_of_replicates_exactly_zero'], 4)} "
                         f"| {_fmt(b['sample_sd_at_R_small_is_exactly_zero'])} |")
            L.append("")
        s = cc["settings"]
        L.append(f"`R_small = {s['R_small']}`, `R_large = {s['R_large']}`, "
                 f"component perturbed: `{COMPONENTS[s['component_perturbed']]}`, "
                 f"`obs_sigma = {_fmt(s['obs_sigma'])}`.")
        L.append("")

    L.append("---")
    L.append("")
    L.append("## Provenance of every run quoted above")
    L.append("")
    L.append("| File | script | commit | dirty | seed |")
    L.append("|---|---|---|---|---|")
    for p in sorted(ROB.glob("*.yaml")):
        d = _load(p)
        pr = d.get("provenance", {})
        L.append(f"| `{p.relative_to(REPO)}` | `{pr.get('script', '?')}` "
                 f"| `{str(pr.get('commit', '?'))[:12]}` | {pr.get('dirty')} | {pr.get('seed')} |")
    L.append("")
    return "\n".join(L) + "\n"


def main() -> int:
    out = ROB / "ROBUSTNESS_TABLE.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(), encoding="utf-8")
    print(f"wrote {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
