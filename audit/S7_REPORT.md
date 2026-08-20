# S7 — Session G7 report

**For a reader who has not seen this session.** Written 2026-08-21.

> ## THE PAPER'S SCOPE IS CLOSED, AND FOR THE FIRST TIME THE REPOSITORY CONTAINS FIGURES
>
> **Eight sessions in, the project stops deciding what it is and starts being it.**
> `docs/DECISIONS.md` **D-16**, the operator's: the MMC composition is dropped as an
> experimental vehicle and kept as a **stated negative result**. Four contributions, no
> composition, consolidated in `audit/FINAL_CLAIMS.md` — the file a drafting session works from
> directly.
>
> | | claim | kind | figures |
> |---|---|---|---|
> | **C1** | the rank and coherence diagnostic, as a pre-inference decision procedure | method | 1, 2 |
> | **C2** | `S_B` separates the three components under **all eight** declarable family assignments | positive | 3, 4, 5 |
> | **C3** | at two distortion parameters per component the same set is **inseparable**, on a progression–observation confound | boundary | 3, 7 |
> | **C4** | rejection-sampling-based exact conditional inference **does not terminate** for this class of simulator | cautionary | 6 |
>
> **Seven figures now exist and none did before.** `figures/`, vector PDF at the venue's own
> 5.5-inch column width — a number parsed out of `neurips_2026.sty` at import time rather than
> typed. Each carries a `.provenance.json` recording the `results/` files it read, their
> hashes, the commit that drew it, its drafted caption, and — per plotted series — **the exact
> dotted path in the YAML the numbers came from**, re-read from disk and compared.
>
> **The boundary is located, and the collapse turns out to be a slide rather than a cliff.**
> `results/boundary_sweep.yaml`: ten half-widths from 0.001 to 0.05, 7,602,000 null draws, six
> minutes. **About one decade of acceptance probability per 0.7% of relative nuisance error**,
> log-linear at `R² = 0.94`. The pre-registered cost gate passes at every declared corner
> **only inside a ±0.5% box** on all five nuisance coordinates at once.
>
> **A prediction made before the run held.** The sweep's docstring, committed before it produced
> a number, predicted the nuisance shift would overtake the observation noise near `w ≈ 0.006`.
> It does, between 0.005 and 0.0075 — **and that is exactly where the gate stops passing.**
>
> **One thing to read with suspicion**, disclosed in full below and in `DEVIATIONS.md`: a flag
> written this session **read FALSE for a reason other than the one it named**, which is D-8's
> failure mode for the **third** time in this project (**D-17**), and the countermeasure D-8
> itself proposed was available and was not applied to it.

---

## 1. WHAT THIS SESSION DID

| Path | Status |
|---|---|
| `docs/OPEN_QUESTIONS.md` | **Q-16 ANSWERED** — the diagnostic-only path, with the rationale above the question it settles |
| `docs/DECISIONS.md` | **D-16 DECIDED** — composition dropped as a vehicle, kept as a negative result; scope closed at four contributions |
| `audit/MMC_COMPOSITION_SPEC.md` | **re-headed** as a historical / negative-result document, **nothing deleted**; **§4.1** annotates the superseded 10⁷–10⁹ estimate (**O-28**) and **§4.2** reports the boundary sweep (**O-30**) |
| `src/diagnostics/boundary_sweep.py` | **new** — the sweep, its design, and the shape criterion, all committed *before* it produced a number |
| `results/boundary_sweep.yaml` | **new numbers** — 10 widths × 42 design points, plus a `θ₀` anchor and 33 re-measured points; Wilson intervals throughout; seed spans asserted disjoint from G6's |
| `results/BOUNDARY_TABLE.md` | **new, generated**, so no number in prose is hand-typed (S11) |
| `src/viz/style.py`, `src/viz/provenance.py` | **new** — one place where every visual decision lives, and the trace from a figure back to `results/` |
| `src/viz/fig1..fig7` | **new** — seven figure scripts |
| `figures/` | **new** — 7 PDFs, 7 preview PNGs, 2 editable SVGs, 7 provenance sidecars, an index |
| `audit/FINAL_CLAIMS.md` | **new** — the current claim set, superseding every claim structure in `audit/` |
| `results/FINAL_CLAIMS_NUMBERS.md` | **new, generated** — 75 load-bearing numbers, each with its dotted path |
| `audit/CLAIM_GRAPH.md` | **superseded** by a banner pointing at `FINAL_CLAIMS.md`; not rewritten, seventh session |
| `tests/` | **140 → 177**; of the 37 added, **19** require a check to fail, a bad input to be refused, or a flag to come out both ways |
| `GATES.md` | **G7 added**, unsigned |
| `DEVIATIONS.md` | **D-16** (a results file written twice), **D-17** (a flag reading FALSE for the wrong reason) |
| `PROVENANCE.md`, `results/README.md`, `audit/README.md` | extended to cover figures and the new results files |
| `results/jacobian_rank.*`, `results/robustness/*`, `results/p_sel.yaml`, `results/cost_gate.yaml`, `docs/THRESHOLDS.md` | **untouched.** No threshold revised, no prior number overwritten |

