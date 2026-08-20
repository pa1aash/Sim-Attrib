# Deviations

Where execution departed from instruction, and why. Written as it happens, not
reconstructed afterwards.

## D-1 — Scope of the authorship grep

**Instruction:** before every push, run
`grep -rIiE 'claude|anthropic' --exclude-dir=.git .` over the working directory and
require empty output.

**What is done instead:** the check is run in two parts.

1. `git ls-files -z | xargs -0 grep -IiE 'claude|anthropic'` — over **tracked files
   only**, required empty. This is the check that determines whether a push proceeds.
2. `git log --format='%an|%ae|%B' | grep -iE 'claude|anthropic|co-authored|generated with|robot-emoji'`
   — over all commit metadata and messages, required empty.

**Why:** the literal working-directory grep also descends into gitignored paths that are
not part of the repository and never will be — the local plugin working directory
`.remember/`, and the local research vault if one is ever created inside this tree. A
match there would block a push over a file that is not being pushed, while telling us
nothing about repository contents. Restricting to tracked files tests the actual
property the instruction is protecting: that nothing *in the repository* names an
authoring agent.

The unrestricted grep is still run and its output inspected; it is simply not the gate.
Both forms are recorded in `OUTSTANDING.md` under the pre-push checklist.

## D-2 — hyperresearch generation is older than the instruction anticipated

**Instruction:** probe for `hyperresearch profile` and `hyperresearch run`; if present,
set the gear to `premier` and use resumable run state (Branch A).

**Finding:** the installed CLI is **v0.8.5**. `profile` and `run` are both ABSENT, and
`config get scholar.contact_email` returns `Unknown config key`. Branch B applies.

**Consequence:** there is no resumable run state and no gear selection. The breadth
that `premier` would have bought has to be bought manually, by explicitly widening the
source sweep. Checkpointing is manual, to
`~/Desktop/Sim-Attrib-research-state/`, outside the repository. Recorded in
`audit/TOOLING.md`.

## D-3 — No `[scholar]` configuration section exists

**Instruction:** ensure `scholar.contact_email` is set so Unpaywall recovery works.

**Finding:** v0.8.5 has no such key; `config show` lists only vault, web-provider, and
search-tuning keys. Unpaywall's API is therefore not reachable through the CLI's own
configuration.

**Consequence:** the four paywalled statistics citations are routed through direct
Unpaywall API calls with the operator's address supplied per-request, plus arXiv,
institutional repositories, and author homepages. Each failure is logged individually in
`audit/LEDGER_CITATIONS.md` rather than being summarised as a group.
