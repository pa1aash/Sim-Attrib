# S12 — Session G12 report

**Prepared 2026-08-25.** This session's mandate: close everything remaining before a second
external review — the page-limit overflow, the two Tier-2 findings G11 lost to context
compaction (T2-4, T2-6), and a conscious re-sign of G10 given the `TEXINPUTS` defect G11 found
in its own verification method.

## 1. THE HEADLINE

**T2-4 and T2-6 are both closed, and the honest story for each is different from what the
session brief assumed going in.** T2-6 turned out to be **already substantially applied** by
G11 before its own context compaction hit — this session's job there was mostly verification,
not drafting, with one real gap found and closed. T2-4 required a genuine second compute run,
which this session ran twice: once contaminated by its own mistake, once clean.

**Twelve sessions in, this project's twelfth-session complete checklist against the external
review, in one place, for the first time:**

| Tier | Item | Status |
|---|---|---|
| T1 | T1-1 through T1-6 | All six fixed and verified (G11) |
| T2 | T2-1, T2-2, T2-3, T2-5, T2-7 through T2-15 (13 items) | All fixed and verified (G11) |
| T2 | **T2-4** | **Fixed this session** — real second-θ test run, separability reproduces |
| T2 | **T2-6** | **Fixed** — found mostly applied by G11; one apologetic-framing instance and the strengthened-result incorporation closed this session |

**All 6 Tier-1 and all 15 Tier-2 findings from the external review are now addressed.** This is
the first session in this project's history that can say so.

**The page limit is narrower than it has ever been, and it is still not closed.** Six pages of
body content against Sim2Science's five-page limit — the same raw count G9, G11, and this
session all report — but the composition of that sixth page has changed materially: it used to
carry a full paragraph of Section 5's own prose plus Figure 4 plus the Limitations section; it
now carries only Figure 4 and Limitations. §4 below has the full accounting, including exactly
which levers were pulled and which were not.

**This session's own re-verification (Phase 4) found one more defect of the same class G11
found, disclosed at the same length, and confirmed it does not change anything that matters for
submission.** §3.

**G10, which has never had a gate entry in this project's history, has one now** — written
retroactively, honestly labeled as such, proposing exactly the amendment the session brief asked
for. §5.

## 2. T2-4 AND T2-6 — WHAT THEY ACTUALLY REQUIRED, AND WHAT THIS SESSION FOUND

### T2-6 — mostly already done, and here is exactly how it was checked rather than assumed

The session brief carried an explicit warning: T2-6 might be partially applied inside G11 before
compaction hit, and a fresh drafting pass should not be attempted blind. Reading Section 5 and
the Limitations section as they stood at the start of this session, against the external
review's original four-part instruction:

1. **Retitle to lead with the finding.** Already done — "Where exact conditional attribution
   becomes unaffordable, and why" is the current title, not the caveat-first title the review
   was responding to.
2. **Move the predicted-before-measured sentence to the first paragraph.** Already done — it is
   the second sentence of Section 5's opening paragraph.
