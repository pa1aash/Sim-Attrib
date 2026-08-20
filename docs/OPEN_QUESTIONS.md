# Open questions

Questions an agent session cannot answer. Numbered and carried across sessions. Answered
questions stay, with the answer and the date, because the reasoning behind a settled
decision is worth more later than the decision alone.

## Open

> ### Standing audit debt, carried and non-blocking (noted G3)
>
> **Some of G0's and G1's negative findings were made before the `search_classic` fix and are
> UNVERIFIED, not confirmed.** `audit/TOOLING.md` establishes that the arXiv API's `all:` field
> searches metadata, not full text, so every zero those sessions reported as evidence of
> absence was a *metadata* zero. Two have since been re-checked on the working index and
> survived (G2 re-checked one; G3's R2 sweep is the first check run entirely on the corrected
> instrument). **The rest are instrument gaps, not measured zeros.** Tracked as **O-13**.
>
> This is recorded here so a future session does not treat those findings as settled, and it is
> **not blocking**: the project's live claims — the composition in
> `audit/MMC_COMPOSITION_SPEC.md` and the empirical result in `results/` — do not rest on them.
> The *positive* findings that killed C2, R1 and the composite-null gap are unaffected, since a
> paper that does the thing does not depend on how it was found.

### Q-2 — Repository visibility *(answered in principle, action outstanding)*
**Answered 2026-08-20 by `docs/DECISIONS.md` D-4:** public during the build phase, private
before the paper draft or final results are committed. The *action* — flipping the setting
— remains the operator's and is tracked as O-1, not as an open question. `gh` is still
unauthenticated on this machine (re-checked 2026-08-20), so current visibility cannot be
confirmed from here; see O-4.

### Q-3 — Who is the nominated reciprocal reviewer? **(now unconditional — venue is decided)**
Sim2Science requires a named co-author at submission time who will review **2** papers.
Failure to review is grounds for **desk-rejecting our own submission**. All authors must
be listed at submission; none can be added later. This needs a real person committed.
No longer conditional: `docs/DECISIONS.md` **D-2** commits the project to Sim2Science.

### Q-6 — Is a multi-component misspecification condition in scope? *(unchanged, but now cheaper to decide)*

Still open and still a scope call. **Note for whoever answers it:** this question was framed
around strengthening C1's competitive-testing argument, and C1 no longer exists in that form.
Under `Q-8` option (b) the question becomes far less pressing — a rank diagnostic does not
care how many components are off-spec at once. Under option (a) it stays exactly as sharp as
`LEDGER_DESIGN.md` D6 describes.

Original question follows.


The design knocks exactly one component off-spec at a time, so ground truth is unique by
construction. But real simulators are wrong in several places at once — and that is the
regime where competitive-vs-marginal testing matters *most*. As designed, the experiment
tests C1's mechanism where its advantage is smallest. Adding one multi-component condition
would strengthen C1 considerably. Scope call.

### Q-7 — How should the plan's citation errors be handled? *(partly acted on; confirm the policy)*

**Acted on 2026-08-20 without waiting**, since it was cheap and the reference list was still
small: `audit/BIBLIOGRAPHY.bib` was built by **fetching** all 52 entries, and all four byline
errors are corrected against the fetched records. What still needs the operator's answer is
the **policy** — specifically whether a full re-verification pass *against the papers
themselves* is required before submission, over and above fetching from canonical indexes.

**This session found the reason it might be.** Crossref **and** OpenAlex both return an
incomplete author list for Catchpole & Morgan (1997), omitting Morgan; it took the
publisher's own article page to catch it. **Fetching from a canonical index is necessary but
not sufficient.** And one of G0's own citations — "Presanis et al. (2017)" — cannot be
resolved at all (O-11).

Original question follows.


Four byline errors were verified against the papers themselves, including one author
credited with a paper she is not on, and one citation that conflates two different papers
(`LEDGER_CITATIONS.md`). Sim2Science's scientific advisors include Jakob Macke, so the
related-work section will be read by people who know this literature. Recommend a full
re-verification pass over every reference before anything is submitted. Confirm.

### Q-8 — R1 is prior art. What is the paper now? **(BLOCKING — narrowed 2026-08-20)**

> **Update, G2.** Option **(a)** of this question — "rescope R1 to the transfer claim,
> requires solving Q-9 first" — is **FORECLOSED**. Q-9 is now answered, and its answer is
> that the repair is Dufour (2006). There is nothing left to contribute on that path. The
> live options are **(b) promote the diagnostic and go empirical** and **(c) report the
> negative outcome**, and they are now folded into **Q-10**, which supersedes this question
> as the blocking one. Original text follows.

