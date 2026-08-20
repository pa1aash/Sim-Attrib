"""The liveness check, run in the state where it is expected to give the opposite answer.

``DEVIATIONS.md`` D-8's stated lesson, applied to the thing that failed in G4: a check that
has only ever been run against a live process is not known to be able to report a dead one.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time

from src import runlock


def _spawn_sleeper(tag: str) -> subprocess.Popen:
    """A real child process whose command line contains ``tag``."""
    return subprocess.Popen([sys.executable, "-c",
                             f"import time; _ = {tag!r}; time.sleep(30)"])


def test_reports_alive_for_a_live_matching_process():
    proc = _spawn_sleeper("marker_alpha")
    try:
        time.sleep(0.4)
        got = runlock.check(proc.pid, expect_module="marker_alpha")
        assert got["alive"], got
        assert got["module_matches"]
    finally:
        proc.kill()
        proc.wait()


def test_reports_dead_for_a_process_that_has_exited():
    """The direction G4's check got wrong was the other one; this is the cheaper half."""
    proc = subprocess.Popen([sys.executable, "-c", "pass"])
    proc.wait()
    time.sleep(0.2)
    got = runlock.check(proc.pid, expect_module="anything")
    assert not got["alive"], got


def test_reports_dead_when_the_pid_has_been_recycled_by_another_process():
    """A live PID is not evidence that MY run is alive. This is the guard that makes it so.

    Fails if the module check is dropped -- which is the natural "simplification" of this
    file, and would turn it back into a check that says ALIVE for any live process.
    """
    proc = _spawn_sleeper("marker_beta")
    try:
        time.sleep(0.4)
        got = runlock.check(proc.pid, expect_module="a_module_that_is_not_running")
        assert not got["alive"], got
        assert got["state"] is not None, "the process must genuinely be alive for this to test anything"
        assert not got["module_matches"]
    finally:
        proc.kill()
        proc.wait()


def test_pidfile_round_trip_and_missing_file(tmp_path):
    # The module token is taken from THIS process's real command line, so the round trip is
    # a genuine one rather than one that happens to match a string chosen to make it pass.
    _state, command = runlock._ps(os.getpid())
    token = command.split()[0]
    p = tmp_path / "run.json"
    runlock.write_pidfile(p, module=token,
                          outputs=["results/robustness/k6_spectrum.yaml"])
    rec = json.loads(p.read_text())
    assert rec["pid"] == os.getpid()
    got = runlock.check_pidfile(p)
    assert got["alive"], got          # this test process is, definitionally, alive
    assert got["outputs"] == ["results/robustness/k6_spectrum.yaml"]
    assert not runlock.check_pidfile(tmp_path / "absent.json")["alive"]


def test_pidfile_for_a_module_that_is_not_running_reads_dead(tmp_path):
    """The half that matters: a stale pidfile must not read as a live run."""
    p = tmp_path / "run.json"
    runlock.write_pidfile(p, module="src.diagnostics.a_module_nobody_is_running",
                          outputs=["results/robustness/k6_spectrum.yaml"])
    got = runlock.check_pidfile(p)
    assert not got["alive"], got


def test_the_check_does_not_match_its_own_command_line():
    """The failure mode in the other direction: a pattern check that matches the checker.

    ``ps -p`` cannot do this, and the assertion pins it: asking about a dead PID while this
    very test process has ``runlock`` in its own command line must still read DEAD.
    """
    proc = subprocess.Popen([sys.executable, "-c", "pass"])
    proc.wait()
    time.sleep(0.2)
    assert not runlock.check(proc.pid, expect_module="runlock")["alive"]
