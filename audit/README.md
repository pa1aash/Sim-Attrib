# audit/

The governance layer: what the plan asserted, what was checked, and what the check found.

**Belongs here:**
- `PLAN_SOURCE.md` — the originating planning document, byte-for-byte unchanged.
- `LEDGER_ASSERTIONS.md` — every checkable factual assertion in the plan, numbered,
  each with confirming evidence, refuting evidence, and a verification status.
- `LEDGER_CITATIONS.md` — every reference named in the plan, with identifier, retrieval
  status, and whether the plan's characterisation of it is accurate.
- `LEDGER_DESIGN.md` — design commitments and the consequence of violating each.
- `FINAL_CLAIMS.md` *(G7)* — **the current claim set, and the file a drafting session
  works from.** Four contributions, scoped by `docs/DECISIONS.md` D-16, each with the
  exact claim, its evidence files, its scope conditions, and the figures that support it.
- `CLAIM_GRAPH.md` — **SUPERSEDED by `FINAL_CLAIMS.md`.** C1 and C2, their dependencies,
  and which ledger entries each rests on. Kept as the reasoning trail; its dependency
  graph has been stale since G2 and is not to be read as current.
- `TOOLING.md`, `VENUE.md`, `PIVOT.md`, `S0_REPORT.md`.

**Does not belong here:** full text of third-party papers. Bibliographic facts and
short quotations for verification are fine; retrieved article bodies stay in the local
research vault, which is gitignored and never redistributed.

The distinction this directory exists to enforce: the plan is a set of *assertions by its
author*, not a set of *verified facts*. Nothing in the plan is treated as established
merely because the plan states it.

## Provenance of `PLAN_SOURCE.md`

`PLAN_SOURCE.md` is the originating planning document, moved here unchanged from
`S2-simulator-discrepancy-attribution.md` at the repository root. It is **not edited**.
Corrections, disagreements, and refutations are recorded in the ledgers alongside it, so
that the plan as it stood can always be compared against what verification found.

```
file:    audit/PLAN_SOURCE.md
sha256:  2ff70482ef31fbaa7aa75b46f0bab72123af156d0575ecc9da58412f975ae689
bytes:   9015
lines:   139
ingested: 2026-08-20
```

The digest was verified against the expected value both before and after the move and
matched on both sides. Any future change to this file changes the digest and is a
governance failure, not an edit.
