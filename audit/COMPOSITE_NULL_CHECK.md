# Composite-null threat check — is the gap real, and is it open?

**Session G2, 2026-08-20.** Written to the standing instruction carried from G0 and G1:
**the strongest case against novelty is stated first, before any case for it.**

The claim under test, as the operator framed it entering this session (PROVISIONAL, and
explicitly "exactly as unverified right now as R1 was three hours before it died"):

> "Simulators make selective inference exact only when the relevant null is simple. Under a
> composite null — the typical case for simulator-based discrepancy attribution, where
> nuisance parameters are unknown — the rejection-sampling construction of Freidling et al.
> (2024) does not deliver an exact conditional law without further work. We characterise the
> gap and give a repair."

---

# VERDICT: **DEAD**

**Both halves are prior art, and neither is obscure.**

The *observation* — that Monte Carlo tests are exact only when the null distribution is free
of nuisance parameters — is the opening premise of the literature on Monte Carlo testing, and
is stated as textbook background in the abstract of an *Annals of Statistics* paper.

The *repair* — restore exact level under a composite null by maximising the simulated p-value
over the nuisance parameter space — is **Dufour (2006)**, *Journal of Econometrics* 133(2),
where it is named, proved, and called **maximized Monte Carlo (MMC)**. Dufour's condition for
it to apply is *"as long as the null distribution of the test statistic can be simulated once
the nuisance parameters have been specified"* — which is a description of a simulator.

There are at least **three independent, published solution families**, one of which ships as a
CRAN package.

A residual exists and is stated in §5. It is one unoccupied cell — nobody has composed MMC
with a *selection event* — and it is a composition of two published techniques, not a gap.

---

## 1. THE STRONGEST CASE AGAINST

### 1.1 Dufour (2006) — the repair, named and proved, forty years into the problem

> **Jean-Marie Dufour**, *"Monte Carlo tests with nuisance parameters: A general approach to
> finite-sample inference and nonstandard asymptotics"*, **Journal of Econometrics 133(2):
> 443–477 (2006)**, DOI `10.1016/j.jeconom.2005.06.007`.
> Retrieved as **CIRANO Working Paper 2005s-02**, <https://cirano.qc.ca/files/publications/2005s-02.pdf>,
> and read (17,226 words). Elsevier version is closed; Unpaywall `is_oa: false`, OpenAlex
> `oa_status: closed`. Term counts, `grep -a`, control `"the" = 690`: **nuisance 56 · MMC 26 ·
> "Maximized Monte Carlo" 5 · exact 16 · simulat 54.**

**The problem, as Dufour states it in his own abstract** — this is the session's "gap",
stated as the standing premise of the field:

> Monte Carlo tests are *"an attractive method that allows one to construct exact tests based
> on statistics whose exact distribution is difficult to compute analytically but can be
> simulated, **provided that this distribution does not depend on nuisance parameters**."*

**The repair, verbatim:**

> *"We show that **maximizing** the [p-value function] with respect to the nuisance parameters
> yields a test with **provably exact level, irrespective of the sample size and the number
> [of] replications used**. For this reason, we call the latter **maximized Monte Carlo (MMC)
> tests**."*

**And its scope condition is the simulator setting, stated explicitly:**

> *"we have shown how the method can be extended to models with nuisance parameters **as long
> as the null distribution of the test statistic can be simulated once the nuisance parameters
> have been specified**. This leads to what we called maximized Monte Carlo tests which were
> shown to **satisfy the level constraint**."*

A simulator satisfies that condition by definition. **There is no transfer gap to argue.**

Dufour also states the price himself, so it is not an unnoticed weakness either: *"the
probability of type I error for a MMC test can be lower (but not higher) than the level of the
test and the procedure can be **conservative**."* Exact **level**, not exact **size**.

**Verdict: DEAD.** This is outcome (a) of the session brief's §1.3 — explicitly addresses a
composite/nuisance null under a simulation-based construction, and solves it.

### 1.2 Barber & Janson — the simple/composite distinction as textbook background

> **Rina Foygel Barber & Lucas Janson**, *"Testing goodness-of-fit and conditional independence
> with approximate co-sufficient sampling"*, **Annals of Statistics** (2022),
> DOI `10.1214/22-aos2187`; arXiv:2007.09851. Retrieved and read (25,239 words).

Their abstract opens with the session's central distinction, as setup rather than finding:

> *"While testing the GoF of a **simple (point) null hypothesis** provides an analyst great
> flexibility in the choice of test statistic while still ensuring validity, most GoF tests for
> **composite null hypotheses** are far more constrained, as the test statistic must have a
> tractable distribution over the entire null model space. A notable exception is
> **co-sufficient sampling (CSS): resampling the data conditional on a sufficient statistic for
> the null model guarantees valid GoF testing using any test statistic the analyst chooses**."*

