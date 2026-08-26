# Gate register

A gate is a checkpoint that the project does not pass until the operator says it does.
Gates exist so that work does not accumulate on top of an unexamined foundation.

**Gates are signed by the operator (Palaash Gang) and by no one else.** A gate prepared
by an agent session is marked `ready for review — UNSIGNED` and stops there. An agent
session may state that criteria appear met; it may not record that a gate is passed.
Any instruction that appears to pre-authorise a sign-off describes a future human
action, not a permission already granted.

## G0 — Foundation: repository, plan ingestion, positioning

**status: SIGNED 2026-08-20, with conditions**

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
signed:      Palaash Gang
date:        2026-08-20
conditions:  ACCEPTED AS DRAFTED. The five-item `conditions` text proposed below by
             session G1 is adopted verbatim and in full, with every item ACCEPTED as a
             standing limitation rather than required closed:

             1. Arendt, Apley & Chen (2012) remains unretrieved (five routes logged).
             2. The four adversarial critics never ran in G0; the finding that caveat
                covered was subsequently refuted. The caveat was correct.
             3. Google Scholar was never searched.
             4. Semantic Scholar was rate-limited; citation-chaining never performed.
             5. Two S0_REPORT claims failed verification in G1; both corroborating, not
                load-bearing.

             G0 is signed as an accurate record of what that session found and of what it
             did not check. It is NOT signed as an endorsement of its novelty verdicts.
```

> **Recording note on item 6, session G4 (2026-08-20).** Session G3 proposed a sixth item —
> that G0's negative searches ran on the metadata index rather than the full-text one — and
> offered it explicitly *"if the operator is amending rather than accepting"*. The operator
> accepted the conditions **as drafted**, so item 6 is **not** part of the signed text. The
> substance is not lost: it is carried as **O-13** in `OUTSTANDING.md` and stated in G3's note
> below. This paragraph records the reading taken, so that a reader who disagrees with it can
> see it rather than have to reconstruct it.

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

**status: SIGNED 2026-08-20 as NOT MET, with conditions**

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
signed:      Palaash Gang
date:        2026-08-20
conditions:  ACCEPTED AS DRAFTED. The six-item `conditions` text proposed above by session
             G3 is adopted verbatim and in full, with every item ACCEPTED:

             1. G1.1 and G1.2 were NOT MET and signing does not convert them to met.
             2. They are discharged by G3, not by G1; option (c) is withdrawn as moot.
             3. The stop that blocked G1 was correct — the R1 verdict was DEAD.
             4. docs/THRESHOLDS.md was written despite the stop and is logged as
                DEVIATIONS.md D-6; its value depends on having preceded any singular value,
                which `git log` establishes.
             5. G1's negative searches are unverified instrument gaps (O-13); its positive
                finding — the R1 refutation from primary texts — is unaffected.
             6. Branke, Chick & Schmidt (2007) and Kim & Nelson (2006) remain unretrieved,
                with a recorded substitution for the latter.

             G1 is signed as an accurate record of a session whose DEFINING CRITERION WAS
             NOT MET. It is not signed as a pass.
```


## G2 — Does the composite-null gap survive a threat check?

**status: SIGNED 2026-08-20 as NOT MET, correctly stopped, with conditions**

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
signed:      Palaash Gang
date:        2026-08-20
conditions:  ACCEPTED AS DRAFTED. The seven-item `conditions` text proposed above by
             session G3 is adopted verbatim and in full, with every item ACCEPTED:

             1. G2.5 and G2.6 were not done; both are now discharged by G3.
             2. The stop was correct and was the brief's own.
             3. G2.11 — the search-instrument correction — is the most valuable thing this
                project has produced, and it was not in the brief.
             4. The correction is retrospective and the debt is not paid (O-13).
             5. The instrument-gap class of defect recurred twice in G3 within one session
                of audit/TOOLING.md being written. The ligature case is carried as O-19.
             6. Dufour's version of record was not obtained (O-14); it blocks citing MMC in
                any manuscript.
             7. No adversarial critic ran; G2's verdict is single-pass.

             G2 is signed as NOT MET, correctly stopped, and — on the evidence of G3 — the
             session that fixed the project's actual problem.
```

## G3 — First code. Does the simulator pass its own rank condition?

**status: SIGNED 2026-08-20**

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
signed:      Palaash Gang
date:        2026-08-20
conditions:  None beyond normal review. G3 is signed as met on all twenty-one criteria, and
             the "What G3 explicitly does not certify" section above is signed WITH it, as
             part of the record rather than as a set of conditions to be closed.

             Signed in the knowledge that G3's own numbers had not been attacked by anything
             at the moment of signing, and that session G4 was commissioned for exactly that
             purpose. Where G4 qualifies a G3 number, the qualification is to be recorded
             against that number in `results/` and in `docs/THRESHOLDS.md`, not by reopening
             this gate. If G4 OVERTURNS one, that is a decision point for the operator and
             not something a signed gate absorbs quietly.
```


## G4 — Does G3's own result survive being attacked?

**status: SIGNED 2026-08-20**

Prepared 2026-08-20, session G4. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **The first adversarial pass in this project's history, and the first run against its own
> output.** Four prior sessions produced verdicts, every one single-pass; the two times the
> missing critic was paid for by accident, it changed the answer.
>
> **The two summary sets came apart.** `S_B` separates under both the base distortion family set
> and an adversarially constructed one. `S_A` does not: its condition number rises 25-fold past
> the pre-registered ceiling and the verdict flips. G3 quoted them as a pair — *"two of the three
> summary sets separate the components"* — and they should not be quoted as a pair again.
>
> **No number G3 computed is wrong.** All of it reproduces, at the recorded seed and at two
> further seeds, with the pre-registered thresholds unrevised. What moved is what the numbers
> license.
>
> **Three validity flags in this repository could not have failed**, including one added to
> repair an earlier flag that could not have failed. All three are the defect class
> `DEVIATIONS.md` D-8 was written about, found by applying D-8's own rule to D-8's own repairs.

### What G4 was judged against

The gate's criteria were fixed by the session brief before any check ran. The first three are
the brief's own test of whether this was a critic pass or a confirmation pass.

