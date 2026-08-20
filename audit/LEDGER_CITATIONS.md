# Ledger of citations

Every reference named in `PLAN_SOURCE.md`, with identifier, retrieval status, and — the
column that matters — whether the plan's *characterisation* of it is accurate. A citation
can be real, retrievable, and still wrongly described.

Retrieval status: `NOT ATTEMPTED` · `RETRIEVED (VoR)` · `RETRIEVED (preprint)` ·
`METADATA ONLY` · `FAILED`

**A preprint is not a substitute for the version of record** when a specific theorem or
result is being attributed. Where only a preprint is obtained, the entry says so and the
attribution is provisional.

---

## Group 1 — SBI misspecification (arXiv-native, expected retrievable)

| # | Reference | Identifier | Retrieval | Characterisation accurate? |
|---|---|---|---|---|
| C1 | Anau Montel, Alvey & Weniger — *the gatekeeper* | arXiv:2412.15100 | NOT ATTEMPTED | **decides C1** — see A/B group in `LEDGER_ASSERTIONS.md` |
| C2 | Schmitt, Radev & Bürkner | arXiv:2112.08866 | NOT ATTEMPTED | plan says MMD-based global detection (A3) |
| C3 | Schmitt, Radev & Bürkner (second work) | arXiv:2406.03154 | NOT ATTEMPTED | as above |
| C4 | Cannon, Ward & Gutmann | arXiv:2209.01845 | NOT ATTEMPTED | not characterised in the plan beyond inclusion |
| C5 | Ward, Cannon, Beaumont, Fasiolo & Naderiparizi — RNPE | NeurIPS 2022; arXiv ID to confirm | NOT ATTEMPTED | **open check** — see C1b |
| C6 | RoPE | arXiv:2405.08719, ICML 2025 | NOT ATTEMPTED | **author list suspect** — see note below |
| C7 | Tomaselli, Ventura & Wasserman | arXiv:2508.02404 | NOT ATTEMPTED | uncharacterised |
| C8 | Leclercq | arXiv:2209.11057 | NOT ATTEMPTED | uncharacterised |
| C9 | Yang, Nott & Presanis | arXiv:2511.02977 | NOT ATTEMPTED | **note the Presanis overlap** — see below |
| C10 | Pierre et al. | arXiv:2507.03086 | NOT ATTEMPTED | uncharacterised |

**Note on C6 (RoPE).** The plan writes "Kelly, Huang, Tomaselli, Wehenkel (RoPE)". That
list mixes names that appear across several different papers in this area and should not
be trusted as a byline. Verify the actual author list against arXiv:2405.08719 before any
citation is written. Miscrediting authors in a related-work section is the kind of error
reviewers in a small subfield notice immediately.

**Note on C9 (Yang, Nott & Presanis, arXiv:2511.02977).** *Presanis* appears both here
and as an author of the conflict-diagnostics work the plan proposes to distinguish itself
from (C16). A 2025 paper by an author of the DAG conflict-diagnostics literature,
surfacing in an SBI-adjacent sweep, is **precisely where a bridge between the two
literatures would appear** — and such a bridge is the refutation scenario D2(a)/(b) warns
about. This paper is a priority read, not a filler citation. The plan lists it without
comment.

**Note on identifiers.** arXiv IDs of the form 2508.*, 2511.*, and 2507.* denote 2025
submissions. They are recorded as given in the plan and each must be confirmed to resolve
to the claimed work — a transposed identifier resolves to an unrelated paper and produces
a citation that is wrong rather than missing.

---

## Group 2 — Calibration and discrepancy (journal-side; the plan flags all four as unretrieved)

These four carry the weight of the C2 novelty argument. The plan's own closing line says:
*"The four journal-side statistics citations were not retrieved directly — verify before
writing."*

| # | Reference | Identifier | Retrieval | Why it matters |
|---|---|---|---|---|
| C11 | Kennedy & O'Hagan, "Bayesian calibration of computer models", *JRSS-B* 63(3), 2001 | DOI 10.1111/1467-9868.00294 | NOT ATTEMPTED | Origin of the calibration-plus-discrepancy formulation the whole of C2 is an analogue of. |
| C12 | Brynjarsdottir & O'Hagan, *Inverse Problems* 30(11), 2014 | DOI to confirm | NOT ATTEMPTED | **The plan names this as the direct precedent for C2's confounding argument.** If it already contains a rank-type condition for when discrepancy is separable, C2 narrows sharply. |
| C13 | Tuo & Wu, *Annals of Statistics* 43(6), 2015 | DOI to confirm | NOT ATTEMPTED | Inconsistency of the calibration parameter under discrepancy. The plan invokes it as an analogue; whether the analogy is loose or exact is E2/E3. |
| C14 | Arendt, Apley & Chen, 2012 | DOI to confirm | NOT ATTEMPTED | **Most dangerous of the four for C2.** This work is specifically about *identifiability* of calibration parameters and discrepancy, and about whether multiple responses can separate them. Separating confounded discrepancy contributions using multiple outputs is structurally the same question as E3. The plan cites it in passing and does not engage it. |

