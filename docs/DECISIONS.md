# Decisions

Choices made by the **operator** that future sessions must not silently revisit. Each
entry records the date, the decision, why it was made, and — the column that matters —
**what it forecloses**, so that a later session can see the cost of reopening it.

An agent session may record a decision here. It may not make one. Where a decision has
consequences an agent session then executed, those are listed under *Executed*.

---

## D-1 — Target NeurIPS 2026. Calendar feasibility is not a planning input.

**Date:** 2026-08-20 · **Answers:** Q-1 (blocking since G0)

**Decision.** The project targets NeurIPS 2026. Separately and as a **standing
instruction**: calendar and deadline feasibility are explicitly excluded as a planning
input for this project. No session is to reason about how many days remain, to scale
scope to a countdown, or to recommend a format on the grounds that it is the only one
that fits the time available.

**Rationale.** G0's report opens with the deadline and lets it dominate everything after
it — the venue recommendation, the format recommendation, and the sequencing of the
technical work were all argued from "nine days". That is a legitimate consideration for
a person and a corrosive one for an agent session, because it converts every methodological
question into a scheduling question and supplies a standing reason to cut the check rather
than the claim. The operator has removed it from the agent's remit. The deadline facts
themselves remain true and remain recorded; what is removed is their use as an argument.

**What it forecloses.** No session may again recommend a smaller format, a reduced
protocol, or a dropped verification on time-cost grounds. Scope arguments must be made
from what the work supports. If the work is not ready when a deadline arrives, that is
the operator's problem, not the session's.

**Executed 2026-08-20.** The deadline-countdown banner is removed from the top of
`OUTSTANDING.md`. The underlying facts — submission 29 Aug 2026 AoE, notification
29 Sep 2026, non-extendable — are retained in `audit/VENUE.md` only, stripped of urgency
framing. "N days left" language is not to be reintroduced into any file.

`audit/S0_REPORT.md` and `audit/PIVOT.md` were **deliberately left unedited**. They are
dated reports of what session G0 concluded and on what basis; editing the deadline
reasoning out of them would falsify the record of how G0 reached its recommendations.
They are history, not live guidance. This decision supersedes them where they conflict.

---

## D-2 — Venue: Sim2Science, 5-page MAIN track.

**Date:** 2026-08-20 · **Closes:** O-3, and the venue half of Q-1

**Decision.** Submit to **Sim2Science: ML with Imperfect Scientific Models** (NeurIPS 2026
workshop, Paris satellite), **5-page main track**. Not the 2-page Tiny Paper track.

**Rationale.** The Tiny Paper track was viable in G0's analysis only as a vehicle for
C2-as-headline — the identifiability result standing alone. C2 is now Kahl, Wendland,
Neidhardt, Weber & Kschischo (2019), *Physical Review X* 9:041046, resting on Sain &
Massey (1969). Presenting it standalone at two pages, to a workshop whose scientific
advisors include Jakob Macke, would read as restating a published PRX result to an
audience that knows it. The main track is the only format with room for the reframed
contribution recorded in D-3.

**What it forecloses.** The e-values workshop and Representations for the Physical
Sciences are out; Sim2Science discourages parallel submission to other NeurIPS 2026
workshops, so this is a choice rather than a hedge. The 5-page budget, the mandatory
reproducibility checklist, the mandatory reciprocal reviewer (Q-3, still open), and
mandatory in-person Paris attendance are all now committed obligations rather than
contingencies. See `audit/VENUE.md` §1.

