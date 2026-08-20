"""The pre-registered cost gate, applied to the measured ``p_sel`` -- session G6, Phase 2.

THE GATE IS NOT WRITTEN HERE. IT WAS WRITTEN IN SESSION G3, BEFORE ``p_sel`` EXISTED
--------------------------------------------------------------------------------------
``audit/MMC_COMPOSITION_SPEC.md`` §4, verbatim, and this module implements it rather than
restating it::

    E[ draws ]  =  M  x  N  /  p_sel(theta)        <- per nuisance value, MULTIPLIED

    A pre-registered cost gate, so this is decidable rather than arguable. Before any
    implementation, the next session should measure p_sel directly ... and record it. If
    M x N / min_theta p_sel exceeds 10^8 simulator draws at the demonstration's scale, the
    composition is not affordable on the declared budget and the honest output is the cost
    analysis itself, not a scaled-down experiment that hides it.

and the factors, from the same section's table::

    1 / p_sel                             ~150            Freidling et al., their experiments
    N                                     99-999          Dufour's standard choice
    M, simulated-annealing evaluations    10^3-10^4       derivative-free search over Omega_0
    Product                               ~10^7-10^9 simulator draws

``M`` and ``N`` are taken from that table and are **not** re-derived here. The specification
gives them as RANGES, so the gate is evaluated at all four corners of the declared box and
the spread between corners is reported rather than collapsed.

THE DECISION RULES, PRE-REGISTERED IN THIS FILE BEFORE ``results/p_sel.yaml`` EXISTED
--------------------------------------------------------------------------------------
1. **Which ``p_sel``.** §4 point 1 says the cost is governed by ``min over theta`` across the
   searched set, *"not by its value at a plausible theta"*. So the gate takes the minimum
   over the nuisance box declared as the headline in ``src/diagnostics/p_sel.py``, using the
   independently re-measured value wherever a point was refined. It also takes the minimum
   over the ``K`` selection cells, because the cell is chosen by the data and the procedure
   has to terminate for whichever one arises.
2. **Per-corner verdict.** A corner ``(M, N)`` PASSES when ``M*N/p_sel <= 1e8``.
3. **Per-case verdict.** ``PASS`` when all four corners pass; ``FAIL`` when all four fail;
   ``SPLIT`` otherwise -- meaning the gate is not decided by the specification's own declared
   ranges, which is a fact about the specification and is reported as one.
4. **Session verdict.** Taken on the PRIMARY case only -- ``S_B`` under ``AAA``, per the
   session brief -- and only ``PASS`` if that case passes under **both** studentisation
   variants of the selection rule. Anything else is ``SPLIT`` or ``FAIL``. **A ``SPLIT`` is
   not a pass**, and is treated as one for the purpose of what the session may do next. This
   is G5's own convention (``WEAKENED is not a clean pass``) applied to a different verdict.
5. **Uncertainty (standing constraint S5).** Every cost is reported with the interval induced
   by the 95% Wilson interval on ``p_sel``. ``ci_decides_the_gate`` reads **FALSE** when the
   per-case verdict differs between the two ends of that interval -- in which case the
   measurement is too imprecise to decide the gate, and that is the headline rather than a
   footnote.
6. **Zero acceptances.** ``p_sel = 0`` in ``n`` draws is not ``p_sel = 0``. The point cost is
   infinite and the reported bound is ``M*N/upper``, with ``upper`` the Wilson upper limit.
   Specification §3.4 names this case separately: a nuisance value at which the observed
   selection is impossible is one where *"the rejection sampler never terminates"*.

UNDER WHAT CONDITION DOES EACH FLAG READ FALSE? (standing constraint S4)
------------------------------------------------------------------------
``corner.passes``          FALSE whenever ``M*N/p_sel > 1e8``. The exact ``p_sel`` at which
    each corner flips is reported next to it (``p_sel_at_which_this_corner_flips = M*N/1e8``),
    so the boundary is visible rather than implied, and ``tests/test_cost_gate.py`` requires
    the flag to come out both ways on either side of it.
``ci_decides_the_gate``    FALSE when the verdict at the CI lower end differs from the verdict
    at the CI upper end. Reachable, and the test constructs a case where it fires.
``within_declared_budget`` FALSE when the cost exceeds the 1e7 forward solves
    ``audit/S0_REPORT.md`` §7 prices as the point where CPU-only stops holding. **This is a
    different and stricter number than the gate's own 1e8**, and the discrepancy is reported
    rather than reconciled: the gate says "not affordable on the declared budget" at a
    threshold ten times the declared budget.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Any

import yaml

from ..provenance import header, now_iso

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results"

#: From audit/MMC_COMPOSITION_SPEC.md section 4's table. Not chosen here.
M_VALUES: tuple[int, ...] = (10 ** 3, 10 ** 4)
N_VALUES: tuple[int, ...] = (99, 999)

#: The pre-registered gate, audit/MMC_COMPOSITION_SPEC.md section 4.
GATE_DRAWS: float = 1e8

#: The declared compute budget, audit/S0_REPORT.md section 7: "Forward simulation only,
#: <=10^7 solves, no neural components | CPU-only holds; local, overnight". Reported
#: alongside the gate; it is NOT the gate.
DECLARED_BUDGET_DRAWS: float = 1e7


def cost(m: int, n: int, p: float) -> float:
    """``M * N / p_sel``. Infinite at ``p_sel = 0``, which is the honest value."""
    return float("inf") if p <= 0.0 else float(m) * float(n) / float(p)


def corner_rows(p: float, lo: float, hi: float) -> list[dict[str, Any]]:
    """One row per declared ``(M, N)`` corner, with the flip point stated next to the flag."""
    rows = []
    for m in M_VALUES:
        for n in N_VALUES:
            rows.append({
                "M": int(m), "N": int(n), "M_times_N": int(m * n),
                "expected_draws": cost(m, n, p),
                "expected_draws_ci95_lower": cost(m, n, hi),   # larger p -> smaller cost
                "expected_draws_ci95_upper": cost(m, n, lo),
                "passes": bool(cost(m, n, p) <= GATE_DRAWS),
                "passes_at_ci95_lower_p": bool(cost(m, n, lo) <= GATE_DRAWS),
                "passes_at_ci95_upper_p": bool(cost(m, n, hi) <= GATE_DRAWS),
                "p_sel_at_which_this_corner_flips": float(m * n) / GATE_DRAWS,
                "within_declared_budget_1e7": bool(cost(m, n, p) <= DECLARED_BUDGET_DRAWS),
            })
    return rows


def verdict(rows: list[dict[str, Any]], key: str = "passes") -> str:
    """PASS if every corner passes, FAIL if none does, SPLIT otherwise."""
    flags = [bool(r[key]) for r in rows]
    if all(flags):
        return "PASS"
    if not any(flags):
        return "FAIL"
    return "SPLIT"


def gate_case(p: float, lo: float, hi: float) -> dict[str, Any]:
    """The full gate for one (assignment, variant): corners, verdict, and the CI's verdict."""
    rows = corner_rows(p, lo, hi)
    v = verdict(rows)
    v_lo = verdict(rows, "passes_at_ci95_lower_p")
    v_hi = verdict(rows, "passes_at_ci95_upper_p")
    return {
        "p_sel": float(p), "p_sel_ci95": [float(lo), float(hi)],
        "corners": rows,
        "verdict": v,
        "verdict_at_ci95_lower_p": v_lo,
        "verdict_at_ci95_upper_p": v_hi,
        "ci_decides_the_gate": bool(v_lo == v_hi == v),
    }


