# Gate register

A gate is a checkpoint that the project does not pass until the operator says it does.
Gates exist so that work does not accumulate on top of an unexamined foundation.

**Gates are signed by the operator (Palaash Gang) and by no one else.** A gate prepared
by an agent session is marked `ready for review — UNSIGNED` and stops there. An agent
session may state that criteria appear met; it may not record that a gate is passed.
Any instruction that appears to pre-authorise a sign-off describes a future human
action, not a permission already granted.

## G0 — Foundation: repository, plan ingestion, positioning

**status: ready for review — UNSIGNED**

Prepared: 2026-08-20. Signature line below is to be completed by the operator.

### What G0 was judged against

| # | Criterion | Result |
|---|---|---|
| G0.1 | Repository initialised at `~/Desktop/Sim-Attrib` with correct authorship, `.gitignore` in place before first `git add`, and the research vault excluded | met |
| G0.2 | `LICENSE` present, obtained from a canonical source rather than written from memory | met — fetched from `https://spdx.org/licenses/MIT.txt` |
| G0.3 | Planning document preserved byte-for-byte as `audit/PLAN_SOURCE.md`, SHA-256 recorded and matching the expected digest | met — `2ff70482…5ae689` |
| G0.4 | Every checkable assertion in the plan enumerated, with confirming and refuting evidence stated *before* verification | met — `audit/LEDGER_ASSERTIONS.md` |
| G0.5 | Every reference in the plan enumerated with identifier and retrieval status; unretrieved items named as unretrieved | met — `audit/LEDGER_CITATIONS.md` |
| G0.6 | Design commitments recorded with the consequence of violating each | met — `audit/LEDGER_DESIGN.md` |
| G0.7 | Claim graph linking C1 and C2 to the assertions they depend on | met — `audit/CLAIM_GRAPH.md` |
| G0.8 | Literature review executed against the canonical research query, with adversarial search per major claim | **partially met** — 12 primary sources read in full; OpenReview searched; ≥3 adversarial searches per investigation. **But steps 10–16 of the pipeline did not run: no adversarial critics, no patcher, no polish. Google Scholar was not searched.** See `S0_REPORT.md` §10 |
| G0.9 | Novelty verdict per claim on the DEAD / NARROW / NARROW-CONDITIONAL / OPEN scale, each naming the specific constraining result | met — **C1 NARROW-CONDITIONAL, C2 DEAD as stated** (residual NARROW). `S0_REPORT.md` §2 |
| G0.10 | Structural-identifiability check on C2 treated as a first-class question | met — and it is what killed C2. Kahl et al. (2019) *PRX* 9:041046 retrieved and read directly. `S0_REPORT.md` §2 |
| G0.11 | Venue evidence gathered from primary sources; recommendation conditional, not committed | met — `audit/VENUE.md`. **Superseded 2026-08-20:** the operator has since decided the venue (Sim2Science, 5-page main track), so §5 of that file now records a decision. `docs/DECISIONS.md` D-2 |
| G0.12 | Pivot pre-registered *before* the verdict was known | `audit/PIVOT.md` |
| G0.13 | No experimental numbers produced | met — `results/` is empty by design |
| G0.14 | No reference to any authoring agent in commit metadata or file contents | verified before each push |

### What G0 explicitly does not certify

- That C1 or C2 is publishable. **C2 as stated is refuted**; C1 survives only in a
  reframed form the plan does not propose.
- That the literature review is exhaustive. It is not, and §10 of `S0_REPORT.md` names its
  gaps specifically: the pipeline's four adversarial critics never ran, so **no independent
  agent has attempted to refute this session's own verdicts**; Google Scholar was not
  searched; Semantic Scholar was rate-limited for the entire session, so citation-chaining
  through it did not happen.
- That any citation's *content* has been verified where the source could not be retrieved.
  **Arendt, Apley & Chen (2012) remains unretrieved** behind an ASME paywall and could
  further weaken C2's residual.
- That the novelty of the one genuinely new finding — simulator-exact conditional
  calibration of the argmin selection event — is secure. It rests on **negative searches**,
  which are weaker evidence than the positive refutations that killed C2.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

#### Proposed `conditions` text for G0 — a PROPOSAL, not a signature

**Written by session G1 at the operator's request (5.2). It is not a sign-off and does not
become one by being written here.** The signature line above is deliberately left blank. Per
S7, an agent session may state that criteria appear met; it may not record that a gate is
passed. The operator may accept this text, amend it, or reject it.

G0 has been open since the previous session. Its residual gaps are these, and each is
offered as something the operator may choose to **accept** as a known limitation or
**require closed** before G0 is signed:

