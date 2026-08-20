# Venue evidence

Every fact below was retrieved from the **venue's own site, `neurips.cc`, or the
OpenReview API** on 2026-08-20, and carries the URL it came from. Nothing is from memory
or from a secondary aggregator. Where a fact could not be verified, the row says so and
names the URL that was tried.

---

## Reference facts — NeurIPS 2026 dates and structure

Per `docs/DECISIONS.md` **D-1**, calendar feasibility is not a planning input for this
project. These are retained as reference facts only. **Do not reintroduce countdown or
urgency framing anywhere in this repository.**

| Fact | Value | Source |
|---|---|---|
| Workshop submission deadline | **29 August 2026, 23:59 AoE** | <https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/>; Sim2Science CFP; OpenReview API `duedate` 2026-08-30 11:59 UTC |
| Accept/reject notification | **29 September 2026 AoE** | <https://neurips.cc/Conferences/2026/WorkshopsGuidance> |
| Is the notification date extendable? | **No.** NeurIPS states it "cannot be extended under any circumstances" | as above |
| Workshop list announced | 2026-08-10 | blog post above |
| Shared across candidates | All four candidate venues use the same 29 August date | per-venue sections below |
| Archival status | **All NeurIPS 2026 workshop papers are non-archival** and do not appear in proceedings | <https://neurips.cc/Conferences/2026/WorkshopsGuidance> |

### NeurIPS 2026 is three-site — the plan's "Paris" is half right

| Site | Conference | Workshops |
|---|---|---|
| **Sydney (MAIN)** | Dec 6–12 | Dec 11–12 |
| Atlanta (satellite) | Dec 9–13 | Dec 12–13 |
| **Paris (satellite)** | Dec 9–13 | Dec 12–13 |

Source: <https://neurips.cc/Conferences/2026>. All three candidate workshops are
**Paris**-site, so the plan is right about where the relevant workshop is and wrong if it
believes the conference itself is in Paris. The AI4Science backup is in **Sydney** — a
different continent in the same week, so it is a *parallel* choice, not a fallback.

**All NeurIPS 2026 workshop papers are non-archival** and do not appear in proceedings
(<https://neurips.cc/Conferences/2026/WorkshopsGuidance>). Publishing at any of these
does not burn the work for a later archival venue.

---

## 1. Sim2Science: ML with Imperfect Scientific Models — EXISTS, VERIFIED

<https://www.sim2science.com/> · CFP <https://www.sim2science.com/cfp.html> ·
portal <https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/Sim2Sci>

| Field | Value |
|---|---|
| Location / date | Paris; 12 or 13 Dec 2026 (day TBD) |
| **Deadline** | **29 Aug 2026, 23:59 AoE.** OpenReview hard `duedate` 2026-08-30 11:59 UTC, with a 30-minute grace to 12:29 UTC — the two agree exactly |
| Notification | 29 Sep 2026 |
| **Page limit** | **5 pages**; separate **Tiny Paper** track at **2 pages**; references excluded; appendix unlimited but "reviewers are not obligated to read it" |
| **Template** | NeurIPS 2026 LaTeX with `\usepackage[dblblindworkshop]{neurips_2026}` and `\workshoptitle{Sim2Science}` |
| **Template URL** | <https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip> (verified HTTP 200, 20,259 bytes) |
| **Blind** | **Double-blind.** "failure to anonymize, or to follow the required template, may lead to desk rejection" |
| **Archival** | **Non-archival.** "accepted work remains eligible for submission to archival venues afterward" |
| **Dual submission** | **Allowed** — "recently published results and work currently under review" both welcome |
| **Concurrent NeurIPS workshops** | **Discouraged** — "We discourage parallel submission of the same paper to multiple NeurIPS 2026 workshops" |
| Checklist | **Required** — NeurIPS reproducibility checklist, after references, not counted in the page limit. "Missing or incomplete checklists may lead to desk rejection" |

**Organisers:** Georgia Channing (Hugging Face), Noémi Éltető (Google DeepMind), Richard
Gao (Goethe Frankfurt), Daniel Gedon (Tübingen), Magdalena Lederbauer (MIT). **Scientific
advisors:** Cecilia Clementi, **Jakob Macke**, Max Welling. **Invited:** Shirley Ho, Jonas
Köhler, Pablo Samuel Castro, Marta Skreta, Santiago Cadena, Petros Koumoutsakos.

*Note: Jakob Macke as scientific advisor means the SBI community proper is in the room.
The related-work section will be read by people who know this literature — which raises
the cost of the four byline errors recorded in `LEDGER_CITATIONS.md`.*

### Scope — the plan's claim is confirmed **verbatim**

Topics of Interest, bullet 2:

> *"Understanding and mitigating model misspecification, including **simulator diagnostics
> and discrepancy modeling**"*

And, unprompted, bullet 4 — which the plan did not know about and which is a **direct
match for C2**:

> *"Analysis of simulator structure, **degeneracy**, simplifications, and
> **identifiability**"*

That bullet is the strongest single piece of venue evidence in this document. The
workshop has explicitly solicited identifiability-and-degeneracy analysis of simulators.
C2 is not a stretch for this venue; it is the bullet point.

### Three obligations the plan does not mention

1. **Mandatory reciprocal review.** A named co-author is nominated at submission and
   assigned **2** papers. Failure to review is grounds for **desk-rejecting your own
   submission**. Enforced by a required OpenReview field.
2. **The reproducibility checklist is required here** and waived at the other three.
3. **In-person attendance in Paris is mandatory** for accepted papers; "We cannot
   accommodate remote presentations."

**Verdict on the plan's four claims for this venue: all four CONFIRMED** (Paris; scope
language verbatim; 29 Aug AoE; 5 pages / 2-page tiny / refs excluded / appendix
unlimited).

