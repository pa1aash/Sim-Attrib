"""Tests for the ``p_sel`` measurement.

The load-bearing one is the first: the whole measurement rests on a claimed IDENTITY between
the memoised null draw and a full ``simulate`` call, and an identity that is merely
approximate would silently change every number downstream. It is checked at several nuisance
points and several seeds, to floating point, and the test is written so that it fails if the
memoisation ever stops being exact.
"""

from __future__ import annotations

import numpy as np
import pytest

from src.diagnostics import p_sel as ps
from src.simulators.sir3 import BASE, K, simulate, with_params
from src.simulators.summaries import SUMMARY_SETS


def test_null_summaries_are_bit_identical_to_calling_simulate():
    """The identity the measurement's affordability rests on. Not 'close': identical."""
    fn = SUMMARY_SETS[ps.SUMMARY_SET]
    thetas = [
        {},
        {"beta": 0.35 * 1.2, "gamma": 0.14 * 0.8},
        {"rho": 0.40 * 1.5, "I0": 10.0 * 0.5, "obs_sigma": 0.15 * 1.4},
    ]
    for theta in thetas:
        seed0 = 777_000
        got = ps.null_summaries(theta, seed0, 6)
        params = with_params(**theta)
        want = np.asarray([fn(simulate(np.zeros(K), seed=seed0 + r, params=params))
                           for r in range(6)], dtype=float)
        assert np.array_equal(got, want), f"memoised draws differ at theta={theta}"


def test_null_summaries_would_notice_a_wrong_seed_offset():
    """The companion: the identity test above is only meaningful if a WRONG mapping from
    draw index to seed would fail it. Shifting the seeds by one must break equality."""
    fn = SUMMARY_SETS[ps.SUMMARY_SET]
    seed0 = 777_000
    got = ps.null_summaries({}, seed0, 4)
    shifted = np.asarray([fn(simulate(np.zeros(K), seed=seed0 + 1 + r, params=BASE))
                          for r in range(4)], dtype=float)
    assert not np.array_equal(got, shifted)


def test_the_two_family_sets_give_identical_null_draws():
    """One set of null draws serves both family assignments only because of this."""
    a = simulate(np.zeros(K), seed=99, params=with_params(families="adversarial"))
    b = simulate(np.zeros(K), seed=99, params=with_params(families="base"))
    assert np.array_equal(a.reported, b.reported)


def test_the_nuisance_grid_is_the_declared_design_and_nothing_else():
    grid = ps.nuisance_grid(ps.BOX_HALF_WIDTHS)
    per_width = 2 ** len(ps.NUISANCE_COORDS) + 2 * len(ps.NUISANCE_COORDS)
    assert len(grid) == len(ps.BOX_HALF_WIDTHS) * per_width
    assert len({p["key"] for p in grid}) == len(grid), "duplicate design points"
    for pt in grid:
        for c, v in pt["theta"].items():
            base = float(getattr(BASE, c))
            assert abs(abs(v / base - 1.0) - pt["width"]) < 1e-12 or v == base


def test_every_grid_point_is_a_legal_parameter_vector():
    """`SIR3Params.__post_init__` rejects impossible parameters. A design point that could
    not be simulated would silently drop out of the minimum and understate the cost."""
    for pt in ps.nuisance_grid(ps.BOX_HALF_WIDTHS):
        with_params(**pt["theta"])


def test_the_headline_box_is_one_of_the_measured_ones():
    assert ps.HEADLINE_BOX in ps.BOX_HALF_WIDTHS


def test_wilson_pins_its_boundaries_exactly():
    assert ps.wilson(0, 100_000)[0] == 0.0
    assert ps.wilson(100_000, 100_000)[1] == 1.0


def test_load_jacobian_identifies_the_step_size_by_reproducing_the_record():
    """The representative `h` is not assumed: it is the one whose spectrum reproduces what
    `results/robustness/k6_spectrum.yaml` records. If none did, the run aborts."""
    for code in ps.FAMILY_CODES:
        j = ps.load_jacobian(code)
        assert j["reproduces"], code
        assert j["max_relative_difference_to_recorded_spectrum"] < 1e-10
        sv = np.linalg.svd(j["J"], compute_uv=False)
        assert abs(sv[0] / sv[-1] - j["recorded_condition_number"]) < 1e-8


def test_load_normalisation_matches_a_freshly_computed_one():
    """The constants the selection rule sits in must be the ones the Jacobian was normalised
    by, or the rule and the Jacobian are in different coordinate systems."""
    norm = ps.load_normalisation()
    rows = ps.null_summaries({}, norm["seed0"], 200)
    # 200 replicates is not 2000, so this is a sanity check on the same population rather
    # than an equality: the recorded sd must be inside a generous band of the short estimate.
    assert np.all(np.abs(rows.std(axis=0, ddof=1) / norm["sd"] - 1.0) < 0.35)
    assert np.all(np.abs(rows.mean(axis=0) / norm["mean"] - 1.0) < 0.10)
