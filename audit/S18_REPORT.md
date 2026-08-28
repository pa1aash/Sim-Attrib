# S18 — Session G18 report

**Prepared 2026-08-28.** This session's mandate was a pure tone-and-readability cold read of
`paper/main.tex` and `paper/checklist.tex`, adopting the stance of the harshest reviewer on a
NeurIPS workshop committee but restricted entirely to prose quality — not correctness, not
evidence, not claims, all of which are settled by three independent external reviews and the
operator's own verified recompile. Full detail in `GATES.md` G18; this is the summary to start
from.

## Headline numbers

**Five findings from Phase 1's cold read. All five fixed in Phase 2. Zero flagged as substance
questions for the operator** (no fix in this session came close to S3's boundary — every one is
a wording, ordering, or punctuation change, verified against the rendered PDF, not assumed).
**Final page count: main text pages 1–5, References begins page 6, unchanged from the state this
session started in.** Two-tier isolation compile passes both tiers at 23 pages, 602,400 bytes,
zero undefined references or citations.

**In this session's own honest judgment: yes, this reads as a finished paper.** The cold read
found a real, if narrow, set of things worth fixing — not a paper in need of substantial rework.
Three of the six things the brief specifically asked to check (mechanical listing in Method and
Experiments, confidence versus evidence, and the register comparison to Cranmer/Talts) came back
clean on the first read, which per S9 is reported as found rather than dressed up into
manufactured edits. The paper's remaining open item is not something this session can close: no
fully independent reader has looked at this version for tone, and G17's own gate already said so
about its version. That recommendation stands, unchanged, after this session.

## What Phase 1 found, and what Phase 2 did about it

**The abstract and introduction restated the same finding almost word-for-word.** The
introduction's third sentence carried "…is affordable at a known parameter but fails to
terminate once the nuisance parameters are known only to the precision a maximum-likelihood fit
gives them" — nearly identical to the abstract's own phrasing of the same finding, roughly
fifteen lines earlier. This was the session's single most consequential finding: a cold reader
reads the introduction immediately after the abstract, and a verbatim clause repeated that close
together reads as padding no matter how confident the voice. Fixed by rewording the sentence to
carry the identical claim without echoing the abstract's exact words.

**The introduction's closing sentence undercut its own strong ending.** "…the prediction holds
(Table~1, Appendix~A, pairs each finding with its evidence figure)" trails a genuinely strong
beat ("the prediction holds") into a comma-spliced, administrative fragment. Split into two
sentences: the paragraph now ends on "the prediction holds," with the table pointer as its own
properly formed sentence immediately after.

**Section 4 opened with a provenance disclaimer instead of its actual substance.** "Every number
below traces to a results file and an exact dotted path…" led the section; the real opening
sentence — "We apply the diagnostic to a $K=3$ compartmental epidemic simulator…" — sat one
sentence behind it. Reordered so the substantive sentence leads, matching every other section's
opening in the paper.

**The abstract's fourth sentence had a dangling appositive.** "…gives them, a box wider, on every
coordinate, than one already shown to break it" makes a reader work to figure out that "a box"
describes the confidence region implied by that precision, not the noun it sits directly after.
Fixed with a single punctuation change, comma to colon, which makes the appositive relationship
explicit without changing a word.

**A sentence fragment in the appendix's claims-ledger introduction was missing its verb.**
"Every number the main text's four contributions … rest on, generated programmatically …" has no
main verb connecting subject to predicate. Fixed by inserting "is."

**Two transition points were checked and deliberately left alone.** Related Work into Method, and
the negative-result section into Limitations, both open directly on a bolded sub-heading with no
lead-in sentence. Checked against the brief's explicit ask (1.4) and judged acceptable — this is
common practice at this venue for a Method or Limitations section, and a manufactured bridge
sentence would add words without adding anything a reader needs. Not fixed, per S9, rather than
invented to make Phase 2 look busier.

## No claim changed. This is measured, not asserted.

Same standard G17 set, re-run rather than trusted:

- **Numeric literals.** A `pdftotext -layout` diff between the pre-edit and post-edit compiled
  PDF shows exactly four paragraph-local hunks — the four locations F1–F5 touch — and nothing
  else. A separate token-level count of every numeric literal in the rendered text returns 1,606
  before and 1,606 after.
- **Citations.** 20 occurrences, 19 distinct keys, identical to G17's own measured baseline.
  Section 2, where every citation lives, was not touched this session.
- **The appendix claims ledger.** `src/diagnostics/report_claims.py` was re-run against the
  underlying `results/*.yaml` files and regenerated both `results/FINAL_CLAIMS_NUMBERS.md` and
  `paper/appendix_claims_table.tex`. Both came back byte-identical to the committed versions —
  125 numbers, zero drift, confirmed by full regeneration rather than by spot-checking a sample.
- **Protected clauses.** T2-7 (the scope restriction inside the introduction's own contribution
  sentence) and T2-10 (the abstract's `κ=628.9`, rank 4 of 6) both sit immediately adjacent to
  sentences this session edited; both individually re-checked by grep and confirmed present
  verbatim.

## One disclosed judgment call

G17's own gate documented the introduction as four sentences in a deliberate voice pattern — "We
find that…", "Separability then fails…", "We find that…", "And we predict…". This session's fix
to the third of those four (F2, above) rewords it away from "We find that" because the verbatim
overlap with the abstract was judged the more consequential problem for a cold read. Three of
G17's four voice markers are untouched and still present verbatim; the fourth carries the
identical claim in different, still active and declarative, words. This is a partial supersession
of one G17 decision, disclosed here and in `GATES.md` (P-2) specifically so the operator can
overrule it on read-through — it was not checked by any second reader before this report.

## Page count

Main text is pages 1–5; References begins on page 6, confirmed by parsing the freshly compiled
PDF's own form-feeds. Full PDF 23 pages. None of this session's five fixes changed sentence count
by more than one (F2 and F3 each add one sentence break; F1, F4, F5 are pure reordering or
punctuation), and the page boundary did not move.

## Isolation compile and package

Both tiers pass against a freshly built zip (`build/sim_attrib_overleaf_47ccb87.zip`) extracted
to two separate fresh temp directories, never the repo working copy, `TEXINPUTS` genuinely unset
in both: exit 0, 23 pages, zero undefined references or citations, identical 602,400-byte
`main.pdf` in both tiers, and `pdftotext` output textually identical to the repo working copy.
§2a (`TEXMFHOME` unset) passes in the same narrower this-machine-fallback sense G12 named; this
report does not re-claim it as genuine isolation. Anonymization re-scanned across every packaged
source file and the compiled PDF's extracted text: zero hits in all six locations checked; PDF
`/Author` metadata empty.

## What this report does not certify

Everything `GATES.md` G18's "does not certify" section states. The two most important:

**This is not an independent fourth review.** It is this project's own process doing a
self-review, by the same kind of agent that wrote the prose it is now judging. G17's gate named
this exact limitation and recommended a genuinely external, tone-focused review; that
recommendation is repeated here, not resolved by this session having happened.

**The register is not certified exhausted.** G17 found nine further instances on a second pass
after fixing the six its own brief named. This session found five on one pass. Nothing about a
single clean read rules out a sixth or seventh instance a second reader would catch.

## Honest process caveat

This session's review was one pass by one reader, same as every voice judgment in G16 and G17.
No adversarial critic or second independent agent ran against any of the five findings, or against
the two transition points judged acceptable and left alone.

**Status: `GATES.md` G18 is `ready for review — UNSIGNED`.** Points requiring operator input are
collected, not resolved: P-1 (sign G18 after reading the recompiled PDF start to finish, for how
it sounds), P-2 (whether F2's supersession of G17's four-sentence introduction pattern was the
right call), P-3 (everything else — Q-3, Paris, visibility, disclosure text, the anonymized
package upload, OpenReview submission — unchanged).
