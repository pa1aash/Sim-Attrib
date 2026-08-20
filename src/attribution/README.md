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

Empty. No attribution code exists yet.
