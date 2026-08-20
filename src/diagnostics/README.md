# src/diagnostics/

Diagnostics computed from simulations alone, with no observed data.

**Belongs here:** the Jacobian rank/coherence diagnostic — the summary Jacobian
d(summaries)/d(per-component perturbation), its rank, its condition number, and the
pairwise coherence between component directions. This diagnostic *gates everything
downstream*: it decides before any inference is run whether components are separable
for a given simulator and summary set.

This directory also owns the STOP condition. If the rank diagnostic reports that
components are inseparable under any reasonable summary set, the correct output of this
project is a negative identifiability result, not an attribution method.

**Does not belong here:** anything that requires observed data, anything that requires a
fitted posterior, and any procedure that selects a component. Selection lives in
`../attribution/`.

Empty. The diagnostic is the first technical deliverable of the next session.
