# S6 — Session G6 report

**For a reader who has not seen this session.** Written 2026-08-20.

> ## THE COST GATE FIRED, AND IT FIRED FOR A REASON NOBODY HAD PRICED
>
> **`p_sel` is measured.** Seventh session, three of them having deferred it. 3,780,038 null
> draws, 23 minutes, clean tree. `results/p_sel.yaml`, `results/cost_gate.yaml`,
> `results/COST_GATE_TABLE.md`.
>
> **The verdict is FAIL.** Not "expensive". **Unbounded.**
>
> - **If the nuisance parameters were known, the composition would be comfortably
>   affordable.** At the base parameter point the worst selection cell holds **0.2346** of null
>   draws under `S_B` with the primary all-adversarial assignment (95% CI 0.2320–0.2372), so
>   one MMC test costs **4.2×10⁵ to 4.3×10⁷** draws against a pre-registered gate of 10⁸.
>   **PASS.** It is the only case in this session that passes anything.
> - **They are not known — that is the entire reason Dufour is being composed in — and over the
>   nuisance set the minimum acceptance probability is ZERO.** Zero acceptances in 100,000
>   draws at a relative half-width of **0.05**, the narrowest box measured; 95% upper bound
>   3.84×10⁻⁵; cost at least **2.6×10⁹** draws at the cheapest declared `(M, N)` and
>   **2.6×10¹¹** at the dearest. **FAIL at all four declared corners, under both selection-rule
>   variants, for both family assignments.** `ci_decides_the_gate` is **TRUE**: the measurement
>   is precise enough that the verdict does not move within its own confidence interval.
>
> **The obstruction is structural, not budgetary, and a bigger machine does not touch it.** The
> selection rule has to be a fixed function of the data, because
> `audit/MMC_COMPOSITION_SPEC.md` §3.4's lemma — the composition's only theorem — needs one
> event applied to the observation and to every replicate. The nuisance parameters move the
> normalised summary distribution by a **median of 27 and up to 65 standard deviations** at a
> half-width of 0.05, against a single-draw noise magnitude of √10 ≈ 3.16. **A `θ`-free rule
> facing a shift twenty times the noise selects one component deterministically, and the
> observed cell becomes unreachable.** That is the case §3.4 itself names — *"the rejection
> sampler never terminates there"* — and it now has a number instead of a warning.
>
> **Two things to read with suspicion**, both disclosed in full below and in `DEVIATIONS.md`:
> the statistic the whole measurement is a property of was **chosen by this session**, because
> the specification deferred it (**D-14**); and a flag this session wrote **read FALSE for a
> reason other than the one it named** (**D-15**), which is `DEVIATIONS.md` D-8's failure mode
> committed by the session that had just re-read D-8.

---

## 1. WHAT THIS SESSION DID

| Path | Status |
|---|---|
| `results/p_sel.yaml` | **new numbers** — `p_sel` at the base point (100,000 draws) and at 168 nuisance points across four nested boxes (10,000 draws each), with the 20 lowest re-measured on independent draws at 100,000 each; Wilson intervals throughout; a linearised cross-check; an attribution sanity table |
| `results/cost_gate.yaml` | **new** — the pre-registered gate applied: per-corner costs, propagated uncertainty, three-valued verdicts, the floor at known `θ`, and the demonstration-scale numbers labelled as not part of the gate |
| `results/COST_GATE_TABLE.md` | **new** — generated, so no number in this report is hand-typed (S11) |
| `src/attribution/selection.py` | **new** — the selection rule the specification deferred. The first file in `src/attribution/`, and deliberately the only one |
| `src/diagnostics/p_sel.py` | **new** — the measurement, with its design pre-registered in the docstring and committed before the run |
| `src/diagnostics/cost_gate.py` | **new** — the gate's decision rules, committed before any `p_sel` existed |
| `tests/` | **109 → 140 tests**; of the 31 added, **16** require a check to fail, a bad input to be refused, or a flag to come out both ways |
| `GATES.md` | **G5 signed** per the operator; **G6 added**, unsigned |
| `docs/DECISIONS.md` | **D-12 decided** (Path 1); **D-14** written (the single-mechanism scope restriction, DECIDED) |
| `docs/OPEN_QUESTIONS.md` | **Q-16** raised (blocking); **Q-14 answered** and closed |
| `DEVIATIONS.md` | **D-14** (the `T_k` choice), **D-15** (the mis-named flag) |
| `audit/MMC_COMPOSITION_SPEC.md` | **untouched**, deliberately — the brief's FAIL branch forbids Phase 3, so its superseded 10⁷–10⁹ estimate is left standing and flagged as **O-28** rather than quietly corrected |
| `results/jacobian_rank.*`, `results/robustness/*`, `docs/THRESHOLDS.md` | **untouched.** No threshold revised, no prior number overwritten |

