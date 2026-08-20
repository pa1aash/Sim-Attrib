# src/diagnostics/

Diagnostics computed from simulations alone, with no observed data.

**Belongs here:** the Jacobian rank/coherence diagnostic — the summary Jacobian
d(summaries)/d(per-component perturbation), its rank, its condition number, and the
pairwise coherence between component directions. This diagnostic *gates everything
downstream*: it decides before any inference is run whether components are separable
for a given simulator and summary set.

This directory also owns the STOP condition. If the rank diagnostic reports that
components are inseparable under any reasonable summary set, the correct output of this
project is a negative identifiability result, not an attribution method.

**Does not belong here:** anything that requires observed data, anything that requires a
fitted posterior, and any procedure that selects a component. Selection lives in
`../attribution/`.

**Status, session G3 (2026-08-20): built and run.** `jacobian_rank.py` is the diagnostic,
`floor_check.py` the random-attributor floor, `run_diagnostic.py` the runner that emits
`results/jacobian_rank.*.yaml`, and `report_tables.py` generates the tables the reports quote
so that no number is hand-typed into a markdown file.

The STOP condition is owned here and **did not fire**: see `results/SUMMARY_TABLE.md` §7.

A note on framing, because it has changed since this file was written: the diagnostic is
**infrastructure, cited not claimed** (`docs/DECISIONS.md` D-6). It does not gate "everything
downstream" in the sense of being the paper's contribution; it establishes the precondition
under which the composition specified in `audit/MMC_COMPOSITION_SPEC.md` is worth building.
