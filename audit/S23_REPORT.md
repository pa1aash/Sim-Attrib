# S23 — Session G23 report: three stale references fixed, a document-wide audit run, and the final readiness answer

**Prepared 2026-08-29.** This is the twenty-third and explicitly final internal session, closing
the four-session operator line-edit (G20-G23). This document is not a narrow session report — it
is the top-level answer to the question the operator actually needs before acting on the
remaining pure-logistics items: **is this paper ready to submit, given everything found and fixed
across twenty-three sessions and four independent review rounds.**

## The direct answer

**Yes — the document itself is ready.** Every finding raised by three external Fable 5 reviews,
one internal tone/readability pass, and every session's own re-verification (G11 through G23) is
either fixed and confirmed intact, or disclosed with an explicit, unchanged reason it was not
fixed. This session found and fixed the three stale cross-references the operator located by
reading the G22 PDF directly, ran the document-wide cross-reference audit no prior session's scope
covered, found and fixed one further stale reference that audit surfaced, and re-verified the
entire document from a clean compile through both submission packages. Nothing outstanding is a
document defect. What remains is a short list of actions only the operator can take — reading and
signing the PDF, writing the AI-use disclosure, and the logistics of visibility and submission —
none of which this or any prior session was positioned to do.

## What this session did

**Phase 1 — the three named fixes.** Section 4's Montel-comparison sentence pointed at Appendix
A.5 for a simplification the appendix no longer discusses (moved to `CLAIMS.md` by G20); the
pointer was deleted and the sentence verified complete on its own. Checklist items 4 and 8 both
pointed at an appendix section — "Every number this paper's claims rest on" and "the generated
claim table" — that G20 renamed and emptied into a one-paragraph pointer; both justifications were
rewritten to describe the paper's actual current state (numeric claims trace to a dotted path; the
full table ships as `CLAIMS.md` in the anonymized package, cross-referenced via checklist item 5
rather than duplicated). Item 8's three cited draw counts — 7.6 million, 9,216, 722,000 — were
independently checked against `results/boundary_sweep.yaml`, `results/robustness/k6_spectrum.yaml`,
and `results/confidence_set_mmc.yaml` directly rather than trusted because only the pointer was
moving, and all three are exact.

**Phase 2 — the audit no prior session ran.** Every internal cross-reference in the compiled
document was enumerated, not sampled: 39 `\ref` usages, 20 `\label` definitions, 9 hardcoded
`Section N` mentions, all 16 checklist items' location claims. Each was checked two ways —
does it resolve at all (zero undefined references, every compile this session), and does the
location it resolves to actually hold what the sentence claims is there, the specific way FIX-1/2/3
failed and a resolve-only check cannot catch. One further stale reference surfaced: the appendix's
summary table cited "Figure 3a" for a sub-panel label Figure 3's own caption never defines (it
uses "Left:"/"Right:", not lettered panels). Fixed to "3, left." Full findings, including the
complete 39-row reference table:
[`audit/G23_CROSSREF_AUDIT.md`](G23_CROSSREF_AUDIT.md).

