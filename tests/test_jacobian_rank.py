"""Tests for the Jacobian rank/coherence diagnostic and the random-attributor floor.

These run at a small replicate count. They test the ESTIMATOR's properties -- that a
plateau exists, that S_C fails as designed, that the rank verdict does not depend on the
arbitrary common scale -- not the production numbers, which live in ``results/`` and are
produced by ``src/diagnostics/run_diagnostic.py``.
"""

from __future__ import annotations

import numpy as np
import pytest

from src.diagnostics.floor_check import floor_check
from src.diagnostics.jacobian_rank import (
    H_VALUES,
    KAPPA_MAX,
    TAU,
    analyse,
    estimate_jacobian,
)
from src.simulators.sir3 import ETA_SCALE, K, prior_predictive_sd
from src.simulators.summaries import SUMMARY_SETS

R_SMALL = 4
SEED = 4242


@pytest.fixture(scope="module")
def sd_map():
    return {n: prior_predictive_sd(f, n_replicates=40, seed0=777_000)[1]
            for n, f in SUMMARY_SETS.items()}


@pytest.fixture(scope="module")
def sweeps(sd_map):
    return estimate_jacobian(SUMMARY_SETS, sd_map, h_values=H_VALUES,
                             n_replicates=R_SMALL, seed0=SEED)


# --------------------------------------------------------------------------------------
# 1. A single-h call must not be expressible. Brief §2.4.
# --------------------------------------------------------------------------------------

def test_scalar_h_is_rejected(sd_map):
    with pytest.raises(TypeError, match="not a scalar"):
        estimate_jacobian(SUMMARY_SETS, sd_map, h_values=1e-3,
                          n_replicates=1, seed0=SEED)


def test_single_element_h_list_is_rejected(sd_map):
    with pytest.raises(ValueError, match="at least 2 step sizes"):
        estimate_jacobian(SUMMARY_SETS, sd_map, h_values=[1e-3],
                          n_replicates=1, seed0=SEED)


def test_missing_normalisation_is_rejected():
    with pytest.raises(ValueError, match="no prior-predictive sd"):
        estimate_jacobian(SUMMARY_SETS, {}, h_values=H_VALUES,
                          n_replicates=1, seed0=SEED)


def test_degenerate_normalisation_is_rejected(sd_map):
    bad = dict(sd_map)
    bad["S_A"] = np.array([1.0, 1.0, 0.0, 1.0])
    with pytest.raises(ValueError, match="degenerate"):
        estimate_jacobian(SUMMARY_SETS, bad, h_values=H_VALUES,
                          n_replicates=1, seed0=SEED)


# --------------------------------------------------------------------------------------
# 2. The h-sweep plateau genuinely exists. Brief §2.11.
#    R2a is the claim that a plateau exists at all; if it does not, no rank call is
#    defensible and the diagnostic is uninterpretable.
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize("name", ["S_A", "S_B", "S_C"])
def test_plateau_exists_and_is_not_a_fallback(sweeps, name):
    a = analyse(sweeps[name])
    assert a["plateau"]["found"], f"{name}: no plateau; R2a fails and no rank call is defensible"
    assert a["plateau"]["n_h_in_plateau"] >= 2


@pytest.mark.parametrize("name", ["S_A", "S_B", "S_C"])
def test_plateau_is_flat_not_merely_slowly_drifting(sweeps, name):
    """A monotone drift can look like a plateau at any fixed tolerance. Check total drift."""
    a = analyse(sweeps[name])
    lo, hi = a["plateau"]["h_indices"]
    svs = np.array([row["singular_values"] for row in a["h_sweep"]][lo:hi + 1])
    lead = svs[:, 0]
    assert lead.max() / lead.min() < 1.05, f"{name}: leading singular value drifts across plateau"


@pytest.mark.parametrize("name", ["S_A", "S_B", "S_C"])
def test_singular_values_are_resolved_across_the_plateau(sweeps, name):
    """THRESHOLDS §1.4: unresolved singular values are counted toward the rank in neither
    direction, so an unresolved spectrum is a G-gate failure, not a pass."""
    a = analyse(sweeps[name])
    # Structural zeros (d < K) are resolved as zero and are not a failure.
    assert all(a["resolved"]), f"{name}: unresolved singular value(s) {a['singular_value_variation_factor']}"


def test_rank_noise_does_not_increase_monotonically_with_decreasing_h(sweeps):
    """The failure mode the plateau requirement exists to catch.

    Without common random numbers the estimate degrades as 1/h and the spectrum grows without
    bound. With them it must not: the sweep's leading singular value must stop growing.
    """
    a = analyse(sweeps["S_A"])
    lead = [row["singular_values"][0] for row in a["h_sweep"]]
    assert lead[-1] < 2.0 * lead[1], f"leading singular value still growing at small h: {lead}"


