"""Does the argmax inside the peak statistics contaminate S_A's Jacobian? Measured, not argued.

WHY THIS EXISTS
---------------
``src/simulators/summaries.py`` identifies the danger and states a defence:

  * the danger -- ``argmax`` on a daily grid is integer-valued, so peak time is a step
    function of eta with no finite-difference derivative at any h;
  * the defence -- both peak statistics are computed by PARABOLIC INTERPOLATION through the
    discrete maximum, and the docstring asserts that the interpolated values *"remain
    continuous across a change of the discrete argmax (at the switch point the peak sits
    midway between two bins and both parabolas agree there)"*.

**Half of that assertion is false, and this script establishes which half.** Write the three
points at the switch as ``a = y[i-1]``, ``m = y[i] = y[i+1]``, ``c = y[i+2]``. Approaching the
switch from the left the vertex is at offset ``+1/2`` with height ``m + (m-a)/8``; from the
right it is at offset ``-1/2`` from the next index -- the SAME location -- but with height
``m + (m-c)/8``. **The location matches; the height does not, unless a == c.** So the
interpolation removes the discontinuity from peak TIME and leaves one, of size ``(c-a)/8``, in
peak HEIGHT.

That is an argument. What follows are three measurements, because an argument about a
discontinuity is worth much less than a count of how often it was actually crossed.

  1. **A fine eta sweep at a fixed seed**, which locates real argmax switches and measures the
     jump in each statistic across them. This tests the claim above directly.
  2. **A census at the estimator's own settings.** For every component and the h values where
     a switch is most and least likely, how many of the R replicates actually had
     ``argmax(y(+h)) != argmax(y(-h))``? A discontinuity that is never crossed cannot
     contaminate anything, and a discontinuity that is crossed by 40 of 128 replicates is not
     a caveat, it is the result.
  3. **Leave-one-coordinate-out.** S_A's verdict is recomputed with each of its four summary
     coordinates dropped in turn. If the verdict survives dropping peak height and peak time,
     it does not rest on them, and that is a stronger statement than any argument about how
     well the interpolation behaves.

    python -m src.diagnostics.summary_smoothness_check
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import yaml

from ..provenance import header, now_iso
from ..simulators.sir3 import BASE, ETA_SCALE, K, prior_predictive_stats, simulate
from ..simulators.summaries import SUMMARY_SETS, peak_interpolated, s_a
from .jacobian_rank import H_VALUES, KAPPA_MAX, RESOLVE_FACTOR, TAU

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results" / "robustness"

SEED = 20260820
R = 128
R_NORM = 2000
LABELS = ["peak_height", "peak_time", "final_size", "growth_rate"]


def _fine_sweep(seed: int, k: int, lo: float, hi: float, n: int) -> dict[str, Any]:
    """Walk eta_k finely at one fixed seed and record every argmax switch that occurs."""
    etas = np.linspace(lo, hi, n)
    rows = []
    for e in etas:
        eta = np.zeros(K)
        eta[k] = e
        y = simulate(eta, seed=seed).reported
        loc, hgt = peak_interpolated(y)
        rows.append((float(e), int(np.argmax(y)), float(loc), float(hgt)))

    switches = []
    for (e0, i0, l0, h0), (e1, i1, l1, h1) in zip(rows[:-1], rows[1:]):
        if i0 != i1:
            switches.append({
                "eta_before": e0, "eta_after": e1,
                "argmax_before": i0, "argmax_after": i1,
                "eta_gap": e1 - e0,
                "peak_time_jump": l1 - l0,
                "peak_height_jump": h1 - h0,
                "peak_time_jump_per_eta_gap": (l1 - l0) / (e1 - e0),
                "peak_height_jump_per_eta_gap": (h1 - h0) / (e1 - e0),
            })
    locs = np.array([r[2] for r in rows])
    hgts = np.array([r[3] for r in rows])
    steps = np.diff(etas)
    return {
        "component_k": k,
        "eta_range": [float(lo), float(hi)],
        "n_points": int(n),
        "eta_step": float(steps[0]),
        "n_argmax_switches": len(switches),
        "switches": switches,
        "largest_step_in_peak_time": float(np.abs(np.diff(locs)).max()),
        "largest_step_in_peak_height": float(np.abs(np.diff(hgts)).max()),
        "median_step_in_peak_time": float(np.median(np.abs(np.diff(locs)))),
        "median_step_in_peak_height": float(np.median(np.abs(np.diff(hgts)))),
    }


def _switch_census(seed0: int, n_rep: int, h_values: tuple[float, ...]) -> list[dict[str, Any]]:
    """At the estimator's own settings: how many replicates straddle an argmax switch?"""
    out = []
    for h in h_values:
        step = h * ETA_SCALE
        for k in range(K):
            n_switch = 0
            n_boundary = 0
            dq_height = []
            for r in range(n_rep):
                ep, em = np.zeros(K), np.zeros(K)
                ep[k], em[k] = step, -step
                yp = simulate(ep, seed=seed0 + r).reported
                ym = simulate(em, seed=seed0 + r).reported
                ip, im = int(np.argmax(yp)), int(np.argmax(ym))
                if ip != im:
                    n_switch += 1
                if ip in (0, len(yp) - 1) or im in (0, len(ym) - 1):
                    n_boundary += 1
                dq_height.append((peak_interpolated(yp)[1] - peak_interpolated(ym)[1]) / (2 * h))
            arr = np.asarray(dq_height)
            out.append({
                "h": float(h), "component_k": int(k), "n_replicates": int(n_rep),
                "n_replicates_straddling_an_argmax_switch": int(n_switch),
                "n_replicates_with_a_boundary_argmax_fallback": int(n_boundary),
                "peak_height_difference_quotient_mean": float(arr.mean()),
                "peak_height_difference_quotient_sd": float(arr.std(ddof=1)),
                "peak_height_difference_quotient_max_abs": float(np.abs(arr).max()),
            })
            print(f"  h={h:g} k={k}: {n_switch}/{n_rep} straddle a switch, "
                  f"{n_boundary} boundary fallbacks")
    return out


