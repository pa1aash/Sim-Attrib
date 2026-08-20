# Provenance

> **Status, session G3 (2026-08-20): this repository now contains numbers, and the contract
> below was written before any of them existed.** `git log` is the evidence: the contract was
> committed in session G0, and the first results file was written in G3. It has not been
> amended since numbers started to exist, and it should not be.

**The contract as originally written (session G0), unedited:** this repository contains no
numbers. `results/` is empty, `src/` is empty, and nothing has been computed. This document
defines the contract that will govern numbers when they start to exist, and it is written now,
before any exist, so that it cannot be shaped retroactively to fit whatever the first run
happens to emit.

## The rule

Any number that appears in the manuscript, in a figure, in a table, or in a claim
anywhere in this repository must be traceable, without human memory, to:

1. the script in `src/` that computed it,
2. the file in `results/` that captured it,
3. the git commit of the working tree at the moment it was computed,
4. the seed and the exact command line that produced it.

A number that cannot be traced this way does not go in the manuscript. This is not a
tidiness preference. Attribution accuracy is the headline quantity of this project and
it is the kind of quantity that silently changes when a summary set, a seed, a
collinearity level, or a distortion magnitude changes underneath it. Without the chain
above, a stale number is indistinguishable from a current one.

## Required shape of a results file

One file per emitting script, named for that script. Each carries a header:

```yaml
script:      src/diagnostics/jacobian_rank.py
commit:      <full 40-char sha of the tree at run time>
dirty:       false          # true if the tree had uncommitted changes — see below
command:     python -m src.diagnostics.jacobian_rank --sim sir3 --seed 20260820
seed:        20260820
started:     2026-08-20T11:40:00+05:30
finished:    2026-08-20T11:41:12+05:30
host:        <machine identifier>
python:      3.11.x
deps:        numpy==x.y.z, scipy==x.y.z
```

`dirty: true` is permitted during exploration and **disqualifying for any number that
reaches the manuscript**. A dirty tree means the recorded commit does not describe the
code that ran.

## Additional requirement for accuracy figures

Any results file reporting attribution accuracy must record, in the same file:

- `K` — the number of components,
- `floor` — the degenerate accuracy 1/K that uniform random attribution achieves,
- the accuracy of the actual uniform/random attributor as *run*, not as computed
  analytically, so that the harness itself is checked against its own known answer.

Accuracy is reported against the floor. An accuracy quoted in isolation is not
admissible; with K=3 an unqualified "41% accurate" describes a method barely
distinguishable from guessing.

## Leakage attestation

Any results file produced by an attribution run must additionally record:

- `leakage_checked: true|false` — whether the run was executed under the test that
  confirms the attributor cannot observe which component was knocked off-spec.

A `false` here invalidates the accuracy number in that file. Ground-truth leakage does
not produce an obviously broken result; it produces a plausible, publishable, wrong one.

## Figures

Every figure carries, in its caption or in a sidecar file, the results file(s) it was
drawn from. A figure regenerated from changed results gets a new results file, not an
edit to the old one.


---

## What now exists, and where it is verified (added session G3, 2026-08-20)

### Emitting scripts and their results files

| Script | Results file(s) |
|---|---|
| `src/diagnostics/run_diagnostic.py` | `results/jacobian_rank.{S_A,S_B,S_C}.yaml`, `results/jacobian_rank.S_A.no_crn_control.yaml` |
| `src/diagnostics/floor_check.py` (via the runner) | `results/floor_check.yaml` |
| `src/diagnostics/report_tables.py` | `results/SUMMARY_TABLE.md` — **generated**, never hand-edited |

`src/provenance.py` builds the header defined above. It is the only place that header's shape
is defined, so a results file cannot drift from this contract by being written by hand.

### The no-hand-typed-numbers rule, and how it is honoured

Standing constraint S11 forbids hand-typing a number into a markdown file. The reports in
`audit/` need to state what the diagnostic found, so `results/SUMMARY_TABLE.md` is **generated
from the YAML** by `src/diagnostics/report_tables.py`, and the reports quote or reference it.
`results/STOP_CONDITION_FIRED.md` is likewise written by the runner, not by hand, and is
deleted by the runner when the condition does not fire — so its presence is always a current
statement rather than a stale one.

### A run that was discarded, recorded because the discard is otherwise invisible

The **first** production run of the diagnostic was thrown away. It recorded `dirty: true`
because the working tree had uncommitted changes when it ran, and this document makes
`dirty: true` disqualifying for any number that reaches the manuscript. The code was committed
and the run repeated from a clean tree. The discarded files were deleted rather than kept,
because a superseded results file in `results/` is exactly the "stale number indistinguishable
from a current one" this contract exists to prevent.

### Test locations

Required by the session G3 brief §2.11.

| What is tested | Where |
|---|---|
| `δ_k(·;0)` is **bit-identical** to the base simulator, per component | `tests/test_sir3.py::test_zero_distortion_is_bit_identical_to_base_deterministic`, `::test_each_family_alone_is_identity_at_zero` |
| Each family actually moves the output (so the identity test is not vacuous) | `tests/test_sir3.py::test_each_family_actually_moves_the_output` |
| Smoothness through zero — one-sided derivatives agree; second difference bounded | `tests/test_sir3.py::test_family_is_smooth_through_zero`, `::test_family_second_difference_is_bounded` |
| Common random numbers cancel in the difference; independent seeds do not | `tests/test_sir3.py::test_common_random_numbers_cancel_in_the_difference` |
| A count-valued observation layer is not differentiable (the negative control) | `tests/test_sir3.py::test_poisson_noise_model_is_not_differentiable` |
| Peak statistics are differentiable — interpolation is exact on a parabola, continuous where the discrete argmax moves | `tests/test_summaries.py::test_peak_interpolation_recovers_a_known_parabola_vertex`, `::test_peak_interpolation_is_continuous_where_the_discrete_argmax_moves` |
| **The h-sweep plateau genuinely exists**, and is flat rather than slowly drifting | `tests/test_jacobian_rank.py::test_plateau_exists_and_is_not_a_fallback`, `::test_plateau_is_flat_not_merely_slowly_drifting` |
| Rank noise does **not** grow monotonically as h shrinks | `tests/test_jacobian_rank.py::test_rank_noise_does_not_increase_monotonically_with_decreasing_h` |
| The no-CRN control has no plateau and blows up as 1/h | `tests/test_jacobian_rank.py::test_no_crn_control_has_no_plateau_and_blows_up_as_one_over_h` |
| **`S_C`'s positive-control behaviour** — cannot be full rank, reports an *exact* null direction | `tests/test_jacobian_rank.py::test_s_c_cannot_have_full_column_rank`, `::test_s_c_reports_an_exact_null_direction` |
| A single-`h` call is not expressible | `tests/test_jacobian_rank.py::test_scalar_h_is_rejected` |
| Rank and condition number are invariant to the common `eta_scale`; column norms are not | `tests/test_jacobian_rank.py::test_rank_and_condition_number_are_invariant_to_the_common_eta_scale` |
| Pre-registered thresholds have not drifted from `docs/THRESHOLDS.md` | `tests/test_jacobian_rank.py::test_pre_registered_thresholds_have_not_drifted` |
| **The floor check lands near 1/3** | `tests/test_jacobian_rank.py::test_floor_check_lands_near_one_third` |

### Not yet satisfied

No **attribution accuracy** figure exists, so the additional requirement above — `K`, `floor`,
and the as-run uniform attributor in the same file — has not yet had to be met by an accuracy
results file. `results/floor_check.yaml` establishes the floor in advance of any accuracy being
computed, which is the order this contract intends.
