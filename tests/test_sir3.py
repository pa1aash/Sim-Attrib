"""Tests for the simulator and its distortion families.

The identity test comes FIRST, in file order and in intent. If delta_k(.; 0) is not exactly
the base simulator, every Jacobian column is measured from the wrong base point and nothing
downstream means anything.
"""

from __future__ import annotations

import numpy as np
import pytest

from src.simulators.sir3 import (
    BASE,
    COMPONENTS,
    ETA_SCALE,
    K,
    SIR3Params,
    peak_prevalence_fraction,
    prior_predictive_sd,
    simulate,
)
from src.simulators.summaries import SUMMARY_SETS


# --------------------------------------------------------------------------------------
# 1. delta_k(.; 0) == base simulator, EXACTLY. Brief §2.2, checked before anything else.
# --------------------------------------------------------------------------------------

def test_zero_distortion_is_bit_identical_to_base_deterministic():
    base = simulate(seed=11, stochastic=False)
    zero = simulate(np.zeros(K), seed=11, stochastic=False)
    assert np.array_equal(base.true_incidence, zero.true_incidence)
    assert np.array_equal(base.reported, zero.reported)


def test_zero_distortion_is_bit_identical_to_base_stochastic():
    base = simulate(seed=11, stochastic=True)
    zero = simulate(np.zeros(K), seed=11, stochastic=True)
    assert np.array_equal(base.reported, zero.reported)


@pytest.mark.parametrize("k", range(K))
def test_each_family_alone_is_identity_at_zero(k):
    """Set component k's parameter to exactly 0 with the others at 0: must be the base run."""
    eta = np.zeros(K)
    eta[k] = 0.0
    out = simulate(eta, seed=5, stochastic=False)
    base = simulate(seed=5, stochastic=False)
    assert np.array_equal(out.reported, base.reported), f"family {COMPONENTS[k]} not identity at 0"


@pytest.mark.parametrize("k", range(K))
def test_each_family_actually_moves_the_output(k):
    """A family that does nothing would pass the identity test vacuously."""
    eta = np.zeros(K)
    eta[k] = 0.05
    out = simulate(eta, seed=5, stochastic=False)
    base = simulate(seed=5, stochastic=False)
    rel = np.max(np.abs(out.reported - base.reported)) / np.max(base.reported)
    assert rel > 1e-6, f"family {COMPONENTS[k]} has no detectable effect at eta_k=0.05"


# --------------------------------------------------------------------------------------
# 2. Smoothness through zero. Brief §2.2: finite-difference the family itself and confirm
#    there is no discontinuity at eta_k = 0.
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize("k", range(K))
def test_family_is_smooth_through_zero(k):
    """One-sided derivatives at 0 must agree, and the value must be continuous.

    A kink at zero would make the central difference at eta = 0 an average of two different
    derivatives, which is exactly the failure this test exists to exclude.
    """
    h = 1e-4
    ep, em = np.zeros(K), np.zeros(K)
    ep[k], em[k] = h, -h

    y0 = simulate(np.zeros(K), seed=3, stochastic=False).reported
    yp = simulate(ep, seed=3, stochastic=False).reported
    ym = simulate(em, seed=3, stochastic=False).reported

    scale = np.max(np.abs(y0))
    # continuity
    assert np.max(np.abs(yp - y0)) / scale < 1e-2
    assert np.max(np.abs(ym - y0)) / scale < 1e-2

    fwd = (yp - y0) / h
    bwd = (y0 - ym) / h
    denom = max(np.max(np.abs(fwd)), 1e-12)
    assert np.max(np.abs(fwd - bwd)) / denom < 1e-3, (
        f"one-sided derivatives of family {COMPONENTS[k]} disagree at eta=0: not smooth"
    )


