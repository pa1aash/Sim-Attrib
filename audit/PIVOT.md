# Pre-registered pivot

**Written 2026-08-20, before the literature verdict was known.** No search had been run
against the canonical research query when this file was committed; the commit history
establishes that. It is a plan, not a rescue.

The operator has already accepted the premise: **if C1 dies, the paper becomes a smaller
one built on C2 alone.** This file specifies what that paper claims, what it must show,
and what it drops.

---

## Trigger

The pivot fires if **any** of the following is established:

- **B3 refuted** — Anau Montel, Alvey & Weniger's distortion tests are competitive rather
  than marginal;
- **B4 refuted** — they do report error control over the selected component;
- **C1b resolves per-component** — RNPE's model-criticism step operates per simulator
  component rather than per summary statistic;
- **F2 refuted** — the selective-inference guarantees C1's method depends on do not
  transfer to the simulator-distortion setting.

Any one is sufficient. They are not scored or weighed; the plan's own differentiators
are B3 and B4, and losing either removes the stated difference from the gatekeeper.

**The pivot does not fire on E3.** If E3 fails, C2 is the thing that is damaged, and the
pivot has nowhere to go. That case is handled at the bottom of this file.

---

## The pivoted paper

**Title shape:** the limits of component-level discrepancy attribution in
simulation-based inference.

**One sentence:** per-component discrepancy attribution is not identifiable from data
alone; here is the exact condition under which it becomes identifiable, a diagnostic that
checks it before any inference is run, and evidence that a realistic simulator fails it.

### What it claims

1. **A limits result.** Per-component discrepancy attribution is non-identifiable without
   further structure, because the data constrain only the sum of per-component
   discrepancies. Any reallocation preserving the total is observationally equivalent.
2. **A boundary.** Attribution is identifiable on the subspace where the summary Jacobian
   has full column rank; outside it, only equivalence classes are recoverable.
3. **A diagnostic.** The rank/coherence computation, which requires simulations only —
   no observed data, no fitted posterior, no inference machinery — and which therefore
   costs almost nothing to run before committing to a study.
4. **A negative empirical finding, if that is what the diagnostic returns.** That a
   realistic, standard, published-in-spirit simulator fails the condition under
   defensible summary sets.

### What it must show

| # | Deliverable | Why it is required |
|---|---|---|
| P1 | The identifiability statement, proved, with the additive-decomposition assumptions stated exactly | It is the paper's core. It is also close to definitional, so the proof must be honest about how much work it does. |
| P2 | **A precise, defended statement of what the rank condition adds beyond standard local structural identifiability** | Non-negotiable. See "The E3 problem" below. Without it the paper is a restatement. |
| P3 | The diagnostic implemented, on a 3-component SIR simulator, with rank, condition number, and pairwise coherence | The first technical deliverable regardless of pivot. |
| P4 | The diagnostic run across **several defensible summary sets**, not one | A negative result under one summary set is a statement about that choice, not about the simulator. |
| P5 | Equivalence classes recovered, with the singular-value/coherence threshold justified and its sensitivity reported | The threshold is a substantive part of the method; see D8 in `LEDGER_DESIGN.md`. |
| P6 | A demonstration that a method which ignores the condition mis-attributes where the condition fails | Turns the limits result from an observation into a warning with consequences. **This is C1's negative half, which survives even when C1's positive half dies** — see below. |
| P7 | Engagement with structural and practical identifiability (M1, M2) and with global sensitivity analysis (M4) | These literatures ask a version of the same question. Their absence from the plan's bibliography is a coverage gap, not evidence of novelty. |

### What it drops

- The competitive-vs-marginal comparison as a **claimed contribution**.
- Error control over the selected component as a **claimed contribution**.
- The e-BH/knockoff selection machinery, and with it the dependency on F2.
- The collinearity-sweep mis-attribution curve as the *headline* figure. The headline
  becomes the rank diagnostic itself.

### What it keeps that is easy to overlook

**C1's negative half survives its positive half.** Even where the pivot fires, the
demonstration that marginal per-component testing mis-attributes under collinearity
remains true and remains worth showing — it is what makes the identifiability result
consequential rather than merely correct. It is demoted from "our method fixes this" to
"here is what goes wrong when the condition is ignored", which needs no selective-inference
guarantee and therefore does not depend on F2. P6 is that demotion.

This matters because the collinearity sweep is the most expensive experiment in the
project, and the pivot **does not** make it wasted work.

---

## Venue consequence

The pivoted paper is a limits-and-diagnostics result about imperfect simulators, with no
selection or error-control contribution. **Sim2Science is then the only sensible home**
of the three candidates; the e-values venue loses its hook entirely, since the e-value
machinery is precisely what was dropped. See `VENUE.md`.

The pivoted paper is also **shorter and more certain**, which suits a 5-page non-archival
workshop format better than the full version does. This is worth saying plainly: the
pivot is not obviously the worse paper. A clean limits result with a cheap diagnostic is
more likely to be used than a method with a guarantee that holds under assumptions a
reader cannot check.

---

## The E3 problem — the case this pivot does not cover

The pivot assumes C2 is intact. If **E3** fails — if the full-column-rank condition is
the standard local structural-identifiability criterion restated in SBI vocabulary — then
C2 is an application, and the pivot has nothing left to pivot to.

**Pre-registered response, in order of preference:**

1. **Sharpen the claim to what is actually new.** Candidates, all of which must be
   checked rather than asserted: that the perturbations are *functional* (whole distortion
   families δ_k(·; η_k)) rather than scalar parameters; that the attributed object is
   *model discrepancy* rather than a model parameter; that the condition is evaluated from
   simulation alone, with no likelihood and no observed data, which is what makes it
   deployable in the SBI setting where the classical machinery cannot run. If one of
   these holds, the contribution is **the transfer and its consequences**, stated as such
   — not as a new theorem.
2. **Let the empirical finding carry the paper.** "A standard 3-component SIR simulator
   fails the separability condition under every summary set we tried, so component
   attribution is not achievable for it" is a legitimate and useful negative result for
   an imperfect-models workshop, independent of who first wrote the rank condition.
3. **Report the negative outcome and stop.** If neither 1 nor 2 holds, this is a project
   that has learned its central question was answered elsewhere. Recording that clearly is
   the correct output, and it costs days rather than weeks — which is the whole reason the
   diagnostic is the first thing built.

Option 3 is a real option. It is written here, in advance, so that reaching it is a
decision rather than a failure.
