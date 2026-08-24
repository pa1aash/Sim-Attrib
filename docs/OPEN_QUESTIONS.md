# Open questions

Questions an agent session cannot answer. Numbered and carried across sessions. Answered
questions stay, with the answer and the date, because the reasoning behind a settled
decision is worth more later than the decision alone.

## Open

### Q-17 — What did the external reviewer's T2-4 and T2-6 findings say? *(new, G11; not blocking the gate, blocking full closure of the review)*

**Raised 2026-08-25 by session G11's own preparation of `GATES.md` G11 / `audit/S11_REPORT.md`.**

An independent external reviewer with no project history returned Weak Reject on the paper, with
6 Tier-1 and 15 Tier-2 findings, all reproduced verbatim in G11's session brief. A mid-session
context compaction retained every finding's substance in the carried-forward summary except
two: **T2-4 and T2-6**. Every other Tier-1/Tier-2 item's content was independently
reconstructible from this session's own commit messages (each states the finding it addresses in
prose, not only its tag); a full `git log` search for T2-4 and T2-6, under any label, found
nothing. **This session did not invent plausible content for them.**

**Why this is the operator's question and not a session's.** Nothing in this repository can
answer it — only the operator's own copy of the external review (wherever it was received) can.
Guessing at defensible-sounding content to close the gap would be exactly the kind of quiet
self-approval this project's own standing discipline exists to prevent.

**What must not happen:** a future session treating T2-4/T2-6 as closed, minor, or already
covered by some other fix, without the original text in hand to check against.

> ### Standing audit debt, carried and non-blocking (noted G3)
>
> **Some of G0's and G1's negative findings were made before the `search_classic` fix and are
> UNVERIFIED, not confirmed.** `audit/TOOLING.md` establishes that the arXiv API's `all:` field
> searches metadata, not full text, so every zero those sessions reported as evidence of
> absence was a *metadata* zero. Two have since been re-checked on the working index and
> survived (G2 re-checked one; G3's R2 sweep is the first check run entirely on the corrected
> instrument). **The rest are instrument gaps, not measured zeros.** Tracked as **O-13**.
>
> This is recorded here so a future session does not treat those findings as settled, and it is
> **not blocking**: the project's live claims — the composition in
> `audit/MMC_COMPOSITION_SPEC.md` and the empirical result in `results/` — do not rest on them.
> The *positive* findings that killed C2, R1 and the composite-null gap are unaffected, since a
> paper that does the thing does not depend on how it was found.

### Q-2 — Repository visibility *(answered in principle, action outstanding)*
**Answered 2026-08-20 by `docs/DECISIONS.md` D-4:** public during the build phase, private
before the paper draft or final results are committed. The *action* — flipping the setting
— remains the operator's and is tracked as O-1, not as an open question. `gh` is still
unauthenticated on this machine (re-checked 2026-08-20), so current visibility cannot be
confirmed from here; see O-4.

### Q-3 — Who is the nominated reciprocal reviewer? **(now unconditional — venue is decided)**
Sim2Science requires a named co-author at submission time who will review **2** papers.
Failure to review is grounds for **desk-rejecting our own submission**. All authors must
be listed at submission; none can be added later. This needs a real person committed.
No longer conditional: `docs/DECISIONS.md` **D-2** commits the project to Sim2Science.

### Q-6 — Is a multi-component misspecification condition in scope? *(unchanged, but now cheaper to decide)*

Still open and still a scope call. **Note for whoever answers it:** this question was framed
around strengthening C1's competitive-testing argument, and C1 no longer exists in that form.
Under `Q-8` option (b) the question becomes far less pressing — a rank diagnostic does not
care how many components are off-spec at once. Under option (a) it stays exactly as sharp as
`LEDGER_DESIGN.md` D6 describes.

Original question follows.


The design knocks exactly one component off-spec at a time, so ground truth is unique by
construction. But real simulators are wrong in several places at once — and that is the
regime where competitive-vs-marginal testing matters *most*. As designed, the experiment
tests C1's mechanism where its advantage is smallest. Adding one multi-component condition
would strengthen C1 considerably. Scope call.

### Q-7 — How should the plan's citation errors be handled? *(partly acted on; confirm the policy)*

**Acted on 2026-08-20 without waiting**, since it was cheap and the reference list was still
small: `audit/BIBLIOGRAPHY.bib` was built by **fetching** all 52 entries, and all four byline
errors are corrected against the fetched records. What still needs the operator's answer is
the **policy** — specifically whether a full re-verification pass *against the papers
themselves* is required before submission, over and above fetching from canonical indexes.

