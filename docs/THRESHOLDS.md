# Thresholds — pre-registered, before any singular value exists

**Written 2026-08-20, session G1.** This file answers **Q-4** and **Q-5**, and carries the
argument Phase 3.7 requires before `LEDGER_DESIGN.md` **D8** may be implemented.

> **Provenance claim, and it is checkable.** At the commit that introduces this file,
> `results/` is empty, `src/` contains no Python, and no Jacobian has been computed in this
> repository. Every number below was therefore chosen **without any possibility of having
> been fitted to a result**, which is the property `LEDGER_DESIGN.md` D3 and `S0_REPORT.md`
> §8 both demand and which is otherwise only assertable, not demonstrable. `git log` is the
> evidence. See `DEVIATIONS.md` **D-6** for why this file exists in a session whose code
> phase was stopped.

Revising anything here after results exist requires a logged entry in `DEVIATIONS.md`
stating what changed, what the result was that prompted it, and why the change is not
motivated by the result.

> ### Session G4 (2026-08-20) — checked, and **nothing in this file was revised**
>
> The thresholds below were attacked in `audit/G3_ADVERSARIAL_REVIEW.md`. **No number here has
> been changed**, and the annotations added at §1.2, §1.3 and §1.4 qualify how the results may
> be *described*; they do not move a threshold. That distinction is the whole point: the value
> of this file is that it predates every singular value, which `git log` establishes, and a
> threshold re-derived after the numbers exist would forfeit it (`LEDGER_DESIGN.md` D3,
> **Q-11**).
>
> Read the annotations at **§1.2** (how far the tolerance can move before the verdict does),
> **§1.3** (the two criteria are one criterion) and **§1.4** (what the h-plateau does and does
> not certify) before quoting any number from `results/`.

---

## 0. The normalisation these numbers presuppose

**No threshold below means anything without this section.** The rank of *J* is not
scale-invariant (`S0_REPORT.md` §8), so a tolerance on its singular values is a statement
about a choice of units. Both normalisations are fixed here, in advance.

**Summaries.** Each summary statistic `s_d` is divided by its **prior-predictive standard
deviation** `σ_d`, estimated by simulating from the base parameters with **no distortion**
(`η = 0`) over `R_norm` independent replicates. `R_norm` and the resulting `σ_d` vector are
to be recorded **in every results file**, not only in code, so a reader of `results/` can
audit the scale choice without reading `src/`. A summary with `σ_d = 0` under the base
simulator is degenerate and must be dropped, with the drop recorded.

**Distortion parameters.** Each `η_k` is normalised by a **fixed relative perturbation
scale** `η_k^scale`, not an absolute one — so that "one unit of normalised `η_k`" means the
same *fractional* change to component *k* for every *k*. The scales are properties of the
distortion families, fixed once, and recorded in every results file.

**Consequently `J` is dimensionless**, and entry `J_dk` reads: *"the change in summary d, in
prior-predictive standard deviations, produced by a full-scale relative distortion of
component k."* Every threshold below is a statement about that quantity and about nothing
else.

---

## 1. Q-4 — the summary sets, and what counts as "inseparable"

### 1.1 The list is closed

Exactly three summary sets will be searched. **`S_A`, `S_B`, `S_C`, and no others.**

| Set | Contents | Role |
|---|---|---|
| **S_A** | Epidemic-curve features: peak height, peak time, final size, exponential growth rate | The set a domain modeller would actually choose |
| **S_B** | ~10 time-binned incidence counts | The set an SBI practitioner would actually choose |
| **S_C** | Final size + peak height only | **Positive control, expected to FAIL** |

`S_C` exists because a rank number with nothing to validate against is uninterpretable. With
`d = 2 < K = 3`, `J` cannot have rank 3 — **`S_C` must fail by construction**, and if it does
not, the implementation is wrong rather than the simulator being surprising. That is the
point of including it: it is a test of the harness, not of the science.

> **If `S_C` does not fail, that is a finding to report, not a bug to silently fix**
> (Phase 3.3). Concretely: a reported rank of 3 from a 2×3 matrix would mean the rank
> routine is not doing what it claims, and the correct response is to report it as a harness
> failure — it would invalidate `S_A` and `S_B`'s numbers too.