3. **Fix apologetic framing in at least 4 locations.** Three of the four named instances were
   already fixed (the title itself; the opening sentence, now finding-focused rather than
   conservativeness-focused; "we evaluate this construction on our own simulator rather than
   propose it," now "we measure the composition against our own simulator"). The fourth —
   Limitations bullet 2's original framing — was less clearly resolved and is the one instance
   this session can take credit for, tightened from "The diagnostic is prior art, local, and
   single-point" (leads with a novelty concession) to "The diagnostic is prior art and a local
   linearization" (states the fact without leading with the concession), and this session found
   one further redundant instance of the same pattern in Background's composite-null bullet
   ("we cite both as established and evaluate the composition, rather than propose either as
   new") and cut it during the page-limit pass, both for space and because a fifth redundant
   restatement of the same disclaimer was not adding anything the abstract and Section 5 do not
   already say once each.
4. **Reconcile the 8.4-vs-27-65 figure discrepancy.** Already resolved, and by a mechanism this
   session had to trace rather than assume: G11's own T2-8 fix redesigned `fig6_nontermination`
   from a single panel carrying "a secondary top axis for the shift-to-noise ratio" into two
   separate panels, and in the same pass the raw per-coordinate z-score figure (median 27, up to
   65 standard deviations — the number `docs/DECISIONS.md` D-16 originally quoted) was dropped
   from the main-text prose entirely. What remains, in the figure's right panel and nowhere else
   in numeric form, is a different statistic: the Euclidean-norm-based shift-to-noise ratio
   (`nuisance_shift_norm_of_mean_z.median_over_noise` in `results/boundary_sweep.yaml`), which
   tops out at `8.39` at the widest measured half-width — the "8.4" the external review's T2-6
   finding was written against, before G11's own T2-8 redesign moved it into its own panel. The
   two numbers measure genuinely different things (a per-coordinate raw z-score versus a
   vector-norm ratio normalized by `√d`), and the paper now states only the more informative one
   (the ratio, because it is what directly explains where the gate stops passing), consistently,
   which satisfies the review's own "report the more informative number consistently" option
   without needing the "explain why both appear" alternative.

**The one substantive addition this session made beyond verification**: incorporating the
Dufour confidence-set result as **primary** evidence was itself already done by G11 (Section 5's
opening paragraph leads with the data-implied box, and the original `±5%` sweep is explicitly
demoted to "below" / secondary). This session confirmed that framing against
`audit/DUFOUR_CONFIDENCE_SET_CHECK.md` §4's own instruction and found it already matched.

### T2-4 — the real test, run twice

The second-θ test needed a prior range that did not exist anywhere in this project's records
(`docs/THRESHOLDS.md` has bounds for the MLE optimizer, not a prior over `θ`). This session
pre-registered one before drawing anything: independent `±20%` relative perturbation per
coordinate (`β, γ, ρ, I₀, σ_obs`), a factor of two wider than `ETA_SCALE` (the paper's own
"one normalised unit"), and wider than every coordinate of the data-implied 95% confidence box
G11 measured (2.3%–16.6% half-width) — wide enough to be a real second point, not a restatement
of the fit's own uncertainty. `src/diagnostics/second_theta_check.py`, committed before any draw
was taken, matching this project's own commit-then-run discipline for every prior diagnostic
script.

**The first run was thrown away, and the reason is disclosed rather than smoothed over.** This
session edited `paper/main.tex` (the page-limit pass) while the diagnostic ran in the
background, which — per `header()`'s own tracked-file check — recorded `dirty: true` on the
result even though the code that actually ran was unaffected by that edit. This is precisely the
failure `DEVIATIONS.md` D-8 and D-9 exist to name, and it recurred in a session that had read
both before writing any code, the same way it recurred for G4 one session after G3's version of
it. The fix was the same one those entries prescribe: stash the paper edit, re-run from a
genuinely clean tree, and only then restore the paper edit. The re-run reproduced the discarded
run's numbers exactly (`κ=10.917` at `θ₂`, `κ=10.074` at `θ₀` under the identical harness, both
times), which is a useful secondary confirmation that the computation itself is deterministic
and correct — the only thing wrong with the first attempt was its provenance record, not its
arithmetic.

**Result: `S_B` separates at `θ₂`** (full column rank, all three singular values resolved,
`κ=10.9`), **matching `θ₀`'s own verdict computed through the identical harness** (`κ=10.1`).
The paper's Limitations section now states this plainly, with the caveat the session brief
itself anticipated: one additional point is not a distribution over `θ`, and this does not
establish separability holds everywhere — it establishes that the verdict survived the one
honest check available within this session's scope.

## 3. PHASE 4 — WHAT THIS SESSION'S OWN VERIFICATION FOUND

Applying S6's standing instruction — treat this project's own tooling with suspicion until
proven otherwise, specifically for the same failure class G11 found — to G11's own work rather
than assuming a clean bill of health:

1. **The `TEXINPUTS` fix re-verifies clean, with no regression.** Rebuilt the package from this
   session's own final commit, re-ran both isolation tiers with `TEXINPUTS` unset: exit 0,
   byte-identical `main.pdf` between the repo working copy and a fresh isolated extraction.

2. **A second, lower-severity defect of the same class, in the tier G11's own report already
   flagged as suspicious but did not chase down.** G11 wrote, about the "STRICT isolation"
   tier's mysterious pass: *"Whatever closed that gap between sessions is a local-machine TeX
   Live state change, not a change this session made to the package's contents — recorded here
   as observed, not further chased."* This session chased it. `TEXMFHOME` "unset" does not mean
   "no personal package tree" to kpathsea — it falls back to its own configured default, which
   on this machine is `~/Library/texmf`, an ordinary personal TeX install unrelated to this
   project, which happens to carry local installs of exactly the five packages (`environ`,
   `enumitem`, `trimspaces`, `units`/`nicefrac`, the `phvr8t.tfm` Helvetica metric) G10's own
   original report recorded as missing. Verified directly: pointing `TEXMFHOME` at a genuinely
   empty directory reproduces G10's original failure on this exact rebuilt package,
   `! LaTeX Error: File 'environ.sty' not found.`. **This does not change the
   submission-readiness verdict** — the tier the project actually gates on sets `TEXMFHOME`
   explicitly to a real package tree (a defensible proxy for Overleaf's own full TeX Live
   distribution, which has these standard packages natively) rather than unsetting it, and that
   tier re-verifies clean, byte-for-byte. Full detail, `audit/OVERLEAF_PACKAGE_REPORT.md` §0c.

3. **`audit/FINAL_CLAIMS.md` was missing the C5 section its own referenced document said it
   would add.** `audit/DUFOUR_CONFIDENCE_SET_CHECK.md` §4 states plainly that the confidence-set
   check "adds a fifth claim section (C5) to `audit/FINAL_CLAIMS.md`'s numbering" — and no
   session ever actually wrote it, a real instance of the "a file that documents what should be
   true is not the same as the file being true" pattern this project has now found four times
   (`DEVIATIONS.md` D-18 names the first three). Closed this session, framed explicitly as
   evidentiary strengthening of contribution 4 rather than a fifth contribution, since `D-16`
   closes the paper's scope at four and no session may widen that without a new decision there.

4. **`audit/OVERLEAF_PACKAGE_REPORT.md`'s own page-count table was stale**, describing an
   ordering (checklist before references and appendix) that T2-14 changed in G11 and that no
   session had re-checked the table against since. Corrected against a fresh compile.

Beyond these four, this session confirms clean without further findings:

- **The full test suite**, re-run after this session's own edits: 177 passed, unchanged.
- **This session's own new numbers** (`κ=10.9`, `κ=10.1`) traced directly to
  `results/second_theta_check.yaml`.
- **A token-level diff of every number touched by the page-limit commit**, confirming none was
  altered in value during the wording trims — each evidentiary number (`344.9`, `31.9`, `8.0`,
  `2.80`, etc.) appears in matched removed/added pairs, meaning it was reformatted, not changed.

## 4. THE PAGE LIMIT — THE HONEST ACCOUNTING

Six pages of body content against a five-page limit, unchanged in raw count from G9 and G11's
end states, but the composition of the overflow has changed. Before this session's pass, page 6
carried: the tail of Section 5's second paragraph, Figure 4, and the full Limitations section.
After: Figure 4 and Limitations only — Section 5's own prose now fits entirely within page 5.

**What was cut, all disclosed as levers rather than hidden as a single diff.** Related Work
prose tightened (every T2-5 citation and its specific engagement point kept — this session did
not remove a single citation or weaken an engagement, only trimmed the connective framing around
them); several other phrase-level cuts in the Method and Experiments sections, chosen to remove
redundant wording rather than any evidentiary number or qualifier; tighter inter-float spacing
(`\textfloatsep`, `\floatsep`, `\intextsep`, pure whitespace, no font-size or content effect);
and two `\includegraphics` width reductions (`fig2_simulator`, `fig6_nontermination`, both
1.0→0.92 of `\linewidth`).

**The figure-width reductions were verified safe by measurement, not by reasoning about ratios
alone — G9's own report records a fourth-round figure-legibility attempt as the reason it
stopped short of closing the page, and G11 tried and reverted a similar cut for the same
reason.** Both figures reduced this session use `style.SIZE_LABEL` (8pt) as their smallest text
size at their full design width, giving real headroom above the venue's 6pt floor — unlike
`fig3_spectrum` and `fig4_assignments`, which G11 already established have none (their smallest
text is `style.SIZE_TICK`, 7pt, already close to the floor at their current display width). This
session rendered the compiled pages at 300dpi after each width change and read the smallest
rendered text directly, rather than trusting the ratio arithmetic alone, before committing
either change.

**What was not cut, and why.** Figure 4 plus the complete three-bullet Limitations section is
roughly four-fifths of a page on its own, and page 5 is already full edge-to-edge with Section
5's own two paragraphs after every safe cut available. Fitting both onto page 5 would require
one of: cutting real content (a whole bullet, or Figure 4's own substance), a bigger
figure-width reduction than the two already taken (risking the same font-floor violation G9 and
G11 both declined), or restructuring — moving Figure 4 to the appendix, which would relocate the
paper's own central evidence out of the main text a reader would actually read. None of these is
taken unilaterally this session, for the same reason G9 and G11 both gave: the operator should
make that tradeoff, not a session acting alone.

## 5. WHAT SHOULD HAPPEN NEXT

1. **Decide whether six pages is acceptable for submission**, or whether closing the last page
   is worth one of the three remaining levers (a real content cut, a riskier figure reduction, or
   restructuring), or accepting the overage and disclosing it — `audit/VENUE.md` still does not
   establish Sim2Science's own enforcement strictness on this point.
2. **Consider a second external review** against G11's and this session's combined fixes. All 6
   Tier-1 and all 15 Tier-2 findings from the original review are now addressed for the first
   time in this project's history; whether that upgrades the Weak Reject verdict has not been
   tested by anyone outside this project.
3. **Sign or reject G10 and G12.** Both are `status: ready for review — UNSIGNED`.
4. **Q-3 (reciprocal reviewer), Paris in-person attendance, repository visibility, OpenReview
   submission** — all still the operator's, unchanged from every prior session.

## 6. PROCESS CAVEATS — WHAT THIS SESSION DID BADLY OR NOT AT ALL

- **The first T2-4 run was contaminated by this session's own concurrent edit to
  `paper/main.tex`**, recorded and discarded rather than kept, but it should not have happened —
  the tree-edit-while-a-run-is-in-flight failure has now recurred in G3, G4, and this session,
  three separate times across this project's history, despite each occurrence being read by the
  session that then repeated it.
- **The full ~150+-item number trace was not re-run from scratch.** This session's own additions
  were independently verified and a token-level diff confirms no accidental alteration during
  the page-limit pass, but everything G11 already verified is relied on rather than
  re-derived — disclosed here rather than claimed as freshly exhaustive.
- **The page limit is not closed.** Narrowed materially, for the third session running, and
  still not five pages.
- **No second external review has been commissioned or run.** Twelfth session, same gap.
- **Google Scholar still not searched.** Twelfth session with code. **O-7**, unchanged since G0.

## 7. POINTS REQUIRING OPERATOR INPUT

- **P-1.** G12 sign-off, after reading the recompiled PDF directly.
- **P-2.** G10's proposed re-sign amendment — review and sign if satisfied.
- **P-3.** Whether to run the second external Fable 5 review now, or make further manual edits
  (most plausibly, a decision on the page limit) first.
- **P-4 (carried).** Q-3, Paris in-person attendance, repository visibility switch, OpenReview
  submission.

## 8. THE ONE-PARAGRAPH VERSION

Both findings G11 lost to context compaction are closed, and for different reasons: T2-6 turned
out to be almost entirely already applied before the compaction hit, verified rather than
redrafted, with one real gap closed; T2-4 required and got a genuine second compute run, thrown
away once for a provenance mistake this session caught in itself and re-run clean. All 6 Tier-1
and all 15 Tier-2 findings from the external review are now addressed, for the first time in
this project's twelve-session history. The page limit is narrower than it has ever been and
still not closed, for the same disclosed reason G9 and G11 both stopped short. This session's
own re-verification, held to the same standard of suspicion it applied to G10's inherited
tooling, found one more defect of the same class — disclosed at the same length, confirmed not
to change the submission-readiness verdict. G10 has a gate entry for the first time. Status:
ready for review, unsigned, not submitted, repository visibility unchanged.
