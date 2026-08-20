"""Generate the results tables that the reports quote, from the results files.

``PROVENANCE.md`` and this project's standing constraint S11 require that no number be
hand-typed into a markdown file. The reports in ``audit/`` need to state what the diagnostic
found, so the tables they state it with are GENERATED from ``results/*.yaml`` by this script
and written to ``results/SUMMARY_TABLE.md``, which the reports reference and reproduce.

Usage
-----
    python -m src.diagnostics.report_tables
"""

from __future__ import annotations

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "results"
SETS = ("S_A", "S_B", "S_C")


def _fmt(x: float, sig: int = 4) -> str:
    if x != x:
        return "nan"
    if x == float("inf"):
        return "inf"
    return f"{x:.{sig}g}"


def build() -> str:
    docs = {}
    for name in SETS:
        p = RESULTS / f"jacobian_rank.{name}.yaml"
        if not p.exists():
            raise SystemExit(f"missing {p}; run src.diagnostics.run_diagnostic first")
        docs[name] = yaml.safe_load(p.read_text(encoding="utf-8"))

    prov = docs["S_A"]["provenance"]
    fc = yaml.safe_load((RESULTS / "floor_check.yaml").read_text(encoding="utf-8"))["floor_check"]
    ctrl_path = RESULTS / "jacobian_rank.S_A.no_crn_control.yaml"
    ctrl = yaml.safe_load(ctrl_path.read_text(encoding="utf-8")) if ctrl_path.exists() else None

    L: list[str] = []
    L.append("# Results tables — GENERATED, not typed")
    L.append("")
    L.append("Produced by `src/diagnostics/report_tables.py` from `results/*.yaml`. Do not edit by")
    L.append("hand: this file exists so that the reports in `audit/` can quote numbers without any")
    L.append("number being hand-typed into a markdown file (S11, `PROVENANCE.md`).")
    L.append("")
    L.append(f"- commit: `{prov['commit']}`")
    L.append(f"- dirty: `{prov['dirty']}`")
    L.append(f"- command: `{prov['command']}`")
    L.append(f"- seed: `{prov['seed']}`")
    L.append(f"- python `{prov['python']}`, deps `{prov['deps']}`")
    L.append("")

    # --- 1. headline verdicts -----------------------------------------------------------
    L.append("## 1. Verdict per summary set")
    L.append("")
    L.append("| Summary set | d | rank at tau=1e-2 | full column rank | condition number | verdict |")
    L.append("|---|---|---|---|---|---|")
    for name in SETS:
        r = docs[name]["results"]
        nr = r["numerical_rank"]
        rank = f"{nr['rank_certain']}" if nr["determined"] else f"{nr['rank_certain']}–{nr['rank_possible']}"
        L.append(
            f"| {name} | {r['dimensions']['d']} | {rank} | "
            f"{'yes' if nr['full_column_rank'] else 'NO'} | {_fmt(r['condition_number'])} | "
            f"{'INSEPARABLE' if r['inseparable'] else 'separable'} |"
        )
    L.append("")
    for name in SETS:
        L.append(f"- **{name}** — {docs[name]['results']['inseparable_reason']}")
    L.append("")

    # --- 2. singular values and plateau -------------------------------------------------
    L.append("## 2. Singular values, plateau, and resolution")
    L.append("")
    L.append("| Summary set | singular values at representative h | plateau (h range) | "
             "n h in plateau | censored small / large h | all resolved |")
    L.append("|---|---|---|---|---|---|")
    for name in SETS:
        r = docs[name]["results"]
        pl = r["plateau"]
        sv = ", ".join(_fmt(x) for x in r["singular_values_at_representative_h"])
        L.append(
            f"| {name} | {sv} | {_fmt(pl['h_range'][0])} → {_fmt(pl['h_range'][1])} | "
            f"{pl['n_h_in_plateau']} | {pl['censored_at_small_h']} / {pl['censored_at_large_h']} | "
            f"{all(r['resolved'])} |"
        )
    L.append("")
    L.append("A plateau reaching the edge of the pre-registered sweep is reported as **censored**")
    L.append("there: the sweep stopped, not the plateau.")
    L.append("")

    L.append("### 2.1 Full h-sweep, leading singular value")
    L.append("")
    hs = [row["h"] for row in docs["S_A"]["results"]["h_sweep"]]
    L.append("| h | " + " | ".join(SETS) + (" | S_A no-CRN control |" if ctrl else " |"))
    L.append("|---|" + "---|" * (len(SETS) + (1 if ctrl else 0)))
    for i, h in enumerate(hs):
        cells = [_fmt(docs[n]["results"]["h_sweep"][i]["singular_values"][0]) for n in SETS]
        if ctrl:
            cells.append(_fmt(ctrl["results"]["h_sweep"][i]["singular_values"][0]))
        L.append(f"| {_fmt(h)} | " + " | ".join(cells) + " |")
    L.append("")

    # --- 3. columns and coherence -------------------------------------------------------
    comps = docs["S_A"]["component_labels"]
    L.append("## 3. Column norms and pairwise coherence")
    L.append("")
    L.append("A near-zero **column norm** means a component is invisible to these summaries — a")
    L.append("different failure from collinearity, with different consequences. Rank alone conflates")
    L.append("them, so they are reported separately.")
    L.append("")
    L.append("| Summary set | " + " | ".join(f"‖J·{c}‖" for c in comps) + " | invisible (<0.1) |")
    L.append("|---|" + "---|" * (len(comps) + 1))
    for name in SETS:
        r = docs[name]["results"]
        inv = [comps[i] for i in r["invisible_components"]] or ["none"]
        L.append(f"| {name} | " + " | ".join(_fmt(x) for x in r["column_norms"]) + f" | {', '.join(inv)} |")
    L.append("")
    L.append("| Summary set | " + " | ".join(
        f"mu({comps[i]},{comps[j]})" for i in range(len(comps)) for j in range(i + 1, len(comps))
    ) + " | flagged (>=0.98) |")
    L.append("|---|" + "---|" * (3 + 1))
    for name in SETS:
        r = docs[name]["results"]
        coh = r["pairwise_coherence"]
        vals = [_fmt(coh[i][j]) for i in range(len(comps)) for j in range(i + 1, len(comps))]
        fl = [f"{comps[i]}–{comps[j]}" for i, j in r["coherence_flagged_pairs"]] or ["none"]
        L.append(f"| {name} | " + " | ".join(vals) + f" | {', '.join(fl)} |")
    L.append("")
    L.append("Coherence is reported for interpretation and is **not** the decision rule; the decision")
    L.append("rule is on the singular values (`docs/THRESHOLDS.md` §2.2).")
    L.append("")

    # --- 4. near-null directions --------------------------------------------------------
    L.append("## 4. Near-null directions and equivalence classes")
    L.append("")
    any_nn = False
    for name in SETS:
        r = docs[name]["results"]
        for nn in r["near_null_directions"]:
            any_nn = True
            v = ", ".join(_fmt(x) for x in nn["right_singular_vector_at_representative_h"])
            mem = ", ".join(comps[k] for k in nn["equivalence_class_members"]) or "none"
            bor = ", ".join(comps[k] for k in nn["borderline_members"]) or "none"
            L.append(f"**{name}**, direction {nn['index']} — `sigma = {_fmt(nn['singular_value'])}`, "
                     f"`sigma/sigma_1 = {_fmt(nn['sigma_ratio_to_sigma1'])}`, "
                     f"**{nn['degeneracy_kind']}** degeneracy")
            L.append("")
            L.append(f"- right singular vector: ({v}) over ({', '.join(comps)})")
            L.append(f"- equivalence-class members (|v_k| >= 0.3 across the whole plateau): {mem}")
            L.append(f"- borderline (|v_k| crosses 0.3 within the plateau): {bor}")
            L.append(f"- |v_k| ranges across plateau: " + "; ".join(
                f"{comps[k]} [{_fmt(a)}, {_fmt(b)}]"
                for k, (a, b) in enumerate(nn["abs_vk_range_across_plateau"])))
            L.append("")
    if not any_nn:
        L.append("None. No summary set has a singular value at or below `tau * sigma_1`.")
        L.append("")
    L.append("`docs/THRESHOLDS.md` §3.4: an **exact** degeneracy is a statement about")
    L.append("identifiability, matching Kahl et al. (2019). A **near** degeneracy at condition number")
    L.append("kappa is a statement about **affordability** — separation costs about kappa^2 replicates")
    L.append("— and must never be written as an identifiability claim.")
    L.append("")

    # --- 5. floor check -----------------------------------------------------------------
    L.append("## 5. Random-attributor floor check")
    L.append("")
    L.append("| K | analytic floor 1/K | simulated accuracy | deviation | tolerance (4 s.e.) | passes |")
    L.append("|---|---|---|---|---|---|")
    L.append(f"| {fc['K']} | {_fmt(fc['floor_analytic'], 6)} | {_fmt(fc['accuracy_simulated'], 6)} | "
             f"{_fmt(fc['deviation_from_floor'], 3)} | {_fmt(fc['tolerance_4se'], 3)} | {fc['passes']} |")
    L.append("")
    L.append(f"Run as {fc['n_draws']} draws at seed {fc['seed']}. Every attribution accuracy this")
    L.append("project reports is reported against this floor.")
    L.append("")

    # --- 6. no-CRN control --------------------------------------------------------------
    if ctrl:
        L.append("## 6. Negative control — the same sweep without common random numbers")
        L.append("")
        c = ctrl["results"]
        L.append(f"- plateau found: **{c['plateau']['found']}**")
        lead = [row["singular_values"][0] for row in c["h_sweep"]]
        L.append(f"- leading singular value across the sweep: "
                 + ", ".join(_fmt(x) for x in lead))
        ratios = [lead[i + 1] / lead[i] for i in range(len(lead) - 1) if lead[i] > 0]
        L.append(f"- ratio between successive (ten-fold smaller) h: "
                 + ", ".join(_fmt(x, 3) for x in ratios))
        L.append("")
        L.append("Without common random numbers the difference quotient carries noise of order")
        L.append("`obs_sigma / h`, so the leading singular value grows as `1/h` and no plateau exists.")
        L.append("This is the control that makes the main sweep's plateau meaningful rather than")
        L.append("assumed.")
        L.append("")

    # --- 7. STOP condition --------------------------------------------------------------
    L.append("## 7. D4 STOP condition")
    L.append("")
    fired = all(docs[n]["results"]["inseparable"] for n in SETS)
    sep = [n for n in SETS if not docs[n]["results"]["inseparable"]]
    if fired:
        L.append("**FIRED.** All three summary sets are inseparable. See")
        L.append("`results/STOP_CONDITION_FIRED.md`. This is a legitimate negative identifiability")
        L.append("result for this simulator, not a project failure.")
    else:
        L.append(f"**Did not fire.** Separable summary set(s): **{', '.join(sep)}**.")
        L.append("")
        L.append("`docs/THRESHOLDS.md` §1.6 notes that because `S_C` is expected to fail by")
        L.append("construction, the STOP condition is decided by `S_A` and `S_B`, and `S_C`'s designed")
        L.append("failure must not later be read as one third of the evidence for stopping.")
    L.append("")
    return "\n".join(L) + "\n"


def main() -> int:
    out = RESULTS / "SUMMARY_TABLE.md"
    out.write_text(build(), encoding="utf-8")
    print(f"wrote {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