**This session found the reason it might be.** Crossref **and** OpenAlex both return an
incomplete author list for Catchpole & Morgan (1997), omitting Morgan; it took the
publisher's own article page to catch it. **Fetching from a canonical index is necessary but
not sufficient.** And one of G0's own citations — "Presanis et al. (2017)" — cannot be
resolved at all (O-11).

Original question follows.


Four byline errors were verified against the papers themselves, including one author
credited with a paper she is not on, and one citation that conflates two different papers
(`LEDGER_CITATIONS.md`). Sim2Science's scientific advisors include Jakob Macke, so the
related-work section will be read by people who know this literature. Recommend a full
re-verification pass over every reference before anything is submitted. Confirm.

### Q-8 — R1 is prior art. What is the paper now? **(BLOCKING — narrowed 2026-08-20)**

> **Update, G2.** Option **(a)** of this question — "rescope R1 to the transfer claim,
> requires solving Q-9 first" — is **FORECLOSED**. Q-9 is now answered, and its answer is
> that the repair is Dufour (2006). There is nothing left to contribute on that path. The
> live options are **(b) promote the diagnostic and go empirical** and **(c) report the
> negative outcome**, and they are now folded into **Q-10**, which supersedes this question
> as the blocking one. Original text follows.

**Q-8 as originally written (G1):**

**Raised 2026-08-20 by `audit/R1_THREAT_CHECK.md`, verdict DEAD.**

The mechanism promoted to the paper's headline by `docs/DECISIONS.md` **D-3** — calibrating
a selection event by rejection sampling from an exact null, so that no analytic
characterisation is needed — is published. **Freidling, Zhao & Gao (arXiv:2405.07026)**
implement it as a titled algorithm ("Algorithm 1: Rejection sampling") for arbitrary
conditioning events, with the same 1/p₀ cost analysis. The April-2026 review of the field
(**Neufeld, Perry & Witten, arXiv:2604.09779**) catalogues it as a known "Monte Carlo
strategy" and states the two standard objections to it. And **Liu, Markovic-Voronov &
Taylor (arXiv:2203.14504)** — the paper D-3 cites as *identifying the barrier* — does not
identify a barrier; it removes one, by bootstrap.

D-3 was recorded as conditional on this check returning SAFE. It returned DEAD.

**The options, with the honest cost of each:**

- **(a) Rescope R1 to the transfer claim.** "The construction is exact where the null is
  exact; a simulator supplies an exact model-based null, so this is the only exact option
  in SBI." Small, defensible, and requires solving the composite-null problem in Q-9 first.
  It is a *transfer and its consequences*, not a mechanism — precisely the wording
  `audit/PIVOT.md` pre-registered as response 1 to a novelty failure.
- **(b) Promote R2 and the demonstration.** Make the paper the noisy-rank estimator plus
  component attribution, with the conditional calibration cited rather than claimed. This
  is `PIVOT.md` response 2 — let the empirical finding carry it. It is a diagnostics paper.
  R2's novelty has **not** been threat-checked to the standard R1 just was.
- **(c) Report the negative outcome and stop.** `PIVOT.md` response 3, written in advance
  so that reaching it is a decision rather than a failure. Two successive headline claims
  have now been found to be prior art by direct retrieval.

**This question blocks Phase 3.** Per the session brief §2.4 and P-1, no code was written
for the mechanism, and the Jacobian diagnostic was not built. See `audit/S1_REPORT.md` §3
for the argument that option (b)'s deliverable is *technically* unblocked — R2 does not
depend on R1 — which the operator may wish to authorise separately.

### Q-10 — Three consecutive kills. Does this project continue? **ANSWERED 2026-08-20 — and executed**

> **ANSWER (operator, 2026-08-20).** *Option (a) then (b), in that order, with (b)
> unconditional.* Verbatim as recorded in session G3's brief:
>
> > "run ONE corrected-instrument check on R2 — narrow, not a new investigation phase — then
> > build the diagnostic regardless of what it finds. The diagnostic was already established
> > in G1's GATES.md as passing on either branch of its own STOP condition, independent of any
> > novelty verdict, so R2 coming back DEAD does not block Phase 2 — it only changes whether
> > the rank estimator is claimed as a method contribution or used purely as infrastructure."
>
> **Executed in full, session G3.** The R2 check ran on the corrected full-text instrument
> and returned **NARROW-CONDITIONAL** (`audit/R2_THREAT_CHECK.md`) — the first of four
> prior-art checks in this project not to return DEAD. Its consequence for framing is
> recorded as **D-6**: R2 is cited infrastructure, not a claimed method contribution. The
> diagnostic was then built and run: `src/simulators/sir3.py`,
> `src/simulators/summaries.py`, `src/diagnostics/jacobian_rank.py`, and
> `results/jacobian_rank.*.yaml`. **This repository now contains code and numbers, for the
> first time.**
>
> **The reading that should be carried forward, and it is not simply "the project
> continues".** R2 survived because it was never the headline. What survives of it is a
> one-sentence observation about a rank tolerance. All three claims that *were* headlines
> died. The project's viability now rests on the composition specified in
> `audit/MMC_COMPOSITION_SPEC.md`, which is a composition of two published techniques and
> says so first — and on the empirical finding in `results/`, whose value does not depend on
> any novelty verdict.

