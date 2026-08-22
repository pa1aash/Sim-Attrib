# The final claim set

**Session G7, 2026-08-21.** This document supersedes every claim structure in `audit/` for the
purpose of drafting the paper. `audit/CLAIM_GRAPH.md` has been stale since G2 and stays as
history; `audit/PIVOT.md`, `audit/S0_REPORT.md` and the R1/R2 structure describe paths the
project no longer takes. **A drafting session works from this file.**

**Scope is closed by `docs/DECISIONS.md` D-16 (DECIDED, operator, start of G7).** Four
contributions, no MMC composition. No session may widen this without a new decision recorded
in `docs/DECISIONS.md`.

**Every number below is generated**, not typed: `results/FINAL_CLAIMS_NUMBERS.md`, produced by
`src/diagnostics/report_claims.py`, gives each one with the exact dotted path in the exact
`results/` file it comes from, and is reproduced verbatim in the appendix. Standing constraint
S11.

---

## The four claims, in one table

| | claim | kind | evidence | figure |
|---|---|---|---|---|
| **C1** | Using established diagnostic tools (rank/condition-number screening; maximized Monte Carlo), we find where component-level misspecification attribution is and is not identifiable for a canonical epidemic simulator under a realistic adversarial threat model, and give a quantitative, predictive account of why a natural selective-inference construction fails | empirical finding (case study) | `src/diagnostics/jacobian_rank.py`, `docs/THRESHOLDS.md`, `results/jacobian_rank.*.yaml`, `results/floor_check.yaml` | **Fig. 1**, **Fig. 2** |
| **C2** | `S_B` separates the simulator's three components under **all eight** component-wise family assignments the two declared sets permit | positive | `results/robustness/k6_spectrum.yaml`, `audit/K6_SPECTRUM_CHECK.md` | **Fig. 3**, **Fig. 4**, **Fig. 5** |
| **C3** | At two distortion parameters per component the same summary set is **inseparable**, and both near-null directions confound **progression with observation** | boundary | `results/robustness/k6_spectrum.yaml`, `audit/K6_SPECTRUM_CHECK.md` | **Fig. 3**, **Fig. 7** |
| **C4** | Rejection-sampling-based exact conditional inference **does not terminate** for this class of simulator once the nuisance parameters are unknown, and the width at which it stops is measured | cautionary | `results/p_sel.yaml`, `results/cost_gate.yaml`, `results/boundary_sweep.yaml`, `audit/MMC_COMPOSITION_SPEC.md` §4.1–4.2 | **Fig. 6** |

**C2 and C3 are one statement with two halves and must be written as one.** `docs/DECISIONS.md`
D-14 is explicit: a reader told C2 without C3 has been told something the evidence does not
support.

---

## C1 — the empirical finding, using established diagnostic tools

> ### ✅ RESOLVED 2026-08-21 — operator ruling on the tension flagged below (P-2)
>
> **C1 is not a method-novelty claim.** The rank/coherence diagnostic and its composition into
> a pre-inference gate are not claimed as a contribution: D-6 already forecloses the estimator
> and the rank rule, and the gating composition has never been threat-checked — and this
> project's track record (R1, C2-original, R2-standalone all died under threat-checking) means
> an untested novelty claim should not be introduced this late rather than checked in a ninth
> session. **The reconciled reading G7 wrote below — "what is offered is the composition into a
> decision procedure" — is superseded by this ruling.** What C1 claims instead is the **finding**
> produced by applying these established tools: where component-level misspecification
> attribution is and is not identifiable for this simulator under a realistic adversarial threat
> model (the `S_A`/`S_B` split of C2, the `K=6` confound of C3), plus a quantitative, predictive
> account of why a natural selective-inference construction fails (the nuisance-to-noise ratio
> of C4, predicted before the measurement that confirmed it). This is a strictly safer and
> equally real contribution, and requires no further novelty check before the paper is written.
> This makes the paper a **diagnostics-and-limits** paper — matching Sim2Science's CFP language
> on "simulator diagnostics" and "degeneracy, simplifications, and identifiability" — not a
> methods paper, and every section drafted from this file must reflect that framing.

### The claim, as it goes in the paper

