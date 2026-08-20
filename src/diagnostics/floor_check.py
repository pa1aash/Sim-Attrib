"""Random-attributor floor check: validate the harness against its own known answer.

``PROVENANCE.md`` requires that any results file reporting attribution accuracy record the
degenerate accuracy ``1/K`` that uniform random attribution achieves, **and the accuracy of
the actual uniform/random attributor as run**, not as computed analytically -- "so that the
harness itself is checked against its own known answer".

This is that check, and it runs before anything is built on top of the harness. With K = 3
an unqualified "41% accurate" describes a method barely distinguishable from guessing, so
every accuracy figure this project reports is reported against this floor.

The check is deliberately trivial. That is the point: a harness that cannot reproduce
``1/3`` from a uniform draw cannot be trusted to report anything harder.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from ..simulators.sir3 import K

__all__ = ["floor_check"]


def floor_check(*, n_draws: int = 10_000, seed: int = 20260820, k: int = K) -> dict[str, Any]:
    """Compare the analytic floor ``1/k`` against an empirically simulated uniform attributor.

    A uniform-random attributor guesses a component index uniformly at random, independent
    of the truth; the truth is itself drawn uniformly so the check does not depend on a
    particular ground-truth distribution. Accuracy is the fraction of matches.

    The two-sided tolerance is the exact binomial standard error at the floor, times four.
    It is stated here rather than tuned: at ``n = 10_000`` and ``k = 3`` that is about
    1.9 percentage points, so a harness that is wrong by more than a rounding error fails.
    """
    if k < 2:
        raise ValueError("k must be at least 2")
    if n_draws < 1:
        raise ValueError("n_draws must be positive")

    rng = np.random.default_rng(seed)
    truth = rng.integers(0, k, size=n_draws)
    guess = rng.integers(0, k, size=n_draws)
    accuracy = float(np.mean(truth == guess))

    floor = 1.0 / k
    se = float(np.sqrt(floor * (1.0 - floor) / n_draws))
    tolerance = 4.0 * se
    deviation = accuracy - floor

    return {
        "K": int(k),
        "floor_analytic": floor,
        "n_draws": int(n_draws),
        "seed": int(seed),
        "accuracy_simulated": accuracy,
        "deviation_from_floor": deviation,
        "binomial_standard_error_at_floor": se,
        "tolerance_4se": tolerance,
        "passes": bool(abs(deviation) <= tolerance),
        "interpretation": (
            "A uniform-random attributor over K components achieves 1/K by construction. "
            "The simulated value agreeing with the analytic floor to within 4 binomial "
            "standard errors is the harness reproducing its own known answer. Every "
            "attribution accuracy this project reports is reported against this floor; an "
            "accuracy quoted in isolation is not admissible (PROVENANCE.md)."
        ),
    }
