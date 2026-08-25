"""Figure 3 -- the full singular-value spectrum of ``S_B``'s summary Jacobian.

WHAT THE FIGURE HAS TO MAKE VISIBLE
------------------------------------
Three spectra of the same simulator under the same summary set, differing only in the
distortion directions the Jacobian's columns span:

* **base**, three columns, `kappa = 10.12`, separable;
* **adversarial**, three columns, `kappa = 64.62`, separable -- a family set *designed to
  fail* and which does not;
* **the six-column union**, two distortion parameters per component, `kappa = 628.9`,
  **INSEPARABLE**, rank 4 of 6.

and the one thing that distinguishes them, which is **where the registered tolerance sits**.
Under either three-column set `tau` lies an order of magnitude below the whole spectrum, so
the rank call is not a threshold decision. In the six-column union it falls *inside* the
spectrum, between `sigma_4` and `sigma_5` -- which is the Gutenkunst objection
(`audit/R2_THREAT_CHECK.md` §1.3) arriving in this project's own data.

WHY RATIOS AND NOT RAW SINGULAR VALUES
---------------------------------------
The decision rule is `sigma_i >= tau * sigma_1`, so the quantity the rule sees is
`sigma_i / sigma_1` and the threshold is a horizontal line at `tau` on every series at once.
Plotting raw singular values would put three unrelated scales on one axis and make the
threshold three different lines. The ratios are read from the results file, not computed
here: ``sigma_i_over_sigma_1`` is a recorded field.

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
STEM = "figures/fig3_spectrum"
SCRIPT = "src/viz/fig3_spectrum.py"

CASES = (
    ("base", "base", "base families, $K=3$"),
    ("adversarial", "adversarial", "adversarial families, $K=3$"),
    ("six_columns", "union", "six-column union"),
)

CAPTION = (
    "Singular-value spectrum of the summary Jacobian for summary set $S_B$, normalised by "
    "the leading singular value, under three distortion column sets: the base families "
    "($K=3$), the adversarial families ($K=3$), and their six-column union ($K=6$, two "
    "one-parameter families per component). The dashed line is the pre-registered rank "
    "tolerance $\\tau = 10^{-2}$, fixed in docs/THRESHOLDS.md before any singular value "
    "existed; a component set is called separable when every $\\sigma_i/\\sigma_1$ lies "
    "above it. Under either three-column set the whole spectrum clears $\\tau$ by an order "
    "of magnitude, so the verdict is not a threshold decision -- including under the "
    "adversarial set, which was designed to fail and does not. Under the six-column union "
    "$\\tau$ falls inside the spectrum, between $\\sigma_4$ and $\\sigma_5$: the rank is 4 "
    "of 6 and the set is inseparable at $\\kappa = 629$. Every singular value shown is "
    "resolved under the pre-registered h-plateau criterion (largest variation factor 1.023 "
    "against an admissible 2), so the rank deficiency is a property of the matrix and not "
    "of the estimator. The contrast between the two panels' worth of evidence is the scope "
    "restriction of DECISIONS.md D-14: the positive result holds at one distortion "
    "parameter per component and fails at two."
)


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["FAMILY"])
    prov = vp.FigureProvenance("fig3_spectrum", script=SCRIPT)
    doc = prov.source(SRC)
    sb = doc["summary_sets"]["S_B"]
    tau = prov.plotted("registered tau", [doc["thresholds_pre_registered"]["tau"]], SRC,
                       "thresholds_pre_registered.tau")[0]

    fig, ax = plt.subplots(figsize=(style.FIG_TWOTHIRDS, 2.05))

    for i, (block, colour_key, label) in enumerate(CASES):
        ratios = prov.plotted(
            f"S_B {block} sigma_i/sigma_1", sb[block]["spectrum"]["sigma_i_over_sigma_1"],
            SRC, f"summary_sets.S_B.{block}.spectrum.sigma_i_over_sigma_1")
        kappa = prov.plotted(
            f"S_B {block} kappa", [sb[block]["condition_number"]], SRC,
            f"summary_sets.S_B.{block}.condition_number")[0]
        verdict = sb[block]["verdict"]
        mark = "INSEPARABLE" if sb[block]["inseparable"] else "separable"
        ax.plot(range(1, len(ratios) + 1), ratios,
                marker=("o" if not sb[block]["inseparable"] else "s"),
                markerfacecolor=("none" if sb[block]["inseparable"] else style.FAMILY[colour_key]),
                color=style.FAMILY[colour_key], dashes=style.DASHES[i][1] or (),
                linewidth=1.1, markersize=3.6, markeredgewidth=0.9,
                label=f"{label}  ($\\kappa={kappa:.3g}$, {mark})", zorder=3 - i * 0.1)
        assert verdict  # recorded, and reported in the label above

    ax.axhspan(5e-4, tau, color=style.FAINT, alpha=0.22, linewidth=0, zorder=0)
    style.threshold_line(ax, tau, r"registered $\tau = 10^{-2}$")
    ax.set_yscale("log")
    ax.set_xlabel("singular-value index $i$")
    ax.set_ylabel(r"$\sigma_i / \sigma_1$   (dimensionless)")
    ax.set_xlim(0.7, 6.3)
    ax.set_xticks(range(1, 7))
    ax.set_ylim(5e-4, 2.0)
    ax.legend(loc="lower left", fontsize=style.SIZE_TICK, borderpad=0.2)
    rank = sb["six_columns"]["numerical_rank"]["rank_certain"]
    ncol = sb["six_columns"]["n_columns"]
    ax.text(0.985, 0.97,
            f"union: rank {rank} of {ncol}\n"
            r"$\tau$ falls between $\sigma_4$ and $\sigma_5$"
            "\n"
            r"($\sigma_5,\sigma_6$ below $\tau$)",
            transform=ax.transAxes, ha="right", va="top",
            fontsize=style.SIZE_TICK, color=style.FAMILY["union"], linespacing=1.25)
    fig.tight_layout(pad=0.2)

    out = style.save(fig, REPO / STEM, script=SCRIPT)
    plt.close(fig)
    prov.note("sigma_i/sigma_1 is a recorded field, not computed here; the decision rule "
              "sigma_i >= tau*sigma_1 acts on exactly this ratio, which is why the threshold "
              "is one horizontal line across three series of different absolute scale.")
    prov.note("The annotation naming rank 4 of 6 is placed by hand and is NOT covered by the "
              "data_matches_source check; the rank it states is "
              f"{sb['six_columns']['numerical_rank']['rank_certain']} of "
              f"{sb['six_columns']['n_columns']} in the source file.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