**Adding a fourth summary set requires a `DEVIATIONS.md` entry** naming the set, the reason,
and whether `S_A`/`S_B` results were known at the time of the decision. Without this the
D4 STOP condition can be evaded indefinitely by proposing one more summary set — which is
the failure mode `LEDGER_DESIGN.md` D4 was written to prevent.

### 1.2 Numerical rank, at a stated and parameterised tolerance

**Rule.** `rank(J) = #{ i : σ_i ≥ τ · σ_1 }` with **`τ = 10⁻²`**.

**Not** the LAPACK default `max(d,K)·ε_machine·σ_1 ≈ 10⁻¹⁶·σ_1`. That tolerance describes
floating-point noise in an *exactly known* matrix. This Jacobian is estimated by central
differences from a simulator whose observation layer is stochastic, so its error floor sits
many orders of magnitude above machine epsilon and a machine-epsilon tolerance would report
full rank on a matrix that is numerically meaningless.

**Where `10⁻²` comes from — a compute budget, not a convention.** Because summaries are
normalised to unit prior-predictive standard deviation, a Monte Carlo estimate of the
summary vector from `n` replicates carries error of order `n^(-1/2)` per coordinate.
Recovering `η` from an observed summary shift amplifies that error by the condition number
`κ = σ_1/σ_K`. Resolving the components therefore needs roughly `n ≳ κ²` replicates.

| `κ` | replicates `n ≈ κ²` needed to separate components | verdict |
|---|---|---|
| 10 | ~10² | comfortable |
| 100 | ~10⁴ | affordable but expensive |
| 1000 | ~10⁶ per replicate — and `S0_REPORT.md` §7 already prices the full protocol at 10⁶–10⁷ simulations *in total* | **not affordable** |

So `κ = 100`, i.e. `τ = 1/κ = 10⁻²`, is the point at which separating the components costs
more than the study's entire declared simulation budget. That is a defensible place to put
the line because it is derived from a constraint fixed before the diagnostic existed, rather
than chosen to make a matrix look full-rank.

`τ` is **a parameter of the function, not a constant in it** (Phase 3.4), and results files
record the singular values in full so any reader can re-apply their own tolerance.

> #### G4 annotation — the margin, measured
>
> A reader *has now* re-applied their own tolerance. `results/robustness/ROBUSTNESS_TABLE.md`
> §1 tabulates the verdict across a range of alternatives and, more usefully, gives the **exact**
> tolerance at which each set flips: since the rule is `σ_K ≥ τ·σ₁`, the flip point is
> `τ* = σ_K/σ₁ = 1/κ`.
>
> **Halving or doubling `τ` changes nothing for either `S_A` or `S_B`. At one order of
> magnitude, `S_B` flips to INSEPARABLE and `S_A` does not.**
>
> **And a sharper point that needs no disagreement with `τ` at all.** The table above is this
> file's own derivation, and it labels `κ = 10` *comfortable* and `κ = 100` *affordable but
> expensive*. The line was drawn at the third row. **`S_B`'s measured `κ` sits just outside the
> first row** — it is separable at the registered threshold and it is not *comfortably*
> separable, and those are different sentences. `S_A` is inside on either reading.
>
> This is not a case for revising `τ`. It is a constraint on description: reporting "both sets
> are separable" without the distinction reports a threshold decision as a structural finding.
> See `audit/G3_ADVERSARIAL_REVIEW.md` finding 1.

### 1.3 The condition-number ceiling for the D4 STOP condition

**`κ_max = 100`.** A summary set is **"inseparable"** if **either**:

- `rank(J) < 3` at `τ = 10⁻²`, **or**
- `κ = σ_1/σ_3 > 100`.

These are the same criterion stated two ways for `K = 3`, and both are recorded because the
second degrades gracefully in a way the first does not: `κ = 98` and `κ = 102` are nearly
the same situation, while `rank = 3` and `rank = 2` are not.

