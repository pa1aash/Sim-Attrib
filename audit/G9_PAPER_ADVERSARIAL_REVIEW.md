# The paper, reviewed as an argument rather than as a checklist

**Session G9, 2026-08-24.** The same discipline G4 applied to the diagnostic's numerical
result, applied here to whether the written argument in `paper/main.tex` actually supports the
claims it makes. Read cold, start to finish, before cross-checking against the audit trail
(1.1); reaction recorded below before it could be contaminated by already knowing the answer.

---

# VERDICT: **NEEDS TARGETED FIXES — TWO APPLIED THIS SESSION, ONE STRUCTURAL GAP LEFT OPEN.**

One real citation-rendering defect found and fixed (a compound surname silently truncated by
BibTeX's default parser, in a project that has caught this exact class of error four times
before and thought it had this one covered too). One real readability issue found and fixed
(the introduction's finding-preview read as a dense, hard-to-parse run-on after this session's
own page-limit compression). Everything else checked in 1.2–1.6 **stands** — no method-novelty
drift, no abstract/body inconsistency, no apologetic framing in the negative-result section,
and the four standard reviewer objections all have direct textual answers. **The paper is not
submission-ready on its own terms**: it remains fractionally over the 5-page limit (§4 below),
which this session narrowed dramatically but did not close, and that gap is reported rather
than forced shut.

---

## 1.1 Cold read, before cross-checking anything

Recorded as a naive-but-expert reader's reaction would have it, before consulting the audit
trail. Three things stood out on a first pass:

- **The abstract's closing line -- "Every tool used is prior art; the contribution is the
  finding" -- is doing real work and reads well.** It preempts the "what's new here" objection
  in the first paragraph a reader sees, rather than making them wait for the discussion.
- **The introduction's four-finding preview, before this session's edits, read as four nearly
  identical long sentences in a row**, each opening with a bolded "Where..." clause and running
  15-25 words before its first full stop. On a cold read this felt like skimming a compressed
  outline rather than reading prose -- a legitimate reviewer complaint, addressed in §3 below.
- **The negative-result section (Section 5) reads as confident reporting of a real finding, not
  as an apology for an unbuilt experiment.** "The acceptance probability is not merely small,
  it is statistically indistinguishable from zero, and the obstruction does not move with more
  compute" is assertive, specific language, not hedged. This survived the cold read as the
  paper's strongest section, matching the operator's own prior assessment of it.

## 1.2 Abstract-versus-body consistency — STANDS

The abstract's account of the MMC composition ("we then evaluate a natural selective-inference
construction... it is comfortably affordable at a known parameter and fails to terminate once
the nuisance parameters are only known within a realistic neighborhood") is checked against
Section 5's actual framing ("We evaluate this construction on our own simulator rather than
propose it... [finding] Affordable at a known parameter, unbounded over the nuisance set").
**They agree.** The abstract does not describe the composition as something built and validated
as a working tool; it correctly previews the negative result. No stale framing from an earlier
draft of the abstract survived.

## 1.3 The C1 reframe, checked for drift a second time — STANDS

