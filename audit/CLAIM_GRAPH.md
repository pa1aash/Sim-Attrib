# Claim graph

> ## ⚠️ STATUS 2026-08-20 (session **G3**) — THIS FILE IS STILL STALE BELOW THIS BANNER
>
> **Third session in which this file has been flagged rather than rewritten.** Recorded as such
> rather than excused.
>
> What has changed since the G2 banner below was written:
>
> - **R2 has now been threat-checked** — `audit/R2_THREAT_CHECK.md`, verdict
>   **NARROW-CONDITIONAL** — and is carried as **cited infrastructure, not a claimed
>   contribution** (`docs/DECISIONS.md` **D-6**). The "R2 — Secondary. The noisy-rank estimator"
>   node below describes it as a contribution and is therefore **wrong as written**.
> - **Q-10 is answered and executed.** The G2 banner's instruction that "no claim structure
>   should be drawn until the operator answers it" is discharged.
> - **The live claim is now the composition** specified in `audit/MMC_COMPOSITION_SPEC.md`, which
>   appears nowhere below.
> - **R1 remains DEAD.** The "R1 — Primary" node below is historical.
>
> Do not read the dependency graph below as current. `DEVIATIONS.md` **D-7**.

> ## ⚠️ STATUS 2026-08-20 (session G2) — THIS FILE IS STALE BELOW THIS BANNER
>
> **R1 is DEAD** (G1, `audit/R1_THREAT_CHECK.md`) and the **composite-null successor claim is
> also DEAD** (G2, `audit/COMPOSITE_NULL_CHECK.md` — the repair is Dufour's maximized Monte
> Carlo, 2006). **R2 has still never been threat-checked.**
>
> The R1/R2 structure below was written in G1 and has **not** been rewritten, because G2's
> Phase 3 was not reached — Phase 1 returned DEAD and stopped the session. Do not read the
> dependency graph below as current. The live question is **Q-10**, and no claim structure
> should be drawn until the operator answers it. `DEVIATIONS.md` **D-7**.


**Rewritten 2026-08-20** for the reframe recorded in `docs/DECISIONS.md` **D-3**. The
paper's surviving claims are **R1** and **R2**. `C1` and `C2` are retired as *historical
labels*; the analysis that produced their verdicts is preserved verbatim below the fold,
because the reasoning trail is why R1 and R2 are what they are.

The purpose of this file is unchanged: no assertion can be quietly refuted without it
being immediately visible which claim goes with it.

Ledger entry codes refer to `LEDGER_ASSERTIONS.md`.

---

## The claims as they now stand

**R1 — Primary. The rejection-sampling mechanism.**
In simulation-based settings, exact conditional inference given a selection event requires
**no analytic characterisation of that event**. Under the null the simulator draws from the
exact null distribution, so the conditional law given a selection cell — e.g. {argmin = i} —
is obtained by **rejection sampling**: simulate, apply the selection rule, keep the draws
that land in the cell. This removes the obstruction that **Liu, Markovic-Voronov & Taylor
(2023)** identify as the central barrier to conditional selective inference in general. The
cost is compute, of order N_alt/α draws, which is a budget problem rather than an
identification problem.

**R2 — Secondary. The noisy-rank estimator.**
A simulation-based estimator of the summary Jacobian **J = ∂s/∂η**, together with a
defensible rule for calling **numerical rank from a noisy, sampled Jacobian**. Every source
G0 found assumes the map is symbolic or analytically differentiable. A simulator's Jacobian
is neither: it is estimated by finite differences from stochastic output, so its singular
values carry both discretisation error and simulation noise, and the rank call is a
statistical decision rather than a linear-algebra one.

**The demonstration.** Component-level misspecification attribution on a 3-component
simulator. This is what R1 is shown *on*. It is not the subject of the paper.

**The precondition, cited not claimed.** Per-component discrepancy attribution is
non-identifiable in general (data constrain only the sum) and becomes identifiable exactly
when the summary Jacobian has full column rank. This is **prior art** and is cited as such:
**Brynjarsdóttir & O'Hagan (2014)**, **Catchpole & Morgan (1997)**, **Kahl, Wendland,
Neidhardt, Weber & Kschischo (2019)**. It establishes when the demonstration's target
quantity is well-posed at all, and it is R2's reason for existing.

---

## Dependency structure