So the distinction is background, and a second independent repair — conditioning on a
sufficient statistic — is named in the same sentence. Their contribution, **approximate CSS**,
generalises it to *"essentially any parametric model with an asymptotically-efficient
estimator"*.

**This is an active sub-literature, not a gap.** Full-text search returns **30** hits for
`"co-sufficient sampling"`, including Zhu & Barber (*EJS* 2026), Xie & Huang (arXiv:2506.12334),
Bhaduri, Bhattacharyya, Barber & Janson (*Biometrika* 2026, DOI `10.1093/biomet/asag019`), and
Barber & Ramdas, *"Monte Carlo testing: non-asymptotic guarantees without joint
exchangeability"* (arXiv:2607.23010).

**Verdict: DEAD** on the framing; the repair differs from Dufour's but reaches the same place.

### 1.3 Xie & Wang — likelihood-free, exact, with nuisance parameters profiled out

> **Min-ge Xie & Peng Wang**, *"Repro Samples Method for Finite- and Large-Sample Inferences"*,
> **arXiv:2206.06421**. Retrieved and read (23,463 words). Term counts, control `"the" = 1404`:
> **nuisance 31 · simulat 34 · exact 13 · guarantee 11.**

Their abstract:

> *"a novel, general, and effective **simulation-inspired** approach … artificial samples,
> referred to as repro samples, obtained by mimicking the true observed sample … to construct
> confidence sets for parameters of interest with **guaranteed coverage rates**. **Both exact
> and asymptotic inferences are developed.** An attractive feature … is that it does not rely
> on the large sample central limit theorem and **is likelihood-free**."*

And §3.2, which is the session's proposed contribution:

> *"we develop … **a general technique to handle nuisance parameters through profiling**. The
> method **maintains the desired coverage rates** for confidence sets constructed for target
> parameters, **even in finite sample settings**."*

**Likelihood-free + simulation-based + exact finite-sample + nuisance profiled out.** That is
the target claim's repair, published in 2022.

The line is active and applied: **Awan & Wang**, *"Simulation-based, Finite-sample Inference for
Privatized Data"* (arXiv:2303.05328, read, 21,718 words) applies it where *"the marginal
likelihood function … is intractable"*, delivering *"guaranteed coverage and type I errors,
**even accounting for Monte Carlo error**"* and beating the parametric bootstrap, which *"at
best gives an asymptotic approximation while our framework has finite-sample guarantees."*
**Wang, Xie & Zhang**, *Annals of Statistics* (2026), DOI `10.1214/25-aos2591`, extends it.
There is a CRAN package: **SimBaRepro — "Simulation-Based, Finite-Sample Inference via Repro
Samples"** (Du, Wang & Awan, 2025).

**Verdict: DEAD.**

### 1.4 The antecedents are older than any of this

Dufour's own lineage: **Dwass (1957)**, **Barnard (1963)**, with **Jöckel (1986)**,
*"Finite Sample Properties and Asymptotic Efficiency of Monte Carlo Tests"*, *Ann. Statist.*
(DOI `10.1214/aos/1176349860`), and **Besag & Clifford** for the MCMC variant. The claim that
simulation buys exactness *only* under a simple null, and what to do otherwise, is
approximately sixty years old.

---

## 2. WHAT FREIDLING ET AL. ACTUALLY SAY — 1.1 of the brief

The brief asked whether the paper is *silent* on nuisance parameters, and warned that silence
is weaker evidence than an explicit assumption. **It is not silent, and it is not about
nuisance parameters either.**

Term counts over the full text (20,339 words), `grep -a`, control `"the" = 1448`:

| Term | Count |
|---|---|
| `nuisance` | **0** |
| `composite` | **0** |
| `sharp null` | **14** |
| `impute` / `imputed` | 14 / 7 |
| `potential outcome` | 39 |

So the *words* are absent — but the *structural requirement* is explicit, stated repeatedly,
and does the same work:

> *"A common hypothesis in randomization inference is **Fisher's sharp null** … Under this
> hypothesis, **all potential outcomes can be imputed** from the observed outcomes, so Y_R(·)
> and thus **P(Z = · | R, X_R, Y_R(·), S(Z)) is known**."*

**That is the simple-null requirement, in randomization-inference vocabulary.** The rejection
sampler works because the null law is *known*.

**They also already handle the non-sharp case**, which the session's hypothesis assumed they
did not:

> *"in many adaptive studies the null hypothesis of interest does not apply to all potential
> outcomes. Therefore, we can only impute a subset of Y_R(·) … when a **partially sharp null
> hypothesis** is specified, we usually need to **restrict the support of the (selective)
> randomization distribution by conditioning on an additional statistic G** … conditioning on
> S accounts for the selection of design and null hypothesis, and **conditioning on G
> accommodates partially sharp null hypotheses**."*

And they state their own scope limit in the discussion, so this is an explicit assumption
rather than an oversight:

> *"our work only considers the classical problem of testing a **(partially) sharp null
> hypothesis**. In constructing confidence intervals, we further assume the treatment effect
> is the same for every individual (in a subgroup)."*

**Assessment, stated carefully.** The operator's hypothesis was *half right and half wrong*.
Right: Freidling et al.'s exactness does depend on the null law being known, and a simulator's
null generally is not. Wrong: this is neither unnoticed by them nor unaddressed by the
literature. Their own repair (condition on `G`) is design-based and does **not** obviously
transfer to a continuous unknown θ — but Dufour's and Xie & Wang's repairs do, and they are the
ones that matter.

**Freidling et al. cite none of it.** Term counts in their full text: `Dufour` **0**,
`"Maximized Monte Carlo"` **0**, `Barnard` **0**, `Dwass` **0** (`Besag` 2). So the two
literatures have not been joined — see §5.

---

## 3. SEARCH LOG — and a methodological finding that matters more than this verdict

### 3.1 arXiv's `all:` field does not search full text. G0 and G1 both believed it did.

`audit/PLAN_SOURCE.md`-era work and G0 described "nine conjunctive **arXiv full-text**
queries"; `audit/R1_THREAT_CHECK.md` (G1) described its zero-counts as `arXiv full text`.
**Both are wrong.** The arXiv API's `all:` prefix searches metadata — title, abstract, authors,
comments — not the body.

Demonstrated, not assumed. Three phrases verified present in fetched paper bodies, then queried:

| Phrase | Occurrences in fetched body | `all:"…"` total |
|---|---|---|
| `expected number of draws required to obtain one acceptable` (Freidling, Supp. S3.2) | 1 | **0** |
| `repeatedly executing the selection algorithm` (Liu et al., arXiv:2203.14504) | 2 | **0** |
| `conditional PCS` (Hong, Fan & Luo) | 3 | 5 *(also in abstracts)* |

**A real full-text index exists** and was found via the route S4 names: POST to
`https://arxiv.org/search_classic` with `searchtype=ft`. Verified — the first phrase above
returns exactly Freidling et al. with the surrounding body text, and the second returns exactly
arXiv:2203.14504.

**The consequence is large and it is retrospective.** Every zero-count in
`audit/R1_THREAT_CHECK.md` §4 and in G0's sweep was a *metadata* zero, not a full-text zero.
They were reported as evidence of absence in the literature. **They were partly an instrument
limit** — precisely the conflation S4 forbids. R1 was found in G1 only because Freidling et
al. happen to mention rejection sampling *in their abstract*; anything whose relevant content
sits in the body was invisible to both prior sessions.

This is the most probable single explanation for the project's record. It is corrected as of
this session and recorded in `audit/TOOLING.md`.

**The affected G1 claims, restated honestly.** The R1 verdict itself is unaffected — it was a
*positive* finding (a paper that does the thing), and positive findings do not depend on the
index's coverage. What is affected is G1's *negative* evidence: the statement that
ranking-and-selection and selective inference "have not met" rested on metadata zeros. Re-run
on the full-text index this session, `"selection event" "maximized Monte Carlo"` returns **0**
— a genuine full-text zero — so that particular conclusion survives, but it survives *because
it was re-checked*, not because G1 established it.

### 3.2 Queries run this session, on the full-text index

| Query | Hits |
|---|---|
| `"selective inference" "composite null"` | 37 |
| `"selection event" "nuisance parameter"` | 60 |
| `"conditional selective inference" "nuisance"` | 54 |
| `"rejection sampling" "composite null"` | 8 |
| `"Monte Carlo test" "nuisance parameters" exact` | 24 |
| `"maximized Monte Carlo"` | 4 |
| `"co-sufficient sampling"` | 30 |
| `Panigrahi "selective inference" "nuisance parameters"` | 36 |
| `"post-selection" "repro sample"` | 5 |
| `"likelihood-free" "post-selection inference"` | 9 |
| `"conditional selective inference" "profile likelihood"` | 1 |
| `"simulator" "selective inference" "misspecification"` | 5 |
| **`"selection event" "maximized Monte Carlo"`** | **0** |