@pytest.mark.parametrize("k", range(K))
def test_family_second_difference_is_bounded(k):
    """A discontinuity in the first derivative shows up as an exploding second difference."""
    h = 1e-3
    ep, em = np.zeros(K), np.zeros(K)
    ep[k], em[k] = h, -h
    y0 = simulate(np.zeros(K), seed=3, stochastic=False).reported
    yp = simulate(ep, seed=3, stochastic=False).reported
    ym = simulate(em, seed=3, stochastic=False).reported
    second = (yp - 2 * y0 + ym) / (h * h)
    first = (yp - ym) / (2 * h)
    assert np.max(np.abs(second)) < 1e3 * max(np.max(np.abs(first)), 1.0)


# --------------------------------------------------------------------------------------
# 3. Reproducibility and common random numbers.
# --------------------------------------------------------------------------------------

def test_same_seed_gives_bit_identical_output():
    a = simulate([0.01, -0.02, 0.03], seed=99)
    b = simulate([0.01, -0.02, 0.03], seed=99)
    assert np.array_equal(a.reported, b.reported)


def test_different_seed_gives_different_noise():
    a = simulate(seed=1)
    b = simulate(seed=2)
    assert not np.array_equal(a.reported, b.reported)
    # but the same underlying mean
    assert np.allclose(a.reported_mean, b.reported_mean)


def test_common_random_numbers_cancel_in_the_difference():
    """Under CRN the noise multiplies out of the difference quotient; without it, it does not."""
    h = 1e-4
    ep, em = np.array([h, 0, 0]), np.array([-h, 0, 0])
    crn = (simulate(ep, seed=7).reported - simulate(em, seed=7).reported) / (2 * h)
    no_crn = (simulate(ep, seed=7).reported - simulate(em, seed=8).reported) / (2 * h)
    truth = (simulate(ep, seed=7, stochastic=False).reported
             - simulate(em, seed=7, stochastic=False).reported) / (2 * h)
    scale = np.max(np.abs(truth))
    assert np.max(np.abs(crn - truth)) / scale < 0.5
    assert np.max(np.abs(no_crn - truth)) / scale > 10.0


def test_poisson_noise_model_is_not_differentiable():
    """The negative control behind the lognormal choice: count noise quantises the output.

    Under CRN with a count-valued layer both evaluations are integers, so the difference
    quotient has exactly two behaviours and neither is a derivative:

      * no draw flips between +h and -h  ->  the quotient is EXACTLY ZERO, and shrinking h
        makes this more likely, so the estimator converges confidently to the wrong answer;
      * a draw does flip                 ->  the quotient is O(1/h) and grows without bound.

    Both are present below. The test asserts the failure to converge, not one branch of it.
    """
    hs = (1e-3, 1e-4, 1e-5)
    mags = []
    for h in hs:
        ep, em = np.array([h, 0, 0]), np.array([-h, 0, 0])
        d = (simulate(ep, seed=4, noise_model="poisson").reported
             - simulate(em, seed=4, noise_model="poisson").reported) / (2 * h)
        mags.append(float(np.max(np.abs(d))))

    truth = np.max(np.abs(
        (simulate(np.array([hs[0], 0, 0]), seed=4, stochastic=False).reported
         - simulate(np.array([-hs[0], 0, 0]), seed=4, stochastic=False).reported) / (2 * hs[0])
    ))
    assert truth > 0

    # No h gives an estimate anywhere near the true derivative...
    rel_errors = [abs(m - truth) / truth for m in mags]
    assert min(rel_errors) > 0.5, f"poisson quotients {mags} unexpectedly close to {truth}"
    # ...and the estimates do not agree with each other either.
    assert max(mags) > 100 * max(min(mags), truth * 1e-6)


# --------------------------------------------------------------------------------------
# 4. Guards and constants.
# --------------------------------------------------------------------------------------

def test_eta_shape_is_validated():
    with pytest.raises(ValueError):
        simulate([0.0, 0.0], seed=1)
    with pytest.raises(ValueError):
        simulate([0.0, 0.0, np.nan], seed=1)


def test_transmission_saturation_guard_fires():
    """The saturating-incidence family is undefined where its denominator hits zero."""
    with pytest.raises(ValueError, match="saturation denominator"):
        simulate([-50.0, 0.0, 0.0], seed=1)


