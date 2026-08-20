# results/

Every number this project emits.

**Belongs here:** one file per emitting script, named for that script. Each file records
the numbers, the seed(s), the git commit of the tree that produced them, the exact
command line, and the wall-clock date. `PROVENANCE.md` at the repository root defines
the contract; a results file that does not satisfy it is not admissible in the paper.

**Does not belong here:** hand-edited numbers, numbers copied from a terminal into a
document, numbers transcribed from a prior run, or aggregate figures whose inputs are
not themselves in this directory. If a number appears in the manuscript and cannot be
traced to a file here, it does not go in the manuscript.

Accuracy figures carry a further requirement: they are quoted against the 1/K degenerate
floor, never in isolation. A results file reporting attribution accuracy must record K
and the corresponding floor alongside the accuracy.

**Status, session G3 (2026-08-20): no longer empty.** `floor_check.yaml`,
`jacobian_rank.{S_A,S_B,S_C}.yaml`, `jacobian_rank.S_A.no_crn_control.yaml`, and the generated
`SUMMARY_TABLE.md`. These are the project's first numbers.

`SUMMARY_TABLE.md` is **generated** by `src/diagnostics/report_tables.py` and must not be
edited by hand; it exists so the reports in `audit/` can quote results without any number
being typed into a markdown file.

**Added session G7 (2026-08-21).** `boundary_sweep.yaml` and the generated
`BOUNDARY_TABLE.md`, from `src/diagnostics/boundary_sweep.py` and
`src/diagnostics/report_boundary.py`. They locate the nuisance half-width at which the MMC
composition's selection cells stop being reachable — `OUTSTANDING.md` O-30, closed. The sweep
is **characterisation of a decision already taken** (`docs/DECISIONS.md` D-16) and the results
file says so in every gate row a reader might land on, because a number that could be read as
re-pricing a closed question has to carry its own context.

`boundary_sweep.yaml` was written twice. The second run corrected a defective check and
reproduces the first bit-for-bit in every measured field; `DEVIATIONS.md` **D-16** and
**D-17** record what changed and why the overwrite loses nothing.
