# S11 — Session G11 report

**Prepared 2026-08-25.** This session's mandate: an independent external reviewer with no
project history returned **Weak Reject, confidence 4/5** on the paper, with 6 Tier-1 (must-fix)
and 15 Tier-2 (should-fix) findings, and a specific instruction to run the real
Dufour-confidence-set-bounded MMC check rather than a cheaper reframe of it, before fixing
everything else and re-verifying the whole draft more rigorously than any prior session did.

## 1. THE HEADLINE

**T1-3 is done, and the paper's central claim survives — decisively.** A maximum-likelihood fit
of the simulator's five nuisance parameters (transmission rate, recovery rate, reporting
fraction, initial infections, observation noise scale) to one realised dataset, with a
Bonferroni-corrected 95% Wald confidence box built from the observed Fisher information, gives
relative half-widths from 2.3% to 16.6% on every coordinate — wider, on every single one, than
the ±0.5% box the paper's existing fixed-box sweep already showed breaks the MMC composition.
Re-measuring the cost gate inside this **data-implied** box rather than an assumed one: the
acceptance probability collapses to 1×10⁻⁵ at the primary case and to exactly zero at the other
three declared combinations, and the gate fails at every corner under all four. The cheapest
declared corner alone needs 9.9×10⁹ draws against a 10⁸ budget — two orders of magnitude over,
before the confidence interval is even taken into account. Section 5's negative result is now
grounded in a real, measured confidence set instead of a round assumed number, and it comes out
**stronger**, not weaker.

**All six Tier-1 findings and 13 of the 15 Tier-2 findings are fixed.** Two — T2-4 and T2-6 —
are not, and their content is genuinely unknown to this session. §2 explains why and what it
means.

**This session's own re-verification pass (Phase 4) found and fixed four defects beyond what the
external review flagged**, the largest of which is that the prior session's own "Overleaf-
equivalent" isolation test was never actually testing what it claimed to test. §3.

**The page limit is not closed.** Six pages of body content against a five-page limit — the same
page count G9 ended at, despite this session absorbing the full external-review content mandate
(a new section, eight new citations, a restructured summary table, expanded figures) into that
same six pages. §4 has the honest accounting, including a fix this session tried and reverted.

## 2. WHAT WAS FIXED, AND THE ONE THING THAT WASN'T

### T1-3 — the confidence-set check itself

`src/diagnostics/confidence_set_check.py` builds the data-implied box and re-measures the gate.
Two things worth recording about how it was built:

- **Dufour's actual text was fetched and full-text-searched before any construction was
  attributed to him.** The word "Bonferroni" appears zero times in his paper. The Bonferroni
  correction used here is this session's own choice for turning Dufour's Wald-ellipsoid
  confidence-set machinery into a rectangular box compatible with the project's existing
  box-based MMC infrastructure, and `audit/DUFOUR_CONFIDENCE_SET_CHECK.md` states this
  attribution precisely rather than letting a reader infer it from Dufour.
- **The MLE fit needed a real numerical-methods fix.** Raw L-BFGS-B from a perturbed starting
  point sent its first trial step, sized from a steep initial gradient, to a corner of parameter
  space where every coordinate gives a non-positive incidence mean — infinite negative
  log-likelihood — and then reported spurious convergence at the unmoved starting point. Fixed
  by switching to Nelder-Mead in log-parametrized space, which does not size its first step from
  a single gradient evaluation. This is documented in the module's own docstring so a future
  session does not rediscover it by repeating the failure.

### T1-1, T1-4, T1-5, T1-6 — bundled, and individually verified this session

Committed together (`c40a512`) since they touch the same region of the appendix and Section 4.
T1-1 replaced the appendix's literal TODO with a generated claim-to-source table. T1-4 moved the
simulator schematic into Section 4 and reduced it — a verbose "three distortion families"
prose block became a compact 3×2 table, and two footnote-style qualifications moved into the
caption. T1-5 was a full anonymity re-scan, not just the two instances the external review
named, and found five more: a baked-in internal decision ID in a figure's rendered SVG text, a
phrase inviting a search for related work by the same authors, and session/operator-decision
language in four LaTeX comments. T1-6 corrected three checklist answers that no longer matched
the compiled PDF.

