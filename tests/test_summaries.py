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


def test_peak_interpolation_LOCATION_is_continuous_where_the_discrete_argmax_moves():
    """The peak LOCATION is continuous across a switch of the discrete argmax.

    Renamed and re-scoped in session G4. As originally written this test was named
    "..._is_continuous_..." without qualification and discarded the height it computed, while
    its docstring asserted that *"both parabolas agree there"* -- a claim about BOTH statistics.
    It also used a symmetric parabola, for which the two outer neighbours are equal and the
    height jump is **identically zero by construction**, so it could not have failed however
    wrong the general claim was. See `test_peak_interpolation_HEIGHT_jumps_...` below and
    `audit/G3_ADVERSARIAL_REVIEW.md` finding 4.

    The location claim is true, including for asymmetric curves, and that is what is pinned
    here -- now on an asymmetric curve, so it is a test rather than a tautology.
    """
    x = np.arange(21.0)
    for skew in (0.0, 0.35):
        prev = None
        for centre in np.linspace(9.0, 11.0, 401):
            y = -(x - centre) ** 2 + 5.0 + skew * x   # skew != 0 makes the neighbours unequal
            loc, _h = peak_interpolated(y)
            if prev is not None:
                assert abs(loc - prev) < 0.02, f"location jumped at skew={skew}"
            prev = loc


def test_peak_interpolation_HEIGHT_jumps_where_the_discrete_argmax_moves():
    """The peak HEIGHT is NOT continuous across a switch of the discrete argmax.

    Write the three points at the switch as ``a = y[i-1]``, ``m = y[i] = y[i+1]``,
    ``c = y[i+2]``. From the left the vertex height is ``m + (m-a)/8``; from the right it is
    ``m + (m-c)/8``. Equal only when ``a == c``. The interpolation therefore removes the
    discontinuity from peak time and leaves one in peak height, of size ``(a-c)/8``.

    This is asserted rather than merely noted because `src/simulators/summaries.py` documents
    the opposite, and because peak height is a coordinate of both `S_A` and `S_C`. Whether the
    discontinuity is ever actually crossed by the diagnostic is a separate, empirical question
    -- `results/robustness/summary_smoothness_check.yaml` answers it.
    """
    a, c = 8.0, 5.0
    m, eps = 10.0, 1e-9
    left = peak_interpolated(np.array([1.0, a, m, m - eps, c, 1.0]))
    right = peak_interpolated(np.array([1.0, a, m - eps, m, c, 1.0]))

    assert left[0] == pytest.approx(right[0], abs=1e-6), "location should NOT jump"
    assert left[1] == pytest.approx(m + (m - a) / 8, abs=1e-6)
    assert right[1] == pytest.approx(m + (m - c) / 8, abs=1e-6)
    assert abs(right[1] - left[1]) == pytest.approx(abs(a - c) / 8, abs=1e-6)
    assert abs(right[1] - left[1]) > 0.3, "the height jump is real, not a rounding artefact"


def test_peak_height_is_continuous_when_the_outer_neighbours_are_equal():
    """The one case in which the docstring's claim IS true, pinned so the boundary is visible.

    A test that only ever exercised this case is what let the general claim stand unchallenged,
    so it is kept -- labelled as the special case it is, next to the general one above.
    """
    m, eps = 10.0, 1e-9
    left = peak_interpolated(np.array([1.0, 7.0, m, m - eps, 7.0, 1.0]))
    right = peak_interpolated(np.array([1.0, 7.0, m - eps, m, 7.0, 1.0]))
    assert left[1] == pytest.approx(right[1], abs=1e-6)


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