---

## 2. THE MEASUREMENT, AND THE ONE THING IT NEEDED THAT DID NOT EXIST

`audit/MMC_COMPOSITION_SPEC.md` §4 defines `p_sel(θ) = P(k̂(y) = k | θ, η = 0)` and §6 leaves
`T_k` — the statistic `k̂` maximises — *"not specified"* and *"deferred"*. `OUTSTANDING.md`
**O-16** already recorded the consequence in one line: *"One thing must be specified before it
can be measured at all."*

**So the session's first act was to specify it, and that is the largest judgement call in the
session.** `src/attribution/selection.py`: normalise the summary discrepancy, apply the
pseudo-inverse of the recorded summary Jacobian, take the largest component. It discharges §6's
own requirement — *"sensitive to `η_k` and insensitive to `η_j`, which is a statement about the
same Jacobian the diagnostic estimates"* — as an identity rather than an aspiration, since
`J⁺J = I` **is** that sentence written as an equation, and it is measured at machine precision
(`max |J⁺J − I| ≤ 3.6×10⁻¹⁵`). It also satisfies §3.2 (built on a separable set), §5.4
(summaries only) and §3.4 (a fixed function of the data, nothing estimated from `y_obs`).

**The free choice inside it is the scale on which three components are compared**, and there
are two defensible ones — divide by each component's null standard deviation (`studentised`) or
compare on the common `ETA_SCALE` (`plain`). **Studentising raises the smallest cell
probability, and the cost is `1/min p_sel`, so the primary choice is the one favourable to the
gate.** It was nominated primary before any number existed, for a reason written down at the
time: under `plain` the argmax is dominated by whichever component is estimated worst, which is
a bad attributor before it is anything else. **Both variants were measured and both fail**,
which is the only reason the choice is not load-bearing. `DEVIATIONS.md` **D-14**.

### 2.1 The favourable half, and it is genuinely favourable

At the base parameter point the studentised rule does exactly what it was designed to do.

| case | cell probabilities at `θ₀` | worst cell | gate verdict at `θ₀` |
|---|---|---|---|
| `AAA` studentised **(primary)** | 0.2346, 0.3267, 0.4388 | **0.2346** | **PASS**, 4.2×10⁵ – 4.3×10⁷ draws |
| `BBB` studentised | 0.2495, 0.3205, 0.4301 | 0.2495 | **PASS**, 4.0×10⁵ – 4.0×10⁷ draws |
| `AAA` plain | 0.00071, 0.1660, 0.8333 | 0.00071 | **FAIL** |
| `BBB` plain | 0.0241, 0.6115, 0.3644 | 0.0241 | SPLIT |

Two things worth keeping from this table. **The studentised rule balances the cells to within a
factor of two under a condition number of 64.6**, which is the property it was chosen for, and
the `plain` rows show what the alternative costs: the worst-estimated component is selected 0.07%
of the time and the composition would be priced by that. And **the pre-registered gate is
comfortably passed at a known `θ`** — the composition is not intrinsically extravagant.

**A cross-check that could have failed and did not.** The same cell probabilities computed from
the Jacobian alone, under `z ~ N(0, I)`, with no simulator calls at all: 0.2335, 0.3253, 0.4412
against the measured 0.2346, 0.3267, 0.4388. Agreement to three decimal places on every cell of
every case. The linearisation the rule is built on, and the assumption that the normalised
summaries are uncorrelated with unit variance, are both good at `θ₀` — the largest off-diagonal
correlation among the ten binned counts is **0.0083**.

