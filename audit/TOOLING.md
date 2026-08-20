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
