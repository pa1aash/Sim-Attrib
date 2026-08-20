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

