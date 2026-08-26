# G15 — Exhaustive number-trace (S4)

**Prepared 2026-08-26, session G15, Phase 3.** Every distinct number appearing in the compiled
PDF's main text, figure captions, tables, and appendix, checked against its source: either the
generated ledger at Appendix A.5 (`paper/appendix_claims_table.tex`, produced by
`src/diagnostics/report_claims.py` from `results/*.yaml`, never hand-typed — G3.19), a
`results/*.yaml` file directly, or (for the small set of non-empirical constants) flagged as
such explicitly rather than silently skipped.

This pass is exhaustive over distinct numeric claims, not a sample: every number in the abstract,
Sections 1–6, Figure 1–3's captions (main text), the Limitations bullets, and every row of
Appendix A.1–A.5 and the checklist was read and matched. Numbers that repeat verbatim across
sections (e.g. $\kappa=628.9$ in both the abstract and Section 4) are counted once per location
they appear, since each occurrence is a separate opportunity for drift.

## Two genuine defects found and fixed

Both surfaced during this pass, not before it — neither was flagged by any prior session's own
number-trace, which (per G13.6/G14.17, disclosed at the time) worked by diffing against
previously-verified numbers rather than re-deriving the full text fresh each session. This
session's Phase 2/3 combination — a full read *plus* a full re-derivation — is what caught them.

**1. Section 4: "stays two orders past $\kappa_{\max}=100$" for $\kappa=344.9$.** $344.9/100 =
3.45$, not two orders of magnitude ($100\times$). Checked against the correctly-used instance of
the same phrase in Section 5 ("$9.9\times10^9$ draws... two orders of magnitude over budget" —
$9.9\times10^9/10^8=99\approx100\times$, correct) to confirm this was not a stylistic convention
this paper uses loosely. Git history shows the phrase (in a slightly different form, "two orders
of magnitude") attached to this same $344.9$-vs-$100$ comparison as far back as the
result's first appearance in the draft — an error that predates every review round, not something
this session's own dash-removal or compression passes introduced. **Fixed**: `paper/main.tex`,
"stays two orders past" → "stays $3.4\times$ past" ($344.9/100=3.449$, matching the paper's own
convention elsewhere of stating exact multiplicative margins, e.g. "$9.881\times$", "$0.9\%$ past
the ceiling").

**2. Section 5: "every one wider than the $\pm0.5\%$ box already known to break the
composition."** This directly contradicts the same section's own later, more precise statement —
independently re-verified against `results/boundary_sweep.yaml` in this session's Phase 1
(`audit/R1R2R3_RECONCILIATION.md`) — that $\pm0.5\%$ is the **last fully-passing** box (`verdict:
PASS` at every corner) and $\pm0.75\%$ is the box at which the gate **first fails** (`verdict:
SPLIT`). The two paragraphs, four sentences apart in the same section, named different boxes for
the same event. **Fixed**: `paper/main.tex`, "$\pm0.5\%$ box already known to break the
composition" → "$\pm0.75\%$ box already known to break the composition" — the referent the data
actually supports, and the fix that keeps the paragraph's own logic intact (every data-implied
half-width, $2.3\%$ to $16.6\%$, is still wider than $0.75\%$, so the *a fortiori* argument the
sentence makes still holds).

Both are load-bearing prose in Section 5, the section a third external reviewer is most likely to
scrutinize closely given R-3's history across two review rounds. Both predate this session (git
history confirms the first; the second was introduced whenever the precise $\pm0.75\%$/$\pm0.5\%$
boundary language was added and never reconciled against the earlier paragraph). Recorded here in
full per S8, not folded quietly into a "numbers checked" count.

Both fixes verified: recompiled (exit 0, no undefined references), page count re-confirmed at 22
total / 5 main-text pages, and page 4 re-rendered at 250dpi to confirm the corrected sentences sit
cleanly with no reflow issue.

## Everything else: traced clean

**Abstract** (2 distinct numbers: $\kappa=628.9$, rank 4 of 6) — both trace to
`robustness/k6_spectrum.yaml` via Appendix A.5's C3 rows.

**Section 3 (Method)** — $\tau=10^{-2}$, $\kappa_{\max}=100$, resolution factor 2, equivalence-class
threshold 0.3: all four trace to `jacobian_rank.S_B.yaml`'s `thresholds_pre_registered` block via
Appendix A.5's C1 rows. The two-component ($\approx0.707$) and three-component ($\approx0.577$)
confound values are exact mathematical constants ($1/\sqrt2$, $1/\sqrt3$), not measurements —
correctly not ledger entries; their correctness is checkable by arithmetic alone, not empirical
provenance.

**Section 4 (Experiments)** — every number checked: the random-attributor floor
(0.3333/0.3299), the eight-assignment $\kappa$ range (6.628–65.64), $S_A$'s knife-edge failure
(100.9, "0.9% past the ceiling" — simple derived arithmetic from the traced 100.9 and 100), the
$\tau^*$ margins (9.881$\times$/1.523$\times$), the MLE-SE-based rescaling ($\kappa=31.9$, $8.0$,
both separable), the six-column result ($\kappa=628.9$, rank 4/6), the plateau/threshold/
structural checks (1.023 vs. admissible 2; $\tau$ from 0.005 to 1.0; $d=10\ge6$), the
near-null-direction transmission energies (both under 5%), and the data-motivated six-column
scaling ($\kappa=344.9$, rank 5/6) — all trace directly to Appendix A.5's C1–C3 rows.

