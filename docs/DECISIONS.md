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

## Not decisions — still open

`Q-3` (reciprocal reviewer), `Q-6` (multi-component scope), and `Q-7` (citation-error
policy) remain open operator questions and are **not** settled by anything above. See
`docs/OPEN_QUESTIONS.md`.
