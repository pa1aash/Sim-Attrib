# The cost gate, measured

Produced by `src/diagnostics/cost_gate.py` from the measured `results/p_sel.yaml`,
which is produced by `src/diagnostics/p_sel.py`. This table and `results/cost_gate.yaml`
are both generated; neither is edited by hand (S11).

## SESSION VERDICT: **FAIL**

Primary assignment `AAA`, per-variant verdicts `AAA|studentised` = **FAIL**, `AAA|plain` = **FAIL**.

> PASS only if every declared (M, N) corner passes under BOTH studentisation variants of the selection rule. A SPLIT is not a pass.

**Headline case `AAA|studentised`.** `p_sel` = **0** (95% CI 0 to 3.84131e-05), attained at `w0.05|corner|-+---` in cell 1 (0 of 100000 draws, refined).

Expected draws for ONE test: **unbounded** to **unbounded**, i.e. **unbounded** to **unbounded** the pre-registered gate of 1e+08 draws. At the measured 0.0003622 s per draw that is unbounded to unbounded core-hours.

**The cost consistent with the data at the 95% level is at least 2.577e+09 draws** and at least 2.601e+11 at the most expensive declared `(M, N)`. That lower bound is the number to read when the point estimate is unbounded: it is what the measurement rules out, rather than what it asserts.

`ci_decides_the_gate` = **True**.

## 1. Every declared (M, N) corner, for every case

`M` and `N` are the specification's own declared ranges, not this session's choices.
The flip column is the `p_sel` at which that corner changes its answer, so the flag
has a visible boundary rather than an implied one.

### `AAA|studentised` — headline box, `p_sel` = 0, verdict **FAIL**

| M | N | M*N | expected draws | CI95 draws | <= gate? | flips at p_sel | <= 1e7 budget? |
|---|---|---|---|---|---|---|---|
| 1000 | 99 | 99000 | unbounded | 2.577e+09 – unbounded | **no** | 0.00099 | **no** |
| 1000 | 999 | 999000 | unbounded | 2.601e+10 – unbounded | **no** | 0.00999 | **no** |
| 10000 | 99 | 990000 | unbounded | 2.577e+10 – unbounded | **no** | 0.0099 | **no** |
| 10000 | 999 | 9.99e+06 | unbounded | 2.601e+11 – unbounded | **no** | 0.0999 | **no** |

### `AAA|plain` — headline box, `p_sel` = 0, verdict **FAIL**

| M | N | M*N | expected draws | CI95 draws | <= gate? | flips at p_sel | <= 1e7 budget? |
|---|---|---|---|---|---|---|---|
| 1000 | 99 | 99000 | unbounded | 2.577e+09 – unbounded | **no** | 0.00099 | **no** |
| 1000 | 999 | 999000 | unbounded | 2.601e+10 – unbounded | **no** | 0.00999 | **no** |
| 10000 | 99 | 990000 | unbounded | 2.577e+10 – unbounded | **no** | 0.0099 | **no** |
| 10000 | 999 | 9.99e+06 | unbounded | 2.601e+11 – unbounded | **no** | 0.0999 | **no** |

### `BBB|studentised` — headline box, `p_sel` = 0, verdict **FAIL**

| M | N | M*N | expected draws | CI95 draws | <= gate? | flips at p_sel | <= 1e7 budget? |
|---|---|---|---|---|---|---|---|
| 1000 | 99 | 99000 | unbounded | 2.577e+09 – unbounded | **no** | 0.00099 | **no** |
| 1000 | 999 | 999000 | unbounded | 2.601e+10 – unbounded | **no** | 0.00999 | **no** |
| 10000 | 99 | 990000 | unbounded | 2.577e+10 – unbounded | **no** | 0.0099 | **no** |
| 10000 | 999 | 9.99e+06 | unbounded | 2.601e+11 – unbounded | **no** | 0.0999 | **no** |

### `BBB|plain` — headline box, `p_sel` = 0, verdict **FAIL**

