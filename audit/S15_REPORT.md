# S15 — Session G15 report

**Prepared 2026-08-26.** This session's mandate: independently re-confirm the second external
review's literal R-1/R-2/R-3 cross-check (the one gap G14's own report left open), then perform a
final, exhaustive, ground-up consistency pass — reading the entire compiled paper as if for the
first time — before a third external review is commissioned. This is the last internal session
before that review.

## 1. THE HEADLINE

**Every item from both external review rounds is now genuinely, independently confirmed closed —
not just reported closed by the session that made the fix.** R-1, R-2, and R-3 (the second
review's own cross-check, distinct from the first review's R1/R2 novelty threat-checks) are each
verified directly against current source: `src/simulators/sir3.py` for R-1's family mechanisms,
current `paper/main.tex` for R-2's ledger reference and undefined-criteria resolution, and a
from-scratch recomputation of R-3's Mahalanobis radii from `results/confidence_set_mmc.yaml` and
`results/boundary_sweep.yaml` — matching the paper's stated 2.71/3.56 to four significant figures.
Full detail in `audit/R1R2R3_RECONCILIATION.md`.

**This session found and fixed four real, previously-uncaught defects that survived fourteen
prior sessions' own verification passes.** None was found by re-checking a prior session's claim
— all four were found by re-deriving from source, which is precisely why they had survived this
long: every prior re-verification pass in this project's history (per its own disclosed
methodology, G13.6/G14.17) worked by diffing against previously-verified numbers, not by
re-reading the compiled document cold or re-computing every claim from its underlying file. This
session did both, per its brief, and that is what surfaced these four:

1. **Figure 7's legend crossed its own data.** `figures/fig6b_nontermination_variants.pdf`
   (Appendix A.3) placed its legend at `loc="lower left"`, directly where the descending AAA/BBB
   curves and their zero-acceptance markers cross. G14's own P-4 sweep reported this figure
   "clean" — for a different defect class (font floors, hyphenation) than this one (legend-over-
   data). Fixed: `loc="upper right"`, the one region no series reaches. No data changed.
2. **Section 4 overstated a margin by ~30×.** "$\kappa$ falls to $344.9$ but stays two orders past
   $\kappa_{\max}=100$" — $344.9/100=3.45$, not $100\times$. Git history shows this imprecision
   predates every review round. Fixed to "$3.4\times$ past," matching the paper's own convention
   of exact multiplicative margins elsewhere.
3. **Section 5 named the wrong box as "known to break the composition."** "every one wider than
   the $\pm0.5\%$ box already known to break the composition" directly contradicts the same
   section's own later statement (independently re-verified against `boundary_sweep.yaml` in this
   session's Phase 1) that $\pm0.5\%$ is the **last fully-passing** box and $\pm0.75\%$ is what
   **first fails**. A real, four-sentence-apart, same-section contradiction — exactly the class of
   defect a full read-through catches and a targeted grep does not. Fixed to name $\pm0.75\%$.
4. **Three stale provenance flags.** `figures/fig3_spectrum.provenance.json` and
   `figures/fig6_nontermination.provenance.json` each carried `dirty: true` since separate G14
   sessions (the R14-6 fix and the mid-session connectivity-interrupted dash fix respectively),
   each regenerated mid-edit and never re-generated from a clean tree afterward — silently undoing
   a discipline session G3 established and a sibling commit had already applied to `fig3_spectrum`
   once before. A third, `figures/fig6b_nontermination_variants.provenance.json`, was this
   session's own oversight: Phase 2's legend fix was committed correctly but never followed by the
   second clean-tree regeneration that records the flag clean. Found only because this session
   actually re-ran the full pytest suite (176/177 passed on first run) rather than assuming G14's
   report of a clean suite still held. Confirmed content-harmless in all three — pixel-identical
   regenerations, verified by both `pdftotext` diff and a full pixel-difference bounding-box
   check, both empty — and fixed as the last step of this session, from a genuinely clean tree
   each time. Full suite re-run clean afterward (177 passed).

**None of the four is catastrophic**, and the paper's substantive findings, numbers, and argument
are unchanged by all four fixes combined. But three are exactly the class of small, load-bearing
imprecision an external reviewer specifically reads a paper to find, and this session's mandate
was explicit that "if this pass finds ANYTHING wrong — however small — report it exactly as
found" (S8). It is reported that way here, not folded into a summary that undersells it.

**Final page count: exactly 22 total pages; main text (Abstract–Limitations) 5 pages, References
starting page 6** — unchanged by every fix this session made, re-confirmed by direct page render
after each edit round, not estimated.

**Both isolation tiers pass clean against the final package** (`build/sim_attrib_overleaf_19f9a59.zip`):
§2b (OVERLEAF-EQUIVALENT) exit 0, 22 pages, zero undefined references/citations; §2a (this-machine
`TEXMFHOME`-unset sense) exit 0, same narrow caveat as every prior gate.

## 2. R-1/R-2/R-3, IN FULL

See `audit/R1R2R3_RECONCILIATION.md` for the complete, independently-derived verification of all
three items, including the exact main-text locations checked and (for R-3) the full recomputation
with its eigenvalue cross-check. Summary: all three **CONFIRMED FIXED**, closing the one gap
G14's own report left open.

## 3. THE FOUR DEFECTS, WHY THEY SURVIVED, AND WHAT THAT SAYS ABOUT THIS PROJECT'S PROCESS

Three of the four were content defects (Figure 7's legend, and the two Section 5 numeric/logical
errors); one was a process defect (the stale provenance flag). All four share a common cause:
**every one of them was invisible to a diff-based re-verification against a prior session's own
already-checked claims**, because none of them was ever flagged as "checked and correct" by any
prior session — they were simply never independently re-derived. G13.6 and G14.17 both explicitly
disclosed using a diff-based method for numbers *not* touched by their own session's edits, which
is a defensible efficiency choice for genuinely unchanged content, but it cannot catch an error
that was present from the moment a number or figure was first written and never independently
re-checked since. This session's Phase 2 (full read) and Phase 3 (full re-derivation, not a diff)
are what caught three of the four; Phase 4's full pytest re-run (rather than assuming G14's own
report of "the test suite still passes" — a claim G14 never actually made explicitly, but which
this project's own process could easily have assumed) caught the fourth.

**This is not a criticism of any single prior session.** Each of G0 through G14 operated under its
own scope and its own disclosed methodology, and each was honest about what it did and did not
re-derive from scratch. It is, however, a concrete demonstration of why this project's own
standing instruction (S6: do not trust prior sessions' own verification claims without
re-checking) exists, and why a session explicitly scoped to full re-derivation — this one — was
worth running before a third external review, rather than another targeted pass.

## 4. WHAT SHOULD HAPPEN NEXT

1. **The third external review is ready to be commissioned.** Every item from both prior review
   rounds is independently confirmed closed; this session's own full re-derivation found and fixed
   four further real defects. This is the strongest state this document has been in across fifteen
   sessions.
2. **This session's own "does not certify" section (`GATES.md` G15) should be read before
   commissioning that review** — in particular, that this session's methods, however more thorough
   than prior sessions', are not a guarantee the document is now free of every possible defect.
3. **Q-3 (reciprocal reviewer), Paris in-person attendance, repository visibility, the AI-use
   disclosure placeholder, and the actual OpenReview submission** remain entirely the operator's,
   unchanged from every prior gate.

This session does not submit, does not switch repository visibility, and does not run a third
external review itself, per its own standing instructions.
