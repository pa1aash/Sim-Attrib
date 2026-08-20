# Outstanding actions

> ## ⏰ NINE DAYS TO THE NEURIPS 2026 DEADLINE
>
> **29 August 2026, 23:59 AoE.** Verified against the venue's own CFP and the OpenReview
> API (`duedate` 2026-08-30 11:59 UTC). Notification 29 September, and NeurIPS's own
> guidance says that date **"cannot be extended under any circumstances."**
>
> All four candidate venues share the same deadline, so **missing it closes NeurIPS 2026
> entirely** — there is no sequential fallback. See `audit/VENUE.md`.
>
> Against that: `src/` and `results/` are empty, and the plan's own effort estimate is
> 2–3 weeks. The full 5-page paper as designed cannot be built, run, and written in nine
> days. The honest options are the **2-page Tiny Paper track** at Sim2Science carrying
> the identifiability result plus the rank diagnostic, or **skipping NeurIPS 2026**
> — everything here is non-archival, so a later venue costs nothing. **Operator decision:
> Q-1 in `docs/OPEN_QUESTIONS.md`.**

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