---

## 2. THE BOUNDARY SWEEP, AND WHY THE ORDER OF EVENTS IS THE ARGUMENT

The composition's cost gate failed in G6 on **non-termination**: at a relative nuisance
half-width of 0.05 — the narrowest box measured — zero acceptances in 100,000 draws. So the
boundary lay below everything measured and nobody knew where.

**The session brief closed the scope question before the sweep ran, and that ordering is the
whole reason the sweep is admissible.** `docs/DECISIONS.md` D-16 was decided, committed and
pushed at `f11de77`. The sweep's script was written afterwards and committed at `c2f3641`
before it produced a number. Its docstring states in advance what it would have done had the
result gone the other way:

> *"if this sweep had found that the cells stay reachable out to 0.04 and collapse only past
> it, the composition would still be dropped."*

and every gate row in the results file carries a field saying it decides nothing. **A check
that could only soften a verdict, thought of after seeing that verdict, is the pattern
`DEVIATIONS.md` D-9 and D-13 exist to make visible**, and this is what it looks like when the
pattern is avoided rather than merely disclaimed.

### 2.1 What it found

Reproduced from `results/BOUNDARY_TABLE.md`, generated, primary case `AAA` studentised:

| half-width `w` | `p_min(w)` | shift ÷ noise | gate |
|---|---|---|---|
| 0 (`θ₀`) | 0.2331 | 0 | **PASS** |
| 0.001 – 0.003 | 0.2323 → 0.2320 | 0.15 → 0.46 | **PASS** |
| **0.005** | 0.1770 | **0.77** | **PASS** — the last one |
| **0.0075** | 0.0965 | **1.15** | SPLIT |
| 0.01 – 0.02 | 0.0548 → 1.68×10⁻³ | 1.52 → 3.05 | SPLIT |
| 0.03 | 1.00×10⁻⁵ | 4.79 | **FAIL** |
| **0.05** | **0** (≤ 3.84×10⁻⁵) | 8.39 | **FAIL** |

**The collapse is GRADUAL under the pre-registered criterion** — the largest local log-slope is
2.265× the median, against a declared threshold of 3 — and close to exponential in the
distortion magnitude at **−141 decades per unit relative half-width**, `R² = 0.94`. The two
`plain` variants classify **ABRUPT**, and that split is reported rather than averaged: the shape
is a property of the selection rule as much as of the simulator.

### 2.2 The sentence this buys, which a bare threshold statement could not

**The pre-registered gate passes at every declared `(M, N)` corner only inside a ±0.5%
relative box on `β`, `γ`, `ρ`, `I₀` and `σ_obs` simultaneously.** `docs/OPEN_QUESTIONS.md` Q-16
guessed the requirement would land near ±0.4% and called such a bound *"no epidemiologist will
accept"*. **The guess was close and the judgement stands**: a transmission rate known to half a
percent is not a nuisance parameter, it is a known constant. Option (a) of Q-16 — bound `Ω₀`
until termination returns — now has a price stated in the units a domain reader argues in, on
top of the CSEMMC downgrade from finite-sample to asymptotic validity that §4 point 2 already
charged for it.

### 2.3 The prediction that held, and it is the transportable part

The script's docstring, before the run: from G6's recorded median shift of 26.5 standard
deviations at `w = 0.05` and a single-draw noise magnitude of `√d = 3.162`, the shift should
overtake the noise near **`w ≈ 0.006`**, and the grid was placed to resolve that region.
Measured: **0.77 at `w = 0.005` and 1.15 at `w = 0.0075`.**

**And that crossing is where the gate stops passing.** In one sentence: *the composition remains
affordable for exactly as long as the nuisance perturbation is smaller than the observation
noise, and stops when it is not.* That is a one-line check anybody holding a different simulator
can run before attempting this composition on it, and it is the most transportable thing this
project has produced.

### 2.4 Two reproductions nobody arranged

Both on draws G6 never took; both checks were written into the script before the run and report
either way.

