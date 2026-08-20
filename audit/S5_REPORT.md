# S5 — Session G5 report

**For a reader who has not seen this session.** Written 2026-08-20.

> ## WHICH OF THE THREE OUTCOMES THIS SESSION REACHED
>
> The brief named three. **This is (a): Phase 1 stopped the session — but not for the reason
> (a) anticipated, and the difference is the whole report.**
>
> (a) was written for *"`S_B`'s separability overturned at `K = 6`"*. What happened is a split:
>
> - **`S_B` separates under all eight component-wise family assignments** the two declared
>   distortion family sets permit — `κ` from **6.628** to **65.64**, every singular value
>   resolved. **Six of those eight had never been tested.** This is the strongest evidence this
>   project has ever produced for the precondition its whole method rests on.
> - **`S_B` does not separate when a component may carry two distortion parameters at once.**
>   The six-column union is **INSEPARABLE at `κ = 628.9`**, rank 4 of 6, and the confound is
>   **progression against observation** — two different components, not two deformations of one.
>
> **The verdict is WEAKENED. WEAKENED is not a clean pass, and the brief permits continuation
> only in the absence of "any verdict other than a clean pass". So the session halted.**
> `p_sel` was not measured, `results/cost_gate.yaml` does not exist, and no line of the MMC
> composition was written.
>
> **One thing to read with suspicion.** A rule this session committed *before* the run said that
> a cross-mechanism six-column confound overturns the three-column result. It fired. A
> measurement taken afterwards — the eight assignments — shows that implication was too strong.
> The refinement is in the project's favour and was made after seeing the data. It is disclosed
> at the top of `audit/K6_SPECTRUM_CHECK.md`, in `DEVIATIONS.md` **D-13**, and in G5's "does not
> certify" section, and **it bought the session nothing: the halt happened anyway.**

---

## 1. WHAT THIS SESSION DID

| Path | Status |
|---|---|
| `audit/K6_SPECTRUM_CHECK.md` | **new** — Phase 1 in full. Verdict at the top, three sub-verdicts, the pre-registered-rule disclosure first |
| `results/robustness/k6_spectrum.yaml` | **new numbers** — three summary sets × (base `K=3`, adversarial `K=3`, union `K=6`, eight mixed triples), each with the h-plateau, resolution test, equivalence classes, leakage check, nine-point `τ` sweep under two couplings, and a 108-point `(τ, κ_max)` grid. Plus the normalised columns at every step size, so the next session can re-analyse without re-simulating |
| `results/robustness/K6_TABLE.md` | **new** — generated from the YAML; the audit document quotes it verbatim |
| `src/diagnostics/k6_spectrum.py` | **new** — the K = 6 check, with a parallel column estimator proved bit-identical to `estimate_jacobian` |
| `src/diagnostics/report_k6.py` | **new** — the table generator, so no number is hand-typed |
| `src/runlock.py` | **new** — the S3 liveness check, rebuilt after G4's reported a live run as dead |
| `tests/` | **84 → 109 tests**, of which eight require a check to fail or a bad input to be rejected |
| `GATES.md` | **G0–G4 signed** per the operator; **G5 added**, unsigned |
| `docs/DECISIONS.md` | **D-11** (visibility ruled on, not pending); **D-12** (two paths, PROPOSED not decided) |
| `docs/OPEN_QUESTIONS.md` | **Q-14** raised (blocking); **Q-15** raised (not blocking); **Q-13 narrowed**, not closed |
| `DEVIATIONS.md` | **D-12** (the brief asked for two six-column spectra; one exists), **D-13** (the pre-registered implication) |
| `OUTSTANDING.md` | visibility banner corrected to the operator's ruling; **O-20 closed** |
| `results/`, `docs/THRESHOLDS.md` | **untouched.** No threshold revised, no G3 or G4 number overwritten |

---

## 2. PHASE 1 — THE FAVOURABLE HALF, REPORTED FIRST BECAUSE S10 CUTS BOTH WAYS

