"""Tests for the selection rule that defines the cell ``p_sel`` is a probability of.

Every check here is written so that it FAILS against a broken version of the thing it
checks -- ``DEVIATIONS.md`` D-8's standing rule. Where a test asserts a good input is
accepted there is a companion test requiring a bad one to be refused.
"""

from __future__ import annotations

import numpy as np
import pytest

from src.attribution.selection import build_rule
from src.diagnostics.jacobian_rank import KAPPA_MAX, TAU
from src.simulators.sir3 import COMPONENTS, K

D = 10


def _rule(J, variant="studentised", tau=TAU, kappa_max=KAPPA_MAX):
    d = J.shape[0]
    return build_rule(summary_set="S_B", family_code="TEST", variant=variant,
                      m0=np.zeros(d), sd=np.ones(d), J=J, component_labels=COMPONENTS[:J.shape[1]],
                      tau=tau, kappa_max=kappa_max)


def _well_conditioned(seed=0, d=D, k=K):
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(rng.standard_normal((d, d)))
    return q[:, :k] * np.array([3.0, 2.0, 1.0])[:k]


def test_pseudo_inverse_recovers_a_planted_eta_exactly():
    """`J^+ J = I` is what the specification means by 'sensitive to eta_k, insensitive to
    eta_j'. If this fails, the rule is not the rank-conditioned procedure it claims to be."""
    J = _well_conditioned()
    rule = _rule(J, variant="plain")
    for k in range(K):
        eta = np.zeros(K)
        eta[k] = 1.7
        recovered = rule.eta_hat(J @ eta)
        assert np.allclose(recovered, eta, atol=1e-10)
        assert rule.select(J @ eta) == k


def test_selection_sees_the_summary_vector_and_nothing_else():
    """The hard constraint of `src/attribution/README.md`: no path by which the identity of
    a knocked-off component can reach the attributor. Feeding the SAME summary vector twice
    under contradictory labelling must give the same answer, and it does because the answer
    is a function of that vector alone."""
    J = _well_conditioned()
    rule = _rule(J)
    s = J @ np.array([0.2, 1.4, 0.1])
    first = rule.select(s)
    # Any amount of surrounding context, including a deliberately wrong "truth", cannot
    # change the value because there is no argument through which to pass it.
    for _pretend_truth in range(K):
        assert rule.select(s) == first
    assert rule.select_many(np.vstack([s, s]))[0] == first
    with pytest.raises(TypeError):
        rule.select(s, 2)  # type: ignore[call-arg]


def test_select_many_agrees_with_select_row_by_row():
    J = _well_conditioned(seed=3)
    rule = _rule(J)
    rng = np.random.default_rng(11)
    block = rng.standard_normal((64, D))
    many = rule.select_many(block)
    assert [rule.select(row) for row in block] == [int(x) for x in many]


def test_build_refuses_a_structurally_rank_deficient_jacobian():
    """`S_C`'s shape: d = 2 < K = 3, so no J can have rank 3 and the pseudo-inverse would
    silently return a minimum-norm answer about a component the data cannot separate."""
    rng = np.random.default_rng(5)
    J = rng.standard_normal((2, 3))
    with pytest.raises(ValueError, match="refusing to build"):
        _rule(J)


def test_build_refuses_a_jacobian_past_the_condition_number_ceiling():
    """`S_A` under the adversarial families sits at kappa = 136.7 and must be refused."""
    J = _well_conditioned()
    J[:, 2] *= 1.0 / 200.0          # kappa ~ 600
    with pytest.raises(ValueError, match="refusing to build"):
        _rule(J)


def test_build_accepts_the_same_jacobian_once_the_ceiling_is_raised():
    """The companion to the two refusals: the check is not refusing everything."""
    J = _well_conditioned()
    J[:, 2] *= 1.0 / 200.0
    rule = _rule(J, kappa_max=1e4, tau=1e-4)
    assert rule.K == K


def test_studentised_scale_is_the_null_standard_deviation_of_eta_hat():
    """`c_k = ||J^+[k,:]||` is claimed to be the null sd of eta_hat_k when z ~ N(0, I).
    Measured against draws rather than asserted from the algebra alone."""
    J = _well_conditioned(seed=7)
    rule = _rule(J)
    rng = np.random.default_rng(23)
    z = rng.standard_normal((200_000, D))
    empirical = (z @ rule.Jplus.T).std(axis=0, ddof=1)
    assert np.allclose(empirical, rule.scale, rtol=0.02)


def test_the_two_variants_are_not_the_same_rule():
    """If plain and studentised always agreed, measuring both would be theatre. On an
    ill-conditioned J they must disagree on a non-trivial fraction of null draws."""
    J = _well_conditioned(seed=9)
    J[:, 2] *= 1.0 / 20.0           # kappa ~ 60, close to S_B under AAA
    plain = _rule(J, variant="plain")
    stud = _rule(J, variant="studentised")
    rng = np.random.default_rng(31)
    z = rng.standard_normal((5_000, D))
    disagree = float(np.mean(plain.select_many(z) != stud.select_many(z)))
    assert disagree > 0.05


def test_tie_fraction_finds_a_planted_tie_and_reports_zero_without_one():
    """Dufour's Proposition 4.1 assumes ties have probability zero (spec section 2.2). A
    flag that cannot report a tie would be vacuous, so it is shown doing both."""
    J = np.zeros((D, K))
    J[0, 0] = J[1, 1] = J[2, 2] = 1.0
    rule = _rule(J, variant="plain")
    tied = np.zeros((1, D))
    tied[0, 0] = tied[0, 1] = 1.0          # exactly equal T_0 and T_1
    assert rule.tie_fraction(tied) == 1.0
    untied = np.zeros((1, D))
    untied[0, 0], untied[0, 1] = 1.0, 0.5
    assert rule.tie_fraction(untied) == 0.0


def test_a_wrong_shape_summary_is_rejected_rather_than_broadcast():
    J = _well_conditioned()
    rule = _rule(J)
    with pytest.raises(ValueError, match="shape"):
        rule.eta_hat(np.zeros(D - 1))