def session_verdict(cases: dict[str, dict[str, Any]], primary: str) -> dict[str, Any]:
    """PASS only if the primary assignment passes under BOTH variants. SPLIT is not a pass."""
    vs = [c["verdict"] for k, c in cases.items() if k.startswith(primary + "|")]
    if not vs:
        raise ValueError(f"no cases for primary assignment {primary!r}")
    if all(v == "PASS" for v in vs):
        out = "PASS"
    elif all(v == "FAIL" for v in vs):
        out = "FAIL"
    else:
        out = "SPLIT"
    return {
        "primary_assignment": primary,
        "per_variant_verdicts": {k: c["verdict"] for k, c in cases.items()
                                 if k.startswith(primary + "|")},
        "verdict": out,
        "is_a_pass": bool(out == "PASS"),
        "rule": "PASS only if every declared (M, N) corner passes under BOTH studentisation "
                "variants of the selection rule. A SPLIT is not a pass.",
    }


def worst_over_box(doc: dict[str, Any], key: str, width: float) -> dict[str, Any]:
    """Smallest ``p_sel`` over the cells and over the box of the given half-width.

    Uses the independently re-measured value at any point that was refined, because the
    smallest of many noisy estimates is biased low and re-measuring it on fresh draws is the
    correction rather than a second look.
    """
    best: dict[str, Any] | None = None
    for pt in doc["stage_B_nuisance_box"]:
        if pt["width"] > width:
            continue
        block = pt["refined"] if pt["refined"] is not None else pt["screen"]
        src = "refined" if pt["refined"] is not None else "screen"
        b = block[key]
        for k, p in enumerate(b["p_sel"]):
            cand = {"p_sel": float(p), "ci95": [float(b["ci95_lower"][k]),
                                                float(b["ci95_upper"][k])],
                    "n_draws": int(b["n_draws"]), "counts": int(b["counts"][k]),
                    "cell": int(k), "theta_key": pt["key"], "width": float(pt["width"]),
                    "estimate_source": src}
            if best is None or cand["p_sel"] < best["p_sel"]:
                best = cand
    assert best is not None
    return best


