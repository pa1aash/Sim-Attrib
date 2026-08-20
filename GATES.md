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

> #### Session G3 note on this proposal (2026-08-20) — it still stands, and one item is now sharper
>
> **The G1-drafted text above is not amended.** Two things have changed that a signer should
> know, and both strengthen rather than weaken it:
>
> - **Item 2 has been vindicated twice more.** G1's proposal said G0's missing critics were the
>   reason its novelty finding was insecure, and that the finding was then refuted. Two further
>   headline claims have died since. **No critic has run in any of the four sessions.**
> - **Items 3 and 4 are now four sessions old, not two.** Google Scholar has still never been
>   searched; Semantic Scholar rate-limited again in G3, so citation-chaining has still never
>   been performed in this project.
>
> **One item should be ADDED if the operator is amending rather than accepting**, because it was
> not known when the G1 text was written:
>
> > ```
> >              6. G0'S NEGATIVE SEARCHES WERE RUN ON THE WRONG INSTRUMENT. audit/TOOLING.md
> >                 establishes that the arXiv API's all: field searches METADATA, NOT FULL
> >                 TEXT. Every zero G0 reported as evidence of absence was a metadata zero.
> >                 Under S4 these are INSTRUMENT GAPS, not measured zeros. One has since been
> >                 re-checked on the working index and survived; the rest are unverified
> >                 (O-13). G0's POSITIVE findings -- the Kahl refutation above all -- are
> >                 unaffected, because a paper that does the thing does not depend on how it
> >                 was found.
> > ```
>
> **Recommendation unchanged:** sign with the conditions accepted rather than required closed.

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

#### Proposed `conditions` text for G1 — a PROPOSAL, not a signature

**Written by session G3 at the operator's request (brief §4.2). It is not a sign-off and does
not become one by being written here.** The signature line below is deliberately blank (S9).

G1 offered the operator three ways to close itself: **(a)** re-scope the gate, **(b)** authorise
Phase 3 separately, **(c)** record G1 as failed and re-prepare it next session. **The operator
took (b)**, via the Q-10 decision, and **session G3 then discharged the deliverable**. So the
useful thing to record is that G1's unmet criteria are *closed elsewhere*, not that they are
still open — which means G1 does **not** need re-preparing and option (c) is moot.

> ```
> conditions:  Signed as an accurate record of a session whose DEFINING CRITERION WAS NOT MET,
>              and whose unmet criteria have since been discharged by G3. Specifically:
>
>              1. G1.1 AND G1.2 WERE NOT MET AND THAT IS NOT REVISED HERE. The diagnostic was
>                 not built and no branch of the D4 STOP condition had an answer. Signing this
>                 gate does not convert those to met.
>              2. THEY ARE NOW DISCHARGED BY G3, not by G1. The diagnostic exists, was run, and
>                 the STOP condition did not fire. G1 therefore does not need re-preparing, and
>                 option (c) of its own three options is withdrawn as moot.
>              3. THE STOP THAT BLOCKED G1 WAS CORRECT. Phase 2.4 required halting on a DEAD
>                 verdict on R1, and the verdict was DEAD. Building a mechanism that had just
>                 lost its novelty is exactly what that condition exists to prevent. The gate
>                 failed; the session did not misbehave.
>              4. docs/THRESHOLDS.md WAS WRITTEN DESPITE THE STOP, and is logged as a deviation
>                 (D-6). That judgement call has since paid off in a way it could not have been
>                 predicted to: the pre-registered argument against a machine-epsilon rank
>                 tolerance turns out to be an argument against the standard practice in the
>                 literature G3 later found (Cintron-Arias et al. 2009 call rank at MATLAB's
>                 machine tolerance). Its value depends on having been written BEFORE any
>                 singular value existed, which git log establishes.
>              5. G1'S NEGATIVE SEARCHES ARE UNVERIFIED for the same reason as G0's (O-13).
>                 Its POSITIVE finding -- the R1 refutation, from primary texts read directly --
>                 is unaffected.
>              6. BRANKE, CHICK & SCHMIDT (2007) AND KIM & NELSON (2006) REMAIN UNRETRIEVED,
>                 with a recorded substitution for the latter. Accepted as a standing limitation.
> ```

