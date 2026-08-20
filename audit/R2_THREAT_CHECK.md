# R2 threat check — the noisy-rank estimator, on the corrected instrument

**Session G3, 2026-08-20.** Written to the standing instruction carried from G0, G1 and G2:
**the strongest case against novelty is stated first, before any case for it.**

This is the check that was mandated in G1's brief and again in G2's, and cut both times by a
Phase-1 stop rule. It is the **first** prior-art check in this project run entirely on the
corrected full-text instrument (S4). It is deliberately narrow and time-boxed: one sweep, not
an investigation phase, per the operator's decision on **Q-10** recorded 2026-08-20.

The claim under test, unchanged from G2's framing:

> "A simulation-based estimator of the rank/column-space structure of a summary-statistic
> Jacobian from NOISY, finite-difference-sampled data, together with a rule for calling
> numerical rank under that noise."

---

# VERDICT: **NARROW-CONDITIONAL**

**Both halves of R2 are prior art separately. Their composition is not — and the composition
is one sentence wide.**

- The **rank-and-condition-number rule** for deciding which parameters a sensitivity matrix
  can separate is published, is applied to **epidemic models specifically**, and is cited 122
  times: **Cintrón-Arias, Banks, Capaldi & Lloyd (2009)**. The decision rule
  `docs/THRESHOLDS.md` §1.3 pre-registers — full column rank, then a condition-number ceiling
  — is structurally the rule that paper already runs.
- The **step-size-under-noise problem** that R2's h-sweep exists to solve is solved, and
  solved better than by sweeping: **Moré & Wild (2010/2012)** derive a *"provably
  near-optimal"* difference parameter from an estimated noise level. R2's "sweep h over
  decades and report the plateau" is a weaker heuristic than an existing algorithm.

What is **not** joined: nobody calls numerical rank at a **tolerance derived from the
simulation's noise level**. The existing rank-based identifiability practice calls rank at
*machine* tolerance on a matrix whose error floor sits many orders of magnitude above machine
epsilon. That is a real and specific defect, and it is the whole of what R2 has left.

**Conditional on two things**, neither of which is settled by this check:
1. **R2a must hold** — a plateau in `h` must actually exist for this simulator. If the
   finite-difference Jacobian has no regime where truncation error and simulation noise are
   both small, no rank call is defensible and R2 is dead outright. Phase 2 tests this.
2. **R2 must be framed as a composition**, with Moré & Wild and Cintrón-Arias et al. cited as
   the two things being composed — not as a new estimator.

**Consequence for the paper: R2 is INFRASTRUCTURE plus one scoped methodological note. It is
not a headline method contribution.** Recorded as **D-6** in `docs/DECISIONS.md`.

---

## 1. THE STRONGEST CASE AGAINST

### 1.1 Cintrón-Arias, Banks, Capaldi & Lloyd (2009) — rank *and* condition number, on an epidemic model

> **A. Cintrón-Arias, H.T. Banks, A. Capaldi & A.L. Lloyd**, *"A sensitivity matrix based
> methodology for inverse problem formulation"*, **Journal of Inverse and Ill-posed Problems
> 17(6): 545–564 (2009)**, DOI `10.1515/jiip.2009.034`. Elsevier-side closed (Unpaywall
> `is_oa: false`); retrieved as **arXiv:2004.06831** and read in full (8,420 words).
> Semantic Scholar citation count **122**.
>
> Term counts, ligature- and hyphenation-normalised, control `the` = 452: **sensitivity matrix
> 30 · rank 26 · "full rank" 11 · condition number 18 · singular value 12 · identifiab 28 ·
> SVD 3 · epidemic 12.**

Their own abstract states the criterion:

> *"First, the algorithm selects the parameter combinations that correspond to **sensitivity
> matrices with full rank**. Second, the algorithm involves uncertainty quantification by
> using the inverse of the Fisher Information Matrix."*

And the condition number is defined and used exactly as `docs/THRESHOLDS.md` §1.3 uses it:

> *"For a full rank sensitivity matrix χ(θ₀) ∈ Rⁿˣᵖ … its **condition number κ is defined as
> the ratio of the largest to smallest singular value**: κ(χ(θ₀)) = s₁/s_p … if the columns of
> χ(θ₀) are **nearly dependent** then κ(χ(θ₀)) is large."*

Their algorithm's step 2 is literally headed **"Full rank test."** This is a rank-condition
identifiability screen, run computationally, on an epidemiological model, published in 2009.

