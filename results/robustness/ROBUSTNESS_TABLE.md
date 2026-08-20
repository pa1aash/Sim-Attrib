# Robustness tables — GENERATED, not typed

Produced by `src/diagnostics/report_robustness.py` from `results/robustness/*.yaml`.
Do not edit by hand. `audit/G3_ADVERSARIAL_REVIEW.md` quotes this file verbatim.

**Nothing here replaces `results/jacobian_rank.*.yaml`.** Those files record what
session G3 ran and are untouched.

---

## 1. The spectrum, and how far the tolerance can move before the verdict does

Re-analysis of the recorded singular values. No simulation. Pre-registered `tau = 0.01`, `kappa_max = 100`.

| Summary set | singular values | sigma_i/sigma_1 | adjacent ratios | spread (decades) | largest gap after |
|---|---|---|---|---|---|
| S_A | 4.156, 1.043, 0.7727 | 1, 0.251, 0.186 | 3.99, 1.35 | 0.731 | sigma_1 |
| S_B | 27.8, 5.208, 2.747 | 1, 0.187, 0.0988 | 5.34, 1.9 | 1.01 | sigma_1 |
| S_C | 4.155, 0.9557, 0 | 1, 0.23, 0 | 4.35, inf | — | sigma_1 |

**Spread** is `log10(sigma_1/sigma_K)`. Gutenkunst et al. report spectra spread over
*many decades without a gap*; the number above is the like-for-like quantity.

### 1.1 Flip points — the exact tolerance at which each verdict changes

| Summary set | recorded verdict | tau* | as a multiple of pre-registered tau | kappa* | as a fraction of kappa_max |
|---|---|---|---|---|---|
| S_A | separable | 0.1859 | 18.6x | 5.378 | 0.0538 |
| S_B | separable | 0.09881 | 9.88x | 10.12 | 0.101 |
| S_C | INSEPARABLE | 0 | 0x | inf | — |

`tau* = sigma_K/sigma_1 = 1/kappa` exactly, so the two pre-registered criteria are
one threshold under two names (`docs/THRESHOLDS.md` §1.3 says so).

### 1.2 The verdict at alternative tolerances

| tau | kappa_max | S_A rank | S_B rank | S_C rank | S_A verdict | S_B verdict | S_C verdict |
|---|---|---|---|---|---|---|---|
| 0.001 | 1000 | 3 | 3 | 2 | separable | separable | INSEPARABLE |
| 0.005 | 200 | 3 | 3 | 2 | separable | separable | INSEPARABLE |
| 0.01 | 100 | 3 | 3 | 2 | separable | separable | INSEPARABLE |
| 0.02 | 50 | 3 | 3 | 2 | separable | separable | INSEPARABLE |
| 0.1 | 10 | 3 | 2 | 2 | separable | INSEPARABLE | INSEPARABLE |

---

## 2. Re-runs: a different family set, and different seeds

Same diagnostic code, same pre-registered thresholds, same `h` sweep, same
normalisation rule, same replicate count. Only the family set and the seed differ.

| Run | Summary set | d | rank at tau | kappa | plateau found | verdict |
|---|---|---|---|---|---|---|
| **G3 as recorded** | S_A | 4 | 3 | 5.378 | yes | separable |
| **G3 as recorded** | S_B | 10 | 3 | 10.12 | yes | separable |
| **G3 as recorded** | S_C | 2 | 2 | inf | yes | INSEPARABLE |
| adversarial family set | S_A | 4 | 2 | 136.7 | yes | INSEPARABLE |
| adversarial family set | S_B | 10 | 3 | 64.62 | yes | separable |
| adversarial family set | S_C | 2 | 2 | inf | yes | INSEPARABLE |
| base families, seed 20260821 | S_A | 4 | 3 | 5.379 | yes | separable |
| base families, seed 20260821 | S_B | 10 | 3 | 10.12 | yes | separable |
| base families, seed 20260821 | S_C | 2 | 2 | inf | yes | INSEPARABLE |
| base families, seed 20260822 | S_A | 4 | 3 | 5.386 | yes | separable |
| base families, seed 20260822 | S_B | 10 | 3 | 10.11 | yes | separable |
| base families, seed 20260822 | S_C | 2 | 2 | inf | yes | INSEPARABLE |

