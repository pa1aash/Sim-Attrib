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

**Status, session G6 (2026-08-20):** `attribution/` is no longer empty — it holds
`selection.py`, the selection rule the composition specification deferred, and nothing else.
`diagnostics/` has gained `p_sel.py` and `cost_gate.py`. Sessions G4 and G5 added
`diagnostics/{crn_count_check,threshold_sensitivity,summary_smoothness_check,wide_spectrum_check,run_family_check,report_robustness,k6_spectrum,report_k6}.py`
and `runlock.py`.
