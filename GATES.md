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
