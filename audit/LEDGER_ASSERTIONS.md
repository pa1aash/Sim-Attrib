# Ledger of assertions

Every checkable factual assertion in `PLAN_SOURCE.md`, in the plan's own framing, with
the evidence that would confirm it and the evidence that would refute it — **written
before verification**, so the refutation criteria are pre-registered rather than fitted
to whatever the literature turns out to say.

**All entries open at `UNVERIFIED`.** Status is changed only by a session that has read
the source, not by a session that has read *about* the source. `S0_REPORT.md` §3 lists
every entry that failed.

Status values: `UNVERIFIED` · `CONFIRMED` · `REFUTED` · `PARTIAL` · `UNRESOLVED`
(`UNRESOLVED` = checked, but the evidence needed was not retrievable — distinct from
unchecked, and distinct from confirmed.)

---

## Group A — The prior-art sweep and its coverage

### A1 — Screening breadth
**Assertion (plan's framing):** "The SBI-misspecification literature (≈33 papers
screened) detects or robustifies only… None attribute."
**Confirms:** an independent sweep across Semantic Scholar, arXiv, OpenAlex and
OpenReview returns a comparable candidate set, and every member of that set is
classifiable as detection, robustification, or neither — with no member performing
component-level localisation.
**Refutes:** any single paper that localises misspecification to a named simulator
component. One counterexample refutes this outright; the count 33 is not the load-bearing
part and its exact value does not matter.
**Note:** the plan's own text records that its sweep used the arXiv API and full-text
search only, with no OpenReview and no Scholar coverage. The assertion is therefore made
on admittedly incomplete evidence and the gap is specifically where a refutation would
hide.
**Status: UNVERIFIED**

### A2 — Sweep methodology limitation is as stated
**Assertion:** the originating session's web-search budget was exhausted; the sweep ran
on the arXiv API and full-text search only, with no OpenReview or Scholar coverage.
**Confirms:** self-reported in `PLAN_SOURCE.md` lines 122–123.
**Refutes:** nothing available — this is a report about a prior session, not about the
world.
**Consequence regardless of status:** A1 inherits the gap. This entry exists to make the
inheritance explicit rather than to be independently checked.
**Status: CONFIRMED (self-report; scope of the gap is what matters, not its truth)**

### A3 — Characterisation of Schmitt, Radev & Bürkner
**Assertion:** they perform MMD-based *global* detection of misspecification.
**Confirms:** the papers' own method sections describe a global/summary-level MMD
statistic with no per-component decomposition.
**Refutes:** any per-component or per-summary decomposition of the MMD statistic that
supports localisation.
**Status: UNVERIFIED**

### A4 — Characterisation of RoPE
**Assertion:** Kelly, Huang, Tomaselli, Wehenkel (RoPE) *robustify* the posterior; they
do not attribute.
**Confirms:** the paper frames its contribution as robustness of inference under
misspecification, with no localisation claim.
**Refutes:** any diagnostic output of RoPE that names a responsible component.
**Caution:** the plan's author list for RoPE is a compression of several works and should
not be taken as an accurate byline. See `LEDGER_CITATIONS.md` C6.
**Status: UNVERIFIED**

---

## Group B — The gatekeeper: Montel, Alvey & Weniger (arXiv:2412.15100)

This group decides C1. If B3 or B4 is refuted, C1 is dead as stated.

### B1 — What their method does
**Assertion:** they augment a simulator with *stochastic distortions* — including
"distortions in individual data bins… or additional model components" — and run many
simultaneous likelihood-ratio tests with simulator-calibrated p-values.
**Confirms:** the quoted phrase appears in the paper and the method is as described.
**Refutes:** the quotation is inaccurate, or the tests are not simultaneous, or the
p-values are not simulator-calibrated.
**Status: UNVERIFIED**

### B2 — Their method subsumes the naive version of this project
**Assertion:** "A generic 'per-component score with a calibrated null' proposal **is**
that paper."
**Confirms:** their distortion families can be instantiated per-component, and the
resulting per-component test with calibrated null is exactly what they run.
**Refutes:** a structural obstacle preventing per-component instantiation.
**If confirmed:** this is *the plan agreeing that its own generic framing is dead.* It is
recorded as an assertion because the paper depends on it being true only in the generic
case and false for the identifiability-aware case — the distinction C1 lives in.
**Status: UNVERIFIED**

