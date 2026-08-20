"""The one place every visual decision in this project lives -- session G7.

WHY THIS FILE EXISTS BEFORE ANY FIGURE DOES
--------------------------------------------
No figure existed anywhere in this repository until session G7. Seven were commissioned at
once. Written one at a time they would have become seven visual identities -- seven palettes,
seven font sizes, seven ideas of how wide a figure is -- and a reader would see that before
they saw any result. So the style is fixed here, once, and every figure script imports
:func:`apply_style` and :func:`save` rather than touching ``rcParams`` itself.

THE PAGE GEOMETRY IS READ FROM THE VENUE'S TEMPLATE, NOT ASSUMED
-----------------------------------------------------------------
``paper/neurips_2026_template/neurips_2026.sty`` sets ``textwidth=5.5in`` inside its
``\\newgeometry`` block, and the workshop options this project uses
(``docs/DECISIONS.md`` D-2: Sim2Science, ``dblblindworkshop``) do not change it -- the
geometry block is unconditional. :func:`template_facts` parses those values out of the style
file at import time and :func:`_check_template` asserts they still match the constants below.
**That check can fail**: if the template is ever re-fetched and the venue has changed its
geometry or its body font, every figure in this project is silently the wrong size, and this
is where that gets caught rather than at submission.

THE FONT
--------
The same style file sets ``\\renewcommand{\\rmdefault}{ptm}``, which is Times. Figures are
therefore set in Times, so that a label inside a figure and the caption beneath it are the
same typeface. ``mathtext`` uses STIX, which is metrically designed against Times, so an
inline ``$\\kappa$`` in an axis label does not arrive from a different family.

**A gap, stated rather than hidden (standing constraint S7).** Matplotlib will render with
whatever Times-compatible face the machine has. This machine has *Times New Roman*; a machine
without it falls through :data:`SERIF_STACK` to Nimbus Roman and then to DejaVu Serif, and
DejaVu is **not** Times-metric. :func:`apply_style` reports which face it actually resolved,
and :func:`resolved_serif` is recorded in every figure's provenance sidecar, so a figure set
in the wrong face is visible in the record rather than only to the eye.

SIZES
-----
The venue's own floors, read from the same style file, are the sizes used here:
``\\footnotesize`` is forced to no smaller than 8pt and ``\\scriptsize`` to no smaller than
7pt, with ``\\tiny`` at 6pt as the absolute floor. Figures are drawn at their final printed
width, so a point inside a figure is a point on the page: **8pt for labels, 7pt for tick
labels, and nothing below 6pt anywhere.** :func:`apply_style` sets those and
:func:`assert_no_text_below_floor` re-checks a finished figure against them, because an
``ax.text`` call with an explicit ``fontsize`` bypasses ``rcParams`` entirely.

THE PALETTE, AND THE ONE RULE THAT GOVERNS IT
-----------------------------------------------
**Okabe-Ito**, the eight-colour qualitative set designed for the two common forms of colour
vision deficiency, and legible in greyscale by luminance ordering. It is chosen over
matplotlib's default cycle and over ColorBrewer because it is the only widely used set whose
*design criterion* is deuteranope and protanope separability rather than aesthetic balance,
and because it prints. Reference: Okabe & Ito, *Color Universal Design* (2002).

Eight colours have to cover more than eight roles across this project's figures, so the
colours are assigned to **roles** and a figure may use only one role scale at a time:

* :data:`COMPONENT` -- transmission / progression / observation. The simulator's three
  mechanisms, in the order ``src/simulators/sir3.COMPONENTS`` lays out the Jacobian's columns.
* :data:`FAMILY` -- base / adversarial / union (the six-column K = 6 object).
* :data:`SUMMARY` -- S_A / S_B / S_C.

:data:`COMPONENT` and :data:`FAMILY` are disjoint, so a figure showing mechanisms under two
family sets is unambiguous. :data:`SUMMARY` deliberately reuses two of :data:`FAMILY`'s
colours, because the project's summary sets and its family sets never appear in one legend --
and :func:`assert_scales_do_not_collide` refuses at draw time if a script tries, rather than
producing a figure in which orange means two things.

Annotation -- thresholds, gates, reference lines, arrows -- is **achromatic** by rule
(:data:`RULE`, :data:`FAINT`), so that every coloured thing on a page is a data category and
nothing else is.

OUTPUT
------
**PDF is the deliverable**; a low-resolution PNG is written beside it as
``<stem>.preview.png`` for quick visual review and is named that way so it cannot be mistaken
for a submission asset. The two schematics additionally emit an editable ``.svg`` source, so
that a later session can move a box without re-deriving the drawing; the figure script stays
canonical and a divergence between the two is a defect in the SVG. Fonts are embedded as TrueType (``pdf.fonttype = 42``) rather than
Type 3, which is what NeurIPS's own instructions ask for and what makes text in the figure
selectable and searchable.

METADATA, AND STANDING CONSTRAINT S1
--------------------------------------
Matplotlib stamps ``Creator: Matplotlib v3.x, https://matplotlib.org`` and a ``CreationDate``
into every PDF it writes, and ``Software: Matplotlib version...`` into every PNG. **There is
no ``savefig.metadata`` rcParam** -- verified against ``matplotlib.rcParams`` on this machine,
not assumed -- so metadata cannot be set globally and must be passed at each ``savefig`` call.
That is precisely why :func:`save` exists and why no figure script may call ``savefig``
directly: it is the only way to guarantee that every file this project emits carries the
metadata this project chose. :func:`save` overwrites ``Creator`` and ``Producer`` with the
emitting script's own identity, and drops ``CreationDate`` entirely -- which also makes the
output **byte-reproducible**, so the hash a provenance sidecar records is a hash of the
figure's content rather than of the minute it was drawn.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

REPO = Path(__file__).resolve().parents[2]
TEMPLATE_STY = REPO / "paper" / "neurips_2026_template" / "neurips_2026.sty"


def _rel(path: Path) -> str:
    """Repo-relative where possible, absolute otherwise. Tests write outside the repo."""
    try:
        return str(path.resolve().relative_to(REPO))
    except ValueError:
        return str(path)

# ---------------------------------------------------------------------------------------
# PAGE GEOMETRY -- the constants, and the template values they are checked against
# ---------------------------------------------------------------------------------------

#: Text width of the venue's page, inches. From neurips_2026.sty's \newgeometry block.
TEXTWIDTH_IN: float = 5.5

#: A figure spanning the full text column. Drawn at final printed size: no \includegraphics
#: scaling, so a point in the figure is a point on the page.
FIG_FULL: float = TEXTWIDTH_IN

#: Two figures side by side, with a 0.14in gutter.
FIG_HALF: float = (TEXTWIDTH_IN - 0.14) / 2.0

#: Two-thirds width, for a figure that needs more than half but should not fill the column.
FIG_TWOTHIRDS: float = TEXTWIDTH_IN * 2.0 / 3.0

#: The venue's LaTeX body font family code, from \renewcommand{\rmdefault}{...}.
TEMPLATE_RMDEFAULT: str = "ptm"

#: Serif stack, most Times-faithful first. See the module docstring on what a fall-through
#: to DejaVu costs and how it is made visible rather than silent.
SERIF_STACK: tuple[str, ...] = (
    "Times New Roman", "Times", "Nimbus Roman", "Nimbus Roman No9 L",
    "Liberation Serif", "STIX Two Text", "DejaVu Serif",
)

# ---------------------------------------------------------------------------------------
# TYPE SIZES -- the venue's own floors
# ---------------------------------------------------------------------------------------

SIZE_LABEL: float = 8.0    #: axis labels, legends, annotations. \footnotesize floor.
SIZE_TICK: float = 7.0     #: tick labels. \scriptsize floor.
SIZE_TITLE: float = 8.0    #: panel titles. Captions live in LaTeX, not in the figure.
SIZE_SMALL: float = 6.0    #: absolute floor. \tiny. Used only where nothing else fits.

# ---------------------------------------------------------------------------------------
# THE PALETTE -- Okabe & Ito (2002)
# ---------------------------------------------------------------------------------------

OKABE_ITO: dict[str, str] = {
    "black": "#000000",
    "orange": "#E69F00",
    "sky_blue": "#56B4E9",
    "bluish_green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "reddish_purple": "#CC79A7",
}

#: The simulator's three mechanisms. Column order of every Jacobian in this repository.
COMPONENT: dict[str, str] = {
    "transmission": OKABE_ITO["sky_blue"],
    "progression": OKABE_ITO["orange"],
    "observation": OKABE_ITO["bluish_green"],
}

#: The declared distortion family sets, plus their six-column union.
FAMILY: dict[str, str] = {
    "base": OKABE_ITO["blue"],
    "adversarial": OKABE_ITO["vermillion"],
    "union": OKABE_ITO["reddish_purple"],
}

#: The three summary sets. Reuses two FAMILY colours -- see the module docstring, and
#: :func:`assert_scales_do_not_collide`, which is what stops that being a defect.
SUMMARY: dict[str, str] = {
    "S_A": OKABE_ITO["orange"],
    "S_B": OKABE_ITO["blue"],
    "S_C": OKABE_ITO["reddish_purple"],
}

SCALES: dict[str, dict[str, str]] = {
    "COMPONENT": COMPONENT, "FAMILY": FAMILY, "SUMMARY": SUMMARY,
}

# Achromatic annotation. Every coloured mark on a page is a data category; nothing else is.
INK: str = "#1A1A1A"      #: text and axis spines
RULE: str = "#4D4D4D"     #: pre-registered thresholds, gates, reference lines
FAINT: str = "#B3B3B3"    #: grid, minor guides, censored regions
PANEL: str = "#FFFFFF"    #: figure and axes background

#: Line styles that survive greyscale printing, in the order figures should reach for them.
DASHES: tuple[tuple[int, tuple[int, ...]] | tuple[int, tuple[()]], ...] = (
    (0, ()), (0, (4, 1.6)), (0, (1, 1.4)), (0, (5, 1.4, 1, 1.4)),
)


# ---------------------------------------------------------------------------------------
# the template check -- read, do not assume
# ---------------------------------------------------------------------------------------

def template_facts(path: Path = TEMPLATE_STY) -> dict[str, Any]:
    """Geometry and body font parsed out of the venue's own style file.

    Returns ``{"textwidth_in", "textheight_in", "rmdefault", "source"}``. Raises if the file
    is absent, because a figure sized against a template nobody read is a guess.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"the venue template is not in this repository at {path}. Figure geometry is read "
            f"from it and must not be guessed -- see paper/README.md.")
    text = path.read_text(encoding="utf-8", errors="replace")
    tw = re.search(r"textwidth\s*=\s*([0-9.]+)in", text)
    th = re.search(r"textheight\s*=\s*([0-9.]+)in", text)
    rm = re.search(r"\\renewcommand\{\\rmdefault\}\{([a-z]+)\}", text)
    if not (tw and th and rm):
        raise ValueError(
            f"could not parse geometry or body font out of {path}. The template's shape has "
            f"changed; figure sizes in src/viz/style.py must be revisited, not patched around.")
    return {
        "source": _rel(path),
        "textwidth_in": float(tw.group(1)),
        "textheight_in": float(th.group(1)),
        "rmdefault": rm.group(1),
    }