> We apply established diagnostic tools — rank/condition-number screening on a simulation-based
> Jacobian (Cintrón-Arias et al. 2009; Moré & Wild 2010/2012) and maximized Monte Carlo (Dufour
> 2006) — as **cited infrastructure**, and report what they find. Declare the simulator as `K`
> components, give each one a one-parameter distortion family that is the base simulator exactly
> at zero, estimate the summary Jacobian `J = ∂s/∂η` at `η = 0` by central differences under
> common random numbers across an `h`-sweep, normalise summaries by their prior-predictive
> standard deviation and each `η_k` by a common relative scale, and call the numerical rank at a
> pre-registered tolerance together with the condition number against a pre-registered ceiling.
> Where the call fails, report the **equivalence class** of components the near-null right
> singular vectors name, rather than a component. **The contribution is not this procedure — it
> is what the procedure finds** when run against this simulator under an adversarial threat
> model, and the predictive account of where a natural selective-inference construction on top
> of it fails.

### The sentence about novelty, which is not optional

**Every ingredient is prior art and is cited as such.** The rank-and-condition-number screen on
a sensitivity matrix is **Cintrón-Arias, Banks, Capaldi & Lloyd (2009)**, worked on an epidemic
model. Finite differencing under simulation noise is **Moré & Wild (2010/2012)**, whose
near-optimal difference parameter is a stronger result than the `h`-sweep used here. The
identifiability condition itself — attribution is identifiable exactly where the summary
Jacobian has full column rank — is **Kahl, Wendland, Neidhardt, Weber & Kschischo (2019)** via
**Sain & Massey (1969)**, with **Catchpole & Morgan (1997)** and **Brynjarsdóttir & O'Hagan
(2014)**.

> ### ⚠️ SUPERSEDED 2026-08-21 — the tension below is resolved by the operator ruling at the top of C1
>
> **This callout is kept, not deleted, as the record of what P-2 actually asked and how G7 first
> tried to answer it.** G7 wrote the composition-into-a-decision-procedure reading below as a
> reconciliation between D-6 and D-16, and flagged that a session may not decide it was the right
> reading. **The operator has now decided it was not.** D-6 wins outright: neither the estimator,
> the rank rule, nor their composition into a gate is claimed as new. See the ✅ RESOLVED box at
> the top of this section for the reading that replaces the one below.
>
> **`docs/DECISIONS.md` D-6 forecloses claiming either the estimator or the rank rule as new**,
> in those words: *"'We contribute a simulation-based rank estimator' and 'we contribute a rule
> for calling numerical rank under noise' are both unavailable as contributions and must not
> reappear as such."*
>
> **`docs/DECISIONS.md` D-16 names "the rank/coherence diagnostic itself (method)" as the
> paper's first contribution.** *(Superseded reading, kept for the record:)* ~~These are
> reconcilable, and the claim above is written to satisfy both: what is offered is the
> **composition into a decision procedure applied before inference**, together with the
> pre-registration protocol and the equivalence-class output — not the estimator and not the
> rank rule.~~ **A session may not decide that this is the right reading. It was not.**
>
> D-6 also names the one seam it found unoccupied — carrying an estimated noise level forward
> into the rank tolerance — and requires that a paper claiming it must first re-derive `τ` from
> a noise level. **This project has not done that**, and `docs/THRESHOLDS.md` derives `τ` from
> a compute budget instead. So the seam must be **named and disclaimed** in the paper, not
> claimed — this still applies under the resolved reading, since the diagnostic is still used.

### What makes it a procedure rather than a calculation

Four conditions, each of which is a place where doing this carelessly gives a confident wrong
answer, and each of which this project either hit or came close to hitting:

1. **`δ_k(·;0)` must be the base simulator bit-for-bit**, or the Jacobian is the derivative of
   something that is not the model. Asserted in `tests/test_sir3.py` before anything else runs.
2. **Common random numbers are what make the difference quotient well posed at all.** The
   negative control is run and recorded: without CRN there is **no plateau**
   (`plateau.found = False`, one `h` value in the run), against a plateau spanning **all six**
   step sizes with CRN.
3. **Rank is not scale-invariant**, so both normalisations must be fixed in advance;
   `docs/THRESHOLDS.md` §0 fixes them before any singular value existed.