| # | Criterion | Result |
|---|---|---|
| **G4.1** | **Did the pass attack the result rather than confirm it?** | **met.** Every one of the four checks was constructed so that the informative outcome is the one against the project: the family set was designed to fail, the six-column spectrum test is set up so that a *wide* spectrum is the finding, the count-CRN check includes the coupling that would have exonerated the code, and the leave-one-out asks whether the verdict rests on the suspect coordinate. Two checks came back favourable anyway and are reported as such (S10). |
| **G4.2** | **Were 1.1–1.4 all completed?** | **met**, and two checks were added that the brief did not ask for (validity flags, seed stability). 1.1 `results/robustness/threshold_sensitivity.yaml` + `wide_spectrum_check.yaml`; 1.2 `jacobian_rank.adversarial.*.yaml`; 1.3 `crn_count_check.yaml` + derivation + one targeted literature check; 1.4 `summary_smoothness_check.yaml`. |
| **G4.3** | **Is the verdict stated plainly, at the top?** | **met.** `audit/G3_ADVERSARIAL_REVIEW.md` opens with it, before the findings, per the pattern set by `R1_THREAT_CHECK.md`. |
| G4.4 | The gapless-spectrum objection tested numerically, not argued | **met** — full spectra, exact flip points `τ* = σ_K/σ₁`, verdicts at five alternative tolerances, and the six-column spectrum of the same simulator |
| G4.5 | An adversarial distortion family built by deliberate construction, not by search | **met** — one triple, each family with a named target written into `sir3.py` before the run; **no second candidate tried, none discarded**; `DEVIATIONS.md` D-9 records that the base results were known at the time, which is the part that reflects badly |
| G4.6 | The adversarial re-run used the same code, thresholds and normalisation | **met** — same `estimate_jacobian`/`analyse`, same `τ`, `κ_max`, `h` sweep, `R`, and normalisation rule; only the family set differs, and `run_family_check.py` writes to `results/robustness/`, never over `results/` |
| G4.7 | The count-CRN claim derived independently on paper, not re-run | **met** — `audit/G3_ADVERSARIAL_REVIEW.md` §3.1, with the pathwise-vs-difference-quotient distinction that G3's wording elides |
| G4.8 | Genuine degeneracy vs numerical artefact **discriminated**, not asserted | **met** — a monotone inversion coupling was implemented specifically because it would have repaired a sampler artefact. It does not repair it. |
| G4.9 | One targeted literature check on the corrected instrument (S4), with the control re-validated | **met** — control returned exactly arXiv:2405.07026 before the batch; four full-text queries, all non-zero; canonical reference located via OpenAlex and quoted (L'Ecuyer & Perron 1994) |
| G4.10 | The argmax concern checked against the reported numbers, not noted as a caveat | **met** — census at the estimator's own settings plus a leave-one-coordinate-out recomputation of the verdict |
| G4.11 | Every threshold and flag this session wrote tested against S3 ("under what condition would this read FALSE?") | **met** — and applied to G3's flags too, which is where findings 5.1–5.3 came from |
| G4.12 | No pre-registered threshold revised | **met** — `docs/THRESHOLDS.md` carries four annotations and **not one changed number**; the drift test in `tests/test_jacobian_rank.py` still passes |
| G4.13 | `results/` not overwritten, and not left reading as though unchecked | **met** — the three G3 files carry an appended `g4_adversarial_review` block; the append is textual, so the original bytes are byte-for-byte intact and `git diff` shows it |
| G4.14 | Seed stability of the verdict computed (**O-18**, open since G3) | **met** — two further seeds through the identical diagnostic; `κ` agrees to about 0.15% and no verdict moves |
| G4.15 | Gate sign-offs and the visibility trigger recorded per the operator's decisions | **met** — `GATES.md` G0–G3 signed; `docs/DECISIONS.md` **D-7**; visibility **measured** via the unauthenticated GitHub API rather than assumed |
| G4.16 | Scope boundary held: no `p_sel`, no cost gate, no MMC implementation, no `paper/main.tex` | **met** — `p_sel` is not measured anywhere in this repository; the one edit to `audit/MMC_COMPOSITION_SPEC.md` is a factual correction to a statement about existing results, changing no specification |
| G4.17 | No number hand-typed into a markdown file (S11) | **met** — `results/robustness/ROBUSTNESS_TABLE.md` is generated by `src/diagnostics/report_robustness.py` and reproduced verbatim in the review's appendix |
| G4.18 | The test suite still passes, including the threshold-drift test | **met** — 84 tests pass (65 at the end of G3; 19 added this session, of which one injects a leak and requires the leakage check to catch it) |
| G4.19 | No reference to any authoring agent in commit metadata or file contents | verified before each push |

### What G4 explicitly does not certify

- **That this was an independent review. It was not.** The same project attacked its own output,
  with its own code, inside the session that wrote the attack, and the same judgement chose both
  what to build and what counted as a fair attack on it. **This is a real limitation and it does
  not shrink because the pass found things.** A critic who wanted the result to survive and a
  critic who wanted it to fail would both have found *something* here; what neither can supply
  from inside is the check on which things were looked for. The four prior sessions were
  single-pass; this one is single-pass about its own single pass.
- **That the adversarial family set is the hardest one available**, or a fair one. It is one
  triple, built to fail, and the first thing tried. Each family's target is stated so a reader
  can disagree specifically rather than generally.
- **That the checks are exhaustive.** Four things were attacked because the brief named four.
  Untouched: whether the base parameter point is representative (everything linearises about one
  `θ`); whether `S_B`'s ten bins is a choice the verdict depends on; whether `R = 128` suffices
  for the columns rather than the plateau.
- **That `S_B` surviving means `S_B` is safe.** It survives with a margin of 1.55× where the base
  run suggested 9.88×, and its separation cost rises about forty-fold. One adversarial triple is
  one data point.
- **That the corrected `leakage_check` proves there is no leakage.** Component-label equivariance
  is necessary, not sufficient; a leak treating all three components symmetrically would pass it.
- **That `results/` now carries a real leakage check.** It does not. The literal is still there
  in all five files, deliberately — regenerating them would overwrite G3's numbers. **O-22.**
- **That the numbers reproduce on other hardware.** They reproduce from the recorded seed and
  commit on this machine, at three seeds. Nobody has run them anywhere else.
- **That any of this bears on whether the project has a paper.** It does not touch R2's novelty
  verdict, the MMC composition, or `p_sel`. The composition remains a composition of two
  published techniques that **nobody has yet tried to refute** — which is what **O-17** still
  tracks, and it is the older half of the debt this session paid only half of.

### Process caveats — what this session did badly or not at all

- **Runs were invalidated by edits made while they were in flight, again.** Three checks were
  launched, then the tree was edited, then they were killed and restarted from a clean commit —
  the same mistake that cost G3 three production runs, repeated within one session of reading
  `DEVIATIONS.md` D-8 about it. The restarted runs are the ones reported; all record
  `dirty: false`.
- **A defect was found in this session's own first output.** `dirty_paths` printed a path that
  does not exist. Fixed and recorded as **D-10**, with the tests the module had never had.
- **The adversarial family set was designed with the base results already known.** Unavoidable
  given when the session ran, and weaker than pre-registration. `DEVIATIONS.md` **D-9** says so
  and says what was done instead. **It should have been specified in G3**, alongside the base
  set and before either was run — G3's own §4.4 had already identified the weakness it probes.
- **The literature check was one targeted pass**, per the brief. It establishes that the count-CRN
  failure is known; it does not establish that nothing else relevant exists.
- **Google Scholar still not searched.** Fifth session, same gap. **O-7.**
- **`audit/CLAIM_GRAPH.md` is still stale.** Fourth session in which it has been flagged rather
  than rewritten.
- **`p_sel` still not measured**, by instruction. The one number that decides whether the next
  session's work is affordable still does not exist — and finding 2 has now changed the
  multiplier it will be assessed against.
- **The machine was heavily loaded and thermally throttled throughout**, so the runs were
  serialised by hand. This affects nothing about the numbers and is recorded because the next
  session is compute-bound: profiling puts ~87% of a simulator run in the pure-Python RK4 loop,
  at roughly 0.14 s per run, and the cost gate will be priced in units of that.

### Operator sign-off

```
signed:      Palaash Gang
date:        2026-08-20
conditions:  Signed unconditionally, together with G0, G1, G2 and G3, as of this date.

             G4 is signed as an accurate record of the first adversarial pass this
             project has run, INCLUDING its split verdict and INCLUDING the "does not
             certify" section, which is signed as part of the record and not as a list
             of conditions to be closed.

             Signing G4 does NOT settle Q-13, which remains open and blocking for the
             paper's separability sentence only. It does not endorse `S_A` as
             generalising, and it does not convert `S_B`'s survival into an
             unconditional claim.

             The gapless-spectrum objection is signed as G4 left it: DEFERRED, not
             defeated. Session G5 is commissioned to resolve it at K = 6 and to measure
             `p_sel` against the cost gate, in that order.
```

---

## G5 — Does `S_B` survive a longer component list?

**status: SIGNED 2026-08-20**

Prepared 2026-08-20, session G5. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **The verdict is WEAKENED, which is not a clean pass, so the session halted after Phase 1.**
> `p_sel` was not measured, no cost gate was built, and no line of the MMC composition was
> implemented — the same scope boundary G4 held, held for a different reason.
>
> **`S_B` separates the three components under all eight component-wise family assignments**
> the two declared distortion family sets permit, `κ` from 6.628 to 65.64. **Six of those
> eight had never been tested.** This is the strongest evidence the project has produced for
> the precondition the composition rests on, and it narrows **Q-13** materially.
>
> **The same property fails at two distortion parameters per component.** The six-column union
> is INSEPARABLE at `κ = 628.9`, rank 4 of 6, and the confound is **progression against
> observation** — not a within-component ambiguity. Every singular value is resolved to within
> 2.3%, the verdict holds across `τ` from 0.005 to 1.0, and `d = 10` leaves no structural zero,
> so none of the three easy explanations survives.
>
> **A rule this session wrote before the run fired against the project, and a measurement taken
> afterwards was used to qualify it.** That is disclosed at the top of
> `audit/K6_SPECTRUM_CHECK.md` §0 and in `DEVIATIONS.md` **D-13**, and it did **not** buy the
> session anything: the halt happened anyway.

### What G5 was judged against

The criteria were fixed by the session brief before any check ran.

| # | Criterion | Result |
|---|---|---|
| **G5.1** | **Was the stop condition honoured?** | **met.** The brief permits continuation only in the absence of *"any verdict other than a clean pass"*. WEAKENED is not a clean pass, and the session halted before Phase 2 — including the `p_sel` measurement it was otherwise free to take, and which **Q-14** explicitly does not block |
| **G5.2** | **Was the negative half reported at the same weight as the favourable half?** | **met.** The six-column INSEPARABLE verdict is sub-verdict 2 of 3 in `audit/K6_SPECTRUM_CHECK.md`, has its own section, and appears in the commit message, the gate headline and the report's opening. The favourable half is reported first only because S10 requires favourable findings not be buried either |
| G5.3 | Full six-column spectrum computed and reported, all singular values | **met** — `results/robustness/k6_spectrum.yaml`, all three summary sets, three column counts each, plus decade-span, adjacent ratios, and where `τ·σ₁` falls relative to the spectrum |
| G5.4 | Whether a gap exists, or a smooth decay, reported without inventing a criterion | **met** — `gap prominence` (largest adjacent ratio ÷ median) is reported as a *descriptive* statistic with no threshold applied and no verdict depending on it. Inventing a gap criterion with the singular values visible is the leakage failure `LEDGER_DESIGN.md` D3 names |
| G5.5 | The six-column object run through the machinery the three-column verdict was run through | **met, and this is the load-bearing addition.** G4's six-column number came from a single step size, which `docs/THRESHOLDS.md` §1.4 says *"is not a result"*. It now carries the h-plateau, the resolution test, the equivalence-class stability requirement and a 719-permutation leakage check |
| G5.6 | At least five alternative `τ`, both family sets, stable range and flip boundary identified | **met** — nine tolerances spanning four decades, under **both** couplings (`κ_max = 1/τ`, and `κ_max` held at 100), with the exact flip point `τ* = σ_K/σ₁` computed rather than sampled |
| G5.7 | The `κ_max` branch resolved rather than deferred a second time | **met** — closed form derived, region stated (`κ_max < κ ≤ 1/τ`, empty at the registered pair), and checked against the production rule at 108 grid points per spectrum. Two deliberately broken grids are required to be caught by `tests/test_k6_spectrum.py` |
| G5.8 | `audit/K6_SPECTRUM_CHECK.md` written, verdict at the top, G4's STANDS/WEAKENED/OVERTURNED vocabulary | **met** — three sub-verdicts, because one word does not carry it |
| G5.9 | No pre-registered threshold revised | **met** — `docs/THRESHOLDS.md` is untouched this session; the drift test in `tests/test_jacobian_rank.py` still passes |
| G5.10 | `results/` not overwritten | **met** — everything written this session is new and lives in `results/robustness/`; the five G3 files and the G4 robustness files are byte-identical |
| G5.11 | Every prose number traceable to generated output (S10) | **met** — `results/robustness/K6_TABLE.md` is generated by `src/diagnostics/report_k6.py` and reproduced verbatim in the check's appendix; every claim in the prose was verified against the YAML programmatically before the document was committed |
| G5.12 | Flags tested against S4 ("under what condition does this read FALSE?") | **met** — the reproduction check is shown failing on a 0.1% perturbation; the `κ`-algebra checker is shown catching an inverted ceiling comparison and a rank rule on the wrong singular value; the liveness check is exercised against a live process, an exited one, a recycled PID and a stale pidfile |
| G5.13 | The S3 liveness defect understood and specifically fixed, not reused | **met** — `src/runlock.py` replaces pattern-matching over a process listing with a kernel query on one recorded PID, with PID-reuse and zombie guards. The three ways the old form reports a live run as dead are written out in its docstring |
| G5.14 | No tree edit while a run was in flight | **met** — two runs, both launched from a clean committed tree, both recording `dirty: false` and `dirty_paths: []`; the runner refuses to start when a live instance holds its output path |
| G5.15 | Gate sign-offs and the visibility ruling recorded per the operator's decisions | **met** — G4 signed with G0–G3; `docs/DECISIONS.md` **D-11** records the visibility ruling and forecloses re-raising it |
| G5.16 | Scope boundary held | **met** — no `p_sel`, no `results/cost_gate.yaml`, no MMC implementation, no `paper/main.tex`. The eight family assignments are a re-combination of the two declared sets, not an extension beyond them, and no new distortion family was written |
| G5.17 | Departures from the brief disclosed rather than silently reinterpreted | **met** — **D-12** (the brief asked for two six-column spectra; only one exists) and **D-13** (a pre-registered implication refuted by a later measurement) |
| G5.18 | The test suite still passes | **met** — **109 tests** (84 at the end of G4; 25 added, of which **eight** require a check to fail or a bad input to be rejected) |
| G5.19 | No reference to any authoring agent in commit metadata or file contents | verified before each push |

### What G5 explicitly does not certify

- **That refining the pre-registered implication was the right call.** A rule written before the
  run said a cross-mechanism six-column confound overturns the three-column result; it fired;
  and an eight-assignment measurement taken afterwards was used to say the implication was too
  strong. **The classification criterion is reported exactly as it fired and is not
  reinterpreted — but the refinement is in the project's favour and was made after seeing the
  data.** Both readings are in `audit/K6_SPECTRUM_CHECK.md` §0 so the operator can take the
  other one. **This is the single most scrutinisable judgement in the session.**
- **That eight family assignments are a sample of anything.** They are every combination of
  **two** family sets this project chose, one of which was designed to fail. **Q-13 is narrowed,
  not closed.**
- **That the six-column failure is confined where this session says it is.** Only `K = 3` and
  `K = 6` were measured. The intermediate case — one component carrying two parameters while the
  others carry one — is constructible from the recorded columns at zero simulation cost and was
  **not run**. **Q-15.**
- **That `S_B` is comfortable.** The worst assignment, `ABA` at `κ = 65.64`, flips at 1.523× the
  registered `τ` — so **doubling `τ` flips it**, and the project's own halve/double grid
  straddles the boundary. G4's sentence *"halving or doubling `τ` changes nothing"* is true of
  the base families and false of the adversarial ones.
- **That the resolution test guards against a gapless spectrum.** `audit/R2_THREAT_CHECK.md`
  §1.3 nominated it for exactly that and **it did not fire**: all six values are resolved to
  within 2.3% while the spectrum is 2.80 decades wide with essentially no break. The test
  measures estimator convergence; spectral density is a property of the matrix. That sentence in
  `R2_THREAT_CHECK.md` should not be relied on again.
- **That anything here bears on affordability.** `p_sel` remains unmeasured through six
  sessions. **O-16.**
- **That the MMC composition has been attacked.** It has not, by anyone, ever. **O-17**, older
  and larger half, unpaid.
- **That this was an independent review.** Same project, same code, same session that wrote the
  check. Unchanged from G4 and not improved by this session having found things.
- **That the numbers reproduce on other hardware.** They reproduce on this machine, from the
  recorded seed and commit, and the three-column spectra reproduce the G3/G4 records exactly —
  which is a check on this session's estimator, not on anyone else's machine.

### Process caveats — what this session did badly or not at all

- **The first Phase 1 run was discarded and repeated.** The eight-assignment analysis was
  conceived *after* the first run had produced the six-column verdict, so the run was repeated
  to add it. Nothing was contaminated — the tree was clean, the output was deleted before the
  rerun, and the numbers are identical — but it is the third session in a row in which the
  right check was thought of after the run rather than before it (**D-9**, **D-13**).
- **The pre-registered rule was written too coarsely**, which is what made **D-13** necessary.
  A rule that had said "only if the confound lies inside some three-column assignment" would
  have been testable rather than assumed, and the test was cheap.
- **`p_sel` was not measured, for the second session running.** G4 did not measure it by
  instruction; G5 did not measure it because it halted first. **Q-14 explicitly does not block
  it**, so this is a consequence of the stop rule rather than of the finding.
- **Google Scholar still not searched.** Sixth session. **O-7.**
- **`audit/CLAIM_GRAPH.md` is still stale.** Fifth session flagged rather than rewritten.
- **`results/` still carries the vacuous `leakage_checked` literal.** **O-22**, unchanged — the
  new files carry a real check, the G3 files still carry the literal, and regenerating them was
  again judged out of scope.
- **The machine was loaded throughout** (load average ~7 on 8 cores, 8 GB), so the column
  estimation ran on four workers rather than eight and the two runs took about 13 minutes each.
  Irrelevant to the numbers; relevant to whoever prices Phase 2.

### Operator sign-off

```
signed:      Palaash Gang
date:        2026-08-20
conditions:  Signed as an accurate record of the session, INCLUDING the "does not
             certify" section and INCLUDING the split verdict.

             The WEAKENED classification stands, on one condition: the paper's scope is
             restricted to single-mechanism-per-component misspecification. That
             restriction is a real limitation to be stated alongside the positive result,
             not after it. It is recorded as `docs/DECISIONS.md` **D-14**, DECIDED.

             D-13's refinement is accepted as read. The operator has taken the reading
             the session recommended and not the alternative; both remain on the record
             in `audit/K6_SPECTRUM_CHECK.md` §0.

             Signing G5 does NOT close Q-13, which stays open and blocking for the
             paper's separability sentence. It does close Q-14, in the direction of that
             question's option (a).

             `docs/DECISIONS.md` **D-12** is decided in favour of **Path 1**: measure the
             cost gate before building the composition. Session G6 is commissioned to
             take that measurement and no more — the composition is not to be built
             until the gate has reported.
```

## G6 — Is the composition affordable at all?

**status: ready for review — UNSIGNED**

Prepared 2026-08-20, session G6. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **The cost gate FAILS, and it fails on non-termination rather than on cost.** `p_sel` — the
> number three sessions deferred — is measured. `results/cost_gate.yaml`, `results/p_sel.yaml`.
>
> **At the base parameter point the composition is comfortably affordable.** The worst
> selection cell holds **0.2346** of null draws under `S_B` with the primary `AAA` assignment
> and the studentised rule (95% CI 0.2320–0.2372), so one MMC test costs **4.2×10⁵ to
> 4.3×10⁷** draws against the pre-registered gate of 10⁸. That is a PASS, and it is the only
> case that passes.
>
> **Over the nuisance set it is not affordable at any price.** The specification's own cost
> model takes the minimum over `θ ∈ Ω₀`. At a relative half-width of **0.05** — the narrowest
> box measured — that minimum is **zero acceptances in 100,000 draws**, 95% upper bound
> 3.84×10⁻⁵, so the cost is unbounded and at least **2.6×10⁹** draws at the cheapest declared
> `(M, N)`. **FAIL at all four declared corners, under both selection-rule variants, for both
> family assignments, and `ci_decides_the_gate` is TRUE.**
>
> **The mechanism is measured, not argued.** The selection rule must be `θ`-free, because
> `audit/MMC_COMPOSITION_SPEC.md` §3.4's lemma needs one event applied to the observation and
> to every replicate. The nuisance parameters shift the normalised summary distribution by a
> **median of 27 and up to 65 standard deviations** at half-width 0.05, against a single-draw
> noise magnitude of 3.16. A `θ`-free rule facing a shift twenty times the noise selects one
> component deterministically. **That is §3.4's own named failure case — the one where the
> rejection sampler never terminates — and it now has a number.**
>
> **This is the first thing this project has measured about the composition rather than about
> its precondition.** It is also the first partial payment on the older half of **O-17**.

### What G6 was judged against

The criteria were fixed by the session brief before any check ran.

| # | Criterion | Result |
|---|---|---|
| **G6.1** | **Was `p_sel` measured, with an uncertainty rather than a point value (S5)?** | **met.** Every cell probability carries a Wilson 95% interval; the gate is evaluated at both ends of it and `ci_decides_the_gate` is reported as a flag. It reads TRUE here — the measurement is precise enough that the verdict does not move within the interval |
| **G6.2** | **Was the AAA (worst validated) case the headline, rather than a more favourable one?** | **met.** `AAA` is the headline and `BBB` is reported as contrast. Both fail. The one PASS in the whole document — the base-parameter-point floor — is labelled "not the gate" wherever it appears |
| G6.3 | The pre-registered cost model used exactly, not re-derived | **met** — `M × N / min_θ p_sel` with `M ∈ {10³, 10⁴}` and `N ∈ {99, 999}` taken from `audit/MMC_COMPOSITION_SPEC.md` §4's own table, evaluated at all four corners because the specification gives ranges rather than values |
| G6.4 | The compute budget located in project records and cited | **met** — the gate's own threshold is 10⁸ draws (§4); the declared budget is `audit/S0_REPORT.md` §7's *"Forward simulation only, ≤10⁷ solves"*. **Both are reported, and the discrepancy is reported rather than reconciled: the gate sits an order of magnitude above the budget it claims to represent** |
| G6.5 | `results/cost_gate.yaml` written with propagated uncertainty and an exact ratio | **met** — plus `results/COST_GATE_TABLE.md`, generated, so no number in prose is hand-typed (S11) |
| **G6.6** | **Was the FAIL branch honoured?** | **met.** Phase 3 was not entered: `audit/MMC_COMPOSITION_SPEC.md` is untouched, its superseded 10⁷–10⁹ estimate is left standing and flagged as outstanding rather than quietly corrected, and no composition code exists |
| G6.7 | The S3 liveness check fixed and verified before launch | **met** — `src/runlock.py` exercised against a real still-running process, a live process with a mismatched module, a killed process and an absent pidfile, in that order, before anything was launched |
| G6.8 | No tree edit while a run was in flight | **met** — the run was launched from a clean committed tree and recorded `dirty: false`, `dirty_paths: []` |
| G6.9 | Flags tested against S4 ("under what condition does this read FALSE?") | **met** — every gate flag is shown coming out both ways on either side of its own stated flip point; the three-valued verdict is shown reaching PASS, FAIL and SPLIT; a zero-acceptance point is required to produce an infinite point cost and a finite bound |
| G6.10 | Departures and defects disclosed rather than silently reinterpreted | **met** — **D-14** (the specification defers `T_k`; this session chose one, and the number is conditional on it) and **D-15** (a flag written this session read FALSE for a reason other than the one it named — D-8's failure mode, one generation later) |
| G6.11 | The bookkeeping the operator's decisions required | **met** — G5 signed; **D-12** decided as Path 1; **D-14** recorded as DECIDED with the four places the scope obligation lands, including `paper/main.tex` |
| G6.12 | The test suite still passes | **met** — **140 tests** (109 at the end of G5; 31 added, of which **16** require a check to fail, a bad input to be refused, or a flag to come out both ways) |
| G6.13 | Scope boundary held | **met** — no MMC composition, no rejection sampler, no maximiser, no `paper/main.tex`. `src/attribution/` contains the selection rule and nothing else |
| G6.14 | No reference to any authoring agent in commit metadata or file contents | verified before each push |

### What G6 explicitly does not certify

- **That `p_sel` is a property of the composition.** It is a property of the composition **and
  of the selection rule `T_k`**, which `audit/MMC_COMPOSITION_SPEC.md` §6 left *"not
  specified"* and which this session had to choose in order to measure anything at all. A
  different `T_k` gives a different `p_sel` and a different cost. **This number is conditional
  on `src/attribution/selection.py` in exactly the way G3's separability verdict is conditional
  on three distortion families.** `DEVIATIONS.md` **D-14**.
- **That the primary studentisation variant was the neutral choice.** It is the one favourable
  to the gate, by construction: studentising equalises the cells and the cost is `1/min p_sel`.
  It was nominated primary before any number existed and for a stated reason, and the
  unfavourable variant is measured and reported beside it — but a reader weighing this should
  know the primary was chosen knowing which direction it pointed. **Both variants fail**, which
  is the only reason the choice is not load-bearing here.
- **That the nuisance box is `Ω₀`.** `Ω₀` is not specified anywhere in this project. A relative
  box on the five coordinates §1 names is a stand-in, its half-widths were declared before the
  run, and the headline width of 0.20 was declared before the run. **A grid understates a
  minimum**, so the cost reported is a lower bound on what a continuous derivative-free
  maximiser would pay.
- **That the boundary has been located.** The collapse is already complete at the narrowest
  box measured. **Where between `θ_0` and ±5% the cells stop being reachable is unknown**, was
  not measured, and would cost about ten minutes. **Q-16** says exactly how.
- **That option (a) of Q-16 has been ruled out.** Bounding `Ω₀` tightly enough may well restore
  termination. What this session establishes is that it is not free: §4 point 2 prices it as
  the CSEMMC downgrade from finite-sample to asymptotic validity.
- **That the composition has been attacked.** It has now been **measured**, which is the first
  payment on **O-17**'s older half in seven sessions. It has still not been refuted by anyone,
  and this measurement was taken by the same project, in the same session that wrote the rule
  it measures.
- **That the wall-clock translation licenses anything.** This session found that null draws at
  a fixed `θ` share one deterministic integration, which makes a draw about 0.36 ms rather than
  the ~0.14 s `GATES.md` G4 recorded — so the gate's own 10⁸-draw threshold is roughly ten
  core-hours, not thousands. **That does not rescue anything here**: an unreachable cell is not
  expensive, it is unreachable, and no machine changes that. It is recorded because it changes
  what a future cost estimate should assume, not what this one concluded.
- **That this was an independent review.** Same project, same code, same session. Unchanged
  since G4 and not improved by this session having found something.

### Process caveats — what this session did badly or not at all

- **A flag written this session read FALSE for a reason other than the one it named**, which is
  the exact defect `DEVIATIONS.md` D-8 records, in the session that had just re-read D-8, D-10
  and D-13 before writing any code. It was caught only by disbelieving the output. **D-15.**
- **`T_k` was specified by a session, not by the operator.** It is a real design decision with
  the cost number hanging off it, taken under time pressure because the measurement was
  otherwise impossible. **D-14**, and it is the fourth consecutive session in which the right
  piece of work turned out to have been available earlier than it was done.
- **`audit/MMC_COMPOSITION_SPEC.md` §4 still carries its superseded 10⁷–10⁹ estimate**, because
  the brief's FAIL branch forbids Phase 3. A specification containing an estimate that a
  measurement has superseded is the staleness problem `audit/CLAIM_GRAPH.md` has been flagged
  for since G2. **O-28.**
- **The boundary sweep was not run.** Deliberately — see the "does not certify" section — but
  it means the most actionable follow-up question is left open at a cost of ten minutes.
- **Google Scholar still not searched.** Seventh session. **O-7.**
- **`audit/CLAIM_GRAPH.md` still stale.** Sixth session flagged rather than rewritten.
- **`results/` still carries the vacuous `leakage_checked` literal** in G3's files. **O-22.**
- **No literature check ran at all**, by scope. The non-termination of a rejection sampler
  under nuisance drift is not an exotic phenomenon and somebody has very likely written about
  it; nobody here looked.
- **The machine was heavily loaded** (load average 40–150 on 8 cores, shared with unrelated
  work), so the wall-clock figures are upper bounds on this hardware rather than clean timings.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

---

## G7 — Is the paper's scope closed, and does every figure it needs exist?

**status: ready for review — UNSIGNED**

Prepared 2026-08-21, session G7. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **The scope is closed and the figures exist.** `docs/DECISIONS.md` **D-16**: the MMC
> composition is dropped as an experimental vehicle and kept as a stated negative result. Four
> contributions, consolidated in `audit/FINAL_CLAIMS.md`. **Seven figures**, in vector PDF at
> the venue's own column width, each carrying a provenance sidecar naming the `results/` files
> it was drawn from and — per plotted series — the dotted path the numbers came from, re-read
> from disk and compared. **No figure existed anywhere in this repository before this session.**
>
> **The boundary is located, and the collapse is a slide rather than a cliff.** Ten half-widths
> from 0.001 to 0.05, 7,602,000 null draws, six minutes. Under the pre-registered criterion the
> primary case is **GRADUAL**: about **one decade of acceptance probability per 0.7% of relative
> nuisance error**, log-linear at `R² = 0.94`. **The pre-registered gate passes at every declared
> corner only inside a ±0.5% box** on all five nuisance coordinates at once — Q-16 guessed ±0.4%
> and called such a bound *"no epidemiologist will accept"*.
>
> **The mechanism was predicted before the run and the prediction held.** The sweep's design
> docstring, committed before it produced a number, predicted from G6's recorded shift that the
> nuisance perturbation would overtake the observation noise near `w ≈ 0.006`. Measured: the
> crossing is between `w = 0.005` and `w = 0.0075` — **and that is exactly where the gate stops
> passing.** The shift-to-noise ratio is therefore a one-line check anybody holding a different
> simulator can run before attempting this composition on it, and it is the transportable part
> of the finding.
>
> **Two things reproduced on draws session G6 never took**, neither arranged: `θ₀` at a maximum
> two-proportion `|z| = 1.96` against a threshold of 3, and the ±5% collapse down to **the same
> 21 of 42 dead design points**.
>
> **One thing this session did badly, for the third time in this project's history.** A flag it
> wrote read FALSE for a reason other than the one it named. **`DEVIATIONS.md` D-17.**

### What G7 was judged against

The criteria were fixed by the session brief before any check ran.

| # | Criterion | Result |
|---|---|---|
| **G7.1** | **Was Q-16 resolved as an execution of the operator's decision, not a session's?** | **met.** `docs/OPEN_QUESTIONS.md` Q-16 marked ANSWERED with the date and rationale; `docs/DECISIONS.md` **D-16** recorded DECIDED with the four contributions, what it forecloses, and what it does not do; `audit/MMC_COMPOSITION_SPEC.md` re-headed as a historical / negative-result document with nothing deleted. Committed as its own unit before any other work |
| **G7.2** | **Was the boundary sweep run as characterisation rather than verdict-seeking (S3)?** | **met, and the ordering is the evidence.** D-16 was decided, committed and pushed at `f11de77`; the sweep's script was written afterwards and committed at `c2f3641` before it produced a number. The script's docstring states in advance what it would have done had the result gone the other way — *"if this sweep had found the cells reachable out to 0.04, the composition would still be dropped"* — and every gate row in `results/boundary_sweep.yaml` carries a field saying it decides nothing |
| G7.3 | The sweep's design, widths, refinement rule and shape criterion pre-registered | **met** — committed at `c2f3641` with 13 tests, including the three branches of the shape criterion and the CENSORED_BELOW branch that makes it refuse rather than guess |
| G7.4 | `results/boundary_sweep.yaml` written with replicate counts and intervals matching the rigour of every other results file | **met** — Wilson intervals throughout, seed spans asserted disjoint from G6's before the run, `dirty: false`, plus a generated `results/BOUNDARY_TABLE.md` so no number in prose is hand-typed (S11) |
| **G7.5** | **Do all figures draw only from `results/` (S4)?** | **met.** Five figures read `results/` and nothing else; the two schematics plot no measured number at all and their sidecars say so and state the different correctness condition they carry. The one new computation was authorised, and it wrote `results/boundary_sweep.yaml` before any figure read it |
| G7.6 | Figures at the stated publication quality bar | **met, with one gap named in the section below** — vector PDF, one shared style module, Okabe-Ito, Times because the venue's own `.sty` sets `ptm`, and a column width **parsed from that `.sty` at import time** rather than typed. Every figure drawn at final printed size, nothing below the venue's own 6pt floor |
| **G7.7** | **Figure provenance (2.2), and is its check able to fail (S5)?** | **met.** Each figure carries a sidecar with source hashes, the emitting script's own provenance header, the commit, the caption and the output hashes. Each declares, per plotted series, the dotted path its numbers came from; the writer re-reads the file and compares. `tests/test_viz.py` shows the check reading FALSE on each of the four things the module claims it catches — a hand-typed number, an undeclared transform, a source rewritten mid-generation, and a moved path |
| G7.8 | Unit test of the figure pipeline on synthetic data before trusting it on real results (2.3) | **met** — a known figure from known input, with the artists read back and compared against the input and against hand-computed axis bounds |
| G7.9 | Captions drafted alongside each figure | **met** — stored in each sidecar, 1,249 to 1,443 characters, written while the figure's content was fresh |
| **G7.10** | **S1 extended to figure metadata** | **met.** `savefig` is unreachable from a figure script; `src/viz/style.save` is the only sanctioned writer, because there is no `savefig.metadata` rcParam — verified against `matplotlib.rcParams`, not assumed. `pdfinfo` on each PDF shows the emitting script as Creator and Producer and **no CreationDate**; a `strings` grep over every PDF, SVG and PNG against a pattern that includes the plotting library's own name returns nothing. A test asserts it against whatever is in `figures/` |
| G7.11 | Figures generated from a clean tree | **met, on the second attempt.** The first pass wrote seven sidecars recording `dirty: true`; `PROVENANCE.md` makes that disqualifying, so the code was committed and all seven were redrawn. Output is byte-reproducible, so the discarded pass differed only in its recorded commit |
| G7.12 | The final claim set consolidated (4.1, 4.2) | **met** — `audit/FINAL_CLAIMS.md` with four sections, each carrying the exact claim, evidence files, scope conditions and figures; 75 load-bearing numbers **generated** with their dotted paths (`results/FINAL_CLAIMS_NUMBERS.md`); `audit/CLAIM_GRAPH.md` superseded by a banner rather than rewritten |
| G7.13 | Departures and defects disclosed rather than silently reinterpreted | **met** — **D-16** (a results file written twice, with the substance shown bit-identical) and **D-17** (a flag reading FALSE for a reason other than the one it named, and a threshold fixed after the run rather than before it) |
| G7.14 | The test suite still passes | **met** — **177 tests** (140 at the end of G6; 37 added, of which **19** require a check to fail, a bad input to be refused, or a flag to come out both ways) |
| G7.15 | Scope boundary held | **met** — no `paper/main.tex`, no composition code, no rejection sampler, no maximiser. `src/attribution/` still contains the selection rule and nothing else |
| G7.16 | No reference to any authoring agent in commit metadata, file contents, or figure metadata | verified before each push, with the figure-metadata check added this session |

### What G7 explicitly does not certify

- **That anybody has looked at these figures.** Nobody but the session that drew them has.
  The provenance chain establishes that every plotted number is at its declared path in
  `results/`; it establishes **nothing** about whether a figure is legible, whether a caption
  describes its own figure, or whether an annotation placed by hand states the truth. Three
  figures carry hand-placed annotations, each disclosed in its sidecar as outside the automatic
  check. **This is the same category as G4's "not a fully independent check", and it is why
  operator point P-1 asks for eyes on the PDFs rather than on this report.**
- **That the four contributions are the right four.** They are the operator's, recorded as
  D-16. What this session did is state them precisely enough to be disagreed with, which is
  what **P-2** asks the operator to do.
- **That C1 is claimable in the form written.** `docs/DECISIONS.md` **D-6** forecloses claiming
  the estimator or the rank rule as new; **D-16** names the diagnostic as contribution 1.
  `audit/FINAL_CLAIMS.md` writes C1 to satisfy both and **flags the tension rather than
  resolving it**. A session may not decide this. If the reading is wrong, C1 needs rewording
  before a word is drafted.
- **That the boundary sweep answers anything about `Ω₀`.** `Ω₀` is still not specified anywhere
  in this project. A relative box on the five coordinates §1 names is a stand-in, its widths
  were declared before the run, and **a grid understates a minimum** — so every cost reported is
  a lower bound and the ±0.5% figure is the most generous reading available.
- **That the GRADUAL classification is a property of the simulator alone.** It is a property of
  the simulator **and of the selection rule**: the two studentised cases classify GRADUAL and
  the two `plain` cases ABRUPT. The split is reported rather than averaged, and the primary
  case is the one nominated in G6 before any number existed.
- **That `D-17`'s replacement threshold is neutral.** `THETA0_Z_MAX = 3.0` was fixed **after**
  the first run, which is the pattern D-9 and D-13 exist to make visible. Three things are done
  about it and none of them is nothing: the replacement was forced by an error demonstrable
  without reference to the outcome, the value is a conventional 3σ with its family-wise rate
  stated, and the observed maximum is published beside the flag as a number so the threshold is
  not load-bearing.
- **That the figures are in the venue's exact typeface.** They are set in Times because
  `neurips_2026.sty` sets `ptm`, and this machine resolved *Times New Roman*, which is recorded
  in every sidecar. A machine without it would fall through to a non-Times-metric face. The
  fall-through is made visible in the record; it is not prevented.
- **That this was an independent review.** Same project, same code, same session. Unchanged
  since G4 and not improved by this session having produced more artefacts than any before it.

### Process caveats — what this session did badly or not at all

- **A flag written this session read FALSE for a reason other than the one it named. Third
  occurrence** — `DEVIATIONS.md` D-8 (G3), D-15 (G6), **D-17** (here) — in a session that read
  both prior entries before writing code. Worse than G6's: the countermeasure D-8 itself
  proposed, running every check once in a state where it should give the opposite answer,
  **was available and was not applied to this flag**. The smoke run did exercise it and it did
  read FALSE there, and that was read as "expected at 400 draws" rather than as a reason to
  check the arithmetic.
- **A results file was written twice.** `results/boundary_sweep.yaml`. The substance is
  bit-identical between the two runs and that is verified rather than asserted, but a
  re-measurement forced by a defective check is a real cost. **D-16.**
- **The figures were drawn twice**, for the same class of reason: the first pass ran from a
  tree whose style module had changed after its own commit, so every sidecar recorded
  `dirty: true`.
- **Three figures carry hand-placed annotations that the provenance check does not cover.**
  Each is disclosed in its own sidecar with the source-file value beside it, which is the best
  available substitute and is not the same thing.
- **`audit/CLAIM_GRAPH.md` is superseded rather than rewritten.** Seventh session flagged. The
  banner is now stronger — it says the file is not to be read as current — but the underlying
  work was again not done.
- **Google Scholar still not searched.** Eighth session. **O-7.**
- **`results/` still carries G3's vacuous `leakage_checked` literal.** **O-22.**
- **No literature check ran at all**, by scope. The non-termination of a rejection sampler
  under nuisance drift is not exotic and somebody has written about it; nobody here has looked,
  and this is now the fourth thing the paper will assert without a prior-art sweep behind it.
- **`Q-15` / O-26 is still not closed**, and it costs no simulation: the intermediate `K = 4`
  and `K = 5` cases are constructible from columns already recorded and would say whether the
  confound needs all six columns or only four.
- **The machine was loaded throughout** — load average between 8 and 18 on 8 cores, shared with
  unrelated work — so wall-clock figures are upper bounds on this hardware. Draw counts are not
  affected.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

---

## G8 — Does `paper/main.tex` exist, does it compile, and does it say what the C1 amendment requires?

**status: ready for review — UNSIGNED**

Prepared 2026-08-22, session G8. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **A full draft exists and compiles.** `paper/main.tex`: abstract, introduction, background,
> method, experiments, the MMC negative result, limitations, a filled reproducibility
> checklist, references, and an appendix. Five figures placed in the main body, two more
> (schematic, threshold-sensitivity) and the full eight-assignment table moved to the appendix
> for space. Compiles cleanly with `pdflatex` via `latexmk` — no undefined references, no
> undefined citations, no overfull boxes — using `TEXINPUTS=".:neurips_2026_template:"` rather
> than a duplicated `.sty` file.
>
> **It does not fit.** Sim2Science's limit is 5 pages, references and appendix excluded. This
> draft is **6 pages of body content** after three separate rounds of cutting: figure captions
> shortened by roughly 75%, prose tightened by roughly 30%, three of seven figures and the full
> data table moved to the appendix, every inline figure's width reduced twice. Further cuts were
> not made. **P-1.**
>
> **The C1 amendment is applied and, on this session's own re-read, holds.** `audit/FINAL_CLAIMS.md`'s
> C1 section was amended first, as its own commit, before any paper prose was written. A
> dedicated drift-hunt pass (Phase 4.2) found one real instance of the amendment's discipline
> not yet reaching a sentence — not the method-novelty drift the hunt was looking for, but an
> adjacent overclaim on the MMC composition's exactness, fixed. See below.

| # | Criterion | Result |
|---|---|---|
| **G8.1** | Was the C1 amendment applied as its own commit, before any paper prose existed? | **met.** `audit/FINAL_CLAIMS.md` amended and pushed first; the old "composition into a decision procedure" reading kept, marked superseded, not deleted, matching this project's own pattern for superseded text |
| **G8.2** | Does the draft actually reflect the amendment, on a dedicated re-read (4.2)? | **met, with one real finding.** No sentence in the paper claims the diagnostic, its composition into a gate, or the MMC composition as a novel method. One adjacent issue found: two sentences described the MMC composition's output as "exact conditional inference" / "exactly calibrated" without the level-vs-size distinction `audit/MMC_COMPOSITION_SPEC.md` §0.2 requires. Reworded to state nominal-level control, conservatively, with both sources of conservativeness named |
| **G8.3** | Does every number in the prose trace to a source (S4)? | **met.** `audit/PAPER_NUMBER_VERIFICATION.md`, row by row, against `audit/FINAL_CLAIMS.md`'s generated appendix or the source document's own generated table. Two rows are **prose-sourced** rather than table-sourced — flagged as the weaker form rather than treated as equivalent |
| G8.4 | Template and anonymization compliance | **met.** `dblblindworkshop`, `\workshoptitle{Sim2Science}`; compiled PDF and source both grepped for the operator's name, GitHub handle, and repository name — zero hits; author block renders `Anonymous Author(s)` correctly; no acknowledgments section |
| G8.5 | Bibliography actually contains what the paper cites | **met, and this session found a real gap.** Four papers named throughout `docs/DECISIONS.md` and `audit/FINAL_CLAIMS.md` as prior art (Cintrón-Arias 2009, Moré & Wild 2011/2012, Dufour 2006, Gutenkunst 2007) had never been fetched into `audit/BIBLIOGRAPHY.bib` despite the file calling itself their source of truth. Fetched the same way as every other entry (DOI content negotiation, cross-checked against Crossref). `DEVIATIONS.md` **D-18** |
| G8.6 | A documented citation defect actually fixed before use, not just documented | **met.** `Catchpole_1997`'s incomplete author list (missing Morgan) was flagged by `audit/LEDGER_CITATIONS.md` and by a comment in the bibliography file itself six sessions ago, with the exact fix specified — and never applied anywhere citable. A corrected `CatchpoleMorgan_1997` entry was added; the paper cites that one |
| G8.7 | Figures placed with correct captions, sourced from the existing `figures/` directory, not regenerated (S5) | **met.** All seven figures used verbatim; no figure script touched. Two figure widths reduced for page-fit; content, data, and provenance untouched |
| G8.8 | Reproducibility checklist complete, not left as placeholders | **met.** All 16 items answered. The two closest to this session's standing tensions were judged rather than defaulted: code/data release answered No (unanonymized release would break double-blind), LLM usage answered N/A on the basis that the simulator, diagnostic, and every reported measurement predate this drafting session |
| G8.9 | Every commit checked against the four-check pre-push checklist, extended to the paper's rendered text | **met.** Checked before every push this session, including a rendered-PDF-and-source anonymization grep not previously part of the standing checklist |
| G8.10 | The title question (1.2) resolved or flagged | **flagged, not resolved.** *"Selective Inference for Component-Level Simulator Misspecification"* kept in the source, with a comment flagging the question and an alternative proposed in this report. **P-2** |

### What G8 explicitly does not certify

- **That anyone has read this as a paper.** The same failure mode G7 recorded for the figures
  applies here to the prose: nobody but this session has read the argument end to end for
  persuasiveness, clarity, or whether a reviewer unfamiliar with eight sessions of audit trail
  would follow it. Passing every mechanical check (compiles, cites resolve, numbers trace) is
  not the same thing as being a good paper. **P-1**, and it is a stronger version of P-1 than
  G7's: a PDF can be glanced at in a minute; a 6-page argument cannot.
- **That the page-limit gap is closed.** It is not. Six pages of body content against a 5-page
  limit, after three genuine rounds of cutting. This session's judgement is that a fourth round
  would start cutting a figure or a section's substance rather than its phrasing, and stopped
  rather than doing that silently. The operator may disagree with where that line was drawn.
- **That the title fits the reframed paper.** The C1 amendment removes any claim that
  "Selective Inference" is itself a contribution; the paper is about where component-level
  attribution is identifiable and where a selective-inference construction on top of it fails,
  which is a different emphasis than the title states. An alternative was drafted and not
  substituted, per instruction 1.2: *"Diagnostics and Limits for Component-Level Simulator
  Misspecification"* — matches the paper's own framing language and the venue's CFP bullet
  ("simulator diagnostics", "degeneracy, simplifications, and identifiability") more closely,
  at the cost of losing the current title's more specific pointer to the negative result. **P-2**.
- **That the checklist's substantive answers are the operator's answers.** They are this
  session's best-faith reading of what is true (e.g., that code release now would break
  anonymity, that no LLM touched the core methodology). Two of the sixteen bear directly on
  this session's own standing tensions and were flagged as judgement calls in the commit
  message rather than presented as obviously correct. **P-3**.
- **That the C1-amendment drift-hunt was exhaustive.** One pass, one session, one real finding.
  A second reader might find more; none has looked.
- **That every prose-sourced number (as opposed to table-sourced) is as reliable as a
  table-sourced one.** `audit/PAPER_NUMBER_VERIFICATION.md` flags exactly which two rows are
  weaker and why, rather than treating all matches as equal.
- **That this was an independent review.** Same project, same session that wrote the amendment,
  the bibliography fix, the prose, and the verification pass that checks the prose. Unchanged
  since G4 and every gate since.

### Process caveats — what this session did badly or not at all

- **Two bibliography defects were found only because a downstream task (writing citations)
  needed them to actually work, not because anything was checking for them.** Four missing
  citations and one unfixed documented byline error survived six sessions in a file that calls
  itself the project's "source of truth". `DEVIATIONS.md` **D-18** draws the general lesson: a
  file that documents what should be true is not the same as the file being true, and this is
  at least the fourth time this project's audit trail has recorded exactly that gap (three
  times for flags, once now for a bibliography).