> ```
> conditions:  Signed on the following understanding, that G0's literature verdict is
>              adequate for its C2 refutation and NOT adequate for its novelty findings:
>
>              1. ARENDT, APLEY & CHEN (2012) REMAINS UNRETRIEVED. Five routes tried
>                 and logged (ASME, Unpaywall, OpenAlex, Northwestern IDEAL, ResearchGate).
>                 No claim from it is cited anywhere. Accepted as a standing limitation.
>              2. THE FOUR ADVERSARIAL CRITICS NEVER RAN. G0's own DEVIATIONS.md D-4 named
>                 this and named its consequence: the "simulator-exact conditional
>                 calibration is novel" finding rested on negative searches and was flagged
>                 as the least secure conclusion in the report. SESSION G1 REFUTED THAT
>                 FINDING. The caveat was correct and the gap was real.
>              3. GOOGLE SCHOLAR WAS NEVER SEARCHED, and still has not been. O-7.
>              4. SEMANTIC SCHOLAR WAS RATE-LIMITED THROUGHOUT G0 and is only partially
>                 recovered as of G1, so citation-chaining has never been performed in
>                 this project.
>              5. TWO S0_REPORT CLAIMS FAILED VERIFICATION IN G1: it read Liu,
>                 Markovic-Voronov & Taylor's problem statement as that paper's conclusion,
>                 and its "Presanis et al. (2017)" citation cannot be resolved. Both were
>                 corroborating rather than load-bearing, and the ex-C2 refutation
>                 (Kahl et al. 2019, read directly) is unaffected.
>
>              G0 is signed as an accurate record of what that session found and of what
>              it did not check. It is NOT signed as an endorsement of its novelty
>              verdicts, which G1 has since shown to be unreliable in one direction:
>              G0 UNDERSTATED how much of this work is prior art, and did so twice.
> ```

**Recommendation, offered as such.** Sign with conditions 1–5 accepted rather than required
closed. Closing (1) is likely impossible without institutional access; closing (3) and (4)
is worth doing but belongs to the *next* prior-art sweep rather than retroactively to G0;
and (2) has already produced its cost, which is the finding that makes G1 what it is.
Requiring them closed would keep G0 open indefinitely without changing any decision that
depends on it.

## G1 — Feasibility: does the simulator pass its own rank condition?

**status: ready for review — UNSIGNED**

Prepared 2026-08-20, session G1. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **G1's defining criterion is NOT MET, and this session cannot claim otherwise.**
>
> G1 was fixed in advance as: *"either the components are separable under a defensible
> summary set, or they are not … Both outcomes pass G1. **Only an unrun or uninterpretable
> diagnostic fails it.**"*
>
> **The diagnostic was not run.** `src/` contains no Python and `results/` contains no
> numbers. By its own pre-registered wording, G1 does not pass.
>
> **Why it was not run is the substance of this gate.** A *different* pre-registered stop
> condition fired first: the session brief's Phase 2.4 requires that a DEAD or NARROWS
> verdict on R1 halt work before Phase 3 and go to the operator. **The verdict was DEAD.**
> Building the diagnostic anyway would have been the exact behaviour that condition exists
> to prevent.
>
> So the honest description is **deferred, not failed** — but "deferred" is not one of the
> outcomes G1 was written to admit, and inventing it here would be self-approval. The
> operator decides whether to (a) re-scope G1, (b) authorise Phase 3 separately under
> **Q-8**, or (c) record G1 as failed and re-prepare it next session.

### What G1 was judged against