**Q-8 as originally written (G1):**

**Raised 2026-08-20 by `audit/R1_THREAT_CHECK.md`, verdict DEAD.**

The mechanism promoted to the paper's headline by `docs/DECISIONS.md` **D-3** — calibrating
a selection event by rejection sampling from an exact null, so that no analytic
characterisation is needed — is published. **Freidling, Zhao & Gao (arXiv:2405.07026)**
implement it as a titled algorithm ("Algorithm 1: Rejection sampling") for arbitrary
conditioning events, with the same 1/p₀ cost analysis. The April-2026 review of the field
(**Neufeld, Perry & Witten, arXiv:2604.09779**) catalogues it as a known "Monte Carlo
strategy" and states the two standard objections to it. And **Liu, Markovic-Voronov &
Taylor (arXiv:2203.14504)** — the paper D-3 cites as *identifying the barrier* — does not
identify a barrier; it removes one, by bootstrap.

D-3 was recorded as conditional on this check returning SAFE. It returned DEAD.

**The options, with the honest cost of each:**

- **(a) Rescope R1 to the transfer claim.** "The construction is exact where the null is
  exact; a simulator supplies an exact model-based null, so this is the only exact option
  in SBI." Small, defensible, and requires solving the composite-null problem in Q-9 first.
  It is a *transfer and its consequences*, not a mechanism — precisely the wording
  `audit/PIVOT.md` pre-registered as response 1 to a novelty failure.
- **(b) Promote R2 and the demonstration.** Make the paper the noisy-rank estimator plus
  component attribution, with the conditional calibration cited rather than claimed. This
  is `PIVOT.md` response 2 — let the empirical finding carry it. It is a diagnostics paper.
  R2's novelty has **not** been threat-checked to the standard R1 just was.
- **(c) Report the negative outcome and stop.** `PIVOT.md` response 3, written in advance
  so that reaching it is a decision rather than a failure. Two successive headline claims
  have now been found to be prior art by direct retrieval.

**This question blocks Phase 3.** Per the session brief §2.4 and P-1, no code was written
for the mechanism, and the Jacobian diagnostic was not built. See `audit/S1_REPORT.md` §3
for the argument that option (b)'s deliverable is *technically* unblocked — R2 does not
depend on R1 — which the operator may wish to authorise separately.

### Q-10 — Three consecutive kills. Does this project continue? **ANSWERED 2026-08-20 — and executed**

> **ANSWER (operator, 2026-08-20).** *Option (a) then (b), in that order, with (b)
> unconditional.* Verbatim as recorded in session G3's brief:
>
> > "run ONE corrected-instrument check on R2 — narrow, not a new investigation phase — then
> > build the diagnostic regardless of what it finds. The diagnostic was already established
> > in G1's GATES.md as passing on either branch of its own STOP condition, independent of any
> > novelty verdict, so R2 coming back DEAD does not block Phase 2 — it only changes whether
> > the rank estimator is claimed as a method contribution or used purely as infrastructure."
>
> **Executed in full, session G3.** The R2 check ran on the corrected full-text instrument
> and returned **NARROW-CONDITIONAL** (`audit/R2_THREAT_CHECK.md`) — the first of four
> prior-art checks in this project not to return DEAD. Its consequence for framing is
> recorded as **D-6**: R2 is cited infrastructure, not a claimed method contribution. The
> diagnostic was then built and run: `src/simulators/sir3.py`,
> `src/simulators/summaries.py`, `src/diagnostics/jacobian_rank.py`, and
> `results/jacobian_rank.*.yaml`. **This repository now contains code and numbers, for the
> first time.**
>
> **The reading that should be carried forward, and it is not simply "the project
> continues".** R2 survived because it was never the headline. What survives of it is a
> one-sentence observation about a rank tolerance. All three claims that *were* headlines
> died. The project's viability now rests on the composition specified in
> `audit/MMC_COMPOSITION_SPEC.md`, which is a composition of two published techniques and
> says so first — and on the empirical finding in `results/`, whose value does not depend on
> any novelty verdict.

Original question follows.


**Raised 2026-08-20 by `audit/COMPOSITE_NULL_CHECK.md`, verdict DEAD.**

Three primary claims have now died to prior art, each found by direct retrieval, each after
being adopted as the paper's headline:

