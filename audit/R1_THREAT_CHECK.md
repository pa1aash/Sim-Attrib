# R1 threat check — is the rejection-sampling mechanism prior art?

**Session G1, 2026-08-20.** Written to the standing instruction carried from G0's canonical
query: **the strongest case against novelty is stated first, before any case for it.**

R1 is the claim promoted to the paper's headline by `docs/DECISIONS.md` **D-3**:

> "in simulation-based settings, exact conditional inference given a selection event
> requires no analytic characterisation of that event, because the selection event can be
> calibrated by rejection sampling from the simulator's own null. This removes the
> obstruction Liu, Markovic-Voronov & Taylor (2023) identify as the central barrier to
> conditional selective inference."

---

# VERDICT: **DEAD**

**The mechanism is prior art.** Not adjacent, not anticipated-in-spirit — published,
implemented, named, and costed, with the identical cost analysis. It exists in the
randomization-inference literature as a titled algorithm, it is catalogued as a known
strategy in the April 2026 review of the field, and the specific paper D-3 names as
identifying the barrier does not identify a barrier: **it removes it.**

Both clauses of D-3's sentence are false as written.

A residual survives. It is small, it is a *transfer* rather than a mechanism, and it is
described in §6 — after the case against.

---

## 1. THE STRONGEST CASE AGAINST R1

### 1.1 Freidling, Zhao & Gao — the mechanism, as a named algorithm

> **Tobias Freidling, Qingyuan Zhao & Zijun Gao**, *"Selective Randomization Inference for
> Adaptive Experiments"*, **arXiv:2405.07026v4** (22 May 2026). Retrieved and read in full
> (20,339 words).

Their abstract:

> *"our approach applies **conditional post-selection inference to randomization tests**
> … we derive a **selective randomization p-value that controls the selective type-I
> error**. As inference only relies on the randomness in the treatment assignment, **no
> modelling assumptions or independent and identically distributed data are needed**. We
> elaborate on conditions that render the proposed p-value computable and provide
> **rejection sampling** and MCMC algorithms to find a Monte Carlo approximation."*

Their Supplementary §S3.2 is headed **"Rejection Sampling"** and **Algorithm 1** is titled
**"Rejection sampling"**. The procedure, verbatim:

> *"Rejection sampling is a versatile procedure that allows for **arbitrary treatment
> assignment schemes and conditioning events**. In every step of the algorithm, we generate
> a sample Z\* from the non-selective randomization distribution. If Z\* is feasible, i.e.
> Z\* ∈ Z_{S(Z),G(Z)}, we **accept** it; otherwise, Z\* is **rejected**."*

Draw from the exact null → apply the selection rule → keep the draws landing in the
selection cell. That is R1's construction, term for term.

**They also derive R1's cost claim, in the same form.** S0_REPORT.md §2 states R1's cost as
"~N_alt/α draws". Freidling et al.:

> *"Suppose the success probability P(Z\* ∈ Z_{S(Z),G(Z)} | …) equals p₀; then the
> **expected number of draws required to obtain one acceptable treatment is 1/p₀**."*

And they measure it: *"the conditional randomization test with rejection sampling takes
around **150 times longer** than the Monte Carlo approximation of the randomization test
without conditioning; in other words, roughly only one out of 150 proposals is accepted."*

**Overlap: total.** The only difference is the *source* of the exact null — treatment
randomization by design, rather than a simulator. The construction, the guarantee
(selective type-I error), the freedom from analytic characterisation, the freedom from
modelling assumptions, and the cost analysis are all the same.

**Verdict: DEAD.**

### 1.2 Neufeld, Perry & Witten — it is in the review, with the objection already stated

> **Anna Neufeld, Ronan Perry & Daniela Witten**, *"Inference conditional on selection: a
> review"*, **arXiv:2604.09779** (10 April 2026).

G0 lists this review among the sources it searched against R1. Its §3.1 says:

> *"in general, developing an analytical characterization for a selection event is a
> time-consuming task that must be re-done each time a new selection event is considered."*

and, immediately, the alternative:

