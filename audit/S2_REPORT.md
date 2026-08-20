# S2 — Session G2 report

**For a reader who has not seen this session.** Written 2026-08-20.

> **Three things to know before anything else.**
>
> **1. The third headline claim is prior art.** The composite-null gap is real and was
> correctly identified — and it is the founding premise of a sixty-year-old literature, with
> at least three published repairs. The one the session proposed to invent is **Dufour
> (2006)**, *maximized Monte Carlo*: maximise the simulated p-value over the nuisance space
> and you get *"provably exact level, irrespective of the sample size."*
>
> **2. A large part of why this keeps happening is now known, and it is not a research
> problem.** G0 and G1 both reported "arXiv full-text" searches. **Those searches were
> metadata-only.** The real full-text index found Dufour, the repro-samples line and the
> co-sufficient-sampling line within the first hour of looking.
>
> **3. Still no code.** Third consecutive session in which the technical deliverable did not
> happen. Each stop was instruction-following, not drift. The cumulative effect is the same.

---

## 1. WHAT THIS SESSION DID

Phase 0 (sync) and Phase 1 (the composite-null threat check) ran. **Phase 1 returned DEAD,
which under the brief's §1.5 stops the session before Phases 2, 3 and 4.** It did.

| Path | Status |
|---|---|
| `audit/COMPOSITE_NULL_CHECK.md` | **new** — the threat check. Verdict **DEAD** |
| `audit/TOOLING.md` | **appended** — the arXiv full-text correction |
| `docs/OPEN_QUESTIONS.md` | **Q-10 raised (blocking)**; Q-9 answered; Q-8 narrowed |
| `GATES.md` | **G2 added — `NOT MET — UNSIGNED`** |
| `audit/CLAIM_GRAPH.md` | status banner only; **not rewritten** (Phase 3 not reached) |
| `DEVIATIONS.md` | **D-7** |
| `audit/R2_THREAT_CHECK.md` | **NOT WRITTEN** — Phase 2 did not run |
| `src/`, `results/` | **unchanged.** No Python. No numbers |

---

## 2. THE VERDICT

Full evidence in `audit/COMPOSITE_NULL_CHECK.md`. In brief:

| Source | What it does | Class |
|---|---|---|
| **Dufour (2006)**, *J. Econometrics* 133(2) | *"maximizing the [p-value] with respect to the nuisance parameters yields a test with **provably exact level**, irrespective of the sample size and the number [of] replications used … we call the latter **maximized Monte Carlo (MMC) tests**."* Applies *"as long as the null distribution … **can be simulated** once the nuisance parameters have been specified"* | **(a) solves it** |
| **Xie & Wang (2022)**, arXiv:2206.06421 | Repro samples: *"simulation-inspired"*, *"guaranteed coverage"*, *"**likelihood-free**"*, and §3.2 *"a general technique to handle nuisance parameters through **profiling** … maintains the desired coverage rates … **even in finite sample settings**"* | **(a) solves it** |
| **Awan & Wang (2023)**, arXiv:2303.05328 | Repro samples applied where *"the marginal likelihood … is intractable"*; *"guaranteed coverage and type I errors, **even accounting for Monte Carlo error**"* | **(a) solves it** |
| **Barber & Janson (2022)**, *Ann. Statist.* | States the simple-vs-composite distinction as **textbook background**, then repairs it by conditioning on a sufficient statistic; generalised as approximate CSS | **(a) solves it** |
| **Freidling, Zhao & Gao (2024)** | Assumes a **(partially) sharp null**, says so explicitly, and states the limitation in its own discussion | (c) does not address it |

The brief: *"Only (a) kills this session's target claim outright."* **There are three.**

### What Freidling et al. actually say — because the brief asked precisely

`nuisance` **0**, `composite` **0** across 20,339 words (control `the`=1448). But **not
silent**: `sharp null` appears 14 times, and the requirement is explicit —

> *"Under this hypothesis, **all potential outcomes can be imputed** from the observed
> outcomes, so … **P(Z = · | R, X_R, Y_R(·), S(Z)) is known**."*

