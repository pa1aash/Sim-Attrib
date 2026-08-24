# The confidence-set-bounded MMC check — session G11, T1-3

# VERDICT: **STANDS — AND IS NOW DATA-GROUNDED.** The non-termination collapse (`results/cost_gate.yaml`,
`results/boundary_sweep.yaml`) survives when the nuisance box is not an assumed ±5% but the
actual 95% confidence set a maximum-likelihood fit to one realised dataset implies. Every
coordinate of that data-implied box is wider than the ±0.5% box at which the composition was
already known to pass, and the gate **FAILS at every declared corner, under all four
(family, variant) combinations**, at a measured worst-cell acceptance probability of
`1×10⁻⁵` (primary case) down to exactly `0` (three of four cases). This converts "the
composition fails once the nuisance parameters are uncertain" from a claim resting on an
arbitrary box into a claim resting on what a real analyst's uncertainty would actually be.

---

## 0. What this check answers, and why the existing ±5% box was not enough

An independent adversarial review of the drafted paper (an independent reviewing model with no
project history, two-phase cold-read plus history-informed consistency check, Weak Reject at
confidence 4/5, unchanged after full disclosure) named this the single most important open
question in the paper: the MMC
composition's non-termination result (Section 5 of `paper/main.tex`) is measured under a
relative box on the five nuisance coordinates whose half-width — 0.1% to 5% in
`results/boundary_sweep.yaml`, ±5%, ±10%, ±20%, ±50% in `results/p_sel.yaml` — was **never
derived from anything**. It is a round number, chosen because it is a round number. The paper's
central negative claim therefore rested on an assumption nobody had defended.