**Recommendation, offered as such.** Sign with conditions 1–6 accepted. Requiring them closed
would keep G1 open over a deliverable that has already been produced under a different gate.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```


## G2 — Does the composite-null gap survive a threat check?

**status: NOT MET — UNSIGNED**

Prepared 2026-08-20, session G2. Signature block below is for the operator.

> ### Outcome, stated before the table
>
> **Outcome (a) of the three the brief named: a third consecutive kill, stopped at Phase 1.**
>
> The session's target claim — that a simulator's composite null breaks the rejection-sampling
> construction, and that characterising and repairing that gap is the contribution — is
> **prior art in both halves**. The observation is the founding premise of Monte Carlo
> testing; the repair is **Dufour (2006)**, *maximized Monte Carlo*, which delivers *"provably
> exact level"* under exactly the condition a simulator satisfies. Two further independent
> repairs exist (repro samples with profiling; approximate co-sufficient sampling), one of
> which ships as a CRAN package.
>
> Per the brief's §1.5, a DEAD verdict stops the session before Phases 2–4. **It did.**

### What G2 was judged against

| # | Criterion | Result |
|---|---|---|
| **G2.1** | **Composite-null gap threat-checked to the standard R1 was** | **met** — `audit/COMPOSITE_NULL_CHECK.md`. **Verdict: DEAD**, on three independent (a)-class sources |
| G2.2 | Freidling et al. re-read in full for what it says about nuisance parameters | **met** — `nuisance` **0**, `composite` **0** (control `the`=1448), but *not* silent: it states an explicit `sharp null` requirement (14×) and an explicit scope limitation. The brief's warning against conflating silence with an explicit assumption was applicable and is honoured in §2 of the check |
| G2.3 | ≥3 adversarial reformulations, academic sources first, no headed browser (S4) | **met** — 13 full-text queries logged with per-query hit counts; no browser launched |
| G2.4 | Verdict on the DEAD/NARROW/NARROW-CONDITIONAL/OPEN scale | **met** — DEAD, with the one unoccupied cell stated at its true size in §5 |
| **G2.5** | **R2 threat-checked (Phase 2)** | **NOT DONE.** Phase 1 hit DEAD and the brief stops the session before Phase 2. **R2 remains entirely untested — the same state G1 left it in** |
| **G2.6** | **The diagnostic built and run (Phase 4)** | **NOT DONE.** Blocked behind Phase 1. `src/` still contains no Python; `results/` still contains no numbers. **Third session in which the technical deliverable did not happen** |
| G2.7 | D-5 written, claim graph rewritten, working title restated (Phase 3) | **NOT DONE** — Phase 3 is reached only if Phase 1 did not stop the session |
| G2.8 | Q-8/Q-9 resolved or restated; Q-10 raised | **met** — Q-9 **answered** (the repair is Dufour's, so it is a citation not a question); Q-8 **narrowed**, its option (a) foreclosed; **Q-10 raised as blocking** |
| G2.9 | No number produced outside the provenance contract | **met vacuously** — no number was produced |
| G2.10 | No reference to any authoring agent in commit metadata or file contents | verified before each push |
| **G2.11** | *(not in the brief; raised by this session)* **Search instrument validated** | **met, and it is the session's most consequential finding** — the arXiv `all:` API field searches **metadata, not full text**. G0 and G1 both described their searches as full-text. Demonstrated with two phrases present in paper bodies that return 0. The real index (`arxiv.org/search_classic`, `searchtype=ft`) was found, verified, and used. `audit/TOOLING.md` |

### What G2 explicitly does not certify

- **That the project has a viable contribution.** It does not identify one. Three headline
  claims have now been refuted and no replacement is proposed — deliberately, since proposing
  a fourth framing without operator input is the behaviour that produced the first three.
- **That R2 is novel, or that it is not.** **R2 has never been tested.** After three kills,
  its untested status must not be read as survival.
- **That the area is exhausted.** The opposite may be true: the project has never had a
  competent prior-art sweep, because the instrument was wrong until this session. Both
  readings are put to the operator in **Q-10**.
- **That G0's and G1's negative findings hold.** They were metadata zeros reported as
  literature absences. Only one has been re-checked on the working index (it survived). The
  rest are **unverified**, and under S4 they are instrument gaps, not measured zeros.
- **That the simulator passes its own identifiability precondition.** Unanswered since G1,
  and unanswerable until the diagnostic is built.

### Process caveats

- **No code, third session running.** `src/` and `results/` are exactly as G0 left them. Each
  stop was instruction-following rather than drift — G1 stopped on Phase 2.4, G2 on Phase 1.5
  — but the cumulative effect is a project with a large audit trail and no software.
- **Phase 2 was skipped, so the most useful remaining check did not run.** If the operator
  takes Q-10 option (a) or (b), the R2 threat check is the first thing to do, and it is now
  overdue by two sessions.
- **`audit/CLAIM_GRAPH.md` was not rewritten** (Phase 3.3 not reached). A dated status
  pointer was added to it so a future session is not misled by a stale dependency graph; the
  full rewrite is deferred. Logged in `DEVIATIONS.md` **D-7**.
- **Dufour's version of record was not obtained.** *J. Econometrics* is paywalled; Unpaywall
  and OpenAlex both report closed. The **CIRANO working-paper version** was retrieved and read,
  and every MMC quotation is attributed to it, not to the VoR.
- **No adversarial critic ran, for the third consecutive session.** This report's verdict is
  single-pass. It rests on positive evidence — named theorems in retrieved papers — which is
  the strongest kind available here, but nobody has tried to refute it.
- **Semantic Scholar was not queried this session.** Not needed; not a gap this time, but
  citation-chaining still has never been performed in this project.

#### Proposed `conditions` text for G2 — a PROPOSAL, not a signature

**Written by session G3 at the operator's request (brief §4.2). Not a sign-off (S9).**

G2 is recorded `NOT MET` because it stopped at Phase 1. That is accurate and should not be
softened. It is also, on the evidence of the session that followed it, **the most consequential
session in the project so far**, and a `conditions` text that does not say so would misdescribe
the record.

> ```
> conditions:  Signed as NOT MET, correctly stopped, and -- on the evidence of G3 -- the
>              session that fixed the project's actual problem. Specifically:
>
>              1. G2.5 AND G2.6 WERE NOT DONE. The R2 check did not run and the diagnostic was
>                 not built. Signing does not convert those to met. Both are now discharged by
>                 G3.
>              2. THE STOP WAS CORRECT AND WAS THE BRIEF'S OWN. A DEAD verdict on the
>                 composite-null gap stopped the session before Phases 2-4, exactly as
>                 pre-registered.
>              3. G2.11 -- THE SEARCH-INSTRUMENT CORRECTION -- IS THE MOST VALUABLE THING THIS
>                 PROJECT HAS PRODUCED, and it was not in the brief. G0 and G1 both reported
>                 "arXiv full-text" searches that were metadata-only. Demonstrated with two
>                 phrases present in paper bodies that return 0. Every subsequent finding,
>                 including G3's entire R2 check, depends on that correction.
>              4. THE CORRECTION IS RETROSPECTIVE AND THE DEBT IS NOT PAID. G0's and G1's
>                 negative findings are downgraded to instrument gaps. One has been re-checked
>                 and survived; the rest are unverified (O-13). Accepted as a standing
>                 limitation, non-blocking, because no live claim rests on them.
>              5. THE INSTRUMENT-GAP CLASS OF DEFECT RECURRED IN G3, within one session of
>                 audit/TOOLING.md being written -- twice (arXiv's "No Results." string, and
>                 ff/fi ligatures in extracted PDF text defeating a plain grep). Both were
>                 caught by checking rather than by the rule. The rule needs the ligature case
>                 added alongside S7.
>              6. DUFOUR'S VERSION OF RECORD WAS NOT OBTAINED (O-14). Every MMC quotation in
>                 this project, including G3's specification, is attributed to CIRANO WP
>                 2005s-02. O-14 must be closed before MMC is cited in any manuscript.
>              7. NO ADVERSARIAL CRITIC RAN. G2's verdict is single-pass, like every other
>                 verdict in this project.
> ```

**Recommendation, offered as such.** Sign with conditions 1–7 accepted. Item 3 in particular
should be recorded as a finding rather than buried: the project's three-for-three record was at
least partly an instrument failure, and G2 is the session that established that.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G3 — First code. Does the simulator pass its own rank condition?

**status: ready for review — UNSIGNED**

Prepared 2026-08-20, session G3. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **This is the first session to produce code and numbers.** `src/` contains a simulator, three
> summary sets, a diagnostic, a floor check and a runner; `results/` contains five files;
> `tests/` contains 65 tests. Three prior sessions produced an audit trail and no software.
>
> **Phase 1's R2 verdict is NARROW-CONDITIONAL** — the first of four prior-art checks in this
> project not to return DEAD. That is not as good as it sounds, and §"does not certify" below
> says why: R2 survived because it was never the headline, and what survives of it is a
> one-sentence observation about a rank tolerance.
>
> **The D4 STOP condition did NOT fire.** Two of the three summary sets are separable under the
> criteria pre-registered in `docs/THRESHOLDS.md`, and the impoverished control `S_C` failed
> exactly as designed, with an *exact* null direction. Per G1's own wording, **both branches of
> that condition pass the gate; only an unrun or uninterpretable diagnostic fails it.** The
> diagnostic was run and is interpretable.
>
> **Phase 3 is specification only, by instruction.** No MMC code exists.

### What G3 was judged against

| # | Criterion | Result |
|---|---|---|
| G3.1 | Corrected full-text instrument (S4) validated with a known-present phrase **before** anything load-bearing | **met** — control returned exactly arXiv:2405.07026; re-run inside the final batch so the reported zeros are attested against a live instrument |
| G3.2 | R2 threat-checked against the three literatures G2 named, ≥3 queries, each reformulated at least once | **met** — 20 full-text queries logged with per-query counts; three primary sources retrieved and read in full. `audit/R2_THREAT_CHECK.md` |
| G3.3 | Verdict on the DEAD / NARROW / NARROW-CONDITIONAL / OPEN scale, strongest case against novelty first | **met** — **NARROW-CONDITIONAL** |
| G3.4 | R2's framing consequence recorded as a decision | **met** — `docs/DECISIONS.md` **D-6**: cited infrastructure, not a claimed method contribution |
| **G3.5** | **The simulator exists, with components declared in code and docstring, and `δ_k(·;0)` exactly the base** | **met** — `src/simulators/sir3.py`; identity tested **bit-identical**, and smoothness tested by one-sided derivatives and a bounded second difference |
| G3.6 | Three summary sets, including the impoverished positive control | **met** — `src/simulators/summaries.py`, list closed at `S_A`/`S_B`/`S_C` |
| **G3.7** | **The diagnostic exists and has been RUN on a 3-component SIR simulator** — G1.1, unmet for three sessions | **met** — `src/diagnostics/jacobian_rank.py`, `results/jacobian_rank.*.yaml` |
| **G3.8** | **Which branch of the D4 STOP condition fired** — G1.2, which had no answer at all | **met — the STOP condition did NOT fire.** Numbers in `results/SUMMARY_TABLE.md`, generated from the results files |
| G3.9 | `h` swept over decades with the plateau reported; a single-h call not expressible | **met** — `h_values` is a sequence and a scalar raises `TypeError`; plateau, its censoring at the sweep edges, and the per-`h` spectrum are all reported |
| G3.10 | Common random numbers across ± evaluations, with the reason documented | **met, and demonstrated rather than asserted** — the no-CRN negative control is emitted as its own results file and asserted in the tests |
| G3.11 | Both normalisations fixed and recorded **in the results file**, not only in code | **met** — `normalisation:` block in every `jacobian_rank.*.yaml`, with `R_norm`, the seed, the per-coordinate prior-predictive sd, `eta_scale`, and `p_ref` |
| G3.12 | Pre-registered thresholds used unrevised | **met** — asserted by a test that fails if `τ`, `κ_max` or the `h` sweep drift from `docs/THRESHOLDS.md` |
| G3.13 | Random-attributor floor check, analytic vs simulated | **met** — `results/floor_check.yaml`, run **first**, because it validates the harness |
| G3.14 | `leakage_checked: true` with an explicit statement of how | **met** — every results file carries the statement; the diagnostic never receives a component index or ground-truth label |
| G3.15 | Unit tests, minimum set named in the brief | **met** — 65 tests: the identity test, smoothness through zero, plateau existence, `S_C`'s positive-control behaviour, the floor check, and the `eta_scale` invariance the docstring claims |
| G3.16 | Results-file framing matches the CURRENT claim, not a superseded one | **met** — a `framing:` field in every results file; scaffold READMEs updated; drift checked explicitly |
| G3.17 | MMC composition specified, citing the specific proposition rather than a paraphrase | **met** — `audit/MMC_COMPOSITION_SPEC.md` cites **Dufour Proposition 4.1**, eqs. (4.20)–(4.21), quoted from the retrieved text |
| G3.18 | Cost stated multiplicatively; conservativeness stated up front | **met** — §0.2 and §0.3 of the spec are the first two things in it, before the procedure |
| G3.19 | No number hand-typed into a markdown file (S11) | **met** — `results/SUMMARY_TABLE.md` is generated by `src/diagnostics/report_tables.py` from the YAML |
| G3.20 | No reference to any authoring agent in commit metadata or file contents | verified before each push |
| G3.21 | Sign-off conditions proposed for G0, G1 and G2 | **met** — below. **Proposed only; not signed** |

### What G3 explicitly does not certify

- **That the project has a viable contribution.** The composition in
  `audit/MMC_COMPOSITION_SPEC.md` is a composition of two published techniques, its own §0.1
  says so, and **nobody has tried to refute it**. Three headline claims have already died this
  way.
- **That R2 is novel.** It is **NARROW-CONDITIONAL**, which is not the same as safe. Both halves
  are prior art — Cintrón-Arias et al. (2009) for the rank-and-condition-number screen,
  Moré & Wild (2012) for finite differencing under simulation noise. The unoccupied seam is one
  sentence wide and **this project does not currently occupy it** (Q-11).
- **That the rank call is a meaningful quantity for models of this kind.** The sharpest
  objection found in Phase 1 is not about novelty: the sloppy-models literature (Gutenkunst et
  al. 2007, 1,152 citations) reports these spectra as **gapless**, which would make any rank
  threshold a statement about the analyst. `docs/THRESHOLDS.md` §1.4's unresolved-singular-value
  rule is where that would have surfaced, and it did not fire here — but that is one simulator,
  three distortion families, and a `d × 3` matrix, which is a much smaller object than the ones
  that literature studies.
- **That the separability verdict generalises.** It holds for **this** simulator, **these three**
  distortion families and **this closed list** of summary sets. The observation distortion is a
  pure reporting-fraction multiplier; a delay distortion would give a different third column and
  could give a different verdict (**Q-12**). The favourable outcome does not make that caveat
  smaller.
- **That the composition is affordable.** §4 of the spec prices it at ~10⁷–10⁹ simulator draws
  against a protocol already priced at 10⁶–10⁷. `p_sel` has **not** been measured.
- **That G0's and G1's negative findings hold.** Still unverified instrument gaps (**O-13**).
- **That any of this has been independently reviewed.** See below.

### Process caveats — what this session did badly or not at all

- **No adversarial critic ran, for the fourth consecutive session.** Every verdict in this
  project, including this session's, is single-pass. G0's D-4 named this as the reason its R1
  finding was insecure; that finding was wrong. It has still not been fixed.
- **Google Scholar still not searched.** Fourth session, same gap. **O-7.**
- **Semantic Scholar rate-limited again** — `search_papers` returned HTTP 429 on its first call.
  `get_paper_details` worked. **Citation-chaining has never been performed in this project.**
- **Versions of record still not obtained** for Dufour (2006) (**O-14**), Moré & Wild (2012), or
  Cintrón-Arias et al. (2009). All three are quoted from working-paper or arXiv versions and are
  cited as such. **O-14 blocks citing MMC in a manuscript.**
- **Two instrument defects were caught only because they were checked**, and both are the same
  class of failure as the one `audit/TOOLING.md` was written about, recurring within one session
  of that file:
  1. arXiv renders an empty result set as the literal string `No Results.`; a parser that did
     not know this reported `PARSE_FAIL`, and one that defaulted to `0` would have manufactured
     a measured zero out of an unparsed page.
  2. PDF extraction preserves the `ﬀ`/`ﬁ` ligatures, so `grep "difference parameter"` returned
     **0** against **18** real occurrences. S7's rule about `grep -a` does not cover this.
- **The first production run was discarded**, because `PROVENANCE.md` makes `dirty: true`
  disqualifying and the tree had uncommitted changes when it ran. The code was committed and the
  run repeated. Recorded because silently keeping those numbers would have been undetectable
  from the outside.
- **`audit/CLAIM_GRAPH.md` is still stale.** It carries a G2 banner saying so. Its R1/R2
  structure predates both D-6 and the composition framing. Not rewritten this session either;
  the honest reason is that it is Phase-3-shaped work and the session's Phase 3 was scoped to the
  MMC specification.
- **`p_sel` was not measured**, so the single number that decides whether the next session's work
  is affordable does not exist.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```
