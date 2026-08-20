"""Is that long run still alive? A check that answers from the kernel, not from a pattern.

WHY THIS MODULE EXISTS
-----------------------
Standing constraint S3 forbids editing the working tree while a run is in flight, and it has
been violated twice -- session G3 (``DEVIATIONS.md`` D-8) and session G4, which repeated it
within one session of reading D-8 about it. G4 then hit the mirror-image failure:
``audit/S4_REPORT.md`` §7 records that **a faulty liveness check reported a run as dead while
it was alive**, and a second copy was launched against the same output paths. It was caught by
inspecting process state directly rather than by the check.

The defect class is the same one D-8 names, pointed at process state: **a check whose answer
does not actually depend on the thing it claims to be checking.** A liveness check built out of
``pgrep -f <pattern>`` or ``ps aux | grep <pattern> | head`` has three ways to say DEAD about a
live process and none of them is visible when it happens --

  * the pattern does not match the argv the kernel actually holds (``python -m pkg.mod`` is
    three argv entries, and a pattern written against the module path alone can miss);
  * the listing is truncated by a downstream ``head``, or the pipeline's writer is killed by
    ``SIGPIPE`` before the matching line is emitted;
  * the process is a child of the shell that was launched, so the launcher's own exit is
    mistaken for the run's.

and one way to say ALIVE about a dead one: the pattern matches the *checking* command's own
command line.

THE FIX, AND WHY IT CANNOT FAIL THE SAME WAY
---------------------------------------------
Ask about **one PID**, recorded by the run itself at start-up, and ask the kernel directly:
``ps -p <pid>``. There is no listing to truncate, no pattern to mis-write, and no chance of
matching the checker. Two guards on top of that:

  * **PID reuse.** A PID is recycled once its process is reaped, so "PID 4711 exists" is not
    "my run is alive". The pidfile records the expected module, and :func:`check` requires the
    live process's command line to contain it.
  * **Zombies.** A reaped-but-not-collected process still appears in ``ps``. A state field
    beginning ``Z`` is reported as dead.

UNDER WHAT CONDITION DOES THIS READ FALSE?
-------------------------------------------
When the PID is absent from the process table, when it is a zombie, and when the PID has been
recycled by an unrelated process. ``tests/test_runlock.py`` exercises all three against real
processes -- a live one, one that has certainly exited, and a live one whose command line does
not match -- because a liveness check that has only ever been run against a live process is
exactly the check G4 trusted.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any


def write_pidfile(path: str | Path, *, module: str, outputs: list[str]) -> Path:
    """Record this process's PID, the module it is running, and what it will write.

    ``outputs`` is not decoration: it is what a second session must consult before launching
    anything, since the failure S3 guards against is two processes writing the same path.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"pid": os.getpid(), "module": module,
                             "outputs": list(outputs)}, indent=2), encoding="utf-8")
    return p


def _ps(pid: int) -> tuple[str, str] | None:
    """``(state, command)`` for one PID, or ``None`` if the kernel has no such process."""
    r = subprocess.run(["ps", "-p", str(pid), "-o", "state=,command="],
                       capture_output=True, text=True, check=False)
    line = r.stdout.strip()
    if r.returncode != 0 or not line:
        return None
    state, _, command = line.partition(" ")
    return state, command.strip()


def check(pid: int, *, expect_module: str) -> dict[str, Any]:
    """Is PID ``pid`` a live process running ``expect_module``?

    Returns a dict with ``alive`` and the evidence for it. The evidence is returned rather
    than swallowed so a caller that disbelieves the answer can look at what it was based on --
    which is what G4 had to do by hand.
    """
    got = _ps(pid)
    if got is None:
        return {"pid": pid, "alive": False, "reason": "no such process in the process table",
                "state": None, "command": None, "module_matches": False}
    state, command = got
    zombie = state.startswith("Z")
    matches = expect_module in command
    return {
        "pid": pid,
        "alive": bool(not zombie and matches),
        "reason": ("zombie: exited, not yet reaped" if zombie
                   else "PID exists but is a different process — recycled PID" if not matches
                   else "running"),
        "state": state,
        "command": command,
        "module_matches": bool(matches),
    }


def check_pidfile(path: str | Path) -> dict[str, Any]:
    """:func:`check` against a pidfile written by :func:`write_pidfile`."""
    p = Path(path)
    if not p.exists():
        return {"pid": None, "alive": False, "reason": f"no pidfile at {p}",
                "state": None, "command": None, "module_matches": False}
    rec = json.loads(p.read_text(encoding="utf-8"))
    out = check(int(rec["pid"]), expect_module=str(rec["module"]))
    out["outputs"] = rec.get("outputs", [])
    return out
