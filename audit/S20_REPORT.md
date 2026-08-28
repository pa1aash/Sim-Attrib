# S20 — Session G20 report: a large structural line-edit, and one disclosed shortfall

**Prepared 2026-08-29.** This is the twentieth internal session, the first of a planned four
(G20-G23) covering a detailed operator line-edit. G20's own mandate was explicitly narrow:
**structural changes only** — where content lives, not how individual sentences read. Full detail
in `GATES.md` G20; this is the top-level summary.

## The direct answer

**Every phase in the operator's brief ran to completion, and the structure it produced is sound
— except that main text now compiles to 6 pages, not 5.** That overage is disclosed, not hidden
or rounded away, and it was not this session's to fix: the operator was asked mid-session whether
to close the gap by touching pre-existing Limitations prose (bending this session's own "structure
only" boundary) or to defer it to G21's already-planned prose-tightening pass, and chose to defer.
**G21 must treat re-closing the page count as its first task**, before any general prose work,
not as an incidental side effect of tightening sentences elsewhere.

## What this session actually did

**Phase 1 — Table 1 (A.1) placement.** Kept in the appendix; the Section 1 pointer was shrunk to
one clause rather than the table being moved into Section 1, since by the time this decision was
reached (deliberately last, per the operator's own instruction) main text had no spare room.

**Phase 2 — Table 2/Table 3 (A.4).** Table 2 (`tab:sb-eight`) untouched. Table 3 (`tab:sa-eight`,
the $S_A$ control table) dropped entirely — it near-duplicated Figure 1's right panel, and the one
column that didn't (the named equivalence class per failing assignment) is now one clause in
Section 4's prose. Table 3's full numbers survive in the new `CLAIMS.md`, not lost.

**Phase 3 — the A.5 surgical cut, the largest change this session:**
- Promoted the no-CRN negative control's actual numbers into Section 3 (previously referenced
  with no numbers at all); the $S_C$ positive control was already stated in main text before this
  session.
- Promoted a new eight-row threshold table into Appendix A.2 (moved there from Section 3 after
  the first placement measurably cost too much main-text space).
- Promoted a new five-column confidence-box table (relative half-widths and the MLE point) into
  Section 5, next to Figure 3.
- Cut everything else that was in A.5 — the former C2/C3/C4/C5/L1/B1 dotted-path tables, roughly
  seven pages of paths — down to one paragraph, renamed the subsection "Claim-to-source table,"
  and moved the full ledger (every row, nothing dropped) into a new
  `scripts/anonymous_package/CLAIMS.md`, which now ships inside the anonymized reproducibility
  package. `paper/appendix_claims_table.tex` was removed. **`scripts/build_overleaf_package.sh`
  still had that file hardcoded in its allowlist** — found only by actually running the rebuild,
  fixed before the Overleaf package was rebuilt.

**Phase 4 — the misplaced result.** The Anau Montel et al. baseline comparison, a full
experimental result, was sitting inside "Background and related work" as a citation aside. Moved
to a new paragraph at the end of Section 4, with one forward-pointing sentence left in Section 2.

**Phase 5 — Section 5 reorder.** The boundary sweep now precedes the data-implied confidence box,
per the operator's requested order. The forward reference and the backward-repair sentence the
operator predicted would become unnecessary were both removed; a stray "above"/"below" was
corrected after the swap. Every number and cross-reference in the section re-checked after
reordering.

**Phase 6 — triple redundancy.** The introduction's second paragraph no longer restates the
abstract's four findings; it explains why this simulator and what a practitioner gets from
running the screen instead. Section 5's opening paragraph was checked and found not to be doing
full-restatement duty either (it only frames findings 3-4), so it needed no further cut.

**Phase 7 — Conclusion.** A new two-sentence Conclusion section states the paper's practical
recommendation as an instruction for the first time and closes on the contribution, in plain
declarative sentences.

## The page-budget shortfall, and why it wasn't fixed in-session

Baseline main text (post-G19) was exactly 5 pages with no slack. This session's mandatory
additions (the confidence-box table, the Conclusion, the equivalence-class clause, the
negative-control numbers) outweighed what Phase 3.2's appendix move and Phase 4's relocation gave
back. Every whitespace lever this project has used since G12 (`\parskip`, `\floatsep`,
`\textfloatsep`, `\abovecaptionskip`) was confirmed still at the floor prior sessions already
tightened it to. A page-break-specific `\enlargethispage` was calibrated by rendering the page to
an image and reading it directly — `pdftotext` alone was not trusted, and correctly so: two tested
values looked clean in extracted text while visibly overlapping the page-footer number when
rendered. The paper now ships at the largest value confirmed clean by rendering
(`\enlargethispage{2\baselineskip}`). Every sentence and table this session added was then
compressed as far as it would go without dropping a requirement. What remains — roughly the back
half of Limitations bullet 2, all of bullet 3, and the Conclusion — cannot close without touching
pre-existing Limitations prose, which is explicitly out of this session's scope and squarely
G21's. Asked directly, the operator chose to defer rather than have this session bend its own
boundary.

## Re-verification

- **Number trace:** every promoted value (negative control, all eight threshold-table entries,
  all five confidence-box half-widths and the MLE point, all four equivalence-class labels)
  checked directly against the rendered PDF text and the underlying `results/*.yaml` files, not
  against memory of the old A.5 prose.
- **Anonymization re-scan:** clean across the compiled PDF's text and metadata and every file
  this session touched. The one grep hit, in `scripts/build_anonymous_package.sh`, is that
  script's own obfuscated name-pattern definition matching itself — the exact behavior its own
  comment explains, not a leak.
- **Two-tier isolation compile:** both tiers pass against a freshly rebuilt
  `build/sim_attrib_overleaf_380b694.zip`, extracted to two separate isolated temp directories —
  exit 0, 17 pages, zero undefined references or citations, `pdftotext` output byte-identical
  across the repo working copy and both isolated extractions (583,882-byte `main.pdf` in all
  three).
- **Package rebuilds:** the anonymized reproducibility package was rebuilt with `CLAIMS.md`
  confirmed present (92-row ledger, 21,111 bytes); the Overleaf package was rebuilt after fixing
  its stale allowlist entry.

## Honesty about what this session did not do

This session did not touch any sentence outside the specific insertions Phases 2, 3.1, 4, 6, and
7 required, and did not review prose quality anywhere else in the document — that is explicitly
G21/G22's job on the structure this session produced. It did not close the page-budget gap it
created, by the operator's own choice, made mid-session rather than assumed. Every other
deliverable in this session's brief — five structural phases, a full re-verification pass, both
package rebuilds — is complete as of this session's own checking.

**Status: `GATES.md` G20 is `ready for review — UNSIGNED`.** Points requiring operator input,
including the carried-over G19 items and the new page-budget disposition, are collected in
`GATES.md`, not resolved by this session.
