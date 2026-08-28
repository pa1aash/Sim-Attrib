# S21 — Session G21 report: a dense voice-only line-edit, and the page-budget gap closed as a side effect

**Prepared 2026-08-29.** This is the twenty-first internal session, second of the four planned
(G20-G23) covering a detailed operator line-edit. G21's mandate was explicitly **voice only** —
eliminate the "not X, rather Y" rhetorical-negation pattern, announcement sentences, softening
adverbs, trailing appositive qualifications, run-on sentences, and aphoristic paragraph endings,
across the entire document. Full detail in `GATES.md` G21; this is the top-level summary.

## The direct answer

**Every phase in the operator's brief ran to completion, no claim or number changed, and G20's
disclosed page-budget shortfall is closed — as a side effect of this session's cuts, not as a
separately tracked task.** Main text now compiles to exactly 5 pages (Introduction through
Conclusion); references begin page 6 and the appendix begins page 7. G20's `S20_REPORT.md`
flagged closing this gap as G21's first job before any general prose work; it closed on its own
once the announcement-sentence cuts (Phase 2) and the Section 5 opening-paragraph reduction were
in place, without touching `\enlargethispage` or any other whitespace lever.

## What this session actually did

**Phase 1 — rhetorical negation.** 16 instances of the "not X, rather Y" / "X, not Y" pattern
fixed, 3 kept deliberately per the brief's own instruction (two legitimate technical contrasts,
one genuine estimator/matrix distinction). The worst instance — three consecutive "not X"
rule-outs in Section 4 before naming the actual cause — was inverted to state the cause first (a
confound between progression and observation) and then rule out the three alternatives in one
sentence, every numeric justification kept. Full instance-by-instance accounting in `GATES.md`.

**Phase 2 — announcement sentences.** All 7 addressed: 4 cut outright (each pure duplication of a
caption, an appendix paragraph, or an adjacent sentence), 1 rewritten with substance, and
Section 5's opening paragraph reduced to its non-redundant core — the conservativeness/
reachability sentence (which does not restate anywhere else in the paper) survives; the three
sentences restating claims the bold-led paragraphs below already state do not.

**Phase 3 — softening adverbs.** Every located instance fixed: "real" cut from all three
surviving hedge-against-artifact occurrences, "essentially always" rewritten to a plain
declarative, and nine further individual adverb/intensifier cuts ("usually," "actually,"
"exactly" ×2, "partly," "comfortably" ×2, "almost exactly," "directly"). One item from the
brief ("it survives, by a wide margin") was searched for directly and confirmed absent from the
current draft — not fixed because there was nothing left to fix.

**Phase 4 — trailing appositives.** 6 of 9 fixed directly (abstract precondition promoted to its
own sentence, two citation appositives integrated, a dangling modifier corrected to name what is
actually derived from the compute budget, an exclusion parenthetical unnested). 3 were moot,
confirmed by direct search rather than assumed: two were already resolved by G20's own Section 5
reorder or Phase 2.5's cut, and one (a Figure 4 caption clause) is deferred to G22 per the
brief's own routing of caption work to that session.

**Phase 5 — run-ons.** All 3 flagged sentences split: the five-clause boundary-collapse sentence
into four sentences (shape verdict, rate, fit quality, passing region); the confidence-set-
scaling sentence split with its exclusion parenthetical unnested into its own sentence; the
four-check sentence split into two with the duplicated "pre-registered" removed. The Section 4→5
forward reference this item also asked to verify was checked directly: it is a genuine,
intentional forward pointer (Section 5 necessarily follows Section 4), and G20's Phase 3.3
already promoted the referenced computation to sit early in Section 5 — nothing further needed.

**Phase 6 — aphoristic endings.** All six addressed; exactly one survives, the abstract's "the
contribution is the finding," per the operator's explicit instruction that it earns its place
there. The internal contradiction the brief flagged — "a portable one-line check for other
simulators" claimed as established fact while Limitations says transport is untested — is fixed
as a substance issue: the claim now reads as an explicit conjecture, not a stated fact.