**Executed 2026-08-20.** The venue's LaTeX template was fetched from
`https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip`
(HTTP 200, 20,259 bytes, SHA-256 `82473931e3ef710fcd3f4a8cd4119b9de32e56825f90f9e5a6d55f2d01b817d9`)
and unpacked **unmodified** into `paper/neurips_2026_template/`. Reading
`neurips_2026.sty` directly confirms the two requirements `audit/VENUE.md` records:
`\DeclareOption{dblblindworkshop}` sets `\@workshoptrue` and leaves `\@anonymous` at its
default `true` (so it is genuinely double-blind, unlike `sglblindworkshop` which sets
`\@anonymousfalse`), and `\workshoptitle{}` is the macro that fills the track name.
`paper/main.tex` was **not** created this session and must use
`\usepackage[dblblindworkshop]{neurips_2026}` with `\workshoptitle{Sim2Science}` when it is.

---

## D-3 — Reframe: the mechanism is the paper; attribution is the demonstration.

**Date:** 2026-08-20

**Decision, recorded verbatim as the operator stated it:**

> "The paper's primary claim is no longer component-level attribution with error control
> (former C1) alongside an identifiability boundary (former C2, now refuted as an original
> result). The primary claim is: in simulation-based settings, exact conditional inference
> given a selection event requires no analytic characterisation of that event, because the
> selection event can be calibrated by rejection sampling from the simulator's own null.
> This removes the obstruction Liu, Markovic-Voronov & Taylor (2023) identify as the
> central barrier to conditional selective inference. Component-level misspecification
> attribution is the demonstration of this mechanism, not the subject of the paper. The
> identifiability characterisation (ex-C2) is retained only as a cited precondition —
> Brynjarsdóttir & O'Hagan (2014), Catchpole & Morgan (1997), Kahl et al. (2019) —
> establishing when the demonstration's target quantity is well-posed at all. The second
> contribution is a simulation-based estimator of the summary Jacobian's rank together
> with a defensible rule for calling numerical rank from a NOISY, sampled Jacobian —
> every source found in G0 assumes the map is symbolic or analytically differentiable,
> which a simulator's Jacobian is not."

**Working title** — a placeholder that fixes the emphasis, not the wording:
*"Simulators Make Selective Inference Exact: Component-Level Misspecification Attribution
as a Demonstration."*

**Rationale.** G0 established that both of the plan's headline claims are constrained by
prior art, and that the one thing found nowhere in the searched literature was a mechanism
the plan never proposed. Building the paper around the claim that survived, rather than
around the claim that was planned, is the only honest response to that finding.

**What it forecloses.** "We characterise identifiability" is no longer available as a
contribution and must not reappear as one; it is a **cited precondition**. "We are the
first to attribute misspecification to components" is likewise unavailable — Leclercq
(arXiv:2209.11057) localises to a named model layer, and RNPE localises per summary
statistic. The paper's novelty budget is spent entirely on the rejection-sampling
mechanism (R1) and the noisy-rank estimator (R2).

**What it does not settle.** R1's novelty rests on **negative searches**, which G0 named
as the least secure conclusion in its report. D-3 is therefore conditional on the Phase-2
threat check in `audit/R1_THREAT_CHECK.md` returning SAFE. If it returns NARROWS or DEAD,
this decision must be revisited by the operator before further work.

**Executed 2026-08-20.** `audit/CLAIM_GRAPH.md` was rewritten around R1 and R2, with the
original C1/C2 analysis **appended and preserved**, not deleted.

> ### ⛔ D-3 IS SUSPENDED — the condition it was recorded under has failed
>
> The Phase-2 threat check returned **DEAD**, not SAFE. R1's mechanism is prior art:
> **Freidling, Zhao & Gao (arXiv:2405.07026)** publish it as a named rejection-sampling
> algorithm with the same cost analysis, the **April-2026 review** (Neufeld, Perry &
> Witten, arXiv:2604.09779) catalogues it as a known Monte Carlo strategy, and **Liu,
> Markovic-Voronov & Taylor (arXiv:2203.14504)** — cited in D-3 as identifying the barrier —
> in fact removes it. Full evidence: `audit/R1_THREAT_CHECK.md`.
>
> D-3's verbatim text is **retained above, unedited**, because it is the operator's own
> words and the record of what was decided and why. It is **not** live guidance. No work
> proceeds on R1 as stated until the operator answers **Q-8**.