**What this kills.** It kills any claim that applying a rank/condition-number screen to a
sensitivity matrix, to decide which quantities are jointly recoverable, is new. It also kills
the narrower version — "…for epidemic models" — because that is their worked example.

**What it does not kill, and this is the one live seam.** Their sensitivity matrix is
computed from a **deterministic** ODE model. Against control `the` = 452:

| Term | Count |
|---|---|
| `finite difference` | **0** |
| `stochastic` | **0** |
| `Monte Carlo` | **0** |
| `noise` | 2 |
| `summary statistic` | **0** |

And the rank call itself is made at machine precision:

> *"using the MATLAB (The Mathworks, Inc.) routine **rank** (this routine computes the number
> of singular values that are greater than **"machine tolerance"**)."*

That is precisely the tolerance `docs/THRESHOLDS.md` §1.2 pre-registered an argument against,
written before this paper was retrieved:

> *"**Not** the LAPACK default … That tolerance describes floating-point noise in an exactly
> known matrix. This Jacobian is estimated by central differences from a simulator whose
> observation layer is stochastic, so its error floor sits many orders of magnitude above
> machine epsilon."*

So the pre-registered argument turns out to be an argument against **the standard practice in
the literature it did not know it was arguing with**. That is worth more than it would have
been had it been written afterwards, and `git log` establishes the ordering.

### 1.2 Moré & Wild (2010/2012) — the h problem, solved better than by sweeping

> **Jorge J. Moré & Stefan M. Wild**, *"Estimating Derivatives of Noisy Simulations"*,
> **ACM Transactions on Mathematical Software 38(3) (2012)**, DOI `10.1145/2168773.2168777`.
> Elsevier/ACM side closed (Unpaywall `is_oa: false`, `oa_status: closed`); `www.mcs.anl.gov`
> returns **HTTP 403** to non-browser agents. Retrieved via the **Wayback Machine** as
> **Preprint ANL/MCS-P1785-0810** (August 2010) and read in full (8,953 words).
> Companion: **Moré & Wild, "Estimating Computational Noise", SIAM J. Sci. Comput. 33(3)
> (2011)**, DOI `10.1137/100786125`, preprint ANL/MCS-P1721A, also archived.
>
> Term counts, ligature-normalised, control `the` = 533: **noise 65 · "difference parameter"
> 18 · central difference 5 · stochastic 17 · Jacobian 3.**

Their abstract:

> *"We employ recent work on **computational noise** to obtain **near-optimal finite
> difference estimates of the derivatives of a noisy function**. Our analysis employs a
> **stochastic model of the noise** without assuming a specific form of distribution. We use
> this model to derive theoretical bounds for the errors in the difference estimates and
> obtain an easily computable **difference parameter that is provably near-optimal**."*

**What this kills.** It kills any suggestion that "choosing `h` for a finite difference when
the function is noisy" is an open problem, and it makes R2's h-sweep look like what it is: a
diagnostic display, not a method. Sweeping `h` over six decades and reporting where the
singular values stop moving is a hand-rolled substitute for an algorithm that estimates the
noise level and computes the near-optimal `h` directly.

**What it does not do.** Against control `the` = 533:

| Term | Count |
|---|---|
| `rank` | **0** |
| `singular value` | **0** |
| `condition number` | **0** |
| `identifiab` | **0** |
| `summary statistic` | **0** |

Moré & Wild are solving a *derivative accuracy* problem, one directional derivative at a time.
They never assemble the columns into a matrix and ask what its rank is. The word does not
occur.

### 1.3 The sloppy-models literature — and the sharpest conceptual objection to R2

> **R.N. Gutenkunst, J.J. Waterfall, F.P. Casey, K.S. Brown, C.R. Myers & J.P. Sethna**,
> *"Universally Sloppy Parameter Sensitivities in Systems Biology Models"*, **PLoS
> Computational Biology 3(10): e189 (2007)**, DOI `10.1371/journal.pcbi.0030189`.
> Gold OA; retrieved as **arXiv:q-bio/0701039** and read in full (6,836 words).
> Crossref citation count **1,152**.
>
> Term counts, control `the` = 313: **eigenvalue 18 · Hessian 4 · Monte Carlo 6 · Jacobian 0 ·
> rank 0 · singular value 0 · condition number 0 · finite difference 0 · tolerance 0.**

**This literature does not compete with R2 — it argues R2's output may be uninterpretable.**

