# S14 — Session G14 report

**Prepared 2026-08-26.** This session's mandate: close every item on the second external
review's "Path to Acceptance, Round 2" (R14-1 through R14-10), then a broader polish pass
(paper-wide dash removal, a title/abstract tightening check, figure-caption compression to
3 sentences or fewer, a diagram-overlap sweep), then a full re-verification against both
review rounds' complete history.

## 1. THE HEADLINE

**Every item from both review rounds is now closed.** All 6 Tier-1 and 15 Tier-2 findings from
the *first* external review (closed as of G12, page limit closed as of G13) remain intact after
this session's substantial rewriting — individually re-checked, not assumed carried forward
(§4 below). All 10 items on the *second* external review's Path to Acceptance are addressed:
R14-1 (the one Tier-1 item) and R14-2 through R14-9 fixed; R14-10 (optional) explicitly declined,
with the reasoning stated rather than silently skipped.

**Final page count: exactly 5 pages** (Abstract through Limitations; References start page 6),
confirmed by rendering pages 5–6 directly, twice — once after this session's own R14-series
additions reopened the budget, and again after Figure 1's legibility fix reopened it a second
time.

**Final abstract word count: 168 words**, essentially unchanged from the ~170 the second review
itself measured and judged "accurate and appropriately scoped." No further trim was needed after
the P-1 dash-removal pass; the abstract was judged, on a fresh close read, to already earn its
place and state its findings at the right confidence level (P-2, below).

**This session's own recomputation of the review's own highest-value suggestion (R14-2) did not
confirm the review's estimate.** The review guessed the MMC gate's failure boundary sits at
Mahalanobis radius "roughly 1.3," comfortably inside the 95% confidence ellipsoid. The rigorous,
correlation-aware recomputation from this project's own Fisher-information covariance puts it at
radius 3.56 — just past the ellipsoid's edge (radius ≈3.33), not comfortably inside it. This is
reported as the paper's actual finding, not silently adjusted to match the review's guess: see §2.

**This session's own visual sweep (P-4) found two real, previously-undetected legibility defects**
— Figure 1's labels rendering below the venue's ~6pt floor, and Table 1 hyphenating mid-word in
its narrow columns — neither of which either external review located precisely enough to act on
directly, and neither of which any of the thirteen prior sessions' own re-verification passes
caught. Both fixed; see §3.

**A connectivity/API failure interrupted this session mid-task**, during the dash-removal pass.
Resumed by checking actual git/file state rather than trusting this session's own prior
narration — see §5.

**A final complete read-through of the compiled PDF, done as part of preparing this report, found
one further miss: a literal `--` baked into Figure 3(b)'s hand-placed annotation text** (matplotlib
`annotate()`, not LaTeX source), which the source-level P-1 grep (scoped to `paper/*.tex`) could
not have caught because the text lives in `src/viz/fig6_nontermination.py`, not in a `.tex` file.
Found by reading the compiled PDF's own extracted text end to end rather than trusting the P-1
grep's scope was already exhaustive. Fixed and the figure regenerated; see §5.

**The paper reads coherently, start to finish, after this session's rewriting** — confirmed by a
complete read-through of the freshly compiled PDF (not a mechanical checklist pass) as the last
step before writing this report, which is what caught the Figure 3 annotation miss above.

## 2. R14-2 — THE ELLIPSOID COMPUTATION, IN FULL

The review's suggestion: state the Mahalanobis radius of the round box at which the MMC gate
first fails, relative to the Fisher-information-based standard errors, and compare it to the 95%
chi-squared radius for 5 degrees of freedom ($\sqrt{\chi^2_{5,0.95}}\approx3.33$). The review's own
back-of-envelope check suggested a radius of roughly 1.3 — "well inside" the ellipsoid.

This session recomputed it directly, in two stages, before writing anything into the paper:

