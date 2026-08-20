# The K = 6 spectrum, and the eight family assignments

Produced by `src/diagnostics/report_k6.py` from `results/robustness/k6_spectrum.yaml`.
Do not edit by hand. `audit/K6_SPECTRUM_CHECK.md` quotes this file verbatim.

**Nothing here replaces `results/jacobian_rank.*.yaml` or the G4 files in
`results/robustness/`.** Those record what sessions G3 and G4 ran and are untouched.

Run: script `src/diagnostics/k6_spectrum.py`, commit `2efb4ae9232c`, dirty `False`, seed `20260820`, 9216 simulator runs.

---

## 1. The three spectra, in full

`base` and `adversarial` are the two declared family sets, three columns each.
`union` is the six-column Jacobian their columns define — **the only six-column object
the two declared sets supply**, since a family set assigns one family per component
(`DEVIATIONS.md` D-12).

| Summary set | columns | singular values | sigma_i/sigma_1 | spread (decades) | rank at tau | kappa | verdict |
|---|---|---|---|---|---|---|---|
| S_A | base | 4.156, 1.043, 0.7727 | 1, 0.251, 0.186 | 0.731 | 3/3 | 5.378 | separable |
| S_A | adversarial | 6.689, 0.9094, 0.04894 | 1, 0.136, 0.00732 | 2.14 | 2/3 | 136.7 | INSEPARABLE |
| S_A | **union (K=6)** | 7.02, 3.803, 0.8901, 0.007222, 0, 0 | 1, 0.542, 0.127, 0.00103, 0, 0 | 2.99 | 3/6 | inf | INSEPARABLE |
| S_B | base | 27.8, 5.208, 2.747 | 1, 0.187, 0.0988 | 1.01 | 3/3 | 10.12 | separable |
| S_B | adversarial | 63.1, 3.639, 0.9765 | 1, 0.0577, 0.0155 | 1.81 | 3/3 | 64.62 | separable |
| S_B | **union (K=6)** | 68.13, 11.5, 4.679, 2.642, 0.625, 0.1083 | 1, 0.169, 0.0687, 0.0388, 0.00917, 0.00159 | 2.8 | 4/6 | 628.9 | INSEPARABLE |
| S_C | base | 4.155, 0.9557, 0 | 1, 0.23, 0 | 0.638 | 2/3 | inf | INSEPARABLE |
| S_C | adversarial | 3.049, 0.5323, 0 | 1, 0.175, 0 | 0.758 | 2/3 | inf | INSEPARABLE |
| S_C | **union (K=6)** | 5.013, 1.62, 0, 0, 0, 0 | 1, 0.323, 0, 0, 0, 0 | 0.491 | 2/6 | inf | INSEPARABLE |

### 1.1 Is there a gap anywhere, or a smooth decay throughout?

`gap prominence` is the largest adjacent ratio divided by the median adjacent ratio.
**It is descriptive and no verdict depends on it**: 1.0 means a perfectly geometric
decay with no break anywhere, larger means one ratio dominates. No threshold is applied
to it, because inventing a gap criterion now — with the singular values visible — is the
leakage failure `LEDGER_DESIGN.md` D3 exists to prevent.

`where tau*sigma_1 sits` needs no threshold at all, and is the operational form of the
Gutenkunst objection: a tolerance cutting through a dense spectrum reports where the
analyst put it; a tolerance an order of magnitude below every singular value does not.

| Summary set | columns | adjacent ratios | largest | median | gap prominence | where tau*sigma_1 sits |
|---|---|---|---|---|---|---|
| S_A | base | 3.986, 1.349 | 3.986 | 2.668 | 1.49 | below the whole spectrum |
| S_A | adversarial | 7.356, 18.58 | 18.58 | 12.97 | 1.43 | inside the spectrum, between sigma_2 and sigma_3 |
| S_A | **union (K=6)** | 1.846, 4.273, 123.2, inf, inf | 123.2 | 4.273 | 28.8 | inside the spectrum, between sigma_3 and sigma_4 |
| S_B | base | 5.338, 1.896 | 5.338 | 3.617 | 1.48 | below the whole spectrum |
| S_B | adversarial | 17.34, 3.726 | 17.34 | 10.53 | 1.65 | below the whole spectrum |
| S_B | **union (K=6)** | 5.927, 2.457, 1.771, 4.228, 5.769 | 5.927 | 4.228 | 1.4 | inside the spectrum, between sigma_4 and sigma_5 |
| S_C | base | 4.348, inf | 4.348 | 4.348 | 1 | inside the spectrum, between sigma_2 and sigma_3 |
| S_C | adversarial | 5.728, inf | 5.728 | 5.728 | 1 | inside the spectrum, between sigma_2 and sigma_3 |
| S_C | **union (K=6)** | 3.094, inf, inf, inf, inf | 3.094 | 3.094 | 1 | inside the spectrum, between sigma_2 and sigma_3 |