A distortion family set assigns **one** family to each component. The two sets this project has
declared are the two corners: base everywhere, adversarial everywhere. **Between them sit six
further assignments**, each a perfectly ordinary three-column distortion model of the same
simulator that an analyst could equally have declared — and none had been measured.

They cost nothing: every column was already estimated for the six-column object, so all eight
run at no additional simulator cost, and **no new distortion family was invented** (which
matters, because inventing one now would be `DEVIATIONS.md` D-9's problem again).

| `S_B` | `BBB`* | `BBA` | `BAB` | `BAA` | `ABB` | `ABA` | `AAB` | `AAA`* |
|---|---|---|---|---|---|---|---|---|
| `κ` | 10.12 | 30.98 | **6.628** | 27.40 | 25.64 | **65.64** | 20.76 | 64.62 |
| verdict | sep. | sep. | sep. | sep. | sep. | sep. | sep. | sep. |

**All eight separable. Every singular value resolved. No coherence pair flagged. The
permutation leakage check passes on all eight.** `BBB` and `AAA` reproduce the recorded
`κ = 10.12` and `κ = 64.62` exactly, so their agreement is a check on the assembly rather than
a repetition of it.

**What this does to Q-13.** G4 raised Q-13 because the verdict was conditional on *"three
specific distortion families"*, measured at two points. It is now measured at every point the
declared families permit, and does not move. Q-13's own option (b) — *"run the diagnostic
across a designed set of family triples and report the distribution of verdicts"* — is
**executed for the closed set the declared families allow, and the distribution is degenerate:
eight separable, none otherwise.** That narrows the condition from "these three families" to
"these two family sets in any component-wise combination". It does not remove it: eight points
drawn from two sets, one of which was built to fail, is not a sample of distortion families.

### 2.1 It also sharpens a G4 sentence, in the unfavourable direction

`S_A` is dead as a generalising result and this does not revive it — but the same sweep
corrects the account of why. **The split is exactly on the transmission family:** all four
assignments with the base transmission family separate (`κ` 5.186–9.531); all four with the
adversarial one do not (`κ` 100.9, 123.3, 136.7, 875.2). G4 read `S_A`'s failure as working
*"through its third family rather than its first two"*. **Changing only the transmission
family — `ABB` — already breaks `S_A`**, at `κ = 100.9`, which is **0.9% past the ceiling** and
the closest to a threshold this project has measured anything.

---

## 3. PHASE 1 — THE UNFAVOURABLE HALF, AND WHY THE EASY EXPLANATIONS DO NOT SURVIVE

Place all six declared distortion directions side by side — two per component — and `S_B` is
**INSEPARABLE**.

| | `K = 3` base | `K = 3` adversarial | `K = 6` union |
|---|---|---|---|
| spread (decades) | 1.01 | 1.81 | **2.80** |
| gap prominence | 1.48 | 1.65 | **1.40** |
| where `τ·σ₁` sits | below the whole spectrum | below the whole spectrum | **inside, between `σ₄` and `σ₅`** |
| rank at `τ` | 3/3 | 3/3 | **4/6** |
| `κ` | 10.12 | 64.62 | **628.9** |

**Not an unresolved estimator.** All six singular values are **resolved** — largest variation
factor across the h-plateau **1.023**, against the pre-registered factor of 2 — so the rank is
determined, not an interval. This is the addition that matters: G4's six-column number came
from a **single step size**, and this project's own `docs/THRESHOLDS.md` §1.4 says *"a rank
computed at a single step size `h` is not a result"*. It now has the plateau, the resolution
test, the equivalence-class stability requirement and a 719-permutation leakage check, and it
survives all four.

**Not a threshold artefact.** INSEPARABLE across `τ` from **0.005 to 1.0**. It flips only at
`τ ≤ 0.001` — a tenfold loosening — and at that setting `κ_max` becomes 1000 against a measured
`κ` of 628.9, which on `docs/THRESHOLDS.md` §1.2's own pricing table costs `κ² ≈ 4×10⁵`
replicates to separate. **There is no tolerance at which the six-column object is both
separable and affordable.**

**Not structural.** `d = 10 ≥ 6`, so no singular value is zero by construction.

**What is confounded, in words.** Both near-null directions place their weight on
`base:progression`, `adversarial:progression` and `adversarial:observation` together, stable to
three decimal places across the whole plateau, with no borderline members. **A drifting removal
hazard is nearly indistinguishable from a constant hazard change combined with a drifting
reporting rate.** That is not a contrivance — it is the confound `docs/OPEN_QUESTIONS.md`
**Q-12** predicted in prose before any of these numbers existed. It is also exactly why it does
not reach a three-column model: it needs one component to carry two distortion parameters at
once, and a one-parameter family cannot.

### 3.1 The gapless objection, and a safeguard that was pointed at the wrong quantity

`audit/R2_THREAT_CHECK.md` §1.3 records the sharpest objection to the whole diagnostic:
Gutenkunst et al. (2007) find spectra *"spread roughly uniformly over many decades, with no
gap"*, in which case a rank at tolerance `τ` reports where the analyst put `τ`. **At `K = 6`
that picture describes `S_B` well** — 2.80 decades, gap prominence 1.40 (a near-geometric decay
with no break anywhere), `τ·σ₁` inside the spectrum. G4's reassurance is confirmed as a fact
about `K = 3`.

**And the safeguard nominated to catch this did not fire.** `R2_THREAT_CHECK.md` §1.3 proposed
that a gapless spectrum *"should surface"* in the resolution test. It did not: all six values
are resolved to within 2.3%. **The resolution test measures whether the estimator has
converged; spectral density is a property of the matrix.** A dense spectrum estimated perfectly
passes it. This is not a vacuous flag — it can and does fail on unconverged estimates — but it
is a safeguard aimed at the wrong quantity, and that sentence should not be relied on again.

### 3.2 The `κ_max` branch — resolved, not deferred a second time

G4 named this and left it. The closed form: with every singular value resolved, the `κ` branch
fires **alone** exactly on `κ_max < κ ≤ 1/τ`, which is **empty whenever `κ_max ≥ 1/τ`** — and
the registered pair sets `κ_max = 1/τ` precisely, so it is unreachable there for any `κ`
whatsoever. The verdict was recomputed through the production `analyse()` at 108 `(τ, κ_max)`
points per spectrum and **every row agrees with the closed form**; the checker is fed a grid
with the ceiling comparison inverted and a grid with the rank rule on the wrong singular value
and is required to catch both, so agreement is a measurement rather than a tautology.

Concretely reachable for the first time in this project: `S_B`'s six-column spectrum at
`κ_max = 100` and `τ ∈ {10⁻⁴, 10⁻³}` has **full column rank 6/6** and is INSEPARABLE **on the
condition-number criterion alone**.

### 3.3 One correction to a G4 sentence about tolerance

G4 wrote *"Halving or doubling `τ` changes nothing for either `S_A` or `S_B`."* True of the base
families. **False for `S_B` under the adversarial ones: doubling `τ` flips it to INSEPARABLE**,
because the flip point is 1.547× the registered value. The worst of the eight assignments,
`ABA`, is tighter still at 1.523×. **The project's own halve/double grid straddles the boundary
on the upper side.**

---

## 4. WHY THE SESSION STOPPED, AND WHAT IT DID NOT DO

The brief's continuation rule: *"The stop conditions below (any verdict other than a clean
pass) are the only reasons to halt before Phase 3 begins."* **WEAKENED is not a clean pass.**

