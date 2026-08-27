# S17 — Session G17 report

**Prepared 2026-08-27.** This session's mandate was a pure prose voice rewrite of
`paper/main.tex` and `paper/checklist.tex`. Sixteen sessions of writing internal audit documents
in this project's own register — state a finding, hedge it, disclaim its scope, cross-reference
its origin, qualify it against three ways it could be wrong — had leaked into the paper's actual
prose. That register is right for a gate entry and wrong for a paper. Full detail in `GATES.md`
G17; this is the summary to start from.

## No claim changed. This is measured, not asserted.

Leading with it because it is the session's binding constraint and the one thing a reader should
not have to take on trust.

- **Numeric literals.** A token-level diff of every numeric literal in `paper/main.tex` between
  `HEAD` (`2ad4e68`) and this session's final state returns **two** differing tokens. Both are
  accounted for: the `topsep=1pt,itemsep=0pt,parsep=0pt` list-spacing parameters that went away
  with Section 2's `itemize` environment (LaTeX formatting directives, not data), and one
  redundant *second* statement of `1/τ` whose content survives in words as "these are one
  condition, not two" — which is T2-1's own protected phrasing. A multiset diff over the
  *rendered* main text, with the venue template's left-margin line numbers stripped, agrees. No
  scientific number, unit, or caveat was added, removed, or altered.
- **Citations.** 20 occurrences, 19 distinct keys — **identical** before and after, verified by
  key-multiset diff rather than by eye. This matters because Section 2 was structurally rewritten.
- **Protected clauses.** All 35 greppable prior-review fixes re-checked individually against the
  current text: 35 intact, 0 missing. Five things that *should* be absent (the K-vs-columns
  disclaimer, `K=6` legend text, "for space" language, "automated check", prose em-dashes) are
  confirmed absent.
- **Figures.** No figure was regenerated. No figure's data changed.

## What was rewritten

