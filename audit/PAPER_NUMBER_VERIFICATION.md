# Every number in `paper/main.tex`'s prose, and where it comes from

**Session G8, 2026-08-22.** Phase 4.1 of this session's brief: a verification pass over
every numeric claim in the paper's prose, checked against `audit/FINAL_CLAIMS.md`'s
generated appendix (dotted paths into `results/*.yaml`) or, where a number is stated in
prose in `audit/K6_SPECTRUM_CHECK.md` / `audit/MMC_COMPOSITION_SPEC.md` rather than
tabulated, against that document's own generated tables.

**Scope.** This is a manual pass, not a script, done section by section against the
draft as committed. It covers `paper/main.tex`'s prose (Introduction through
Limitations); it does **not** re-verify numbers inside figure captions or the figures
themselves, because those already carry their own `data_matches_source` check from
figure-generation time (`figures/*.provenance.json`, session G7) — re-deriving that
machinery here would duplicate a check that already exists and already passes. It does
not yet cover the appendix's generated-numbers table (Section 3 of the appendix), which
is a verbatim reproduction of `results/FINAL_CLAIMS_NUMBERS.md` and is TODO pending
Phase 4.3 (compile/reference check) confirming the reproduction is complete.

**The vacuous-flag test (S6).** This pass would fail, and is capable of failing, if: a
number in the prose does not appear (to reasonable rounding) at the cited dotted path;
if the cited path does not exist in the named file; or if a number is present in the
prose with no traceable source at all. Two of the rows below required tracking down a
value stated only in a source document's prose (not its generated table) — those are
marked **prose-sourced** rather than **table-sourced**, which is a weaker form of
traceability worth disclosing rather than treating as equivalent.

---

## Method (Section 3)

| Number in prose | Source | Path / location | Status |
|---|---|---|---|
| $\tau = 10^{-2}$ | `docs/THRESHOLDS.md` §1.2 | registered value | MATCH |
| $\kappa_{\max} = 1/\tau = 100$ | `docs/THRESHOLDS.md` §1.3 | registered value | MATCH |
| resolution factor 2 (h-plateau) | `docs/THRESHOLDS.md` §1.4 | registered value | MATCH |
| "$\kappa=100$ ... exhausts this study's budget" | `docs/THRESHOLDS.md` §1.2 | prose: *"κ = 100 ... is the point at which separating the components costs more than the study's entire declared simulation budget"* | MATCH (prose-sourced, near-verbatim) |
| $|v_k|\ge 0.3$ equivalence-class threshold | `docs/THRESHOLDS.md` §2.1 | registered value | MATCH |
| two-component confound $\approx 0.707$, three-component $\approx 0.577$ | `docs/THRESHOLDS.md` §2.1 | derivation ($1/\sqrt2$, $1/\sqrt3$) | MATCH (arithmetic, not tabulated) |
| coherence flag $\mu\approx0.9998$ | `docs/THRESHOLDS.md` §2.2 | derivation from $\kappa_{\max}=100$ | MATCH |

## Experiments (Section 4)