So, not done, deliberately:

- **`p_sel` not measured. `results/cost_gate.yaml` does not exist.** Sixth session without the
  one number that decides affordability. **Q-14 explicitly does not block it** — the halt is a
  consequence of the stop rule, not of the finding.
- **No MMC composition.** Not a line. **O-17** — nobody has ever attacked it — is unpaid for
  the sixth session, and the composition remains unimplemented as well as unrefuted.
- **No `paper/main.tex`**, under any branch.
- **No threshold revised, no `results/` file overwritten.**

**The judgement that is worth arguing with.** The verdict could have been written OVERTURNED,
honouring the letter of the rule this session committed before the run. It is written WEAKENED,
because all eight three-column assignments separate and the confound needs a distortion space
no declarable model reaches. **The stop happened either way**, which is the only reason the
refinement is not load-bearing — had it unlocked Phases 2 and 3, it would be indistinguishable
from the failure it is disclosed to guard against. `DEVIATIONS.md` **D-13**; the operator may
take the other reading, and **P-2** is where.

---

## 5. THE SIX-SESSION TRAJECTORY

Extending `audit/S4_REPORT.md` §6.

| Session | Claim adopted as headline | Outcome | Killed / qualified by |
|---|---|---|---|
| **G0** | **ex-C2** — attribution identifiable iff the summary Jacobian has full column rank | **DEAD** | Kahl et al. (2019), via Sain & Massey (1969) |
| **G1** | **R1** — calibrate the selection event by rejection sampling from the simulator's null | **DEAD** | Freidling, Zhao & Gao (2024), Algorithm 1 |
| **G2** | **the composite-null gap and its repair** | **DEAD** | Dufour (2006), maximized Monte Carlo |
| **G3** | *(none adopted)* — **R2** checked, having never been a headline | **NARROW-CONDITIONAL** | Cintrón-Arias et al. (2009) + Moré & Wild (2012) |
| **G4** | *(none adopted)* — **G3's own numbers** attacked | **SPLIT: `S_B` stands, `S_A` does not generalise** | this project, for the first time |
| **G5** | *(none adopted)* — **G4's own deferral** closed | **SPLIT: separable at one distortion parameter per component, not at two** | this project, for the second time |

