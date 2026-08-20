# S0 — Session G0 report

**For a reader who has not seen this session.** Written 2026-08-20.

> **Two things to know before anything else.**
>
> **1. The NeurIPS 2026 deadline is 29 August 2026 AoE — nine days away.** All four
> candidate venues share it. Nothing in this repository is buildable into a 5-page paper
> in nine days.
>
> **2. The plan's risk model is inverted.** It treats C2 — the identifiability result — as
> "the real contribution" and C1 as the claim at risk. In fact **C2 as a theorem is prior
> art**, published in *Physical Review X* in 2019 and traceable to a 1969 control-theory
> result; while **C1 survives narrowly**, via a mechanism the plan does not propose.

---

## 1. STATE — what exists, and what does not

### Exists

| Path | What it is |
|---|---|
| `README.md` | Project description; no venue commitment |
| `GATES.md` | Gate register. G0 `ready for review — UNSIGNED` |
| `PROVENANCE.md` | Number-traceability contract, written before any number exists |
| `OUTSTANDING.md` | Numbered open actions; carries the deadline and repo-visibility banners |
| `DEVIATIONS.md` | Three recorded departures from instruction, with reasons |
| `LICENSE` | MIT, fetched from `spdx.org`, not written from memory |
| `audit/PLAN_SOURCE.md` | The plan, byte-for-byte. SHA-256 verified: `2ff70482…5ae689` |
| `audit/LEDGER_ASSERTIONS.md` | 20 assertions with pre-registered confirm/refute criteria, plus appended verification results |
| `audit/LEDGER_CITATIONS.md` | Every reference, with identifier, retrieval status, and accuracy of the plan's characterisation |
| `audit/LEDGER_DESIGN.md` | 8 design commitments, each with the consequence of violating it |
| `audit/CLAIM_GRAPH.md` | C1/C2 dependencies and failure propagation |
| `audit/PIVOT.md` | Pre-registered pivot, **committed before any search was run** |
| `audit/VENUE.md` | Three workshops + backup, from venue sites and the OpenReview API |
| `audit/TOOLING.md` | Research-tooling probe; Branch B |
| `docs/OPEN_QUESTIONS.md` | Q-1..Q-7 |

### Does not exist

**No simulator. No diagnostic. No attribution code. No results. No manuscript. No figure.
No number.**

`src/`, `results/`, `paper/`, and `review/` contain nothing but a README and a `.gitkeep`.
This is by design for this session — but it is the fact that collides with §5.

---

## 2. VERDICT

### C1 — competitive attribution with error control over the selected component
# **NARROW-CONDITIONAL**

It survives, but not as written, and not independently of C2.

**What constrains it:**

| Constraint | Source | Effect |
|---|---|---|
| The problem framing is textbook | **Fan & Lv (2008) §4.1**; **Example 1 of Fithian, Sun & Taylor (2017)**; **Example 1 of Neufeld–Perry–Witten (2026)** | "Marginal tests mis-attribute under correlation" is the opening pedagogical example of selective inference, twice over. Solutions since **Hsu's MCB (1984)**, including a simulator-specific one (**Matejcik & Nelson, 1995**). **Zero novelty budget available here.** |
| Per-coordinate localisation already exists in SBI | **RNPE, arXiv:2210.06564** | Spike-and-slab per summary statistic, reporting a posterior misspecification probability per statistic, with indicators inferred **jointly** — closer to "competitive" than the named gatekeeper is |
| Module-level conflict p-values already exist, likelihood-free | **Chakraborty, Nott, Drovandi, Frazier & Sisson, arXiv:2203.09782** | Calibrated module-level conflict p-value in likelihood-free cutting feedback |
| Layer-level localisation already exists in SBI | **Leclercq, arXiv:2209.11057** — *in the plan's own bibliography* | Diagnoses misspecification at a named layer, on Lotka–Volterra |
| Knockoff control requires C2's condition | **Barber & Candès Prop. 2.2** | FDR control over distortion components holds **iff the summary Jacobian has full column rank**. C1's method and C2's theorem are the same statement |