---

## 2. E-values: from Statistics to ML — EXISTS, VERIFIED

<https://e-values-workshop.github.io/> · portal
<https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/E-values>

| Field | Value |
|---|---|
| Location / date | Paris; 12 or 13 Dec 2026 |
| **Deadline** | Site: **29 Aug 2026, 23:59 AoE**. OpenReview `duedate` 2026-08-30 13:00 UTC — **1h01m later than the stated AoE deadline.** Treat the site as binding |
| **Page limit** | **4 pages**, references and optional appendices excluded. No tiny track |
| **Template** | NeurIPS 2026 with the **`sglblindworkshop`** option |
| **Blind** | **Single-blind — inferred, not stated.** The page never uses "blind" or "anonymous". Resolved by reading NeurIPS's own `neurips_2026.sty`, where `sglblindworkshop` sets `\@anonymousfalse`. **This is a derivation from the official style file, not a venue quotation** |
| **Archival** | Non-archival ("The workshop is non-archival") |
| **Dual/concurrent submission** | **NOT STATED — no policy of any kind on the page.** Contact evalue.workshop.2026@gmail.com |
| Reviewing obligation | None |

**Organisers:** Shubhada Agrawal (IISc), Sebastian Arnold (CWI), Yo Joong Choe (INSEAD),
**Peter Grünwald** (CWI/Leiden), **Aaditya Ramdas** (Stanford). **Invited:** Michael I.
Jordan, Rianne de Heide, Eugenio Clerico, Emilie Kaufmann, Nick Koning.

*Grünwald and Ramdas are the e-value literature. A paper claiming e-value machinery here
would be read by the people who built it.*

### Scope — and the problem with it

Relevant bullets: *"Multiple testing, FDR, FWER, and empirical-Bayes connections"*;
*"Compositional e-value guarantees across multi-stage or multi-agent workflows"*;
*"Applications in science, medicine, safety-critical systems, and decision support"*.

**The scope contains no mention of simulators, scientific models, discrepancy, or
misspecification.** Fit would be by *method* — e-values and selection error control — not
by topic. That makes this venue viable only if the paper's contribution genuinely *is*
the selection machinery.

---

## 3. Representations for the Physical Sciences — EXISTS, VERIFIED

<https://representations-physical-sciences.github.io/workshop-2026/> · portal
<https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/RPS>

