# S1 — Session G1 report

**For a reader who has not seen this session.** Written 2026-08-20.

> **Three things to know before anything else.**
>
> **1. The paper's headline claim is prior art, for the second time.** G0 promoted a
> mechanism — calibrating a selection event by rejection sampling from an exact null — as
> the one genuinely new thing it had found. It is published: **Freidling, Zhao & Gao,
> arXiv:2405.07026**, where it is a titled algorithm with the same cost analysis. The
> April-2026 review of the field lists it as a known strategy and gives the two standard
> objections to it.
>
> **2. This session produced no code and no numbers.** That is not a shortfall against the
> brief; it is the brief being followed. A pre-registered stop condition fired and blocked
> Phase 3.
>
> **3. The literature this session was sent to check turned out to be the safe one.** The
> brief named ranking-and-selection as "a first-class risk to R1". R&S is clean. The
> refutation came from selective inference — the literature G0 believed it had already
> cleared.

---

## 1. STATE — what exists, and what does not

### New this session

| Path | What it is |
|---|---|
| `docs/DECISIONS.md` | Operator decisions D-1…D-4, each with what it forecloses. D-3 now carries a suspension notice |
| `audit/R1_THREAT_CHECK.md` | The Phase-2 prior-art check on R1. **Verdict: DEAD** |
| `docs/THRESHOLDS.md` | Q-4 and Q-5 answered, plus the Kahl/D8 argument. Written before any number existed |
| `audit/BIBLIOGRAPHY.bib` | 52 entries, every one fetched. Now the citation source of truth |
| `paper/neurips_2026_template/` | The NeurIPS 2026 template, fetched and unmodified |

### Still does not exist

**No simulator. No diagnostic. No attribution code. No results. No manuscript. No figure.
No number.** `src/` contains three READMEs and three `.gitkeep` files, exactly as G0 left
it. `results/` is empty. This is the state G0 described, unchanged.

---

## 2. THE VERDICT ON R1

### R1 — simulator-exact conditional calibration of the selection event
# **DEAD as an original mechanism.**

Full evidence and per-source verdicts in `audit/R1_THREAT_CHECK.md`. In brief:

| Source | What it does | Verdict |
|---|---|---|
| **Freidling, Zhao & Gao**, arXiv:2405.07026 | Supplementary §S3.2 headed *"Rejection Sampling"*; **Algorithm 1** titled *"Rejection sampling"*. Draw from the exact null, apply the selection rule, keep the accepted draws — for *"arbitrary treatment assignment schemes and **conditioning events**"*. Controls selective type-I error with *"no modelling assumptions"*. Derives **the same cost**: *"the expected number of draws required to obtain one acceptable treatment is 1/p₀"* | **DEAD** |
| **Neufeld, Perry & Witten**, arXiv:2604.09779 (April 2026) | The field's review names the *"Monte Carlo strategy"* for an intractable conditional-given-selection law and states its two objections: *"not always applicable"*, *"typically quite inefficient"*. **Example 1 is inference on a "winner"** — the argmax selection event | **DEAD** |
| **Liu, Markovic-Voronov & Taylor**, arXiv:2203.14504 | The paper D-3 cites as *identifying* the barrier. It removes one: bootstrap the selection algorithm, estimate the selection probability, condition. Guarantee is asymptotic and needs normality plus smoothness | **DEAD** on "no analytic characterisation" |
| **Liu & Panigrahi**, arXiv:2506.01150 | Normalizing-flow transport map to the conditional law, *"even when the underlying selection event lacks an analytical description"* | **NARROWS** |
| **Tian & Taylor**, *Ann. Statist.* 46(2) | Samples the conditional law — but only *after* characterising the selection event as a **polyhedron** | **NARROWS** |
| **Panigrahi, Fry & Taylor**, arXiv:2212.12940 | Exact, by a closed-form pivot. Zero "Monte Carlo", zero "rejection sampling", zero "simulator" | SAFE |

**Both clauses of D-3 are false as written.** The mechanism is published, and the paper cited
as naming the barrier is a paper that removes it.

### What survives, stated small

Three things, none of them a headline:

1. **One of the review's two objections is void for simulators.** "Not always applicable"
   does not bind a thing that can always sample its own null. **"Typically quite
   inefficient" binds exactly as hard** — it is the 1/p₀ cost that Freidling et al. measure
   at 150× and that `S0_REPORT.md` already conceded.
2. **Exactness without regularity conditions.** Of the three published routes past analytic
   characterisation, one is asymptotic, one is a learned approximation, and one is exact but
   draws its exactness from a *design-based* null. A simulator supplies an exact
   *model-based* null. This is a **transfer claim** — precisely the wording `PIVOT.md`
   pre-registered as response 1 to a novelty failure.