| Session | Claim adopted as headline | Killed by |
|---|---|---|
| G0 | **ex-C2** — per-component discrepancy identifiable iff the summary Jacobian has full column rank | **Kahl, Wendland, Neidhardt, Weber & Kschischo (2019)**, *PRX* 9:041046, via Sain & Massey (1969) |
| G1 | **R1** — calibrate the selection event by rejection sampling from the simulator's null; no analytic characterisation needed | **Freidling, Zhao & Gao (2024)**, arXiv:2405.07026, Algorithm 1 "Rejection sampling" |
| G2 | **The composite-null gap and its repair** | **Dufour (2006)**, *J. Econometrics* 133(2) — maximized Monte Carlo, provably exact level |

Each kill took between one and three targeted queries once the right instrument was used. The
third was found in the first hour of the session that went looking for it.

**A large part of the explanation is now known and is not a research problem.** Both prior
sessions ran what they described as "arXiv full-text" searches. Those searches were
**metadata-only** — see `audit/TOOLING.md`. The real full-text index found Dufour, the
repro-samples line and the co-sufficient-sampling line immediately. So the pattern is at
least partly an instrument failure, now fixed, rather than evidence that the whole area is
picked over.

**That cuts both ways, and the operator should weigh both.**

- *Argument to continue:* the searches were being run with a broken instrument, so the
  project has never actually had a competent prior-art sweep of its own idea space. One
  should now be run **before** a fourth claim is adopted, not after.
- *Argument to stop:* three for three is not bad luck, and the area — exact inference from
  simulation, with and without nuisance parameters, with and without selection — is
  demonstrably crowded, mature, and worked on by strong groups (Taylor, Barber, Witten,
  Panigrahi, Dufour, Xie). `audit/PIVOT.md` response 3 was written in advance precisely so
  that stopping would be a decision rather than a failure.

**The options:**

- **(a) Run one clean full-text prior-art sweep first, then decide.** Cheap, and it is the
  first sweep the project would have had with a working instrument. It should cover R2 —
  which has *still* never been checked — before anything else.
- **(b) Drop the mechanism entirely and go empirical.** `PIVOT.md` response 2: build the
  diagnostic, run it on a 3-component SIR simulator, report whether a standard simulator
  passes its own identifiability precondition. The novelty budget then rests on an
  empirical finding, not on machinery. **This is buildable now** and does not depend on
  any surviving mechanism claim.
- **(c) Stop and write up the negative result.** `PIVOT.md` response 3.

**This question blocks everything.** No further claim should be adopted, and no code written
against a claim, until it is answered.

### Q-13 — The separability verdict is conditional on the distortion families. What may be claimed from it? **(BLOCKING — new, G4)**

**Raised 2026-08-20 by `audit/G3_ADVERSARIAL_REVIEW.md` finding 2.**

`S_A` and `S_B` separate the three components under the three distortion families `sir3.py`
declares. Session G4 built **one** alternative triple, designed against a named target component
per family, ran it through the identical diagnostic at the identical pre-registered thresholds,
and reports the outcome in `results/robustness/`. **No second candidate set was tried and none
was discarded** — there was no search over families.

**Why this is the operator's question and not a session's.** It is not a correctness question:
both verdicts are correct statements about their own family sets, and nothing in `results/`
needs withdrawing. It is a question about **what sentence the paper is allowed to write**, and
the two available sentences differ in what a reviewer would do with them:

- **(a) The narrow sentence.** *"Under these three distortion families the components separate;
  under an adversarially chosen alternative triple built from the same simulator, they do not."*
  Defensible, and it is what the evidence supports. It also concedes, in the paper, that the
  precondition for the composition holds conditionally — and `audit/MMC_COMPOSITION_SPEC.md` §5
  makes that precondition load-bearing for whether the composition is worth building.
- **(b) Establish which side the typical case falls on.** Run the diagnostic across a
  *designed set* of family triples — not one favourable and one adversarial — and report the
  distribution of verdicts. This converts a conditional claim into a characterised one and is
  the only route to a sentence stronger than (a). It costs a session, and the set would have to
  be specified before any of it is run, or it becomes the leakage failure `LEDGER_DESIGN.md` D3
  names, pointed at whichever conclusion is wanted.

**Recommendation, offered as such: (a) now, and (b) only if the paper needs the stronger
sentence.** (a) requires no further compute and is honest. (b) is a real experiment with a real
design problem attached — "which family triples are representative" has no obvious answer, and
answering it badly is worse than conceding (a).

**What must not happen:** the base result being quoted without its condition. `results/` and
`docs/THRESHOLDS.md` now carry the qualification inline so that a future session cannot pick up
the number without it.