- **`θ₀` reproduces.** Twelve `(assignment, variant, cell)` comparisons, maximum two-proportion
  `|z| = 1.96` against a threshold of 3.
- **The ±5% collapse reproduces exactly** — zero acceptances again in 100,000 independent
  draws, and **21 of 42 design points with a dead cell, the same 21 of 42 G6 recorded.**

---

## 3. THE FIGURES, AND THE CONTRACT THEY ARE BUILT UNDER

`PROVENANCE.md` has required this since session G0, before any number existed:

> *"Every figure carries, in its caption or in a sidecar file, the results file(s) it was drawn
> from."*

**No figure existed until now, so the rule had never had to be honoured.** It is honoured by
machinery rather than by discipline.

| | figure | sources | data claims checked |
|---|---|---|---|
| **1** | the diagnostic, end to end | *(schematic)* | — |
| **2** | the simulator's structure and where each distortion acts | *(schematic)* | — |
| **3** | `S_B`'s full spectrum: base, adversarial, six-column union, with `τ` marked | `k6_spectrum.yaml` | 7 |
| **4** | all eight family assignments for `S_B`, with `S_A` as the control that fails | `k6_spectrum.yaml` | 3 |
| **5** | the verdict as a function of `τ`, with the exact flip points | `k6_spectrum.yaml`, `threshold_sensitivity.yaml` | 7 |
| **6** | the acceptance probability collapsing to zero — the negative-result figure | `boundary_sweep.yaml`, `cost_gate.yaml` | 11 |
| **7** | what the six-column confound actually confounds | `k6_spectrum.yaml` | 9 |

### 3.1 The check that can fail, and what makes it fail

A sidecar listing source files proves only that a script opened them. So each figure
**declares, per plotted series, the dotted path in the source YAML that series came from**, and
the sidecar writer re-reads the file from disk and compares. It reads FALSE when a number in
the figure is not at its declared path — a hand-typed value, a stale one, a transform applied
but not declared — or when the source changed under the figure, or when a schema change moved
the path. `tests/test_viz.py` shows it reading FALSE on each of those four.

**What it cannot catch, stated so it is not over-trusted:** it checks the declared series, not
the whole canvas. **Three figures carry hand-placed annotations that it does not cover**, each
disclosed in its own sidecar with the source-file value printed beside it. And it cannot say
whether a declared path is the *right* quantity to plot.

### 3.2 Two figures worth singling out

**Figure 6** is the paper's negative-result figure and it had one thing to avoid: reading as a
cost curve with a budget caption. The widths at which no draw ever entered the observed cell are
drawn as **downward triangles at the Wilson upper limit and joined to nothing**, because they
are bounds and not measurements — joining them would draw a cost where the finding is
non-termination. The gate is drawn as a **band** rather than a line, because the specification
declares `M` and `N` as ranges and the SPLIT region is a fact about the specification.

**Figure 7** was added beyond the six the brief scoped. Figure 3 shows *that* the six-column
object is rank deficient; Figure 7 shows *what the deficiency is made of*, and that is the
claim that carries the weight. `docs/DECISIONS.md` D-14's scope restriction is justified not by
a number crossing a threshold but by **both near-null directions mixing progression with
observation**, with transmission carrying under 5% of the energy in either — and until this
figure that existed only as two rows of a table.

### 3.3 Where the visual identity comes from, and one gap

Okabe-Ito, because it is the qualitative palette whose *design criterion* is deuteranope and
protanope separability. Roles assigned to colours once, with a guard that **refuses at draw
time** if a script asks for two scales that share one. Times, because `neurips_2026.sty` sets
`\rmdefault` to `ptm`, and the column width parsed out of that same file with an assertion that
it still matches — **a check that fires if the venue ever re-issues its template**.

**The gap, stated plainly (S7).** Matplotlib renders with whatever Times-compatible face the
machine has. This one resolved *Times New Roman*, recorded in every sidecar; a machine without
it falls through to a non-Times-metric face. **The fall-through is made visible in the record.
It is not prevented**, and preventing it would mean vendoring a font, which is a licensing
question this session did not have the standing to answer.

---

## 4. THE EIGHT-SESSION TRAJECTORY

Extending `audit/S6_REPORT.md` §5.