---

## D-4 — Repository visibility: public during build, private before the paper.

**Date:** 2026-08-20 · **Answers:** Q-2, partially

**Decision.** The repository stays **public** through the research and build phase, and is
switched to **private** immediately before the paper draft or final results are committed,
ahead of the double-blind Sim2Science submission.

**Rationale.** Operator's considered judgement, made with G0's warning in front of them.
What is public during the build phase is audit trail, a simulator, and a diagnostic — none
of which is the submission. The double-blind risk attaches to the manuscript and to final
results, not to the scaffolding.

**What it forecloses.** No session is to re-raise visibility as a blocker on committing
code, and no session is to change visibility itself — that is the operator's action, at
`https://github.com/pa1aash/Sim-Attrib/settings`. The banner at the top of `OUTSTANDING.md`
carries the reminder until it is resolved.

---

## D-6 — R2 is cited infrastructure, not a claimed method contribution.

**Date:** 2026-08-20 · **Recorded by session G3, executing the operator's Q-10 decision**
· **Evidence:** `audit/R2_THREAT_CHECK.md`, verdict **NARROW-CONDITIONAL**

> **On the numbering.** **There is no D-5.** It was named in G2's brief as that session's
> addition and never written, because it was a Phase-3 artefact and G2 stopped at Phase 1
> (`DEVIATIONS.md` D-7 records this). The gap is left rather than closed by renumbering, so
> that a reader who finds D-5 referenced in G2's brief can see what happened to it.

**Decision.** The noisy-rank diagnostic (**R2**) is carried in the eventual paper as
**infrastructure that is cited and used**, not as a claimed method contribution. Concretely:
the paper may say *"we compute the summary Jacobian by central differences and call its
numerical rank at a pre-registered tolerance, following [Cintrón-Arias et al. 2009] for the
rank-and-condition-number screen and [Moré & Wild 2012] for finite differencing under
simulation noise"*. It may **not** say that either the estimator or the rank rule is new.

**Rationale — the operator pre-specified this branch, and the check landed on it.** The Q-10
decision recorded in G3's brief was: run one narrow corrected-instrument check on R2, then
build the diagnostic regardless of the outcome, with the outcome determining only *how R2 is
framed*. The check returned **NARROW-CONDITIONAL**:

- the rank + condition-number screen on a sensitivity matrix is **Cintrón-Arias, Banks,
  Capaldi & Lloyd (2009)**, 122 citations, worked on an **epidemic model**;
- finite differencing under simulation noise is **Moré & Wild (2010/2012)**, with a *"provably
  near-optimal"* difference parameter — a stronger result than R2's h-sweep;
- the only unoccupied seam is that nobody carries the estimated noise level forward into the
  **rank tolerance** (four full-text zeros, live control). That seam is one sentence wide, and
  `docs/THRESHOLDS.md` does not in fact occupy it — it derives `τ = 10⁻²` from a **compute
  budget**, not from a noise level.

**What it forecloses.** "We contribute a simulation-based rank estimator" and "we contribute a
rule for calling numerical rank under noise" are both unavailable as contributions and must
not reappear as such — the same way ex-C2's identifiability characterisation became a cited
precondition under **D-3**. Any future session that wants to claim the noise-calibrated
tolerance seam must **first** either re-derive `τ` from a noise level, with a `DEVIATIONS.md`
entry stating that the numeric threshold changed and why the change is not motivated by a
result, or state plainly in the paper that the project named the gap and did not fill it.

**What it does NOT foreclose.** R2's *empirical output* — whether a standard 3-component SIR
simulator passes its own rank condition, and under which summary set — is untouched by this.
That is a finding about this simulator, not a claim about method, and its value does not
depend on any novelty verdict. It is what Phase 2 produces.