Original question follows.


**Raised 2026-08-20 by `audit/COMPOSITE_NULL_CHECK.md`, verdict DEAD.**

Three primary claims have now died to prior art, each found by direct retrieval, each after
being adopted as the paper's headline:

| Session | Claim adopted as headline | Killed by |
|---|---|---|
| G0 | **ex-C2** — per-component discrepancy identifiable iff the summary Jacobian has full column rank | **Kahl, Wendland, Neidhardt, Weber & Kschischo (2019)**, *PRX* 9:041046, via Sain & Massey (1969) |
| G1 | **R1** — calibrate the selection event by rejection sampling from the simulator's null; no analytic characterisation needed | **Freidling, Zhao & Gao (2024)**, arXiv:2405.07026, Algorithm 1 "Rejection sampling" |
| G2 | **The composite-null gap and its repair** | **Dufour (2006)**, *J. Econometrics* 133(2) — maximized Monte Carlo, provably exact level |

Each kill took between one and three targeted queries once the right instrument was used. The
third was found in the first hour of the session that went looking for it.

**A large part of the explanation is now known and is not a research problem.** Both prior
sessions ran what they described as "arXiv full-text" searches. Those searches were
**metadata-only** — see `audit/TOOLING.md`. The real full-text index found Dufour, the
repro-samples line and the co-sufficient-sampling line immediately. So the pattern is at
least partly an instrument failure, now fixed, rather than evidence that the whole area is
picked over.

**That cuts both ways, and the operator should weigh both.**

- *Argument to continue:* the searches were being run with a broken instrument, so the
  project has never actually had a competent prior-art sweep of its own idea space. One
  should now be run **before** a fourth claim is adopted, not after.
- *Argument to stop:* three for three is not bad luck, and the area — exact inference from
  simulation, with and without nuisance parameters, with and without selection — is
  demonstrably crowded, mature, and worked on by strong groups (Taylor, Barber, Witten,
  Panigrahi, Dufour, Xie). `audit/PIVOT.md` response 3 was written in advance precisely so
  that stopping would be a decision rather than a failure.

**The options:**

- **(a) Run one clean full-text prior-art sweep first, then decide.** Cheap, and it is the
  first sweep the project would have had with a working instrument. It should cover R2 —
  which has *still* never been checked — before anything else.
- **(b) Drop the mechanism entirely and go empirical.** `PIVOT.md` response 2: build the
  diagnostic, run it on a 3-component SIR simulator, report whether a standard simulator
  passes its own identifiability precondition. The novelty budget then rests on an
  empirical finding, not on machinery. **This is buildable now** and does not depend on
  any surviving mechanism claim.
- **(c) Stop and write up the negative result.** `PIVOT.md` response 3.

**This question blocks everything.** No further claim should be adopted, and no code written
against a claim, until it is answered.

### Q-13 — The separability verdict is conditional on the distortion families. What may be claimed from it? **(BLOCKING — G4; NARROWED, not closed, by G5)**

**Raised 2026-08-20 by `audit/G3_ADVERSARIAL_REVIEW.md` finding 2.**

`S_A` and `S_B` separate the three components under the three distortion families `sir3.py`
declares. Session G4 built **one** alternative triple, designed against a named target component
per family, ran it through the identical diagnostic at the identical pre-registered thresholds,
and reports the outcome in `results/robustness/`. **No second candidate set was tried and none
was discarded** — there was no search over families.

**Why this is the operator's question and not a session's.** It is not a correctness question:
both verdicts are correct statements about their own family sets, and nothing in `results/`
needs withdrawing. It is a question about **what sentence the paper is allowed to write**, and
the two available sentences differ in what a reviewer would do with them:

- **(a) The narrow sentence.** *"Under these three distortion families the components separate;
  under an adversarially chosen alternative triple built from the same simulator, they do not."*
  Defensible, and it is what the evidence supports. It also concedes, in the paper, that the
  precondition for the composition holds conditionally — and `audit/MMC_COMPOSITION_SPEC.md` §5
  makes that precondition load-bearing for whether the composition is worth building.
- **(b) Establish which side the typical case falls on.** Run the diagnostic across a
  *designed set* of family triples — not one favourable and one adversarial — and report the
  distribution of verdicts. This converts a conditional claim into a characterised one and is
  the only route to a sentence stronger than (a). It costs a session, and the set would have to
  be specified before any of it is run, or it becomes the leakage failure `LEDGER_DESIGN.md` D3
  names, pointed at whichever conclusion is wanted.