### 2.2 The unfavourable half, which is the session

The specification's cost model is explicit that the relevant `p_sel` is the worst one:

> **`p_sel` is worst-case, not average-case.** The cost is governed by `min over theta of
> p_sel(theta)` across the searched set, not by its value at a plausible `theta`. A nuisance
> value that makes the observed selection unlikely is exactly the one the maximiser is drawn
> toward, because that is where the p-value is largest.

`Ω₀` is not specified anywhere in this project, so a relative box on the five nuisance
coordinates §1 names was declared before the run at half-widths 0.05, 0.10, 0.20 and 0.50, with
**0.20 declared as the headline**. Each box contributes its 32 corners and its 10 axis
endpoints.

| half-width | design points with a dead cell | median worst-cell `p_sel` | best point's worst cell |
|---|---|---|---|
| **0.05** | **21 of 42** | 5×10⁻⁶ | 0.2405 |
| 0.10 | 32 of 42 | **0** | 0.2368 |
| 0.20 | 36 of 42 | **0** | 0.2287 |
| 0.50 | 40 of 42 | **0** | 0.2371 |

**Half the design points at ±5% already have a selection cell that no null draw ever enters.**
The minimum over the headline box is zero acceptances in 100,000 independent draws, and the
95% upper bound of 3.84×10⁻⁵ is what converts that into the reported cost floor of 2.6×10⁹
draws. The verdict is identical for all four cases, and it is unchanged at either end of the
confidence interval.

**The collapse is directional, not merely wide.** At every half-width there are still design
points where all three cells are healthy — the best point at ±50% has a worst cell of 0.2371.
It is not that a large nuisance perturbation destroys the selection event; it is that
**particular directions do, and they do so completely, at perturbations of a few percent.**

---

## 3. THE MECHANISM, MEASURED RATHER THAN ARGUED

Three facts, each independently recorded in `results/p_sel.yaml`:

1. **The rule must be `θ`-free.** §3.4's lemma requires `S_0, S_1(θ_0), …, S_N(θ_0)` to be
   exchangeable *conditional on the same event `E_k`* — one event, applied to `y_obs` and to
   every replicate. A reference point that tracked `θ` would make the replicate acceptance test
   a different event from the one that selected `y_obs`, and the lemma would not apply. This is
   forced by the specification, not chosen here.
2. **The nuisance shift dwarfs the observation noise.** ‖E[z]‖ over the design points has a
   median of **26.5** and a maximum of **64.8** at half-width 0.05, rising to a maximum of
   **11,183** at 0.50. A single null draw has ‖z‖ ≈ √10 ≈ **3.16** by construction, since every
   summary coordinate is divided by its prior-predictive standard deviation.
3. **So the argmax stops being random.** At the point that sets the headline —
   `β = 0.3325, γ = 0.147, ρ = 0.38, I₀ = 9.5, σ_obs = 0.1425`, a 5% move on each — all 100,000
   draws land in the same cell and the other two are empty.

**In one sentence: the observation noise is small compared with what a few percent of nuisance
error does to an epidemic curve, so a selection rule that is not allowed to know `θ` becomes
deterministic, and the cell the data actually selected becomes impossible to sample.**

That is a statement about this simulator's noise-to-nuisance ratio, and it will not be peculiar
to it. **An epidemiologist would not be surprised** that a 5% error in `β` moves a binned
incidence curve by far more than lognormal reporting noise at `σ = 0.15`. The composition's cost
was priced in §4 against Freidling et al.'s measured `1/p_sel ≈ 150`, which is a number from a
setting where the conditioning event stayed reachable. **Nobody checked whether it stays
reachable here, and it does not.**

---

## 4. WHAT THIS NUMBER IS AND IS NOT CONDITIONAL ON

**Conditional on:** the selection rule (**D-14** — a different `T_k` gives a different `p_sel`);
the summary set `S_B`; the base parameter point about which everything is linearised; the box
standing in for `Ω₀`; and a grid, which **understates a minimum**, so the true cost over a
continuous box can only be worse.