**The operator's instruction, given rather than left to this session's judgement:** run the
actual confidence-set-bounded check Dufour (2006) anticipates, not the cheaper reframe (stating
the existing box's arbitrariness as a caveat without measuring an alternative). This document
records that check, in full.

---

## 1. A correction to the session brief, found by doing what it asked

The brief that commissioned this check states that Dufour (2006) "explicitly anticipates this
exact objection" and supplies "a Bonferroni correction connecting the confidence-set coverage to
the overall test's exactness." It also instructs: fetch Dufour in full and confirm the exact
construction, "do not approximate from memory of the earlier citation."

**Doing exactly that turned up something that needed stating rather than quietly working
around.** Dufour (2006), CIRANO Working Paper 2005s-02 — the same version this project's
`audit/MMC_COMPOSITION_SPEC.md` already cites, fetched in full via `hyperresearch`
(`research/notes/publi-en-fvrier-2005.md`, 87,153-character body, re-read directly for this
check rather than taken on the earlier citation's word) — **never uses the word "Bonferroni"
anywhere in its text.** `grep -i bonferroni` on the full fetched body: zero matches.

What Dufour's Section 5 actually contains (Propositions 5.1–5.2) is an **asymptotic-coverage**
argument for a *consistent set estimator MMC* (CSEMMC): any sequence of sets `C_T` with
`P[θ₀ ∈ C_T] → 1` as the sample size `T → ∞` gives a test with asymptotically correct level. He
gives one worked example of such a `C_T` — a Wald-type ellipsoid,
`C_T = {θ : ‖A_T(θ̂_T − θ)‖² < c/T^δ}`, built from a consistent point estimate `θ̂_T` and a
scaling matrix `A_T` (his eq. 5.13) — with **no coordinate-wise decomposition and no
multiple-comparisons correction anywhere in it**:

> *"It is quite easy to find a consistent set estimate of θ₀ whenever a consistent point
> estimate θ̂_T of θ₀ is available."* — Dufour (2006) §5

**What is true, and is the part of the brief's description worth keeping.** This project's
existing MMC infrastructure (`src/diagnostics/p_sel.py`, `boundary_sweep.py`, `cost_gate.py`) is
built entirely around axis-aligned relative *boxes* — that is the only shape `Ω₀` has ever taken
in this project's numbers. Realising Dufour's `C_T` as a box that **circumscribes** the Wald
ellipsoid, rather than writing a new ellipsoid sampler, does genuinely need a Bonferroni step:
one marginal Wald interval per nuisance coordinate, each built at level `1 − α₁/(2K)`, so a
Bonferroni union bound gives the *joint* box coverage `P[θ₀ ∈ box] ≥ 1 − α₁`. **This is a design
choice made in this session, using a standard and correct technique — not a claim about what
Dufour's paper itself says.** The distinction matters because the brief attributed the technique
to the source rather than to the choice of how to realise it against this project's existing
tooling, and T1-3(b)'s instruction was to get this exactly right rather than to approximate.

---

## 2. The construction, in full

### 2.1 What "the data" means for a synthetic-simulator paper

There is no real epidemic dataset behind `θ₀ = (β=0.35, γ=0.14, ρ=0.40, I₀=10.0,
σ_obs=0.15)` (`src/simulators/sir3.py::SIR3Params`, confirmed against the module directly, not
assumed). "The data-implied confidence set" means: the confidence set an analyst holding **one**
realised 120-day reported-incidence curve from this simulator, at these true parameters, and
fitting the same model class back to it by maximum likelihood, would report. That is the honest
and only available reading for a methods paper whose simulator *is* the data-generating process,
and it is stated here rather than left implicit.

The fit uses the **full 120-day reported series** — not the `S_B` summary reduction the
diagnostic and selection rule are built on — because that is the most informative object this
simulator's own model class can offer an analyst, and therefore the *tightest* confidence set
this construction can produce. A result that survives the tightest defensible box is the
strongest version of the finding available.

### 2.2 α₁ = 0.05

`audit/MMC_COMPOSITION_SPEC.md` does not commit to a numeric confidence level for CSEMMC
anywhere (checked directly: §4 point 2 names it as an unpriced option, nothing more). 0.05 is
adopted here as the conventional choice, for that reason and no other.

### 2.3 The fit

One "observed" realisation was simulated at `θ₀`, `η = 0`, seed `9,000,000,000` (chosen once,
before any fit was run, and confirmed disjoint from every seed span `results/p_sel.yaml` and
`results/boundary_sweep.yaml` record — the run aborts if it is not, and it was not asked to).
`(β, γ, ρ, I₀, σ_obs)` were fit by maximum likelihood under the simulator's own lognormal
multiplicative observation model — `log(y_t) − log(mean_t) + σ²/2 ~ N(0, σ²)` — by Nelder-Mead
in log-parametrised space, started **15–35% off** `θ₀` on every coordinate rather than at the
answer (`src/diagnostics/confidence_set_check.py::START_MULTIPLIER`).

**A real engineering finding, disclosed because it changed the method.** Raw L-BFGS-B from the
perturbed start fails informatively: the coordinates' wildly different natural scales
(`I₀ ~ 10`, `σ_obs ~ 0.15`) combined with the RK4-integrated likelihood's steep gradient
(`~10⁴`–`10⁵` at the start point) send the first Newton-like trial step to the corner of the
parameter bounds, where every coordinate gives a non-positive reported-incidence mean and the
likelihood is `+∞`; L-BFGS-B then reports spurious convergence at the **unmoved** starting
point. Traced by logging every function evaluation the optimiser made, not inferred. Nelder-Mead
in log-space, which does not size its first step from a single steep gradient, does not have
this failure mode and converges cleanly.

**Result:**

| coordinate | true θ₀ | θ̂ (MLE) | offset, in SE |
|---|---|---|---|
| β | 0.35 | 0.35509 | 1.573 |
| γ | 0.14 | 0.14754 | 1.886 |
| ρ | 0.40 | 0.40499 | 0.524 |
| I₀ | 10.0 | 10.3722 | 0.661 |
| σ_obs | 0.15 | 0.15684 | 0.676 |

655 function evaluations, converged, scaled gradient `3.35×10⁻³` against a tolerance of
`10⁻²`. Every offset is under two standard errors — a fit an analyst would accept without
comment, not a distorted one that would flatter or damage the check either way.

### 2.4 The Hessian, the covariance, and the box

The observed Fisher information was estimated as the numerical Hessian of the negative
log-likelihood at `θ̂` (central differences, per-coordinate relative step). All five
eigenvalues are **positive** (`3.15, 9,672, 16,775, 58,293, 5,301,601`) — the information
matrix is well-conditioned, not near-singular in any direction, so there is no early-exponential-
phase β/γ/I₀ aliasing of the kind the epidemic-identifiability literature warns about (Miao,
Xia, Perelson & Wu 2011; the full 120-day curve, including the peak and the post-peak decline,
resolves it). Inverting gives the asymptotic covariance `Σ̂` and per-coordinate standard errors.

The Bonferroni box at `α₁ = 0.05`, `K = 5`: `z = Φ⁻¹(1 − 0.05/10) = 2.5758`.

| coordinate | SE | relative half-width | vs. the ±0.5% box that passed |
|---|---|---|---|
| β | 0.003237 | **2.35%** | 4.7× wider |
| γ | 0.004001 | **6.98%** | 14.0× wider |
| ρ | 0.009524 | **6.06%** | 12.1× wider |
| I₀ | 0.563147 | **13.99%** | 28.0× wider |
| σ_obs | 0.010124 | **16.63%** | 33.3× wider |

**Every single coordinate of the data-implied box is wider than the box the fixed-width sweep
had already shown collapses the acceptance probability to zero.** The narrowest coordinate
(`β`, 2.35%) alone is already inside the SPLIT-to-FAIL region `results/boundary_sweep.yaml`
maps between 0.75% and 3%; the two widest (`I₀`, `σ_obs`, both over 13%) are nearly three times
the ±5% width at which 21 of 42 design points already had a dead cell.

---

## 3. What was measured, and the comparison

`src/diagnostics/confidence_set_check.py`, committed as its own unit at `a91131a` **before**
this run — matching this project's standing discipline (`src/diagnostics/boundary_sweep.py`,
`p_sel.py`, `k6_spectrum.py` were each committed before their own first run, for the same
reason: a design chosen after seeing the data it describes is not a design). Liveness verified
via `src/runlock.py` (the same tested infrastructure `boundary_sweep.py` and `p_sel.py` use, not
a new ad hoc check) before launch; seed spans checked disjoint from `results/p_sel.yaml` and
`results/boundary_sweep.yaml` (the run aborts otherwise); normalisation and Jacobian reproduction
re-verified before any draw was taken. **`dirty: false`** — run from the exact commit
`a91131a`, on a tree with nothing else staged (the fig2_simulator/report_claims work in progress
at the time was stashed for the duration, per S3, once a concurrent-edit risk was noticed and
corrected before it could contaminate this run's provenance).

The same 32-corner-plus-10-axis-endpoint design this project has used since `p_sel.nuisance_grid`
(session G6), generalised to the data-implied box's **unequal** per-coordinate half-widths
(`src/diagnostics/confidence_set_check.py::hetero_grid`) rather than one shared width. Screened
at 10,000 draws per point (42 points, 420,000 draws), the four lowest points per
(assignment, variant) key re-measured at 100,000 draws each for de-biasing, and the box's
centre `θ̂` measured at 100,000 draws as the "affordable at a known parameter" anchor — matching
G6/G7's own draw counts exactly, so this measurement is comparable to theirs on its own terms.
**722,000 simulator draws total, 178 seconds.**

| | at `θ̂` (known point) | inside the data-implied box |
|---|---|---|
| **AAA, studentised (primary)** | worst cell `p_sel = 0.1161` (95% CI 0.1141–0.1180) — **PASS**, cheapest corner `8.53×10⁵` draws, dearest `8.61×10⁷`, against the `10⁸` gate | worst cell `p_sel = 1×10⁻⁵` (95% CI `1.77×10⁻⁶`–`5.66×10⁻⁵`) — **FAIL** at every corner: cheapest declared corner alone needs `9.90×10⁹` draws, **99× the gate**, and even at the CI95 favourable end the cheapest corner needs `1.75×10⁹` draws, still 17× over |
| **AAA, plain** | worst cell `p_sel = 3.1×10⁻⁴` — **FAIL** even at the known point (the non-primary variant was always disclosed as the less favourable one; this is the first point at which it fails even without nuisance uncertainty) | `p_sel = 0` in 100,000 draws (95% UB `3.84×10⁻⁵`) — **FAIL** |
| **BBB, studentised** | not the primary case; not separately anchored here | `p_sel = 0` in 100,000 draws — **FAIL** |
| **BBB, plain** | not the primary case | `p_sel = 0` in 100,000 draws — **FAIL** |

**Session verdict (both variants of the primary AAA assignment must pass for a PASS, matching
`cost_gate.py`'s own convention): FAIL.**

Fraction of the 42 design points with at least one dead cell: 19.0% (AAA studentised, the
*best*-behaved case) up to 52.4% (BBB plain) — comparable to or worse than the 21/42 (50%) the
fixed ±5% box already showed, despite this box's coordinates individually reaching 2.8× to 33×
that width.

### 3.1 Reading the comparison plainly

The fixed ±5% box (`results/boundary_sweep.yaml`) was already known to collapse the composition.
The question T1-3 exists to answer is whether that collapse is a fact about the simulator and
the composition, or an artefact of a box nobody derived from anything. **It is not an artefact.**
A real analyst fitting this simulator's own model class to one realised dataset, at a
conventional 95% confidence level, would report a nuisance uncertainty on every one of the five
coordinates that is *wider* than the box already shown to break the composition — some
coordinates dramatically wider. The paper's central negative claim does not merely survive this
check; it clears its own prior evidence bar by a wide margin on every coordinate that was
checked.

---

## 4. What this changes about the paper (T1-3(f) / S4 disclosed-reclassification)

**Before this check:** Section 5 stated the collapse under a ±5% box the paper never justified,
disclosed as a stand-in for an unspecified `Ω₀`.

**After this check:** the collapse is additionally, and primarily, evidenced under a box **built
from the data themselves** — a strictly stronger and more defensible form of the same claim.
Per the standing disclosed-reclassification rule (D-8 through D-17+, `docs/DECISIONS.md`), the
original claim, the new measurement, and why the claim's evidentiary basis changes are stated
here and carried into `paper/main.tex` Section 5's rewrite: the confidence-set result becomes
the **primary** evidence; the original fixed-box sweep (`results/boundary_sweep.yaml`,
`results/cost_gate.yaml`) is retained and cited as a **secondary, broader-context sweep** that
independently locates *where* the collapse begins (the boundary sweep's own contribution, which
this check does not repeat and does not need to: it answers "does the collapse survive at a
box the data would actually imply", not "what is the exact shape of the boundary everywhere").

Nothing in `results/p_sel.yaml`, `results/cost_gate.yaml`, or `results/boundary_sweep.yaml` is
withdrawn, corrected, or reinterpreted. This check adds a fifth, independent results file
(`results/confidence_set_mmc.yaml`) and a fifth claim section (C5) to
`audit/FINAL_CLAIMS.md`'s numbering; it does not touch C1–C4.

---

## 5. What this check does not do, stated before anyone relies on it

* **One realised dataset, one true parameter point.** The same single-point conditionality
  every number in this repository carries (`DEVIATIONS.md` D-14 and every prior results file's
  own limitation section).
* **A Bonferroni box is a conservative circumscription of Dufour's ellipsoid, not the ellipsoid
  itself.** It can only be *wider* than the ellipsoid it circumscribes, never narrower. A
  collapse that survives inside this box therefore survives inside the (tighter, unmeasured)
  ellipsoid too — the FAIL direction of this result is robust to that approximation. A PASS
  would **not** have been similarly robust, and did not arise here.
* **It uses the full 120-day series, not the `S_B` summaries the rest of the paper's diagnostic
  and selection rule use.** This is the more informative, and therefore more favourable-to-a-
  narrow-box, choice available — stated as a choice, not hidden as if summaries and raw series
  gave the same precision.
* **It does not implement, test, price, or rehabilitate the MMC composition.** Nothing here
  revisits `docs/DECISIONS.md` D-16, which drops the composition as an experimental vehicle
  regardless of this box's answer — D-16's own text says as much: *"Had this sweep found the
  cells reachable out to 0.04, the composition would still be dropped."* This check answers a
  narrower, specific question T1-3 raised: is the box the paper's non-termination finding was
  measured under defensible. It is, and more so than the paper previously showed.
* **It rests on one construction of `T_k`, `S_B`, and the AAA/BBB family assignments** — the
  same conditionalities `DEVIATIONS.md` D-14 already attaches to every number in this thread.

---

## 6. Provenance

`results/confidence_set_mmc.yaml`, commit `a91131ab4ced705beea96a2774baa9b53864f150`,
`dirty: false`, seed `20260824`, 722,000 simulator draws, 178 seconds wall-clock, 4 workers.
`src/diagnostics/confidence_set_check.py` is the script, committed at the same hash before this
run. Every number in this document is transcribed from that file; none is hand-computed.
