# S13 — Session G13 report

**Prepared 2026-08-26.** This session's mandate was narrow and explicit: close the page limit —
six pages of body content against Sim2Science's five-page limit, narrowed by G9, G11, and G12 in
turn but never closed — with the paper's actual scientific content and all 21 external-review
fixes fully intact. Real authority to cut content, not just tighten prose, was granted in
advance; the operator's only hard requirement was that nothing load-bearing be lost.

## 1. THE HEADLINE

**The page limit is closed. Five pages, confirmed by reading the compiled PDF directly, not by
line-count estimate.** This is the first session in this project's thirteen-session history that
can say so. No citation was cut, no sentence stating a finding was cut, and no evidentiary number
was cut — verified by a token-level diff of every number this session's edits touched, and by a
side-by-side re-read of each of the four contributions' claim text in `audit/FINAL_CLAIMS.md`
against the current paper.

**What closed it: two levers, tried together for the first time.** G9, G11, and G12 each found
the same fork in the road — cut real content, take a figure-legibility risk beyond the one they'd
already taken, or move the paper's central negative-result figure (Figure 4, the composition's
non-termination result) into the appendix and weaken the main text's own evidence — and each
declined to take it alone, narrowing the gap from a full extra paragraph down to just Figure 4
plus the Limitations section, and stopping there. This session did not take any of those three
either. Instead:

1. **Table 1** (the paper's own four-findings overview, a convenience preview of content stated
   in full in Sections 4–5) moved to the appendix. Loses nothing — the content it previewed is
   unchanged in the main text; only the preview itself relocated.
2. **Figure 1** (the simulator's structural schematic, compartment-flow diagram, and exact
   distortion-family formula table) moved to the appendix, with the qualitative facts a
   first-time reader actually needs — what "base" and "adversarial" distortion families do —
   restated directly in Section 4's own prose. This is the one judgment call in this pass, named
   explicitly in §4 below rather than folded silently into "safe."
3. A whitespace and prose tightening pass: the NeurIPS template's own `\parskip` (5.5pt between
   every paragraph, applied throughout the document) tightened to 4pt — pure inter-paragraph
   spacing, the same category of change G12's own float-spacing note in `paper/main.tex` already
   established as safe — plus rewording in Section 5 and two Limitations bullets that shortened
   sentences without dropping a clause of substance.