### 2.1 Singular values and pairwise coherence, per run

| Run | Summary set | singular values | sigma_3/sigma_1 | mu(tra,pro) | mu(tra,obs) | mu(pro,obs) | flagged |
|---|---|---|---|---|---|---|---|
| **G3 as recorded** | S_A | 4.156, 1.043, 0.7727 | 0.186 | 0.338 | 0.777 | 0.196 | none |
| **G3 as recorded** | S_B | 27.8, 5.208, 2.747 | 0.0988 | 0.951 | 0.657 | 0.538 | none |
| **G3 as recorded** | S_C | 4.155, 0.9557, 0 | 0 | 0.992 | 0.778 | 0.694 | transmission–progression |
| adversarial family set | S_A | 6.689, 0.9094, 0.04894 | 0.00732 | 0.958 | 0.0728 | 0.353 | none |
| adversarial family set | S_B | 63.1, 3.639, 0.9765 | 0.0155 | 0.977 | 0.812 | 0.754 | none |
| adversarial family set | S_C | 3.049, 0.5323, 0 | 0 | 0.948 | 0.789 | 0.943 | none |
| base families, seed 20260821 | S_A | 4.154, 1.044, 0.7723 | 0.186 | 0.339 | 0.777 | 0.197 | none |
| base families, seed 20260821 | S_B | 27.79, 5.207, 2.747 | 0.0988 | 0.951 | 0.657 | 0.538 | none |
| base families, seed 20260821 | S_C | 4.154, 0.9565, 0 | 0 | 0.992 | 0.778 | 0.692 | transmission–progression |
| base families, seed 20260822 | S_A | 4.155, 1.045, 0.7715 | 0.186 | 0.34 | 0.776 | 0.197 | none |
| base families, seed 20260822 | S_B | 27.78, 5.209, 2.748 | 0.0989 | 0.951 | 0.657 | 0.538 | none |
| base families, seed 20260822 | S_C | 4.154, 0.9573, 0 | 0 | 0.991 | 0.777 | 0.688 | transmission–progression |

### 2.2 Column norms — is any component invisible?

| Run | Summary set | ‖J·transmission‖ | ‖J·progression‖ | ‖J·observation‖ | invisible (<0.1) |
|---|---|---|---|---|---|
| **G3 as recorded** | S_A | 1.575 | 0.9132 | 3.955 | none |
| **G3 as recorded** | S_B | 25.36 | 11.01 | 6.578 | none |
| **G3 as recorded** | S_C | 1.572 | 0.2584 | 3.955 | none |
| adversarial family set | S_A | 6.096 | 2.852 | 0.5291 | none |
| adversarial family set | S_B | 60.68 | 17.63 | 1.77 | none |
| adversarial family set | S_C | 2.498 | 1.755 | 0.5105 | none |
| base families, seed 20260821 | S_A | 1.574 | 0.9135 | 3.954 | none |
| base families, seed 20260821 | S_B | 25.35 | 11 | 6.576 | none |
| base families, seed 20260821 | S_C | 1.571 | 0.2595 | 3.954 | none |
| base families, seed 20260822 | S_A | 1.573 | 0.9136 | 3.955 | none |
| base families, seed 20260822 | S_B | 25.34 | 11 | 6.577 | none |
| base families, seed 20260822 | S_C | 1.57 | 0.2609 | 3.955 | none |

### 2.3 Where the adversarial run's near-null direction points

**S_A**, direction 2 — `sigma = 0.04894`, `sigma/sigma_1 = 0.007316`, **near** degeneracy

- right singular vector: (0.2312, -0.5272, -0.8177) over (transmission, progression, observation)
- equivalence-class members (|v_k| >= 0.3 across the plateau): progression, observation
- borderline: none

**S_C**, direction 2 — `sigma = 0`, `sigma/sigma_1 = 0`, **exact** degeneracy

- right singular vector: (-0.1839, 0.483, 0.8561) over (transmission, progression, observation)
- equivalence-class members (|v_k| >= 0.3 across the plateau): progression, observation
- borderline: none

---

## 3. Does the argmax inside S_A's peak statistics contaminate its Jacobian?

