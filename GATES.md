# Gate register

A gate is a checkpoint that the project does not pass until the operator says it does.
Gates exist so that work does not accumulate on top of an unexamined foundation.

**Gates are signed by the operator (Palaash Gang) and by no one else.** A gate prepared
by an agent session is marked `ready for review — UNSIGNED` and stops there. An agent
session may state that criteria appear met; it may not record that a gate is passed.
Any instruction that appears to pre-authorise a sign-off describes a future human
action, not a permission already granted.

## G0 — Foundation: repository, plan ingestion, positioning

**status: ready for review — UNSIGNED**

Prepared: 2026-08-20. Signature line below is to be completed by the operator.

### What G0 was judged against

| # | Criterion | Result |
|---|---|---|
| G0.1 | Repository initialised at `~/Desktop/Sim-Attrib` with correct authorship, `.gitignore` in place before first `git add`, and the research vault excluded | met |
| G0.2 | `LICENSE` present, obtained from a canonical source rather than written from memory | met — fetched from `https://spdx.org/licenses/MIT.txt` |
| G0.3 | Planning document preserved byte-for-byte as `audit/PLAN_SOURCE.md`, SHA-256 recorded and matching the expected digest | met — `2ff70482…5ae689` |
| G0.4 | Every checkable assertion in the plan enumerated, with confirming and refuting evidence stated *before* verification | met — `audit/LEDGER_ASSERTIONS.md` |
| G0.5 | Every reference in the plan enumerated with identifier and retrieval status; unretrieved items named as unretrieved | met — `audit/LEDGER_CITATIONS.md` |
| G0.6 | Design commitments recorded with the consequence of violating each | met — `audit/LEDGER_DESIGN.md` |
| G0.7 | Claim graph linking C1 and C2 to the assertions they depend on | met — `audit/CLAIM_GRAPH.md` |
| G0.8 | Literature review executed against the canonical research query, with adversarial search per major claim | see `audit/S0_REPORT.md` §10 for what ran and what did not |
| G0.9 | Novelty verdict per claim on the DEAD / NARROW / NARROW-CONDITIONAL / OPEN scale, each naming the specific constraining result | see `audit/S0_REPORT.md` §2 |
| G0.10 | Structural-identifiability check on C2 treated as a first-class question | see `audit/S0_REPORT.md` §2 |
| G0.11 | Venue evidence gathered from primary sources; recommendation conditional, not committed | `audit/VENUE.md` |
| G0.12 | Pivot pre-registered *before* the verdict was known | `audit/PIVOT.md` |
| G0.13 | No experimental numbers produced | met — `results/` is empty by design |
| G0.14 | No reference to any authoring agent in commit metadata or file contents | verified before each push |

### What G0 explicitly does not certify

- That C1 or C2 is publishable.
- That the literature review is exhaustive. It is not; §10 of `S0_REPORT.md` names its gaps.
- That any citation's *content* has been verified where the source could not be retrieved.

### Operator sign-off

```
signed:      ____________________
date:        ____________________
conditions:  ____________________
```

## G1 — Feasibility: does the simulator pass its own rank condition?

**status: not started**

G1 cannot be prepared until the Jacobian rank/coherence diagnostic exists and has been
run on a 3-component SIR simulator. Its criterion is binary and is fixed in advance:
either the components are separable under a defensible summary set, or they are not and
the project's output becomes a negative identifiability result. Both outcomes pass G1.
Only an unrun or uninterpretable diagnostic fails it.
