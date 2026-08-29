# G23 Phase 2 — document-wide internal cross-reference audit

**Prepared 2026-08-29.** This audit did not exist as a check in any of the twenty-two prior
sessions; G20's restructuring (appendix relocation, Section 2/5 restructuring) moved enough
content that stale pointers could survive undetected by any earlier session's verification
scope, which checked number-tracing and compilation but never "does every pointer to a specific
location still resolve to content actually there." Three such stale pointers were operator-found
on a direct PDF read and fixed in Phase 1 (FIX-1/2/3, `paper/main.tex` and `paper/checklist.tex`,
commit `ea932b2`). This document is the exhaustive follow-up sweep across the entire compiled
document, per the session brief's explicit instruction not to stop at three just because three
were named going in (S9).

## Method

Every internal cross-reference in `paper/main.tex`, `paper/appendix_tables.tex`, and
`paper/checklist.tex` was enumerated by grep, not sampled:

- 39 `\ref{...}` usages
- 20 `\label{...}` definitions
- 9 hardcoded `Section N` / `Sections N--M` textual mentions (checklist.tex uses plain numbers,
  not `\ref`, since it is a separate `\input` file authored against the compiled section
  numbering directly)
- 7 textual `Appendix` mentions (6 paired with `\ref{sec:appendix}`, 1 bare parenthetical in
  checklist item 11)

Each was checked two ways: (1) LaTeX-level — does the reference resolve at all (a two-pass
`pdflatex` compile with zero `undefined reference` warnings, confirmed clean before and after
every edit this session); (2) content-level — does the location the reference resolves to
actually contain what the referencing sentence claims is there, the specific failure mode
FIX-1/2/3 exhibited and that (1) alone cannot catch, since a reference can resolve to a real
label that no longer holds the claimed content.

## Findings

**39 of 39 `\ref` usages: VALID.** Every one resolves to a label defined in the same document
(zero undefined references at every compile this session) and every one's surrounding sentence
was checked against the actual content at that location:

| # | Reference | Location in main.tex | Points to | Content check |
|---|---|---|---|---|
| 1 | `\ref{sec:experiments}` | line 112 | Section 4 | VALID — describes the Montel comparison, run there |
| 2 | `\ref{sec:experiments}` | line 128 | Section 4 | VALID — Cintrón-Arias epidemic model class matches |
| 3 | `\ref{sec:method}` | line 131 | Section 3 | VALID — step-size sweep is Method step 2 |
| 4 | `\ref{sec:negative-result}` | line 137 | Section 5 | VALID — MMC composition is Section 5's subject |
| 5 | `\ref{sec:negative-result}` | line 147 | Section 5 | VALID — same |
| 6 | `\ref{sec:background}` | line 190 | Section 2 | VALID — resolution-vs-spectrum-shape point is stated there |
| 7 | `\ref{tab:thresholds}` | line 199 | Table 3 (appendix) | VALID — table lists exactly the pre-registered thresholds named |
| 8 | `\ref{sec:appendix}` | line 199 | Appendix | VALID — generic appendix pointer, correct |
| 9 | `\ref{fig:simulator}` | line 206 | Figure 4 | VALID — simulator structure figure |
| 10 | `\ref{sec:appendix}` | line 207 | Appendix | VALID |
| 11 | `\ref{fig:assignments}` | line 223 | Figure 1 | VALID — eight-assignment figure |
| 12 | `\ref{tab:sb-eight}` | line 234 | Table 4 | VALID — checked against `appendix_tables.tex` directly: BBB row shows `9.881×`, ABA row shows `1.523×`, matching the referencing sentence's "$9.881\times$ under the base assignment... $1.523\times$ under the tightest one" exactly |
| 13 | `\ref{sec:appendix}` | line 234 | Appendix | VALID |
| 14 | `\ref{sec:negative-result}` | line 238 | Section 5 | VALID — confidence-set rescaling is Section 5's subject |
| 15 | `\ref{fig:spectrum}` | line 254 | Figure 2 | VALID — spectrum figure |
| 16 | `\ref{fig:confound}` | line 259 | Figure 6 | VALID — caption text ("cross-mechanism, naming progression together with observation, with transmission carrying under 5% of the energy in either") matches the referencing sentence verbatim |
| 17 | `\ref{sec:appendix}` | line 259 | Appendix | VALID |
| 18 | `\ref{sec:background}` | line 301 | Section 2 | VALID — Dufour/selective-randomization citations are there |
| 19 | `\ref{fig:nontermination}` | line 313 | Figure 3 | VALID |
| 20 | `\ref{fig:nontermination}` | line 321 | Figure 3 | VALID |
| 21 | `\ref{sec:negative-result}` | line 338 | Section 5 | VALID — self-reference to the cost gate defined in the section the figure sits in |
| 22 | `\ref{fig:nontermination-variants}` | line 340 | Figure 7 | VALID — plain/BBB variants figure |
| 23 | `\ref{sec:appendix}` | line 340 | Appendix | VALID |
| 24 | `\ref{tab:confidence-box}` | line 355 | Table 1 | VALID — table shows half-widths 2.35%–16.63%, matching "2.3% to 16.6%" |
| 25 | `\ref{sec:method}` | line 387 | Section 3 | VALID — scope assumption is Method's opening paragraph |
| 26 | `\ref{sec:method}` | line 391 | Section 3 | VALID — rank-and-condition-number screen is Method's subject |
| 27 | `\ref{tab:summary}` | line 422 | Table 2 | VALID |
| 28 | `\ref{sec:experiments}` | line 424 | Section 4 | VALID — findings 1–2 stated there |
| 29 | `\ref{sec:negative-result}` | line 424 | Section 5 | VALID — findings 3–4 stated there |
| 30 | `\ref{fig:simulator}` | line 454 | Figure 4 | VALID |
| 31 | `\ref{sec:experiments}` | line 456 | Section 4 | VALID — family descriptions are there |
| 32 | `\ref{sec:experiments}` | line 467 | Section 4 | VALID — same |
| 33 | `\ref{tab:thresholds}` | line 471 | Table 3 | VALID — self-reference, correct |
| 34 | `\ref{sec:method}` | line 472 | Section 3 | VALID — thresholds Section 3 uses |
| 35 | `\ref{fig:nontermination}` | line 526 | Figure 3 | VALID |
| 36 | `\ref{sec:experiments}` | line 549 | Section 4 | VALID — comparison-of-Section-4 reference in the (now-pointer-only) claims-ledger paragraph |
| 37 | `\ref{sec:experiments}` (appendix_tables.tex) | line 10 | Section 4 | VALID — plateau-stability detail is stated there |
| 38 | `\ref{fig:nontermination}` (checklist.tex) | line 98 | Figure 3 | VALID — checked against Figure 3's own caption: Wilson intervals are there |
| 39 | `\ref{fig:simulator}` (checklist.tex) | line 181 | Figure 4 | VALID |