### 1.2 Is the six-column rank deficiency real, or is the estimator not resolving it?

`docs/THRESHOLDS.md` §1.4: a singular value is **resolved** if it varies by less than a
factor of 2 across the h-plateau, and an unresolved one is counted toward the rank in
neither direction. `results/robustness/wide_spectrum_check.yaml` measured the six-column
spectrum at a single h and therefore could not answer this.

| Summary set | columns | plateau found | h range | variation factor per sigma | all resolved | rank determined |
|---|---|---|---|---|---|---|
| S_A | base | yes | 0.01, 1e-06 | 1, 1, 1 | yes | yes |
| S_A | adversarial | yes | 0.001, 1e-06 | 1, 1, 1 | yes | yes |
| S_A | **union (K=6)** | yes | 0.001, 1e-06 | 1, 1, 1, 1, 1, 1 | yes | yes |
| S_B | base | yes | 0.1, 1e-06 | 1, 1, 1 | yes | yes |
| S_B | adversarial | yes | 0.1, 1e-06 | 1.002, 1.004, 1 | yes | yes |
| S_B | **union (K=6)** | yes | 0.1, 1e-06 | 1.001, 1.001, 1, 1.001, 1.003, 1.023 | yes | yes |
| S_C | base | yes | 0.1, 1e-06 | 1, 1.002, 1 | yes | yes |
| S_C | adversarial | yes | 0.1, 1e-06 | 1.016, 1.06, 1 | yes | yes |
| S_C | **union (K=6)** | yes | 0.1, 1e-06 | 1.003, 1.029, 1, 1, 1, 1 | yes | yes |

## 2. What the six-column near-null directions actually confound

The six columns are two distortions of each of the same three mechanisms, so a rank
deficiency can mean two opposite things. **Within-mechanism**: two deformations of the
SAME component are hard to tell apart — which component attribution never claimed to do.
**Cross-mechanism**: two different components are confounded — which is the failure the
K = 3 verdict rules out. The distinction was written into
`src/diagnostics/k6_spectrum.py` before this run produced a number.

Membership uses the pre-registered rule of `docs/THRESHOLDS.md` §2.1 (`|v_k| >= 0.3`
throughout the plateau). `mechanism energy` is threshold-free: the squared weight the
direction places on each mechanism's two columns, summing to one.

Columns, in order: `base:transmission`, `base:progression`, `base:observation`, `adversarial:transmission`, `adversarial:progression`, `adversarial:observation`

### 2.1 S_A

| sigma | sigma/sigma_1 | kind | class members | mechanisms | energy: transmission / progression / observation |
|---|---|---|---|---|---|
| 0.007222 | 0.00103 | **cross-mechanism** | `base:progression`, `adversarial:transmission`, `adversarial:progression`, `adversarial:observation` | observation, progression, transmission | 0.121 / 0.576 / 0.302 |
| 0 | 0 | **within-mechanism** | `base:progression`, `adversarial:progression` | progression | 0.00851 / 0.926 / 0.065 |
| 0 | 0 | **cross-mechanism** | `base:progression`, `adversarial:progression`, `adversarial:observation` | observation, progression | 0.0325 / 0.299 / 0.668 |

Right singular vectors at the representative `h`, with `|v_k|` ranges across the plateau:

| sigma | `base:transmission` | `base:progression` | `base:observation` | `adversarial:transmission` | `adversarial:progression` | `adversarial:observation` |
|---|---|---|---|---|---|---|
| 0.007222 | -0.0588<br>[0.0588, 0.0588] | +0.3129<br>[0.3129, 0.3129] | -0.0817<br>[0.0817, 0.0817] | -0.3435<br>[0.3435, 0.3435] | +0.6918<br>[0.6918, 0.6918] | +0.5436<br>[0.5436, 0.5436] |
| 0 | +0.0663<br>[0.0663, 0.0663] | -0.8250<br>[0.8250, 0.8250] | -0.1431<br>[0.1431, 0.1431] | -0.0641<br>[0.0641, 0.0641] | +0.4959<br>[0.4959, 0.4959] | -0.2110<br>[0.2110, 0.2110] |
| 0 | -0.0154<br>[0.0154, 0.0154] | -0.4421<br>[0.4421, 0.4421] | +0.1646<br>[0.1646, 0.1646] | +0.1796<br>[0.1796, 0.1796] | -0.3220<br>[0.3220, 0.3220] | +0.8008<br>[0.8008, 0.8008] |

### 2.2 S_B

| sigma | sigma/sigma_1 | kind | class members | mechanisms | energy: transmission / progression / observation |
|---|---|---|---|---|---|
| 0.625 | 0.00917 | **cross-mechanism** | `base:progression`, `adversarial:progression`, `adversarial:observation` | observation, progression | 0.043 / 0.595 / 0.362 |
| 0.1083 | 0.00159 | **cross-mechanism** | `base:progression`, `adversarial:progression`, `adversarial:observation` | observation, progression | 0.0446 / 0.333 / 0.622 |

Right singular vectors at the representative `h`, with `|v_k|` ranges across the plateau:

| sigma | `base:transmission` | `base:progression` | `base:observation` | `adversarial:transmission` | `adversarial:progression` | `adversarial:observation` |
|---|---|---|---|---|---|---|
| 0.625 | -0.0006<br>[0.0000, 0.0006] | -0.6783<br>[0.6783, 0.6799] | -0.0418<br>[0.0418, 0.0418] | +0.2073<br>[0.2073, 0.2074] | -0.3673<br>[0.3669, 0.3673] | -0.6003<br>[0.5986, 0.6003] |
| 0.1083 | -0.0158<br>[0.0151, 0.0158] | -0.4015<br>[0.4011, 0.4015] | +0.1834<br>[0.1830, 0.1834] | +0.2107<br>[0.2101, 0.2107] | -0.4146<br>[0.4129, 0.4146] | +0.7673<br>[0.7673, 0.7686] |

### 2.3 S_C

| sigma | sigma/sigma_1 | kind | class members | mechanisms | energy: transmission / progression / observation |
|---|---|---|---|---|---|
| 0 | 0 | **cross-mechanism** | `base:transmission`, `base:progression` | progression, transmission | 0.398 / 0.586 / 0.0155 |
| 0 | 0 | **cross-mechanism** | `base:transmission`, `base:progression`, `adversarial:transmission` | progression, transmission | 0.563 / 0.435 / 0.00173 |
| 0 | 0 | **cross-mechanism** | `base:transmission`, `adversarial:progression` | progression, transmission | 0.14 / 0.823 / 0.0375 |
| 0 | 0 | **within-mechanism** | `adversarial:observation` | observation | 0.00662 / 0.00776 / 0.986 |

Right singular vectors at the representative `h`, with `|v_k|` ranges across the plateau:

| sigma | `base:transmission` | `base:progression` | `base:observation` | `adversarial:transmission` | `adversarial:progression` | `adversarial:observation` |
|---|---|---|---|---|---|---|
| 0 | +0.5588<br>[0.5471, 0.5655] | +0.7602<br>[0.7542, 0.7705] | +0.0487<br>[0.0441, 0.0516] | +0.2935<br>[0.2910, 0.2943] | -0.0911<br>[0.0845, 0.0950] | +0.1144<br>[0.1142, 0.1148] |
| 0 | +0.5625<br>[0.5619, 0.5631] | -0.6310<br>[0.6171, 0.6387] | +0.0416<br>[0.0356, 0.0447] | +0.4967<br>[0.4875, 0.5132] | -0.1923<br>[0.1914, 0.1937] | +0.0004<br>[0.0000, 0.0011] |
| 0 | +0.3477<br>[0.3463, 0.3501] | -0.0859<br>[0.0834, 0.0901] | -0.1919<br>[0.1901, 0.1930] | -0.1371<br>[0.1360, 0.1390] | +0.9030<br>[0.9018, 0.9037] | +0.0252<br>[0.0251, 0.0254] |
| 0 | -0.0753<br>[0.0740, 0.0761] | -0.0871<br>[0.0864, 0.0882] | +0.1172<br>[0.1169, 0.1177] | -0.0308<br>[0.0304, 0.0309] | +0.0134<br>[0.0126, 0.0138] | +0.9858<br>[0.9858, 0.9859] |

## 3. The eight component-wise family assignments

`B` is the base family for that component, `A` the adversarial one, in the order
`(transmission, progression, observation)`. **`BBB` and `AAA` are the two declared sets**;
the other six are three-column distortion models built from the same columns, which an
analyst could equally have declared. No new family is invented and no additional
simulation was run.

### 3.1 S_A

| code | families | declared? | singular values | rank at tau | kappa | tau* / registered tau | verdict | equivalence class |
|---|---|---|---|---|---|---|---|---|
| `BBB` | base:transmission + base:progression + base:observation | **yes** | 4.156, 1.043, 0.7727 | 3/3 | 5.378 | 18.6x | separable | — |
| `BBA` | base:transmission + base:progression + adv:observation | no | 1.661, 0.8695, 0.2814 | 3/3 | 5.902 | 16.9x | separable | — |
| `BAB` | base:transmission + adv:progression + base:observation | no | 4.589, 2.101, 0.8849 | 3/3 | 5.186 | 19.3x | separable | — |
| `BAA` | base:transmission + adv:progression + adv:observation | no | 3.062, 1.189, 0.3213 | 3/3 | 9.531 | 10.5x | separable | — |
| `ABB` | adv:transmission + base:progression + base:observation | no | 6.35, 3.649, 0.06294 | 2/3 | 100.9 | 0.991x | **INSEPARABLE** | {progression} |
| `ABA` | adv:transmission + base:progression + adv:observation | no | 6.163, 0.5403, 0.04998 | 2/3 | 123.3 | 0.811x | **INSEPARABLE** | {progression} |
| `AAB` | adv:transmission + adv:progression + base:observation | no | 6.901, 3.649, 0.007885 | 2/3 | 875.2 | 0.114x | **INSEPARABLE** | {transmission, progression} |
| `AAA` | adv:transmission + adv:progression + adv:observation | **yes** | 6.689, 0.9094, 0.04894 | 2/3 | 136.7 | 0.732x | **INSEPARABLE** | {progression, observation} |

### 3.2 S_B

| code | families | declared? | singular values | rank at tau | kappa | tau* / registered tau | verdict | equivalence class |
|---|---|---|---|---|---|---|---|---|
| `BBB` | base:transmission + base:progression + base:observation | **yes** | 27.8, 5.208, 2.747 | 3/3 | 10.12 | 9.88x | separable | — |
| `BBA` | base:transmission + base:progression + adv:observation | no | 27.5, 3.225, 0.8877 | 3/3 | 30.98 | 3.23x | separable | — |
| `BAB` | base:transmission + adv:progression + base:observation | no | 29.87, 9.218, 4.506 | 3/3 | 6.628 | 15.1x | separable | — |
| `BAA` | base:transmission + adv:progression + adv:observation | no | 29.63, 8.851, 1.081 | 3/3 | 27.4 | 3.65x | separable | — |
| `ABB` | adv:transmission + base:progression + base:observation | no | 61.7, 5.735, 2.407 | 3/3 | 25.64 | 3.9x | separable | — |
| `ABA` | adv:transmission + base:progression + adv:observation | no | 61.63, 2.549, 0.9389 | 3/3 | 65.64 | 1.52x | separable | — |
| `AAB` | adv:transmission + adv:progression + base:observation | no | 63.17, 6.047, 3.043 | 3/3 | 20.76 | 4.82x | separable | — |
| `AAA` | adv:transmission + adv:progression + adv:observation | **yes** | 63.1, 3.639, 0.9765 | 3/3 | 64.62 | 1.55x | separable | — |