**What it does not settle.** **R2a** — whether an h-plateau exists at all for this simulator.
If it does not, no rank call is defensible and the diagnostic is uninterpretable regardless of
framing. That is an empirical question, answered by the run and not by the literature. A
second, sharper threat is recorded in `audit/R2_THREAT_CHECK.md` §1.3: the sloppy-models
literature (Gutenkunst et al. 2007, 1,152 citations) finds these spectra **gapless**, and a
gapless spectrum makes any rank threshold a statement about the analyst rather than the model.
`docs/THRESHOLDS.md` §1.4's unresolved-singular-value rule is the pre-registered place where
that would surface.

**Executed 2026-08-20, session G3.** The diagnostic was built and run; see `results/`.
Docstrings and results-file descriptive fields describe R2 in these terms and not in the
terms of `PLAN_SOURCE.md`, G0's C1/C2, or G1's R1 (brief §2.10).

---

## D-7 — D-4's visibility trigger has fired. Recorded, not executed.

**Date:** 2026-08-20 · **Recorded by session G4** · **Depends on:** D-4 · **Action:** O-1, P-4

**This entry records that a condition already decided in D-4 has been met. It does not make a
new decision and does not reopen D-4.**

**The condition.** D-4 fixed the repository as public during the build and private *"immediately
before the paper draft or final results are committed"*; `OUTSTANDING.md` **O-1** states the same
trigger as *"the moment `paper/` gains a draft or `results/` gains a final number."*

**The finding.** `results/` contains numbers — five files produced by session G3, recorded in
`results/SUMMARY_TABLE.md`, each carrying a provenance header naming the commit and seed that
produced it. G3 raised this as a factual notice and hedged it as *"arguably"* met. **The operator
has now resolved the hedge: the trigger has fired.** That resolution is what this entry records.

**Measured state, not assumed state.** `gh` is not authenticated on this machine (**O-4**), so
`gh repo view` was unavailable. Visibility was measured instead through the **unauthenticated**
GitHub REST API, which answers the question without credentials: an anonymous
`GET /repos/pa1aash/Sim-Attrib` returned **HTTP 200** with `"private": false`,
`"visibility": "public"`. **A private repository returns 404 to an anonymous request**, so the
check gives different answers in the two cases and is a real check rather than a restatement of
what was already believed — the test standing constraint S3 requires of anything written as a
flag. Measured state at 2026-08-20: **PUBLIC**.

**What this session did about it: nothing, deliberately.** D-4 forecloses any session changing
visibility itself. The operator was notified. **See D-11 for how the operator ruled**: the
repository stays public through the build phase and is switched before submission, which means
the sentence "is making the switch directly on GitHub" — written by G4 as an expectation about
what would follow — was an expectation and not an observation. It is left in place, corrected
here rather than edited away.

**What it forecloses.** Nothing new. It removes one thing only: a later session may not treat the
trigger as still-open or still-arguable. It has fired, on a specified date, against a measured
visibility state. **P-4** is the confirmation that the switch was made, and it belongs to the
operator.

**What it does not settle.** Whether the switch has actually happened. This session can see the
repository was public when it looked; it cannot see what the operator does afterwards, and it
must not be read later as evidence that the repository is still public.

---

## D-11 — The visibility trigger is ruled on: public through build, private before submission.

**Date:** 2026-08-20 · **Recorded by session G5** · **Depends on:** D-4, D-7 · **Action:** O-1

**This is the operator's ruling on the trigger D-7 recorded as fired. It is a decision, not a
notice, and it is the last word on the subject until the switch is made.**

**The ruling, verbatim in substance.** The repository **remains PUBLIC through the build
phase**. It will be switched to **PRIVATE before submission**, as a separate action, outside
any session's scope. The operator reconfirmed this explicitly after G4 flagged the D-4/D-7
trigger.

