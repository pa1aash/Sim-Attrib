"""Provenance headers for results files.

``PROVENANCE.md`` requires that any number in this repository be traceable, without human
memory, to the script that computed it, the results file that captured it, the git commit
of the working tree at the moment it was computed, and the seed and exact command line
that produced it. This module builds that header. It is the only place the header's shape
is defined, so a results file cannot drift from the contract by being written by hand.

``dirty: true`` is permitted during exploration and is DISQUALIFYING for any number that
reaches the manuscript: a dirty tree means the recorded commit does not describe the code
that ran.
"""

from __future__ import annotations

import platform
import subprocess
import sys
from datetime import datetime, timezone
from typing import Any


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=False
    ).stdout.strip()


def _dep_versions() -> str:
    parts = []
    for mod in ("numpy", "scipy", "yaml"):
        try:
            m = __import__(mod)
            name = "pyyaml" if mod == "yaml" else mod
            parts.append(f"{name}=={m.__version__}")
        except Exception:  # pragma: no cover - a missing optional dep is reported, not fatal
            parts.append(f"{mod}==UNAVAILABLE")
    return ", ".join(parts)


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def header(*, script: str, command: str, seed: int, started: str) -> dict[str, Any]:
    """Build the provenance header required by ``PROVENANCE.md``."""
    # `dirty` means what PROVENANCE.md says it means: THE RECORDED COMMIT DOES NOT DESCRIBE
    # THE CODE THAT RAN. That is a statement about tracked files, so it is computed with
    # `-uno` (tracked modifications only).
    #
    # Using plain `--porcelain` here was a real defect and it is worth stating why, because
    # the failure was silent and self-inflicted: a run writes its own results files into
    # `results/`, those files are untracked at the moment they are written, so every file
    # after the first saw a non-empty `git status` and recorded `dirty: true`. The flag was
    # therefore GUARANTEED true for all but the first output of any multi-file run, which
    # made it carry no information at all while looking like it did. A provenance flag that
    # is always tripped is worse than none: it trains a reader to ignore it.
    #
    # Untracked paths are still recorded, separately and without prejudice, because a run's
    # own outputs are expected to appear there and an unexpected entry is worth seeing.
    tracked = _git("status", "--porcelain", "-uno")
    untracked = _git("ls-files", "--others", "--exclude-standard")
    dirty_paths = sorted(line[3:] for line in tracked.splitlines() if line[3:])
    return {
        "script": script,
        "commit": _git("rev-parse", "HEAD") or "UNKNOWN",
        "dirty": bool(tracked),
        "dirty_paths": dirty_paths,
        "untracked_paths": sorted(p for p in untracked.splitlines() if p),
        "command": command,
        "seed": seed,
        "started": started,
        "finished": now_iso(),
        "host": platform.node(),
        "python": sys.version.split()[0],
        "deps": _dep_versions(),
    }