**What is not constrained — the one genuinely new thing found this session:**

Conditional selective inference is blocked in general because the selection event must be
characterised analytically. **In SBI that blocker is removable.** Under H₀ the simulator
draws from the exact null, so rejection-sampling the cell {argmin = i} gives the **exact
conditional null distribution** — no characterisation needed. This removes the obstruction
that **Liu, Markovic-Voronov & Taylor (2023)** call the central barrier to conditional SI.
The cost is compute (~N_alt/α draws), which is a budget problem, not an identification
problem.

No prior statement was found, across nine conjunctive arXiv full-text queries, OpenAlex
queries for `"selective inference" + "likelihood-free"` and `+ "ABC"`, OpenReview, the
2026 selective-inference review, and the full text of Anau Montel et al.

**Conditional on:** (a) reframing around this mechanism rather than around "e-BH/knockoff-
style selection"; (b) stating **which** guarantee is delivered — see §3; (c) C2's rank
condition holding, since knockoff well-posedness requires it.

### C2 — the identifiability characterisation and rank condition
# **DEAD as stated.** Residual: **NARROW**.

Both halves are prior art, **in the model-discrepancy setting specifically** — which
removes the "but ours is about discrepancy, not parameters" defence.

| Half | Prior art |
|---|---|
| "Data constrain only the sum" | **Brynjarsdóttir & O'Hagan (2014), eqs. (16)–(17)**, verbatim: *"There is redundancy in the model; ζ(·) is identifiable from observations, but θ and δ(·) are not"* — with the manifold M_ζ = {(θ,δ) : η(x,θ)+δ(x) = ζ(x)} and the infinite-data limit explicit. **The plan cites this paper as lacking the result it actually contains.** |
| "Identifiable iff full column rank" | **Catchpole & Morgan (1997), Theorem 1** — an *iff* on rk[∂μ/∂θ]; equivalent by their Theorem 3 to **Rothenberg (1971)**; restated for ODE observables by **Chis, Banga & Balsa-Canto (2011)**; Lie-derivative form in the **Hermann–Krener** observability rank condition |
| **Both, applied to an additive per-component model-error term, plus an observable-design algorithm** | **Kahl et al. (2019), *Physical Review X* 9:041046**, via the **Sain–Massey (1969)** invertibility rank condition |
| Column-space version on a discrepancy function | **Plumlee (2017), *JASA* 112:1274** |

**Verified directly, not via report.** Retrieved and read in full:
**Kahl, Wendland, Neidhardt, Weber & Kschischo (2019)**, *"Structural Invertibility and
Optimal Sensor Node Placement for Error and Input Reconstruction in Dynamic Systems"*,
*Physical Review X* 9:041046, open access. Its abstract states that *"unknown inputs to
open systems and **model errors** can be treated under the common framework of
**invertibility**, which is a requirement for **reconstructing these disturbances from
output measurements**"*, and that they *"introduce a new **sensor node placement
algorithm** to select a minimum set of **measurement positions** … required for
invertibility."* §III D gives *"the algebraic rank condition proven by **Sain and
Massey**"*: the system *"is invertible **if and only if** rank Q_{N−1} − rank Q_{N−2} =
M."* Term counts over the full text: "invertib" 231, "model error" 32, "Sain"/"Massey" 4
each.

That is C2's rank condition (an iff), C2's object (per-component additive model error),
and C2's summary-design consequence (which measurements make attribution possible) — in
one 2019 *PRX* paper resting on a 1969 result.

**Kahl et al. is the killing citation.** It is not the generic parameter result. It treats
model errors as additive **per-component** unknown inputs, gives a necessary-and-sufficient
rank condition for attributing them, and adds an algorithm for choosing which observables
make attribution possible — which is C2's rank condition *and* its summary-design
consequence, in *PRX*, in 2019.

Corroborating: **Presanis et al. (2017)** already state a Jacobian non-singularity
condition for valid node-level conflict inference; **Wu, Shirvan & Kozlowski (2018),
arXiv:1801.10309** already establish sensitivity↔identifiability in the Kennedy–O'Hagan
discrepancy setting.