### 3.1 Fine eta sweep at one fixed seed — what happens at a real argmax switch

| Component | eta range | points | switches found | largest step in peak_time | largest step in peak_height | median step, peak_time | median step, peak_height |
|---|---|---|---|---|---|---|---|
| transmission | [-0.6, 0.6] | 99 | 1 | 0.2353 | 170.2 | 0.001296 | 19.26 |
| progression | [-0.6, 0.6] | 121 | 2 | 3.169 | 24.68 | 0.005059 | 4.342 |
| observation | [-0.6, 0.6] | 121 | 0 | 0 | 36.88 | 0 | 20.34 |

Steps are between adjacent eta grid points, in native summary units. A step much
larger than the median is the signature of a discontinuity being crossed.

### 3.2 Census at the estimator's own settings — how often is a switch actually straddled?

| h | component | replicates | straddling an argmax switch | boundary fallbacks | peak_height difference quotient: mean | sd | max abs |
|---|---|---|---|---|---|---|---|
| 0.1 | transmission | 128 | 1 | 0 | -233.1 | 33.95 | 304.7 |
| 0.1 | progression | 128 | 5 | 0 | 41.85 | 58.41 | 185.3 |
| 0.1 | observation | 128 | 0 | 0 | 190.1 | 16.82 | 237.5 |
| 0.0001 | transmission | 128 | 0 | 0 | -232.7 | 33.93 | 304.7 |
| 0.0001 | progression | 128 | 0 | 0 | 41.42 | 58.4 | 185.3 |
| 0.0001 | observation | 128 | 0 | 0 | 190.1 | 16.82 | 237.5 |

### 3.3 Leave-one-coordinate-out — does S_A's verdict rest on the peak statistics?

| S_A computed with | singular values | rank at tau | kappa | verdict |
|---|---|---|---|---|
| all four coordinates | 4.156, 1.043, 0.7727 | 3 | 5.378 | separable |
| dropping peak height | 3.928, 0.8794, 0.00337 | 2 | 1165 | INSEPARABLE |
| dropping peak time | 4.156, 1.043, 0.7727 | 3 | 5.379 | separable |
| dropping final size | 1.675, 0.8521, 0.002224 | 2 | 753.4 | INSEPARABLE |
| dropping growth rate | 4.155, 0.9558, 0.01566 | 2 | 265.3 | INSEPARABLE |
| dropping both peak statistics | 3.928, 0.8793, 0 | 2 | inf | INSEPARABLE |

---

## 4. Count observations under common random numbers — degeneracy or artefact?

Test statistic `final_size`, which is linear, so the target derivative is available
in closed form from the deterministic mean with no Monte Carlo error.

### 4.1 The pathwise map, walked finely at one fixed seed

`eta` walked over [-0.01, 0.01] in 801 steps.

| Coupling | distinct values | jumps | adjacent pairs exactly equal | largest jump | total variation | net change across the range |
|---|---|---|---|---|---|---|
| lognormal | 801 / 801 | 800 | 0 | 0.2432 | 191.8 | -191.8 |
| poisson_numpy | 168 / 801 | 486 | 0.3925 | 40 | 2885 | -129 |
| poisson_inversion | 168 / 801 | 412 | 0.485 | 4 | 519 | -167 |

### 4.2 The difference quotient across the pre-registered h sweep

`R_small` is the replicate count the reported diagnostic used; `R_large` is large
enough to separate bias from variance.

**lognormal**

| h | exact derivative of the mean | estimate at R_small | relative error at R_small | mean at R_large | relative bias at R_large | sd of one replicate | fraction of replicates exactly zero | sample sd at R_small exactly zero |
|---|---|---|---|---|---|---|---|---|
| 0.1 | -866.583 | -859.443 | -0.00824 | -866.725 | 0.000165 | 101.2 | 0 | no |
| 0.01 | -866.539 | -859.399 | -0.00824 | -866.682 | 0.000165 | 101.2 | 0 | no |
| 0.001 | -866.539 | -859.399 | -0.00824 | -866.682 | 0.000165 | 101.2 | 0 | no |
| 0.0001 | -866.539 | -859.399 | -0.00824 | -866.682 | 0.000165 | 101.2 | 0 | no |
| 1e-05 | -866.539 | -859.399 | -0.00824 | -866.682 | 0.000165 | 101.2 | 0 | no |
| 1e-06 | -866.539 | -859.399 | -0.00824 | -866.682 | 0.000165 | 101.2 | 0 | no |

