"""Tests for the provenance header.

`DEVIATIONS.md` **D-8** records that the `dirty` flag was once structurally guaranteed true and
therefore said nothing, and draws the general lesson: *"every check in this project should be
run once in a state where it is expected to give the opposite answer."* **D-10** records that
the `dirty_paths` field added in response to D-8 then silently corrupted the first path it
reported. Both defects were in code with no test. These are those tests.
"""

from __future__ import annotations

import os
import subprocess

from src.provenance import header


def _hdr():
    return header(script="tests/test_provenance.py", command="pytest", seed=0, started="t")


def test_every_dirty_path_actually_exists():
    """The defect D-10 records: the first reported path lost its leading character.

    A path that does not exist is the observable signature of that class of bug, and it is a
    signature no amount of reading the boolean would have revealed. This test fails on a dirty
    tree with the pre-fix code and passes with it fixed; on a clean tree it is vacuous, which
    is stated rather than hidden -- see the companion test below.
    """
    h = _hdr()
    for p in h["dirty_paths"]:
        assert os.path.exists(p), (
            f"provenance reported dirty path {p!r}, which does not exist -- the porcelain "
            f"parse is corrupting paths (DEVIATIONS.md D-10)"
        )
    for p in h["untracked_paths"]:
        assert os.path.exists(p), f"provenance reported untracked path {p!r}, which does not exist"


def test_dirty_paths_matches_what_git_reports():
    """Compare against git's own answer, parsed independently of the module under test.

    `git status --porcelain -z` is NUL-separated and needs no column arithmetic at all, so it
    cannot share the bug being tested for. If the two disagree, the header is wrong.
    """
    raw = subprocess.run(["git", "status", "--porcelain", "-z", "-uno"],
                         capture_output=True, text=True, check=False).stdout
    expected = sorted(rec[3:] for rec in raw.split("\0") if rec[3:])
    assert _hdr()["dirty_paths"] == expected


def test_dirty_is_false_on_a_clean_tree_and_true_otherwise():
    """D-8's lesson made executable: the flag must be able to read BOTH ways.

    Asserting it against git's own emptiness test is the only version of this that works
    wherever it runs -- a test that demanded a clean tree would fail during development, and a
    test that demanded a dirty one would fail in CI.
    """
    raw = subprocess.run(["git", "status", "--porcelain", "-uno"],
                         capture_output=True, text=True, check=False).stdout
    assert _hdr()["dirty"] is bool(raw.strip())


def test_untracked_output_files_do_not_set_dirty():
    """The exact defect D-8 records: a run's own results are untracked and must not count.

    `-uno` is what makes this true, so the test pins it: if someone drops the flag, the header
    starts reporting every run as dirty again, which is how the contract died the first time.
    """
    h = _hdr()
    for p in h["untracked_paths"]:
        assert p not in h["dirty_paths"], f"untracked file {p!r} leaked into dirty_paths"


def test_header_records_a_resolvable_commit():
    h = _hdr()
    assert h["commit"] != "UNKNOWN"
    rc = subprocess.run(["git", "cat-file", "-e", h["commit"] + "^{commit}"], check=False)
    assert rc.returncode == 0, f"recorded commit {h['commit']!r} is not in this repository"
