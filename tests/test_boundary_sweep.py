"""Tests for the boundary sweep -- session G7, Phase 1.

The shape criterion is the only thing in this session that converts a table of numbers into
a WORD, so it is the thing that has to be shown coming out every way it can. Standing
constraint S5: a check that cannot fail is not a check, and the CENSORED_BELOW branch is the
one that makes the classification falsifiable rather than decorative.
"""

from __future__ import annotations

import math

import pytest

from src.diagnostics.boundary_sweep import (
    NOISE_MAGNITUDE_SQRT_D,
    SLOPE_RATIO_ABRUPT,
    WIDTHS,
    classify_shape,
    gate_row,
    loglinear_fit,
    two_proportion_z,
)
from src.diagnostics.cost_gate import GATE_DRAWS, M_VALUES, N_VALUES


# --------------------------------------------------------------------------------------
# the pre-registered design constants
# --------------------------------------------------------------------------------------

def test_widths_are_strictly_increasing_and_inside_the_measured_range():
    assert list(WIDTHS) == sorted(WIDTHS)
    assert len(set(WIDTHS)) == len(WIDTHS)
    assert WIDTHS[0] > 0.0
    # The sweep must not extrapolate past the width G6 already measured, and its top end must
    # BE that width, or the reproduction check at 0.05 has nothing to compare against.
    assert WIDTHS[-1] == 0.05


def test_the_sweep_is_denser_where_the_boundary_was_predicted_to_be():
    """Q-16 predicted 0.002-0.02. At least half the widths must lie there, or the design does
    not do what its docstring says it does."""
    inside = [w for w in WIDTHS if 0.002 <= w <= 0.02]
    assert len(inside) >= len(WIDTHS) / 2


def test_noise_magnitude_is_sqrt_of_S_B_dimension():
    assert NOISE_MAGNITUDE_SQRT_D == pytest.approx(math.sqrt(10.0))


# --------------------------------------------------------------------------------------
# the shape criterion, shown coming out all three ways
# --------------------------------------------------------------------------------------

def test_shape_is_censored_when_the_smallest_width_is_already_dead():
    """The branch that makes the classification refuse rather than guess."""
    out = classify_shape([0.0, 0.001, 0.002, 0.005, 0.01], [0.0, 0.0, 0.0, 0.0, 0.0])
    assert out["shape"] == "CENSORED_BELOW"
    assert out["shape_is_determined"] is False
    assert out["slope_ratio"] is None


def test_shape_is_censored_when_there_are_too_few_live_widths():
    out = classify_shape([0.0, 0.001, 0.002, 0.005], [0.2, 0.1, 0.0, 0.0])
    assert out["shape"] == "CENSORED_BELOW"
    assert out["shape_is_determined"] is False
    assert out["n_live_widths"] == 2


def test_shape_is_gradual_on_a_pure_exponential_decay():
    """log10 p linear in w with a constant slope: every local slope is identical, so the ratio
    is exactly 1 and the criterion cannot call it a threshold."""
    ws = [0.0, 0.005, 0.010, 0.015, 0.020, 0.025]
    ps = [0.25 * 10 ** (-100.0 * w) for w in ws]
    out = classify_shape(ws, ps)
    assert out["shape"] == "GRADUAL"
    assert out["shape_is_determined"] is True
    assert out["slope_ratio"] == pytest.approx(1.0, abs=1e-9)
    assert out["loglinear_fit"]["slope_b_decades_per_unit_half_width"] == pytest.approx(-100.0)
    assert out["loglinear_fit"]["r_squared"] == pytest.approx(1.0)


def test_shape_is_abrupt_when_one_interval_carries_the_collapse():
    """Flat, flat, cliff, flat. The criterion must name the cliff and say where it is."""
    ws = [0.0, 0.005, 0.010, 0.015, 0.020]
    ps = [0.25, 0.24, 0.23, 1e-6, 9e-7]
    out = classify_shape(ws, ps)
    assert out["shape"] == "ABRUPT"
    assert out["slope_ratio"] >= SLOPE_RATIO_ABRUPT
    assert out["steepest_interval"] == [0.010, 0.015]


def test_the_two_shapes_are_separated_by_the_declared_threshold_and_not_by_taste():
    """Immediately either side of SLOPE_RATIO_ABRUPT the answer must differ. Without this the
    threshold could be any number and nothing would notice."""
    # three equal slopes of -1 decade per unit, then one steeper by a chosen factor
    def series(factor: float) -> tuple[list[float], list[float]]:
        ws = [0.0, 0.01, 0.02, 0.03, 0.04]
        logs = [0.0, -1.0, -2.0, -3.0, -3.0 - factor]
        return ws, [10.0 ** (v - 1) for v in logs]

    lo_w, lo_p = series(SLOPE_RATIO_ABRUPT * 0.9)
    hi_w, hi_p = series(SLOPE_RATIO_ABRUPT * 1.1)
    assert classify_shape(lo_w, lo_p)["shape"] == "GRADUAL"
    assert classify_shape(hi_w, hi_p)["shape"] == "ABRUPT"


