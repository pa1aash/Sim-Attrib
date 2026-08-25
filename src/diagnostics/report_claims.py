"""Generate ``results/FINAL_CLAIMS_NUMBERS.md`` -- every load-bearing number in the paper.

Standing constraint S11 forbids hand-typing a number into a markdown file. ``audit/FINAL_CLAIMS.md``
is the document a drafting session will work from directly, so it is the one place where a
transcription error would propagate straight into the manuscript. This module emits the
numbers it rests on, each with the **exact dotted path** in the exact ``results/`` file it
came from, and ``audit/FINAL_CLAIMS.md`` reproduces the table verbatim.

**What this is not.** It is not a claim checker. It cannot tell whether a claim's prose
describes the number beside it, only that the number is what the file records. That
judgement belongs to a reader, and it is exactly what operator point **P-2** asks for.

**What would make it fail.** Any path below that no longer exists raises, naming itself. A
results-file schema change therefore breaks this table loudly rather than silently emitting a
blank cell -- the same discipline ``src/viz/provenance.py`` applies to figures.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Any, Callable

import yaml

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results" / "FINAL_CLAIMS_NUMBERS.md"
TEX_OUT = REPO / "paper" / "appendix_claims_table.tex"

JAC_B = "results/jacobian_rank.S_B.yaml"
JAC_C = "results/jacobian_rank.S_C.yaml"
NOCRN = "results/jacobian_rank.S_A.no_crn_control.yaml"
FLOOR = "results/floor_check.yaml"
K6 = "results/robustness/k6_spectrum.yaml"
ALTSCALE = "results/robustness/alt_eta_scaling.yaml"
PSEL = "results/p_sel.yaml"
GATE = "results/cost_gate.yaml"
BOUND = "results/boundary_sweep.yaml"
CONFSET = "results/confidence_set_mmc.yaml"

CODES = ("BBB", "BBA", "BAB", "BAA", "ABB", "ABA", "AAB", "AAA")


def dig(doc: Any, path: str, src: str) -> Any:
    cur = doc
    for part in path.split("."):
        if part.endswith("]"):
            key, idx = part[:-1].split("[")
            if key:
                cur = cur[key]
            cur = cur[int(idx)]
        else:
            try:
                cur = cur[part]
            except (KeyError, TypeError, IndexError) as exc:
                raise KeyError(f"{src}: no path {path!r} (failed at {part!r})") from exc
    return cur


def g(n: float, sig: int = 4) -> str:
    if isinstance(n, bool):
        return str(n)
    if isinstance(n, int):
        return f"{n:,}"
    if n == 0:
        return "0"
    if math.isinf(n):
        return "∞"
    # Values that sit just above 1 are variation factors, and four significant figures
    # rounds "1.000114" to "1" -- which reads as "exactly unchanged" rather than as
    # "changed in the fifth digit". Those are the rows the resolution criterion turns on.
    if 1.0 < abs(n) < 1.1:
        return f"{n:.7g}"
    if abs(n) >= 1e-3 and abs(n) < 1e5:
        return f"{n:.{sig}g}"
    return f"{n:.3e}"


def cell(s: str) -> str:
    """A markdown table cell. `|` is the column separator, so any literal one -- a case key
    like ``AAA|studentised``, or an absolute value ``|z|`` -- has to be escaped or the table
    silently loses a column and every heading after it shifts."""
    return s.replace("|", r"\|")


#: (contribution, what the number is, source file, dotted path, post-processing)
ROWS: tuple[tuple[str, str, str, str, Callable[[Any], Any] | None], ...] = (
    # --- C1: the diagnostic -------------------------------------------------------------
    ("C1", "rank tolerance τ, pre-registered", JAC_B, "thresholds_pre_registered.tau_rank_tolerance", None),
    ("C1", "condition-number ceiling κ_max, pre-registered", JAC_B, "thresholds_pre_registered.kappa_max", None),
    ("C1", "resolution factor (h-plateau), pre-registered", JAC_B, "thresholds_pre_registered.resolve_factor", None),
    ("C1", "plateau relative tolerance", JAC_B, "thresholds_pre_registered.plateau_rel_tol.value", None),
    ("C1", "equivalence-class loading threshold v_k,min", JAC_B, "thresholds_pre_registered.vk_min_equivalence_class", None),
    ("C1", "coherence flag threshold", JAC_B, "thresholds_pre_registered.coherence_flag", None),
    ("C1", "invisible-component column-norm threshold", JAC_B, "thresholds_pre_registered.colnorm_invisible", None),
    ("C1", "step sizes swept (decades)", JAC_B, "thresholds_pre_registered.h_values", len),
    ("C1", "S_B: plateau found across the whole sweep", JAC_B, "results.plateau.n_h_in_plateau", None),
    ("C1", "S_B: largest singular-value variation factor across the plateau", JAC_B, "results.singular_value_variation_factor", max),
    ("C1", "NEGATIVE CONTROL, no CRN: plateau found?", NOCRN, "results.plateau.found", None),
    ("C1", "NEGATIVE CONTROL, no CRN: h values inside the plateau", NOCRN, "results.plateau.n_h_in_plateau", None),
    ("C1", "POSITIVE CONTROL S_C (d = 2 < K): rank at τ", JAC_C, "results.numerical_rank.rank_certain", None),
    ("C1", "POSITIVE CONTROL S_C: condition number", JAC_C, "results.condition_number", None),
    ("C1", "POSITIVE CONTROL S_C: verdict", JAC_C, "results.inseparable_reason", None),
    ("C1", "random-attributor floor 1/K, analytic", FLOOR, "floor_check.floor_analytic", None),
    ("C1", "random-attributor floor, as run", FLOOR, "floor_check.accuracy_simulated", None),
    ("C1", "floor check passes", FLOOR, "floor_check.passes", None),
    # --- C2: the eight-assignment separability result ------------------------------------
    ("C2", "S_B, number of family assignments tested", K6, "summary_sets.S_B.mixed_triples", len),
    ("C2", "S_B, number separable", K6, "summary_sets.S_B.mixed_triples",
     lambda d: sum(1 for c in CODES if d[c]["verdict"] == "separable")),
    ("C2", "S_B, smallest κ over the eight (BAB)", K6, "summary_sets.S_B.mixed_triples",
     lambda d: min(d[c]["condition_number"] for c in CODES)),
    ("C2", "S_B, largest κ over the eight (ABA)", K6, "summary_sets.S_B.mixed_triples",
     lambda d: max(d[c]["condition_number"] for c in CODES)),
    ("C2", "S_B, κ under the declared base set BBB", K6, "summary_sets.S_B.base.condition_number", None),
    ("C2", "S_B, κ under the declared adversarial set AAA", K6, "summary_sets.S_B.adversarial.condition_number", None),
    ("C2", "S_B, worst singular-value variation factor over the eight", K6,
     "summary_sets.S_B.mixed_triples",
     lambda d: max(max(d[c]["singular_value_variation_factor"]) for c in CODES)),
    ("C2", "S_B, leakage check passes on all eight", K6, "summary_sets.S_B.mixed_triples",
     lambda d: all(d[c]["leakage_check_passes"] for c in CODES)),
    ("C2", "S_B, smallest τ* margin over the eight (× registered τ)", K6,
     "summary_sets.S_B.mixed_triples",
     lambda d: min(d[c]["tau_sensitivity"]["exact_flip_point"]["as_multiple_of_registered_tau"]
                   for c in CODES)),
    ("C2", "S_B base, τ* margin (× registered τ)", K6,
     "summary_sets.S_B.base.tau_sensitivity.exact_flip_point.as_multiple_of_registered_tau", None),
    ("C2", "CONTRAST S_A, number separable of eight", K6, "summary_sets.S_A.mixed_triples",
     lambda d: sum(1 for c in CODES if d[c]["verdict"] == "separable")),
    ("C2", "CONTRAST S_A, κ at its knife-edge failure ABB", K6,
     "summary_sets.S_A.mixed_triples.ABB.condition_number", None),
    ("C2", "replicates per Jacobian column R", K6, "settings.R", None),
    ("C2", "replicates for the normalisation R_norm", K6, "settings.R_norm", None),
    ("C2", "AAA under MLE-SE-based scaling: κ", ALTSCALE,
     "eight_assignment_triples.AAA.mle_se_based.kappa", None),
    ("C2", "AAA under MLE-SE-based scaling: separable", ALTSCALE,
     "eight_assignment_triples.AAA.mle_se_based.separable", None),
    ("C2", "BBB under MLE-SE-based scaling: κ", ALTSCALE,
     "eight_assignment_triples.BBB.mle_se_based.kappa", None),
    ("C2", "BBB under MLE-SE-based scaling: separable", ALTSCALE,
     "eight_assignment_triples.BBB.mle_se_based.separable", None),
    # --- C3: the K = 6 boundary ----------------------------------------------------------
    ("C3", "S_B six-column κ", K6, "summary_sets.S_B.six_columns.condition_number", None),
    ("C3", "S_B six-column rank at τ", K6, "summary_sets.S_B.six_columns.numerical_rank.rank_certain", None),
    ("C3", "S_B six-column columns", K6, "summary_sets.S_B.six_columns.n_columns", None),
    ("C3", "S_B six-column spectrum spread (decades)", K6,
     "summary_sets.S_B.six_columns.spectrum.spread_decades_over_positive_singular_values", None),
    ("C3", "S_B six-column gap prominence (largest ÷ median adjacent ratio)", K6,
     "summary_sets.S_B.six_columns.spectrum.gap_prominence_largest_over_median_adjacent_ratio", None),
    ("C3", "S_B six-column: where τ·σ₁ sits", K6,
     "summary_sets.S_B.six_columns.spectrum.where_tau_sigma1_sits", None),
    ("C3", "S_B six-column structurally zero singular values", K6,
     "summary_sets.S_B.six_columns.spectrum.n_structurally_zero", None),
    ("C3", "S_B six-column worst variation factor (estimator resolved?)", K6,
     "summary_sets.S_B.six_columns.singular_value_variation_factor", max),
    ("C3", "S_B six-column INSEPARABLE stable over τ from", K6,
     "summary_sets.S_B.six_columns.tau_sensitivity.coupled_stability.stable_over_tau_range[0]", None),
    ("C3", "S_B six-column INSEPARABLE stable over τ to", K6,
     "summary_sets.S_B.six_columns.tau_sensitivity.coupled_stability.stable_over_tau_range[1]", None),
    ("C3", "S_B six-column flips to separable only at τ", K6,
     "summary_sets.S_B.six_columns.tau_sensitivity.coupled_stability.flips_at_next_tau_below", None),
    ("C3", "near-null direction 1: σ", K6,
     "summary_sets.S_B.six_columns.near_null_directions[0].singular_value", None),
    ("C3", "near-null direction 1: σ/σ₁", K6,
     "summary_sets.S_B.six_columns.near_null_directions[0].sigma_ratio_to_sigma1", None),
    ("C3", "near-null direction 1: kind", K6,
     "summary_sets.S_B.six_columns.near_null_classification[0].kind", None),
    ("C3", "near-null direction 1: transmission energy", K6,
     "summary_sets.S_B.six_columns.near_null_classification[0].mechanism_energy.transmission", None),
    ("C3", "near-null direction 2: σ", K6,
     "summary_sets.S_B.six_columns.near_null_directions[1].singular_value", None),
    ("C3", "near-null direction 2: σ/σ₁", K6,
     "summary_sets.S_B.six_columns.near_null_directions[1].sigma_ratio_to_sigma1", None),
    ("C3", "near-null direction 2: kind", K6,
     "summary_sets.S_B.six_columns.near_null_classification[1].kind", None),
    ("C3", "near-null direction 2: transmission energy", K6,
     "summary_sets.S_B.six_columns.near_null_classification[1].mechanism_energy.transmission", None),
    ("C3", "six-column under MLE-SE-based scaling: κ", ALTSCALE,
     "six_column.mle_se_based.kappa", None),
    ("C3", "six-column under MLE-SE-based scaling: rank at τ", ALTSCALE,
     "six_column.mle_se_based.rank_at_tau", None),
    ("C3", "six-column under MLE-SE-based scaling: separable", ALTSCALE,
     "six_column.mle_se_based.separable", None),
    # --- C4: the MMC non-termination result ----------------------------------------------
    ("C4", "null draws taken to measure p_sel", PSEL, "settings.n_simulator_runs", None),
    ("C4", "p_sel at θ₀, worst cell, AAA studentised", PSEL,
     "stage_A_theta0.AAA|studentised.p_sel", min),
    ("C4", "p_sel at θ₀, 95% CI lower", PSEL, "stage_A_theta0.AAA|studentised.ci95_lower", min),
    ("C4", "p_sel at θ₀, 95% CI upper", PSEL, "stage_A_theta0.AAA|studentised.ci95_upper", min),
    ("C4", "cost at θ₀, cheapest declared (M, N)", GATE,
     "cost_floor_theta_known.AAA|studentised.corners[0].expected_draws", None),
    ("C4", "cost at θ₀, dearest declared (M, N)", GATE,
     "cost_floor_theta_known.AAA|studentised.corners[3].expected_draws", None),
    ("C4", "pre-registered gate, simulator draws", GATE, "gate.threshold_draws", None),
    ("C4", "HEADLINE p_sel over the nuisance box", GATE, "headline.p_sel", None),
    ("C4", "HEADLINE 95% upper bound on p_sel", GATE, "headline.p_sel_ci95[1]", None),
    ("C4", "HEADLINE verdict", GATE, "headline.verdict", None),
    ("C4", "the confidence interval decides the gate", GATE, "headline.ci_decides_the_gate", None),
    ("C4", "cost floor at the CI upper bound, cheapest corner", GATE,
     "headline.expected_draws_ci95_lower_range[0]", None),
    ("C4", "cost floor at the CI upper bound, dearest corner", GATE,
     "headline.expected_draws_ci95_lower_range[1]", None),
    ("C4", "boundary sweep: null draws", BOUND, "settings.n_simulator_runs", None),
    ("C4", "boundary sweep: shape of the collapse (primary)", BOUND,
     "shape_of_the_collapse.AAA|studentised.shape", None),
    ("C4", "boundary sweep: slope ratio against a threshold of 3", BOUND,
     "shape_of_the_collapse.AAA|studentised.slope_ratio", None),
    ("C4", "boundary sweep: decades of p per unit half-width", BOUND,
     "shape_of_the_collapse.AAA|studentised.loglinear_fit.slope_b_decades_per_unit_half_width", None),
    ("C4", "boundary sweep: R² of that fit (descriptive)", BOUND,
     "shape_of_the_collapse.AAA|studentised.loglinear_fit.r_squared", None),
    ("C4", "median ‖E[z]‖ ÷ √d at w = 0.005", BOUND,
     "per_width[3].nuisance_shift_norm_of_mean_z.median_over_noise", None),
    ("C4", "median ‖E[z]‖ ÷ √d at w = 0.0075", BOUND,
     "per_width[4].nuisance_shift_norm_of_mean_z.median_over_noise", None),
    ("C4", "single-draw noise magnitude √d", BOUND,
     "per_width[0].nuisance_shift_norm_of_mean_z.single_draw_noise_magnitude_sqrt_d", None),
    ("C4", "design points with a dead cell at w = 0.05 (of 42)", BOUND,
     "per_width[9].by_key.AAA|studentised.n_design_points_with_a_dead_cell", None),
    ("C4", "θ₀ reproduction: maximum two-proportion |z|", BOUND, "checks.theta0_max_abs_z", None),
    ("C4", "θ₀ reproduction: threshold", BOUND, "checks.theta0_z_threshold", None),
    # --- C5: the confidence-set-bounded MMC check (session G11, T1-3) ---------------------
    ("C5", "confidence level α1", CONFSET, "alpha1", None),
    ("C5", "Bonferroni z (α1/2K per coordinate)", CONFSET, "z_bonferroni", None),
    ("C5", "θ̂ (MLE), beta", CONFSET, "mle_fit.theta_hat.beta", None),
    ("C5", "θ̂ (MLE), gamma", CONFSET, "mle_fit.theta_hat.gamma", None),
    ("C5", "θ̂ (MLE), rho", CONFSET, "mle_fit.theta_hat.rho", None),
    ("C5", "θ̂ (MLE), I0", CONFSET, "mle_fit.theta_hat.I0", None),
    ("C5", "θ̂ (MLE), obs_sigma", CONFSET, "mle_fit.theta_hat.obs_sigma", None),
    ("C5", "MLE gradient converged (scaled max |g| below tolerance)", CONFSET,
     "checks.mle_gradient_near_zero", None),
    ("C5", "observed information matrix positive definite", CONFSET,
     "checks.hessian_is_positive_definite", None),
    ("C5", "data-implied relative half-width, beta", CONFSET,
     "confidence_set_box.beta.relative_half_width", None),
    ("C5", "data-implied relative half-width, gamma", CONFSET,
     "confidence_set_box.gamma.relative_half_width", None),
    ("C5", "data-implied relative half-width, rho", CONFSET,
     "confidence_set_box.rho.relative_half_width", None),
    ("C5", "data-implied relative half-width, I0", CONFSET,
     "confidence_set_box.I0.relative_half_width", None),
    ("C5", "data-implied relative half-width, obs_sigma", CONFSET,
     "confidence_set_box.obs_sigma.relative_half_width", None),
    ("C5", "affordable at θ̂: worst cell p_sel (AAA studentised)", CONFSET,
     "anchor_theta_hat.AAA|studentised.reported_min.p_sel", None),
    ("C5", "affordable at θ̂: gate verdict", CONFSET,
     "anchor_theta_hat.AAA|studentised.gate.verdict", None),
    ("C5", "inside the confidence-set box: worst cell p_sel (AAA studentised)", CONFSET,
     "by_key.AAA|studentised.reported_min.p_sel", None),
    ("C5", "inside the confidence-set box: gate verdict (AAA studentised)", CONFSET,
     "by_key.AAA|studentised.gate.verdict", None),
    ("C5", "inside the confidence-set box: gate verdict (AAA plain)", CONFSET,
     "by_key.AAA|plain.gate.verdict", None),
    ("C5", "inside the confidence-set box: gate verdict (BBB studentised)", CONFSET,
     "by_key.BBB|studentised.gate.verdict", None),
    ("C5", "inside the confidence-set box: fraction of design points with a dead cell "
     "(AAA studentised)", CONFSET,
     "by_key.AAA|studentised.fraction_of_design_points_with_a_dead_cell", None),
    ("C5", "session verdict (both variants of the primary assignment)", CONFSET,
     "session_verdict.verdict", None),
    ("C5", "simulator draws taken for this check", CONFSET, "settings.n_simulator_runs", None),
    ("C5", "design points (32 corners + 10 axis endpoints of the data-implied box)", CONFSET,
     "settings.n_design_points", None),
)

TITLES = {
    "C1": "C1: the rank and coherence diagnostic (method)",
    "C2": "C2: the eight-assignment separability result for `S_B` (positive)",
    "C3": "C3: the `K = 6` cross-mechanism confound (boundary)",
    "C4": "C4: the MMC non-termination result (cautionary)",
    "C5": "C5: the confidence-set-bounded MMC check",
}


def render() -> str:
    docs: dict[str, Any] = {}
    L = ["<!-- GENERATED by src/diagnostics/report_claims.py from the results/ files named in",
         "     the 'source' column. Do not edit. Standing constraint S11. -->",
         "",
         "### Every load-bearing number in `audit/FINAL_CLAIMS.md`, and where it comes from",
         "",
         "One row per number the paper's four claims rest on. The **path** column is the exact "
         "dotted path in the named file, so a reader can check any row without running "
         "anything.",
         ""]
    for c in ("C1", "C2", "C3", "C4", "C5"):
        L += ["", f"#### {TITLES[c]}", "",
              "| quantity | value | source | path |", "|---|---|---|---|"]
        for contrib, label, src, path, fn in ROWS:
            if contrib != c:
                continue
            if src not in docs:
                docs[src] = yaml.safe_load((REPO / src).read_text(encoding="utf-8"))
            raw = dig(docs[src], path, src)
            val = fn(raw) if fn else raw
            shown = g(val) if isinstance(val, (int, float)) else str(val)
            L.append(f"| {cell(label)} | `{cell(shown)}` | `{src}` | `{cell(path)}` |")
    L += ["", "**Provenance of the source files.**", "",
          "| file | script | commit | dirty | seed |", "|---|---|---|---|---|"]
    for src in sorted(docs):
        p = docs[src].get("provenance", {})
        L.append(f"| `{src}` | `{p.get('script')}` | `{str(p.get('commit'))[:7]}` | "
                 f"`{p.get('dirty')}` | `{p.get('seed')}` |")
    L.append("")
    return "\n".join(L) + "\n"


#: Unicode math substrings appearing in ROWS' labels, longest/most-specific first, mapped to
#: real LaTeX math. plain `pdflatex` + `inputenc[utf8]` does not render Greek letters or math
#: operators as text glyphs in the venue's font -- they need to be inside `$...$` as macros, or
#: the compile either errors or drops the character. Compound sequences (a base letter plus a
#: combining accent or a subscript digit) are listed before the single characters they contain,
#: so they are matched whole rather than leaving a stray accent or subscript behind.
MATH_SUBSTITUTIONS: tuple[tuple[str, str], ...] = (
    ("θ̂", r"$\hat{\theta}$"), ("θ₀", r"$\theta_0$"), ("σ₁", r"$\sigma_1$"),
    ("√d", r"$\sqrt{d}$"), ("R²", r"R$^2$"),
    ("α", r"$\alpha$"), ("θ", r"$\theta$"), ("κ", r"$\kappa$"), ("σ", r"$\sigma$"),
    ("τ", r"$\tau$"), ("‖", r"$\|$"), ("×", r"$\times$"), ("÷", r"$\div$"),
    ("·", r"$\cdot$"), ("∞", r"$\infty$"), ("²", r"$^2$"), ("₀", r"$_0$"), ("₁", r"$_1$"),
    ("—", "--"),
)


def tex_escape(s: str) -> str:
    """Escape a string for use as LaTeX table text, protecting math substitutions first.

    Unicode math substrings are swapped for placeholder tokens before the ordinary LaTeX
    special characters (``_``, ``%``, ``&``, ...) are escaped, then swapped back in as real
    (unescaped) LaTeX math -- otherwise, e.g., the underscore inside a substituted
    ``$\\sigma_1$`` would itself be escaped to ``\\_``, breaking the subscript it was meant to
    render. Applied to every label, value, and title.
    """
    placeholders: list[str] = []
    out = s
    for pattern, latex in MATH_SUBSTITUTIONS:
        if pattern in out:
            token = f"\x00{len(placeholders)}\x00"
            placeholders.append(latex)
            out = out.replace(pattern, token)
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("_", r"\_"),
                ("#", r"\#"), ("$", r"\$"), ("{", r"\{"), ("}", r"\}")):
        out = out.replace(a, b)
    for i, latex in enumerate(placeholders):
        out = out.replace(f"\x00{i}\x00", latex)
    return out


def tex_breakable(s: str) -> str:
    """As :func:`tex_escape`, plus break opportunities after ``.``/``_``/``|`` in `texttt` text.

    A dotted path like ``by_key.AAA|studentised.fraction_of_design_points_with_a_dead_cell``
    is one unbroken "word" to (pdf)LaTeX's line breaker -- `cmtt`/`ptm` typewriter text does
    not hyphenate -- so without an explicit break opportunity at each separator, a long path
    overflows its table column instead of wrapping. No extra package is required for this.
    """
    out = tex_escape(s)
    for sep in (r"\_", r".", r"|"):
        out = out.replace(sep, sep + r"\allowbreak{}")
    return out


def render_latex() -> str:
    """Appendix A.3, as a set of `longtable`s -- one per claim, generated rather than typed.

    This is the object `paper/main.tex`'s Appendix~A.3 `\\input`s. It reuses exactly the same
    `ROWS`/`dig` machinery as :func:`render`, so the two can never drift: a path that resolves
    for the markdown table resolves identically here, and a broken path raises in both.
    """
    docs: dict[str, Any] = {}
    # NOTE: this file is generated. It ships as part of the submission source, so -- unlike
    # the sibling markdown render() above -- nothing in it may name an internal repository
    # path, script, or session/process identifier; only the measurement files a reader could
    # plausibly be given (results/*.yaml) are named, in the table body itself.
    L = [r"% Generated programmatically from the underlying measurement files; not hand-typed.",
         ""]
    for c in ("C1", "C2", "C3", "C4", "C5"):
        title = tex_escape(TITLES[c].replace("`", ""))
        L += [r"\subsubsection*{" + title + "}",
              r"\begin{longtable}{p{0.35\linewidth} p{0.14\linewidth} p{0.41\linewidth}}",
              r"\toprule",
              r"quantity & value & source (file, path) \\",
              r"\midrule",
              r"\endhead"]
        for contrib, label, src, path, fn in ROWS:
            if contrib != c:
                continue
            if src not in docs:
                docs[src] = yaml.safe_load((REPO / src).read_text(encoding="utf-8"))
            raw = dig(docs[src], path, src)
            val = fn(raw) if fn else raw
            shown = g(val) if isinstance(val, (int, float)) else str(val)
            src_short = src.replace("results/", "")
            L.append(f"{tex_escape(label)} & {tex_escape(shown)} & "
                     f"\\texttt{{\\footnotesize {tex_breakable(src_short)}}}, "
                     f"\\texttt{{\\footnotesize {tex_breakable(path)}}} \\\\")
        L += [r"\bottomrule", r"\end{longtable}", ""]
    L += [r"\paragraph{Provenance of the source files.}",
         r"\begin{longtable}{p{0.45\linewidth} p{0.25\linewidth} p{0.20\linewidth}}",
         r"\toprule", r"file & commit & seed \\", r"\midrule", r"\endhead"]
    for src in sorted(docs):
        p = docs[src].get("provenance", {})
        L.append(f"\\texttt{{\\footnotesize {tex_escape(src.replace('results/', ''))}}} & "
                 f"\\texttt{{\\footnotesize {tex_escape(str(p.get('commit'))[:7])}}} & "
                 f"{tex_escape(str(p.get('seed')))} \\\\")
    L += [r"\bottomrule", r"\end{longtable}", ""]
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="generate results/FINAL_CLAIMS_NUMBERS.md")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--tex-out", default=str(TEX_OUT))
    args = ap.parse_args(argv)
    Path(args.out).write_text(render(), encoding="utf-8")
    Path(args.tex_out).write_text(render_latex(), encoding="utf-8")
    print(f"wrote {args.out} and {args.tex_out}  ({len(ROWS)} numbers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
