"""Tests for the K = 6 spectrum check.

Every check here is written so that it FAILS against a broken version of the thing it
checks -- ``DEVIATIONS.md`` D-8's rule, which this project has now had to apply to its own
repairs three times (D-8, D-10, the ``leakage_checked`` literal). Where a test asserts that
a check passes on good input, there is a companion test feeding it bad input and requiring
the check to catch it.
"""

from __future__ import annotations

import math

import numpy as np
import pytest

from src.diagnostics import k6_spectrum as k6
from src.diagnostics.jacobian_rank import TAU, estimate_jacobian
from src.simulators.sir3 import prior_predictive_stats, with_params
from src.simulators.summaries import SUMMARY_SETS

SMALL_H = (1e-1, 1e-2)
SMALL_R = 3
SEED = 777


# --- the parallel estimator is not taken on trust ----------------------------------------

def test_parallel_columns_are_bit_identical_to_sequential():
    """Scheduling must not touch the estimate.

    Fails if the worker function is impure, if results are reassembled by arrival order
    rather than by task index, or if any per-process state (the p_ref cache, an RNG) leaks
    across tasks.
    """
    seq = k6.estimate_columns(h_values=SMALL_H, n_replicates=SMALL_R, seed0=SEED, workers=1)
    par = k6.estimate_columns(h_values=SMALL_H, n_replicates=SMALL_R, seed0=SEED, workers=2)
    assert set(seq) == set(par)
    for key in seq:
        for name in seq[key]:
            assert np.array_equal(seq[key][name], par[key][name]), (key, name)


def test_columns_match_the_production_estimator_exactly():
    """This script must not be a second implementation of the Jacobian estimator.

    ``estimate_jacobian`` produced every number in ``results/``. If the columns here differ
    from it at all, the six-column spectrum is a different object from the three-column one
    and cannot be compared with it.
    """
    stats = prior_predictive_stats(SUMMARY_SETS, n_replicates=8, seed0=999)
    sd_map = {n: sd for n, (_m, sd) in stats.items()}
    mine = k6.estimate_columns(h_values=SMALL_H, n_replicates=SMALL_R, seed0=SEED, workers=1)
    for family_set in k6.FAMILY_SETS:
        ref = estimate_jacobian(SUMMARY_SETS, sd_map, h_values=SMALL_H,
                                n_replicates=SMALL_R, seed0=SEED,
                                params=with_params(families=family_set), crn=True)
        for name in SUMMARY_SETS:
            for hi in range(len(SMALL_H)):
                got = np.column_stack(
                    [mine[(family_set, hi, k)][name] / sd_map[name] for k in range(3)]
                )
                assert np.array_equal(got, ref[name].jacobians[hi]), (family_set, name, hi)


# --- the kappa-branch algebra check, in both directions -----------------------------------

def _grid_row(tau, kappa_max, kappa):
    """A row as the production rule would produce it for a fully-resolved spectrum."""
    rank_fires = kappa > 1.0 / tau
    kappa_fires = kappa > kappa_max
    return {
        "tau": tau, "kappa_max": kappa_max, "condition_number": kappa,
        "rank_determined": True,
        "rank_branch_fires": rank_fires,
        "kappa_branch_fires": kappa_fires,
        "kappa_branch_fires_alone": kappa_fires and not rank_fires,
    }


def test_kappa_algebra_check_passes_on_a_correct_grid():
    kappa = 64.62
    grid = [_grid_row(t, km, kappa)
            for t in (1e-3, 1e-2, 1e-1) for km in (10.0, 100.0, 1000.0)]
    assert k6.check_kappa_algebra({"measured_condition_number": kappa, "grid": grid}) == []


def test_kappa_algebra_check_catches_an_inverted_ceiling_comparison():
    """The companion test D-8 requires: the check must be seen giving the opposite answer.

    Here the ceiling comparison is inverted, which is the most plausible single-character
    defect in this rule and the one that would make every INSEPARABLE verdict on the kappa
    branch wrong in the favourable direction.
    """
    kappa = 64.62
    grid = []
    for t in (1e-3, 1e-2, 1e-1):
        for km in (10.0, 100.0, 1000.0):
            row = _grid_row(t, km, kappa)
            row["kappa_branch_fires"] = kappa < km          # inverted
            row["kappa_branch_fires_alone"] = row["kappa_branch_fires"] and not row["rank_branch_fires"]
            grid.append(row)
    bad = k6.check_kappa_algebra({"measured_condition_number": kappa, "grid": grid})
    assert bad, "an inverted ceiling comparison must be caught"


def test_kappa_algebra_check_catches_a_rank_rule_stated_on_the_wrong_singular_value():
    kappa = 64.62
    grid = []
    for t in (1e-3, 1e-2, 1e-1):
        for km in (10.0, 100.0, 1000.0):
            row = _grid_row(t, km, kappa)
            row["rank_branch_fires"] = not row["rank_branch_fires"]
            row["kappa_branch_fires_alone"] = row["kappa_branch_fires"] and not row["rank_branch_fires"]
            grid.append(row)
    assert k6.check_kappa_algebra({"measured_condition_number": kappa, "grid": grid})


