# Outstanding actions

> ## ⚠️ THIS REPOSITORY IS PUBLIC
>
> **It must be switched to private at <https://github.com/pa1aash/Sim-Attrib/settings>
> before any unpublished result, draft manuscript, or novel technical claim is
> committed.**
>
> What has been pushed so far is a planning document and scaffolding, which is why the
> push proceeded. The moment `src/`, `results/`, or `paper/` stops being empty, this is
> a public preprint of unreviewed work under a double-blind submission plan.
>
> This was not verified from the machine: `gh` is not authenticated here
> (`gh auth login` has not been run), so `gh repo view` could not report visibility.
> The status above is carried from the operator's own statement of it. Confirm it
> directly. Visibility is not changed by this session by design — it is the operator's
> action.

Numbered, with an owner. `OPERATOR` means it cannot be resolved by an agent session.

## Blocking — resolve before the next session commits code

| # | Action | Owner | Notes |
|---|---|---|---|
| O-1 | Switch repository visibility public → private | OPERATOR | See banner. Blocks all Phase-2 commits. |
| O-2 | Sign or reject gate G0 after reading `audit/S0_REPORT.md` | OPERATOR | `GATES.md` is `ready for review — UNSIGNED`. |
| O-3 | Select a venue once the conditional recommendation in `audit/VENUE.md` is read | OPERATOR | Determines page limit and template, which determine how much of the work is presentable. |

## Non-blocking — carry forward

| # | Action | Owner | Notes |
|---|---|---|---|
| O-4 | Authenticate `gh` (`gh auth login`) | OPERATOR | Without it, repository state cannot be verified from this machine and workshop OpenReview pages cannot be queried through the API. |
| O-5 | Obtain the venue's LaTeX template from the venue itself, once O-3 is settled | agent | Fetched, never reconstructed. Until then `paper/` stays empty. |
| O-6 | Retrieve the four paywalled statistics references, or record final failure | agent | Tracked individually in `audit/LEDGER_CITATIONS.md`. A preprint is not a substitute for the version of record when a specific theorem is being attributed. |
| O-7 | Re-run the prior-art sweep against OpenReview and Google Scholar before submission | agent | The originating plan's sweep covered neither. |

## Pre-push checklist

Run all of these; each must be empty before `git push`.

```bash
# 1. toplevel assertion — never stage from a directory whose toplevel is $HOME
test "$(git rev-parse --show-toplevel)" = "$HOME/Desktop/Sim-Attrib"

# 2. commit metadata and messages
git log --format='%an|%ae|%B' | grep -iE 'claude|anthropic|co-authored|generated with'

# 3. tracked file contents  (see DEVIATIONS.md D-1 for why this is scoped to tracked files)
git ls-files -z | xargs -0 grep -IiE 'claude|anthropic'

# 4. authorship of every commit
git log --format='%an <%ae> | %cn <%ce>' | sort -u   # expect exactly one line
```