def test_no_crn_control_has_no_plateau_and_blows_up_as_one_over_h(sd_map):
    """The negative control, asserted rather than merely emitted."""
    ctrl = estimate_jacobian({"S_A": SUMMARY_SETS["S_A"]}, {"S_A": sd_map["S_A"]},
                             h_values=H_VALUES, n_replicates=R_SMALL, seed0=SEED, crn=False)
    a = analyse(ctrl["S_A"])
    lead = [row["singular_values"][0] for row in a["h_sweep"]]
    assert not a["plateau"]["found"], "no-CRN control unexpectedly produced a plateau"
    # Ten-fold smaller h should give roughly ten-fold larger leading singular value.
    assert lead[-1] / lead[-2] > 5.0
    assert lead[-1] > 100 * lead[0]


# --------------------------------------------------------------------------------------
# 3. S_C, the positive control. Brief §2.11 and §2.3: reported whichever way it goes.
# --------------------------------------------------------------------------------------

def test_s_c_cannot_have_full_column_rank(sweeps):
    """d = 2 < K = 3, so rank <= 2 by construction.

    If this fails, the rank routine is not doing what it claims and S_A's and S_B's numbers
    are invalidated too -- it is a harness failure, not a surprising simulator.
    """
    a = analyse(sweeps["S_C"])
    assert a["dimensions"]["d"] < a["dimensions"]["K"]
    assert not a["numerical_rank"]["full_column_rank"]
    assert a["numerical_rank"]["rank_certain"] <= 2
    assert a["inseparable"]


def test_s_c_reports_an_exact_null_direction(sweeps):
    """The economy SVD would omit it. Omitting it would hide the entire point of the control."""
    a = analyse(sweeps["S_C"])
    kinds = [nn["degeneracy_kind"] for nn in a["near_null_directions"]]
    assert "exact" in kinds, f"S_C near-null directions: {a['near_null_directions']}"
    assert len(a["right_singular_vectors_at_representative_h"]) == K


def test_s_c_null_direction_is_a_unit_vector(sweeps):
    a = analyse(sweeps["S_C"])
    for nn in a["near_null_directions"]:
        v = np.array(nn["right_singular_vector_at_representative_h"])
        assert np.linalg.norm(v) == pytest.approx(1.0, abs=1e-9)


# --------------------------------------------------------------------------------------
# 4. Scale invariance -- the property that makes the common eta_scale defensible.
# --------------------------------------------------------------------------------------

def test_rank_and_condition_number_are_invariant_to_the_common_eta_scale(sd_map):
    """Because eta_scale is COMMON across k, changing it multiplies J by a constant.

    The normalised spectrum, the numerical rank at a relative tolerance, and the condition
    number are therefore unchanged; only the column-norm test depends on the absolute value.
    Asserted here because the module docstring claims it.
    """
    kw = dict(h_values=H_VALUES, n_replicates=2, seed0=SEED)
    a = analyse(estimate_jacobian({"S_A": SUMMARY_SETS["S_A"]}, {"S_A": sd_map["S_A"]},
                                  eta_scale=ETA_SCALE, **kw)["S_A"])
    b = analyse(estimate_jacobian({"S_A": SUMMARY_SETS["S_A"]}, {"S_A": sd_map["S_A"]},
                                  eta_scale=ETA_SCALE / 4.0, **kw)["S_A"])
    assert a["numerical_rank"]["rank_certain"] == b["numerical_rank"]["rank_certain"]
    assert a["condition_number"] == pytest.approx(b["condition_number"], rel=1e-3)
    # ...and the column norms DO scale, which is why the invisibility test is not invariant.
    ratio = np.array(b["column_norms"]) / np.array(a["column_norms"])
    assert np.allclose(ratio, 0.25, rtol=1e-2)


# --------------------------------------------------------------------------------------
# 5. Reporting completeness -- every field the brief §2.7 requires.
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize("name", ["S_A", "S_B", "S_C"])
def test_every_required_field_is_reported(sweeps, name):
    a = analyse(sweeps[name])
    for key in (
        "h_sweep", "plateau", "singular_values_at_representative_h", "numerical_rank",
        "condition_number", "pairwise_coherence", "column_norms", "near_null_directions",
        "resolved", "inseparable", "inseparable_reason",
    ):
        assert key in a, f"{name} missing {key}"
    coh = np.array(a["pairwise_coherence"])
    assert coh.shape == (K, K)
    assert np.allclose(np.diag(coh), 1.0)
    assert np.allclose(coh, coh.T)
    assert len(a["column_norms"]) == K


