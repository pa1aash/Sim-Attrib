# S4 — Session G4 report

**For a reader who has not seen this session.** Written 2026-08-20.

> **Four things to know before anything else.**
>
> **1. The project attacked its own result for the first time, and the result split in two.**
> G3 reported that *"two of the three summary sets separate the components."* The two are not
> equivalent. **`S_B` survives an adversarially constructed distortion family set; `S_A` does
> not** — its condition number rises 25-fold past the pre-registered ceiling and its verdict
> flips. They should not be quoted as a pair again.
>
> **2. No number G3 computed is wrong.** Everything reproduces, at the recorded seed and at two
> further seeds, with the pre-registered thresholds unrevised and not one of them changed this
> session. What moved is **what the numbers license**, not the numbers.
>
> **3. Three validity flags in this repository could not have failed** — including one that was
> added specifically to repair an earlier flag that could not have failed. `leakage_checked:
> true` was a hard-coded literal in every results file; the test guarding the peak-interpolation
> claim swept a curve on which the discontinuity it checked for is zero by construction; and
> `dirty_paths`, the field `DEVIATIONS.md` D-8 introduced to make `dirty` informative, was
> corrupting the first path it printed. All three are D-8's own defect class, found by applying
> D-8's own rule to D-8's own repairs.
>
> **4. This is still not an independent review, and that limit does not shrink because the pass
> found things.** The same project attacked its own output, with its own code, in the session
> that wrote the attack. A critic hoping for survival and a critic hoping for failure would both
> have found *something*; what neither can supply from inside is a check on which things were
> looked for.

---

## 1. WHAT THIS SESSION DID

All three phases ran. The scope boundary held: **`p_sel` was not measured, no cost gate was
built, no part of the MMC composition was implemented, and `paper/main.tex` was not created.**

| Path | Status |
|---|---|
| `audit/G3_ADVERSARIAL_REVIEW.md` | **new** — the critic pass. Six findings, verdict at the top |
| `results/robustness/` | **new numbers** — the adversarial family run, two seed re-runs, a threshold re-analysis, a summary-smoothness census, a count-coupling discriminator, a six-column spectrum, and a generated table |
| `src/diagnostics/run_family_check.py` | **new** — re-runs the diagnostic under a different family set or seed, into `results/robustness/`, never over `results/` |
| `src/diagnostics/threshold_sensitivity.py`, `summary_smoothness_check.py`, `crn_count_check.py`, `wide_spectrum_check.py`, `report_robustness.py` | **new** — one per finding, plus the table generator |
| `src/simulators/sir3.py` | **`families="adversarial"`** — a second distortion triple. The base branch is unchanged and bit-identical at `η = 0` |
| `src/diagnostics/jacobian_rank.py` | **`leakage_check()`** — replaces a hard-coded literal with a check that can fail |
| `src/provenance.py` | **fixed** — `dirty_paths` was corrupting the first path it reported |
| `src/simulators/summaries.py` | **docstring corrected** — a claim about the peak interpolation was false |
| `tests/` | **65 → 84 tests**, including `tests/test_provenance.py` (new) and a test that injects a leak and requires the leakage check to catch it |
| `results/jacobian_rank.{S_A,S_B,S_C}.yaml` | **annotated, not recomputed** — an appended `g4_adversarial_review` block; original bytes byte-for-byte intact |
| `docs/THRESHOLDS.md` | four annotations, **zero changed numbers** |
| `docs/OPEN_QUESTIONS.md` | **Q-13** raised (blocking); **Q-12** answered and closed |
| `docs/DECISIONS.md` | **D-7** — D-4's visibility trigger has fired |
| `DEVIATIONS.md` | **D-9** (the adversarial set was designed with the results known), **D-10** (the `dirty_paths` defect) |
| `GATES.md` | **G0, G1, G2, G3 signed** per the operator's decision; **G4 added**, unsigned |
| `audit/MMC_COMPOSITION_SPEC.md` | one factual correction note. **No specification changed, nothing implemented** |

---

## 2. PHASE 1 — THE CRITIC PASS

Full evidence in `audit/G3_ADVERSARIAL_REVIEW.md`. Every number there is reproduced from
`results/robustness/ROBUSTNESS_TABLE.md`, which is generated from the YAML files (S11).

