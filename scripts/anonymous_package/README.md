# Diagnostics and Limits for Component-Level Simulator Misspecification

Anonymized reproducibility package for a paper submitted for double-blind review.

This package contains the code and result data behind every number, figure, and
table in the paper. The paper itself is submitted separately; it is not included
here.

## What this is

A diagnostic that checks, for a compartmental epidemic simulator with three
components (transmission, progression, observation), whether the available summary
statistics can distinguish *which* component is responsible for a misspecification.
The method is a rank-and-condition-number screen on a simulation-estimated Jacobian
(established diagnostic machinery, applied to a new setting); the paper's contribution
is the finding, not the diagnostic. A second part of the paper composes a selective-
inference construction (maximized Monte Carlo + rejection-sampling calibration) on top
of the identifiable case and measures where it becomes unaffordable.

## Setup

Python 3.11+ (developed and tested on 3.13/3.14). From this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

No GPU, no external data, no network access is required. Every experiment is CPU-only
forward simulation of a compartmental ODE plus finite-difference linear algebra.

## Layout

```
src/simulators/     the three-component SIR simulator and its distortion families
src/simulators/summaries.py   the three summary-statistic sets (S_A, S_B, S_C)
src/diagnostics/    the rank/condition-number diagnostic and every robustness check
src/baselines/      the comparison against Anau Montel, Alvey & Weniger (2025)'s
                     global-null test (Section 2 of the paper)
src/attribution/    the selection rule used by the selective-inference composition
src/viz/            the figure-generation scripts (matplotlib, one script per figure);
                     figures themselves are not included, only the code that draws them
results/            every emitted numeric result, as YAML, one file per experiment
tests/              the unit test suite
```

Every script under `src/diagnostics/`, `src/baselines/`, and `src/viz/` is runnable
directly, e.g.:

```bash
python -m src.diagnostics.jacobian_rank --help
python -m src.baselines.montel_marginal --help
```

Each writes its output to `results/` and never overwrites an existing file silently —
see each script's docstring for its exact invocation and settings.

## Reproducing the paper's numbers

Every numeric result already exists in `results/` (as YAML) so the paper's tables and
figures can be checked without re-running anything. Each result file is
self-describing: it carries a `provenance` block naming the script, the exact command
line, the seed, and the software versions used to produce it. The `host` and `commit`
fields of that block are redacted in this package (they identify the machine and
private repository state the result was originally computed on, not anything about
the result itself); every other field is untouched.

To regenerate a result from scratch, run the script named in its `provenance.script`
field with the same seed; the diagnostic modules are deterministic given a seed.

## Mapping from the paper to this package

| Paper reference | What it is | Result file(s) | Figure script |
|---|---|---|---|
| Section 3 (Method), the diagnostic | rank/condition-number screen | `results/jacobian_rank.S_A.yaml`, `.S_B.yaml`, `.S_C.yaml` | -- |
| Section 4, "eight family assignments" | `S_B`/`S_A` under all 8 component-wise distortion assignments | `results/robustness/k6_spectrum.yaml` | `fig4_assignments.py` (Fig. 1), `fig5_threshold.py` (appendix) |
| Section 4, the six-column confound | `S_B` under two distortion parameters per component | `results/robustness/k6_spectrum.yaml` (`six_columns` block) | `fig3_spectrum.py` (Fig. 2), `fig7_confound.py` (appendix) |
| Section 5, negative-result / MMC | selective-inference cost at a known parameter and over a nuisance box | `results/p_sel.yaml`, `results/cost_gate.yaml`, `results/boundary_sweep.yaml`, `results/confidence_set_mmc.yaml` | `fig6_nontermination.py` (Fig. 3), `fig6b_nontermination_variants.py` (appendix) |
| Section 4, the Anau Montel et al. baseline comparison | the trials-corrected global-null test, run on this project's own simulator | `results/montel_marginal_test.yaml` | -- |
| Section 6 (Limitations), second-theta check | separability verdict at a second, independently-drawn parameter point | `results/second_theta_check.yaml` | -- |
| Appendix, simulator structure | compartment diagram | -- | `fig2_simulator.py` (appendix) |

`CLAIMS.md`, at the top level of this package, gives the exact dotted path inside each
result file for every number the paper's prose cites; the paper's own Appendix A.5
("Claim-to-source table") points here rather than repeating it.

## Tests

```bash
pip install pytest
pytest tests/ --ignore=tests/test_viz.py \
  --deselect tests/test_provenance.py::test_header_records_a_resolvable_commit
```

164 pass. Two categories are excluded above, deliberately, and not because anything is
broken:

- `tests/test_viz.py` (6 tests) exercises the figure-drawing scripts, which read page
  geometry from the NeurIPS venue's `.sty` file. That file is part of the paper
  submission, not this code package, so it is not included here. None of the
  simulator, diagnostic, or baseline code depends on it -- only figure rendering does.
- `test_header_records_a_resolvable_commit` asserts that `git rev-parse HEAD` resolves
  to a real commit, which is true inside the private repository this code was
  developed in and is trivially false in this package, which deliberately carries no
  git history.

Running the full, undeselected `pytest tests/` will show these 7 as failures, not
errors, for exactly the two reasons above.

## License

MIT. See `LICENSE`.