### 3.3 S_C

| code | families | declared? | singular values | rank at tau | kappa | tau* / registered tau | verdict | equivalence class |
|---|---|---|---|---|---|---|---|---|
| `BBB` | base:transmission + base:progression + base:observation | **yes** | 4.155, 0.9557, 0 | 2/3 | inf | 0x | **INSEPARABLE** | {progression} |
| `BBA` | base:transmission + base:progression + adv:observation | no | 1.646, 0.2997, 0 | 2/3 | inf | 0x | **INSEPARABLE** | {progression} |
| `BAB` | base:transmission + adv:progression + base:observation | no | 4.481, 1.055, 0 | 2/3 | inf | 0x | **INSEPARABLE** | {transmission, progression} |
| `BAA` | base:transmission + adv:progression + adv:observation | no | 2.373, 0.4225, 0 | 2/3 | inf | 0x | **INSEPARABLE** | {progression, observation} |
| `ABB` | adv:transmission + base:progression + base:observation | no | 4.461, 1.43, 0 | 2/3 | inf | 0x | **INSEPARABLE** | {progression} |
| `ABA` | adv:transmission + base:progression + adv:observation | no | 2.543, 0.3115, 0 | 2/3 | inf | 0x | **INSEPARABLE** | {progression} |
| `AAB` | adv:transmission + adv:progression + base:observation | no | 4.779, 1.458, 0 | 2/3 | inf | 0x | **INSEPARABLE** | {transmission, progression} |
| `AAA` | adv:transmission + adv:progression + adv:observation | **yes** | 3.049, 0.5323, 0 | 2/3 | inf | 0x | **INSEPARABLE** | {progression, observation} |

## 4. Threshold sensitivity

Every row is produced by calling the production `analyse()` with the thresholds passed
as the parameters they already are — nothing is transcribed, so nothing can drift from
the rule the reported numbers were produced by.

`docs/THRESHOLDS.md` §1.2 derives `kappa_max = 1/tau`, so the **coupled** rows move both
together, which is the pair the project registered. The **tau alone** rows hold
`kappa_max` at 100 and are how the `kappa` branch becomes reachable at all.

### S_A — base

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0.185934** = **18.59x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 3/3 | separable | 3/3 | separable | no |
| 0.001 | 0.1x | 3/3 | separable | 3/3 | separable | no |
| 0.005 | 0.5x | 3/3 | separable | 3/3 | separable | no |
| 0.01 | 1x | 3/3 | separable | 3/3 | separable | no |
| 0.02 | 2x | 3/3 | separable | 3/3 | separable | no |
| 0.05 | 5x | 3/3 | separable | 3/3 | separable | no |
| 0.1 | 10x | 3/3 | separable | 3/3 | separable | no |
| 0.5 | 50x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |
| 1 | 100x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |

Verdict at the registered `tau` is **separable**, stable over `tau` in [0.0001, 0.1] = x0.01 to x10; flips at the next grid point below: —, above: 0.5. Grid-censored below: yes, above: no.

### S_A — adversarial

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0.00731577** = **0.7316x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 3/3 | separable | 3/3 | INSEPARABLE | yes |
| 0.001 | 0.1x | 3/3 | separable | 3/3 | INSEPARABLE | yes |
| 0.005 | 0.5x | 3/3 | separable | 3/3 | INSEPARABLE | yes |
| 0.01 | 1x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.02 | 2x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.05 | 5x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.1 | 10x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.5 | 50x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |
| 1 | 100x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |

Verdict at the registered `tau` is **INSEPARABLE**, stable over `tau` in [0.01, 1] = x1 to x100; flips at the next grid point below: 0.005, above: —. Grid-censored below: no, above: yes.