**The residual, and it is real but modest:** every source above assumes the map is
available **symbolically** or is **analytically differentiable**. A simulator is neither.
So what survives is *a simulation-based estimator of the summary Jacobian and the
finite-sample behaviour of its rank* — with Kahl et al.'s own dichotomy, *"there is no such
thing like nearly invertible"*, making the noisy near-degenerate case acute and unsolved.

---

## 3. WHAT DIED

| # | Assertion | Verdict | Refuted by |
|---|---|---|---|
| **E1** | The non-identifiability claim is novel | **REFUTED** | Brynjarsdóttir & O'Hagan (2014) eqs. (16)–(17); also Marshall & Spiegelhalter (2007) for the prior-vs-likelihood case |
| **E3** | The full-column-rank condition is novel | **REFUTED** | Catchpole & Morgan (1997) Thm 1; Rothenberg (1971); **Kahl et al. (2019) *PRX* 9:041046** via Sain–Massey (1969); Plumlee (2017) *JASA* |
| **F1** | Marginal tests mis-attribute under correlation — as a contribution | **REFUTED as novelty** | Fan & Lv (2008) §4.1; Fithian, Sun & Taylor (2017) Ex. 1; Neufeld–Perry–Witten (2026) Ex. 1; Hsu MCB (1984) |
| **D2(a)** | Conflict diagnostics need a tractable likelihood | **REFUTED** | Chakraborty, Nott & Evans (arXiv:2202.09993): *"applicable regardless of whether the likelihood is tractable or not"*; Mao et al. (2021); Chakraborty et al. (arXiv:2203.09782); Yuyan/Evans/Nott (2025); Ratmann et al. (*PNAS* 2009) |
| **D2(b)** | SBI has no DAG | **REFUTED as stated** | Decomposing a simulator supplies one. The repaired requirement — a separator node with two conditionally independent partitions — **is C2's identifiability claim**, so it is not an independent distinction |
| **H1** | CPU-only, 10⁴–10⁵ runs | **REFUTED as stated** | The protocol's own factors multiply to ~2×10⁶ for one baseline; see §7 |
| **A1** | ≈33 papers detect/robustify, **none attribute** | **DOWNGRADED to PARTIAL** | **Leclercq (arXiv:2209.11057)** — in the plan's own bibliography — localises misspecification to a named model layer, on Lotka–Volterra |
| **C6, C5, C1, C2** | Four citation bylines | **REFUTED** | Verified against the papers themselves. See §6 |

### The structural finding

**C1 and C2 are not independent, and the plan's fallback strategy assumes they are.** Three
separate couplings were found:

1. RNPE's per-summary granularity means C1's remaining defence is the component-vs-summary
   distinction, which only has content where summaries do not map one-to-one onto
   components — i.e. where C2's rank condition fails.
2. The repaired "no DAG" defence collapses into C2's identifiability claim.
3. Knockoff FDR control over distortion components holds **iff** the summary Jacobian has
   full column rank — C1's method and C2's theorem are one statement.

`CLAIM_GRAPH.md` predicted that the genuinely bad outcome was not "C1 dies" but "E3 or D2
fails, damaging the fallback and the primary claim together." **Both failed.**

### And the guarantee the plan does not name

"Error control over the selected component" conflates three different things:

1. **Selective type-I error** — valid given that component i was selected, under H₀.
2. **FDR over the selected set** — proportion of flagged components not responsible.
3. **Probability of correct selection** — that the flagged component *is* the culprit.

**An applied reader will assume (3), and no selective-inference method delivers it.** It
belongs to ranking-and-selection / MCB, which the plan does not cite. The paper must say
which one it provides.

---

## 4. WHAT SURVIVED — and what it now needs

### Survivor 1 — the differentiators against the named gatekeeper (fully intact)

Anau Montel, Alvey & Weniger genuinely do not do this. Read in full (11,676 words):
"competitive" 0, "degeneracy" 0, "attribution" 0, "which distortion" 0; both uses of
"distinguish" are H₀-vs-H₁. Their own conclusion claims **detection**.

