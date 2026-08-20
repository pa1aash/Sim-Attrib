"""Where the selection cells stop being reachable -- session G7, Phase 1. ``OUTSTANDING.md`` O-30.

WHAT THIS IS, AND WHAT IT IS EXPLICITLY NOT
--------------------------------------------
Session G6 measured ``p_sel`` at relative nuisance half-widths of 0.05, 0.10, 0.20 and 0.50
and found the collapse **already complete at the narrowest of them**: zero acceptances in
100,000 draws, 95% upper bound ``3.84e-5``. So the boundary -- the width at which the observed
selection cell stops being reachable -- lies somewhere below 0.05 and its location was unknown.
``docs/OPEN_QUESTIONS.md`` Q-16 priced locating it; ``OUTSTANDING.md`` **O-30** carries it.

**THIS SWEEP IS CHARACTERISATION, NOT VERDICT-SEEKING, AND THE ORDER OF EVENTS IS THE PROOF.**
``docs/DECISIONS.md`` **D-16** -- the composition is dropped as an experimental vehicle and kept
as a stated negative result -- was DECIDED by the operator at the start of session G7, **before
this script was written and before any number it produces existed**. Nothing measured here can
soften, reopen, or re-price that decision. What it buys is a negative result with a *shape*
instead of a bare threshold statement: a reader of the paper should be able to see whether the
collapse from "affordable" to "never terminates" is a cliff or a slide, because those two
pictures license different advice to somebody holding a different simulator.

Stated the other way round, so the reader can hold this session to it: **if this sweep had found
that the cells stay reachable out to 0.04 and collapse only past it, the composition would still
be dropped.** D-16's reason is that §3.4's lemma forces a ``theta``-free rule and the
nuisance-to-noise ratio of this simulator then makes the observed cell unreachable *somewhere*
inside any box an epidemiologist would call plausible. Where exactly is a fact about the
simulator, not about the decision.

THE DESIGN, PRE-REGISTERED -- committed before this script is run for the first time
------------------------------------------------------------------------------------
This module is committed before it produces a number, in the same way
``src/diagnostics/k6_spectrum.py`` was at ``a8159f8`` and ``src/diagnostics/cost_gate.py`` was
at ``5ba0623``, and for the same reason: a design chosen after seeing the data it describes is
not a design.

**The object measured.** For each half-width ``w``, the same deterministic design G6 used --
``src/diagnostics/p_sel.nuisance_grid``, 32 corners and 10 axis endpoints of the relative box on
the five nuisance coordinates ``audit/MMC_COMPOSITION_SPEC.md`` §1 names -- and

    p_min(w)  =  min over design points theta in D(w),  min over cells k,  of  p_sel(theta)_k

which is exactly the quantity ``src/diagnostics/cost_gate.py`` consumes: §4 point 1 takes the
minimum over ``theta``, and the gate takes the minimum over cells because the cell is chosen by
the data and the procedure must terminate for whichever one arises. **Reusing G6's grid function
rather than writing a new one is deliberate**: it makes the ``w = 0.05`` row of this sweep
directly comparable with the recorded ±5% number, on independent draws.

**The widths.** ``WIDTHS`` below spans ``0.001`` to ``0.05`` with ten points, denser between
``0.002`` and ``0.02`` where Q-16 predicted the boundary would lie. The prediction is not free:
the normalised nuisance shift is close to linear in ``w`` at small ``w`` (G6 measured a median
``||E[z]|| = 26.5`` at ``w = 0.05``, i.e. about ``0.53`` per ``0.001`` of width), and a single
null draw has ``||z|| = sqrt(d) = sqrt(10) ~ 3.16`` by construction, so the shift crosses the
noise magnitude near ``w ~ 0.006``. The grid is placed to resolve that region rather than to
confirm it.

**The anchor at ``w = 0``.** ``theta_0`` itself, re-measured at ``N_THETA0`` draws on seeds
disjoint from every seed G6 used. It is the sweep's left-hand endpoint AND a reproduction check:
an independent measurement of a recorded number.

**The refinement.** The smallest of 42 noisy estimates is biased low, and reporting it would
overstate the collapse. At each width the point attaining the screened minimum -- for each of
the four (assignment, variant) keys, deduplicated and capped at ``N_REFINE_POINTS_PER_WIDTH`` --
is re-drawn on fresh seeds at ``N_REFINE_DRAWS``. The refined value is the one reported and the
one the shape criterion is computed on. This is G6's stage B2 applied per width instead of
globally.

**The one place the refinement could bias the answer the OTHER way, and what is done about it.**
If a key's own screened argmin were not among the re-measured points, reporting the minimum over
the points that were re-measured would return a value that is too HIGH -- i.e. that flatters the
composition. The cap is set to four, the number of keys, so this cannot arise; the code does not
rely on that, and falls back to the screened value with its own wider interval, flagged
``de_biased: false``, whenever it does. The fallback direction is chosen to be the one that does
not understate the collapse.

THE SHAPE CRITERION, DECLARED BEFORE THE DATA EXIST
----------------------------------------------------
"Is the collapse gradual or abrupt?" is the question this sweep exists to answer, so the answer
must not be a judgement made while looking at the answer. Let ``W+`` be the widths at which
``p_min(w) > 0``, ordered, and let

    s_i  =  [ log10 p_min(w_{i+1}) - log10 p_min(w_i) ]  /  ( w_{i+1} - w_i )

be the local log-slope in decades per unit relative half-width. Then:

* **CENSORED_BELOW** -- if ``p_min`` is already zero at the smallest width measured, or if
  ``|W+| < 4``. The sweep does not have enough live points to describe a shape and says so
  rather than describing one. **This is the branch that makes the classification falsifiable:
  it is reachable, and it is the outcome if the boundary lies below 0.001.**
* **ABRUPT** -- if ``max|s_i| / median|s_i| >= SLOPE_RATIO_ABRUPT``: one interval carries the
  collapse and the others do not, which is a threshold.
* **GRADUAL** -- otherwise, i.e. the log-slope is roughly constant. Reported together with the
  log-linear fit ``log10 p_min = a + b*w`` and its ``R^2``, so a reader can see how well
  "exponential in the distortion magnitude" actually describes it. **``R^2`` is reported, not
  used as a criterion**, because a threshold on a fit quality chosen at the same time as the
  fit is not a threshold.

UNDER WHAT CONDITION DOES EACH FLAG THIS SCRIPT WRITES READ FALSE? (standing constraint S4/S5)
-----------------------------------------------------------------------------------------------
``normalisation_reproduces``   -- FALSE when the prior-predictive mean and sd recomputed here
    from the recorded settings differ from ``results/jacobian_rank.S_B.yaml`` by more than
    ``NORM_TOL`` relatively. Inherited from ``p_sel.py``; the run aborts rather than proceeding
    in inconsistent coordinates.
``jacobian_reproduces``        -- FALSE when no recorded step size reproduces the singular
    values ``results/robustness/k6_spectrum.yaml`` records for the triple.
``family_sets_agree_at_zero``  -- FALSE when the base and adversarial branches differ at
    ``eta = 0``, which would mean one set of null draws cannot serve both assignments.
``seed_spans_disjoint_from_G6`` -- FALSE when any seed span used here overlaps a span recorded
    in ``results/p_sel.yaml``. Reachable: it is exactly what would happen if the default
    ``--seed`` were left at G6's. The run aborts, because a "reproduction check" run on the
    same draws is not a check.
``theta0_reproduces_recorded_p_sel`` -- FALSE when the re-measured ``theta_0`` cell probability
    lies outside the Wilson interval of the value ``results/p_sel.yaml`` records for the same
    cell, for any cell of any key. Reachable: a changed summary set, a changed normalisation, a
    changed selection rule, or a genuine non-reproducibility would each trip it. **It is not a
    tautology -- the two measurements share no draw.**
``w005_reproduces_the_recorded_collapse`` -- FALSE when this sweep's own ``w = 0.05`` minimum is
    NOT zero, i.e. this run finds acceptances at a width where G6 found none in 100,000 draws.
    **Reachable, and it would be a finding rather than a defect**: it would mean the recorded
    zero was a property of G6's particular draws. Reported either way.
``shape_is_determined``        -- FALSE on the CENSORED_BELOW branch above.

WHAT THIS SWEEP CANNOT DO, STATED BEFORE IT IS RUN
---------------------------------------------------
* **A grid understates a minimum.** ``min`` over 42 points is an upper bound on ``min`` over the
  box, so every ``p_min`` here is an upper bound and every cost derived from it a lower bound.
  Unchanged from G6.
* **It measures a boundary in ``w``, not in any epidemiologically meaningful unit.** A relative
  half-width is a stand-in for ``Omega_0``, which this project has never specified. What a 0.6%
  box on ``beta`` means to somebody fitting a real epidemic is not a question this file answers.
* **It is one simulator, one summary set, one base parameter point, one selection rule.** The
  same conditionality every number in this repository carries, plus ``DEVIATIONS.md`` D-14's.
* **It does not price, implement or rehabilitate the composition.** D-16 forecloses that.
"""