def test_thresholds_are_parameters_not_constants(sweeps):
    """A reader must be able to re-apply their own tolerance. Brief §2.4."""
    strict = analyse(sweeps["S_A"], tau=0.9)
    loose = analyse(sweeps["S_A"], tau=1e-12)
    assert strict["numerical_rank"]["rank_certain"] <= loose["numerical_rank"]["rank_certain"]
    assert strict["numerical_rank"]["tau"] == 0.9


def test_pre_registered_thresholds_have_not_drifted():
    """These come from docs/THRESHOLDS.md and must not be revised after seeing a result."""
    assert TAU == 1e-2
    assert KAPPA_MAX == 100.0
    assert H_VALUES == (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6)


# --------------------------------------------------------------------------------------
# 6. The random-attributor floor. Brief §2.8 and §2.11.
# --------------------------------------------------------------------------------------

def test_floor_check_lands_near_one_third():
    fc = floor_check(n_draws=10_000, seed=20260820)
    assert fc["K"] == 3
    assert fc["floor_analytic"] == pytest.approx(1.0 / 3.0)
    assert fc["accuracy_simulated"] == pytest.approx(1.0 / 3.0, abs=0.02)
    assert fc["passes"]


def test_floor_check_is_reproducible():
    assert floor_check(seed=1)["accuracy_simulated"] == floor_check(seed=1)["accuracy_simulated"]


def test_floor_check_tracks_k():
    assert floor_check(n_draws=20_000, seed=5, k=5)["accuracy_simulated"] == pytest.approx(0.2, abs=0.02)


# --------------------------------------------------------------------------------------
# Leakage: a check that can fail, replacing a hard-coded literal (session G4).
# --------------------------------------------------------------------------------------

def test_leakage_check_passes_on_the_real_diagnostic(sweeps):
    """Component-label equivariance holds for every summary set.

    Until G4 this property was recorded in the results files as `leakage_checked: true` and
    nothing computed it -- a literal, with no condition under which it could have read false.
    See `audit/G3_ADVERSARIAL_REVIEW.md` finding 5 and `DEVIATIONS.md` D-8 for the defect class.
    """
    from src.diagnostics.jacobian_rank import leakage_check
    for name in SUMMARY_SETS:
        r = leakage_check(sweeps[name])
        assert r["passes"], f"{name}: {r['failures']}"
        assert r["n_permutations_tested"] == 5  # 3! - 1


def test_leakage_check_detects_a_component_indexed_analysis(sweeps, monkeypatch):
    """D-8's rule: run the check once in a state where it must give the opposite answer.

    A check that has only ever been seen passing is indistinguishable from one that cannot
    fail -- which is precisely what it is replacing. So a deliberately label-dependent
    analysis is injected here (a tolerance applied to one named column only, the shape a real
    leak would take) and the check must catch it.
    """
    import src.diagnostics.jacobian_rank as jr
    from src.diagnostics.jacobian_rank import leakage_check

    real_analyse = jr.analyse

    def leaky_analyse(sweep, **kw):
        out = real_analyse(sweep, **kw)
        # "Component 2 is the observation component, and we know it is well determined."
        out["column_norms"] = list(out["column_norms"])
        out["column_norms"][2] *= 2.0
        return out

    monkeypatch.setattr(jr, "analyse", leaky_analyse)
    r = leakage_check(sweeps["S_A"])
    assert not r["passes"], "the leakage check failed to detect a component-indexed analysis"
    assert r["worst_discrepancy"]["column_norms"] > 0


def test_leakage_check_is_not_vacuous_on_a_synthetic_leak():
    """The same demonstration without monkeypatching, on a matrix built to break equivariance.

    A Jacobian whose columns are genuinely asymmetric is NOT a leak -- equivariance must still
    hold for it, and does. What breaks equivariance is component-indexed *analysis*, not an
    asymmetric matrix, and the two are separated here so the check's meaning is not misread.
    """
    from src.diagnostics.jacobian_rank import JacobianSweep, leakage_check
    J = np.array([[5.0, 0.1, 0.0], [0.0, 3.0, 0.2], [0.1, 0.0, 1.0], [2.0, 0.0, 0.0]])
    sw = JacobianSweep("synthetic", (1e-1, 1e-2, 1e-3, 1e-4),
                       tuple(J + 1e-12 * i for i in range(4)),
                       np.ones(4), 8, 1, True, ETA_SCALE, 0)
    assert leakage_check(sw)["passes"]
