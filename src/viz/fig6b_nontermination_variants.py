"""Appendix companion to fig6_nontermination -- the plain-vs-studentised comparison.

Session G11 (T2-8): the main-text figure was split to show the primary case (AAA,
studentised) alone; this figure carries the comparison across both family assignments and
both studentisation variants that the main-text panel dropped, so the robustness check is
still in the paper, in the appendix rather than crowding the headline panel.

Sources: ``results/boundary_sweep.yaml``. Nothing is computed here.
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
STEM = "figures/fig6b_nontermination_variants"
SCRIPT = "src/viz/fig6b_nontermination_variants.py"

PRIMARY = "AAA|studentised"
SERIES = (
    ("AAA|studentised", "adversarial", 0, 1.5, "AAA, studentised  (primary; main text)"),
    ("BBB|studentised", "base", 0, 1.5, "BBB, studentised"),
    ("AAA|plain", "adversarial", 2, 0.9, "AAA, plain"),
    ("BBB|plain", "base", 2, 0.9, "BBB, plain"),
)

CAPTION = (
    "Acceptance probability $p_{\\min}(w)$ across all four (family assignment, "
    "studentisation variant) combinations the composition was measured under, on the same "
    "42-point design and axes as Figure~\\ref{fig:nontermination}'s left panel. The primary "
    "case (AAA, studentised) is reproduced here for comparison; the other three collapse the "
    "same way, generally sooner. Open triangles are 95\\% Wilson upper bounds at zero "
    "measured acceptances, not values, and are joined to nothing."
)


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["FAMILY"])
    prov = vp.FigureProvenance("fig6b_nontermination_variants", script=SCRIPT)
    doc = prov.source(SRC)

    widths = prov.plotted("swept half-widths", [e["width"] for e in doc["per_width"]], SRC,
                          "per_width",
                          transform=("width of each swept row",
                                     lambda rs: [r["width"] for r in rs]))

    fig, ax = plt.subplots(figsize=(style.FIG_FULL * 0.62, 2.9))
    ylo, yhi = 1.2e-6, 1.4

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
        xs = np.array([0.0] + list(widths))
        vals = np.array([p0] + list(ps))
        live = vals > 0
        c = style.FAMILY[colour_key]

        ax.plot(xs[live], vals[live], color=c, linewidth=lw,
                dashes=style.DASHES[dash_i][1] or (), marker="o", markersize=3.2,
                markeredgewidth=0, label=label, zorder=4 if lw > 1 else 3,
                alpha=1.0 if lw > 1 else 0.75)
        for x, hi in zip(xs[~live], np.array(hi_ci)[~live]):
            ax.plot([x], [hi], marker="v", markersize=4.2, markerfacecolor=style.PANEL,
                    markeredgecolor=c, markeredgewidth=0.9, zorder=5)

    ax.set_yscale("log")
    ax.set_xlim(-0.0018, 0.0525)
    ax.set_ylim(ylo, yhi)
    ax.set_xlabel("relative nuisance half-width $w$", fontsize=style.SIZE_LABEL)
    ax.set_ylabel("$p_{\\min}(w)$  (worst cell, worst design point)", fontsize=style.SIZE_LABEL)
    ax.tick_params(labelsize=style.SIZE_LABEL)
    ax.legend(loc="upper right", fontsize=style.SIZE_LABEL, borderpad=0.3, handlelength=1.8)
    fig.subplots_adjust(left=0.16, right=0.98, bottom=0.16, top=0.98)

    out = style.save(fig, REPO / STEM, script=SCRIPT)
    plt.close(fig)
    prov.note(
        "Companion to fig6_nontermination (T2-8): carries the plain-vs-studentised and "
        "AAA-vs-BBB comparison the main-text panel dropped in favour of the primary case "
        "alone plus a dedicated mechanism panel.")
    prov.note(
        "Widths at which the acceptance probability is exactly zero are drawn as open "
        "downward triangles at the 95% Wilson upper limit and are joined to nothing.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