**Needs:** the B4 claim re-framed. They are **not** naive about multiplicity — §II.3
computes a trials-corrected global p-value on the **minimum** p-value, accounting for
correlations. That controls the **global null**, not the identity of the argmin. Write the
distinction, not the flat "no error control", or a reviewer who has read §II.3 will
object and land it.

### Survivor 2 — simulator-exact conditional calibration of the selection event (the real find)

The mechanism in §2. **Needs:** a proof that the rejection-sampling construction gives the
exact conditional null; a compute budget (~N_alt/α); and a demonstration that it beats the
marginal procedure where they disagree.

### Survivor 3 — the simulation-based rank diagnostic (C2's residual)

**Needs:** the estimator itself; a defensible rule for deciding rank from a *noisy*
Jacobian; and honest positioning as *"specialises to … and we give the first
simulation-based estimator"*, not *"we characterise"*.

### Survivor 4 — the coupling, which nothing in the literature does

The rank condition says **when the attribution question is well-posed**; the
selective-inference machinery controls error **given** that it is. No source found couples
them, and Group F shows the coupling is exact rather than thematic.

### A technical warning that lands on the design, not the positioning

Kahl et al. also state, and this was read directly:

> *"For a noninvertible system, the null space of Φ is always infinite dimensional …
> which means that for noninvertible systems there are **infinitely many independent
> inputs which cannot be distinguished from each other**. This property shows that
> **there is no such thing as "nearly invertible."** Thus, any algorithm attempting to
> infer the inputs from the outputs is **bound to fail without further assumptions**."*

**This threatens design commitment D8 — "report equivalence classes where the rank
condition fails."** In their setting the degeneracy is not pairwise and not finite: the
null space is infinite-dimensional, so "components 2 and 5 are indistinguishable" is not
the right description of what fails. There is no graceful degradation to describe.

**But the setting differs, and the difference is exactly where this project's residual
lives.** Kahl et al. treat *function-space* unknown inputs in continuous-time systems, so
non-invertibility is infinite-dimensional by construction. This project's distortion
families are **finite-dimensional and parametric** (η ∈ ℝ^K), making the Jacobian a
finite d×K matrix where near-degeneracy *is* meaningful and a condition number *is*
informative. So the dichotomy does not straightforwardly import — **and saying precisely
why is itself part of the residual contribution**, since it is the difference between a
structural result and a numerical one.

This must be settled before D8 is implemented, and it sharpens Q-5. It is also the
clearest illustration of the session's general finding: the prior art is close enough that
the contribution has to be stated as a *difference from* it, not in ignorance of it.

**This is the strongest available framing of the paper**, and it is neither C1 nor C2 as
the plan states them. It is: *component attribution is well-posed exactly under a rank
condition estimable from simulation alone, and exactly there, simulators admit conditional
error control that ordinary statistics cannot obtain.*

---

## 5. VENUE

Full evidence in `audit/VENUE.md`; every fact carries its source URL.

**All three candidate workshops exist and all four of the plan's Sim2Science claims are
confirmed**, the scope language verbatim: *"Understanding and mitigating model
misspecification, including simulator diagnostics and discrepancy modeling."* The plan
missed a second bullet that is a direct solicitation of the identifiability work:
*"Analysis of simulator structure, degeneracy, simplifications, and identifiability."*

**Deadline: 29 August 2026 AoE — nine days.** Notification 29 September, which NeurIPS
says cannot be extended. All four venues share the deadline, so missing it closes NeurIPS
2026 entirely rather than one workshop.

**Conditional recommendation, per instruction — not a commitment.**

- **If C1 survives (it does, narrowly):** **Sim2Science** remains the better home even so.
  The e-values venue fits the *machinery*, but its scope contains no simulator or
  misspecification language at all, so the motivating problem would have to be
  re-explained from scratch inside 4 pages — and it would be read by Grünwald and Ramdas.
  Sim2Science names **both** halves of the work and gives 5 pages.
- **If C1 had died and C2 carried the paper:** Sim2Science would be the only home of the
  three. That branch is now moot, since C2 is the weaker claim.
