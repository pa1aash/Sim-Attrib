# Research tooling probe

Run 2026-08-20, before any research command was issued. The purpose of probing first is
that the two generations of this CLI differ in whether a research run has resumable
state, and the wrong assumption loses a long run at the point it is interrupted.

## Installed generation

```
$ hyperresearch --version
hyperresearch v0.8.5
```

Binary: `/opt/homebrew/Caskroom/miniforge/base/bin/hyperresearch` (not on `PATH`).

## Capability probe

| Probe | Result | Evidence |
|---|---|---|
| `hyperresearch profile list` | **ABSENT** | `No such command 'profile list'.` |
| `hyperresearch run status -j` | **ABSENT** | `No such command 'run status'. Did you mean 'status'?` |
| `hyperresearch config get scholar.contact_email` | **ABSENT** | `Unknown config key: scholar.contact_email` |

**Verdict: BRANCH B.** There is no gear/profile selection and no resumable run state.
`profile` and `run` were probed once each and are not called again.

## Commands that do exist

`install, setup, init, status, sync, search, fetch, fetch-batch, research, tags, dedup,`
`archive-run, vault-tag, import, repair, watch, serve, mcp, note, graph, index, lint,`
`export, config, topic, batch, template, git, tag, sources, assets, link`

The Branch B equivalents named in the session instructions — `research`, `fetch`,
`archive-run`, `export` — are all present.

## Vault configuration

```
vault_name:    Research Base
vault_path:    /Users/palaash          <- NOT this repository
research_dir:  research                 -> /Users/palaash/research
web_provider:  crawl4ai
web_profile:   (none)
web_magic:     False
```

Two consequences worth recording.

First, **the vault lives at `/Users/palaash/research`, outside this repository.**
Retrieved paper text therefore never lands inside the repo tree at all. The `research/`
entry in `.gitignore` is defensive rather than load-bearing, and is kept.

Second, `web_profile` is unset and `web_magic` is false, so **no authenticated crawling
is configured**. Login-gated sources — publisher sites behind institutional
authentication in particular — will return login walls rather than content. This is the
direct cause of the retrieval difficulty on the four journal-side statistics references;
see `LEDGER_CITATIONS.md`.

Vault at probe time: 438 notes, 275 unique tags, unrelated prior topics.

## Consequence 1 — checkpointing is manual

There is no run manifest and no `run resume`. The pipeline is conversation-driven, which
means an interruption loses everything not written to disk. This is a known failure mode
for this setup; a prior run was lost at step 2 of 16.

Checkpoints are therefore written by hand, **outside the repository**, to:

```
~/Desktop/Sim-Attrib-research-state/
    STATE.md                    <- names the last completed step
    step_NN_<name>.md           <- one per completed step
```

Outside the repository because these are working artefacts of a specific session, not
project record. What they produce that *is* project record — verdicts, citations,
venue evidence — is written into `audit/` and committed.

## Consequence 2 — open-access recovery has no configured path

With no `[scholar]` section and no `scholar.contact_email`, the CLI offers no Unpaywall
integration. Unpaywall's terms require a real contact address per request, so recovery of
the paywalled references is routed manually instead:

1. Unpaywall REST API called directly with the operator's address as the `email`
   parameter;
2. arXiv, where a preprint exists — **marked as a preprint**, because a preprint is not
   a substitute for the version of record when a specific theorem is being attributed to
   a specific paper;
3. institutional repositories and author homepages;
4. Europe PMC for anything with biomedical indexing.

Each attempt and each failure is logged individually in `LEDGER_CITATIONS.md`, per
reference, not summarised as a group.

## Consequence 3 — breadth must be bought manually

Branch A would have set the gear to `premier` and widened the source sweep automatically.
That is unavailable. Since the prior-art verdict is the crux of this paper, and since the
originating plan's own sweep covered neither OpenReview nor Google Scholar, the sweep is
widened by explicit instruction instead: academic APIs first (Semantic Scholar, arXiv,
OpenAlex), then OpenReview, then general web search, then at least one deliberately
adversarial search per major claim.

