"""The simulator's structure, and where each distortion family acts -- main-text figure.

REDUCED FOR THE MAIN TEXT -- session G11, T1-4
------------------------------------------------
An external adversarial review of the paper found that the main text uses "the six columns"
and specific component names (progression, observation) before ever defining them for a
main-text reader; the only figure that defines them lived in the appendix. This is that
figure, reduced and moved into Section 4 before its first reference. Two changes from the
appendix version this replaces:

* **The three-distortion-family section is now a compact 3x2 table** (rows: the three
  components; columns: base family, adversarial family) instead of the previous six lines of
  formula-plus-description text. The descriptive annotations ("a prevalence nonlinearity",
  "a timing distortion", ...) move to the caption's prose, which already carried most of this
  content, rather than being dropped.
* **The two footnote-style qualification paragraphs are removed from the figure** and their
  content folded into Section 3's prose instead (T2-8), which is where a scope qualification
  belongs rather than in small print under a diagram.

The figure is roughly a third shorter as a result, appropriate for main-text real estate under
a 5-page limit. Nothing about what it draws is invented for the reduction: every number and
formula is the same transcription from `src/simulators/sir3.py` the appendix version used.

BUILT FROM THE CODE, NOT FROM A MEMORY OF IT
----------------------------------------------
Every expression on this diagram is transcribed from ``src/simulators/sir3.py`` and
``src/simulators/summaries.py`` as they stand, not from an earlier session's description of
them. Three things a report might have got wrong and the code settles:

* **There is no explicit ``R`` compartment.** The integrated state is ``(S, I, C)`` with ``C``
  cumulative infections; removal leaves ``I`` and is not tracked further, because nothing
  downstream observes it. Drawing an ``R`` box would be drawing a variable that does not
  exist.
* **The delay kernel and the noise scale are held fixed under the observation distortion.**
  Only the reporting fraction moves. That is a real limitation of the design, recorded in the
  module docstring and in the results files, and the diagram marks it rather than smoothing
  it over.
* **The adversarial transmission and progression families are sign-aligned on purpose**, so
  that both move `R_0 = beta/gamma` in the same direction rather than in opposite ones.

WHAT IS DRAWN, AND WHAT IS DELIBERATELY NOT
---------------------------------------------
The deterministic core, the observation chain, the three distortion insertion points with
both declared family forms at each, and the three summary maps. **The numerical method is
named but not drawn** -- fixed-step RK4 at 24 substeps per day is a fact about the
implementation with real consequences (an adaptive solver would destroy the finite
difference; ``sir3.py`` says so), so it appears as a label on the integrator rather than as a
box of its own.

This figure reads no ``results/`` file. It has no provenance sidecar entry for plotted data
because it plots none; the sidecar records the source files it was transcribed from instead.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from . import provenance as vp
from . import style

REPO = Path(__file__).resolve().parents[2]
STEM = "figures/fig2_simulator"
SCRIPT = "src/viz/fig2_simulator.py"

CAPTION = (
    "Structure of the three-component compartmental simulator, and the point at which each "
    "distortion family acts. The deterministic core integrates $(S, I, C)$ by fixed-step "
    "RK4 at 24 substeps per day over a 120-day window; $C$ is cumulative infections, and "
    "daily true incidence is its first difference. There is no explicit removed compartment "
    "because nothing downstream observes one. The observation chain convolves true incidence "
    "with a gamma reporting-delay kernel (mean 3 days, shape 3, support 21 days), scales by "
    "the reporting fraction $\\rho$, and applies multiplicative lognormal noise at "
    "$\\sigma = 0.15$; the noise must be continuous and multiplicative rather than "
    "count-valued, or the common-random-numbers finite difference the diagnostic depends on "
    "does not exist. Each of the three components carries one one-parameter distortion "
    "family $\\delta_k(\\cdot\\,;\\eta_k)$ with $\\delta_k(\\cdot\\,;0)$ bit-identical to the "
    "base simulator (asserted bit-for-bit; $\\eta_k$ in units of a fixed 10\\% relative "
    "deformation), and two family sets are declared: a base set of three qualitatively "
    "different deformations -- a saturating-incidence nonlinearity on transmission, a "
    "mean-centred hazard drift (a timing distortion) on progression, and a pure amplitude "
    "error on observation -- and an adversarial set designed so that all three columns "
    "perturb the same feature of an epidemic curve, its observed exponential growth rate. "
    "Under the observation family only the reporting fraction moves -- the delay kernel and "
    "the noise scale are held at base values, which is a stated limitation of the design and "
    "not an omission from this diagram."
)

BOX = dict(boxstyle="round,pad=0.32,rounding_size=0.10", linewidth=0.7)


def box(ax, x, y, w, h, text, *, ec, fc="none", fs=None, ha="center"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, edgecolor=ec, facecolor=fc, zorder=2,
                                mutation_scale=1.0, **BOX))
    ax.text(x + w / 2 if ha == "center" else x + 0.06, y + h / 2, text,
            ha=ha, va="center", fontsize=fs or style.SIZE_SMALL, color=style.INK,
            zorder=3, linespacing=1.35)


def arrow(ax, xy0, xy1, *, colour=None, style_="-|>", lw=0.8, rad=0.0):
    ax.add_patch(FancyArrowPatch(xy0, xy1, arrowstyle=style_, linewidth=lw,
                                 color=colour or style.INK, mutation_scale=6.5,
                                 shrinkA=1.5, shrinkB=1.5,
                                 connectionstyle=f"arc3,rad={rad}", zorder=2))


#: Reduction scale (T1-4): the appendix version used a 100-unit-tall canvas over 4.00in
#: (0.04 in/unit). Zones A and B below keep every original coordinate multiplied by this
#: factor, so their PHYSICAL size on the page -- box heights, gaps, font-to-box ratios -- is
#: unchanged; what shrinks is how much total canvas the figure spans, because zone D is
#: dropped and zone C is replaced by a table roughly a third the height of the prose it
#: replaces. The same 0.04 in/unit scale is kept for the new canvas height, so this factor
#: is the only number that needed choosing.
SCALE = 0.625


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["COMPONENT"])
    prov = vp.FigureProvenance("fig2_simulator", script=SCRIPT)

    ymax = 62.5
    fig, ax = plt.subplots(figsize=(style.FIG_FULL, ymax * 0.04))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, ymax)
    ax.axis("off")

    ct, cp, co = (style.COMPONENT["transmission"], style.COMPONENT["progression"],
                  style.COMPONENT["observation"])
    s = SCALE

    # ---- zone A: the deterministic core ---------------------------------------------------
    ax.text(0.0, 99.0 * s, "DETERMINISTIC CORE   —   fixed-step RK4, 24 substeps/day, "
                           "$T=120$ days, $N=10^5$", ha="left", va="top",
            fontsize=style.SIZE_TICK, color=style.RULE)
    box(ax, 1, 86 * s, 8, 8 * s, "$S$", ec=style.INK, fs=style.SIZE_LABEL)
    box(ax, 23, 86 * s, 8, 8 * s, "$I$", ec=style.INK, fs=style.SIZE_LABEL)
    box(ax, 45, 86 * s, 13, 8 * s, "$C$\ncumulative", ec=style.INK)
    box(ax, 68, 86 * s, 31, 8 * s, "daily true incidence $=\\mathrm{diff}(C)$\nnever observed",
        ec=style.INK)
    arrow(ax, (9, 90 * s), (23, 90 * s))
    arrow(ax, (31, 90 * s), (45, 90 * s))
    arrow(ax, (58, 90 * s), (68, 90 * s))
    ax.text(16.0, 91.0 * s, "incidence", ha="center", va="bottom", fontsize=style.SIZE_SMALL,
            color=ct)
    arrow(ax, (27, 86 * s), (27, 79 * s), colour=cp)
    ax.text(28.5, 81.5 * s, "removal (not tracked further)", ha="left", va="center",
            fontsize=style.SIZE_SMALL, color=cp)
    ax.plot([16.0], [90.0 * s], marker="o", markersize=4.2, color=ct,
            markeredgecolor=style.PANEL, markeredgewidth=0.6, zorder=6)
    ax.plot([27.0], [84.0 * s], marker="o", markersize=4.2, color=cp,
            markeredgecolor=style.PANEL, markeredgewidth=0.6, zorder=6)

    # ---- zone B: the observation chain ----------------------------------------------------
    ax.text(0.0, 75.0 * s, "OBSERVATION COMPONENT", ha="left", va="top",
            fontsize=style.SIZE_TICK, color=style.RULE)
    box(ax, 1, 62 * s, 21, 8 * s, "delay kernel\ngamma, mean 3 d, shape 3", ec=co)
    box(ax, 25, 62 * s, 15, 8 * s, "reporting fraction\n$\\rho = 0.4$", ec=co)
    box(ax, 43, 62 * s, 24, 8 * s, "lognormal noise\n$\\exp(\\sigma z-\\sigma^2/2)$, "
                                   "$\\sigma=0.15$", ec=co)
    box(ax, 70, 62 * s, 29, 8 * s, "reported series $y_t$\n$\\rightarrow$ summaries $s(y)$",
        ec=style.INK)
    for a, b in ((22, 25), (40, 43), (67, 70)):
        arrow(ax, (a, 66 * s), (b, 66 * s))
    arrow(ax, (84, 86 * s), (84, 70 * s))
    ax.plot([32.5], [62.0 * s], marker="o", markersize=4.2, color=co,
            markeredgecolor=style.PANEL, markeredgewidth=0.6, zorder=6)
    ax.text(0.0, 59.5 * s,
            "a CONTINUOUS multiplicative layer is required (a count-valued one is not "
            "differentiable under CRN, kept as a negative control)",
            ha="left", va="top", fontsize=style.SIZE_SMALL, color=style.RULE)

    # ---- zone C: the three distortion families, as a compact 3x2 table --------------------
    table_top, table_bottom = 26.5, 1.5
    col_label, col_base, col_adv = 0.0, 29.0, 65.0
    ax.plot([0, 100], [table_top + 3.0, table_top + 3.0], color=style.FAINT,
            linewidth=0.6, zorder=1)
    ax.text(0.0, table_top + 4.3, "THE THREE DISTORTION FAMILIES   —   one one-parameter "
                                  "family per component, in two declared sets", ha="left",
            va="bottom", fontsize=style.SIZE_TICK, color=style.RULE)
    ax.text(col_base, table_top + 1.2, "base family", ha="left", va="bottom",
            fontsize=style.SIZE_TICK, color=style.INK)
    ax.text(col_adv, table_top + 1.2, "adversarial family", ha="left", va="bottom",
            fontsize=style.SIZE_TICK, color=style.INK)
    ax.plot([0, 100], [table_top, table_top], color=style.FAINT, linewidth=0.6, zorder=1)
    for x in (col_base - 2.0, col_adv - 2.0):
        ax.plot([x, x], [table_bottom, table_top], color=style.FAINT, linewidth=0.6, zorder=1)

    rows = (
        (ct, r"$\eta_1$" "\nTRANSM.",
         r"$\beta S I/N \,\div\,$" "\n" r"$[1+\eta_1 (I/N)/p_{\mathrm{ref}}]$",
         r"$\beta \rightarrow \beta\, e^{\eta_1}$"),
        (cp, r"$\eta_2$" "\nPROGR.",
         r"$\gamma \rightarrow \gamma\, e^{\eta_2 (t/T - 1/2)}$",
         r"$\gamma \rightarrow \gamma\, e^{-\eta_2}$"),
        (co, r"$\eta_3$" "\nOBS.",
         r"$\rho \rightarrow \rho\, e^{\eta_3}$",
         r"$\rho \rightarrow \rho\, e^{\eta_3 (t/T - 1/2)}$"),
    )
    row_h = (table_top - table_bottom) / 3.0
    for i, (colour, label, base_txt, adv_txt) in enumerate(rows):
        y = table_top - row_h * (i + 0.5)
        if i > 0:
            ax.plot([0, 100], [table_top - row_h * i] * 2, color=style.FAINT,
                    linewidth=0.4, zorder=1)
        ax.plot([1.2], [y], marker="s", markersize=4.5, color=colour, zorder=5)
        ax.text(4.0, y, label, ha="left", va="center", fontsize=style.SIZE_SMALL,
                color=colour, zorder=5, linespacing=1.2)
        ax.text(col_base, y, base_txt, ha="left", va="center", fontsize=style.SIZE_TICK,
                color=style.INK, zorder=5, linespacing=1.3)
        ax.text(col_adv, y, adv_txt, ha="left", va="center", fontsize=style.SIZE_TICK,
                color=style.INK, zorder=5)

    fig.subplots_adjust(left=0.005, right=0.995, bottom=0.01, top=0.99)
    out = style.save(fig, REPO / STEM, script=SCRIPT, svg=True)
    plt.close(fig)

    prov.note("This figure reads no results file and plots no measured number, so the "
              "data_matches_source check has nothing to check. Its correctness condition is "
              "different and is stated here: every expression is transcribed from "
              "src/simulators/sir3.py and src/simulators/summaries.py at the commit recorded "
              "above, and a change to either file invalidates the diagram without invalidating "
              "any number. A future session editing those modules must regenerate this figure.")
    prov.note("Transcribed from: src/simulators/sir3.py (SIR3Params defaults, _rhs, "
              "_integrate, _delay_kernel, simulate, ETA_SCALE) and "
              "src/simulators/summaries.py (s_a, s_b, s_c, N_BINS).")
    prov.note("An editable .svg is written beside the .pdf so a later session can move a box "
              "without re-deriving the drawing. The .py stays canonical; a divergence between "
              "them is a defect in the .svg.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
