# Provenance

**Current state: this repository contains no numbers.** `results/` is empty, `src/` is
empty, and nothing has been computed. This document defines the contract that will
govern numbers when they start to exist, and it is written now, before any exist, so
that it cannot be shaped retroactively to fit whatever the first run happens to emit.

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