def _check_template() -> dict[str, Any]:
    """Assert the constants above still describe the committed template."""
    facts = template_facts()
    if abs(facts["textwidth_in"] - TEXTWIDTH_IN) > 1e-9:
        raise ValueError(
            f"the venue template's textwidth is {facts['textwidth_in']}in but this module is "
            f"built for {TEXTWIDTH_IN}in. Every figure would be the wrong size on the page.")
    if facts["rmdefault"] != TEMPLATE_RMDEFAULT:
        raise ValueError(
            f"the venue template's body font is {facts['rmdefault']!r}, not "
            f"{TEMPLATE_RMDEFAULT!r} (Times). Figure text would not match caption text.")
    return facts


def resolved_serif() -> str:
    """The serif face matplotlib will actually use, resolved against installed fonts.

    Recorded in every figure's provenance sidecar. See the module docstring: a fall-through
    past the Times-metric faces is a real defect in the output and this is what makes it
    visible in the record.
    """
    from matplotlib.font_manager import FontProperties, findfont
    fp = FontProperties(family=list(SERIF_STACK))
    return Path(findfont(fp)).name


# ---------------------------------------------------------------------------------------
# the style itself
# ---------------------------------------------------------------------------------------

def apply_style() -> dict[str, Any]:
    """Apply the project's one style. Every figure script calls this and nothing else.

    Returns the facts a provenance sidecar should record: the template values the geometry
    was checked against, the serif face that resolved, and the matplotlib version.
    """
    facts = _check_template()
    matplotlib.use("Agg")
    plt.rcdefaults()
    plt.rcParams.update({
        # --- fonts ---------------------------------------------------------------------
        "font.family": "serif",
        "font.serif": list(SERIF_STACK),
        "mathtext.fontset": "stix",
        "font.size": SIZE_LABEL,
        "axes.labelsize": SIZE_LABEL,
        "axes.titlesize": SIZE_TITLE,
        "xtick.labelsize": SIZE_TICK,
        "ytick.labelsize": SIZE_TICK,
        "legend.fontsize": SIZE_LABEL,
        "figure.titlesize": SIZE_TITLE,
        # --- colour --------------------------------------------------------------------
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "figure.facecolor": PANEL,
        "axes.facecolor": PANEL,
        "savefig.facecolor": PANEL,
        "axes.prop_cycle": plt.cycler(color=[
            OKABE_ITO["blue"], OKABE_ITO["vermillion"], OKABE_ITO["bluish_green"],
            OKABE_ITO["orange"], OKABE_ITO["reddish_purple"], OKABE_ITO["sky_blue"],
            OKABE_ITO["black"],
        ]),
        # --- geometry of the axes ------------------------------------------------------
        "axes.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 2.5,
        "ytick.major.size": 2.5,
        "xtick.minor.width": 0.4,
        "ytick.minor.width": 0.4,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "lines.linewidth": 1.2,
        "lines.markersize": 3.5,
        "grid.color": FAINT,
        "grid.linewidth": 0.4,
        "legend.frameon": False,
        "legend.handlelength": 1.8,
        "legend.labelspacing": 0.3,
        "legend.columnspacing": 1.2,
        "legend.borderaxespad": 0.3,
        # --- output --------------------------------------------------------------------
        "figure.dpi": 200,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.01,
        "pdf.fonttype": 42,      # TrueType, not Type 3. NeurIPS asks for embedded fonts.
        "ps.fonttype": 42,
        "pdf.compression": 6,
        "svg.fonttype": "none",
        "svg.hashsalt": "sim-attrib",   # deterministic element ids
    })
    return {
        "template": facts,
        "resolved_serif_face": resolved_serif(),
        "matplotlib_version": matplotlib.__version__,
        "palette": "Okabe-Ito (Okabe & Ito 2002), colour-vision-deficiency safe",
        "type_sizes_pt": {"label": SIZE_LABEL, "tick": SIZE_TICK, "floor": SIZE_SMALL},
        "figure_widths_in": {"full": FIG_FULL, "two_thirds": FIG_TWOTHIRDS, "half": FIG_HALF},
    }


