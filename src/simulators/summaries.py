"""Summary-statistic sets for the three-component SIR simulator.

The list of summary sets is CLOSED at three -- ``S_A``, ``S_B``, ``S_C`` -- by
``docs/THRESHOLDS.md`` §1.1, which was written before any singular value existed. Adding
a fourth requires an entry in ``DEVIATIONS.md`` naming the set, the reason, and whether
the ``S_A``/``S_B`` results were known at the time of the decision. Without that rule the
D4 STOP condition could be evaded indefinitely by proposing one more summary set.

  S_A  Epidemic-curve features: peak height, peak time, final size, exponential growth
       rate. The set a domain modeller would actually choose.  d = 4.

  S_B  Ten time-binned reported-incidence counts. The set an SBI practitioner would
       actually choose.  d = 10.

  S_C  Final size and peak height only. A POSITIVE CONTROL, expected to FAIL: with
       d = 2 < K = 3 the Jacobian cannot have rank 3, so S_C must be rank-deficient by
       construction. If it is reported as full rank, the implementation is wrong rather
       than the simulator being surprising -- and that would invalidate S_A's and S_B's
       numbers too. It is a test of the harness, not of the science.  d = 2.

DIFFERENTIABILITY IS A DESIGN CONSTRAINT ON THE SUMMARIES, NOT AN AFTERTHOUGHT
------------------------------------------------------------------------------
The diagnostic estimates ``J = ds/deta`` by central differences. A summary that is not a
smooth function of eta has no column in J, however well-defined it is as a statistic.

The obvious offender is PEAK TIME. Defined as ``argmax`` over a daily grid it is
integer-valued: a step function of eta, whose difference quotient is 0 almost everywhere
and O(1/h) at the jumps. Its "derivative" would be an artefact of where the jumps happen
to fall relative to h.

Both peak statistics are therefore computed by PARABOLIC INTERPOLATION through the
discrete maximum and its two neighbours -- the standard sub-sample peak estimator. The
interpolated location and height vary continuously with eta, and remain continuous across
a change of the discrete argmax (at the switch point the peak sits midway between two
bins and both parabolas agree there). This is a substantive modelling choice about the
summary, and it is recorded in the results files alongside the numbers it produces.

The remaining statistics are smooth without special handling: final size is a sum, the
binned counts are sums, and the growth rate is an ordinary-least-squares slope over a
fixed window.
"""

from __future__ import annotations

from typing import Callable, Mapping

import numpy as np

from .sir3 import SimOutput

__all__ = [
    "SUMMARY_SETS",
    "SUMMARY_LABELS",
    "GROWTH_WINDOW",
    "N_BINS",
    "s_a",
    "s_b",
    "s_c",
    "peak_interpolated",
]

#: Fixed window (day indices, inclusive-exclusive) for the exponential growth-rate fit.
#: Chosen to sit in the base model's growth phase, well before the peak at ~day 43, and
#: fixed here rather than derived per-run so that it cannot move with eta.
GROWTH_WINDOW: tuple[int, int] = (5, 25)

#: Number of equal-width time bins in S_B.
N_BINS: int = 10


def peak_interpolated(y: np.ndarray) -> tuple[float, float]:
    """Sub-sample peak (location, height) by parabolic interpolation.

    Fits a parabola through ``(i-1, i, i+1)`` where ``i`` is the discrete argmax and
    returns its vertex. See the module docstring for why the discrete argmax is not
    usable here.

    Falls back to the discrete value when the maximum sits on a boundary or the three
    points are collinear (a flat top), which are the only cases where the vertex is not
    defined.
    """
    i = int(np.argmax(y))
    if i == 0 or i == len(y) - 1:
        return float(i), float(y[i])
    y0, y1, y2 = float(y[i - 1]), float(y[i]), float(y[i + 1])
    denom = y0 - 2.0 * y1 + y2
    if denom == 0.0:
        return float(i), y1
    offset = 0.5 * (y0 - y2) / denom
    height = y1 - 0.25 * (y0 - y2) * offset
    return float(i) + offset, height


def _growth_rate(y: np.ndarray) -> float:
    """OLS slope of log reported incidence over :data:`GROWTH_WINDOW`.

    The window is fixed in day indices. A floor of one case is applied before the log so
    that the statistic is defined for any non-negative series; under the lognormal
    observation model at these magnitudes the floor is never active, and the tests assert
    that it is not.
    """
    lo, hi = GROWTH_WINDOW
    seg = np.maximum(y[lo:hi], 1.0)
    t = np.arange(lo, hi, dtype=float)
    logy = np.log(seg)
    t_c = t - t.mean()
    return float((t_c @ (logy - logy.mean())) / (t_c @ t_c))


def s_a(out: SimOutput) -> np.ndarray:
    """S_A -- epidemic-curve features. ``[peak_height, peak_time, final_size, growth_rate]``."""
    loc, height = peak_interpolated(out.reported)
    return np.array([height, loc, float(out.reported.sum()), _growth_rate(out.reported)])


def s_b(out: SimOutput) -> np.ndarray:
    """S_B -- :data:`N_BINS` equal-width time-binned reported-incidence counts."""
    y = out.reported
    if len(y) % N_BINS != 0:
        raise ValueError(
            f"T_days={len(y)} is not divisible by N_BINS={N_BINS}; the bin edges would "
            f"not be equal width and the summary would not mean what it says"
        )
    return y.reshape(N_BINS, -1).sum(axis=1)


def s_c(out: SimOutput) -> np.ndarray:
    """S_C -- the impoverished positive control. ``[final_size, peak_height]``. d = 2 < K = 3."""
    _loc, height = peak_interpolated(out.reported)
    return np.array([float(out.reported.sum()), height])


#: The closed set of summary maps (THRESHOLDS §1.1).
SUMMARY_SETS: Mapping[str, Callable[[SimOutput], np.ndarray]] = {
    "S_A": s_a,
    "S_B": s_b,
    "S_C": s_c,
}

#: Human-readable component labels, one per coordinate, for the results files.
SUMMARY_LABELS: Mapping[str, list[str]] = {
    "S_A": ["peak_height", "peak_time", "final_size", "growth_rate"],
    "S_B": [f"binned_incidence_{i:02d}" for i in range(N_BINS)],
    "S_C": ["final_size", "peak_height"],
}