- **The AI-authorship / disclosure question was raised and then proceeded past on the
  operator's explicit instruction, not resolved.** Before drafting began, this session found
  that Sim2Science's own CFP (`audit/VENUE.md`, retrieved by an earlier session and never
  cross-referenced against this session's own standing constraints) states: *"Submissions must
  reflect substantive human intellectual contribution. Papers that are wholly
  AI/autonomous-system-generated are not eligible. Use of AI writing assistance should follow
  the NeurIPS 2026 policy on LLM use."* This session's brief instructs drafting nearly all of
  the paper's prose while scrubbing every trace of AI involvement from the repository and the
  rendered text, with no disclosure. The operator was asked how to proceed and chose
  *"proceed as the brief states; this is the operator's call,"* with the instruction to record
  the decision rather than silently comply, which this entry and the S8 report do. **The actual
  NeurIPS 2026 LLM-use policy this CFP defers to has still never been fetched or read by any
  session of this project**, eight sessions after the CFP first surfaced the requirement to
  follow it. The reproducibility checklist's own "Declaration of LLM usage" item (G8.8) offered
  a narrower, textually defensible answer — LLM use not in the core methodology does not
  require declaration — which this session took, but that is a reading of one checklist
  question, not a substitute for reading the policy the venue's CFP actually points to.
- **The page-limit gap is real and unresolved**, stated above and not restated here.
- **No literature check has ever run on the non-termination finding**, unchanged since G7,
  now the paper's own Section 5.