> *"In practice, it is often the case that the distribution of T_{S(Y)}(Y) | {S(Y)=k} is
> **intractable for inference** … In such a setting, it may be fruitful to apply a **Monte
> Carlo strategy**; however, this is **not always applicable** and is **typically quite
> inefficient**."*

The field's April-2026 review names the strategy, and states the two standard objections to
it. R1 is not an unnoticed opening; it is a known option with known drawbacks.

Worse for the framing: the review's **Example 1 is inference on a "winner"** — the
`argmax` selection event, i.e. structurally R1's demonstration — used as one of three
canonical motivating examples.

**Verdict: DEAD.**

### 1.3 Liu, Markovic-Voronov & Taylor — the paper D-3 cites is the paper that refutes it

> **Sifan Liu, Jelena Markovic-Voronov & Jonathan Taylor**, *"Black-box Selective Inference
> via Bootstrapping"*, **arXiv:2203.14504v2** (20 Aug 2023). Retrieved and read in full
> (9,699 words).

This is the "Liu, Markovic-Voronov & Taylor (2023)" of D-3 and of `S0_REPORT.md` §2 —
authors, year and topic all match. **It is not a statement of a barrier. It is a solution
to one.** Its abstract:

> *"Conditional selective inference requires an exact characterization of the selection
> event, which is often unavailable except for a few examples like the lasso. **This work
> addresses this challenge** by introducing a generic approach to estimate the selection
> event … The method proceeds by **repeatedly generating bootstrap data and running the
> selection algorithm on the new datasets** … This leads to an estimate of the distribution
> of the data conditioned on the selection event … demonstrated through a variety of
> problems that **lack exact characterizations of selection, where conditional selective
> inference was previously infeasible**."*

G0 quoted the paper's first sentence — the problem statement — and reported it as the
paper's finding. The rest of the abstract removes the obstruction that D-3 claims R1
removes.

**What is genuinely different.** Their guarantee is **asymptotic**, not exact — Theorem 4.5
gives *"an asymptotic coverage probability of 1 − α"* under Assumption 4.1 (asymptotic
normality of the pre-selection distribution), Assumption 4.3 (**smooth** selection
probability), and accurate estimation of that probability. They estimate the selection
probability as a learned function of summary statistics. R1's rejection sampling needs none
of that. **This is the whole of R1's surviving distinctness, and it is a distinction in
regularity conditions, not in mechanism.**

**Verdict: DEAD on "no analytic characterisation"; the exactness gap is real and is §6.**

### 1.4 Liu & Panigrahi — a third independent removal of the same obstruction

> **Sifan Liu & Snigdha Panigrahi**, *"Flexible Selective Inference with Flow-based
> Transport Maps"*, **arXiv:2506.01150v1** (1 June 2025).

> *"existing data-carving approaches typically require an analytically tractable
> characterization of the selection event. This paper introduces a new method that leverages
> tools from flow-based generative modeling to approximate a potentially complex conditional
> distribution, **even when the underlying selection event lacks an analytical
> description** … **without imposing any further restrictions on the nature of the selection
> event**."*

A third published route past the same obstruction, by generative modelling. Together with
§1.1 and §1.3 this establishes that "conditional selective inference without an analytic
characterisation of the selection event" is **an active sub-literature with at least three
distinct solutions**, not an open problem.

**Verdict: NARROWS — and it removes any claim that the obstruction is open.**

### 1.5 Tian & Taylor — sampling the conditional law, but only after characterising it

> **Xiaoying Tian & Jonathan Taylor**, *"Selective inference with a randomized response"*,
> **Annals of Statistics** 46(2):679–710 (2018); **arXiv:1507.06739**. Retrieved and read
> (16,670 words). Term counts (`grep -a`, control "the" = 1,062): "selection event" 24,
> "Monte Carlo" 2, "rejection sampling" **0**.

2.3 named this as the most likely home of R1's mechanism in the general literature. It is
**not**, and the reason is precise. They do sample the conditional law — *"we use a
Gibbs-type sampler, which iterate[s] over y, y_inter, y_CV and y_select, conditional on the
other three and the selection event"* — but sampling is available to them **because the
selection event has already been characterised analytically**:

> *"the selection events in (20) are **polyhedrons** and thus a hit-and-run or Hamiltonian
> Monte Carlo algorithm … can be used for sampling."*

Analytic characterisation first, sampling second. The randomization there is added noise for
power, not a device for avoiding characterisation.

**Verdict: NARROWS.** Sampling-based computation of the selective law is standard; doing it
*without* a characterisation is the part §1.1–§1.4 have already taken.

---

## 2. RANKING AND SELECTION — the literature G0 never checked

This was flagged in the session brief as "a first-class risk to R1, not a footnote". **It is
not the risk.** The risk was in selective inference all along.

### 2.1 Kim & Nelson — the canonical tutorial

> **Seong-Hee Kim & Barry L. Nelson**, *"Selecting the Best System: Theory and Methods"*,
> **Proceedings of the 2003 Winter Simulation Conference**, pp. 101–112.
> <https://informs-sim.org/wsc03papers/013.pdf> — retrieved and read in full (9,010 words).

R&S guarantees are obtained by **analytic bounding under a normality assumption**, which is
the opposite of R1's route. Their own statement of the method:

> *"A theme that runs throughout much of R&S is first using appropriate **standardization of
> estimators** and then **bounding the resulting probability statements** in such a way that
> a difficult multivariate probability statement becomes one that is **readily solvable**."*

The machinery is **Slepian's inequality** (Theorem 4 in their §2), **Kimball's inequality**,
and **Bonferroni** — applied to multivariate normal order statistics. Term counts
(`grep -a`, control "the" = 624): "selection event" **0**, "rejection sampling" **0**,
"post-selection" **0**, "conditional" 1, Slepian 3, Bonferroni 3.

**And the conditioning is on a different thing.** The indifference-zone guarantee is
`Pr{select k | μ_k − μ_{k−1} ≥ δ} ≥ 1 − α`. That conditions on **the parameter
configuration**, not on the selection event. PCS is a *marginal* probability over the
randomness of selection; conditional selective inference asks a question **given which
system was selected**. These are different guarantees, and R&S does not compute the latter.

**Verdict: SAFE.**

### 2.2 Hong, Fan & Luo — the modern review

> **L. Jeff Hong, Weiwei Fan & Jun Luo**, *"Review on Ranking and Selection: A New
> Perspective"*, **arXiv:2008.00249v3**. Retrieved and read (19,258 words).

Term counts (`grep -a`, control "the" = 1,514): **"selection event" 0 · "selective
inference" 0 · "post-selection" 0 · "rejection sampling" 0 · "conditional" 3 · PCS 64.**

All three occurrences of "conditional" are *"conditional PCS"* in the covariate sense —
*"the probability of selecting the best alternative … for an individual whose random
covariates … take the value x"*. Conditioning on **covariates**, not on selection. A
19,000-word review of the field, published in a top OR outlet, never uses the vocabulary.

**Verdict: SAFE.** The two literatures have not met: arXiv full-text for
`all:"ranking and selection" AND all:"selective inference"` returns **0** results, against
controls of 309 (`"selective inference"`) and 8
(`"ranking and selection" AND "probability of correct selection"`).

### 2.3 Bayesian R&S

> **Björn Görder & Michael Kolonko**, *"Ranking and Selection: A New Sequential Bayesian
> Procedure for Use with Common Random Numbers"*, **arXiv:1410.6782**. Read (11,023 words).

Multivariate-normal likelihood, uninformative prior, posterior-driven budget allocation.
Term counts (control "the" = 757): "selection event" 0, "rejection sampling" 0, "selective
inference" 0, "posterior" 42. The Bayesian branch assumes normality and allocates; it does
not calibrate a selection event.

**Verdict: SAFE.**

### 2.4 What R&S *does* own, and it matters for the demonstration