### B3 — Marginal, not competitive  ← **load-bearing for C1**
**Assertion:** "their tests are **marginal, not competitive**. When several component
distortions all fit, they do not answer which component is responsible."
**Confirms:** each distortion is tested against the null one at a time, with no joint
fit across distortions and no procedure that adjudicates between simultaneously
significant distortions.
**Refutes:** any joint/competitive fit, any conditional test, any adjudication step, any
ranking with a stated selection guarantee, or any discussion of correlated alternatives
in their setting. **A section on handling multiple simultaneously-firing distortions
would refute this even if they do not use the word "competitive".**
**Status: UNVERIFIED**

### B4 — No error control over the selected component  ← **load-bearing for C1**
**Assertion:** "they report no error control over the *selected* component."
**Confirms:** their guarantees are per-test (size/calibration of each individual test),
possibly with a multiplicity correction such as FDR over the family, but with nothing
conditional on which distortion was selected.
**Refutes:** any selective-inference guarantee, any post-selection correction, any
conditional coverage statement, or any claim of FDR control *over the selection event*
rather than over the family of tests.
**Sharp distinction that must not be blurred:** family-wise or FDR control over many
tests is **not** error control over a selected component. If they have the former only,
B4 stands. If they have the latter, B4 falls and C1 falls with it.
**Status: UNVERIFIED**

### B5 — They have no identifiability characterisation
**Assertion (implied throughout, explicit at plan line 103):** they do not have the
identifiability result; leading with it differentiates this work.
**Confirms:** no rank condition, no non-identifiability statement, no
observational-equivalence argument over component allocations in their paper.
**Refutes:** any statement in their paper that per-component distortion attribution is
underdetermined, or any condition under which it becomes determined.
**Status: UNVERIFIED**

---

## Group C — RNPE (Ward, Cannon, Beaumont, Fasiolo & Naderiparizi)

The plan flags this as a genuine open check, not a formality.

### C1a — RNPE places an error model on summary statistics
**Assertion:** RNPE places an error model on summary statistics and performs statistical
model criticism.
**Confirms:** the paper's model places a per-summary error/denoising layer between
observed and simulated summaries.
**Refutes:** the error model is on raw data or on parameters rather than summaries.
**Status: UNVERIFIED**

### C1b — Is RNPE's model-criticism step per-summary-statistic?  ← **narrows C1**
**Assertion (posed by the plan as an open question, not answered):** if RNPE's criticism
step is per-summary-statistic, then C1 narrows further and must be defended on the
component-vs-summary distinction and the identifiability result alone.
**Confirms per-summary:** the criticism step reports a statistic or posterior quantity
*per summary component*, flagging individual summaries as inconsistent.
**Refutes per-summary (i.e. would be worse for this project):** the criticism step is
per-*simulator-component*, which would make RNPE a second gatekeeper alongside Montel et
al. and would take C1 with it.
**Third possibility the plan does not consider:** the criticism step is global only, in
which case RNPE is weaker prior art than the plan fears.
**Why this matters beyond C1:** a per-summary criticism step is *architecturally the same
move* as a per-component one whenever summaries map one-to-one onto components. The
defence then rests entirely on cases where they do not — which is exactly the regime C2
characterises. C1 and C2 are less independent than the plan presents them.
**Status: UNVERIFIED**

---

## Group D — Bayesian conflict diagnostics

### D1 — What this literature does
**Assertion:** Marshall & Spiegelhalter conflict p-values, and Presanis, Ohlssen,
Spiegelhalter & De Angelis (*Statistical Science* 2013), perform **node-level
localisation with calibrated p-values**.
**Confirms:** the papers localise conflict to specific nodes of a graphical model with
calibrated diagnostics.
**Refutes:** the diagnostics are global model-fit measures without node attribution.
**Status: UNVERIFIED**

