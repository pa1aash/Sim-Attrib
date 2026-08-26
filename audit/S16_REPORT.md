# S16 — Session G16 report

**Prepared 2026-08-26.** This session's mandate: close a third independent external review's
two real findings and nine smaller ones, with the highest priority on actually running the
Anau Montel et al. (2025) comparison Section 2 had previously asserted rather than measured;
then build a safe, working, anonymized public reproducibility package. Full detail in
`GATES.md` G16; this is the summary a reader should start from.

## The Montel comparison's actual result, leading

`src/baselines/montel_marginal.py` implements Anau Montel, Alvey & Weniger (2025)'s Section
II.3 trials-corrected minimum-per-summary-statistic global-null test, run against this
project's own simulator (`src/simulators/sir3.py`), not a toy example. The one stated
simplification: an exact per-summary test statistic in place of their neural local tests,
since this project's summaries admit a direct Monte Carlo null and never needed the amortised
density-ratio machinery their general SBI setting requires in the first place. The
trials-corrected aggregation itself — the actual object W16-2 asked about — is implemented
exactly as they construct it.

**Measured, not asserted:** the global test correctly rejects $H_0$ at both declared corners
(BBB, AAA) and at two finite-magnitude realizations of the six-column confound's own named
mechanisms — "a drifting removal hazard" and "a constant hazard change combined with a
drifting reporting rate" (`audit/FINAL_CLAIMS.md` C3) — at $p\approx0.004$ each (resolution-
limited by a 3,000-draw reference batch; every reported $p$-value is an honest upper bound,
not a point estimate). A null-data control correctly does **not** reject ($p=0.61$) — the S5
vacuous-flag test, applied to the test's own calibration machinery, passing explicitly.

**The arg-min result reverses the paper's prior unmeasured claim.** Section 2 previously
asserted, without running anything, that the arg-min "would flag on both sides rather than
resolve" the six-column equivalence-class ambiguity. Measured: the two confound mechanisms'
arg-min summary coordinates are **disjoint** (`binned_incidence_01` vs. `binned_incidence_02`,
near-min coordinate sets with zero Jaccard overlap) at this magnitude. Section 2 is rewritten
to report this, with the caveat the finding itself demands: one realization per mechanism is a
measurement, not a distribution over them, and a marginal test's finite-magnitude power is a
separate question from the Jacobian's local ($\eta=0$) near-null identifiability the rest of
the paper establishes. Full numbers: `results/montel_marginal_test.yaml`.

## The anonymized package

Built (`scripts/build_anonymous_package.sh`), verified safe, and verified to actually work —
all three, not asserted. Full contents list and exclusion checklist in `GATES.md` G16. The one
finding worth restating here: **every `results/*.yaml` file leaked the operator's hostname and
a private commit hash under two different field names each** (`host`/`measured_on`,
`commit`/`p_sel_run_commit`), found by grepping the operator's own name across every file
rather than trusting a hand-enumerated key list. The package's redaction is value-based (any
40-hex-character line, any line naming the operator) specifically because a key-based list
already proved incomplete once. Independently re-scanned after building: zero hits for the
operator's name, GitHub username, email, or any AI-authorship token across all 91 packaged
files, and zero `.git*` paths. Extracted fresh into an isolated directory, dependencies
installed from `requirements.txt`, and the test suite run: 164 pass; 7 documented, non-
blocking exclusions (6 need the paper's venue template, correctly not bundled; 1 asserts a
git commit that a package with no git history cannot have). The repository's own `LICENSE`
could not be reused verbatim as the session brief literally suggested, because it has the
operator's real name filled into the copyright line — caught and replaced with the canonical
MIT template's anonymized form before packaging, not after.

Not done, and not this session's to do: uploading the zip anywhere, or pasting the resulting
URL over the placeholder left at `paper/checklist.tex` item 5.

## Page count

Main text (Introduction through Limitations) is exactly 5 pages; References begins on page 6.
Confirmed by parsing the compiled PDF's own page breaks (`pdftotext`), not by eyeballing a page
counter. Getting there required tightening the same whitespace levers G12–G14 already used
(`\parskip`, float/caption separations) by a further small amount, plus trimming a handful of
non-load-bearing connective sentences (e.g. "We measure the composition against our own
simulator.") — no numeric result, citation, or caveat was cut to make room. Full PDF: 23 pages
including appendix, checklist, and references.

## Tier-2 items, briefly (full table in `GATES.md` G16)

W16-1 confirmed unchanged (operator's, per standing instruction). W16-3: the coherence and
column-norm thresholds were genuinely computed and clean on all eight assignments; stated
explicitly in Section 4 rather than left as unexplained appendix entries. W16-4: the orphaned
random-attributor-floor sentence and its ledger rows removed from main-text prose (the
underlying `results/floor_check.yaml` stays as historical record). W16-5: the second-theta
check now has a ledger entry (`L1`). W16-6: "two orders of magnitude" softened to
"approximately." W16-7: the PASSES/FAILS inline labels removed from Figure 3's plotting code;
the same framing now lives in the caption. W16-8: Wilson intervals added to Figure 7 (the
underlying replicate data already supported it); the caption's "generally sooner" claim
replaced with the actual crossing widths, which contradict it for one of the three non-primary
combinations. W16-9: $d$ defined in Section 3. W16-10: Fithian/Sun/Taylor and Lee/Sun/Sun/
Taylor cited in Section 2, both already correctly in `audit/BIBLIOGRAPHY.bib` from an earlier
session and re-verified against arXiv's own record before reuse. W16-11: the "every tool is
prior art" aphorism kept once, with force, in the abstract; trimmed from Section 1, both
Section 2 instances, and checklist item 1.

## What this report does not certify

Everything `GATES.md` G16's own "does not certify" section states, restated because it is the
part most likely to be skipped: no fourth external review has run on this version; the
Montel-comparison's confound-resolution finding is one realization per mechanism, not a
distribution; and the anonymization redaction is evidence-based from what this session
actually found, not a claim that every identifying field in every file has been enumerated.

## Honest process caveats

This session's own commits are coarser-grained than the brief's suggested five-way Tier-2
split — two commits (code, then a clean-tree data regeneration) rather than five, the same
split G3 established for exactly this reason. The Montel comparison's batch sizes were reduced
partway through (`N_ref`/`N_calib` from 5,000/5,000/2,000 to 3,000/3,000/1,500) because this
machine's load average reached 159 during the session, confirmed via `uptime`, not assumed;
the reduction changes reported $p$-value *resolution*, not validity. A real reproducibility bug
— Python's randomised `hash()` used to seed one case's observed-data draw, which would have
made the Montel numbers silently non-reproducible run to run — was caught by re-reading the
module before the production run, not after. No adversarial critic or second independent agent
ran against this session's own findings; every check above is this session's own re-derivation,
the same limitation every gate before it names about itself.

**Status: `GATES.md` G16 is `ready for review — UNSIGNED`.** Points requiring operator input
are collected, not resolved, at the end of the session brief (P-1 through P-4) and are
unchanged by anything in this report.