**Not conditional on:** the studentisation variant (both fail); the family assignment (both
fail); the confidence interval (the verdict is the same at both ends); or the machine. The last
deserves a sentence, because this session found something that changes future cost estimates
and does not change this one. **Null draws at a fixed `θ` share their entire deterministic
core** — at `η = 0` the RK4 integration, the delay convolution and the reporting multiplier
produce the same array for every seed, and only the noise layer differs. Exploiting that
identity, which is asserted bit-for-bit in `tests/test_p_sel.py`, made a draw cost **0.36 ms**
against the ~0.14 s `GATES.md` G4 recorded for a full run. The gate's own 10⁸-draw threshold is
therefore about **ten core-hours**, not thousands. **It rescues nothing here** — an unreachable
cell is not expensive, it is unreachable — but a future estimate that prices the composition in
wall clock should assume the cheap draw, not the dear one.

### 4.1 A floor on attribution that nobody had noticed

The rule's reference point `m₀` is the prior-predictive mean recorded in
`results/jacobian_rank.S_B.yaml`, estimated from **2000** replicates, so it carries Monte Carlo
error of order `1/√2000 = 0.0224` per normalised coordinate. Propagated through `J⁺`, that lands
as an offset of **0.005 to 0.014 normalised units in `η̂` before any distortion is planted at
all** — and with no distortion whatsoever the rule still names a component, a different one for
each assignment and variant. **This is a floor on what the selection rule can attribute**, it is
a property of the recorded normalisation rather than of the simulator, and it is removable only
by re-estimating `m₀` with more replicates. It is the reason **D-15** exists: the flag that
found it was written to mean something else.

For scale, the rule recovers a planted single-component distortion at **0.05 and 0.1**
normalised units under every assignment and out to **1.0** under the base families. It does
**not** recover one at **0.01** under any assignment, which is the floor above doing its work.
And it stops recovering under the adversarial families beyond **0.25** studentised and beyond
**0.1** plain — that end being nonlinearity rather than the rule, since the Jacobian is a
derivative estimated at a step of 10⁻⁴ and a full normalised unit is four orders of magnitude
further out.

---

## 5. THE SEVEN-SESSION TRAJECTORY

Extending `audit/S5_REPORT.md` §5.

| Session | Claim adopted as headline | Outcome | Killed / qualified by |
|---|---|---|---|
| **G0** | **ex-C2** — attribution identifiable iff the summary Jacobian has full column rank | **DEAD** | Kahl et al. (2019), via Sain & Massey (1969) |
| **G1** | **R1** — calibrate the selection event by rejection sampling from the simulator's null | **DEAD** | Freidling, Zhao & Gao (2024), Algorithm 1 |
| **G2** | **the composite-null gap and its repair** | **DEAD** | Dufour (2006), maximized Monte Carlo |
| **G3** | *(none adopted)* — **R2** checked, having never been a headline | **NARROW-CONDITIONAL** | Cintrón-Arias et al. (2009) + Moré & Wild (2012) |
| **G4** | *(none adopted)* — **G3's own numbers** attacked | **SPLIT: `S_B` stands, `S_A` does not generalise** | this project, for the first time |
| **G5** | *(none adopted)* — **G4's own deferral** closed | **SPLIT: separable at one distortion parameter per component, not at two** | this project, for the second time |
| **G6** | *(none adopted)* — **the composition itself** priced | **FAIL: the rejection sampler does not terminate over the nuisance set** | this project, for the third time — and the first time against the *method* rather than its precondition |

