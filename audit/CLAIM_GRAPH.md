# Claim graph

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