def test_p_ref_is_a_property_of_the_undistorted_model():
    """p_ref must not depend on any distortion; it normalises one, so circularity would be fatal."""
    a = peak_prevalence_fraction(BASE)
    b = peak_prevalence_fraction(SIR3Params())
    assert a == b
    assert 0.0 < a < 1.0


def test_eta_scale_is_the_pre_registered_value():
    assert ETA_SCALE == 0.1


def test_prior_predictive_sd_is_positive_for_every_summary_set():
    """A coordinate with zero prior-predictive sd is degenerate and must be dropped."""
    for name, fn in SUMMARY_SETS.items():
        _mean, sd = prior_predictive_sd(fn, n_replicates=40, seed0=123456)
        assert np.all(sd > 0), f"{name} has a degenerate coordinate"


# --------------------------------------------------------------------------------------
# 5. The adversarial family set (session G4). The base branch must be untouched by it, and
#    the adversarial branch must satisfy the SAME identity and movement contracts.
# --------------------------------------------------------------------------------------

ADV = SIR3Params(families="adversarial")


def test_unknown_family_set_is_rejected():
    """A typo must not silently fall through to the base families."""
    with pytest.raises(ValueError):
        SIR3Params(families="advarsarial")


def test_adversarial_families_are_identity_at_zero():
    """delta'_k(.; 0) == the BASE simulator exactly -- the same contract, bit for bit.

    This is the check that makes the two family sets comparable at all. If they disagreed at
    eta = 0 they would be linearised about different points and their Jacobians would not be
    two answers to one question.
    """
    base = simulate(np.zeros(K), seed=11, stochastic=False)
    adv = simulate(np.zeros(K), seed=11, params=ADV, stochastic=False)
    assert np.array_equal(base.true_incidence, adv.true_incidence)
    assert np.array_equal(base.reported, adv.reported)
    b_noisy = simulate(np.zeros(K), seed=11, stochastic=True)
    a_noisy = simulate(np.zeros(K), seed=11, params=ADV, stochastic=True)
    assert np.array_equal(b_noisy.reported, a_noisy.reported)


@pytest.mark.parametrize("k", range(K))
def test_adversarial_families_actually_move_the_output(k):
    """A family that does nothing would pass the identity test vacuously."""
    eta = np.zeros(K)
    eta[k] = 0.05
    out = simulate(eta, seed=5, params=ADV, stochastic=False)
    base = simulate(np.zeros(K), seed=5, params=ADV, stochastic=False)
    rel = np.max(np.abs(out.reported - base.reported)) / np.max(base.reported)
    assert rel > 1e-6, f"adversarial family {COMPONENTS[k]} barely moves the output ({rel:.3g})"


@pytest.mark.parametrize("k", range(K))
def test_adversarial_families_differ_from_the_base_families(k):
    """The point of the set is that it is a DIFFERENT set. If a family were accidentally
    identical to its base counterpart, the re-run would silently re-measure the base result."""
    eta = np.zeros(K)
    eta[k] = 0.05
    base = simulate(eta, seed=5, stochastic=False)
    adv = simulate(eta, seed=5, params=ADV, stochastic=False)
    assert not np.allclose(base.reported, adv.reported), (
        f"adversarial family {COMPONENTS[k]} is indistinguishable from the base family"
    )


def test_adversarial_observation_family_tilts_rather_than_scales():
    """The observation family's whole purpose is that it is NOT a pure amplitude error.

    A pure amplitude error multiplies the reported series by a constant, so the ratio to the
    undistorted series is flat. This one is a log-linear tilt, so the ratio must vary -- and
    must vary by exp(eta), the full swing of the mean-centred modulation across the window.
    """
    eta = np.array([0.0, 0.0, 0.3])
    base = simulate(np.zeros(K), seed=5, params=ADV, stochastic=False).reported
    tilted = simulate(eta, seed=5, params=ADV, stochastic=False).reported
    m = base > 0
    ratio = tilted[m] / base[m]
    assert ratio.max() / ratio.min() > 1.2, "observation family behaved like a pure multiplier"
    assert np.isclose(ratio.max() / ratio.min(), np.exp(0.3 * (BASE.T_days - 1) / BASE.T_days),
                      rtol=1e-6)
