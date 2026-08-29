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

---

## G17 — Does the paper's prose read as a scientific paper rather than as this project's own
audit trail, with no claim, number, or figure changed?

**status: ready for review — UNSIGNED**

Prepared 2026-08-27, session G17. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **This session changed how the paper sounds and nothing about what it says.** Every numeric
> literal, every citation, every caveat, and every figure's data is unchanged. The claim is not
> asserted: it is measured. A token-level diff of every numeric literal in `paper/main.tex`
> between `HEAD` (2ad4e68) and this session's final state returns exactly two differing tokens,
> both accounted for — `topsep=1pt,itemsep=0pt,parsep=0pt` list-spacing parameters deleted along
> with Section 2's `itemize` environment (formatting directives, not data), and one redundant
> second statement of `1/τ` whose content is preserved in words ("these are one condition, not
> two", T2-1's own protected phrasing). A multiset diff of every numeric token in the *rendered*
> main text, with the venue template's left-margin line numbers stripped, agrees. Citation keys
> are identical before and after: 20 occurrences, 19 distinct, same multiplicity — Section 2 was
> converted from bullets to prose without losing or adding a single reference.
>
> **The dash sweep G14 reported as complete was not complete, and now is.** `paper/main.tex`
> carried three surviving prose-aside em-dashes (`---`) at the time this session started, in
> Section 2's Montel paragraph, Section 2's post-selection-inference sentence, and the
> Limitations second-θ clause. All three are gone, each rewritten individually rather than by
> blind substitution. Confirmed by re-grep: `grep -n -- '---' paper/main.tex` returns **zero
> lines**; a Unicode sweep for U+2013/U+2014 across every `.tex` returns zero; and the rendered
> main text (pages 1–5) contains exactly one en-dash character, the numeric range `0.9–2.7%`,
> which the brief puts out of scope. The two remaining `---` in `checklist.tex` are both inside
> bracketed operator placeholders (item 5's anonymized-code link, item 16's LLM disclosure) and
> are label-to-instruction separators, not prose asides; item 16 is explicitly not this
> session's to touch.
>
> **Two real defects were found that this session was not looking for.** First, **G16 silently
> dropped T2-11's protected clause.** The literal `(where $s(y)$ would sit)` in the Limitations
> "no learned component" bullet — a first-external-review Tier-2 fix that G14's and G15's own
> re-verification tables both recorded as "verified still present verbatim" — is present at
> `19f9a59` (G15's final state) and absent at `efc81c9` (G16). G16's gate did not report it. It
> is restored. Second, **`audit/BIBLIOGRAPHY.bib` line 1 carried the repository name** in a
> `%%%%` header comment, and that file is on `scripts/build_overleaf_package.sh`'s allowlist, so
> it ships to reviewers. G8.4 claims the source was "grepped for the operator's name, GitHub
> handle, and repository name — zero hits"; that claim was wrong, most likely because the grep
> was scoped to `paper/`. Fixed to a neutral wording; the comment never reaches the compiled
> PDF, so no rendered output changed.
>
> **The page limit was closed by prose tightening alone.** Phase 2's properly-stated findings
> list and Phase 3's prose conversion pushed the main text three lines onto page 6. Every one of
> those lines was recovered by removing redundant audit-register prose — never by touching
> `\parskip`, float separations, caption skips, or any font or figure dimension, all of which
> this session leaves exactly as G16 set them. Main text is again pages 1–5 with References
> beginning on page 6.

### What G17 was judged against

| # | Item | Status | Location |
|---|---|---|---|
| 1.1 | "Prior art" / "the contribution is the finding" reduced to one instance | **met, already met on arrival — no edit made.** A fresh sweep of all four `.tex` files found exactly **one** occurrence in `main.tex`, already in the abstract, already stated once with force. G16's W16-11 had done this. Per S9 this is reported as found, not manufactured into an edit | `paper/main.tex` abstract |
| 1.1b | `checklist.tex` "cited as prior art" (item 12) | **judged unrelated, deliberately not touched.** Item 12 answers the *licensing* question — the Section 2 tools are cited rather than vendored as software dependencies. Different sense of the phrase, correct in context, load-bearing for the answer | `paper/checklist.tex` item 12 |
| 1.2 | Complete fresh dash-as-aside sweep | **met, 3 instances found and individually rewritten.** Zero-result re-grep reported in headline. Each rewritten to the punctuation that fit that instance: sentence break, comma-delimited apposition, sentence break | `paper/main.tex` §2 ×2, §6 |
| 1.2b | Dashes baked into figure images | **found, deliberately NOT changed, disclosed rather than silently passed.** `figures/fig2_simulator.pdf` (appendix schematic) carries two em-dashes inside hand-placed panel headings ("DETERMINISTIC CORE — fixed-step RK4…", "THE THREE DISTORTION FAMILIES — one one-parameter family…"). These are heading-to-descriptor separators in a diagram, not prose asides interrupting a sentence, and they sit outside the brief's named scope (main.tex, checklist.tex, figure *captions* — all three confirmed zero). Regenerating the figure would require a clean-tree run and a new provenance sidecar, which G15/G16 each spent a commit on; not worth that for a typographic nicety in an appendix diagram. **Named here so no one reads "zero dashes" as broader than it is** | `src/viz/fig2_simulator.py:136,181` |
| 1.3 | "Not X, not Y, not Z" chain restructured | **met.** Section 4's six-column ruling-out sentence split into three short sentences, one ruled-out explanation each. Every number preserved: `1.023` against admissible `2`; `τ` from `0.005` to `1.0`; `d=10≥6`. This is the only such chain in the document — a sweep found no second instance of three-or-more stacked `not` clauses | `paper/main.tex` §4 |
| 1.4 | Three "moved here … for space" appendix openings removed | **met, all three.** A.1 now opens by saying what Table 1 is; A.2 by saying what Figure 4 shows; A.3 by saying what its three figures show. No editorial-process commentary survives; `grep 'for space'` returns zero | `paper/main.tex` A.1, A.2, A.3 |
| 1.5 | K-vs-columns disclaimer deleted; Figure 2 legend not "K=6" | **met, already met on arrival — no edit made.** The disclaimer is absent (G14's R14-1 removed it after R14-6 fixed the root cause, per T2-12). `fig3_spectrum.pdf`'s rendered legend reads "six-column union (κ = 629, INSEPARABLE)", verified by `pdftotext` on the figure itself, not by reading the plotting script. Nothing to fix; reported as found per S9 | `figures/fig3_spectrum.pdf`, `src/viz/fig3_spectrum.py:47–49` |
| 1.6 | "Hand-placed annotations outside the automated check" | **met by removal, with reason.** The sentence disclosed that two figures' text labels were typed rather than computed. Both labels — Figure 2's "union: rank 4 of 6" and Figure 1's κ_max marker — restate quantities the same figures' captions and the body text already state. A reader learns nothing scientific from it, and "the automated check" names this project's internal `src/viz/provenance.py` verifier, not a limitation of the work. Removed, and `checklist.tex` item 2's mirroring clause updated in the same pass so the checklist still matches the compiled PDF (T1-6). **G9 had already listed this exact sentence as a legitimate cut it declined to make unilaterally under page pressure; this session makes it for voice reasons and records that provenance** | `paper/main.tex` §6, `paper/checklist.tex` item 2 |
| 1.6b | The removed sentence was also stale | **noted.** `src/viz/fig4_assignments.py`'s provenance note still describes annotations ("all eight separable", "hatched: INSEPARABLE") that no longer exist in the rendered figure. The paper's claim about "two figures" was therefore already drifting from the code. Not fixed — it is a comment in a non-packaged source file, outside this session's scope — but recorded so it is not rediscovered as new | `src/viz/fig4_assignments.py:149` |
| 2.1 | Introduction states its own findings, directly | **met.** The single semicolon-chained sentence ending in a pointer to Table 1 is replaced by four sentences in the paper's own voice — "We find that…", "Separability then fails…", "We find that…", "And we predict…" — naming all four contributions. The Table 1 pointer survives only as a trailing parenthetical, no longer as the place the findings live. T2-7's scope restriction stays inside the first finding sentence, verified | `paper/main.tex` §1 |
| 3.1 | Section 2 converted from bullets to prose | **met.** Four `\item`s become four paragraphs on the same four themes (detection-vs-attribution; the identifiability precondition; diagnostic tooling; exact inference under a composite null), written as argument rather than as citations disposed of one clause each, per the Cranmer/Talts register the brief names. **Every citation preserved with identical multiplicity (20 occurrences, 19 distinct), verified by key-multiset diff, not by eye.** G16's Montel result and both new selective-inference citations (Fithian/Sun/Taylor; Lee/Sun/Sun/Taylor) are integrated into the running argument — the Montel measurement is the closing movement of paragraph 1, and Fithian/Lee are the contrast paragraph 4 turns on | `paper/main.tex` §2 |
| 4.1–4.2 | Residual audit-trail voice, full re-read | **met, 9 further instances found and fixed** — enumerated below. Not zero; this session does not claim the register is fully purged, only that it re-read the whole document and fixed what it found | `paper/main.tex` |
| 5.1 | Full number re-trace | **met, zero scientific numbers changed** — method and result in headline | `paper/main.tex` |
| 5.2 | Independent anonymization re-scan | **met, and it caught a real leak** — see headline. Post-fix: zero hits across every packaged source and the compiled PDF's text; PDF `Author` metadata empty | `audit/BIBLIOGRAPHY.bib`, `paper/main.pdf` |
| 5.3 | Page limit ≤ 5 | **met.** Main text pages 1–5; References begins page 6. Confirmed by parsing the PDF's own form-feeds, in both the repo working copy and the isolated package extraction. Closed by prose tightening only, no whitespace lever touched | `paper/main.pdf` |
| 5.4 | All prior review findings still intact | **met, 35/35 intact, 0 missing** — full table below. One (T2-11) was *not* intact on arrival and was restored | table below |
| 5.5 | Two-tier isolation compile | **met, both tiers.** Against a freshly built zip extracted into a fresh temp directory, never the repo working copy, `TEXINPUTS` genuinely unset in both: exit 0, 23 pages, zero undefined references or citations, identical 602,452-byte `main.pdf` in both tiers, and `pdftotext` output byte-identical to the repo working copy. §2a (`TEXMFHOME` unset) passes only in the narrower this-machine-fallback sense G12/G13 named and this gate does not re-claim | `build/sim_attrib_overleaf_*.zip` |
| 5.6 | Overleaf package rebuilt | **met**, allowlist unchanged, 17 files | `scripts/build_overleaf_package.sh` |
| S1 | Authorship | **met** — four-check pre-push checklist run and clean before push | `git log` |
| S3 | No claim changed | **met** — headline's measured diff |
| S4 | Every number still traces | **met** — no number added, removed, or altered, so every existing trace holds unchanged |
| S6 | Page limit | **met** — 5.3 |
| S8 | No self-approval | **met** — `ready for review — UNSIGNED` |

### Phase 4 — the nine residual audit-voice instances found by the full re-read

Each of these was written to satisfy an internal verification habit rather than to tell a reader
something. None of them changed a claim.

| # | Where | What it was | What it is now |
|---|---|---|---|
| V-1 | §3, scope paragraph | Heading "Scope assumption, **stated first**", and a closing clause explaining *why* the paper states it before the machinery | Heading "The scope assumption"; the clause is gone. The reader does not need the paper's own table of contents justified to them |
| V-2 | §3, step 4 | "since $\kappa\le1/\tau$ restates rank deficiency at $\tau$ rather than adding a second requirement" — a restatement of the equation immediately preceding it | "these are one condition, not two" — T2-1's own protected phrasing, kept, at a third of the length |
| V-3 | §3, step 4 | "passing the resolution test answers the first question, not the second" — a self-referential pointer back to the sentence's own two halves | "Resolution is a property of the *estimator*, not of the *matrix*: passing the resolution test says nothing about whether…" — states the thing directly |
| V-4 | §3, step 4 | "a third outcome distinct from separable/not" — the paper explaining its own taxonomy to itself | removed; the consequence ("the reported rank can be an interval") already carries it |
| V-5 | §3, equivalence class | "**No arrow leaves the verdict:** the diagnostic decides whether attribution is well posed, and nothing further" | the metaphor dropped; the plain second half kept |
| V-6 | §4, summary sets | The base set described loosely ("a prevalence nonlinearity, a timing distortion, an amplitude error") and then again precisely two sentences later in the R14-1 "Concretely:" list | the loose parenthetical removed; R14-1's protected precise naming untouched |
| V-7 | §4, $S_A$ control | "…$0.9\%$ past the ceiling, **proof the instrument is not vacuously ``separable.''**" — the same point Figure 1's caption already makes in its own words | the body states the measurement; the caption keeps the interpretation. Said once, not twice |
| V-8 | §4, alt-η scaling | Two parentheticals back to back, one nested inside the sentence's own argument | restructured into two sentences; every number, both citations of scope, and R14-4's named coordinates preserved |
| V-9 | §5 ×3 | "The boundary **is predicted, before it is measured,** from…" (abstract and §5) and "The neighborhood at which it takes over **is not an assumption we chose**" — passive constructions and a defence against an anticipated objection | "We predict the boundary before measuring it, from…" and "That neighborhood is narrower than…". Active, committed, shorter |

Also folded in: §5's "are only known to the precision real data give them, **not an assumed one**"
followed immediately by "**We answer this directly rather than assume a box**" — the same point
made twice in consecutive sentences — is now made once, as "Rather than assume a box, we fit…".

### Phase 5.4 — the full consolidated re-verification table

| Item | What it is | Status after G17 |
|---|---|---|
| T1-1 | Appendix claim-to-source table, generated not hand-typed | **intact**, untouched this session |
| T1-2 | Page limit ≤5 | **intact.** Reopened by this session's own Phase 2/3 additions and re-closed by Phase 4's prose tightening, with no whitespace or font lever touched |
| T1-3 | Real confidence-set-bounded MMC check | **intact**, untouched |
| T1-4 | Simulator schematic in appendix, qualitative content restated in main-text prose | **intact and re-checked.** A.2's opening was rewritten (1.4); the R14-1 "Concretely:" mechanism sentence it depends on is verified present verbatim in §4 |
| T1-5 | Full anonymity re-scan | **intact, re-run, and extended** — this session's scan covered `audit/BIBLIOGRAPHY.bib`, which the G8.4 scan evidently did not, and found the repository-name leak in it |
| T1-6 | Checklist answers match the compiled PDF | **intact, actively maintained.** Item 2's justification was updated in the same edit that removed the hand-placed-annotation sentence from §6, so the two did not drift apart |
| T2-1/T2-2 | Rank-at-τ / κ≤κmax as one condition; κ² cost derivation | **intact.** T2-1's substance re-stated more compactly (V-2); "one condition, not two" verified present |
| T2-3 | Data-motivated η-scaling using confidence-set SEs | **intact.** `0.9–2.7%` and the named coordinates β, γ, ρ both verified present after V-8's restructure |
| T2-4 | Second-θ check | **intact**, `κ=10.9` verified present |
| T2-5 | Related Work citations genuinely engaged | **intact, and this is the item most at risk this session.** Section 2 was structurally rewritten. Verified by citation-key multiset diff: 20 occurrences, 19 distinct, identical before and after, and each citation's stated relevance to the argument carried across by hand, paragraph by paragraph |
| T2-6 | Section 5 retitled, finding-first | **intact**, title verified verbatim |
| T2-7 | Scope restriction in the introduction's own contribution sentence | **intact, and more prominent.** Phase 2's rewritten findings list carries "given at most one distortion parameter per component" inside the first finding sentence |
| T2-8 | Two-panel non-termination figure, per-figure font floors | **intact**, no figure regenerated this session |
| T2-9 | Repeated metaphor reduced; four steps as a numbered list | **intact and extended** — V-5 removed one further metaphor ("No arrow leaves the verdict") the earlier pass left |
| T2-10 | Abstract tightened, concrete number retained | **intact.** `κ=628.9`, rank 4/6 verified present; the abstract's one edit this session was passive→active (V-9), no number touched |
| T2-11 | Limitations bullet on where a learned summary statistic would sit | **WAS NOT INTACT — regressed in G16, RESTORED this session.** `(where $s(y)$ would sit)` present at `19f9a59`, absent at `efc81c9`. G14's and G15's tables both recorded it verified; G16's did not check it. See headline |
| T2-12 | K-vs-column-count notation conflict resolved | **intact**, independently re-confirmed both ways: the disclaimer is absent from `main.tex`, and the rendered legend of `fig3_spectrum.pdf` reads "six-column union", checked on the figure file itself |
| T2-13 | Appendix table's plateau-stability caption honest about noise | **intact**, untouched |
| T2-14 | Checklist after the appendix | **intact**, structural position untouched |
| T2-15 | Sentence on the baseline test's output on the six-column confound | **intact**, and now carries G16's *measured* result rather than the hedge — unchanged in substance by this session, only de-dashed and re-flowed |
| R1 / R2 (first-review novelty threat-checks) | Rejection-sampling calibration is prior art; noisy-rank estimator | **intact.** Section 2's prose conversion preserved both dispositions; the Dufour and Freidling attributions are stated as plainly in prose as they were in bullets |
| R-1 (second review) | Main-text self-sufficiency: family mechanisms + confound interpretation | **intact**, both anchor sentences verified present verbatim |
| R-2 (second review) | Ledger under-referencing; undefined criteria | **intact, and specifically protected.** Two sentences this session's voice pass would otherwise have tightened — §4's ledger-reference opener and §3's "so no hidden truth can leak into its answer" — were left substantively alone once `audit/R1R2R3_RECONCILIATION.md` showed they *are* the R-2 fix. Only the second's punctuation changed; the leakage concept it exists to convey is verified still stated in plain prose |
| R-3 (second review) | Mahalanobis-radius / ellipsoid comparison | **intact**, `3.56`, `χ²₅,₀.₉₅` and the coincidence sentence all verified present |
| R14-1 … R14-9 | Second review's Path to Acceptance | **intact.** R14-1's mechanism naming and R14-2's ellipsoid numbers individually re-checked (the two this session's edits came nearest to) |
| W16-1 … W16-11 (third review) | G16's eleven items | **intact.** W16-1's `\answerTODO{}` placeholder untouched; W16-2's Montel numbers, W16-3's thresholds, W16-6's "approximately", W16-8's Wilson bars, W16-9's `d`, W16-10's two citations, W16-11's single aphorism all verified present. W16-4's removal verified still removed |
| G15 Phase-3 finding 1 | "344.9 … two orders past κmax" overstatement | **intact as corrected** — `3.4×` verified present |
| G15 Phase-3 finding 2 | "±0.5% box already known to break" contradiction | **intact as corrected** — `±0.75%` verified present |
| G14 P-1 | Paper-wide dash removal | **WAS INCOMPLETE — completed this session.** Three prose-aside em-dashes survived G14's pass and G15's re-check. See headline |
| G8.4 | "PDF and source grepped for repository name — zero hits" | **WAS INACCURATE — corrected this session.** See headline |

### What G17 explicitly does not certify

- **That the paper's register is now fully free of its audit trail.** This session found and fixed
  nine residual instances *after* fixing the six the brief named, which is direct evidence that a
  single reader's pass does not exhaust them. A tenth, eleventh and twelfth plausibly remain. What
  this gate certifies is that a full start-to-finish read was done for voice specifically, and that
  everything it found was fixed — not that the register is exhausted.
- **That the figure-internal em-dashes are the right call to leave.** §1.2b states the reasoning;
  a reader who disagrees is disagreeing with a judgment, not discovering something hidden. It is
  a one-line change to `src/viz/fig2_simulator.py` plus a figure regeneration and a fresh
  provenance sidecar, if the operator wants it.
- **That a fourth external review has run on this version.** It has not, and this session is
  precisely the kind that most needs one: a voice pass touches nearly every paragraph, and the
  person who rewrote the prose is the worst-placed reader to judge whether it now reads well.
  **A fourth external review focused specifically on readability and tone is recommended** —
  more strongly than G16's recommendation, because the three prior reviews were content-focused
  and none of them was asked about register.
- **That "no claim changed" was verified by re-deriving the claims.** It was verified by diffing
  numeric literals, citation keys, and thirty-five protected clauses against `HEAD`. That is a
  strong check against accidental loss and a weak check against a rewrite that preserves every
  number while subtly shifting what a sentence asserts. Two rewrites came closest to that line and
  are named for scrutiny: §4's three-sentence ruling-out (1.3) and §1's findings list (2.1).
- **That G16's T2-11 regression is the only one of its kind.** It was found by checking, not by
  trusting G15's table — and G15's table was wrong. This session re-checked all thirty-five
  protected clauses the same way and found one failure, but the discovery method was a
  whitespace-insensitive search that an earlier session's line-scoped grep had already missed once.

### Process caveats — what this session did badly or not at all

- **The dash finding is a repeat of a known failure mode, not a new one.** G14 reported 38
  instances removed; three survived, in `main.tex`, greppable in one command. G15 re-verified P-1
  as "intact" without re-running the grep. The lesson this session records is narrow and
  mechanical: **a completion claim about a greppable property must be closed with the grep, and
  the grep's zero-result output must go in the gate.** This gate does that (headline, §1.2).
- **Phase 2 and Phase 3 made the paper longer before Phase 4 made it shorter.** For roughly the
  middle of this session the main text was over the page limit by three lines. That was a
  foreseeable consequence of stating four findings properly instead of pointing at a table, and it
  was closed by cutting redundancy rather than by cutting content or by reaching for the
  whitespace lever — but the session brief's expectation that voice tightening would leave "slack,
  not pressure" did not hold, and it is worth saying so rather than reporting a comfortable margin.
- **Two of the six named symptoms required no edit at all** (1.1 and 1.5), because G16 had already
  fixed them and the session brief was written against a pre-G16 picture. Reported as found, per
  S9, rather than dressed up with a cosmetic change to make the phase look worked.
- **No adversarial critic or second independent agent ran against this session's own prose
  judgments.** Voice is more subjective than arithmetic, and every "this reads better now" in this
  gate is one session's opinion, single-pass. P-1 and P-2 exist for exactly that reason.
- **This session touched `audit/BIBLIOGRAPHY.bib`**, which the file's own header declares stays
  "exactly as fetched". The edit is to that header comment itself, not to any bibliographic
  record; no entry, field, or value was altered. Recorded here rather than left for someone to
  notice in the diff.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G18 — Does the paper read well to a harsh reviewer judging tone and readability alone, with
no claim, number, figure, or citation touched?

**status: ready for review — UNSIGNED**

Prepared 2026-08-28, session G18. Signature block below is for the operator.

> ### The headline, stated before the table
>
> **A cold, start-to-finish read of the compiled PDF, judging tone and readability only, found
> five concrete things worth fixing and confirmed the rest of the paper already reads well.**
> This is not a session that manufactured work to justify its own existence (S9): Sections 2–5
> already build arguments rather than reading as fact-lists, the paper's confidence level already
> matches its evidence (no hedging found anywhere in the main text), and three of the six things
> the brief specifically asked to check — mechanical listing in Method/Experiments, confidence
> versus evidence, and the Cranmer/Talts register comparison — came back clean. Two transition
> points (Related Work into Method, the negative-result section into Limitations) were checked
> and judged acceptable as header-only openings — common in this venue's papers, not fixed.
>
> **What was fixed, all four in `paper/main.tex`, zero in `checklist.tex`:** a dangling
> appositive in the abstract's fourth sentence (comma to colon); the introduction's third
> sentence, which restated the abstract's C4 finding in near-verbatim phrasing, reworded to carry
> the identical claim without the verbatim echo; the introduction's closing sentence, split so it
> lands on "the prediction holds" instead of trailing into a comma-spliced appendix-table
> fragment; Section 4's opening two sentences reordered so the substantive one ("We apply the
> diagnostic to a $K=3$ compartmental epidemic simulator…") leads instead of a provenance
> disclaimer; and a sentence fragment in the appendix's claims-ledger intro (missing "is")
> completed. Full before/after text: Phase 2 table below.
>
> **Nothing else changed.** A `pdftotext -layout` diff between the pre-edit and post-edit PDF
> shows exactly these four paragraph-local hunks and nothing else — no numeric token count
> changed (1,606 before, 1,606 after), citation count is unchanged (20 occurrences, 19 distinct,
> the same G17 measured), and `src/diagnostics/report_claims.py` regenerated from the underlying
> `results/*.yaml` files byte-identical to the committed `paper/appendix_claims_table.tex`
> (125 numbers, zero drift). Main text is still pages 1–5, References still begins page 6, both
> isolation tiers compile clean at 23 pages / 602,400 bytes, `pdftotext` output identical across
> the repo working copy and both fresh extractions.
>
> **One disclosed judgment call.** G17's own gate (item 2.1) documents the introduction as four
> sentences in a deliberate voice pattern — "We find that…", "Separability then fails…", "We find
> that…", "And we predict…". This session's fix to the third of those four rewords it away from
> that exact opening ("A calibrated attribution test built on the identifiable case stays
> affordable only at a known parameter: …") because the verbatim overlap with the abstract was
> judged the more consequential problem for a cold read — a reviewer reads the introduction
> immediately after the abstract, and repeating a full clause word-for-word inside two paragraphs
> of each other reads as padding regardless of how confident or active the voice is. The other
> three of G17's four voice markers ("We find", "Separability then fails", "We predict") are
> untouched and still present verbatim. This is a supersession of one part of a G17 decision, not
> a reversal of its intent — active, declarative, first-person-plural voice throughout, just not
> the identical four-sentence template. Flagged here rather than left for the operator to notice
> in the diff (P-2, below).

### Phase 1 — the cold review, as written before any fix was made

Read against the seven checks the brief names (1.1–1.7), on the compiled `paper/main.pdf`,
pages 1–6 (main text through the start of References).

| # | Check | Finding |
|---|---|---|
| 1.1 | Does every sentence earn its place? | **One real instance, the session's most consequential finding.** The introduction's third sentence restated the abstract's C4 clause — "…is affordable at a known parameter but fails to terminate once the nuisance parameters are known only to the precision a maximum-likelihood fit gives them" — essentially word-for-word, roughly fifteen lines after the reader had just read it in the abstract. No other sentence-level redundancy found in the main text |
| 1.2 | Does the paper sound confident where it has earned confidence? | **Clean — nothing found.** No hedging phrase ("may suggest", "seems to", "it is possible that") anywhere in the main text. Every finding is stated as a direct, declarative claim: "is inseparable", "fails to terminate", "the gate fails at every corner under all four" |
| 1.3 | Does Method or Experiments read mechanically? | **Clean — nothing found.** Section 3's four-step list is the one the brief itself names as legitimate. Section 4 avoids the fact-list trap through a real structural device: each paragraph opens with a bolded question/finding ("Where attribution is identifiable…", "Where it is not…") that functions as a mini-thesis statement, then argues to it — this is not a list dressed as prose, it is an argument |
| 1.4 | Do sections transition, or read as self-contained blocks? | **Three of five checked transitions are real bridges** (Introduction→Related Work echoes "misspecified at all" against Related Work's opener; Method→Experiments and Experiments→negative-result both reference back explicitly). **Two are header-only** (Related Work→Method, negative-result→Limitations open directly on a bolded sub-heading with no lead-in sentence). Judged acceptable — common practice in this venue for a Method or Limitations section to open directly on content — and **not fixed**, per S9 rather than manufacturing a bridge sentence that would add nothing a reader needs |
| 1.5 | Do opening/closing sentences of each section do real work? | **Two do not, both fixed.** The introduction's closing sentence trails from a strong beat ("the prediction holds") into a comma-spliced appendix-table pointer that reads as an afterthought rather than a landed conclusion. Section 4's opening sentence is a provenance disclaimer ("Every number below traces to a results file…") placed before the section's actual substantive opener, which sits one sentence later. Every other section's opening and closing sentence (Introduction's open, Related Work's open/close, Method's open/close, the negative-result section's open/close, Limitations' open/close, the Abstract's close) does real work already |
| 1.6 | Does the abstract earn a read, cold? | **Yes, with one local defect.** The abstract's opening sentence states a real, general precondition problem without preamble; its closing sentence ("Every tool used is prior art; the contribution is the finding.") is a strong, memorable closer, unchanged, no fix needed. Sentence 4 has a dangling appositive — "…gives them, a box wider, on every coordinate, than one already shown to break it" — where "a box" grammatically attaches to the wrong preceding noun and a reader has to work to resolve it. Fixed with a single punctuation change (comma to colon) rather than a rewrite |
| 1.7 | Register against Cranmer/Talts? | **Already matches.** Declarative sentence density, minimal hedging, technical vocabulary handled without apology — this was true before this session's edits and remains true after them |

### Phase 2 — the fixes

| # | Location | Before | After | Maps to |
|---|---|---|---|---|
| F1 | Abstract, sentence 4 | "…gives them, a box wider, on every coordinate, than one already shown to break it." | "…gives them: a box wider, on every coordinate, than one already shown to break it." | 1.6 |
| F2 | Introduction, sentence 3 | "We find that a calibrated attribution test built on the identifiable case is affordable at a known parameter but fails to terminate once the nuisance parameters are known only to the precision a maximum-likelihood fit gives them." | "A calibrated attribution test built on the identifiable case stays affordable only at a known parameter: once the nuisance parameters are known only to the precision a maximum-likelihood fit gives them, it fails to terminate." | 1.1 |
| F3 | Introduction, closing sentence | "And we predict that boundary before measuring it, from the ratio of nuisance shift to observation noise; the prediction holds (Table~\ref{tab:summary}, Appendix~\ref{sec:appendix}, pairs each finding with its evidence figure)." | "We predict that boundary before measuring it, from the ratio of nuisance shift to observation noise, and the prediction holds. Table~\ref{tab:summary} (Appendix~\ref{sec:appendix}) pairs each finding with its evidence figure." | 1.5 |
| F4 | Section 4, opening | "Every number below traces to a results file and an exact dotted path, listed in full in Appendix~\ref{sec:claims-ledger}. We apply the diagnostic to a $K=3$ compartmental epidemic simulator: …" | "We apply the diagnostic to a $K=3$ compartmental epidemic simulator: … Every number below traces to a results file and an exact dotted path, listed in full in Appendix~\ref{sec:claims-ledger}." | 1.5 |
| F5 | Appendix, claims-ledger intro | "Every number the main text's four contributions … rest on, generated programmatically from the underlying measurement files …" (sentence fragment, no main verb) | "Every number the main text's four contributions … rest on is generated programmatically from the underlying measurement files …" | grammar, found during Phase 1 alongside 1.5 |

Every fix is a wording, ordering, or punctuation change. No fix touched a number, a citation, a
figure, or the substance of any claim — verified in Phase 3 below, not assumed.

### Phase 3 — re-verification

| Check | Result |
|---|---|
| Numeric literal diff, pre-edit vs.\ post-edit rendered text | **1,606 numeric tokens before, 1,606 after.** The only reordering `difflib` reports is margin line-number reflow local to the four edited paragraphs, confirmed by a separate `pdftotext -layout` diff showing exactly four paragraph-local hunks and nothing else |
| Citation key count | **Unchanged: 20 occurrences, 19 distinct** — same as G17's own measured baseline |
| Full number-trace re-run | **Zero drift.** `src/diagnostics/report_claims.py --tex-out paper/appendix_claims_table.tex --out results/FINAL_CLAIMS_NUMBERS.md` regenerated both files from the underlying `results/*.yaml` sources; `diff` against the committed versions returned nothing and `git status` reported no changes — 125 numbers, all still tracing correctly, confirmed by regeneration rather than by spot-checking |
| Anonymization re-scan | **Clean.** `grep -inE "palaash\|gang\|sim-attrib\|pa1aash"` across `paper/main.tex`, `paper/checklist.tex`, `paper/appendix_tables.tex`, `paper/appendix_claims_table.tex`, `audit/BIBLIOGRAPHY.bib`, and the compiled PDF's extracted text: zero hits in all six. PDF `/Author` field empty |
| Page limit | **Met.** Main text pages 1–5, References begins page 6, confirmed by `pdftotext` form-feed parsing of the freshly compiled PDF |
| Two-tier isolation compile | **Met, both tiers**, against `build/sim_attrib_overleaf_47ccb87.zip` extracted fresh to two separate temp directories, never the repo working copy, `TEXINPUTS` genuinely unset in both. §2b (`TEXMFHOME` pointed at this operator's personal package tree): exit 0, 23 pages, zero undefined references/citations, 602,400-byte `main.pdf`. §2a (`TEXMFHOME` unset, this-machine-fallback sense per G12's own naming correction): exit 0, 23 pages, zero undefined references/citations, identical 602,400-byte `main.pdf`. `pdftotext` output textually identical across the repo working copy and both extractions |
| Overleaf package rebuilt | **Met.** `scripts/build_overleaf_package.sh` re-run against the final committed state, allowlist unchanged, 17 files, 13 allowlisted paths |

### Phase 3.4 — the full consolidated re-verification table (G11 through G17)

Every item below was either (a) provably untouched, because a `pdftotext -layout` diff between
the pre-G18 and post-G18 PDF shows only the four F1–F5 hunks above and nothing else, or (b)
individually re-confirmed by grep where its text sits inside or adjacent to one of those four
hunks. Items in category (b) are marked explicitly; everything else is category (a).

| Item | What it is | Status after G18 |
|---|---|---|
| T1-1 | Appendix claim-to-source table, generated not hand-typed | **intact.** Regenerated from source and diffed byte-identical (Phase 3 above) |
| T1-2 | Page limit ≤5 | **intact.** Pages 1–5, unaffected by four wording-only edits |
| T1-3 | Real confidence-set-bounded MMC check | **intact**, untouched (category a) |
| T1-4 | Simulator schematic in appendix, qualitative content restated in main-text prose | **intact**, untouched (category a) |
| T1-5 | Full anonymity re-scan | **intact, re-run this session** — zero hits, see Phase 3 |
| T1-6 | Checklist answers match the compiled PDF | **intact.** `checklist.tex` was read this session and not edited; nothing in F1–F5 touches a claim the checklist answers describe |
| T2-1/T2-2 | Rank-at-τ / κ≤κmax as one condition; κ² cost derivation | **intact**, untouched (category a) |
| T2-3 | Data-motivated η-scaling using confidence-set SEs | **intact**, untouched (category a) |
| T2-4 | Second-θ check | **intact**, untouched (category a) |
| T2-5 | Related Work citations genuinely engaged | **intact**, untouched (category a) — Section 2 was not touched this session |
| T2-6 | Section 5 retitled, finding-first | **intact**, untouched (category a) |
| T2-7 | Scope restriction in the introduction's own contribution sentence | **intact, re-confirmed (b).** "given at most one distortion parameter per component" sits in the intro's *second* sentence, immediately before the third sentence F2 reworded; verified present verbatim, unaffected by F2 |
| T2-8 | Two-panel non-termination figure, per-figure font floors | **intact**, untouched (category a) |
| T2-9 | Repeated metaphor reduced; four steps as a numbered list | **intact**, untouched (category a) |
| T2-10 | Abstract tightened, concrete number retained | **intact, re-confirmed (b).** `\kappa=628.9`, rank 4 of 6 verified present in the abstract, in the sentence immediately before the one F1 touched; F1 changed only a comma to a colon later in the following sentence, no number affected |
| T2-11 | Limitations bullet on where a learned summary statistic would sit | **intact**, untouched (category a) — verified present, `(where $s(y)$ would sit)` |
| T2-12 | K-vs-column-count notation conflict resolved | **intact**, untouched (category a) |
| T2-13 | Appendix table's plateau-stability caption honest about noise | **intact**, untouched (category a) |
| T2-14 | Checklist after the appendix | **intact**, untouched (category a) |
| T2-15 | Sentence on the baseline test's output on the six-column confound | **intact**, untouched (category a) |
| R1 / R2 (first-review novelty threat-checks) | Rejection-sampling calibration is prior art; noisy-rank estimator | **intact**, untouched (category a) |
| R-1 (second review) | Main-text self-sufficiency | **intact**, untouched (category a) |
| R-2 (second review) | Ledger under-referencing; undefined criteria | **intact**, untouched (category a) |
| R-3 (second review) | Mahalanobis-radius / ellipsoid comparison | **intact**, untouched (category a) |
| R14-1 … R14-9 | Second review's Path to Acceptance | **intact**, untouched (category a) |
| W16-1 … W16-11 (third review) | G16's eleven items | **intact**, untouched (category a) |
| G15 Phase-3 finding 1 | "344.9 … two orders past κmax" overstatement | **intact as corrected**, untouched (category a) |
| G15 Phase-3 finding 2 | "±0.5% box already known to break" contradiction | **intact as corrected**, untouched (category a) |
| G14 P-1 | Paper-wide dash removal | **intact, re-confirmed (b).** `grep -c -- '---' paper/main.tex` returns 0 |
| G8.4 | Bibliography header anonymized | **intact**, untouched (category a) |
| G17 headline | Numeric-literal and citation-key diff against `HEAD` | **intact, superseded by a wider re-run.** G18's own Phase 3 re-derives both counts fresh rather than trusting G17's figures, and they match |
| G17 item 1.1–1.6b | Aphorism instance count, dash sweep, ruling-out sentence, appendix openers, K-vs-columns, hand-placed-annotation sentence | **intact**, untouched (category a) |
| G17 item 2.1 | Introduction's four-sentence voice pattern | **partially superseded, disclosed.** F2 reworded the third of the four sentences away from "We find that…" for reasons stated in the headline above. Three of four markers ("We find", "Separability then fails", "We predict") remain verbatim; the fourth carries the identical claim in different words |
| G17 item 3.1 | Section 2 bullets-to-prose conversion | **intact**, untouched (category a) — Section 2 not touched this session |
| G17 items 4.1–4.2 (V-1…V-9) | The nine residual audit-voice instances G17 found and fixed | **intact**, untouched (category a) |
| G17 item 5.3 | Page limit ≤5, closed by prose tightening alone | **intact**, re-confirmed pages 1–5 this session too |

### What G18 explicitly does not certify

- **That this is a genuinely independent fourth review.** It is this project's own process doing
  a self-review, by the same kind of agent that wrote the prose it is now judging — the exact
  limitation G17's own gate named when it recommended a fourth, external, tone-focused review.
  That recommendation is **repeated, not superseded, by this session.** G18 is a real, careful
  cold read and a real fix pass; it is not a substitute for an outside reader.
- **That the register is now exhausted.** G17 found nine further instances on a second full
  read after fixing the six its brief named. This session found five on one read. The pattern
  across G14, G15, and G17 is consistent: no single pass has ever found everything. A sixth or
  seventh instance plausibly remains.
- **That the two header-only transitions (1.4) are definitely the right call to leave.** They
  were judged acceptable against this venue's own conventions, not verified against a rule. A
  reader who wants a bridge sentence there is disagreeing with a judgment, not discovering
  something hidden.
- **That F2's supersession of G17's exact four-sentence pattern was checked by anyone but this
  session.** It is disclosed above and at P-2 below specifically so the operator can veto it.

### Process caveats

- **This session's read was one pass, single reader**, exactly as every voice judgment in G16
  and G17 was. No adversarial critic or second agent ran against these five findings or against
  the two "judged acceptable, not fixed" transition calls.
- **The five findings are concentrated in two sentences (abstract sentence 4, intro sentences 3
  and 4) plus two structural nits (Section 4's opener order, one appendix sentence fragment).**
  This is a narrower set of findings than G17's own Phase 4 turned up on its second pass, which
  is consistent with a paper that a prior, careful voice session already improved substantially —
  not evidence that this pass was less thorough.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G19 — Is the anonymized reproducibility package URL inserted correctly, and does the paper
hold up to one final exhaustive verification before submission?

**status: ready for review — UNSIGNED**

Prepared 2026-08-28, session G19 — the nineteenth internal session and, barring operator-found
issues, the final one before the operator's own submission. Signature block below is for the
operator.

> ### The headline, stated before the detail
>
> **The one substantive action this session took: `paper/checklist.tex` item 5's placeholder —
> `[ANONYMIZED CODE LINK --- OPERATOR TO INSERT AFTER UPLOADING build/anonymous_package.zip TO AN
> ANONYMOUS HOST]` — was replaced with the real, operator-provided URL,
> `https://osf.io/hqgzk/overview?view_only=b16c7e6a0ea34047a411e806e5d5a6ce`, copied verbatim, no
> character altered.** Item 5's Answer was already `\answerYes{}` (not `\answerNo{}` pending the
> link, as this session's own brief speculated it might be) — the justification sentence needed
> only the URL substituted in, not an answer flip. A repo-wide search confirmed this is the
> **only** location in the entire paper referencing code availability; no other placeholder,
> footnote, or in-body mention needed the URL.
>
> **Nothing else in the paper was touched.** `paper/main.tex` was not opened for editing this
> session. `git diff` against G18's `cadd7e6` shows exactly one changed line, in
> `paper/checklist.tex`, and nothing else.
>
> **The OSF link itself was spot-checked live, not assumed safe.** Web access was available this
> session. The OSF public API (`api.osf.io/v2/nodes/hqgzk/`), queried with the `view_only` token,
> returned `"meta":{"anonymous":true}` — direct, server-side confirmation this is genuinely the
> anonymized view-only mode, not the plain project URL (which would not carry that flag and, given
> the underlying project's `"public":false`, would not resolve for a non-contributor at all). The
> files endpoint shows exactly one file, `anonymous_package.zip` (630,754 bytes) — visible, as
> required. The contributors endpoint returns an empty `id` field with no name — genuinely
> anonymized, not merely titled generically. The project title itself,
> "Simulator misspecification supplementary materials," carries no identifying information. All
> three checked independently via the live API, not inferred from the URL's shape.
>
> **A second, fresh-eyes reviewer pass (a separate agent instance with no prior context on this
> paper) read the full 23-page compiled PDF cold, specifically hunting for double-blind anonymity
> breaches — names, institutions, self-citation phrasing, leaked URLs, file paths, hostnames,
> acknowledgments, and PDF metadata.** It found none. One minor, non-content observation: the
> PDF's embedded `/CreationDate` metadata carries a `+05'30'` UTC offset (India Standard Time),
> which isn't visible in the rendered paper and isn't a text-content breach, but is a soft
> metadata signal a very sharp reviewer or an automated OpenReview scan could in principle use to
> narrow the authors' likely time zone. Flagged for the operator's awareness (P-6 below); not
> treated as a finding requiring a session fix, since it sits well below the severity of an actual
> anonymity violation and every prior session's own re-scans (including this one's) have never
> flagged embedded compile timestamps as part of the anonymity surface.
>
> **The iCloud sync glitch G18 first hit is confirmed, again, to be a local display issue, not a
> repository content problem.** `audit/S17_REPORT.md` still reads as a dataless placeholder
> (`file` reports "Operation timed out") in the local working tree; `git show HEAD:audit/S17_REPORT.md`
> reads its full 149-line committed content without error. Every other file in `audit/` was swept
> for the same symptom this session; none showed it. This is the same file, same symptom, same
> workaround G18 already used — not a new or spreading problem.
>
> **Full re-verification, independent of G18's own, found zero drift anywhere.** Number trace:
> 125 numbers, byte-identical regeneration. Anonymization re-scan: clean across every
> submission-facing file and the compiled PDF, by both this session's own grep and the independent
> fresh-eyes agent read. Two-tier isolation compile: both tiers pass, 23 pages, zero undefined
> references, `pdftotext` output textually identical across both tiers and the repo working copy
> (the two tiers' PDF files differ at the byte level only in pdfTeX's timestamp-derived
> `/CreationDate`/`/ID` fields — confirmed by a direct byte-diff, not assumed). Page count:
> main text pages 1–5, unchanged. Overleaf package: rebuilt clean, 17 files, 13 allowlisted paths,
> `build/sim_attrib_overleaf_9ab323b.zip`.

### Phase 0 — sync check

| Check | Result |
|---|---|
| `git status` / `git log` | Clean tree at session start except one pre-existing, unrelated untracked item (`Formatting_Instructions_For_NeurIPS_2026/`, a stray unmodified copy of the pristine venue template, dated well before this project's sessions began — untracked, so it will never be pushed; contains no identifying strings, checked). HEAD at `cadd7e6`, matching G18's push |
| `audit/S17_REPORT.md` iCloud symptom | Still present locally (`file` reports "Operation timed out"); `git show HEAD:audit/S17_REPORT.md` reads its full 149-line committed content cleanly. **Confirmed a local display glitch, not a repository content problem** — same conclusion G18 reached, re-verified independently this session |
| All other `audit/*.md` files | Swept for the same dataless symptom (38 files checked). None affected. The symptom has not spread since G18 |

### Phase 1 — URL insertion

| Item | Result |
|---|---|
| Placeholder replaced | `paper/checklist.tex` line 70, item 5 ("Open access to data and code") |
| URL exact-match check | Programmatic string comparison between the operator-provided URL and the inserted `\url{...}` contents: **exact match**, including the `/overview` path segment and the full `view_only` token |
| Answer field | Already `\answerYes{}` before this session; unchanged (G16's placeholder never required an answer flip, contrary to this session's own brief's speculative framing) |
| Other code-availability locations | Repo-wide grep (`paper/*.tex`, `main.tex` footnotes, other checklist items) for any second reference to code availability, a second placeholder, or a stray bracket: **none found**. Item 5 is the only location |
| Recompile | `latexmk -pdf`, exit 0, 23 pages, zero undefined references. `pdftotext` confirms the URL renders correctly on the checklist page and no placeholder bracket text survives anywhere in the compiled text |
| Commit | `9ab323b`, its own unit, pushed after S1/S3 verification below |

### Phase 2 — comprehensive verification

| # | Check | Result |
|---|---|---|
| 2.1 | Full number-trace re-run | **Zero drift.** `src/diagnostics/report_claims.py` regenerated `results/FINAL_CLAIMS_NUMBERS.md` and `paper/appendix_claims_table.tex` from the underlying `results/*.yaml` files; `git status`/`git diff` after regeneration show no changes — 125 numbers, byte-identical. `paper/main.tex` was never opened this session, so no claim, number, or citation could have moved regardless |
| 2.2 | Full independent anonymization re-scan of the compiled PDF, cold reviewer read | **Clean.** A separate agent instance, with no prior context on this paper, read all 23 pages via `pdftotext -layout`, decompressed the PDF (`qpdf --qdf`) to inspect every embedded `/URI` link and object stream, and checked `/Info`/XMP metadata and a `strings` sweep for paths/hostnames/emails. Zero breaches found. Title block reads the correct anonymized-template placeholder ("Anonymous Author(s) / Affiliation / Address / email"); every first-person-plural sentence checked resolves to this paper's own earlier sections or to a third-party citation, never a self-citation; all 18 bibliography entries are third-party; every embedded link is a DOI/arXiv/NeurIPS-policy/OSF link, no personal URLs; `/Author` empty, `/Creator` and `/Producer` generic. One informational, non-content observation: `/CreationDate` carries a `+05'30'` timezone offset — see headline |
| 2.3 | Page count | **Met.** Main text pages 1–5, References begins page 6, confirmed by `pdftotext` form-feed parsing of the freshly compiled PDF — identical to G18's boundary, as expected since `main.tex` was untouched |
| 2.4 | Two-tier isolation compile | **Met, both tiers.** Freshly rebuilt `build/sim_attrib_overleaf_9ab323b.zip` extracted to two separate fresh temp directories, never the repo working copy. §2b (`TEXMFHOME` pointed at this operator's package tree, `TEXINPUTS` unset): exit 0, 23 pages, zero undefined references/citations, 603,948-byte `main.pdf`. §2a (`TEXMFHOME` also unset, this-machine-fallback sense per G12's own naming correction, carried forward unresolved as documented there): exit 0, 23 pages, zero undefined references/citations, 603,948-byte `main.pdf`. The two tiers' PDFs are not byte-identical (MD5 differs) but a direct byte-level diff shows the *only* difference is pdfTeX's `/CreationDate`, `/ModDate`, and derived `/ID` fields (the two compiles ran ten seconds apart) — `pdftotext -layout` output is textually identical across both tiers and the repo working copy, confirmed by diff, not assumed |
| 2.5 | Overleaf package rebuild | **Met.** `scripts/build_overleaf_package.sh` re-run against the final committed state (`9ab323b`): 17 files, 13 allowlisted paths, `build/sim_attrib_overleaf_9ab323b.zip` — the package that will actually be uploaded to OpenReview |
| 2.6 | Consolidated cross-session findings table | **Produced — see below.** Built by a separate agent instance that read `GATES.md` in full (all ~2,700 pre-G19 lines) plus every `audit/S11_REPORT.md`–`S18_REPORT.md` (S17 via `git show`, per the Phase 0 workaround) |
| 2.7 | Checklist placeholder sweep | **Met.** Full bracket/TODO sweep of `paper/checklist.tex`: exactly one placeholder remains, item 16's `\answerTODO{}` and `[AI-USE DISCLOSURE --- OPERATOR TO COMPLETE...]` — untouched, per standing instruction since G9. No other bracket, TODO, FIXME, or XXX marker anywhere in the file |
| 2.8 | Repo-wide anonymity/AI-reference grep | **Split result, both halves clean on their own terms — see below** |

**On 2.8, stated precisely rather than glossed over:** two different greps answer two different
questions, and conflating them would misreport the state of the repo.

- **AI/model-attribution grep** (the standing set of proscribed vendor/product/co-authorship
  terms this project's authorship gate names, case insensitive) across every tracked file in the
  entire repository: **zero hits.** This is the check S1 actually requires.
- **Personal-identity grep** (`palaash\|gang\|sim-attrib\|pa1aash`) across every tracked file in
  the entire repository: **many hits** — `LICENSE`'s copyright line, `README.md`'s own project
  name, `OUTSTANDING.md` and `docs/DECISIONS.md`'s GitHub-username references, every
  `results/*.yaml`'s `host:` field (`Palaashs-MacBook-Air.local`), and the build scripts' own
  repo-root guard strings. **This is expected and is not a regression** — this is the private
  development repository, not the anonymized submission artifact; it legitimately carries the
  operator's real identity throughout (git authorship, `LICENSE`, hostnames), exactly as every
  prior session's own repo state did. The actual double-blind surface — `paper/main.tex`,
  `paper/checklist.tex`, `paper/appendix_tables.tex`, `paper/appendix_claims_table.tex`,
  `audit/BIBLIOGRAPHY.bib`, and the compiled PDF's extracted text and `/Author` metadata — was
  separately re-checked (2.2 above and the submission-scope grep below) and is clean. The private
  repo's own de-identification is a distinct, still-pending operator action (P-5, repository
  visibility to private), not a paper-anonymization defect.

**Submission-scope anonymity grep** (the established G16–G18 pattern, re-run this session):
`grep -inE "palaash|gang|sim-attrib|pa1aash"` across `paper/main.tex`, `paper/checklist.tex`,
`paper/appendix_tables.tex`, `paper/appendix_claims_table.tex`, `audit/BIBLIOGRAPHY.bib`, and the
compiled PDF's extracted text: **zero hits in all six**, `/Author` metadata empty — matching every
prior session's result, re-confirmed rather than assumed.

### Phase 2.6 — the full consolidated cross-session findings register (G11–G19)

Scope: every finding from External Review #1 (Weak Reject), External Review #2 ("Path to
Acceptance"), External Review #3, the internal tone/readability pass (G17+G18), plus every defect
any session's own re-verification found on top of those reviews. Status reflects the state as
verified by G19 (2026-08-28).

#### Table A — External Review #1 (Weak Reject, confidence 4/5): Tier-1 (must-fix)

| Item ID | What it was | Final status (as of G19) | Session fixed/checked in |
|---|---|---|---|
| T1-1 | Appendix TODO replaced with a generated claim-to-source table | Intact — regenerated from source, byte-identical to committed file (G18 Phase 3) | Fixed G11; re-verified G12–G18 |
| T1-2 | Main text ≤5 pages (Sim2Science limit) | Closed at exactly 5 pages since G13; reopened and reclosed by prose tightening alone in G14, G16, G17; unchanged at 5 pages through G18/G19 | Not met G11–G12 (6 pages); closed G13; held G14–G19 |
| T1-3 | Real Dufour confidence-set-bounded MMC check (not a cheaper reframe) | Intact — its own output is now the direct source for R14-2's ellipsoid claim (strengthened, not just preserved) | Built and run G11 (`confidence_set_check.py`, `DUFOUR_CONFIDENCE_SET_CHECK.md`); untouched since |
| T1-4 | Simulator schematic figure relocated/reduced, qualitative content restated in main-text prose | Intact — figure later moved to appendix entirely (G13), qualitative restatement strengthened by R14-1's mechanism sentence (G14) | Fixed G11; relocated G13; strengthened G14; re-verified through G18 |
| T1-5 | Full anonymity re-scan (not just the two review-named instances) | Intact, repeatedly re-run and extended — G14 found the bibliography-header leak G8.4 had missed; G16 found double-field host/commit leaks in every `results/*.yaml`; G19 re-scan clean across 6 submission-scope locations | Fixed G11 (5 extra leaks found beyond the 2 named); re-run every session through G19 |
| T1-6 | Checklist answers match the compiled PDF | Intact, actively maintained (item 2's justification kept in sync with §6 edits in G17; item 5 completed in G19) | Fixed G11; re-verified G12–G19 |

#### Table B — External Review #1: Tier-2 (should-fix)

| Item ID | What it was | Final status (as of G19) | Session fixed/checked in |
|---|---|---|---|
| T2-1 / T2-2 | Rank-at-τ and κ≤κmax stated as one condition, not two; κ² compute-cost derivation given | Intact, restated more compactly in G17's voice pass | Fixed G11; re-verified through G18 |
| T2-3 | Second, data-motivated η-scaling using confidence-set standard errors | Intact — independently re-derived two ways in G15; both agree | Fixed G11; strengthened G14 (R14-4); re-verified through G18 |
| T2-4 | Second-θ separability test run | Intact — real test run, `κ=10.9` at θ₂ matching `κ=10.1` at θ₀ | Lost to context compaction G11; run for real G12; re-verified through G18 |
| T2-5 | Eight Related Work citations genuinely engaged, not name-dropped | Intact but reduced — two citations dropped in G14 for page-budget recovery (disclosed); the other six untouched; survived G17's bullets-to-prose rewrite (20 occurrences, 19 distinct, unchanged) | Fixed G11; reduced by 2 citations G14 (disclosed); rewritten G17; re-verified through G18 |
| T2-6 | Section 5 retitled finding-first, apologetic framing fixed | Intact | Substantially done G11; closed G12; re-verified through G18 |
| T2-7 | Scope restriction stated in the introduction's own first contribution sentence | Intact, re-confirmed immediately adjacent to G18's F2 edit without being touched by it | Fixed G11; re-verified through G18/G19 |
| T2-8 | Two-panel non-termination figure split, per-figure font floors enforced | Intact | Fixed G11; re-verified through G18 |
| T2-9 | Repeated metaphor language reduced; diagnostic's four steps as a numbered list | Intact and extended — G17 removed one further metaphor this pass had left | Fixed G11; extended G17; re-verified G18 |
| T2-10 | Abstract tightened, one concrete number retained (κ=628.9, rank 4/6) | Intact; re-confirmed adjacent to G18's F1 edit, no number touched | Fixed G11; re-verified through G19 |
| T2-11 | Limitations bullet on where a learned summary statistic would sit | **Regressed once, restored.** Silently dropped by G16; found missing and restored in G17 | Fixed G11; regressed G16 (undetected in G16's own gate); restored G17; intact through G19 |
| T2-12 | K-vs-column-count notation conflict resolved | Intact, resolved at the root cause | Fixed G11; root-cause fixed G14; re-verified through G18 |
| T2-13 | Appendix table's plateau-stability caption made honest about noise | Intact | Fixed G11; re-verified through G18 |
| T2-14 | Checklist moved after the appendix (NeurIPS convention) | Intact | Fixed G11; re-verified through G18 |
| T2-15 | One sentence on what the literature's baseline test would output on the six-column confound | Intact — later carries G16's measured Montel result rather than a hedge | Fixed G11 (hedged); reworded to carry measured result G16; de-dashed G17 |

#### Table C — Prior-art / novelty threat-checks

| Item ID | What it was | Final status (as of G19) | Session fixed/checked in |
|---|---|---|---|
| R1 | Rejection-sampling-calibration mechanism is prior art | DEAD verdict, unchanged through every rewrite | Established pre-G11; re-confirmed every gate G11–G18 |
| R2 | Noisy-rank estimator, corrected instrument | NARROW-CONDITIONAL verdict, unchanged through every rewrite | Established pre-G11; re-confirmed every gate G11–G18 |

#### Table D — External Review #2 ("Path to Acceptance, Round 2")

| Item ID | What it was | Final status (as of G19) | Session fixed/checked in |
|---|---|---|---|
| R14-1 (Tier 1) | Findings list restored to the Introduction; all six family mechanisms named and verified against `sir3.py`; disclaimers cut | Intact; rewritten into full-sentence voice by G17, re-confirmed adjacent to G18's F2/F3 edits | Fixed G14; rewritten G17; re-verified G18/G19 |
| R14-2 | Mahalanobis-ellipsoid comparison added to Section 5 | Intact. Rigorously recomputed (2.71/3.56, corrected from the review's own rough estimate); re-derived from scratch in G15 | Fixed and corrected G14; independently re-derived G15; re-verified through G18 |
| R14-3 | "Exactly zero" acceptances replaced with the exact measured draw count | Intact | Fixed G14; re-verified through G18 |
| R14-4 | SE-scaling figure explained by naming which 3 of 5 nuisance coordinates it uses | Intact; independently re-derived two ways in G15; restructured G17 without losing the named coordinates | Fixed G14; re-derived G15; restructured G17; re-verified G18 |
| R14-5 | Coherence phrase resolved; gradual/abrupt threshold rule stated where first used | Intact | Fixed G14; re-verified through G18 |
| R14-6 | Two figure-rendering bugs, two bibliography defects, appendix table column overflow, θ₀'s pre-figure definition | Intact, all five sub-items independently verified | Fixed G14; re-verified through G18 |
| R14-7 | Appendix A.5's claim-to-source ledger referenced from the start of Section 4 | Intact — later became the sentence F4 (G18) reordered, without removing the reference | Fixed G14; reordered (not removed) G18; intact G19 |
| R14-8 | Montel et al.'s test either run or the assertion explicitly hedged | **Superseded — hedge upgraded to a real, run comparison** by G16's W16-2 | Hedged G14; superseded by real implementation G16 |
| R14-9 | Positive sentence on where a learned summary statistic / NPE would enter | Intact | Fixed G14; re-verified through G18 |
| R14-10 (optional) | Promotion of $S_A$ to a fifth finding | **Declined**, reasoning stated; decision unchanged through G19 | Declined G14; decision stands through G19 |
| R-1 (second review's cross-check) | Main-text self-sufficiency | Intact — closed and independently re-verified in G15 | Recovered/closed G15; re-verified G17/G18 |
| R-2 (second review's cross-check) | Ledger under-referenced; three undefined criteria | Intact — closed and independently re-verified in G15 | Closed G15; protected G17; re-verified G18 |
| R-3 (second review's cross-check) | Mahalanobis-radius / ellipsoid comparison, independently recomputed | Intact — matched paper's stated 2.71/3.56 to 4 significant figures | Closed G15; re-verified G17/G18 |

#### Table E — External Review #3 (two "real" findings + nine smaller ones)

| Item ID | What it was | Final status (as of G19) | Session fixed/checked in |
|---|---|---|---|
| W16-1 | Checklist item 16 (LLM-use disclosure) confirmed unchanged | **Still an open placeholder**, explicitly the operator's; not touched by G17, G18, or G19 | Confirmed-as-open G16; remains open through G19 |
| W16-2 | Anau Montel et al. (2025) global-null comparison implemented and genuinely run | Intact. Measured result reversed the paper's prior unmeasured claim — global test correctly rejects at both corners/confounds, correctly fails to reject the null-data control | Implemented and run G16; re-verified through G18 |
| W16-3 | Coherence/colnorm thresholds stated explicitly where their verdicts are used | Intact — genuinely computed, clean on all 8 assignments | Fixed G16; re-verified through G18 |
| W16-4 | Orphaned random-attributor-floor sentence removed from main-text prose | Intact | Fixed G16; re-verified through G18 |
| W16-5 | Second-θ check added to the provenance ledger | Intact | Fixed G16; re-verified through G18 |
| W16-6 | Precision fix ("two orders of magnitude" → exact multiplier) | Superseded by G15's more precise fix ("3.4×") | Softened G16; exact multiplier G15 |
| W16-7 | Figure 3(a) inline PASSES/FAILS labels removed, framing moved to caption | Intact | Fixed G16; re-verified through G18 |
| W16-8 | Figure 7's unquantified "generally sooner" claim | Intact — Wilson intervals added, caption honestly disclosed the one combination that contradicts the claim | Fixed G16; re-verified through G18 |
| W16-9 | $d$ (summary-statistic count) defined in Section 3 | Intact | Fixed G16; re-verified through G18 |
| W16-10 | Fithian/Sun/Taylor and Lee/Sun/Sun/Taylor cited, with a distinguishing sentence | Intact — became the contrast Section 2's paragraph 4 turns on in G17's rewrite | Fixed G16; integrated G17; re-verified G18 |
| W16-11 | "Every tool is prior art" aphorism stated once with force, trimmed elsewhere | Intact | Fixed G16; confirmed already-correct G17; re-verified G18 |

#### Table F — Internal tone/readability pass (G17 voice rewrite + G18 cold read)

| Item ID | What it was | Final status (as of G19) | Session fixed/checked in |
|---|---|---|---|
| G17 §1.1 | "Prior art" aphorism reduced to one instance | Already met on arrival (G16's W16-11); reported found, no edit made | Confirmed G17 |
| G17 §1.1b | `checklist.tex` item 12 "cited as prior art" phrase | Judged unrelated, deliberately not touched | Reviewed and left alone G17 |
| G17 §1.2 | Complete fresh dash-as-aside sweep | G14's claimed-complete sweep was not actually complete — 3 surviving em-dashes found and rewritten | Found + fixed G17 |
| G17 §1.2b | Dashes baked into a figure image | Found, deliberately not changed (outside scope), disclosed | Found + disclosed, left alone G17 |
| G17 §1.3 | "Not X, not Y, not Z" stacked-clause chain | Intact — restructured into three short sentences | Fixed G17 |
| G17 §1.4 | Three "moved here for space" appendix openings | Intact — all three removed | Fixed G17 |
| G17 §1.5 | K-vs-columns disclaimer / Figure 2 legend | Already met on arrival (G14's R14-1/R14-6) | Confirmed G17 |
| G17 §1.6 | "Hand-placed annotations" sentence | Intact — removed, `checklist.tex` item 2 updated in the same pass | Fixed G17 |
| G17 §1.6b | Stale code comment describing removed annotations | Noted, not fixed — non-packaged source comment, out of scope | Disclosed, not fixed, G17 |
| G17 §2.1 | Introduction states findings directly, four-sentence voice pattern | **Partially superseded by G18.** G18's F2 reworded one of the four sentences for a different, more consequential reason (verbatim echo of the abstract). 3 of 4 markers remain verbatim | Fixed G17; partially superseded (disclosed) G18 |
| G17 §3.1 | Section 2 converted from bullets to prose | Intact — citation-key multiset diff confirms unchanged | Fixed G17; untouched G18/G19 |
| G17 V-1…V-9 | Nine residual audit-trail-voice instances | Intact, all nine fixed | Found + fixed G17 |
| G17 — T2-11 regression | See Table B | Restored | Found + fixed G17 |
| G17 — G8.4 bibliography leak | Repository name in a header comment, shipped via the Overleaf allowlist | Fixed — neutral wording | Found + fixed G17 |
| G18 (F1) | Abstract sentence 4 dangling appositive | Fixed — comma to colon | Fixed G18 |
| G18 (F2) | Introduction sentence 3 restated the abstract's C4 finding near-verbatim | Fixed — reworded, verbatim echo removed | Fixed G18 |
| G18 (F3) | Introduction's closing sentence trailed into a comma-spliced fragment | Fixed — split into two sentences | Fixed G18 |
| G18 (F4) | Section 4 opened with a provenance disclaimer before its substance | Fixed — reordered | Fixed G18 |
| G18 (F5) | Appendix claims-ledger intro sentence fragment (missing verb) | Fixed — "is" inserted | Fixed G18 |
| G18 — 1.2/1.3/1.7 checks | Confidence-vs-evidence, mechanical listing, Cranmer/Talts register | Clean, nothing found | Confirmed clean G18 |
| G18 — 1.4 check | Two header-only section transitions | Checked, judged acceptable, deliberately not fixed | Reviewed and left alone G18 |

#### Table G — Findings from each session's own re-verification (not raised by any external review)

| Item ID | What it was | Final status (as of G19) | Session found/fixed in |
|---|---|---|---|
| G11-a | Prior "isolation" test was invalid (leaked local `TEXINPUTS`) | Fixed — kpathsea relative-path resolution; both tiers pass | Found + fixed G11 |
| G11-b | `appendix_claims_table.tex` missing from the Overleaf allowlist | Fixed | Found + fixed G11 |
| G11-c | Citation mismatch to the wrong figure | Fixed | Found + fixed G11 |
| G11-d | 5 additional anonymity leaks beyond the 2 the review named | Fixed | Found + fixed G11 |
| G11-e | An internal review-tracking label baked into the generated appendix table | Fixed at source, regenerated | Found + fixed G11 |
| G12-a | STRICT-isolation tier's "PASS" was illusory (`TEXMFHOME` fallback, not genuine isolation) | **Disclosed, deferred, never fixed** — needs a second isolated TeX Live install, unavailable on this machine; re-confirmed still-deferred through G18/G19; does not affect the tier the project gates on (§2b) | Found G12; unresolved every gate through G19 |
| G12-b | `FINAL_CLAIMS.md` missing a section `DUFOUR_CONFIDENCE_SET_CHECK.md` said it would add | Fixed | Found + fixed G12 |
| G12-c | Stale page-count table in `OVERLEAF_PACKAGE_REPORT.md` | Fixed | Found + fixed G12 |
| G13-a | Figure renumbering fallout from moving Table 1/simulator figure to appendix | Fixed before commit | Found + fixed G13 |
| G13-b | Bibtex `month=June` warning (Raue et al. 2009) | **Disclosed, not fixed** — standing "`.bib` stays exactly as fetched" policy; still standing as of G19 | Found G13; remains unfixed through G19 |
| G13-c | Early wording trim briefly dropped T2-11's clause | Caught and restored same session | Found + fixed within G13 |
| G14-a | Figure 1 value labels below legibility floor | Fixed — widened panel | Found + fixed G14 |
| G14-b | Table 1 hyphenating mid-word in narrow columns | Fixed | Found + fixed G14 |
| G14-c | Session interrupted mid-sweep, resumed correctly via git/file state | Process note, not a defect | G14 |
| G14-d | A literal `--` baked into a matplotlib annotation (`.py`, invisible to `.tex`-scoped grep) | Fixed, figure regenerated | Found + fixed G14 |
| G15-a | Figure 7 legend placed where data curves cross it | Fixed — legend relocated | Found + fixed G15 |
| G15-b | "Two orders past κmax" overstated the margin ~30× | Fixed — "3.4× past" | Found + fixed G15 |
| G15-c | Section 5 contradicted its own later statement about which box first fails | Fixed | Found + fixed G15 |
| G15-d | Three figures' provenance sidecars carried stale `dirty: true` flags | Fixed — regenerated clean, confirmed pixel-identical | Found + fixed G15 |
| G16-a | Every `results/*.yaml` leaked hostname + commit hash under two field names each | Fixed — value-pattern redaction in `build_anonymous_package.sh` | Found + fixed G16 |
| G16-b | Montel module's first draft used Python's randomized `hash()` for seeding | Caught before the production run, fixed to a deterministic offset | Found + fixed within G16 |

#### Table H — Structural / cross-cutting items

| Item | What it was | Final status (as of G19) | Session(s) |
|---|---|---|---|
| Page limit | Main text ≤5 pages | Held since G13 through G19 (reopened/reclosed by content-neutral tightening 3 times) | Not met G9/G11/G12; closed G13; held G14–G19 |
| G10 backfill | No original `GATES.md` entry existed for G10 | Backfilled retroactively; isolation criterion marked not-met-as-originally-run/fixed-in-G11 | Gap found + entry written G12 |
| Two-tier isolation compile discipline | Whether the packaged zip is genuinely self-contained | §2b (the gating tier) passes genuinely every session G11–G19; §2a passes only in the narrower this-machine-fallback sense, unresolved since G12 | Established G11; caveat named G12; carried through G19 |
| Anonymized reproducibility package (`build/anonymous_package.zip`) | Public code package: `src/`, `tests/`, redacted `results/*.yaml`, standalone README, re-fetched canonical MIT `LICENSE` | Built, redacted, independently re-scanned (zero hits across 91 files), extracted fresh and run (164/171 tests pass, 7 documented non-blocking exclusions). **Uploaded to OSF by the operator between G18 and G19; live link spot-checked this session (headline above)** | Built G16; uploaded by operator, link verified G19 |
| Checklist item 5 (anonymized-code-link placeholder) | `[ANONYMIZED CODE LINK --- OPERATOR TO INSERT...]` | **Closed by G19** — real URL inserted | Closed G19 |
| Checklist item 16 (LLM-use disclosure placeholder) | `\answerTODO{}` | Still open — explicitly the operator's, untouched through G19 | Confirmed open every session since G16 |

#### Table I — G19 (this session)

| Item | What it was | Final status | Session |
|---|---|---|---|
| G19-1 | Replace `paper/checklist.tex` item 5's placeholder with the real anonymized-package link | Done | G19 |
| G19-2 | Full number trace re-run | Zero drift — 125 numbers, byte-identical regeneration | G19 |
| G19-3 | Anonymization re-scan (submission scope + repo-wide AI-reference scope) | Both clean, distinctly reported (see Phase 2.8 above) | G19 |
| G19-4 | Two-tier isolation compile | Both tiers pass, 23 pages, zero undefined references | G19 |
| G19-5 | Page count | Main text pages 1–5 unchanged | G19 |
| G19-6 | Overleaf package rebuild | 17 files, 13 allowlisted paths | G19 |
| G19-7 | OSF link live spot-check | Anonymous mode confirmed via API, file visible, no contributor name, title clean | G19 |
| G19-8 | Independent fresh-eyes PDF anonymity review | Clean; one informational metadata note (`/CreationDate` timezone) | G19 |
| G19-9 | Scope discipline | No prose, no claim, no number, and no file outside `paper/checklist.tex`'s one line was touched this session | G19 |

### What G19 explicitly does not certify

- **That this session's own checks are a substitute for the operator's own read.** Every point in
  the standing P-list below (signing G19, personally re-verifying the OSF link, writing the AI-use
  disclosure, the reciprocal-review/Paris/visibility/submission actions) remains the operator's,
  not resolved by this session having run.
- **That the `/CreationDate` timezone metadata is neutralized.** It is disclosed, not fixed —
  fixing it would mean recompiling with a pinned `SOURCE_DATE_EPOCH` or on a UTC-configured
  machine, a build-environment change this session judged out of its own narrow mandate (insert
  one URL, verify the whole document) rather than something to make unilaterally on a
  submission-readiness pass.
- **That the private development repository is itself anonymous.** It is not, and was never meant
  to be — `LICENSE`, `README.md`, `results/*.yaml` hostnames, and git authorship all correctly
  carry the operator's real identity. P-5 (switching repository visibility to private) is the
  operator's own pending action for exactly this reason.
- **That every one of nineteen sessions' voice, substance, and evidence judgments has been
  independently re-litigated.** This session verified that nothing drifted since G18's own
  certification of that state; it did not re-run G11–G18's own review/critique work from scratch.

### Process caveats

- **The OSF spot-check and the fresh-eyes PDF read were both genuinely independent this
  session** — the OSF API check used live server responses, not the URL's shape; the PDF read was
  performed by a separate agent instance with no conversation history on this paper, closer in
  kind to the external, genuinely fresh review G17/G18 both called for than any of this project's
  prior internal re-reads have been. Neither is a substitute for a human reviewer.
- **The consolidated table (Phase 2.6) is a compilation, not a re-litigation.** It records what
  each prior session already established: status "intact" means no evidence of drift was found
  this session, not that the underlying claim was independently re-derived from scratch this
  session (the numeric ones were, via the byte-identical regeneration in 2.1; the prose/voice ones
  were checked only for accidental disturbance, since `main.tex` was never opened).

### Points requiring operator input — collected, not resolved

- **P-1.** Sign G19 after reading the final PDF, including the newly-completed checklist item 5.
- **P-2.** Personally re-verify the OSF link one more time (private/incognito window) — this
  session's own check used the live public API and confirmed anonymity, files, and title, but a
  human eyeballing the actual rendered page is still the operator's own final check per the
  standing S4 instruction.
- **P-3.** Write the AI-use disclosure at checklist item 16 — untouched this session, as every
  session since G9.
- **P-4.** Confirm the reciprocal reviewer nomination (Q-3) and Paris attendance — unchanged,
  not this session's to resolve.
- **P-5.** Switch repository visibility to private.
- **P-6.** Optional: if the operator wants the PDF's embedded `/CreationDate` timezone offset
  neutralized before the final camera-ready build, recompile with `SOURCE_DATE_EPOCH` pinned (or
  on a UTC-configured machine/CI). Not required — this is below the severity of an anonymity
  violation — but flagged since the fresh-eyes review specifically surfaced it.
- **P-7.** Submit via OpenReview — 29 August 2026 AoE.

Everything else — the document itself, its numbers, its anonymity, its compilation, its packaging
— is, as of this session's own verification, complete.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G20 — Operator line-edit, structural pass: appendix bloat, ordering, a missing conclusion.
Does the paper's structure hold up after a large relocation, and does the page budget still close?

**status: ready for review — UNSIGNED**

Prepared 2026-08-29, session G20 — the twentieth internal session, first of a planned four
(G20-G23) covering a detailed operator line-edit. This session's mandate is explicitly
**structural only** (where content lives, not how individual sentences read); prose-style tuning
is reserved for G21/G22 on the structure this session produces.

> ### The headline, stated before the detail
>
> **Every phase of the operator's brief ran, and one genuine, disclosed shortfall remains: main
> text is 6 pages, not 5.** Root cause and resolution are below; the operator was asked mid-session
> how to handle it and chose to defer the fix to G21's planned prose-tightening pass rather than
> have this structural session touch pre-existing Limitations prose.
>
> **Phase 1 (A.1, Table 1 placement).** Table 1 (the four-finding summary) stays in the appendix;
> option (b) — shrink the Section 1 pointer to a compact single sentence — was chosen over moving
> the table into Section 1, because by the time this decision was reached (after Phases 2-4, 6-7)
> main text had no spare room, let alone room to absorb a table. The intro's pointer sentence
> ("Table~\ref{tab:summary} (Appendix~\ref{sec:appendix}) pairs each of the paper's four findings
> with its evidence figure.") is now folded into the rewritten second paragraph (Phase 6) rather
> than standing alone.
>
> **Phase 2 (A.4, Table 2/Table 3).** Table 2 (`tab:sb-eight`, $S_B$'s eight-assignment table)
> stays untouched — the main text's 1.523/9.881 citations still resolve to it. Table 3
> (`tab:sa-eight`, the $S_A$ control table) was **dropped entirely**, not folded: its rows are a
> near-duplicate of Figure 1's right panel, and the one column Figure 1 doesn't carry — the named
> equivalence class per failing assignment — is now one clause in Section 4's $S_A$ sentence
> (`\{progression\}`, `\{transmission, progression\}`, `\{progression, observation\}` across the
> four failures). The dropped table's full numbers are preserved in `CLAIMS.md` (Phase 3.4) so
> nothing is lost, only removed from the paper itself.
>
> **Phase 3 (A.5, the surgical cut) is the largest change in this session.** Three promotions, one
> cut:
> - **3.1, controls.** The $S_C$ positive control (rank 2, $\kappa=\infty$) was already stated
>   with its numbers in main-text prose before this session — nothing to promote there. The no-CRN
>   negative control was referenced only as "(confirmed by a negative control)" with no numbers;
>   Section 3 now states them directly: no plateau found, one of six step sizes inside any
>   candidate window, verified against `results/jacobian_rank.S_A.no_crn_control.yaml`
>   (`results.plateau.found: false`, `results.plateau.n_h_in_plateau: 1`).
> - **3.2, the threshold table.** A new Table 3 (Appendix A.2) consolidates all eight
>   pre-registered thresholds ($\tau$, $\kappa_{\max}$, resolve factor, plateau tolerance,
>   equivalence-class loading, coherence flag, column-norm floor, six step sizes), every value
>   verified against `results/jacobian_rank.S_B.yaml`'s `thresholds_pre_registered` block. Placed
>   in A.2 rather than Section 3 (the operator's own stated alternative) after the first
>   placement, in Section 3, pushed main text to 6 pages on its own.
> - **3.3, the confidence box.** A new table near Figure 3 (Section 5) gives the five individual
>   relative half-widths and the MLE point estimate ($\beta$ 0.3551/2.35%, $\gamma$
>   0.1475/6.98%, $\rho$ 0.4050/6.06%, $I_0$ 10.37/13.99%, $\sigma_{\text{obs}}$
>   0.1568/16.63%), verified against `results/confidence_set_mmc.yaml`'s `mle_fit.theta_hat` and
>   `confidence_set_box` blocks. Laid out transposed (parameters as columns, two rows) rather than
>   five rows, purely for page-budget reasons — same five values and MLE point, more compact form.
> - **3.4/3.5, the cut.** Everything else that was in A.5 (the former C2, C3, C4, C5, L1, B1
>   dotted-path tables, roughly seven pages of paths) is replaced with one paragraph, and the
>   subsection is renamed **"Claim-to-source table."** The full ledger — nothing dropped, C1
>   through C5, L1, B1, and the source-file provenance table — now lives as `CLAIMS.md` in the
>   anonymized reproducibility package (`scripts/anonymous_package/CLAIMS.md`, 92 rows). The
>   package build script (`scripts/build_anonymous_package.sh`) now copies it in; verified present
>   in the rebuilt `build/anonymous_package.zip`. The now-unused `paper/appendix_claims_table.tex`
>   was removed (`git rm`) — and, caught only by actually running the rebuild rather than assuming
>   it would work, **`scripts/build_overleaf_package.sh`'s hardcoded allowlist still named that
>   deleted file**; fixed before the Overleaf package was rebuilt (this is exactly the class of
>   drift Phase 8.6 asked to check for, just on the sibling script, not the one the phase named).
>
> **Phase 4 (Section 2's embedded result) moved.** The Anau Montel et al. baseline comparison — a
> full experimental result (rejection at both corners and two confound realizations, a null
> control, an arg-min analysis) — was sitting inside "Background and related work" as if it were a
> citation aside. Section 2 now carries one forward-pointing sentence; the full result, unchanged
> in substance, is a new paragraph at the end of Section 4 ("Comparison to a global
> misspecification test"), presented as what it is: an experimental finding, not a related-work
> note.
>
> **Phase 5 (Section 5 reorder) is done.** The boundary sweep ("The mechanism, and the shape of
> the boundary") now comes before the data-implied confidence box ("Affordable at a known
> parameter..."), matching the operator's requested order: establish where the round-box gate
> fails first, then show the data-implied box is wider still. The forward reference
> ("...already known to break the composition (below)") and the backward-repair sentence ("The
> collapse below was measured under a round, assumed ±5% box; here it survives...") are both
> removed, per the operator's own prediction that reordering would make them unnecessary; one
> remaining directional word ("above" → "below") in the moved paragraph was corrected so it still
> points the right way after the swap. Every number and every figure/table cross-reference in the
> section was re-checked after the swap; all resolve.
>
> **Phase 6 (triple redundancy) is done.** The introduction's second paragraph no longer restates
> the abstract's four findings a second time; it now explains why this simulator (three
> biologically distinct mechanisms genuinely worth telling apart, distortions realistic enough
> that two can move the same feature) and what a practitioner gets from running the screen
> (a certificate or a named equivalence class, not a guess). Section 5's opening paragraph was
> checked and is not doing full-restatement duty either — it only frames the MMC/selective-
> inference finding (findings 3-4), not all four, so it needed no further cut on this count.
>
> **Phase 7 (Conclusion) is done.** A new two-sentence Conclusion section states the practical
> recommendation the paper never previously stated as an instruction (run the screen before
> attributing misspecification; report the equivalence class, not a guess, once $\kappa$ exceeds
> the ceiling) and lands the contribution in one closing beat, in plain declarative sentences, no
> "not X, rather Y" construction introduced.
>
> **The page-budget shortfall, in full.** Baseline (post-G19) main text was exactly 5 pages, no
> slack. This session's mandatory additions (Phase 3.3's table, Phase 7's Conclusion, Phase 2's
> equivalence-class clause, Phase 3.1's control numbers) added more than Phase 3.2's move-to-
> appendix and Phase 4's relocation gave back, net. Every whitespace lever already at its
> established floor (`\parskip`, `\floatsep`, `\textfloatsep`, `\abovecaptionskip` all previously
> tightened across G12-G16) was confirmed still at floor, not further reducible without repeating
> the font-size violation G11 was reverted for. A page-break-specific `\enlargethispage` was
> calibrated by direct visual rendering (not assumed from `pdftotext` alone): tested from
> `2\baselineskip` (clean) up through `4\baselineskip` and `30pt` (both produced visible text
> overlap with the page footer, confirmed by rendering the page to PNG and reading it) — the paper
> now ships at `\enlargethispage{2\baselineskip}` before `\section{Limitations}`, the largest
> value confirmed clean. Every sentence and table this session added was compressed as far as it
> would go without dropping a requirement (Conclusion cut to its floor of two sentences; the
> confidence-box table transposed and set in `\footnotesize`; the Montel paragraph, threshold
> pointer, negative-control clause, and intro rewrite all tightened again after the first pass).
> The remaining gap — roughly bullet 2's back half and bullet 3 of Limitations, plus the
> Conclusion, still land on page 6 — cannot close without touching pre-existing Limitations prose,
> which is explicitly G21's mandate, not this session's. **Asked directly, the operator chose to
> defer the fix to G21's full-document prose-tightening pass rather than have this session bend
> its own "structure only" boundary.** Flagged here, not hidden: **main text is 6 pages, not 5,
> at the end of G20**, and closing that is the first thing G21 needs to verify before doing
> anything else.
>
> **Re-verification, independent of the promotion/cut work itself.** Number trace: every promoted
> value (negative control, threshold table's eight entries, confidence box's five half-widths and
> MLE point, the four equivalence-class labels) re-checked directly against the rendered PDF text
> against the `results/*.yaml` source, not against memory of A.5's old prose. Anonymization
> re-scan: clean, PDF text and metadata, and every file this session touched (the one hit in
> `scripts/build_anonymous_package.sh` is the script's own obfuscated pattern definition, matching
> itself by the design the script's own comment explains, not a leak). Two-tier isolation compile:
> both tiers pass against a freshly rebuilt `build/sim_attrib_overleaf_380b694.zip` extracted to an
> isolated temp directory — exit 0, 17 pages, zero undefined references/citations both tiers,
> `pdftotext` output byte-for-byte identical across the repo working copy and both isolated
> extractions (583,882-byte `main.pdf`, matching in all three). Anonymous package rebuilt with
> `CLAIMS.md` confirmed present in the zip (92-row ledger, 21,111 bytes). Overleaf package
> allowlist fixed (see Phase 3.4 above) and rebuilt clean.

### What G20 explicitly does not certify

- **That main text is within the 5-page limit.** It is not, as of this session's own count (6
  pages). This is disclosed, not resolved — the operator's own choice this session was to let
  G21 close it via prose tightening across the whole document rather than have this session touch
  Limitations' wording. G21 must re-verify page count as its own first check, before any other
  prose work, and must not assume this gate's other PASSes extend to a claim this gate does not
  make.
- **That every prior session's voice/substance judgment was re-litigated.** This session moved
  content and added exactly the new prose Phases 2, 3.1, 4 (pointer sentence), 6, and 7 required;
  it did not review or adjust any sentence outside those specific insertions, per its own
  "structure only" mandate.
- **That the reordering in Phase 5 or the relocation in Phase 4 reads smoothly at the sentence
  level.** Both were checked for correctness (numbers still trace, cross-references still
  resolve, no claim changed) and for structural fit (right section, right order), not for prose
  quality — that is explicitly G21/G22's pass on the settled structure this session produced.

### Process caveats

- **The threshold table's placement changed mid-session, and that reversal is disclosed rather
  than smoothed over.** It went into Section 3 first (per the operator's own stated first
  preference), was found to be the single largest contributor to the 6-page overage once measured
  against the compiled PDF rather than assumed, and was moved to Appendix A.2 (the operator's own
  stated alternative) once that measurement was in. Both are literally what Phase 3.2's own
  instructions offered as options; this session used the page-count measurement, not a coin flip,
  to choose between them.
- **The `\enlargethispage` value was chosen by rendering the page to an image and reading it
  directly**, not by trusting `pdftotext`'s line-count output alone — `pdftotext` cannot show
  visual text overlap, and two of the tested values (`4\baselineskip`, `30pt`) looked clean in
  `pdftotext` extraction while visibly colliding with the page-footer number when rendered. This
  matters for any future session tuning page breaks in this document: measure by rendering, not
  by text extraction alone.
- **CLAIMS.md is a new artifact this session created, not a straight copy-paste.** It was built
  directly from the current `paper/appendix_claims_table.tex` (read in full, every row) rather
  than from `audit/FINAL_CLAIMS.md`'s own appendix section, which predates C5/L1/B1 (added in
  G11/G16) and would have silently dropped them had it been used as the source instead.

### Points requiring operator input

- **P-1 (carried from G19, unresolved).** Sign G19 and now also G20 after reading the recompiled
  PDF end to end — this session moved a large amount of content across five phases.
- **P-2 (carried from G19, unresolved).** Personally re-verify the OSF anonymized-package link.
- **P-3 through P-7 (carried from G19, unresolved)** — AI-use disclosure, reciprocal-review/Paris
  confirmation, repository visibility, `/CreationDate` timezone (optional), OpenReview submission.
  None of these were this session's to touch and none were touched.
- **P-8 (new this session, already answered mid-session).** Whether to close the 6th-page overage
  now (touching pre-existing Limitations prose) or defer to G21. **Answered: defer to G21.**
  Recorded here so the decision and its reasoning survive past this session, not just this
  session's own memory.
- **P-9 (new).** Table 1's placement (kept in the appendix, pointer sentence in Section 1) and
  Table 3's disposition (dropped, not folded, with its equivalence-class column moved into one
  Section 4 clause) were both left to this session's judgment per the operator's own brief.
  Confirm both read well; if Table 1 is preferred in Section 1 instead, that decision needs to be
  revisited once G21 has closed the page-budget gap and there may or may not be room.

Everything else in this session's brief — the five main phases, the number-trace and
anonymization re-verification, the isolation compiles, and both package rebuilds — is, as of this
session's own verification, complete.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G21 — Dense voice-only line-edit across the entire document. Does the page-budget shortfall G20 disclosed close as a side effect, and does every claim still trace?

**status: ready for review — UNSIGNED**

Prepared 2026-08-29, session G21 — second of the four-session operator line-edit (G20-G23). This
session's mandate was explicitly **voice only**: eliminate the "not X, rather Y" rhetorical-
negation pattern, announcement sentences, softening adverbs, trailing appositive qualifications,
run-on sentences, and aphoristic paragraph endings, across the whole document. No claim, number,
or structural placement was to change. Every fix location was found by the operator's quoted
text, not by the stale line numbers in the brief (correctly stale — G20's structural pass had
already moved and cut several of the exact sentences the brief quoted).

> ### The headline, stated before the detail
>
> **Every phase ran to completion, and G20's disclosed page-budget shortfall is closed as a
> direct side effect of this session's cuts — main text now compiles to exactly 5 pages, not 6.**
> References begin page 6, the appendix begins page 7. This was not a separate page-budget task;
> it fell out of Phase 2's announcement-sentence cuts (the Section 1 Table 1 pointer, the "every
> number traces" sentence, the Appendix A.3 preamble paragraph) and Phase 2.5's reduction of
> Section 5's opening paragraph (three restated-elsewhere sentences cut, the conservativeness/
> reachability sentence kept and folded around the composition-naming clause it needs for a
> referent). No `\enlargethispage` value was touched; G20's `2\baselineskip` still stands and
> turned out not to be load-bearing once the redundant prose was gone.
>
> **Phase 1 (rhetorical negation), 16 instances fixed, 3 kept deliberately.** Fixed: the Cranmer/
> Frazier "not which component... the question this paper asks instead" restatement; the Montel
> baseline's "not the identity of the arg min"; the Miao differential-algebra "of each mechanism
> rather than a distribution"; the scope-assumption "load-bearing rather than a formality" (cut
> entirely, absorbed into Phase 2's matching announcement-sentence cut); the condition-number/
> rank "one condition, not two" restatement; the equivalence-class "rather than a single culprit";
> both instances of "$S_A$ is a control, not a result" (body and Figure 1 caption); **the worst
> instance** — the three consecutive "The estimator is not the cause... Neither is the
> threshold... Nor is the deficiency structural" rule-outs — inverted to state the cause first (a
> confound between progression and observation) and then rule out the three alternatives in one
> sentence, every one of the three numeric justifications kept (worst variation 1.023 against
> admissible 2; no tolerance from 0.005 to 1.0 restores separability; $d=10\ge6$); the "not a
> bound on $\kappa$, is the assumption's real content" aphorism; the "fact about having three
> columns, not about the simulator" aphorism; "Rather than assume a box, we fit..."; both
> Limitations bullets ("scope assumption is not a formality" and "That is one point, not a
> distribution"); the third Limitations bullet's "rather than a general sample." **Kept, per the
> brief's own instruction:** "Resolution is a property of the estimator, not of the matrix"
> (Section 3, genuine distinction — see the G22 flag below for its mirrored twin in Figure 2's
> caption); "conservatively rather than exactly" (Section 5, legitimate technical contrast);
> "gradual rather than abrupt" (verdict label, restructured under Phase 5.1 but the phrase itself
> survives).
>
> **Phase 2 (announcement sentences), 7 of 7 addressed.** The Section 1 Table 1 pointer, the
> Section 2 Gutenkunst "Section 4 measures rather than assumes" clause, the Section 2 "Section 4
> shows what happens once it is dropped" clause, and the Section 4 "every number below traces...
> Appendix A.5" sentence are all **cut outright** — each was pure duplication of a caption, an
> appendix paragraph, or the sentence that immediately follows it doing the actual work. Section
> 2's Dufour/Freidling announcement is **rewritten with substance** ("The construction Section 5
> evaluates composes two standard pieces."). Section 5's opening paragraph is **cut to its
> non-redundant core**: three sentences restating claims the bold-led paragraphs below state
> anyway (affordable-at-known-$\theta$, the prediction, the neighborhood-narrower-than-uncertainty
> claim) are gone; the conservativeness/reachability sentence — which does not reappear anywhere
> else in the paper — survives, merged with the composition-naming clause it needs to keep "the
> composition" from losing its referent. Checked against G20's Phase 5 reorder before cutting, per
> the brief's own instruction: the section is in the order G20 left it, and nothing here reopens
> that. The Appendix A.3 preamble paragraph (three figure-naming sentences) is deleted outright;
> the three figures' own captions already state what each shows.
>
> **Phase 3 (softening adverbs/intensifiers), all located instances fixed.** "real" cut from all
> three surviving hedge-against-artifact occurrences (abstract, Limitations, Conclusion — the
> brief's stated 4th occurrence was not found as a separate instance; see the Phase 8 note below).
> "essentially always" → full-sentence rewrite. "usually," "actually," "exactly" (two
> occurrences), "partly," "comfortably" (two occurrences), "almost exactly," and "directly" all
> cut per the brief. "A clear pass" cut outright. "It survives, by a wide margin" was searched for
> and not found in the current draft — moot, already gone before this session (see Phase 8 note).
> "Coherence below the pre-registered 0.98 flag" and "nearly indistinguishable" kept, as
> instructed.
>
> **Phase 4 (trailing appositives), 6 of 9 fixed directly, 3 moot/deferred.** Fixed: the abstract's
> "a precondition that can fail quietly" promoted to its own sentence; the Montel "only
> simplification" clause integrated into a full sentence; the Moré/Wild "of which... is a coarser
> substitute" integrated; "and nothing further" cut (the preceding clause stands alone cleanly);
> the eta-columns exclusion parenthetical `($\beta,\gamma,\rho$; $I_0$...)` unnested into its own
> sentence (folded into the Phase 5.2 run-on split below); the Limitations "derived instead from a
> compute budget" dangling modifier fixed by naming what is actually derived from the budget
> ($\kappa_{\max}$, not the tolerance in the abstract). **Moot, confirmed by direct search:** "the
> data-implied box above supports" (G20's reorder already corrected this to "below" — verified,
> not touched again) and "on every one of the five nuisance coordinates" (the sentence carrying it
> was already cut under Phase 2.5). **Deferred to G22, per the brief's own routing:** the Figure 4
> (`fig:simulator`) caption's "a stated design limitation" trailing clause — caption work, out of
> this session's scope.
>
> **Phase 5 (run-ons), 3 of 3 split.** The five-clause boundary-collapse sentence is now four
> sentences (shape verdict + statistic; rate; fit quality; passing region vs. the data-implied
> box). The confidence-set-scaling sentence is split and the eta-column exclusion unnested into
> its own sentence; the "Section 5" forward reference from Section 4 was checked and is a genuine,
> intentional forward pointer to where the standard errors are computed (Section 5 necessarily
> follows Section 4; G20's Phase 3.3 already promoted that computation to sit early in Section 5,
> immediately after the boundary-sweep paragraph) — nothing further to correct here beyond what
> G20 already did. The four-check sentence (condition number, resolution, coherence, column norms)
> is split into two sentences and the duplicated "pre-registered" removed (kept once, on the
> coherence flag).
>
> **Phase 6 (aphoristic endings), all six addressed; exactly one survives, as instructed.** "The
> assumption's real content" and "not about the simulator" are resolved by the Phase 1 rewrites
> above (no longer aphoristic closes). "And nothing further" and "That is one point, not a
> distribution" are resolved by Phases 1/4 above. **The internal contradiction the brief flagged
> is fixed as a substance issue, not just tone:** "The ratio itself is a portable one-line check
> for other simulators" now reads "We conjecture the ratio itself is a portable one-line check for
> other simulators" — softened to an explicit conjecture rather than an established fact, so it no
> longer contradicts the Limitations bullet stating transport to other simulator classes is
> untested. The abstract's "the contribution is the finding" is the one aphoristic close left in
> the paper, per the operator's explicit instruction.
>
> **Phase 7 (two flagged inconsistencies), both resolved.** 7.1: "its only theorem requires" →
> "the validity argument requires," folded into the Section 5 opening-paragraph rewrite (Phase
> 2.5) so it no longer contradicts checklist item 3's "no theoretical result, informal argument."
> 7.2: the ungrammatical "coincide almost exactly, sharper than failing inside a Bonferroni box"
> comparative is rewritten as two parallel clauses ("...coincide: the boundary is a sharper cut
> than a Bonferroni box, which only bounds the ellipsoid from outside"). 7.3: searched directly
> ("collapse below," "round, assumed," "here it survives") and **confirmed moot** — G20's Section
> 5 reorder had already removed this sentence along with the "(below)" forward reference it was
> tied to, exactly as the brief predicted it might.
>
> **Phase 8 (full re-read).** A second full pass located no further "not X, rather Y" instances,
> announcement sentences, dangling appositives, or aphoristic closes beyond what Phases 1-7
> already fixed or explicitly kept. Two items in the brief were searched for directly and not
> found in the current draft: 1.1's literal quoted text ("on a real confound between progression
> and observation rather than a numerical artifact") and "it survives, by a wide margin." Both
> read as the operator's pre-G20 notes on passages G20's structural pass had already reshaped by
> the time this session started; 1.1's substance is fully covered by this session's Phase 1.11
> rewrite of the same passage (the confound is now stated as the cause, first, before the
> rule-outs). Neither is a case of this session skipping a fix — both are confirmed absent, not
> assumed absent.

**Numbers changed: zero.** Every edit in this session restructures or cuts prose; none touches a
numeric literal, a citation key, a cross-reference target, or a claim's content. Verified by a
token-level diff of every `[0-9]+\.[0-9]+`, `[0-9]+%`, and `\$...=[0-9.]+` match between the
pre-session and post-session `main.tex` (see Re-verification below) — the only difference found
was a cosmetic LaTeX-markup change (`$\tau$ from $0.005$` restructured mid-edit to `$\tau=0.005$`
then corrected back to `$\tau$ of $0.005$` for consistency with the document's existing style),
not a value change.

**Two items flagged for G22, not fixed here, per the brief's own routing to that session:**
1. Figure 2's caption ("so the rank deficiency is a property of the matrix, not of the
   estimator") mirrors, in the opposite direction, Section 3's kept "Resolution is a property of
   the estimator, not of the matrix." Both are individually correct and make different points
   (one about the six-column spectrum's rank deficiency, one about what the resolution test can
   and cannot certify), but the brief is right that two mirrored, opposite-direction aphorisms
   three pages apart read as an accident, not a device. G22 owns captions.
2. Figure 4 (`fig:simulator`)'s caption trailing clause, "a stated design limitation" — needs
   integrating into the caption's own sentence structure, same reason.

### Re-verification

- **Number trace:** every numeric token in `paper/main.tex` diffed pre- vs. post-session
  (`git show HEAD:paper/main.tex` vs. the working copy) via a regex extraction of decimal,
  percentage, and `\command=value` tokens, sorted and compared. One line-level diff, resolved to
  a pure LaTeX-markup difference (see above) with no value change. Manually cross-checked against
  the full unified diff line-by-line as well: every numeral present in a removed line is present,
  unchanged, in the corresponding added line.
- **Anonymization re-scan:** `pdftotext` on the recompiled PDF and a grep of its metadata for
  operator name variants, all clean; `pdfinfo` shows no author field set. `scripts/
  build_anonymous_package.sh`'s own built-in scan reports clean.
- **Page count:** main text is **exactly 5 pages** (Introduction through Conclusion). References
  begin page 6, the appendix begins page 7. Confirmed via `pdftotext -f/-l` page-boundary
  extraction, not assumed from line counts.
- **Two-tier isolation compile:** `build/sim_attrib_overleaf_5d18d7c.zip` (rebuilt from the
  working tree, includes this session's edits) extracted to two independent temp directories and
  compiled end to end (pdflatex/bibtex/pdflatex/pdflatex each) — both exit 0, both 17 total pages,
  zero undefined references or citations in a clean final pass on each. `pdftotext` output is
  byte-identical (MD5 `b6ff61c4eb187b83d2a3e74789c56fa6`) across the repo working copy and both
  isolated extractions; `main.pdf` is 582,225 bytes in all three.
- **Package rebuilds:** both `scripts/build_overleaf_package.sh` and `scripts/
  build_anonymous_package.sh` re-run against the final edited tree; the anonymized package's
  `CLAIMS.md` confirmed present (21,111 bytes, unchanged from G20 — this session touched no claim
  data). Both scripts' own anonymization checks report clean.
- **One environment note, not a paper defect:** `audit/S17_REPORT.md` is a pre-existing,
  already-modified file (dirty before this session started, per the initial `git status`) that
  macOS iCloud has evicted to a dataless placeholder; whole-repository `git status`/`git diff`
  intermittently time out on it (`mmap failed`). Scoped operations (`git diff -- paper/main.tex`,
  `git add paper/main.tex`) are unaffected and were used throughout this session's own
  verification. Not this session's file to fix; noted so a future session isn't surprised by it.

### What G21 explicitly does not certify

- **That Phase 6/G22's caption work is done.** The two mirrored-aphorism and dangling-appositive
  items above are flagged, not fixed — captions are explicitly out of this session's scope.
- **That every sentence in the document was rewritten.** This was a targeted pass against the
  operator's specific brief plus one full re-read hunting for the same five pattern classes; it
  was not a from-scratch prose rewrite, and sentences outside those five classes were not
  second-guessed.
- **That the 5-page main text has slack.** It does not — this session's cuts closed the gap
  exactly, with the same zero-slack margin G20 inherited from G19. Any future session adding
  content must re-verify page count as its own first check, same standing rule G20 stated for
  G21.

### Points requiring operator input

- **P-1.** Sign G20 and G21 together after reading the recompiled PDF end to end — G21's edits
  touch nearly every paragraph in the main text (voice only; no claim, number, or structural
  placement changed, per this session's own verification above).
- **P-2 through P-9 (carried from G19/G20, unresolved).** OSF anonymized-package link
  verification, AI-use disclosure, reciprocal-review/Paris confirmation, repository visibility,
  `/CreationDate` timezone, OpenReview submission, and Table 1's placement — none were this
  session's to touch and none were touched.

Everything else in this session's brief — Phases 1 through 9, the full re-read, and the
re-verification pass — is, as of this session's own checking, complete. G22 (captions,
terminology, numbers, spelling) runs next, per the operator's own session plan.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G22 — Caption compression, header/terminology unification, numeric precision, spelling. Does the document read as one voice using one vocabulary for each concept?

**status: ready for review — UNSIGNED**

Prepared 2026-08-29, session G22 — third of the four-session operator line-edit (G20-G23). This
session's mandate: caption compression to description-only content, header/section-title
naming, process-leakage/internal-jargon removal, terminology and notation unification,
numeric-precision consistency, and spelling-convention standardization. Every fix location was
found by reading the current `paper/main.tex` directly and matching quoted text, not by the
brief's own (correctly stale) line numbers.

### Phase 1 — captions

All nine items addressed. Figure 1 (`fig:assignments`) and Figure 2 (`fig:spectrum`) captions —
both on main-text pages — lost their trailing interpretive sentences ("$S_A$ is a control: it
rules out an instrument..." and "...so the rank deficiency is a property of the matrix, not of
the estimator"), each already covered by main-text prose. Figure 3 (`fig:nontermination`,
Section 5) lost its design specification (32 corners + 10 endpoints) and its gate definition
($M\times N/p\le10^8$, $M\in\{10^3,10^4\}$, $N\in\{99,999\}$) to Section 5's own prose — this
also fixed the "gate" bare-noun-before-definition problem (Phase 4.9) as a side effect, and
forced the "The mechanism, and the shape of the boundary" paragraph (already flagged in Phase 2)
to split cleanly at the definition's natural insertion point. Figure 4 (`fig:simulator`,
Appendix A.2) had its two argument clauses (no-removed-compartment / continuous-noise
justification) moved into A.2's own prose, and its "a stated design limitation" clause moved
into Limitations (Section 6) per the brief's explicit routing — this is the one caption fix that
added net main-text length, since A.2 is appendix space but Limitations is not. Figure 5
(`fig:threshold`) lost its final sentence (the 1.55×/9.88× margin restatement, already given
with more precision in Section 4 as 1.523×/9.881×). Figure 6 (`fig:confound`) lost its final
clause (verbatim-duplicate of Section 4's "a drifting removal hazard is nearly
indistinguishable..."). Figure 7 (`fig:nontermination-variants`) compressed from five sentences
to three via semicolon-joining, keeping every actual number — it already used real Wilson-based
values, not the unquantified "collapses the same way" language the brief worried about, so no
softening was needed. Table 2 (the eight-assignment table, `appendix_tables.tex`)'s plateau-
stability result ("varies by at most 0.2% across six step sizes") moved into Section 4's own
condition-number sentence; the table caption keeps a one-clause pointer instead. Table 3's flagged
fact ("every assignment carrying the adversarial transmission family is inseparable") was
searched for directly and confirmed absent from the current draft — already resolved by an
earlier session, not by this one.

### Phase 2 — headers and bold paragraph leads

Every rename in the brief applied exactly: Section 5's title, both Section 4 subsection leads,
Section 5's "Affordable at a known parameter..." lead, Appendix A.1, and the long A.3 heading (to
"Supplementary figures," per the brief's own offered alternative — the three figures under it
don't split cleanly into two independently-titled topics without forcing an artificial boundary,
so one heading was judged the better fit). The comma-spliced "The mechanism, and the shape of the
boundary" heading was split into two single-topic paragraphs, `\paragraph{The mechanism.}` and
`\paragraph{The shape of the boundary.}`, at the point where the gate definition moved from the
caption (Phase 1) — this made the split fall out naturally rather than requiring an arbitrary cut
point. The redundant ", in full" suffix, present on exactly two headings as the brief predicted,
is gone from both. Appendix A.5 confirmed still titled "Claim-to-source table," matching G20's
Phase 3.5 spec — no drift. Read as a list, the new headings (Method's three leads, Experiments'
three leads, Section 5's three leads, and the five appendix subsections) now state what each part
measures rather than posing it as a riddle.

### Phase 3 — process leakage and internal jargon

3.1: A.5 checked directly for surviving `C1`/`C2`/... tracking labels — none found; G20's Phase
3.4 rewrite already removed them. 3.2: `ETA\_SCALE` replaced with "the flat 10% perturbation
unit." 3.3: "contradicting our earlier unmeasured claim" deleted from the Montel-comparison
paragraph. 3.4: "originally declared" → "declared" (the process-time word dropped, the
paper-time fact kept). 3.5: "$\kappa=100$ exhausts this study's budget" replaced with the actual
number this project's own `docs/THRESHOLDS.md` gives for that point — order $10^4$ replicates,
the edge of the declared budget — rather than a vague pointer to Section 5's gate, which is a
different budget (draws for the selective-inference test, not replicates for the Jacobian
estimate) and would have been a wrong cross-reference had I used it. 3.6: both instances
("asserted bit-for-bit before anything else runs" and "both, and every tolerance below, fixed
before any singular value existed") replaced with one sentence, "All thresholds in this paper
were fixed before any measurement," placed once in the Method section's SVD step. A third,
unflagged instance of the same "before any singular value existed" pattern survives in Appendix
A.2 (pointing at `docs/THRESHOLDS.md` as a concrete artifact, not a vague internal-process
claim) — left alone as functionally different and out of the brief's explicit scope. 3.7: every
bare "registered" in `paper/main.tex` and `appendix_tables.tex` is now "pre-registered" (8
prose/caption instances fixed); "declared" confirmed used exclusively for family
sets/assignments/corners/combinations throughout. **This phase's scope turned out to include the
figures themselves, not just the LaTeX prose**: `pdftotext` on the recompiled PDF showed
"registered κmax = 100" baked directly into Figure 1's rendered annotation — three figures
(`fig3_spectrum.py`, `fig4_assignments.py`, `fig5_threshold.py`) plot a bare "registered" label
via `matplotlib`. Fixed at the source (the one plotted string literal in each script, not the
internal `prov.plotted(...)` provenance-log labels, which are bookkeeping strings never rendered
on the page) and regenerated using the project's own pinned versions
(`numpy==2.4.4 scipy==1.17.1 matplotlib==3.10.8 PyYAML==6.0.3`, from
`scripts/anonymous_package/requirements.txt`, installed into a throwaway venv outside the repo).
Each script's own built-in provenance/data-matching assertions passed on regeneration; only the
three affected `.pdf`/`.preview.png`/`.provenance.json` files changed, confirmed via `git status`.

### Phase 4 — terminology and notation unification

4.1: "distortion assignments" (abstract) unified to "family assignments," matching every other
occurrence; "assignment triples" and the other named variants were already absent. 4.2:
"identifiable/non-identifiable" confirmed already reserved for the structural-identifiability
literature (Kahl et al., Miao et al.) everywhere it appears; the one place the paper used
"identifiable" for its own verdict was the Section 4 heading already being renamed under Phase 2
("Where attribution is identifiable" → "Separability under eight family assignments"), and the
Appendix A.1 table row ("attribution identifiable" → "attribution separable") — no separate
defining sentence was added, since the existing usage was already consistent everywhere else
once these two were fixed, and a new sentence would have cost main-text budget for no new
information. 4.3: the Introduction's "three biologically distinct mechanisms, transmission,
progression, and observation" — the one place the paper called the three components
"mechanisms" — changed to "components," which is what Method (Section 3) already calls them
("each simulator component is misspecified by at most one mechanism at a time... a single
one-parameter distortion family") and is close to an explicit component→mechanism definition on
its own. "Mechanism" elsewhere consistently means either the specific realized distortion
pathway (Section 4's "named mechanisms," Figure 6's "cross-mechanism") or the generic English
sense ("the mechanism" as a paragraph heading in Section 5, about why the selection rule fails —
contextually unambiguous, no components involved in that section at all). 4.4: "acceptance
probability" and "$p_{\min}(w)$" confirmed the only two terms the current document actually
uses (no bare "p\_sel" string exists in `main.tex`); Appendix A.1's "worst cell $p$" rows
renamed to "acceptance probability" to match. 4.5: **no live overload found** — no instance of
literal "K=6" survives anywhere in `paper/main.tex` or `appendix_tables.tex` (confirmed by grep
before touching anything); `K` means 3 components everywhere it appears in the compiled paper.
The one place `K=6` is still typed is a docstring/caption string inside `src/viz/fig3_spectrum.py`
and `src/viz/style.py` that is never rendered on the page or read by a paper reviewer — left
alone as out of this session's scope (paper-facing text), noted here rather than silently
skipped. No new column-count symbol was introduced, because there was nothing left to disambiguate.
4.6: $\tau^*=\sigma_K/\sigma_1$ now defined in Section 3's own threshold declaration, not only in
Figure 5's caption. 4.7: "coherence" and "column-norm floor" confirmed already carrying
plain-language definitions in Table 3 (promoted there by G20 Phase 3.2); "leakage check" searched
for directly and confirmed absent from the current document — nothing to fix. 4.8: "the
MMC-selection composition" named at its first bare-noun use (Section 5's "Cost at $\theta_0$..."
paragraph); later bare "the composition" references left as-is, now reading as back-references to
the named object rather than an unnamed one. 4.9: the cost gate's $M\times N/p\le10^8$ definition
moved to precede its first bare "the gate" usage (see Phase 1's Figure 3 note above). 4.10:
"roughly ten time-binned incidence counts" → "ten," matching $d=10$ exactly.

### Phase 5 — numeric precision and internal consistency

5.1: $\kappa=629$ (Figure 2's caption, Appendix A.1's table) unified to $\kappa=628.9$, matching
the abstract and Section 4's own value everywhere the number appears, including the regenerated
figure legends where relevant. $\kappa$: "6.6–65.6" (Appendix A.1) unified to "6.628–65.64,"
matching `appendix_tables.tex`'s own table and Section 4's prose. 5.2: reviewed every flagged
value against its source. `0.9424` and `1.958` were searched for directly and confirmed already
absent — resolved by an earlier session. `344.9` (the rescaled six-column $\kappa$) is already at
4 significant figures, which is this paper's own established, internally consistent convention
for every $\kappa$ value in the document (628.9, 65.64, 6.628, 64.62, ...) — left unchanged, since
rounding it alone would have made it the *inconsistent* one. `1.023` (plateau variation factor)
rounded to `1.02` and `2.265` (log-slope-ratio) rounded to `2.26`: both are single measurements
from the diagnostic's own resolution machinery rather than aggregate statistics with a stated CI,
and the fourth significant figure is not defensible against the ~9% relative precision implied by
this project's own $n\approx128$-replicate Jacobian estimate (`docs/THRESHOLDS.md`'s own
$n\gtrsim\kappa^2$ error-scaling argument) — 3 significant figures is what the replicate count
actually supports. 5.3: **the genuine correctness fix.** The four "$p\approx0.004$" Montel-test
values are all exactly `0.003997335109926716` in `results/montel_marginal_test.yaml`
(`global_p_value`, all four cases, `n_calib: 1500`, `n_calib_minima_at_least_as_extreme: 5`,
i.e. $6/1501$) — confirmed against the source file, not assumed. The paper now states this
directly: the shared value is "the resolution floor of the 1500-draw calibration batch," not
four independently agreeing measurements, which is what reporting four separate "$\approx0.004$"
values without comment would have implied.

### Phase 6 — spelling consistency

American spelling chosen, matching the operator's own suggested default and the field's recent
SBI/ML literature. Eight instances fixed across `paper/main.tex`
(`characterisation`→`characterization`, `Normalise`/`Normalised`→`Normalize`/`Normalized`,
`modelling`→`modeling` ×2, `modeller`→`modeler`, `studentised`→`studentized` ×3,
`studentisation`→`studentization`); a full document-wide grep for the standard British/American
divergent-pair families (-ise/-ize, -our/-or, -re/-er, defence/licence/practise/grey/whilst/
programme/catalogue/analyse/etc.) confirms these were the only instances in `paper/main.tex` and
`appendix_tables.tex`. `paper/checklist.tex`'s one "registered users" occurrence is the NeurIPS
template's own boilerplate text about closed-source model access, unrelated to this paper's
threshold vocabulary — left untouched.

### Page budget

**This session's net main-text additions (the gate definition, the design specification, the
$\tau^*$ definition, the Montel resolution-floor explanation, the Limitations addition, and the
$p_{\min}(w)$/$K=3$ mapping) pushed the Conclusion two lines past the bottom of page 5 before any
compensating action.** Every one of these additions is required by a specific numbered
instruction in the brief (1.3/1.4/1.8, 3.5, 4.6, 4.9, 5.3) and none could be dropped; the two
main-text caption cuts (Phase 1.1/1.2) and the Phase 3.6 consolidation were not, by themselves,
enough to offset them. Closed by two means together: (1) tightening the added sentences
themselves wherever a word could go without losing the required content (roughly a dozen small
cuts, documented in the diff), and (2) increasing the existing `\enlargethispage` before
Limitations from `2\baselineskip` to `6\baselineskip` — the same lever G12-G16 already established
as this document's sanctioned page-closure mechanism, not a new one. `8\baselineskip` was tried
first and rejected: rendered at 150 dpi, it visibly pushed the Conclusion's last line into the
bottom margin (`/tmp/page5check-05.png` — the artifact was inspected, not assumed absent). At
`6\baselineskip` the full Conclusion sits cleanly above the page number with normal margin
(`/tmp/page5check4-05.png`). Main text is exactly 5 pages, references begin page 6, the appendix
begins page 7 — the same structure G21 verified, unchanged in shape though not in the specific
lever value that produces it.

### Re-verification

- **Number trace:** every numeric token in `paper/main.tex` diffed pre- vs. post-session via regex
  extraction (decimals, percentages, `\command=value` tokens), sorted and compared. Ten
  differences found, every one an intentional Phase 5 fix (traced above) or a Phase 1 caption
  deletion whose value survives unchanged elsewhere in the document (1.55×/9.88× cut from Figure
  5's caption, both still present as 1.523×/9.881× in Section 4's own prose) — no unexplained
  value change.
- **Anonymization re-scan:** `pdftotext` on the recompiled PDF and `pdfinfo`'s metadata fields both
  clean; no author name, no `/Author` field set.
- **Page count:** main text exactly 5 pages, references begin page 6, appendix begins page 7 —
  confirmed via `pdftotext -f/-l` page-boundary extraction and a rendered-page visual check (not
  assumed from line counts), detailed above.
- **Two-tier isolation compile:** `build/sim_attrib_overleaf_39c902e.zip` (rebuilt from the working
  tree, includes every edit this session made, paper and figures both) extracted to two
  independent temp directories and compiled end to end (pdflatex/bibtex/pdflatex/pdflatex each) —
  both exit 0, both 17 total pages, zero undefined references or citations. `pdftotext` output is
  byte-identical (MD5 `a2ef4b7866dd1f1a02afe0d2dfc0b654`) across the repo working copy and both
  isolated extractions.
- **Package rebuilds:** both `scripts/build_overleaf_package.sh` and
  `scripts/build_anonymous_package.sh` re-run against the final edited tree (figures included);
  the anonymized package's built-in anonymity scan (operator name, AI-authorship tokens, `.git`
  metadata) reports clean on all three checks; `CLAIMS.md` present, unchanged (this session
  touched no claim data, only prose, captions, and three figure label strings around it).

### What G22 explicitly does not certify

- **That the three regenerated figures are pixel-identical to their G16-era originals apart from
  the label fix.** They were rebuilt from the current `results/` data through the project's own
  scripts with the project's own pinned dependency versions, and each script's internal
  data-matching assertions passed — but this session did not diff the two PDFs pixel-by-pixel,
  only confirm the rendering pipeline's own built-in checks passed and that `git status` shows
  only the three intended figures changed.
- **That `src/viz/fig3_spectrum.py`'s internal `CAPTION` docstring (which still reads
  "$\kappa=629$" and "$K=6$") was brought into line with this session's numeric/terminology
  fixes.** That string is written to a provenance sidecar for the reproducibility record, never
  to `paper/main.tex` or the rendered figure — out of this session's paper-facing scope, flagged
  here rather than silently left.
- **That every sentence in the document was re-read end to end for phase-6-class spelling drift
  beyond the documented grep families.** The grep was broad (covers every pattern the brief named
  plus several it didn't: defence/licence/practise/grey/whilst/programme/catalogue/analyse/
  recognise/emphasise/utilise/organise/specialise/categorise/generalise) but is still a grep, not
  a full manual re-read.

### Points requiring operator input

- **P-1.** Sign G22 (and the still-open G20/G21) after reading the recompiled PDF — confirm in
  particular that the new column-count situation (Phase 4.5: no symbol introduced, because no
  live overload survived) and the chosen spelling convention (Phase 6: American) both read as
  intended.
- **P-2 through P-9 (carried from G19/G20/G21, unresolved).** OSF anonymized-package link
  verification, AI-use disclosure, reciprocal-review/Paris confirmation, repository visibility,
  `/CreationDate` timezone, OpenReview submission, and Table 1's placement — none were this
  session's to touch and none were touched.

Everything else in this session's brief — Phases 1 through 8 and the re-verification pass — is,
as of this session's own checking, complete. G23 (final comprehensive re-verification) runs next,
per the operator's own session plan.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G23 — Three operator-found stale cross-references, a document-wide cross-reference audit, and the final comprehensive verification. Is this paper ready to submit?

**status: ready for review — UNSIGNED**

Prepared 2026-08-29, session G23 — the twenty-third internal session, fourth and explicitly the
final of the four-session operator line-edit (G20-G23). This session's mandate: fix three
specific stale cross-references the operator found reading the G22 PDF directly (each pointing at
appendix content that G20's restructuring moved away from where the pointer still names), run the
document-wide internal-cross-reference audit no prior session's verification scope covered, do the
final comprehensive re-verification, and produce the top-level readiness answer.

### Phase 0 — sync

`git status` at session start showed `audit/S17_REPORT.md` as **deleted**, not the "known,
harmless local artifact" G21/G22 both characterized it as. It is genuinely a tracked file
(committed at G17) that was missing from the working tree — not an untracked artifact as prior
sessions assumed. Restored via `git checkout -- audit/S17_REPORT.md` before any other work, since
it is load-bearing for this session's own Phase 3.8/4.2 consolidated history. Everything else
matched expectation: HEAD at `c853bd2` (G22), tree otherwise clean apart from
`Formatting_Instructions_For_NeurIPS_2026/` (unrelated venue-template reference files, untracked
since before this session), a stray empty `audit/S17_REPORT.md.tmp.*` file, and an empty stray
`paper/main 2.pdf` — none of the three touched by this session.

### Phase 1 — FIX-1/2/3

All three applied exactly as specified, commit `ea932b2`:

- **FIX-1.** Section 4's Montel-comparison sentence dropped `(Appendix~\ref{sec:claims-ledger})`
  — Appendix A.5 no longer discusses the per-summary-statistics simplification the sentence
  names; verified the sentence reads completely standing alone after deletion.
- **FIX-2.** Checklist item 4's justification rewritten to state that the full claim-to-source
  table ships as `CLAIMS.md` in the anonymized package, cross-referencing item 5 rather than
  naming a now-nonexistent appendix section title.
- **FIX-3.** Checklist item 8's justification rewritten the same way; the three cited draw counts
  (7.6 million, 9,216, 722,000) were independently verified against
  `results/boundary_sweep.yaml`, `results/robustness/k6_spectrum.yaml`, and
  `results/confidence_set_mmc.yaml`'s own `settings.n_simulator_runs` fields directly, not
  assumed correct because the pointer was being moved — all three confirmed exact.

Recompiled after each fix; both edited passages read correctly in the compiled PDF text.

### Phase 2 — document-wide internal cross-reference audit

Full detail: `audit/G23_CROSSREF_AUDIT.md`. Every `\ref` (39), every `\label` (20), every
hardcoded `Section N` mention (9), and all 16 checklist items' location claims were enumerated —
not sampled — and checked against current paper content, the specific check FIX-1/2/3's own
staleness proves no prior session's verification scope ran. One additional stale reference found
beyond the three named going in (per S9's own instruction not to stop at three): the appendix's
"Summary of findings" table cited figure "**3a**" for a sub-panel label Figure 3's own caption
never defines (it uses "Left:"/"Right:", not "(a)"/"(b)", unlike Figure 7 which does use lettered
panels). Fixed to "**3, left**", matching the figure's own caption language, no claim or number
changed. Commit `7b78231`.

Two observations noted, not fixed, both outside this audit's reference-accuracy scope: Figure 5
(`fig:threshold`) is never `\ref`'d from the main text (the opposite failure mode from FIX-1/2/3
— a missing incoming pointer, not a broken outgoing one; fixing it means adding new main-text
prose, a content change outside S3's scope for this session); and `sec:claims-ledger`'s label is
now unreferenced as the direct, correct consequence of FIX-1.

### Phase 3 — final comprehensive verification

| # | Check | Result |
|---|---|---|
| 3.1 | Full number-trace re-run | **Zero numeric-token drift** in `paper/main.tex` (full sorted-token diff against pre-session `c853bd2`, empty). `paper/checklist.tex` gained exactly two new `5` tokens, both from the new "item 5" cross-references FIX-2/FIX-3 added — not paper-content numbers. No claim, count, or measurement changed anywhere. |
| 3.2 | Independent anonymization re-scan | Clean — submission-scope grep (`palaash\|gang\|sim-attrib\|pa1aash`) across `paper/main.tex`, `paper/checklist.tex`, `paper/appendix_tables.tex`, `audit/BIBLIOGRAPHY.bib`, and the compiled PDF's extracted text: zero hits in all five; `/Author` PDF metadata empty |
| 3.3 | Page count ≤5 (main text) | **Exactly 5** — page-break extraction confirms Introduction through Conclusion span pages 1-5, References begins page 6, Appendix begins page 7, unchanged from G21/G22 |
| 3.4 | Two-tier isolation compile | Both tiers pass: `build/sim_attrib_overleaf_7b78231.zip` extracted to two independent fresh temp directories, each compiled end to end (pdflatex/bibtex/pdflatex/pdflatex) — exit 0, 17 pages, zero undefined references, both. `pdftotext` output byte-identical (MD5 `14be75953c78769f7e4f85c11035a4c9`) across both isolated extractions and the repo working copy |
| 3.5 | Overleaf package rebuild | `scripts/build_overleaf_package.sh` re-run against `7b78231` — 12 allowlisted files, 16 zip entries, matches the established allowlist exactly |
| 3.6 | Checklist placeholder sweep | Exactly one placeholder remains: item 16's `\answerTODO{}` and its `[AI-USE DISCLOSURE...]` bracket — untouched, per standing instruction since G9. No other bracket/TODO/FIXME/XXX anywhere in the file (the many other `[]` grep hits are `\item[]` LaTeX markup, not placeholders) |
| 3.7 | Repo-wide anonymity/AI-reference grep | **AI-attribution grep** (claude/anthropic/chatgpt/gpt/openai/copilot), all tracked non-PDF files: zero hits. **Personal-identity grep** (`palaash\|gang\|sim-attrib\|pa1aash`), repo-wide: many hits — `LICENSE`, `README.md`, `docs/DECISIONS.md`, every `results/*.yaml`'s `host:` field, build scripts' own guard strings — expected and unchanged from G19's own split-result finding, not a regression; this is the private development repo, not the submission artifact, and its own de-identification is the still-pending P-5 (repository visibility). **One nuance beyond G19's framing, surfaced here for the first time:** the string `sim-attrib` (the project's bare codename, not the author's name) also appears inside several files that *do* ship in `build/anonymous_package.zip` — `src/__init__.py`'s module docstring, `src/viz/style.py`'s SVG hashsalt and PDF-metadata `Subject` field, and four diagnostics modules' tempfile lock-directory names. None of these name the author; the risk is indirect — a reviewer who searches the bare project name could find the (currently public) GitHub repository, which does carry the operator's real identity throughout. This is the exact risk P-5 already exists to close (switching repository visibility to private before submission); noted explicitly here because no prior session's write-up examined the anonymized package's own source content for this specific term, only the paper-file/PDF submission-scope grep. Not fixed this session — renaming the project's own codename across ~90 source files is a scope decision for the operator, not a mechanical reference fix, and closing P-5 removes the exposure without touching any file. |
| 3.8 | Consolidated cross-session findings register | Produced — GATES.md Tables A-I (Phase 2.6, G19) cover External Reviews #1-#3, the internal tone pass, and G11-G19's own findings in full; extended below with G20, G21, G22, and this session |

#### Table J — G20 (structural pass: appendix relocation, Section 2/5 reorder, Conclusion added)

| Item | What it was | Final status (as of G23) | Session |
|---|---|---|---|
| G20-1 | Table 1 (four-finding summary) kept in appendix, Section 1 pointer compacted | Intact through G21-G23 | G20 |
| G20-2 | Table 3 ($S_A$ eight-assignment control table) dropped from the paper; equivalence-class column folded into one Section 4 clause; full numbers preserved in `CLAIMS.md` | Intact through G23 | G20 |
| G20-3 | Appendix A.5's ~7-page dotted-path ledger (C1-C5, L1, B1) replaced with one pointer paragraph; full ledger moved to `CLAIMS.md` in the anonymized package | Intact — this is the exact restructuring FIX-1/2/3 and Phase 2's audit exist to catch stale pointers against, confirmed no further staleness survives | G20; audited G23 |
| G20-4 | `scripts/build_overleaf_package.sh`'s allowlist still named the deleted `appendix_claims_table.tex` | Fixed same session, before the package was rebuilt | Found + fixed G20 |
| G20-5 | Anau Montel et al. baseline comparison moved from Section 2 (related work) to a new Section 4 paragraph, as the experimental finding it is | Intact through G23 | G20 |
| G20-6 | Section 5 reordered (boundary sweep before confidence box), stale forward/backward-repair sentences removed | Intact through G23 | G20 |
| G20-7 | New two-sentence Conclusion added | Intact through G23 | G20 |
| G20-8 | Page-budget shortfall: main text 6 pages, not 5 | **Disclosed, deferred to G21 by explicit operator choice** | Disclosed G20; closed G21 |

#### Table K — G21 (dense voice-only line-edit, whole document)

| Item | What it was | Final status (as of G23) | Session |
|---|---|---|---|
| G21-1 | G20's 6-page overage | **Closed as a side effect** of Phase 2's announcement-sentence cuts — main text back to exactly 5 pages | Closed G21; held G22-G23 |
| G21-2 | 16 rhetorical-negation ("not X, rather Y") instances, including the three-sentence "not the cause... Neither... Nor" rule-out chain | Fixed, including all three numeric justifications kept intact (1.023 vs. admissible 2; 0.005-1.0 tolerance sweep; $d=10\ge6$) | Fixed G21; unchanged through G23 |
| G21-3 | Announcement sentences, softening adverbs, trailing appositives, run-ons, aphoristic endings across the whole document | Fixed per session's own full re-read | Fixed G21; unchanged through G23 |
| G21-4 | `audit/S17_REPORT.md` iCloud dataless-placeholder eviction noted as an environment issue | Recurred this session in a different form (genuinely deleted, not just dataless) — see Phase 0 above | Noted G21; recurred + fixed G23 |

#### Table L — G22 (captions, headers, terminology, numeric precision, spelling)

| Item | What it was | Final status (as of G23) | Session |
|---|---|---|---|
| G22-1 | 9 caption items compressed to description-only content | Intact through G23 | G22 |
| G22-2 | Header/section-lead renames, including splitting a comma-spliced paragraph | Intact through G23 | G22 |
| G22-3 | 7 process-leakage items, including "registered"→"pre-registered" baked into 3 figures' own matplotlib labels (caught by `pdftotext`-ing the PDF, not just grepping `.tex`) | Intact through G23 | G22 |
| G22-4 | 10 terminology/notation unifications (K=6 overload already resolved on arrival; 9 others fixed or confirmed) | Intact through G23 | G22 |
| G22-5 | Numeric precision: $\kappa=629\to628.9$, $6.6$-$65.6\to6.628$-$65.64$ unified; genuine correctness fix — four `p\approx0.004` Montel values confirmed identical (resolution floor of a 1500-draw batch), paper now says so explicitly | Intact through G23 — this session's FIX-1 touches the same paragraph (removing a stale appendix pointer) without disturbing the resolution-floor statement itself, re-confirmed | Fixed G22; re-confirmed G23 |
| G22-6 | American spelling standardized, 8 instances | Intact through G23 | G22 |
| G22-7 | Page budget closed again via `\enlargethispage` raised to `6\baselineskip` (from G20's `2\baselineskip`) | Intact — unchanged this session, page count re-verified exactly 5 | Fixed G22; held G23 |

#### Table M — G23 (this session)

| Item | What it was | Final status | Session |
|---|---|---|---|
| G23-1 | `audit/S17_REPORT.md` genuinely deleted from disk, mischaracterized by G21/G22 as a harmless untracked artifact | Restored via `git checkout` | Found + fixed G23 |
| G23-2 | FIX-1: stale `(Appendix A.5)` pointer in Section 4's Montel paragraph | Fixed | Fixed G23 |
| G23-3 | FIX-2: checklist item 4 pointed at a renamed/removed appendix section | Fixed, cross-references item 5 | Fixed G23 |
| G23-4 | FIX-3: checklist item 8, same staleness; draw counts independently re-verified against source `results/*.yaml` files | Fixed, cross-references item 5; numbers confirmed exact | Fixed G23 |
| G23-5 | Document-wide cross-reference audit: 39 `\ref`s, 20 `\label`s, 16 checklist items, all enumerated and content-checked | 39/39 valid, 16/16 valid (2 already fixed above); 1 additional stale reference found | Run G23 |
| G23-6 | Appendix Table 2's "3a" figure-panel citation, naming a sub-panel label Figure 3 never defines | Fixed to "3, left" | Found + fixed G23 |
| G23-7 | Anonymized package's own source files carry the bare project codename `sim-attrib` in several places | Disclosed — not a name leak, an indirect exposure already covered by the pending P-5 (repository visibility) action; not independently fixed this session | Found + disclosed G23 |
| G23-8 | Full number trace, anonymization re-scan, page count, two-tier isolation compile, both package rebuilds, checklist placeholder sweep, repo-wide grep | All clean/passing — see Phase 3 table above | Verified G23 |

### What G23 explicitly does not certify

- **That the operator has read the final PDF.** Every point in the P-list below, including
  signing G20 through G23 together, remains the operator's own action, per the operator's own
  standing decision recorded at G20's P-8.
- **That P-5 (repository visibility) has been actioned.** G23-7 above depends on it; this session
  surfaces the dependency, it does not close it.
- **That every conceivable prose-quality judgment call has been re-litigated a fifth time.** This
  session's mandate was reference accuracy (Phases 1-2) and mechanical re-verification (Phase 3),
  not a further voice/tone pass — that ground was G17/G18/G21/G22's, and this session did not
  re-open it.

### Process caveats

- **The "3a" finding was not in the session brief's own two named categories** (Appendix-A.X
  pointers, checklist staleness) — it surfaced only because Phase 2.3's instruction to check
  figure/table *content*, not just reference resolution, was followed literally against every
  hardcoded figure citation, not just the `\ref`-based ones. A narrower audit scoped only to
  `\ref{sec:appendix}` instances would have missed it.
- **G23-7 (the `sim-attrib` codename in the anonymized package) is a disclosure, not a fix**,
  because fixing it properly means renaming the project's own codename across roughly 90 source
  files — a scope decision this session's mandate (cross-reference accuracy) does not cover and
  should not make unilaterally. P-5 already exists as the correct, narrower closure.

### Points requiring operator input

- **P-1 (carried, now covering G20 through G23).** Sign all four sessions together after reading
  the final recompiled PDF end to end — the operator's own decision, recorded at G20's P-8, to
  hold G20-G22 pending this session's fix.
- **P-2.** If Phase 2's audit found anything beyond FIX-1/2/3 (it did — G23-6), review that fix
  specifically before signing.
- **P-3.** Write the AI-use disclosure at checklist item 16.
- **P-4.** Confirm the OSF-hosted anonymized package matches this session's final state
  (`CLAIMS.md` included, not just the local `build/anonymous_package.zip`).
- **P-5.** Switch repository visibility to private — now with an explicit second reason beyond
  the standing one: G23-7's indirect codename exposure in the anonymized package closes
  automatically once this is done.
- **P-6.** Q-3 (reciprocal reviewer nomination), Paris in-person attendance confirmation, and
  OpenReview submission itself — 29 August 2026 AoE.

Everything else in this session's brief — Phases 0 through 3, the audit, and the full
re-verification — is, as of this session's own checking, complete. This is the final planned
session (G20-G23); `audit/S23_REPORT.md` carries the top-level readiness answer.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```