- **Representations for the Physical Sciences does not fit.** Self-described as "tightly
  scoped" to self-supervision, transfer, sampling, tokenization.

**Format, given nine days and an empty `src/`:** the **2-page Tiny Paper track** is the
only format the current state can honestly fill. **The alternative worth putting
explicitly is skipping NeurIPS 2026** — everything here is non-archival, so a later venue
costs nothing but time.

**Three obligations the plan does not mention:** a mandatory reciprocal reviewer whose
failure to review desk-rejects our own paper; a required reproducibility checklist the
other venues waive; and discouraged parallel submission, making the three Paris venues
mutually exclusive.

---

## 6. CITATIONS — retrieval status, every failure named

**12 papers retrieved in full text and read**, including both decisive ones. Details in
`audit/LEDGER_CITATIONS.md`.

### Four byline errors, verified against the papers themselves

| Plan says | Actually |
|---|---|
| "**Montel**, Alvey & Weniger" | **Anau Montel** — a compound surname, split |
| "Ward, Cannon, Beaumont, Fasiolo & **Naderiparizi**" | Fifth author is **Sebastian M. Schmon**. arXiv:**2210.06564** |
| "**Kelly, Huang, Tomaselli, Wehenkel** (RoPE)" | **Wehenkel, Gamella, Sener, Behrmann, Sapiro, Jacobsen, Cuturi**. Only Wehenkel is right; "Tomaselli" belongs to a different paper |
| "Schmitt, Radev & Bürkner" | Schmitt, Bürkner, **Köthe**, Radev |

This is a pattern, not slips. Sim2Science's scientific advisors include **Jakob Macke** —
the related-work section will be read by people who know this literature.

### The "paywalled four" — the premise was wrong

Three of four are **open access**, located via OpenAlex: Kennedy & O'Hagan
(10.1111/1467-9868.00294), Brynjarsdóttir & O'Hagan (10.1088/0266-5611/30/11/114007),
Tuo & Wu (10.1214/15-AOS1314; arXiv:1507.07280). They were not blocked — they were not
looked for with an OA resolver.

### Retrieval failures — named, not glossed

| Ref | Status |
|---|---|
| **Arendt, Apley & Chen (2012), DOI 10.1115/1.4007390** | **NOT RETRIEVED.** ASME paywall. Abstract read via Crossref; full text unobtainable. **This matters**: if they state a rank or linear-independence condition, C2's residual weakens further. Current reading is inferred from the abstract, **not read from the text**. Logged **O-6** |
| **Tuo & Wu** | Retrieved as **preprint (arXiv:1507.07280)**, not the *Ann. Statist.* version of record. Adequate for context, **not** for attributing a specific theorem |
| Marshall & Spiegelhalter (2007) | Full citation **recovered**: *Bayesian Analysis* 2(2), DOI 10.1214/07-BA218. The plan gave no year, title, or venue |
| Presanis et al. (2013) | Full title recovered; DOI 10.1214/13-STS426, open access |

---

## 7. COMPUTE

**The plan's "CPU-only, ~10⁴–10⁵ simulator runs" does not hold as stated.**

The figure counts forward simulations for **one** experiment. The protocol is a product of
factors the plan lists separately and never multiplies: ≥200 replicates × ~10 collinearity
levels × K components × 4 baselines × **N_mc Monte-Carlo null draws** — the last of which
the plan never mentions, though a calibrated null is the point of the method.

At R=200, L=10, N_mc=1000, the Anau Montel-style baseline **alone** costs ~**2×10⁶**
simulations — 20× the stated ceiling, from one of four baselines. At N_mc=10⁴, which is
what a global p-value of order 10⁻³ actually requires, it is ~2×10⁷.

**CPU-only is right about the wrong thing.** The ODE solves are genuinely cheap —
milliseconds, embarrassingly parallel; 10⁷ of them finishes overnight. **The binding cost
is neural density estimation**, which the plan does not account for at all. NPE is
amortised over parameters but **not over the simulator**: each collinearity level changes
the simulator and forces a retrain, for both the RNPE baseline and the learned-test-
statistic baseline.

