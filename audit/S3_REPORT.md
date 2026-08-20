# S3 — Session G3 report

**For a reader who has not seen this session.** Written 2026-08-20.

> **Four things to know before anything else.**
>
> **1. This repository now contains code and numbers.** A three-component SIR simulator, three
> summary sets, a Jacobian rank/coherence diagnostic, a random-attributor floor check, and a
> test suite. Three prior sessions produced an extensive audit trail and no software. That is
> the single most important difference between this session and the three before it.
>
> **2. The D4 STOP condition did not fire.** Two of the three summary sets separate the three
> components under thresholds pre-registered in a session that provably produced no numbers.
> The deliberately impoverished control failed exactly as designed — with an *exact* null
> direction, not a near-null one, which is the strongest form that control can take.
>
> **3. R2 came back NARROW-CONDITIONAL — the first prior-art check in four sessions not to
> return DEAD.** It should not be read as good news. Both halves of R2 are prior art
> separately; only their composition is unoccupied, and that composition is one sentence wide.
> **R2 survived because it was never the headline.** All three claims that were headlines died.
>
> **4. Nothing has been independently reviewed, for the fourth consecutive session.** No
> adversarial critic has ever run in this project. Every verdict it holds, including this
> one, is single-pass.

---

## 1. WHAT THIS SESSION DID

All four phases ran. No stop condition fired.

| Path | Status |
|---|---|
| `audit/R2_THREAT_CHECK.md` | **new** — the check mandated in G1's brief and cut twice. Verdict **NARROW-CONDITIONAL** |
| `src/simulators/sir3.py` | **new** — 3-component SIR, one distortion family per component |
| `src/simulators/summaries.py` | **new** — `S_A`, `S_B`, `S_C` |
| `src/diagnostics/jacobian_rank.py` | **new** — the diagnostic |
| `src/diagnostics/floor_check.py`, `run_diagnostic.py`, `report_tables.py` | **new** — floor check, runner, table generator |
| `src/provenance.py` | **new** — the `PROVENANCE.md` header, defined in one place |
| `tests/` | **new** — the identity test, smoothness, plateau existence, `S_C`'s control, the floor |
| `results/` | **new numbers** — `jacobian_rank.{S_A,S_B,S_C}.yaml`, a no-CRN negative control, `floor_check.yaml`, generated `SUMMARY_TABLE.md` |
| `audit/MMC_COMPOSITION_SPEC.md` | **new** — Phase 3, **specification only**; nothing built |
| `docs/DECISIONS.md` | **D-6** — R2 is cited infrastructure, not a claimed contribution |
| `docs/OPEN_QUESTIONS.md` | **Q-10 answered and executed**; **Q-11**, **Q-12** raised; audit debt recorded |
| `GATES.md` | **G3 added**; **proposed sign-off conditions for G0, G1 and G2**, all unsigned |
| `PROVENANCE.md` | no longer describes a repository with no numbers; test-location table added |

---

## 2. PHASE 1 — THE R2 VERDICT

Full evidence in `audit/R2_THREAT_CHECK.md`. In brief:

| Source | What it does | Class |
|---|---|---|
| **Cintrón-Arias, Banks, Capaldi & Lloyd (2009)**, *J. Inverse Ill-posed Probl.* 17(6) | Selects parameter subsets by *"sensitivity matrices with **full rank**"* plus a condition number `κ = s₁/s_p`, **worked on an epidemic model**. 122 citations | **prior art for the rank screen** |
| **Moré & Wild (2010/2012)**, *ACM TOMS* 38(3) | *"near-optimal finite difference estimates of the derivatives of a **noisy function**"*, with a *"provably near-optimal"* difference parameter | **prior art for the noisy differencing — and stronger than an h-sweep** |
| **Gutenkunst et al. (2007)**, *PLoS Comput. Biol.* | Eigenvalue spectra spread over decades **without a gap**. 1,152 citations | **not a novelty threat — a threat to the quantity itself** |

