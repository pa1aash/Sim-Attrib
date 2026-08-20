# src/attribution/

Procedures that, given simulator output and a set of candidate component distortions,
name a component or an equivalence class of components.

**Belongs here:** the competitive/conditional attribution procedure with error control
over the *selected* component; the baselines it is measured against, including the
degenerate uniform/random attributor that establishes the 1/K floor; and the logic that
reports equivalence classes wherever the rank condition fails.

**Hard constraint enforced in this directory:** the attributor must never receive, by
argument, filename, global, or side channel, the identity of the component that was
knocked off-spec. Any code path that could leak it is a correctness bug, not a style
issue. Test for leakage explicitly; a leaked ground-truth label produces accuracy
numbers that are worthless and not obviously wrong.

**Does not belong here:** the separability diagnostic, which must be runnable and
reportable independently of whether any attributor works.

**Status, session G3 (2026-08-20): still empty, deliberately.** The selection event and the
maximized-Monte-Carlo composition that would live here are SPECIFIED but not implemented —
`audit/MMC_COMPOSITION_SPEC.md`. Implementing them is the next session's work and is
contingent on the cost gate in §4 of that specification.