### S_A — union (K=6)

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0** = **0x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 4/6 | INSEPARABLE | 4/6 | INSEPARABLE | no |
| 0.001 | 0.1x | 4/6 | INSEPARABLE | 4/6 | INSEPARABLE | no |
| 0.005 | 0.5x | 3/6 | INSEPARABLE | 3/6 | INSEPARABLE | no |
| 0.01 | 1x | 3/6 | INSEPARABLE | 3/6 | INSEPARABLE | no |
| 0.02 | 2x | 3/6 | INSEPARABLE | 3/6 | INSEPARABLE | no |
| 0.05 | 5x | 3/6 | INSEPARABLE | 3/6 | INSEPARABLE | no |
| 0.1 | 10x | 3/6 | INSEPARABLE | 3/6 | INSEPARABLE | no |
| 0.5 | 50x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 1 | 100x | 1/6 | INSEPARABLE | 1/6 | INSEPARABLE | no |

Verdict at the registered `tau` is **INSEPARABLE**, stable over `tau` in [0.0001, 1] = x0.01 to x100; flips at the next grid point below: —, above: —. Grid-censored below: yes, above: yes.

### S_B — base

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0.0988114** = **9.881x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 3/3 | separable | 3/3 | separable | no |
| 0.001 | 0.1x | 3/3 | separable | 3/3 | separable | no |
| 0.005 | 0.5x | 3/3 | separable | 3/3 | separable | no |
| 0.01 | 1x | 3/3 | separable | 3/3 | separable | no |
| 0.02 | 2x | 3/3 | separable | 3/3 | separable | no |
| 0.05 | 5x | 3/3 | separable | 3/3 | separable | no |
| 0.1 | 10x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.5 | 50x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |
| 1 | 100x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |

Verdict at the registered `tau` is **separable**, stable over `tau` in [0.0001, 0.05] = x0.01 to x5; flips at the next grid point below: —, above: 0.1. Grid-censored below: yes, above: no.

### S_B — adversarial

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0.0154747** = **1.547x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 3/3 | separable | 3/3 | separable | no |
| 0.001 | 0.1x | 3/3 | separable | 3/3 | separable | no |
| 0.005 | 0.5x | 3/3 | separable | 3/3 | separable | no |
| 0.01 | 1x | 3/3 | separable | 3/3 | separable | no |
| 0.02 | 2x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.05 | 5x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.1 | 10x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |
| 0.5 | 50x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |
| 1 | 100x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |

Verdict at the registered `tau` is **separable**, stable over `tau` in [0.0001, 0.01] = x0.01 to x1; flips at the next grid point below: —, above: 0.02. Grid-censored below: yes, above: no.

### S_B — union (K=6)

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0.00159019** = **0.159x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 6/6 | separable | 6/6 | INSEPARABLE | yes |
| 0.001 | 0.1x | 6/6 | separable | 6/6 | INSEPARABLE | yes |
| 0.005 | 0.5x | 5/6 | INSEPARABLE | 5/6 | INSEPARABLE | no |
| 0.01 | 1x | 4/6 | INSEPARABLE | 4/6 | INSEPARABLE | no |
| 0.02 | 2x | 4/6 | INSEPARABLE | 4/6 | INSEPARABLE | no |
| 0.05 | 5x | 3/6 | INSEPARABLE | 3/6 | INSEPARABLE | no |
| 0.1 | 10x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 0.5 | 50x | 1/6 | INSEPARABLE | 1/6 | INSEPARABLE | no |
| 1 | 100x | 1/6 | INSEPARABLE | 1/6 | INSEPARABLE | no |

Verdict at the registered `tau` is **INSEPARABLE**, stable over `tau` in [0.005, 1] = x0.5 to x100; flips at the next grid point below: 0.001, above: —. Grid-censored below: no, above: yes.

### S_C — base

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0** = **0x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.001 | 0.1x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.005 | 0.5x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.01 | 1x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.02 | 2x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.05 | 5x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.1 | 10x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.5 | 50x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |
| 1 | 100x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |

Verdict at the registered `tau` is **INSEPARABLE**, stable over `tau` in [0.0001, 1] = x0.01 to x100; flips at the next grid point below: —, above: —. Grid-censored below: yes, above: yes.

### S_C — adversarial

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0** = **0x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.001 | 0.1x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.005 | 0.5x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.01 | 1x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.02 | 2x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.05 | 5x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.1 | 10x | 2/3 | INSEPARABLE | 2/3 | INSEPARABLE | no |
| 0.5 | 50x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |
| 1 | 100x | 1/3 | INSEPARABLE | 1/3 | INSEPARABLE | no |

