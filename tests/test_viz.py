"""Tests for the figure pipeline -- session G7, Phase 2.3.

**These run before any real figure is trusted.** A figure is the one artefact in this project
whose defects are invisible to the reader who most needs to see them: a mislabelled axis, a
series drawn from the wrong file, or a number that exists nowhere in ``results/`` all look
exactly like a correct figure. So the pipeline is exercised end to end on **synthetic data
whose right answer is known in advance**, and the provenance check is shown reading FALSE on
each of the four things the module claims can make it read FALSE.

Standing constraint S5. A check that cannot fail is not a check, and a figure-generation
sanity check is exactly the kind of thing that ends up vacuous.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
import yaml

from src.viz import provenance as vp
from src.viz import style

REPO = Path(__file__).resolve().parents[1]


# --------------------------------------------------------------------------------------
# the style: geometry read from the venue's template, not from a constant somebody typed
# --------------------------------------------------------------------------------------

def test_template_geometry_is_parsed_from_the_committed_style_file():
    facts = style.template_facts()
    assert facts["textwidth_in"] == pytest.approx(5.5)
    assert facts["rmdefault"] == "ptm"            # Times
    assert facts["source"].endswith("neurips_2026.sty")


def test_apply_style_checks_the_template_and_reports_what_it_resolved():
    facts = style.apply_style()
    assert facts["template"]["textwidth_in"] == pytest.approx(style.TEXTWIDTH_IN)
    assert facts["figure_widths_in"]["full"] == pytest.approx(5.5)
    # the serif face that actually resolved is recorded, whatever it is
    assert facts["resolved_serif_face"]


def test_template_check_fails_when_the_template_geometry_moves(tmp_path):
    """If the venue re-issues its template with a different column width, every figure in
    this project is the wrong size. This is where that is caught."""
    sty = tmp_path / "neurips_2026.sty"
    sty.write_text(r"""
\renewcommand{\rmdefault}{ptm}
\usepackage[verbose=true,letterpaper]{geometry}
  \newgeometry{ textheight=9in, textwidth=6.75in, top=1in }
