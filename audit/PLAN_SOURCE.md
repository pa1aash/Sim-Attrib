# S2 — Which Component of the Simulator Is Wrong?

**One sentence:** Simulation-based inference can detect and absorb misspecification but cannot say
*which component* is at fault — and the honest reason is that component attribution is **not
identifiable in general**; the contribution is the exact rank condition under which it *is*, plus a
selection-corrected estimator that reports equivalence classes when it isn't.

| | |
|---|---|
| **Target venue** | NeurIPS 2026 **Sim2Science: ML with Imperfect Scientific Models** (Paris) — CFP names "simulator diagnostics and discrepancy modeling" |
| **Deadline / format** | **Aug 29 2026 AoE**, 5 pages (tiny track: 2), refs excluded, **appendix unlimited**, double-blind, non-archival |
| **Backup venue** | AI for Science (Sydney); ICBINB-style failure-modes venues |
| **Prior-art verdict** | **NARROW** — the generic framing is dead (Montel et al.); the identifiability-aware form survives |
| **Compute** | CPU-only. ~10⁴–10⁵ simulator runs of a small ODE/compartmental model. |
| **Data** | None — synthetic, with a deliberately knocked-off-spec component |
| **Est. effort** | 2–3 weeks |

---

## The gap, stated honestly

The SBI-misspecification literature (≈33 papers screened) **detects or robustifies only**:
Schmitt/Radev/Bürkner do MMD-based global detection; Ward et al. (RNPE) place an error model on
summaries; Kelly, Huang, Tomaselli, Wehenkel (RoPE) robustify the posterior. None attribute.

**The gatekeeper is Montel, Alvey & Weniger (arXiv:2412.15100).** They augment a simulator with
*stochastic distortions* — including "distortions in individual data bins... or additional model
components" — and run many simultaneous likelihood-ratio tests with simulator-calibrated p-values.
A generic "per-component score with a calibrated null" proposal **is** that paper.

**What they do not do:** their tests are **marginal, not competitive**. When several component
distortions all fit, they do not answer which component is responsible, and they report no error
control over the *selected* component. That gap is real — and it is a selection problem, not a
testing problem.

## Primary claim (C1)

Component-level misspecification attribution is a **multiple-selection problem with correlated
alternatives**. Marginal distortion tests systematically **mis-attribute** when component effects are
correlated in summary space; a competitive/conditional attribution with **error control over the
selected component** corrects this, and the mis-attribution rate of marginal testing is quantifiable
as a function of component collinearity.

## Secondary claim (C2) — and this is the real contribution

**The identifiability boundary.** Lead with it; do not bury it.

If discrepancy decomposes as δ(x) = Σ_k δ_k(x) over components, the data constrain only the **sum**.
Any reallocation of δ across components preserving the total is observationally equivalent, so
**component attribution is non-identifiable without further structure. Full stop.** This is the
simulator analogue of Brynjarsdottir & O'Hagan's calibration/discrepancy confounding and Tuo & Wu's
inconsistency result.

Attribution becomes identifiable exactly when components have **distinct, non-collinear signatures in
summary space** — i.e. when the Jacobian ∂(summaries)/∂(per-component perturbation) has full column
rank. So deliver three things no reviewer can call ill-posed:

1. A **rank/coherence diagnostic**, computable from simulations alone with no real data, that says up
   front whether components are separable for this simulator and summary set.
2. Attribution **only inside the identifiable subspace**, reporting **equivalence classes**
   ("components 2 and 5 are indistinguishable given these summaries") rather than a single culprit.
3. A **calibrated null with control over the selected component**, not marginal tests.

Framed this way identifiability stops being the objection and becomes the paper.

## Method

1. **Component perturbation basis.** For each simulator component k, define a parametric distortion
   family δ_k(·; η_k).
2. **Separability diagnostic.** Simulate under each δ_k; form the Jacobian of summary statistics with
   respect to η; report its rank, condition number, and the pairwise coherence between component
   directions. This is cheap and it *gates everything downstream*.
3. **Competitive attribution.** Within the identifiable subspace, fit components jointly (rather than
   one-at-a-time) and select via a procedure with error control over the selection — e.g. an
   e-BH/knockoff-style selection or a conditional test that accounts for the correlated alternatives.
4. **Report equivalence classes** wherever the rank condition fails.