A second, independent read of every sentence in the paper against `docs/DECISIONS.md`'s C1
ruling, deliberately not reusing G8's own drift-hunt notes (`audit/S8_REPORT.md` §4) as a
checklist. Every place the paper introduces a tool is hedged: "using established
rank-and-condition-number diagnostics rather than proposing new ones" (abstract); "reports four
findings, none a claim about a new method" (introduction); "Every ingredient below is prior
art, applied rather than proposed" (Method); "we cite both as established and evaluate the
composition, rather than propose either as new" (Background); "We evaluate this construction on
our own simulator rather than propose it" (negative result). **No sentence, on this second
pass, implies the diagnostic or the gating composition is a novel method.** Two independent
passes (G8's and this one) finding nothing is meaningfully reassuring without being proof that
a third pass would find nothing -- stated so this isn't oversold.

## 1.4 The four standard reviewer objections — all STANDS, with textual pointers

| Objection | Where the paper answers it | Verdict |
|---|---|---|
| "Why should I believe a 3-component SIR simulator generalizes to anything?" | Limitations: "Every result here is measured on a single simulator under two distortion family sets chosen by us... transport to other simulator classes is untested." Stated plainly, not implied. | STANDS |
| "Isn't the MMC failure just because you didn't try hard enough / didn't use enough compute?" | Section 5: "The acceptance probability is not merely small, it is statistically indistinguishable from zero, **and the obstruction does not move with more compute**." Followed by a structural mechanism (fixed-selection-rule requirement vs. nuisance-induced shift), not just an empirical observation. | STANDS, and preempted structurally rather than only empirically |
| "The single-mechanism-per-component assumption seems very restrictive -- why should I care?" | Method states it first, before any machinery, as load-bearing rather than a footnote; Experiments' "Where it is not" paragraph actively rules out estimator, threshold, and structural explanations for the K=6 confound rather than merely asserting it. Reads as a genuine boundary characterization, not an excuse. | STANDS |
| "This looks like assembled existing tools with no new theorem -- what's the contribution?" | Introduction's closing line: the paper is about a boundary "that can be predicted rather than only discovered" -- the transportability of the *nuisance-to-noise-ratio check itself* (not the specific numeric boundary) is the defended value, and the paper is careful to claim only that narrower, more defensible form of transportability. | STANDS, though this is the softest of the four and a reviewer could reasonably want it argued more forcefully |

## 1.5 Citation and related-work check — ONE DEFECT FOUND AND FIXED

Cross-referenced every `\citet`/`\citep` in Background against `audit/BIBLIOGRAPHY.bib`'s
corrected entries, then verified by **compiling and reading the actual rendered PDF** rather
than trusting the `.bib` source alone -- the same discipline that caught the Catchpole byline
gap in G9's own Phase 0 sweep of the bibliography (`DEVIATIONS.md` D-18).

**Found: `montel2025testsmodelmisspecificationsimulationbased` rendered as "Montel et al.
[2025]" in-text, silently dropping "Anau."** The `.bib` entry's own comment, six sessions old,
already says *"'Anau Montel' is a compound surname and must not be split"* -- and the full name
`Noemi Anau Montel` was correctly entered in the author field. **The correction was recorded
but never enforced**: BibTeX's default name parser splits unprotected multi-word surnames on
whitespace and keeps only the last token for the short citation form (`\citet`, the `bibitem`
label), even though the full reference-list entry rendered the complete name correctly. This is
a rendering-level instance of the exact byline-accuracy failure this project has now caught five
times (G3's four plan-level errors, G8's Catchpole fix, and this one) -- each time because a
downstream task needed the citation to actually be right and checked, not because anything
checks this automatically.

**Fixed**: `author={Noemi Anau Montel and ...}` → `author={Noemi {Anau Montel} and ...}` in
`audit/BIBLIOGRAPHY.bib`, protecting the compound surname as one token for BibTeX's parser
without changing the recorded name string. Verified by recompiling: in-text now renders "Anau
Montel et al. [2025]"; the `bibitem` short-form label now reads `{Anau Montel} et~al.`. Every
other citation in the paper was spot-checked against its rendered form the same way (Kahl,
Sain and Massey, Catchpole and Morgan, Brynjarsdóttir and O'Hagan, Cintrón-Arias, Moré and
Wild, Dufour, Gutenkunst, Freidling) and all render correctly -- Montel was the only compound
(space-containing) surname in the bibliography, which is consistent with it being the only
instance of this failure mode. `DEVIATIONS.md` entry recorded.

## 1.6 The negative-result section's tone — STANDS

Re-read specifically hunting for apologetic language ("unfortunately," "we were unable to,"
hedged framing) versus confident reporting of a genuine, quantified finding. **None found.**
Representative phrases: "a clear pass" (for the affordable half); "not merely small... obstruction
does not move with more compute" (for the negative half); "it is the most transportable result
here" (explicit self-assessment of the finding's value). The section reads as reporting a
result, not excusing an absence. This matches the operator's own prior read of this section as
the project's strongest, and this session's independent check agrees with that assessment
rather than merely repeating it.

## Additional finding, outside the pre-specified checklist: introduction readability, and a formatting inconsistency it revealed

Not one of the six items the session brief pre-specified, but surfaced directly by the cold
read (1.1) and worth recording with the same rigor as the specified items, per the spirit of
the review rather than its letter.

**Found**: the introduction's four-finding preview, after this session's own page-limit
compression (Phase 0), had become four long, structurally identical sentences in a row --
readable on a careful re-read but genuinely hard to parse on a first pass, which is exactly the
failure mode a real reviewer hits once and doesn't forgive. Meanwhile Background and
Limitations had *already* been converted to tight itemized lists for space reasons in the same
Phase 0 pass, leaving the paper in an inconsistent state: two sections itemized, the
structurally identical introduction paragraph left as dense prose.

**Fixed**: converted the introduction's four-finding preview to a matching itemized list.
Recompiled and confirmed no numeric claim changed (`audit/PAPER_NUMBER_VERIFICATION.md`'s
underlying numbers spot-checked against the current file's numeric literals -- unchanged).
**Cost**: this fix cost roughly 90-100 words of the page-limit progress Phase 0 had made (the
itemize environment's overhead is not free), moving the remaining overflow from roughly 20-46
words back up to approximately 116 words (see §4). This trade -- quality over the last fraction
of a page -- was made deliberately and is disclosed here rather than reverted silently to
reclaim the space.

**A second thing the cold read raised and this session talked itself out of, disclosed per the
reclassification rule (S5) rather than silently dropped**: whether Background and Limitations
being formatted as bulleted lists, while Method/Experiments/the negative result remain flowing
prose, reads as an inconsistent or rushed formatting choice. **Initially flagged as a possible
issue during the cold read.** On reflection: bulleted related-work and limitations sections are
common, often reviewer-preferred practice in ML venues (scannable, explicit about what's being
claimed), and NeurIPS papers under space pressure do this routinely. **Reclassified as not a
problem** -- the heterogeneity is a normal stylistic pattern, not a defect, and no change was
made on this account.

---

## What this review does not certify

- **That a genuinely independent reviewer would reach the same conclusions.** This is one
  session's adversarial read of its own (and the prior session's) prose. The same limitation
  every gate in this project has recorded since G4.
- **That the four pre-specified reviewer objections (1.4) are answered as forcefully as they
  could be.** Three stand cleanly; the fourth ("what's the contribution if it's all existing
  tools") is answered but is the softest of the four, and a real reviewer might still push on
  it. Not rewritten further this session, on the judgement that doing so risked overclaiming the
  paper's own transportability result to make the contribution sound larger than it is --
  exactly the failure mode the C1 amendment exists to prevent.
- **That the page limit is closed.** It is not; see §4 below and `audit/S9_REPORT.md`.
- **That this is the only citation-rendering defect in the bibliography.** One was found by
  spot-checking every citation's rendered form after finding the first. A systematic check --
  compiling and grep-checking every `\bibitem` short-form label against its full author list --
  was not run as an automated check; it was done by eye, once.

---

## 4. The page limit, honestly restated

`paper/main.tex` compiles cleanly (no undefined references, no undefined citations, no
overfull boxes) at **6 physical pages of body content**, one page over Sim2Science's 5-page
limit. This session narrowed the gap substantially through legitimate means: moving the
simulator schematic to the appendix (operator decision 2), flexible figure placement, converting
two sections to tight itemized lists, further figure-width reduction, and further prose
tightening throughout, re-verified against `audit/PAPER_NUMBER_VERIFICATION.md` at each step so
no number or claim was cut. At the tightest point reached this session, the overflow was **20
words** -- a single clause. The introduction readability fix (above) traded roughly 90-100 of
those words back for a real quality improvement, landing the current state at approximately
**116 words of overflow**, well under a fifth of a page.

**What would close the rest of the gap, and why none of it was done unilaterally**: cutting the
last remaining Limitations item outright (the hand-placed-annotation disclosure), cutting
further from the now-tightened introduction or background, or a typographic nudge beyond what
`enumitem`'s list spacing already provides. Each trades either real content or further
readability against the last fraction of a page. This is precisely the class of decision S7
("honesty about absence") asks to be flagged rather than forced through, and precisely the
kind of judgement call `GATES.md` G8 already made once this session's predecessor and disclosed
rather than hid. **NEEDS FIX**, carried to `audit/S9_REPORT.md` and `GATES.md` G9 rather than
patched further.