4. **A singular value the estimator has not resolved is counted toward the rank in neither
   direction**, so the reported rank may be an interval. The registered resolution factor is
   **2**; the worst variation across `S_B`'s plateau is **1.000114**.

### The controls, both of which are run and recorded

- **Positive control.** `S_C`, an impoverished two-summary set with `d = 2 < K = 3`, **cannot**
  have full column rank and does not: rank 2, `κ = ∞`, verdict *"rank deficient at tau"*, with
  an exact null direction reported. A diagnostic that passed `S_C` would be broken.
- **Random-attributor floor.** `1/K = 0.3333` analytically; **0.3299** as actually run over
  10,000 draws, inside four binomial standard errors. `PROVENANCE.md` requires every accuracy
  this project ever reports to be quoted against this floor.

### Scope and limits, to be stated with the claim

- The diagnostic is a statement about a **linearisation at one parameter point**. Every
  Jacobian in this repository is estimated about the same `θ₀`, and nothing here says what
  happens elsewhere.
- **Passing the resolution test does not answer the gapless-spectrum objection.** Resolution is
  a property of the *estimator*; spectral density is a property of the *matrix*. They are
  independent, and `audit/K6_SPECTRUM_CHECK.md` §2.4 records this project nominating the
  resolution test for a job it cannot do. **This correction must reach the paper**: it is the
  clearest instance of a safeguard pointed at the wrong quantity.
- **`τ` and `κ_max` are one threshold with two names at the registered pair**, because
  `κ_max` was *defined* as `1/τ`. Results files, `SUMMARY_TABLE.md` and the verdict string all
  present them as two checks. That reporting defect is open (`audit/G3_ADVERSARIAL_REVIEW.md`
  §1.4) and the paper must not present a conjunction of two independent checks passing when
  what passed was one check reported twice.

---

## C2 — the eight-assignment separability result

### The claim, as it goes in the paper

> **Under a distortion model that assigns one one-parameter family to each component, the
> three components of this simulator separate for `S_B` under every one of the eight
> assignments our two declared family sets permit.**

That is `docs/OPEN_QUESTIONS.md` Q-14 option (a), and `docs/DECISIONS.md` **D-14** makes it the
sentence the paper writes.

### The evidence

`κ` ranges from **6.628** (`BAB`) to **65.64** (`ABA`) against a registered ceiling of **100**.
All eight separable, every singular value resolved (worst variation factor **1.003883** against
an admissible 2), no coherence pair flagged, the leakage check passing on all eight. The two
declared sets sit inside that range: `BBB` at **10.12** and `AAA` at **64.62**. Six of the eight
assignments had never been tested before session G5.

**The contrast that makes it a measurement rather than a property of the instrument.** The same
sweep on `S_A`, a four-dimensional summary set, separates **4 of 8** — and the split is exactly
on the transmission family, with `ABB` failing at `κ = 100.9`, **0.9% past the ceiling**. An
instrument that always said "separable" could not produce that. `S_A` belongs in the paper as a
control and **not** as a result: it is dead as a generalising finding
(`audit/G3_ADVERSARIAL_REVIEW.md` finding 2).

### Scope conditions, all three of which are binding

1. **D-14: at most one one-parameter distortion family per component.** Outside that scope the
   project's own measurement is a counterexample — that is C3.
2. **Q-13 is open and blocking for this sentence.** The verdict is conditional on the two
   *family sets*, which are this project's own choices, and eight assignments drawn from two
   sets is not a sample of distortion families in general. G5 narrowed this materially; it did
   not close it. **`OUTSTANDING.md` O-21.**
3. **The threshold margin is not uniform and the smallest one is small.** The verdict survives
   `τ` moving by a factor of **9.881** under the base families but only **1.523** at the
   tightest assignment (`ABA`) — so **doubling `τ` flips it**, and the project's own proposed
   robustness grid, *"halve, double"*, straddles the boundary on the upper side. G4's sentence
   *"halving or doubling `τ` changes nothing"* is **false** under the adversarial families and
   must not be repeated.

### What must not be said

- Not *"component-level misspecification is identifiable"*. Refuted by this project's own
  `results/robustness/k6_spectrum.yaml` — C3.
