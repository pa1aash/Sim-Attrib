# Results tables — GENERATED, not typed

Produced by `src/diagnostics/report_tables.py` from `results/*.yaml`. Do not edit by
hand: this file exists so that the reports in `audit/` can quote numbers without any
number being hand-typed into a markdown file (S11, `PROVENANCE.md`).

- commit: `570692c2f16b04c1948b47665c162c9478fe1de8`
- dirty: `False`
- command: `python -m src.diagnostics.run_diagnostic --seed 20260820 --replicates 128 --norm-replicates 2000 --floor-draws 10000`
- seed: `20260820`
- python `3.13.12`, deps `numpy==2.4.4, scipy==1.17.1, pyyaml==6.0.3`

## 1. Verdict per summary set

| Summary set | d | rank at tau=1e-2 | full column rank | condition number | verdict |
|---|---|---|---|---|---|
| S_A | 4 | 3 | yes | 5.378 | separable |
| S_B | 10 | 3 | yes | 10.12 | separable |
| S_C | 2 | 2 | NO | inf | INSEPARABLE |

- **S_A** — separable: full column rank at tau and condition number within ceiling
- **S_B** — separable: full column rank at tau and condition number within ceiling
- **S_C** — rank deficient at tau

## 2. Singular values, plateau, and resolution

| Summary set | singular values at representative h | plateau (h range) | n h in plateau | censored small / large h | all resolved |
|---|---|---|---|---|---|
| S_A | 4.156, 1.043, 0.7727 | 0.01 → 1e-06 | 5 | True / False | True |
| S_B | 27.8, 5.208, 2.747 | 0.1 → 1e-06 | 6 | True / True | True |
| S_C | 4.155, 0.9557, 0 | 0.1 → 1e-06 | 6 | True / True | True |

A plateau reaching the edge of the pre-registered sweep is reported as **censored**
there: the sweep stopped, not the plateau.

### 2.1 Full h-sweep, leading singular value

| h | S_A | S_B | S_C | S_A no-CRN control |
|---|---|---|---|---|
| 0.1 | 4.157 | 27.8 | 4.156 | 4.263 |
| 0.01 | 4.156 | 27.8 | 4.155 | 6.658 |
| 0.001 | 4.156 | 27.8 | 4.155 | 48.63 |
| 0.0001 | 4.156 | 27.8 | 4.155 | 474.9 |
| 1e-05 | 4.156 | 27.8 | 4.155 | 4738 |
| 1e-06 | 4.156 | 27.8 | 4.155 | 4.737e+04 |

## 3. Column norms and pairwise coherence

A near-zero **column norm** means a component is invisible to these summaries — a
different failure from collinearity, with different consequences. Rank alone conflates
them, so they are reported separately.

| Summary set | ‖J·transmission‖ | ‖J·progression‖ | ‖J·observation‖ | invisible (<0.1) |
|---|---|---|---|---|
| S_A | 1.575 | 0.9132 | 3.955 | none |
| S_B | 25.36 | 11.01 | 6.578 | none |
| S_C | 1.572 | 0.2584 | 3.955 | none |

| Summary set | mu(transmission,progression) | mu(transmission,observation) | mu(progression,observation) | flagged (>=0.98) |
|---|---|---|---|---|
| S_A | 0.3376 | 0.7771 | 0.1963 | none |
| S_B | 0.9508 | 0.6575 | 0.5381 | none |
| S_C | 0.9921 | 0.7785 | 0.6936 | transmission–progression |

Coherence is reported for interpretation and is **not** the decision rule; the decision
rule is on the singular values (`docs/THRESHOLDS.md` §2.2).

## 4. Near-null directions and equivalence classes

**S_C**, direction 2 — `sigma = 0`, `sigma/sigma_1 = 0`, **exact** degeneracy

- right singular vector: (0.1854, 0.9826, 0.01282) over (transmission, progression, observation)
- equivalence-class members (|v_k| >= 0.3 across the whole plateau): progression
- borderline (|v_k| crosses 0.3 within the plateau): none
- |v_k| ranges across plateau: transmission [0.1854, 0.1872]; progression [0.9822, 0.9826]; observation [0.01282, 0.01327]

`docs/THRESHOLDS.md` §3.4: an **exact** degeneracy is a statement about
identifiability, matching Kahl et al. (2019). A **near** degeneracy at condition number
kappa is a statement about **affordability** — separation costs about kappa^2 replicates
— and must never be written as an identifiability claim.

## 5. Random-attributor floor check

| K | analytic floor 1/K | simulated accuracy | deviation | tolerance (4 s.e.) | passes |
|---|---|---|---|---|---|
| 3 | 0.333333 | 0.3299 | -0.00343 | 0.0189 | True |

Run as 10000 draws at seed 20260820. Every attribution accuracy this
project reports is reported against this floor.

## 6. Negative control — the same sweep without common random numbers

- plateau found: **False**
- leading singular value across the sweep: 4.263, 6.658, 48.63, 474.9, 4738, 4.737e+04
- ratio between successive (ten-fold smaller) h: 1.56, 7.3, 9.77, 9.98, 10

Without common random numbers the difference quotient carries noise of order
`obs_sigma / h`, so the leading singular value grows as `1/h` and no plateau exists.
This is the control that makes the main sweep's plateau meaningful rather than
assumed.

## 7. D4 STOP condition

**Did not fire.** Separable summary set(s): **S_A, S_B**.

`docs/THRESHOLDS.md` §1.6 notes that because `S_C` is expected to fail by
construction, the STOP condition is decided by `S_A` and `S_B`, and `S_C`'s designed
failure must not later be read as one third of the evidence for stopping.

