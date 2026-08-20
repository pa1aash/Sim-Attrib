"""Generate ``results/robustness/K6_TABLE.md`` from ``results/robustness/k6_spectrum.yaml``.

``audit/K6_SPECTRUM_CHECK.md`` quotes this file verbatim, so no number in that document is
typed by hand (standing constraint S10). Same device as
``src/diagnostics/report_robustness.py``, which G4 used for the same reason.

    python -m src.diagnostics.report_k6
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "results" / "robustness" / "k6_spectrum.yaml"
OUT = REPO / "results" / "robustness" / "K6_TABLE.md"


def g(x: Any, digits: int = 4) -> str:
    if x is None:
        return "—"
    if isinstance(x, bool):
        return "yes" if x else "no"
    if isinstance(x, (int,)):
        return str(x)
    if isinstance(x, float):
        if math.isinf(x):
            return "inf"
        return f"{x:.{digits}g}"
    return str(x)


def lst(xs, digits: int = 4) -> str:
    return ", ".join(g(x, digits) for x in xs)


def main() -> int:
    d = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    p = d["provenance"]
    L: list[str] = []
    A = L.append

    A("# The K = 6 spectrum, and the eight family assignments")
    A("")
    A("Produced by `src/diagnostics/report_k6.py` from `results/robustness/k6_spectrum.yaml`.")
    A("Do not edit by hand. `audit/K6_SPECTRUM_CHECK.md` quotes this file verbatim.")
    A("")
    A("**Nothing here replaces `results/jacobian_rank.*.yaml` or the G4 files in")
    A("`results/robustness/`.** Those record what sessions G3 and G4 ran and are untouched.")
    A("")
    A(f"Run: script `{p['script']}`, commit `{p['commit'][:12]}`, dirty `{p['dirty']}`, "
      f"seed `{p['seed']}`, {d['settings']['n_simulator_runs']} simulator runs.")
    A("")
    A("---")
    A("")

    # --- 1. the three spectra -----------------------------------------------------------
    A("## 1. The three spectra, in full")
    A("")
    A("`base` and `adversarial` are the two declared family sets, three columns each.")
    A("`union` is the six-column Jacobian their columns define — **the only six-column object")
    A("the two declared sets supply**, since a family set assigns one family per component")
    A("(`DEVIATIONS.md` D-12).")
    A("")
    A("| Summary set | columns | singular values | sigma_i/sigma_1 | spread (decades) | rank at tau | kappa | verdict |")
    A("|---|---|---|---|---|---|---|---|")
    for name, blk in d["summary_sets"].items():
        for key, label in (("base", "base"), ("adversarial", "adversarial"),
                           ("six_columns", "**union (K=6)**")):
            k = blk[key]
            sp = k["spectrum"]
            A(f"| {name} | {label} | {lst(sp['singular_values'])} | "
              f"{lst(sp['sigma_i_over_sigma_1'], 3)} | "
              f"{g(sp['spread_decades_over_positive_singular_values'], 3)} | "
              f"{k['numerical_rank']['rank_certain']}/{k['n_columns']} | "
              f"{g(k['condition_number'])} | {k['verdict']} |")
    A("")
    A("### 1.1 Is there a gap anywhere, or a smooth decay throughout?")
    A("")
    A("`gap prominence` is the largest adjacent ratio divided by the median adjacent ratio.")
    A("**It is descriptive and no verdict depends on it**: 1.0 means a perfectly geometric")
    A("decay with no break anywhere, larger means one ratio dominates. No threshold is applied")
    A("to it, because inventing a gap criterion now — with the singular values visible — is the")
    A("leakage failure `LEDGER_DESIGN.md` D3 exists to prevent.")
    A("")
    A("`where tau*sigma_1 sits` needs no threshold at all, and is the operational form of the")
    A("Gutenkunst objection: a tolerance cutting through a dense spectrum reports where the")
    A("analyst put it; a tolerance an order of magnitude below every singular value does not.")
    A("")
    A("| Summary set | columns | adjacent ratios | largest | median | gap prominence | where tau*sigma_1 sits |")
    A("|---|---|---|---|---|---|---|")
    for name, blk in d["summary_sets"].items():
        for key, label in (("base", "base"), ("adversarial", "adversarial"),
                           ("six_columns", "**union (K=6)**")):
            sp = blk[key]["spectrum"]
            A(f"| {name} | {label} | {lst(sp['adjacent_ratios'])} | "
              f"{g(sp['largest_adjacent_ratio'])} | {g(sp['median_adjacent_ratio'])} | "
              f"{g(sp['gap_prominence_largest_over_median_adjacent_ratio'], 3)} | "
              f"{sp['where_tau_sigma1_sits']} |")
    A("")
    A("### 1.2 Is the six-column rank deficiency real, or is the estimator not resolving it?")
    A("")
    A("`docs/THRESHOLDS.md` §1.4: a singular value is **resolved** if it varies by less than a")
    A("factor of 2 across the h-plateau, and an unresolved one is counted toward the rank in")
    A("neither direction. `results/robustness/wide_spectrum_check.yaml` measured the six-column")
    A("spectrum at a single h and therefore could not answer this.")
    A("")
    A("| Summary set | columns | plateau found | h range | variation factor per sigma | all resolved | rank determined |")
    A("|---|---|---|---|---|---|---|")
    for name, blk in d["summary_sets"].items():
        for key, label in (("base", "base"), ("adversarial", "adversarial"),
                           ("six_columns", "**union (K=6)**")):
            k = blk[key]
            A(f"| {name} | {label} | {g(k['plateau']['found'])} | "
              f"{lst(k['plateau']['h_range'])} | "
              f"{lst(k['singular_value_variation_factor'])} | "
              f"{g(all(k['resolved']))} | {g(k['numerical_rank']['determined'])} |")
    A("")

    # --- 2. near-null classification ------------------------------------------------------
    A("## 2. What the six-column near-null directions actually confound")
    A("")
    A("The six columns are two distortions of each of the same three mechanisms, so a rank")
    A("deficiency can mean two opposite things. **Within-mechanism**: two deformations of the")
    A("SAME component are hard to tell apart — which component attribution never claimed to do.")
    A("**Cross-mechanism**: two different components are confounded — which is the failure the")
    A("K = 3 verdict rules out. The distinction was written into")
    A("`src/diagnostics/k6_spectrum.py` before this run produced a number.")
    A("")
    A("Membership uses the pre-registered rule of `docs/THRESHOLDS.md` §2.1 (`|v_k| >= 0.3`")
    A("throughout the plateau). `mechanism energy` is threshold-free: the squared weight the")
    A("direction places on each mechanism's two columns, summing to one.")
    A("")
    A(f"Columns, in order: `{'`, `'.join(d['six_column_labels'])}`")
    A("")
    for name, blk in d["summary_sets"].items():
        cls = blk["six_columns"].get("near_null_classification", [])
        if not cls:
            continue
        A(f"### 2.{list(d['summary_sets']).index(name) + 1} {name}")
        A("")
        A("| sigma | sigma/sigma_1 | kind | class members | mechanisms | energy: transmission / progression / observation |")
        A("|---|---|---|---|---|---|")
        for nn, cl in zip(blk["six_columns"]["near_null_directions"], cls):
            e = cl["mechanism_energy"]
            A(f"| {g(nn['singular_value'])} | {g(nn['sigma_ratio_to_sigma1'], 3)} | "
              f"**{cl['kind']}** | {', '.join('`' + m + '`' for m in cl['column_members'])} | "
              f"{', '.join(cl['mechanisms_in_class'])} | "
              f"{g(e['transmission'], 3)} / {g(e['progression'], 3)} / {g(e['observation'], 3)} |")
        A("")
        A("Right singular vectors at the representative `h`, with `|v_k|` ranges across the plateau:")
        A("")
        A("| sigma | " + " | ".join(f"`{c}`" for c in d["six_column_labels"]) + " |")
        A("|---|" + "---|" * len(d["six_column_labels"]))
        for nn in blk["six_columns"]["near_null_directions"]:
            cells = [f"{v:+.4f}<br>[{r[0]:.4f}, {r[1]:.4f}]"
                     for v, r in zip(nn["right_singular_vector_at_representative_h"],
                                     nn["abs_vk_range_across_plateau"])]
            A(f"| {g(nn['singular_value'])} | " + " | ".join(cells) + " |")
        A("")

    # --- 3. the eight triples --------------------------------------------------------------
    A("## 3. The eight component-wise family assignments")
    A("")
    A("`B` is the base family for that component, `A` the adversarial one, in the order")
    A("`(transmission, progression, observation)`. **`BBB` and `AAA` are the two declared sets**;")
    A("the other six are three-column distortion models built from the same columns, which an")
    A("analyst could equally have declared. No new family is invented and no additional")
    A("simulation was run.")
    A("")
    for name, blk in d["summary_sets"].items():
        A(f"### 3.{list(d['summary_sets']).index(name) + 1} {name}")
        A("")
        A("| code | families | declared? | singular values | rank at tau | kappa | tau* / registered tau | verdict | equivalence class |")
        A("|---|---|---|---|---|---|---|---|---|")
        for code, t in blk["mixed_triples"].items():
            ts = t["tau_sensitivity"]["exact_flip_point"]
            cls = "; ".join("{" + ", ".join(c) + "}" for c in t["equivalence_classes"]) or "—"
            A(f"| `{code}` | {t['families']} | {'**yes**' if t['is_a_declared_family_set'] else 'no'} | "
              f"{lst(t['spectrum']['singular_values'])} | "
              f"{t['numerical_rank']['rank_certain']}/3 | {g(t['condition_number'])} | "
              f"{g(ts['as_multiple_of_registered_tau'], 3)}x | "
              f"{'**' + t['verdict'] + '**' if t['verdict'] == 'INSEPARABLE' else t['verdict']} | {cls} |")
        A("")

    # --- 4. tau sensitivity ----------------------------------------------------------------
    A("## 4. Threshold sensitivity")
    A("")
    A("Every row is produced by calling the production `analyse()` with the thresholds passed")
    A("as the parameters they already are — nothing is transcribed, so nothing can drift from")
    A("the rule the reported numbers were produced by.")
    A("")
    A("`docs/THRESHOLDS.md` §1.2 derives `kappa_max = 1/tau`, so the **coupled** rows move both")
    A("together, which is the pair the project registered. The **tau alone** rows hold")
    A("`kappa_max` at 100 and are how the `kappa` branch becomes reachable at all.")
    A("")
    for name, blk in d["summary_sets"].items():
        for key, label in (("base", "base"), ("adversarial", "adversarial"),
                           ("six_columns", "union (K=6)")):
            ts = blk[key]["tau_sensitivity"]
            A(f"### {name} — {label}")
            A("")
            fp = ts["exact_flip_point"]
            A(f"Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = "
              f"**{g(fp['tau_star_sigma_K_over_sigma_1'], 6)}** = "
              f"**{g(fp['as_multiple_of_registered_tau'], 4)}x** the registered `tau`.")
            A("")
            A("| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |")
            A("|---|---|---|---|---|---|---|")
            for rc, ra in zip(ts["coupled_kappa_max_equals_one_over_tau"],
                              ts["tau_varied_alone_kappa_max_held_at_registered_100"]):
                A(f"| {g(rc['tau'])} | {g(rc['tau'] / 0.01, 3)}x | "
                  f"{rc['rank_certain']}/{ts['K']} | {rc['verdict']} | "
                  f"{ra['rank_certain']}/{ts['K']} | {ra['verdict']} | "
                  f"{g(ra['kappa_branch_fires_alone'])} |")
            st = ts["coupled_stability"]
            A("")
            A(f"Verdict at the registered `tau` is **{st['verdict_at_registered_tau']}**, stable over "
              f"`tau` in [{g(st['stable_over_tau_range'][0])}, {g(st['stable_over_tau_range'][1])}] "
              f"= x{g(st['stable_over_multiplier_range'][0], 3)} to x{g(st['stable_over_multiplier_range'][1], 3)}; "
              f"flips at the next grid point below: {g(st['flips_at_next_tau_below'])}, "
              f"above: {g(st['flips_at_next_tau_above'])}. "
              f"Grid-censored below: {g(st['boundary_is_censored_by_the_grid_below'])}, "
              f"above: {g(st['boundary_is_censored_by_the_grid_above'])}.")
            A("")

    # --- 5. kappa branch --------------------------------------------------------------------
    A("## 5. The kappa_max branch — reachable, and exactly where")
    A("")
    A("`audit/G3_ADVERSARIAL_REVIEW.md` finding 1.4 established that at the registered pair the")
    A("two criteria of `docs/THRESHOLDS.md` §1.3 are one criterion, and left the branch")
    A("unexplored. The prediction, from the algebra: **with every singular value resolved, the")
    A("`kappa` branch fires alone exactly on `kappa_max < kappa <= 1/tau`, which is empty")
    A("whenever `kappa_max >= 1/tau` — and the registered pair sets `kappa_max = 1/tau`.**")
    A("")
    A("The grid below recomputes the verdict through the production `analyse()` at every")
    A("`(tau, kappa_max)` pair and the script checks each row against that prediction, so a")
    A("disagreement between the algebra and the production rule is a failure and not a footnote.")
    A("")
    A("| Summary set | columns | kappa | grid points | where kappa branch fires alone | algebra agrees | smallest kappa_max at registered tau that flips the verdict |")
    A("|---|---|---|---|---|---|---|")
    for name, blk in d["summary_sets"].items():
        for key, label in (("base", "base"), ("adversarial", "adversarial"),
                           ("six_columns", "**union (K=6)**")):
            kb = blk[key]["kappa_branch"]
            A(f"| {name} | {label} | {g(kb['measured_condition_number'])} | "
              f"{kb['n_grid_points']} | {kb['n_where_kappa_branch_fires_alone']} | "
              f"{g(kb['algebra_agrees_with_production_rule'])} | "
              f"{g(kb['smallest_kappa_max_at_registered_tau_that_flips_the_verdict'])} |")
    A("")

    # --- 6. checks --------------------------------------------------------------------------
    A("## 6. The checks this run had to pass before any of the above counts")
    A("")
    A("| Summary set | columns | leakage check (permutation equivariance) | permutations tested | reproduces the recorded singular values |")
    A("|---|---|---|---|---|")
    for name, blk in d["summary_sets"].items():
        for key, label in (("base", "base"), ("adversarial", "adversarial"),
                           ("six_columns", "**union (K=6)**")):
            k = blk[key]
            rep = k.get("reproduction_check")
            rep_s = ("—" if rep is None else
                     ("n/a — no recorded run at these settings" if not rep.get("available")
                      else f"{g(rep['reproduces'])} (max rel diff {g(rep['max_relative_difference'], 2)})"))
            A(f"| {name} | {label} | {g(k['leakage_check']['passes'])} | "
              f"{k['leakage_check']['n_permutations_tested']} | {rep_s} |")
    A("")
    A("The reproduction check is the load-bearing one: the three-column spectra computed here")
    A("must equal, to floating point, the ones already on record from sessions G3 and G4 at the")
    A("same seed, replicate count and step size. If they did not, this run's estimator would be")
    A("a different estimator and no six-column number from it could be compared with the")
    A("three-column result it is supposed to extend.")
    A("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} ({len(L)} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