**The strongest case against R2 is that it is the composition of two mature literatures**, one
of which already runs the rank-and-condition-number screen on an epidemic model. Against a
control of `the` = 452, Cintrón-Arias et al. contain `finite difference` **0**, `stochastic`
**0**, `Monte Carlo` **0** — their sensitivity matrix comes from a deterministic ODE — and they
call rank using MATLAB's routine at *"machine tolerance"*.

**That last detail is the one live seam, and it cuts both ways.** `docs/THRESHOLDS.md` §1.2
argued against a machine-epsilon tolerance for a noisy Jacobian, in writing, before this paper
was retrieved — so the pre-registered argument turns out to be an argument against the standard
practice of a literature it did not know it was arguing with, and `git log` establishes the
ordering. But **this project does not occupy the seam either**: `τ = 10⁻²` was derived from a
compute budget, not from a noise level. Occupying it now would mean re-deriving a pre-registered
threshold with the singular values already visible, which is the leakage failure
`LEDGER_DESIGN.md` D3 exists to prevent. That tension is **Q-11** and it is the operator's.

**The sharpest objection found is not about novelty at all.** The sloppy-models literature
reports these spectra as gapless; a gapless spectrum makes "numerical rank at tolerance τ" a
statement about where the analyst put τ. `rank` and `condition number` both appear **0** times
in Gutenkunst et al. against a control of `the` = 313 — declining to make a rank call is that
literature's position, not an oversight. `docs/THRESHOLDS.md` §1.4's unresolved-singular-value
rule is the pre-registered place where that would have surfaced in this session's results.

**Consequence, which the operator pre-specified: `docs/DECISIONS.md` D-6.** R2 is cited
infrastructure. "We contribute a simulation-based rank estimator" and "we contribute a rule for
calling numerical rank under noise" are both now unavailable as claims.


---

## 3. PHASE 2 — THE DIAGNOSTIC, BUILT AND RUN

**The tables in this section are reproduced verbatim from `results/SUMMARY_TABLE.md`, which is
generated by `src/diagnostics/report_tables.py` from the YAML results files.** No number in this
report was typed by hand (S11). Everything below traces to the recorded commit and seed.

### 3.1 What was built

- **`src/simulators/sir3.py`** — a three-component SIR simulator. Components declared in code and
  docstring: **TRANSMISSION** (`βSI/N`), **PROGRESSION** (`γI`), **OBSERVATION** (reporting
  fraction, delay, noise). Deterministic core is **fixed-step RK4, not adaptive**, because
  adaptive step selection changes discontinuously with parameters and is a classical source of
  the computational noise that would destroy the finite difference.
- **One distortion family per component**, each exactly the base simulator at `η=0`
  (tested **bit-identical**) and smooth through zero (tested by one-sided derivatives and a
  bounded second difference). The three are deliberately of three different kinds — a prevalence
  nonlinearity, a timing drift, and a pure amplitude error — so the Jacobian's columns are not
  similar by construction.
- **`src/simulators/summaries.py`** — the closed list `S_A` (epidemic-curve features), `S_B`
  (time-binned incidence), `S_C` (the impoverished positive control).
- **`src/diagnostics/jacobian_rank.py`** — the diagnostic. `h` is a **sequence**; a scalar raises,
  so a single-`h` call is not expressible.
- **`src/diagnostics/floor_check.py`** — the random-attributor floor, run **first**, because it
  validates the harness before anything rests on it.

### 3.2 The verdict

**The D4 STOP condition did not fire.** Both `S_A` and `S_B` are separable under the
pre-registered criteria; `S_C` is not, which is what it was built to be.

**Reproduced verbatim from `results/SUMMARY_TABLE.md`.** Headings are demoted one level to
nest under this section; nothing else is altered.

- commit: `570692c2f16b04c1948b47665c162c9478fe1de8`
- dirty: `False`
- command: `python -m src.diagnostics.run_diagnostic --seed 20260820 --replicates 128 --norm-replicates 2000 --floor-draws 10000`
- seed: `20260820`
- python `3.13.12`, deps `numpy==2.4.4, scipy==1.17.1, pyyaml==6.0.3`