| | G0 | G1 | G2 | G3 | G4 | **G5** |
|---|---|---|---|---|---|---|
| Prior-art check run | yes | yes | yes | yes | n/a | **n/a** |
| Verdict | DEAD | DEAD | DEAD | NARROW-COND. | SPLIT | **WEAKENED** |
| Stopped early by its own rule | no | **yes** | **yes** | no | no | **yes** |
| Code written | none | none | none | yes | yes | **yes** |
| Numbers produced | none | none | none | yes | yes | **yes** |
| Adversarial check against own output | no | no | no | no | **yes** | **yes** |
| A pre-registered rule fired against the project | — | — | — | no | no | **yes** |
| `p_sel` measured | no | no | no | no | no | **no** |
| Independent review | no | no | no | no | no | **no** |
| Google Scholar searched | **no** | **no** | **no** | **no** | **no** | **no** |

### The shape of it, read honestly

**The first three sessions each adopted a headline and each died to a paper found in the next
session. The last three adopted none and have been attacking the project's own output
instead** — G3 built the diagnostic, G4 attacked its numbers, G5 closed the deferral G4 left.
That is a healthier pattern than the first three, and it has a cost that is now visible: **three
consecutive sessions have ended without the project's central affordability number, and two of
them ended by their own stop rules.**

**What is genuinely better than it was.** The separability precondition is supported at eight
family assignments rather than two, six of them new; the `κ_max` branch is resolved in closed
form and checked; the six-column verdict now carries the machinery the three-column one always
had; the S3 liveness defect that nearly caused a duplicate run in G4 is specifically fixed and
tested in both directions; and the diagnostic-only paper of `audit/PIVOT.md` is closer to
written than it has ever been.

**What is not.** **The MMC composition has still never been implemented and still never been
attacked by anyone.** That is the older half of **O-17**, unpaid through six sessions, and it is
the thing the project's viability actually rests on. Every session so far has strengthened or
qualified the *precondition* for a method nobody has yet tried to build or break.

**The pattern worth naming, updated.** G4 named its own: *"this session chose which attacks to
run."* G5's version is one level sharper and is the reason **D-13** exists. This session chose
which attacks to run **and** wrote, in advance, the rule for interpreting the result — and then
found that its own advance rule had predicted the wrong consequence. **Pre-registration
protected the criterion and did not protect the inference drawn from it**, which is a limit of
the device this project has been leaning on since G1, and it is worth knowing before the next
session leans on it again.

---

## 6. PROCESS CAVEATS — what this session did badly