- Not *"both summary sets are separable"* without the margin. `S_B`'s `κ = 10.12` passes the
  registered line with a factor of ten to spare and fails `docs/THRESHOLDS.md`'s own
  *"comfortable"* row **by 1.2%**. It is separable at the registered threshold and is **not
  comfortably separable**, and the distinction is the substance of the Gutenkunst objection even
  though the mechanism that objection names is absent at `K = 3`.
- Not anything resting on a single seed. Seed stability was checked in G4 across two further
  seeds; that is two, not many.

---

## C3 — the `K = 6` cross-mechanism confound

### The claim, as it goes in the paper

> **The same summary set is inseparable once a component carries two distortion parameters.**
> Placing all six declared distortion directions side by side — two per component — `S_B` is
> INSEPARABLE at `κ = 628.9`, rank **4 of 6**, and **both** near-null directions confound
> **progression with observation**. Stated as modelling rather than as linear algebra: *a
> drifting removal hazard is nearly indistinguishable from a constant hazard change combined
> with a drifting reporting rate.*

### Why none of the easy explanations survives

- **Not an unresolved estimator.** Worst variation factor across the `h`-plateau: **1.02254**,
  against an admissible **2**. The rank is *determined*: 4, not an interval.
- **Not a threshold artefact.** INSEPARABLE across `τ` from **0.005 to 1.0**, flipping only at
  `τ = 0.001` — a tenfold loosening at which `κ_max` rises to 1000 while the measured `κ` is
  628.9. On `docs/THRESHOLDS.md` §1.2's own pricing table separation would then cost `κ² ≈ 4×10⁵`
  replicates. **There is no tolerance at which the six-column object is both separable and
  cheap.**
- **Not structural.** `d = 10 ≥ 6`, so no singular value is zero by construction:
  `n_structurally_zero = 0`.

### What is confounded, and why it is the right shape for a scope restriction

| direction | `σ` | `σ/σ₁` | kind | transmission energy |
|---|---|---|---|---|
| `v₅` | 0.625 | 0.009173 | cross-mechanism | 0.04297 |
| `v₆` | 0.1083 | 0.00159 | cross-mechanism | 0.04463 |

Both name **progression and observation**; transmission carries under 5% of the energy in
either. **The confound requires the progression component to carry two distortion parameters at
once**, and a one-parameter family cannot supply that — which is exactly why it does not reach
any three-column model the declared families permit, and exactly why D-14's restriction is
stated as *one parameter per component* rather than as a bound on `κ`.

This is not a contrivance. `docs/OPEN_QUESTIONS.md` **Q-12 predicted it in prose before any of
these numbers existed**, and it is an epidemiological commonplace.

### The objection this result concedes

At `K = 6` the Gutenkunst picture describes `S_B` well: the spectrum spans **2.799 decades**,
its gap prominence is **1.402** — decay close to geometric with no break anywhere — and `τ·σ₁`
falls *inside* it, between `σ₄` and `σ₅`. **The reassurance that `τ` sits an order of magnitude
below everything is a fact about `K = 3`, not about the simulator.** The paper should say so.

---

## C4 — the MMC non-termination result

### The claim, as it goes in the paper

> **Naive rejection-sampling-based exact conditional inference does not terminate for this
> class of simulator once the nuisance parameters are unknown, and the failure is structural
> rather than budgetary.** At a known parameter point the composition is comfortably
> affordable. Over any nuisance set a domain reader would accept, the observed selection cell
> becomes unreachable and the cost is unbounded rather than large.

### The two halves, and the second is the finding

| | | |
|---|---|---|
| **At `θ₀`** | worst selection cell holds **0.2346** of null draws (95% CI 0.232–0.2372) | one test costs **4.22×10⁵ – 4.26×10⁷** draws against a pre-registered gate of **10⁸**: **PASS** |
| **Over the nuisance set** | **0 acceptances in 100,000 draws**, 95% upper bound **3.841×10⁻⁵** | cost at least **2.577×10⁹** draws at the cheapest declared `(M, N)` and **2.601×10¹¹** at the dearest: **FAIL**, with `ci_decides_the_gate = True` |