| | G0 | G1 | G2 | G3 | G4 | G5 | **G6** |
|---|---|---|---|---|---|---|---|
| Prior-art check run | yes | yes | yes | yes | n/a | n/a | **n/a** |
| Verdict | DEAD | DEAD | DEAD | NARROW-COND. | SPLIT | WEAKENED | **FAIL** |
| Stopped early by its own rule | no | **yes** | **yes** | no | no | **yes** | **yes** |
| Code written | none | none | none | yes | yes | yes | **yes** |
| Numbers produced | none | none | none | yes | yes | yes | **yes** |
| Adversarial check against own output | no | no | no | no | **yes** | **yes** | **yes** |
| A pre-registered rule fired against the project | — | — | — | no | no | **yes** | **yes** |
| `p_sel` measured | no | no | no | no | no | no | **YES** |
| Something measured about the **composition** | no | no | no | no | no | no | **YES** |
| Independent review | no | no | no | no | no | no | **no** |
| Google Scholar searched | **no** | **no** | **no** | **no** | **no** | **no** | **no** |

### The shape of it, read honestly

**Four sessions have now ended on a stop rule, and three consecutive sessions have found
against the project using the project's own code.** That is the pattern G4 and G5 named, and it
held again. What is different this time is *what* was attacked: G4 and G5 attacked the
diagnostic and the precondition, and both survived in narrowed form. **G6 attacked the thing the
project was actually going to build, and it did not survive.**

**What is genuinely better than it was.** `p_sel` exists, with an uncertainty, from 3.78 million
draws, at a precision that decides the gate at both ends of its interval. The statistic the
specification deferred is written, tested and disclosed. The first line of `src/attribution/`
exists and it is the right line. **O-17**'s older half — *nobody has ever attacked the
composition* — has its first partial payment in seven sessions, by measurement rather than by
argument.

**What is not.** The measurement was taken by the same project, in the same session that wrote
the rule it measures, with no independent eye anywhere. And the thing it found is the kind of
thing a domain reader would have predicted in a sentence: **that a few percent of nuisance error
moves an epidemic curve much more than its reporting noise does.** Nobody in seven sessions
asked that question until the number forced it.

---

## 6. PROCESS CAVEATS — what this session did badly

- **A flag written this session read FALSE for a reason other than the one it named.** It was
  meant to mean "the rule is wrong"; it actually meant "the reference point carries 2000-replicate
  Monte Carlo error". Caught by disbelieving the output, not by any check. **This is
  `DEVIATIONS.md` D-8's failure mode, committed by the session that re-read D-8, D-10 and D-13
  before writing a line of code. D-15.**
- **`T_k` was chosen by a session, not by the operator**, with the cost number hanging off the
  choice, because the measurement was otherwise impossible. **Fourth consecutive session in
  which the right piece of work turns out to have been available earlier than it was done**
  (D-9, D-13, D-14).
- **The boundary was not located.** The collapse is complete at the narrowest box measured, so
  where between `θ₀` and ±5% the cells stop being reachable is **unknown**. It costs about ten
  minutes. It was not run because the brief halts the session on a FAIL and because a check that
  could only soften a verdict, thought of after seeing that verdict, is exactly what D-9 and
  D-13 exist to make visible. **Q-16** states the design and the cost so the operator can order
  it in one line.
- **`audit/MMC_COMPOSITION_SPEC.md` still carries its superseded 10⁷–10⁹ estimate**, for the
  same reason. A specification containing an estimate a measurement has superseded is the
  staleness problem `audit/CLAIM_GRAPH.md` has been flagged for since G2. **O-28.**
- **No literature check ran at all.** By scope. The non-termination of a rejection sampler under
  nuisance drift is not exotic and somebody has written about it; nobody here looked.
- **Google Scholar still not searched.** Seventh session. **O-7.**
- **`audit/CLAIM_GRAPH.md` still stale**; **`results/`** still carries G3's vacuous
  `leakage_checked` literal (**O-22**).
- **The machine was heavily loaded throughout** — load average between 40 and 150 on 8 cores,
  shared with unrelated work — so wall-clock figures are upper bounds on this hardware. The
  draw counts are not affected.

---

## 7. WHAT SHOULD HAPPEN NEXT

1. **Answer Q-16.** It is the only blocking question this session raised and it decides what the
   project's experimental vehicle is. Three options, priced: bound `Ω₀` hard enough to restore
   termination and accept Dufour's own CSEMMC downgrade from finite-sample to asymptotic
   validity; find a selection rule that survives nuisance drift without becoming
   `θ`-dependent (nobody has proposed one, and inventing one after this measurement is the
   leakage failure `LEDGER_DESIGN.md` D3 names); or take the diagnostic-only path of
   `audit/PIVOT.md`. **The recommendation is the third, with this measurement reported as a
   finding rather than as a failure.**