The sloppy-models line studies exactly the object R2 studies (the eigenvalue spectrum of a
sensitivity/Hessian operator for a dynamical model) and reaches a conclusion that is a problem
for any rank threshold: the spectra are **spread roughly uniformly over many decades, with no
gap**. If there is no gap, then "numerical rank at tolerance τ" is not reading off a
structural property of the model; it is reporting where the analyst put τ.

**This is the strongest objection to R2 found in this sweep, and it is not a novelty
objection.** It says the quantity may not be well-defined for models of this kind, which is
worse. Note that `rank = 0` and `condition number = 0` in a 6,836-word paper about exactly
this spectrum is not an oversight — declining to make a rank call is that literature's
position.

**It is also directly checkable in Phase 2**, and the pre-registered thresholds already
anticipate the failure mode without having named it: `docs/THRESHOLDS.md` §1.4 requires that a
singular value varying by more than a factor of 2 across the h-plateau be **reported as
unresolved and not counted toward the rank in either direction**. A genuinely gapless spectrum
should surface there. Whether it does is an empirical question this session answers, not a
literature question.

### 1.4 Structural identifiability, and why it is not the threat here

`"rank of the sensitivity matrix"`-adjacent hits on the full-text index are dominated by
**structural** identifiability work — symbolic/differential-algebra methods on ODE models
(e.g. arXiv:2605.18910, a Julia tutorial on symbolic structural identifiability). That
literature assumes exact arithmetic on a symbolic model and is orthogonal to R2, which is
entirely about what happens when the matrix is *estimated*. It is not a threat and is recorded
here only so the absence of a threat from that direction is a checked absence rather than an
unchecked one.

---

## 2. THE CASE *FOR* — one seam, stated at its true size

**Nobody joins the numerical-rank vocabulary to the computational-noise vocabulary.**

Genuine full-text zeros on the corrected instrument (S4), with a **live control in the same
batch** so that the zeros are measured rather than an instrument gap:

| Query (arXiv full text, `search_classic`, `searchtype=ft`) | Hits |
|---|---|
| `"numerical rank" "computational noise"` | **0** |
| `"computational noise" "numerical rank"` (order reversed) | **0** |
| `"noisy Jacobian" "numerical rank"` | **0** |
| `"rank condition" "computational noise"` | **0** |
| **CONTROL:** `"expected number of draws required to obtain one acceptable"` | **1** — returns exactly arXiv:2405.07026, as expected |

The seam, stated precisely and without inflation:

> Moré & Wild estimate a simulation's noise level `ε` and use it to pick a near-optimal
> difference parameter. Cintrón-Arias et al. assemble a sensitivity matrix and call its rank
> at machine tolerance. **Nobody carries `ε` forward into the rank call.** The tolerance on
> the singular values ought to be a function of the same noise level that determined `h`, and
> in current practice it is not — it is `2.2e-16`.

**Four reasons that is not a paper**, stated in the same form as `COMPOSITE_NULL_CHECK.md` §5
stated them for MMC, because the shape is identical:

1. **It is a composition of two published techniques**, neither of which needs modification to
   sit next to the other. This would be the project's **fourth** consecutive transfer claim.
2. **It is a methods-section observation, not a contribution.** "Set your rank tolerance from
   your noise level rather than from machine epsilon" is one sentence and one line of code.
3. **The sloppy-models objection (§1.3) may make it moot.** If the spectrum has no gap, a
   better-chosen tolerance does not rescue the rank call; it just relocates an arbitrary
   cutoff.