1. **Diagonal (uncorrelated) approximation**, using only the per-coordinate standard errors from
   `results/confidence_set_mmc.yaml`'s `fisher_information.standard_errors`: the ±0.75% box (the
   smallest round box at which the gate first fails, per `results/boundary_sweep.yaml`'s
   per-width gate verdicts) gives radius ≈0.93 — in the same ballpark as the review's guess.
2. **Full, correlation-aware Mahalanobis distance**, using the actual covariance
   $\Sigma = D\,R\,D$ built from the file's own `standard_errors` and `correlation_matrix`
   (cross-checked: $\Sigma^{-1}$'s eigenvalues match the file's own stored `hessian_eigenvalues`
   exactly, confirming the inversion is correct before trusting it further). Because
   $\beta$ and $\gamma$ are correlated at 0.88 in this project's own Fisher information, the
   diagonal approximation is not the mathematically correct statistic to compare against a
   chi-squared threshold (that comparison is only valid for the true, correlation-aware distance).
   Using the actual worst-cell corner directions recorded in `boundary_sweep.yaml`
   (`"w0.005|corner|--+--"` and `"w0.0075|corner|--++-"`): the ±0.5% box (still passing at every
   corner) sits at radius 2.71; the ±0.75% box (first fails) sits at radius 3.56 — just past the
   ellipsoid's edge.

**This is not the review's own claim confirmed; it is a different, more precise finding**, and a
sharper one: rather than the failure boundary sitting deep inside a generous confidence region,
it sits essentially where a real analyst's 95% confidence region itself ends. Section 5 now states
this directly, with both boxes' radii and the comparison, rather than the review's own imprecise
estimate. The diagonal approximation's closer match to the review's guess is noted in this report
(not in the paper) as the likely source of the review's own back-of-envelope number.

## 3. THE TWO DEFECTS P-4 FOUND

**Figure 1 (`fig4_assignments`), value labels and $\kappa_{\max}$ annotation below the venue's
~6pt floor.** Root cause: `src/viz/fig4_assignments.py` sets its native matplotlib figure width
to `style.FIG_FULL` (5.5in, i.e. designed for near-full-linewidth inclusion), with 8pt nominal
label fonts — but `paper/main.tex` included it at only `width=0.62\linewidth`, a leftover
consistency choice against a sibling figure (`fig3_spectrum`) whose *own* native design width
(`style.FIG_TWOTHIRDS`, 3.67in) makes 0.62\linewidth the right choice for it, but not for
`fig4_assignments`. The effective on-page font size was therefore $8\text{pt}\times0.62\approx5.0$pt,
below the floor. Session G11 investigated exactly this class of defect (`audit/S11_REPORT.md` §4)
but only tested a *further* reduction from the existing 0.62 (to 0.5), correctly found that made
things worse, and reverted — without checking whether the existing 0.62 itself already violated
the floor. It did. Fixed by widening to `width=0.78\linewidth` (effective ≈6.2pt, the smallest
value this session found that clears the floor with a small margin), verified by reading a fresh
400dpi render directly.

**Table 1 (the compact four-findings overview), mid-word hyphenation.** "attribution identifi-
able", "data-implied nui-sance box", and "once a component carries 2 distor-tion parameters" were
all wrapping with a forced hyphen inside a real word, inside the table's narrow `p{}` columns —
exactly the "illegible cell" defect R14-6 named for the *appendix* claims table, but present here
too, in a table the review evidently did not inspect at print resolution. Fixed by rebalancing
column widths (finding 0.17→0.20\linewidth, object 0.17→0.13, key number 0.15→0.14) and setting
`\hyphenpenalty=10000` for the table (compound words with real hyphens, like
"one-parameter-per-component", still break at their own hyphens normally). Verified by a fresh
render: every cell now wraps at whole words.