3. **The demonstration is unoccupied.** Nobody does component-level misspecification
   attribution in a simulator with conditional error control. But D-3 demoted the
   demonstration to "not the subject of the paper", so this cannot carry a paper without
   reversing D-3.

### And a problem nobody else has

**A simulator's null is composite; a randomization null is not.** Freidling et al. can
rejection-sample because the treatment-assignment distribution is known exactly *by design*.
A simulator's null is exact only *given θ*, and θ is unknown — so "the simulator's own null"
is a **family**, not a distribution, and the construction is not automatically valid over it.
Handling that nuisance parameter is the real technical content of any SBI version of this
mechanism, and **D-3 does not mention it.** This threatens R1 independently of novelty and is
logged as **Q-9**.

### Ranking and selection — the risk that wasn't

The brief sent this session to check R&S as a first-class threat. **It is clean.** R&S
derives its guarantees by *analytic bounding under normality* — Kim & Nelson's own summary is
*"first using appropriate standardization of estimators and then **bounding** the resulting
probability statements … [so that] a difficult multivariate probability statement becomes one
that is **readily solvable**"*, via Slepian's and Kimball's inequalities and Bonferroni.

And **the conditioning is on a different object.** The indifference-zone guarantee is
`Pr{select k | μ_k − μ_{k−1} ≥ δ}` — conditioning on the **parameter configuration**, not on
the selection event. In Hong, Fan & Luo's 19,258-word review, all three occurrences of
"conditional" mean *conditional on covariates*. Term counts there, with `grep -a` and control
`"the" = 1514`: **"selection event" 0, "selective inference" 0, "post-selection" 0, "rejection
sampling" 0.** arXiv full text for `"ranking and selection" AND "selective inference"`
returns **0** against passing controls.

**What R&S does own, and it matters:** *probability of correct selection* — the guarantee
`S0_REPORT.md` §3 warned "an applied reader will assume" and that no selective-inference
method delivers. The paper must not describe its demonstration in language that promises it.

---

## 3. WHAT THIS MEANS FOR THE PROJECT

Two successive headline claims have now been found to be prior art by direct retrieval:
**ex-C2** (Kahl et al. 2019, found by G0) and **R1** (Freidling et al., found here). The
pattern is not bad luck. Both were claims about *statistical machinery*, in fields — control
theory, selective inference — that are large, mature, and were searched only from the SBI
side.

The three options are set out as **Q-8** and are the operator's. Briefly:

- **(a) Rescope R1 to the transfer claim.** Small, defensible, requires solving Q-9 first.
- **(b) Promote R2 and the demonstration.** A diagnostics paper. `PIVOT.md` response 2.
- **(c) Report the negative outcome and stop.** `PIVOT.md` response 3, written in advance so
  that reaching it is a decision rather than a failure.

**One observation the operator should have when choosing.** Option (b)'s deliverable —
Phase 3, the Jacobian rank diagnostic — is **technically unblocked**. R2 does not depend on
R1; `audit/CLAIM_GRAPH.md` records them as independent and the Phase-2 refutation touches
only R1. Phase 3 was stopped **by instruction**, not because its subject died. If the
operator wants the diagnostic built, it can be authorised on its own without settling Q-8.

**And a caution against reaching for (b) too quickly.** **R2 has not been threat-checked.**
R1's refutation took a single arXiv query pairing two obvious terms. Nobody has run the
equivalent against "numerical rank of a noisy, simulation-estimated Jacobian" — a phrase that
sits next to derivative-free optimisation, stochastic-gradient estimation, and the
sloppy-models literature. Given a base rate of two-for-two, **R2 should be threat-checked
before it is promoted, not after.**

---

## 4. WHAT WAS BUILT INSTEAD

### Thresholds, pre-registered and demonstrably so

`docs/THRESHOLDS.md` closes Q-4 and Q-5. The list of summary sets is **closed at S_A, S_B,
S_C**; numerical rank is called at `τ = 10⁻²` relative to `σ₁`; a summary set is
"inseparable" if `rank(J) < 3` or `κ > 100`.

**`κ_max = 100` is derived, not chosen.** Because summaries are normalised to unit
prior-predictive standard deviation, recovering `η` amplifies Monte Carlo error by `κ`, so
separating the components needs `n ≳ κ²` replicates. `κ = 100` costs ~10⁴ replicates;
`κ = 1000` costs ~10⁶ *per replicate*, which exceeds what `S0_REPORT.md` §7 prices the entire
protocol at. The line sits where separation costs more than the study's whole budget.

