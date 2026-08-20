# Outstanding actions

> ## ⚠️ REPOSITORY VISIBILITY — PUBLIC DURING BUILD, PRIVATE BEFORE THE PAPER
>
> Repository is intentionally PUBLIC during the build phase. MUST be switched to
> PRIVATE at <https://github.com/pa1aash/Sim-Attrib/settings> before the paper draft or
> final results are committed, ahead of Sim2Science submission (double-blind).
> Operator decision, 2026-08-20.
>
> This banner stays at the top of this file for the rest of the project's life until it
> is resolved. It is not a blocker on committing code this session — the operator has
> considered the trade-off and accepted it — but it becomes one the moment `paper/`
> gains a draft or `results/` gains a final number.
>
> **TRIGGER FIRED — recorded 2026-08-20, session G4.** `results/` contains real numbers, which
> is the condition D-4 names. `docs/DECISIONS.md` **D-7** records the firing.
>
> **OPERATOR RULING ON THE TRIGGER — 2026-08-20, reconfirmed at the start of session G5, and
> NOT a reopened question.** The repository **stays PUBLIC through the build phase**. The switch
> to private happens **before submission**, as a separate action outside any session's scope.
> D-4's trigger having fired does not make the switch due now; the operator has weighed it and
> ruled. **No session is to re-raise this, re-measure it, or treat it as pending.** It is settled
> and it is the operator's to execute.
>
> **Visibility as measured when it last was, recorded rather than re-checked.** `gh` was not
> authenticated here (`gh auth status`: "You are not logged into any GitHub hosts", 2026-08-20),
> so `gh repo view` was unavailable. It was measured instead through the **unauthenticated**
> GitHub REST API: an anonymous `GET /repos/pa1aash/Sim-Attrib` returned **HTTP 200** with
> `"private": false`, `"visibility": "public"`. A private repository returns **404** to an
> anonymous request, so that check reads differently in the two cases and was not vacuous
> (standing constraint S3). **Measured state at 2026-08-20: PUBLIC — which is the intended
> state for the build phase.** See O-4.

Numbered, with an owner. `OPERATOR` means it cannot be resolved by an agent session.

## Blocking — resolve before the next session commits code

> **Note, G3 (2026-08-20):** the heading is now slightly wrong and is kept for continuity. Code
> has been committed. Nothing in this table blocked it: the two items that did (**O-8**, **O-15**)
> were resolved by the operator and executed this session, and are closed below.