**Recommendation, offered as such: (a) now, and (b) only if the paper needs the stronger
sentence.** (a) requires no further compute and is honest. (b) is a real experiment with a real
design problem attached — "which family triples are representative" has no obvious answer, and
answering it badly is worse than conceding (a).

**What must not happen:** the base result being quoted without its condition. `results/` and
`docs/THRESHOLDS.md` now carry the qualification inline so that a future session cannot pick up
the number without it.

> #### Narrowed, session G5 (2026-08-20) — measured at eight points instead of two
>
> Q-13 was raised with the verdict measured at **two** family assignments: all-base and
> all-adversarial. `audit/K6_SPECTRUM_CHECK.md` measures it at **all eight** the two declared
> sets permit — every combination of one family per component — and **`S_B` separates at all
> eight**, `κ` from 6.628 to 65.64, every singular value resolved, no coherence pair flagged.
> Six of those eight assignments had never been tested. **Option (b) of this question — "run
> the diagnostic across a designed set of family triples and report the distribution of
> verdicts" — has therefore been executed for the closed set of triples the declared families
> allow, at zero simulation cost, and the distribution is degenerate: eight separable, none
> otherwise.**
>
> **Why this narrows rather than closes it.** Eight assignments drawn from **two** family sets
> is not a sample of distortion families in general, and one of the two sets was designed to
> fail. The conditioning Q-13 names has moved from "these three families" to "these two family
> sets, in any component-wise combination", which is a materially weaker condition and still a
> condition. **Recommendation (a) is unchanged and is now cheaper to defend.**
>
> The same session opened **Q-14**, which is the other half: what happens when a component
> carries *two* distortion parameters rather than one. Q-13 and Q-14 jointly, not severally,
> govern the paper's separability sentence.
>
> The same session also sharpened one G4 sentence in the unfavourable direction. G4 finding 2
> read `S_A`'s adversarial failure as working *"through its third family rather than its first
> two"*. The eight-assignment sweep shows the split is exactly on the **transmission** family:
> every assignment with the adversarial transmission family fails, every one with the base
> transmission family passes, and `ABB` — changing only that one family — already breaks `S_A`
> at `κ = 100.9`, which is 0.9% past the ceiling.

**This question is BLOCKING in one specific sense only:** it blocks writing the separability
claim into `paper/main.tex`. It does **not** block the `p_sel`/cost-gate measurement (**P-3**),
which measures a different quantity and would be informative under either answer.

### Q-14 — Separability holds one distortion parameter per component and fails at two. Which does the paper claim? **ANSWERED 2026-08-20 (operator, at the start of G6)**

**Raised 2026-08-20 by `audit/K6_SPECTRUM_CHECK.md`.**

`S_B` separates the three components under **all eight** component-wise assignments of a family
to a component that the two declared family sets permit — `κ` from 6.628 to 65.64, every
singular value resolved, six of the eight never tested before this session. **That is the
strongest evidence the project has produced for the separability precondition, and it is
reported first for that reason.**

**And the same run shows it does not extend.** Place all six declared distortion directions
side by side — two per component — and `S_B` is **INSEPARABLE** at `κ = 628.9`, rank 4 of 6,
with both near-null directions confounding **progression with observation**. None of the easy
explanations survives: every singular value is resolved to within 2.3% across the h-plateau, so
it is not an unconverged estimator; the verdict holds across `τ` from 0.005 to 1.0, so it is not
a threshold artefact; and `d = 10 ≥ 6` leaves no structural zero. Stated as a modelling
sentence: **a drifting removal hazard is nearly indistinguishable from a constant hazard change
combined with a drifting reporting rate.**

**Why this is the operator's question and not a session's.** Both results are correct and
neither withdraws anything. What is at stake is which sentence the paper writes, and the two
differ in what a reviewer can do with them:

- **(a) The one-parameter sentence.** *"Under a distortion model that assigns one
  one-parameter family to each component, the three components separate for `S_B` under every
  one of the eight assignments our two declared family sets permit."* True, now well supported,
  and it is exactly the precondition `audit/MMC_COMPOSITION_SPEC.md` §5 requires — so it is
  sufficient to license the composition. Its cost is that a reviewer may reasonably ask why a
  component's misspecification should be one-dimensional, and the honest answer is that it need
  not be.
- **(b) Claim identifiability of component-level misspecification more generally.** **Not
  available.** The six-column measurement is a counterexample, produced by this project's own
  code from its own declared families. Any sentence implying that a component's discrepancy is
  identifiable irrespective of how richly it is parameterised is refuted by
  `results/robustness/k6_spectrum.yaml`.

