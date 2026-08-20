"""Tests for the pre-registered cost gate.

The gate is a pass/fail flag, so ``DEVIATIONS.md`` D-8's rule bites hardest here: a gate
that cannot fail, or cannot pass, would look exactly like one that works. Every flag below
is shown coming out BOTH ways, and the boundary it turns on is checked from either side.
"""

from __future__ import annotations

import math

import pytest

from src.diagnostics import cost_gate as cg
from src.diagnostics.p_sel import wilson


def test_cost_is_the_specifications_formula_and_nothing_else():
    assert cg.cost(1000, 99, 0.5) == 1000 * 99 / 0.5
    assert math.isinf(cg.cost(1000, 99, 0.0))


def test_each_corner_flips_on_either_side_of_its_own_stated_flip_point():
    """The vacuous-flag test. Every corner reports the p_sel at which it changes answer;
    a hair above it the corner must pass and a hair below it must fail."""
    rows = cg.corner_rows(0.5, 0.4, 0.6)
    assert rows, "no corners"
    for r in rows:
        flip = r["p_sel_at_which_this_corner_flips"]
        above = [x for x in cg.corner_rows(flip * 1.01, flip, flip)
                 if (x["M"], x["N"]) == (r["M"], r["N"])][0]
        below = [x for x in cg.corner_rows(flip * 0.99, flip, flip)
                 if (x["M"], x["N"]) == (r["M"], r["N"])][0]
        assert above["passes"] is True
        assert below["passes"] is False


def test_verdict_reaches_all_three_of_pass_fail_and_split():
    """If SPLIT were unreachable the three-valued verdict would be theatre."""
    assert cg.verdict(cg.corner_rows(1.0, 1.0, 1.0)) == "PASS"
    assert cg.verdict(cg.corner_rows(1e-6, 1e-6, 1e-6)) == "FAIL"
    # M*N spans 9.9e4 to 9.99e6, so the corners' flip points span 9.9e-4 to 9.99e-2.
    split = cg.verdict(cg.corner_rows(1e-2, 1e-2, 1e-2))
    assert split == "SPLIT"


def test_the_declared_M_and_N_ranges_alone_span_two_orders_of_magnitude():
    """Recorded as a test because it is the reason SPLIT is reachable at all: the
    specification's own declared ranges differ by a factor of 100, which is wider than the
    uncertainty any feasible p_sel measurement carries."""
    prods = [m * n for m in cg.M_VALUES for n in cg.N_VALUES]
    assert max(prods) / min(prods) > 90


def test_session_verdict_treats_a_split_as_not_a_pass():
    cases = {
        "AAA|studentised": {"verdict": "PASS"},
        "AAA|plain": {"verdict": "FAIL"},
        "BBB|studentised": {"verdict": "PASS"},
    }
    sv = cg.session_verdict(cases, "AAA")
    assert sv["verdict"] == "SPLIT"
    assert sv["is_a_pass"] is False


def test_session_verdict_passes_only_when_both_variants_pass():
    both = {"AAA|studentised": {"verdict": "PASS"}, "AAA|plain": {"verdict": "PASS"}}
    assert cg.session_verdict(both, "AAA")["is_a_pass"] is True
    neither = {"AAA|studentised": {"verdict": "FAIL"}, "AAA|plain": {"verdict": "FAIL"}}
    assert cg.session_verdict(neither, "AAA")["verdict"] == "FAIL"


def test_session_verdict_refuses_a_primary_assignment_it_has_no_cases_for():
    with pytest.raises(ValueError):
        cg.session_verdict({"BBB|plain": {"verdict": "PASS"}}, "AAA")


def test_ci_decides_the_gate_reads_false_when_the_interval_straddles_a_corner():
    """A wide interval around a corner's flip point must be reported as undecided, and a
    tight one away from every flip point must be reported as decided."""
    flip = min(m * n for m in cg.M_VALUES for n in cg.N_VALUES) / cg.GATE_DRAWS
    straddling = cg.gate_case(flip, flip * 0.5, flip * 2.0)
    assert straddling["ci_decides_the_gate"] is False
    tight = cg.gate_case(0.5, 0.49, 0.51)
    assert tight["ci_decides_the_gate"] is True


def test_zero_acceptances_give_an_infinite_point_cost_and_a_finite_bound():
    """Specification section 3.4: a theta at which the observed selection is impossible is
    one where the rejection sampler never terminates. Reported as a bound, not as a number."""
    lo, hi = wilson(0, 6000)
    case = cg.gate_case(0.0, lo, hi)
    assert lo == 0.0 and 0.0 < hi < 1e-3
    assert all(math.isinf(r["expected_draws"]) for r in case["corners"])
    assert all(math.isfinite(r["expected_draws_ci95_lower"]) for r in case["corners"])
    assert case["verdict"] == "FAIL"


def test_wilson_is_sane_at_both_boundaries_and_in_the_middle():
    lo, hi = wilson(0, 1000)
    assert lo == 0.0 and 0.0 < hi < 0.01
    lo, hi = wilson(1000, 1000)
    assert hi == 1.0 and 0.99 < lo < 1.0
    lo, hi = wilson(500, 1000)
    assert lo < 0.5 < hi and (hi - lo) < 0.07


def _doc(screen_p, refined_p, width, key="AAA|studentised"):
    def blk(p, n):
        lo, hi = wilson(int(round(p * n)), n)
        return {key: {"n_draws": n, "counts": [int(round(p * n)), n, n],
                      "p_sel": [p, 1.0, 1.0], "ci95_lower": [lo, 1.0, 1.0],
                      "ci95_upper": [hi, 1.0, 1.0], "se": [0.0, 0.0, 0.0]}}
    return {"stage_B_nuisance_box": [{
        "key": "test", "width": width, "kind": "corner",
        "screen": blk(screen_p, 1000),
        "refined": blk(refined_p, 6000) if refined_p is not None else None}]}


def test_worst_over_box_prefers_the_independently_remeasured_value():
    """The smallest of many noisy estimates is biased low; the refined draw is the
    correction. If this preferred the screen value the reported cost would be too high."""
    d = _doc(screen_p=0.001, refined_p=0.02, width=0.2)
    got = cg.worst_over_box(d, "AAA|studentised", 0.2)
    assert got["p_sel"] == 0.02
    assert got["estimate_source"] == "refined"


def test_worst_over_box_ignores_points_outside_the_requested_width():
    d = _doc(screen_p=1e-6, refined_p=None, width=0.5)
    with pytest.raises(AssertionError):
        cg.worst_over_box(d, "AAA|studentised", 0.05)
    assert cg.worst_over_box(d, "AAA|studentised", 0.5)["p_sel"] == 1e-6