3,782,038 null draws. The gate was registered in `audit/MMC_COMPOSITION_SPEC.md` §4 in session
G3, before `p_sel` existed.

### The mechanism, measured rather than argued — and this is the transportable part

The composition's only theorem (§3.4) requires the selection rule to be a **fixed function of
the data**: one event applied to the observation and to every replicate. So the rule cannot see
`θ`. Meanwhile the nuisance parameters move the normalised summaries by far more than the
observation noise does. The single-draw noise magnitude is `√d = 3.162` by construction; the
median nuisance shift crosses it between `w = 0.005` (**0.7707**) and `w = 0.0075` (**1.146**).

> **A `θ`-free rule facing a shift larger than the noise selects one component
> deterministically, and the cell the data actually selected becomes impossible to sample.**

That is §3.4's own named failure case — *"the rejection sampler never terminates there"* — with
a number instead of a warning. **And the crossing is where the gate stops passing**, which makes
the shift-to-noise ratio a one-line check anybody holding a different simulator can run before
attempting this composition on it.

### Where the boundary is, and what shape the collapse has

`results/boundary_sweep.yaml`, session G7: ten half-widths from 0.001 to 0.05, **7,602,000**
null draws, run **after** D-16 had already dropped the composition, so it characterises a closed
question rather than reopening one.

- The collapse is **GRADUAL** under the pre-registered criterion — largest local log-slope
  **2.265×** the median, against a declared threshold of 3 — and close to exponential in the
  distortion magnitude: **−141.2 decades per unit relative half-width**, `R² = 0.9424`. **About
  one decade of acceptance probability per 0.7% of relative nuisance error.**
- **The gate passes at every declared corner only inside a ±0.5% box** on all five nuisance
  coordinates at once. `docs/OPEN_QUESTIONS.md` Q-16 guessed ±0.4% and called such a bound *"no
  epidemiologist will accept"*. The guess was close and the judgement stands.
- At ±5%, **21 of 42** design points have a cell no draw ever enters.

### What the paper may and may not do with this

- **May** report it as a finding about a class of simulators, stated through the
  nuisance-to-noise ratio, which is the property that transports.
- **May not** describe it as "future work pending more compute". The obstruction is not compute
  and saying so would misstate this project's own measurement.
- **May not** present a scaled-down version of the experiment. §4's own words: on a failed gate
  *"the honest output is the cost analysis itself, not a scaled-down experiment that hides it."*
- **Must** disclose that `p_sel` is a property of the composition **and of the selection rule
  `T_k`**, which §6 left *"not specified"* and which session G6 had to choose in order to
  measure anything. `DEVIATIONS.md` **D-14**. A different `T_k` gives a different number.
- **Must** disclose that `Ω₀` is not specified anywhere in this project; a relative box on the
  five coordinates §1 names is a stand-in, and **a grid understates a minimum**, so every cost
  reported is a lower bound.

---

## What none of the four claims rests on, and what is still open

**Not verified by anyone outside this project.** No independent review has ever been run — not
of the diagnostic, not of the numbers, not of the composition. `OUTSTANDING.md` **O-17**'s older
half is partly paid by measurement and entirely unpaid as criticism. `GATES.md` records this at
every gate and it does not improve by repetition.

**Open and blocking for the paper's separability sentence: Q-13** (**O-21**), the
family-conditionality of C2.

**Open and non-blocking:** Q-15 / **O-26**, the intermediate `K = 4` and `K = 5` cases, which
are constructible from columns already recorded and would say whether the confound needs all six
columns or only four. **O-22**, `results/` still carrying G3's vacuous `leakage_checked`
literal. **O-7**, Google Scholar never searched, in eight sessions. And no literature check has
ever been run on the non-termination finding itself, which is not an exotic phenomenon and which
somebody has very likely written about.

**One requirement that must survive to the drafting session**, restated because D-14 lists four
places the obligation lands and `paper/main.tex` is the one that does not yet exist:
**the single-mechanism restriction goes in the scope or limitations section, and the six-column
counterexample is stated rather than omitted.**

---

## Appendix — the generated numbers, reproduced verbatim

