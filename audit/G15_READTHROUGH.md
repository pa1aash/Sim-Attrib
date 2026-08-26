# G15 — Ground-up read-through

**Prepared 2026-08-26, session G15, Phase 2.** A complete read of the compiled PDF, start to
finish (abstract through the reproducibility checklist, 22 pages), done before any mechanical
check this session ran, as if seeing the document for the first time — not a targeted grep, not a
checklist pass against prior sessions' own claims. Text read via `pdftotext -layout` against a
freshly compiled, isolated extraction; every figure and every table additionally rendered at
200–400dpi and inspected visually, since G14's own report records that a prose-only or
grep-scoped check has twice missed a real defect this project (the Figure 1 font floor, the
Figure 3(b) annotation dash) that only a direct look at the rendered page caught.

## Finding: Figure 7's legend overlaps its own data (fixed this session)

**The one genuine, previously-uncaught defect this pass found.** `figures/fig6b_nontermination_variants.pdf`
(Appendix A.3, "Figure 7") placed its legend at `loc="lower left"` — directly where the AAA/BBB
studentised curves and their zero-acceptance open-triangle markers pass on their way down to
$p_{\min}\sim10^{-5}$. The legend text "AAA, studentised (primary; main text)" had a data line and
a marker crossing through it. Confirmed in the source figure itself
(`figures/fig6b_nontermination_variants.preview.png`), not a LaTeX compile artifact: the overlap
is baked into the matplotlib figure, independent of `\includegraphics` width.

G14's own P-4 sweep (`GATES.md` G14.14) reported "every other figure (2, 3, 5, 6, 7) … checked at
up to 400dpi: clean." That was wrong for Figure 7 specifically — recorded here plainly, per S8,
rather than silently corrected without note. The likely reason it was missed: G14's sweep was
checking for the class of defect R14-6 and P-4 had already found elsewhere (illegible font,
mid-word hyphenation), not a legend-over-data overlap, which is a different failure mode from
either of those.

**Fixed.** `src/viz/fig6b_nontermination_variants.py` line 91: `ax.legend(loc="lower left", ...)`
changed to `loc="upper right"` — the one region of the plot no series or marker ever reaches
(all four curves collapse well before the axis's right edge). Regenerated
(`figures/fig6b_nontermination_variants.pdf`/`.preview.png`/`.provenance.json`); verified by a
fresh render that no line or marker now crosses the legend box, at any width in the sweep.
Diff confirmed to touch only that one line in the script and the regenerated figure outputs —
no data changed, no other figure touched. Recompiled and re-rendered page 9 of the isolated PDF
directly to confirm: legend clean, main text still ends at page 5, References still start page 6.

## Everything else: read clean, nothing else found

**Prose, start to finish.** Abstract, Introduction, Background, Method, Experiments, Section 5,
Limitations, References, all four appendix subsections, and the full 16-item checklist read for
sense, flow, and internal consistency. No sentence failed to parse; no place found where a
dash-removal rewrite (G14's highest-risk residual, by its own report) appears to have altered
meaning — every rewritten clause reads as a direct, faithful substitution for what a dash would
have joined.

**Figures and tables standing on their own.** Every figure caption re-checked against its own
panel with no other page open: Figures 1–7 and Tables 1–3 all state what they show without
requiring the reader to hold main-text context in their head simultaneously. Table 1 (appendix,
the compact four-findings overview) rewraps at whole-word boundaries only — the mid-word
hyphenation G14 fixed there stayed fixed. Figure 1's value labels (`fig4_assignments`, at
`0.78\linewidth`) are clearly legible at 400dpi, consistent with G14's fix holding.

**Cross-section consistency.** $K=3$ used consistently for the base simulator throughout (never
conflated with the six-column case, which is named "six-column"/"six columns" everywhere, never
"$K=6$") — the K-notation conflict two earlier reviews caught stays resolved. Figure numbering
(1 = eight-assignment bars, 2 = spectrum, 3 = primary nontermination, 4–7 = appendix) is
consistent between in-text `\ref`s, the appendix Table 1's "fig." column, and the actual page
order. Condition-number and Mahalanobis-radius figures repeated across the abstract, Section 4,
Section 5, and the appendix ledger (Appendix A.5) match at every occurrence checked (see also
`audit/R1R2R3_RECONCILIATION.md`'s independent recomputation for the Section 5 numbers
specifically).

**Abstract-to-body consistency, specifically against R-3's current ellipsoid finding.** The
abstract does not state a Mahalanobis radius, an ellipsoid comparison, or a "well inside"/"just
past" characterization of the boundary at all — it says only that the data-implied box is "wider,
on every coordinate, than one already shown to break it" and that "the boundary is predicted
before it is measured … and the prediction holds," both still accurate and unaffected by the
precise radius value. No adjustment needed; checked directly, not assumed from G14's own P-2
finding.

**Anonymization**, read as encountered rather than grepped for: "Anonymous Author(s) / Affiliation
/ Address / email" throughout, no institution, no identifying phrasing anywhere in 22 pages of
extracted text. The one deliberate placeholder (`\answerTODO{}` on the LLM-usage-disclosure
checklist item, with its own explanatory comment in `paper/checklist.tex`) is exactly what prior
sessions established and disclosed; not a new finding.

## Nothing flagged for operator judgment

Per S8, this section is honestly empty this session — every observation above was either already
correct or was fixed outright (the Figure 7 legend), not left as a borderline call. Nothing in
this pass warranted "note but don't fix" treatment.