### Verdict per summary set

| Summary set | d | rank at tau=1e-2 | full column rank | condition number | verdict |
|---|---|---|---|---|---|
| S_A | 4 | 3 | yes | 5.378 | separable |
| S_B | 10 | 3 | yes | 10.12 | separable |
| S_C | 2 | 2 | NO | inf | INSEPARABLE |

- **S_A** — separable: full column rank at tau and condition number within ceiling
- **S_B** — separable: full column rank at tau and condition number within ceiling
- **S_C** — rank deficient at tau

### Singular values, plateau, and resolution

| Summary set | singular values at representative h | plateau (h range) | n h in plateau | censored small / large h | all resolved |
|---|---|---|---|---|---|
| S_A | 4.156, 1.043, 0.7727 | 0.01 → 1e-06 | 5 | True / False | True |
| S_B | 27.8, 5.208, 2.747 | 0.1 → 1e-06 | 6 | True / True | True |
| S_C | 4.155, 0.9557, 0 | 0.1 → 1e-06 | 6 | True / True | True |

A plateau reaching the edge of the pre-registered sweep is reported as **censored**
there: the sweep stopped, not the plateau.

#### 2.1 Full h-sweep, leading singular value

| h | S_A | S_B | S_C | S_A no-CRN control |
|---|---|---|---|---|
| 0.1 | 4.157 | 27.8 | 4.156 | 4.263 |
| 0.01 | 4.156 | 27.8 | 4.155 | 6.658 |
| 0.001 | 4.156 | 27.8 | 4.155 | 48.63 |
| 0.0001 | 4.156 | 27.8 | 4.155 | 474.9 |
| 1e-05 | 4.156 | 27.8 | 4.155 | 4738 |
| 1e-06 | 4.156 | 27.8 | 4.155 | 4.737e+04 |

### Column norms and pairwise coherence

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

### Near-null directions and equivalence classes

**S_C**, direction 2 — `sigma = 0`, `sigma/sigma_1 = 0`, **exact** degeneracy

- right singular vector: (0.1854, 0.9826, 0.01282) over (transmission, progression, observation)
- equivalence-class members (|v_k| >= 0.3 across the whole plateau): progression
- borderline (|v_k| crosses 0.3 within the plateau): none
- |v_k| ranges across plateau: transmission [0.1854, 0.1872]; progression [0.9822, 0.9826]; observation [0.01282, 0.01327]

`docs/THRESHOLDS.md` §3.4: an **exact** degeneracy is a statement about
identifiability, matching Kahl et al. (2019). A **near** degeneracy at condition number
kappa is a statement about **affordability** — separation costs about kappa^2 replicates
— and must never be written as an identifiability claim.

### Random-attributor floor check

| K | analytic floor 1/K | simulated accuracy | deviation | tolerance (4 s.e.) | passes |
|---|---|---|---|---|---|
| 3 | 0.333333 | 0.3299 | -0.00343 | 0.0189 | True |

Run as 10000 draws at seed 20260820. Every attribution accuracy this
project reports is reported against this floor.

### Negative control — the same sweep without common random numbers

- plateau found: **False**
- leading singular value across the sweep: 4.263, 6.658, 48.63, 474.9, 4738, 4.737e+04
- ratio between successive (ten-fold smaller) h: 1.56, 7.3, 9.77, 9.98, 10

Without common random numbers the difference quotient carries noise of order
`obs_sigma / h`, so the leading singular value grows as `1/h` and no plateau exists.
This is the control that makes the main sweep's plateau meaningful rather than
assumed.

### D4 STOP condition

**Did not fire.** Separable summary set(s): **S_A, S_B**.

`docs/THRESHOLDS.md` §1.6 notes that because `S_C` is expected to fail by
construction, the STOP condition is decided by `S_A` and `S_B`, and `S_C`'s designed
failure must not later be read as one third of the evidence for stopping.


### 3.3 Reading the result, with the caveats attached rather than appended

