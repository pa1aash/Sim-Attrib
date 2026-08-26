"""Unit tests for src/baselines/montel_marginal.py (W16-2).

Exercises the trials-corrected global-null machinery against synthetic arrays (fast, no
simulator calls) plus one small end-to-end smoke test against the real simulator at
sizes far below the production N_REF/N_CALIB, to catch a wiring bug without paying the
production run's cost.
"""

from __future__ import annotations

import numpy as np

from src.baselines.montel_marginal import (
    calibrate_global_null,
    cp_upper_bound_zero_count,
    evaluate,
    local_p_values,
    local_test_statistics,
)
from src.simulators.sir3 import BASE, with_params


def test_local_test_statistics_zero_at_the_mean():
    mu = np.array([1.0, 2.0, 3.0])
    sigma = np.array([1.0, 1.0, 1.0])
    t = local_test_statistics(mu, mu, sigma)
    assert np.allclose(t, 0.0)


def test_local_test_statistics_grows_with_deviation():
    mu = np.zeros(3)
    sigma = np.ones(3)
    small = local_test_statistics(np.array([1.0, 0.0, 0.0]), mu, sigma)
    large = local_test_statistics(np.array([3.0, 0.0, 0.0]), mu, sigma)
    assert large[0] > small[0]
    assert small[1] == large[1] == 0.0


def test_local_p_values_extreme_observation_gets_small_p():
    rng = np.random.default_rng(0)
    t_ref = rng.chisquare(df=1, size=(2000, 4))
    t_obs_extreme = np.array([50.0, 0.0, 0.0, 0.0])  # far in the upper tail of coordinate 0
    p = local_p_values(t_obs_extreme, t_ref)
    assert p[0] < 0.01
    # a coordinate matching the median of its null distribution should NOT be extreme
    t_obs_typical = np.array([50.0, float(np.median(t_ref[:, 1])), 0.0, 0.0])
    p2 = local_p_values(t_obs_typical, t_ref)
    assert p2[1] > 0.1


def test_local_p_values_never_exactly_zero():
    """The +1/(n+1) form must never report a literal zero p-value (module docstring)."""
    rng = np.random.default_rng(1)
    t_ref = rng.chisquare(df=1, size=(500, 3))
    t_obs = np.array([1e6, 1e6, 1e6])  # far beyond anything in t_ref
    p = local_p_values(t_obs, t_ref)
    assert np.all(p > 0.0)
    assert np.allclose(p, 1.0 / 501.0)


def test_calibrate_global_null_is_uniform_ish_under_null():
    """Under H0, the global test's own null minima should behave like genuine p-values:
    plugging the reference batch's OWN distribution back in as 'calibration' data should
    produce minima spread across (0, 1], not clustered at one extreme -- the vacuous-flag
    test (S5) applied to the calibration machinery itself, before it ever sees real data."""
    rng = np.random.default_rng(2)
    t_ref = rng.chisquare(df=1, size=(3000, 5))
    t_calib = rng.chisquare(df=1, size=(1000, 5))
    m_calib = calibrate_global_null(t_ref, t_calib)
    assert m_calib.min() > 0.0
    # trials-corrected: with 5 roughly-independent tests, the minimum of 5 uniforms has
    # mean ~1/6, not ~1/2 -- so this checks it lands in a sane trials-corrected range,
    # not that it is itself uniform.
    assert 0.05 < float(np.mean(m_calib)) < 0.4


def test_cp_upper_bound_zero_count_matches_rule_of_three():
    # -ln(0.05)/n approximates the exact bound for large n
    n = 10_000
    bound = cp_upper_bound_zero_count(n)
    approx = -np.log(0.05) / n
    assert abs(bound - approx) / approx < 0.01


def test_cp_upper_bound_decreases_with_more_trials():
    assert cp_upper_bound_zero_count(100) > cp_upper_bound_zero_count(10_000)


def test_evaluate_end_to_end_smoke():
    """Small end-to-end run against the real simulator: does the whole pipeline wire up?

    Sizes far below production (N_REF/N_CALIB in the module are 5000/2000); this only
    checks that evaluate() runs and returns a self-consistent, well-formed result.
    """
    from src.simulators.summaries import SUMMARY_LABELS, SUMMARY_SETS

    labels = list(SUMMARY_LABELS["S_B"])
    fn = SUMMARY_SETS["S_B"]
    seed = 999_000
    n = 200

    rows = []
    for r in range(n):
        out = __import__("src.simulators.sir3", fromlist=["simulate"]).simulate(
            (0.0, 0.0, 0.0), seed=seed + r, params=BASE)
        rows.append(fn(out))
    batch = np.asarray(rows, dtype=float)
    mu, sigma = batch.mean(axis=0), batch.std(axis=0, ddof=1)

    ref_rows = []
    for r in range(n):
        out = __import__("src.simulators.sir3", fromlist=["simulate"]).simulate(
            (0.0, 0.0, 0.0), seed=seed + 1_000 + r, params=BASE)
        ref_rows.append(fn(out))
    t_ref = np.array([local_test_statistics(np.asarray(s), mu, sigma) for s in ref_rows])

    calib_rows = []
    for r in range(n):
        out = __import__("src.simulators.sir3", fromlist=["simulate"]).simulate(
            (0.0, 0.0, 0.0), seed=seed + 2_000 + r, params=BASE)
        calib_rows.append(fn(out))
    t_calib = np.array([local_test_statistics(np.asarray(s), mu, sigma) for s in calib_rows])
    m_calib = calibrate_global_null(t_ref, t_calib)

    # H0 true (eta = 0): the global test should typically NOT reject (S5).
    r_null = evaluate((0.0, 0.0, 0.0), BASE, seed + 3_000, mu=mu, sigma=sigma, t_ref=t_ref,
                      m_calib=m_calib, labels=labels)
    assert 0.0 < r_null["global_p_value"] <= 1.0
    assert r_null["argmin_coordinate_label"] in labels

    # A large, obvious distortion should get a smaller global p-value than the null case.
    r_dist = evaluate((0.0, 0.5, 0.0), with_params(families="base"), seed + 4_000, mu=mu,
                      sigma=sigma, t_ref=t_ref, m_calib=m_calib, labels=labels)
    assert r_dist["global_p_value"] <= r_null["global_p_value"]