| Number in prose | Source | Path | Status |
|---|---|---|---|
| $S_C$: $d=2<K=3$, rank 2, $\kappa=\infty$ | `results/jacobian_rank.S_C.yaml` via `audit/FINAL_CLAIMS.md` appendix | `results.numerical_rank.rank_certain`, `results.condition_number` | MATCH |
| floor $1/K$ analytic 0.3333 | `results/floor_check.yaml` | `floor_check.floor_analytic` | MATCH |
| floor measured 0.3299 | `results/floor_check.yaml` | `floor_check.accuracy_simulated` | MATCH |
| "over 10,000 draws" | `audit/FINAL_CLAIMS.md` C1 prose | *"0.3299 as actually run over 10,000 draws"* | MATCH (prose-sourced) |
| $S_B$ $\kappa$: 6.628 to 65.64 | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.mixed_triples` (BAB, ABA) | MATCH |
| $S_A$ ABB failure $\kappa=100.9$, "0.9% past ceiling" | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_A.mixed_triples.ABB.condition_number` | MATCH (0.9% computed: $100.9/100-1$) |
| margins $9.881\times$ / $1.523\times$ | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.base.tau_sensitivity...`, smallest margin over the eight | MATCH |
| six-column $\kappa=628.9$, rank 4/6 | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.condition_number`, `.numerical_rank.rank_certain` | MATCH |
| worst variation factor 1.023 vs admissible 2 | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.singular_value_variation_factor` (1.02254, rounded) | MATCH |
| inseparable across $\tau\in[0.005,1.0]$ | `results/robustness/k6_spectrum.yaml` | `...tau_sensitivity.coupled_stability.stable_over_tau_range` | MATCH |
| $d=10\ge6$, structural zeros 0 | `audit/K6_SPECTRUM_CHECK.md` §2.2 | prose: *"S_B has d = 10 ≥ 6 ... n_structurally_zero = 0"* | MATCH (prose-sourced) |
| transmission energy $<5\%$ in either direction | `results/robustness/k6_spectrum.yaml` | `...near_null_classification[0/1].mechanism_energy.transmission` (0.04297, 0.04463) | MATCH |
| spread 2.80 decades, gap prominence 1.40 | `results/robustness/k6_spectrum.yaml` | `...six_columns.spectrum.spread_decades...` (2.799), `.gap_prominence...` (1.402) | MATCH (rounded) |
| $\tau\sigma_1$ inside spectrum, between $\sigma_4,\sigma_5$ | `results/robustness/k6_spectrum.yaml` | `...spectrum.where_tau_sigma1_sits` | MATCH |

## The MMC negative result (Section 5)

| Number in prose | Source | Path | Status |
|---|---|---|---|
| worst cell 23% of null draws | `results/p_sel.yaml` | `stage_A_theta0.AAA\|studentised.p_sel` (0.2346) | MATCH (rounded) |
| cost $4.2\times10^5$ to $4.3\times10^7$ vs gate $10^8$ | `results/cost_gate.yaml` | `cost_floor_theta_known...corners[0/3].expected_draws` (4.220e5, 4.259e7), `gate.threshold_draws` | MATCH (4.259e7 rounds to 4.3e7 at 2 s.f.) |
| $w=5\%$: zero acceptances / 100,000 draws | `results/cost_gate.yaml` | `headline.p_sel` = 0 | MATCH |
| 95% upper bound $3.84\times10^{-5}$ | `results/cost_gate.yaml` | `headline.p_sel_ci95[1]` (3.841e-5) | MATCH |
| cost floor $\ge2.6\times10^9$ | `results/cost_gate.yaml` | `headline.expected_draws_ci95_lower_range[0]` (2.577e9) | MATCH |
| collapse GRADUAL | `results/boundary_sweep.yaml` | `shape_of_the_collapse.AAA\|studentised.shape` | MATCH |
| $R^2=0.94$ | `results/boundary_sweep.yaml` | `...loglinear_fit.r_squared` (0.9424) | MATCH (rounded) |
| "one decade per 0.7% of relative nuisance error" | `audit/MMC_COMPOSITION_SPEC.md` §4.2 | prose, near-verbatim; also derivable from `...slope_b_decades_per_unit_half_width` = -141.2 ($1/141.2\approx0.00708$) | MATCH (prose-sourced + arithmetic cross-check) |
| gate passes at every corner only inside $\pm0.5\%$ | `audit/MMC_COMPOSITION_SPEC.md` §4.2 | prose, table | MATCH |
| crossing between $w=0.5\%$ and $0.75\%$ | `audit/MMC_COMPOSITION_SPEC.md` §4.2 | prose: *"the crossing is at w ≈ 0.0065"*, bracketed by measured points at 0.005 and 0.0075 | MATCH (deliberately stated as a bracket, not the point estimate, since the point estimate itself is a derived quantity rather than a directly measured one) |

---

## What this pass does not certify

- **The appendix's Section 3 (`\input{appendix_tables.tex}`) and Section 4 (generated-numbers
  reproduction)** are checked for internal consistency with `audit/K6_SPECTRUM_CHECK.md`'s own
  generated table (Section 3.1/3.2 there), which they are copied from, but the appendix's own
  TODO for reproducing `results/FINAL_CLAIMS_NUMBERS.md` verbatim is not yet discharged.
- **No independent reader has checked this table.** It was produced by the same session that
  wrote the prose it checks — the same limitation this project's audit trail records for every
  self-check so far (`GATES.md`).
- **Rounding is not re-derived from raw data in every row.** Where a `results/*.yaml` gives a
  value to 4+ significant figures and the prose rounds it, this pass confirms the rounding is
  in the right direction and of a normal magnitude, not that every digit was independently
  recomputed from `src/`.