Equivalence classes: component *k* joins the class named by a near-null right singular vector
`v` iff `|v_k| ≥ 0.3`, reported as a range across the h-plateau. **Coherence is reported but
is deliberately not the decision rule** — the coherence consistent with `κ_max = 100` is
`μ ≈ 0.9998`, too close to 1 to be estimable, so `|μ| ≥ 0.98` only flags which pair is
responsible.

**Why "pre-registered" is a stronger word here than usual.** These were fixed in a session
that produced **no singular values at all**. They cannot have been fitted to a result, and
`git log` shows it. `LEDGER_DESIGN.md` D3 and `S0_REPORT.md` §8 both warn that setting these
after seeing the numbers is "the respectable form of the leakage failure"; this is the one
circumstance in which that worry is not merely mitigated but excluded.

### The Kahl / D8 argument, with a real concession

`docs/THRESHOLDS.md` §3 argues that Kahl et al.'s *"there is no such thing as nearly
invertible"* does not import: their unknown inputs live in an infinite-dimensional function
space where a non-trivial null space is generically infinite-dimensional, while `η ∈ ℝ³`
makes `J` a `d × 3` matrix whose kernel has dimension 0, 1, 2 or 3. The dimensional premise
of the dichotomy is simply not met.

The load-bearing part is that **the decision problems differ**. Kahl et al. ask whether inputs
can be *reconstructed exactly* — a deterministic inverse problem with a clean yes/no. This
project asks whether a *finite-precision statistical decision among three hypotheses* is
achievable at a stated budget, and there `κ` is the exchange rate between degeneracy and
sample size.

**§3.4 is a concession, not a defence.** Where `J` is *exactly* rank-deficient, Kahl's
dichotomy does import and there is a wall rather than a gradient. So D8 must label its two
cases differently: exact degeneracy is an **identifiability** claim; near-degeneracy at `κ` is
an **affordability** claim, and writing the second as the first would be the same
self-refuting error one level up.

### Citation repair

`audit/BIBLIOGRAPHY.bib`: **52 entries, every one fetched** — 26 from `arxiv.org/bibtex/`, 26
from `doi.org` via BibTeX content negotiation. Zero fetch failures. All four of G0's byline
corrections confirmed against the fetched records.

**Three defects were found in the fetched records themselves**, which is the more useful
finding:

1. **Catchpole & Morgan (1997): Crossref *and* OpenAlex both omit Morgan.** Verified against
   the publisher's article page. Two major indexes are wrong about a load-bearing citation.
   **Fetching from a canonical index is necessary but not sufficient.**
2. **Arendt, Apley & Chen (2012): still UNRETRIEVED**, now with five routes logged
   individually. Marked in the `.bib` with an explicit instruction not to cite any claim
   from it.
3. **"Presanis et al. (2017)" cannot be resolved.** `S0_REPORT.md` §2 cites it for a Jacobian
   non-singularity condition. Three Crossref queries return nothing; the nearest 2017 work is
   **Gåsemyr & Natvig**, different authors. Either G0 committed a byline error of exactly the
   kind it was documenting, or the citation points to something unindexed. The corroborating
   claim is **UNVERIFIED**. The ex-C2 refutation is unaffected — it rests on Kahl et al., read
   directly.

A fifth byline detail, new: the two 1995 MCB papers have opposite author orders —
*Operations Research* is **Matejcik & Nelson**, *Management Science* is **Nelson & Matejcik**.

### Decisions and venue

`docs/DECISIONS.md` records D-1 (target NeurIPS 2026; **calendar feasibility is excluded as a
planning input**, standing instruction), D-2 (**Sim2Science, 5-page main track**), D-3 (the
reframe — now suspended), D-4 (visibility). The deadline-countdown banner is gone from
`OUTSTANDING.md`; the facts survive in `audit/VENUE.md` stripped of urgency.

The template was fetched unmodified (20,259 bytes, SHA-256 `82473931…b817d9`). Reading
`neurips_2026.sty` confirms `dblblindworkshop` leaves `\@anonymous` at its default `true` —
genuinely double-blind, unlike `sglblindworkshop`, which sets `\@anonymousfalse`.
`paper/main.tex` was **not** created.

---

## 5. GATE G1

**`ready for review — UNSIGNED`. Its defining criterion is NOT MET.**

G1 was fixed in advance as: *"Both outcomes pass G1. Only an unrun or uninterpretable
diagnostic fails it."* **The diagnostic was not run.** By its own wording G1 does not pass.

