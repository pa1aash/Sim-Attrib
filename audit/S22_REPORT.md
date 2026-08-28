# S22 — Session G22 report: captions, headers, terminology, numeric precision, spelling

**Prepared 2026-08-29.** This is the twenty-second internal session, third of the four planned
(G20-G23) covering a detailed operator line-edit. G22's mandate: compress captions to
description-only content, rename headers/section leads for navigability, remove process-leakage
and internal jargon, unify terminology and notation, standardize numeric precision, and pick one
spelling convention document-wide. Full detail in `GATES.md` G22; this is the top-level summary.

## The direct answer

**Every phase in the operator's brief ran to completion, one genuine correctness fix was made
(the four `p≈0.004` Montel values are the resolution floor of a 1500-draw calibration batch, not
four independent measurements), and the 5-page main-text / page-6-references / page-7-appendix
structure G20 and G21 established still holds** — closed this time by tightening this session's
own additions plus a larger (but still visually-verified-safe) `\enlargethispage` value, not by
new prose cuts elsewhere in the document.

## What this session actually did

**Phase 1 — captions.** All nine items fixed: two main-text figure captions (Figures 1 and 2)
lost interpretive sentences already stated in the body; one main-text figure (Figure 3, Section
5) had its design specification and gate definition moved into Section 5's own prose rather than
just deleted, since the operator's brief required that content survive somewhere; four appendix
items (Figures 4-7) were trimmed of duplicated or argumentative content; Table 2's plateau-
stability result moved into Section 4's prose. Table 3's flagged fact was searched for directly
and confirmed already absent.

**Phase 2 — headers.** Every rename applied exactly as specified, including splitting the
comma-spliced "The mechanism, and the shape of the boundary" into two single-topic paragraphs —
which fell out naturally once the gate definition moved out of the caption and into that exact
spot in the prose.

**Phase 3 — process leakage.** All seven items fixed, including one the brief did not anticipate:
"registered" (bare, without "pre-") was baked into three figures' own plotted matplotlib labels,
not just the LaTeX captions. Caught by `pdftotext`-ing the recompiled PDF rather than only
grepping the `.tex` source. Fixed at the source Python scripts and regenerated using the
project's own pinned dependency versions in a throwaway virtual environment; each figure's
built-in data-matching assertions passed on regeneration.

**Phase 4 — terminology.** All ten items addressed. The most consequential item in the brief
(4.5, the K=6 overload) turned out to already be resolved — no live "K=6" instance survives
anywhere in the compiled paper, confirmed by grep before any editing began, so no new symbol was
introduced. The other nine (assignment-terminology unification, identifiable/separable
reservation, component/mechanism, acceptance-probability naming, τ*, coherence/column-norm-floor
definitions, "the composition," "the gate," and "ten" vs. "roughly ten") were each either fixed
directly or confirmed already resolved by an earlier session, checked rather than assumed in
every case.

**Phase 5 — numeric precision.** κ=629/628.9 and the 6.6–65.6/6.628–65.64 pair unified to the
higher-precision, already-dominant form. `0.9424` and `1.958` confirmed already absent.
`344.9` left alone — it already matches this paper's own 4-significant-figure convention for
every κ value, and rounding it in isolation would have made it the inconsistent one, contrary to
the brief's own stated goal. `1.023`→`1.02` and `2.265`→`2.26` rounded to a precision this
project's own ~128-replicate Jacobian estimate can actually support. **The genuine correctness
fix**: the four `p≈0.004` Montel-test values are confirmed, against `results/
montel_marginal_test.yaml` directly, to be identically `0.003997335109926716` — the resolution
floor of a 1500-draw calibration batch (6/1501) — and the paper now says so explicitly instead of
implying four independent near-agreements.

**Phase 6 — spelling.** American spelling chosen. Eight instances fixed across `paper/main.tex`;
a document-wide grep across every standard British/American divergent-pair family confirmed
these were the only instances remaining in `paper/main.tex` and `appendix_tables.tex`.

## The page-budget interaction

Several of this session's required additions (the gate definition, the 42-point design spec, the
τ* definition, the Montel resolution-floor explanation, one Limitations sentence, and the
acceptance-probability mapping) are net new main-text content, required by specific numbered
instructions and not droppable. Combined, they pushed the Conclusion two lines past the bottom of
page 5. Closed by tightening the added sentences themselves wherever possible without losing
required content, plus raising the existing `\enlargethispage` before Limitations from
`2\baselineskip` to `6\baselineskip` — the same lever G12-G16 already established for this exact
purpose, not a new one. An `8\baselineskip` value was tried first and rejected after a rendered-
page visual check showed it pushing the last line of the Conclusion into the bottom margin;
`6\baselineskip` was confirmed clean by the same method. Main text remains exactly 5 pages,
references begin page 6, the appendix begins page 7 — unchanged in shape from G21, produced by a
different specific lever value.

## Re-verification

- **Number trace:** every numeric token in `paper/main.tex` diffed pre- vs. post-session. Ten
  differences found, every one an intentional Phase 5 fix or a Phase 1 caption deletion whose
  value survives unchanged elsewhere in the document.
- **Anonymization re-scan:** clean across the recompiled PDF's text and metadata.
- **Two-tier isolation compile:** `build/sim_attrib_overleaf_39c902e.zip`, rebuilt from the
  working tree with this session's edits (including the three regenerated figures), extracted to
  two independent temp directories and compiled end to end — both exit 0, both 17 total pages,
  zero undefined references, `pdftotext` output byte-identical (MD5
  `a2ef4b7866dd1f1a02afe0d2dfc0b654`) across the repo working copy and both isolated extractions.
- **Package rebuilds:** both the Overleaf package and the anonymized reproducibility package
  rebuilt against the final edited tree; both anonymity scans report clean; `CLAIMS.md` confirmed
  present and unchanged (this session touched no claim data).

## Honesty about what this session did not do

This session did not diff the three regenerated figures pixel-by-pixel against their G16-era
originals — it confirmed each figure script's own built-in provenance/data-matching assertions
passed on regeneration and that `git status` shows only the three intended files changed, which
is not the same guarantee. It did not touch `src/viz/fig3_spectrum.py`'s internal `CAPTION`
docstring, which still reads `κ=629` and `K=6` — that string is written to a provenance sidecar
never shown to a paper reader or reviewer, judged out of this session's paper-facing scope rather
than silently missed. It did not re-read the whole document by eye hunting for spelling drift
beyond the documented grep families, though those families were broad. The `\enlargethispage`
value is now project-specific tuning (`6\baselineskip`), not a portable constant — a future
session that adds or removes main-text content must re-verify the page break visually, not just
by page count, since the earlier `8\baselineskip` attempt showed that page count alone (still 17
throughout every value tried) does not catch text pushed into the bottom margin.

**Status: `GATES.md` G22 is `ready for review — UNSIGNED`.** Points requiring operator input,
including the carried-over P-2 through P-9 items and the request to confirm the spelling
convention and the (absence of a) new column-count symbol both read as intended, are collected in
`GATES.md`, not resolved by this session.