**Phase 7 — two flagged inconsistencies.** Both resolved: "its only theorem requires" → "the
validity argument requires" (removes the contradiction with checklist item 3's "no theoretical
result" statement); the ungrammatical comparative in the Mahalanobis-radius sentence rewritten as
two parallel clauses. The third item (7.3, a wrong-subject "the collapse... survives" sentence)
was searched for directly and confirmed moot — G20's Section 5 reorder had already removed it
along with the forward reference it was tied to, exactly as the brief predicted it might.

**Phase 8 — full re-read.** A second complete pass located no further instances of any of the
five pattern classes beyond what Phases 1-7 already addressed. Two brief items were searched for
directly and confirmed absent from the current draft rather than assumed resolved: item 1.1's
literal quoted text, and "it survives, by a wide margin." Both read as the operator's notes on
passages G20's structural pass had already reshaped before this session started; 1.1's substance
is fully covered by this session's rewrite of the same passage under Phase 1.11.

## The page-budget closure

G20's `S20_REPORT.md` disclosed a 6-page main text and asked G21 to close it as its first task.
It closed without a dedicated pass: Phase 2's four outright cuts (the Section 1 Table 1 pointer,
the Section 2 "Section 4 measures rather than assumes" clause pairing, the Section 4 "every
number traces" sentence, the Appendix A.3 preamble paragraph) and Phase 2.5's reduction of
Section 5's opening paragraph removed enough duplicated prose that main text now compiles to
exactly 5 pages with no `\enlargethispage` value changed and no whitespace lever retightened.
This was verified by rendering, not assumed: `pdftotext -f/-l` page-boundary extraction confirms
references begin page 6 and the appendix begins page 7.

## Re-verification

- **Number trace:** every numeric token in `paper/main.tex` diffed pre- vs. post-session via
  regex extraction (decimals, percentages, `\command=value` tokens), sorted and compared. One
  difference found, resolved to a cosmetic LaTeX-markup change with no value change, and
  corrected to match the document's existing notational style. Cross-checked against the full
  unified diff line-by-line: every numeral in a removed line is present, unchanged, in the
  corresponding added line.
- **Anonymization re-scan:** clean across the recompiled PDF's text and metadata, and clean per
  `scripts/build_anonymous_package.sh`'s own built-in scan.
- **Two-tier isolation compile:** `build/sim_attrib_overleaf_5d18d7c.zip`, rebuilt from the
  working tree with this session's edits, extracted to two independent temp directories and
  compiled end to end — both exit 0, both 17 total pages, zero undefined references or citations
  in a clean final pass on each, `pdftotext` output byte-identical (MD5
  `b6ff61c4eb187b83d2a3e74789c56fa6`) across the repo working copy and both isolated extractions,
  582,225-byte `main.pdf` in all three.
- **Package rebuilds:** both the Overleaf package and the anonymized reproducibility package
  rebuilt against the final edited tree; `CLAIMS.md` confirmed present and unchanged (this
  session touched no claim data, only prose around it).

## Honesty about what this session did not do

This session did not touch captions — the two items flagged for G22 (Figure 2's mirrored
"property of the matrix, not of the estimator" aphorism, and Figure 4's "a stated design
limitation" trailing clause) are named, not fixed, per the operator's own routing of caption work
to that session. It did not rewrite sentences outside the five flagged pattern classes; this was
a targeted pass plus one full re-read against those five classes, not a from-scratch rewrite. The
5-page main text carries no slack — the same zero-slack margin G20 inherited from G19 — so any
future session adding content must re-verify page count as its own first check.

One environment note, not a paper defect: `audit/S17_REPORT.md` — already modified before this
session started, per the initial `git status` — is a macOS iCloud dataless placeholder, and
whole-repository `git status`/`git diff` intermittently time out on it. Scoped git operations
were used throughout this session's own verification and are unaffected.

**Status: `GATES.md` G21 is `ready for review — UNSIGNED`.** Points requiring operator input,
including the carried-over G19/G20 items and the request to sign G20 and G21 together after
reading the recompiled PDF, are collected in `GATES.md`, not resolved by this session.