| Session | Claim adopted as headline | Outcome | Killed / qualified by |
|---|---|---|---|
| **G0** | **ex-C2** — attribution identifiable iff the summary Jacobian has full column rank | **DEAD** | Kahl et al. (2019), via Sain & Massey (1969) |
| **G1** | **R1** — calibrate the selection event by rejection sampling from the simulator's null | **DEAD** | Freidling, Zhao & Gao (2024), Algorithm 1 |
| **G2** | **the composite-null gap and its repair** | **DEAD** | Dufour (2006), maximized Monte Carlo |
| **G3** | *(none adopted)* — **R2** checked, having never been a headline | **NARROW-CONDITIONAL** | Cintrón-Arias et al. (2009) + Moré & Wild (2012) |
| **G4** | *(none adopted)* — **G3's own numbers** attacked | **SPLIT: `S_B` stands, `S_A` does not generalise** | this project, for the first time |
| **G5** | *(none adopted)* — **G4's own deferral** closed | **SPLIT: separable at one distortion parameter per component, not at two** | this project, for the second time |
| **G6** | *(none adopted)* — **the composition itself** priced | **FAIL: the rejection sampler does not terminate over the nuisance set** | this project, for the third time |
| **G7** | **four contributions adopted, by the operator** | **SCOPE CLOSED** — and the negative result acquires a shape and a boundary | *(nothing killed; the first session that ends by adopting rather than losing)* |

| | G0 | G1 | G2 | G3 | G4 | G5 | G6 | **G7** |
|---|---|---|---|---|---|---|---|---|
| Prior-art check run | yes | yes | yes | yes | n/a | n/a | n/a | **n/a** |
| Verdict | DEAD | DEAD | DEAD | N-COND | SPLIT | WEAK | FAIL | **SCOPE CLOSED** |
| Stopped early by its own rule | no | **yes** | **yes** | no | no | **yes** | **yes** | **no** |
| Code written | none | none | none | yes | yes | yes | yes | **yes** |
| Numbers produced | none | none | none | yes | yes | yes | yes | **yes** |
| Adversarial check against own output | no | no | no | no | **yes** | **yes** | **yes** | **partial** |
| A pre-registered rule fired against the project | — | — | — | no | no | **yes** | **yes** | **no** |
| **Figures produced** | no | no | no | no | no | no | no | **YES (7)** |
| **A claim set a drafting session can use** | no | no | no | no | no | no | no | **YES** |
| Independent review | no | no | no | no | no | no | no | **no** |
| Google Scholar searched | **no** | **no** | **no** | **no** | **no** | **no** | **no** | **no** |

### The shape of it, read honestly

**This is the first session that ends by adopting something rather than by losing something**,
and that is worth stating carefully, because the reason is not that the evidence improved. The
evidence is exactly what G5 and G6 left. **What changed is that the operator decided what the
paper is**, and the session's job was execution rather than adjudication. A reader of this
repository's history should notice that the four contributions include **two negative results
and one boundary** — the project is not claiming more than it did last session, it is claiming
the same thing in a shape that can be written down.

**What is genuinely better than it was.** The scope question that has been open in one form or
another since G1's `Q-8` is closed. The boundary the previous session deliberately did not
locate is located, and it was located in the only order that makes it admissible. Seven figures
exist, under a provenance contract the project wrote before it had any numbers and had never
had to honour. Every number the paper rests on now carries a path to its source.

**What is not.** No independent eye has been anywhere near this — not the figures, not the
claims, not the sweep. **The same session drew the figures, wrote the checks the figures pass,
and decided which of its own annotations the checks would not cover.** And the one process
failure this session had is the one the project keeps having: a flag that read FALSE for the
wrong reason, caught only by disbelieving output, in a session that had read both prior entries
about exactly that failure before writing any code.

---

## 5. PROCESS CAVEATS — what this session did badly

- **`DEVIATIONS.md` D-17: a flag read FALSE for a reason other than the one it named.**
  `theta0_reproduces_recorded_p_sel` asked whether this run's estimate lay inside the *recorded*
  estimate's Wilson interval — which uses one of the two measurements' sampling errors and
  rejects perfectly consistent 100,000-draw estimates about 17% of the time per cell. It was
  very nearly guaranteed to read FALSE whatever the data did: a **vacuous flag in the opposite
  direction**, one that can hardly ever pass. Replaced by a two-proportion `z`, with the
  observed maximum published beside it as a number so the threshold is not load-bearing, and
  with the superseded comparison kept under a name that says what it actually tests.
- **The threshold that replaced it was fixed after the run**, which is D-9's and D-13's pattern.
  Disclosed in the constant's own docstring, in the results file, and in `DEVIATIONS.md`.
- **`results/boundary_sweep.yaml` was written twice** and **the figures were drawn twice**, both
  because of defects caught after the fact rather than before. The sweep's substance is
  bit-identical between runs, verified rather than asserted; the figures are byte-reproducible,
  so the discarded pass differed only in a recorded flag. **D-16.**
