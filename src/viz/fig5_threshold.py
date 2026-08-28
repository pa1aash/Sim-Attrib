"""Figure 5 -- the separability verdict as a function of the rank tolerance ``tau``.

WHAT THE FIGURE IS FOR
-----------------------
Every separability verdict in this project is a comparison of a measured spectrum against a
number fixed in ``docs/THRESHOLDS.md`` before any singular value existed. The obvious
objection -- Gutenkunst et al.'s, recorded in ``audit/R2_THREAT_CHECK.md`` §1.3 -- is that
such a verdict may report where the analyst put `tau` rather than a property of the model.
The answer is not an argument, it is a margin: **how far can `tau` move before the verdict
does?**

The flip point is exact rather than sampled. The rule is `sigma_K >= tau * sigma_1`, so the
verdict flips precisely at `tau* = sigma_K / sigma_1 = 1 / kappa`. The nine sampled
tolerances are drawn as well, because they are what was actually run through the production
`analyse()`, and their agreement with the closed form is a check rather than a decoration.

THE BAND THAT MATTERS MOST
---------------------------
The project's own robustness proposal was *"halve, double, and one order of magnitude
looser"*. `audit/K6_SPECTRUM_CHECK.md` §3 found that under the adversarial families **that
grid straddles the boundary**: `S_B` flips at 1.547x the registered `tau`, so doubling `tau`
changes the answer. The shaded band is that grid, and the figure exists partly so a reader
sees the adversarial flip point falling inside it.

CROSS-CHECK AGAINST THE OTHER RECORDED SWEEP
----------------------------------------------
Two files in this repository record threshold sensitivity for `S_B` base: G4's
``results/robustness/threshold_sensitivity.yaml`` (five tolerances) and G5's
``results/robustness/k6_spectrum.yaml`` (nine, plus the adversarial and six-column cases).
This script reads **both** and requires them to agree on the flip point and on every verdict
at a shared tolerance. **That check can fail**: it is exactly what transcription drift
between two sessions' files would look like, and it is why the figure is drawn from the
recorded sweeps rather than from any prose summary of them.
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
SRC_G4 = "results/robustness/threshold_sensitivity.yaml"
STEM = "figures/fig5_threshold"
SCRIPT = "src/viz/fig5_threshold.py"

LANES = (
    ("base", "base", "BBB, base families, three columns"),
    ("adversarial", "adversarial", "AAA, adversarial families, three columns"),
    ("six_columns", "union", "union, six columns"),
)

CAPTION = (
    "Separability verdict for summary set $S_B$ as a function of the rank tolerance $\\tau$, "
    "with $\\kappa_{\\max}$ held at $1/\\tau$ as docs/THRESHOLDS.md derives it. Filled "
    "circles are the nine tolerances actually run through the production analysis; the "
    "vertical tick on each lane is the exact flip point $\\tau^* = \\sigma_K/\\sigma_1 = "
    "1/\\kappa$, which is closed-form rather than sampled. The vertical dashed line is the "
    "registered $\\tau = 10^{-2}$ and the shaded band is the halve-and-double grid the "
    "project itself proposed for testing it. Under the base families the verdict survives "
    "$\\tau$ moving by a factor of 9.88; under the adversarial families the margin is only "
    "1.547, so the flip point falls inside the project's own coarse grid and doubling $\\tau$ "
    "turns the verdict over. The six-column union is inseparable across $\\tau$ from 0.005 to "
    "1.0 and becomes separable only at $\\tau \\le 10^{-3}$, a tenfold loosening at which "
    "$\\kappa_{\\max}$ rises to 1000 while the measured $\\kappa$ is 629 -- so there is no "
    "tolerance at which the six-column object is both separable and cheap. The lower end of "
    "each lane is censored by the sweep's own grid: at $\\tau = 10^{-4}$ every three-column "
    "verdict is still separable, so the sweep stopped rather than the stability doing so."
)


def build() -> None:
    facts = style.apply_style()
    style.assert_scales_do_not_collide(["FAMILY"])
    prov = vp.FigureProvenance("fig5_threshold", script=SCRIPT)
    doc = prov.source(SRC)
    g4 = prov.source(SRC_G4)
    sb = doc["summary_sets"]["S_B"]
    tau_reg = prov.plotted("registered tau", [doc["thresholds_pre_registered"]["tau"]], SRC,
                           "thresholds_pre_registered.tau")[0]

    # ---- the cross-check between two sessions' recorded sweeps -------------------------
    g4_flip = g4["summary_sets"]["S_B"]["flip_point"]["tau_star"]
    g5_flip = sb["base"]["tau_sensitivity"]["exact_flip_point"]["tau_star_sigma_K_over_sigma_1"]
    if abs(g4_flip - g5_flip) > 1e-12:
        raise ValueError(
            f"the two recorded threshold sweeps disagree on S_B base's flip point: G4 has "
            f"{g4_flip!r} in {SRC_G4}, G5 has {g5_flip!r} in {SRC}. One of them has drifted "
            f"and this figure must not be drawn until it is known which.")
    g5_rows = {r["tau"]: r["verdict"]
               for r in sb["base"]["tau_sensitivity"]["coupled_kappa_max_equals_one_over_tau"]}
    shared = 0
    for row in g4["summary_sets"]["S_B"]["sensitivity"]:
        if row["tau"] in g5_rows and g5_rows[row["tau"]] != row["verdict"]:
            raise ValueError(
                f"the two recorded sweeps disagree at tau = {row['tau']}: G4 says "
                f"{row['verdict']!r}, G5 says {g5_rows[row['tau']]!r}.")
        shared += row["tau"] in g5_rows
    if shared < 3:
        raise ValueError(f"only {shared} tolerances are shared between the two sweeps; the "
                         f"cross-check is too weak to be worth reporting as one.")

    # ---- the figure ---------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(style.FIG_FULL, 2.15))
    lo, hi = 6e-5, 1.7
    ax.axvspan(tau_reg / 2, tau_reg * 2, color=style.FAINT, alpha=0.30, linewidth=0, zorder=0)

    for lane, (block, colour_key, label) in enumerate(LANES):
        y = len(LANES) - 1 - lane
        ts = sb[block]["tau_sensitivity"]
        star = prov.plotted(
            f"S_B {block} exact flip tau*",
            [ts["exact_flip_point"]["tau_star_sigma_K_over_sigma_1"]], SRC,
            f"summary_sets.S_B.{block}.tau_sensitivity.exact_flip_point"
            ".tau_star_sigma_K_over_sigma_1")[0]
        rows = ts["coupled_kappa_max_equals_one_over_tau"]
        taus = prov.plotted(
            f"S_B {block} swept tau", [r["tau"] for r in rows], SRC,
            f"summary_sets.S_B.{block}.tau_sensitivity"
            ".coupled_kappa_max_equals_one_over_tau",
            transform=("tau of each swept row", lambda rs: [r["tau"] for r in rs]))
        verdicts = [r["verdict"] for r in rows]

        c = style.FAMILY[colour_key]
        ax.plot([lo, star], [y, y], color=c, linewidth=5.0, solid_capstyle="butt",
                alpha=0.95, zorder=2)
        ax.plot([star, hi], [y, y], color=c, linewidth=5.0, solid_capstyle="butt",
                alpha=0.25, zorder=2)
        ax.plot([star, star], [y - 0.30, y + 0.30], color=style.INK, linewidth=1.0, zorder=4)
        for t, v in zip(taus, verdicts):
            sep = v == "separable"
            ax.plot([t], [y], marker="o" if sep else "s", markersize=3.4,
                    markerfacecolor=style.PANEL if not sep else style.INK,
                    markeredgecolor=style.INK, markeredgewidth=0.7, zorder=5)
        mult = star / tau_reg
        ax.annotate(rf"$\tau^*={star:.4g}$  (${mult:.3g}\times$ pre-registered)",
                    xy=(star, y + 0.34), xytext=(0, 0), textcoords="offset points",
                    ha="center", va="bottom", fontsize=style.SIZE_SMALL, color=style.INK)
        ax.text(lo * 1.25, y + 0.30, label, ha="left", va="bottom",
                fontsize=style.SIZE_TICK, color=c)

    style.threshold_line(ax, tau_reg, "", axis="x", zorder=3)
    ax.annotate("pre-registered $\\tau=10^{-2}$  (shaded: halve / double)",
                xy=(tau_reg, 1.0), xycoords=("data", "axes fraction"),
                xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=style.SIZE_SMALL, color=style.RULE)

    ax.set_xscale("log")
    ax.set_xlim(lo, hi)
    ax.set_ylim(-0.52, len(LANES) - 0.22)
    ax.set_yticks([])
    ax.set_xlabel(r"rank tolerance $\tau$  (dimensionless), with $\kappa_{\max}=1/\tau$")
    ax.spines["left"].set_visible(False)
    handles = [
        plt.Line2D([], [], color=style.INK, marker="o", linestyle="none", markersize=3.4,
                   markeredgewidth=0.7),
        plt.Line2D([], [], color=style.INK, marker="s", linestyle="none", markersize=3.4,
                   markerfacecolor=style.PANEL, markeredgewidth=0.7),
        plt.Line2D([], [], color=style.INK, linewidth=1.0),
    ]
    fig.legend(handles, ["separable (swept)", "INSEPARABLE (swept)",
                         r"exact flip point $\tau^*=\sigma_K/\sigma_1$"],
               loc="lower center", ncol=3, fontsize=style.SIZE_TICK, handlelength=1.2,
               columnspacing=1.8, bbox_to_anchor=(0.5, 0.0))
    fig.subplots_adjust(left=0.02, right=0.995, bottom=0.36, top=0.86)

    out = style.save(fig, REPO / STEM, script=SCRIPT)
    plt.close(fig)
    prov.note(
        "Cross-check between two sessions' recorded sweeps PASSED: G4's "
        f"{SRC_G4} and G5's {SRC} agree on S_B base's exact flip point to within 1e-12 and on "
        f"the verdict at all {shared} shared tolerances. The figure raises rather than draws "
        "if they disagree, because a disagreement between two files recording the same "
        "quantity is transcription drift and it must not be averaged over.")
    prov.note(
        "The saturated half of each lane is the tolerance range at which the case is "
        "separable and the faded half where it is INSEPARABLE. The boundary between them is "
        "the exact flip point, not an interpolation between swept points: the rule is "
        "sigma_K >= tau*sigma_1, so the flip is at sigma_K/sigma_1 exactly.")
    prov.write(REPO / STEM, caption=CAPTION, style_facts=facts, outputs=out)
    print(f"wrote {STEM}.pdf")


if __name__ == "__main__":
    build()
    sys.exit(0)