Verdict at the registered `tau` is **INSEPARABLE**, stable over `tau` in [0.0001, 1] = x0.01 to x100; flips at the next grid point below: —, above: —. Grid-censored below: yes, above: yes.

### S_C — union (K=6)

Exact flip point `tau* = sigma_K/sigma_1 = 1/kappa` = **0** = **0x** the registered `tau`.

| tau | tau/registered | coupled kappa_max=1/tau: rank | verdict | tau alone, kappa_max=100: rank | verdict | kappa branch fires alone |
|---|---|---|---|---|---|---|
| 0.0001 | 0.01x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 0.001 | 0.1x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 0.005 | 0.5x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 0.01 | 1x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 0.02 | 2x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 0.05 | 5x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 0.1 | 10x | 2/6 | INSEPARABLE | 2/6 | INSEPARABLE | no |
| 0.5 | 50x | 1/6 | INSEPARABLE | 1/6 | INSEPARABLE | no |
| 1 | 100x | 1/6 | INSEPARABLE | 1/6 | INSEPARABLE | no |

Verdict at the registered `tau` is **INSEPARABLE**, stable over `tau` in [0.0001, 1] = x0.01 to x100; flips at the next grid point below: —, above: —. Grid-censored below: yes, above: yes.

## 5. The kappa_max branch — reachable, and exactly where

`audit/G3_ADVERSARIAL_REVIEW.md` finding 1.4 established that at the registered pair the
two criteria of `docs/THRESHOLDS.md` §1.3 are one criterion, and left the branch
unexplored. The prediction, from the algebra: **with every singular value resolved, the
`kappa` branch fires alone exactly on `kappa_max < kappa <= 1/tau`, which is empty
whenever `kappa_max >= 1/tau` — and the registered pair sets `kappa_max = 1/tau`.**

The grid below recomputes the verdict through the production `analyse()` at every
`(tau, kappa_max)` pair and the script checks each row against that prediction, so a
disagreement between the algebra and the production rule is a failure and not a footnote.

| Summary set | columns | kappa | grid points | where kappa branch fires alone | algebra agrees | smallest kappa_max at registered tau that flips the verdict |
|---|---|---|---|---|---|---|
| S_A | base | 5.378 | 108 | 21 | yes | 1 |
| S_A | adversarial | 136.7 | 108 | 21 | yes | 1 |
| S_A | **union (K=6)** | inf | 108 | 0 | yes | 1 |
| S_B | base | 10.12 | 108 | 24 | yes | 1 |
| S_B | adversarial | 64.62 | 108 | 24 | yes | 1 |
| S_B | **union (K=6)** | 628.9 | 108 | 18 | yes | 1 |
| S_C | base | inf | 108 | 0 | yes | 1 |
| S_C | adversarial | inf | 108 | 0 | yes | 1 |
| S_C | **union (K=6)** | inf | 108 | 0 | yes | 1 |

## 6. The checks this run had to pass before any of the above counts

| Summary set | columns | leakage check (permutation equivariance) | permutations tested | reproduces the recorded singular values |
|---|---|---|---|---|
| S_A | base | yes | 5 | yes (max rel diff 0) |
| S_A | adversarial | yes | 5 | yes (max rel diff 0) |
| S_A | **union (K=6)** | no | 719 | — |
| S_B | base | yes | 5 | yes (max rel diff 0) |
| S_B | adversarial | yes | 5 | yes (max rel diff 0) |
| S_B | **union (K=6)** | yes | 719 | — |
| S_C | base | yes | 5 | yes (max rel diff 0) |
| S_C | adversarial | yes | 5 | yes (max rel diff 0) |
| S_C | **union (K=6)** | no | 719 | — |

The reproduction check is the load-bearing one: the three-column spectra computed here
must equal, to floating point, the ones already on record from sessions G3 and G4 at the
same seed, replicate count and step size. If they did not, this run's estimator would be
a different estimator and no six-column number from it could be compared with the
three-column result it is supposed to extend.