- **Three figures carry hand-placed annotations outside the automatic check.** Disclosed per
  figure; not the same as checked.
- **`audit/CLAIM_GRAPH.md` still not rewritten**, seventh session. The banner is stronger and
  the work is still not done.
- **No literature check ran**, by scope. The non-termination of a rejection sampler under
  nuisance drift is not exotic; nobody here has looked, and C4 will be asserted without a
  prior-art sweep behind it.
- **Google Scholar still not searched.** Eighth session. **O-7.**
- **`results/` still carries G3's vacuous `leakage_checked` literal.** **O-22.**
- **Q-15 / O-26 still open at zero simulation cost.**
- **The machine was loaded throughout** (load average 8–18 on 8 cores, shared with unrelated
  work), so wall-clock figures are upper bounds. Draw counts are unaffected.

---

## 6. WHAT SHOULD HAPPEN NEXT

1. **Look at the seven PDFs.** **P-1.** This is the one gate where reading the report is not
   sufficient: the provenance chain says the numbers are right and says nothing about whether
   the pictures are legible or whether a caption describes its own figure.
2. **Confirm or correct `audit/FINAL_CLAIMS.md`.** **P-2.** In particular **C1**, where
   `docs/DECISIONS.md` D-6 and D-16 pull in different directions and this session wrote a
   sentence intended to satisfy both rather than deciding between them.
3. **Draft `paper/main.tex`** — the next session's scope, working from `audit/FINAL_CLAIMS.md`
   and `figures/`. It must carry **D-14's four obligations**, of which the one that has never
   had a home is the first: *the single-mechanism restriction goes in the scope or limitations
   section, and the six-column counterexample is stated rather than omitted.*
4. **Answer Q-13** (**O-21**), still blocking the exact wording of C2's separability sentence
   and now the only blocking question left.
5. **Close Q-15 / O-26.** It costs no simulation and it sharpens C3: the intermediate `K = 4`
   and `K = 5` cases are constructible from columns already recorded.
6. **Run one literature check on the non-termination finding**, which is the one claim in the
   set that has never been checked against prior art at all.

---

## 7. POINTS REQUIRING OPERATOR INPUT

| # | Point | Notes |
|---|---|---|
| **P-1** | **Sign or reject G7 — after looking at the figures** | `GATES.md`. The "does not certify" section is the part that matters, and its first item is that **nobody but this session has seen these figures**. Reading this report is not sufficient for this gate |
| **P-2** | **Confirm `audit/FINAL_CLAIMS.md` is the paper you want to submit** | Especially **C1**: D-6 forecloses claiming the estimator or the rank rule as new, D-16 names the diagnostic as contribution 1, and the sentence written to satisfy both is a judgement a session should not be making alone |
| **P-3** | **Q-13** (**O-21**) — what may be claimed from a family-conditional separability verdict | **BLOCKING for C2's sentence only.** Narrowed by G5 to eight measured assignments; not closed |
| **P-4** | **Q-3** (reciprocal reviewer), Paris in-person attendance | Unresolved since G0 |

*Q-16 is closed — the operator answered it at the start of this session and it is recorded as
`docs/DECISIONS.md` D-16. Repository visibility is settled by D-11 and is not on this list.*

---

## 8. THE ONE-PARAGRAPH VERSION

The project stopped deciding what it is. **Four contributions, closed by the operator: the
diagnostic, the eight-assignment separability result under a single-mechanism scope, the
six-column confound that shows exactly where that scope is load-bearing, and the
non-termination finding stated as a genuine negative result.** Two of the four are negative and
one is a boundary, which is the honest shape of what eight sessions produced. The boundary the
previous session deliberately left unlocated is now located, and located in the only order that
makes it admissible — the scope decision was taken, committed and pushed before the script that
measures it was written. **The collapse is a slide, not a cliff: about one decade of acceptance
probability per 0.7% of relative nuisance error, with the pre-registered gate passing at every
declared corner only inside a ±0.5% box.** The mechanism was predicted before the run from a
ratio of nuisance shift to observation noise, the prediction held, and the crossing is exactly
where the gate stops passing — which turns the finding into a one-line check somebody with a
different simulator can actually run. **And for the first time the repository contains figures**:
seven of them, each carrying the results file it came from, the hash of that file, and the
dotted path of every number on the page. What none of it has is a second pair of eyes. The
figures were drawn, checked, and had their own exceptions decided by one session, and the single
process failure this session had was the one this project keeps having — a flag reading FALSE
for a reason other than the one it named, caught by disbelief rather than by any check.