That is the simple-null requirement in randomization-inference vocabulary. They **also**
already handle partial non-sharpness, by conditioning on an extra statistic `G`. And they
state their own scope limit in the discussion. So the operator's hypothesis was **half right**
— the exactness really does depend on the null law being known, and a simulator's generally is
not — and **half wrong**: this is neither unnoticed nor unaddressed.

### The one unoccupied cell, at its true size

Nobody has composed MMC with a *selection event*: full-text `"selection event" "maximized
Monte Carlo"` returns **0**, and Freidling et al. cite none of Dufour, Barnard or Dwass. But it
is a composition of two published, composable techniques; it would be the project's **third
consecutive transfer claim**; the costs multiply (`1/p₀` rejection cost *at every nuisance
value visited*, and Freidling et al. already measure 150× for the rejection cost alone); and
MMC is **conservative by construction**, which sits badly under a headline containing the word
"exact".

---

## 3. THE TRAJECTORY ACROSS THREE SESSIONS

The brief asks for this comparison as output in its own right. It is the most useful thing
this session produced.

### What the originating plan claimed, and what is left

| Claim, as `audit/PLAN_SOURCE.md` stated it | Status now | Killed by |
|---|---|---|
| **C1** — component attribution is a multiple-selection problem; competitive testing with error control over the selected component corrects marginal mis-attribution | **DEAD as novelty.** The framing is the *opening pedagogical example* of selective inference | Fan & Lv (2008) §4.1; Fithian, Sun & Taylor (2017) Ex. 1; Neufeld–Perry–Witten (2026) Ex. 1; Hsu MCB (1984) |
| **C2** — non-identifiable in general; identifiable iff the summary Jacobian has full column rank; *described by the plan as "the real contribution"* | **DEAD** | **Kahl et al. (2019)**, *PRX* 9:041046, resting on Sain & Massey (1969); also Brynjarsdóttir & O'Hagan (2014) eqs. (16)–(17); Catchpole & Morgan (1997) Thm 1 |
| **A1** — ≈33 papers detect or robustify, *none attribute* | **PARTIAL** | Leclercq (arXiv:2209.11057), which localises to a named model layer — and was in the plan's own bibliography |
| **D2** — Bayesian conflict diagnostics need a tractable likelihood, so they don't transfer | **DEAD** | Chakraborty, Nott & Evans: *"applicable regardless of whether the likelihood is tractable or not"* |
| **H1** — CPU-only, 10⁴–10⁵ simulator runs | **DEAD as stated** | The protocol's own factors multiply to ~2×10⁶ for one baseline |
| **R1** (G1's replacement headline) — the simulator's null lets you rejection-sample the selection event, so no analytic characterisation is needed | **DEAD** | **Freidling, Zhao & Gao (2024)**, Algorithm 1 *"Rejection sampling"*; and the 2026 review already lists the strategy with its objections |
| **The composite-null gap** (G2's replacement headline) | **DEAD** | **Dufour (2006)** MMC; Xie & Wang (2022); Barber & Janson (2022) |
| **R2** — simulation-based noisy-rank estimator | **UNTESTED.** Never checked, in any session | — |

**Nothing from the original plan survives as a novelty claim.** One thing has never been
tested.

### The shape of it

Each session adopted a headline, and each headline died to a paper found by direct retrieval
in the *next* session, usually within a few queries:

- **G0** killed the plan's own headline (C2) and proposed R1.
- **G1** killed R1 and proposed the composite-null gap.
- **G2** killed the composite-null gap and proposes **nothing**.

That last clause is deliberate. Proposing a fourth framing without operator input is the
behaviour that generated the first three.

### The instrument, which changes how to read all of the above

`audit/TOOLING.md` now records that **the arXiv API's `all:` field searches metadata, not full
text**, and that G0 and G1 both described their searches as full-text. Demonstrated, not
assumed: two phrases verified present in paper bodies return **0** from the API.

Coverage difference on the same questions, this session:

| Query | Metadata API | Full-text index |
|---|---|---|
| selective inference + nuisance | 7 | **54** |
| Monte Carlo test + nuisance parameters | 2 | **24** |

**All three of this session's killing sources surfaced only on the full-text index.**

**What that invalidates, precisely.** *Positive* findings are unaffected — "here is a paper
that does this" does not depend on how it was found, so the Kahl and Freidling refutations
stand. *Negative* findings from G0 and G1 are downgraded to **instrument gaps**: every zero
they reported as evidence that a literature lacks something was a metadata zero. One was
re-checked here on the working index and survived; the rest are unverified.

**So the honest reading of "three for three" is ambiguous, and both readings should be put
plainly.** It may mean the area is crowded and mature — Taylor, Barber, Witten, Panigrahi,
Dufour and Xie are all working in it. It may equally mean the project has never once had a
competent prior-art sweep of its own idea space. Both are in **Q-10**.

---

## 4. GATE G2

**`NOT MET — UNSIGNED`.** Outcome (a) of the three the brief named: third consecutive kill,
stopped at Phase 1.

`GATES.md` records the criteria, what was not done (R2 check, the diagnostic, Phase 3), and
what G2 explicitly does not certify — including that **R2's untested status is not survival**.

---

## 5. WHAT REMAINS, AND WHAT SHOULD HAPPEN NEXT

**Q-10 blocks everything.** Its options:

- **(a) One clean full-text prior-art sweep, then decide.** Cheap. It would be the project's
  first sweep with a working instrument, and **R2 should be its first target** — it has been
  overdue for two sessions.
- **(b) Drop the mechanism and go empirical.** `PIVOT.md` response 2: build the diagnostic,
  run it, report whether a standard 3-component SIR simulator passes its own identifiability
  precondition. **This is buildable now** and needs no surviving mechanism claim. The
  thresholds are already pre-registered in `docs/THRESHOLDS.md` from a session that produced
  no numbers, which is the strongest form that commitment can take.
- **(c) Stop and write up the negative result.** `PIVOT.md` response 3, written in advance so
  that reaching it is a decision rather than a failure.

**My reading, offered as such and not acted on.** (b) is the only option that produces
something this project does not already have, and it is the one whose value does not depend on
any novelty verdict — a rank diagnostic showing that a standard simulator fails its own
separability condition is a real finding regardless of who first wrote the rank condition.
(a) is cheap enough to do first and should gate (b) only for R2.

---

## 6. PROCESS CAVEATS

**No code, for the third consecutive session.** G1 stopped at Phase 2.4, G2 at Phase 1.5. Both
were the brief's own pre-registered stop conditions firing, and honouring them is the point of
writing them. It remains true that this project has an extensive audit trail and no software.

**Phase 2 did not run, so R2 is still untested.** This is now the single most overdue item in
the project. It was flagged as mandatory in this session's own brief and was cut by the Phase-1
stop rule.

**No adversarial critic ran, for the third consecutive session.** This report's verdict is
single-pass. It rests on positive evidence — named, quoted theorems in retrieved full texts —
which is the strongest kind available, but no independent agent has attempted to refute it.

**Dufour's version of record was not retrieved.** *J. Econometrics* is paywalled; Unpaywall and
OpenAlex both report `closed`. The **CIRANO working paper 2005s-02** was retrieved and read
(17,226 words), and every MMC quotation is attributed to that, not to the VoR. Under the
project's standing rule, a working paper is not a substitute for the VoR when a specific
theorem is attributed — so if MMC is cited in any manuscript, the VoR must be obtained first.

**`audit/CLAIM_GRAPH.md` was flagged, not rewritten** (`DEVIATIONS.md` D-7), and
`docs/DECISIONS.md` D-5/D-6 named in the brief's header were not written, because both are
Phase-3 artefacts and Phase 3 was not reached.

**One thing this session got wrong before catching it.** The first arXiv queries were run
through the metadata API exactly as G0 and G1 had, and the discrepancy was noticed only when a
zero-count looked implausible against a paper already sitting in the vault. The check that
caught it — query a phrase you have already verified is present in a fetched body — took two
minutes and should have been run in G0. It is now a standing rule in `audit/TOOLING.md`.

**What would most improve confidence, in order:** (1) threat-check **R2** on the working index;
(2) re-run G0's and G1's load-bearing *negative* searches on the full-text index, since none of
them have been verified; (3) run an adversarial critic against this report's verdict; (4)
obtain Dufour's version of record before citing MMC.