```
R1  (simulator-exact conditional calibration of the selection event)
 |
 ├── R1a  No prior work calibrates a selection event by drawing MORE           ── HARD, and
 |          simulator samples instead of characterising it analytically           the whole claim
 |          → tested in audit/R1_THREAT_CHECK.md (Phase 2, G1)
 ├── R1b  Ranking-and-selection / simulation-optimization does NOT already     ── HARD
 |          do this  (Kim & Nelson; Chick; Branke, Chick & Schmidt; IZ         ── the search
 |          and PCS procedures)                                                  G0 never ran
 ├── R1c  Randomized selective inference (Tian & Taylor) does not already      ── HARD
 |          contain the construction in non-simulator form
 ├── R1d  The rejection-sampling construction actually yields the EXACT        ── HARD (proof)
 |          conditional null — a theorem, not yet written
 ├── R1e  The construction beats the marginal procedure where they disagree    ── SOFT (empirical)
 └── R1f  Compute cost ~N_alt/α is affordable at the demonstration's scale     ── SOFT (budget)

R2  (numerical rank of a noisy, simulation-estimated Jacobian)
 |
 ├── R2a  Finite-difference J has an identifiable plateau in h — signal is     ── HARD
 |          separable from truncation error and simulation noise                 (G1, Phase 3)
 ├── R2b  A rank rule can be stated and defended BEFORE seeing results         ── HARD (D3 leakage)
 |          → docs/THRESHOLDS.md, written before any singular value exists
 ├── R2c  Near-degeneracy is MEANINGFUL in the finite-parametric case, i.e.    ── HARD
 |          Kahl et al.'s "no such thing as nearly invertible" does not import    → threatens D8
 ├── R2d  Rank is reported under a fixed, documented normalisation of both     ── HARD (validity)
 |          summaries and η — rank of J is not scale-invariant
 └── R2e  The impoverished control set S_C fails as predicted                  ── SOFT (validation)

Shared / inherited:
 ├── PRE   The rank condition itself (prior art, cited)                        → R2's subject,
 |                                                                                R1's precondition
 └── D8    Equivalence-class reporting where the rank condition fails          → depends on R2c
```

`HARD` = the claim does not survive in its stated form if this fails.
`SOFT` = the claim survives but is weakened, usually in scope or in evidence rather than
in truth.

---

## Failure propagation — what dies with what