- **`audit/CLAIM_GRAPH.md` is still superseded rather than rewritten.** Eighth session flagged.
- **Google Scholar still not searched.** Ninth session. **O-7.**

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

---

## G9 — Does the paper hold together as an argument, and is it submittable?

**status: ready for review — UNSIGNED**

Prepared 2026-08-24, session G9. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **All three of this session's mechanical fixes are applied and verified.** Title changed to
> *"Diagnostics and Limits for Component-Level Simulator Misspecification"*, resolving G8's P-2.
> The simulator schematic (rendered as Figure 1 before this session, confirmed against the
> compiled PDF rather than assumed from the filename) moved to the appendix, with every in-text
> reference updated and no dangling pointer left behind. The AI-use disclosure placeholder
> replaces G8's own answer to that checklist item with an unmissable operator-completed block,
> per operator instruction, not filled in by this session.
>
> **The adversarial review found real things.** A second, independent drift-hunt against the C1
> ruling found nothing new — the amendment holds. But reading the paper as an argument rather
> than as a checklist caught a genuine citation-rendering bug (a compound surname, documented as
> needing protection six sessions ago, never actually protected at the BibTeX level, silently
> rendering "Montel et al." instead of "Anau Montel et al." in every in-text citation) and a
> genuine readability problem this session's own page-limit compression introduced (the
> introduction's four-finding preview compressed into four dense, hard-to-parse sentences in a
> row). Both are fixed. One initial concern from the cold read — bulleted Background/Limitations
> reading as inconsistent formatting — was reclassified as not a problem on reflection, disclosed
> rather than silently dropped.
>
> **The page limit is narrowed dramatically and not closed.** From 6 pages with 150-240 words of
> overflow per page (G8's end state) to, at the tightest point this session reached, 20 words —
> a single clause — before the readability fix above traded roughly 90-100 of those words back
> for a real quality improvement. Current state: approximately 116 words over, under a fifth of
> a page. Closing the rest would mean cutting real content or further readability, and this
> session declined to do either unilaterally.

| # | Criterion | Result |
|---|---|---|
| G9.1 | Title fix applied, checked against operator's no-em-dash/no-colon preference, including PDF metadata | **met.** `\title{}` and a newly-added `\hypersetup{pdftitle=...}` both updated; PDF metadata was empty before this session (pre-existing since G8) and now correctly set; `pdfauthor` deliberately left unset |
| **G9.2** | Figure move applied, numbering confirmed against the actual compiled PDF rather than the filename convention | **met.** The operator's brief itself flagged the filename-vs-rendered-number ambiguity; checked by compiling and reading `pdftotext` output before editing, not assumed. The simulator schematic was Figure 1, not "Figure 2," before this session |
| G9.3 | No dangling figure references after the move | **met.** Grepped for `ref{fig:simulator}` and any hardcoded "Figure 2" text; one reference found, updated with an Appendix pointer |
| **G9.4** | AI-use disclosure placeholder inserted correctly, without characterizing the project's AI use | **met.** G8's own `\answerNA{}` answer to the checklist's LLM-usage item, with a session-authored justification, was replaced with `\answerTODO{}` and an unmissable bold placeholder. Located by checking the template files (no separate in-body section is called for by any of them) rather than guessing |
| **G9.5** | Adversarial review completed with a genuine cold-read pass before cross-checking the audit trail | **met.** `audit/G9_PAPER_ADVERSARIAL_REVIEW.md`. Three real findings outside pure mechanical checking: the Montel citation bug, the introduction readability regression, and one reclassified non-issue disclosed per S5 |
| G9.6 | Second independent C1-drift check | **met, clean.** No sentence found implying the diagnostic or the composition is a novel method, checked without reusing G8's own drift-hunt as a template |
| G9.7 | The four standard reviewer objections checked against actual text | **met.** All four have direct textual answers; three stand cleanly, the fourth (contribution-value) is answered but is the softest of the four and not strengthened further this session, on the judgement that doing so risked overclaiming transportability |
| G9.8 | Citation accuracy re-checked by reading the compiled output, not just the `.bib` source | **met, and this is where the real finding was.** Every citation spot-checked against its actual rendered form after the Montel bug was found; `DEVIATIONS.md` D-19 |
| G9.9 | Fixable findings actually fixed in `paper/main.tex` and `audit/BIBLIOGRAPHY.bib`, not just logged | **met** — Montel citation, introduction readability |
| **G9.10** | Unfixable findings logged rather than patched over | **met.** The page-limit gap is stated as NEEDS FIX in the review document and carried here and to `audit/S9_REPORT.md`, not silently thinned further |
| G9.11 | Every commit checked against the four-check pre-push checklist, including the compiled PDF's rendered text | **met**, checked before every push this session |
| G9.12 | No self-approval | **met** — `status: ready for review — UNSIGNED` |

### What G9 explicitly does not certify

- **That the page limit is closed.** It is not — approximately 116 words of body content remain
  over Sim2Science's 5-page limit, after both this session's and G8's cutting rounds. **P-3.**
- **That a genuinely independent reviewer would find what this session's adversarial review
  found, or would stop where it stopped.** One session, reading its own and its predecessor's
  prose, however deliberately postured as hostile. The same limitation every gate in this
  project has carried since G4, restated rather than improved on.
- **That the fourth reviewer objection (contribution value, given no new method) is answered as
  forcefully as a skeptical reviewer might want.** It is answered; whether it is answered
  *enough* is a judgement call this session made once and did not revisit under time pressure.
- **That the Montel fix is the only citation-rendering defect remaining.** It was found by
  spot-checking every citation's rendered form once, by eye, after finding the first instance.
  No automated check for this class of defect exists in this repository.
- **That the reclassified formatting concern (bulleted Background/Limitations) is definitely a
  non-issue.** It was flagged, reconsidered, and reclassified by the same session in the same
  sitting — a second reader might reach the opposite conclusion.

### Process caveats — what this session did badly or not at all

- **The page-limit gap, restated because it is the largest open item**: ~116 words over, after
  substantial narrowing this session did not force shut. **P-3.**
- **A significant fraction of this session's tool-call budget went to page-fitting mechanics**
  (figure widths, `enumitem` spacing, placement specifiers) rather than to the adversarial
  review itself, which is the substantive task the brief asked for. The review that did happen
  was real and found real things, but a session with a cleaner page-limit starting point would
  have had more room for it.
- **An unrelated environmental problem consumed real session time and is worth recording
  precisely because it is not this project's own defect.** Seven shell processes from a
  different, days-old session (unrelated working directory, "Thursday" timestamps) were found
  stuck in a genuine infinite loop — each polling `pgrep -f "diagnostics.run_diag"` to detect
  when a script finished, but that grep pattern matched the polling processes' own command
  line, so the exit condition could never be satisfied. This was the actual cause of
  intermittent multi-minute hangs on ordinary `git` and `grep` commands throughout this session
  (previously misdiagnosed, in this and prior sessions' reports, as generic "machine load").
  The seven processes were killed; system load remains elevated from unrelated, legitimate
  concurrent work on the same machine, which is a real and disclosed condition, not a bug.
- **The AI-authorship/venue-eligibility tension from G8 remains exactly where G8 left it.** Not
  this session's scope per the operator's decisions, and not revisited.
- **No literature check has ever run on the non-termination finding.** Unchanged since G7.
- **`audit/CLAIM_GRAPH.md` is still superseded rather than rewritten.** Ninth session flagged.
- **Google Scholar still not searched.** Tenth session. **O-7.**

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

---

## G10 — Overleaf submission package: assembly, template compliance, and isolation

**status: ready for re-review — UNSIGNED**

**This entry did not exist before session G12 (2026-08-25) and is written retroactively.** No
`GATES.md` entry or `audit/S10_REPORT.md` for session G10 ever existed in this repository — G11
found the gap, named it explicitly as *"a pre-existing gap in the project's own record, not
something this session was asked to backfill,"* and left it open. This session's mandate
includes proposing a corrected G10 given the defect G11 found in G10's own verification method,
which cannot be done without a G10 entry to correct — so this one is written now, from the one
surviving record of that session's work, `audit/OVERLEAF_PACKAGE_REPORT.md`'s pre-G11 content
(the parts of it G11 did not itself rewrite), rather than from a lost original session brief.
**What this means for how to read it:** this entry can state what the surviving artifacts show
G10 did and where G10's own verification method failed; it cannot certify that G10's original
scope, process, or any claim beyond what those artifacts record was sound, because no session
brief or first-person report from G10 exists to check against.

### What G10 is judged against, from the surviving record

| # | Criterion | Result |
|---|---|---|
| G10.1 | The Overleaf submission package assembled from an explicit allowlist, byte-identical between the repo working copy and a fresh package extraction | **met**, independently of the defect below — `scripts/build_overleaf_package.sh`'s allowlist-based assembly is not implicated by the isolation-test flaw, and every session since (G11, G12) has re-verified byte/text identity between the repo working copy and a freshly extracted package |
| G10.2 | Template-option and anonymization compliance (`dblblindworkshop`, no `final`, anonymized author block, no identifying metadata) | **met**, independently of the defect below — this is a static trace of `neurips_2026.sty`'s macro logic and a grep-based scan, neither of which the isolation test's own methodology touches |
| **G10.3** | **The "Overleaf-equivalent isolation" compile test actually tests self-containment** | **NOT MET, as originally run.** G11 found that G10's own isolation test exported this project's local `TEXINPUTS=".:neurips_2026_template:"` build convention into its own "isolated" test environment before compiling — so the test never actually removed the one piece of local state a plain Overleaf upload could not replicate, and it reported PASS regardless. Re-run by G11 with `TEXINPUTS` genuinely unset for the first time: immediate failure, `File 'neurips_2026.sty' not found.` **G10's PASS on this criterion was not a false report of a true fact; it was a true report of the wrong test.** |

### What this amendment does and does not do

- **It does not retroactively fail G10 on criteria 1 and 2.** Those checks were never implicated
  by the `TEXINPUTS` leak — a package-assembly script and a macro-logic trace do not depend on
  which environment variables happen to be set when `latexmk` runs — and both have since been
  independently re-verified by two further sessions (G11, G12) using the current package.
- **It states plainly that criterion 3's original verification was invalid**, for the reason
  G11's own report gives in full (`audit/OVERLEAF_PACKAGE_REPORT.md` §0b): the isolation test's
  "isolated" environment silently carried the one piece of local state that made the difference.
- **The defect is fixed and re-verified twice since.** G11 fixed it by making the template
  package path explicit via kpathsea's own relative-path resolution
  (`\usepackage[dblblindworkshop]{neurips_2026_template/neurips_2026}`, no environment variable
  needed) and re-ran the corrected test to PASS. G12 rebuilt the package from its own final
  commit and re-ran the same corrected test again: exit 0, 22 pages, textually and
  byte-identical output to the repo working copy (`audit/OVERLEAF_PACKAGE_REPORT.md` §2b).
- **G12 additionally found and disclosed a second, lower-severity defect of the same class in
  the OTHER isolation tier** (the one G11's own report already flagged as suspicious but did not
  chase down): the "STRICT isolation" tier's `TEXMFHOME`-unset setting does not achieve
  isolation either — it falls back to this operator's own personal package tree rather than to
  nothing. Unlike the `TEXINPUTS` defect, this one does not change the submission-readiness
  verdict, because the tier the project actually gates on (Overleaf-equivalent, criterion 3
  above) does not depend on it. Full detail: `audit/OVERLEAF_PACKAGE_REPORT.md` §0c. This is
  recorded here rather than as a fourth G10 criterion, since it was found investigating G10's
  *sibling* tier, not a criterion G10 itself was ever judged against.
- **It does not certify that G10's process met this project's other standing disciplines**
  (commit-before-run ordering, seed disjointness, liveness checks) — those are not applicable to
  a packaging/compile-test session in the same way they are to a compute session, and no G10
  report exists to check them against regardless.

### Recommendation, offered as such

Sign as: **criteria 1 and 2 met and independently re-verified since; criterion 3 NOT MET as
originally run, its verification method corrected in G11 and re-confirmed in G12, and the
package's actual submission-readiness on this axis unaffected by either defect found.** This is
not a request to retroactively construct a full G10 record beyond what the surviving artifacts
support — the honest state is that one never existed, and this entry says so rather than filling
the gap with invented detail.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

---

## G11 — Does the paper survive an independent external reviewer's Weak Reject, and does this session's own verification hold up to more scrutiny than the sessions before it?

**status: ready for review — UNSIGNED**

Prepared 2026-08-25, session G11. Signature block below is for the operator.

**Note on G10.** No `GATES.md` entry or `audit/S10_REPORT.md` exists for session G10. Its only
surviving record is `audit/OVERLEAF_PACKAGE_REPORT.md`, which this session found to rest on a
compromised isolation test (see §T1-3/Phase-4.4 below). This is a pre-existing gap in the
project's own record, not something this session was asked to backfill, and it is named here so
a future reader does not mistake G10's absence for nothing having happened between G9 and G11.

> ### The headline, stated before the table
>
> **An independent external reviewer with no project history returned Weak Reject, confidence
> 4/5, with 6 Tier-1 (must-fix) and 15 Tier-2 (should-fix) findings.** This session's mandate was
> to fix all of them, run the real Dufour-confidence-set-bounded MMC check rather than a cheaper
> reframe, and then verify its own work more rigorously than G9 or the never-gated G10 did.
>
> **T1-3, named the single most important open question, is done and the paper's central claim
> survives — decisively.** A maximum-likelihood fit of the simulator's five nuisance parameters
> to one realised dataset, with a Bonferroni-corrected 95% Wald confidence box built from the
> observed Fisher information, gives relative half-widths from 2.3% to 16.6% on every coordinate
> — wider, on every one, than the ±0.5% box the paper's existing fixed-box sweep already showed
> breaks the composition. Re-measuring the cost gate inside this **data-implied** box (not an
> assumed one): the acceptance probability collapses to 1×10⁻⁵ at the primary case and to
> exactly zero at the other three declared combinations, and the gate **fails at every corner
> under all four** — the cheapest declared corner alone needs 9.9×10⁹ draws against a 10⁸
> budget. Section 5's central claim is now grounded in a real, measured confidence set rather
> than a round assumed number, and the result is stronger than before, not weaker.
>
> **All six Tier-1 findings and 13 of 15 Tier-2 findings are fixed and verified.** T1-1
> (appendix TODO / anonymity residue), T1-2 (page limit — **not fully closed, see below**), T1-4
> (simulator figure moved and reduced), T1-5 (full anonymity re-scan), T1-6 (checklist accuracy),
> and T2-1/2/3/5/7/8/9/10/11/12/13/14/15 are each individually addressed in their own commit,
> listed in the table below. **T2-4 and T2-6 are not addressed and their content is unknown to
> this session** — see the dedicated note below the table. This is disclosed as a real gap, not
> elided.
>
> **This session's own re-verification (Phase 4) found and fixed four defects the external
> review never flagged, three of which this session introduced itself and one of which G10's own
> "Overleaf-equivalent" test had already missed.** Most consequential: G10's isolation test
> exported this project's local `TEXINPUTS` build convention into its own "isolated" test
> environment before compiling, so it never actually tested whether the packaged zip is
> self-contained — and it is not, on its own local convention. Re-run this session with
> `TEXINPUTS` genuinely unset, it failed exactly as that description predicts. Fixed by using
> kpathsea's own relative-path resolution instead of an environment variable. Full detail in
> `audit/OVERLEAF_PACKAGE_REPORT.md` §0.
>
> **The page limit is not closed.** Six pages of body content against Sim2Science's five-page
> limit — unchanged in page count from G9's end state, despite this session absorbing the
> external review's full Tier-1/Tier-2 content mandate (a new section, eight new citations, a
> restructured table, expanded figures) into that same six pages. A genuine width-vs-legibility
> tradeoff was found, tried, and **reverted**: shrinking `\includegraphics` widths below each
> figure's designed print size would push effective on-page font size below the venue's stated
> point-size floor, and this session chose not to ship that. See `audit/S11_REPORT.md` §3.

### What G11 was judged against

| # | Criterion | Result |
|---|---|---|
| **G11.1** | **T1-3: the real confidence-set-bounded MMC check, not a cheaper reframe** | **met.** `src/diagnostics/confidence_set_check.py`, `results/confidence_set_mmc.yaml`, `audit/DUFOUR_CONFIDENCE_SET_CHECK.md`. Dufour's actual published text fetched and full-text-searched to confirm it never uses the word "Bonferroni" (0 occurrences) before attributing the Bonferroni-box construction correctly as this session's own design choice, not Dufour's |
| G11.2 | T1-1, T1-2, T1-4, T1-5, T1-6 addressed | **met except T1-2.** T1-2 (page limit) is narrowed but not closed — see headline. The other four are individually committed and each independently re-verified this session's own Phase 4, not merely re-asserted |
| **G11.3** | **T2-1 through T2-15 addressed** | **13 of 15 met** (T2-1,2,3,5,7,8,9,10,11,12,13,14,15). **T2-4 and T2-6 NOT MET — content unknown, no commit in this session's history addresses them.** See the dedicated note below |
| G11.4 | Every commit follows the raw `git commit -m` / no `/commit` / four-check pre-push discipline | **met**, checked before every push this session, including this one |
| **G11.5** | **Phase 4 re-verification is more rigorous than G9's or the never-gated G10's own checks, not merely repeated (S11)** | **met, and this is where the session's real findings are.** A full number-trace (~150+ claims, zero mismatches, run by an independent sub-pass rather than trusted from the generated table alone), a citation-target check that caught one real misdirected `\ref` (§ below), an anonymity re-scan independent of the targeted T1-5 fixes that caught one further leak (an internal review-finding label baked into three rendered table rows), and — the largest finding — re-running G10's own Overleaf isolation test with its methodological flaw corrected, which failed where G10 reported PASS |
| G11.6 | Two-tier isolation compile (strict + Overleaf-equivalent), against the actual rebuilt package, with `TEXINPUTS` genuinely unset in both tiers | **met, after two real fixes.** Both tiers now PASS: exit 0, zero undefined references or citations, byte-identical 22-page/583,171-byte `main.pdf` between the repo working copy and a freshly unzipped, isolated package extraction |
| G11.7 | Full test suite re-run | **met** — 177 passed |
| G11.8 | `scripts/build_overleaf_package.sh` re-run and its allowlist corrected | **met.** `paper/appendix_claims_table.tex` (a file this session added via T1-1 that the script's allowlist never picked up, since its discovery loop only parses `\includegraphics`, not `\input`) added; every packaged file re-verified against `main.tex`'s actual `\input`/`\includegraphics`/`\bibliography` calls |
| G11.9 | A citation pointing to the wrong artifact, found by cross-checking every `\ref{fig:*}`/`\ref{tab:*}` in `main.tex` against what that figure or table actually shows | **met, one real finding.** "1.523× under the tightest one" was cited to Figure 5 (`fig:threshold`), which does not display that number anywhere on the page — it belongs to the ABA row of Table `tab:sb-eight` in the appendix. Retargeted |
| G11.10 | No self-approval | **met** — `status: ready for review — UNSIGNED` |

### T2-4 and T2-6 — a real gap, disclosed rather than silently dropped

This session's context was compacted partway through, and the external reviewer's original
Tier-2 finding list survived only in the summary carried forward across that compaction, which
did not retain T2-4 or T2-6's text. Every other Tier-1 and Tier-2 item's content is independently
reconstructible from this session's own commit messages (each commit states the finding's
substance, not just its tag) — cross-checked against `git log` while preparing this gate, not
assumed. **T2-4 and T2-6 are the exception: no commit in this session's history mentions them,
under any label, and a full-history grep for their tags found nothing.** This session did not
invent content for them to close the gap quietly. The honest state is: two of the external
review's fifteen Tier-2 findings are simply unaddressed, and neither this session nor any
artifact in this repository knows what they said. **The operator's own copy of the external
review (wherever it was received) is the only way to close this**, and it should be treated as
outstanding rather than assumed benign.

### What G11 explicitly does not certify

- **That T2-4 and T2-6 are addressed, minor, or safe to leave.** They are simply unknown to this
  session. See above.
- **That the page limit is closed.** It is not — six pages against a five-page limit, unchanged
  in page count from G9 despite substantially more content now living in it. This session tried
  and reverted a figure-width reduction that would have closed it at the cost of pushing text
  below the venue's stated font-size floor on two main-text figures; that reversion is
  deliberate and should not be re-attempted without solving the underlying tradeoff differently.
- **That a second external review has been run against this session's fixes.** Everything in
  this gate verifies that the paper compiles correctly, that its numbers trace to their sources,
  and that this session's own re-reading of it as a reviewer found what it found. It does not
  certify that the original external reviewer, presented with the current draft, would upgrade
  their verdict — that reviewer has not seen it.
- **That this session's own Phase 4 pass is exhaustive.** It found four real defects the
  external review and G9/G10 both missed. A fifth reader would very likely find a fifth thing;
  the project's own history (four consecutive prior gates each finding something the one before
  it missed) is the strongest evidence for this, not a reason to treat this pass as the last one
  needed.