> #### G4 annotation — this sentence is correct and it did not propagate
>
> "The same criterion stated two ways" is exact, not approximate. With `d ≥ K = 3` and every
> singular value resolved, `rank = 3 ⟺ σ₃ ≥ τσ₁ ⟺ κ ≤ 1/τ = κ_max`, boundary included, because
> `κ_max` was *defined* as `1/τ`. **The second criterion cannot fail unless the first already
> has.**
>
> **Everything downstream of this file reports them as two checks.**
> `results/jacobian_rank.*.yaml` carries `full_column_rank` and `condition_number` as separate
> fields; `results/SUMMARY_TABLE.md` prints them as separate columns; the verdict string reads
> *"full column rank at tau **and** condition number within ceiling"*; `audit/S3_REPORT.md` §3.2
> reproduces all of it. A reader who has not returned to this section sees a conjunction of two
> independent tests passing, when one test passed twice. In
> `src/diagnostics/jacobian_rank.py` the `inseparable_reason` branch naming the condition number
> is **unreachable at the pre-registered pair** for the same reason (it is reachable if a caller
> passes a non-reciprocal `τ` and `κ_max`, which the function permits).
>
> **Under `DEVIATIONS.md` D-8's rule — under what condition would "condition number within
> ceiling" read FALSE while "full column rank" read TRUE? — there is none.** The design is sound
> and disclosed here; the reporting is what needs fixing, and the fix is to describe one
> criterion once. `audit/G3_ADVERSARIAL_REVIEW.md` finding 1.4.

### 1.4 The h-plateau, and unresolved singular values

A rank computed at a single step size `h` is not a result (Phase 3.4). `h` is swept over
`{10⁻¹, 10⁻², 10⁻³, 10⁻⁴, 10⁻⁵, 10⁻⁶}` and the **plateau** — the contiguous range of `h`
over which the singular values are stable — is reported, not a single `h`.

**Pre-registered stability criterion.** A singular value is **resolved** if it varies by less
than a **factor of 2** across the identified plateau. A singular value that is not resolved
**must be reported as unresolved and must not be counted** toward the rank in either
direction. If `σ_3` is unresolved, the honest output is *"the rank of this Jacobian is not
determined by this estimator at this precision"* — which is a third outcome distinct from
both branches of D4, and it is a **G1 failure** (an uninterpretable diagnostic), not a pass.

**Why the plateau must exist at all.** Central differences carry truncation error `O(h²)` and
noise-amplification error `O(ε/h)`. A plateau exists only if there is a range of `h` where
both are small. If no plateau exists, **R2 is dead** and no rank call is defensible —
`audit/CLAIM_GRAPH.md` records this as R2a, and it is checked first.

**Common random numbers** are used across the `f(η+h)` and `f(η−h)` evaluations at each `h`
(same seed for both). Without them the finite difference is contaminated by simulation noise
that is indistinguishable from the signal being measured, and the `O(ε/h)` term swamps the
plateau.

> #### G4 annotation — what the CRN construction rests on, named
>
> The plateau exists because the common-random-numbers difference estimates a **pathwise**
> derivative, and that requires the simulator's sample path to be a smooth function of `η` at a
> fixed seed. This is the standing precondition of the whole finite-difference-with-common-
> random-numbers literature, not a property of this simulator: **L'Ecuyer & Perron (1994)**,
> *"On the Convergence Rates of IPA and FDC Derivative Estimators"*, Operations Research 42(4)
> 643–656, DOI `10.1287/opre.42.4.643`, prove that FDC matches IPA's `O(n^{-1/2})` rate
> *"under the (sufficient) conditions usually given for infinitesimal perturbation analysis
> (IPA) to apply"*, and state that their developments *"are based on continuity and
> smoothness."*
>
> **Where the sample path is not smooth, the guarantee is void and no plateau exists.** A
> count-valued observation layer is exactly that case, and
> `results/robustness/crn_count_check.yaml` measures it under two different couplings to show
> the failure is the discreteness rather than any particular sampler. `audit/G3_ADVERSARIAL_
> REVIEW.md` finding 3.
>
> **Consequence for this section:** a plateau is evidence that the estimator has converged. It
> is **not** evidence that the summary map is smooth — the smoothness is the *assumption* under
> which the plateau means anything, and it has to be argued separately for each summary
> coordinate. `S_A`'s peak statistics are where that argument was wrong; see finding 4.

### 1.5 Invisible components — a different failure, kept separate

A near-zero **column norm** means a component is invisible to these summaries. A near-zero
**smallest singular value** with all column norms healthy means two or more components are
confounded. These are different failures with different consequences and **rank alone
conflates them** (`S0_REPORT.md` §8), so they get separate criteria and separate fields.

**Rule.** Component *k* is **invisible** under a summary set if `‖J_·k‖₂ < 0.1`.

