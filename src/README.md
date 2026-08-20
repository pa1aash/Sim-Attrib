# src/

All executable code: simulators, perturbation bases, diagnostics, and attribution
procedures. Subdirectories are `simulators/`, `diagnostics/`, and `attribution/`.

**Belongs here:** deterministic, seeded, runnable code. Every script that emits a
number must write that number to a file in `results/` and must record the seed, the
git commit of the working tree, and its own path in the output. `PROVENANCE.md`
defines the required shape of that record.

**Does not belong here:** results, figures, notebooks used as scratch space, or
anything that reads real observational data. This project is synthetic by design —
ground truth is known by construction because a component is deliberately knocked
off-spec.

**Status, session G3 (2026-08-20): this directory now contains code.** `simulators/sir3.py`,
`simulators/summaries.py`, `diagnostics/jacobian_rank.py`, `diagnostics/floor_check.py`,
`diagnostics/run_diagnostic.py`, `diagnostics/report_tables.py`, and `provenance.py`. Tests
are in `tests/`. `attribution/` is still empty.