### D2 — Why it does not transfer  ← **load-bearing for the whole paper**
**Assertion:** "these need a tractable likelihood and a DAG; SBI has neither."
**Confirms:** their construction requires evaluating conditional distributions at nodes
of an explicit DAG, which is unavailable when the simulator is a black box.
**Refutes — and this is the serious risk:** any of the following would damage or kill
the defence:
  (a) a likelihood-free, simulation-based version of conflict p-values;
  (b) a version requiring only *sampling* from node conditionals, which a simulator
      can provide by definition;
  (c) an argument that a simulator's component decomposition **is** a DAG — which it
      arguably is, since decomposing a simulator into components *is* asserting a
      structural graph over it. If a simulator's component structure supplies the DAG,
      then the only missing ingredient is the tractable likelihood, and (b) would
      supply that.
**Assessment recorded in advance:** (c) is the weakest point in the plan's entire
defensive structure and the plan does not anticipate it. The plan treats "SBI has
neither" as one fact; it is two, and the DAG half looks false on inspection — a
3-component SIR model has an obvious DAG. If the conflict-diagnostics machinery has been
extended to simulation-based settings, this literature is not a citation to acknowledge
but a competitor to beat.
**Status: UNVERIFIED**

---

## Group E — The identifiability claim (C2)

### E1 — The data constrain only the sum
**Assertion:** if δ(x) = Σ_k δ_k(x), the data constrain only the sum; any reallocation
preserving the total is observationally equivalent; component attribution is therefore
non-identifiable without further structure.
**Confirms:** this is close to a definitional consequence of an additive decomposition
with no per-component constraints, and it is likely to survive as *stated*.
**Refutes:** nothing likely.
**The real risk is not truth but novelty.** A statement that follows in one line from its
own definitions is rarely a contribution by itself. What matters is E3.
**Status: UNVERIFIED (as a novelty claim, not as a mathematical claim)**

### E2 — The stated analogy to the calibration literature
**Assertion:** this is the simulator analogue of Brynjarsdottir & O'Hagan's
calibration/discrepancy confounding and Tuo & Wu's inconsistency result.
**Confirms:** those works establish confounding between calibration parameters and a
discrepancy term, of which this is a recognisable instance.
**Refutes:** the analogy is loose, or — more dangerously for the paper — it is *exact*,
in which case E3's novelty is in serious question. See E3.
**Status: UNVERIFIED**

### E3 — The rank condition is novel  ← **load-bearing for C2, and the most likely way C2 dies**
**Assertion:** "Attribution becomes identifiable exactly when… the Jacobian
∂(summaries)/∂(per-component perturbation) has full column rank."
**Confirms as novel:** no prior statement of this condition for per-component discrepancy
attribution in a simulator setting.
**Refutes:** the condition is a restatement of an established result. Specifically, a
full-column-rank condition on a sensitivity matrix is the **standard local structural
identifiability criterion** for ODE and compartmental models, and appears throughout that
literature as:
  (a) rank of the sensitivity matrix ∂(observables)/∂(parameters);
  (b) rank/invertibility of the Fisher information matrix (**practical identifiability**);
  (c) profile-likelihood flatness along non-identifiable directions;
  (d) the rank condition in differential-algebra and Lie-derivative structural
      identifiability analysis.
**Pre-registered assessment:** if "per-component perturbation magnitude η_k" is simply a
parameter, then the assertion reduces to *"parameters are locally identifiable when the
sensitivity matrix has full column rank"* — which is textbook, decades old, and not a
contribution. **The burden is on this project to state what is different**, and the
candidate differences are: that the perturbations are *functional* (whole distortion
families δ_k(·; η_k)) rather than scalar parameters; that the object being attributed is
*model discrepancy* rather than a parameter; and that the condition is evaluated from
simulation alone with no observed data and no likelihood. Whether any of those is enough
is exactly what verification must decide.
**This is treated as a first-class question, not a footnote.**
**Status: UNVERIFIED**

