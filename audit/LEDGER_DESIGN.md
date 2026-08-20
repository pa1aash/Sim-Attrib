# Ledger of design commitments

The plan's methodological commitments, each with **the consequence of violating it**.
These are written now, before any code exists, because every one of them is a constraint
that is cheap to honour in advance and expensive-to-impossible to repair afterwards. A
violated design commitment usually does not produce an obviously broken result; it
produces a plausible, publishable, wrong one.

Status here means *implemented and enforced in code*, not *agreed to*. Everything is
`NOT IMPLEMENTED` — there is no code.

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

**Status: NOT IMPLEMENTED**

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

**Status: NOT IMPLEMENTED**

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

**Status: NOT IMPLEMENTED**

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

**Status: NOT IMPLEMENTED — and its threshold is not yet specified**

---

## D5 — Accuracy always quoted against 1/K

Stated separately from D1 in the plan; it is the reporting half of the same commitment.
See D1. Recorded separately so that a reporting violation is not excused by a
measurement that was done correctly.

**Status: NOT IMPLEMENTED**

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

**Status: NOT IMPLEMENTED**

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

**Status: NOT IMPLEMENTED**

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