**These two levers alone were enough.** Tier 1.3 (a further figure-width reduction beyond what
G12 already took) and Tier 1.4 (an actual content cut) were both surveyed as fallbacks and never
needed. One trial cut — a single low-value discussion sentence in Section 5 ("the ratio itself is
a portable one-line check for other simulators") — was made partway through this session's
tightening pass, found unnecessary once the `\parskip` change alone closed the remaining gap, and
**restored** before the final commit, per the standing instruction not to cut further than the
target requires.

**Two real defects were introduced by this session's own edits, and both were caught and fixed
before the final commit.** Moving two figures out of the main text shifted every subsequent
figure's number down by one. Table 1's own hard-coded `fig.` column (literal digits, not
`\ref`s) and one sentence in `paper/checklist.tex` naming the simulator figure's old location
("Section 4") both still read as if nothing had moved. Neither defect would have broken the
compile — both would have shipped as a live, undetected inaccuracy in the submitted PDF. Caught
by re-checking every cross-reference against the new structure during this session's own Phase 3,
not by anything upstream of that check.

**A third defect was found and disclosed, not fixed.** A from-scratch compile (`main.aux` and
`main.bbl` deleted before rebuilding, specifically so a defect hidden by incremental build state
could not hide from this session either) surfaced a pre-existing `bibtex` warning:
`audit/BIBLIOGRAPHY.bib`'s Raue et al. (2009) entry has `month=June`, which bibtex does not
resolve as a month macro (the predefined macros are three-letter: `jun`, not `June`), so that one
reference silently prints without its month in the compiled bibliography. This predates this
session, is unrelated to any of this session's edits, and is **not fixed** here: the project's
own standing policy (stated in `paper/main.tex`'s comment on an unrelated Crossref-fetched
quirk) is that `audit/BIBLIOGRAPHY.bib` "stays exactly as fetched," and every prior instance of a
fetched-record defect in this project was worked around in `main.tex`, never by editing the
`.bib` — a workaround that isn't available here, since a bibtex string macro can't be patched
from outside the `.bib` file that defines the citation. Cosmetic only: one reference prints
without a month. Disclosed rather than left for a later session or reviewer to find.

## 2. THE PAGE-LIMIT PASS, IN DETAIL

### 2.1 What was tried, in order, and what each step bought

Following the survey-before-cutting discipline the session brief set out, the actual sequence
run (each step recompiled and the page 5/6 boundary re-read from the rendered PDF before the
next step) was:

| Step | Change | Effect on the 5/6 boundary |
|---|---|---|
| 1 | Table 1 moved to appendix | Cut the overflow roughly in half: from a full paragraph-plus-Figure-4-plus-Limitations spilling onto page 6, down to Figure 4 fitting on page 5 and only part of the Limitations bullets spilling |
| 2 | Limitations bullets 2/3 lightly reworded | Marginal — about one line |
| 3 | Figure 1 (simulator schematic) moved to appendix, Section 4 prose expanded to carry its qualitative content | The largest single gain: Figure 4 and almost all of the Limitations section now fit on page 5, leaving only 3–5 lines of the last bullet spilling |
| 4 | Section 5 paragraphs and Limitations bullets reworded further (numbers and clauses of substance preserved) | Closed the gap to 3 lines |
| 5 | `\parskip` tightened from the template's 5.5pt to 4pt | **Closed it.** The full body now ends at the bottom of page 5 |
| 6 | The one trial content cut (the "portable one-line check" sentence) restored, since step 5 alone left enough margin | Body still exactly 5 pages after restoring it |

Steps 1 and 3 are Tier 1.1 (appendix moves, content relocated not lost); steps 2, 4, and 5 are
Tier 1.2 (tightening, no content lost). Tier 1.3 (a further figure-width reduction) and Tier 1.4
(an actual cut) were never reached.

### 2.2 Why `\parskip`, specifically, and why it's the same category of change already made

`neurips_2026.sty` sets `\parskip` to 5.5pt, applied between every paragraph in the document —
this is template-default spacing, not a load-bearing part of the venue's formatting requirement
(the template compliance G10/G11 verified is about section options, fonts, and the anonymity
macros, not paragraph spacing specifically). `paper/main.tex` already carries a comment from
G12's own page-limit pass explaining that `\textfloatsep`/`\floatsep`/`\intextsep`/caption-skip
values were tightened for exactly this reason — "float separation tightened, not font size or
figure width." This session's `\parskip` change is the same category of change, made explicit in
its own comment rather than silently added to the existing block, and its effect compounds
because it applies once per paragraph break across the whole five pages rather than once per
figure.

### 2.3 The one judgment call (S8)

Moving Table 1 to the appendix is unambiguously safe: it is a preview of content the main text
already states in full, in the same words, in Sections 4 and 5. Moving Figure 1 (the simulator
schematic) is not quite as clean a call, and is flagged here rather than left for a reader to
notice on their own. The figure carries three things: the compartment-flow diagram (S→I→C, the
observation pipeline), the exact distortion-family formulas (e.g. `β → βe^η` for the adversarial
transmission family), and the qualitative description of what the base and adversarial families
do. The third is now restated directly in Section 4's prose, so nothing about following the
paper's argument on a first read requires the figure. The first two are not restated in prose —
they matter for a reader who wants to reproduce the simulator, not for a reader following the
paper's claims. That is a real, if narrow, reduction in main-text self-containedness, and it is
this session's own judgment that it is worth the space it buys, made under the operator's broad
authorization rather than decided as obviously safe. If the operator disagrees on reading the
compiled PDF, the fix is a one-paragraph revert (restore the figure block, revert the `\parskip`
change or find an equivalent amount of space elsewhere) — recorded here so that judgment is easy
to check and easy to undo.

## 3. VERIFICATION — WHAT WAS RE-CHECKED AND HOW

Per Phase 3's instruction, every check below was re-run against the *current* text after this
session's edits, not assumed to have survived from G11/G12 untouched.

1. **All 21 external-review items**, checked one by one against `audit/S11_REPORT.md`'s own
   itemised list. One regression found and fixed in-session: an early tightening pass on the "no
   learned component" Limitations bullet dropped the `(where $s(y)$ would sit)` clause — which is
   specifically what T2-11 required — while shortening the sentence. Caught during this
   re-check, restored before the commit that closed the page limit. Every other item's specific
   textual anchor (the retitled Section 5, the confidence-set-as-primary framing, the K-vs-column
   notation sentence, the two-panel Figure 4 split, the abstract's retained number, and so on)
   was located in the current text and confirmed unchanged.
2. **All four contributions**, read side by side against `audit/FINAL_CLAIMS.md`'s "as it goes in
   the paper" quotes for C1–C4. None of the four claim-bearing paragraphs (the diagnostic
   framing in Method; "Where attribution is identifiable" and "Where it is not" in Section 4;
   Section 5's two non-termination paragraphs) were touched beyond phrasing trims that a diff
   confirms preserved every number and qualifier.
3. **Section 5's confidence-set framing (C5)**, confirmed still primary evidence: the
   Bonferroni-box construction, the 2.3%–16.6% half-widths, the $10^{-5}$ and exactly-zero
   acceptance probabilities, and the "fails at every corner under all four" verdict are
   unchanged, with the original ±5% sweep still cited as secondary context — not regressed to the
   pre-G11 framing.
4. **Anonymization**, re-scanned after each round of edits rather than once at the end. Grepped
   for session/gate/operator/authorship language after every edit round; every match was inside a
   `%`-comment (never rendered in the compiled PDF) or the pre-existing, deliberate operator-facing
   AI-use-disclosure placeholder. `pdfinfo` on the final compiled PDF carries no `Author` field
   and no identifying path in `Creator`/`Producer`.
5. **Number provenance**, confirmed by diff: every numeric token touched by this session's edits
   (2.3%, 16.6%, $10^{-5}$, $9.9\times10^9$, $\kappa=10.9$, $\kappa=10.1$, and so on) appears
   unchanged in the diff — reformatted or relocated, never altered in value.
6. **Two-tier isolation compile**, against a freshly rebuilt package (`build/sim_attrib_overleaf_
   09a107e.zip`, extracted to an isolated temp directory, never against the repo working copy):
   §2b (OVERLEAF-EQUIVALENT — `TEXMFHOME` pointed explicitly at a real package tree, `TEXINPUTS`
   unset) exit 0, 22 pages, zero undefined references or citations, byte-identical 584502-byte
   `main.pdf` against a freshly recompiled repo working copy (differing only in embedded
   timestamp). §2a (`TEXMFHOME` unset) also exit 0, in the same narrower this-machine sense G12
   already established — not genuine isolation, and not treated as such here. **Every page-count
   and compile claim in this report and in `GATES.md` G13 rests on §2b**, per S6's instruction to
   state explicitly which tier is authoritative.
7. **The STRICT-isolation defect** G12 disclosed (§0c of `audit/OVERLEAF_PACKAGE_REPORT.md`) was
   re-examined for whether a quick fix exists. It does not: a genuine fix needs either a second,
   actually-isolated TeX Live installation on this machine or a containerized build environment,
   neither available within this session's scope. Deferred again, restated rather than silently
   re-deferred, per Phase 0.3's instruction.
8. **Full test suite**: 177 passed, unchanged. No `src/` diagnostic code was touched this
   session — every edit was confined to `paper/main.tex`, `paper/checklist.tex`, and this
   session's own audit documents.

## 4. WHAT WAS CUT — THE COMPLETE LIST, PER S8

For a page-limit session, the honest record is what left the paper, however small. The complete
list:

- **Nothing was cut from the paper's evidentiary content.** No citation, no claim sentence, no
  number, no Limitations caveat was removed.
- **Two pieces of content were relocated** (Table 1, Figure 1's schematic) — not cut, moved to
  the unlimited appendix, with Figure 1's qualitative content restated in the main text (§2.3
  above names the resulting, narrow reduction in main-text self-containedness as the one
  judgment call).
- **One discussion sentence was cut, trialled, and restored** — see §1 above. Net: not cut.
- **Prose was reworded** in Section 5 (two paragraphs) and two Limitations bullets, shortened
  without dropping a clause of substance, each verified against the pre-edit text by diff.

## 5. PROCESS CAVEATS — WHAT THIS SESSION DID BADLY OR NOT AT ALL

- **The tiered-commit structure the session brief asked for (Phase 2.6: a separate commit per
  tier) was not achieved.** An attempt to split the diff into an "appendix moves" commit and a
  "tightening pass" commit via `git add -p` produced hunk-selection behavior this session judged
  too easy to get wrong blind (the interactive tool's own hunk count and numbering shifted
  between invocations in a way that was hard to track reliably through the available tool
  interface). Rather than risk staging a broken intermediate file state, the index was reset and
  the whole page-limit pass was committed as one commit, with every tier named explicitly in the
  commit message body instead. This follows the same precedent G9, G11, and G12 each already set
  for their own page-limit passes (each bundled theirs into one commit too), but it is still a
  real departure from what this session's own brief asked for, and is recorded as such rather
  than silently substituted.
- **The T2-11 regression (§3.1) should not have happened.** It was caught by this session's own
  verification pass, not prevented at the point of the edit. A less thorough Phase 3 would have
  shipped a genuine, narrow regression of a specific external-review fix. This is the clearest
  argument in this session's own experience for why Phase 3's per-item re-check belongs in the
  gate criteria rather than being treated as a formality once "the page count looks right."
- **The `.bib` `month=June` defect (§1) is disclosed but not fixed**, for the reason given there.
  A future session with a broader mandate than page-limit closure could reasonably decide to
  patch around it.
- **No second external review has been commissioned or run.** Not this session's task, but it is
  now the single largest remaining gap in this project's own trajectory — every content fix from
  the original review is applied, and the page limit that review's T1-2 finding named is closed.
- **Google Scholar still not searched.** Thirteenth session with code. O-7, unchanged since G0.

## 6. WHAT SHOULD HAPPEN NEXT

1. **P-1 (operator).** Read the recompiled PDF directly, not just this report — content was
   actually moved and reworded this session, and only a direct read confirms nothing important
   reads badly or is missing. Pay particular attention to Section 4's rewritten opening paragraph
   and the appendix's new Table 1 / simulator-figure placement, since those are this session's
   most consequential edits.
2. **P-2 (operator, once satisfied).** Authorize the second external Fable 5 review — everything
   the first review's Tier-1 and Tier-2 findings named is now applied, and the page limit that
   review's T1-2 finding raised is closed, for the first time giving this project a paper that
   could plausibly be re-reviewed against a clean slate.
3. **P-3 (carried, unchanged).** Q-3 (reciprocal reviewer), Paris in-person attendance, repository
   visibility switch, OpenReview submission — all still the operator's.

## 7. THE ONE-PARAGRAPH VERSION

Six pages against a five-page limit, narrowed by three prior sessions but never closed, is closed
this session at exactly five pages, verified by reading the compiled PDF directly. Two safe
levers — moving a convenience table and (with one disclosed judgment call) a structural figure
to the unlimited appendix, plus a whitespace/prose tightening pass including the template's own
paragraph spacing — were sufficient in combination, something no prior session had tried
together; no citation, claim sentence, or evidentiary number was cut, and a trial content cut was
found unnecessary and restored. Two real cross-reference defects this session's own edits
introduced were caught and fixed before the final commit; a third, unrelated, pre-existing
bibliography defect was found and disclosed rather than fixed, consistent with this project's own
"`.bib` stays exactly as fetched" policy. All 21 external-review findings, all four contributions,
and Section 5's strengthened confidence-set framing were individually re-verified against the
current text, with one narrow external-review regression caught and fixed in the same pass that
found it. Status: ready for review, unsigned, not submitted, repository visibility unchanged.