### E4 — The diagnostic requires no real data
**Assertion:** the rank/coherence diagnostic is "computable from simulations alone with
no real data".
**Confirms:** the Jacobian is a property of the simulator and the summary map only.
**Refutes:** any dependence on the observed value of the summaries — note that the
Jacobian must be evaluated *at a point*, and the choice of that point is a modelling
decision that could smuggle in data dependence. Local rank at the wrong operating point
does not answer the question.
**Status: UNVERIFIED**

---

## Group F — C1's statistical framing

### F1 — Marginal tests systematically mis-attribute under correlation
**Assertion:** marginal distortion tests systematically mis-attribute when component
effects are correlated in summary space.
**Confirms:** a standard consequence of marginal-vs-conditional testing under correlated
alternatives; demonstrable by simulation.
**Refutes:** unlikely to be refuted as a phenomenon. **The risk is again novelty** — this
is a well-known property of marginal testing, and stating it in a new domain is an
application, not a result.
**Status: UNVERIFIED**

### F2 — Selective inference supplies the fix
**Assertion:** a competitive/conditional attribution with error control over the selected
component corrects this — "e.g. an e-BH/knockoff-style selection or a conditional test".
**Confirms:** the mapping to selective inference is sound and the guarantee transfers.
**Refutes:** the required assumptions do not hold in this setting. **Specific hazards to
check, none of which the plan mentions:** knockoffs require a known or well-estimated
covariate distribution and exchangeability constructions that a simulator's distortion
basis may not admit; e-BH requires valid e-values, and constructing e-values from
simulator-calibrated tests is not automatic; conditional selective inference requires a
characterisable selection event.
**Status: UNVERIFIED**

### F3 — Mis-attribution rate is quantifiable as a function of collinearity
**Assertion:** the mis-attribution rate of marginal testing is quantifiable as a function
of component collinearity.
**Confirms:** an analytic or empirical curve relating collinearity to mis-attribution.
**Refutes:** the relationship depends on more than collinearity (distortion magnitude,
sample size, summary choice) in a way that makes a single-parameter curve misleading.
**Note:** the plan makes this the headline figure. If the curve needs three axes, the
headline figure does not exist as described.
**Status: UNVERIFIED**

---

## Group G — Venue facts

Each of these is checkable against the venue's own site or OpenReview page and **none is
takeable from the plan**. Recorded in `VENUE.md`.

| # | Assertion | Status |
|---|---|---|
| G1 | A NeurIPS 2026 workshop "Sim2Science: ML with Imperfect Scientific Models" exists, in Paris | UNVERIFIED |
| G2 | Its CFP names "simulator diagnostics and discrepancy modeling" in scope | UNVERIFIED |
| G3 | Deadline is 29 Aug 2026 AoE | UNVERIFIED |
| G4 | Page limit 5, tiny track 2, references excluded, appendix unlimited | UNVERIFIED |
| G5 | Double-blind | UNVERIFIED |
| G6 | Non-archival | UNVERIFIED |
| G7 | "AI for Science (Sydney)" exists as a viable backup | UNVERIFIED |

**Standing caution:** NeurIPS 2026's location and its workshop list are the kind of fact
that is easy to assert and easy to get wrong, and a wrong deadline is unrecoverable.
Nothing in Group G is acted on until fetched from the venue itself.

---

## Group H — Resource assertions

### H1 — CPU-only is sufficient
**Assertion:** compute is CPU-only, ~10⁴–10⁵ simulator runs of a small ODE/compartmental
model.
**Confirms:** a 3–5 component SIR/Lotka–Volterra forward solve is milliseconds; 10⁵ runs
is minutes to hours on one machine.
**Refutes:** the count omits what dominates. **Pre-registered concern:** the figure
appears to count *forward simulations for one experiment*, not the experiment as
designed. The protocol specifies ≥200 replicates × a collinearity sweep × K components ×
several baselines, and any neural-SBI baseline requires training a density estimator per
replicate. The true count is a product of factors the plan states separately and never
multiplies. Assessed in `S0_REPORT.md` §7.
**Status: UNVERIFIED**

### H2 — Effort estimate
**Assertion:** 2–3 weeks.
**Confirms/refutes:** not independently checkable; recorded for completeness and not
relied upon.
**Status: NOT CHECKABLE**
