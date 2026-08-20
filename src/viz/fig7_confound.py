"""Figure 7 -- what the six-column confound actually confounds.

WHY THIS FIGURE WAS ADDED BEYOND THE SIX THE SESSION SCOPED
-------------------------------------------------------------
Figure 3 shows *that* the six-column object is rank deficient. This one shows *what the
deficiency is made of*, and that is a different claim carrying different weight.

A rank deficiency is only interesting if a reader can say which quantities are confounded.
`docs/DECISIONS.md` **D-14** restricts every claim this project makes to a distortion model
carrying at most one one-parameter family per component, and the justification for that
restriction is not "the number went above a threshold" -- it is that **both near-null
directions mix progression with observation**, so a component-attribution statement made
outside the restriction would be attributing to a component something the data cannot
separate from another component. That is the boundary result, and until this figure it
existed only as two rows of a table.

Stated as modelling rather than as linear algebra: **a drifting removal hazard is nearly
indistinguishable from a constant hazard change combined with a drifting reporting rate.**
It is an epidemiological commonplace, `docs/OPEN_QUESTIONS.md` Q-12 predicted it in prose
before any of these numbers existed, and it needs the progression component to carry two
distortion parameters at once -- which is exactly why it does not reach the `K = 3` model
and exactly why the restriction is the right shape.

WHAT IS DRAWN
--------------
Panels (a) and (b): the two right singular vectors, one bar per distortion column, signed.
The dashed lines are the pre-registered equivalence-class membership threshold
`vk_min = 0.3` from ``docs/THRESHOLDS.md`` §2.1 -- a column is named in the class when its
loading exceeds it. Panel (c): the same two directions as mechanism energy, i.e. the share of
squared loading falling on each of the three mechanisms, which is the quantity the
cross-mechanism / within-mechanism classification is made on.

Every number is from ``results/robustness/k6_spectrum.yaml``. Nothing is computed here.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from . import provenance as vp
from . import style

REPO = Path(__file__).resolve().parents[2]
SRC = "results/robustness/k6_spectrum.yaml"
STEM = "figures/fig7_confound"
SCRIPT = "src/viz/fig7_confound.py"

SHORT = ("base:\ntransmission", "base:\nprogression", "base:\nobservation",
         "adv:\ntransmission", "adv:\nprogression", "adv:\nobservation")

CAPTION = (
    "The two near-null directions of the six-column summary Jacobian for $S_B$, the object "
    "that is inseparable at $\\kappa = 629$. (a, b) Right singular vectors $v_5$ and $v_6$, "
    "one bar per distortion column, coloured by the mechanism the column deforms and hatched "
    "where the column comes from the adversarial family set. Dashed lines mark the "
    "pre-registered equivalence-class threshold $|v_k| = 0.3$ from docs/THRESHOLDS.md "
    "\\S2.1. (c) The same two directions as mechanism energy: the share of squared loading "
    "falling on each mechanism. Both directions are cross-mechanism and both name the same "
    "pair -- progression together with observation -- with transmission carrying under 5\\% "
    "of the energy in either. Read as modelling rather than as linear algebra: a drifting "
    "removal hazard is nearly indistinguishable from a constant hazard change combined with "
    "a drifting reporting rate. The confound requires the progression component to carry two "
    "distortion parameters at once, which is why it cannot arise in any three-column model "
    "the declared families permit, and why the scope restriction of DECISIONS.md D-14 is "
    "stated as one parameter per component rather than as a bound on $\\kappa$. Every "
    "loading is stable to three decimal places across the h-plateau."
)


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["COMPONENT"])
    prov = vp.FigureProvenance("fig7_confound", script=SCRIPT)
    doc = prov.source(SRC)
    six = doc["summary_sets"]["S_B"]["six_columns"]
    labels = doc["six_column_labels"]   # strings, not numbers: recorded in a note below
    vk_min = prov.plotted("registered vk_min",
                          [doc["thresholds_pre_registered"]["vk_min"]], SRC,
                          "thresholds_pre_registered.vk_min")[0]
    dirs = six["near_null_directions"]
    cls = six["near_null_classification"]
    mechanisms = tuple(style.COMPONENT)

    fig, axes = plt.subplots(1, 3, figsize=(style.FIG_FULL, 2.30),
                             gridspec_kw={"width_ratios": [1.0, 1.0, 0.78]})

    y = np.arange(len(labels))
    for panel, (ax, d) in enumerate(zip(axes[:2], dirs)):
        v = prov.plotted(
            f"v_{d['index'] + 1} loadings", d["right_singular_vector_at_representative_h"],
            SRC, f"summary_sets.S_B.six_columns.near_null_directions[{panel}]"
                 ".right_singular_vector_at_representative_h")
        sigma = prov.plotted(
            f"sigma_{d['index'] + 1}", [d["singular_value"]], SRC,
            f"summary_sets.S_B.six_columns.near_null_directions[{panel}].singular_value")[0]
        ratio = prov.plotted(
            f"sigma_{d['index'] + 1}/sigma_1", [d["sigma_ratio_to_sigma1"]], SRC,
            f"summary_sets.S_B.six_columns.near_null_directions[{panel}]"
            ".sigma_ratio_to_sigma1")[0]
        for i, (val, lab) in enumerate(zip(v, labels)):
            fam, mech = lab.split(":")
            ax.barh(y[i], val, height=0.66, color=style.COMPONENT[mech],
                    edgecolor=style.COMPONENT[mech], linewidth=0.7,
                    hatch=("///" if fam == "adversarial" else None),
                    alpha=(0.55 if fam == "adversarial" else 1.0), zorder=2)
        ax.axvline(0.0, color=style.INK, linewidth=0.6, zorder=3)
        for s in (-vk_min, vk_min):
            ax.axvline(s, color=style.RULE, linewidth=0.8, linestyle=(0, (4, 1.6)), zorder=1.5)
        ax.set_xlim(-0.95, 0.95)
        ax.set_ylim(len(labels) - 0.4, -0.6)
        ax.set_yticks(y)
        ax.set_yticklabels(SHORT if panel == 0 else [""] * len(labels),
                           fontsize=style.SIZE_SMALL, linespacing=1.0)
        ax.set_xlabel("loading  (dimensionless)")
        ax.set_title(f"({'ab'[panel]})  $v_{d['index'] + 1}$,  "
                     f"$\\sigma={sigma:.4g}$  ($\\sigma/\\sigma_1={ratio:.4f}$)",
                     fontsize=style.SIZE_TITLE, pad=3)
        ax.tick_params(axis="y", length=0)
        ax.spines["left"].set_visible(False)

    # ---- panel (c): mechanism energy ------------------------------------------------------
    axc = axes[2]
    for panel, c in enumerate(cls):
        energy = prov.plotted(
            f"mechanism energy, direction {panel + 1}",
            [c["mechanism_energy"][m] for m in mechanisms], SRC,
            f"summary_sets.S_B.six_columns.near_null_classification[{panel}].mechanism_energy",
            transform=("energy of transmission, progression, observation in that order",
                       lambda e: [e[m] for m in mechanisms]))
        left = 0.0
        for m, share in zip(mechanisms, energy):
            axc.barh(panel, share, left=left, height=0.5, color=style.COMPONENT[m],
                     edgecolor=style.PANEL, linewidth=0.6, zorder=2)
            if share > 0.12:
                axc.text(left + share / 2, panel, f"{share:.2f}", ha="center", va="center",
                         fontsize=style.SIZE_SMALL, color=style.PANEL)
            left += share
        axc.text(0.0, panel - 0.30, c["kind"], ha="left", va="bottom",
                 fontsize=style.SIZE_SMALL, color=style.INK)
    axc.set_xlim(0, 1)
    axc.set_ylim(1.62, -0.62)
    axc.set_yticks([0, 1])
    axc.set_yticklabels([f"$v_{dirs[0]['index'] + 1}$", f"$v_{dirs[1]['index'] + 1}$"],
                        fontsize=style.SIZE_TICK)
    axc.set_xlabel("mechanism energy  (share of $\\|v\\|^2$)")
    axc.set_title("(c)  which mechanisms", fontsize=style.SIZE_TITLE, pad=3)
    axc.tick_params(axis="y", length=0)
    axc.spines["left"].set_visible(False)

    handles = [plt.Rectangle((0, 0), 1, 1, color=style.COMPONENT[m]) for m in mechanisms]
    handles.append(plt.Rectangle((0, 0), 1, 1, facecolor="none", edgecolor=style.INK,
                                 hatch="///", linewidth=0.7))
    handles.append(plt.Line2D([], [], color=style.RULE, linewidth=0.8,
                              linestyle=(0, (4, 1.6))))
    fig.legend(handles, [*mechanisms, "adversarial-family column",
                         r"$|v_k| = 0.3$: class threshold"],
               loc="lower center", ncol=5, fontsize=style.SIZE_SMALL, handlelength=1.2,
               handleheight=0.9, columnspacing=1.3, bbox_to_anchor=(0.5, 0.0))
    fig.subplots_adjust(left=0.115, right=0.995, bottom=0.30, top=0.86, wspace=0.16)

    out = style.save(fig, REPO / STEM, script=SCRIPT)
    plt.close(fig)
    prov.note(
        "The column labels on panel (a) are abbreviated for width; the recorded labels are "
        f"{doc['six_column_labels']} in that order, and the bars are in that order.")
    prov.note(
        "The 'cross-mechanism' text beside each bar in panel (c) is the recorded `kind` "
        "field, not a reading made here: the classification is computed in "
        "src/diagnostics/k6_spectrum.py from the equivalence-class members, and its meaning "
        "is recorded alongside it in the results file.")
    prov.note(
        "Panel (c) sums to 1 by construction, since the mechanism energies are shares of a "
        "unit-norm singular vector's squared loading. That is not a check -- it cannot fail "
        "-- and it is stated here so a reader does not read it as one.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