| # | What was attacked | Verdict |
|---|---|---|
| 1 | The gapless-spectrum objection | **G3 stands at `K = 3`; the objection is deferred, not defeated** |
| 2 | Whether the verdict survives a different distortion family set | **`S_A` overturned, `S_B` stands** |
| 3 | The count-observation CRN finding | **Genuine degeneracy; not novel; one clause misdescribed** |
| 4 | Whether `S_A`'s argmax summaries contaminate its Jacobian | **A documented claim is false; the numbers are clean** |
| 5 | *(not in the brief)* Validity flags, against the project's own S3 rule | **Three defects** |
| 6 | *(not in the brief)* Seed stability of the verdict — **O-18** | **Stands, unqualified** |

### 2.1 The one that matters — finding 2

`docs/THRESHOLDS.md` §1.1 calls `S_A` *"the set a domain modeller would actually choose"* and
`S_B` *"the set an SBI practitioner would actually choose"*. Under the base distortion families
both separate. Under an alternative triple — **one attempt, no search over candidates, each
family specified against a named target component and its reasoning committed before the run** —

| | `S_A` | `S_B` |
|---|---|---|
| base families | `κ = 5.378`, **separable** | `κ = 10.12`, **separable** |
| adversarial families | `κ = 136.7`, **INSEPARABLE** | `κ = 64.62`, **separable** |

**`S_A`'s favourable result is a property of the three families G3 chose, not of the simulator.**
The confounded pair under the adversarial set is progression–observation: a drifting reporting
rate cannot be told apart from a drifting removal hazard.

**`S_B` survives, and that is a real result rather than a consolation.** Ten binned coordinates
buy robustness that four curve features do not, and `S_B` is the set
`audit/MMC_COMPOSITION_SPEC.md` §5 already nominates for the composition. Two qualifications
travel with it: its margin falls from 9.88× to 1.55×, and its separation cost — priced by
`docs/THRESHOLDS.md` §1.2 at `~κ²` replicates — rises about **forty-fold**, from `~10²` to
`~4×10³`. That multiplier lands directly on the cost gate the next session is meant to build.

**G3 raised this itself, as Q-12, and called it a real limitation.** What this session added is
the size. Q-12 is now closed as answered; **Q-13** is the live question, and it is about what
may be claimed rather than which families are in scope.

### 2.2 The gapless objection, and why the reassuring half is the weaker half

The reported three-column spectra span **one decade or less** and no singular value sits
anywhere near `τ`, so the specific failure Gutenkunst et al. describe — an arbitrary cut through
a gapless continuum — did not occur. `S_A`'s verdict survives `τ` moving by 18.6×, `S_B`'s by
9.88×.

**That reassurance is a fact about `K = 3`, not about the simulator**, and the check that shows
it is the sharpest number in the session. Placing the base and adversarial columns side by side
gives a `d × 6` Jacobian of the same simulator; for `S_B` the six-column spectrum spans **2.80
decades with no break**, `τ` falls *inside* it, and **a 9.01% change in `τ` moves the rank.**
Against ×9.88 at `K = 3`, that is a hundredfold change in tolerance-sensitivity, produced purely
by lengthening the component list.

**So a rank verdict on this simulator is tolerance-insensitive only while the component list is
short.** `κ = 5.38` is not a natural break and must not be written as one.

### 2.3 The two findings that came back favourable

Reported at the same weight as the unfavourable ones, because **S10 cuts both ways** and a
critic pass that only produced bad news would be as unreliable as one that produced none.

- **The reported `S_A` numbers are not contaminated by the argmax discontinuity.** At the
  representative `h = 10⁻⁴` none of 128 replicates straddled an argmax switch, for any of the
  three components — and that is what the `O(h)` scaling predicts from the `h = 10⁻¹` rate, not
  a lucky draw.
- **The verdict is seed-stable.** Across three seeds, `S_A`'s `κ` reads `5.378`, `5.379`,
  `5.386` and `S_B`'s reads `10.12`, `10.12`, `10.11` — a spread of about 0.15%, with every
  verdict unchanged. **O-18**, open since G3 and called there "the cheapest remaining check", is
  closed.

### 2.4 What finding 4 actually found