**`S_C` failed in the strongest way the control could fail.** Its rank deficiency is *exact*, not
near — the third singular value is structurally zero because `d = 2 < K = 3` — and the diagnostic
reports the exact null direction rather than omitting it. That last part is not automatic: the
economy SVD returns only `min(d,K)` right singular vectors and would have silently dropped the
null direction, which is the entire content of the control. Per `docs/THRESHOLDS.md` §3.4, an
exact degeneracy is a statement about **identifiability**, matching Kahl et al. (2019) — not
about affordability.

**`docs/THRESHOLDS.md` §1.6 anticipated the reading error to avoid here** and it is worth
repeating: because `S_C` is *expected* to fail by construction, the STOP condition is decided by
`S_A` and `S_B` alone, and `S_C`'s designed failure must not later be counted as one third of the
evidence for stopping.

**Every singular value is resolved across the plateau**, so the third outcome
`docs/THRESHOLDS.md` §1.4 admits — *"the rank of this Jacobian is not determined by this
estimator at this precision"*, which is a gate **failure** rather than a pass — did not occur.
This is also where the sloppy-models objection of §2 would have surfaced, and it did not.

**The plateaux are censored at the small-`h` end.** They run to the smallest step size in the
pre-registered sweep, which means **the sweep stopped, not the plateau**: the float-cancellation
branch was never reached. The results files record this as `censored_at_small_h` rather than
reporting a bounded plateau, because claiming a lower edge would be claiming knowledge the sweep
does not have.

**The coherence numbers are reported and are deliberately not the decision rule**
(`docs/THRESHOLDS.md` §2.2). They are a pointer to *which pair* is responsible, not a verdict.

---

## 4. WHAT PHASE 2 ACTUALLY FOUND ABOUT *THIS* SIMULATOR

Beyond the verdict, four findings are worth stating on their own, because they are about how
this kind of diagnostic behaves rather than about whether this particular simulator passes.

### 4.1 The observation noise model decides whether the Jacobian exists at all

Under common random numbers, a **count-valued** observation layer (Poisson, negative binomial)
makes the simulator a *step function* of the distortion. The difference quotient is then exactly
zero when no draw flips and O(1/h) when one does — and **shrinking `h` makes the first case more
likely**, so the estimator converges confidently to zero. That is worse than a noisy estimate: it
is a wrong estimate that looks stable.

A **continuous multiplicative** layer multiplies the derivative instead of quantising it, and the
finite difference is well posed. The simulator implements both; the count model is a negative
control and is asserted as one in the tests. **This is a modelling constraint on any
simulation-based Jacobian, not an implementation detail**, and it is the kind of thing that would
silently invalidate a result rather than break it.

### 4.2 Summary statistics defined by `argmax` are not finite-differentiable

Peak *time* on a daily grid is integer-valued, so its difference quotient is zero almost
everywhere and O(1/h) at the jumps. Both peak statistics are therefore computed by parabolic
interpolation about the discrete maximum. This is a substantive choice about the summary — it
changes what `S_A` measures — and it is recorded in the results files rather than buried in code.

### 4.3 Common random numbers are load-bearing, and the control proves it rather than assuming it

The same sweep run with independent noise across the `+h` and `-h` evaluations is emitted as its
own results file. Its leading singular value grows as `1/h` across the entire sweep and no
plateau is identifiable. The main sweep's plateau is meaningful because that control exists.

### 4.4 The verdict is a statement about three specific distortion families

The observation distortion is a pure reporting-fraction multiplier — an *amplitude* error, set
against a prevalence nonlinearity (transmission) and a timing drift (progression). Three
qualitatively different columns is a favourable configuration. **Perturbing the reporting
*delay* instead would make the observation column a timing distortion too, competing directly
with progression, and could plausibly give a different verdict.** That is **Q-12**, and the
favourable outcome does not make it a smaller caveat.

---

## 5. PHASE 3 — THE NEXT SESSION'S TARGET, SPECIFIED NOT BUILT

`audit/MMC_COMPOSITION_SPEC.md`. **No code was written for it**, by instruction.