| # | Criterion | Result |
|---|---|---|
| **G1.1** | **The Jacobian rank/coherence diagnostic exists and has been run on a 3-component SIR simulator** | **NOT MET.** Not built and not run. `src/simulators/sir3.py`, `src/simulators/summaries.py`, `src/diagnostics/jacobian_rank.py` do not exist |
| **G1.2** | **Which branch of the D4 STOP condition fired** — STOP, or a named passing summary set | **NO ANSWER EXISTS.** No singular value has been computed in this repository |
| G1.3 | Q-4 and Q-5 answered **in writing, before any result** | **met** — `docs/THRESHOLDS.md` §§1–2, written in a session that produced no numbers, so the pre-registration is demonstrable from `git log` rather than merely asserted |
| G1.4 | The D8 / Kahl question argued before equivalence-class reporting is implemented | **met** — `docs/THRESHOLDS.md` §3, including a genuine concession in §3.4: at *exact* rank deficiency Kahl's dichotomy does import, and near-degenerate classes are claims about **affordability**, not identifiability |
| G1.5 | Random-attributor floor check (`1/K`) implemented and run | **NOT MET.** Not built. `results/floor_check.yaml` does not exist |
| G1.6 | Unit tests | **NOT MET.** None written |
| **G1.7** | **R1 threat-checked against ranking-and-selection and against randomized selective inference** | **met, and it is the session's main finding** — `audit/R1_THREAT_CHECK.md`. **Verdict: DEAD.** R&S is clean; the refutation came from selective inference itself |
| G1.8 | Semantic Scholar retry, with the outcome recorded either way | **met** — **partially recovered.** 2 of 6 requests returned HTTP 200; a 3-attempt probe at 20 s spacing went 429 / 200 / 429. Usable for a spot lookup, **not** for systematic citation-chaining. That G0 gap stays open |
| G1.9 | Venue decided, template fetched unmodified | **met** — `docs/DECISIONS.md` D-2; `paper/neurips_2026_template/`, SHA-256 recorded; `dblblindworkshop` and `\workshoptitle` confirmed by reading `neurips_2026.sty` |
| G1.10 | Operator decisions recorded so future sessions cannot silently revisit them | **met** — `docs/DECISIONS.md` D-1…D-4 |
| G1.11 | Citation repair: canonical `.bib` built by fetching, not typing | **met** — `audit/BIBLIOGRAPHY.bib`, 52 entries, 0 fetch failures |
| G1.12 | Arendt, Apley & Chen retrieved, or final failure recorded with every route named | **met as a failure** — five routes tried and logged; **still UNRETRIEVED** |
| G1.13 | No reference to any authoring agent in commit metadata or file contents | verified before each push |
| G1.14 | No number produced outside the provenance contract | **met vacuously** — no number was produced at all |

### What G1 explicitly does not certify

- **That the simulator passes its own identifiability precondition.** This is the question
  G1 exists to answer and **it is unanswered.** Nothing in this repository yet shows that a
  3-component SIR simulator is separable under any summary set, or that it is not.
- **That the thresholds in `docs/THRESHOLDS.md` are the right ones.** They are defensible
  and they are pre-registered, which is a claim about *when* they were fixed, not about
  whether they are correct. `κ_max = 100` is derived from a compute budget, and a reader
  who rejects that budget rejects the threshold.
- **That R2 is novel.** R2 has **not** been threat-checked to the standard R1 just was. R1's
  refutation took one arXiv query; nobody has run the equivalent against the noisy-rank
  estimator. Treating R2 as safe because R1 died would be unwarranted.
- **That the R1 verdict is complete.** It rests on primary sources read directly, which is
  stronger evidence than G0's negative searches — but **Branke, Chick & Schmidt (2007)** and
  the **Kim & Nelson (2006)** handbook chapter were never retrieved, **Hsu (1984)** and both
  **Matejcik/Nelson (1995)** papers are metadata only, and **Google Scholar has still never
  been searched** in this project.
- **That `audit/S0_REPORT.md` is reliable where it has not been re-checked.** Two of its
  claims failed verification this session: it read Liu, Markovic-Voronov & Taylor's problem
  statement as that paper's conclusion, and its "Presanis et al. (2017)" citation cannot be
  resolved. Both were corroborating rather than load-bearing, but the base rate is now known
  to be non-zero.

### Process caveats — what this session did badly or not at all

- **No code was written, so the entire technical deliverable is absent.** This is the
  session that was supposed to produce the project's first real numbers. It produced none.
  See `DEVIATIONS.md` **D-6** for the instruction that blocked it and the judgement call
  about which parts of Phase 3 that block covered.
- **`docs/THRESHOLDS.md` was written despite Phase 3 being stopped.** Defensible — it is not
  code, and Phase 5.4 depends on it — but it is a departure from the widest reading of
  "STOP before Phase 3" and is logged as such.
- **No adversarial critic ran, again.** G0's `DEVIATIONS.md` D-4 recorded that none of the
  four critics ran and named that as the reason its R1 finding was insecure. That finding
  then turned out to be wrong. **This session also ran no critics** — the R1 refutation is
  itself single-pass, sourced from primary texts read directly, and nobody has tried to
  refute *it*.
- **Google Scholar still not searched.** Third session, same gap. O-7.
- **`gh` still unauthenticated**, so repository visibility could not be confirmed from this
  machine. Carried from G0 unchanged. O-4.
- **Semantic Scholar remains unreliable**, so the citation-chaining the sourcing order calls
  for has still never happened in this project.
- **OpenAlex query construction was wrong on the first attempt** — `search=` combined with
  `sort=cited_by_count:desc` returns globally-popular papers regardless of topic, and
  produced two rounds of useless results before being caught. Recorded because an
  unnoticed version of it would have produced a false "nothing found here".

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