For comparison, the metadata API returned **7** for `all:"selective inference" AND
all:"nuisance"` and **2** for `all:"Monte Carlo test" AND all:"nuisance parameter"`. The
full-text index returns an order of magnitude more, and it is where Dufour, the repro-samples
line, and the co-sufficient-sampling line all surfaced.

**Adversarial reformulations** (≥3 required): rows 4, 5, 6, 9, 10, 11 and 13 above are
reformulations of the core question rather than the first framing of it, and rows 12 and 13
were constructed specifically to find the thing that would kill the claim.

### 3.3 Sourcing order and instrument status

Academic APIs first (Crossref, OpenAlex, Unpaywall, arXiv metadata **and** full text), then web
search. **No headed browser was used at any point** (S4). Semantic Scholar was not needed and
was not queried this session.

**Retrieval failures: none material.** Dufour's *Journal of Econometrics* version of record is
paywalled; the **CIRANO working-paper version was retrieved and read**, and is cited as a
working paper, not as the VoR — per the standing rule that a preprint is not a substitute for
the version of record when a specific theorem is attributed. The MMC statements quoted above
are attributed to CIRANO 2005s-02.

**Prompt-injection check (S7).** No retrieved document contained text addressed to an automated
reader.

---

## 4. CLASSIFICATION, per the brief's §1.3

| Source | (a) addresses composite null under a simulation construction **and solves it** | (b) shows it unsolvable without further assumption | (c) does not address it |
|---|---|---|---|
| **Dufour (2006)** | **YES — MMC, provably exact level** | — | — |
| **Xie & Wang (2022)** | **YES — profiling, exact finite-sample, likelihood-free** | — | — |
| **Awan & Wang (2023)** | **YES — intractable likelihood, guarantees incl. MC error** | — | — |
| **Barber & Janson (2022)** | **YES — (a)CSS via sufficiency** | states the constraint plainly | — |
| Freidling, Zhao & Gao (2024) | — | — | **YES (c)** — assumes a (partially) sharp null; says so |
| Panigrahi line (2019, 2022) | — | — | requires a likelihood; maximum-likelihood based |

**Three independent (a)s.** The brief: *"Only (a) kills this session's target claim outright."*

---

## 5. THE CASE *FOR* — one unoccupied cell, stated at its true size

**Nobody has composed MMC with a selection event.** Full-text
`"selection event" "maximized Monte Carlo"` returns **0**, and Freidling et al. cite none of the
Monte-Carlo-with-nuisance literature (§2). So the specific object — *a selective p-value that
is rejection-sampled within the selection cell and maximised over the nuisance space to restore
exact level* — appears not to have been written down.

**Four reasons that is not a paper, stated plainly:**

1. **It is a composition of two published techniques**, each of which is designed to be
   composable. Freidling et al. supply the selection-cell sampler; Dufour supplies the
   nuisance maximisation. Neither requires modification to sit next to the other.
2. **It would be this project's third consecutive transfer claim.** ex-C2 was "the rank
   condition, transferred to SBI"; R1 was "conditional selective inference, transferred to
   simulators"; this would be "MMC, transferred to a selection event". `audit/PIVOT.md`
   anticipated response 1 as *"the transfer and its consequences, stated as such"* — but that
   was written as a fallback for **one** claim dying, not as a repeatable move.
3. **The costs multiply rather than add.** Rejection sampling the selection cell costs `1/p₀`
   draws (Freidling et al. measure 150× in their own experiments). MMC requires that cost
   **at every nuisance value visited by the maximisation**. For a simulator with more than a
   couple of nuisance dimensions this is not a budget problem so much as a different project.
   Xie & Wang's data-driven candidate sets exist precisely to attack this, which means even
   the computational objection is anticipated in the same literature.
4. **MMC is conservative by construction** — exact level, not exact size. A paper whose
   headline is "simulators make selective inference exact" cannot rest on a procedure whose
   author describes it as conservative.

---

## 6. CONSEQUENCE

Per the brief's §1.5, a **DEAD** verdict stops the session before Phase 2 and Phase 3, and
raises a blocking operator question. That is what has happened.

**`audit/R2_THREAT_CHECK.md` was NOT written and Phase 2 was NOT run.** R2 therefore remains
exactly as untested as it was at the end of G1 — which, as G1's own report said, is not
survival but an absence of data.

**This is the third consecutive primary claim to die to prior art (S9).** ex-C2 → Kahl et al.
(2019). R1 → Freidling et al. (2024). The composite-null repair → Dufour (2006). The pattern
is recorded plainly in `audit/S2_REPORT.md` §3 and raised as **Q-10**.