**Where `0.1` comes from.** The column is measured in prior-predictive standard deviations
per full-scale distortion. `‖J_·k‖₂ < 0.1` says a full-scale distortion of component *k*
moves the entire summary vector by less than one tenth of a prior-predictive standard
deviation — so *detecting* it, before any question of attributing it, needs ~10² replicates.
A component that cannot be detected cannot be attributed, and reporting it as "confounded
with component j" would be wrong: it is not confounded, it is absent.

### 1.6 The STOP condition, stated so it can fire

**D4 fires if all three of `S_A`, `S_B`, `S_C` are inseparable by §1.3.** Then the project's
output is the negative identifiability result and no further design work proceeds
(`LEDGER_DESIGN.md` D4).

Since **`S_C` is expected to fail by construction** (§1.1), the STOP condition is decided by
`S_A` and `S_B`. This is worth stating explicitly so that `S_C`'s designed failure is not
later read as one third of the evidence for stopping.

---

## 2. Q-5 — the equivalence-class boundary

Where the rank condition fails, D8 requires reporting *equivalence classes* rather than
naming a single culprit. Which components go in a class is decided by the **right singular
vectors of the near-null directions**, not by the coherence matrix.

### 2.1 The rule

A right singular vector `v` with `σ ≤ τ·σ_1` names an unidentifiable direction: the
combination `Σ_k v_k η_k` is not recoverable. **Component *k* participates in that
equivalence class iff `|v_k| ≥ 0.3`.**

**Where `0.3` comes from.** For `K = 3`, `v` is a unit vector in `ℝ³`. A clean two-component
confound gives `v = (1/√2, −1/√2, 0)`, so participants sit at `|v_k| ≈ 0.707` and the
non-participant at `0`. A clean three-way confound gives `|v_k| ≈ 1/√3 ≈ 0.577`. The
threshold has to sit below `0.577` to admit genuine three-way classes, and far enough above
`0` that a non-participating component is not swept in by estimation noise. `0.3` is below
both clean values by a comfortable margin and corresponds to a component contributing under
9% of the direction's squared norm.

**Stability requirement, which is not optional.** `|v_k|` is reported **as a range across
the h-plateau**, not as a single number. A component whose `|v_k|` crosses `0.3` within the
plateau is reported as **borderline** and named as such in the results file. Singular vectors
for nearly-equal singular values are ill-conditioned even when the singular values themselves
are well resolved, so this is the specific place where a confident-looking number is most
likely to be an artefact.

### 2.2 Coherence is reported, and is not the decision rule

Pairwise coherence `μ_ij = |⟨J_·i, J_·j⟩| / (‖J_·i‖‖J_·j‖)` is computed and reported for all
pairs, and pairs with **`|μ_ij| ≥ 0.98`** are flagged for inspection.

**It is deliberately not the criterion**, and the reason is arithmetic. For a two-column
submatrix, `κ₂ = √((1+μ)/(1−μ))`. The coherence consistent with the `κ_max = 100` ceiling of
§1.3 is `μ = (10⁴−1)/(10⁴+1) ≈ 0.9998` — a number so close to 1 that it is dominated by
estimation error and is useless as a decision threshold. The flagging level `0.98`
corresponds to `κ₂ = 10`, the "comfortable/uncomfortable" boundary of §1.2, and is a
**diagnostic pointer to which pair is responsible**, not a verdict.

Using two inconsistent criteria — one on `κ`, one on `μ` — would let the same matrix be
called separable and inseparable depending on which table a reader looked at. One decision
rule, on the singular values; coherence for interpretation.

---

## 3. Phase 3.7 — why finite-parametric equivalence classes are meaningful when Kahl's are not

`LEDGER_DESIGN.md` records this as a threat to **D8**. Kahl, Wendland, Neidhardt, Weber &
Kschischo (2019), *Physical Review X* 9:041046, read in full during G0:

> *"For a noninvertible system, the null space of Φ is always infinite dimensional … there
> are **infinitely many independent inputs which cannot be distinguished from each other**.
> This property shows that **there is no such thing as 'nearly invertible.'** Thus, any
> algorithm attempting to infer the inputs from the outputs is **bound to fail without
> further assumptions**."*

If that dichotomy imports, D8 is ill-posed: there would be no finite equivalence class to
report and no graceful degradation to describe. **The argument that it does not import
follows, and so does the part of it that does.**

### 3.1 The objects are of different dimension, and the dichotomy is a statement about dimension