The "$0.9$–$2.7\%$" SE-scaling figure (cited from Section 5 but stated in Section 4) does **not**
appear as a single ledger row under that literal phrasing, so it was independently recomputed
rather than assumed: `results/confidence_set_mmc.yaml`'s stored standard errors divided by the
corresponding MLE point estimates give $\mathrm{se}_\beta/\hat\beta=0.9116\%$,
$\mathrm{se}_\gamma/\hat\gamma=2.7115\%$, $\mathrm{se}_\rho/\hat\rho=2.3518\%$ — range $0.91\%$ to
$2.71\%$, matching the stated "$0.9$–$2.7\%$" exactly. Cross-checked a second way, against
`results/robustness/alt_eta_scaling.yaml`'s stored `per_column_relative_scale` values (which store
the same ratio *as a multiple of the flat 10% convention* — $10\times$ the raw percentage — per
G14's own disclosed footnote in `S14_REPORT.md` §headline): dividing those by 10 reproduces the
identical $0.91\%/2.71\%/2.35\%$ figures. Both independent routes agree; no discrepancy.

$K=3$, the "10%" ETA_SCALE convention, $S_B$'s "roughly ten" and $S_A$'s "four" summaries, and
$S_C$'s "two summaries" are simulator/summary-set **design choices** stated in `src/simulators/`
and `src/diagnostics/p_sel.py` (confirmed present in code, not fabricated), not empirical
measurements — correctly outside the ledger's scope, which its own text states is for "the main
text's four contributions," i.e. results, not experimental design parameters.

**Section 5** — every number besides the two fixed above traces cleanly: worst-cell $p=23\%$,
per-test cost range ($4.2\times10^5$–$4.3\times10^7$), the $10^8$ gate, the data-implied
half-width range ($2.3\%$–$16.6\%$), the four-corner failure and $9.9\times10^9$-draw cost, the
slope-ratio (2.265$\times$ against threshold 3), the decades-per-half-width figure (one decade per
$0.7\%$, derived from the ledger's $-141.2$ decades-per-unit-half-width: $1/1.412 \approx 0.71\%$
per decade), $R^2=0.94$, and the Mahalanobis radii (2.71/3.56) and ellipsoid radius ($\approx3.33$)
— the last three independently recomputed from scratch in Phase 1
(`audit/R1R2R3_RECONCILIATION.md`), not merely re-checked against the ledger.

**Limitations** — $\kappa=10.9$ (second $\theta$, $\pm20\%$ relative draw) traces to
`results/second_theta_check.yaml`'s `condition_number: 10.916964...` and `rank_certain: 3`
(full rank); $\kappa=10.1$ (the harness's own $\theta_0$ verdict for comparison) traces to
`robustness/k6_spectrum.yaml`'s `summary_sets.S_B.base.condition_number: 10.12`. Neither appears
in the Appendix A.5 ledger (which is explicitly scoped to the four main findings plus the
confidence-set check, not every robustness check in `results/`) but both trace directly to a
named `results/*.yaml` file and field, satisfying S4 on its own terms.

**Appendix A.1 (Table 1)** — all four rows restate numbers already traced above (main text is
their source, per the table's own caption: "adds no claim not already in the main text").

**Appendix A.4 (Tables 2–3)** — `paper/appendix_tables.tex` is generated programmatically from
`results/robustness/k6_spectrum.yaml` (confirmed by the file's own header comment; not
hand-typed), covering all 16 $\kappa$ values (8 for $S_B$, 8 for $S_A$) plus their ranks and
$\tau^*/\tau$ margins.

**Appendix A.5 (the ledger itself)** — all ~80 rows are self-documenting with an exact file and
dotted path, generated by `src/diagnostics/report_claims.py`; spot-checked several against the
underlying YAML directly in this session (Phase 1's Mahalanobis recomputation touched
`confidence_set_mmc.yaml` and `boundary_sweep.yaml` directly; this phase additionally checked
`second_theta_check.yaml` and `alt_eta_scaling.yaml`) rather than trusting the generator's output
blindly.

**Checklist compute-resources item** — "9,216 simulator runs for the eight-assignment sweep"
traces to `robustness/k6_spectrum.yaml`'s `n_simulator_runs: 9216`; "7.6 million" and "722,000"
trace to the ledger's own C4/C5 rows (`boundary_sweep.yaml` `settings.n_simulator_runs: 7,602,000`,
`confidence_set_mmc.yaml` `settings.n_simulator_runs: 722,000`).

## Count

Approximately 75 distinct numeric claims checked across main text, figures, tables, and appendix
(not counting the ~80 self-documenting ledger rows, which were checked as a block against their
own generator plus targeted spot-checks). **Two defects found, both fixed; zero remain untraced.**
`audit/FINAL_CLAIMS.md` needed no update — every number this session added or changed (the two
Section 5 fixes are corrections to existing traced numbers, not new claims) already has a
documented source; no new `results/*.yaml` file or field was introduced this session.
