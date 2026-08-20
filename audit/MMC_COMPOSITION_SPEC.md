# MMC + selection event — specification, not an implementation

**Session G3, 2026-08-20. SPECIFICATION ONLY.** Nothing in this document was built or run
this session, by instruction. It exists so that the next session builds a thing that was
specified before its results were known, rather than specifying a thing after building it.

The composition: **Dufour's maximized Monte Carlo, maximised over the nuisance parameters
implied by this project's simulator, composed with a selection event over the K = 3
components.** It is the one unoccupied cell `audit/COMPOSITE_NULL_CHECK.md` §5 identified,
and it is stated here at the size that check gave it, not larger.

---

## 0. THE THREE THINGS THAT GO AT THE TOP, NOT IN A FOOTNOTE

The first three sessions of this project each adopted a headline that overstated what it
had. These three statements are the opposite failure mode, and they belong in the paper's
abstract, not in its limitations section.

### 0.1 It is a composition of two published techniques, not a new theorem

Freidling, Zhao & Gao (2024) supply the selection-cell sampler; Dufour (2006) supplies the
nuisance maximisation. **Neither requires modification to sit next to the other.** The
paper's only actual theorem is the short lemma in §3.4 below, and that lemma is easy. A
paper that presented this as a new inferential mechanism would be the fourth consecutive
overstatement in this project's record.

### 0.2 It is conservative by construction — exact LEVEL, not exact SIZE

Dufour says so himself, in the paper being composed against:

> *"As one would expect for a statistic whose distribution depends on unknown nuisance
> parameters, **the probability of type I error for a MMC test can be lower (but not higher)
> than the level of the test and the procedure can be conservative**."*
> — CIRANO WP 2005s-02, §1

Under the composition there are **two** independent sources of conservativeness, and they
compound:

1. **The supremum over the nuisance space.** The test rejects only if the p-value is small
   at *every* admissible nuisance value. The wider the nuisance set, the more conservative.
2. **The discreteness of the Monte Carlo p-value.** Proposition 4.1's bound is
   `I[α(N+1)]/(N+1)`, an integer-floor expression: it is an *inequality*, where the
   fixed-nuisance Proposition 2.2 gives an *equality*. Dufour flags exactly this difference
   himself: *"the validity results of propositions 4.1 and 4.2 differ from those of the
   corresponding propositions 2.2 and 2.4 in the sense that **equalities have been replaced
   by inequalities**."*

**Consequence for how the paper may be written.** No sentence of the form "simulators make
selective inference exact" is available. The correct claim is *level control without
regularity conditions, at a stated and large computational price, with conservativeness that
is not quantified in general*. `audit/COMPOSITE_NULL_CHECK.md` §5 point 4 already recorded
that a headline containing the word "exact" cannot rest on a procedure whose own author
calls it conservative.

### 0.3 The cost multiplies. It does not amortise.

Stated in full in §4. In one line: the rejection-sampling cost `1/p_sel` is paid **at every
nuisance value the maximisation visits**, so the total is `M × N / p_sel`, not `N / p_sel`
plus a search. For a simulated-annealing search with `M ~ 10^3`–`10^4` evaluations and
Freidling et al.'s own measured `1/p_sel ~ 150`, the multiplier over a plain Monte Carlo test
is of order `10^5`–`10^6`. **This is the property most likely to make the composition not
worth building, and it must be established before it is built, not after.**

---

## 1. THE INFERENTIAL PROBLEM

A simulator generates data through

    y = g(theta, eta, u),      u ~ known distribution, simulable

where

- `theta` are the **nuisance parameters** — here the base epidemiological parameters of
  `src/simulators/sir3.py` (`beta`, `gamma`, `rho`, `I0`, and the observation-noise scale).
  They are unknown. This is what makes the null composite.
- `eta = (eta_1, eta_2, eta_3)` are the **component distortions**, one per component of the
  declared decomposition (TRANSMISSION, PROGRESSION, OBSERVATION). `eta = 0` is "the
  simulator is correctly specified".
