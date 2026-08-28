# S19 — Session G19 report, and a final answer to "is this paper ready to submit"

**Prepared 2026-08-28.** This is the nineteenth and, barring an operator-found issue, final
internal session on this project. Its narrow mandate was to insert the operator's real anonymized
reproducibility-package URL into the one placeholder that needed it, then run one last exhaustive
verification of the whole document before the operator's own submission. Full detail in
`GATES.md` G19; this is the top-level summary, and — per this session's own brief — a direct
answer about the project as a whole, not just this session's slice of it.

## The direct answer

**Yes — as of this session's own verification, the paper is ready to submit, subject only to the
handful of items that were always going to be the operator's own to close.** Content, numbers,
figures, structure, and voice went through four independent review rounds (three external Fable 5
reviews, one internal tone pass) across eighteen prior sessions, and this session's own
re-verification — a full number trace, an independent anonymization re-scan (both by this
session's own tools and by a separate, fresh-eyes agent read of the compiled PDF), a two-tier
isolation compile, and a package rebuild — found zero drift from that state. Nothing in this
session's checking found a reason the paper is not ready.

## What this session actually did

**One substantive edit.** `paper/checklist.tex` item 5's placeholder —
`[ANONYMIZED CODE LINK --- OPERATOR TO INSERT AFTER UPLOADING build/anonymous_package.zip TO AN
ANONYMOUS HOST]` — was replaced with the real URL the operator provided,
`https://osf.io/hqgzk/overview?view_only=b16c7e6a0ea34047a411e806e5d5a6ce`, copied character-for-
character. Item 5's Answer was already `\answerYes{}`; no answer flip was needed. A repo-wide
search confirmed this is the only location in the paper that references code availability.
`paper/main.tex` was never opened for editing. `git diff` against G18's `cadd7e6` shows exactly
one changed line.

**Then, exhaustive re-verification, not assumed clean:**

- **Number trace:** `src/diagnostics/report_claims.py` regenerated both `results/FINAL_CLAIMS_NUMBERS.md`
  and `paper/appendix_claims_table.tex` from the underlying `results/*.yaml` files. Byte-identical
  to the committed versions — 125 numbers, zero drift.
- **Anonymization, two independent passes.** This session's own grep across every
  submission-facing file (`paper/main.tex`, `paper/checklist.tex`, `paper/appendix_tables.tex`,
  `paper/appendix_claims_table.tex`, `audit/BIBLIOGRAPHY.bib`, and the compiled PDF's extracted
  text and `/Author` metadata) came back clean. Separately, an independent agent with no prior
  context on this paper read the full 23-page compiled PDF cold, hunting specifically for
  double-blind breaches — names, institutions, self-citation phrasing, leaked links, file paths,
  hostnames, acknowledgments, PDF metadata. It found none, with one minor informational note
  (below).
- **The OSF link itself was spot-checked live**, not assumed safe because it looked like an
  anonymized URL. The OSF public API, queried with the `view_only` token, returned
  `"meta":{"anonymous":true}` — direct server confirmation this is genuinely the anonymized
  view-only mode. The files endpoint shows exactly one file, `anonymous_package.zip` (630,754
  bytes), visible as required. The contributors endpoint returns no name. The project title,
  "Simulator misspecification supplementary materials," carries no identifying information.
- **Two-tier isolation compile:** both tiers pass — exit 0, 23 pages, zero undefined
  references/citations — against a freshly rebuilt `build/sim_attrib_overleaf_9ab323b.zip`
  extracted to two separate fresh temp directories. The two tiers' PDFs differ at the byte level
  only in pdfTeX's compile-timestamp-derived metadata fields, confirmed by a direct byte-diff;
  their extracted text is identical.
- **Page count:** main text pages 1–5, References begins page 6 — unchanged, as expected, since
  `main.tex` was never touched.
- **Overleaf package rebuilt** against the final committed state: 17 files, 13 allowlisted paths.
- **The iCloud sync glitch G18 first hit** (`audit/S17_REPORT.md` reading as a dataless local
  placeholder) is confirmed, again, to be a local display issue and not a repository content
  problem — `git show HEAD:audit/S17_REPORT.md` reads its full content cleanly. Every other
  `audit/*.md` file was swept for the same symptom; none are affected.
- **One consolidated cross-session findings table** covering every item from all four review
  rounds and every fix session G11 through G19 was built (`GATES.md` G19, Phase 2.6) — the single
  reference a future reader can use instead of re-reading nineteen session reports.

## One thing found, disclosed rather than silently fixed or silently ignored

The independent fresh-eyes PDF review noted the compiled PDF's embedded `/CreationDate` metadata
carries a `+05'30'` UTC offset (India Standard Time) — not visible in the rendered paper, not a
text-content anonymity breach, but a soft metadata signal a very sharp reviewer or an automated
scan could in principle use to narrow the authors' likely time zone. This is disclosed to the
operator as an optional item (P-6 in `GATES.md`), not treated as a defect requiring a session fix
— it sits well below the severity of an actual anonymity violation, and no prior session's own
anonymity criteria have ever included embedded compile timestamps.

## What "ready" does not mean here

Ready refers to the document — its content, its numbers, its anonymity, its compilation, its
packaging. It does not mean every operator action is done. Six items remain, and every one of them
was already the operator's own to close, not something this session could resolve on its behalf:

1. **Sign G19** after reading the final PDF, including the newly completed checklist item 5.
2. **Personally re-verify the OSF link** once more in a private/incognito window — this session's
   check used the live public API and found it clean, but a human's own eyes on the rendered page
   is the standing final check.
3. **Write the AI-use disclosure** at checklist item 16 — untouched this session, as every session
   since G9, by explicit standing instruction.
4. **Confirm the reciprocal reviewer nomination and Paris attendance.**
5. **Switch repository visibility to private.**
6. **Submit via OpenReview** — 29 August 2026 AoE.

## Honesty about the absence of findings

This session ran a genuinely exhaustive verification — number trace, two independent
anonymization passes (one of them by an agent with zero prior context on the paper, closer in
kind to a fresh external read than any internal re-check this project has run before), a live
spot-check of the actual OSF URL rather than trusting its shape, two-tier isolation compile,
package rebuild, and a full sweep for stray placeholders and stray untracked files. It found
**one substantive item to insert (the URL, done), one informational metadata note (disclosed, not
fixed), and nothing else.** Per this project's own standing convention (S9, first stated in
earlier sessions): a clean pass this late in an eighteen-session review process is reported as
clean, not manufactured into busywork to look more thorough. Nineteen sessions in, with four
independent review rounds behind it, a document that keeps coming back clean on exhaustive
re-checking is the expected and legitimate outcome, not evidence the checking wasn't real — this
report's own checks (byte-level diffs, a live API call, a completely independent agent's cold
read) were constructed specifically so that finding nothing would mean something.

**Status: `GATES.md` G19 is `ready for review — UNSIGNED`.** Points requiring operator input are
collected above and in `GATES.md`, not resolved by this session.