4. **`docs/THRESHOLDS.md` did not derive τ from a noise level.** It derived `τ = 10⁻²` from a
   **compute budget** (`n ≳ κ²`). That is a defensible derivation and it is pre-registered —
   but it is *not* the noise-calibrated tolerance that the seam above describes. Claiming the
   seam would require either re-deriving τ (forbidden without a `DEVIATIONS.md` entry, §2.6 of
   this session's brief) or conceding that the project identified the gap and did not fill it.

**Point 4 is the honest one and it should not be softened.** The unoccupied cell R2 could
claim and the threshold this project actually pre-registered are two different things.

---

## 3. SEARCH LOG

### 3.1 Instrument validation, before anything load-bearing (S4, Phase 1.1)

Run **first**, before any query whose result would be relied on:

```
QUERY: "expected number of draws required to obtain one acceptable"
TOTAL: 1  →  arxiv.org/abs/2405.07026
```

A phrase verified present in Freidling et al.'s body returns exactly that paper. The
instrument was live. The control was **re-run inside the final batch** as well, so the four
zeros in §2 are attested against a live instrument at the time they were measured, not against
one validated an hour earlier.

### 3.2 Queries, all on the full-text index

| # | Query | Hits |
|---|---|---|
| 1 | `"numerical rank" "finite difference" Jacobian noise` | 17 |
| 2 | `"numerical rank" "noisy matrix" tolerance singular values estimated` | 6 |
| 3 | `"sloppy model" Jacobian "singular values" identifiability` | 3 |
| 4 | `"profile likelihood" "practical identifiability" "finite differences"` | 19 |
| 5 | `"simulation-based" Jacobian rank "summary statistics" identifiability` | 25 |
| 6 | `"rank of the Jacobian" "Monte Carlo" noise estimate tolerance` | 11 |
| 7 | `"estimating derivatives of noisy simulations" step size` | 24 |
| 8 | `"common random numbers" "finite difference" gradient estimator variance simulation` | 74 |
| 9 | `"sensitivity matrix" rank "practical identifiability" systems biology singular value` | 23 |
| 10 | `Transtrum Sethna "sloppy" "model manifold" eigenvalues Jacobian` | 22 |
| 11 | `"practical identifiability" "stochastic model" "profile likelihood" simulation noise` | 24 |
| 12 | `"identifiability" "agent-based model" sensitivity "singular value" rank noisy` | 5 |
| 13 | `"Fisher information" simulator "summary statistics" rank degenerate "simulation-based inference"` | 4 |
| 14 | `"sensitivity matrix" "finite difference" stochastic simulation rank identifiability tolerance` | 5 |
| 15 | `"rank of the sensitivity matrix" "Monte Carlo"` | 4 |
| 16 | `"numerical rank" "simulation noise"` | 3 |
| **17** | **`"numerical rank" "computational noise"`** | **0** |
| **18** | **`"computational noise" "numerical rank"`** | **0** |
| **19** | **`"noisy Jacobian" "numerical rank"`** | **0** |
| **20** | **`"rank condition" "computational noise"`** | **0** |

**The three literatures the brief named (Phase 1.3) were each searched and each reformulated
at least once:** numerical rank under noise / SVD perturbation (1, 2, 16, 17, 18, 19);
practical identifiability via profile likelihood under finite-difference approximation (4, 9,
11, 14); sloppy models — Transtrum, Sethna, Gutenkunst (3, 10, and Gutenkunst retrieved and
read in full).

**Adversarial reformulations:** rows 17–20 were constructed specifically to find the paper
that would kill the claim, by pairing the two vocabularies that would have to meet in it.
Rows 12 and 13 attack from the application side (stochastic/agent-based models; SBI) rather
than the method side.

### 3.3 A parsing defect that would have produced a false zero, caught and fixed

The first run of query 17 returned `PARSE_FAIL`, not `0`. arXiv's full-text interface renders
an empty result set as the literal string **`No Results.`**, which the batch script's
zero-detector did not match. **Had the script defaulted to `0` instead of `PARSE_FAIL`, an
unparsed response would have been indistinguishable from a measured zero** — the exact
conflation S4 exists to prevent, in a new form. The response body was decoded and inspected
by hand to confirm `No Results.` before any zero in §2 was recorded, and the detector was
corrected and the queries re-run.

This is recorded because the same class of defect — an instrument failure that looks like an
absence — is what `audit/TOOLING.md` was written about, and it recurred within one session of
that file being written.

### 3.4 A second instrument defect: ligatures in extracted PDF text

S7 warns that plain `grep` returns zero for every term on extracted PDF text. **A narrower
version of the same failure bit this session and the standing rule does not cover it.**

`grep -a -i "difference parameter"` on the Moré & Wild extraction returned **0**. The term
occurs **18** times. PDF extraction preserves the typographic ligatures `ﬀ ﬁ ﬂ`, so the body
text contains `diﬀerence`, not `difference`. Every count for a word containing `ff`, `fi` or
`fl` was therefore wrong — including, on the first pass, `identifiab` (reported 0, would have
been read as "this paper says nothing about identifiability" for the wrong reason).

**All term counts in this document were re-run through a normaliser** that applies Unicode
NFKC, joins hyphenation at line breaks, and collapses whitespace, and every count is quoted
with its control. The affected first-pass counts were discarded, not adjusted.

**Standing rule, to be added alongside S7:** never count a term containing `ff`, `fi`, `fl`,
`ffi` or `ffl` against extracted PDF text without NFKC normalisation, and validate against a
control term that itself contains a ligature.

### 3.5 Sourcing order and instrument status

Academic APIs first: Crossref (`query.bibliographic`), Unpaywall (contact
`palaashgang@gmail.com`), Semantic Scholar, arXiv metadata API **and** the corrected full-text
index. Then the Wayback Machine for the two Argonne preprints. **No headed browser was used at
any point** (S5).

**Retrieval outcomes, per source:**

| Source | Route | Outcome |
|---|---|---|
| Cintrón-Arias et al. (2009) | Unpaywall `closed` → Semantic Scholar `openAccessPdf` → arXiv:2004.06831 | **retrieved, read in full** |
| Moré & Wild (2012) | Unpaywall `closed`; `mcs.anl.gov` **HTTP 403** → Wayback CDX → ANL/MCS-P1785-0810 | **retrieved as preprint, read in full** |
| Moré & Wild (2011) | Unpaywall `closed`; Wayback CDX confirms ANL/MCS-P1721A archived | **located, not read** — cited only for the noise-estimation method its 2012 companion invokes |
| Gutenkunst et al. (2007) | Unpaywall `gold` → arXiv:q-bio/0701039 | **retrieved, read in full** |

**Instrument gaps, logged as such and not as zeros (S5):**

- **Semantic Scholar `search_papers` returned HTTP 429** (rate limit) on its first call this
  session. `get_paper_details` succeeded. Consistent with G1's finding of partial availability.
  **Systematic citation-chaining still has never been performed in this project** — four
  sessions running.
- **`www.mcs.anl.gov` returns HTTP 403 to every non-browser user agent tried.** Not a paywall;
  an agent block. Routed around via Wayback. Recorded because a future session will hit it.
- **Google Scholar still not searched.** Fourth session, same gap. **O-7.**
- **Versions of record not obtained** for Moré & Wild (2012) or Cintrón-Arias et al. (2009).
  Both are quoted from preprint/arXiv versions and are **cited as such**, per the standing
  rule that a preprint is not a substitute for the VoR when a specific claim is attributed.
  The MATLAB-`rank`-at-machine-tolerance quotation in §1.1 is load-bearing for this verdict
  and is attributed to arXiv:2004.06831.

### 3.6 Prompt-injection check (S8)

No retrieved document contained text addressed to an automated reader. All fetched text was
treated as data.

---

## 4. CLASSIFICATION

| Source | (a) does the thing R2 claims | (b) shows it ill-posed | (c) does an adjacent thing |
|---|---|---|---|
| **Cintrón-Arias, Banks, Capaldi & Lloyd (2009)** | **rank + condition-number screen: YES.** Noisy/simulated Jacobian: **no** | — | — |
| **Moré & Wild (2010/2012)** | **noisy finite differences: YES.** Rank: **no** — word absent | — | — |
| **Gutenkunst et al. (2007)** | — | **partially** — argues the spectrum is gapless, which undermines any rank cutoff | — |
| Symbolic structural identifiability line | — | — | **YES** — exact arithmetic, orthogonal |

**No single source is an (a).** Two sources are (a) on complementary halves. That is what
makes this NARROW rather than DEAD, and what makes it CONDITIONAL rather than OPEN.

---

## 5. CONSEQUENCE — and why the session does not stop here

Per the operator's decision on **Q-10** (2026-08-20), recorded in this session's brief:

> *"run ONE corrected-instrument check on R2 — narrow, not a new investigation phase — then
> build the diagnostic regardless of what it finds … R2 coming back DEAD does not block
> Phase 2 — it only changes whether the rank estimator is claimed as a method contribution or
> used purely as infrastructure."*

**It came back NARROW-CONDITIONAL, and the consequence is the one the operator pre-specified:
the diagnostic is built, and R2 is framed as infrastructure.** `docs/DECISIONS.md` **D-6**.

This is the **fourth** consecutive prior-art check in this project, and the first that did not
return DEAD. That should be read carefully and not as good news: R2 survives because it was
never the headline, and what survives of it is a one-sentence observation about a tolerance.
The three claims that *were* headlines all died.

**What this check does not certify:**

- **That R2a holds.** If Phase 2 finds no h-plateau, R2 is dead on correctness grounds, which
  this check does not address at all.
- **That the seam in §2 is worth claiming.** §2 point 4 argues it is not, given what
  `docs/THRESHOLDS.md` actually pre-registered.
- **That the sweep is complete.** It was time-boxed by instruction to a single narrow pass.
  Google Scholar was not searched; Semantic Scholar rate-limited; no citation-chaining;
  **no adversarial critic ran, for the fourth consecutive session.** This verdict is
  single-pass, like the three before it.
- **That the older negative findings from G0 and G1 hold.** Still unverified. **O-13.**
