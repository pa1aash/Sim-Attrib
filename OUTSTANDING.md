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
> Not verifiable from this machine: `gh` is not authenticated here (`gh auth status`
> reports "You are not logged into any GitHub hosts", re-checked 2026-08-20), so
> `gh repo view` cannot report current visibility. The status above is carried from the
> operator's own statement of it. See O-4.

Numbered, with an owner. `OPERATOR` means it cannot be resolved by an agent session.

## Blocking — resolve before the next session commits code

| # | Action | Owner | Notes |
|---|---|---|---|
| O-1 | Switch repository visibility public → private | OPERATOR | See banner. **Rescoped 2026-08-20:** no longer blocks code commits — operator decided the repo stays public through the build phase. Becomes blocking the moment `paper/` gains a draft or `results/` gains a final number. |
| O-2 | Sign or reject gate G0 after reading `audit/S0_REPORT.md` | OPERATOR | `GATES.md` is `ready for review — UNSIGNED`. |
| ~~O-3~~ | ~~Select a venue~~ | — | **CLOSED 2026-08-20.** Sim2Science, 5-page main track. `docs/DECISIONS.md` D-2. |

## Non-blocking — carry forward

| # | Action | Owner | Notes |
|---|---|---|---|
| O-4 | Authenticate `gh` (`gh auth login`) | OPERATOR | Without it, repository state cannot be verified from this machine and workshop OpenReview pages cannot be queried through the API. |
| ~~O-5~~ | ~~Obtain the venue's LaTeX template~~ | — | **CLOSED 2026-08-20.** Fetched unmodified to `paper/neurips_2026_template/`; SHA-256 recorded in `docs/DECISIONS.md` D-2. |
| O-6 | Retrieve the four paywalled statistics references, or record final failure | agent | Tracked individually in `audit/LEDGER_CITATIONS.md`. A preprint is not a substitute for the version of record when a specific theorem is being attributed. |
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