**Recovery route (no `[scholar]` config exists — see `TOOLING.md`):** Unpaywall REST API
with the operator's address supplied per request; arXiv where a preprint exists, marked
as such; institutional repositories and author homepages; Europe PMC for anything
biomedically indexed. **Each failure is logged individually below, per reference, not
summarised as a group.**

### Individual recovery log

| Ref | Attempt | Route | Result |
|---|---|---|---|
| C11 | — | — | not yet attempted |
| C12 | — | — | not yet attempted |
| C13 | — | — | not yet attempted |
| C14 | — | — | not yet attempted |

---

## Group 3 — Conflict diagnostics

| # | Reference | Identifier | Retrieval | Why it matters |
|---|---|---|---|---|
| C15 | Marshall & Spiegelhalter, conflict p-values | full citation missing from the plan | NOT ATTEMPTED | The plan names authors and a concept but gives no year, title, or venue. **This is an incomplete citation, not a citation.** |
| C16 | Presanis, Ohlssen, Spiegelhalter & De Angelis, "Conflict diagnostics in directed acyclic graphs", *Statistical Science* 28(3), 2013 | DOI to confirm | NOT ATTEMPTED | Node-level localisation with calibrated p-values — the closest existing thing to component-level attribution anywhere in the plan's bibliography. D2 decides whether it transfers. |

---

## Group 4 — Background and framing

| # | Reference | Identifier | Retrieval | Notes |
|---|---|---|---|---|
| C17 | Frazier, Robert & Rousseau, *JRSS-B* 2020 | DOI to confirm | NOT ATTEMPTED | ABC under misspecification. |
| C18 | Cranmer, Brehmer & Louppe, *PNAS* 2020 | DOI 10.1073/pnas.1912789117 | NOT ATTEMPTED | Standard SBI framing citation; open access. |
| C19 | Talts, Betancourt, Simpson, Vehtari & Gelman — SBC | arXiv:1804.06788 | NOT ATTEMPTED | Calibration checking; cited for the calibrated-null framing. |

---

## Group 5 — Missing from the plan's bibliography but required by the argument

Not cited by the plan. Listed because the claims cannot be defended without engaging
them, and their absence is itself a finding about the plan's coverage.

| # | Area | Why required |
|---|---|---|
| M1 | **Structural identifiability for ODE/compartmental models** (differential algebra, Lie-derivative methods, and the software that implements them — e.g. DAISY, STRIKE-GOLDD, SIAN) | E3 asserts a rank condition for identifiability of an ODE-model quantity. This field has studied exactly that for decades. **The plan cites none of it.** If C2 is written without engaging this literature, a reviewer from it will reject the paper on sight. |
| M2 | **Practical identifiability / profile likelihood** (Raue et al. and successors) | The distinction between structural and practical identifiability, and sensitivity-matrix rank as the operative criterion, is standard there. Directly overlaps E3. |
| M3 | **Selective inference** — knockoffs (Barber & Candès), e-BH (Wang & Ramdas), conditional selective inference (Lee, Sun, Sun & Taylor; Fithian, Sun & Taylor) | The plan proposes "e-BH/knockoff-style selection" as its method and cites **no** selective-inference paper. The guarantees C1 depends on come from this literature. |
| M4 | **Sensitivity analysis for simulators** (Sobol, Morris, and variance-based global methods) | Attributing output variation to model components is the founding question of this field. A reviewer will ask how component attribution differs from global sensitivity analysis, and the plan has no answer prepared. |

**M1 and M4 are the two most likely sources of an unanticipated rejection**, because both
are large, mature literatures that ask a version of this project's question in different
vocabulary, and the plan engages neither.

---
---

# VERIFICATION RESULTS — session G0, 2026-08-20

Every entry below was checked by **fetching the paper and reading its title block**.
Nothing here is from memory or from secondary description.

## Byline errors in the plan — four found, and it is a pattern