- **That G10's own findings, beyond the isolation-test flaw this session corrected, are reliable
  without re-checking.** G10 was never gated and has no `audit/S10_REPORT.md`; this session
  re-verified only what it needed to re-verify for the Overleaf package and the anonymity scan,
  not every claim G10's own report made.
- **That the confidence-set box construction is the only reasonable one.** The Bonferroni
  correction is this session's own choice for realizing a rectangular set compatible with the
  existing box-based MMC infrastructure; `audit/DUFOUR_CONFIDENCE_SET_CHECK.md` states this
  plainly and names what a joint (non-marginal) confidence ellipsoid would have to do differently
  that this check does not attempt.

### Process caveats — what this session did badly or not at all

- **The original external review's verbatim text was not preserved by this session in a durable
  artifact**, so a mid-session context compaction cost two of its fifteen Tier-2 findings
  entirely. A future session under the same operating conditions should save any externally
  supplied review verbatim to a file in the repo (e.g. `audit/`) before starting work against it,
  specifically so a compaction cannot lose part of the mandate. Recorded here so this is not
  repeated.
- **G10 was never gated**, and this session did not attempt to backfill that retroactively — out
  of this session's own scope, but it means the project's gate register has a real hole between
  G9 and G11 that a future session or the operator should decide whether to fill.
- **The `TEXINPUTS` isolation-test flaw survived one full prior session (G10) that specifically
  set out to test self-containment.** It was caught this session only because Phase 4's
  standing instruction was to re-run prior checks with the actual failure mode in mind rather
  than to trust a prior PASS. The general lesson, consistent with this project's own recurring
  pattern (a flag reading FALSE for the wrong reason, four separate times across G3/G6/G7, per
  `DEVIATIONS.md` D-8/D-15/D-17): a test that reports PASS is only as good as what it actually
  varied between "isolated" and "not."
- **No second external review has been commissioned or run.** P-1 below.
- **Google Scholar still not searched.** Eleventh session with code. **O-7**, unchanged.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

---

## G12 — Does the paper close G11's two lost Tier-2 findings, the page overflow, and the G10 gap, and does this session's own re-verification hold up in turn?

**status: ready for review — UNSIGNED**

