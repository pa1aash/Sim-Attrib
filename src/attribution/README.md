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

**Status, session G6 (2026-08-20): one file, and deliberately only one.** `selection.py` is the
selection rule `k-hat` and the per-component discrepancy statistic `T_k` it maximises. It exists
because `audit/MMC_COMPOSITION_SPEC.md` §6 left `T_k` *"not specified"* and *"deferred"*, and
`p_sel` — the quantity the cost gate turns on — is a property of the cell `T_k` defines, so it
could not be measured until the rule existed. `DEVIATIONS.md` **D-14** records the choice and
what a different one would do to the number.

**The composition itself is still not implemented.** No rejection sampler, no nuisance
maximiser, no p-value. The cost gate that was to gate its construction has since been measured
and it **failed** — `results/cost_gate.yaml`, `docs/OPEN_QUESTIONS.md` **Q-16** — so whether
anything further is ever built here is now an open operator question rather than a scheduled
piece of work.