The concern G3 recorded was aimed at the wrong coordinate. `src/simulators/summaries.py` claimed
the parabolic interpolation left *both* peak statistics continuous across a change of the
discrete argmax. **Peak time is continuous; peak height jumps by `(a−c)/8`**, and jumps further
when the argmax moves between two separated local maxima rather than adjacent bins — a case the
docstring's argument never covered.

The leave-one-coordinate-out recomputation makes the sting precise:

- dropping **peak time** — the coordinate G3 worried about — moves `κ` from **5.378 to 5.379**.
  It carries essentially no information about the rank.
- dropping **peak height** — the coordinate that is genuinely discontinuous, and whose continuity
  was positively asserted — makes `S_A` **INSEPARABLE at `κ = 1165`**. The verdict rests on it.

**The numbers survive. The reasoning that was supposed to protect them did not.**

### 2.5 The count-CRN finding is genuine, and it is textbook

Derived on paper first (`audit/G3_ADVERSARIAL_REVIEW.md` §3.1), then measured under three
couplings of the same deterministic mean. A monotone inversion coupling was implemented
specifically because it would have exonerated the code if the failure were a sampler artefact.
**It does not: both count couplings give a step function** (39% and 49% of adjacent `η` steps
producing exactly equal values, against 0% for the continuous layer). Genuine degeneracy.