**Recommendation, offered as such: (a), with the six-column result stated in the paper as a
limitation rather than omitted.** It is the sentence the evidence supports, it licenses the
composition, and conceding the two-parameter failure in the paper is cheaper than having a
reviewer find it — particularly since the confound it names is one an epidemiologist would
recognise on sight.

**What must not happen:** the eight-assignment result being quoted as though it established
identifiability of component misspecification. It establishes separability of a
**three-dimensional** distortion space, eight times over.

**This question is BLOCKING in one specific sense only:** it blocks the paper's separability
sentence, jointly with **Q-13**, which it narrows but does not close. It does **not** block the
`p_sel`/cost-gate measurement (**O-16**), which measures a different quantity and would be
informative under either answer — and which this session did **not** reach, because the G5
brief halts on any verdict other than a clean pass.

> #### ANSWERED — operator, 2026-08-20, at the start of session G6. Recorded as `docs/DECISIONS.md` D-14.
>
> **Option (a).** The paper's scope is restricted to **single-mechanism-per-component**
> misspecification: at most one one-parameter distortion family per component. Inside that
> scope the eight-assignment result stands as the paper's separability claim. **Option (b) is
> not taken and is not available** — this project's own six-column measurement refutes it.
>
> **The condition attached to the answer is about placement, not content.** The restriction is
> to be stated **alongside** the positive result rather than after it, and the six-column
> counterexample is to be conceded in the paper rather than omitted. `docs/DECISIONS.md` D-14
> lists the four places that obligation lands, including `paper/main.tex`, which no session has
> yet drafted.
>
> **Q-13 is untouched by this.** It asks a different question — conditionality on the
> *distortion families* rather than on the number of parameters per component — and it stays
> **open and blocking** for the paper's separability sentence. The two are jointly binding.
>
> This answer is what G5's `audit/K6_SPECTRUM_CHECK.md` and `audit/S5_REPORT.md` recommended,
> and the operator took the recommendation.

### Q-15 — The intermediate component counts between 3 and 6 were not measured *(new, G5; not blocking)*

`K = 3` separates eight times over and `K = 6` does not. **Nothing was measured in between.**
The informative intermediate case is one component carrying two distortion parameters while the
other two carry one — a `d × 4` Jacobian — which is the smallest departure from the declared
model that could exhibit the progression–observation confound, and which would say whether the
failure needs all six columns or only four.

**It costs no simulation.** The normalised columns at every step size are recorded in
`results/robustness/k6_spectrum.yaml` under `raw_columns_normalised`, precisely so a later
session can answer this by re-analysis. It is not blocking because the composition's
precondition is a `K = 3` statement, and it is recorded so the gap is a named one rather than
an unnoticed one.

### Q-16 — The rejection sampler does not terminate over the nuisance set. Is the MMC composition the right vehicle at all? **ANSWERED 2026-08-20 (operator, at the start of G7) — the diagnostic-only path**

> **THE ANSWER, RECORDED ABOVE THE QUESTION IT SETTLES.** The operator takes **option (c)**,
> the recommendation this question offered: **the MMC composition is dropped as an experimental
> vehicle and retained in the paper as a stated negative result.** Recorded as
> `docs/DECISIONS.md` **D-16**, DECIDED, with the four contributions the paper now claims.
>
> **The rationale, in one paragraph.** The gate did not fail on price, it failed on
> **termination**: over the nuisance set the minimum acceptance probability is zero — no draw
> in 100,000 enters the observed cell at a five-percent perturbation, 95% upper bound
> 3.84×10⁻⁵ — and the obstruction is structural rather than budgetary. `§3.4`'s lemma requires
> the selection rule to be a fixed function of the data; the nuisance parameters shift the
> normalised summaries by a median of 27 standard deviations where the noise supplies about
> 3.16; so a `θ`-free rule selects deterministically and the observed cell becomes unreachable.
> **No machine changes that**, which removes the only reading under which "build it anyway" was
> a compute decision. Option (a) buys termination by bounding `Ω₀`, at the price of Dufour's own
> CSEMMC downgrade from finite-sample to asymptotic validity — i.e. by giving up the property
> the composition exists for — and option (b) requires inventing a rule after seeing the
> measurement that killed the obvious one, which is the leakage failure `LEDGER_DESIGN.md` D3
> names. **The measurement is therefore reported as a finding rather than as a failure**: it is
> the first thing this project has established about the composition rather than about its
> precondition, it is negative in a specific and quantified way, and it tells a reader of any
> simulator of this class what to check before attempting exact conditional inference on it.
>
> **What this does NOT do.** It does not withdraw anything in `results/`. It does not touch the
> separability precondition, which stands inside D-14's scope. It does not say the composition
> is wrong — only that this simulator, and any simulator whose nuisance-to-noise ratio resembles
> it, cannot serve as its demonstration. And it does not close **Q-13**, which remains open and
> blocking for the paper's separability sentence.
>
> **The boundary sweep this question priced was subsequently run** — session G7, Phase 1,
> `results/boundary_sweep.yaml` — **as characterisation, not as verdict-seeking.** The scope
> decision above was taken before it ran and does not depend on it. What it buys is a figure
> with a shape instead of a bare threshold statement.