**Threshold at which off-machine compute becomes necessary:**

| Condition | Consequence |
|---|---|
| Forward simulation only, ≤10⁷ solves, no neural components | CPU-only holds; local, overnight |
| Neural baselines with ≤10 retrainings on low-dimensional summaries | CPU-only holds; wall clock in hours |
| **Neural retraining count × training time > ~1 working day of serial wall clock** (≳20–30 retrainings) | Off-machine becomes worthwhile — the debug loop gets too slow |
| Full protocol as written (≥200 × ≥10 × neural baselines) | **Off-machine required** |

**Nothing has been provisioned.**

**The first deliverable is exempt from all of it.** The rank diagnostic needs no inference
machinery, no neural training, no null calibration, no observed data — forward solves plus
a finite-difference Jacobian and an SVD, order 10³ solves, seconds to minutes on a laptop.
That is what makes the STOP condition cheap enough to be real, and given nine days it is
the only viable sequencing.

---

## 8. NEXT SESSION — first technical deliverable

**The Jacobian rank/coherence diagnostic on a 3-component SIR simulator.** Specified
precisely enough to build; **not built**.

**Files:** `src/simulators/sir3.py`, `src/simulators/summaries.py`,
`src/diagnostics/jacobian_rank.py`, emitting `results/jacobian_rank.<name>.yaml`.

**Components (K=3)** — the decomposition is a modelling commitment, declared in code and
prose: **transmission** (βSI/N), **progression** (γI), **observation** (reporting
fraction / delay / noise). Choosing the observation process is deliberate: it is the
component most likely to be collinear with the others, which is what makes the diagnostic
informative rather than decorative.

**Distortion families** δ_k(·; η_k), η_k ∈ ℝ, η_k = 0 recovering the base simulator, each
**smooth** through zero. The distortion *shape* determines the Jacobian column, so it is a
substantive choice, not a default.

**Summary sets — at least three**, because a rank result under one set is a statement about
that choice: **S_A** epidemic-curve features (peak height, peak time, final size, growth
rate); **S_B** ~10 time-binned incidence counts; **S_C** a deliberately impoverished set
(final size + peak height only) as a **positive control that should fail** — without a case
whose answer is known in advance, a rank number has nothing to validate against.

**The diagnostic:** J = ∂s/∂η ∈ ℝ^(d×3), columns by **central differences**, with **h
swept over several decades and the plateau reported** — a rank computed at one arbitrary h
is not a result. Common random numbers across ± evaluations if the simulator is stochastic.

Report per summary set: singular values; **numerical rank** at a stated tolerance;
**condition number**; **pairwise coherence**; **column norms**; and **right singular
vectors for near-null directions**, which name the equivalence class.

Column norms deserve separate emphasis: **a near-zero column means a component is invisible
to these summaries — a different failure from collinearity, with different consequences,
and rank alone conflates them.**

**The trap that would invalidate everything:** *the rank of J is not scale-invariant.*
Rescaling a summary or reparametrising η_k changes the singular values and can change the
numerical rank. Fix and document both normalisations — summaries by their prior-predictive
standard deviation, η by a fixed relative perturbation — before quoting any number.

**Decision, pre-committed on both branches:** full column rank with moderate condition
number under ≥1 defensible summary set → proceed, and that set becomes the study's;
rank-deficient under every set tried → the D4 STOP condition fires and the output is the
negative result plus equivalence classes. **G1 passes on either branch**; it fails only on
an unrun or uninterpretable diagnostic.

**Answer Q-4 and Q-5 in writing first.** Fixing the summary-set list and the rank tolerance
*after* seeing the singular values is the respectable form of the leakage failure in
`LEDGER_DESIGN.md` D3.

---

## 9. OPERATOR QUESTIONS

Full text in `docs/OPEN_QUESTIONS.md`.