**What it changes about D-4.** Nothing about the destination; only the timing. D-4 set the
switch at *"immediately before the paper draft or final results are committed"*, and D-7 found
that `results/` gaining numbers had met that condition. The operator has weighed the trigger
having fired against the cost of switching mid-build and has chosen to carry the exposure to
the end of the build. **That is a judgement about the operator's own risk, and it is theirs to
make.**

**What it forecloses, and this is the part that matters for future sessions.** No session may
re-raise repository visibility as an open question, re-measure it, treat it as pending, or
argue that the fired trigger obliges action now. **It is settled.** A session that finds itself
reasoning about visibility should stop and cite this entry.

**What it does not settle.** Whether the switch has been made — it has not, by design, and it
is not due yet. **O-1** stays open as an operator action with a stated trigger of "before
submission", and P-4 in `audit/S4_REPORT.md` is superseded by this entry rather than answered
by it.

**The honest reading.** This is a decision to accept a known, named exposure for a stated
period, made with the trigger visible rather than in ignorance of it. That is a different thing
from an unresolved item, and the difference is the reason this entry exists.

---

## D-12 — DECIDED: Path 1. Measure the cost gate before building the composition.

**Date proposed:** 2026-08-20 (session G5) · **Date decided:** 2026-08-20 (operator, at the
start of session G6) · **Status: DECIDED — Path 1 ADOPTED.** · **Evidence:**
`audit/K6_SPECTRUM_CHECK.md`, `audit/S5_REPORT.md` · **Closes:** P-2, `OUTSTANDING.md` O-24

> ### The decision, recorded above the reasoning it was taken on
>
> **Path 1 is adopted. The cost gate is measured before the composition is built.** Session
> G6 is commissioned to take that measurement **and no more**: the MMC composition is not to
> be implemented in the same session that prices it, whatever the price turns out to be, so
> that a favourable number cannot be converted into a build inside the session that produced
> it. Building is G7's scope and is gated on G6's result.
>
> **What this forecloses.** It forecloses spending a session on the diagnostic-only paper of
> `audit/PIVOT.md` *before* the affordability of the composition is known. It does **not**
> foreclose Path 2 itself: every artefact Path 2 needs already exists, none of it is consumed
> by measuring the cost gate, and a failed gate is the evidence on which Path 2 would be
> chosen deliberately rather than out of fatigue.
>
> **What it does not decide.** It does not decide that the composition will be built. It
> decides only the order: price first, then decide. If the gate fails, the choice returns to
> the operator with one measurement in hand instead of none — which is the reason for the
> ordering.
>
> **The argument against, which the operator has weighed and overridden.** Six sessions of
> history say attack before you build, and the composition has still never been attacked by
> anyone (`OUTSTANDING.md` **O-17**, older half). Measuring the cost gate is not an attack on
> the composition and does not discharge that debt. It remains outstanding.

**The body below is session G5's proposal exactly as it wrote it, unedited.** It is kept
because the decision above is only legible next to the case that was actually put.

**This entry exists because the G5 brief requires the diagnostic-only pivot to be written down
as a proposed path whenever the session halts. It halted. But the brief anticipated a halt
caused by `S_B`'s separability being overturned, and that is not what happened**, so writing
the pivot as though the evidence forced it would misrepresent the evidence. Both paths are
below, with an honest reading of which the numbers favour.

### What G5 actually established

- **`S_B` separates the three components under all eight component-wise family assignments**
  the two declared sets permit — `κ` from 6.628 to 65.64, every singular value resolved, six of
  the eight never tested before. This is the **strongest** evidence the project has for the
  separability precondition of `audit/MMC_COMPOSITION_SPEC.md` §5.
- **The same property fails at two distortion parameters per component** — the six-column
  union is INSEPARABLE at `κ = 628.9` with a progression–observation confound that is not an
  estimator artefact, not a threshold artefact, and not structural.
- **`p_sel` is still unmeasured and the cost gate still unbuilt.** The session halted before
  Phase 2 because the brief permits continuation only in the absence of *"any verdict other
  than a clean pass"*, and WEAKENED is not a clean pass.