from __future__ import annotations

import argparse
import math
import os
import sys
import tempfile
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from ..attribution.selection import VARIANTS, build_rule
from ..provenance import header, now_iso
from ..runlock import check_pidfile, write_pidfile
from ..simulators import sir3
from ..simulators.sir3 import BASE, COMPONENTS, K, with_params
from .cost_gate import GATE_DRAWS, M_VALUES, N_VALUES, cost
from .jacobian_rank import KAPPA_MAX, TAU
from .p_sel import (
    FAMILY_CODES,
    NORM_TOL,
    NUISANCE_COORDS,
    SUMMARY_SET,
    _counts,
    _draw_task,
    load_jacobian,
    load_normalisation,
    nuisance_grid,
    wilson,
)

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results"

# ---------------------------------------------------------------------------------------
# PRE-REGISTERED DESIGN CONSTANTS -- committed before the first run
# ---------------------------------------------------------------------------------------

#: Relative half-widths swept, between theta_0 and the recorded +/-5% boundary. Ten points,
#: denser over 0.002-0.02 where Q-16 predicted the boundary lies. See the module docstring
#: for why that region and not another.
WIDTHS: tuple[float, ...] = (0.001, 0.002, 0.003, 0.005, 0.0075, 0.01, 0.015, 0.02, 0.03, 0.05)

