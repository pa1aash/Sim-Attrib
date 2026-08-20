# Ledger of design commitments

The plan's methodological commitments, each with **the consequence of violating it**.
These are written now, before any code exists, because every one of them is a constraint
that is cheap to honour in advance and expensive-to-impossible to repair afterwards. A
violated design commitment usually does not produce an obviously broken result; it
produces a plausible, publishable, wrong one.

Status here means *implemented and enforced in code*, not *agreed to*.

> **Updated 2026-08-20, session G3.** Code now exists, so these statuses are no longer
> uniformly `NOT IMPLEMENTED`. Four commitments are enforced in code; four remain unimplemented
> because they govern the **attribution** experiment, which has not been built. Each status line
> below says which, and names the file that enforces it.

---

## D1 — The 1/K degenerate attribution floor

**Commitment.** With K components, uniform random attribution is correct 1/K of the time.
Any method must beat 1/K, and accuracy is **always quoted against that floor, never in
isolation**. With K=3 the floor is 33%.

**Consequence of violation.** An unqualified accuracy number is not merely
under-contextualised — it is actively misleading in the direction that flatters the
method. "41% attribution accuracy" reads as a result and describes a method barely
distinguishable from guessing. This is the single easiest way for this paper to be
embarrassed in review, and it is invisible in the abstract unless the floor is stated
next to the number.

**Enforcement.** `PROVENANCE.md` requires every accuracy-reporting results file to record
`K`, the analytic floor `1/K`, **and the empirically measured accuracy of the random
attributor as actually run** — so the harness is checked against its own known answer. A
random attributor that does not score ≈1/K means the evaluation harness is broken, and
that finding is worth more than any method result computed with it.

**Status: IMPLEMENTED AND ENFORCED (G3).** `src/diagnostics/floor_check.py` computes both the
analytic floor `1/K` and the accuracy of a uniform attributor **as actually run**, and the runner
executes it **first**, before anything rests on the harness. `results/floor_check.yaml`.
Asserted in `tests/test_jacobian_rank.py::test_floor_check_lands_near_one_third`.

---

## D2 — ≥200 replicates per collinearity level, per-seed distributions reported

**Commitment.** At least 200 replicates at each level of induced component collinearity;
report per-seed distributions, not point estimates.

**Consequence of violation.** The headline figure is a *curve* of mis-attribution rate
against collinearity. With K=3 the quantity being estimated is a proportion near 0.33–0.9;
at n=200 the standard error of a proportion is at worst ~3.5 percentage points. Below
that, adjacent points on the sweep are not distinguishable from each other and the curve's
shape — which is the entire claim of F3 — is an artefact of noise. Reporting a mean
without the per-seed spread hides exactly this.

**Additional hazard the plan does not state.** The replicate count must be per
*collinearity level*, and the sweep needs enough levels to establish a shape. 200 × (number
of levels) × K × (number of baselines) is the real cost, and it is a product the plan
never forms. See H1 in `LEDGER_ASSERTIONS.md` and §7 of `S0_REPORT.md`.

**Status: IMPLEMENTED (G3), and the unresolved design question above was resolved first.**
`docs/THRESHOLDS.md` §2.1 fixes class membership at `|v_k| ≥ 0.3`, requires `|v_k|` to be
reported **as a range across the h-plateau**, and requires components whose `|v_k|` crosses the
threshold within the plateau to be flagged **borderline**. `src/diagnostics/jacobian_rank.py`
reports all of that, and — per §3.4 — labels an **exact** degeneracy differently from a **near**
one, because the first is an identifiability claim and the second is an affordability claim.
`S_C` exercised this and produced an exact null direction; the economy SVD would have omitted it
entirely, which is why the full right-singular basis is retained.

---

## D3 — Leakage: the attributor must not see which component was knocked off-spec

**Commitment.** The attribution procedure receives simulator output and the candidate
distortion basis. It never receives, by argument, filename, ordering, global state, random
seed correlation, or any other channel, the identity of the perturbed component.