Kahl et al.'s unknown inputs are **functions of time**, elements of an infinite-dimensional
function space. Their claim is a claim about the null space of an operator on that space:
where it is non-trivial it is infinite-dimensional, so non-invertibility collapses infinitely
many distinct inputs together and there is no meaningful notion of *how nearly* they are
distinguishable.

This project's distortion families are **finite-dimensional and parametric**: `η ∈ ℝ³`, and
`J` is a real `d × 3` matrix. The kernel of such a matrix has dimension `0`, `1`, `2`, or
`3`. **There is no room for an infinite-dimensional null space**, so the premise of the
dichotomy is unavailable, and the conclusion drawn from it does not transfer. This is not a
loophole; it is the difference between a functional inverse problem and a three-parameter
one.

### 3.2 "Nearly" is meaningful because the parameterisation is finite

With a finite parameterisation there are exactly three singular values, and `σ_3/σ_1` is a
**continuous** quantity taking every value in `[0,1]`. "Components 1 and 2 are nearly
confounded" is not vague: it names a specific direction `v ∈ ℝ³` and a specific pair of
coefficients `(v_1, v_2)`, both of which are estimable and reportable. In Kahl's setting
"nearly" has nothing to attach to, because the collapsed set is not indexed by finitely many
coefficients.

### 3.3 The decision problems are different, and this is the load-bearing point

Kahl et al. ask whether unknown inputs can be **reconstructed exactly** from outputs. That is
a deterministic inverse problem and it admits a clean yes/no: either the operator is
invertible or infinitely many inputs collide. Their dichotomy is *correct for that question*.

This project asks a different question: whether a **finite-precision statistical decision
among three named hypotheses** is achievable **at a stated simulation budget**. There,
"nearly" is not a degenerate notion — it is the entire content of the answer. The condition
number is not a softened version of invertibility; it is the exchange rate between
degeneracy and sample size, and §1.2 makes that exchange rate explicit: `n ≳ κ²`.

So both statements are true and they are about different things. Kahl et al.: *exact
recovery is impossible.* This project: *separation costs `κ²` draws, and here is `κ`.* A
paper that claimed to have softened Kahl's dichotomy would be wrong. A paper that reports the
statistical cost of near-degeneracy in a three-parameter family is not in contradiction with
it.

### 3.4 The concession — and it is a real one, not a hedge

**Where `J` is *exactly* rank-deficient, Kahl's dichotomy does import**, restricted to `ℝ³`.
If `η` enters the summaries only through a fixed linear combination, the null direction is
exact, no simulation budget recovers the components separately, and the equivalence class is
not a matter of cost but of identifiability. There is no graceful degradation in that case —
there is a wall — and D8's language of "graceful" reporting must not be applied to it.

**The consequence for how D8 must be implemented.** An equivalence class reported at
`κ = 50` and an equivalence class reported at exact rank deficiency are different claims and
must be labelled differently in the results file:

- **exactly degenerate** → *"these components are not identifiable from these summaries"* —
  a statement about identifiability, matching Kahl et al.;
- **near-degenerate at `κ`** → *"separating these components requires ~`κ²` replicates,
  which exceeds/does not exceed this study's budget"* — a statement about **affordability**,
  which is not an identifiability claim at all and must never be written as one.

Conflating the two is exactly the self-refuting error `LEDGER_DESIGN.md` D8 exists to
prevent, one level up.

### 3.5 Status of this argument

**Constructed, and I believe it holds** — §§3.1–3.3 are not close calls, since the
dimensional premise of Kahl's dichotomy simply is not met by a `d × 3` matrix. §3.4 is a
genuine restriction on D8 rather than a defence of it, and it is stated as such.

**What it is not.** It has **not** been checked against Kahl et al.'s formal statements
beyond the passage quoted, which is the passage G0 retrieved. It has not been reviewed by
anyone. And it inherits G0's unclosed gap: **Arendt, Apley & Chen (2012) remains
unretrieved**, and if that paper states a linear-independence condition on multiple responses,
§3 may need revisiting. Recorded in `OUTSTANDING.md` as O-6.

**Bearing on the current situation.** This section supports **R2**, which the Phase-2
refutation of R1 does not touch. If the operator takes option (b) of **Q-8** — promote R2
and the demonstration — then §3 is part of that paper's contribution and `S0_REPORT.md` §4
already says so. It is recorded here rather than deferred for that reason.