def build(doc: dict[str, Any]) -> dict[str, Any]:
    """Assemble the whole gate document from a measured ``p_sel`` record."""
    settings = doc["settings"]
    keys = list(doc["stage_A_theta0"].keys())
    headline_w = float(settings["headline_box_half_width"])
    primary = str(settings["family_codes"][0])
    sec_per_draw = float(settings["seconds_per_draw_measured"])

    cases: dict[str, dict[str, Any]] = {}
    floors: dict[str, dict[str, Any]] = {}
    by_width: dict[str, dict[str, Any]] = {}
    for key in keys:
        a = doc["stage_A_theta0"][key]
        worst_cell = min(range(len(a["p_sel"])), key=lambda k: a["p_sel"][k])
        floors[key] = gate_case(a["p_sel"][worst_cell], a["ci95_lower"][worst_cell],
                                a["ci95_upper"][worst_cell])
        floors[key]["cell"] = int(worst_cell)
        floors[key]["what_this_is"] = (
            "theta known exactly. The absolute floor on the cost, reported because it is the "
            "only number that is not a statement about the nuisance set, and NOT the gate: "
            "the null is composite, which is the whole reason the composition needs Dufour.")
        by_width[key] = {}
        for w in settings["box_half_widths"]:
            b = worst_over_box(doc, key, float(w))
            g = gate_case(b["p_sel"], b["ci95"][0], b["ci95"][1])
            g["attained_at"] = b
            by_width[key][f"w={w:g}"] = g
        cases[key] = by_width[key][f"w={headline_w:g}"]

    sv = session_verdict(cases, primary)
    headline = cases[f"{primary}|studentised"]
    p_head = headline["p_sel"]
    return {
        "gate": {
            "source": "audit/MMC_COMPOSITION_SPEC.md section 4, pre-registered in session G3",
            "cost_model": "E[draws] = M * N / min_theta p_sel, per nuisance value, MULTIPLIED",
            "threshold_draws": GATE_DRAWS,
            "declared_M": list(M_VALUES),
            "declared_N": list(N_VALUES),
            "declared_budget_draws": DECLARED_BUDGET_DRAWS,
            "declared_budget_source":
                "audit/S0_REPORT.md section 7: 'Forward simulation only, <=10^7 solves, no "
                "neural components | CPU-only holds; local, overnight'. The gate's own "
                "threshold is 1e8, an order of magnitude ABOVE this. Both are reported; the "
                "gate verdict is taken on the gate's threshold because that is the "
                "pre-registered one.",
            "which_p_sel":
                "minimum over the K selection cells and over the declared nuisance box, "
                "using the independently re-measured value at any refined point. Section 4 "
                "point 1: 'the cost is governed by min over theta of p_sel(theta) across the "
                "searched set, not by its value at a plausible theta'.",
            "headline_box_half_width": headline_w,
        },
        "scope_assumption_D14": doc["scope_assumption_D14"],
        "session_verdict": sv,
        "headline": {
            "case": f"{primary}|studentised",
            "p_sel": p_head,
            "p_sel_ci95": headline["p_sel_ci95"],
            "attained_at": headline["attained_at"],
            "verdict": headline["verdict"],
            "ci_decides_the_gate": headline["ci_decides_the_gate"],
            "expected_draws_range": [
                min(r["expected_draws"] for r in headline["corners"]),
                max(r["expected_draws"] for r in headline["corners"])],
            "ratio_to_gate_range": [
                min(r["expected_draws"] for r in headline["corners"]) / GATE_DRAWS,
                max(r["expected_draws"] for r in headline["corners"]) / GATE_DRAWS],
            "expected_draws_ci95_lower_range": [
                min(r["expected_draws_ci95_lower"] for r in headline["corners"]),
                max(r["expected_draws_ci95_lower"] for r in headline["corners"])],
            "wall_clock_hours_range": [
                min(r["expected_draws"] for r in headline["corners"]) * sec_per_draw / 3600.0,
                max(r["expected_draws"] for r in headline["corners"]) * sec_per_draw / 3600.0],
        },
        "wall_clock": {
            "seconds_per_draw_measured": sec_per_draw,
            "measured_on": doc["provenance"]["host"],
            "note":
                "One draw is one forward simulation plus one summary evaluation, timed over "
                "this run's own draws on a loaded machine. audit/GATES.md G4 records a "
                "profiling figure of roughly 0.14 s per run; the two are measured "
                "differently and the discrepancy is reported rather than reconciled.",
        },
        "cost_floor_theta_known": floors,
        "gate_by_box_width": by_width,
        "not_part_of_the_gate": {
            "what_this_is":
                "The gate prices ONE MMC test. A demonstration is many. These numbers are "
                "recorded because the operator needs them and are explicitly NOT part of the "
                "pre-registered verdict above.",
            "demonstration_multiplier_source":
                "audit/S0_REPORT.md section 7 prices the protocol at R=200 replicates x "
                "L=10 collinearity levels for ONE baseline.",
            "cost_of_R_replicated_tests": {
                str(r): [x * r for x in (
                    min(c["expected_draws"] for c in headline["corners"]),
                    max(c["expected_draws"] for c in headline["corners"]))]
                for r in (1, 10, 200)},
        },
    }