**Raised 2026-08-20 by `results/cost_gate.yaml`, the first measurement this project has taken
of the composition rather than of its precondition.**

**What was measured.** `p_sel` — *"the probability a null draw lands in the observed selection
cell"*, `audit/MMC_COMPOSITION_SPEC.md` §4 — by direct Monte Carlo, 3,780,038 null draws,
under `S_B` with the selection rule of `src/attribution/selection.py`.

- **At the base parameter point the composition is comfortably affordable.** The worst
  selection cell holds **0.2346** of null draws under the primary assignment `AAA` with the
  studentised rule (95% CI 0.2320–0.2372), so one MMC test costs **4.2×10⁵ to 4.3×10⁷** draws
  against the pre-registered gate of 10⁸. **PASS.**
- **Over the nuisance set it is not affordable at any price.** The specification's own cost
  model takes the minimum over `θ ∈ Ω₀`, and at a relative half-width of **0.05** — the
  narrowest box measured — the minimum is **zero acceptances in 100,000 draws**, 95% upper
  bound 3.84×10⁻⁵. The cost is unbounded, and at least **2.6×10⁹** draws even at the cheapest
  declared `(M, N)`. **FAIL at every declared corner, under both selection-rule variants, for
  both family assignments, with the confidence interval deciding it.**

**The mechanism, measured rather than argued.** The selection rule must be a **fixed function
of the data** — §3.4's lemma needs one event applied to `y_obs` and to every replicate, so a
`θ`-dependent rule is not available. The nuisance parameters move the normalised summary
distribution by a **median of 27 and up to 65 standard deviations** at a half-width of 0.05,
against a single-draw noise magnitude of √10 ≈ 3.16. A `θ`-free rule facing a shift twenty
times the noise selects one component deterministically, and the observed cell becomes
unreachable. **That is precisely the case §3.4 singles out: *"If some admissible nuisance
value makes the observed selection impossible, the rejection sampler never terminates
there."*** It now has a number.

**Why this is the operator's question and not a session's.** It is not a correctness question
— nothing in `results/` needs withdrawing, and the separability precondition is untouched. It
is a question about **what the project's experimental vehicle is**, and there are three
answers with different costs:

- **(a) Bound `Ω₀` hard enough that the cells stay reachable.** `audit/MMC_COMPOSITION_SPEC.md`
  §4 point 2 already prices this: bounding `Ω₀` means Dufour's CSEMMC, *"which is
  **asymptotically** valid — trading away precisely the finite-sample exactness that motivates
  MMC"*. So this buys termination by giving up the property the composition exists for. **And
  the width at which termination returns has NOT been measured** — see the note below.
- **(b) Change `T_k` so the cells stay reachable under nuisance drift.** Not available in the
  obvious form: any rule whose reference point tracks `θ` is not a fixed function of the data
  and breaks §3.4's lemma, which is the composition's only theorem. Something cleverer may
  exist; nobody has proposed it, and inventing one after seeing this measurement would be the
  leakage failure `LEDGER_DESIGN.md` D3 names.
- **(c) The diagnostic-only path of `audit/PIVOT.md`.** The rank diagnostic as the
  contribution, with no attribution experiment and no composition. `docs/DECISIONS.md` D-12
  records that this path is not foreclosed by having tried Path 1, and that a failed cost gate
  is exactly the evidence on which it would be chosen deliberately.

**Recommendation, offered as such and not as a decision.** **(c), with this measurement
reported as a finding rather than as a failure.** It is the first result this project has
produced about the composition itself rather than about its precondition, it is negative in a
specific and interpretable way, and a limits paper that says *"here is the identifiability
condition, here is the diagnostic that checks it, and here is why the obvious exact procedure
for acting on it does not terminate"* is a stronger paper than one that omits the last
clause. **(a) is defensible if the operator wants the composition built anyway**, but it must
be taken with the asymptotic downgrade stated in the abstract, not in a limitations section.

**What this session deliberately did NOT measure, and what it would cost.** The half-widths
measured were 0.05, 0.10, 0.20 and 0.50, and the collapse is already complete at 0.05 — so the
**boundary lies below the smallest box measured and its location is unknown**. Locating it
needs the same script at half-widths of roughly 0.002 to 0.02: about 1.7 million null draws,
**ten minutes on this machine**, no new code beyond a command-line argument. It was not run
because the session brief halts the session on a FAIL, and because a check that could only
soften a verdict, thought of after seeing that verdict, is the pattern `DEVIATIONS.md` D-9 and
D-13 exist to make visible. **It is the first thing to run if the operator takes option (a),
and it is cheap.**

