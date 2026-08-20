# Sim-Attrib

**Which component of the simulator is wrong?**

Simulation-based inference can detect that a simulator is misspecified, and can
robustify inference against it. It does not say *which component* is at fault. This
project investigates whether it can — and the honest starting position is that in
general it cannot, because the data constrain only the *sum* of per-component
discrepancies.

The work therefore has two parts. The first is a limits result: per-component
discrepancy attribution is non-identifiable without further structure, and becomes
identifiable under a stated rank condition on the summary Jacobian. The second is a
method that operates inside the identifiable subspace, reports equivalence classes
where the condition fails, and controls error over the *selected* component rather than
testing components one at a time.

## Status

Pre-experimental. This repository contains a planning document, a governance layer
that turns that document's assertions into checkable claims, and the record of a
positioning review against the literature.

There is **no simulator, no diagnostic, no attribution code, no results, and no
manuscript**. No number has been computed. Where this repository refers to a method or
a finding, it refers to something intended, not something demonstrated.

> **Status, session G6 (2026-08-20). The paragraph above was true when it was written in G0
> and has been false since G3; it is left standing because the layout table below was written
> with it and the drift is worth seeing.** There is now a simulator
> (`src/simulators/sir3.py`), 14 diagnostic and reporting modules
> (`src/diagnostics/`, of which `jacobian_rank.py` is the rank condition itself), a
> selection rule (`src/attribution/selection.py`), and 26 files of
> recorded numbers and generated tables (`results/`). There is still **no manuscript**:
> `paper/` holds the venue template and nothing else.
>
> Two findings carry the state of the project. **The separability precondition holds**, for the
> summary set `S_B` under all eight component-wise distortion-family assignments the declared
> families permit — inside a scope restricted to one distortion parameter per component
> (`docs/DECISIONS.md` **D-14**), outside which the project's own measurement is a
> counterexample. **The cost gate on the composition that precondition was for has failed**, on
> non-termination rather than on cost (`results/cost_gate.yaml`, `docs/OPEN_QUESTIONS.md`
> **Q-16**). Start with `audit/S6_REPORT.md`.

## Layout

| Path | Contents |
|---|---|
| `audit/` | Plan of record, claim ledgers, verified bibliography, positioning verdict |
| `src/` | Simulators, perturbation bases, diagnostics, attribution — *empty* |
| `results/` | Every emitted number, one file per emitting script — *empty* |
| `paper/` | LaTeX source; venue templates fetched, never reconstructed — *empty* |
| `review/` | Frozen PDFs and adversarial review — *empty* |
| `docs/` | Operator notes and open questions |

Start with `audit/S0_REPORT.md`, which states what exists, what the literature review
found, and what it did not manage to check.

## Governing documents

- `GATES.md` — gate register. Gates are signed by the operator; nothing self-approves.
- `PROVENANCE.md` — how any number here traces to the code that produced it.
- `OUTSTANDING.md` — numbered open actions with owners.
- `DEVIATIONS.md` — where execution departed from instruction, and why.

## Venue

Not committed. A NeurIPS 2026 workshop is the intended target and the candidates are
evidenced in `audit/VENUE.md`, but the choice is conditional on which claims survive
review and is the operator's to make.

## Licence

MIT — see `LICENSE`.