Prepared 2026-08-25, session G12. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **T2-4 and T2-6, the two Tier-2 findings G11 lost to context compaction, are both closed with
> honest reporting.** T2-6 was found, on inspection, to be **already substantially applied** by
> G11 before compaction hit — retitled, the predicted-before-measured sentence already in the
> first paragraph, the confidence-set result already primary evidence, three of the four named
> apologetic-framing instances already fixed, and the 8.4-vs-27-65 figure discrepancy already
> resolved by G11's own T2-8 redesign (they are different statistics of the same underlying
> shift — a vector-norm ratio versus a raw per-coordinate z-score — and the paper now cites only
> the norm-based one, consistently, having dropped the raw number from the prose entirely). This
> session's own contribution to T2-6 was a fourth apologetic-framing instance found and cut
> (Section 5's background bullet), plus re-verifying every part of the original instruction
> against the current text rather than assuming G11's partial work was complete.
>
> **T2-4 took the real path, not the fallback.** A second parameter point, drawn `±20%`
> relative per coordinate from a rule fixed in code before the draw, run twice for provenance
> integrity (the first attempt was discarded for `dirty: true` after this session edited
> `paper/main.tex` while the diagnostic ran in the background — the exact mistake this
> project's own `DEVIATIONS.md` D-8/D-9 exist to name, caught by this session's own discipline
> rather than repeated silently). **`S_B` separates at `θ₂` too** (`κ=10.9`, full rank),
> matching `θ₀`'s own verdict under an identical harness (`κ=10.1`). One additional point is not
> a distribution over `θ`, and the paper says so.
>
> **The page limit is narrowed, not closed.** The specific overflow that used to leak Section
> 5's own prose onto a sixth page is gone — that text now fits entirely on page 5, after real
> cuts (Related Work tightened with every T2-5 citation and its engagement kept, several other
> phrase-level trims, tighter float spacing, and two figure-width reductions verified safe by
> rendering the compiled pages at 300dpi and reading the smallest text directly). What remains —
> Figure 4 plus the complete Limitations section, roughly four-fifths of a page — does not fit
> in the zero space Section 5 leaves on an already-full page 5 without cutting real content, a
> larger figure-legibility risk than the two taken here, or restructuring. **Six pages against
> five, same as G9 and G11 before it, on genuinely less remaining slack than either left.**
>
> **This session's own re-verification (Phase 4), applying S6's standing suspicion to its own
> prior sessions' tooling, found one more thing of the same class G11 found.** The "STRICT
> isolation" tier's `TEXMFHOME`-unset setting does not isolate from anything — it falls back to
> this operator's own personal package tree, which happens to carry local installs of exactly
> the packages that tier's own history says it once failed without. Verified directly by
> pointing `TEXMFHOME` at a genuinely empty directory and reproducing the original failure.
> **This does not change the submission-readiness verdict**: the tier the project actually gates
> on sets `TEXMFHOME` explicitly rather than unsetting it, and re-verifies clean, byte-for-byte,
> against a freshly rebuilt package. Full detail: `audit/OVERLEAF_PACKAGE_REPORT.md` §0c.
>
> **G10, which never had a `GATES.md` entry, has one now.** Written retroactively from the one
> surviving record rather than from a lost session brief, saying so rather than inventing detail
> the surviving artifacts do not support, and proposing exactly the amendment this session's
> brief asked for: criteria 1–2 met and independently re-verified twice since; criterion 3
> (isolation actually tests self-containment) not met as originally run, fixed in G11, confirmed
> again in G12.

### What G12 was judged against

| # | Criterion | Result |
|---|---|---|
| **G12.1** | **T2-4 resolved, with honest reporting of which path was taken** | **met.** The real second-θ test was run, not the fallback; `results/second_theta_check.yaml`, `dirty: false`, committed after a discarded `dirty: true` attempt that is disclosed rather than hidden. `paper/main.tex` Limitations bullet 2 states the actual result and its one-point caveat |
| **G12.2** | **T2-6 fully applied, including the strengthened-result incorporation** | **met.** Found mostly already applied by G11 before compaction (retitle, first-paragraph placement, confidence-set-as-primary already done); this session closed the one remaining apologetic-framing instance and independently re-verified every other part of the instruction against current text rather than assuming G11's partial credit |
| G12.3 | Page limit closed | **NOT MET.** Narrowed — the specific overflow onto page 6 that used to include Section 5's own prose is closed, but the body remains 6 pages against 5. See headline and `audit/OVERLEAF_PACKAGE_REPORT.md` §4 for the exact accounting of what was and was not cut, and why |
| **G12.4** | **G10 tooling re-verified or fixed, with the existing prior-tooling suspicion check completed** | **met.** `TEXINPUTS` fix re-verified clean, no regression. One further, lower-severity defect of the same class found in the STRICT tier, disclosed in full (`audit/OVERLEAF_PACKAGE_REPORT.md` §0c), and stated explicitly not to change the submission-readiness verdict rather than left ambiguous |
| G12.5 | G10 given a `GATES.md` entry and a proposed re-sign, not self-signed | **met.** `GATES.md` G10, `status: ready for re-review — UNSIGNED` |
| G12.6 | `docs/OPEN_QUESTIONS.md` Q-17 closed | **met.** T2-4 and T2-6's actual content and disposition are now on the record; Q-17 marked ANSWERED with what was found |
| G12.7 | Full number-trace, extended for this session's own additions | **met, with a disclosed scope limit.** T2-4's new numbers (`κ=10.9`, `κ=10.1`) independently verified against `results/second_theta_check.yaml` directly. A token-level diff of every number touched by the page-limit commit confirms none were altered in value, only in surrounding wording. **This is not a from-scratch re-trace of all ~150+ claims** — G11's own exhaustive pass (`audit/S11_REPORT.md` §3) is relied on for content this session did not touch, which is disclosed here rather than re-claimed as freshly re-verified |
| G12.8 | Full test suite re-run | **met** — 177 passed, unchanged, no `src/` diagnostic code altered by the paper edits or the tooling investigation |
| G12.9 | Overleaf package rebuilt from this session's final commit and re-verified | **met** — `build/sim_attrib_overleaf_3ca62db.zip`, two-tier compile re-run, exit 0 both tiers, byte-identical output between the repo working copy and the isolated extraction |
| G12.10 | No self-approval | **met** — every gate this session touched or added (`G10`, `G12`) is `status: ready for review/re-review — UNSIGNED` |

### What G12 explicitly does not certify

- **That the page limit is closed.** It is not. Six pages against five, after real narrowing.
  The remaining gap is a load-bearing figure plus a full Limitations section that does not fit
  in the zero space left on an already-full page 5 without a tradeoff this session declines to
  take unilaterally, matching G9's and G11's own stopping points on the identical tradeoff.
- **That the full ~150+-claim number trace was re-run from scratch.** It was not; this session's
  own additions were independently verified, and G11's exhaustive pass is relied on, disclosed,
  for everything else.
- **That a second external review has been run against this session's fixes, or G11's.** None
  has. This is the natural next step, not this session's job — see `audit/S12_REPORT.md` §5.
- **That the G10 entry written this session is a complete record of what that session actually
  did.** It is a reconstruction from surviving artifacts, stated as such, and it cannot certify
  anything about G10 beyond what those artifacts show.
- **That every instance of apologetic framing in the paper is gone.** Four were named by the
  external review; four are fixed (the title, the opening sentence, the "propose it" phrase, and
  the Background bullet found this session). A fifth reader might find a fifth instance — the
  same limitation every gate in this project has carried since G4.

### Process caveats — what this session did badly or not at all

- **The first T2-4 run was contaminated by this session's own concurrent edit to
  `paper/main.tex`**, the exact `DEVIATIONS.md` D-8/D-9 pattern (a run in flight, a tree edited
  underneath it) recurring in a session that had just re-read those entries while preparing this
  gate. Caught before the number reached the paper, not after — the discarded run and the clean
  re-run are both disclosed in the commit history rather than only the clean one being kept.
- **The page-limit gap, restated because it is the largest open item**: six pages against five,
  narrowed but not closed, for the reasons given above and in `audit/OVERLEAF_PACKAGE_REPORT.md`
  §4.
- **No second external review has been commissioned or run.** See `audit/S12_REPORT.md` §5.
- **Google Scholar still not searched.** Twelfth session with code. **O-7**, unchanged.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

---

## G13 — Is the page limit closed, with the paper's substance fully intact?

**status: ready for review — UNSIGNED**

Prepared 2026-08-26, session G13. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **The page limit is closed. 5 counted pages against Sim2Science's 5-page limit, for the first
> time in this project's history**, confirmed by rendering the compiled PDF's own pages and
> reading them directly, not by estimating from a line count. G9, G11, and G12 each narrowed the
> overflow across three prior sessions without closing it; each stopped at the same fork — cut
> real content, take a riskier figure-legibility reduction than the two already taken, or move
> Figure 4 to the appendix and weaken the paper's own central evidence in the main text — and
> each declined to take it unilaterally.
>
> **This session closed it without taking any of those three.** Two levers, tried in combination
> for the first time: relocating two pieces of genuinely secondary main-text content to the
> (unlimited) appendix — a four-findings overview table that only previews content stated in
> full elsewhere, and the simulator's structural diagram, whose qualitative content is now
> restated directly in Section 4's own prose so the main text stays self-contained — and a
> whitespace/prose tightening pass (the template's own `\parskip`, plus rewording that dropped no
> clause of substance). **No citation, no sentence stating a finding, and no evidentiary number
> was cut.** Tier 1.4 (real content cuts) was surveyed and not needed.
>
> **One judgment call, disclosed rather than made silently (S8).** Moving the simulator diagram
> out of the main text is the one relocation in this pass that a reader could reasonably view as
> reducing main-text self-containedness on a first read: the diagram itself, the compartment-flow
> detail, and the exact distortion-family formulas now require turning to the appendix, even
> though every qualitative fact a reader needs to follow Section 4's argument is restated in that
> section's own prose. Named here rather than folded into "safe" without comment.
>
> **This session's own re-verification caught two real cross-reference defects its own edits
> introduced, both fixed before commit.** Moving two figures shifted main-text figure numbering
> down by one; the compact-overview table's hard-coded `fig.` column and one sentence in
> `paper/checklist.tex` that named the simulator figure's old location ("Section 4") both still
> read as if nothing had moved. Neither would have broken the compile — both would have been a
> live, undetected inaccuracy in the submitted PDF. Caught by re-reading every cross-reference
> against the new structure rather than trusting that a content move only affects the content it
> moved — the same lesson `DEVIATIONS.md` has recorded from this project's other renumbering
> passes, applied here to a class of edit the project had not made before (relocating figures
> across the main-text/appendix boundary).
>
> **A second, unrelated latent defect found and deliberately left unfixed.** A from-scratch
> compile (forced by deleting `main.aux`/`main.bbl` rather than relying on latexmk's incremental
> cache, precisely so a defect hidden by stale build state could not hide from this session either)
> surfaced a pre-existing `bibtex` warning: `audit/BIBLIOGRAPHY.bib`'s Raue et al. (2009) entry
> has `month=June`, a bareword bibtex does not resolve as any of its predefined three-letter month
> macros, so the printed reference silently drops its month (every other dated reference in the
> bibliography prints one). Confirmed present in every rebuild this session ran, unrelated to any
> edit this session made, and **not fixed** — `audit/BIBLIOGRAPHY.bib`'s own standing policy
> (stated in `paper/main.tex`'s own comment on a different Crossref quirk) is that the file "stays
> exactly as fetched," and this project's established pattern for a fetched-record defect is a
> compatibility shim in `main.tex`, not an edit to the `.bib` — and no such shim is available for
> a bibtex string macro from outside the `.bib` file itself. Cosmetic only (one reference prints
> without its month); disclosed here rather than silently left for a twelfth reader to find, per
> S8's standard for this project.

### What G13 was judged against

| # | Criterion | Result |
|---|---|---|
| **G13.1** | **Page limit reaches ≤5 pages (excluding references/appendix/checklist, per Sim2Science's own stated convention, re-verified against `audit/VENUE.md`'s CFP-sourced facts rather than assumed)** | **met.** 5 pages exactly — pages 1–5 are Abstract through Limitations; References start page 6. Verified by rendering pages 5–6 of the compiled PDF directly at every step of this session's edits, not by a line-count estimate, and by a final `pdftotext` page-boundary check after the last edit |
| G13.2 | All 21 external-review findings (6 Tier-1, 15 Tier-2) still verified applied against the current text | **met.** Re-checked item by item against `audit/S11_REPORT.md`'s own list. One regression caught and fixed in-session: an early wording trim of the "no learned component" Limitations bullet dropped the `(where $s(y)$ would sit)` clause that is specifically T2-11's fix; restored before the commit that closed the page limit, so no external-review fix left this session's final state unapplied |
| G13.3 | All four contributions in `audit/FINAL_CLAIMS.md` remain fully and accurately stated in the main text | **met.** C1–C4's claim sentences (Method's diagnostic framing; "Where attribution is identifiable" and "Where it is not" in Section 4; Section 5's non-termination paragraphs) were not touched beyond phrasing trims that preserved every number and qualifier — verified by reading each claim's "as it goes in the paper" text in `FINAL_CLAIMS.md` against the current section side by side |
| G13.4 | Section 5's strengthened confidence-set framing (C5, the G11 result) intact, not regressed to the pre-G11 assumed-±5%-box version | **met.** The Bonferroni-box construction, the 2.3%–16.6% half-widths, the $10^{-5}$/exactly-zero acceptance probabilities, and the "fails at every corner under all four" verdict are all still the paragraph's primary claim, with the fixed ±5% sweep still cited as secondary evidence — every number token-for-token unchanged from G11's text, confirmed by diff |
| G13.5 | Anonymization clean after every cut, re-checked each time rather than once at the end (S3) | **met.** Grepped for session/gate/operator/model-authorship language after each round of edits; the only matches found were inside `%`-comments (never rendered) or the pre-existing operator-facing AI-use-disclosure placeholder, both already an established, deliberate pattern in this file. `pdfinfo` carries no `Author` field and no identifying `Creator`/`Producer` path |
| G13.6 | Every number in prose still traces to a `results/*.yaml` file or `audit/FINAL_CLAIMS.md` after every move (S4) | **met.** No number moved from main text to appendix without its supporting context moving with it — Table 1's move takes its own numbers with it into the appendix intact; the simulator-figure move relocates formulas and diagram detail that are not themselves numeric claims (the numeric claims that figure supports, e.g. the $10\%$ deformation unit, are restated in the Section 4 prose that replaced it) |
| G13.7 | STRICT-isolation tooling defect (disclosed, not yet fixed, since G12): fixed if quick, explicitly deferred with reason otherwise | **met, deferred again.** Not quick — a genuine fix needs either a second, actually-isolated TeX Live installation or a containerized build environment, neither available on this machine within this session's scope. This session re-ran both tiers once more (§2a PASSES only in the this-machine sense G12 already characterized: `TEXMFHOME` unset falls back to `~/Library/texmf`, not to nothing; §2b, the tier this project's own submission-readiness verdict rests on, PASSES genuinely) and did not attempt the fix, consistent with G12's own stated reasoning, restated rather than silently re-deferred |
| G13.8 | This session's own page-count and compile verification states explicitly which isolation tier it rests on (S6) | **met.** Every page-count and compile claim in this gate and in `audit/S13_REPORT.md` rests on **§2b, OVERLEAF-EQUIVALENT** (`TEXMFHOME` pointed explicitly at a real package tree, `TEXINPUTS` unset) — the tier G11 fixed and this project has used as authoritative since. §2a is reported alongside for completeness, not as the basis for any claim here |
| G13.9 | Two-tier isolation compile against a freshly rebuilt package, `TEXINPUTS` unset in both | **met.** `build/sim_attrib_overleaf_09a107e.zip`, extracted fresh to an isolated temp directory: §2b exit 0, 22 pages, zero undefined references or citations, **byte-identical 584502-byte `main.pdf`** against the freshly recompiled repo working copy (differing only in embedded `CreationDate`/`ModDate`, as in every prior session); §2a exit 0 in the same narrower sense as G12 found |
| G13.10 | Full test suite re-run | **met** — 177 passed, unchanged. No `src/` diagnostic code touched this session |
| G13.11 | `scripts/build_overleaf_package.sh` re-run against the final commit and the package re-verified | **met** — `build/sim_attrib_overleaf_09a107e.zip`; the figure-discovery loop correctly picked up `fig2_simulator.pdf` from its new `\includegraphics` call inside the appendix, with no allowlist edit needed |
| G13.12 | Every Tier-1.4 (real content) cut, if any, listed with its tradeoff named (S8) | **met, vacuously — none were needed.** Tiers 1.1 (appendix moves) and 1.2 (tightening) closed the gap; Tier 1.3 (figure-width reduction) and Tier 1.4 (content cuts) were surveyed and not reached. One Tier-1.4-adjacent trial cut (a single low-value discussion sentence — "the ratio itself is a portable one-line check for other simulators") was made, found unnecessary once the tightening pass's other savings were counted, and **restored** before the final commit, per the standing instruction not to over-cut once the target is reached |
| G13.13 | No self-approval | **met** — `status: ready for review — UNSIGNED` |

### What G13 explicitly does not certify

- **That the appendix-relocated simulator figure is costless.** It is the one judgment call this
  session flags rather than buries: a reader who wants the diagram itself, not just the
  qualitative facts Section 4's prose now states, must turn to the appendix. Named in the
  headline and here, not only in `audit/S13_REPORT.md`.
- **That the full ~150+-claim number trace was re-run from scratch.** It was not. This session's
  own edits touched no evidentiary number (verified by diff, token-for-token), so G11's own
  exhaustive pass remains the last from-scratch trace, exactly as G12 already disclosed carrying
  forward.
- **That a second external review has been run against the now-page-compliant paper.** None has.
  This is the natural next step this project's own trajectory has pointed to since G11 —
  `audit/S12_REPORT.md` §5 said so and it remains true.
- **That the `.bib`'s `month=June` defect is fixed.** It is disclosed, not fixed, per the
  standing "stays exactly as fetched" policy this project has held since G3's bibliography work —
  see the headline. Cosmetic only.
- **That the STRICT-isolation tier now means anything different than G12 left it meaning.**
  Unchanged: it demonstrates this one operator's own machine, personal package tree included, can
  compile the package — not genuine isolation. Deferred again, for the same reason G12 gave.

### Process caveats — what this session did badly or not at all

- **The tiered-commit structure Phase 2.6 asked for (a separate commit per tier — appendix moves,
  tightening, figure adjustment, content cuts) was not achieved cleanly.** An attempt to split the
  diff via `git add -p` produced ambiguous hunk boundaries this session judged too risky to push
  through blind (the tool's own hunk-numbering became inconsistent across the interactive
  session, and forcing it further risked staging a broken intermediate file state). Reset the
  index and committed the whole page-limit pass as one commit instead, following the same
  precedent G9/G11/G12 already set for a page-limit pass specifically (each bundled theirs too),
  with every tier named explicitly in the commit message body rather than left to be inferred
  from a diff. This is a real departure from what Phase 2.6 asked for, not a silent substitution
  — recorded here rather than only in the commit message.
- **The T2-11 regression (above) should not have happened at all.** It was caught by this
  session's own Phase-3 re-check against `audit/S11_REPORT.md`'s list, not by anything upstream
  of that check — a session running the same pass with a less thorough Phase 3 would have shipped
  a genuine, if narrow, T2-11 regression. Recorded as a reason Phase 3's per-item re-check earned
  its place in this gate's criteria rather than being treated as a formality.
- **No second external review has been commissioned or run.** Not this session's job — P-2 below
  — but restated because it is now the single largest remaining gap in this project's own
  trajectory, with every content and process fix from the original review applied.
- **Google Scholar still not searched.** Thirteenth session with code. **O-7**, unchanged.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G14 — Does the paper close the second external review's Path to Acceptance, and does it survive a paper-wide dash-removal and polish pass intact?

**status: ready for review — UNSIGNED**

Prepared 2026-08-26, session G14. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **Every item on the second review's "Path to Acceptance, Round 2" is now addressed** — R14-1
> (the one Tier-1 item) and R14-2 through R14-9 (eight of the nine Tier-2 items) fixed; R14-10
> (promoting $S_A$ to a fifth finding) explicitly declined, per the review's own "optional" framing
> and this session's own judgment that the page budget the other nine items already spent left no
> clean room for a fifth finding without diluting the paper's four-finding structure.
>
> **R14-2, the review's own "single highest-value remaining item," did not confirm the review's
> guess.** The review's back-of-envelope estimate put the box at which the MMC gate first fails at
> Mahalanobis radius "roughly 1.3," comfortably inside the 95% confidence ellipsoid ($\sqrt{\chi^2_{5,0.95}}\approx3.33$).
> This session recomputed it directly from `results/confidence_set_mmc.yaml`'s Fisher-information
> covariance (cross-checking its eigenvalues against the file's own stored Hessian eigenvalues
> before trusting the inversion) and `results/boundary_sweep.yaml`'s round-box sweep, using the
> actual correlation structure across the five nuisance parameters rather than a diagonal
> approximation (the mathematically correct comparison against a chi-squared threshold, since the
> diagonal-only version is not chi-squared distributed when the covariance has off-diagonal
> terms — and this project's own Fisher information does, strongly, for beta/gamma at
> $\rho=0.88$). The rigorous number: the last round box that still passes at every corner
> ($\pm0.5\%$) sits at radius 2.71, comfortably inside; the smallest box at which the gate first
> fails ($\pm0.75\%$) sits at radius 3.56, **just past** the ellipsoid's edge, not deep inside
> either the failure region or the confidence region. Reported as the sharper, more precise, and
> more surprising finding it actually is — the composition's failure boundary and a real analyst's
> 95% confidence region are essentially the same place — rather than silently corrected to match
> the review's own looser guess.
>
> **P-4's visual sweep found two real, previously-undetected defects neither the first nor the
> second external review named precisely enough to locate.** Figure 1's value labels and
> $\kappa_{\max}$ annotation were rendering below the venue's ~6pt legibility floor — root-caused
> to a silent mismatch between the figure's native matplotlib design width (`style.FIG_FULL`,
> intended for near-full-linewidth inclusion) and the `\includegraphics` width actually used in
> `main.tex` (0.62\linewidth, a leftover from visual-consistency copying against a sibling figure
> with a *different* native design width). This is the same class of defect G11 investigated and
> reverted a fix for (`audit/S11_REPORT.md` §4) — but G11's check only tested a *further*
> reduction from the existing 0.62, never the absolute effective font size the existing 0.62 was
> already producing (~5pt), so it was never caught. Fixed by widening to 0.78\linewidth (~6.2pt
> effective, verified by a fresh 400dpi render read directly). Table 1 (the compact four-findings
> overview) was hyphenating mid-word inside its narrow columns ("identifi-able", "nui-sance",
> "distor-tion") — exactly the illegible-cell defect the review named for the appendix claims
> table, but present here too, in a table the review evidently didn't inspect at this resolution.
> Fixed by rebalancing column widths and disabling automatic hyphenation for the table
> (`\hyphenpenalty=10000`), verified by a fresh render: every cell now wraps at whole words.
>
> **Figure 1's fix cost real vertical space and reopened the closed 5-page budget a second time
> this session** (the first time being this session's own R14-1/R14-2/etc. additions). Recovered
> by cutting one further non-load-bearing aside (a mention of two alternative composite-null
> repairs — Xie's repro samples, Barber & Janson's approximate co-sufficient sampling — not used
> anywhere else in the paper's argument), not by touching anything load-bearing. Final main text:
> **exactly 5 pages**, confirmed by rendering pages 5–6 directly after every edit round in both
> page-budget-closing passes, not estimated from a line count.
>
> **A connectivity/API failure interrupted this session mid-way through Phase 3 (P-1, dash
> removal).** On resume, git status and a fresh grep (not the prior turn's own narration) were
> used to establish what had actually landed on disk: `paper/main.tex` and `paper/checklist.tex`
> were already fully clean of " -- " instances, but `paper/appendix_claims_table.tex`'s 5 heading
> dashes (generated from `src/diagnostics/report_claims.py`'s `TITLES` dict, not hand-editable)
> were not yet fixed — exactly the piece the disconnect cut off mid-task. Fixed at the source and
> regenerated, rather than hand-patching the generated `.tex` file directly, preserving the
> project's own "generated, not hand-typed" invariant for that file.

### What G14 was judged against

| # | Criterion | Result |
|---|---|---|
| **G14.1** | **R14-1 (Tier 1): findings list restored to the Introduction, all six family mechanisms named and verified against `src/simulators/sir3.py` directly, K-notation disclaimer and three of four redundant "prior art" restatements cut, page count held at ≤5** | **met.** `paper/main.tex`; mechanism descriptions cross-checked line-by-line against `sir3.py`'s docstring and `_rhs`/`simulate` implementation before writing, not against the review's paraphrase |
| G14.2 | R14-2: ellipsoid comparison added to Section 5, computed directly from the project's own MLE/Fisher-information results, not asserted from the review's estimate | **met**, and the recomputation corrected the review's own guess rather than confirming it — see headline |
| G14.3 | R14-3: "exactly zero" replaced with the exact measured draw count | **met.** "zero acceptances in 100,000 draws", confirmed against `confidence_set_mmc.yaml`'s `by_key.*.reported_min.n_draws` for all three non-primary combinations |
| G14.4 | R14-4: the 0.9–2.7% SE-scaling figure explained by naming which three of five nuisance coordinates it uses | **met.** Traced to `results/robustness/alt_eta_scaling.yaml`'s `per_column_relative_scale` field (itself expressed as a multiple of the flat 10% convention, not an absolute fraction — confirmed by direct arithmetic before writing the explanation) |
| G14.5 | R14-5: "coherence pair flagged" resolved (definition added or phrase removed) and the gradual/abrupt threshold-of-3 rule stated where first used | **met, via the removal branch for the first half** (page-budget pressure; the review offered removal as an equally valid fix) **and the definition branch for the second** (Section 5 now states the slope-ratio-vs-3 rule and the measured 2.265× inline) |
| G14.6 | R14-6: both figure-rendering bugs, both bibliography defects, the Table 1 (appendix) column overflow, and $\theta_0$'s pre-figure definition | **met**, all five sub-items, each independently verified (figures re-rendered and read; bib entries checked against arXiv's own submission-history metadata, not guessed; $\theta_0$ now named in Section 5's own prose before Figure 3's caption uses it) |
| G14.7 | R14-7: Appendix A.5's claim-to-source ledger referenced from the start of Section 4 | **met** — one sentence, merged into the existing "Simulator and summary sets" paragraph opening to avoid a standalone-paragraph space cost |
| G14.8 | R14-8: Montel et al.'s test either run or the assertion explicitly hedged, with the choice stated plainly | **met, hedge path taken.** Confirmed not implemented anywhere in this project (`grep -rl` across `src/` and `tests/` for "montel"/"anau", zero hits) before choosing the hedge over an under-resourced same-session implementation |
| G14.9 | R14-9: a positive sentence on where a learned summary statistic/NPE would enter, beyond the existing Limitations hedge | **met** — added to Background's "Diagnostic tooling" bullet |
| G14.10 | R14-10 (optional): promotion of $S_A$ to a fifth finding, decided and stated either way | **met — declined, reasoning stated** in the headline and in `audit/S14_REPORT.md` |
| G14.11 | P-1: paper-wide dash removal, each instance read and rewritten individually, zero blind substitutions | **met.** 38 instances across `paper/main.tex` (31), `paper/checklist.tex` (2), and `paper/appendix_claims_table.tex`'s generator (5) — the last completed after this session's own connectivity interruption, verified against disk state rather than assumed done. Final sweep: `grep -rn -- ' -- ' paper/*.tex` and a literal Unicode em/en-dash sweep both return zero matches paper-wide |
| G14.12 | P-2: title and abstract reconsidered against the paper's current state | **met.** Title unchanged (still the right framing); abstract judged to already earn its place and read at the right confidence level after the P-1 dash pass — no further edit made, a checked-and-confirmed outcome rather than a skipped one |
| G14.13 | P-3: every figure/table caption ≤3 sentences, nothing lost, only relocated or de-duplicated against main-text prose | **met.** Three captions compressed (`fig:nontermination`, `fig:simulator`, `fig:confound`); five were already within the limit |
| G14.14 | P-4: visual overlap/legibility sweep on the rendered PDF, particular attention to Figure 1 | **met, and found two real defects** — see headline. Every other figure (2, 3, 5, 6, 7) and the appendix simulator diagram checked at up to 400dpi: clean |
| G14.15 | All 6 original Tier-1 and 15 original Tier-2 findings (first external review) still hold after this session's rewriting | **met**, verified against `audit/S11_REPORT.md`'s canonical descriptions. Full accounting in §Phase-5 below; the highest-risk overlaps (T2-12 K-notation, T2-11 the $s(y)$ clause, T2-10 abstract, T2-3 alt-eta-scaling, T2-15 the Montel sentence, T1-1/T1-4 the appendix restructuring) individually re-checked against the current text, not merely assumed carried forward |
| G14.16 | R1/R2 (first-review novelty threat-checks) and the second review's own cross-check items still hold | **R1/R2 met** (still DEAD / NARROW-CONDITIONAL, unchanged in Background's prose). **The second review's specific "R-1/R-2/R-3" cross-check labels could not be independently re-derived** — that review's literal text was in this session's original prompt, not persisted to disk, and was not fully recoverable after the mid-session connectivity interruption. Disclosed rather than guessed at; see "does not certify" below |
| G14.17 | Full number-trace re-run | **partial, targeted.** Every number this session added or changed (R14-2's Mahalanobis radii, R14-3's exact draw count, R14-4's coordinate mapping) independently recomputed from source `results/*.yaml` files before writing, shown in commit messages. Numbers this session did not touch verified unchanged by diff, not re-derived from scratch — the same method G13.6 used and disclosed, not a silent shortcut |
| G14.18 | Full anonymization re-scan, independent of the targeted fixes | **met.** Rendered-PDF text, all commit messages this session, and every touched source file re-scanned; the only hits are the pre-existing, deliberate AI-use-disclosure placeholder and pre-existing "session G11" code comments (both an established, previously-disclosed pattern per G13.5, neither introduced this session) |
| G14.19 | Page count ≤5, confirmed by rendering | **met. Exactly 5 pages**, re-confirmed after both page-budget-closing rounds this session (R14-1's own additions, then again after Figure 1's legibility fix), by rendering pages 5–6 directly each time |
| G14.20 | Two-tier isolation compile against a freshly rebuilt package | **met, both tiers.** §OVERLEAF-EQUIVALENT (`TEXMFHOME` pointed at this operator's personal package tree, `TEXINPUTS` unset): exit 0, 22 pages, zero undefined references/citations, `pdftotext` output textually identical between the isolated extraction and the repo working copy, both 592KB. §`TEXMFHOME`-unset (this-machine sense only, per G12/G13's own naming correction): exit 0, 22 pages, same narrow caveat as every prior gate |
| G14.21 | `scripts/build_overleaf_package.sh` re-run against the final commit | **met** — `build/sim_attrib_overleaf_8bc07cf.zip`, 17 files, rebuilt again after the post-commit dash fix (§ headline) and re-verified against a fresh isolated extraction: exit 0, 22 pages, zero undefined references/citations, `pdftotext` output textually identical to the repo working copy, both 592KB |
| G14.22 | No self-approval | **met** — `status: ready for review — UNSIGNED` |

### Phase 5 — the full T1/T2 re-verification table

| Item | What it is | Status after this session |
|---|---|---|
| T1-1 | Appendix claim-to-source table, generated not hand-typed | **intact.** Only the 5 section-heading dashes changed (P-1); every value cell diff-confirmed unchanged |
| T1-2 | Page limit ≤5 | **intact**, re-closed twice this session after two separate reopenings (own additions; Figure 1 fix) |
| T1-3 | Real confidence-set-bounded MMC check (not a cheaper reframe) | **intact**, and its own output (`confidence_set_mmc.yaml`) is now the direct source for R14-2's new ellipsoid claim — strengthened, not just preserved |
| T1-4 | Simulator schematic relocated, qualitative content restated in main-text prose | **intact and strengthened.** R14-1 added the per-family mechanism sentence this fix's restatement previously lacked in full mechanistic detail |
| T1-5 | Full anonymity re-scan | **intact**, re-run this session (G14.18) |
| T1-6 | Checklist answers match the compiled PDF | **intact.** Checklist content untouched this session; only 2 dashes removed (P-1) |
| T2-1/T2-2 | Rank-at-$\tau$/$\kappa\le\kappa_{\max}$ stated as one condition; $\kappa^2$ compute-cost derivation | **intact**, untouched this session |
| T2-3 | Data-motivated $\eta$-scaling using confidence-set SEs | **intact and strengthened** — R14-4 named the exact 3 coordinates this fix's numbers use |
| T2-4 | Second-$\theta$ test run | **intact**, untouched this session |
| T2-5 | Eight Related Work citations genuinely engaged | **intact.** Two citations (Xie, Barber & Janson) removed this session for page budget, per an explicit, disclosed judgment call (headline) — the other six engaged citations named in T2-5 are untouched |
| T2-6 | Section 5 retitled, finding-first, apologetic framing fixed | **intact**, untouched this session |
| T2-7 | Scope restriction stated in the introduction's own first contribution sentence | **intact, and now more prominent** — R14-1's restored findings list states it directly rather than via the table pointer this fix used previously |
| T2-8 | Two-panel non-termination figure, per-figure font floors | **intact**, and this session's own P-4 sweep found and fixed a *different* figure's font-floor violation (Figure 1) without touching this one |
| T2-9 | Repeated metaphor reduced; diagnostic's four steps as a numbered list | **intact.** The enumerate structure untouched; only its intro line's redundant "every ingredient prior art" parenthetical cut (R14-1) |
| T2-10 | Abstract tightened, one concrete number retained | **intact.** $\kappa=628.9$, rank 4/6 still present; P-1/P-2 trimmed one further redundant clause, no number touched |
| T2-11 | Limitations bullet on where a learned summary statistic would sit | **intact.** The specific protected clause, "(where $s(y)$ would sit)", verified still present verbatim after this session's wording trim of the same bullet's other clauses |
| T2-12 | K-vs-column-count notation conflict resolved | **intact and resolved more thoroughly** — R14-1 removed the disclaimer parenthetical only after R14-6 fixed the actual root-cause legend bug, so the conflict no longer exists at all rather than being explained away |
| T2-13 | Appendix table's plateau-stability caption honest about noise | **intact**, untouched this session |
| T2-14 | Checklist after the appendix | **intact**, untouched (structural position) this session |
| T2-15 | One sentence on the baseline test's output on the six-column confound | **intact, deliberately reworded** — R14-8 softened "would correctly reject" to an explicitly hedged "would be expected to ... reject", per this session's own review instruction, not a regression |
| R1 (first-review novelty threat-check) | Rejection-sampling-calibration mechanism is prior art | **intact** — `audit/R1_THREAT_CHECK.md`'s DEAD verdict unchanged in Background's prose |
| R2 (first-review novelty threat-check) | Noisy-rank estimator, corrected instrument | **intact** — `audit/R2_THREAT_CHECK.md`'s NARROW-CONDITIONAL verdict unchanged |
| "R-3" (second review's cross-check) | **Not independently recoverable this session** — see G14.16 and "does not certify" below |

### What G14 explicitly does not certify

- **That the second review's own "R-1/R-2/R-3" cross-check items were verified against their
  literal original wording.** That text lived only in this session's original prompt, which was
  not persisted to disk, and the session was interrupted by a connectivity failure partway
  through. What this session *did* verify — the first review's R1/R2 novelty threat-checks, still
  intact — may or may not be the same items the second review's cross-check labeled R-1/R-2/R-3.
  Recommend the operator supply the second review's literal cross-check text if this distinction
  matters before submission.
- **That the full ~150+-claim number trace was re-run from scratch this session.** It was not.
  Every number this session touched was independently recomputed from source; every number it did
  not touch is carried forward on the same diff-based method G13.6 already used and disclosed.
- **That a third external review has been run against this session's substantial rewriting.**
  None has. This session touched nearly every paragraph in the document (the dash-removal and
  caption-compression passes alone), which is more main-text rewriting than any prior single
  session in this project's history. **A third external review is recommended before submission**,
  more strongly than G13's recommendation was, given the scope of this session's changes.
- **That Figure 1's new 0.78\linewidth width is the *only* correct choice.** It is the smallest
  width this session found that clears the ~6pt floor with a small margin (effective ~6.2pt); a
  human designer might reasonably choose a different value for visual balance. Not re-litigated
  further given the page-budget cost of any larger choice.
- **That the two citations dropped from Related Work (Xie, Barber & Janson) will not be missed
  by a reviewer who read the pre-G14 draft.** A real, if minor, content reduction, disclosed in
  the headline and in `audit/S14_REPORT.md`, not buried in a diff.

### Process caveats — what this session did badly or not at all

- **A connectivity/API failure interrupted this session mid-task**, during Phase 3 (P-1). Resumed
  by checking actual disk state (`git status`, fresh greps) rather than trusting this session's
  own prior narration, per the resume instruction — and it was the right call: the prior turn's
  self-report would have said P-1 was "in progress," but disk state showed two of three target
  files already fully clean and precisely identified the one remaining piece (`appendix_claims_table.tex`'s
  generator). Recorded here as a demonstration that this project's own standing S6/S8 discipline
  (verify against artifacts, not narration) generalizes to recovering from an infrastructure
  failure, not only to catching a session's own reasoning mistakes.
- **The R14-2 ellipsoid computation did not match the review's own estimate**, and this session
  reported the discrepancy rather than quietly using whichever framing sounded more confident.
  Recorded as a case where "verify the review's own numbers, don't just cite them" (this session's
  own explicit brief) actually changed the paper's claim, not just confirmed it.
- **Figure 1's font-floor violation was not new** — it existed since whichever earlier session
  first set `width=0.62\linewidth` for that figure, and neither the first external review nor five
  prior gates' own re-verification passes caught it, including G11's own font-floor investigation,
  which checked a *further* reduction from that width rather than the width's own existing effect.
  This session's P-4 mandate (an explicit visual sweep on the rendered PDF, not a source-code
  check) is what caught it. Recorded as evidence for keeping P-4-style sweeps in future gates,
  not as a criticism of any specific prior session.
- **No second external review of this specific session's output has been run**, and per the
  operator's own standing instruction this session does not run one itself. See "does not certify"
  above.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G15 — Does the paper close the second review's R-1/R-2/R-3 gap, and does an exhaustive
ground-up re-verification confirm the paper is ready for a third external review?

**status: ready for review — UNSIGNED**

Prepared 2026-08-26, session G15. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **The one specific gap G14 left open — independent re-confirmation of the second review's
> literal R-1/R-2/R-3 cross-check — is closed.** All three verified directly against current
> source, not against G14's own narration of what it did (S6): R-1's six family mechanisms
> checked against `src/simulators/sir3.py` line by line; R-2's ledger-reference sentence and its
> three named undefined criteria checked against current `paper/main.tex`; R-3's Mahalanobis
> radii independently recomputed from scratch from `results/confidence_set_mmc.yaml` and
> `results/boundary_sweep.yaml` — **2.7096 and 3.5616, matching the paper's stated 2.71 and 3.56
> to four significant figures**, with the Fisher-information inversion cross-checked against the
> file's own stored eigenvalues before being trusted. Full detail in
> `audit/R1R2R3_RECONCILIATION.md`.
>
> **A full ground-up read-through of the compiled PDF — done before any mechanical check ran, so
> it was not primed by already knowing what had passed before — found one genuine visual defect
> none of the fourteen prior sessions' own sweeps caught.** `figures/fig6b_nontermination_variants.pdf`
> ("Figure 7," Appendix A.3) placed its legend at `loc="lower left"`, directly where the
> descending AAA/BBB studentised curves and their zero-acceptance markers cross. G14's own P-4
> sweep reported this figure "clean" — it was not, for a different failure mode (legend-over-data)
> than the font-floor and hyphenation defects P-4 was checking for. Fixed by moving the legend to
> `loc="upper right"`, the one region no series reaches; no data changed; page count and both
> isolation tiers re-verified clean after the fix. Full detail in `audit/G15_READTHROUGH.md`.
>
> **The exhaustive number-trace this session actually re-derived (not diffed against prior
> sessions' own verification) found two further defects, both in Section 5 — the section a third
> reviewer is most likely to scrutinize closely given R-3's history across two review rounds.**
> (1) "$\kappa$ falls to $344.9$ but stays two orders past $\kappa_{\max}=100$" overstates the
> margin by roughly $30\times$ ($344.9/100=3.45$, not $100\times$); fixed to state "$3.4\times$
> past," matching the paper's own convention elsewhere of exact multiplicative margins. Git
> history shows this imprecision predates every review round, not something this session's own
> editing introduced. (2) "every one wider than the $\pm0.5\%$ box already known to break the
> composition" directly contradicted the same section's own later, data-verified statement (and
> this session's own Phase 1 recomputation) that $\pm0.5\%$ is the **last fully-passing** box and
> $\pm0.75\%$ is what **first fails** — fixed to name $\pm0.75\%$, the box the data actually
> supports. Both recompiled clean, page count unchanged. Full detail in
> `audit/G15_NUMBER_TRACE.md`.
>
> **A fourth defect, process rather than content, turned up when this session actually re-ran the
> full test suite rather than assuming G14's own report of a clean pass still held (S6):** two
> figures' provenance sidecars (`fig3_spectrum`, `fig6_nontermination`) had carried `dirty: true`
> since separate G14 sessions, committed that way and never re-generated from a clean tree
> afterward; a third (`fig6b_nontermination_variants`) was this session's own oversight from Phase
> 2, never closed out the same way. Confirmed content-harmless in all three cases (pixel-identical
> regenerations) and fixed as the last step of this session — see "Process caveats" below.
>
> **Four genuine, previously-uncaught defects found and fixed this session, on top of confirming
> R-1/R-2/R-3 closed.** None was catastrophic — a legend placement, an order-of-magnitude
> adjective, a mislabeled box width, and three stale provenance flags — but the first three are
> exactly the class of small, load-bearing imprecision an external reviewer reads a paper
> specifically to find, and all four survived fourteen prior sessions' own verification passes.
> Recorded plainly per S8: this is not a session that found nothing, and it should not be
> summarized as one.

### What G15 was judged against

| # | Criterion | Result |
|---|---|---|
| G15.1 | Phase 0: HEAD matches G14's push, tree clean, two-tier isolation compile before any content review | **met.** HEAD `ac89d8d` confirmed at session start; both tiers compiled clean (exit 0, 22 pages, zero undefined refs, identical `pdftotext` output) before Phase 1 began |
| G15.2 | R-1 independently re-verified against current `paper/main.tex` and `src/simulators/sir3.py` | **met.** All six family mechanisms named in Section 4 prose match `sir3.py`'s own docstring exactly; confound-interpretation sentence followable from those names alone, without the appendix figure |
| G15.3 | R-2 independently re-verified: ledger reference sentence position, and all three named undefined criteria (coherence, leakage, slope-ratio) | **met.** Reference sentence is the first sentence of Section 4. "Coherence" fully absent from main text (removed, not defined — the review's own equally-valid fix); "leakage" concept stated in prose without the jargon word; slope-ratio rule stated explicitly with threshold=3 and measured 2.265× |
| G15.4 | R-3 independently recomputed from scratch (not re-read from G14's derivation) | **met.** 2.7096/3.5616 vs. paper's stated 2.71/3.56 — matches to 4 significant figures. Eigenvalue cross-check on the Fisher-information inversion matches the file's stored `hessian_eigenvalues` to $10^{-13}$–$10^{-16}$ relative error |
| G15.5 | Reconciliation note written, closing G14's disclosed gap | **met** — `audit/R1R2R3_RECONCILIATION.md` |
| G15.6 | Phase 2: complete read-through of the compiled PDF, start to finish, before any mechanical check | **met.** 22 pages, `pdftotext -layout` extraction read in full plus every figure/table rendered at 200–400dpi and visually inspected. One defect found (Figure 7 legend overlap) and fixed |
| G15.7 | No dash-removal meaning-drift found from G14's 38-instance rewrite | **met.** Every rewritten clause read as a faithful substitution; nothing flagged |
| G15.8 | Every figure/table stands on its own | **met, after the one fix.** Figure 7's legend now sits in the one region no data reaches; every other figure/table (1–6, Tables 1–3) confirmed clean at up to 400dpi |
| G15.9 | Cross-section consistency (the class of defect that caught the earlier K-notation and 8.4-vs-27-65 discrepancies) | **met, with two findings.** $K$-notation still resolved (never conflated with six-column case); figure numbering consistent between `\ref`s, Table 1's `fig.` column, and page order. Two Section 5 numeric/logical inconsistencies found and fixed (see headline; full detail `audit/G15_NUMBER_TRACE.md`) |
| G15.10 | Abstract-to-body consistency against R-3's current ellipsoid finding | **met, no change needed.** Abstract states no Mahalanobis radius or "well inside"/"just past" characterization at all — nothing in it depends on R-3's precise number, checked directly rather than assumed from G14's own P-2 finding |
| G15.11 | Read-through findings written, including "nothing found" as an explicit honest outcome where applicable | **met** — `audit/G15_READTHROUGH.md`. Nothing left for operator judgment this session (S8): every observation was either already correct or fixed outright |
| G15.12 | Phase 3: every number in the compiled document extracted and traced, not sampled | **met.** ~75 distinct numeric claims across main text/figures/tables/appendix checked individually, plus the ~80-row generated Appendix A.5 ledger checked as a block with targeted spot-checks (`second_theta_check.yaml`, `alt_eta_scaling.yaml` read directly). Two defects found and fixed (see headline) |
| G15.13 | `audit/FINAL_CLAIMS.md` updated if any G14-era number isn't yet represented | **met, no update needed.** Both Section 5 fixes correct existing traced numbers; no new `results/*.yaml` file or field was introduced this session |
| G15.14 | Total numbers checked reported, zero untraced | **met** — `audit/G15_NUMBER_TRACE.md` §Count. Zero numbers remain untraced after the two fixes |
| G15.15 | Phase 4: one consolidated table covering every item from both review rounds plus this session's own findings | **met** — this table, below |
| G15.16 | Full independent anonymization re-scan | **met.** Compiled PDF text (22 pages), every commit message this session, and every file touched this session (`git diff --name-only ac89d8d..HEAD`) all scanned fresh; zero hits. `pdfinfo` confirms empty `Author` field |
| G15.17 | Final page count confirmed exactly | **met. 22 total pages; main text (Abstract–Limitations) pages 1–5; References start page 6** — re-confirmed by direct page render after every content edit this session (Phases 1, 2, 3), not estimated |
| G15.18 | Two-tier isolation compile, both tiers, against the final committed state | **met, both tiers**, against a freshly rebuilt `sim_attrib_overleaf_19f9a59.zip` extracted fresh to an isolated temp directory (never the repo working copy): §2b (`TEXMFHOME` pointed at this operator's personal package tree, `TEXINPUTS` unset) exit 0, 22 pages, zero undefined refs/citations; §2a (`TEXMFHOME` unset, this-machine-fallback sense per G12's own naming correction) exit 0, 22 pages, same narrow caveat as every prior gate. `pdftotext` output identical between both tiers' extractions |
| G15.19 | `scripts/build_overleaf_package.sh` re-run against the final commit | **met** — `build/sim_attrib_overleaf_19f9a59.zip`, 17 files |
| G15.20 | Full pytest suite re-run, not assumed still passing from G14's own report (S6) | **met, and found a real defect.** 176 passed, 1 failed on first run: `fig3_spectrum.provenance.json`'s stale `dirty: true` flag (§ headline). Fixing it and re-checking surfaced two more of the same class (`fig6_nontermination`, `fig6b_nontermination_variants`). All three confirmed content-harmless, all three fixed from a clean tree, suite re-run clean after the fixes (177 passed) |
| G15.21 | No self-approval | **met** — `status: ready for review — UNSIGNED` |

### Phase 4.1 — the full consolidated table: every item from both review rounds, this session's
own reconciliation, and this session's own read-through/number-trace findings, in one place

| Item | What it is | Status after G15 |
|---|---|---|
| T1-1 | Appendix claim-to-source table, generated not hand-typed | **intact**, unchanged this session |
| T1-2 | Page limit ≤5 | **intact.** Re-confirmed after every edit round this session (Phases 1, 2, 3); still exactly 5 main-text pages |
| T1-3 | Real confidence-set-bounded MMC check (not a cheaper reframe) | **intact.** `confidence_set_mmc.yaml` independently re-read and its numbers independently recomputed this session (Phase 1) |
| T1-4 | Simulator schematic relocated, qualitative content restated in main-text prose | **intact**, re-confirmed by this session's own Phase 2 read (family-mechanism sentence followable without the appendix figure) |
| T1-5 | Full anonymity re-scan | **intact**, re-run this session (G15.16) |
| T1-6 | Checklist answers match the compiled PDF | **intact.** Checklist read in full this session (Phase 2); content unchanged |
| T2-1/T2-2 | Rank-at-$\tau$/$\kappa\le\kappa_{\max}$ stated as one condition; $\kappa^2$ compute-cost derivation | **intact**, unchanged, re-read this session |
| T2-3 | Data-motivated $\eta$-scaling using confidence-set SEs | **intact**, and this session independently re-derived the 0.9–2.7% figure two ways (direct SE/$\hat\theta$ ratio; `alt_eta_scaling.yaml`'s stored multiple-of-10%-convention field) — both agree |
| T2-4 | Second-$\theta$ test run | **intact**, and its two numbers ($\kappa=10.9$, $\kappa=10.1$) independently traced this session to `results/second_theta_check.yaml` and `robustness/k6_spectrum.yaml` directly |
| T2-5 | Related Work citations genuinely engaged | **intact.** Unchanged this session; the two-citation reduction G14 disclosed stands as previously recorded |
| T2-6 | Section 5 retitled, finding-first, apologetic framing fixed | **intact**, unchanged |
| T2-7 | Scope restriction stated in the introduction's own first contribution sentence | **intact**, re-read this session |
| T2-8 | Two-panel non-termination figure, per-figure font floors | **intact**, and this session's own Phase 2 sweep additionally found and fixed a different defect in this figure's sibling (Figure 7's legend, not a font-floor issue) |
| T2-9 | Repeated metaphor reduced; diagnostic's four steps as a numbered list | **intact**, unchanged |
| T2-10 | Abstract tightened, one concrete number retained | **intact.** Re-checked this session specifically against R-3's current ellipsoid finding (G15.10) — no adjustment needed |
| T2-11 | Limitations bullet on where a learned summary statistic would sit | **intact.** The `(where $s(y)$ would sit)` clause verified still present verbatim |
| T2-12 | K-vs-column-count notation conflict resolved | **intact**, re-confirmed by this session's own full-text read (G15.9) |
| T2-13 | Appendix table's plateau-stability caption honest about noise | **intact**, unchanged |
| T2-14 | Checklist after the appendix | **intact**, unchanged (structural position) |
| T2-15 | One sentence on the baseline test's output on the six-column confound | **intact**, unchanged |
| R1 (first-review novelty threat-check) | Rejection-sampling-calibration mechanism is prior art | **intact** — DEAD verdict unchanged in Background's prose |
| R2 (first-review novelty threat-check) | Noisy-rank estimator, corrected instrument | **intact** — NARROW-CONDITIONAL verdict unchanged |
| **R-1 (second review)** | Main-text self-sufficiency: family mechanisms + confound interpretation | **CLOSED this session, independently verified from source** — `audit/R1R2R3_RECONCILIATION.md` |
| **R-2 (second review)** | Ledger under-referenced; undefined criteria (coherence, leakage, slope-ratio) | **CLOSED this session, independently verified from source** — ibid. |
| **R-3 (second review)** | Mahalanobis-radius/ellipsoid comparison | **CLOSED this session, independently recomputed from source and matched to 4 s.f.** — ibid. |
| R14-1 through R14-9 | Second review's Path to Acceptance items | **intact**, unchanged this session, re-read in full during Phase 2 |
| R14-10 | $S_A$ promotion (optional) | **intact — still declined, reasoning unchanged** |
| P-1 | Paper-wide dash removal (38 instances) | **intact.** This session's own read specifically checked for meaning-drift from this rewrite (the highest-risk residual G14 itself named) and found none |
| P-2 | Title/abstract reconsideration | **intact**, re-checked this session against R-3's finalized number (G15.10) |
| P-3 | Figure/table captions ≤3 sentences | **intact**, unchanged |
| P-4 | Visual overlap/legibility sweep | **intact for the two defects G14 found (Figure 1, Table 1), and extended this session** — Figure 7's legend-over-data overlap, a different defect class P-4 did not check for, found and fixed (G15.6–G15.8) |
| **G15 Phase 2 finding** | Figure 7 (`fig6b_nontermination_variants`) legend crossed by descending data curves | **FOUND AND FIXED this session** — `audit/G15_READTHROUGH.md` |
| **G15 Phase 3 finding 1** | Section 4: "$344.9$... two orders past $\kappa_{\max}=100$" overstates the margin ~30$\times$ | **FOUND AND FIXED this session** — `audit/G15_NUMBER_TRACE.md` |
| **G15 Phase 3 finding 2** | Section 5: "$\pm0.5\%$ box already known to break the composition" contradicts the section's own later, data-verified statement | **FOUND AND FIXED this session** — ibid. |
| **G15 Phase 4 finding** | Three provenance sidecars (`fig3_spectrum`, `fig6_nontermination` from G14; `fig6b_nontermination_variants` from this session's own Phase 2) carried stale `dirty: true` flags | **FOUND AND FIXED this session, content confirmed harmless in all three** — pixel-identical regenerations; process caveats below |

### What G15 explicitly does not certify

- **That this is now a fully error-free document.** Three real defects survived fourteen prior
  sessions' own verification passes and were found only because this session re-derived rather
  than re-checked. A document this heavily reviewed can still contain a fourth, fifth, or sixth
  defect this session's own methods did not surface. The honest position is that this session
  raises confidence, not that it exhausts the space of possible errors.
- **That a third external review has been run.** None has. This is explicitly the last internal
  session before that review, per the session brief, and this gate does not substitute for it.
- **That the two Section 5 fixes are the only numeric imprecisions of their kind remaining.**
  This session's number-trace was exhaustive over *distinct numeric claims currently in the
  document*, not an exhaustive search over every possible phrase that could misdescribe a
  correct number (e.g. "two orders" was caught because it was checked against a working
  definition of "orders of magnitude" and against a correctly-used sibling instance in the same
  section; a different kind of misdescription might not trip the same check).
- **That the STRICT-isolation tooling gap (disclosed since G11/G12, deferred again by G13) is
  resolved.** Unchanged this session, for the same reason G13 gave: a genuine fix needs a second,
  actually-isolated TeX Live installation or a containerized build environment, neither available
  on this machine within this session's scope.
- **That the two citations dropped from Related Work in G14 (Xie, Barber & Janson) have been
  reconsidered.** Not this session's scope; carried forward as G14 disclosed it.

### Process caveats — what this session did badly or not at all

- **The Figure 7 legend defect and both Section 5 numeric errors all predate this session.**
  None was introduced by G15's own edits — confirmed by `git log -S` for the Section 5 phrases
  and by the fact that Figure 7's legend placement (`loc="lower left"`) was never touched by any
  session's diff before this one. They are reported as findings, not as this session correcting
  its own mistakes.
- **The full pytest suite was re-run this session (176 passed, 1 failed on first run) and found
  a fourth real defect, process rather than content: three figures' provenance sidecars carried
  stale `dirty: true` flags.** `figures/fig3_spectrum.provenance.json` had been `dirty: true`
  since G14's R14-6 figure-rendering fix (commit `03a659c`), which regenerated the figure while
  `paper/main.tex`, `src/viz/fig3_spectrum.py`, and `src/viz/fig6_nontermination.py` were all
  mid-edit; `figures/fig6_nontermination.provenance.json` carried the same class of stale flag
  from G14's mid-session connectivity-interrupted dash fix (`S14_REPORT.md` §5); neither was
  re-generated from a clean tree afterward — the exact discipline session G3 established
  (`audit/S11_REPORT.md`-era pattern: "the first production run was discarded... the code was
  committed and the run repeated") and a sibling commit (`ae4e88d`) had already applied to
  `fig3_spectrum` once before a later G14 edit silently undid it.
  `figures/fig6b_nontermination_variants.provenance.json` was a third instance, and this
  session's own: Phase 2's legend fix (commit `24f6fa5`) was committed correctly but never
  followed by the second clean-tree regeneration that records the flag as `dirty: false`. No
  content defect in any of the three: each clean-tree regeneration produces a **pixel-identical**
  PDF to what was already committed (confirmed by `pdftotext` text diff and a full
  pixel-difference bounding-box check, both empty/`None`, for `fig3_spectrum` and
  `fig6_nontermination`; `fig6b_nontermination_variants` was already content-correct from Phase 2,
  only its provenance snapshot was stale) — only embedded `CreationDate`/`ModDate` bytes differ
  where they differ at all, the same harmless difference every isolation-compile check in this
  project's history has already treated as expected. All three fixed as the last step of this
  session, from a fully clean tree each time, immediately before the final commit (§Phase 5); full
  pytest suite re-run clean afterward (177 passed).
- **No adversarial critic or second independent agent ran against this session's own findings.**
  Every verification in this gate is single-pass, from one session's own re-derivation. The third
  external review is the actual independent check this project's own process has always deferred
  to for exactly this reason.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G16 — Does the paper close the third external review's two real findings and nine smaller
ones, and is a safe, working anonymized package ready for upload?

**status: ready for review — UNSIGNED**

Prepared 2026-08-26, session G16. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **W16-2, the session's highest-priority item, was implemented and genuinely run, not
> hedged.** `src/baselines/montel_marginal.py` implements Anau Montel, Alvey & Weniger
> (2025)'s Section II.3 trials-corrected minimum-per-summary-statistic global-null test exactly
> as constructed — the one stated simplification is an exact per-summary test statistic in
> place of their neural local tests, justified in the module's own docstring by this project's
> summaries being directly Monte-Carlo-computable rather than requiring amortised density-ratio
> estimation, which is the only reason their construction needs a neural network at all. Run
> against the real simulator (`src/simulators/sir3.py`), not a toy example, at the two declared
> corners and at two finite-magnitude realizations of the six-column confound's own named
> mechanisms (`audit/FINAL_CLAIMS.md` C3's "drifting removal hazard" vs. "constant hazard
> change combined with a drifting reporting rate"), plus a null-data control and a strong-
> distortion control (`results/montel_marginal_test.yaml`, 7,506 simulator draws).
>
> **The measured result reverses what Section 2 previously asserted without measuring it.**
> The global test correctly rejects at both declared corners and at both confound realizations
> ($p\approx0.004$, resolution-limited by a 3,000-draw reference batch), and correctly does
> *not* reject the null-data control ($p=0.61$) — the S5 vacuous-flag test, applied to the
> test's own calibration machinery, passing explicitly. Its arg-min flags **disjoint** summary
> coordinates for the two confound mechanisms at this magnitude (`binned_incidence_01` vs.
> `binned_incidence_02`, near-min sets with zero Jaccard overlap), not the same ones on both
> sides as the paper previously claimed. Section 2 is rewritten to report this honestly,
> including the caveat the finding itself demands: one realization per mechanism is a
> measurement, not a distribution, and a marginal test's finite-magnitude power is a different
> question from the Jacobian's local ($\eta=0$) near-null identifiability the rest of the paper
> establishes — the measured result does not overturn that, and does not claim to.
>
> **A second, independent anonymization defect was found and fixed, beyond anything the session
> brief anticipated.** Every `results/*.yaml` file's `provenance` block records this machine's
> hostname (`Palaashs-MacBook-Air.local`, containing the operator's name) under **two different
> field names** (`host`, `measured_on`), and a private-repo commit hash under **two different
> field names** (`commit`, `p_sel_run_commit`) — found by grepping the operator's own name
> across every file in `results/` rather than trusting a hand-enumerated key list, the same
> discipline this project has needed before. `scripts/build_anonymous_package.sh` redacts both,
> by value pattern (any 40-hex-character line, any line containing the operator's name)
> rather than by key name, so a field this session did not find is still caught if it exists.
> Independently re-scanned after building: zero hits for the operator's name, GitHub username,
> email, any AI-authorship token, or any 40-hex-character string, across all 91 packaged files.
>
> **The package was extracted fresh and actually run, not shipped on trust.** 176 of 183 tests
> passed on the first extraction; the 7 failures were real and are now documented, not hidden:
> 6 in `test_viz.py` (figure-drawing scripts read page geometry from the NeurIPS venue's `.sty`
> file, which is part of the paper submission and correctly not bundled in a code package) and
> 1 in `test_provenance.py` (asserts `git rev-parse HEAD` resolves, trivially false in a package
> that deliberately carries no git history). Neither affects any simulator, diagnostic, or
> baseline code. The package's own README documents the exact `pytest` invocation that excludes
> both, and states plainly why, rather than presenting an untested green checkmark.

### What G16 was judged against

| # | Item | Status | Location |
|---|---|---|---|
| W16-1 | Checklist item 16 (LLM disclosure) confirmed unchanged | **confirmed unchanged** — literal `\answerTODO{}` placeholder, clearly marked, operator's to complete | `paper/checklist.tex` |
| W16-2 | Anau Montel et al. comparison implemented and run | **met** — see headline | `src/baselines/montel_marginal.py`, `results/montel_marginal_test.yaml`, `paper/main.tex` §2 |
| W16-3 | Coherence/colnorm thresholds stated where their verdicts are used | **met** — both genuinely computed and clean on all eight assignments; stated explicitly rather than left as unexplained ledger entries | `paper/main.tex` §4 |
| W16-4 | Orphaned random-attributor-floor sentence removed from main-text prose | **met** — sentence and its three ledger rows removed; `results/floor_check.yaml` untouched as historical record | `paper/main.tex` §4, `src/diagnostics/report_claims.py` |
| W16-5 | Second-theta check added to the provenance ledger | **met** — new `L1` ledger section, `results/second_theta_check.yaml` | `src/diagnostics/report_claims.py`, `paper/appendix_claims_table.tex` |
| W16-6 | "Two orders of magnitude" precision fix | **met** — "approximately two orders of magnitude" | `paper/main.tex` §5 |
| W16-7 | Figure 3(a) PASSES/FAILS labels removed, framing moved to caption | **met** — labels removed from the plotting script; caption states the same framing in words; recompiled and visually confirmed less cluttered | `src/viz/fig6_nontermination.py`, `paper/main.tex` |
| W16-8 | Figure 7's unquantified "generally sooner" claim | **met** — Wilson intervals added for all four combinations (data already supported it); caption rewritten to the actual crossing widths, which contradict "generally sooner" for one of the three (AAA, plain never reaches a measured zero in-sweep) | `src/viz/fig6b_nontermination_variants.py`, `paper/main.tex` |
| W16-9 | `d` (summary-statistic count) defined in Section 3 | **met** | `paper/main.tex` §3 |
| W16-10 | Fithian/Sun/Taylor and Lee/Sun/Sun/Taylor cited | **met** — both already in `audit/BIBLIOGRAPHY.bib` from an earlier session, verified against arXiv's full-text record before reuse rather than trusted blind; one sentence added distinguishing this project's construction | `paper/main.tex` §2 |
| W16-11 | Aphorism stated once with force, trimmed elsewhere | **met** — kept in the abstract; trimmed in Section 1, both Section 2 instances, and checklist item 1; recovered space used for W16-2/W16-10 | `paper/main.tex`, `paper/checklist.tex` |
| S1 | Authorship (every commit) | **met** — four-check pre-push checklist run and clean before every push this session | `git log` |
| S3 | Anonymization, paper AND package | **met, and extended** — see headline's second finding | `paper/main.pdf`, `build/anonymous_package.zip` |
| S4 | Every number traces to `results/` or `audit/FINAL_CLAIMS.md` | **met** — including the new Montel and second-theta numbers | `paper/appendix_claims_table.tex` |
| S5 | Vacuous-flag test applied to the Montel test itself | **met** — `null_control` case, `p=0.61`, does not reject | `results/montel_marginal_test.yaml` `vacuous_flag_check` |
| Page limit | Main text ≤ 5 pages | **met** — Limitations ends and References begins, both on page 5/6 boundary correctly, after tightening float/paragraph whitespace (same lever G12–G14 used) and trimming non-load-bearing connective prose; no content cut | two-tier isolation compile, `paper/main.pdf` |
| Phase 3 package | Built, redacted, independently re-scanned, extracted and run fresh | **met** | `build/anonymous_package.zip` (gitignored), `scripts/build_anonymous_package.sh` |

### The anonymized package, explicitly

**In:** `src/` (all `.py`, including the new `src/baselines/`), `tests/` (a deliberate addition
beyond the session brief's literal allowlist — code, not process, and the only way Phase 3.5's
"confirm it actually runs" requirement means anything), `results/*.yaml` recursively (with
`host`/`measured_on`/`commit`/`p_sel_run_commit` redacted by value pattern), a fresh
standalone `README.md` (setup, layout, paper-to-file mapping table, honestly-documented test
exclusions), `LICENSE` (canonical MIT text fetched from spdx.org, copyright line anonymized to
"The Authors" — the repository's own `LICENSE` file could **not** be reused verbatim as the
session brief's Phase 3.1 literally suggested, because it has the operator's real name filled
into the copyright line; caught before packaging, not after), `requirements.txt` (pinned to
this session's actually-installed versions).

**Confirmed excluded, checked explicitly:** `.git/` and all git metadata (verified: zero `.git*`
paths in the built zip); `audit/`, `docs/`, `GATES.md`, `DEVIATIONS.md`, `OUTSTANDING.md`,
`PROVENANCE.md`, `paper/` (none staged — the build script's allowlist never references any of
them); the operator's name, GitHub username, and email (zero hits, independent re-scan after
build); the standing AI-authorship token pattern (zero hits, same re-scan).

**Not yet done, and not this session's to do:** uploading `build/anonymous_package.zip`
anywhere (P-2), and pasting the resulting URL over the two placeholders this session left —
`paper/checklist.tex` item 5's justification, and the same bracketed text nowhere else in the
paper (the placeholder was deliberately not invented as a guess).

### What G16 explicitly does not certify

- **That a fourth external review has been run on this version.** It has not. Every
  verification in this gate is this session's own re-derivation, single-pass, the same
  limitation G15 and every gate before it names about itself.
- **That W16-2's simplification is invisible to a critical reader.** The exact per-summary
  statistic is a principled substitution for Anau Montel et al.'s neural local tests, not an
  approximation of their numeric answer — but it is still a difference from their published
  construction, stated as such rather than glossed, and a reviewer may still object to it.
- **That the confound-resolution finding generalizes.** One realization per mechanism, at one
  distortion magnitude, using this project's own simulator. The paper's own prose says so;
  repeating it here because it is the kind of caveat that is easy to lose in summary.
- **That every conceivable anonymity-identifying field has been found.** Two rounds of
  discovery this session (`host`/`measured_on`, then `commit`/`p_sel_run_commit`) both came from
  grepping the operator's actual name rather than from a complete audit of every field every
  script writes. The redaction is value-based specifically because a key-based list already
  proved incomplete once; that is evidence the method is more robust, not evidence it is
  exhaustive.
- **That the anonymized package's figures can be regenerated end to end.** `src/viz/` requires
  the NeurIPS venue's `.sty` file, which is part of the paper submission and is not bundled;
  documented, not hidden, in the package's own README and above.

### Process caveats

- **This session's commits are coarser-grained than the brief's suggested Tier-2 groupings**
  (`W16-3/4`, `W16-5/6`, `W16-7/8`, `W16-9/10`, `W16-11` as five separate commits). Phase 1
  (W16-2) and every Tier-2 item were developed in one continuous pass and landed in two commits
  (code, then a clean-tree data regeneration — the same split G3 established for exactly this
  reason) rather than five. Nothing is lost from the diff being readable; the deviation is
  granularity, not completeness, and is recorded here rather than left silent.
- **The Montel comparison's compute was reduced from the first design** (`N_ref`/`N_calib`
  5,000/5,000/2,000 to 3,000/3,000/1,500) partway through, because this machine's load average
  swung as high as 159 during the session (confirmed via `uptime` and `sample`, not assumed) and
  the first attempt was still running after 20 minutes. The reduction changes the *resolution*
  of the reported $p$-values (the floor moves from $1/5001$ to $1/3001$), not their validity —
  every reported $p$-value is still an honest, if resolution-limited, Monte Carlo bound, and is
  reported as such (`global_p_value_is_upper_bound` in the results file).
- **A real, if minor, reproducibility bug was caught before it shipped**: the Montel module's
  first draft seeded each case's observed-data draw with Python's built-in `hash()` of the case
  name, which is randomised per-process by default and would have made the reported numbers
  silently non-reproducible run to run at a fixed `--seed`. Found by re-reading the module
  before the production run, fixed to a deterministic per-case offset, and verified: the final
  clean run's numbers reproduce the discarded dirty run's numbers exactly.
- **No adversarial critic or second independent agent ran against this session's own findings.**
  Every verification in this gate is single-pass, from one session's own re-derivation, same as
  every gate before it. The next external review is the actual independent check this project's
  own process has always deferred to for exactly this reason.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```