| # | Action | Owner | Notes |
|---|---|---|---|
| **O-1** | **Switch repository visibility public → private, before submission** | OPERATOR | **RULED, NOT PENDING (2026-08-20, reconfirmed G5).** The trigger fired in G4; the operator has ruled that the repository **stays PUBLIC through the build phase** and is switched **before submission**, as a separate action outside any session's scope. `docs/DECISIONS.md` **D-7**, **D-11**. Measured state at 2026-08-20 is **PUBLIC**, which is the intended state. **No session is to re-raise, re-measure, or re-litigate this.** |
| ~~O-2~~ | ~~Sign or reject gates G0, G1, G2 and G3~~ | — | **CLOSED 2026-08-20 (G4).** All four signed by the operator: G0, G1 and G2 with their drafted `conditions` accepted in full, G3 with no conditions beyond normal review. `GATES.md`. **G4 itself is new and UNSIGNED** (S9) — see O-20. Original note follows: All four are `UNSIGNED`. **Proposed `conditions` text is now drafted for all of G0, G1 and G2** in `GATES.md` (G3 §4.2) — accept, amend, or reject. G3 is new and its report is `audit/S3_REPORT.md`. This has been outstanding for three sessions. |
| ~~O-8~~ | ~~Answer Q-8~~ | — | **CLOSED 2026-08-20 (G3).** Superseded by Q-10, which the operator answered and G3 executed. Option (b) — build the diagnostic — was taken and delivered. No longer blocks code; code exists. |
| ~~O-9~~ | ~~Answer Q-9~~ | — | **CLOSED 2026-08-20 (G2).** Answered: the repairs are published (Dufour's MMC; repro samples; co-sufficient sampling). It is a citation, not a research question. |
| ~~O-10~~ | ~~Threat-check R2~~ | — | **CLOSED 2026-08-20 (G3).** `audit/R2_THREAT_CHECK.md`, verdict **NARROW-CONDITIONAL**, run entirely on the corrected full-text instrument. Consequence recorded as **D-6**. |
| **O-13** | **Re-run G0/G1's load-bearing NEGATIVE searches on the arXiv full-text index** | agent | Both sessions used the metadata API while reporting "full text". Every negative they recorded is an **instrument gap**, not a measured zero. One was re-checked in G2 and survived; the rest are unverified. `audit/TOOLING.md`. |
| **O-14** | **Obtain Dufour (2006) version of record** before MMC is cited in any manuscript | agent | *J. Econometrics* 133(2), DOI 10.1016/j.jeconom.2005.06.007 — paywalled; Unpaywall and OpenAlex both `closed`. CIRANO WP 2005s-02 was read and is cited as a working paper. |
| ~~O-15~~ | ~~Answer Q-10~~ | — | **CLOSED 2026-08-20 (G3).** Operator answered: one narrow R2 check, then build the diagnostic regardless. Both done. |
| O-11 | Resolve "Presanis et al. (2017)" or withdraw the claim it supports | agent | Cannot be resolved via Crossref; may be a byline error introduced in G0. `audit/LEDGER_CITATIONS.md`. |
| **O-16** | **Measure `p_sel`** — the probability a null draw lands in the observed selection cell | agent | **DECIDES WHETHER THE NEXT SESSION'S WORK IS AFFORDABLE.** Cheap: needs only null draws and the selection rule, no MMC. The cost gate is pre-registered in `audit/MMC_COMPOSITION_SPEC.md` §4. |
| **O-17** | **Run an adversarial critic** — against the **MMC composition** | agent | **PARTLY DISCHARGED 2026-08-20 (G4).** A critic pass ran against G3's Phase 2 *numbers* — `audit/G3_ADVERSARIAL_REVIEW.md` — and changed the answer, as it did both previous times the debt was paid by accident. **The composition itself is still unrefuted by anyone**, which is what `audit/MMC_COMPOSITION_SPEC.md` §6 says and what this row now tracks. Note also that G4's pass was **not independent**: the same project, its own code, the same session. |
| ~~O-18~~ | ~~Re-run the diagnostic at several seeds~~ | — | **CLOSED 2026-08-20 (G4).** Two further seeds run through the identical diagnostic; `results/robustness/jacobian_rank.seed_*.yaml`, tabulated in `results/robustness/ROBUSTNESS_TABLE.md` §2 and read in `audit/G3_ADVERSARIAL_REVIEW.md`. |
| **O-19** | **Add a ligature rule alongside S7** | agent | *(still open; G4 used `hyperresearch`'s own extraction plus NFKC normalisation rather than raw `grep`, so the defect did not recur, but no rule has been written down.)* PDF extraction preserves `ﬀ`/`ﬁ`/`ﬂ`, so `grep -a "difference parameter"` returned **0** against 18 real occurrences. S7's `grep -a` rule does not cover this. Normalise NFKC and validate against a control term containing a ligature. `audit/R2_THREAT_CHECK.md` §3.4. |
| ~~O-20~~ | ~~Sign or reject gate G4~~ | — | **CLOSED 2026-08-20 (G5).** Signed unconditionally by the operator, together with G0–G3, as recorded in `GATES.md`. The signature is explicit that Q-13 stays open and that the gapless-spectrum objection stays DEFERRED — signing G4 did not settle either. |
| **O-21** | **Answer Q-13** — what may be claimed from a family-conditional separability verdict | OPERATOR | **BLOCKING for the paper's separability sentence only.** Does not block the `p_sel` measurement. `docs/OPEN_QUESTIONS.md`. |
| **O-22** | **Re-run `run_diagnostic.py` once, so `results/` carries a real leakage check** | agent | Every file in `results/` records `leakage_checked: true` as a **hard-coded literal**. `jacobian_rank.leakage_check` now computes a real one and `run_diagnostic.py` records it, but G3's files were deliberately not regenerated (that would overwrite G3's numbers). A clean re-run at the same seed should reproduce them exactly **and** carry the check — and if it does not reproduce them exactly, that is itself the finding. |
| ~~O-3~~ | ~~Select a venue~~ | — | **CLOSED 2026-08-20.** Sim2Science, 5-page main track. `docs/DECISIONS.md` D-2. |

## Non-blocking — carry forward

| # | Action | Owner | Notes |
|---|---|---|---|
| O-4 | Authenticate `gh` (`gh auth login`) | OPERATOR | Without it, repository state cannot be verified from this machine and workshop OpenReview pages cannot be queried through the API. |
| ~~O-5~~ | ~~Obtain the venue's LaTeX template~~ | — | **CLOSED 2026-08-20.** Fetched unmodified to `paper/neurips_2026_template/`; SHA-256 recorded in `docs/DECISIONS.md` D-2. |
| O-6 | Retrieve **Arendt, Apley & Chen (2012)**, or accept final failure | agent/OPERATOR | Three of the original four are retrieved. Arendt: **five routes tried and logged** 2026-08-20 — ASME, Unpaywall, OpenAlex, Northwestern IDEAL, ResearchGate. All failed. Likely needs institutional access. |
| O-12 | Retrieve **Branke, Chick & Schmidt (2007)** and the **Kim & Nelson (2006)** handbook chapter | agent | Both required by the G1 brief, both paywalled, both **not read**. Substitutes were read and are recorded as substitutes in `audit/BIBLIOGRAPHY.bib` §5. |
| O-7 | Re-run the prior-art sweep against OpenReview and Google Scholar before submission | agent | The originating plan's sweep covered neither. |

## Pre-push checklist

Run all of these before `git push`. Checks 2 and 3 must produce **no output**.

The search pattern is **assembled at runtime rather than spelled out**, because a
checklist that spells its own forbidden tokens matches itself and can never pass. Do
not "simplify" this by inlining the literal string.

```bash
# 0. toplevel assertion - never stage from a directory whose toplevel is $HOME
test "$(git rev-parse --show-toplevel)" = "$HOME/Desktop/Sim-Attrib" || echo "ABORT"

# 1. build the pattern without writing the tokens into this file
PAT="$(printf 'c%saude|a%sthropic|co-auth%sred|generat%sd with' l n o e)"

# 2. commit metadata and messages
git log --format='%an|%ae|%B' | grep -iE "$PAT"

# 3. tracked file contents  (scoped to tracked files - see DEVIATIONS.md D-1)
git ls-files -z | xargs -0 grep -IiE "$PAT"

# 4. authorship of every commit - expect exactly one line
git log --format='%an <%ae> | %cn <%ce>' | sort -u
```