**From `results/FINAL_CLAIMS_NUMBERS.md`, generated by `src/diagnostics/report_claims.py`.**
Every number in the prose above is a row below, and no number in this document was typed by
hand. Headings are demoted by one level; nothing else is altered.

the 'source' column. Do not edit. Standing constraint S11. -->

#### Every load-bearing number in `audit/FINAL_CLAIMS.md`, and where it comes from

One row per number the paper's four claims rest on. The **path** column is the exact dotted path in the named file, so a reader can check any row without running anything.


##### C1 — the rank and coherence diagnostic (method)

| quantity | value | source | path |
|---|---|---|---|
| rank tolerance τ, pre-registered | `0.01` | `results/jacobian_rank.S_B.yaml` | `thresholds_pre_registered.tau_rank_tolerance` |
| condition-number ceiling κ_max, pre-registered | `100` | `results/jacobian_rank.S_B.yaml` | `thresholds_pre_registered.kappa_max` |
| resolution factor (h-plateau), pre-registered | `2` | `results/jacobian_rank.S_B.yaml` | `thresholds_pre_registered.resolve_factor` |
| plateau relative tolerance | `0.05` | `results/jacobian_rank.S_B.yaml` | `thresholds_pre_registered.plateau_rel_tol.value` |
| equivalence-class loading threshold v_k,min | `0.3` | `results/jacobian_rank.S_B.yaml` | `thresholds_pre_registered.vk_min_equivalence_class` |
| coherence flag threshold | `0.98` | `results/jacobian_rank.S_B.yaml` | `thresholds_pre_registered.coherence_flag` |
| invisible-component column-norm threshold | `0.1` | `results/jacobian_rank.S_B.yaml` | `thresholds_pre_registered.colnorm_invisible` |
| step sizes swept (decades) | `6` | `results/jacobian_rank.S_B.yaml` | `thresholds_pre_registered.h_values` |
| S_B: plateau found across the whole sweep | `6` | `results/jacobian_rank.S_B.yaml` | `results.plateau.n_h_in_plateau` |
| S_B: largest singular-value variation factor across the plateau | `1.000114` | `results/jacobian_rank.S_B.yaml` | `results.singular_value_variation_factor` |
| NEGATIVE CONTROL, no CRN: plateau found? | `False` | `results/jacobian_rank.S_A.no_crn_control.yaml` | `results.plateau.found` |
| NEGATIVE CONTROL, no CRN: h values inside the plateau | `1` | `results/jacobian_rank.S_A.no_crn_control.yaml` | `results.plateau.n_h_in_plateau` |
| POSITIVE CONTROL S_C (d = 2 < K): rank at τ | `2` | `results/jacobian_rank.S_C.yaml` | `results.numerical_rank.rank_certain` |
| POSITIVE CONTROL S_C: condition number | `∞` | `results/jacobian_rank.S_C.yaml` | `results.condition_number` |
| POSITIVE CONTROL S_C: verdict | `rank deficient at tau` | `results/jacobian_rank.S_C.yaml` | `results.inseparable_reason` |
| random-attributor floor 1/K, analytic | `0.3333` | `results/floor_check.yaml` | `floor_check.floor_analytic` |
| random-attributor floor, as run | `0.3299` | `results/floor_check.yaml` | `floor_check.accuracy_simulated` |
| floor check passes | `True` | `results/floor_check.yaml` | `floor_check.passes` |

##### C2 — the eight-assignment separability result for `S_B` (positive)

| quantity | value | source | path |
|---|---|---|---|
| S_B, number of family assignments tested | `8` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.mixed_triples` |
| S_B, number separable | `8` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.mixed_triples` |
| S_B, smallest κ over the eight (BAB) | `6.628` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.mixed_triples` |
| S_B, largest κ over the eight (ABA) | `65.64` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.mixed_triples` |
| S_B, κ under the declared base set BBB | `10.12` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.base.condition_number` |
| S_B, κ under the declared adversarial set AAA | `64.62` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.adversarial.condition_number` |
| S_B, worst singular-value variation factor over the eight | `1.003883` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.mixed_triples` |
| S_B, leakage check passes on all eight | `True` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.mixed_triples` |
| S_B, smallest τ* margin over the eight (× registered τ) | `1.523` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.mixed_triples` |
| S_B base, τ* margin (× registered τ) | `9.881` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.base.tau_sensitivity.exact_flip_point.as_multiple_of_registered_tau` |
| CONTRAST S_A, number separable of eight | `4` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_A.mixed_triples` |
| CONTRAST S_A, κ at its knife-edge failure ABB | `100.9` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_A.mixed_triples.ABB.condition_number` |
| replicates per Jacobian column R | `128` | `results/robustness/k6_spectrum.yaml` | `settings.R` |
| replicates for the normalisation R_norm | `2,000` | `results/robustness/k6_spectrum.yaml` | `settings.R_norm` |