**Phase 3 — final comprehensive verification.** Zero numeric-token drift anywhere in the compiled
document (a full sorted-token diff against the pre-session commit is empty for `main.tex`;
`checklist.tex` gained exactly the two "item 5" cross-reference numbers FIX-2/3 added, nothing
else). Anonymization clean at submission scope (paper files + compiled PDF, zero hits, empty
`/Author` metadata) and clean at AI-attribution scope (repo-wide, zero hits). Main text confirmed
at exactly 5 pages; references page 6; appendix page 7. Two-tier isolation compile: both tiers
exit 0, 17 pages, zero undefined references, byte-identical `pdftotext` output across both
isolated extractions and the working copy. Both submission packages (Overleaf, anonymized
reproducibility) rebuilt clean against the final commit. Checklist swept for placeholders: exactly
one remains (item 16, the operator's own, untouched by standing instruction).

**One nuance surfaced this session, not previously examined:** the repo-wide personal-identity
grep's "many hits, expected, not a regression" finding (established at G19) covers the *private
development repository*. This session additionally checked the *anonymized package's own source
files* — the ones that actually ship to reviewers via checklist item 5's OSF link — and found the
bare project codename `sim-attrib` (not the author's name) in a handful of places: a module
docstring, an SVG hash-salt string, a PDF-metadata field, and four tempfile lock-directory names.
This does not name the author directly, but a reviewer who searched the codename could reach the
still-public GitHub repository, which does carry the operator's real identity throughout. This is
exactly the exposure the already-pending **P-5 (switch repository visibility to private)** exists
to close — not a new action item, but a second, more concrete reason P-5 matters before
submission. Not fixed directly this session: renaming the project's own codename across roughly
90 source files is a scope decision beyond this session's cross-reference-accuracy mandate.

## The full project history, condensed

Three external Fable 5 reviews (Weak Reject; "Path to Acceptance"; a third round with two
significant findings and nine smaller ones) and one internal tone/readability pass produced every
substantive finding this paper has addressed. `GATES.md`'s Phase 2.6 register (Tables A-I,
compiled at G19) itemizes all of them — every tier-1 and tier-2 item from Review #1, every item
from Review #2's two rounds, every item from Review #3, every internal-voice fix from G17/G18, and
every defect each session's own re-verification found along the way — with a final status and the
session that fixed or disclosed it. This session's own read of that register found nothing
regressed. Three structural/voice sessions followed the review-response work (documented in the
same file, extended this session as Tables J-L): **G20** relocated the appendix's bloated
dotted-path ledger to an external `CLAIMS.md`, reordered Section 5, and added a Conclusion — at
the cost of a disclosed, deferred 6-page overage. **G21** closed that overage as a side effect of
a dense voice-only pass eliminating rhetorical negation, announcement sentences, and run-ons
across the whole document. **G22** compressed captions, unified terminology and numeric precision,
fixed one genuine correctness issue (the four `p≈0.004` Montel values are a measurement-resolution
floor, not four independent near-agreements, and the paper now says so), and standardized spelling.
**G23** (this session, Table M) is the fourth and final planned pass: three named stale references
plus one more the new audit found, all fixed; the whole document re-verified clean.

Two items have stood disclosed and unresolved, unchanged, across every session since they were
first found, because no session has had the means to close them: the STRICT-isolation TeX tier
(§2a) tests genuine self-containment only in a narrower this-machine-fallback sense, pending a
second isolated TeX Live install this machine does not have; and one BibTeX `month=June` warning
on the Raue et al. 2009 entry, standing behind the project's own "`.bib` stays exactly as fetched"
policy. Neither affects the tier the project actually gates on, and neither is a claim, number, or
anonymization defect — both are named again here so "ready to submit" is not read as "zero open
items of any kind."

## What remains — pure logistics, not document work

Everything left is listed in full in `GATES.md`'s G23 section (P-1 through P-6). In short: the
operator needs to read the final PDF and sign G20 through G23 together (the operator's own
standing decision to hold all four pending this session); write the AI-use disclosure at checklist
item 16, the one placeholder no session has touched by design since G9; confirm the OSF-hosted
anonymized package matches this session's final tree, since `CLAIMS.md` was added at G20; switch
repository visibility to private, which also closes this session's G23-7 finding; and handle the
purely administrative items — reciprocal reviewer nomination, Paris attendance, and the OpenReview
submission itself, due 29 August 2026 AoE.

## What this session does not certify

That the operator has personally read the recompiled PDF; that P-5 has been actioned (this
session surfaces why it matters more than previously stated, it does not close it); and that every
conceivable prose-quality judgment call has been re-litigated a fifth time — that ground belonged
to G17, G18, G21, and G22, and this session's mandate was reference accuracy and mechanical
re-verification, not a further voice pass.

**Status: `GATES.md` G23 is `ready for review — UNSIGNED`, alongside the still-unsigned G20, G21,
and G22 by the operator's own standing decision.** This session's own checking found no reason
that decision should change.