> **Web search does not surface this workshop.** Two independent searches for the exact
> title returned nothing; it was located via a deadline aggregator and then confirmed
> against its own site and the OpenReview API. Search silence was not evidence of absence.

| Field | Value |
|---|---|
| Location / date | Paris; 12 or 13 Dec 2026 |
| **Deadline** | "**Target** submission deadline — 29 Aug 2026 AoE" (venue's hedge). OpenReview `duedate` 2026-08-30 11:59 UTC — matches exactly |
| **Page limit** | **4 pages** main content, references excluded, appendices unlimited. A second **Research Notes** track has no page limit but **is not yet open** — "Submission details will be announced soon" |
| **Template** | Custom: <https://representations-physical-sciences.github.io/workshop-2026/assets/rps_2026_template.zip> (verified HTTP 200, 12,534 bytes) |
| **Blind** | **Double-blind**, "following the NeurIPS main-track approach" |
| **Archival** | Non-archival |
| **Concurrent submission** | **Explicitly allowed** — the only one of the three that permits it |
| Checklist | Not required |
| File constraint | **Single PDF only. "Additional files are not allowed"** |

**Organisers:** Pietro Novelli, Massimiliano Pontil (IIT/UCL), Florence d'Alché-Buc
(Télécom Paris), Pierre Gentine, Kara Lamb (Columbia), Mathias Niepert (Stuttgart).
**Invited:** Nils Thuerey, Jean-Philippe Vert, Mark Girolami.

### Scope — the weakest fit of the three

Tagline: *"Self-supervision, transfer learning, sampling, and tokenization for scientific
data and physical systems."* The organisers describe the workshop as **"tightly scoped"**
and restrict this first edition to those four themes.

Simulator discrepancy, misspecification, and identifiability are **not** among them. The
nearest adjacency is the *Sampling* theme's treatment of simulators as data generators.
**This venue does not fit the work as conceived.**

---

## 4. Backup: "AI for Science (Sydney)" — EXISTS, but not a fallback

Full name: **"AI for Science: Verification in the Age of AI Scientists"**.
<https://ai4sciencecommunity.github.io/neurips26.html>

| Field | Value |
|---|---|
| **Location** | **Sydney, Australia** — different continent, same week |
| **Deadline** | "29 Aug 2026 AoE", self-labelled **"Tentative"**. OpenReview `duedate` 2026-08-30 23:59 UTC — **12 hours later** |
| **Page limit** | **4–8 pages** — the widest budget of the four |
| Blind / archival | Double-blind; non-archival |
| Dual submission | Allowed |
| Checklist | Not required |

**It is not a fallback.** Its deadline is the same 29 August and all notifications land
29 September, after which no NeurIPS 2026 workshop remains open. It is a *parallel*
choice. Its framing is verification of AI-generated science, so this work would have to be
positioned as *a verifier under an imperfect simulator* — its scope does say *"when
surrogate verifiers can substitute for ground truth"* and names *"Verification under
imperfect simulators"*, so the hook exists, but it is a reframing rather than a fit.

---

## 5. DECIDED — Sim2Science, 5-page main track

**This section recorded a conditional recommendation. As of 2026-08-20 it records a
decision.** See `docs/DECISIONS.md` **D-2**, which is the authoritative entry; this
section carries the venue-side evidence for it.

| Field | Committed value |
|---|---|
| Venue | **Sim2Science: ML with Imperfect Scientific Models**, NeurIPS 2026, Paris satellite |
| Track | **5-page main track** — *not* the 2-page Tiny Paper track |
| Template | NeurIPS 2026, `\usepackage[dblblindworkshop]{neurips_2026}`, `\workshoptitle{Sim2Science}` |
| Template location | `paper/neurips_2026_template/` — fetched unmodified; SHA-256 in `docs/DECISIONS.md` D-2 |
| Blinding | Double-blind. Verified by reading `neurips_2026.sty`: `dblblindworkshop` leaves `\@anonymous` at its default `true`, where `sglblindworkshop` sets `\@anonymousfalse` |

**Why the main track and not Tiny Papers.** G0 recommended the 2-page track, and that
recommendation had exactly one load-bearing premise: that C2 — the identifiability
result — would be the headline, and two pages is enough to state a boundary condition and
show a diagnostic. That premise died in the same session it was written. C2 is
**Kahl, Wendland, Neidhardt, Weber & Kschischo (2019)**, *Physical Review X* 9:041046,
resting on **Sain & Massey (1969)**. A two-page paper whose headline is a published PRX
result, submitted to a workshop advised by **Jakob Macke**, is a paper that gets read by
someone who already knows the result.

The reframed contribution (`docs/DECISIONS.md` D-3) needs room the Tiny track does not
have: a mechanism claim, a precondition it depends on, a noisy-rank estimator, and a
demonstration. Five pages is the smallest honest container for that.

**The other two Paris venues are now out.** E-values fits the *machinery* but its scope
contains no simulator, misspecification, or discrepancy language, so the motivating
problem would need re-explaining from scratch inside four pages to Grünwald and Ramdas.
Representations for the Physical Sciences is self-described as "tightly scoped" to
self-supervision, transfer, sampling, and tokenization, and does not fit. Sim2Science
discourages parallel submission to other NeurIPS 2026 workshops, so this is a choice and
not a hedge.

**What the decision commits us to** — all four are now obligations, not contingencies:

1. **Mandatory reciprocal review.** A named co-author nominated at submission, assigned
   **2** papers. Failure to review is grounds for desk-rejecting our own submission.
   **Who this is remains open — Q-3.**
2. **The NeurIPS reproducibility checklist**, required here and waived at the other three.
   `paper/neurips_2026_template/checklist.tex` is the fetched source.
3. **In-person attendance in Paris**, mandatory for accepted papers; "We cannot
   accommodate remote presentations."
4. **Double-blind anonymisation**, with the repository-visibility consequence recorded as
   `docs/DECISIONS.md` D-4.

**Scope fit, for the record.** The CFP's bullet 2 —
*"Understanding and mitigating model misspecification, including simulator diagnostics and
discrepancy modeling"* — covers the demonstration; bullet 4 —
*"Analysis of simulator structure, degeneracy, simplifications, and identifiability"* —
covers the precondition. Neither bullet covers the mechanism claim (R1) directly, which
is worth knowing: the paper's actual headline is the part of it the CFP does **not**
solicit, and the introduction has to do that work.

## 6. Not verified — named, not glossed

| Venue | Field | Status |
|---|---|---|
| E-values | Blind policy **in the venue's own words** | Derived from the mandated `sglblindworkshop` option via `neurips_2026.sty`; the page never says "blind" or "anonymous" |
| E-values | Dual/concurrent submission policy | **No policy stated on the page** |
| E-values | Camera-ready date | Venue says "TBD" |
| RPS | Research Notes track — limit, deadline, portal | **Not yet published** |
| RPS | Eligibility of already-published work | Not stated |
| RPS | Camera-ready date | Not stated |
| Sim2Science | Camera-ready date | Venue says "TBD" |
| All three Paris venues | Final workshop day (12 vs 13 Dec) | Not yet assigned by NeurIPS |
| AI4Science | Exact abstract-registration deadline | **Referenced in the FAQ but the date appears nowhere on the site** |

### Retrieval failures

| URL | Result | Impact |
|---|---|---|
| `neurips.cc/Conferences/2026/Workshops` | **404** — no consolidated listing page at this path | Worked around via the official NeurIPS blog announcement carrying the full list. No fact lost |
| `sim2science.com/call-for-papers` | 404 — wrong path guess | Real page is `/cfp.html`, retrieved in full. No fact lost |
| Web search for "Representations for the Physical Sciences" | Zero relevant hits across two queries | Workshop is real but search-invisible; confirmed via its own site and the OpenReview API |

### Prompt-injection check

No fetched page contained text addressed to an automated reader or any instruction
directed at a model. One venue policy is reported here **as content**: Sim2Science states
that *"Submissions must reflect substantive human intellectual contribution. Papers that
are wholly AI/autonomous-system-generated are not eligible. Use of AI writing assistance
should follow the NeurIPS 2026 policy on LLM use."*