- **The first Phase 1 run was discarded and repeated**, because the eight-assignment analysis
  was conceived after the first run had already produced the six-column verdict. Nothing was
  contaminated — clean tree, output deleted before the rerun, numbers identical — but it is the
  **third session running** in which the decisive check was thought of after the run rather
  than before it (D-9, D-13).
- **The pre-registered rule was written too coarsely**, which is what made D-13 necessary. A
  rule saying "only if the confound lies inside some three-column assignment" would have been
  testable rather than assumed, and the test cost nothing.
- **Google Scholar still not searched.** Sixth session. **O-7.**
- **`audit/CLAIM_GRAPH.md` still stale.** Fifth session flagged rather than rewritten.
- **`results/` still carries the vacuous `leakage_checked` literal** (**O-22**). The files
  written this session carry a real check; G3's still do not.
- **No literature check ran this session at all.** By scope, not by oversight — but it means
  the six-column confound has not been checked against anyone else's published account of the
  same aliasing, and an epidemiologist would very likely recognise it.
- **The machine was loaded throughout** (load ~7 on 8 cores, 8 GB), so column estimation used
  four workers and each run took about 13 minutes.

---

## 7. WHAT SHOULD HAPPEN NEXT

1. **Answer Q-14 and re-read Q-13.** Which separability sentence the paper writes. The
   recommendation is the one-parameter sentence with the two-parameter failure conceded in the
   paper rather than omitted.
2. **Choose between the two paths in `docs/DECISIONS.md` D-12** — measure the cost gate and
   build, or pivot to diagnostic-only. **PROPOSED, not decided.** The evidence favours Path 1;
   the argument against it is that six sessions of history say attack before you build.
3. **Measure `p_sel`** (**O-16**) under whichever path is chosen — it is informative either way
   and has now been deferred three sessions.
4. **Attack the MMC composition** (**O-17**, older half) — still entirely unpaid.
5. **Close Q-15 cheaply**: the intermediate `K = 4` case is re-analysable from the columns
   already recorded, with no new simulation.

---

## 8. POINTS REQUIRING OPERATOR INPUT

| # | Point | Notes |
|---|---|---|
| **P-1** | **Sign or reject G5** | `GATES.md`. The "does not certify" section is the part that matters, and its first item is the judgement in §4 above |
| **P-2** | **Choose a path — `docs/DECISIONS.md` D-12** | **PROPOSED, not decided.** Also the place to take the other reading of D-13 if you disagree with WEAKENED over OVERTURNED |
| **P-3** | **Answer Q-14** (and re-read the narrowed Q-13) | **BLOCKING** for the paper's separability sentence, and only for that |
| **P-4** | **Q-3** (reciprocal reviewer), Paris in-person attendance | Unresolved since G0 |

*Repository visibility is **not** on this list. `docs/DECISIONS.md` **D-11** records the
operator's ruling — public through the build, private before submission — and forecloses
re-raising it. It supersedes G4's P-4.*

---

## 9. THE ONE-PARAGRAPH VERSION

This project's first three sessions each adopted a headline and each headline died to a
published paper; the last three have attacked its own output instead. **G5 closed the one
question G4 left open, and the answer splits again.** `S_B` — the summary set the composition
specification nominates — separates the simulator's three components under **all eight**
component-wise assignments of a distortion family to a component that the two declared family
sets permit, six of which had never been tested: the strongest support the separability
precondition has ever had. **And it stops separating the moment a component may be wrong in two
ways at once.** With all six declared distortion directions side by side, `S_B` is inseparable
at a condition number of 629, and the confound is progression against observation — a drifting
removal hazard that cannot be told apart from a constant hazard change plus a drifting
reporting rate, which is a confound an epidemiologist would recognise and which this project's
own Q-12 predicted in prose before the numbers existed. It is not an estimator artefact, not a
threshold artefact, and not structural. **A rule this session committed before the run said that
finding overturns the three-column result; a measurement taken afterwards says the implication
was too strong; both readings are on the record and the operator may take either, and the
session halted regardless.** What has not changed in six sessions is the thing the project
actually rests on: `p_sel` is still unmeasured, and **the MMC composition has still never been
built and never been attacked by anyone.**