| # | Question |
|---|---|
| **Q-1** | **Do we target NeurIPS 2026 at all, given nine days?** Options: 2-page Tiny Paper at Sim2Science; skip NeurIPS 2026 (all non-archival, so nothing is lost); or attempt the full 5-page paper (not recommended). **Blocking — gates the next session** |
| **Q-2** | Repository visibility — it is public and must be private before any unpublished result is committed. `gh` is unauthenticated here, so this could not be verified from this machine |
| **Q-3** | Who is the nominated reciprocal reviewer? Required at submission; failure to review desk-rejects our own paper; authors cannot be added later |
| **Q-4** | What counts as "any reasonable summary set" for the STOP condition, and what rank tolerance defines inseparability? Must be fixed **before** running the diagnostic |
| **Q-5** | What singular-value/coherence threshold defines an equivalence class? A substantive part of the method, not a numerical tolerance |
| **Q-6** | Is a multi-component misspecification condition in scope? As designed, exactly one component is off-spec at a time — the regime where competitive testing's advantage is **smallest** |
| **Q-7** | How should the plan's citation errors be handled? Recommend full re-verification of every reference before submission |

---

## 10. PROCESS CAVEATS — what this session did badly or incompletely

**The full 16-step pipeline did not run.** Steps 1 and 2 ran as specified. **Steps 3–9
were collapsed into four parallel depth investigations**, and **steps 10–16 — the
triple-draft ensemble, the four adversarial critics, the gap-fetch, the patcher, and the
polish/readability passes — did not run at all.** The findings in this report come from
primary sources read directly plus four investigator reports; they have **not** been
through the pipeline's adversarial review layer.

**Only some adversarial checking happened.** Each investigator was instructed to report
the case against novelty first and to run ≥3 adversarial searches, and each did. But
**zero of the four named critics (dialectic, depth, width, instruction) ran**, and no
patcher or polish auditor ran. The conclusions here are single-pass. To be explicit: **no
independent agent has tried to refute this report's own verdicts.**

**Google Scholar was never searched.** The plan flagged OpenReview *and* Scholar as gaps.
OpenReview was searched and is closed. **Scholar was not** — there is no API and no
authenticated path was configured. That gap remains open, unchanged from the plan.

**Arendt, Apley & Chen (2012) was not retrieved** — the one genuine paywall. It is also
the single most likely remaining source of a further weakening of C2's residual. The
current characterisation is inferred from the abstract, not read.

**Tooling failures encountered and worked around:**
- `hyperresearch fetch-batch` **silently returned zero notes** for a 9-URL batch while
  reporting `"ok": true`. Individual `fetch` calls on the same URLs worked. All batch
  fetching was abandoned for sequential fetches. A silent zero-result success is a
  dangerous failure mode and would have gone unnoticed without an explicit count check.
- **Semantic Scholar was rate-limited (HTTP 429) for the entire session.** All academic-API
  work went through OpenAlex and the arXiv API instead. Citation-chaining via Semantic
  Scholar's citations endpoint — which the sourcing order calls for — **did not happen**.
- **`grep` treated the extracted PDF bodies as binary**, silently returning zero matches
  for every term. This nearly produced false "0 occurrences" evidence for the load-bearing
  claims about the gatekeeper paper. Caught because a control term ("the") also returned
  zero. **All load-bearing zero counts were then re-verified with `grep -a`** and hold. Had
  this not been caught, the central B3/B5 evidence would have been fabricated by a tooling
  artefact.

**No `hyperresearch lint` or integrity gate was run**, because the pipeline steps that
produce their inputs (critic findings, patch log, polish log) never ran.

**The vault-tag search is unreliable.** `hyperresearch search "" --tag <tag>` returns zero
results despite the tag being correctly applied, so source counts here were tracked by
total vault growth (438 → 490+ notes) rather than by tag query.

**What would most improve confidence, in order:** (1) retrieve Arendt et al. 2012;
(2) run the four adversarial critics against this report's verdicts, especially the C1
"genuinely new mechanism" claim, which rests on negative searches; (3) search Google
Scholar; (4) *(closed during this session — see below)*.

**Closed before writing:** the Kahl et al. (2019) rank condition was flagged as
load-bearing and unread, then retrieved and read directly (16,492 words, *PRX* is open
access). It confirms the investigator's report and goes further; see §2 and §4. The
remaining three items stand.