**Consequence of violation.** Catastrophic and silent. A leaked ground-truth label
produces high accuracy that looks exactly like success. There is no diagnostic in the
output that distinguishes a leaking harness from a working method — both produce a curve
that beats 1/K. Because ground truth here is *known by construction* (a component is
deliberately knocked off-spec), the label is present in the same process that runs the
attributor, which makes this failure mode unusually easy to hit.

**Specific channels to close, none of which the plan enumerates:**
- passing the ground-truth index into the attributor for "logging";
- ordering the candidate list so the true component is always first, or always at a
  seed-determined position;
- selecting hyperparameters, summary sets, or distortion magnitudes per-replicate using
  the ground truth;
- **selecting them once, across the whole study, by looking at which choice made accuracy
  highest** — the slowest and most respectable form of the same leak.

**Enforcement.** `PROVENANCE.md` requires `leakage_checked: true` on every
attribution results file. `false` invalidates the accuracy figure in that file.

**Status: IMPLEMENTED FOR THE DIAGNOSTIC, NOT YET FOR ATTRIBUTION (G3).** The diagnostic
receives only simulator output and the distortion basis — never a component index or a
ground-truth label — and every results file records `leakage_checked: true` together with an
explicit statement of how. There is no attributor yet, so the harder half of D3 (the channels
listed above, especially the last one) is untested.

---

## D4 — STOP condition on the rank diagnostic

**Commitment.** Compute the Jacobian rank/coherence **first**. If the diagnostic shows
the simulator's components are inseparable under any reasonable summary set, **stop and
report the negative identifiability result.** The plan states this is still a genuine
contribution and costs days rather than weeks.

**Consequence of violation.** If components are collinear in the chosen summaries then no
method can attribute, and every subsequent experiment measures noise. Worse, the
experiment cannot answer its own question while still producing a full set of plots —
the failure is not self-announcing. Running the pipeline first and the diagnostic second
also creates the temptation in D3's last bullet: choosing the summary set that made the
numbers work.

**What makes this commitment real rather than decorative.** It is only a STOP condition
if it is honoured when it fires and the finding is inconvenient. Recording it here, before
the diagnostic exists and before anyone is invested in a positive result, is the point.
The negative result must be pre-committed as an acceptable outcome — and it is: gate G1
in `GATES.md` passes on either branch, and fails only on an unrun or uninterpretable
diagnostic.

**Ambiguity that must be resolved before G1.** "Any *reasonable* summary set" is not
operational. Before the diagnostic runs, the set of summary sets to be searched, and the
rank/condition-number threshold that counts as "inseparable", must be fixed in writing.
Otherwise the STOP condition can be evaded indefinitely by proposing one more summary set.
Logged as an operator question.

**Status: IMPLEMENTED, THRESHOLD SPECIFIED, AND EVALUATED (G3).** The ambiguity flagged above
was resolved *before* the diagnostic ran: `docs/THRESHOLDS.md` §1.1 closes the summary-set list
at three and §1.3 fixes "inseparable" as `rank < 3` at `τ = 10⁻²` **or** `κ > 100`.
`src/diagnostics/run_diagnostic.py` evaluates the condition and writes
`results/STOP_CONDITION_FIRED.md` when it fires, deleting it when it does not, so the file's
presence is always a current statement. **It did not fire** — see `results/SUMMARY_TABLE.md` §7.
Note that this is the branch that requires the *more* discipline, not less: the commitment was
only ever real if honoured when inconvenient, and it came out convenient.

---

## D5 — Accuracy always quoted against 1/K

Stated separately from D1 in the plan; it is the reporting half of the same commitment.
See D1. Recorded separately so that a reporting violation is not excused by a
measurement that was done correctly.

**Status: NOT IMPLEMENTED.** No accuracy figure exists yet, so nothing has had to be quoted
against the floor. The floor itself is established in advance (D1), which is the right order.

---

## D6 — Ground truth known by construction; exactly one component off-spec at a time