**This question is BLOCKING in one specific sense only:** it blocks writing the separability
claim into `paper/main.tex`. It does **not** block the `p_sel`/cost-gate measurement (**P-3**),
which measures a different quantity and would be informative under either answer.

### Q-11 — Should the project occupy the noise-calibrated rank-tolerance seam? *(new, G3; not blocking)*

**Raised 2026-08-20 by `audit/R2_THREAT_CHECK.md` §2.**

The one thing nobody in the retrieved literature does is carry an estimated simulation noise
level forward into the **rank tolerance**. Moré & Wild (2010/2012) estimate the noise level
and use it to pick a near-optimal difference parameter; Cintrón-Arias et al. (2009) assemble
the sensitivity matrix and call its rank at MATLAB's *machine* tolerance. Nobody joins them —
four full-text zeros, control live in the same batch.

**The project does not currently occupy that seam either, and this is the honest part.**
`docs/THRESHOLDS.md` §1.2 derives `τ = 10⁻²` from a **compute budget** (`n ≳ κ²`), not from a
noise level. So there are exactly two options and both have a cost:

- **(a) Occupy it.** Re-derive `τ` from an estimated noise level. Requires a `DEVIATIONS.md`
  entry stating that a pre-registered numeric threshold changed, what result prompted it, and
  why the change is not motivated by that result. **The last condition is the hard one**: the
  numbers now exist, so any re-derivation happens with the singular values already visible.
  That is precisely the leakage failure `LEDGER_DESIGN.md` D3 exists to prevent, and it is
  not obviously escapable by good intentions.
- **(b) Do not occupy it.** State plainly in the paper that the gap was identified and not
  filled, and keep `τ` as pre-registered. Costs the seam; keeps the pre-registration, which
  is currently one of the few things this project has that is demonstrably clean.

**Recommendation, offered as such:** (b). The pre-registration's value is that it is
provable from `git log`; the seam's value is one sentence.

### Q-12 — The observation distortion probes reporting fraction only. Is that enough? **ANSWERED 2026-08-20 (G4) — and the answer is larger than the question**

**Raised 2026-08-20 by the Phase 2 build.**

The OBSERVATION component is declared as *reporting fraction / delay / noise*, but a
distortion family is a **one-parameter** deformation, so one sub-process had to be chosen. The
build chose the **reporting fraction** (`ρ → ρ·exp(η₃)`), a pure amplitude error, deliberately
— it is the cleanest way to ask whether an amplitude error can be told apart from a mechanism
error. The delay kernel and the noise scale are held at base values.

**Why this is a real limitation and not a quibble.** The separability verdict in `results/`
is a statement about *these three columns*. A different observation distortion — perturbing
the reporting **delay** instead, which is a timing distortion — would give a different third
column, and the progression family is *also* a timing distortion. The two could plausibly be
far more collinear than the amplitude/timing pair actually measured. **The favourable verdict
may therefore be partly a consequence of which observation sub-process was chosen**, and that
possibility is not testable without adding the second family.

This is the same class of question as **Q-6** (multi-component scope) and is a scope call, not
a correctness one. Adding a fourth distortion family is **not** governed by THRESHOLDS §1.1,
which closes the list of *summary sets*, not of distortion families — but the same reasoning
applies and any addition should be logged in `DEVIATIONS.md` with whether the existing results
were known at the time.

> #### Answer, session G4 (2026-08-20)
>
> **The question was posed too narrowly.** It asks whether a second *observation* distortion is
> in scope. G4 built an alternative triple in which **all three** families were replaced, each
> designed against a named target component, and ran it through the identical diagnostic:
> `audit/G3_ADVERSARIAL_REVIEW.md` finding 2, numbers in `results/robustness/`.
>
> The observation family G4 used is **strictly harder than the delay perturbation Q-12
> proposes**: a delay *shifts* the reported curve, while a mean-centred log-linear reporting
> trend *tilts* it, and tilt is what the other two columns do. But the finding is not about the
> observation family at all — it is that **the verdict is conditional on the family set as a
> whole**, and that the conditioning is load-bearing rather than decorative.
>
> Q-12 is therefore **closed as answered**, and the live question it opens is **Q-13**, which is
> about what may be claimed rather than about which families are in scope.
>
> The addition is logged in `DEVIATIONS.md` **D-9**, including the part Q-12 asked for and that
> reflects badly on the timing: **the existing results were known when the adversarial set was
> designed.** D-9 states what was done about that and why it is weaker than pre-registration.

## Answered

### Q-9 — The simulator's null is composite. Does the construction survive that? **ANSWERED 2026-08-20**

