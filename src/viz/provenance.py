"""The trace from a figure back to the ``results/`` files it was drawn from -- session G7.

WHAT RULE THIS IMPLEMENTS, AND WHY IT IS NEW
---------------------------------------------
``PROVENANCE.md`` has said this since session G0, before any number in this repository
existed::

    Every figure carries, in its caption or in a sidecar file, the results file(s) it was
    drawn from. A figure regenerated from changed results gets a new results file, not an
    edit to the old one.

No figure existed until session G7, so the rule has never had to be honoured. This module
honours it, and extends the same contract the *numbers* already live under -- *"traceable,
without human memory, to the script, the results file, the commit, the seed and the command"*
-- to visual output.

Every figure this project emits is written beside a ``<stem>.provenance.json`` recording:

* every ``results/*.yaml`` that fed it, with that file's **SHA-256 at generation time** and
  the script / commit / seed that its own provenance header says produced it -- so the chain
  runs figure -> results file -> emitting script -> commit, with no step taken on trust;
* the figure script and the repository commit, with the ``dirty`` flag that
  ``PROVENANCE.md`` makes disqualifying for anything reaching the manuscript;
* the **caption**, drafted with the figure rather than months later when its exact content
  has gone cold;
* the style facts -- including which serif face actually resolved on the drawing machine;
* the output files and their hashes.

THE CHECK THAT CAN FAIL, AND EXACTLY WHAT MAKES IT FAIL (standing constraints S5, D-8, D-13)
----------------------------------------------------------------------------------------------
A sidecar listing source files proves only that a script opened them. So each figure also
**declares, per plotted series, the dotted path in the source YAML that series came from**,
via :meth:`FigureProvenance.plotted`, and :meth:`FigureProvenance.write` re-reads the file
from disk and compares.

**Under what condition does ``data_matches_source`` read FALSE?**

1. **A number in the figure is not in the results file.** A script that hand-typed a value,
   or carried a stale one from a previous run, or mis-transcribed a number out of a report,
   has nothing to declare a path for, and declaring a wrong path raises a ``KeyError``
   naming it. **This is the case the check exists for.**
2. **An undeclared transform.** If a script plots ``log10(sigma)`` but declares the path to
   ``sigma``, the comparison fails. Transforms are legitimate and are declared by name
   (``transform=("log10", np.log10)``), so the sidecar records what was done to the numbers
   between the file and the page.
3. **The source file changed under the figure.** The hash is taken when the data is loaded
   and re-verified when the sidecar is written. A concurrent run rewriting ``results/`` --
   which this project has actually had in flight during a session -- trips it.
4. **A path that has moved.** A results-file schema change breaks every figure that reads
   the old shape, loudly, at generation time.

**What it cannot catch, stated so it is not over-trusted.** It cannot catch a figure that
declares a correct path and then draws something else *in addition* -- an annotation, an
arrow, a hand-placed label. It checks the declared series, not the whole canvas. And it
cannot tell whether the declared path is the *right* quantity to plot, only that the plotted
numbers are the ones at that path. Those are judgement calls and they belong to the figure's
caption and to a reader, not to a flag.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

import numpy as np
import yaml

from ..provenance import _git, _git_raw, now_iso

REPO = Path(__file__).resolve().parents[2]

_INDEX = re.compile(r"^(.*?)\[(\d+)\]$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dig(obj: Any, path: str) -> Any:
    """Walk a dotted path with optional ``[i]`` indices into a loaded YAML document.

    ``summary_sets.S_B.base.spectrum.singular_values`` and
    ``per_width[0].by_key.AAA|studentised.reported_min.p_sel`` are both valid. A missing key
    raises ``KeyError`` naming the full path, because a silently-``None`` provenance path is
    worse than none at all.
    """
    cur = obj
    for raw in path.split("."):
        m = _INDEX.match(raw)
        key, idx = (m.group(1), int(m.group(2))) if m else (raw, None)
        if key:
            try:
                cur = cur[key]
            except (KeyError, TypeError, IndexError) as exc:
                raise KeyError(f"{path!r}: no key {key!r} at this level "
                               f"(available: {_keys_of(cur)})") from exc
        if idx is not None:
            try:
                cur = cur[idx]
            except (IndexError, TypeError, KeyError) as exc:
                raise KeyError(f"{path!r}: index [{idx}] out of range") from exc
    return cur


def _keys_of(obj: Any) -> Any:
    if isinstance(obj, dict):
        return sorted(obj)[:12]
    if isinstance(obj, list):
        return f"<list of {len(obj)}>"
    return type(obj).__name__


class FigureProvenance:
    """Accumulates a figure's sources and claims, then writes its sidecar.

    Usage in a figure script::

        prov = FigureProvenance("figure3_spectrum", script="src/viz/fig3_spectrum.py")
        k6 = prov.source("results/robustness/k6_spectrum.yaml")
        sv = prov.plotted("S_B base spectrum",
                          k6["summary_sets"]["S_B"]["base"]["spectrum"]["singular_values"],
                          "results/robustness/k6_spectrum.yaml",
                          "summary_sets.S_B.base.spectrum.singular_values")
        ...
        prov.write(figure_path, caption="...", style_facts=facts, outputs=written)
    """

    def __init__(self, name: str, *, script: str) -> None:
        self.name = name
        self.script = script
        self.started = now_iso()
        self._sources: dict[str, dict[str, Any]] = {}
        self._loaded: dict[str, Any] = {}
        self._claims: list[dict[str, Any]] = []
        self._notes: list[str] = []

    # -- loading ------------------------------------------------------------------------
    def source(self, rel: str) -> Any:
        """Load one ``results/`` file, recording its hash and its own provenance header."""
        path = REPO / rel
        if not path.exists():
            raise FileNotFoundError(f"figure source {rel} does not exist")
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        head = doc.get("provenance", {}) if isinstance(doc, dict) else {}
        self._sources[rel] = {
            "path": rel,
            "sha256_at_load": sha256(path),
            "bytes": path.stat().st_size,
            "emitted_by": {
                "script": head.get("script"),
                "commit": head.get("commit"),
                "dirty": head.get("dirty"),
                "seed": head.get("seed"),
                "command": head.get("command"),
            },
        }
        self._loaded[rel] = doc
        return doc

    def note(self, text: str) -> None:
        """A fact about the figure that a reader of the sidecar needs and the data lacks."""
        self._notes.append(text)

    # -- claims -------------------------------------------------------------------------
    def plotted(
        self,
        label: str,
        values: Any,
        source: str,
        path: str,
        *,
        transform: tuple[str, Callable[[Any], Any]] | None = None,
        tol: float = 0.0,
    ) -> Any:
        """Declare that ``values`` are what sits at ``path`` in ``source``, and return them.

        ``transform`` names and supplies any operation applied between the file and the page.
        ``tol`` is an absolute tolerance, defaulting to **exact**: a figure normally plots the
        recorded number unchanged, and a nonzero tolerance is a statement that it does not.
        """
        if source not in self._loaded:
            raise ValueError(f"{source} was not loaded through .source() -- its hash is unrecorded")
        self._claims.append({
            "label": label, "source": source, "path": path,
            "transform": transform[0] if transform else "identity",
            "tolerance": float(tol),
            "_values": values, "_fn": transform[1] if transform else None,
        })
        return values

    # -- verification and writing --------------------------------------------------------
    def _verify(self) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for rel, rec in self._sources.items():
            now = sha256(REPO / rel)
            rows.append({
                "check": "source_unchanged_during_generation", "source": rel,
                "passes": bool(now == rec["sha256_at_load"]),
                "sha256_at_load": rec["sha256_at_load"], "sha256_now": now,
            })
        # Re-read each source ONCE, from disk, at write time. Re-reading is the point -- it
        # is what detects a file rewritten under the figure -- but re-reading per claim
        # re-parses a 40,000-line YAML nine times for one figure, which is minutes.
        reread: dict[str, Any] = {}
        for claim in self._claims:
            if claim["source"] not in reread:
                reread[claim["source"]] = yaml.safe_load(
                    (REPO / claim["source"]).read_text(encoding="utf-8"))
            doc = reread[claim["source"]]
            recorded = dig(doc, claim["path"])
            expected = claim["_fn"](recorded) if claim["_fn"] else recorded
            got = claim["_values"]
            a, b = np.atleast_1d(np.asarray(expected, dtype=float)), \
                np.atleast_1d(np.asarray(got, dtype=float))
            same_shape = a.shape == b.shape
            if same_shape:
                both_nan = np.isnan(a) & np.isnan(b)
                diff = np.where(both_nan, 0.0, np.abs(a - b))
                worst = float(np.nanmax(diff)) if diff.size else 0.0
                ok = bool(np.all(both_nan | (diff <= claim["tolerance"])))
            else:
                worst, ok = float("inf"), False
            rows.append({
                "check": "data_matches_source", "label": claim["label"],
                "source": claim["source"], "path": claim["path"],
                "transform": claim["transform"], "tolerance": claim["tolerance"],
                "n_values": int(b.size), "shapes_agree": same_shape,
                "max_abs_difference": worst, "passes": ok,
            })
        return rows

    def write(
        self,
        figure_stem: str | Path,
        *,
        caption: str,
        style_facts: dict[str, Any],
        outputs: dict[str, Any],
        strict: bool = True,
    ) -> dict[str, Any]:
        """Verify every claim, then write ``<figure_stem>.provenance.json``.

        With ``strict`` (the default) a failed check raises instead of writing a sidecar that
        records its own failure. The failure is the point: a figure whose data does not match
        its source must not reach a reader, and a warning in a JSON file nobody opens is not a
        gate. ``strict=False`` exists for the test suite, which needs to see the flag read
        FALSE without the process dying.
        """
        checks = self._verify()
        failed = [c for c in checks if not c["passes"]]
        stem = Path(figure_stem)
        if not stem.is_absolute():
            stem = REPO / stem
        tracked = _git_raw("status", "--porcelain", "-uno")
        doc = {
            "figure": self.name,
            "generated_by": {
                "script": self.script,
                "commit": _git("rev-parse", "HEAD") or "UNKNOWN",
                "dirty": bool(tracked.strip()),
                "dirty_paths": sorted(l[3:] for l in tracked.splitlines() if l[3:]),
                "started": self.started,
                "finished": now_iso(),
            },
            "caption": caption,
            "sources": list(self._sources.values()),
            "checks": checks,
            "all_checks_pass": not failed,
            "what_would_make_data_matches_source_read_false": (
                "a number in the figure that is not at the declared path in the declared "
                "results file: a hand-typed value, a stale value carried from an earlier run, "
                "a transform applied but not declared, a source file rewritten by a "
                "concurrent run between load and write, or a results-schema change that moved "
                "the path. It does NOT check un-declared annotations, and it cannot say "
                "whether the declared path is the right quantity to plot."),
            "style": style_facts,
            "outputs": outputs,
            "output_hashes": {},
            "notes": self._notes,
        }
        for rel in outputs.get("written", []):
            p = Path(rel) if Path(rel).is_absolute() else REPO / rel
            if p.exists():
                doc["output_hashes"][rel] = sha256(p)
        if failed and strict:
            raise ValueError(
                f"figure {self.name}: {len(failed)} provenance check(s) failed and no sidecar "
                f"was written -- " + "; ".join(
                    f"{c['check']}({c.get('label') or c.get('source')}): "
                    f"max_abs_difference={c.get('max_abs_difference')}" for c in failed))
        out = stem.with_suffix("").with_suffix(".provenance.json")
        out.write_text(json.dumps(doc, indent=2, sort_keys=False) + "\n", encoding="utf-8")
        return doc


def caption_of(figure_stem: str | Path) -> str:
    """Read back a figure's drafted caption. For the drafting session, and for tests."""
    stem = Path(figure_stem)
    if not stem.is_absolute():
        stem = REPO / stem
    p = stem.with_suffix("").with_suffix(".provenance.json")
    return json.loads(p.read_text(encoding="utf-8"))["caption"]


def all_figures(figdir: str | Path = "figures") -> list[dict[str, Any]]:
    """Every sidecar under ``figdir``, for a session report or an index table."""
    root = REPO / figdir
    return [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(root.glob("*.provenance.json"))]
