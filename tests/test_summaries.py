"""Tests for the summary-statistic sets."""

from __future__ import annotations

import numpy as np
import pytest

from src.simulators.sir3 import BASE, simulate
from src.simulators.summaries import (
    GROWTH_WINDOW,
    N_BINS,
    SUMMARY_LABELS,
    SUMMARY_SETS,
    peak_interpolated,
    s_a,
    s_b,
    s_c,
)


def test_summary_set_list_is_closed_at_three():
    """THRESHOLDS §1.1 closes the list. A fourth set requires a DEVIATIONS.md entry."""
    assert set(SUMMARY_SETS) == {"S_A", "S_B", "S_C"}


def test_dimensions_are_as_specified():
    out = simulate(seed=1, stochastic=False)
    assert s_a(out).shape == (4,)
    assert s_b(out).shape == (N_BINS,)
    assert s_c(out).shape == (2,)


def test_labels_match_values():
    out = simulate(seed=1, stochastic=False)
    for name, fn in SUMMARY_SETS.items():
        assert len(SUMMARY_LABELS[name]) == len(fn(out))


def test_s_c_is_strictly_impoverished_relative_to_S_A():
    """S_C's coordinates must be a subset of S_A's, or it is not the same control."""
    assert set(SUMMARY_LABELS["S_C"]) < set(SUMMARY_LABELS["S_A"])


def test_s_c_dimension_is_below_K_so_it_must_fail_by_construction():
    from src.simulators.sir3 import K
    assert len(SUMMARY_LABELS["S_C"]) < K


# --------------------------------------------------------------------------------------
# Parabolic peak interpolation -- the reason peak statistics are differentiable at all.
# --------------------------------------------------------------------------------------

def test_peak_interpolation_recovers_a_known_parabola_vertex():
    x = np.arange(11.0)
    loc, height = peak_interpolated(-(x - 4.3) ** 2 + 7.0)
    assert loc == pytest.approx(4.3, abs=1e-9)
    assert height == pytest.approx(7.0, abs=1e-9)


def test_peak_interpolation_is_continuous_where_the_discrete_argmax_moves():
    """At the switch point the peak sits midway between bins and both parabolas agree.

    This is the only place the interpolated peak could jump, so it is the place to check.
    """
    x = np.arange(21.0)
    prev = None
    for centre in np.linspace(9.0, 11.0, 401):
        loc, _h = peak_interpolated(-(x - centre) ** 2 + 5.0)
        if prev is not None:
            assert abs(loc - prev) < 0.02
        prev = loc


def test_peak_interpolation_falls_back_at_a_boundary():
    y = np.array([5.0, 1.0, 0.5])
    assert peak_interpolated(y) == (0.0, 5.0)


def test_peak_interpolation_overshoot_on_a_plateau_is_bounded():
    """On a flat-topped curve the parabola's vertex sits ABOVE the sampled maximum.

    That is inherent to sub-sample peak interpolation, not a defect -- but an unbounded
    overshoot would be one, so the bound is what gets tested. For a maximum at index i the
    vertex offset is confined to +/- 1/2 a sample and the height excess to at most an eighth
    of the neighbour gap.
    """
    y = np.array([1.0, 2.0, 3.0, 3.0, 3.0, 1.0])
    i = int(np.argmax(y))
    loc, height = peak_interpolated(y)
    assert abs(loc - i) <= 0.5
    assert y[i] <= height <= y[i] + 0.125 * abs(y[i - 1] - y[i + 1])


def test_peak_interpolation_denominator_guard_is_unreachable_via_argmax():
    """The ``denom == 0`` branch in ``peak_interpolated`` is defensive, and provably so.

    ``argmax`` returns the FIRST maximum, so ``y[i-1] < y[i]`` strictly for any interior
    ``i``, hence ``denom = (y0 - y1) + (y2 - y1) < 0``. The guard cannot fire on real input.
    Asserting the invariant here means a future change to the peak rule that breaks it fails
    a test rather than silently reaching dead code.
    """
    rng = np.random.default_rng(0)
    for _ in range(200):
        y = rng.random(12)
        i = int(np.argmax(y))
        if 0 < i < len(y) - 1:
            assert (y[i - 1] - 2 * y[i] + y[i + 1]) < 0


# --------------------------------------------------------------------------------------
# Growth rate.
# --------------------------------------------------------------------------------------

def test_growth_rate_recovers_a_known_exponential():
    from src.simulators.summaries import _growth_rate
    r = 0.11
    t = np.arange(BASE.T_days, dtype=float)
    assert _growth_rate(100.0 * np.exp(r * t)) == pytest.approx(r, rel=1e-10)


def test_growth_rate_floor_is_never_active_on_real_output():
    """The log's one-case floor exists for safety; if it binds, the statistic is not a slope."""
    lo, hi = GROWTH_WINDOW
    for seed in range(5):
        y = simulate(seed=seed).reported
        assert np.all(y[lo:hi] > 1.0), "growth-window incidence dipped to the log floor"


def test_growth_window_sits_before_the_peak():
    out = simulate(seed=1, stochastic=False)
    assert GROWTH_WINDOW[1] < int(np.argmax(out.reported))


# --------------------------------------------------------------------------------------
# Binning.
# --------------------------------------------------------------------------------------

def test_binned_counts_sum_to_the_final_size():
    out = simulate(seed=3)
    assert s_b(out).sum() == pytest.approx(out.reported.sum(), rel=1e-12)


def test_binning_rejects_a_window_that_does_not_divide_evenly():
    from dataclasses import replace
    out = simulate(seed=3, params=replace(BASE, T_days=101))
    with pytest.raises(ValueError, match="not divisible"):
        s_b(out)