##### C3 — the `K = 6` cross-mechanism confound (boundary)

| quantity | value | source | path |
|---|---|---|---|
| S_B six-column κ | `628.9` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.condition_number` |
| S_B six-column rank at τ | `4` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.numerical_rank.rank_certain` |
| S_B six-column columns | `6` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.n_columns` |
| S_B six-column spectrum spread (decades) | `2.799` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.spectrum.spread_decades_over_positive_singular_values` |
| S_B six-column gap prominence (largest ÷ median adjacent ratio) | `1.402` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.spectrum.gap_prominence_largest_over_median_adjacent_ratio` |
| S_B six-column: where τ·σ₁ sits | `inside the spectrum, between sigma_4 and sigma_5` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.spectrum.where_tau_sigma1_sits` |
| S_B six-column structurally zero singular values | `0` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.spectrum.n_structurally_zero` |
| S_B six-column worst variation factor (estimator resolved?) | `1.02254` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.singular_value_variation_factor` |
| S_B six-column INSEPARABLE stable over τ from | `0.005` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.tau_sensitivity.coupled_stability.stable_over_tau_range[0]` |
| S_B six-column INSEPARABLE stable over τ to | `1` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.tau_sensitivity.coupled_stability.stable_over_tau_range[1]` |
| S_B six-column flips to separable only at τ | `0.001` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.tau_sensitivity.coupled_stability.flips_at_next_tau_below` |
| near-null direction 1: σ | `0.625` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.near_null_directions[0].singular_value` |
| near-null direction 1: σ/σ₁ | `0.009173` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.near_null_directions[0].sigma_ratio_to_sigma1` |
| near-null direction 1: kind | `cross-mechanism` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.near_null_classification[0].kind` |
| near-null direction 1: transmission energy | `0.04297` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.near_null_classification[0].mechanism_energy.transmission` |
| near-null direction 2: σ | `0.1083` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.near_null_directions[1].singular_value` |
| near-null direction 2: σ/σ₁ | `0.00159` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.near_null_directions[1].sigma_ratio_to_sigma1` |
| near-null direction 2: kind | `cross-mechanism` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.near_null_classification[1].kind` |
| near-null direction 2: transmission energy | `0.04463` | `results/robustness/k6_spectrum.yaml` | `summary_sets.S_B.six_columns.near_null_classification[1].mechanism_energy.transmission` |

##### C4 — the MMC non-termination result (cautionary)