**Widening Figure 1 cost real vertical space and reopened the just-closed 5-page budget.**
Recovered by removing one further non-load-bearing aside from Background (a sentence naming two
alternative composite-null repairs, Xie's repro samples and Barber & Janson's approximate
co-sufficient sampling, not used anywhere else in the paper's argument — a real, if minor, content
reduction, disclosed here and in the gate rather than buried in a diff) rather than by touching
anything load-bearing.

## 4. RE-VERIFICATION AGAINST BOTH REVIEW ROUNDS

The full item-by-item table is in `GATES.md`'s G14 entry (Phase 5 section). Summary: all 21
first-review findings (6 Tier-1, 15 Tier-2) and both first-review novelty threat-checks (R1: DEAD,
R2: NARROW-CONDITIONAL) verified still intact — several (T1-4, T2-3, T2-7, T2-12) strengthened
rather than merely preserved by this session's own R14-series work, which built directly on the
same infrastructure those fixes established. One item, T2-5 (eight Related Work citations
engaged), lost two of its citations to this session's page-budget recovery (§3) — disclosed as a
real, minor reduction, not a silent one.

**One honest limitation of this section.** The G14 session brief asked this session to also
re-verify "the R-1/R-2/R-3 items from the second review's cross-check" specifically. That cross-
check's literal text lived only in this session's original prompt, which is not persisted
anywhere in this repository, and a connectivity failure partway through this session (§5)
prevented full recovery of that text from context. This session verified the first review's own
R1/R2 novelty threat-checks instead (still intact, unchanged), which may or may not be the same
items the second review's cross-check labeled identically. Recorded as a gap rather than papered
over with an assumption; the operator's own copy of the second review's cross-check section would
close it directly if the distinction matters before submission.

## 5. THE CONNECTIVITY INTERRUPTION, AND HOW THIS SESSION RESUMED

Partway through Phase 3 (P-1, paper-wide dash removal), this session was cut off by a
connectivity/API failure. On resume, per the operator's own explicit instruction, this session
checked `git status`, `git log`, and fresh greps against the actual files on disk — not its own
prior turn's narration, which cannot be trusted to reflect what actually landed. This found:
`paper/main.tex` and `paper/checklist.tex` were already fully clean of every " -- " instance
(31 and 2 respectively, both confirmed by grep returning zero matches); `paper/appendix_claims_table.tex`'s
5 section-heading dashes were not yet fixed. That file is generated
(`src/diagnostics/report_claims.py`), so the fix was made at the source (`TITLES` dict) and the
file regenerated, rather than hand-patched — preserving the "generated, not hand-typed" invariant
the file's own header comment states. This is the correct outcome of the standing instruction to
verify against artifacts rather than narration: a session that trusted its own prior turn's
self-report of "P-1 in progress" would not have known precisely which of the three target files
still needed work.

A second, independent miss was caught later, while preparing this report: reading the freshly
compiled PDF's extracted text end to end (not a targeted grep) surfaced a literal `--` inside
Figure 3(b)'s hand-placed matplotlib annotation, invisible to the `paper/*.tex`-scoped P-1 grep
because the text lives in a `.py` file. Fixed (§3's sibling fix, in `fig6_nontermination.py`) and
the figure regenerated. Recorded as a reason a full read-through, not only a grep sweep, earned
its place as this session's final check.

## 6. WHAT SHOULD HAPPEN NEXT

1. **A third external review is recommended before submission**, more strongly than G13's own
   recommendation of a second one — this session touched nearly every paragraph in the document
   (dash removal, caption compression, the R14-series content changes), more main-text rewriting
   than any single prior session in this project's history.
2. **The operator's own copy of the second review's literal cross-check section** (if the
   distinction from R1/R2 in §4 above matters) would close the one honest gap this session leaves.
3. **Q-3 (reciprocal reviewer), Paris in-person attendance, repository visibility, the AI-use
   disclosure placeholder, and the actual OpenReview submission** remain entirely the operator's,
   unchanged from every prior gate.

This session does not submit, does not switch repository visibility, and does not run a third
external review itself, per its own standing instructions.