**Appendix-subsection structure confirmed A.1–A.5, exactly as FIX-1/2/3 assumed:** Summary of
findings (A.1), Simulator structure (A.2), Supplementary figures (A.3), The eight family
assignments (A.4), Claim-to-source table (A.5) — verified by `\subsection` order in the compiled
source, matching the session brief's premise exactly.

**Checklist — all 16 items read against current paper content** (Phase 2.4), not against memory
of what they used to say:

| Item | Location claim | Status |
|---|---|---|
| 1. Claims | "Section 1... Sections 3–6 establish" the four findings; abstract's closing sentence | VALID — closing sentence is "Every tool used is prior art; the contribution is the finding," present verbatim |
| 2. Limitations | "Section 6" states scope-assumption cost, noise-calibration gap, linearization status, single-simulator scope | VALID — all four map onto Section 6's three bullets |
| 3. Theory | "Section 5, the composition's fixed-selection-rule and reachability conditions" | VALID — Section 5's opening paragraph states exactly this |
| 4. Experimental reproducibility | *(FIX-2, Phase 1)* | FIXED |
| 5. Open access to data/code | OSF URL, excludes internal process record | VALID, unchanged this session |
| 6. Experimental setting | "Sections 3–4... full derivation... in the appendix" | VALID — Table 3 (appendix) carries the derivations |
| 7. Statistical significance | "Figure~\ref{fig:nontermination}" reports Wilson intervals | VALID |
| 8. Compute resources | *(FIX-3, Phase 1)* | FIXED |
| 9–12, 14–15 (ethics, broader impacts, safeguards, licenses, crowdsourcing, IRB) | No internal location references | N/A — nothing to check |
| 13. New assets | "Section 4... Figure~\ref{fig:simulator} (Appendix)" | VALID |
| 16. LLM disclosure | Operator placeholder | Untouched, per standing instruction |

**One additional stale reference found and fixed (beyond FIX-1/2/3):** Table 2 ("Summary of
findings," Appendix A.1) cited figure "**3a**" for the selective-inference-affordable finding.
Figure 3's own caption (`fig:nontermination`) labels its two panels "Left:" and "Right:" — it
never defines a lettered sub-panel "(a)"/"(b)" the way Figure 7 does (whose caption explicitly
says "(a, b) ... (c)"). "3a" therefore implied a panel label that does not exist on the figure a
reader would turn to. Fixed to "**3, left**", matching the figure's own caption language exactly,
no claim or number changed. Recompiled clean, 17 pages preserved.

## Observations (not defects — noted for completeness, no fix applied)

- **`fig:threshold` (Figure 5, "Supplementary figures") is never `\ref`'d from the main text.**
  Every other appendix figure/table is explicitly pointed to from a main-text sentence
  (`fig:simulator`, `tab:thresholds`, `fig:confound`, `fig:nontermination-variants`,
  `tab:sb-eight` all have incoming main-text references); Figure 5 stands alone with only its own
  caption. This is a missing *incoming* pointer, not a broken *outgoing* one — the opposite
  failure mode from FIX-1/2/3 — and fixing it would mean adding a new main-text sentence, a
  content change outside this audit's reference-accuracy scope (S3). Left as-is; flagged for
  operator awareness only.
- **`sec:claims-ledger` (Appendix A.5's own label) is now unreferenced** as a direct consequence
  of FIX-1 (Phase 1) removing the one sentence that pointed to it. The subsection itself still
  exists and is reachable by a reader turning the page; only the explicit main-text pointer is
  gone, by design — FIX-1's brief was correct that the Montel-comparison sentence reads completely
  without it.
- **`docs/THRESHOLDS.md`**, cited by path in Table 3's referencing sentence (main.tex:472), was
  independently confirmed to exist at that exact repository path.

## Total count and verdict

- **39/39** `\ref` usages checked: all resolve, all content-verified against their target — 0
  additional stale pointers among them.
- **20/20** `\label` definitions accounted for (19 in `main.tex`, 1 in `appendix_tables.tex`).
- **16/16** checklist items read against current paper content: 2 were already stale (items 4, 8
  — fixed in Phase 1), 14 check out unchanged.
- **1 additional stale reference** found in this phase (Table 2's "3a" cell) and fixed.

**Total: 4 stale internal cross-references found across this session (3 operator-found and
named going in, 1 found by this audit), all 4 fixed. No further staleness survives a full,
non-sampled enumeration of every internal pointer in the compiled document.**