def assert_scales_do_not_collide(scales: Iterable[str]) -> None:
    """Refuse to draw a figure that uses two role scales sharing a colour.

    **This is a check that can fail, and here is what makes it fail:** a script asking for
    ``COMPONENT`` and ``SUMMARY`` in one figure, because ``S_A`` and ``progression`` are both
    Okabe-Ito orange. It raises rather than emitting a figure in which one colour means two
    things and only a careful reader notices.
    """
    names = list(scales)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            shared = set(SCALES[a].values()) & set(SCALES[b].values())
            if shared:
                clash = {
                    f"{a}:{k}": v for k, v in SCALES[a].items() if v in shared
                } | {f"{b}:{k}": v for k, v in SCALES[b].items() if v in shared}
                raise ValueError(
                    f"scales {a} and {b} share {sorted(shared)} -- {clash}. One colour would "
                    f"mean two things in one figure. Use one scale, or encode the second "
                    f"dimension with line style (style.DASHES) or marker.")


def assert_no_text_below_floor(fig: Figure, floor: float = SIZE_SMALL) -> None:
    """Every text element in the figure is at least ``floor`` points.

    ``rcParams`` does not govern an explicit ``fontsize=`` argument, so this walks the
    finished figure instead of trusting the configuration. It fails on any label a script set
    smaller than the venue's own ``\\tiny``.
    """
    offenders = [
        (t.get_text()[:40], t.get_fontsize())
        for t in fig.findobj(match=lambda o: hasattr(o, "get_fontsize"))
        if t.get_fontsize() < floor - 1e-9 and getattr(t, "get_text", lambda: "")()
    ]
    if offenders:
        raise ValueError(
            f"text below the {floor}pt floor: {offenders}. The venue forces \\tiny to 6pt; "
            f"anything smaller is unreadable in print.")


