"""Figure 6 -- the MMC composition's acceptance probability collapsing to zero.

WHAT THIS FIGURE HAS TO SAY, AND WHAT IT MUST NOT
---------------------------------------------------
It is the paper's negative-result figure. It has to make one thing unambiguous: **at a known
parameter point the composition is comfortably affordable, and it stops being affordable at a
nuisance perturbation far smaller than anyone would call a nuisance.** Everything else on the
page is in service of that.

What it must NOT do is read as a cost curve with a budget caption. The obstruction is not
compute: at a relative half-width of 0.05 the acceptance probability is **zero acceptances in
100,000 draws**, so the rejection sampler does not terminate and no machine changes that.
The `p = 0` points are therefore drawn as **upper-bound markers, not as data points**, and
the axis is cut off below them rather than pretending the curve continues.

THE THREE THINGS MARKED ON IT
------------------------------
1. **The known-`theta` point**, `w = 0`, where the worst selection cell holds 23% of null
   draws. This is the PASS, and it is the only one in the whole analysis.
2. **The pre-registered cost gate.** `audit/MMC_COMPOSITION_SPEC.md` §4 registered
   `M x N / p_sel <= 1e8` before `p_sel` existed, with `M` and `N` given as *ranges*. So the
   gate is not one line but a **band**: above it every declared `(M, N)` corner passes, below
   it every corner fails, and inside it the gate is undecided by the specification's own
   declared numbers. Drawing it as a single line would hide that, and the SPLIT verdict is a
   fact about the specification worth showing.
3. **The measured upper bound at ±5%**, which is the number the cost floor of 2.6e9 draws is
   computed from.

THE SECOND AXIS IS THE MECHANISM
---------------------------------
The top axis carries the **measured** nuisance-shift-to-noise ratio at each swept width --
median `||E[z]||` over the design divided by `sqrt(d)`, the magnitude of a single null draw's
normalised discrepancy. It is not a rescaling of the bottom axis: the values are read from the
results file at the widths they were measured at. It is on the page because it is the
transportable part of the finding. The gate stops passing where that ratio crosses one, and
**that crossing is a one-line check anybody holding a different simulator can run before
attempting this composition on it.**

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
SERIES = (
    ("AAA|studentised", "adversarial", 0, 1.5, "AAA, studentised  (primary)"),
    ("BBB|studentised", "base", 0, 1.5, "BBB, studentised"),
    ("AAA|plain", "adversarial", 2, 0.9, "AAA, plain"),
    ("BBB|plain", "base", 2, 0.9, "BBB, plain"),
)

CAPTION = (
    "Acceptance probability of the composition's rejection sampler as a function of "
    "nuisance-parameter distortion magnitude. The plotted quantity is $p_{\\min}(w)$, the "
    "minimum over a 42-point design on a relative box of half-width $w$ about $\\theta_0$ and "
    "over the $K$ selection cells -- the quantity the specification's own cost model is "
    "governed by. Error bars are 95\\% Wilson intervals; downward triangles are widths at "
    "which no draw in 100{,}000 entered the observed cell, plotted at the interval's upper "
    "limit because they are bounds and not measurements. The shaded band is the "
    "pre-registered cost gate of $10^8$ simulator draws, which is a band rather than a line "
    "because the specification declares $M$ and $N$ as ranges: above it every declared "
    "$(M,N)$ corner passes, below it every corner fails, and inside it the gate is undecided "
    "by the specification's own numbers. At a known $\\theta$ the worst cell holds 23\\% of "
    "null draws and one test costs $4.2\\times10^5$ to $4.3\\times10^7$ draws -- a "
    "comfortable pass. The gate still passes at every corner only out to a $\\pm 0.5\\%$ box, "
    "and at $\\pm 5\\%$ the acceptance probability is zero to a 95\\% upper bound of "
    "$3.84\\times10^{-5}$: the sampler does not terminate, and the cost is unbounded rather "
    "than large. The top axis gives the measured ratio of nuisance shift to observation "
    "noise at each width; the gate stops passing where it crosses one, which is the "
    "transportable form of the finding."
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

    # The gate band: the p_sel at which the cheapest and dearest declared (M, N) corners flip.
    corners = gate["cost_floor_theta_known"][PRIMARY]["corners"]
    flips = prov.plotted(
        "gate corner flip points", [c["p_sel_at_which_this_corner_flips"] for c in corners],
        SRC_GATE, f"cost_floor_theta_known.{PRIMARY}.corners",
        transform=("p_sel_at_which_this_corner_flips of each declared (M,N) corner",
                   lambda cs: [c["p_sel_at_which_this_corner_flips"] for c in cs]))
    gate_lo, gate_hi = min(flips), max(flips)

    fig, ax = plt.subplots(figsize=(style.FIG_FULL, 3.05))
    ylo, yhi = 1.2e-6, 1.4

    ax.axhspan(gate_lo, gate_hi, color=style.FAINT, alpha=0.34, linewidth=0, zorder=0)
    ax.axhline(gate_lo, color=style.RULE, linewidth=0.7, linestyle=(0, (4, 1.6)), zorder=1.2)
    ax.axhline(gate_hi, color=style.RULE, linewidth=0.7, linestyle=(0, (4, 1.6)), zorder=1.2)

    for key, colour_key, dash_i, lw, label in SERIES:
        p0 = prov.plotted(f"{key} p at theta_0",
                          [doc["anchor_theta0"][key]["reported_min"]["p_sel"]], SRC,
                          f"anchor_theta0.{key}.reported_min.p_sel")[0]
        ps = prov.plotted(
            f"{key} p_min per width",
            [e["by_key"][key]["reported_min"]["p_sel"] for e in doc["per_width"]], SRC,
            "per_width",
            transform=(f"reported_min.p_sel for {key} of each swept row",
                       lambda rs, k=key: [r["by_key"][k]["reported_min"]["p_sel"]
                                          for r in rs]))
        hi_ci = [doc["anchor_theta0"][key]["reported_min"]["ci95"][1]] + [
            e["by_key"][key]["reported_min"]["ci95"][1] for e in doc["per_width"]]
        lo_ci = [doc["anchor_theta0"][key]["reported_min"]["ci95"][0]] + [
            e["by_key"][key]["reported_min"]["ci95"][0] for e in doc["per_width"]]
        xs = np.array([0.0] + list(widths))
        vals = np.array([p0] + list(ps))
        live = vals > 0
        c = style.FAMILY[colour_key]

        ax.plot(xs[live], vals[live], color=c, linewidth=lw,
                dashes=style.DASHES[dash_i][1] or (), marker="o", markersize=3.2,
                markeredgewidth=0, label=label, zorder=4 if lw > 1 else 3,
                alpha=1.0 if lw > 1 else 0.75)
        if key == PRIMARY:
            ax.errorbar(xs[live], vals[live],
                        yerr=[vals[live] - np.array(lo_ci)[live],
                              np.array(hi_ci)[live] - vals[live]],
                        fmt="none", ecolor=c, elinewidth=0.8, capsize=1.6, zorder=4)
        for x, hi in zip(xs[~live], np.array(hi_ci)[~live]):
            ax.plot([x], [hi], marker="v", markersize=4.2, markerfacecolor=style.PANEL,
                    markeredgecolor=c, markeredgewidth=0.9, zorder=5)

    # ---- the three marks -----------------------------------------------------------------
    p_known = doc["anchor_theta0"][PRIMARY]["reported_min"]["p_sel"]
    ax.annotate(f"known $\\theta$: $p={p_known:.4g}$\n(the only PASS)",
                xy=(0.0, p_known), xytext=(0.0035, 0.62),
                fontsize=style.SIZE_SMALL, color=style.INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", lw=0.5, color=style.INK, shrinkA=1, shrinkB=3))
    w005 = next(e for e in doc["per_width"] if e["width"] == 0.05)
    bound = w005["by_key"][PRIMARY]["reported_min"]["ci95"][1]
    ax.annotate(f"$\\pm5\\%$: 0 acceptances in 100,000 draws.\n"
                f"The triangles are bounds ($\\leq${bound:.2e}), not values.",
                xy=(0.05, bound), xytext=(0.0505, 1.6e-6),
                fontsize=style.SIZE_SMALL, color=style.INK, ha="right", va="bottom",
                arrowprops=dict(arrowstyle="-", lw=0.5, color=style.INK, shrinkA=1, shrinkB=4))
    ax.annotate("pre-registered gate: $M\\!\\times\\!N/p \\leq 10^{8}$\n"
                "(band: undecided by the declared $M$, $N$)",
                xy=(0.0335, np.sqrt(gate_lo * gate_hi)), ha="center", va="center",
                fontsize=style.SIZE_SMALL, color=style.RULE)
    ax.text(0.0505, gate_hi * 1.6, "every declared corner PASSES", ha="right", va="bottom",
            fontsize=style.SIZE_SMALL, color=style.RULE)
    ax.text(0.0505, gate_lo / 1.8, "every declared corner FAILS", ha="right", va="top",
            fontsize=style.SIZE_SMALL, color=style.RULE)

    ax.set_yscale("log")
    ax.set_xlim(-0.0018, 0.0525)
    ax.set_ylim(ylo, yhi)
    ax.set_xlabel("relative nuisance half-width $w$ on all five coordinates "
                  r"($\beta,\gamma,\rho,I_0,\sigma_{\mathrm{obs}}$)")
    ax.set_ylabel("acceptance probability $p_{\\min}(w)$\n(worst cell, worst design point)")
    handles, labels = ax.get_legend_handles_labels()

    # The first measured width at which the nuisance shift exceeds the observation noise.
    # Measured, not interpolated: it is a swept width and its ratio is a recorded number.
    cross_i = next(i for i, s in enumerate(shift) if s > 1.0)
    ax.axvline(widths[cross_i], color=style.RULE, linewidth=0.7, linestyle=(0, (1, 1.4)),
               zorder=1.1)
    ax.annotate("nuisance shift first exceeds\nobservation noise",
                xy=(widths[cross_i], 1.6e-6), xytext=(3, 0), textcoords="offset points",
                ha="left", va="bottom", fontsize=style.SIZE_SMALL, color=style.RULE)

    top = ax.secondary_xaxis("top")
    # Only the widths far enough apart to carry a legible label; the omitted ones are the
    # three smallest, where the ratio is well under 1 and nothing turns on its exact value.
    shown = [i for i, w in enumerate(widths) if w >= 0.005]
    top.set_xticks([widths[i] for i in shown])
    top.set_xticklabels([f"{shift[i]:.2g}" for i in shown], fontsize=style.SIZE_SMALL)
    top.set_xlabel(r"measured nuisance shift $\div$ observation noise, "
                   r"median $\|E[z]\|/\sqrt{d}$", fontsize=style.SIZE_SMALL, labelpad=2)
    top.tick_params(length=2)

    fig.legend(handles, labels, loc="lower center", ncol=4, fontsize=style.SIZE_TICK,
               handlelength=1.8, columnspacing=1.5, bbox_to_anchor=(0.5, 0.0))
    fig.subplots_adjust(left=0.115, right=0.995, bottom=0.235, top=0.855)

    out = style.save(fig, REPO / STEM, script=SCRIPT)
    plt.close(fig)
    prov.note(
        "The top axis is NOT a rescaling of the bottom one. Its tick positions are the swept "
        "widths and its labels are the shift-to-noise ratios measured at those widths, read "
        "from the results file. The relation is close to linear but not exactly so (about 153 "
        "per unit width at the bottom of the range and 168 at the top), and a linear "
        "secondary axis would have been wrong at the top end.")
    prov.note(
        "Widths at which the acceptance probability is exactly zero are drawn as downward "
        "triangles at the 95% Wilson upper limit and are joined to nothing. They are bounds. "
        "Joining them into the curve would draw a cost where the finding is non-termination.")
    prov.note(
        "The gate band's edges are the p_sel at which the cheapest and dearest declared (M,N) "
        f"corners flip, {min(flips):.5g} and {max(flips):.5g}, read from "
        f"{SRC_GATE} rather than recomputed here.")
    prov.note(
        "docs/DECISIONS.md D-16 dropped the composition before the sweep behind this figure "
        "was designed. Nothing on this page re-prices that decision, and the widths at which "
        "the gate would have passed are drawn because they make the negative result specific, "
        "not because they reopen it.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