| M | N | M*N | expected draws | CI95 draws | <= gate? | flips at p_sel | <= 1e7 budget? |
|---|---|---|---|---|---|---|---|
| 1000 | 99 | 99000 | unbounded | 2.577e+09 – unbounded | **no** | 0.00099 | **no** |
| 1000 | 999 | 999000 | unbounded | 2.601e+10 – unbounded | **no** | 0.00999 | **no** |
| 10000 | 99 | 990000 | unbounded | 2.577e+10 – unbounded | **no** | 0.0099 | **no** |
| 10000 | 999 | 9.99e+06 | unbounded | 2.601e+11 – unbounded | **no** | 0.0999 | **no** |

## 2. The cost as a function of how wide the nuisance set is

`Omega_0` is a relative box on the five nuisance coordinates. A wider box can only
lower `min p_sel`, so cost is monotone in width by construction; what the table shows
is how fast.

| case | box half-width | min p_sel | attained at | cell | verdict |
|---|---|---|---|---|---|
| `AAA|studentised` | w=0.05 | 0 | `w0.05|corner|-+---` | 1 | **FAIL** |
| `AAA|studentised` | w=0.1 | 0 | `w0.05|corner|-+---` | 1 | **FAIL** |
| `AAA|studentised` | w=0.2 | 0 | `w0.05|corner|-+---` | 1 | **FAIL** |
| `AAA|studentised` | w=0.5 | 0 | `w0.05|corner|-+---` | 1 | **FAIL** |
| `AAA|plain` | w=0.05 | 0 | `w0.05|corner|+-+--` | 0 | **FAIL** |
| `AAA|plain` | w=0.1 | 0 | `w0.05|corner|+-+--` | 0 | **FAIL** |
| `AAA|plain` | w=0.2 | 0 | `w0.05|corner|+-+--` | 0 | **FAIL** |
| `AAA|plain` | w=0.5 | 0 | `w0.05|corner|+-+--` | 0 | **FAIL** |
| `BBB|studentised` | w=0.05 | 0 | `w0.05|corner|+----` | 0 | **FAIL** |
| `BBB|studentised` | w=0.1 | 0 | `w0.05|corner|+----` | 0 | **FAIL** |
| `BBB|studentised` | w=0.2 | 0 | `w0.05|corner|+----` | 0 | **FAIL** |
| `BBB|studentised` | w=0.5 | 0 | `w0.05|corner|+----` | 0 | **FAIL** |
| `BBB|plain` | w=0.05 | 0 | `w0.05|corner|-----` | 0 | **FAIL** |
| `BBB|plain` | w=0.1 | 0 | `w0.05|corner|-----` | 0 | **FAIL** |
| `BBB|plain` | w=0.2 | 0 | `w0.05|corner|-----` | 0 | **FAIL** |
| `BBB|plain` | w=0.5 | 0 | `w0.05|corner|-----` | 0 | **FAIL** |

## 3. The floor: what it would cost if theta were known

Not the gate. The null is composite, which is the entire reason the composition needs
Dufour's maximisation; this row is what the cost would be if it did not.

| case | worst-cell p_sel at theta_0 | CI95 | expected draws | verdict |
|---|---|---|---|---|
| `AAA|studentised` | 0.23457 | 0.232 – 0.2372 | 4.22e+05 – 4.259e+07 | **PASS** |
| `AAA|plain` | 0.00071 | 0.000563 – 0.0008954 | 1.394e+08 – 1.407e+10 | **FAIL** |
| `BBB|studentised` | 0.24945 | 0.2468 – 0.2521 | 3.969e+05 – 4.005e+07 | **PASS** |
| `BBB|plain` | 0.02412 | 0.02319 – 0.02509 | 4.104e+06 – 4.142e+08 | **SPLIT** |

## 4. Explicitly NOT part of the gate: what a demonstration would cost

The gate prices ONE MMC test. A demonstration is many. These numbers are recorded because the operator needs them and are explicitly NOT part of the pre-registered verdict above.

audit/S0_REPORT.md section 7 prices the protocol at R=200 replicates x L=10 collinearity levels for ONE baseline.

| replicated tests | expected draws (headline case) |
|---|---|
| 1 | unbounded – unbounded |
| 10 | unbounded – unbounded |
| 200 | unbounded – unbounded |