def fmt(x: float) -> str:
    """Render a cost. An infinite cost is a real answer -- no acceptances at all -- and is
    printed as the words rather than as a symbol, so a reader cannot mistake it for a bug."""
    return "unbounded" if not math.isfinite(x) else f"{x:.4g}"


def fmt_ratio(x: float) -> str:
    """As :func:`fmt`, but for a multiple of the gate, so that 'unbounded' does not acquire
    a stray multiplication sign."""
    return "unbounded" if not math.isfinite(x) else f"{x:.4g}x"


def table(g: dict[str, Any]) -> str:
    """The generated markdown table. No number in the audit prose is typed by hand (S11)."""
    L: list[str] = []
    ap = L.append
    ap("# The cost gate, measured")
    ap("")
    ap("Produced by `src/diagnostics/cost_gate.py` from the measured `results/p_sel.yaml`,")
    ap("which is produced by `src/diagnostics/p_sel.py`. This table and `results/cost_gate.yaml`")
    ap("are both generated; neither is edited by hand (S11).")
    ap("")
    sv = g["session_verdict"]
    ap(f"## SESSION VERDICT: **{sv['verdict']}**")
    ap("")
    ap(f"Primary assignment `{sv['primary_assignment']}`, per-variant verdicts "
       + ", ".join(f"`{k}` = **{v}**" for k, v in sv["per_variant_verdicts"].items()) + ".")
    ap("")
    ap(f"> {sv['rule']}")
    ap("")
    h = g["headline"]
    ap(f"**Headline case `{h['case']}`.** `p_sel` = **{h['p_sel']:.6g}** "
       f"(95% CI {h['p_sel_ci95'][0]:.6g} to {h['p_sel_ci95'][1]:.6g}), attained at "
       f"`{h['attained_at']['theta_key']}` in cell {h['attained_at']['cell']} "
       f"({h['attained_at']['counts']} of {h['attained_at']['n_draws']} draws, "
       f"{h['attained_at']['estimate_source']}).")
    ap("")
    ap(f"Expected draws for ONE test: **{fmt(h['expected_draws_range'][0])}** to "
       f"**{fmt(h['expected_draws_range'][1])}**, i.e. **{fmt_ratio(h['ratio_to_gate_range'][0])}** "
       f"to **{fmt_ratio(h['ratio_to_gate_range'][1])}** the pre-registered gate of "
       f"{g['gate']['threshold_draws']:.0g} draws. At the measured "
       f"{g['wall_clock']['seconds_per_draw_measured']:.4g} s per draw that is "
       f"{fmt(h['wall_clock_hours_range'][0])} to {fmt(h['wall_clock_hours_range'][1])} "
       f"core-hours.")
    ap("")
    ap(f"**The cost consistent with the data at the 95% level is at least "
       f"{fmt(h['expected_draws_ci95_lower_range'][0])} draws** and at least "
       f"{fmt(h['expected_draws_ci95_lower_range'][1])} at the most expensive declared "
       f"`(M, N)`. That lower bound is the number to read when the point estimate is "
       f"unbounded: it is what the measurement rules out, rather than what it asserts.")
    ap("")
    ap(f"`ci_decides_the_gate` = **{h['ci_decides_the_gate']}**.")
    ap("")
    ap("## 1. Every declared (M, N) corner, for every case")
    ap("")
    ap("`M` and `N` are the specification's own declared ranges, not this session's choices.")
    ap("The flip column is the `p_sel` at which that corner changes its answer, so the flag")
    ap("has a visible boundary rather than an implied one.")
    ap("")
    for key, case in g["gate_by_box_width"].items():
        c = case[f"w={g['gate']['headline_box_half_width']:g}"]
        ap(f"### `{key}` — headline box, `p_sel` = {c['p_sel']:.6g}, verdict **{c['verdict']}**")
        ap("")
        ap("| M | N | M*N | expected draws | CI95 draws | <= gate? | flips at p_sel | <= 1e7 budget? |")
        ap("|---|---|---|---|---|---|---|---|")
        for r in c["corners"]:
            lo, hi = r["expected_draws_ci95_lower"], r["expected_draws_ci95_upper"]
            ap(f"| {r['M']:g} | {r['N']} | {r['M_times_N']:g} | {fmt(r['expected_draws'])} | "
               f"{fmt(lo)} – {fmt(hi)} | {'yes' if r['passes'] else '**no**'} | "
               f"{r['p_sel_at_which_this_corner_flips']:.4g} | "
               f"{'yes' if r['within_declared_budget_1e7'] else '**no**'} |")
        ap("")
    ap("## 2. The cost as a function of how wide the nuisance set is")
    ap("")
    ap("`Omega_0` is a relative box on the five nuisance coordinates. A wider box can only")
    ap("lower `min p_sel`, so cost is monotone in width by construction; what the table shows")
    ap("is how fast.")
    ap("")
    ap("| case | box half-width | min p_sel | attained at | cell | verdict |")
    ap("|---|---|---|---|---|---|")
    for key, byw in g["gate_by_box_width"].items():
        for w, c in byw.items():
            a = c["attained_at"]
            ap(f"| `{key}` | {w} | {c['p_sel']:.6g} | `{a['theta_key']}` | {a['cell']} | "
               f"**{c['verdict']}** |")
    ap("")
    ap("## 3. The floor: what it would cost if theta were known")
    ap("")
    ap("Not the gate. The null is composite, which is the entire reason the composition needs")
    ap("Dufour's maximisation; this row is what the cost would be if it did not.")
    ap("")
    ap("| case | worst-cell p_sel at theta_0 | CI95 | expected draws | verdict |")
    ap("|---|---|---|---|---|")
    for key, f in g["cost_floor_theta_known"].items():
        lo = min(r["expected_draws"] for r in f["corners"])
        hi = max(r["expected_draws"] for r in f["corners"])
        ap(f"| `{key}` | {f['p_sel']:.6g} | {f['p_sel_ci95'][0]:.4g} – "
           f"{f['p_sel_ci95'][1]:.4g} | {fmt(lo)} – {fmt(hi)} | **{f['verdict']}** |")
    ap("")
    n = g["not_part_of_the_gate"]
    ap("## 4. Explicitly NOT part of the gate: what a demonstration would cost")
    ap("")
    ap(f"{n['what_this_is']}")
    ap("")
    ap(f"{n['demonstration_multiplier_source']}")
    ap("")
    ap("| replicated tests | expected draws (headline case) |")
    ap("|---|---|")
    for r, (lo, hi) in n["cost_of_R_replicated_tests"].items():
        ap(f"| {r} | {fmt(lo)} – {fmt(hi)} |")
    ap("")
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="cost gate (session G6, Phase 2)")
    ap.add_argument("--seed", type=int, default=20260820)
    ap.add_argument("--p-sel", type=str, default="results/p_sel.yaml")
    ap.add_argument("--out-dir", type=str, default="results",
                    help="overridden only for smoke runs, which must not write into results/")
    args = ap.parse_args(argv)
    started = now_iso()
    src = Path(args.p_sel)
    if not src.is_absolute():
        src = REPO / src
    dest = Path(args.out_dir)
    if not dest.is_absolute():
        dest = REPO / dest
    doc = yaml.safe_load(src.read_text(encoding="utf-8"))
    g = build(doc)
    g = {"provenance": header(script="src/diagnostics/cost_gate.py",
                              command="python -m src.diagnostics.cost_gate",
                              seed=args.seed, started=started),
         "measured_p_sel_from": args.p_sel,
         "p_sel_run_commit": doc["provenance"]["commit"],
         **g}
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "cost_gate.yaml").write_text(yaml.safe_dump(g, sort_keys=False, width=100),
                                         encoding="utf-8")
    (dest / "COST_GATE_TABLE.md").write_text(table(g), encoding="utf-8")
    print(f"session verdict: {g['session_verdict']['verdict']}")
    print(f"wrote {dest}/cost_gate.yaml and {dest}/COST_GATE_TABLE.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
