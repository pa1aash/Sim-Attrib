# Open questions

Questions an agent session cannot answer. Numbered and carried across sessions. Answered
questions stay, with the answer and the date, because the reasoning behind a settled
decision is worth more later than the decision alone.

## Open

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

### Q-4 — What counts as "any reasonable summary set" for the STOP condition?
`LEDGER_DESIGN.md` D4 commits to stopping and reporting a negative identifiability result
if components are inseparable "under any reasonable summary set". That phrase is not
operational. Before the diagnostic runs, fix in writing: (i) which summary sets will be
searched, and (ii) what rank / condition-number threshold counts as inseparable.
Otherwise the STOP condition can be evaded indefinitely by proposing one more summary set.

### Q-5 — What singular-value or coherence threshold defines an equivalence class?
`LEDGER_DESIGN.md` D8. Real Jacobians are near-singular rather than singular, so the
equivalence classes reported depend on where the cutoff is set. That choice is a
substantive part of the method, not a numerical tolerance, and its sensitivity must be
reported. Needs a defensible answer before results are generated.

### Q-6 — Is a multi-component misspecification condition in scope?
The design knocks exactly one component off-spec at a time, so ground truth is unique by
construction. But real simulators are wrong in several places at once — and that is the
regime where competitive-vs-marginal testing matters *most*. As designed, the experiment
tests C1's mechanism where its advantage is smallest. Adding one multi-component condition
would strengthen C1 considerably. Scope call.

### Q-7 — How should the plan's citation errors be handled?
Four byline errors were verified against the papers themselves, including one author
credited with a paper she is not on, and one citation that conflates two different papers
(`LEDGER_CITATIONS.md`). Sim2Science's scientific advisors include Jakob Macke, so the
related-work section will be read by people who know this literature. Recommend a full
re-verification pass over every reference before anything is submitted. Confirm.

### Q-8 — R1 is prior art. What is the paper now? **(BLOCKING — gates all further code)**

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

### Q-9 — The simulator's null is composite. Does the construction survive that? **(BLOCKING with Q-8)**

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

## Answered

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