""", encoding="utf-8")
    facts = style.template_facts(sty)
    assert facts["textwidth_in"] == pytest.approx(6.75)
    assert facts["textwidth_in"] != pytest.approx(style.TEXTWIDTH_IN)


def test_template_facts_refuses_a_file_it_cannot_parse(tmp_path):
    sty = tmp_path / "broken.sty"
    sty.write_text("% no geometry, no font\n", encoding="utf-8")
    with pytest.raises(ValueError, match="could not parse"):
        style.template_facts(sty)


# --------------------------------------------------------------------------------------
# the palette rules
# --------------------------------------------------------------------------------------

def test_component_and_family_scales_are_disjoint():
    """These two DO appear together -- mechanisms under two family sets -- so they must not
    share a colour. No exception, no documentation, they just must not."""
    style.assert_scales_do_not_collide(["COMPONENT", "FAMILY"])


def test_summary_and_component_scales_collide_and_the_guard_says_so():
    """S_A and progression are both Okabe-Ito orange. A figure asking for both must be
    refused rather than quietly drawn."""
    with pytest.raises(ValueError, match="mean two things"):
        style.assert_scales_do_not_collide(["COMPONENT", "SUMMARY"])


def test_every_palette_colour_is_from_okabe_ito():
    allowed = set(style.OKABE_ITO.values())
    for name, scale in style.SCALES.items():
        assert set(scale.values()) <= allowed, name


def test_component_scale_covers_exactly_the_simulator_s_components():
    from src.simulators.sir3 import COMPONENTS
    assert tuple(style.COMPONENT) == COMPONENTS


# --------------------------------------------------------------------------------------
# the type-size floor, on a figure that violates it
# --------------------------------------------------------------------------------------

def test_a_label_below_the_venue_s_floor_is_refused(tmp_path):
    import matplotlib.pyplot as plt
    style.apply_style()
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.text(0.5, 0.5, "unreadable in print", fontsize=4.0)
    with pytest.raises(ValueError, match="below the 6.0pt floor"):
        style.save(fig, tmp_path / "bad", script="tests/test_viz.py")
    plt.close(fig)


# --------------------------------------------------------------------------------------
# THE SYNTHETIC FIGURE: known input, known expected output
# --------------------------------------------------------------------------------------

SYNTHETIC = {
    "provenance": {"script": "tests/test_viz.py", "commit": "0" * 40, "dirty": False,
                   "seed": 1, "command": "synthetic"},
    "spectrum": {"singular_values": [10.0, 5.0, 2.0, 1.0]},
    "points": {"x": [0.0, 1.0, 2.0, 3.0], "y": [1.0, 4.0, 9.0, 16.0]},
}


def _write_synthetic(tmp_path: Path) -> str:
    """A results file with known contents, placed inside the repo so relative paths work."""
    d = REPO / "results" / "_test_tmp"
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"synthetic_{tmp_path.name}.yaml"
    p.write_text(yaml.safe_dump(SYNTHETIC, sort_keys=False), encoding="utf-8")
    return str(p.relative_to(REPO))


def _cleanup(rel: str) -> None:
    p = REPO / rel
    if p.exists():
        p.unlink()
    d = p.parent
    if d.exists() and not any(d.iterdir()):
        d.rmdir()


def test_the_pipeline_draws_a_known_figure_and_the_drawn_data_is_the_known_data(tmp_path):
    """End to end on synthetic input: the numbers matplotlib actually holds after the call
    are compared against the numbers that went in, and the axis limits against hand-computed
    bounds. This tests the PIPELINE, before any of it is pointed at a real result."""
    import matplotlib.pyplot as plt
    rel = _write_synthetic(tmp_path)
    try:
        facts = style.apply_style()
        prov = vp.FigureProvenance("synthetic", script="tests/test_viz.py")
        doc = prov.source(rel)
        sv = prov.plotted("spectrum", doc["spectrum"]["singular_values"], rel,
                          "spectrum.singular_values")
        x = prov.plotted("x", doc["points"]["x"], rel, "points.x")
        y = prov.plotted("y", doc["points"]["y"], rel, "points.y")

        fig, ax = plt.subplots(figsize=(style.FIG_HALF, 1.6))
        line, = ax.plot(x, y, color=style.FAMILY["base"])
        ax.scatter(range(len(sv)), sv, color=style.FAMILY["adversarial"], s=6)
        ax.set_xlabel("x (dimensionless)")
        ax.set_ylabel("y (dimensionless)")
        style.threshold_line(ax, 5.0, r"$\tau$")
        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(0.0, 20.0)

        # --- what the figure ACTUALLY holds, read back off the artists -----------------
        gx, gy = line.get_data()
        assert list(gx) == SYNTHETIC["points"]["x"]
        assert list(gy) == SYNTHETIC["points"]["y"]
        pts = ax.collections[0].get_offsets()
        assert np.allclose(pts[:, 1], SYNTHETIC["spectrum"]["singular_values"])
        # every plotted point is inside the declared axes bounds -- no silent clipping
        assert ax.get_ylim() == (0.0, 20.0)
        assert max(SYNTHETIC["points"]["y"]) <= ax.get_ylim()[1]
        assert min(SYNTHETIC["spectrum"]["singular_values"]) >= ax.get_ylim()[0]
        # the figure is the width the venue's template gives, to the millimetre
        assert fig.get_size_inches()[0] == pytest.approx(style.FIG_HALF)
        assert style.FIG_HALF * 2 + 0.14 == pytest.approx(5.5)

        out = style.save(fig, tmp_path / "synthetic", script="tests/test_viz.py")
        plt.close(fig)
        assert (tmp_path / "synthetic.pdf").exists()
        assert (tmp_path / "synthetic.preview.png").exists()

        sidecar = prov.write(tmp_path / "synthetic", caption="A synthetic figure.",
                             style_facts=facts, outputs=out)
        assert sidecar["all_checks_pass"] is True
        assert any(c["check"] == "data_matches_source" for c in sidecar["checks"])
        assert (tmp_path / "synthetic.provenance.json").exists()
    finally:
        _cleanup(rel)


def test_the_pdf_carries_no_plotting_library_identity_and_no_timestamp(tmp_path):
    """Standing constraint S1, extended this session to figure metadata. Matplotlib stamps
    its own name and a wall-clock time into every PDF unless told otherwise."""
    import matplotlib.pyplot as plt
    style.apply_style()
    fig, ax = plt.subplots(figsize=(2, 1.2))
    ax.plot([0, 1], [0, 1])
    style.save(fig, tmp_path / "meta", script="src/viz/fig_test.py")
    plt.close(fig)
    raw = (tmp_path / "meta.pdf").read_bytes()
    for token in (b"Matplotlib", b"matplotlib", b"CreationDate"):
        assert token not in raw, f"{token!r} leaked into the PDF"
    png = (tmp_path / "meta.preview.png").read_bytes()
    assert b"matplotlib" not in png.lower()


def test_two_runs_on_unchanged_data_produce_a_byte_identical_pdf(tmp_path):
    """No CreationDate means the hash in a provenance sidecar describes the figure's content
    rather than the minute it was drawn. If this fails, every sidecar hash is noise."""
    import matplotlib.pyplot as plt
    style.apply_style()
    # same stem, different directories: the PDF Title is the stem, so a differing stem would
    # differ legitimately and the test would be measuring the wrong thing
    for run in ("first", "second"):
        d = tmp_path / run
        d.mkdir()
        fig, ax = plt.subplots(figsize=(2, 1.2))
        ax.plot([0, 1, 2], [1, 3, 2], color=style.FAMILY["base"])
        ax.set_xlabel("t (days)")
        style.save(fig, d / "same", script="src/viz/fig_test.py", preview=False)
        plt.close(fig)
    assert (tmp_path / "first" / "same.pdf").read_bytes() == \
        (tmp_path / "second" / "same.pdf").read_bytes()


# --------------------------------------------------------------------------------------
# the provenance check, shown reading FALSE on each thing it claims to catch
# --------------------------------------------------------------------------------------

def test_a_hand_typed_number_in_a_figure_fails_the_check(tmp_path):
    """Case 1 in the module docstring, and the reason the check exists."""
    rel = _write_synthetic(tmp_path)
    try:
        prov = vp.FigureProvenance("synthetic", script="tests/test_viz.py")
        doc = prov.source(rel)
        fudged = list(doc["spectrum"]["singular_values"])
        fudged[2] = 2.5                      # a number that is in no results file
        prov.plotted("spectrum", fudged, rel, "spectrum.singular_values")
        with pytest.raises(ValueError, match="provenance check"):
            prov.write(tmp_path / "bad", caption="c", style_facts={}, outputs={"written": []})
        out = prov.write(tmp_path / "bad", caption="c", style_facts={}, outputs={"written": []},
                         strict=False)
        bad = [c for c in out["checks"] if not c["passes"]]
        assert bad and bad[0]["max_abs_difference"] == pytest.approx(0.5)
    finally:
        _cleanup(rel)


def test_an_undeclared_transform_fails_and_a_declared_one_passes(tmp_path):
    """Case 2. Plotting log10(sigma) while declaring the path to sigma is a real mistake and
    the sidecar has to be the thing that notices."""
    rel = _write_synthetic(tmp_path)
    try:
        sv = SYNTHETIC["spectrum"]["singular_values"]
        prov = vp.FigureProvenance("s", script="tests/test_viz.py")
        prov.source(rel)
        prov.plotted("logged but undeclared", list(np.log10(sv)), rel,
                     "spectrum.singular_values")
        out = prov.write(tmp_path / "u", caption="c", style_facts={}, outputs={"written": []},
                         strict=False)
        assert out["all_checks_pass"] is False

        prov2 = vp.FigureProvenance("s", script="tests/test_viz.py")
        prov2.source(rel)
        prov2.plotted("logged and declared", list(np.log10(sv)), rel,
                      "spectrum.singular_values", transform=("log10", np.log10), tol=1e-12)
        out2 = prov2.write(tmp_path / "d", caption="c", style_facts={},
                           outputs={"written": []})
        assert out2["all_checks_pass"] is True
        assert out2["checks"][-1]["transform"] == "log10"
    finally:
        _cleanup(rel)


def test_a_source_rewritten_during_generation_fails_the_check(tmp_path):
    """Case 3. This project has had long-running jobs writing into results/ while a session
    worked, so it is not hypothetical."""
    rel = _write_synthetic(tmp_path)
    try:
        prov = vp.FigureProvenance("s", script="tests/test_viz.py")
        doc = prov.source(rel)
        prov.plotted("spectrum", doc["spectrum"]["singular_values"], rel,
                     "spectrum.singular_values")
        changed = dict(SYNTHETIC)
        changed["spectrum"] = {"singular_values": [10.0, 5.0, 2.0, 1.0], "extra": True}
        (REPO / rel).write_text(yaml.safe_dump(changed, sort_keys=False), encoding="utf-8")
        out = prov.write(tmp_path / "c", caption="c", style_facts={}, outputs={"written": []},
                         strict=False)
        hashes = [c for c in out["checks"] if c["check"] == "source_unchanged_during_generation"]
        assert hashes and hashes[0]["passes"] is False
    finally:
        _cleanup(rel)


def test_a_path_that_does_not_exist_raises_and_names_itself(tmp_path):
    """Case 4. A results-schema change must break the figure loudly at generation time."""
    rel = _write_synthetic(tmp_path)
    try:
        prov = vp.FigureProvenance("s", script="tests/test_viz.py")
        doc = prov.source(rel)
        prov.plotted("gone", doc["spectrum"]["singular_values"], rel,
                     "spectrum.eigenvalues")
        with pytest.raises(KeyError, match="spectrum.eigenvalues"):
            prov.write(tmp_path / "p", caption="c", style_facts={}, outputs={"written": []})
    finally:
        _cleanup(rel)


def test_plotted_refuses_a_source_whose_hash_was_never_taken(tmp_path):
    prov = vp.FigureProvenance("s", script="tests/test_viz.py")
    with pytest.raises(ValueError, match="hash is unrecorded"):
        prov.plotted("x", [1.0], "results/p_sel.yaml", "stage_A_theta0")


def test_dig_walks_indices_and_pipe_keys():
    doc = {"per_width": [{"by_key": {"AAA|studentised": {"p": 0.25}}}]}
    assert vp.dig(doc, "per_width[0].by_key.AAA|studentised.p") == 0.25