def test_kappa_branch_is_unreachable_at_the_registered_pair_and_reachable_below_it():
    """G4 finding 1.4, as an assertion rather than a remark.

    At ``kappa_max = 1/tau`` the kappa branch cannot fire alone, for ANY kappa. Below it, it
    can. If this ever stops holding, THRESHOLDS §1.3's "same criterion stated two ways" has
    stopped being true and the results files' two columns have become two checks again.
    """
    for kappa in (0.5, 5.0, 64.62, 100.0, 628.9, 1e6):
        row = _grid_row(1e-2, 100.0, kappa)          # the registered pair, kappa_max = 1/tau
        assert not row["kappa_branch_fires_alone"], kappa
    assert _grid_row(1e-2, 10.0, 64.62)["kappa_branch_fires_alone"]   # ceiling below 1/tau


# --- near-null classification --------------------------------------------------------------

def _direction(v, members, borderline=()):
    return {
        "right_singular_vector_at_representative_h": list(v),
        "equivalence_class_members": list(members),
        "borderline_members": list(borderline),
    }


def test_within_mechanism_direction_is_classified_as_within():
    """base:transmission against adv:transmission -- columns 0 and 3."""
    v = np.zeros(6)
    v[0], v[3] = 1 / math.sqrt(2), -1 / math.sqrt(2)
    out = k6.classify_near_null(_direction(v, [0, 3]))
    assert out["kind"] == "within-mechanism"
    assert out["mechanisms_in_class"] == ["transmission"]
    assert out["mechanism_energy"]["transmission"] == pytest.approx(1.0)
    assert out["mechanism_energy"]["progression"] == pytest.approx(0.0)


def test_cross_mechanism_direction_is_classified_as_cross():
    """progression against observation -- the pair the adversarial S_A run confounded."""
    v = np.zeros(6)
    v[1], v[5] = 1 / math.sqrt(2), -1 / math.sqrt(2)
    out = k6.classify_near_null(_direction(v, [1, 5]))
    assert out["kind"] == "cross-mechanism"
    assert out["mechanisms_in_class"] == ["observation", "progression"]
    assert out["dominant_mechanism_energy_share"] == pytest.approx(0.5)


def test_classification_uses_the_pre_registered_membership_rule_not_the_energy():
    """A direction with energy spread across mechanisms but only one column above vk_min.

    The class is decided by ``THRESHOLDS`` §2.1's |v_k| >= vk_min rule, applied across the
    plateau by ``analyse``; ``mechanism_energy`` is reported alongside it and must not
    silently become the criterion.
    """
    v = np.array([0.9, 0.2, 0.2, 0.2, 0.2, 0.2])
    v = v / np.linalg.norm(v)
    out = k6.classify_near_null(_direction(v, [0]))
    assert out["kind"] == "within-mechanism"
    assert out["mechanisms_in_class"] == ["transmission"]
    assert out["mechanism_energy"]["progression"] > 0.0


# --- spectrum description ------------------------------------------------------------------

def test_where_tau_sits_below_a_well_separated_spectrum():
    d = k6.describe_spectrum([27.8, 5.208, 2.747], TAU)
    assert d["where_tau_sigma1_sits"] == "below the whole spectrum"
    assert d["n_singular_values_at_or_above_tau_sigma1"] == 3
    assert d["spread_decades_over_positive_singular_values"] == pytest.approx(1.005, abs=1e-3)


def test_where_tau_sits_inside_a_wide_spectrum():
    d = k6.describe_spectrum([68.13, 11.5, 4.679, 2.642, 0.625, 0.1083], TAU)
    assert d["where_tau_sigma1_sits"].startswith("inside the spectrum")
    assert d["n_singular_values_at_or_above_tau_sigma1"] == 4


def test_gap_prominence_is_one_for_a_perfectly_geometric_decay():
    """The descriptive statistic must read 1.0 exactly where there is no break at all."""
    d = k6.describe_spectrum([1.0, 0.1, 0.01, 0.001], TAU)
    assert d["gap_prominence_largest_over_median_adjacent_ratio"] == pytest.approx(1.0)


def test_gap_prominence_rises_when_one_ratio_dominates():
    d = k6.describe_spectrum([1.0, 0.9, 0.8, 1e-4], TAU)
    assert d["gap_prominence_largest_over_median_adjacent_ratio"] > 100.0


def test_structural_zeros_are_reported_and_excluded_from_the_spread():
    """S_C's exact null direction must not be mixed into a statement about decay."""
    d = k6.describe_spectrum([4.155, 0.9557, 0.0], TAU)
    assert d["n_structurally_zero"] == 1
    assert d["spread_decades_over_positive_singular_values"] == pytest.approx(
        math.log10(4.155 / 0.9557)
    )


# --- the reproduction check, in both directions ---------------------------------------------

def test_reproduction_check_reads_false_on_perturbed_values(tmp_path, monkeypatch):
    """The self-check must not be a formality: perturb one singular value and it must fail."""
    rec = k6.reproduction_check("S_B", "base", [27.801215370514683, 5.208396026313991,
                                                2.747076714481247])
    if not rec["available"]:
        pytest.skip("no recorded S_B run to compare against")
    assert rec["reproduces"], rec
    bad = k6.reproduction_check("S_B", "base", [27.801215370514683, 5.208396026313991,
                                               2.747076714481247 * 1.001])
    assert not bad["reproduces"]
    assert bad["max_relative_difference"] > 1e-4