def _jacobian_at(h: float, sd: np.ndarray, seed0: int, n_rep: int) -> np.ndarray:
    """S_A's normalised Jacobian at a single h. Same construction as the diagnostic."""
    step = h * ETA_SCALE
    cols = []
    for k in range(K):
        acc = []
        for r in range(n_rep):
            ep, em = np.zeros(K), np.zeros(K)
            ep[k], em[k] = step, -step
            acc.append((s_a(simulate(ep, seed=seed0 + r)) - s_a(simulate(em, seed=seed0 + r)))
                       / (2.0 * h))
        cols.append(np.mean(np.asarray(acc), axis=0) / sd)
    return np.column_stack(cols)


def _verdict_from(J: np.ndarray) -> dict[str, Any]:
    _u, s_raw, _vt = np.linalg.svd(J, full_matrices=True)
    s = np.zeros(K)
    s[: len(s_raw)] = s_raw
    kappa = float(s[0] / s[-1]) if s[-1] > 0 else float("inf")
    rank = int(sum(1 for x in s if x >= TAU * s[0]))
    return {
        "singular_values": [float(x) for x in s],
        "rank_at_tau": rank,
        "condition_number": kappa,
        "verdict": "separable" if (rank == K and kappa <= KAPPA_MAX) else "INSEPARABLE",
    }


def main() -> int:
    started = now_iso()
    print("fine eta sweeps, one fixed seed, looking for real argmax switches ...")
    fine = {
        "transmission": _fine_sweep(SEED, 0, -0.6, 0.6, 121),
        "progression": _fine_sweep(SEED, 1, -0.6, 0.6, 121),
        "observation": _fine_sweep(SEED, 2, -0.6, 0.6, 121),
    }
    for name, blk in fine.items():
        print(f"  {name}: {blk['n_argmax_switches']} switches; "
              f"largest step peak_time={blk['largest_step_in_peak_time']:.4g}, "
              f"peak_height={blk['largest_step_in_peak_height']:.4g}")

    print("\nswitch census at the estimator's own settings ...")
    census = _switch_census(SEED, R, (H_VALUES[0], H_VALUES[3]))

    print("\nleave-one-coordinate-out on S_A ...")
    stats = prior_predictive_stats(SUMMARY_SETS, n_replicates=R_NORM, seed0=SEED + 900_000)
    sd = stats["S_A"][1]
    rep_h = 1e-4  # the representative h recorded in results/jacobian_rank.S_A.yaml
    J = _jacobian_at(rep_h, sd, SEED, R)
    loo = {"all_four_coordinates": _verdict_from(J)}
    for i, lab in enumerate(LABELS):
        keep = [j for j in range(len(LABELS)) if j != i]
        loo[f"dropping_{lab}"] = _verdict_from(J[keep, :])
    loo["dropping_both_peak_statistics"] = _verdict_from(J[[2, 3], :])
    for key, v in loo.items():
        print(f"  {key:<38s} rank {v['rank_at_tau']}/{K}  kappa {v['condition_number']:.4g}  "
              f"-> {v['verdict']}")

    doc: dict[str, Any] = {
        "provenance": header(script="src/diagnostics/summary_smoothness_check.py",
                             command="python -m src.diagnostics.summary_smoothness_check",
                             seed=SEED, started=started),
        "what_this_is": (
            "Session G4 adversarial pass, finding 4. Tests whether the argmax inside S_A's peak "
            "statistics contaminates the Jacobian that results/jacobian_rank.S_A.yaml reports. "
            "Does not modify anything in results/. See audit/G3_ADVERSARIAL_REVIEW.md."
        ),
        "the_claim_under_test": (
            "src/simulators/summaries.py asserts that the parabolic interpolation leaves both "
            "peak statistics continuous across a change of the discrete argmax. Algebraically "
            "the LOCATION is continuous (both parabolas put the vertex midway between the tied "
            "bins) and the HEIGHT is not: from the left it is m + (m-a)/8 and from the right "
            "m + (m-c)/8, equal only if the outer neighbours a and c are equal."
        ),
        "settings": {"seed": SEED, "n_replicates_R": R, "n_replicates_R_norm": R_NORM,
                     "representative_h": rep_h, "eta_scale": ETA_SCALE,
                     "tau": TAU, "kappa_max": KAPPA_MAX, "resolve_factor": RESOLVE_FACTOR},
        "fine_eta_sweeps": fine,
        "argmax_switch_census": census,
        "leave_one_coordinate_out_S_A": loo,
        "leave_one_out_note": (
            "Computed at the single representative h of the recorded run, not across the whole "
            "sweep, because the question is whether the reported verdict depends on the two "
            "suspect coordinates -- and the reported verdict is read off the representative h."
        ),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "summary_smoothness_check.yaml"
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, width=100)
    print(f"\nwrote {path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