### Path 1 — measure the cost gate, then build the composition (what the evidence favours)

The composition's precondition is a `K = 3` statement and it is met, eight times over. Nothing
G5 found touches it. What stands between the project and its first experiment is unchanged from
what G4 said: **`p_sel`, the cost gate, and then the build** — Phases 2 and 3 of the G5 brief,
run as written.

**Cost:** one session, possibly two. **Risk:** the cost gate may fail, which is a real
possibility the G5 brief priced explicitly and which would land the project back at this
decision with one more measurement in hand rather than none.

**What it must carry into the paper regardless:** the six-column result, as a stated
limitation. **Q-14** is the question of which sentence; the recommendation there is the
one-parameter sentence with the two-parameter failure conceded rather than omitted.

### Path 2 — the diagnostic-only pivot (`audit/PIVOT.md`, the pivoted paper)

The rank diagnostic itself as the contribution: the identifiability statement, the boundary,
the diagnostic that checks it before any inference is run, and the empirical finding. No
attribution experiment, no MMC composition, no `p_sel`.

**What G5 adds to this path's case, and it is not nothing.** `PIVOT.md` deliverable **P4**
requires the diagnostic run *"across several defensible summary sets, not one"* and **P5**
requires *"the threshold … justified and its sensitivity reported"*. Both are now
substantially discharged: three summary sets, eight family assignments, nine tolerances across
four decades, both threshold couplings, the `κ_max` branch mapped in closed form and checked
against the production rule at 108 grid points per spectrum, and a six-column counterexample
that gives the boundary teeth. **The diagnostic-only paper is closer to written than the
composition paper is to built.**

**What weakens this path's case.** `PIVOT.md`'s pivoted paper was framed around a *negative*
empirical finding — deliverable P4 anticipates *"a realistic simulator fails the condition
under defensible summary sets"*. **That is not what the simulator does.** `S_B` passes under
every assignment tried. The available finding is the more nuanced and less quotable one: the
condition holds at one distortion parameter per component and fails at two. That is a real
result and it is harder to headline than a clean negative.

### The honest reading, offered as a recommendation and not as a decision

**Path 1.** The precondition is met and better supported than at any point in this project's
history; the cost gate is a measurement that has been deferred through two sessions and decides
the question either way; and Path 2 remains fully available afterwards, since every artefact
Path 2 needs already exists and none of it is consumed by attempting Path 1. **Path 2 is not
foreclosed by trying Path 1 first, and Path 1 is foreclosed by nothing except a failed cost
gate — which is itself the information needed to choose Path 2 on evidence rather than on
fatigue.**

**The argument against the recommendation, stated so it is not only implied.** This project has
adopted three headlines and lost all three, and the composition it would be building has
**still never been attacked by anyone** (**O-17**, the older and larger half, unpaid through
six sessions). Building it before it has been refuted repeats the pattern that killed G0, G1
and G2 — construction ahead of criticism. A reader of this repository's history could
reasonably conclude that the next thing to do is attack the composition, not implement it, and
that would be Path 1 with its first two steps swapped.

**This is a decision, not a calculation, and it is the operator's.** **P-2.**

---

## D-14 — DECIDED: the paper's scope is restricted to single-mechanism-per-component misspecification.

**Date:** 2026-08-20 · **Decided by the operator** at the start of session G6 · **Answers:**
Q-14 (blocking since G5) · **Evidence:** `audit/K6_SPECTRUM_CHECK.md`,
`results/robustness/k6_spectrum.yaml` · **Closes:** `OUTSTANDING.md` O-23, P-3 of G5

### The decision

**Every claim this project makes about component separability, component attribution, and the
composition that rests on them is scoped to a distortion model that assigns AT MOST ONE
one-parameter distortion family to each component.** Inside that scope the separability
precondition holds and is well supported: `S_B` separates the simulator's three components
under **all eight** component-wise assignments the two declared family sets permit, `κ` from
6.628 to 65.64, every singular value resolved.

