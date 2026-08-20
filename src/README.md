# src/

All executable code: simulators, perturbation bases, diagnostics, and attribution
procedures. Subdirectories are `simulators/`, `diagnostics/`, and `attribution/`.

**Belongs here:** deterministic, seeded, runnable code. Every script that emits a
number must write that number to a file in `results/` and must record the seed, the
git commit of the working tree, and its own path in the output. `PROVENANCE.md`
defines the required shape of that record.

**Does not belong here:** results, figures, notebooks used as scratch space, or
anything that reads real observational data. This project is synthetic by design —
ground truth is known by construction because a component is deliberately knocked
off-spec.

Nothing in this directory exists yet. No code has been written for this project.
