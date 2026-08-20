"""Figure generation for the manuscript.

Two modules, and the split is deliberate:

* :mod:`src.viz.style` owns every visual decision -- palette, fonts, sizes, output format,
  and the metadata written into each file. There is exactly one place a style decision
  lives, so seven figure scripts cannot drift into seven visual identities.
* :mod:`src.viz.provenance` owns the trace from a figure back to the ``results/*.yaml``
  files it was drawn from. ``PROVENANCE.md`` has required this of figures since session G0
  -- *"Every figure carries, in its caption or in a sidecar file, the results file(s) it
  was drawn from"* -- and this is the first session in which any figure exists.

No figure script computes a number. Figure scripts read ``results/`` and draw.
"""
