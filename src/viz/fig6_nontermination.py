"""Figure -- the MMC composition's acceptance probability collapsing to zero.

REDESIGNED session G11 (T2-8), split into two panels per an external adversarial review
------------------------------------------------------------------------------------------
The prior single-panel version carried four series (two family assignments x two
studentisation variants) plus a secondary top axis for the shift-to-noise ratio on the same
plot. The review found this asked one panel to do two jobs -- "does the gate pass" and "why
does the gate stop passing" -- and asked for them separated:

* **Left panel: $p_{\\min}(w)$ for the primary case only** (AAA, studentised), with Wilson
  interval bars and the pre-registered cost gate as reference lines. The plain-vs-studentised
  comparison this drops is not lost -- it moves to a companion appendix figure
  (``fig6b_nontermination_variants.pdf``), which is where a reader who wants the robustness
  check across studentisation choices looks, rather than crowding the headline panel.
* **Right panel: the mechanism**, the measured nuisance-shift-to-noise ratio against $w$
  directly (no longer a secondary axis squeezed onto the left panel), with a horizontal
  reference line at ratio $=1$ and a vertical dashed line at the width where the measured
  ratio first crosses it -- which is also where the gate (left panel) stops passing.

Upper-bound points (zero acceptances in 100,000 draws) are open triangles with their own
explicit legend entry, joined to nothing, per the review's request that no line imply
continuity where nothing was measured. Every text element on this figure is set at 8pt or
larger -- the venue's general floor is 6pt (``style.SIZE_SMALL``), but this figure's own
density earned a stricter one from the review, so ``style.SIZE_LABEL`` (8pt) is the smallest
size used anywhere below.

WHAT THIS FIGURE HAS TO SAY, AND WHAT IT MUST NOT
---------------------------------------------------
Unchanged from the single-panel version. It has to make one thing unambiguous: at a known
parameter point the composition is comfortably affordable, and it stops being affordable at a
nuisance perturbation far smaller than anyone would call a nuisance. The `p = 0` points are
upper-bound markers, not data points, and the left axis is not extended below them to imply a
value that was not measured.

Sources: ``results/boundary_sweep.yaml`` for the sweep and ``results/cost_gate.yaml`` for the
gate's own corner flip points. Nothing is computed here.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from . import provenance as vp
from . import style

REPO = Path(__file__).resolve().parents[2]
SRC = "results/boundary_sweep.yaml"
SRC_GATE = "results/cost_gate.yaml"
STEM = "figures/fig6_nontermination"
SCRIPT = "src/viz/fig6_nontermination.py"

PRIMARY = "AAA|studentised"

CAPTION = (
    "Left: acceptance probability $p_{\\min}(w)$, primary case (AAA, studentised), over the "
    "pre-registered 42-point design (32 corners $+$ 10 axis endpoints of the box of "
    "half-width $w$ about $\\theta_0$) and the $K=3$ cells; 95\\% Wilson bars, open triangle "
    "at $w=0.05$ an upper bound joined to nothing. Shaded band: cost gate "
    "$M \\times N / p \\leq 10^8$, a band since $M \\in \\{10^3, 10^4\\}$, "
    "$N \\in \\{99, 999\\}$ are declared as ranges. Plain and BBB variants: "
    "Figure~\\ref{fig:nontermination-variants} (Appendix~\\ref{sec:appendix}). Right: the "
    "mechanism -- measured shift-to-noise ratio vs. $w$; horizontal line at ratio $=1$, "
    "vertical dashed line where it is first crossed, coinciding with where the left panel's "
    "gate stops passing."
)


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["FAMILY"])
    prov = vp.FigureProvenance("fig6_nontermination", script=SCRIPT)
    doc = prov.source(SRC)
    gate = prov.source(SRC_GATE)

    widths = prov.plotted("swept half-widths", [e["width"] for e in doc["per_width"]], SRC,
                          "per_width",
                          transform=("width of each swept row",
                                     lambda rs: [r["width"] for r in rs]))
    shift = prov.plotted(
        "measured shift-to-noise ratio",
        [e["nuisance_shift_norm_of_mean_z"]["median_over_noise"] for e in doc["per_width"]],
        SRC, "per_width",
        transform=("median ||E[z]|| / sqrt(d) of each swept row",
                   lambda rs: [r["nuisance_shift_norm_of_mean_z"]["median_over_noise"]
                               for r in rs]))

    corners = gate["cost_floor_theta_known"][PRIMARY]["corners"]
    flips = prov.plotted(
        "gate corner flip points", [c["p_sel_at_which_this_corner_flips"] for c in corners],
        SRC_GATE, f"cost_floor_theta_known.{PRIMARY}.corners",
        transform=("p_sel_at_which_this_corner_flips of each declared (M,N) corner",
                   lambda cs: [c["p_sel_at_which_this_corner_flips"] for c in cs]))
    gate_lo, gate_hi = min(flips), max(flips)

    p0 = prov.plotted(f"{PRIMARY} p at theta_0",
                      [doc["anchor_theta0"][PRIMARY]["reported_min"]["p_sel"]], SRC,
                      f"anchor_theta0.{PRIMARY}.reported_min.p_sel")[0]
    ps = prov.plotted(
        f"{PRIMARY} p_min per width",
        [e["by_key"][PRIMARY]["reported_min"]["p_sel"] for e in doc["per_width"]], SRC,
        "per_width",
        transform=(f"reported_min.p_sel for {PRIMARY} of each swept row",
                   lambda rs: [r["by_key"][PRIMARY]["reported_min"]["p_sel"] for r in rs]))
    hi_ci = [doc["anchor_theta0"][PRIMARY]["reported_min"]["ci95"][1]] + [
        e["by_key"][PRIMARY]["reported_min"]["ci95"][1] for e in doc["per_width"]]
    lo_ci = [doc["anchor_theta0"][PRIMARY]["reported_min"]["ci95"][0]] + [
        e["by_key"][PRIMARY]["reported_min"]["ci95"][0] for e in doc["per_width"]]
    xs = np.array([0.0] + list(widths))
    vals = np.array([p0] + list(ps))
    live = vals > 0
    c = style.FAMILY["adversarial"]

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(style.FIG_FULL, 2.35))

    # ---- left panel: p_min(w), primary case only ------------------------------------------
    ylo, yhi = 1.2e-6, 1.4
    axL.axhspan(gate_lo, gate_hi, color=style.FAINT, alpha=0.34, linewidth=0, zorder=0)
    axL.axhline(gate_lo, color=style.RULE, linewidth=0.7, linestyle=(0, (4, 1.6)), zorder=1.2)
    axL.axhline(gate_hi, color=style.RULE, linewidth=0.7, linestyle=(0, (4, 1.6)), zorder=1.2)
    axL.plot(xs[live], vals[live], color=c, linewidth=1.5, marker="o", markersize=3.6,
             markeredgewidth=0, label="$p_{\\min}(w)$, measured", zorder=4)
    axL.errorbar(xs[live], vals[live],
                yerr=[vals[live] - np.array(lo_ci)[live], np.array(hi_ci)[live] - vals[live]],
                fmt="none", ecolor=c, elinewidth=0.9, capsize=1.8, zorder=4)
    first_bound = True
    for x, hi in zip(xs[~live], np.array(hi_ci)[~live]):
        axL.plot([x], [hi], marker="v", markersize=5.2, markerfacecolor=style.PANEL,
                 markeredgecolor=c, markeredgewidth=1.0, zorder=5,
                 label="upper bound (0 acceptances in 100,000)" if first_bound else None)
        first_bound = False

    p_known = doc["anchor_theta0"][PRIMARY]["reported_min"]["p_sel"]
    axL.annotate(f"known $\\theta$: $p={p_known:.3g}$\n(the only PASS)",
                xy=(0.0, p_known), xytext=(0.004, 0.5),
                fontsize=style.SIZE_LABEL, color=style.INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.5, color=style.INK, shrinkA=1, shrinkB=3))
    w005 = next(e for e in doc["per_width"] if e["width"] == 0.05)
    bound = w005["by_key"][PRIMARY]["reported_min"]["ci95"][1]
    axL.annotate(f"$\\leq${bound:.1e}",
                xy=(0.05, bound), xytext=(0.0345, bound * 4.2),
                fontsize=style.SIZE_LABEL, color=style.INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.5, color=style.INK, shrinkA=1, shrinkB=4))
    axL.text(0.051, gate_hi * 1.7, "PASSES", ha="right", va="bottom",
             fontsize=style.SIZE_LABEL, color=style.RULE)
    axL.text(0.051, gate_lo / 2.0, "FAILS", ha="right", va="top",
             fontsize=style.SIZE_LABEL, color=style.RULE)
    axL.text(0.0018, np.sqrt(gate_lo * gate_hi), "gate:\n$MN/p\\!\\leq\\!10^8$",
             ha="left", va="center", fontsize=style.SIZE_LABEL, color=style.RULE, linespacing=1.2)

    axL.set_yscale("log")
    axL.set_xlim(-0.0018, 0.0535)
    axL.set_ylim(ylo, yhi)
    axL.set_xlabel("relative nuisance half-width $w$", fontsize=style.SIZE_LABEL)
    axL.set_ylabel("$p_{\\min}(w)$  (worst cell, worst design point)",
                   fontsize=style.SIZE_LABEL)
    axL.set_title("(a)  acceptance probability, primary case", fontsize=style.SIZE_TITLE, pad=3)
    axL.tick_params(labelsize=style.SIZE_LABEL)
    axL.legend(loc="lower left", fontsize=style.SIZE_LABEL, borderpad=0.3, handlelength=1.6,
              bbox_to_anchor=(-0.02, -0.03))

    # ---- right panel: the mechanism ---------------------------------------------------------
    axR.plot(widths, shift, color=style.INK, linewidth=1.3, marker="s", markersize=3.6,
             markeredgewidth=0, zorder=3)
    axR.axhline(1.0, color=style.RULE, linewidth=0.9, linestyle=(0, (4, 1.6)), zorder=1)
    axR.text(0.0505, 1.35, "shift $=$ noise", ha="right", va="bottom",
             fontsize=style.SIZE_LABEL, color=style.RULE)
    cross_i = next(i for i, s in enumerate(shift) if s > 1.0)
    axR.axvline(widths[cross_i], color=style.RULE, linewidth=0.7, linestyle=(0, (1, 1.4)),
               zorder=1.1)
    axR.annotate("measured crossing --\ngate stops passing here",
                xy=(widths[cross_i], max(shift) * 0.55),
                xytext=(widths[cross_i] + 0.004, max(shift) * 0.42),
                fontsize=style.SIZE_LABEL, color=style.RULE, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.5, color=style.RULE, shrinkA=1, shrinkB=3))
    axR.set_xlim(-0.0018, 0.0535)
    axR.set_ylim(0, max(shift) * 1.12)
    axR.set_xlabel("relative nuisance half-width $w$", fontsize=style.SIZE_LABEL)
    axR.set_ylabel("shift $\\div$ noise,  median $\\|E[z]\\|/\\sqrt{d}$",
                   fontsize=style.SIZE_LABEL)
    axR.set_title("(b)  why: nuisance shift vs. observation noise",
                  fontsize=style.SIZE_TITLE, pad=3)
    axR.tick_params(labelsize=style.SIZE_LABEL)

    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.19, top=0.90, wspace=0.32)

    out = style.save(fig, REPO / STEM, script=SCRIPT)
    plt.close(fig)
    prov.note(
        "Split into two panels in session G11 (T2-8): the prior single-panel version's "
        "plain-vs-studentised comparison and secondary top axis are separated out, the former "
        "to fig6b_nontermination_variants (appendix), the latter to this figure's own right "
        "panel with its own primary x-axis rather than a rescaled secondary one.")
    prov.note(
        "Widths at which the acceptance probability is exactly zero are drawn as an open "
        "downward triangle at the 95% Wilson upper limit, with its own legend entry, and are "
        "joined to nothing. They are bounds, not measurements.")
    prov.note(
        "The gate band's edges are the p_sel at which the cheapest and dearest declared (M,N) "
        f"corners flip, {min(flips):.5g} and {max(flips):.5g}, read from "
        f"{SRC_GATE} rather than recomputed here.")
    prov.note(
        "docs/DECISIONS.md D-16 dropped the composition before the sweep behind this figure "
        "was designed. Nothing on this page re-prices that decision.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