---
---

# CORRECTION — session G2, 2026-08-20: the arXiv searches were never full-text

**This corrects a load-bearing methodological claim in both G0 and G1**, and it is the most
probable single explanation for why this project has had three primary claims die to prior art.

## What was believed

`audit/S0_REPORT.md` §2 reports that R1's novelty was checked against *"nine conjunctive arXiv
full-text queries"*. `audit/R1_THREAT_CHECK.md` §4 (G1) reports its zero-counts under the
heading `arXiv full text`. Both sessions used the arXiv **API** with the `all:` field prefix.

## What is true

**The arXiv API's `all:` field searches metadata only** — title, abstract, authors, comments,
journal reference. It does **not** index the body of the paper.

Demonstrated rather than assumed. Three phrases were verified present in already-fetched paper
bodies, then queried through the API:

| Phrase | In fetched body | API `all:"…"` total |
|---|---|---|
| `expected number of draws required to obtain one acceptable` (Freidling et al., Supp. §S3.2) | 1 | **0** |
| `repeatedly executing the selection algorithm` (Liu et al., arXiv:2203.14504) | 2 | **0** |
| `conditional PCS` (Hong, Fan & Luo) | 3 | 5 — also appears in abstracts |

Two phrases that provably exist in arXiv papers return zero.

## The real full-text index, and how to use it

It exists, it works, and it is the route named in the G2 brief's S4:

```bash
curl -sS -L -A "<desktop UA>" -X POST "https://arxiv.org/search_classic" \
     --data-urlencode 'query="<exact phrase>"' --data "searchtype=ft"
```

`https://search.arxiv.org/` renders the form; the form POSTs to `arxiv.org/search_classic`
with `searchtype=ft`. The response is HTML containing `Displaying hits N to M of TOTAL`,
`https://arxiv.org/abs/<id>` links, and a body snippet around each match.

**Verified:** the first phrase in the table above returns exactly Freidling et al. with the
surrounding body text; the second returns exactly arXiv:2203.14504.

A reusable helper was written to the session scratchpad rather than committed, since it is a
working artefact and not project record. The four lines above are the whole of it.

## Order-of-magnitude difference in coverage

Same question, two instruments, this session:

| Query | Metadata API | Full-text index |
|---|---|---|
| selective inference + nuisance | 7 | 54 |
| Monte Carlo test + nuisance parameters | 2 | 24 |

Dufour's maximized Monte Carlo, the repro-samples line, and the co-sufficient-sampling line —
the three findings that killed G2's target claim — **all surfaced only on the full-text index.**

## What this invalidates, stated precisely

**Positive findings are unaffected.** "Here is a paper that does the thing" does not depend on
how the paper was found. The ex-C2 refutation (Kahl et al.) and the R1 refutation (Freidling
et al.) stand.

**Negative findings from G0 and G1 are downgraded.** Every zero-count reported by those
sessions as evidence that a literature does not contain something was a *metadata* zero. Under
S4's rule these were **instrument gaps reported as measured zeros**, which is exactly the
conflation that rule exists to prevent.

Specifically re-checked this session: G1's conclusion that ranking-and-selection and selective
inference "have not met" was based on a metadata zero. Re-run on the full-text index,
`"selection event" "maximized Monte Carlo"` returns a genuine full-text **0**, so that
conclusion survives — **but it survives because it was re-checked, not because G1 established
it.** No other G0/G1 negative has been re-checked.

## Standing rule from here

1. **Never report an arXiv zero from the metadata API as evidence of absence.** Use
   `search_classic` with `searchtype=ft`, and say which instrument produced the number.
2. **State the instrument next to every count**, in the same row.
3. A metadata zero is an **instrument gap**, not a negative result.