The composition: rejection-sample the selection cell (Freidling et al.'s Algorithm 1) *inside*
the nuisance maximisation (Dufour's Proposition 4.1). The spec cites Proposition 4.1 and its
equations (4.20)–(4.21) from the retrieved text, not from G2's summary — including Dufour's own
statement that the maximisation is derivative-free because the objective is *"a step-type
function"* with *"zero derivatives almost everywhere"*.

**Three things the spec puts at the top rather than in a limitations section**, because the
opposite habit is what produced this project's first three failures:

1. **It is a composition of two published techniques, not a theorem.** The only actual theorem
   is a short exchangeability lemma, and the spec says it is short.
2. **It is conservative by construction.** Dufour states it himself: type-I error *"can be lower
   (but not higher) than the level"*. Exact **level**, not exact **size** — and the composition
   has two compounding sources of it. **No sentence of the form "simulators make selective
   inference exact" is available.**
3. **The cost multiplies.** The rejection cost `1/p_sel` is paid **at every nuisance value the
   maximiser visits**: total `M × N / p_sel`, not `N / p_sel` plus a search. Holding the
   simulated disturbances fixed across `θ` does *not* amortise it, because the *acceptance* of a
   draw into the selection cell depends on `θ`.

**A cost gate is pre-registered in the spec, before the number exists**, in the same way the rank
thresholds were: measure `p_sel` first — it needs only null draws and the selection rule, no MMC
at all — and if the product exceeds a stated ceiling, **the honest output is the cost analysis
itself**, not a scaled-down experiment that hides it.

---

## 6. GATE G3, AND THE THREE OLDER GATES

**G3: `ready for review — UNSIGNED`.** Twenty-one criteria, all met. The gate's own
"does not certify" section is longer than its criteria table, which is the right shape for a
session whose main achievement is that it built something rather than that it proved something.

**Proposed sign-off conditions are now drafted for G0, G1 and G2** (brief §4.2), all with blank
signature lines (S9). They have been outstanding for three sessions. In brief:

- **G0** — the G1-drafted text stands; one condition should be *added* if amending, namely that
  G0's negative searches ran on the wrong instrument.
- **G1** — sign as an accurate record of a session whose defining criterion was **not met**, with
  those criteria now **discharged by G3**, so G1 does not need re-preparing.
- **G2** — sign as **NOT MET, correctly stopped**, and record that its unbriefed finding (the
  search-instrument correction) is the most valuable thing this project has produced.

---

## 7. THE FOUR-SESSION TRAJECTORY

Extending `audit/S2_REPORT.md` §3.

### What each session adopted, and what happened to it

| Session | Claim adopted as headline | Outcome | Killed by |
|---|---|---|---|
| **G0** | **ex-C2** — attribution identifiable iff the summary Jacobian has full column rank | **DEAD** | Kahl et al. (2019), *PRX* 9:041046, via Sain & Massey (1969) |
| **G1** | **R1** — calibrate the selection event by rejection sampling from the simulator's null | **DEAD** | Freidling, Zhao & Gao (2024), Algorithm 1 |
| **G2** | **the composite-null gap and its repair** | **DEAD** | Dufour (2006), maximized Monte Carlo |
| **G3** | *(none adopted)* — **R2** checked, having never been a headline | **NARROW-CONDITIONAL** | Cintrón-Arias et al. (2009) + Moré & Wild (2012), on complementary halves |

### What each session produced

| | G0 | G1 | G2 | **G3** |
|---|---|---|---|---|
| Prior-art check run | yes | yes | yes | **yes** |
| Verdict | DEAD | DEAD | DEAD | **NARROW-CONDITIONAL** |
| Stopped early by its own rule | no | **yes** (Phase 2.4) | **yes** (Phase 1.5) | **no** |
| Code written | none | none | none | **yes** |
| Numbers produced | none | none | none | **yes** |
| Adversarial critic run | **no** | **no** | **no** | **no** |
| Google Scholar searched | **no** | **no** | **no** | **no** |

### The shape of it, read honestly

The first three sessions each adopted a headline and each headline died to a paper found by
direct retrieval in the *next* session, usually within a few queries. G2 established that a large
part of the cause was an instrument failure — the arXiv searches were metadata-only — and fixed
it. **G3 is the first session run entirely on the corrected instrument, and it is also the first
session that did not adopt a headline.** Those two facts are not independent: this session was
instructed to check a claim it already had rather than to find a new one.

**What has actually changed:** the project now has a working search instrument, a running
diagnostic, and a specification whose stated weaknesses are in its first section rather than its
last. **What has not:** nothing here has been reviewed by anyone, and the composition that the
project's viability now rests on has not been attacked the way the three dead claims were.

**The one pattern worth naming.** Three sessions overstated what they had and were corrected by
retrieval. This session's risk is the opposite and subtler: a favourable empirical result, on a
simulator this project designed, with distortion families this project chose, under thresholds
this project pre-registered. **Pre-registration protects against fitting thresholds to results.
It does not protect against choosing a simulator whose components happen to separate.** Q-12 is
the sharpest available instance of that and it is unresolved.

---

## 8. PROCESS CAVEATS — what this session did badly or not at all

**No adversarial critic ran. Fourth session running.** This is now the longest-standing
methodological gap in the project and it has already cost it twice.

**Google Scholar still not searched.** Fourth session, same gap (**O-7**). **Semantic Scholar
rate-limited again** — `search_papers` returned HTTP 429 on the first call — so citation-chaining
has still never been performed here.

**No version of record was obtained for any of the three sources this session leans on.** Dufour
(2006) is quoted from CIRANO WP 2005s-02 (**O-14**, and it blocks citing MMC in a manuscript);
Moré & Wild (2012) from an Argonne preprint recovered through the Wayback Machine after
`mcs.anl.gov` returned **HTTP 403** to every non-browser agent; Cintrón-Arias et al. (2009) from
arXiv. All three are cited as such.

**Two instrument defects were caught only because they were checked, and both are the same class
of failure `audit/TOOLING.md` was written about — recurring within one session of that file.**

1. **arXiv renders an empty result set as the literal string `No Results.`** The batch script
   reported `PARSE_FAIL`, and the response was decoded by hand to confirm the zero before any
   zero was recorded. **A script that defaulted to `0` instead would have manufactured a measured
   zero out of an unparsed page** — exactly what S4 forbids.
2. **PDF text extraction preserves the `ﬀ`/`ﬁ` ligatures.** `grep -a "difference parameter"`
   returned **0** against **18** real occurrences, and `identifiab` returned 0 for the same
   reason. S7's rule about `grep -a` does not cover this. Every count in this session's threat
   check was re-run through an NFKC normaliser and every one is quoted with its control.
   **A standing rule for this should be added alongside S7.**

**The first two production runs were discarded**, both because `PROVENANCE.md` makes `dirty:
true` disqualifying: the first ran with uncommitted code, the second was invalidated by
documentation edits made *while it was in flight*. The code and documents were committed and the
run repeated from a clean tree. `src/provenance.py` now records **which** paths were dirty, so a
future session can tell an unrelated concurrent edit from a genuinely stale result. The discarded
files were deleted rather than kept.

**One test was written wrong and the code was right.** The Poisson-differentiability test
asserted that the difference quotient grows as `h` shrinks. It does not always: it is *exactly
zero* when no draw flips, and O(1/h) when one does. The test named one branch of the pathology
and missed the other, which is the more dangerous branch. Corrected to assert the failure to
converge rather than one of its two faces.

**`audit/CLAIM_GRAPH.md` is still stale.** It has carried a "this is stale" banner since G2. Its
R1/R2 structure predates both D-6 and the composition framing. **Third session in which it has
been flagged rather than rewritten.**

**`p_sel` was not measured**, so the one number that decides whether the next session's work is
affordable does not exist.

**The separability result is single-seed.** The diagnostic was run at one seed. The plateau is
stable and the singular values are resolved across it, but **no seed-to-seed variability of the
rank verdict has been computed**, and the tests exercise the estimator's structure rather than
the stability of the verdict. That is the cheapest remaining check and it was not done.

---

## 9. WHAT SHOULD HAPPEN NEXT

In order, and none of it requires a new claim:

1. **Measure `p_sel`.** It is cheap, it needs no MMC, and it decides whether the composition is
   buildable at all. The cost gate is already pre-registered in the spec.
2. **Run an adversarial critic against the composition** — and, while it is running, against
   this report. Four sessions without one is the project's largest methodological debt, and the
   two times it has been paid down by accident it changed the answer.
3. **Re-run the diagnostic at several seeds** and report the verdict's stability, not just the
   plateau's.
4. **Answer Q-11** (occupy the tolerance seam, or state plainly that the gap was named and not
   filled) and **Q-12** (whether a second observation distortion is in scope).
5. **Close O-14** before MMC appears in any manuscript.
6. **Rewrite `audit/CLAIM_GRAPH.md`**, which has now been deferred three times.

---

## 10. POINTS REQUIRING OPERATOR INPUT

Collected, not resolved.

| # | Point | Notes |
|---|---|---|
| **P-1** | **Sign or reject G3**, after reading this report | `GATES.md`. Twenty-one criteria met; the "does not certify" section is the part worth reading |
| **P-2** | **Proposed sign-off conditions for G0, G1 and G2** — accept, amend, or reject | `GATES.md`. Drafted this session, all signature lines blank. Outstanding for three sessions |
| **P-3** | **Whether to build the MMC composition next session** | Contingent on the rank condition, which **passed**. But `audit/MMC_COMPOSITION_SPEC.md` §4 argues the binding constraint is *cost*, not identifiability, and the deciding measurement (`p_sel`) has not been made. **Recommend: authorise the `p_sel` measurement and the cost gate, not the implementation** |
| **P-4** | **Q-3** (reciprocal reviewer) and Paris in-person attendance | Unresolved since G0. Sim2Science desk-rejects for a failed reciprocal review |
| **P-5** | **Repository visibility** | See below — the trigger condition has now been met |
| **P-6** | **Q-11** — occupy the noise-calibrated tolerance seam, or state that it was named and not filled | New. `docs/OPEN_QUESTIONS.md`. Recommend the latter |
| **P-7** | **Q-12** — is a second observation distortion (delay) in scope? | New. It is the sharpest available challenge to this session's favourable result |

### On P-5, stated once and not re-argued

`docs/DECISIONS.md` **D-4** and `OUTSTANDING.md` **O-1** both say the repository stays public
during the build and becomes private *"the moment `paper/` gains a draft or `results/` gains a
final number."* **`results/` now contains numbers.** Whether the diagnostic's output counts as
"final results" in the sense D-4 intended is the operator's call, not this session's, and the
decision itself is not reopened here — this is a factual notice that the condition D-4 names has
arguably been reached, recorded because a trigger nobody notices is not a trigger.

---

## 11. THE ONE-PARAGRAPH VERSION

The project's first four sessions produced three dead headline claims and, in this one, a
working diagnostic. R2 — the only claim never previously checked — came back
**NARROW-CONDITIONAL**: both of its halves are prior art and only their composition is
unoccupied, so it is now carried as **cited infrastructure** rather than a contribution. Built
against thresholds pre-registered before any number existed, the diagnostic finds that **this**
three-component SIR simulator **does** separate its components under two of three summary sets,
with the deliberately impoverished control failing exactly as designed. That clears the
precondition for the composition specified in `audit/MMC_COMPOSITION_SPEC.md` — Dufour's
maximized Monte Carlo composed with a selection event — whose own specification says, in its
first section, that it is a composition rather than a theorem, that it is conservative by
construction, and that its cost multiplies rather than amortises. **The remaining risk has
changed shape**: the first three sessions overstated what they had and were corrected by
retrieval; this one produced a favourable result on a simulator it designed, with distortion
families it chose, and nobody has yet tried to break it.