R&S owns **probability of correct selection** — the guarantee `S0_REPORT.md` §3 already
warned "an applied reader will assume", and which no selective-inference method delivers.
Sixty years of procedures deliver PCS with a guarantee, by drawing more replications. The
paper must not describe its demonstration in language that promises PCS.

Adjacent and unread in full: **Hsu (1984)**, *"Constrained simultaneous confidence intervals
for multiple comparisons with the best"*, *Ann. Statist.* 12:1136–1144; **Matejcik & Nelson
(1995)**, *Management Science* 41(12):1935–1945 and *Operations Research* 43(4):633–640.
MCB gives simultaneous intervals on μ_i − max_{j≠i} μ_j — inference *about the selected
system*, obtained analytically. **Metadata only; not read.** See §5.

---

## 3. ADJACENT: inference on a winner

> **Kenneth Hung & William Fithian**, *"Rank Verification for Exponential Families"*,
> **arXiv:1610.03944**, *Annals of Statistics*.

> *"Having observed the 'winner' (largest observed response) in a noisy experiment, it is
> natural to ask whether that candidate … is actually the 'best' … For **exponential family
> models**, we show under mild conditions that an unadjusted two-tailed pairwise test
> comparing the first two order statistics … is a valid test of whether the winner is truly
> the best."*

Exactly the demonstration's question — is the flagged component the culprit — answered
analytically inside an exponential family. **SAFE on R1's mechanism**, but it is a
competitor for the demonstration's framing and belongs in related work.

---

## 4. SEARCH LOG

| Route | Status |
|---|---|
| **Semantic Scholar** | **Partially recovered** from G0's total blackout. **2 of 6 requests returned HTTP 200; 4 returned 429**, including a 3-attempt probe at 20 s spacing that went 429 / 200 / 429. Usable for a spot lookup, **not** for systematic citation-chaining. That gap remains open. |
| arXiv API | Reliable. Conjunctive full-text queries with controls (see §2.2). |
| OpenAlex | Reliable for metadata and OA status. Note: `search=` + `sort=cited_by_count:desc` is unusable — it returns globally-popular papers regardless of topic. `filter=title.search:` works. |
| Unpaywall | Queried directly with the operator's address. All three R&S DOIs tried returned `is_oa: false`. |
| OpenReview | Not re-run this session; G0 covered it. |
| Web search | Run; surfaced §1.4, §1.2 and §3, all then retrieved from primary sources. |
| **Google Scholar** | **Still not searched.** Unchanged from G0 and from the originating plan. O-7. |

**Adversarial searches run** (≥3 required):

| Query | Result |
|---|---|
| `all:"rejection sampling" AND all:"selective inference"` (arXiv) | 1 hit — **Freidling et al.**, §1.1. The decisive one. |
| `all:"selection event" AND all:"rejection sampling"` (arXiv) | 0 |
| `all:"indifference zone" AND all:"post-selection inference"` (arXiv) | 0 |
| `all:"ranking and selection" AND all:"selective inference"` (arXiv) | 0 |
| `all:"post-selection inference" AND all:"parametric bootstrap"` (arXiv) | 0 |
| `all:"selection event" AND all:"simulation-based inference"` (arXiv) | 0 |
| "conditional selective inference without analytic characterization … Monte Carlo" (web) | Surfaced §1.2, §1.4 — **both fatal** |
| "simulation-based inference + selective inference + misspecification attribution" (web) | No SBI×SI bridge found; the SBI misspecification literature is detection/robustification, as G0 found |

**Zero-count discipline (S5).** Every count above was taken with `grep -a` against a
control term known to be present. Controls: "the" = 624 / 1,514 / 757 / 1,062 / 814 across
the five full texts, and 309 / 8 for the two arXiv control queries. **No zero is reported
without a passing control.**

**Prompt-injection check (S6).** No retrieved document contained text addressed to an
automated reader or any instruction directed at a model.

---

## 5. WHAT WAS NOT RETRIEVED — named, not glossed

