# figures/

Every figure the paper needs, in vector PDF at the venue's own column width.
**Generated, never hand-edited.** Each is produced by one script in `src/viz/` and carries a `.provenance.json` sidecar recording the `results/` files it was drawn from, their hashes, the commit that drew it, and its drafted caption.

**`*.preview.png` is a low-resolution preview for quick visual review and is never submitted.** `*.svg` exists only for the two schematics, as an editable source; the `.py` stays canonical and a divergence between them is a defect in the SVG.

| figure | script | sources | data claims checked |
|---|---|---|---|
| `fig1_method` | `src/viz/fig1_method.py` | —  *(schematic; no results data)* | 0 |
| `fig2_simulator` | `src/viz/fig2_simulator.py` | —  *(schematic; no results data)* | 0 |
| `fig3_spectrum` | `src/viz/fig3_spectrum.py` | `results/robustness/k6_spectrum.yaml` | 7 |
| `fig4_assignments` | `src/viz/fig4_assignments.py` | `results/robustness/k6_spectrum.yaml` | 3 |
| `fig5_threshold` | `src/viz/fig5_threshold.py` | `results/robustness/k6_spectrum.yaml`, `results/robustness/threshold_sensitivity.yaml` | 7 |
| `fig6_nontermination` | `src/viz/fig6_nontermination.py` | `results/boundary_sweep.yaml`, `results/cost_gate.yaml` | 11 |
| `fig7_confound` | `src/viz/fig7_confound.py` | `results/robustness/k6_spectrum.yaml` | 9 |

## Regenerating

```bash
for f in fig1_method fig2_simulator fig3_spectrum fig4_assignments \
         fig5_threshold fig6_nontermination fig7_confound; do
    python -m src.viz.$f
done
```

**Regenerate from a committed tree.** A figure drawn from a modified working tree records `dirty: true` in its sidecar, and `PROVENANCE.md` makes that disqualifying for anything reaching the manuscript. `tests/test_viz.py` asserts it for every figure in this directory.

Output is byte-reproducible: re-running a script on unchanged data produces an identical PDF, so a sidecar's hash describes the figure's content rather than the minute it was drawn.

## What has NOT been checked

**Nobody but the session that drew these has looked at them.** The provenance chain verifies that every plotted number is at its declared path in `results/`; it does not verify that the figure is legible, that a caption describes its own figure, or that an annotation placed by hand states the truth. Those are the operator's to check, and `GATES.md` G7 records it as a real limitation rather than a formality.
