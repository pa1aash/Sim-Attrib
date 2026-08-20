# Open questions

Questions an agent session cannot answer. Numbered and carried across sessions. Answered
questions stay, with the answer and the date, because the reasoning behind a settled
decision is worth more later than the decision alone.

## Open

### Q-1 — Do we target NeurIPS 2026 at all, given nine days? **(blocking, decide first)**
The deadline is 29 Aug 2026 AoE, verified from the venue and the OpenReview API. All four
candidate venues share it; notification is 29 Sep and cannot be extended. `src/` and
`results/` are empty; the plan estimates 2–3 weeks of work.

Options, with the honest cost of each:
- **(a) 2-page Tiny Paper at Sim2Science.** Carries C2's identifiability result and the
  rank diagnostic on a 3-component SIR model. Achievable *if* the diagnostic is built in
  the next two or three days. Drops the collinearity sweep, the baselines, and the
  ≥200-replicate protocol.
- **(b) Skip NeurIPS 2026.** All these venues are non-archival, so a later archival
  submission loses nothing. Buys the time to do the experiment properly.
- **(c) Attempt the full 5-page paper.** Not recommended. Nine days to build a simulator,
  a diagnostic, an attributor, three baselines, and a 200-replicate sweep invites exactly
  the silent failures `LEDGER_DESIGN.md` D1 and D3 describe — a leakage bug or an
  unfloored accuracy number is invisible in an abstract and fatal in review.

*This question gates the next session's work and should be answered before anything is
built.*

### Q-2 — Repository visibility
The repository is public. It must be private before any unpublished result or draft is
committed. `gh` is not authenticated on this machine, so visibility could not be verified
here. See the banner in `OUTSTANDING.md`.

### Q-3 — Who is the nominated reciprocal reviewer, if Sim2Science is chosen?
Sim2Science requires a named co-author at submission time who will review **2** papers.
Failure to review is grounds for **desk-rejecting our own submission**. All authors must
be listed at submission; none can be added later. This needs a real person committed
before 29 August.

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

*(none yet)*
