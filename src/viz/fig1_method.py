"""Figure 1 -- the diagnostic, end to end.

WHAT THIS DIAGRAM IS FOR
-------------------------
The paper's first contribution is a **procedure**, and a procedure's figure has one job: let
a reader who has never seen it decide whether they could run it on their own simulator. So
the boxes are the four things somebody would actually do, and the annotations under them are
the four places where doing it carelessly gives a confident wrong answer.

Those four places are not decoration; each is a defect this project either hit or came close
to hitting, and each is recorded elsewhere in the repository:

* **the distortion families must be the identity at zero, bit-for-bit** -- otherwise the
  Jacobian is the derivative of something that is not the model. Asserted in
  ``tests/test_sir3.py`` before anything else runs;
* **common random numbers are what make the difference quotient well posed at all** --
  without them the quotient carries noise of order ``sigma/h`` and there is no plateau to
  find. ``results/jacobian_rank.S_A.no_crn_control.yaml`` is that negative control;
* **rank is not scale-invariant**, so both normalisations have to be fixed in advance;
  ``docs/THRESHOLDS.md`` §0 fixes them before any singular value existed;
* **a singular value the estimator has not resolved must be counted toward the rank in
  neither direction** -- and, separately, resolution is a property of the *estimator* while
  spectral density is a property of the *matrix*, so passing the resolution test does not
  answer the gapless-spectrum objection. ``audit/K6_SPECTRUM_CHECK.md`` §2.4 records that
  safeguard being pointed at the wrong quantity.

WHAT IS DELIBERATELY ABSENT
----------------------------
No arrow leaves the verdict box toward an inference procedure. ``docs/DECISIONS.md`` D-16
drops the composition this diagnostic was built as a precondition for, and drawing a
downstream stage the paper does not have would be the overstatement this project's first
three sessions were killed for. The diagnostic's output is a verdict about whether a question
is well posed, and the figure stops there.

This figure reads no ``results/`` file. Its correctness condition is transcription from
``src/diagnostics/jacobian_rank.py``, ``docs/THRESHOLDS.md`` and ``src/simulators/sir3.py``,
and that is recorded in the sidecar in place of a data check.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from . import provenance as vp
from . import style

REPO = Path(__file__).resolve().parents[2]
STEM = "figures/fig1_method"
SCRIPT = "src/viz/fig1_method.py"

CAPTION = (
    "The rank and coherence diagnostic, end to end. A simulator is declared as $K$ "
    "components, each carrying a one-parameter distortion family that is bit-identical to "
    "the base simulator at $\\eta_k = 0$. The summary Jacobian $J = \\partial s/\\partial "
    "\\eta$ at $\\eta = 0$ is estimated by central differences under common random numbers, "
    "swept over six decades of step size; without common random numbers the quotient carries "
    "simulation noise of order $\\sigma/h$ and no plateau exists, which the project's "
    "no-CRN negative control demonstrates. Summaries are divided by their prior-predictive "
    "standard deviation and each $\\eta_k$ by a common relative perturbation scale, because "
    "the rank of $J$ is not scale-invariant; both normalisations and both thresholds are "
    "registered before any singular value exists. A singular value that moves by more than a "
    "factor of two across the plateau is counted toward the rank in neither direction, so "
    "the reported rank may be an interval rather than a number. The verdict is separable when "
    "$J$ has full column rank at tolerance $\\tau$ and $\\kappa \\leq \\kappa_{\\max}$; "
    "otherwise the near-null right singular vectors name an equivalence class of components "
    "that the summaries cannot tell apart, and the honest output is that class rather than a "
    "component. No arrow leaves the verdict: the diagnostic decides whether attribution is "
    "well posed, and nothing further."
)

BOX = dict(boxstyle="round,pad=0.4,rounding_size=0.10", linewidth=0.8)


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["COMPONENT"])
    prov = vp.FigureProvenance("fig1_method", script=SCRIPT)

    fig, ax = plt.subplots(figsize=(style.FIG_FULL, 3.10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    stages = (
        (0.0, 21.0, "1.  DECLARE",
         "simulator as $K$ components,\n"
         "one one-parameter distortion\n"
         "family $\\delta_k(\\cdot\\,;\\eta_k)$ each",
         "$\\delta_k(\\cdot\\,;0)$ is the base simulator\nEXACTLY — asserted bit-for-bit"),
        (25.8, 21.0, "2.  SIMULATE",
         "$\\eta = \\pm h\\,e_k$ for each $k$,\n"
         "under common random numbers,\n"
         "swept over six decades of $h$",
         "without CRN the quotient carries\nnoise of order $\\sigma/h$ — no plateau"),
        (51.6, 21.0, "3.  NORMALISE $+$ SVD",
         "$s \\div$ prior-predictive s.d.,\n"
         "$\\eta \\div$ a common scale;\n"
         "$\\sigma_1 \\geq \\ldots \\geq \\sigma_K$ of $J$",
         "rank is NOT scale-invariant, so\nboth normalisations are registered"),
        (77.4, 21.0, "4.  DECIDE",
         "rank at $\\tau$, and $\\kappa$ against\n"
         "$\\kappa_{\\max}$; near-null right\n"
         "singular vectors read off",
         "$\\tau$, $\\kappa_{\\max}$ fixed before any\nsingular value existed"),
    )

    for x, w, title, body, note in stages:
        ax.add_patch(FancyBboxPatch((x, 57), w, 34, edgecolor=style.INK, facecolor="none",
                                    zorder=2, **BOX))
        ax.text(x + w / 2, 88.5, title, ha="center", va="top",
                fontsize=style.SIZE_LABEL, color=style.INK, zorder=3)
        ax.text(x + w / 2, 81.5, body, ha="center", va="top",
                fontsize=style.SIZE_SMALL, color=style.INK, zorder=3, linespacing=1.5)
        ax.plot([x + 1.6, x + w - 1.6], [66.5, 66.5], color=style.FAINT, linewidth=0.5,
                zorder=3)
        ax.text(x + w / 2, 64.5, note, ha="center", va="top",
                fontsize=style.SIZE_SMALL, color=style.RULE, zorder=3, linespacing=1.4)

    for x in (21.5, 47.3, 73.1):
        ax.annotate("", xy=(x + 3.8, 74), xytext=(x, 74),
                    arrowprops=dict(arrowstyle="-|>", linewidth=1.0, color=style.INK,
                                    mutation_scale=8.0, shrinkA=0.0, shrinkB=0.0),
                    annotation_clip=False, zorder=6)

    ax.text(0.0, 98.5, "$K$ components, one distortion family each:",
            ha="left", va="top", fontsize=style.SIZE_SMALL, color=style.RULE)
    for i, (name, colour) in enumerate(style.COMPONENT.items()):
        ax.plot([27.0 + i * 12.5], [96.6], marker="s", markersize=4.0, color=colour, zorder=4)
        ax.text(28.8 + i * 12.5, 96.6, f"$\\eta_{{{i + 1}}}$  {name}", ha="left",
                va="center", fontsize=style.SIZE_SMALL, color=colour)

    # ---- the two outcomes -----------------------------------------------------------------
    ax.annotate("", xy=(88.0, 48.6), xytext=(88.0, 56.6),
                arrowprops=dict(arrowstyle="-|>", linewidth=1.0, color=style.INK,
                                mutation_scale=8.0, shrinkA=0.0, shrinkB=0.0),
                annotation_clip=False, zorder=6)
    ax.add_patch(FancyBboxPatch((28, 28), 32, 20, edgecolor=style.COMPONENT["observation"],
                                facecolor="none", zorder=2, **BOX))
    ax.add_patch(FancyBboxPatch((65, 28), 34, 20, edgecolor=style.COMPONENT["progression"],
                                facecolor="none", zorder=2, **BOX))
    ax.annotate("", xy=(60.6, 38), xytext=(64.6, 38),
                arrowprops=dict(arrowstyle="-|>", linewidth=1.0, color=style.INK,
                                mutation_scale=8.0, shrinkA=0.0, shrinkB=0.0),
                annotation_clip=False, zorder=6)
    ax.text(44, 45.0, "SEPARABLE", ha="center", va="top", fontsize=style.SIZE_LABEL,
            color=style.COMPONENT["observation"])
    ax.text(44, 39.0, "full column rank at $\\tau$\nand $\\kappa \\leq "
                      "\\kappa_{\\max}$:\nattribution is well posed",
            ha="center", va="top", fontsize=style.SIZE_SMALL, color=style.INK,
            linespacing=1.45)
    ax.text(82, 45.0, "INSEPARABLE", ha="center", va="top", fontsize=style.SIZE_LABEL,
            color=style.COMPONENT["progression"])
    ax.text(82, 39.0, "the near-null directions name an\nEQUIVALENCE CLASS of components;\n"
                      "report the class, not a component",
            ha="center", va="top", fontsize=style.SIZE_SMALL, color=style.INK,
            linespacing=1.45)
    ax.text(26.0, 38.0, "the diagnostic stops here.\nD-16 drops the composition\n"
                        "it was built as a precondition for",
            ha="right", va="center", fontsize=style.SIZE_SMALL, color=style.RULE,
            linespacing=1.45)

    # ---- the standing qualifications -------------------------------------------------------
    ax.plot([0, 100], [22.0, 22.0], color=style.FAINT, linewidth=0.6, zorder=1)
    ax.text(0.0, 19.0,
            "a singular value moving by more than a factor of two across the $h$-plateau is "
            "counted toward the rank in NEITHER direction,\nso the reported rank may be an "
            "interval rather than a number",
            ha="left", va="top", fontsize=style.SIZE_SMALL, color=style.RULE,
            linespacing=1.45)
    ax.text(0.0, 11.0,
            "the resolution test is a property of the ESTIMATOR and spectral density a "
            "property of the MATRIX: passing it does not answer\nthe objection that a "
            "gapless spectrum makes rank a threshold decision",
            ha="left", va="top", fontsize=style.SIZE_SMALL, color=style.RULE,
            linespacing=1.45)
    ax.text(0.0, 3.0,
            "the diagnostic never receives a component index or a ground-truth label: it "
            "computes a property of the map $s(\\eta)$, so there is\nno hidden truth "
            "available to leak into its answer",
            ha="left", va="top", fontsize=style.SIZE_SMALL, color=style.RULE,
            linespacing=1.45)

    fig.subplots_adjust(left=0.005, right=0.995, bottom=0.005, top=0.995)
    out = style.save(fig, REPO / STEM, script=SCRIPT, svg=True)
    plt.close(fig)

    prov.note("This figure reads no results file and plots no measured number, so the "
              "data_matches_source check has nothing to check. Its correctness condition is "
              "transcription: every step and every threshold shown is taken from "
              "src/diagnostics/jacobian_rank.py, docs/THRESHOLDS.md and src/simulators/sir3.py "
              "at the commit recorded above. A change to the diagnostic's rule invalidates "
              "this diagram without invalidating any number in results/.")
    prov.note("No arrow leaves the verdict. docs/DECISIONS.md D-16 drops the MMC composition "
              "this diagnostic was built as a precondition for, so a downstream inference "
              "stage would be drawing a capability the paper does not have.")
    prov.note("An editable .svg is written beside the .pdf so a later session can move a box "
              "without re-deriving the drawing. The .py stays canonical; a divergence between "
              "them is a defect in the .svg.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