**This question is BLOCKING** for any further work on the composition, and for nothing else.
It does not block the diagnostic-only paper, whose deliverables are substantially discharged
already (`docs/DECISIONS.md` D-12), and it does not touch Q-13 or D-14.

### Q-11 — Should the project occupy the noise-calibrated rank-tolerance seam? *(new, G3; not blocking)*

**Raised 2026-08-20 by `audit/R2_THREAT_CHECK.md` §2.**

The one thing nobody in the retrieved literature does is carry an estimated simulation noise
level forward into the **rank tolerance**. Moré & Wild (2010/2012) estimate the noise level
and use it to pick a near-optimal difference parameter; Cintrón-Arias et al. (2009) assemble
the sensitivity matrix and call its rank at MATLAB's *machine* tolerance. Nobody joins them —
four full-text zeros, control live in the same batch.

**The project does not currently occupy that seam either, and this is the honest part.**
`docs/THRESHOLDS.md` §1.2 derives `τ = 10⁻²` from a **compute budget** (`n ≳ κ²`), not from a
noise level. So there are exactly two options and both have a cost:

- **(a) Occupy it.** Re-derive `τ` from an estimated noise level. Requires a `DEVIATIONS.md`
  entry stating that a pre-registered numeric threshold changed, what result prompted it, and
  why the change is not motivated by that result. **The last condition is the hard one**: the
  numbers now exist, so any re-derivation happens with the singular values already visible.
  That is precisely the leakage failure `LEDGER_DESIGN.md` D3 exists to prevent, and it is
  not obviously escapable by good intentions.
- **(b) Do not occupy it.** State plainly in the paper that the gap was identified and not
  filled, and keep `τ` as pre-registered. Costs the seam; keeps the pre-registration, which
  is currently one of the few things this project has that is demonstrably clean.

**Recommendation, offered as such:** (b). The pre-registration's value is that it is
provable from `git log`; the seam's value is one sentence.

### Q-12 — The observation distortion probes reporting fraction only. Is that enough? **ANSWERED 2026-08-20 (G4) — and the answer is larger than the question**

**Raised 2026-08-20 by the Phase 2 build.**

The OBSERVATION component is declared as *reporting fraction / delay / noise*, but a
distortion family is a **one-parameter** deformation, so one sub-process had to be chosen. The
build chose the **reporting fraction** (`ρ → ρ·exp(η₃)`), a pure amplitude error, deliberately
— it is the cleanest way to ask whether an amplitude error can be told apart from a mechanism
error. The delay kernel and the noise scale are held at base values.

**Why this is a real limitation and not a quibble.** The separability verdict in `results/`
is a statement about *these three columns*. A different observation distortion — perturbing
the reporting **delay** instead, which is a timing distortion — would give a different third
column, and the progression family is *also* a timing distortion. The two could plausibly be
far more collinear than the amplitude/timing pair actually measured. **The favourable verdict
may therefore be partly a consequence of which observation sub-process was chosen**, and that
possibility is not testable without adding the second family.

This is the same class of question as **Q-6** (multi-component scope) and is a scope call, not
a correctness one. Adding a fourth distortion family is **not** governed by THRESHOLDS §1.1,
which closes the list of *summary sets*, not of distortion families — but the same reasoning
applies and any addition should be logged in `DEVIATIONS.md` with whether the existing results
were known at the time.

> #### Answer, session G4 (2026-08-20)
>
> **The question was posed too narrowly.** It asks whether a second *observation* distortion is
> in scope. G4 built an alternative triple in which **all three** families were replaced, each
> designed against a named target component, and ran it through the identical diagnostic:
> `audit/G3_ADVERSARIAL_REVIEW.md` finding 2, numbers in `results/robustness/`.
>
> The observation family G4 used is **strictly harder than the delay perturbation Q-12
> proposes**: a delay *shifts* the reported curve, while a mean-centred log-linear reporting
> trend *tilts* it, and tilt is what the other two columns do. But the finding is not about the
> observation family at all — it is that **the verdict is conditional on the family set as a
> whole**, and that the conditioning is load-bearing rather than decorative.
>
> Q-12 is therefore **closed as answered**, and the live question it opens is **Q-13**, which is
> about what may be claimed rather than about which families are in scope.
>
> The addition is logged in `DEVIATIONS.md` **D-9**, including the part Q-12 asked for and that
> reflects badly on the timing: **the existing results were known when the adversarial set was
> designed.** D-9 states what was done about that and why it is weaker than pre-registration.