def test_loglinear_fit_refuses_on_too_few_points():
    out = loglinear_fit([0.0, 0.01], [0.2, 0.02])
    assert out["fitted"] is False


# --------------------------------------------------------------------------------------
# the gate row, which must reach all three verdicts
# --------------------------------------------------------------------------------------

def test_gate_row_passes_when_every_corner_is_inside_the_registered_threshold():
    worst_corner = max(M_VALUES) * max(N_VALUES)
    p = 10.0 * worst_corner / GATE_DRAWS          # comfortably affordable at every corner
    out = gate_row(p, p * 0.99, p * 1.01)
    assert out["verdict"] == "PASS"
    assert all(r["passes"] for r in out["corners"])


def test_gate_row_fails_at_zero_acceptances_and_the_cost_is_infinite():
    out = gate_row(0.0, 0.0, 3.84e-5)
    assert out["verdict"] == "FAIL"
    assert all(math.isinf(r["expected_draws"]) for r in out["corners"])
    # the CI upper end still gives a finite BOUND, which is the number the paper quotes
    assert all(math.isfinite(r["expected_draws_ci95_lower"]) for r in out["corners"])


def test_gate_row_splits_between_the_cheapest_and_dearest_declared_corners():
    """The specification gives M and N as RANGES, so a p_sel between the two extremes leaves
    the gate undecided by the specification's own numbers. That is a fact about the
    specification and the verdict has to be able to say it."""
    cheap = min(M_VALUES) * min(N_VALUES)
    dear = max(M_VALUES) * max(N_VALUES)
    p = math.sqrt(cheap * dear) / GATE_DRAWS      # geometric mean of the two flip points
    out = gate_row(p, p * 0.99, p * 1.01)
    assert out["verdict"] == "SPLIT"
    assert any(r["passes"] for r in out["corners"])
    assert not all(r["passes"] for r in out["corners"])


def test_gate_row_carries_the_notice_that_it_decides_nothing():
    """S3: this sweep cannot reopen D-16, and the results file has to say so where a reader
    of a single row would see it."""
    out = gate_row(0.5, 0.49, 0.51)
    assert "D-16" in out["this_is_characterisation_not_a_decision"]


# --------------------------------------------------------------------------------------
# the theta_0 reproduction test, and the wrong instrument it replaced (DEVIATIONS.md D-17)
# --------------------------------------------------------------------------------------

def test_two_proportion_z_is_zero_on_identical_estimates():
    assert two_proportion_z(2500, 10_000, 0.25, 10_000) == pytest.approx(0.0)


def test_two_proportion_z_uses_both_measurements_sampling_errors():
    """The defect this replaced, stated as arithmetic rather than as prose.

    Two estimates from n = 100,000 each, separated by exactly 1.96 standard errors of ONE of
    them. The old check -- 'is the new estimate inside the old one's 95% interval?' -- calls
    that a non-reproduction. A two-proportion test, which knows both estimates are noisy,
    puts it at 1.96/sqrt(2) = 1.39 and does not.
    """
    n = 100_000
    p = 0.25
    se_one = math.sqrt(p * (1 - p) / n)
    x1 = round((p + 1.959963984540054 * se_one) * n)
    z = two_proportion_z(x1, n, p, n)
    assert abs(z) == pytest.approx(1.959963984540054 / math.sqrt(2.0), rel=1e-2)
    assert abs(z) < 1.959963984540054          # the old check would have rejected this pair
    assert abs(z) < SLOPE_RATIO_ABRUPT         # and it is nowhere near THETA0_Z_MAX = 3.0


def test_two_proportion_z_does_reject_a_genuine_disagreement():
    """The replacement is not merely more permissive: it still fires on a real difference.
    Half a percentage point at n = 100,000 each is roughly 2.6 sigma; a full point is over
    five, and no threshold anyone would set survives that."""
    n = 100_000
    assert abs(two_proportion_z(26_000, n, 0.25, n)) > 5.0
    assert abs(two_proportion_z(35_000, n, 0.25, n)) > 40.0


def test_theta0_z_threshold_is_stated_and_conventional():
    from src.diagnostics.boundary_sweep import THETA0_Z_MAX
    assert THETA0_Z_MAX == 3.0
