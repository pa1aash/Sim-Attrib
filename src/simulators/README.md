# src/simulators/

Forward simulators and their component decompositions.

**Belongs here:** the compartmental/ODE simulator (SIR-with-structure), Lotka–Volterra,
and for each a explicit declaration of what its *components* are — because the entire
paper rests on the claim that a simulator decomposes into components whose discrepancy
contributions can in principle be separated. The component decomposition is a modelling
commitment, not an implementation detail, and it is stated in code and in prose.

Also here: the per-component parametric distortion families delta_k(.; eta_k) that
define what "this component is off-spec" means.

**Does not belong here:** diagnostics, attribution logic, or any procedure that
consumes simulator output to make a decision. Those live in the sibling directories,
so that the simulator can be exercised without importing the machinery under test.

**Status, session G3 (2026-08-20):** `sir3.py` implements the three-component SIR simulator
(TRANSMISSION, PROGRESSION, OBSERVATION) with one distortion family per component, and
`summaries.py` implements the closed list of summary sets `S_A`, `S_B`, `S_C`. Lotka-Volterra
is **not** implemented and is not currently planned.
