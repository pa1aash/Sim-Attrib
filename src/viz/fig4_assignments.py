"""Figure 4 -- the eight component-wise family assignments, for ``S_B`` and for ``S_A``.

WHY A BAR CHART ORDERED BY ``kappa`` AND NOT A HEATMAP
--------------------------------------------------------
The eight assignments are the vertices of a 2x2x2 cube: one binary choice (base or
adversarial) per component. A heatmap over that space has to be drawn as two 2x2 tiles or as
a flattened 8x1 strip, and in either layout the reader's first question -- *"is this one
above or below the ceiling?"* -- becomes a colour-to-legend lookup. The decision the figure
reports is a **comparison against a single pre-registered number**, `kappa_max = 100`, so the
right encoding is position against a reference line. Eight bars ordered by `kappa`, on a log
axis, put every assignment's margin in front of the reader directly. The cube structure is
not lost: each bar is labelled with its three-letter code and coloured by the choice that
turns out to matter.

WHY ``S_A`` IS HERE TOO
------------------------
Because a diagnostic that says "separable" eight times out of eight is indistinguishable, in
one panel, from a diagnostic that always says "separable". `S_A` is the same sweep on a
four-dimensional summary set and it splits **exactly on the transmission family**: every
assignment carrying the adversarial transmission family fails, every assignment carrying the
base one passes. That is the evidence that the eight `S_B` passes are a measurement rather
than a property of the instrument, and it belongs beside them.

`S_A` is dead as a generalising result (`audit/G3_ADVERSARIAL_REVIEW.md` finding 2) and this
figure does not revive it. It appears as a **control**, which is what it is.

COLOUR
-------
Bars are coloured by the **transmission** family, base or adversarial, because that is the
choice `S_A`'s split falls on. The colours are the project's FAMILY scale, unchanged from
Figure 3 -- so "blue" means the base family set on every page of this paper.

Every number is from ``results/robustness/k6_spectrum.yaml``. Nothing is computed here.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

from . import provenance as vp
from . import style

REPO = Path(__file__).resolve().parents[2]
SRC = "results/robustness/k6_spectrum.yaml"
STEM = "figures/fig4_assignments"
SCRIPT = "src/viz/fig4_assignments.py"

CODES = ("BBB", "BBA", "BAB", "BAA", "ABB", "ABA", "AAB", "AAA")

CAPTION = (
    "Condition number $\\kappa$ of the summary Jacobian under all eight component-wise "
    "assignments of a distortion family to a component that the two declared family sets "
    "permit, for the ten-dimensional summary set $S_B$ (left) and the four-dimensional "
    "$S_A$ (right). Each three-letter code gives the family chosen for transmission, "
    "progression and observation in that order; B is the base family, A the adversarial "
    "one. Bars are coloured by the transmission choice. The dashed line is the "
    "pre-registered ceiling $\\kappa_{\\max} = 100$ from docs/THRESHOLDS.md, equivalent at "
    "the registered pair to the rank tolerance $\\tau = 10^{-2}$. $S_B$ separates under all "
    "eight assignments, $\\kappa$ from 6.6 to 65.6, every singular value resolved -- six of "
    "the eight had never been tested before. $S_A$ splits exactly on the transmission "
    "family: all four assignments carrying the adversarial transmission family are "
    "inseparable and all four carrying the base one are separable, with ABB failing by "
    "0.9\\%. $S_A$ is shown as a control, not as a result: it establishes that the eight "
    "$S_B$ passes are a measurement rather than a property of an instrument that always "
    "says separable. Under DECISIONS.md D-14 these eight points establish separability of a "
    "three-dimensional distortion space eight times over, and nothing wider: they are every "
    "combination of two family sets this project chose, not a sample of distortion families "
    "in general."
)


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["FAMILY"])
    prov = vp.FigureProvenance("fig4_assignments", script=SCRIPT)
    doc = prov.source(SRC)
    kmax = prov.plotted("registered kappa_max",
                        [doc["thresholds_pre_registered"]["kappa_max"]], SRC,
                        "thresholds_pre_registered.kappa_max")[0]

    fig, axes = plt.subplots(1, 2, figsize=(style.FIG_FULL, 2.55))

    for ax, sset, title in ((axes[0], "S_B", "$S_B$  (10 summaries)"),
                            (axes[1], "S_A", "$S_A$  (4 summaries)")):
        trip = doc["summary_sets"][sset]["mixed_triples"]
        kappas = prov.plotted(
            f"{sset} kappa, eight assignments", [trip[c]["condition_number"] for c in CODES],
            SRC, f"summary_sets.{sset}.mixed_triples", tol=0.0,
            transform=("condition_number of each of BBB,BBA,BAB,BAA,ABB,ABA,AAB,AAA",
                       lambda d: [d[c]["condition_number"] for c in CODES]))
        # Ordered by kappa WITHIN each panel: the ordering is the finding, and each panel
        # therefore carries its own axis labels. Sharing the y axis would label S_A's bars
        # with S_B's ordering, which is the one way this figure could lie.
        order = sorted(range(len(CODES)), key=lambda i: kappas[i])
        for slot, i in enumerate(order):
            code = CODES[i]
            fam = "adversarial" if code[0] == "A" else "base"
            insep = trip[code]["verdict"] != "separable"
            ax.barh(slot, kappas[i], height=0.62, color=style.FAMILY[fam],
                    alpha=(1.0 if not insep else 0.40),
                    edgecolor=style.FAMILY[fam], linewidth=0.7,
                    hatch=("///" if insep else None), zorder=2)
            ax.text(kappas[i] * 1.16, slot, f"{kappas[i]:.4g}", va="center", ha="left",
                    fontsize=style.SIZE_SMALL, color=style.INK)
        ax.set_yticks(range(len(CODES)))
        ax.set_yticklabels([CODES[i] for i in order], fontsize=style.SIZE_TICK,
                           family="monospace")
        ax.set_xscale("log")
        ax.set_xlim(3.0, 1.2e4)
        ax.set_xticks([1e1, 1e2, 1e3, 1e4])
        ax.set_ylim(-0.65, len(CODES) - 0.05)
        ax.set_xlabel(r"condition number $\kappa$  (dimensionless)")
        ax.set_title(title, fontsize=style.SIZE_TITLE, pad=3)
        style.threshold_line(ax, kmax, "", axis="x", zorder=3)
        ax.annotate(r"pre-registered $\kappa_{\max}=100$", xy=(kmax, 1.0),
                    xycoords=("data", "axes fraction"), xytext=(3, -1),
                    textcoords="offset points", ha="left", va="top",
                    fontsize=style.SIZE_LABEL, color=style.RULE)
        ax.spines["left"].set_visible(False)
        ax.tick_params(axis="y", length=0)

    handles = [
        plt.Rectangle((0, 0), 1, 1, facecolor=style.FAMILY["base"],
                      edgecolor=style.FAMILY["base"]),
        plt.Rectangle((0, 0), 1, 1, facecolor=style.FAMILY["adversarial"],
                      edgecolor=style.FAMILY["adversarial"]),
        plt.Rectangle((0, 0), 1, 1, facecolor="none", edgecolor=style.INK, hatch="///",
                      linewidth=0.7),
    ]
    fig.legend(handles,
               ["base transmission family", "adversarial transmission family",
                "INSEPARABLE"],
               loc="lower center", ncol=3, fontsize=style.SIZE_TICK,
               handlelength=1.1, handleheight=0.9, columnspacing=1.6,
               bbox_to_anchor=(0.5, 0.0))
    # subplots_adjust rather than tight_layout: tight_layout does not know about a
    # figure-level legend and lays the panels out over the top of it.
    fig.subplots_adjust(left=0.075, right=0.995, bottom=0.245, top=0.90, wspace=0.28)

    out = style.save(fig, REPO / STEM, script=SCRIPT)
    plt.close(fig)
    prov.note("Bars are ordered by kappa within each panel, so the vertical position of a "
              "code differs between panels. The codes are on the axis for exactly that "
              "reason: the ordering is the point, and a shared ordering would hide S_A's "
              "split on the transmission family.")
    prov.note("The two textual annotations ('all eight separable', 'hatched: INSEPARABLE') "
              "are placed by hand and are not covered by the data_matches_source check. In "
              "the source file, S_B has "
              f"{sum(1 for c in CODES if doc['summary_sets']['S_B']['mixed_triples'][c]['verdict'] == 'separable')}"
              " of 8 separable and S_A has "
              f"{sum(1 for c in CODES if doc['summary_sets']['S_A']['mixed_triples'][c]['verdict'] == 'separable')}"
              " of 8.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