## Experimental protocol

- **Simulators:** a 3–5 component compartmental/ODE model (SIR-with-structure) and Lotka–Volterra;
  knock exactly one component off-spec at a time so ground truth is known by construction.
- **Baselines (must include the trivial one):** (i) **uniform/random attribution** — the degenerate
  floor; (ii) per-summary MMD; (iii) **Montel-style marginal distortion tests** ← the real competitor;
  (iv) RNPE's model-criticism step (**check whether it is per-summary-statistic — see below**).
- **Metric/estimand:** attribution accuracy (correct component identified) and mis-attribution rate,
  as a function of induced component collinearity — the collinearity sweep *is* the headline figure.
- **Statistics:** ≥200 replicates per collinearity level; report per-seed distributions.

## S4 preflight — run BEFORE any compute

1. **Degenerate floor:** with K components, random attribution is correct 1/K of the time. Any method
   must beat 1/K, and with K=3 that floor is 33% — quote your accuracy against it, never in isolation.
2. **MDE:** compute the Jacobian rank/coherence **first**. If components are collinear in your chosen
   summaries, no method can attribute and the experiment cannot answer its own question.
3. **Leakage:** the attributor must not see which component was knocked off-spec.
4. **STOP condition:** if the rank diagnostic shows your simulator's components are inseparable under
   any reasonable summary set, **stop and report the negative identifiability result** — that is still
   a genuine Sim2Science contribution and it costs days, not weeks.

## What kills this paper

**"This is Montel et al."** Pre-registered response: differentiate on *competitive vs marginal* testing
and on error control over the **selected** component, and lead with the identifiability characterization
which they do not have.

**"Attribution is ill-posed."** Correct — and C2 concedes it in the first paragraph, then bounds exactly
when it isn't. Conceding this first is what converts the objection into the contribution.

**"You don't know the Bayesian conflict-diagnostics literature."** Cite Marshall & Spiegelhalter conflict
p-values and **Presanis, Ohlssen, Spiegelhalter & De Angelis, "Conflict diagnostics in directed acyclic
graphs", *Statistical Science* 2013** — node-level localization with calibrated p-values. Your defence is
that these need a tractable likelihood and a DAG; SBI has neither. Omitting them signals unfamiliarity.

## ⚠️ Verify before committing

**Ward, Cannon, Beaumont, Fasiolo & Naderiparizi, "Robust Neural Posterior Estimation and Statistical
Model Criticism" (NeurIPS 2022)** did not surface in the sweep but is directly on point — RNPE places an
error model on summary statistics and performs model criticism. **Read it first.** If its criticism step
is per-summary-statistic, C1 narrows further and must be defended on the component-vs-summary distinction
and the identifiability result alone. This is a genuine open check, not a formality.

Also note this session's WebSearch budget was exhausted; the sweep ran on the arXiv API and full-text
search only, with no OpenReview or Scholar coverage. Re-run those before submission.

## Prior art you must cite

**Montel, Alvey & Weniger, arXiv:2412.15100**; Schmitt, Radev & Bürkner (arXiv:2112.08866, 2406.03154);
Cannon, Ward & Gutmann (arXiv:2209.01845); Ward et al., RNPE (NeurIPS 2022); Wehenkel et al., RoPE
(ICML 2025, arXiv:2405.08719); Tomaselli, Ventura & Wasserman (arXiv:2508.02404); Leclercq
(arXiv:2209.11057); Yang, Nott & Presanis (arXiv:2511.02977); Pierre et al. (arXiv:2507.03086);
**Kennedy & O'Hagan (*JRSS-B* 2001)**; **Brynjarsdottir & O'Hagan (*Inverse Problems* 2014)**;
**Tuo & Wu (*AoS* 2015)**; Arendt, Apley & Chen (2012); Frazier, Robert & Rousseau (*JRSS-B* 2020);
Cranmer, Brehmer & Louppe (*PNAS* 2020); Talts et al. (SBC); Presanis et al. (*Statist. Sci.* 2013).
*(The four journal-side statistics citations were not retrieved directly — verify before writing.)*

## Day-1 starting point

Write the Jacobian rank/coherence diagnostic on a 3-component SIR simulator. It needs no inference
machinery at all, and it tells you within a day whether the paper is possible.
