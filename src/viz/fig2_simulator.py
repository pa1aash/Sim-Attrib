"""Figure 2 -- the simulator's structure, and where each distortion family acts.

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
    "base simulator, and two family sets are declared: a base set of three qualitatively "
    "different deformations, and an adversarial set designed so that all three columns "
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


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["COMPONENT"])
    prov = vp.FigureProvenance("fig2_simulator", script=SCRIPT)

    fig, ax = plt.subplots(figsize=(style.FIG_FULL, 4.00))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    ct, cp, co = (style.COMPONENT["transmission"], style.COMPONENT["progression"],
                  style.COMPONENT["observation"])

    # ---- zone A: the deterministic core (y 82-99) ----------------------------------------
    ax.text(0.0, 99.0, "DETERMINISTIC CORE   —   fixed-step RK4, 24 substeps/day, "
                       "$T=120$ days, $N=10^5$", ha="left", va="top",
            fontsize=style.SIZE_TICK, color=style.RULE)
    box(ax, 1, 86, 8, 8, "$S$", ec=style.INK, fs=style.SIZE_LABEL)
    box(ax, 23, 86, 8, 8, "$I$", ec=style.INK, fs=style.SIZE_LABEL)
    box(ax, 45, 86, 13, 8, "$C$\ncumulative", ec=style.INK)
    box(ax, 68, 86, 31, 8, "daily true incidence $=\\mathrm{diff}(C)$\nnever observed",
        ec=style.INK)
    arrow(ax, (9, 90), (23, 90))
    arrow(ax, (31, 90), (45, 90))
    arrow(ax, (58, 90), (68, 90))
    ax.text(16.0, 91.0, "incidence", ha="center", va="bottom", fontsize=style.SIZE_SMALL,
            color=ct)
    ax.text(41.0, 84.8, "the same incidence term", ha="center", va="top",
            fontsize=style.SIZE_SMALL, color=style.RULE)
    arrow(ax, (27, 86), (27, 79), colour=cp)
    ax.text(28.5, 81.5, "removal (not tracked further)", ha="left", va="center",
            fontsize=style.SIZE_SMALL, color=cp)
    ax.plot([16.0], [90.0], marker="o", markersize=4.2, color=ct,
            markeredgecolor=style.PANEL, markeredgewidth=0.6, zorder=6)
    ax.plot([27.0], [84.0], marker="o", markersize=4.2, color=cp,
            markeredgecolor=style.PANEL, markeredgewidth=0.6, zorder=6)

    # ---- zone B: the observation chain (y 58-74) -----------------------------------------
    ax.text(0.0, 75.0, "OBSERVATION COMPONENT", ha="left", va="top",
            fontsize=style.SIZE_TICK, color=style.RULE)
    box(ax, 1, 62, 21, 8, "delay kernel\ngamma, mean 3 d, shape 3", ec=co)
    box(ax, 25, 62, 15, 8, "reporting fraction\n$\\rho = 0.4$", ec=co)
    box(ax, 43, 62, 24, 8, "lognormal noise\n$\\exp(\\sigma z-\\sigma^2/2)$, "
                           "$\\sigma=0.15$", ec=co)
    box(ax, 70, 62, 29, 8, "reported series $y_t$\n$\\rightarrow$ summaries $s(y)$",
        ec=style.INK)
    for a, b in ((22, 25), (40, 43), (67, 70)):
        arrow(ax, (a, 66), (b, 66))
    arrow(ax, (84, 86), (84, 70))
    ax.plot([32.5], [62.0], marker="o", markersize=4.2, color=co,
            markeredgecolor=style.PANEL, markeredgewidth=0.6, zorder=6)
    ax.text(0.0, 59.5,
            "a CONTINUOUS multiplicative layer is required: a count-valued one is not\n"
            "differentiable under common random numbers, and is kept as a negative control",
            ha="left", va="top", fontsize=style.SIZE_SMALL, color=style.RULE,
            linespacing=1.35)

    ax.text(99.5, 51.5,
            "$S_A$: peak height, peak time, final size, growth rate   ($d=4$)\n"
            "$S_B$: 10 equal-width time-binned incidence counts   ($d=10$)\n"
            "$S_C$: final size, peak height   ($d=2$, impoverished control)",
            ha="right", va="top", fontsize=style.SIZE_SMALL, color=style.INK,
            linespacing=1.45)

    # ---- zone C: the three distortion families (y 8-44) -----------------------------------
    ax.plot([0, 100], [40.5, 40.5], color=style.FAINT, linewidth=0.6, zorder=1)
    ax.text(0.0, 39.0, "THE THREE DISTORTION FAMILIES   —   one one-parameter family per "
                       "component, in two declared sets", ha="left", va="top",
            fontsize=style.SIZE_TICK, color=style.RULE)

    rows = (
        (ct, r"$\eta_1$  TRANSMISSION",
         r"base:  $\beta S I/N \;\div\; [\,1+\eta_1 (I/N)/p_{\mathrm{ref}}\,]$"
         "\u2003\u2003saturating incidence — a prevalence nonlinearity",
         r"adv:  $\beta \rightarrow \beta\, e^{\eta_1}$"
         "\u2003\u2003constant multiplier, aimed at progression through $R_0$"),
        (cp, r"$\eta_2$  PROGRESSION",
         r"base:  $\gamma \rightarrow \gamma\, e^{\eta_2 (t/T - 1/2)}$"
         "\u2003\u2003mean-centred hazard drift — a timing distortion",
         r"adv:  $\gamma \rightarrow \gamma\, e^{-\eta_2}$"
         "\u2003\u2003sign-aligned with $\eta_1'$, so both raise $R_0$"),
        (co, r"$\eta_3$  OBSERVATION",
         r"base:  $\rho \rightarrow \rho\, e^{\eta_3}$"
         "\u2003\u2003pure amplitude error",
         r"adv:  $\rho \rightarrow \rho\, e^{\eta_3 (t/T - 1/2)}$"
         "\u2003\u2003reporting trend; adds $\eta_3/T$ to the fitted growth rate"),
    )
    for i, (colour, title, base_txt, adv_txt) in enumerate(rows):
        y = 34.5 - i * 10.0
        ax.plot([1.2], [y - 1.4], marker="s", markersize=4.5, color=colour, zorder=5)
        ax.text(4.0, y, title, ha="left", va="top", fontsize=style.SIZE_SMALL,
                color=colour, zorder=5)
        ax.text(24.0, y, base_txt, ha="left", va="top", fontsize=style.SIZE_SMALL,
                color=style.INK, zorder=5)
        ax.text(24.0, y - 4.6, adv_txt, ha="left", va="top", fontsize=style.SIZE_SMALL,
                color=style.INK, zorder=5)

    # ---- zone D: the two standing qualifications (y 0-6) ----------------------------------
    ax.plot([0, 100], [6.3, 6.3], color=style.FAINT, linewidth=0.6, zorder=1)
    ax.text(0.0, 5.2,
            r"every family is the base simulator EXACTLY at $\eta_k=0$, asserted "
            r"bit-for-bit;   $\eta_k$ is in units of $\mathrm{ETA\_SCALE}=0.1$, a 10\% "
            r"relative deformation",
            ha="left", va="top", fontsize=style.SIZE_SMALL, color=style.RULE)
    ax.text(0.0, 1.8,
            r"under the observation family the delay kernel and $\sigma$ are HELD FIXED and "
            r"only $\rho$ moves — a stated limitation of the design, not an omission here",
            ha="left", va="top", fontsize=style.SIZE_SMALL, color=style.RULE)

    fig.subplots_adjust(left=0.005, right=0.995, bottom=0.005, top=0.995)
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