### T1-2 — the page-limit pass, done last as instructed

See §4.

### T2-1 through T2-15 — 13 of 15 fixed

T2-1/T2-2 (the rank-at-τ and κ≤κ_max criteria stated as one condition rather than two, and the
κ² compute-cost claim given a one-line derivation), T2-3 (a second, data-motivated η-scaling
using the confidence-set standard errors, showing the eight-assignment and six-column verdicts
hold in direction under it too), T2-5 (eight citations engaged in Related Work, not
name-dropped — four of the eight turned out to already be silently present in the bibliography
from earlier sessions and simply uncited), T2-7 (the scope restriction stated in the
introduction's own first contribution sentence rather than left implicit), T2-8 (the
two-panel non-termination figure split, per-figure font floors enforced), T2-9 (repeated
metaphor language reduced, the diagnostic's four steps turned into an actual numbered list),
T2-10 (abstract tightened, one concrete number retained for a skimming reader), T2-11 (a
Limitations bullet on where a learned summary statistic would sit), T2-12 (the K-vs-column-count
notation conflict resolved explicitly), T2-13 (the appendix table's plateau-stability caption
made honest about noise rather than presenting point estimates as exact), T2-14 (checklist moved
after the appendix, matching NeurIPS convention), T2-15 (one sentence stating precisely what the
literature's existing baseline test would output on the paper's own six-column confound).

**T2-4 and T2-6 are not fixed, and this session does not know what they said.** This session's
context was compacted partway through, and the summary carried forward across that compaction
retained every other Tier-1/Tier-2 item's substance but not these two. Every other item's
content was independently reconstructible from this session's own commit messages while
preparing this report — each commit states the finding it addresses in prose, not just its tag
— and a full-history grep confirms T2-4 and T2-6 appear under no commit, anywhere. This report
does not invent plausible content for them to look complete. **The operator's own copy of the
external review is the only way to close this gap**, and it should be treated as a real,
outstanding item, not assumed to be something minor that happened to get skipped.

## 3. PHASE 4 — WHAT THIS SESSION'S OWN VERIFICATION FOUND

The standing instruction was that this session's own re-verification had to exceed prior
sessions' rigor, not repeat it. Four things were found this way, none flagged by the external
review:

1. **An internal review-tracking label ("T2-3") baked into three rows of the generated appendix
   claims table**, introduced by this session's own T2-3 fix and caught by an anonymity re-scan
   run independently of the targeted T1-5 fixes — reading the rendered output the way a
   reviewer would, not re-running the same grep pattern that caught the earlier five. Fixed at
   the source (`src/diagnostics/report_claims.py`) and regenerated.

2. **`paper/appendix_claims_table.tex` missing from the Overleaf package's allowlist.** This
   session's own T1-1 fix added a third `\input{}` call to `main.tex`; the packaging script's
   figure-discovery loop only parses `\includegraphics`, and the allowlist is otherwise
   hand-maintained, so this file — which the paper cannot compile without — was silently absent
   from every package built since it was created. Every submission zip built between T1-1 and
   this fix would have failed to compile on Overleaf with a file-not-found error.

3. **The larger of the two: `\usepackage[dblblindworkshop]{neurips_2026}` depends on a local
   `TEXINPUTS` environment variable this project's own build scripts export, which a plain
   Overleaf project upload has no way to set.** The prior session's own "Overleaf-equivalent"
   isolation test reported PASS, but its own test setup exported the same local `TEXINPUTS`
   convention into the "isolated" environment before compiling — so it was never actually
   testing self-containment, only re-confirming the local convention it started from. This
   session re-ran that test with `TEXINPUTS` genuinely unset for the first time and it failed
   immediately: `File 'neurips_2026.sty' not found.` Fixed using kpathsea's own path-relative
   file resolution (`\usepackage[...]{neurips_2026_template/neurips_2026}`, which needs no
   environment variable), and verified against both the repo working copy and a freshly
   unzipped, isolated copy of the rebuilt package: identical exit 0, identical 22 pages,
   byte-identical `main.pdf` in both. Full detail in `audit/OVERLEAF_PACKAGE_REPORT.md` §0,
   including why this is disclosed at this length rather than summarized — it is the kind of
   defect that would only have surfaced after an actual OpenReview upload, at which point it is
   a missed deadline rather than a quiet fix.

4. **A citation pointing to the wrong artifact.** `main.tex`'s eight-family-assignments
   paragraph cited "1.523× under the tightest one" to Figure 5 (`fig:threshold`). Figure 5's own
   three lanes show only 9.88× (base) and 1.547× (adversarial/AAA); the 1.523× figure belongs to
   the ABA assignment, one of the eight rows in Table `tab:sb-eight` in the appendix — a
   different artifact Figure 5 does not display. Found by cross-checking every `\ref{fig:*}` and
   `\ref{tab:*}` call against what that figure or table actually shows, not by trusting that a
   citation pointing at a real figure means it points at the right one. Retargeted to the table.

Beyond these four, this session ran and confirms clean:

- **A full number-trace of the entire document** (~150+ distinct numeric claims in `main.tex`
  and `appendix_tables.tex`, checked against the underlying `results/*.yaml` files directly, not
  against the generated claims table) — **zero mismatches**. One initially-flagged discrepancy
  (the "0.9–2.7%" MLE-standard-error-scaling range) was chased into `alt_eta_scaling.py`'s
  source and confirmed correct; the yaml's own internally-used `per_column_relative_scale` field
  is a different, non-cited ratio that superficially looked like the right one.
- **The provenance table's commit hashes and seeds**, each confirmed to exist in `git log` and
  each recorded commit confirmed to precede, by minutes, the commit that actually added the
  corresponding results file — the expected "code committed → script run → results committed"
  pattern, not merely a hash that happens to exist somewhere in history.
- **The full test suite** — 177 passed.
- **The rebuilt Overleaf package**, both isolation tiers, `TEXINPUTS` unset in both — PASS, PASS,
  byte-identical output.
- **PDF metadata** (`pdfinfo` on the local preview compile) — no `Author` field, no identifying
  path in `Creator`/`Producer`; the local compile's `CreationDate` does carry this machine's
  timezone, which is exactly why that file is not the submission artifact.
- **Every checklist answer**, re-read against the current compiled PDF item by item rather than
  assumed carried-over — all thirteen filled items still match; item 13 (AI-use disclosure)
  remains the operator's own placeholder, untouched.

## 4. THE PAGE LIMIT — THE HONEST ACCOUNTING

Six pages of body content against Sim2Science's five-page limit. This is unchanged in raw page
count from G9's end state, but that comparison undersells what happened: between G9 and this
session, the paper absorbed an entire new section (Section 5's confidence-set result), eight new
citations genuinely engaged rather than name-dropped, a restructured four-row summary table, and
an expanded two-panel main-text figure — all mandated by the external review — and still landed
at the same six pages, not eight or nine. Real cuts made this pass: the introduction's bullet
list replaced by the summary table, the coherence discussion the external review flagged as
"reported for interpretation and then not used" removed, five near-duplicate "everything here is
prior art" statements collapsed to two, Limitations merged from five bullets to three without
dropping any of the five distinct limitations, and the two largest Related Work paragraphs and
the T2-3 robustness paragraphs shortened while keeping every citation and every number.

**One cut was tried and reverted, and that reversal should not be re-attempted without solving
the underlying tradeoff differently.** Reducing `\includegraphics` width for `fig4_assignments`
and `fig3_spectrum` (0.62→0.5\linewidth) and `fig2_simulator` (\linewidth→0.88\linewidth) would
have bought the needed vertical space. Each figure's matplotlib script sets its internal font
sizes (`style.SIZE_LABEL`=8pt, `style.SIZE_TICK`=7pt) calibrated for a specific *designed* print
width (`style.FIG_FULL` or `style.FIG_TWOTHIRDS`). Rendering at a smaller `\includegraphics`
width than that design intent shrinks the effective on-page font size proportionally — at
0.5\linewidth against a `FIG_FULL` design, roughly 50%, taking an 8pt label below the venue's
absolute 6pt floor. Reverted to the original widths; the needed savings were found through
text-only cuts instead, which is why the page count did not close all the way to five.

## 5. WHAT SHOULD HAPPEN NEXT

1. **Close T2-4 and T2-6.** Needs the operator's own copy of the external review; nothing in
   this repository can supply their content.
2. **Decide whether the six-page state is acceptable**, or whether closing the last page is worth
   further text-only cuts, a font-floor exception, or accepting the overage and disclosing it at
   submission (Sim2Science's own enforcement strictness for this is not established in this
   project's records — `audit/VENUE.md` does not settle it).
3. **Consider a second external review** against this session's fixes before submitting, given
   how much of this session's own most consequential finding (the `TEXINPUTS` defect) came from
   not trusting a prior session's own "PASS."
4. **Fill or explicitly accept the G10 gap** — no `GATES.md` entry, no `audit/S10_REPORT.md`
   exists for that session, discovered while preparing G11 and not backfilled here since it is
   not this session's own work to gate.

## 6. PROCESS CAVEATS — what this session did badly or not at all

- **The external review's verbatim text was not saved to a durable file in this repository
  before work began against it.** A mid-session context compaction cost two of its fifteen
  Tier-2 findings entirely, and they cannot be recovered from anything in this repository. A
  future session working from an externally supplied review should save it verbatim to `audit/`
  as its first action, specifically so a compaction cannot cost part of the mandate.
- **G10's own isolation-test flaw survived one full session whose purpose was exactly to test
  self-containment.** It was caught here only because this session's standing instruction was to
  re-run prior checks with the actual failure mode in mind, not to trust a reported PASS. Every
  prior gate in this project that found something the one before it missed (G4 on G3, G5 on G4,
  G9 on G8) is the same pattern one level up: a test that reports PASS is only as good as what it
  varied between "isolated" and "not," and this project has now demonstrated that failure mode at
  every level from a single numeric flag up to an entire isolation-test methodology.
- **No second external review has been commissioned.** See §5.
- **Google Scholar still not searched.** Eleventh session with code. O-7, unchanged since G0.

## 7. POINTS REQUIRING OPERATOR INPUT

- **P-1 (carried from G11's brief).** G11 sign-off itself.
- **P-2.** Confirmation of the T1-3 confidence-set verdict's framing in Section 5 — this session
  read the result as strengthening the paper's central claim (a data-implied box, not an assumed
  one, still fails the composition, by a wide margin) and wrote the section that way. The
  operator may read the emphasis differently.
- **P-3.** Whether to commission a second external review before submission, and if so, whether
  to wait for T2-4/T2-6 to be recovered first.
- **P-4 (carried from prior sessions, still open).** Q-3 (reciprocal reviewer nomination),
  repository visibility, and in-person Paris attendance — all OpenReview-form or logistics
  questions, not file problems, tracked in `docs/OPEN_QUESTIONS.md` and
  `audit/OVERLEAF_PACKAGE_REPORT.md` §7.

## 8. THE ONE-PARAGRAPH VERSION

The external reviewer's single most important ask — the real confidence-set-bounded MMC check —
is done, and the paper's negative result comes out of it stronger than before. Six of six Tier-1
findings and thirteen of fifteen Tier-2 findings are fixed and individually verified; two Tier-2
findings were lost to a mid-session context compaction and are disclosed as unknown rather than
invented. This session's own re-verification, held to a higher standard than any prior session's,
found and fixed four more defects on its own — most notably that the previous session's Overleaf
self-containment test was testing the wrong thing and would have let a broken submission package
through. The page limit is not closed, at six pages against five, after a genuine tradeoff was
found and correctly declined rather than shipped quietly. Status: ready for review, unsigned, not
submitted, repository visibility unchanged.