## Answered

### Q-9 — The simulator's null is composite. Does the construction survive that? **ANSWERED 2026-08-20**

**Answer: yes, and by published means — which is why it is not a contribution.**
`audit/COMPOSITE_NULL_CHECK.md`.

The composite-null obstruction is real and was correctly identified. It is also the founding
premise of the Monte-Carlo-testing literature, and it has at least three published repairs
that apply to simulators: **Dufour's maximized Monte Carlo** (maximise the simulated p-value
over the nuisance space; *"provably exact level, irrespective of the sample size"*; applies
*"as long as the null distribution … can be simulated once the nuisance parameters have been
specified"*), **repro samples with profiling** (Xie & Wang 2022 — likelihood-free, exact,
finite-sample), and **(approximate) co-sufficient sampling** (Barber & Janson 2022).

Q-9 was raised in G1 as a correctness threat to R1. It is answered as a correctness question
— the construction does not survive a composite null unrepaired, and the repairs are
off-the-shelf. It therefore stops being a research question and becomes a citation.

Original question follows.



**Raised 2026-08-20, and it is independent of the novelty verdict.**

Freidling, Zhao & Gao can rejection-sample because the treatment-assignment distribution is
**known exactly by design**. A simulator's null is exact only **given parameters θ**, and θ
is unknown. "The simulator's own null" is therefore a *family* of distributions, not a
distribution, and the rejection-sampling construction is not automatically valid over a
composite null — the conditional type-I error must hold uniformly over the nuisance
parameter, or the nuisance must be conditioned away on a sufficient statistic.

D-3's formulation does not mention this. It is the actual technical content of any
simulation-based version of the mechanism, and it is unsolved here. Nothing should be
claimed about exact conditional validity in SBI until it is answered.

---


### Q-4 — What counts as "any reasonable summary set", and what rank tolerance? **ANSWERED 2026-08-20**

**Answered in `docs/THRESHOLDS.md` §1** — referenced, not duplicated here.

In summary: the list is **closed at `S_A`, `S_B`, `S_C`**, with a `DEVIATIONS.md` entry
required to add a fourth. Numerical rank is called at `τ = 10⁻²` relative to `σ_1`, and a
summary set is "inseparable" if `rank(J) < 3` or `κ > 100`. The ceiling `κ_max = 100` is
derived from the study's own simulation budget — separation costs `n ≈ κ²` replicates, and
`κ = 1000` would cost more than `S0_REPORT.md` §7 prices the entire protocol at.

**These were fixed before any singular value existed**, in a session that produced no
numbers at all; `git log` is the evidence. A near-zero column norm (`‖J_·k‖ < 0.1`) is
recorded as a **separate** failure — a component invisible to the summaries, not a
confounded one.

### Q-5 — What threshold defines an equivalence class? **ANSWERED 2026-08-20**

**Answered in `docs/THRESHOLDS.md` §2** — referenced, not duplicated here.

Component *k* joins the class named by a near-null right singular vector `v` iff
**`|v_k| ≥ 0.3`**, reported as a range across the h-plateau with border-crossing components
flagged. **Coherence is reported but is deliberately not the decision rule**: the coherence
consistent with `κ_max = 100` is `μ ≈ 0.9998`, too close to 1 to be estimable, so `|μ| ≥ 0.98`
is used only to flag which pair is responsible.

`docs/THRESHOLDS.md` §3 additionally carries the Phase-3.7 argument for why finite-parametric
equivalence classes are meaningful where Kahl et al.'s function-space ones are not — with a
real concession in §3.4: at *exact* rank deficiency Kahl's dichotomy does import, and near-
degeneracy claims must be labelled as statements about **affordability**, not identifiability.

---
### Q-1 — Do we target NeurIPS 2026 at all? **ANSWERED 2026-08-20**

**Answer: yes, and the question's own framing is retired.** `docs/DECISIONS.md` **D-1**.

The operator targets NeurIPS 2026 and has additionally ruled that calendar and deadline
feasibility are **not a planning input for this project** — a standing instruction. Q-1 was
posed as a scheduling trade-off ("given nine days"), and that framing is precisely what
D-1 removes: no session may again argue for a smaller format, a reduced protocol, or a
dropped verification on time-cost grounds.

Option (a) as originally posed — the 2-page Tiny Paper track — was **rejected** on
substantive rather than scheduling grounds. It was viable only as a vehicle for the
identifiability result standing alone, and that result is prior art (Kahl et al. 2019,
*PRX* 9:041046). See `docs/DECISIONS.md` **D-2**.

**Venue selection is resolved:** Sim2Science, **5-page main track**. O-3 is closed;
`audit/VENUE.md` §5 now records a decision rather than a conditional recommendation.

---