**The six named symptoms.** Two needed no edit and are reported as found rather than
manufactured into work: the "prior art / the contribution is the finding" aphorism already
appeared exactly once, in the abstract (G16's W16-11 had done it), and the K-vs-columns
disclaimer was already gone with Figure 2's legend already reading "six-column union" rather than
"K=6" (verified on the rendered figure file, not on the plotting script). The other four:

- **Dashes.** Three prose-aside em-dashes survived G14's reported 38-instance sweep and G15's
  re-verification — in Section 2's Montel paragraph, Section 2's post-selection-inference
  sentence, and the Limitations second-θ clause. Each was rewritten individually, not by blind
  substitution. `grep -n -- '---' paper/main.tex` now returns zero lines; a Unicode sweep for
  U+2013/U+2014 across every `.tex` returns zero; the rendered main text contains exactly one
  en-dash, the numeric range `0.9–2.7%`, which is out of scope.
- **The "not X, not Y, not Z" chain.** Section 4's six-column ruling-out sentence — one sentence
  carrying three ruled-out explanations, reading as a defence brief — is now three short
  sentences, one explanation each. Every number preserved.
- **"Moved here … for space."** All three appendix subsections now open by saying what they
  contain instead of narrating the paper's own editing history.
- **"Hand-placed annotations outside the automated check."** Removed. Both annotations it
  disclosed restate quantities the same figures' captions already state, and "the automated
  check" names this project's internal `src/viz/provenance.py`, not a limitation of the work.
  `checklist.tex` item 2's mirroring clause was updated in the same edit so the checklist did not
  drift from the PDF.

**The introduction** now states its four findings in the paper's own voice — "We find that…",
"Separability then fails…", "We find that…", "And we predict…" — instead of one semicolon-chained
sentence ending in a pointer to an appendix table.

**Section 2** is four prose paragraphs on the same four themes instead of four bullets, written
as an argument about what is and is not already known. G16's measured Montel result closes
paragraph 1 rather than sitting appended; Fithian/Sun/Taylor and Lee/Sun/Sun/Taylor are the
contrast paragraph 4 turns on.

**Phase 4's full re-read found nine further instances** of the same register that the six named
symptoms did not cover — a heading justifying the paper's own ordering, a step-4 clause restating
the equation above it, a self-referential "answers the first question, not the second", the paper
explaining its own taxonomy to itself, one surviving metaphor, one loose description immediately
superseded by a precise one, one interpretation stated in both body and caption, a
double-parenthetical, and three passive constructions where an active statement was equally
defensible. All nine are enumerated in `GATES.md` G17.

## Two defects found that this session was not looking for

**G16 silently dropped a protected external-review fix.** The literal `(where $s(y)$ would sit)`
in the Limitations "no learned component" bullet is T2-11, a first-review Tier-2 item. It is
present at `19f9a59` (G15's final state) and absent at `efc81c9` (G16). G14's and G15's
re-verification tables both record it as "verified still present verbatim"; G16's table does not
mention it. Restored. It survived undetected because the clause spans a source line break, so a
line-scoped grep misses it — the same class of miss as the dash finding.

**`audit/BIBLIOGRAPHY.bib` line 1 carried the repository name** in a `%%%%` header comment, and
that file is on `scripts/build_overleaf_package.sh`'s allowlist, so it ships to reviewers. G8.4
claims the source was "grepped for the operator's name, GitHub handle, and repository name — zero
hits"; that claim was wrong, most likely because the grep was scoped to `paper/`. Fixed to a
neutral wording. The comment never reaches the compiled PDF, so no rendered output changed. Only
the header comment was touched; no bibliographic record, field, or value was altered.

## Page count

Main text is pages 1–5; References begins on page 6. Confirmed by parsing the PDF's own
form-feeds, in both the repo working copy and the isolated package extraction. Full PDF 23 pages.

Getting there is worth stating honestly: Phase 2's properly-stated findings list and Phase 3's
prose conversion pushed the main text **three lines onto page 6**, and every one of those lines
was recovered by cutting redundant audit-register prose. `\parskip`, float separations, caption
skips, font sizes and figure widths are all exactly as G16 left them — this session did not touch
the whitespace lever G12–G14 and G16 each reached for. The brief's expectation that voice
tightening would leave "slack, not pressure" did not hold; it came out even.

## Isolation compile and package

Both tiers pass against a freshly built zip extracted into a fresh temp directory (never the repo
working copy), `TEXINPUTS` genuinely unset in both: exit 0, 23 pages, zero undefined references
or citations, identical 602,452-byte `main.pdf` in both tiers, and `pdftotext` output byte-
identical to the repo working copy. §2a (`TEXMFHOME` unset) passes only in the narrower
this-machine-fallback sense G12/G13 named, which this session does not re-claim as genuine
isolation. Anonymization re-scanned inside the extraction itself: zero hits.

## What this report does not certify

Everything `GATES.md` G17's "does not certify" section states. The two most likely to be skipped:

**The register is not certified exhausted.** This session fixed nine residual instances *after*
fixing the six the brief named — direct evidence that one reader's pass does not find them all. A
tenth plausibly remains.

**"No claim changed" was verified by diffing, not by re-deriving.** Numeric literals, citation
keys and thirty-five protected clauses were all diffed against `HEAD`. That is a strong check
against accidental loss and a weaker one against a rewrite that keeps every number while subtly
shifting what a sentence asserts. The two rewrites nearest that line are named for scrutiny:
Section 4's three-sentence ruling-out and Section 1's findings list.

**A fourth external review, focused on readability and tone, is recommended** — more strongly
than G16 recommended a third, because the three prior reviews were content-focused and none was
asked about register, and because the agent that rewrote the prose is the worst-placed reader to
judge whether it now reads well.

## Honest process caveats

The dash finding is a repeat of a known failure mode, not a new one: G14 claimed the sweep
complete, G15 re-verified it "intact" without re-running the grep, and three instances were
sitting there behind one command. The narrow, mechanical lesson recorded in the gate is that a
completion claim about a greppable property must be closed with the grep, and the grep's
zero-result output belongs in the gate entry.

Two of the six named symptoms needed no work because the brief was written against a pre-G16
picture. Figure-internal em-dashes were found in `figures/fig2_simulator.pdf`'s hand-placed panel
headings and **deliberately not changed** — they are heading-to-descriptor separators in a
diagram rather than prose asides, and they sit outside the brief's named scope, but they are
named in the gate so nobody reads "zero dashes" as broader than it is. And no adversarial critic
or second independent agent ran against this session's own prose judgments; every "this reads
better now" here is one session's single-pass opinion.

**Status: `GATES.md` G17 is `ready for review — UNSIGNED`.** Points requiring operator input are
collected, not resolved: P-1 (sign G17 after reading the recompiled PDF start to finish for how
it sounds, not for defects), P-2 (whether a fourth, tone-focused external review is worth
running), P-3 (everything else — Q-3, Paris, visibility, disclosure text, the anonymized package
upload, OpenReview submission — unchanged).