**Answer: yes, and by published means — which is why it is not a contribution.**
`audit/COMPOSITE_NULL_CHECK.md`.

The composite-null obstruction is real and was correctly identified. It is also the founding
premise of the Monte-Carlo-testing literature, and it has at least three published repairs
that apply to simulators: **Dufour's maximized Monte Carlo** (maximise the simulated p-value
over the nuisance space; *"provably exact level, irrespective of the sample size"*; applies
*"as long as the null distribution … can be simulated once the nuisance parameters have been
specified"*), **repro samples with profiling** (Xie & Wang 2022 — likelihood-free, exact,
finite-sample), and **(approximate) co-sufficient sampling** (Barber & Janson 2022).

Q-9 was raised in G1 as a correctness threat to R1. It is answered as a correctness question
— the construction does not survive a composite null unrepaired, and the repairs are
off-the-shelf. It therefore stops being a research question and becomes a citation.

Original question follows.



**Raised 2026-08-20, and it is independent of the novelty verdict.**

Freidling, Zhao & Gao can rejection-sample because the treatment-assignment distribution is
**known exactly by design**. A simulator's null is exact only **given parameters θ**, and θ
is unknown. "The simulator's own null" is therefore a *family* of distributions, not a
distribution, and the rejection-sampling construction is not automatically valid over a
composite null — the conditional type-I error must hold uniformly over the nuisance
parameter, or the nuisance must be conditioned away on a sufficient statistic.

D-3's formulation does not mention this. It is the actual technical content of any
simulation-based version of the mechanism, and it is unsolved here. Nothing should be
claimed about exact conditional validity in SBI until it is answered.

---


### Q-4 — What counts as "any reasonable summary set", and what rank tolerance? **ANSWERED 2026-08-20**

**Answered in `docs/THRESHOLDS.md` §1** — referenced, not duplicated here.

In summary: the list is **closed at `S_A`, `S_B`, `S_C`**, with a `DEVIATIONS.md` entry
required to add a fourth. Numerical rank is called at `τ = 10⁻²` relative to `σ_1`, and a
summary set is "inseparable" if `rank(J) < 3` or `κ > 100`. The ceiling `κ_max = 100` is
derived from the study's own simulation budget — separation costs `n ≈ κ²` replicates, and
`κ = 1000` would cost more than `S0_REPORT.md` §7 prices the entire protocol at.

**These were fixed before any singular value existed**, in a session that produced no
numbers at all; `git log` is the evidence. A near-zero column norm (`‖J_·k‖ < 0.1`) is
recorded as a **separate** failure — a component invisible to the summaries, not a
confounded one.

### Q-5 — What threshold defines an equivalence class? **ANSWERED 2026-08-20**

**Answered in `docs/THRESHOLDS.md` §2** — referenced, not duplicated here.

Component *k* joins the class named by a near-null right singular vector `v` iff
**`|v_k| ≥ 0.3`**, reported as a range across the h-plateau with border-crossing components
flagged. **Coherence is reported but is deliberately not the decision rule**: the coherence
consistent with `κ_max = 100` is `μ ≈ 0.9998`, too close to 1 to be estimable, so `|μ| ≥ 0.98`
is used only to flag which pair is responsible.

`docs/THRESHOLDS.md` §3 additionally carries the Phase-3.7 argument for why finite-parametric
equivalence classes are meaningful where Kahl et al.'s function-space ones are not — with a
real concession in §3.4: at *exact* rank deficiency Kahl's dichotomy does import, and near-
degeneracy claims must be labelled as statements about **affordability**, not identifiability.

---
### Q-1 — Do we target NeurIPS 2026 at all? **ANSWERED 2026-08-20**

**Answer: yes, and the question's own framing is retired.** `docs/DECISIONS.md` **D-1**.

The operator targets NeurIPS 2026 and has additionally ruled that calendar and deadline
feasibility are **not a planning input for this project** — a standing instruction. Q-1 was
posed as a scheduling trade-off ("given nine days"), and that framing is precisely what
D-1 removes: no session may again argue for a smaller format, a reduced protocol, or a
dropped verification on time-cost grounds.

Option (a) as originally posed — the 2-page Tiny Paper track — was **rejected** on
substantive rather than scheduling grounds. It was viable only as a vehicle for the
identifiability result standing alone, and that result is prior art (Kahl et al. 2019,
*PRX* 9:041046). See `docs/DECISIONS.md` **D-2**.

**Venue selection is resolved:** Sim2Science, **5-page main track**. O-3 is closed;
`audit/VENUE.md` §5 now records a decision rather than a conditional recommendation.

---