N_THETA0: int = 100_000      #: the w = 0 anchor, and the reproduction check
N_SCREEN: int = 10_000       #: per design point per width. G6's stage B1 count, unchanged
N_REFINE_DRAWS: int = 100_000  #: per re-measured point. G6's stage B2 count, unchanged
N_REFINE_POINTS_PER_WIDTH: int = 4  #: cap on distinct points re-measured at each width.
#: Four is the number of (assignment, variant) keys, so the cap can never drop a key's own
#: screened argmin. Where it nevertheless is not refined -- it cannot be, at this cap, but
#: the code does not rely on that -- the reported minimum falls back to the SCREENED value
#: rather than to a refined value measured somewhere else, because the screened minimum is
#: biased LOW and a fallback that rounded upward would flatter the composition.

#: The shape criterion's one threshold. Declared here, before the data exist.
SLOPE_RATIO_ABRUPT: float = 3.0

#: sqrt(d) for S_B: the magnitude of a single null draw's normalised discrepancy, by
#: construction, since every summary coordinate is divided by its prior-predictive sd.
#: Reported next to the nuisance shift so the ratio the mechanism turns on is visible.
NOISE_MAGNITUDE_SQRT_D: float = math.sqrt(10.0)


def loglinear_fit(w: list[float], p: list[float]) -> dict[str, Any]:
    """``log10 p = a + b*w`` by least squares, with ``R^2``. Descriptive, not a criterion."""
    if len(w) < 3:
        return {"fitted": False, "why": "fewer than three live widths"}
    x = np.asarray(w, dtype=float)
    y = np.log10(np.asarray(p, dtype=float))
    b, a = np.polyfit(x, y, 1)
    pred = a + b * x
    ss_res = float(np.sum((y - pred) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    return {
        "fitted": True,
        "intercept_a": float(a),
        "slope_b_decades_per_unit_half_width": float(b),
        "r_squared": float(1.0 - ss_res / ss_tot) if ss_tot > 0 else float("nan"),
        "residuals_log10": [float(v) for v in (y - pred)],
        "note": "descriptive. R^2 is reported and is NOT part of the shape criterion.",
    }


def classify_shape(widths: list[float], p_min: list[float]) -> dict[str, Any]:
    """The pre-registered shape criterion. See the module docstring for the three branches."""
    live = [(w, p) for w, p in zip(widths, p_min) if p > 0.0]
    smallest_is_dead = bool(p_min and p_min[0] <= 0.0)
    if smallest_is_dead or len(live) < 4:
        return {
            "shape": "CENSORED_BELOW",
            "shape_is_determined": False,
            "why": ("p_min is already zero at the smallest width measured, so the boundary lies "
                    "below this sweep" if smallest_is_dead else
                    f"only {len(live)} widths have p_min > 0; the criterion requires 4"),
            "n_live_widths": len(live),
            "slope_ratio": None,
            "loglinear_fit": None,
        }
    lw = [w for w, _ in live]
    lp = [p for _, p in live]
    slopes = [(math.log10(lp[i + 1]) - math.log10(lp[i])) / (lw[i + 1] - lw[i])
              for i in range(len(live) - 1)]
    a = [abs(s) for s in slopes]
    ratio = float(max(a) / np.median(a)) if np.median(a) > 0 else float("inf")
    return {
        "shape": "ABRUPT" if ratio >= SLOPE_RATIO_ABRUPT else "GRADUAL",
        "shape_is_determined": True,
        "criterion": (f"ABRUPT iff max|s_i| / median|s_i| >= {SLOPE_RATIO_ABRUPT}, with s_i the "
                      "local log-slope in decades per unit relative half-width"),
        "n_live_widths": len(live),
        "live_widths": lw,
        "local_log_slopes_decades_per_unit_half_width": [float(s) for s in slopes],
        "slope_ratio": ratio,
        "slope_ratio_threshold": SLOPE_RATIO_ABRUPT,
        "steepest_interval": [float(lw[int(np.argmax(a))]), float(lw[int(np.argmax(a)) + 1])],
        "loglinear_fit": loglinear_fit(lw, lp),
    }


def gate_row(p: float, lo: float, hi: float) -> dict[str, Any]:
    """The pre-registered cost gate applied at one ``p_sel``, for characterisation only.

    **This does not reopen anything.** ``docs/DECISIONS.md`` D-16 is decided and is not
    contingent on any width at which the gate would have passed. The row exists so the
    negative-result figure can mark the gate line the specification registered, at the scale
    the specification registered it on.
    """
    rows = []
    for m in M_VALUES:
        for n in N_VALUES:
            rows.append({
                "M": int(m), "N": int(n),
                "expected_draws": cost(m, n, p),
                "expected_draws_ci95_lower": cost(m, n, hi),
                "expected_draws_ci95_upper": cost(m, n, lo),
                "passes": bool(cost(m, n, p) <= GATE_DRAWS),
            })
    n_pass = sum(1 for r in rows if r["passes"])
    return {
        "gate_draws_threshold": GATE_DRAWS,
        "corners": rows,
        "verdict": "PASS" if n_pass == len(rows) else ("FAIL" if n_pass == 0 else "SPLIT"),
        "this_is_characterisation_not_a_decision":
            "docs/DECISIONS.md D-16 drops the composition and was decided before this sweep "
            "ran. A PASS at some width does not revive it.",
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="boundary sweep (session G7, Phase 1; O-30)")
    ap.add_argument("--seed", type=int, default=20260821)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--theta0-draws", type=int, default=N_THETA0)
    ap.add_argument("--screen-draws", type=int, default=N_SCREEN)
    ap.add_argument("--refine-draws", type=int, default=N_REFINE_DRAWS)
    ap.add_argument("--out", type=str, default="results/boundary_sweep.yaml",
                    help="output path relative to the repository root. Overridden only for "
                         "smoke runs, which must not write into results/.")
    args = ap.parse_args(argv)

    command = "python -m src.diagnostics.boundary_sweep " + " ".join(
        f"--{k.replace('_', '-')} {v}" for k, v in vars(args).items())
    started = now_iso()
    t_start = time.perf_counter()

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = REPO / out_path
    lock = Path(tempfile.gettempdir()) / "sim-attrib-runs" / f"{out_path.stem}.json"
    prior = check_pidfile(lock)
    if prior["alive"]:
        raise SystemExit(
            f"REFUSING TO START: pid {prior['pid']} is already running {prior['command']!r} "
            f"and will write {prior.get('outputs')}. Standing constraint S3.")
    write_pidfile(lock, module="src.diagnostics.boundary_sweep", outputs=[str(out_path)])
    print(f"pidfile {lock} (pid {os.getpid()})", flush=True)

    # -- the constants the rule is built from, and the checks that they are the right ones --
    norm = load_normalisation()
    norm_rows = _draw_task((0, {}, norm["seed0"], norm["n_replicates"]))[1]
    m_re, sd_re = norm_rows.mean(axis=0), norm_rows.std(axis=0, ddof=1)
    rel_mean = float(np.max(np.abs(m_re - norm["mean"]) / np.abs(norm["mean"])))
    rel_sd = float(np.max(np.abs(sd_re - norm["sd"]) / np.abs(norm["sd"])))
    norm_ok = bool(max(rel_mean, rel_sd) < NORM_TOL)
    print(f"normalisation reproduces: {norm_ok} (mean {rel_mean:.3e}, sd {rel_sd:.3e})",
          flush=True)
    if not norm_ok:
        raise SystemExit("ABORTING: the recorded normalisation does not reproduce here.")

    a = sir3.simulate(np.zeros(K), seed=7, params=with_params(families="adversarial"))
    b = sir3.simulate(np.zeros(K), seed=7, params=with_params(families="base"))
    families_agree = bool(np.array_equal(a.reported, b.reported))
    if not families_agree:
        raise SystemExit("ABORTING: the family sets differ at eta = 0.")

    jac = {code: load_jacobian(code) for code in FAMILY_CODES}
    for code, j in jac.items():
        if not j["reproduces"]:
            raise SystemExit(f"ABORTING: no step size reproduces the recorded spectrum for {code}.")
    print("jacobian reproduces: True for " + ", ".join(FAMILY_CODES), flush=True)

    rules = {
        (code, variant): build_rule(
            summary_set=SUMMARY_SET, family_code=code, variant=variant,
            m0=norm["mean"], sd=norm["sd"], J=jac[code]["J"],
            component_labels=COMPONENTS, tau=TAU, kappa_max=KAPPA_MAX)
        for code in FAMILY_CODES for variant in VARIANTS
    }
    keys = sorted(f"{c}|{v}" for c in FAMILY_CODES for v in VARIANTS)
    primary = "AAA|studentised"

    # -- seed spans, and the check that they do not touch anything G6 drew ----------------
    grid = nuisance_grid(WIDTHS)
    seed_anchor = args.seed + 1_000_000_000
    seed_screen = args.seed + 2_000_000_000
    seed_refine = args.seed + 3_500_000_000
    mine = {
        "anchor": (seed_anchor, seed_anchor + args.theta0_draws),
        "screen": (seed_screen, seed_screen + len(grid) * 1_000_000),
        "refine": (seed_refine, seed_refine + len(WIDTHS) * N_REFINE_POINTS_PER_WIDTH * 1_000_000),
    }
    recorded = yaml.safe_load((OUT / "p_sel.yaml").read_text(encoding="utf-8"))
    g6 = recorded["settings"]["seeds"]
    theirs = {
        "G6_theta0": (int(g6["theta0"]), int(g6["theta0"]) + int(recorded["settings"]["n_draws_theta0"])),
        "G6_screen": (int(g6["screen"]), int(g6["screen"]) + int(recorded["settings"]["n_grid_points"]) * 1_000_000),
        "G6_refine": (int(g6["refine"]), int(g6["refine"]) + int(recorded["settings"]["n_points_refined"]) * 1_000_000),
        "normalisation": (norm["seed0"], norm["seed0"] + norm["n_replicates"]),
    }
    overlaps = [f"{n1}{s1} vs {n2}{s2}"
                for n1, s1 in mine.items() for n2, s2 in theirs.items()
                if not (s1[1] <= s2[0] or s2[1] <= s1[0])]
    spans_disjoint = not overlaps
    if not spans_disjoint:
        raise SystemExit(
            "ABORTING: seed spans overlap G6's: " + "; ".join(overlaps) +
            ". A reproduction check run on the same draws is not a check.")
    print("seed spans disjoint from results/p_sel.yaml: True", flush=True)

    pool_kw = {"max_workers": args.workers}
    total_draws = 0

    # ---- the w = 0 anchor: theta_0, on independent draws --------------------------------
    print(f"\nanchor: theta_0, {args.theta0_draws} draws", flush=True)
    chunk = 5_000
    tasks = [(i, {}, seed_anchor + i * chunk, min(chunk, args.theta0_draws - i * chunk))
             for i in range((args.theta0_draws + chunk - 1) // chunk)]
    acc0: dict[str, list[int]] = {}
    with ProcessPoolExecutor(**pool_kw) as pool:
        for _idx, block in pool.map(_draw_task, tasks, chunksize=1):
            new = _counts(rules, block)
            for key, c in new.items():
                acc0.setdefault(key, [0] * K)
                for k in range(K):
                    acc0[key][k] += c[k]
            total_draws += len(block)
    print(f"  theta_0 cells (primary): {acc0[primary]}", flush=True)

    # Does it reproduce what G6 recorded, on draws G6 never took?
    rec_a = recorded["stage_A_theta0"]
    repro_rows = []
    for key in keys:
        for k in range(K):
            p_here = acc0[key][k] / args.theta0_draws
            lo_r, hi_r = float(rec_a[key]["ci95_lower"][k]), float(rec_a[key]["ci95_upper"][k])
            inside = bool(lo_r <= p_here <= hi_r)
            repro_rows.append({
                "key": key, "cell": COMPONENTS[k],
                "p_sel_here": float(p_here),
                "p_sel_recorded": float(rec_a[key]["p_sel"][k]),
                "recorded_ci95": [lo_r, hi_r],
                "inside_recorded_ci95": inside,
            })
    theta0_reproduces = bool(all(r["inside_recorded_ci95"] for r in repro_rows))
    print(f"  theta0_reproduces_recorded_p_sel: {theta0_reproduces}", flush=True)

    # ---- the sweep ----------------------------------------------------------------------
    print(f"\nsweep: {len(WIDTHS)} widths x 42 points x {args.screen_draws} draws", flush=True)
    tasks_s = [(i, pt["theta"], seed_screen + i * 1_000_000, args.screen_draws)
               for i, pt in enumerate(grid)]
    screen: list[dict[str, list[int]]] = [None] * len(grid)  # type: ignore[list-item]
    z_means: list[list[float]] = [None] * len(grid)  # type: ignore[list-item]
    with ProcessPoolExecutor(**pool_kw) as pool:
        for idx, block in pool.map(_draw_task, tasks_s, chunksize=1):
            screen[idx] = _counts(rules, block)
            z_means[idx] = [float(x) for x in ((block - norm["mean"]) / norm["sd"]).mean(axis=0)]
            total_draws += len(block)
            if (idx + 1) % 10 == 0 or idx == len(grid) - 1:
                print(f"  point {idx + 1}/{len(grid)}  {grid[idx]['key']}", flush=True)

    # which points to re-measure: the screened argmin for each key, per width, deduplicated
    by_width: dict[float, list[int]] = {w: [] for w in WIDTHS}
    for i, pt in enumerate(grid):
        by_width[pt["width"]].append(i)
    refine_targets: list[int] = []
    for w in WIDTHS:
        idxs = by_width[w]
        cand: list[int] = []
        for key in keys:
            j = min(idxs, key=lambda i: min(screen[i][key]))
            if j not in cand:
                cand.append(j)
        cand.sort(key=lambda i: min(screen[i][primary]))
        refine_targets.extend(cand[:N_REFINE_POINTS_PER_WIDTH])

    print(f"\nrefine: {len(refine_targets)} points x {args.refine_draws} draws", flush=True)
    tasks_r = [(j, grid[i]["theta"], seed_refine + j * 1_000_000, args.refine_draws)
               for j, i in enumerate(refine_targets)]
    refined: dict[int, dict[str, list[int]]] = {}
    with ProcessPoolExecutor(**pool_kw) as pool:
        for j, block in pool.map(_draw_task, tasks_r, chunksize=1):
            refined[refine_targets[j]] = _counts(rules, block)
            total_draws += len(block)
            print(f"  refine {j + 1}/{len(refine_targets)}  {grid[refine_targets[j]]['key']}",
                  flush=True)

    elapsed = time.perf_counter() - t_start

    # ---- assemble ------------------------------------------------------------------------
    def cell_block(counts: list[int], n: int) -> dict[str, Any]:
        lo_hi = [wilson(counts[k], n) for k in range(K)]
        return {
            "n_draws": int(n),
            "counts": [int(x) for x in counts],
            "p_sel": [float(x / n) for x in counts],
            "ci95_lower": [float(lo_hi[k][0]) for k in range(K)],
            "ci95_upper": [float(lo_hi[k][1]) for k in range(K)],
        }

    def worst(counts: list[int], n: int) -> tuple[float, float, float, int]:
        """Worst cell: (p, ci_lo, ci_hi, k)."""
        k = int(np.argmin(counts))
        lo, hi = wilson(counts[k], n)
        return counts[k] / n, lo, hi, k

    # per width, per key, the minimum over the design and where it is attained
    per_width: list[dict[str, Any]] = []
    for w in WIDTHS:
        idxs = by_width[w]
        zs = [float(np.linalg.norm(z_means[i])) for i in idxs]
        entry: dict[str, Any] = {
            "width": float(w),
            "n_design_points": len(idxs),
            "nuisance_shift_norm_of_mean_z": {
                "median": float(np.median(zs)), "max": float(np.max(zs)),
                "min": float(np.min(zs)),
                "single_draw_noise_magnitude_sqrt_d": NOISE_MAGNITUDE_SQRT_D,
                "median_over_noise": float(np.median(zs) / NOISE_MAGNITUDE_SQRT_D),
            },
            "by_key": {},
        }
        for key in keys:
            j = min(idxs, key=lambda i: min(screen[i][key]))
            p_s, lo_s, hi_s, k_s = worst(screen[j][key], args.screen_draws)
            own_refined = j in refined
            # Candidates for the reported minimum. The screened value at this key's own argmin
            # enters ONLY when that point was not re-measured, because a screened minimum is
            # biased low and using it where a de-biased value exists would overstate the
            # collapse; dropping it where no de-biased value exists would understate it.
            cands = [(p_s, lo_s, hi_s, k_s, grid[j]["key"], "screen", args.screen_draws)] \
                if not own_refined else []
            for i in idxs:
                if i in refined:
                    p_r, lo_r, hi_r, k_r = worst(refined[i][key], args.refine_draws)
                    cands.append((p_r, lo_r, hi_r, k_r, grid[i]["key"], "refined",
                                  args.refine_draws))
            p_u, lo_u, hi_u, k_u, at_u, src, n_used = min(cands, key=lambda c: c[0])
            n_dead = sum(1 for i in idxs if min(screen[i][key]) == 0)
            entry["by_key"][key] = {
                "screened_min": {"p_sel": p_s, "ci95": [lo_s, hi_s], "cell": COMPONENTS[k_s],
                                 "at_point": grid[j]["key"], "n_draws": args.screen_draws},
                "own_argmin_was_re_measured": bool(own_refined),
                "reported_min": {"p_sel": p_u, "ci95": [lo_u, hi_u], "cell": COMPONENTS[k_u],
                                 "at_point": at_u, "source": src, "n_draws": n_used,
                                 "de_biased": bool(src == "refined")},
                "n_design_points_with_a_dead_cell": n_dead,
                "fraction_of_design_points_with_a_dead_cell": float(n_dead / len(idxs)),
                "gate": gate_row(p_u, lo_u, hi_u),
            }
        per_width.append(entry)

    # the anchor as width 0, on the same shape, so a figure can plot one series
    anchor_by_key = {}
    for key in keys:
        p0, lo0, hi0, k0 = worst(acc0[key], args.theta0_draws)
        anchor_by_key[key] = {
            "cells": cell_block(acc0[key], args.theta0_draws),
            "reported_min": {"p_sel": p0, "ci95": [lo0, hi0], "cell": COMPONENTS[k0],
                             "at_point": "theta_0", "source": "anchor",
                             "n_draws": args.theta0_draws},
            "gate": gate_row(p0, lo0, hi0),
        }

    shape = {}
    for key in keys:
        ws = [0.0] + [float(w) for w in WIDTHS]
        ps = [anchor_by_key[key]["reported_min"]["p_sel"]] + [
            e["by_key"][key]["reported_min"]["p_sel"] for e in per_width]
        shape[key] = classify_shape(ws, ps)

    w005 = next(e for e in per_width if e["width"] == 0.05)
    w005_min = min(w005["by_key"][key]["reported_min"]["p_sel"] for key in keys)
    w005_collapse_reproduces = bool(w005_min == 0.0)

    doc: dict[str, Any] = {
        "provenance": header(script="src/diagnostics/boundary_sweep.py", command=command,
                             seed=args.seed, started=started),
        "what_this_is":
            "Session G7, Phase 1. OUTSTANDING.md O-30: the nuisance half-width at which the "
            "selection cells stop being reachable, between theta_0 and the +/-5% boundary "
            "session G6 measured. It reports p_min(w) = min over the 42-point design, min over "
            "the K cells, of p_sel -- the quantity audit/MMC_COMPOSITION_SPEC.md section 4 "
            "point 1 and src/diagnostics/cost_gate.py both consume.",
        "this_is_characterisation_not_verdict_seeking":
            "docs/DECISIONS.md D-16 -- the MMC composition is dropped as an experimental "
            "vehicle and kept as a stated negative result -- was DECIDED by the operator at the "
            "start of session G7, BEFORE this script was written and before any number in this "
            "file existed. Nothing here can soften or reopen it. What it buys is a negative "
            "result with a shape rather than a bare threshold statement. Had this sweep found "
            "the cells reachable out to 0.04, the composition would still be dropped: D-16's "
            "reason is that section 3.4's lemma forces a theta-free rule and this simulator's "
            "nuisance-to-noise ratio then makes the observed cell unreachable somewhere inside "
            "any box a domain reader would call plausible.",
        "scope_assumption_D14":
            "docs/DECISIONS.md D-14 (DECIDED, operator, 2026-08-20): every claim this project "
            "makes about component separability and attribution is scoped to a distortion model "
            "that assigns AT MOST ONE one-parameter distortion family to each component. The "
            "selection rule measured here is a K = 3 object and is meaningful only under that "
            "restriction.",
        "settings": {
            "summary_set": SUMMARY_SET,
            "family_codes": list(FAMILY_CODES),
            "variants": list(VARIANTS),
            "primary_key": primary,
            "nuisance_coordinates": list(NUISANCE_COORDS),
            "theta_0": {c: float(getattr(BASE, c)) for c in NUISANCE_COORDS},
            "widths": [float(w) for w in WIDTHS],
            "design_per_width": "32 corners + 10 axis endpoints, from "
                                "src/diagnostics/p_sel.nuisance_grid -- G6's design function, "
                                "reused rather than rewritten so the w = 0.05 row is directly "
                                "comparable with the recorded number",
            "n_grid_points": len(grid),
            "n_draws_theta0": args.theta0_draws,
            "n_draws_screen": args.screen_draws,
            "n_draws_refine": args.refine_draws,
            "n_points_refined": len(refine_targets),
            "n_refine_points_per_width_cap": N_REFINE_POINTS_PER_WIDTH,
            "seeds": {"anchor": seed_anchor, "screen": seed_screen, "refine": seed_refine},
            "seed_spans_used": {k: list(v) for k, v in mine.items()},
            "seed_spans_recorded_in_p_sel_yaml": {k: list(v) for k, v in theirs.items()},
            "workers": args.workers,
            "n_simulator_runs": int(total_draws + norm["n_replicates"]),
            "wall_clock_seconds": float(elapsed),
            "seconds_per_draw_measured": float(elapsed / max(1, total_draws)),
        },
        "checks": {
            "normalisation_reproduces": norm_ok,
            "normalisation_max_relative_difference": {"mean": rel_mean, "sd": rel_sd,
                                                      "tolerance": NORM_TOL},
            "jacobian_reproduces": {c: jac[c]["reproduces"] for c in FAMILY_CODES},
            "family_sets_agree_at_zero": families_agree,
            "seed_spans_disjoint_from_G6": spans_disjoint,
            "theta0_reproduces_recorded_p_sel": theta0_reproduces,
            "theta0_reproduction_detail": repro_rows,
            "w005_reproduces_the_recorded_collapse": w005_collapse_reproduces,
            "w005_reproduction_note":
                "FALSE here would mean this run found acceptances at a width where G6 found "
                "none in 100,000 draws -- a finding about the recorded zero, not a defect in "
                "this run. The two measurements share no draw.",
            "shape_is_determined": {key: shape[key]["shape_is_determined"] for key in keys},
        },
        "anchor_theta0": anchor_by_key,
        "shape_of_the_collapse": shape,
        "per_width": per_width,
        "design_points": [
            {
                "key": pt["key"], "width": pt["width"], "kind": pt["kind"],
                "theta": {c: float(v) for c, v in pt["theta"].items()},
                "norm_of_mean_z": float(np.linalg.norm(z_means[i])),
                "screen": {key: cell_block(screen[i][key], args.screen_draws) for key in keys},
                "refined": ({key: cell_block(refined[i][key], args.refine_draws) for key in keys}
                            if i in refined else None),
            }
            for i, pt in enumerate(grid)
        ],
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(yaml.safe_dump(doc, sort_keys=False, width=100), encoding="utf-8")
    print(f"\nwrote {out_path}  ({total_draws} draws, {elapsed:.0f} s)", flush=True)
    for key in keys:
        print(f"  {key}: shape = {shape[key]['shape']}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