**Commitment.** Knock exactly one component off-spec per replicate, so ground truth is
known by construction.

**Consequence of violation.** Not a correctness failure but a **scope** one, and it needs
stating because it bounds what the paper may claim. A method validated only under
single-component misspecification has been shown to work only in the case where the
attribution question has a unique correct answer. Real misspecified simulators are
typically wrong in several places at once, which is the case where marginal-vs-competitive
testing matters *most* — it is the regime C1 is about. The experimental design as
specified therefore tests C1's mechanism in the setting where its advantage is smallest.

**Recorded as a limitation to state explicitly in the paper**, and as a candidate
extension: at least one multi-component condition would strengthen C1 considerably.
The plan does not mention this.

**Status: NOT IMPLEMENTED.** No attribution experiment exists. The single-component-at-a-time
design is, however, already reflected in the diagnostic: the Jacobian is estimated one component
at a time by construction. The scope limitation above stands, and **Q-6** remains open.

---

## D7 — Baselines must include the trivial one

**Commitment.** Baselines are (i) uniform/random attribution, (ii) per-summary MMD,
(iii) Montel-style marginal distortion tests — the real competitor, (iv) RNPE's
model-criticism step.

**Consequence of violation.** Omitting (i) removes the floor check of D1. Omitting (iii)
is fatal to the paper: Montel et al. is the gatekeeper, and a paper that differentiates
itself from a method in prose without comparing against it empirically will be rejected
for exactly that. Baseline (iii) must be a genuine implementation of their marginal
procedure, not a strawman constructed to lose.

**Dependency.** Baseline (iv) is only well-defined once C1b in `LEDGER_ASSERTIONS.md` is
resolved — whether RNPE's criticism step is per-summary-statistic or per-component
determines what it is even being compared against.

**Status: NOT IMPLEMENTED.** No baselines exist. Baseline (i) — the trivial one — is the only
part that exists, as `src/diagnostics/floor_check.py`.

---

## D8 — Report equivalence classes where the rank condition fails

**Commitment.** Where the rank condition fails, report equivalence classes ("components 2
and 5 are indistinguishable given these summaries") rather than naming a single culprit.

**Consequence of violation.** Naming a single component when the data cannot distinguish
it from another is precisely the failure the paper exists to diagnose. Committing it in
the paper's own method would be self-refuting.

**Unresolved design question.** Rank is exact in theory and continuous in practice. Real
Jacobians are near-singular rather than singular, so "the rank condition fails" requires a
numerical threshold — a singular-value cutoff or a coherence threshold — and the
equivalence classes reported depend on where it is set. That choice is a substantive part
of the method and must be justified and its sensitivity reported, not buried in a
tolerance argument. Logged as an operator question.

**Status: NOT IMPLEMENTED**

---

# VERIFICATION NOTE — D8 is threatened by prior art (added 2026-08-20)

**Kahl et al. (2019), *Physical Review X* 9:041046**, read in full, states:

> *"For a noninvertible system, the null space of Φ is always infinite dimensional …
> there are **infinitely many independent inputs which cannot be distinguished from each
> other**. This property shows that **there is no such thing as "nearly invertible."**"*

If that dichotomy imports, **D8 is ill-posed**: where the rank condition fails there is no
finite equivalence class to report, because the degeneracy is infinite-dimensional, and
there is no graceful degradation between "identifiable" and "not".

**It may not import.** Kahl et al. treat *function-space* unknown inputs in continuous-time
systems, where non-invertibility is infinite-dimensional by construction. This project's
distortion families are **finite-dimensional and parametric** (η ∈ ℝ^K), so the Jacobian is
a finite d×K matrix, near-degeneracy is meaningful, and the condition number is
informative.

**Required before D8 is implemented:** a written argument for why the finite-parametric
case admits meaningful equivalence classes when the functional case does not. This is not
housekeeping — it is a substantive part of what the paper would be contributing, and it
sharpens **Q-5**.