- `u` is randomness with a known, simulable distribution.

We do not know in advance which component is misspecified, so we look at the data and pick
one. Let `T_k(y)` be a per-component discrepancy statistic and let

    k-hat(y) = argmax_k T_k(y)

be the selected component. The hypothesis of interest is chosen *after* seeing the data:

    H_0 :  eta_{k-hat} = 0,      theta in Omega_0 (unrestricted, unknown).

Testing `H_0` with the marginal null distribution of `T_{k-hat}` is invalid — this is the
opening example of the selective-inference literature and `audit/S0_REPORT.md` §2 already
records ex-C1's death on exactly that point. The valid object is the law of `T_{k-hat}`
**conditional on the selection event**

    E_k = { y : k-hat(y) = k }.

**Two obstructions, and each already has a published answer.**

| Obstruction | Published answer | Why it applies here |
|---|---|---|
| `E_k` has no analytic characterisation (`argmax` of three nonlinear functionals of a simulator's output) | **Rejection sampling** — Freidling, Zhao & Gao (2024), arXiv:2405.07026, Algorithm 1, for *"arbitrary treatment assignment schemes and conditioning events"* | The simulator can draw from its own null, so the cell can be sampled rather than described |
| The null is **composite**: the conditional law depends on the unknown `theta` | **Maximized Monte Carlo** — Dufour (2006), Proposition 4.1 | The null law *"can be simulated once the nuisance parameters have been specified"*, which is what a simulator is |

Neither answer is this project's. The composition of the two is what is unoccupied.

---

## 2. THE MMC PROCEDURE BEING COMPOSED AGAINST — CITED, NOT PARAPHRASED

> **Jean-Marie Dufour**, *"Monte Carlo tests with nuisance parameters: A general approach to
> finite-sample inference and nonstandard asymptotics"*, *Journal of Econometrics* **133(2)**:
> 443–477 (2006), DOI `10.1016/j.jeconom.2005.06.007`.
>
> **VERSION USED: CIRANO Working Paper 2005s-02**, <https://cirano.qc.ca/files/publications/2005s-02.pdf>,
> retrieved and read in full (17,308 words; control `the` = 565; `nuisance` 56, `MMC` 26,
> `"maximized Monte Carlo"` 5). **The version of record has NOT been obtained** — *J.
> Econometrics* is paywalled and both Unpaywall and OpenAlex report `closed`. Every statement
> below is attributed to the working paper. **O-14 stands: the VoR must be obtained before
> MMC is cited in any manuscript**, because a preprint is not a substitute for the version of
> record when a specific proposition is being attributed.

### 2.1 The setup (Dufour §4, eqs. 4.10–4.13)

`S_0` is the test statistic on the observed data at the true `theta_0`; `S_1(theta), ...,
S_N(theta)` are i.i.d. simulated replications of the statistic under parameter `theta`. The
assumption Prop. 4.1 needs is **exchangeability at the true parameter**:

> *"the variables S_0, S_1(theta_0), ... , S_N(theta_0) are **exchangeable** for some theta_0
> in Omega, each one with distribution function F[x | theta_0]."*  (4.11)

And the simulation representation is written in exactly the form a simulator has:

> *"In parametric models, the statistic S will usually be simulated by first generating an
> 'observation' vector y according to an equation of the form* **y = g(theta, u)** *where u
> has a known distribution (which can be simulated) and then computing S(theta) ≡ S[g(theta,
> u)]."*  (4.12)–(4.13)

**This is the composability hook and it is exact, not analogical.** `src/simulators/sir3.py`
is literally `y = g(theta, eta, u)` with `u` a seeded standard-normal vector.

### 2.2 The proposition (Dufour Prop. 4.1), which is the thing being cited

> **Proposition 4.1 — VALIDITY OF MMC TESTS WHEN TIES HAVE ZERO PROBABILITY.** Under the
> assumptions and notations (4.10), (4.11) and (4.16)–(4.18), set `S_0(theta_0) = S_0` and
> suppose `P[S_i(theta_0) = S_j(theta_0)] = 0` for `i != j`. If `theta_0` is in `Omega_0`,
> then for `0 <= alpha_1 <= 1`,
>
>     P[ sup{ G-hat_N[S_0 | theta] : theta in Omega_0 } <= alpha_1 ]  <=  (I[alpha_1 N] + 1)/(N + 1)      (4.20)
>
> and
>
>     P[ sup{ p-hat_N[S_0 | theta] : theta in Omega_0 } <= alpha ]  <=  I[alpha(N + 1)]/(N + 1)            (4.21)

Dufour's own gloss on what (4.20) buys:

> *"the critical region `sup{G-hat_N[S_0 | theta] : theta in Omega_0} <= alpha_1` **has level
> alpha irrespective of the presence of nuisance parameters** in the distribution of the test
> statistic S under the null hypothesis H_0. ... We shall call such tests **maximized Monte
> Carlo (MMC) tests**."*

**Proposition 4.2** relaxes the no-ties assumption (4.19) via an auxiliary randomisation, and
is the one to cite if `T_k` can tie — which, for an `argmax` over three continuous
statistics, it will not, but the paper should say so rather than assume it.

### 2.3 How the maximisation is actually performed — Dufour's own words

This matters for §4's cost accounting and is routinely glossed over:

> *"The function `G-hat_N[S_0 | theta]` ... is then maximized with respect to `theta` in
> `Omega_0` **keeping the observed statistic S_0 and the simulated disturbance vectors
> u_1, ..., u_N fixed**. The function `G-hat_N[S_0 | theta]` is a **step-type function** which
> typically has **zero derivatives almost everywhere**, except on isolated points (or
> manifolds) where it is not differentiable. Further, the supremum ... is typically not
> unique ... **So it cannot be maximized with usual derivative-based algorithms.** However,
> the required maximizations can be performed by using appropriate optimization algorithms
> that do not require differentiability, **such as simulated annealing**."*

Two consequences the composition inherits and must state:

- **The maximisation is derivative-free.** No gradient method applies, so the number of
  nuisance evaluations `M` is large — that is the whole content of §4.
- **The simulated disturbances `u_1,...,u_N` are held fixed across `theta`.** This is a
  common-random-numbers construction, and it is the *same* device the rank diagnostic uses
  for a different reason (`src/diagnostics/jacobian_rank.py`). Under the composition it does
  **not** remove the rejection cost, because the *acceptance* of a draw into the selection
  cell depends on `theta`, so the accepted subset changes even when `u` does not. **This is
  the specific reason the cost does not amortise, and §4 turns on it.**

### 2.4 Dufour's one free lunch, which the composition should use

> *"if a **pointwise** MC p-value is larger than the level alpha of the test ... it is clear
> that the **maximized p-value must be larger than alpha** (so that the maximized MC test is
> not significant at level alpha)."*

An early exit: evaluate at any single `theta` first; if that p-value already exceeds `alpha`,
stop, because the supremum can only be larger. This costs one nuisance evaluation and
short-circuits every non-rejection. It does **not** help the rejection case, which is the
expensive one and the one that matters.

---

## 3. THE COMPOSITION

### 3.1 The procedure, stated as an algorithm

Given observed data `y_obs`, a level `alpha`, a replication count `N`, and a nuisance set
`Omega_0`:

1. **Select.** Compute `k = k-hat(y_obs) = argmax_j T_j(y_obs)`. Record the selection event
   `E_k`. Set `S_0 = T_k(y_obs)`.
2. **For each candidate `theta` in `Omega_0` visited by the maximiser:**
   a. Draw simulator replicates `y_i = g(theta, eta = 0, u_i)` under the null.
   b. **Reject-sample the selection cell:** keep only those `y_i` with `k-hat(y_i) = k`.
      Continue drawing until `N` are accepted.
   c. Form `S_i(theta) = T_k(y_i)` on the `N` accepted draws.
   d. Compute the conditional simulated p-value `p-hat_N[S_0 | theta, E_k]` by Dufour (2.16).
3. **Maximise.** `p-hat_MMC = sup{ p-hat_N[S_0 | theta, E_k] : theta in Omega_0 }`, by a
   derivative-free method (§2.3).
4. **Reject** `H_0 : eta_k = 0` iff `p-hat_MMC <= alpha`.

Step 2b is Freidling et al.'s Algorithm 1. Steps 2d–4 are Dufour's Proposition 4.1. **Step 2
is the composition: the rejection sampling sits inside the maximisation loop.**

### 3.2 What the diagnostic supplies

`T_k` must be built from a summary set under which the components are actually separable —
otherwise the test is well-calibrated about a quantity that is not identified. That is what
`results/jacobian_rank.*.yaml` decides, and it is why the diagnostic is a precondition rather
than a side-quest. See §5.

### 3.3 What is genuinely new, at its true size

The object *"a selective p-value that is rejection-sampled within the selection cell and
maximised over the nuisance space to restore exact level"* appears not to have been written
down: full-text `"selection event" "maximized Monte Carlo"` returns **0**, re-verified on the
corrected instrument in G2, and Freidling et al. cite none of Dufour, Barnard or Dwass
(`Dufour` 0, `"Maximized Monte Carlo"` 0, `Barnard` 0, `Dwass` 0 in their full text).

That is the whole of the novelty. It is a composition, and §0.1 says so first.

### 3.4 The lemma that must actually be proved — and why it is easy

**The composition is not free of content.** Proposition 4.1 requires (4.11): `S_0,
S_1(theta_0), ..., S_N(theta_0)` exchangeable with common distribution `F[x | theta_0]`. The
composed procedure applies it to the **conditional** law given `E_k`, so what must hold is

    S_0, S_1(theta_0), ..., S_N(theta_0)  exchangeable under  P[ . | theta_0, E_k ],
    each with distribution  F[x | theta_0, E_k].

**Sketch of why it goes through.** Under `H_0` the observed `y_obs` is a draw from
`P_{theta_0}` and we condition on the *observed* selection `E_k`; each accepted replicate is,
by construction of the rejection sampler, a draw from `P_{theta}` conditioned on the *same*
event `E_k`. At `theta = theta_0` these are the same law, and the accepted draws are i.i.d.,
so the (N+1)-tuple is exchangeable. Proposition 4.1 then applies verbatim with `F[x | theta]`
replaced by `F[x | theta, E_k]`.

**Two conditions this sketch quietly uses, both of which the paper must state:**

- `P(E_k | theta) > 0` for every `theta` in `Omega_0`. If some admissible nuisance value makes
  the observed selection impossible, the rejection sampler never terminates there. The
  maximiser must treat such `theta` explicitly rather than hang.
- The selection rule `k-hat(.)` must be a **fixed, deterministic function of the data**, the
  same one applied to `y_obs` and to every replicate. Any data-dependent tuning of `T_k`
  (a bandwidth, a normalisation estimated from `y_obs`) breaks it.

**This lemma is the paper's only theorem, and it is a short one.** Saying so plainly is the
point of this document. A reader who expects a hard result here should be told in the
abstract that there isn't one.

---

## 4. COST — STATED MULTIPLICATIVELY

Let

- `N` = accepted replicates per nuisance evaluation (Dufour's `N`; `N = 99` or `999` typical),
- `p_sel(theta) = P(k-hat(y) = k | theta, eta = 0)` = probability a null draw lands in the
  observed selection cell,
- `M` = number of nuisance values the derivative-free maximiser evaluates.

**Simulator draws required:**

    E[ draws ]  =  M  x  N  /  p_sel(theta)        <- per nuisance value, MULTIPLIED

not `N / p_sel + (cost of a search)`. The rejection cost is paid **again at every `theta`**,
because the acceptance test `k-hat(y_i) = k` depends on `theta` through the law of `y_i`.
Holding `u_1, ..., u_N` fixed across `theta` (§2.3) does **not** amortise it: the same `u`
mapped through a different `theta` lands in a different cell.

**Order of magnitude, from the literatures' own measured numbers.**

| Factor | Value | Source |
|---|---|---|
| `1 / p_sel` | ~150 | Freidling et al. measure this in their own experiments; recorded in `audit/R1_THREAT_CHECK.md` and `audit/S1_REPORT.md` |
| `N` | 99–999 | Dufour's standard choice |
| `M`, simulated-annealing evaluations | 10^3–10^4 | derivative-free search over a continuous `Omega_0`; Dufour names simulated annealing (§2.3) |
| **Product** | **~10^7–10^9 simulator draws** | |

For comparison, `audit/S0_REPORT.md` §7 already prices this project's *entire* protocol at
10^6–10^7 simulations, and `docs/DECISIONS.md` records H1 (10^4–10^5 runs) as **dead as
stated** for that reason.

**Three things follow, and they are the substance of whether this gets built.**

1. **`p_sel` is worst-case, not average-case.** The cost is governed by
   `min over theta of p_sel(theta)` across the searched set, not by its value at a plausible
   `theta`. A nuisance value that makes the observed selection unlikely is exactly the one
   the maximiser is drawn toward, because that is where the p-value is largest.
2. **`Omega_0` must be bounded, and bounding it costs the exactness.** Dufour's own §5
   (CSEMMC) replaces `Omega_0` with a consistent *set estimate*, which is **asymptotically**
   valid — trading away precisely the finite-sample exactness that motivates MMC. If the
   composition needs CSEMMC to be affordable, the paper's claim weakens from finite-sample to
   asymptotic and must say so.
3. **The dimension of `theta` is the binding constraint, not `K`.** `K = 3` is small. The
   simulator's nuisance vector is 5-dimensional as specified. `M` grows with `dim(theta)`,
   so the cost is set by the *nuisance* dimension. `audit/COMPOSITE_NULL_CHECK.md` §5 point 3
   put it as *"for a simulator with more than a couple of nuisance dimensions this is not a
   budget problem so much as a different project."* That judgement stands and this
   specification does not soften it.

**A pre-registered cost gate, so this is decidable rather than arguable.** Before any
implementation, the next session should measure `p_sel` directly — it is cheap, needing only
null draws and the selection rule, with no MMC at all — and record it. **If
`M x N / min_theta p_sel` exceeds 10^8 simulator draws at the demonstration's scale, the
composition is not affordable on the declared budget and the honest output is the cost
analysis itself**, not a scaled-down experiment that hides it. Recording that threshold here,
before the number exists, is the same device `docs/THRESHOLDS.md` used for the rank
tolerance.

---

## 5. WHAT WOULD NEED TO BE TRUE OF PHASE 2'S RESULTS

The composition is only worth building where component attribution is **well posed**. If no
summary set separates the components, an exactly-calibrated test would be exactly calibrated
about a quantity the data do not identify — which is worse than a miscalibrated test about a
well-posed one, because it looks correct.

**The pre-registered conditions, in order:**

1. **At least one summary set must be separable** — full column rank at `tau = 1e-2` and
   condition number within `kappa_max = 100` (`docs/THRESHOLDS.md` §1.3). If the D4 STOP
   condition fires, the composition is **not** built and the project's output is the negative
   identifiability result.
2. **The h-plateau must exist** for that set (R2a), or the rank verdict is not defensible in
   the first place.
3. **No component may be invisible** to that set (`||J_.k|| >= 0.1`, THRESHOLDS §1.5). A
   component invisible to the summaries cannot be selected *or* tested, and a selection event
   over a component that cannot be seen is not a selection event.
4. **The chosen set's `T_k` must be computable from summaries only**, since the rejection
   sampler evaluates `k-hat` on every replicate and cannot afford anything expensive.

**Outcome of Phase 2, this session.** Recorded in `results/jacobian_rank.*.yaml` and
tabulated in `results/SUMMARY_TABLE.md` — generated from those files, not typed. In words:
**the STOP condition did not fire**, two of the three summary sets are separable under the
pre-registered criteria, and the impoverished control `S_C` failed exactly as designed, with
an *exact* null direction rather than a near-null one.

**Which set the composition should use, and the one caveat.** `S_B` (ten time-binned
incidence counts) is the natural choice: it is separable, it is what an SBI practitioner
would use, and its coordinates are cheap. `S_A` is separable with a smaller condition number
and is the better-conditioned option; the trade-off is that `S_A`'s peak statistics require
the parabolic interpolation described in `src/simulators/summaries.py`, which the rejection
sampler must then evaluate on every replicate. **This choice is not made here** — it depends
on the `p_sel` measurement of §4, which has not been run.

> #### Correction, session G4 (2026-08-20) — the paragraph above is left unedited and one of its
> #### sentences is now known to be false
>
> **"`S_A` … is the better-conditioned option" is true of one distortion family set and was
> written as though it were a property of the summary set.** Under the adversarial family triple
> of `audit/G3_ADVERSARIAL_REVIEW.md` finding 2 the ordering **reverses**: `S_A` becomes
> INSEPARABLE while `S_B` remains separable. Numbers in `results/robustness/`.
>
> **This strengthens `S_B` as the recommendation and removes `S_A` as the alternative**, so the
> paragraph's conclusion survives while its reason does not. Two things a reader planning the
> next session needs:
>
> - **`S_B`'s separation cost under the adversarial families is about forty times the base
>   figure** (`κ` rises from 10.12 to 64.62, and §1.2 of `docs/THRESHOLDS.md` prices separation
>   at `~κ²` replicates). The cost gate pre-registered in §4 above should be evaluated against
>   both numbers, not just the favourable one.
> - **`S_A`'s peak-height coordinate is not a continuous function of `η`**
>   (`audit/G3_ADVERSARIAL_REVIEW.md` finding 4), which is an additional reason not to build the
>   rejection sampler around `S_A` — the sampler would evaluate that coordinate on every
>   replicate.
>
> **Nothing in this specification was implemented, and none of it is implemented now.** This
> block is a factual correction to a statement about existing results, added because leaving a
> known-false sentence in a specification the next session is meant to build from is the failure
> mode `audit/CLAIM_GRAPH.md` has been flagged for since G2.

**The caveat that must not be dropped.** Separability was established for **this simulator,
these three distortion families, and this closed list of summary sets**. The observation
distortion in particular is a pure reporting-fraction multiplier; a different observation
distortion (perturbing the reporting *delay* instead) would give a different third column and
could give a different verdict. That limitation is recorded in the results files and is not
softened by the fact that the verdict came out favourably.

---

## 6. WHAT THIS SPECIFICATION DOES NOT DO

- **It was not implemented.** No MMC code exists. No selection event has been sampled. No
  `p_sel` has been measured. Session G3's brief is explicit that Phase 3 is specification only
  and that the composition is the next session's work.
- **It has not been threat-checked as a claim.** `audit/COMPOSITE_NULL_CHECK.md` §5 found the
  cell unoccupied on a phrase-level search and immediately gave four reasons it is not a
  paper. **Nobody has since tried to refute the composition itself**, and no adversarial
  critic has run in this project in four sessions.
- **It rests on a working paper, not the version of record.** O-14.
- **It assumes `T_k` exists and is sensible.** The per-component discrepancy statistic is
  named `T_k` throughout and is **not specified**. Choosing it is a real design problem —
  it must be sensitive to `eta_k` and insensitive to `eta_j`, which is a statement about the
  same Jacobian the diagnostic estimates — and it is deferred.