def save(fig: Figure, path: str | Path, *, script: str, preview: bool = True,
         svg: bool = False) -> dict[str, Any]:
    """Write the figure as PDF, plus a low-resolution PNG preview beside it.

    **The only sanctioned way to write a figure in this project.** No script may call
    ``fig.savefig`` directly, because metadata cannot be set through ``rcParams`` (there is no
    ``savefig.metadata`` key) and a direct call would silently stamp the plotting library's
    identity and a wall-clock timestamp into the file. Standing constraint **S1** extends the
    authorship grep to figure metadata, and this is where that is enforced rather than checked
    afterwards.

    ``CreationDate`` is dropped, which also makes the PDF byte-reproducible: re-running a
    figure script on unchanged data produces an identical file, so the hash in its provenance
    sidecar describes the figure's content rather than the minute it was drawn.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    assert_no_text_below_floor(fig)

    pdf_meta = {
        "Title": path.stem,
        "Author": "",
        "Subject": "Sim-Attrib",
        "Keywords": "",
        "Creator": script,
        "Producer": script,
        "CreationDate": None,
    }
    fig.savefig(path.with_suffix(".pdf"), format="pdf", metadata=pdf_meta)
    written = [path.with_suffix(".pdf")]
    if svg:
        # An editable vector source, for the two schematics: a later session can nudge a box
        # in an SVG editor without re-deriving the drawing. The .py remains canonical -- the
        # SVG is a convenience, and a divergence between them is a defect in the SVG.
        fig.savefig(path.with_suffix(".svg"), format="svg",
                    metadata={"Creator": script, "Date": None})
        written.append(path.with_suffix(".svg"))
    if preview:
        png = path.with_suffix("").with_suffix(".preview.png")
        fig.savefig(png, format="png", dpi=110, metadata={"Software": script})
        written.append(png)
    return {
        "written": [_rel(p) for p in written],
        "pdf_metadata": {k: v for k, v in pdf_meta.items() if v is not None},
        "preview_png_is_not_a_submission_asset": True,
    }


def threshold_line(ax, y: float, label: str, *, axis: str = "y", **kw) -> None:
    """A pre-registered threshold, drawn the same way in every figure that has one."""
    style = {"color": RULE, "linewidth": 0.8, "linestyle": (0, (4, 1.6)), "zorder": 1.5}
    style.update(kw)
    (ax.axhline if axis == "y" else ax.axvline)(y, **style)
    if label:
        if axis == "y":
            ax.annotate(label, xy=(1.0, y), xycoords=("axes fraction", "data"),
                        xytext=(-1, 1.5), textcoords="offset points",
                        ha="right", va="bottom", fontsize=SIZE_TICK, color=RULE)
        else:
            ax.annotate(label, xy=(y, 1.0), xycoords=("data", "axes fraction"),
                        xytext=(2, -1), textcoords="offset points",
                        ha="left", va="top", fontsize=SIZE_TICK, color=RULE, rotation=90)