**Outside that scope the project's own measurement is a counterexample and the claim is not
available.** With two distortion parameters on a component — the six-column union of the two
declared sets — `S_B` is INSEPARABLE at `κ = 628.9`, rank 4 of 6, with both near-null
directions confounding **progression with observation**. It is not an estimator artefact
(every singular value resolved to within 2.3% across the h-plateau), not a threshold artefact
(INSEPARABLE across `τ` from 0.005 to 1.0), and not structural (`d = 10 ≥ 6`).

### This is a limitation to be stated alongside the positive result, not after it

**The operator's instruction is explicit on placement and it is recorded here so that a later
session cannot demote it.** The single-mechanism restriction is not an audit footnote. It is a
condition on the result, and a reader who is told the eight-assignment finding without it has
been told something the evidence does not support.

Concretely, this requires all four of:

1. **`paper/main.tex`, when it is drafted, must state the restriction in the scope or
   limitations section**, and must state the six-column counterexample rather than omit it.
   No session has drafted `paper/main.tex` as of this decision; the requirement is recorded
   now precisely because the drafting session will be several sessions away from the
   measurement that produced it.
2. **Any results file this project writes from here on carries the restriction inline**, in
   the same way `results/` already carries the distortion-family qualification.
3. **`audit/MMC_COMPOSITION_SPEC.md` states it**, because the composition's implementation
   must include a precondition check that refuses to run outside the scope rather than
   running and reporting a number.
4. **The sentence the paper writes is Q-14's option (a)** — *"under a distortion model that
   assigns one one-parameter family to each component, the three components separate for
   `S_B` under every one of the eight assignments our two declared family sets permit"* — and
   not any sentence implying that component-level misspecification is identifiable
   irrespective of how richly a component is parameterised. That stronger sentence is refuted
   by this project's own `results/robustness/k6_spectrum.yaml`.

### What it forecloses

It forecloses the general identifiability claim, permanently, on this project's own evidence.
It also forecloses quoting the eight-assignment result on its own: **eight separable
assignments establish separability of a three-dimensional distortion space, eight times over,
and nothing wider.**

### What it does NOT do

- **It does not close Q-13.** Q-13 asks what may be claimed from a verdict conditional on the
  *distortion families*; D-14 answers the different question of how many parameters a
  component may carry. The two are jointly, not severally, binding on the paper's separability
  sentence, and **Q-13 remains open and blocking**.
- **It does not make the restriction true.** It records the operator's ruling that the project
  will work inside a scope where the evidence supports the claim. Whether a component's
  misspecification is one-dimensional in any real application is a modelling question, and the
  honest answer — already written into `docs/OPEN_QUESTIONS.md` Q-14 — is that it need not be.
- **It does not bear on the cost gate.** `p_sel` and affordability are a different quantity;
  D-14 neither blocks nor licenses that measurement.

---

## D-16 — DECIDED: the MMC composition is dropped as an experimental vehicle and kept as a stated negative result.

**Date:** 2026-08-20 · **Decided by the operator** at the start of session G7 · **Answers:**
Q-16 (blocking since G6) · **Evidence:** `results/cost_gate.yaml`, `results/p_sel.yaml`,
`audit/S6_REPORT.md` · **Closes:** P-2 of G6 · **Executes:** Q-16 option (c), the
diagnostic-only path of `audit/PIVOT.md`

### The decision

**The MMC + selection-event composition is not built.** It is retained in the paper as a
**negative result**: a quantified account of why naive rejection-sampling-based exact
conditional inference does not terminate for this class of simulator.

**The paper's scope is closed at four contributions**, and no session may widen it without a
new decision here:

1. **The rank/coherence diagnostic** — the method.
2. **The eight-assignment separability result for `S_B`** under single-mechanism distortion —
   the positive result, scoped by **D-14**.