| Source | Status |
|---|---|
| **Branke, Chick & Schmidt (2007)**, *"Selecting a Selection Procedure"*, *Management Science* 53(12):1916–1932, DOI 10.1287/mnsc.1070.0721 | **NOT RETRIEVED.** OpenAlex `oa_status: closed`; Unpaywall `is_oa: false`; no WSC-2005 companion PDF located on `informs-sim.org` or ACM DL. Named in the brief as a required read. Its content — an empirical comparison of IZ, Bayesian and OCBA procedures — is covered in outline by §2.1–§2.3, but **not read**. |
| **Kim & Nelson (2006)**, *"Chapter 17: Selecting the Best System"*, *Handbooks in OR & MS* vol. 13, DOI 10.1016/S0927-0507(06)13017-0 | **NOT RETRIEVED.** Elsevier, closed. **Substituted** by the same authors' WSC-2003 tutorial (§2.1), read in full. A substitution, and recorded as one. |
| **Hsu (1984)**; **Matejcik & Nelson (1995)** ×2 | **METADATA ONLY.** Bylines, venues and page ranges confirmed; **texts not read**. |
| **Chick**, "Subjective probability and Bayesian methodology" (Handbooks vol. 13, ch. 9) | **NOT RETRIEVED.** Same Elsevier volume. Substituted by §2.3, which is a different paper by different authors. |

---

## 6. THE CASE *FOR* R1 — what actually survives, stated small

Everything below is a **residual**, not the claim in D-3.

**(a) The review's own objection is void for simulators — but only one of the two.**
Neufeld, Perry & Witten reject the Monte Carlo strategy as *"not always applicable"* and
*"typically quite inefficient."* The **applicability** objection genuinely does not bind a
simulator: drawing from the null is the one operation a simulator always affords. The
**inefficiency** objection binds exactly as hard — it is the 1/p₀ cost that Freidling et al.
measure at 150× and that `S0_REPORT.md` §2 already conceded. So the honest statement is
*"one of the two standard objections to a known strategy does not apply in our setting"*.
That is an observation. It is not a mechanism, and it is not a headline.

**(b) Exactness without regularity conditions.** Of the three published routes past analytic
characterisation, one is asymptotic and needs smoothness plus estimated selection
probabilities (§1.3), one is a learned approximation (§1.4), and one is exact (§1.1) — but
§1.1's exactness comes from a *design-based* null. A simulator supplies an exact
model-based null. **This is the strongest surviving thread**, and it is a transfer claim:
*"the construction of Freidling et al. carries over from randomization to simulation, and
there it is the only exact option."*

**(c) The demonstration is still unoccupied.** No source found does component-level
misspecification attribution in a simulator with conditional error control. But D-3
explicitly demoted the demonstration to "not the subject of the paper", so this cannot
carry a paper on its own without reversing D-3.

### And a problem R1 has that none of the prior art has

**A simulator's null is composite; a randomization null is not.** Freidling et al. can
rejection-sample because the treatment-assignment distribution is **known exactly by
design**. A simulator's null distribution is exact only **given the parameters θ**, and θ is
unknown — so "the simulator's own null" is a *family*, not a distribution, and the naive
rejection-sampling construction is not automatically valid over it. Handling that nuisance
parameter is the real technical content of any SBI version of this mechanism, and **D-3's
formulation does not mention it.** This is a threat to R1 independent of novelty, and it is
logged as a new open question.

---

## 7. CONSEQUENCE

Per the session brief §2.4, a **DEAD** verdict stops work before Phase 3 and raises a
blocking operator question rather than proceeding. That is what has happened. See
`docs/OPEN_QUESTIONS.md` **Q-8** and **Q-9**, and `audit/S1_REPORT.md`.

**A note on process, since it is the second time this pattern has appeared.** G0 recorded
that its R1 finding rested on *negative searches* and named it "the least secure conclusion
in the report", and `DEVIATIONS.md` D-4 recorded that none of the four adversarial critics
ran. The refutation above took a single arXiv query pairing two obvious terms. The finding
is not that G0 searched badly — it searched nine conjunctive queries — but that it did not
run the one adversarial layer designed to catch exactly this, and it read one paper's
problem statement as that paper's conclusion. Both failures are the ones its own process
caveats predicted.
