# S9 — Session G9 report

**For a reader who has not seen this session.** Written 2026-08-24.

> ## THE PAPER HOLDS TOGETHER AS AN ARGUMENT. IT DOES NOT FIT THE PAGE LIMIT.
>
> **Not submission-ready pending only the operator's disclosure text and a final visual
> check — one real, unclosed gap remains.** Three mechanical fixes from the operator's
> decisions are done and verified: the title, the figure move, and the AI-use disclosure
> placeholder. A genuine adversarial review of the paper as an argument — cold-read first,
> cross-checked against the audit trail second — found two real defects and fixed both: a
> citation-rendering bug where a compound surname's own six-session-old documented correction
> had never been enforced at the BibTeX level, and a readability regression this session's own
> page-limit compression introduced in the introduction. **What it did not do is close the
> page limit.** The draft narrowed from 6 pages with 150-240 words of overflow per page down to,
> at its tightest, a single clause — then a genuine readability fix traded some of that back.
> Current state: **6 pages, roughly 116 words over Sim2Science's 5-page limit.** Closing the
> rest means cutting real content or more readability, and this session did neither
> unilaterally, following S7's instruction to flag rather than force it through.

---

## 1. WHAT THIS SESSION DID

| Path | Status |
|---|---|
| `paper/main.tex` | Title changed; simulator schematic moved to appendix with all references updated; three of four sections converted to tight `enumitem` lists (Background, Limitations, and the introduction's finding preview); figure widths and placement specifiers adjusted throughout for page-fit; `\hypersetup{pdftitle=...}` added, fixing empty PDF metadata pre-existing since G8 |
| `paper/checklist.tex` | G8's own answer to the "Declaration of LLM usage" item replaced with an operator-completed placeholder, per operator instruction |
| `audit/BIBLIOGRAPHY.bib` | Montel entry's compound surname braced (`{Anau Montel}`) to fix a citation-rendering bug found in adversarial review |
| `audit/G9_PAPER_ADVERSARIAL_REVIEW.md` | **new** — the review itself, structured verdict-first per this project's established pattern |
| `DEVIATIONS.md` | **D-19** — the Montel bug's root cause and the general lesson |
| `GATES.md` | **G9 added**, unsigned |
| Seven zombie shell processes | Killed — an environmental artefact from an unrelated session, not this project's own defect (§4) |
| `results/`, `figures/`, `src/` | **untouched.** No figure regenerated, no results file rewritten |

---

## 2. THE THREE MECHANICAL FIXES, AND ONE THING WORTH NOTING ABOUT EACH

**Title.** Changed to *"Diagnostics and Limits for Component-Level Simulator Misspecification"*
— the alternative G8 drafted and flagged rather than substituted. No em-dash, no colon, checked
against the operator's stated preference. The compiled PDF's own metadata title was empty
before this session (a gap pre-existing since G8, not introduced here — `\title{}` alone
doesn't populate `pdftitle` in this document class) and is now set correctly; `pdfauthor`
deliberately left empty for anonymity.

**Figure move.** The operator's brief named the figure to move as *"Figure 2 (the simulator
structure schematic)"* and explicitly hedged that this might not match the actual rendered
numbering — *"confirm against the actual file before editing."* It did not match: compiling and
reading the actual PDF showed the simulator schematic rendering as **Figure 1**, not Figure 2,
before this session touched anything. The figure named by content (the simulator schematic,
`fig2_simulator.pdf` by filename) was moved to the appendix; the operator's filename-based
identification was correct even though the rendered number wasn't what the brief guessed.

**AI-use disclosure placeholder.** Located by reading the template files this project already
has locally (`neurips_2026.sty`, `neurips_2026.tex`, `checklist.tex`) rather than fetching the
NeurIPS Main Track Handbook. **This is a real scope limitation worth naming precisely**: the
checklist's own "Declaration of LLM usage" item is the only disclosure mechanism any local
template file calls for, and the placeholder was put there — but this session did not fetch and
read the actual NeurIPS 2026 LLM-use policy the checklist references, so it cannot certify that
a checklist-item-only placeholder is where the operator's eventual disclosure text should
actually live, only that no local file suggests otherwise. `audit/S8_REPORT.md` P-4 already
named the underlying policy as unread across eight sessions; it is still unread after nine.

---

## 3. THE ADVERSARIAL REVIEW, AND WHAT MADE IT REAL RATHER THAN PRO FORMA

The brief asked for a cold read before cross-checking the audit trail, specifically so a fresh
reaction wouldn't be contaminated by already knowing the intended answer. That ordering is what
surfaced the introduction's readability problem — a reviewer reading start to finish hits four
long, structurally identical sentences in a row and notices it as friction, in a way that
checking each sentence against a rubric one at a time would not have caught.

**The Montel citation bug is the review's most consequential single finding.** It is not a new
kind of error for this project — it is the same class of defect D-18 named in `DEVIATIONS.md`
one session ago (*"a file that documents what should be true is not the same as the file being
true"*), now found a layer deeper: a correction that was not merely undocumented but
**documented and still not enforced**, in a comment written six sessions before this one that
correctly identified exactly what needed to happen and then didn't happen. It was caught only
because this session compiled the paper and read the actual rendered citations rather than
trusting the `.bib` file's own text, which is precisely the discipline `audit/PAPER_NUMBER_VERIFICATION.md`
established for numbers in G8 and this session extended to citations.

**What the review confirmed rather than found**: the C1 amendment holds under a second,
independent drift-hunt; the abstract and body agree about what the MMC composition is and
isn't; the negative-result section reads as confident reporting rather than apology; and all
four standard reviewer objections (single-simulator generalization, "just needs more compute,"
the scope-assumption's restrictiveness, "what's new here") have direct textual answers. None of
this is a new claim this session originated — it is a second check on claims G8 already made,
and it agreeing with G8 is worth exactly as much as an independent check agreeing usually is:
meaningfully reassuring, not proof.

---

## 4. AN ENVIRONMENTAL FINDING, RECORDED BECAUSE IT IS NOT THIS PROJECT'S DEFECT

A genuinely large fraction of this session's wall-clock time went to git and compile commands
hanging for one to five minutes at a time, previously attributed (by this session, initially,
and by prior sessions' reports) to generic "machine load." **It had a specific, findable
cause.** Seven shell processes from an entirely different, days-old session — different working
directory hash, timestamped "Thursday" — were stuck in a genuine infinite loop: each was
polling `pgrep -f "diagnostics.run_diag"` to detect when some script finished, but that grep
pattern matched the polling processes' own command line (which contains the literal string
`"diagnostics.run_diag"` as part of the `pgrep` invocation being run), so the exit condition
could never become true. Seven processes, each burning CPU on an unbounded sleep-check-repeat
loop, for what the process start times suggest was several days.

**This is disclosed here rather than filed as a project defect because it isn't one** — it is
an artefact of running many concurrent Claude Code sessions on one machine, which this
project's own prior reports (`audit/S7_REPORT.md`, `audit/S8_REPORT.md`) already disclosed as a
standing condition (*"the machine was loaded throughout... shared with unrelated work"*). What
this session adds is a specific mechanism for one recurring instance of it, and the fact that
killing seven identifiable, provably-stuck processes is different from that generic disclosure
— it was an actual bug (a self-matching `pgrep` pattern) with an actual fix, not merely
background contention this project has no standing to touch. The seven processes were killed;
remaining load on the machine is from other, legitimate, currently-running Claude Code
sessions, which this session did not and should not touch.

---

## 5. THE TEN-SESSION TRAJECTORY

Extending `audit/S8_REPORT.md` §6.

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
| **G8** | **C1 amended, by the operator; the draft written** | **DRAFTED, NOT SUBMITTABLE AS-IS** — a page over limit, unsigned | *(nothing new killed; the first session that produces the actual submission artefact and finds it does not yet fit)* |
| **G9** | **the draft attacked as an argument, by this session itself** | **NARROWED, STILL NOT SUBMITTABLE** — two real defects found and fixed, the page gap cut by roughly half but not closed | *(nothing killed; the first session whose job was adversarial review of prose rather than of numbers)* |

| | G4 | G5 | G6 | G7 | G8 | **G9** |
|---|---|---|---|---|---|---|
| Verdict | SPLIT | WEAK | FAIL | SCOPE CLOSED | DRAFTED, OVER LIMIT | **NARROWED, OVER LIMIT** |
| **A submittable-length draft** | n/a | n/a | n/a | n/a | no — 6pp | **no — 6pp, ~116 words over (was ~200+ words/page)** |
| A compiling paper.pdf | n/a | n/a | n/a | n/a | yes | **yes, and re-verified after every edit this session** |
| **Adversarial review of the prose itself** | n/a (diagnostic only) | n/a | n/a | n/a | no | **yes — 2 real defects found and fixed** |
| Citation-rendering defects found by reading compiled output | n/a | n/a | n/a | n/a | no | **yes (1, fixed)** |
| Independent review | no | no | no | no | no | **no** |
| Google Scholar searched | no | no | no | no | no | **no** |

### The shape of it, read honestly

**This is the first session whose job was reading rather than writing or measuring**, and the
distinction matters for what "progress" means here. G0 through G6 each lost or qualified a
claim through measurement; G7 closed the scope; G8 produced the artefact. G9 did not produce
new numbers, new figures, or new claims — it read what exists, adversarially, and found two
real things wrong with it that no prior session's checklist-style verification would have
caught, because both were failures of *rendering* (a citation that looked right in the source
and wrong in the output; a paragraph that was individually correct but collectively hard to
read) rather than failures of fact. That is a different kind of defect than this project has
mostly hunted for, and finding two of them in one session's single read suggests there may be
more of the same kind not yet found — stated as a real possibility, not a criticism of this
session's thoroughness, which was genuine.

**What is genuinely better than it was.** Three operator decisions executed and verified. A
second independent check on the paper's central framing risk (C1 drift) found nothing, which is
meaningfully more assurance than one check alone. A citation that would have rendered wrong in
front of reviewers who, per `audit/VENUE.md`, include people from exactly this literature, now
renders right. The page-limit gap — the single largest problem G8 left open — is roughly halved.

**What is not.** The page limit remains open. The actual NeurIPS LLM-use policy remains unread,
across nine sessions since the CFP first named the requirement to follow it. No independent
reader has been anywhere near this paper — the adversarial posture in this session is still one
session reading its own and its predecessor's prose, and calling that posture "hostile" doesn't
make it independent.

---

## 6. PROCESS CAVEATS — what this session did badly or not at all

- **The page-limit gap, restated because it is the largest open item**: approximately 116 words
  of body content over the 5-page limit, after this session narrowed but did not close it. **P-3.**
- **A significant share of tool calls went to page-fitting mechanics** rather than to the
  adversarial review the brief actually asked for as the substantive task. The review that
  happened was real, but a cleaner starting point would have left more room for it.
- **The AI-authorship/venue-eligibility tension G8 surfaced is untouched.** Not this session's
  scope by explicit operator decision, and this report does not attempt to resolve it — but it
  is worth noting that the actual policy remains unread and the placeholder this session
  inserted is located by inference from local template files, not by reading the venue's own
  authoritative statement of where LLM-use disclosure belongs.
- **The environmental hang (§4) cost real session time before its cause was identified.**
  Diagnosed and fixed mid-session rather than at the start, because the first several instances
  were treated as ordinary transient slowness rather than investigated.
- **No literature check has ever run on the non-termination finding.** Unchanged since G7.
- **`audit/CLAIM_GRAPH.md` is still superseded rather than rewritten.** Ninth session flagged,
  tenth session still not done.
- **Google Scholar still not searched.** Tenth session. **O-7.**
- **The adversarial review was one session's single pass.** A second reader, with no exposure
  to this project's own framing of its findings, might find things this one didn't.

---

## 7. WHAT SHOULD HAPPEN NEXT

1. **Read the actual compiled PDF.** **P-1.** Same standard as every gate since G7: a report
   summarizing changes is not sufficient for judging whether prose actually reads well.
2. **Decide the page-limit question**, now narrowed to roughly 116 words rather than a full
   page. The two live options are cutting the last Limitations item or accepting the current
   length and treating the 5-page figure as a target rather than a hard constraint pending
   confirmation of exactly how strictly Sim2Science enforces it. Not this session's call to make
   twice.
3. **Write and insert the actual AI-use disclosure**, at the placeholder in `paper/checklist.tex`.
   **P-2.** Consider reading the actual NeurIPS LLM-use policy first, given the placeholder's
   location was inferred rather than confirmed against that policy directly.
4. **Sign or reject G9.**
5. **Consider a second, differently-postured adversarial pass** before submission, given this
   session's own finding that the checklist-style review style (G8's own drift-hunt) and the
   cold-read style (this session's) caught different classes of defect — there may be a third
   class neither has tried.

---

## 8. POINTS REQUIRING OPERATOR INPUT

| # | Point | Notes |
|---|---|---|
| **P-1** | **Sign or reject G9 — after reading the actual compiled PDF** | `GATES.md`. Reading this report is not sufficient |
| **P-2** | **Write and insert the AI-use disclosure** | Placeholder in `paper/checklist.tex`, per operator decision 3 |
| **P-3** | **The remaining page-limit gap** | ~116 words over, down from a full page; §2 of `audit/G9_PAPER_ADVERSARIAL_REVIEW.md` has the detailed accounting |
| **P-4** | **Q-3** (reciprocal reviewer), Paris in-person attendance | Unresolved since G0, now genuinely time-relevant |

*Repository visibility is settled by D-11 and is not on this list.*

---

## 9. THE ONE-PARAGRAPH VERSION

Three operator decisions executed and verified: the title, the figure move (confirmed against
the actual compiled PDF rather than the filename convention the brief itself flagged as
possibly wrong), and an AI-use disclosure placeholder that replaces G8's own answer with
something the operator will complete. A genuine adversarial review — cold read first,
audit-trail cross-check second — confirmed the C1 amendment holds under a second independent
check and found two real defects nothing else in this project's process would have caught: a
citation whose own six-session-old documented correction was never enforced at the BibTeX
level, silently dropping part of an author's name in every in-text citation, and a readability
regression this session's own compression introduced. Both are fixed. The page limit is not:
narrowed from a full page of overflow to roughly a paragraph's worth, and closing the rest would
mean cutting real content or the readability fix this session just made, which is exactly the
kind of trade-off flagged for the operator rather than forced through. An unrelated
environmental problem — seven stuck processes from a different session, caught in a
self-matching infinite loop — explains hangs this and prior sessions had attributed to generic
machine load; it is fixed and disclosed as not being this project's own defect.