The honest description is *deferred* rather than *failed* — a different pre-registered stop
condition fired first and blocked Phase 3 — but "deferred" is not an outcome G1 admits, and
inventing it would be self-approval. `GATES.md` puts the choice to the operator: re-scope
G1, authorise Phase 3 separately under Q-8, or record G1 as failed and re-prepare it.

`GATES.md` also carries **proposed `conditions` text for G0's still-open signature**, per
5.2. It is a proposal. The signature line is blank and stays blank.

---

## 6. NEXT SESSION

Contingent on **Q-8**, and on nothing else:

- **If (a) or (b):** threat-check **R2** before building it, to the standard R1 was checked
  here — then build Phase 3 as specified in `S0_REPORT.md` §8, against the thresholds already
  fixed in `docs/THRESHOLDS.md`. **Q-9** must be answered before any exactness claim is made.
- **If (c):** the output is the negative result, and `PIVOT.md` already specifies its shape.

**Independent of Q-8, and overdue:** search Google Scholar (O-7, now three sessions old);
retry Semantic Scholar citation-chaining; authenticate `gh` (O-4).

---

## 7. PROCESS CAVEATS — what this session did badly or not at all

**No code was written, so the session's stated technical deliverable is entirely absent.**
This was the session that was supposed to produce the project's first real numbers. It
produced none. `DEVIATIONS.md` **D-6** records the instruction that blocked it.

**`docs/THRESHOLDS.md` was written despite Phase 3 being stopped.** The brief says "STOP
before Phase 3" (§2.4) and "before any further code is written" (P-1). I took the narrower
reading for a pre-registration document and the wider reading for everything else. A reader
who disagrees should treat that file as a proposal; nothing depends on it, because nothing
has been run. Logged in `DEVIATIONS.md` D-6 rather than left as a silent judgement.

**No adversarial critic ran — again, and this is the second time it has cost something.**
G0's `DEVIATIONS.md` D-4 recorded that none of the four critics ran, and named the R1 novelty
finding as the least secure conclusion in its report *because* of it. That finding was wrong.
**This session also ran no critics.** The R1 refutation is single-pass. It is better sourced
than what it overturns — primary texts read in full, with positive evidence rather than
negative searches — but **no independent agent has tried to refute it either.**

**Two G0 claims failed verification here, and the base rate is now known to be non-zero.**
Reading a paper's problem statement as its conclusion (Liu et al.) and an unresolvable
citation (Presanis 2017). Neither was load-bearing. Both are the kind of error that a second
reader catches and a single pass does not.

**Retrieval failures, named:**
- **Branke, Chick & Schmidt (2007)** — required by the brief, **not retrieved**. INFORMS
  paywall; Unpaywall `is_oa: false`; no WSC-2005 companion PDF found. Its content is covered
  in outline by two other R&S surveys that *were* read, but **it was not read**.
- **Kim & Nelson (2006)** handbook chapter — **not retrieved** (Elsevier). **Substituted** by
  the same authors' WSC-2003 tutorial, read in full. A substitution, recorded as one.
- **Hsu (1984)** and both **Matejcik/Nelson (1995)** papers — **metadata only**.
- **Chick's** Bayesian R&S handbook chapter — **not retrieved**; a different Bayesian R&S
  paper by different authors was read instead.
- **Arendt, Apley & Chen (2012)** — **not retrieved**, fifth attempt.

**Tooling failures and quirks:**
- **Semantic Scholar is only partially recovered.** 2 of 6 requests returned 200; a
  3-attempt probe at 20 s spacing went 429/200/429. Citation-chaining still has not happened
  in this project.
- **OpenAlex `search=` with `sort=cited_by_count:desc` is unusable** — it returns globally
  popular papers regardless of topic, and produced two rounds of garbage before being
  caught. `filter=title.search:` works. An unnoticed version of this would have produced a
  false "nothing found in this literature".
- **`hyperresearch fetch` failed on `arxiv.org/abs/…` and on `arxiv.org/html/…`** for the
  2026 review; the `arxiv.org/pdf/` form works. The review was read via its HTML through a
  different route.
- **zsh does not word-split unquoted variables**, which silently turned a 26-element URL list
  into one malformed request that reported `HTTP 000`. Caught by a count check. This is the
  same class of failure as G0's silent `fetch-batch` zero-result: a loop that appears to run
  and does nothing.

**What would most improve confidence, in order:** (1) run an adversarial critic against
**this report's** R1 verdict, since the project's record on single-pass novelty findings is
now 0-for-2; (2) threat-check **R2** before any decision to build on it; (3) search Google
Scholar; (4) answer **Q-9**, which is a correctness question rather than a novelty one and
does not go away under any option in Q-8.