It is also not a discovery. It is the standing precondition of the entire
finite-difference-with-common-random-numbers literature — **L'Ecuyer & Perron (1994)**,
*Operations Research* 42(4), prove the CRN guarantee *"under the (sufficient) conditions usually
given for infinitesimal perturbation analysis to apply"* and note their results are *"based on
continuity and smoothness"* — and the discrete case is the textbook failure of that condition
(**Mohamed, Rosca, Figurnov & Mnih**, JMLR 21, 2020: *"if the measure is discrete on its domain
then the score-function or measure-valued gradient are available"*). **D-6's framing applies:
cited infrastructure, not a finding.**

One clause needs rewriting. G3 says the estimator *"converges confidently to zero"*; what was
measured is that at `R = 128` the estimate swings between `0`, `3125` and `−3906` against a truth
of `−866.6`, dominated by rare single-count flips. The failure is **unbounded variance**, not
bias — which matters, because it names the remedy: no `h` and no affordable `R` fixes it.

---

## 3. PHASE 2 — WHAT WAS DONE ABOUT IT

The brief offers two branches and **neither fits cleanly**, since `S_A`'s generalisation is
overturned while `S_B` stands. The judgement call is stated in
`audit/G3_ADVERSARIAL_REVIEW.md` and summarised here:

- **The annotation required by 2.2 was done in full**, and would have been done under either
  branch. `results/jacobian_rank.{S_A,S_B,S_C}.yaml` carry an appended `g4_adversarial_review`
  block — **appended as text, so the original bytes are byte-for-byte intact** and `git diff`
  shows it. `docs/THRESHOLDS.md` carries four annotations and **no changed number**.
- **The blocking question required by 2.1 was raised**, as **Q-13**.
- **2.1's STOP was not triggered.** Its purpose is to stop further work being built on a result
  that has moved, and no further work was built on it: `p_sel` is unmeasured, no cost gate
  exists, no MMC code exists.
- **2.2's instruction to name `p_sel` as the next session's target was NOT executed
  unilaterally**, because that is conditional on a STANDS verdict and this is not one. It stays
  as **P-3**, for the operator.

---

## 4. WHAT WAS DELIBERATELY NOT DONE

- **`p_sel` was not measured.** Still the one number that decides affordability, and finding 2
  has changed the multiplier it will be judged against.
- **No cost gate, no MMC implementation, no `paper/main.tex`.**
- **No threshold was revised.** `docs/THRESHOLDS.md` is annotated in four places and every number
  in it is the number G1 wrote before any singular value existed. Re-deriving `τ` now, with the
  spectra visible, is the leakage failure `LEDGER_DESIGN.md` D3 exists to prevent, and **Q-11**
  remains open with (b) still recommended.
- **`results/` was not regenerated.** Not even to replace the vacuous `leakage_checked` literal
  with the real check that now exists — that would overwrite G3's numbers to fix a metadata
  field. **O-22** tracks doing it deliberately, where the re-run reproducing the numbers exactly
  is itself the test.

---

## 5. GATE G4

**`ready for review — UNSIGNED`.** Eighteen criteria, all met; the first three are the brief's
own test of whether this was a critic pass or a confirmation pass. **The "does not certify"
section is the part worth reading**, and its first item is that this was not an independent
review.

---

## 6. THE FIVE-SESSION TRAJECTORY

Extending `audit/S3_REPORT.md` §7.

| Session | Claim adopted as headline | Outcome | Killed by |
|---|---|---|---|
| **G0** | **ex-C2** — attribution identifiable iff the summary Jacobian has full column rank | **DEAD** | Kahl et al. (2019), via Sain & Massey (1969) |
| **G1** | **R1** — calibrate the selection event by rejection sampling from the simulator's null | **DEAD** | Freidling, Zhao & Gao (2024), Algorithm 1 |
| **G2** | **the composite-null gap and its repair** | **DEAD** | Dufour (2006), maximized Monte Carlo |
| **G3** | *(none adopted)* — **R2** checked, having never been a headline | **NARROW-CONDITIONAL** | Cintrón-Arias et al. (2009) + Moré & Wild (2012) |
| **G4** | *(none adopted)* — **G3's own numbers** attacked | **SPLIT: `S_B` stands, `S_A` does not generalise** | **this project, for the first time** |

| | G0 | G1 | G2 | G3 | **G4** |
|---|---|---|---|---|---|
| Prior-art check run | yes | yes | yes | yes | n/a |
| Verdict | DEAD | DEAD | DEAD | NARROW-COND. | **SPLIT** |
| Stopped early by its own rule | no | **yes** | **yes** | no | no |
| Code written | none | none | none | yes | **yes** |
| Numbers produced | none | none | none | yes | **yes** |
| **Adversarial critic run** | **no** | **no** | **no** | **no** | **yes — against its own output** |
| Independent review | no | no | no | no | **no** |
| Google Scholar searched | **no** | **no** | **no** | **no** | **no** |

### The shape of it, read honestly

The first three sessions each adopted a headline and each headline died to a paper found by
direct retrieval in the next session. G3 adopted none, built the diagnostic, and produced the
project's first favourable number. **G4 is the first session whose target was the project's own
output, and it found something in every place it looked** — which is the outcome the four
previous sessions' missing critics predicted.

**What has changed:** the largest methodological debt has been half paid. The favourable result
is now a *conditional* favourable result with the condition measured. Two of this repository's
own validity mechanisms have been repaired, and a third has been repaired for the second time.

**What has not:** nothing here has been reviewed by anyone outside the project. The MMC
composition — the thing the project's viability actually rests on — **has still never been
attacked by anything**, which is the older and larger half of **O-17**, and this session did not
touch it by instruction.

**The pattern worth naming, updated.** G3's report said its risk was the opposite of G0–G2's:
*"a favourable empirical result, on a simulator this project designed, with distortion families
this project chose"*, and that *"pre-registration protects against fitting thresholds to results.
It does not protect against choosing a simulator whose components happen to separate."* **That
was the correct diagnosis and finding 2 is its confirmation.** The remaining version of it is
one level up and unaddressed: this session chose which attacks to run.

---

## 7. PROCESS CAVEATS — what this session did badly

- **Runs were invalidated by edits made while they were in flight, again.** Three checks were
  launched, the tree was then edited, and they were killed and restarted from a clean commit —
  the same mistake that cost G3 three production runs, repeated within one session of reading
  `DEVIATIONS.md` D-8 about it. The restarted runs are the ones reported; all record
  `dirty: false`.
- **A duplicate process was very nearly allowed to race.** A faulty check reported a seed run as
  dead when it was alive, and a second copy was launched writing to the same output paths. Caught
  by inspecting process state directly rather than trusting the check, and killed before either
  wrote. **A second instance of "the check was wrong, not the thing it checked"**, in the same
  session that found three of them in the repository.
- **The adversarial family set was designed with the base results already known.** Unavoidable
  given when this session ran, and weaker than pre-registration. **It should have been specified
  in G3**, whose own §4.4 already identified the weakness it probes. `DEVIATIONS.md` **D-9**.
- **A seed run was killed by memory pressure mid-sweep** and had to be restarted; and a faulty
  liveness check then led to a duplicate being launched against the same output paths, caught
  before either wrote. Both are recorded above rather than tidied away.
- **The literature check was one targeted pass**, per instruction. It establishes the count-CRN
  failure is known; it does not establish nothing else relevant exists.
- **Google Scholar still not searched.** Fifth session. **O-7.**
- **`audit/CLAIM_GRAPH.md` is still stale.** Fourth session flagged rather than rewritten.
- **The machine was thermally throttled and heavily loaded throughout**, so runs were serialised
  by hand. Irrelevant to the numbers, relevant to the next session: profiling puts ~87% of a
  simulator run in the pure-Python RK4 loop at ~0.14 s per run, and the cost gate will be priced
  in units of that.

---

## 8. WHAT SHOULD HAPPEN NEXT

1. **Answer Q-13** — what may be claimed from a family-conditional separability verdict. Blocking
   for the paper's separability sentence, and only for that.
2. **Measure `p_sel` and build the cost gate** (**P-3**, recommended by G3 and unchanged by this
   session's findings, except that finding 2 raises the `κ²` multiplier it must be assessed
   against about forty-fold for `S_B`).
3. **Run an adversarial critic against the MMC composition** — the older half of **O-17**, still
   entirely unpaid, and the one this session was scoped away from.
4. **Re-run `run_diagnostic.py` once** so `results/` carries a real leakage check (**O-22**), and
   treat exact reproduction of the existing numbers as the test.
5. **Close O-14** before MMC appears in any manuscript, and **rewrite `audit/CLAIM_GRAPH.md`**,
   deferred four times.

---

## 9. POINTS REQUIRING OPERATOR INPUT

| # | Point | Notes |
|---|---|---|
| **P-1** | **Sign or reject G4**, after reading this report | `GATES.md`. The "does not certify" section is the part that matters |
| **P-2** | **Q-13 — what may be claimed from a family-conditional verdict** | **BLOCKING** for the paper's separability sentence. Recommendation offered in `docs/OPEN_QUESTIONS.md`: the narrow sentence now, the larger experiment only if the paper needs the stronger one |
| **P-3** | **Confirm `p_sel`/cost-gate as the next session's scope** | Recommended, and unchanged by Phase 1 — but the verdict is a split rather than a clean pass, so this is a confirmation the operator should make knowingly rather than one this session records |
| **P-4** | **Confirm the repository visibility switch has been made** | `docs/DECISIONS.md` **D-7**. Measured state at 2026-08-20 was **PUBLIC**; the trigger has fired and the switch is the operator's |
| **P-5** | **Q-3** (reciprocal reviewer) and Paris in-person attendance | Unresolved since G0 |
| **P-6** | **Q-11** — occupy the noise-calibrated tolerance seam, or state it was named and not filled | Unchanged; (b) still recommended, and finding 1.4 gives a second reason not to touch the thresholds |

---

## 10. THE ONE-PARAGRAPH VERSION

The project's first four sessions produced three dead headline claims and one favourable
empirical result; this session attacked that result, which nobody had ever done to anything this
project produced. **The result splits.** `S_B` — ten binned incidence counts, and the set the
composition specification already nominates — separates the simulator's three components under
both the original distortion families and an adversarially constructed alternative, though with a
margin cut from 9.88× to 1.55× and a separation cost forty times higher. **`S_A` does not
generalise**: under the alternative families its condition number rises 25-fold past the
pre-registered ceiling and the verdict flips, so the epidemic-curve result is a statement about
three chosen families rather than about the simulator. The reassurance that the rank call is
tolerance-insensitive turns out to be a fact about having only three components — with six, a
**9% change in the tolerance** moves the rank. Along the way, three of this repository's own
validity flags turned out to be incapable of failing, one of them the flag added to repair
another one that could not fail. **No number G3 computed is wrong, no threshold was revised, and
the two findings that came back favourable are reported at the same weight as the ones that did
not.** What has not changed is the thing that matters most: the MMC composition the project rests
on has still never been attacked by anyone, and this review — by the project, of the project,
in the session that designed it — is not the independent check that gap needs.