| If this fails | Then |
|---|---|
| **R1a / R1b / R1c** (the mechanism is prior art) | **R1 is DEAD**, and with it the paper's headline. What remains is R2 plus a demonstration — a diagnostics paper, not a mechanism paper. This is the single highest-consequence open question in the project and is why Phase 2 of G1 exists. |
| **R1b** partially (R&S calibrates PCS by replication but not a *conditional* law) | **R1 NARROWS.** The claim becomes "conditional selective inference specifically", and the paper must position against R&S explicitly rather than ignore it — R&S delivers probability-of-correct-selection, which is the guarantee an applied reader assumes anyway. |
| **R1d** (the construction does not give the exact conditional null) | **R1 is DEAD as a theorem** and survives at best as a heuristic with empirical calibration — which is a different and much weaker paper. |
| **R1e** (no empirical advantage) | R1 survives as a correctness result with no demonstrated payoff. Publishable, but the demonstration section becomes an anticlimax. |
| **R2a** (no h-plateau) | **R2 is DEAD**, and so is the diagnostic. If the finite-difference Jacobian has no regime where truncation error and simulation noise are both small, its singular values are not estimating anything and no rank call is defensible. This is a real possibility and is checked first. |
| **R2c** (Kahl's dichotomy imports) | **D8 is ill-posed** and equivalence-class reporting must be withdrawn. R2 survives — a rank *test* is still meaningful — but the graceful-degradation story goes, and the diagnostic becomes binary. |
| **R2b** violated (thresholds fixed after seeing results) | **R2's numbers are inadmissible**, per `LEDGER_DESIGN.md` D3. Not a truth failure — a validity one, and unrecoverable after the fact. |
| **R2d** violated (undocumented normalisation) | Every singular value and every rank call in the paper is uninterpretable. Cheap to honour, impossible to repair. |
| **PRE** (the rank condition is wrong, not merely prior) | Vanishingly unlikely — it is a 1997 *iff* with a 1971 antecedent and a 2019 *PRX* restatement. If it happened, R2 has no subject. |

---

## The load-bearing observation, restated for the new structure

Under the old structure the danger was that C1 and C2 were **coupled** while the plan's
risk model treated them as independent. Under the new structure the danger is different
and sharper: **R1 and R2 are genuinely independent, and R1 carries almost all of the
weight.**

R2 is safe in the sense that matters — nobody disputes that a simulator's Jacobian must be
estimated rather than differentiated, and the estimator either works or produces an
interpretable negative result. But R2 alone is a diagnostics note. **R1 is the paper**, and
R1's entire defence is a **negative search result**: no prior work was found that does this.
G0 named that as the least secure conclusion in its own report, and it was tested against
nine conjunctive arXiv queries, OpenAlex, OpenReview, and a 2026 review — but **not**
against ranking-and-selection, which is the literature that has spent forty years
exploiting exactly the property R1 rests on: that in a simulation you can always draw more
samples.

That gap is R1b, and closing it is Phase 2 of G1. Until it is closed, every line of code
written on the assumption that R1 is novel is written at risk.

---

## Status

> **UPDATED 2026-08-20, after Phase 2.** R1a and R1c **FAILED**. R1b **passed**. The
> threat was not where this graph predicted: ranking-and-selection is clean (R1b SAFE),
> and the refutation came from selective inference itself — the literature G0 believed it
> had already cleared. `audit/R1_THREAT_CHECK.md`. R1 is **DEAD** as an original
> mechanism; the paper's structure is now an open operator question (**Q-8**).

| Node | Status |
|---|---|
| **R1a** — no prior work calibrates a selection event by drawing more samples | **FAILED.** Freidling, Zhao & Gao, arXiv:2405.07026, Algorithm 1 "Rejection sampling" |
| **R1b** — ranking-and-selection does not already do this | **PASSED.** R&S bounds analytically under normality (Slepian/Kimball/Bonferroni) and conditions on the parameter configuration, not the selection event. 0 hits for `"ranking and selection" AND "selective inference"` on arXiv full text |
| **R1c** — randomized selective inference does not contain it | **FAILED.** Tian & Taylor sample the conditional law, but only after polyhedral characterisation — so R1c is narrowly intact; it fails via Liu et al. (2023), Liu & Panigrahi (2025), and the Neufeld–Perry–Witten review, which together give three published routes past analytic characterisation |
| R1d | **NOT ATTEMPTED** — no proof written |
| R1e, R1f | **NOT ATTEMPTED** — no attributor implemented |
| R2a, R2b, R2d, R2e | **G1 Phase 3** — `docs/THRESHOLDS.md` and `results/jacobian_rank.*.yaml` |
| R2c | **G1 Phase 3.7** — written argument required before D8 is implemented |
| PRE | **VERIFIED as prior art** — G0, `S0_REPORT.md` §2 |

---
---

# HISTORICAL — the C1 / C2 claim graph as written before the reframe

**Preserved unedited.** This is the structure the project had when session G0 began, and
the verdicts recorded against it are what produced the R1 / R2 structure above. `C1`
survives, reframed, as the *demonstration*; its one genuinely novel component became `R1`.
`C2` is refuted as an original result and survives only as `PRE`, a cited precondition; its
residual — the noisy simulation-based estimator — became `R2`.

## (original file begins)

C1 and C2 as the plan states them, what each rests on, and **what falls when a
dependency falls**. The purpose is that no assertion can be quietly refuted without it
being immediately visible which claim goes with it.

Ledger entry codes refer to `LEDGER_ASSERTIONS.md`.

---

## The claims as stated

**C1 — Primary.** Component-level misspecification attribution is a multiple-selection
problem with correlated alternatives. Marginal distortion tests systematically
mis-attribute when component effects are correlated in summary space; a
competitive/conditional attribution with **error control over the selected component**
corrects this, and the mis-attribution rate of marginal testing is quantifiable as a
function of component collinearity.

**C2 — Secondary, described by the plan as "the real contribution".** Per-component
discrepancy attribution is non-identifiable in general, because the data constrain only
the sum; it becomes identifiable exactly when the summary Jacobian has full column rank.
Delivered as: a rank/coherence diagnostic, attribution restricted to the identifiable
subspace with equivalence-class reporting, and a calibrated null with control over the
selected component.

---

## Dependency structure

```
C1  (marginal → competitive, with selection error control)
 |
 ├── B3   Montel et al.'s tests are MARGINAL, not competitive       ── HARD
 ├── B4   Montel et al. have NO error control over the SELECTED     ── HARD
 |          component
 ├── C1b  RNPE's criticism step is per-SUMMARY, not per-COMPONENT   ── HARD
 ├── F1   Marginal tests mis-attribute under correlation            ── SOFT (novelty)
 ├── F2   Selective inference supplies a transferable guarantee     ── HARD (method)
 ├── F3   Mis-attribution rate is a function of collinearity        ── SOFT (figure)
 └── D2   Bayesian conflict diagnostics do NOT transfer to SBI      ── HARD (shared)

C2  (non-identifiability + rank condition)
 |
 ├── E1   Data constrain only the sum                               ── SOFT (near-definitional)
 ├── E2   Analogy to Kennedy & O'Hagan / Brynjarsdottir & O'Hagan   ── DOUBLE-EDGED
 |          / Tuo & Wu is apt
 ├── E3   The full-column-rank condition is NOVEL                   ── HARD, and the
 |          (vs. structural/practical identifiability: M1, M2)         most likely killer
 ├── E4   Diagnostic needs no real data                             ── SOFT
 └── D2   Bayesian conflict diagnostics do NOT transfer to SBI      ── HARD (shared)

Also bearing on both, and cited by neither:
 ├── M1/M2  structural & practical identifiability for ODE models   → threatens E3
 ├── M3     selective inference (knockoffs, e-BH, conditional SI)   → C1's method rests on it
 └── M4     global sensitivity analysis (Sobol, Morris)             → threatens the framing of both
```

`HARD` = the claim does not survive in its stated form if this fails.
`SOFT` = the claim survives but is weakened, usually in novelty rather than in truth.

---

## Failure propagation — what dies with what

| If this fails | Then |
|---|---|
| **B3** (their tests are competitive after all) | **C1 is DEAD.** The differentiator from the gatekeeper is gone entirely. No reframing rescues it; the paper becomes C2-only. → `PIVOT.md` |
| **B4** (they do have selection error control) | **C1 is DEAD.** Same as B3 — this is the second of the two differentiators and either one alone is sufficient to kill it. |
| **C1b** resolves as *per-component* | **C1 is DEAD or near-dead.** RNPE becomes a second gatekeeper and the component-vs-summary distinction, C1's fallback defence, evaporates. |
| **C1b** resolves as *per-summary* | C1 **narrows** as the plan anticipates. It must then be defended on the component-vs-summary distinction — which is only meaningful when summaries do not map one-to-one onto components, i.e. exactly the regime C2 characterises. **C1 becomes dependent on C2.** The plan presents them as independent; they are not. |
| **F2** (selective-inference guarantees do not transfer) | **C1 loses its method.** The negative half (marginal testing mis-attributes) survives as a critique, but a paper that diagnoses a problem without a working fix is a workshop note, not the primary claim. |
| **D2** (conflict diagnostics *do* transfer to SBI) | **Both C1 and C2 are damaged.** Node-level localisation with calibrated p-values in a likelihood-free setting is this project's stated contribution arriving from another literature. The plan treats this as a citation to acknowledge; it is a competitor. |
| **E3** (rank condition is a known result restated) | **C2 collapses to an application.** The identifiability *framing* survives — being first to state it for SBI discrepancy has some value — but "we restate the standard local identifiability criterion in SBI vocabulary" is not a NeurIPS-workshop contribution on its own. The paper would then need the diagnostic's *empirical* payoff to carry it: showing that a realistic simulator actually fails the condition. |
| **E1** (data constrain more than the sum) | Very unlikely. If it happened, C2's premise is wrong and the whole framing goes. |
| **F1, F3, E4** | Claims survive; contributions shrink. F3's failure specifically costs the headline figure. |

---

## The load-bearing observation

**C1 and C2 are not independent, and the plan's risk model assumes they are.**

The plan's fallback is: *if C1 dies, C2 carries a smaller paper.* That works only if C2
is unaffected by whatever killed C1. But:

- if C1b resolves per-summary, C1's remaining defence *routes through C2*;
- D2 is a shared dependency — a transferable conflict diagnostic damages both at once;
- E3 is C2's own most likely failure and is entirely untouched by C1's fate.

So the genuinely bad outcome is not "C1 dies". It is **D2 or E3 failing**, either of
which damages the fallback and the primary claim together. The single highest-value
question this session can answer is therefore not "is C1 novel" — the plan already
concedes that ground is narrow — but **E3: is the rank condition a new result or a
known one in new vocabulary?**

That is why the structural-identifiability check is treated as a first-class
investigation and not a footnote.

---

## Status

Every dependency in this graph is `UNVERIFIED` at the time of writing. Verdicts are
recorded in `S0_REPORT.md` §2 and the status changes propagate back into
`LEDGER_ASSERTIONS.md`.