| # | Plan's citation | The paper itself | Severity |
|---|---|---|---|
| C1 | "**Montel**, Alvey & Weniger" | Surname is **Anau Montel**. *Noemi Anau Montel, James Alvey, Christoph Weniger* | Moderate — compound surname split |
| C5 | "Ward, Cannon, Beaumont, Fasiolo & **Naderiparizi**" | Fifth author is **Sebastian M. Schmon** (Improbable / Durham). arXiv:**2210.06564** | **Serious** — names an author who is not on the paper |
| C6 | "**Kelly, Huang, Tomaselli, Wehenkel** (RoPE), arXiv:2405.08719" | arXiv:2405.08719 is *"Addressing Misspecification in Simulation-based Inference through Data-driven Calibration"* — **Antoine Wehenkel, Juan L. Gamella, Ozan Sener, Jens Behrmann, Guillermo Sapiro, Jörn-Henrik Jacobsen, Marco Cuturi**. Only Wehenkel is right; "Tomaselli" belongs to arXiv:2508.02404 | **Serious** — two papers conflated |
| C2 | "Schmitt, Radev & Bürkner" | *Marvin Schmitt, Paul-Christian Bürkner, **Ullrich Köthe**, Stefan T. Radev* | Minor — one author omitted |

The plan concedes its four *journal-side* citations were unretrieved. The finding here is
that the **arXiv-side** citations were not reliably retrieved either. Treat every
reference as unverified until fetched.

## Retrieval log — full text obtained

| Ref | Identifier | Words | Status |
|---|---|---|---|
| C1 Anau Montel et al. | arXiv:2412.15100 | 11,676 | RETRIEVED (preprint) — **read in full** |
| C5 Ward et al. RNPE | arXiv:2210.06564 | 9,556 | RETRIEVED (preprint) — **read in full** |
| C2 Schmitt et al. | arXiv:2112.08866 | 14,979 | RETRIEVED (preprint) |
| C3 Schmitt et al. | arXiv:2406.03154 | 15,026 | RETRIEVED (preprint) |
| C4 Cannon, Ward & Gutmann | arXiv:2209.01845 | 8,463 | RETRIEVED (preprint) |
| C6 Wehenkel et al. | arXiv:2405.08719 | 16,986 | RETRIEVED (preprint) |
| C7 Tomaselli, Ventura & Wasserman | arXiv:2508.02404 | 19,696 | RETRIEVED (preprint) — plan's citation **correct** |
| C8 Leclercq | arXiv:2209.11057 | 4,334 | RETRIEVED (preprint) |
| C10 Pierre et al. | arXiv:2507.03086 | 10,479 | RETRIEVED (preprint) |
| C13 Tuo & Wu | arXiv:1507.07280 | 8,703 | RETRIEVED (**preprint, not the version of record** — *Ann. Statist.* 43(6), DOI 10.1214/15-AOS1314) |
| — Wu, Shirvan & Kozlowski | arXiv:1801.10309 | 9,280 | RETRIEVED (preprint) — **not in the plan; bears directly on C2** |

## The "paywalled four" — the premise was wrong

The plan treats these as unretrievable. Located via OpenAlex, **three of four are openly
accessible**:

| Ref | DOI | OA | Route |
|---|---|---|---|
| C11 Kennedy & O'Hagan, *JRSS-B* 63(3) 2001 | 10.1111/1467-9868.00294 | **Yes** | OUP PDF |
| C12 Brynjarsdóttir & O'Hagan, *Inverse Problems* 30(11) 2014 | 10.1088/0266-5611/30/11/114007 | **Yes** | IOP PDF |
| C13 Tuo & Wu, *Ann. Statist.* 43(6) 2015 | 10.1214/15-AOS1314 | **Yes** | OSTI; arXiv:1507.07280 |
| C14 Arendt, Apley & Chen 2012 | 10.1115/1.4007390 | **No** | ASME paywall — **still open**, and it is the one most likely to matter for C2 |

They were not blocked by paywalls. They were not looked for with an open-access resolver.

## C15 — the incomplete citation, now complete

The plan gives "Marshall & Spiegelhalter conflict p-values" with no year, title, or
venue. The paper is:

> **E. C. Marshall & D. J. Spiegelhalter (2007)**, *"Identifying outliers in Bayesian
> hierarchical models: **a simulation-based approach**"*, **Bayesian Analysis 2(2)**,
> DOI **10.1214/07-BA218**. Open access.

**The subtitle is a problem for the plan's defence.** The plan argues conflict
diagnostics "need a tractable likelihood; SBI has neither". A paper whose title announces
a simulation-based approach is prima facie evidence against that, and the plan was
written without retrieving it.

## C16 — full title recovered

> **Presanis, Ohlssen, Spiegelhalter & De Angelis (2013)**, *"Conflict Diagnostics in
> Directed Acyclic Graphs, **with Applications in Bayesian Evidence Synthesis**"*,
> *Statistical Science* **28(3)**, DOI **10.1214/13-STS426**. Open access; also Cambridge
> Apollo, DOI 10.17863/cam.34842.

## Note on C9 — the flagged overlap

C9 (Yang, Nott & Presanis, arXiv:2511.02977) shares an author with C16. As logged before
verification, this is where a bridge between the conflict-diagnostics and SBI literatures
would appear. Under dedicated investigation; verdict pending.
