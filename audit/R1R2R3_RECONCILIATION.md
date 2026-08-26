# R-1/R-2/R-3 reconciliation — Session G15

**Prepared 2026-08-26, session G15.** Closes the one honest gap G14 left open (`audit/S14_REPORT.md`
§4, GATES.md G14.16/"does not certify"): the second external review's own "R-1/R-2/R-3" cross-check
items (distinct from the *first* review's R1/R2 novelty threat-checks, already resolved separately)
were never individually re-confirmed against the current document. This file does that, checked
directly against `paper/main.tex` and the underlying `results/*.yaml` files — not against G14's own
narration of what it did (S6).

## R-1 — main-text self-sufficiency

**Verdict: CONFIRMED FIXED.**

**Family-description passage.** `paper/main.tex`, Section 4, "Simulator and summary sets" paragraph
(lines 204–207): "transmission's base/adversarial pair is a prevalence-saturating nonlinearity and a
constant multiplier on the transmission rate; progression's is a time-drifting removal hazard and a
constant multiplier on the recovery rate; observation's is a constant reporting-fraction error and a
time-drifting reporting fraction." All six family mechanisms (three components × base/adversarial)
are named in main-text prose, not only in the appendix figure.

Checked directly against `src/simulators/sir3.py`'s own docstring, not against G14's paraphrase of
it: `eta_1` (saturating incidence → "prevalence-saturating nonlinearity"), `eta_1'` (`beta ->
beta*exp(eta_1)`, a constant multiplier on the transmission rate), `eta_2` (log-linear drift in the
removal hazard → "time-drifting removal hazard"), `eta_2'` (`gamma -> gamma*exp(-eta_2)`, a constant
multiplier on the recovery rate — gamma is the removal/recovery rate), `eta_3` (reporting-fraction
multiplier → "constant reporting-fraction error"), `eta_3'` (mean-centred log-linear reporting
trend, `rho -> rho*exp(eta_3*(t/T-0.5))` → "time-drifting reporting fraction"). Every main-text
phrase maps onto its source-code family exactly; none is a loose paraphrase.

**Confound-interpretation sentence.** Section 4 (line 253–254): "a drifting removal hazard is nearly
indistinguishable from a constant hazard change combined with a drifting reporting rate." This
sentence is followable from the family-description passage alone: "drifting removal hazard" =
progression-base, "constant hazard change" = progression-adversarial, "drifting reporting rate" =
observation-adversarial — all three named two sentences earlier in the same section, in the same
prose a reader has already seen. A reader does **not** need to open the Figure 7 appendix panel to
parse this sentence; the appendix figure now supplies quantitative evidence (which direction, how
much energy) for a claim the main text already states in words a reader can follow. This is a
genuine fix, not merely reported as one.

## R-2 — ledger under-referencing and undefined criteria

**Verdict: CONFIRMED FIXED.**

**Reference sentence.** Section 4 opens (line 197–198) with: "Every number below traces to a results
file and an exact dotted path, listed in full in Appendix~\ref{sec:claims-ledger}." This is the
first sentence of the first paragraph of Section 4 — before any of that section's other content, not
buried later — merged into the existing "Simulator and summary sets" paragraph opening exactly as
G14 reported.

**Undefined criteria, independently re-checked (not assumed carried forward from G14.5):**
- **"coherence"** — zero occurrences of the word anywhere in `paper/main.tex` (confirmed by direct
  grep). It was removed from main-text prose entirely rather than defined, per the review's own
  "definition added or phrase removed" framing and G14's stated choice of the removal branch under
  page-budget pressure. Since the main text no longer uses or implies the term, it is not an
  undefined criterion the main text exposes; it survives only as one supplementary row in the
  Appendix A.5 ledger (`coherence flag threshold: 0.98`), which is explicitly a secondary/
  interpretive diagnostic per `docs/THRESHOLDS.md` ("rule, on the singular values; coherence for
  interpretation") — not part of the Section 3 decision rule the main text states, which turns on
  $\kappa$/rank alone.
- **"leakage"** — the literal word does not appear in `paper/main.tex` either, but the concept is
  stated in main-text prose without the jargon term: Section 3 states "[the diagnostic] never
  receives a component identity or a ground-truth label, so there is no hidden truth available to
  leak into its answer" (line 168–169). A reader who later meets "leakage check passes" in the
  Appendix A.5 ledger has already been told, in main-text prose, what such a check verifies.
- **"slope-ratio rule"** — stated explicitly and numerically in Section 5 (line 320–322): "gradual
  rather than abrupt (log-slope ratio against a pre-registered threshold of 3; measured
  $2.265\times$)." The rule and the measured value are both present inline, not only in the ledger.

All three of the review's named undefined criteria are independently confirmed resolved.

## R-3 — the Mahalanobis-radius/ellipsoid check

**Verdict: CONFIRMED — independent recomputation matches the paper's stated numbers exactly.**

Recomputed from scratch this session, not by re-reading G14's derivation, directly from
`results/confidence_set_mmc.yaml` (Fisher-information standard errors and correlation matrix at
$\hat\theta$) and `results/boundary_sweep.yaml` (the round-box sweep's worst-cell corner directions
for the primary case, `AAA|studentised`):

- Covariance $\Sigma = D R D$ built from `confidence_set_mmc.yaml`'s `fisher_information.standard_errors`
  and `correlation_matrix`. **Cross-check performed before trusting the inversion**: $\Sigma^{-1}$'s
  eigenvalues were computed and compared against the file's own stored `hessian_eigenvalues` —
  relative agreement to $10^{-13}$–$10^{-16}$ (floating-point noise), confirming the inversion is
  correct.
- Worst-cell corner at $w=0.005$: `boundary_sweep.yaml`'s `AAA|studentised` entry at `width: 0.005`,
  `reported_min.at_point: w0.005|corner|--+--`, gate `verdict: PASS` (all four $(M,N)$ configurations
  pass). Shift vector $\delta_k = \text{sign}_k \cdot w \cdot \theta_{0,k}$, per
  `src/diagnostics/p_sel.py::nuisance_grid`'s own construction (`theta[c] = base[c] * (1.0 + s*w)`).
  **Recomputed Mahalanobis radius: 2.7096** — matches the paper's stated **2.71**.
- Worst-cell corner at $w=0.0075$: same entry at `width: 0.0075`, `reported_min.at_point:
  w0.0075|corner|--++-`, gate `verdict: SPLIT` (one of four $(M,N)$ configurations fails — the first
  width at which any configuration fails, i.e. the smallest box at which the gate first fails).
  **Recomputed Mahalanobis radius: 3.5616** — matches the paper's stated **3.56**.
- 95% joint ellipsoid radius: $\sqrt{\chi^2_{5,0.95}} = 3.3272$ — matches the paper's stated
  **$\approx3.33$**.

**The independent recomputation matches the paper's own stated figures to four significant
figures in every case.** No discrepancy found; nothing to escalate.

**Phrasing check.** Section 5's exact sentence: "The smallest round box at which the gate first
fails ($\pm0.75\%$) sits at Mahalanobis radius $3.56$ under the Fisher information at $\hat\theta$,
against a joint $95\%$ ellipsoid radius $\sqrt{\chi^2_{5,0.95}}\approx3.33$; the last fully-passing
box ($\pm0.5\%$) sits at $2.71$. The failure boundary and a real $95\%$ confidence region coincide
almost exactly." This states both numbers plainly (3.56 vs. 3.33, a difference of about 7%), uses
"coincide almost exactly" rather than either "well inside" (the review's own imprecise guess) or an
overclaiming phrase like "exactly at the edge" (3.56 is past 3.33, not on it). Judged precise and
defensible to an external reviewer: a reader can see the two numbers and their relationship without
having to trust an adjective.

## Summary

| Item | Second review's finding | Status |
|---|---|---|
| R-1 | Main text insufficient for the confound interpretation without the appendix figure | **Fixed, confirmed independently** — six family mechanisms named in Section 4 prose; confound sentence follows from them |
| R-2 | Ledger under-referenced from Sections 3–5; undefined criteria (coherence, leakage, slope-ratio) exposed | **Fixed, confirmed independently** — one reference sentence at the top of Section 4; all three named criteria resolved (two removed from main text, slope-ratio rule stated explicitly) |
| R-3 | Ellipsoid comparison never stated; gap in the confidence-set check | **Fixed, confirmed independently** — recomputation from source YAML matches the paper's 3.56/3.33/2.71 exactly; phrasing judged precise |

This closes the gap `audit/S14_REPORT.md` §4 and `GATES.md` G14.16 left open. The distinction G14
could not resolve — whether the second review's literal "R-1/R-2/R-3" labels are the same items as
the first review's R1/R2 novelty threat-checks — is moot for this reconciliation: this session
worked directly from the second review's full R-1/R-2/R-3 text as supplied in the G15 session brief,
not from either review's label alone, so the ambiguity G14 flagged does not affect the verification
above.