**poisson_numpy**

| h | exact derivative of the mean | estimate at R_small | relative error at R_small | mean at R_large | relative bias at R_large | sd of one replicate | fraction of replicates exactly zero | sample sd at R_small exactly zero |
|---|---|---|---|---|---|---|---|---|
| 0.1 | -866.583 | -844.766 | -0.0252 | -865.694 | -0.00103 | 149.9 | 0 | no |
| 0.01 | -866.539 | -1018.36 | 0.175 | -854.038 | -0.0144 | 1362 | 0.00875 | no |
| 0.001 | -866.539 | -359.375 | -0.585 | -765.4 | -0.117 | 1.198e+04 | 0.07915 | no |
| 0.0001 | -866.539 | 3125 | -4.61 | -1047.5 | 0.209 | 4.632e+04 | 0.5007 | no |
| 1e-05 | -866.539 | 0 | -1 | -2630 | 2.04 | 1.461e+05 | 0.9264 | no |
| 1e-06 | -866.539 | -3906.25 | 3.51 | -4325 | 3.99 | 3.464e+05 | 0.9934 | no |

**poisson_inversion**

| h | exact derivative of the mean | estimate at R_small | relative error at R_small | mean at R_large | relative bias at R_large | sd of one replicate | fraction of replicates exactly zero | sample sd at R_small exactly zero |
|---|---|---|---|---|---|---|---|---|
| 0.1 | -866.583 | -867.305 | 0.000833 | -866.466 | -0.000135 | 24.25 | 0 | no |
| 0.01 | -866.539 | -868.75 | 0.00255 | -867.39 | 0.000982 | 177.3 | 0 | no |
| 0.001 | -866.539 | -765.625 | -0.116 | -854 | -0.0145 | 1244 | 0.128 | no |
| 0.0001 | -866.539 | -507.812 | -0.414 | -857.75 | -0.0101 | 4381 | 0.5208 | no |
| 1e-05 | -866.539 | 390.625 | -1.45 | -770 | -0.111 | 1.425e+04 | 0.925 | no |
| 1e-06 | -866.539 | -3906.25 | 3.51 | -600 | -0.308 | 4.5e+04 | 0.9925 | no |

`R_small = 128`, `R_large = 20000`, component perturbed: `transmission`, `obs_sigma = 0.15`.

---

## Provenance of every run quoted above

| File | script | commit | dirty | seed |
|---|---|---|---|---|
| `results/robustness/crn_count_check.yaml` | `src/diagnostics/crn_count_check.py` | `26cfbaf23bee` | False | 20260820 |
| `results/robustness/jacobian_rank.adversarial.S_A.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260820 |
| `results/robustness/jacobian_rank.adversarial.S_B.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260820 |
| `results/robustness/jacobian_rank.adversarial.S_C.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260820 |
| `results/robustness/jacobian_rank.seed_20260821.S_A.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260821 |
| `results/robustness/jacobian_rank.seed_20260821.S_B.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260821 |
| `results/robustness/jacobian_rank.seed_20260821.S_C.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260821 |
| `results/robustness/jacobian_rank.seed_20260822.S_A.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260822 |
| `results/robustness/jacobian_rank.seed_20260822.S_B.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260822 |
| `results/robustness/jacobian_rank.seed_20260822.S_C.yaml` | `src/diagnostics/run_family_check.py` | `26cfbaf23bee` | False | 20260822 |
| `results/robustness/summary_smoothness_check.yaml` | `src/diagnostics/summary_smoothness_check.py` | `26cfbaf23bee` | False | 20260820 |
| `results/robustness/threshold_sensitivity.yaml` | `src/diagnostics/threshold_sensitivity.py` | `06be55c01b1b` | False | 0 |
| `results/robustness/wide_spectrum_check.yaml` | `src/diagnostics/wide_spectrum_check.py` | `26cfbaf23bee` | False | 20260820 |