2. **If the composition is to be pursued anyway, run the boundary sweep first.** Ten minutes,
   no new code beyond a command-line argument, and it is the difference between "bound `Ω₀`" and
   "bound `Ω₀` to ±0.4%, which no epidemiologist will accept".
3. **Annotate `audit/MMC_COMPOSITION_SPEC.md` §4** with the measured `p_sel`, preserving the
   original estimate. **O-28.** This session was forbidden to.
4. **Attack the composition properly** — **O-17**'s older half is now partly paid and still
   unpaid as *criticism*. What this session did is measure it, which is not the same as somebody
   trying to break it.
5. **Close Q-15 cheaply** — still re-analysable from recorded columns, still not done.

### 7.1 A requirement that must not be lost between here and the paper

**`docs/DECISIONS.md` D-14 is DECIDED and it lands on a file that does not yet exist.** The
paper's scope is restricted to **single-mechanism-per-component** misspecification, and the
operator's instruction is explicit that this is *"a real limitation to be stated alongside the
positive result, not buried after it"*. **Whichever session first drafts `paper/main.tex` must
put that restriction in the scope or limitations section, and must state the six-column
counterexample rather than omit it.** No session has drafted `paper/main.tex`; the drafting
session will be several sessions downstream of the measurement that produced the restriction;
this paragraph exists so the requirement survives the distance. D-14 lists all four places the
obligation lands.

---

## 8. POINTS REQUIRING OPERATOR INPUT

| # | Point | Notes |
|---|---|---|
| **P-1** | **Sign or reject G6** | `GATES.md`. The "does not certify" section is the part that matters, and its first item is that `p_sel` is a property of a statistic this session chose |
| **P-2** | **Answer Q-16** — is the MMC composition still the vehicle? | **BLOCKING.** The cost gate failed on non-termination. Three options, priced in Q-16; the recommendation is the diagnostic-only path, offered as a recommendation and not as a decision |
| **P-3** | *(closed)* | Authorisation to build the composition was contingent on a PASS. The gate failed, so there is nothing to authorise until P-2 is answered |
| **P-4** | **Q-3** (reciprocal reviewer), Paris in-person attendance | Unresolved since G0 |

*Q-13 remains open and blocking for the paper's separability sentence. Q-14 is closed — the
operator answered it at the start of this session and it is recorded as `docs/DECISIONS.md`
D-14. Repository visibility is settled by D-11 and is not on this list.*

---

## 9. THE ONE-PARAGRAPH VERSION

The number this project has deferred for three sessions now exists, and it says the composition
cannot be run. **At a known parameter point it would be comfortably affordable** — the worst
selection cell holds 23% of null draws and one test costs between 4×10⁵ and 4×10⁷ simulator
draws against a gate of 10⁸. **But the parameters are not known, which is the entire reason
Dufour's maximisation is in the design, and over the nuisance set the acceptance probability is
zero**: no draw in 100,000 enters the observed cell at a five-percent perturbation, half the
design points at that width have a dead cell, and the cost is unbounded rather than large.
**The reason is structural.** The selection rule is required by the composition's own lemma to
be a fixed function of the data, the nuisance parameters shift the normalised summaries by a
median of 27 standard deviations where the noise supplies about 3, and a rule that cannot see
`θ` therefore selects deterministically — which is the specification's own named case of a
rejection sampler that never terminates. **No machine fixes that.** The measurement is
conditional on a statistic this session had to choose because the specification deferred it,
and on a nuisance box nobody has ever specified, and both are disclosed as the largest
judgements in the session. What it is not conditional on is the confidence interval, the
studentisation, or the family assignment: **every case fails, at every declared corner, at both
ends of the interval.** Seven sessions in, the project has a diagnostic that works, a
precondition that holds inside a stated scope, and — for the first time — a measured reason to
doubt the method it was built to enable.