| quantity | value | source | path |
|---|---|---|---|
| null draws taken to measure p_sel | `3,782,038` | `results/p_sel.yaml` | `settings.n_simulator_runs` |
| p_sel at θ₀, worst cell, AAA studentised | `0.2346` | `results/p_sel.yaml` | `stage_A_theta0.AAA\|studentised.p_sel` |
| p_sel at θ₀, 95% CI lower | `0.232` | `results/p_sel.yaml` | `stage_A_theta0.AAA\|studentised.ci95_lower` |
| p_sel at θ₀, 95% CI upper | `0.2372` | `results/p_sel.yaml` | `stage_A_theta0.AAA\|studentised.ci95_upper` |
| cost at θ₀, cheapest declared (M, N) | `4.220e+05` | `results/cost_gate.yaml` | `cost_floor_theta_known.AAA\|studentised.corners[0].expected_draws` |
| cost at θ₀, dearest declared (M, N) | `4.259e+07` | `results/cost_gate.yaml` | `cost_floor_theta_known.AAA\|studentised.corners[3].expected_draws` |
| pre-registered gate, simulator draws | `1.000e+08` | `results/cost_gate.yaml` | `gate.threshold_draws` |
| HEADLINE p_sel over the nuisance box | `0` | `results/cost_gate.yaml` | `headline.p_sel` |
| HEADLINE 95% upper bound on p_sel | `3.841e-05` | `results/cost_gate.yaml` | `headline.p_sel_ci95[1]` |
| HEADLINE verdict | `FAIL` | `results/cost_gate.yaml` | `headline.verdict` |
| the confidence interval decides the gate | `True` | `results/cost_gate.yaml` | `headline.ci_decides_the_gate` |
| cost floor at the CI upper bound, cheapest corner | `2.577e+09` | `results/cost_gate.yaml` | `headline.expected_draws_ci95_lower_range[0]` |
| cost floor at the CI upper bound, dearest corner | `2.601e+11` | `results/cost_gate.yaml` | `headline.expected_draws_ci95_lower_range[1]` |
| boundary sweep: null draws | `7,602,000` | `results/boundary_sweep.yaml` | `settings.n_simulator_runs` |
| boundary sweep: shape of the collapse (primary) | `GRADUAL` | `results/boundary_sweep.yaml` | `shape_of_the_collapse.AAA\|studentised.shape` |
| boundary sweep: slope ratio against a threshold of 3 | `2.265` | `results/boundary_sweep.yaml` | `shape_of_the_collapse.AAA\|studentised.slope_ratio` |
| boundary sweep: decades of p per unit half-width | `-141.2` | `results/boundary_sweep.yaml` | `shape_of_the_collapse.AAA\|studentised.loglinear_fit.slope_b_decades_per_unit_half_width` |
| boundary sweep: R² of that fit (descriptive) | `0.9424` | `results/boundary_sweep.yaml` | `shape_of_the_collapse.AAA\|studentised.loglinear_fit.r_squared` |
| median ‖E[z]‖ ÷ √d at w = 0.005 | `0.7707` | `results/boundary_sweep.yaml` | `per_width[3].nuisance_shift_norm_of_mean_z.median_over_noise` |
| median ‖E[z]‖ ÷ √d at w = 0.0075 | `1.146` | `results/boundary_sweep.yaml` | `per_width[4].nuisance_shift_norm_of_mean_z.median_over_noise` |
| single-draw noise magnitude √d | `3.162` | `results/boundary_sweep.yaml` | `per_width[0].nuisance_shift_norm_of_mean_z.single_draw_noise_magnitude_sqrt_d` |
| design points with a dead cell at w = 0.05 (of 42) | `21` | `results/boundary_sweep.yaml` | `per_width[9].by_key.AAA\|studentised.n_design_points_with_a_dead_cell` |
| θ₀ reproduction: maximum two-proportion \|z\| | `1.958` | `results/boundary_sweep.yaml` | `checks.theta0_max_abs_z` |
| θ₀ reproduction: threshold | `3` | `results/boundary_sweep.yaml` | `checks.theta0_z_threshold` |

**Provenance of the source files.**

| file | script | commit | dirty | seed |
|---|---|---|---|---|
| `results/boundary_sweep.yaml` | `src/diagnostics/boundary_sweep.py` | `792b7dc` | `False` | `20260821` |
| `results/cost_gate.yaml` | `src/diagnostics/cost_gate.py` | `5ba0623` | `False` | `20260820` |
| `results/floor_check.yaml` | `src/diagnostics/floor_check.py` | `570692c` | `False` | `20260820` |
| `results/jacobian_rank.S_A.no_crn_control.yaml` | `src/diagnostics/run_diagnostic.py` | `570692c` | `False` | `20260820` |
| `results/jacobian_rank.S_B.yaml` | `src/diagnostics/run_diagnostic.py` | `570692c` | `False` | `20260820` |
| `results/jacobian_rank.S_C.yaml` | `src/diagnostics/run_diagnostic.py` | `570692c` | `False` | `20260820` |
| `results/p_sel.yaml` | `src/diagnostics/p_sel.py` | `5ba0623` | `False` | `20260820` |
| `results/robustness/k6_spectrum.yaml` | `src/diagnostics/k6_spectrum.py` | `2efb4ae` | `False` | `20260820` |