3. **The `K = 6` cross-mechanism confound** — the boundary result, which is where D-14's
   assumption is load-bearing rather than decorative.
4. **The MMC non-termination finding** — the cautionary result, stated as a genuine negative
   result and quantified.

### Why, and the part that is not a compute argument

**The gate failed on termination, not on price.** Over the nuisance set the minimum acceptance
probability is zero — no draw in 100,000 enters the observed cell at a relative half-width of
0.05, 95% upper bound 3.84×10⁻⁵ — and the mechanism is structural. `audit/MMC_COMPOSITION_SPEC.md`
§3.4's lemma, the composition's only theorem, requires the selection rule to be a **fixed
function of the data**; the nuisance parameters move the normalised summaries by a median of 27
and up to 65 standard deviations at that half-width, against a single-draw noise magnitude of
√10 ≈ 3.16; a `θ`-free rule facing a shift twenty times the noise selects deterministically, and
the cell the data actually selected becomes unreachable. **A larger machine does not touch
that**, which is what removes "build it anyway on more compute" from the table.

**The two alternatives, and their prices, both refused.** Option (a) — bound `Ω₀` until the
cells stay reachable — buys termination with Dufour's own CSEMMC downgrade from finite-sample to
asymptotic validity, i.e. by surrendering the property the composition exists for. Option (b) —
find a selection rule that survives nuisance drift without becoming `θ`-dependent — requires
inventing one *after* seeing the measurement that killed the obvious one, which is the leakage
failure `LEDGER_DESIGN.md` D3 names.

### This is not a smaller paper. It is a different and more defensible one.

Sim2Science's call names **"simulator diagnostics"** and **"analysis of … degeneracy,
simplifications, and identifiability"** among its interests. The four contributions above are
that paper: here is the identifiability condition, here is the diagnostic that checks it before
any inference is run, here is exactly where the condition's scope assumption breaks, and here is
why the obvious exact procedure for acting on the condition does not terminate. **The last
clause is a contribution and is to be written as one**, not as an apology for an unbuilt
experiment.

### What it forecloses

- **No session may implement the composition, the rejection sampler, or the maximiser** without
  a superseding decision recorded here. `src/attribution/` keeps the selection rule, which is
  now evidence for contribution 4 rather than infrastructure for an unbuilt experiment.
- **No session may report the composition as "future work with a compute caveat".** The
  obstruction is not compute and describing it that way misstates this project's own
  measurement.
- **`audit/MMC_COMPOSITION_SPEC.md` becomes a historical / negative-result document**, not a
  build target. Its content is not deleted: it is the source for the negative-result section
  and for the non-termination figure.

### What it does NOT do

- **It does not withdraw any number.** Nothing in `results/` is affected; the separability
  precondition stands inside D-14's scope.
- **It does not close Q-13**, which remains open and blocking for the paper's separability
  sentence, nor does it touch D-14, whose four placement obligations still land on
  `paper/main.tex`.
- **It does not claim the composition is wrong.** It claims this simulator cannot serve as its
  demonstration, and states the property of the simulator — the nuisance-to-noise ratio — that
  makes it so, so that a reader can check their own.
- **It does not license a scaled-down or hidden version of the experiment.** §4's own words: on
  a failed gate *"the honest output is the cost analysis itself, not a scaled-down experiment
  that hides it."*

**Executed 2026-08-20 (session G7).** Q-16 marked ANSWERED in `docs/OPEN_QUESTIONS.md`;
`audit/MMC_COMPOSITION_SPEC.md` re-headed as historical; the boundary sweep (**O-30**) run as
characterisation of the negative result; the claim set consolidated in
`audit/FINAL_CLAIMS.md`.

---

## Not decisions — still open

`Q-3` (reciprocal reviewer), `Q-6` (multi-component scope), and `Q-7` (citation-error
policy) remain open operator questions and are **not** settled by anything above. See
`docs/OPEN_QUESTIONS.md`.
