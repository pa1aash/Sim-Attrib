"""The rank verdict at K = 6, run through the machinery the K = 3 verdict was run through.

WHY THIS EXISTS, AND WHAT IT IS AND IS NOT ANSWERING
-----------------------------------------------------
``audit/G3_ADVERSARIAL_REVIEW.md`` finding 1 leaves the gapless-spectrum objection
**DEFERRED rather than defeated**: the reported three-column spectra span about a decade,
so Gutenkunst et al.'s "many decades, no gap" picture does not describe them -- but three
columns *cannot* display a decades-wide gapless decay however badly conditioned the model
is, so the reassurance may be a fact about ``K = 3`` rather than about the simulator.
``results/robustness/wide_spectrum_check.yaml`` measured a six-column spectrum and found it
2.80 decades wide for ``S_B``, with ``tau`` falling inside it.

**That measurement was taken at ONE step size.** ``docs/THRESHOLDS.md`` §1.4 states, in this
project's own words, that *"a rank computed at a single step size h is not a result"*, and
requires the h-plateau and the resolution test. The number the deferred objection now rests
on was computed without either. This script supplies them: the same ``H_VALUES`` sweep, the
same plateau rule, the same resolution criterion, the same equivalence-class rule and the
same permutation-equivariance leakage check that produced every number in ``results/``,
applied to the six-column object.

THE SIX-COLUMN OBJECT, AND WHY THERE IS EXACTLY ONE OF THEM
------------------------------------------------------------
The session brief asks for the six-column spectrum *"under (a) the base distortion families
and (b) the adversarial families"*. **Those are not two objects.** A family set declares
three one-parameter families, so it supplies three columns and no more; the only
six-column Jacobian available from the two declared sets is the one whose columns are their
union, and that union is the same matrix whichever set you start from. Manufacturing a
second one would mean inventing three further families **after** the results are known,
which is ``DEVIATIONS.md`` **D-9**'s problem at twice the size. So this script reports:

  * the three-column spectrum under the base families, in full;
  * the three-column spectrum under the adversarial families, in full;
  * the one six-column spectrum their union defines, in full.

Recorded as ``DEVIATIONS.md`` **D-12**.

THE EIGHT MIXED TRIPLES, AND WHY THEY ARE IN SCOPE
----------------------------------------------------
A six-column verdict answers a question nobody asked: *can all six declared distortion
directions be identified at once?* The question that bears on the paper is one step back from
it. A family set assigns **one** family to each component; the two declared sets assign base
to all three and adversarial to all three. Between those two extremes sit **six further
assignments** -- base transmission with adversarial progression, and so on -- and each is a
perfectly ordinary three-column distortion model of the same simulator.

**No new family is invented to build them.** Every column comes from the two sets already
declared; the eight triples are a re-combination, not an extension, which is why this stays
inside the session's scope boundary of "the two family sets already defined". They are cheap:
the columns are already estimated for the six-column object, so all eight run through the
full machinery at no additional simulator cost.

They are also the informative object. If all eight separate, a six-column failure is a
statement about a six-dimensional distortion space and nothing narrower. If some do not, then
the failure reaches a three-column model an analyst could plausibly have declared, and the
separability claim is conditional on the family assignment and not only on the family set.

THE QUESTION THE SIX-COLUMN VERDICT ACTUALLY ANSWERS
-----------------------------------------------------
A six-column verdict is **not** a harder version of the three-column one. The six columns
are two distortions of each of the same three mechanisms, so a rank deficiency at ``K = 6``
can arise two ways, and they mean opposite things:

  * **within-mechanism** -- a near-null direction supported on ``base:X`` and ``adv:X`` for a
    single mechanism ``X``. That says two different deformations of the SAME component are
    hard to tell apart. It is not a threat to component attribution, which never claimed to
    identify *which* deformation of a component occurred.
  * **cross-mechanism** -- a near-null direction mixing two different mechanisms. That IS a
    threat to component attribution, and it is the same failure the ``K = 3`` verdict rules
    out under each family set separately.

The script therefore classifies every near-null direction, using the pre-registered
``VK_MIN`` rule from ``docs/THRESHOLDS.md`` §2.1 and no new threshold, and reports a
threshold-free ``mechanism_energy`` alongside it. **A six-column INSEPARABLE verdict whose
null directions are all within-mechanism does not overturn the three-column result; one
with a cross-mechanism null direction does.** That distinction is stated here, before the
numbers, so it cannot be chosen afterwards to suit them.

THE TAU AND KAPPA_MAX SWEEP
----------------------------
``audit/G3_ADVERSARIAL_REVIEW.md`` finding 1.4 establishes that at the registered pair
``(tau, kappa_max) = (1e-2, 100)`` the two criteria of ``docs/THRESHOLDS.md`` §1.3 are one
criterion, because ``kappa_max`` was defined as ``1/tau`` -- so the ``kappa`` branch cannot
fire unless the rank branch already has. That was named and left unexplored. Here it is
explored: the verdict is recomputed on a grid over ``tau`` AND ``kappa_max`` independently,
and the script asserts the algebra that predicts the outcome, so a disagreement between the
prediction and the production code is a failure rather than a footnote.

Every recomputation calls :func:`~src.diagnostics.jacobian_rank.analyse` itself, with the
thresholds passed as the parameters they already are. Nothing is transcribed, so nothing can
drift from the rule the reported numbers were produced by.

    python -m src.diagnostics.k6_spectrum
"""

from __future__ import annotations

import argparse
import math
import os
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any, Sequence

import numpy as np
import yaml

from ..provenance import header, now_iso
from ..runlock import check_pidfile, write_pidfile
from ..simulators import sir3
from ..simulators.sir3 import COMPONENTS, ETA_SCALE, K, prior_predictive_stats, with_params
from ..simulators.summaries import SUMMARY_LABELS, SUMMARY_SETS
from .jacobian_rank import (
    COHERENCE_FLAG,
    COLNORM_INVISIBLE,
    H_VALUES,
    KAPPA_MAX,
    PLATEAU_REL_TOL,
    RESOLVE_FACTOR,
    TAU,
    VK_MIN,
    JacobianSweep,
    analyse,
    leakage_check,
)

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results" / "robustness"

FAMILY_SETS: tuple[str, str] = ("base", "adversarial")

#: Column layout of the six-column Jacobian: three base families then three adversarial ones,
#: in COMPONENTS order within each. The mechanism of column j is ``COMPONENTS[j % K]``.
SIX_COLUMN_LABELS: tuple[str, ...] = tuple(
    f"{fs}:{c}" for fs in FAMILY_SETS for c in COMPONENTS
)
SIX_COLUMN_MECHANISM: tuple[str, ...] = tuple(COMPONENTS[j % K] for j in range(2 * K))

#: The eight component-wise assignments of a family to each component. ``"B"`` is the base
#: family for that component, ``"A"`` the adversarial one. ``BBB`` and ``AAA`` are the two
#: declared sets; the other six are re-combinations of the same columns.
TRIPLES: tuple[str, ...] = tuple(
    "".join(code) for code in __import__("itertools").product("BA", repeat=K)
)

#: Multipliers of the pre-registered tau at which the verdict is recomputed. Eight
#: alternatives spanning four decades around the registered value, which is more than the
#: brief's five and wider than G4's range -- the stakes are higher because S_B is now the only
#: surviving summary set.
TAU_MULTIPLIERS: tuple[float, ...] = (0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0)

#: Ceilings at which the kappa branch is probed INDEPENDENTLY of tau. THRESHOLDS §1.3 ties
#: kappa_max = 1/tau; these break the tie deliberately, which is the only way the kappa branch
#: is reachable at all (G4 finding 1.4).
KAPPA_MAX_GRID: tuple[float, ...] = (1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0,
                                     500.0, 1000.0, 1e4, 1e6)


# --------------------------------------------------------------------------------------
# Column estimation, parallel over (family set, h, component)
# --------------------------------------------------------------------------------------

def _column_task(
    task: tuple[int, str, float, int, int, int],
) -> tuple[int, dict[str, list[float]]]:
    """One (family set, h, component) column, unnormalised. Pure function of its arguments.

    Returns the task's index alongside its payload so the caller can reassemble in a fixed
    order regardless of completion order -- the estimate must not depend on how the work was
    scheduled, and reassembling by index rather than by arrival is what makes that true.
    """
    idx, family_set, h, k, seed0, n_rep = task
    params = with_params(families=family_set)
    step = h * ETA_SCALE
    acc: dict[str, list[np.ndarray]] = {n: [] for n in SUMMARY_SETS}
    for r in range(n_rep):
        ep, em = np.zeros(K), np.zeros(K)
        ep[k], em[k] = step, -step
        op = sir3.simulate(ep, seed=seed0 + r, params=params)
        om = sir3.simulate(em, seed=seed0 + r, params=params)
        for n, fn in SUMMARY_SETS.items():
            acc[n].append((fn(op) - fn(om)) / (2.0 * h))
    return idx, {n: [float(x) for x in np.mean(np.asarray(v), axis=0)] for n, v in acc.items()}


def estimate_columns(
    *,
    h_values: Sequence[float],
    n_replicates: int,
    seed0: int,
    workers: int,
) -> dict[tuple[str, int, int], dict[str, np.ndarray]]:
    """Unnormalised Jacobian columns for every (family set, h index, component).

    ``workers <= 1`` runs the identical computation sequentially. ``tests/test_k6_spectrum.py``
    asserts the two paths agree bit-for-bit, so the parallel path is not taken on trust.
    """
    tasks: list[tuple[int, str, float, int, int, int]] = []
    keys: list[tuple[str, int, int]] = []
    for family_set in FAMILY_SETS:
        for hi, h in enumerate(h_values):
            for k in range(K):
                tasks.append((len(tasks), family_set, float(h), k, seed0, n_replicates))
                keys.append((family_set, hi, k))

    payloads: list[dict[str, list[float]] | None] = [None] * len(tasks)
    if workers <= 1:
        for t in tasks:
            i, payload = _column_task(t)
            payloads[i] = payload
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for i, payload in pool.map(_column_task, tasks, chunksize=1):
                payloads[i] = payload
                print(f"  column {i + 1}/{len(tasks)} done", flush=True)

    out: dict[tuple[str, int, int], dict[str, np.ndarray]] = {}
    for key, payload in zip(keys, payloads):
        assert payload is not None
        out[key] = {n: np.asarray(v, dtype=float) for n, v in payload.items()}
    return out


def _sweep(
    name: str,
    cols: list[list[np.ndarray]],
    sd: np.ndarray,
    *,
    h_values: Sequence[float],
    n_replicates: int,
    seed0: int,
    n_simulations: int,
) -> JacobianSweep:
    """Assemble a :class:`JacobianSweep`; ``cols[hi]`` is the list of columns at step ``hi``."""
    return JacobianSweep(
        summary_set=name,
        h_values=tuple(float(h) for h in h_values),
        jacobians=tuple(np.column_stack([c / sd for c in per_h]) for per_h in cols),
        sd=np.asarray(sd, dtype=float),
        n_replicates=n_replicates,
        seed0=seed0,
        crn=True,
        eta_scale=ETA_SCALE,
        n_simulations=n_simulations,
    )


# --------------------------------------------------------------------------------------
# Description of a spectrum -- descriptive only, no new pass/fail threshold
# --------------------------------------------------------------------------------------

def describe_spectrum(sv: Sequence[float], tau: float) -> dict[str, Any]:
    """Shape of a spectrum, in quantities that introduce no decision threshold.

    Deliberately NOT a gap test. Inventing a "there is a gap iff ratio > G" rule now, with the
    singular values already visible, is the leakage failure ``LEDGER_DESIGN.md`` D3 exists to
    prevent (**Q-11**). Everything here is a description; the only verdict is the
    pre-registered one, computed elsewhere by :func:`analyse`.

    ``where_tau_sits`` is the operational quantity and needs no threshold at all: the objection
    Gutenkunst et al. raise is that ``tau`` cuts arbitrarily through a dense continuum, and
    whether ``tau`` is *inside* the spectrum or an order of magnitude below its smallest member
    is a fact, not a judgement.
    """
    s = [float(x) for x in sv]
    s1 = s[0]
    pos = [x for x in s if x > 0]
    ratios = [x / s1 for x in s]
    adj = [(s[i] / s[i + 1]) if s[i + 1] > 0 else math.inf for i in range(len(s) - 1)]
    finite = [a for a in adj if math.isfinite(a)]
    median_adj = float(np.median(finite)) if finite else None
    largest = max(finite) if finite else None

    # Where tau*sigma_1 falls relative to the spectrum: the index of the smallest singular
    # value still at or above it, and the gap to the next one down, in decades.
    n_above = sum(1 for x in s if x >= tau * s1)
    if n_above == len(s):
        where = "below the whole spectrum"
    elif n_above == 0:
        where = "above the whole spectrum"
    else:
        where = f"inside the spectrum, between sigma_{n_above} and sigma_{n_above + 1}"

    return {
        "singular_values": s,
        "sigma_i_over_sigma_1": ratios,
        "n_positive": len(pos),
        "n_structurally_zero": len(s) - len(pos),
        "adjacent_ratios": adj,
        "spread_decades_over_positive_singular_values": (
            float(math.log10(pos[0] / pos[-1])) if len(pos) > 1 else None
        ),
        "largest_adjacent_ratio": largest,
        "largest_adjacent_ratio_falls_after_index": (
            int(int(np.argmax([a if math.isfinite(a) else -1.0 for a in adj])) + 1) if adj else None
        ),
        "median_adjacent_ratio": median_adj,
        "gap_prominence_largest_over_median_adjacent_ratio": (
            float(largest / median_adj) if (largest is not None and median_adj) else None
        ),
        "gap_prominence_is_descriptive_not_a_criterion": (
            "A dimensionless shape statistic: 1.0 means the decay is perfectly geometric (no "
            "break anywhere), larger means one adjacent ratio dominates the rest. No threshold "
            "is applied to it and no verdict depends on it."
        ),
        "where_tau_sigma1_sits": where,
        "tau_times_sigma1": float(tau * s1),
        "n_singular_values_at_or_above_tau_sigma1": int(n_above),
    }


def classify_near_null(direction: dict[str, Any]) -> dict[str, Any]:
    """Is a six-column near-null direction WITHIN one mechanism, or ACROSS mechanisms?

    Uses the pre-registered equivalence-class rule (``THRESHOLDS`` §2.1: component k is in the
    class iff ``|v_k| >= VK_MIN`` throughout the plateau) and introduces no new threshold. The
    ``mechanism_energy`` figures alongside it are threshold-free: the squared weight the
    direction puts on each mechanism's two columns, summing to one.

    See the module docstring for why the distinction decides what a six-column INSEPARABLE
    verdict means.
    """
    v = np.asarray(direction["right_singular_vector_at_representative_h"], dtype=float)
    energy = {c: float(v[j] ** 2 + v[j + K] ** 2) for j, c in enumerate(COMPONENTS)}
    members = list(direction["equivalence_class_members"])
    borderline = list(direction["borderline_members"])
    mech_members = sorted({SIX_COLUMN_MECHANISM[j] for j in members})
    mech_borderline = sorted({SIX_COLUMN_MECHANISM[j] for j in borderline})
    return {
        "column_members": [SIX_COLUMN_LABELS[j] for j in members],
        "column_borderline": [SIX_COLUMN_LABELS[j] for j in borderline],
        "mechanisms_in_class": mech_members,
        "mechanisms_borderline": mech_borderline,
        "kind": (
            "no members above vk_min" if not mech_members
            else "within-mechanism" if len(mech_members) == 1
            else "cross-mechanism"
        ),
        "mechanism_energy": energy,
        "dominant_mechanism_energy_share": float(max(energy.values())),
        "what_the_kind_means": (
            "within-mechanism: two different deformations of the SAME component are hard to "
            "tell apart, which component attribution never claimed to do and which does not "
            "bear on the K = 3 verdict. cross-mechanism: two DIFFERENT components are "
            "confounded, which is the same failure the K = 3 verdict rules out."
        ),
    }


# --------------------------------------------------------------------------------------
# tau / kappa_max exploration
# --------------------------------------------------------------------------------------

def _row(sweep: JacobianSweep, tau: float, kappa_max: float) -> dict[str, Any]:
    a = analyse(sweep, tau=tau, kappa_max=kappa_max)
    nr = a["numerical_rank"]
    return {
        "tau": float(tau),
        "kappa_max": float(kappa_max),
        "rank_certain": int(nr["rank_certain"]),
        "rank_possible": int(nr["rank_possible"]),
        "rank_determined": bool(nr["determined"]),
        "condition_number": a["condition_number"],
        "rank_branch_fires": bool((not nr["determined"]) or nr["rank_certain"] < a["dimensions"]["K"]),
        "kappa_branch_fires": bool(a["condition_number"] > kappa_max),
        "kappa_branch_fires_alone": bool(
            a["condition_number"] > kappa_max
            and nr["determined"]
            and nr["rank_certain"] == a["dimensions"]["K"]
        ),
        "verdict": "INSEPARABLE" if a["inseparable"] else "separable",
        "reason": a["inseparable_reason"],
    }


def tau_sensitivity(sweep: JacobianSweep) -> dict[str, Any]:
    """Verdict at alternative tolerances, both couplings, plus the exact flip point."""
    coupled = [_row(sweep, TAU * m, 1.0 / (TAU * m)) for m in TAU_MULTIPLIERS]
    tau_only = [_row(sweep, TAU * m, KAPPA_MAX) for m in TAU_MULTIPLIERS]
    base = analyse(sweep)
    sv = base["singular_values_at_representative_h"]
    kk = base["dimensions"]["K"]
    tau_star = float(sv[-1] / sv[0]) if sv[0] > 0 else 0.0

    def _stable_span(rows: list[dict[str, Any]]) -> dict[str, Any]:
        reg = next(r for r in rows if abs(r["tau"] - TAU) < 1e-15)
        verdict = reg["verdict"]
        lo = hi = rows.index(reg)
        while lo - 1 >= 0 and rows[lo - 1]["verdict"] == verdict:
            lo -= 1
        while hi + 1 < len(rows) and rows[hi + 1]["verdict"] == verdict:
            hi += 1
        return {
            "verdict_at_registered_tau": verdict,
            "stable_over_tau_range": [rows[lo]["tau"], rows[hi]["tau"]],
            "stable_over_multiplier_range": [rows[lo]["tau"] / TAU, rows[hi]["tau"] / TAU],
            "flips_at_next_tau_below": (rows[lo - 1]["tau"] if lo > 0 else None),
            "flips_at_next_tau_above": (rows[hi + 1]["tau"] if hi + 1 < len(rows) else None),
            "boundary_is_censored_by_the_grid_below": bool(lo == 0),
            "boundary_is_censored_by_the_grid_above": bool(hi == len(rows) - 1),
        }

    return {
        "K": int(kk),
        "registered": {"tau": TAU, "kappa_max": KAPPA_MAX},
        "exact_flip_point": {
            "tau_star_sigma_K_over_sigma_1": tau_star,
            "as_multiple_of_registered_tau": (tau_star / TAU) if tau_star > 0 else 0.0,
            "meaning": (
                "the rank branch fires for any tau > tau_star. Exact, not sampled: the rule is "
                "sigma_K >= tau*sigma_1, so the flip is at sigma_K/sigma_1 = 1/kappa."
            ),
        },
        "coupled_kappa_max_equals_one_over_tau": coupled,
        "coupled_stability": _stable_span(coupled),
        "tau_varied_alone_kappa_max_held_at_registered_100": tau_only,
        "tau_varied_alone_stability": _stable_span(tau_only),
    }


def kappa_branch_exploration(sweep: JacobianSweep) -> dict[str, Any]:
    """The kappa_max branch, varied independently of tau. G4 finding 1.4, left unexplored there.

    The algebra is exact and is asserted rather than described. With every singular value
    resolved, the rank branch fires iff ``kappa > 1/tau`` and the kappa branch fires iff
    ``kappa > kappa_max``. So the kappa branch fires ALONE exactly on
    ``kappa_max < kappa <= 1/tau``, which is empty when ``kappa_max >= 1/tau`` -- and the
    registered pair sets ``kappa_max = 1/tau`` precisely.

    The grid below recomputes the verdict through :func:`analyse` at every ``(tau, kappa_max)``
    pair and the caller checks the grid against that prediction, so a disagreement between the
    algebra and the production code is a failure and not a footnote.
    """
    grid = []
    for m in TAU_MULTIPLIERS:
        for km in KAPPA_MAX_GRID:
            grid.append(_row(sweep, TAU * m, km))
    alone = [r for r in grid if r["kappa_branch_fires_alone"]]
    kappa = analyse(sweep)["condition_number"]
    return {
        "measured_condition_number": kappa,
        "prediction": (
            "with every singular value resolved, the kappa branch fires alone exactly on "
            "kappa_max < kappa <= 1/tau; it is unreachable whenever kappa_max >= 1/tau, and "
            "the registered pair sets kappa_max = 1/tau exactly"
        ),
        "n_grid_points": len(grid),
        "n_where_kappa_branch_fires_alone": len(alone),
        "kappa_branch_alone_region": [
            {"tau": r["tau"], "kappa_max": r["kappa_max"], "condition_number": r["condition_number"]}
            for r in alone
        ],
        "smallest_kappa_max_at_registered_tau_that_flips_the_verdict": min(
            (r["kappa_max"] for r in grid
             if abs(r["tau"] - TAU) < 1e-15 and r["verdict"] == "INSEPARABLE"),
            default=None,
        ),
        "largest_kappa_max_at_registered_tau_still_INSEPARABLE": max(
            (r["kappa_max"] for r in grid
             if abs(r["tau"] - TAU) < 1e-15 and r["verdict"] == "INSEPARABLE"),
            default=None,
        ),
        "grid": grid,
    }


def check_kappa_algebra(block: dict[str, Any]) -> list[str]:
    """Every grid row must agree with the algebra in :func:`kappa_branch_exploration`.

    Returns the list of disagreements; empty means the production rule and the closed-form
    prediction coincide. This is a check that CAN fail: feeding it a grid computed with the
    rank rule stated on ``sigma_1`` instead of ``sigma_K``, or with the ceiling comparison
    inverted, produces disagreements at once. ``tests/test_k6_spectrum.py`` does exactly that.
    """
    bad: list[str] = []
    kappa = block["measured_condition_number"]
    for r in block["grid"]:
        if not r["rank_determined"]:
            continue  # the closed form assumes every singular value resolved
        predicted_rank = kappa > 1.0 / r["tau"]
        predicted_kappa = kappa > r["kappa_max"]
        predicted_alone = predicted_kappa and not predicted_rank
        if bool(r["rank_branch_fires"]) != bool(predicted_rank):
            bad.append(f"rank branch at tau={r['tau']:g}: got {r['rank_branch_fires']}, "
                       f"predicted {predicted_rank}")
        if bool(r["kappa_branch_fires"]) != bool(predicted_kappa):
            bad.append(f"kappa branch at kappa_max={r['kappa_max']:g}: "
                       f"got {r['kappa_branch_fires']}, predicted {predicted_kappa}")
        if bool(r["kappa_branch_fires_alone"]) != bool(predicted_alone):
            bad.append(f"kappa-alone at (tau={r['tau']:g}, kappa_max={r['kappa_max']:g}): "
                       f"got {r['kappa_branch_fires_alone']}, predicted {predicted_alone}")
    return bad


# --------------------------------------------------------------------------------------
# Reproduction self-check
# --------------------------------------------------------------------------------------

def reproduction_check(name: str, family_set: str, sv: Sequence[float]) -> dict[str, Any]:
    """Does this run reproduce the singular values already on record for the same settings?

    Same seed, same replicate count, same h sweep, same normalisation -- so the three-column
    spectra computed here must match the recorded ones to floating-point. If they do not, the
    parallel estimator or the assembly is wrong and no six-column number from this file is
    trustworthy. Under what condition does this read false? Any change to the estimator, the
    seeding, the summary maps or the column ordering.
    """
    path = (REPO / "results" / f"jacobian_rank.{name}.yaml") if family_set == "base" else (
        OUT / f"jacobian_rank.adversarial.{name}.yaml")
    if not path.exists():
        return {"reference_file": str(path), "available": False,
                "note": "no recorded run at these settings to compare against"}
    rec = yaml.safe_load(path.read_text(encoding="utf-8"))
    ref = [float(x) for x in rec["results"]["singular_values_at_representative_h"]]
    got = [float(x) for x in sv]
    rel = [
        (abs(a - b) / b if b > 0 else (0.0 if a == 0 else math.inf))
        for a, b in zip(got, ref)
    ]
    return {
        "reference_file": str(path.relative_to(REPO)),
        "available": True,
        "recorded_singular_values": ref,
        "recomputed_singular_values": got,
        "max_relative_difference": float(max(rel)) if rel else 0.0,
        "reproduces": bool(max(rel) < 1e-12) if rel else True,
    }


def triple_columns(code: str) -> list[tuple[str, int]]:
    """The (family set, component) column keys for a mixed triple such as ``"BAB"``."""
    if len(code) != K or any(c not in "BA" for c in code):
        raise ValueError(f"bad triple code {code!r}")
    return [("base" if c == "B" else "adversarial", k) for k, c in enumerate(code)]


def triple_label(code: str) -> str:
    return " + ".join(f"{'base' if c == 'B' else 'adv'}:{COMPONENTS[k]}"
                      for k, c in enumerate(code))


# --------------------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="K = 6 spectrum check (session G5, Phase 1)")
    ap.add_argument("--seed", type=int, default=20260820)
    ap.add_argument("--replicates", type=int, default=128)
    ap.add_argument("--norm-replicates", type=int, default=2000)
    ap.add_argument("--workers", type=int, default=max(1, min(4, (os.cpu_count() or 2) - 2)))
    args = ap.parse_args(argv)

    command = "python -m src.diagnostics.k6_spectrum " + " ".join(
        f"--{k.replace('_', '-')} {v}" for k, v in vars(args).items()
    )
    started = now_iso()
    seed_norm = args.seed + 900_000

    # S3: refuse to start if another instance is already writing this file. The check asks the
    # kernel about one recorded PID rather than grepping a process listing -- see src/runlock.py
    # for the three ways the pattern-matching version reports a live run as dead, which is what
    # session G4 hit. The pidfile lives OUTSIDE the repository so that having a run in flight
    # does not itself dirty the tree.
    out_path = OUT / "k6_spectrum.yaml"
    lock = Path(tempfile.gettempdir()) / "sim-attrib-runs" / "k6_spectrum.json"
    prior = check_pidfile(lock)
    if prior["alive"]:
        raise SystemExit(
            f"REFUSING TO START: pid {prior['pid']} is already running "
            f"{prior['command']!r} and will write {prior.get('outputs')}. "
            f"Standing constraint S3. Kill it deliberately or wait."
        )
    write_pidfile(lock, module="src.diagnostics.k6_spectrum",
                  outputs=[str(out_path.relative_to(REPO))])
    print(f"pidfile {lock} (pid {os.getpid()})", flush=True)

    print(f"prior-predictive sd (R_norm={args.norm_replicates}, seed0={seed_norm}) ...", flush=True)
    stats = prior_predictive_stats(SUMMARY_SETS, n_replicates=args.norm_replicates, seed0=seed_norm)
    sd_map = {n: sd for n, (_m, sd) in stats.items()}

    # The normalisation is estimated at eta = 0, where BOTH family sets are the identity, so it
    # cannot depend on which set is selected -- which is exactly why the six columns can be put
    # side by side at all. Asserted rather than assumed.
    adv_stats = prior_predictive_stats(SUMMARY_SETS, n_replicates=8, seed0=seed_norm,
                                       params=with_params(families="adversarial"))
    base_stats = prior_predictive_stats(SUMMARY_SETS, n_replicates=8, seed0=seed_norm)
    for n in SUMMARY_SETS:
        if not np.array_equal(adv_stats[n][1], base_stats[n][1]):
            raise AssertionError(
                f"prior-predictive sd for {n} differs between family sets at eta = 0; the two "
                f"family sets are then NOT the identity at zero and the six columns do not live "
                f"in one space"
            )

    print(f"columns: {len(FAMILY_SETS)} family sets x {len(H_VALUES)} h x {K} components, "
          f"R={args.replicates}, workers={args.workers}", flush=True)
    cols = estimate_columns(h_values=H_VALUES, n_replicates=args.replicates,
                            seed0=args.seed, workers=args.workers)
    n_sims = 2 * len(H_VALUES) * K * args.replicates * 2

    doc: dict[str, Any] = {
        "provenance": header(script="src/diagnostics/k6_spectrum.py", command=command,
                             seed=args.seed, started=started),
        "what_this_is": (
            "Session G5, Phase 1. The K = 6 spectrum run through the SAME machinery the K = 3 "
            "verdict was run through -- the pre-registered h sweep, the plateau rule, the "
            "resolution criterion, the equivalence-class rule and the permutation leakage "
            "check. results/robustness/wide_spectrum_check.yaml measured the six-column "
            "spectrum at ONE step size, which docs/THRESHOLDS.md §1.4 says is not a result. "
            "Nothing in results/ is modified. See audit/K6_SPECTRUM_CHECK.md."
        ),
        "why_there_is_only_one_six_column_object": (
            "A family set declares three one-parameter families and therefore supplies three "
            "columns. The only six-column Jacobian available from the two declared sets is the "
            "union of their columns, and that union is the same matrix whichever set you start "
            "from -- so 'the six-column spectrum under the base families' and 'under the "
            "adversarial families' are not two objects. Inventing three further families now, "
            "with the results known, would be DEVIATIONS.md D-9's problem at twice the size. "
            "Recorded as DEVIATIONS.md D-12."
        ),
        "what_a_six_column_verdict_does_and_does_not_bear_on": (
            "The six columns are two distortions of each of the same three mechanisms. A "
            "near-null direction supported on one mechanism's two columns says two deformations "
            "of the SAME component are hard to tell apart, which component attribution never "
            "claimed to do. A near-null direction mixing mechanisms is the failure the K = 3 "
            "verdict rules out. Every near-null direction below is classified, by the "
            "pre-registered vk_min rule and by a threshold-free mechanism-energy figure."
        ),
        "settings": {
            "seed": args.seed, "R": args.replicates, "R_norm": args.norm_replicates,
            "seed0_normalisation": seed_norm, "h_values": list(H_VALUES),
            "eta_scale": ETA_SCALE, "workers": args.workers,
            "n_simulator_runs": n_sims,
        },
        "thresholds_pre_registered": {
            "source": "docs/THRESHOLDS.md, unchanged",
            "tau": TAU, "kappa_max": KAPPA_MAX, "colnorm_invisible": COLNORM_INVISIBLE,
            "coherence_flag": COHERENCE_FLAG, "vk_min": VK_MIN,
            "resolve_factor": RESOLVE_FACTOR, "plateau_rel_tol": PLATEAU_REL_TOL,
        },
        "six_column_labels": list(SIX_COLUMN_LABELS),
        "summary_sets": {},
    }

    for name in SUMMARY_SETS:
        sd = sd_map[name]
        blocks: dict[str, Any] = {
            "d": int(len(sd)),
            "coordinate_labels": list(SUMMARY_LABELS[name]),
        }
        sweeps: dict[str, JacobianSweep] = {}
        for family_set in FAMILY_SETS:
            per_h = [[cols[(family_set, hi, k)][name] for k in range(K)]
                     for hi in range(len(H_VALUES))]
            sweeps[family_set] = _sweep(name, per_h, sd, h_values=H_VALUES,
                                        n_replicates=args.replicates, seed0=args.seed,
                                        n_simulations=n_sims // 2)
        per_h6 = [[cols[(fs, hi, k)][name] for fs in FAMILY_SETS for k in range(K)]
                  for hi in range(len(H_VALUES))]
        sweeps["six_columns"] = _sweep(name, per_h6, sd, h_values=H_VALUES,
                                       n_replicates=args.replicates, seed0=args.seed,
                                       n_simulations=n_sims)

        # The eight component-wise family assignments. BBB and AAA are the two declared sets
        # and are recomputed here from the same columns, so their agreement with the 'base'
        # and 'adversarial' blocks above is a check on the assembly rather than a repetition.
        triples: dict[str, Any] = {}
        for code in TRIPLES:
            keys = triple_columns(code)
            per_h_t = [[cols[(fs, hi, k)][name] for fs, k in keys]
                       for hi in range(len(H_VALUES))]
            sw = _sweep(name, per_h_t, sd, h_values=H_VALUES, n_replicates=args.replicates,
                        seed0=args.seed, n_simulations=n_sims // 2)
            a_t = analyse(sw)
            triples[code] = {
                "code": code,
                "families": triple_label(code),
                "is_a_declared_family_set": code in ("BBB", "AAA"),
                "spectrum": describe_spectrum(a_t["singular_values_at_representative_h"], TAU),
                "resolved": a_t["resolved"],
                "singular_value_variation_factor": a_t["singular_value_variation_factor"],
                "plateau_found": a_t["plateau"]["found"],
                "numerical_rank": a_t["numerical_rank"],
                "condition_number": a_t["condition_number"],
                "column_norms": a_t["column_norms"],
                "invisible_components": a_t["invisible_components"],
                "coherence_flagged_pairs": a_t["coherence_flagged_pairs"],
                "near_null_directions": a_t["near_null_directions"],
                "equivalence_classes": [
                    [COMPONENTS[j] for j in nn["equivalence_class_members"]]
                    for nn in a_t["near_null_directions"]
                ],
                "verdict": "INSEPARABLE" if a_t["inseparable"] else "separable",
                "reason": a_t["inseparable_reason"],
                "tau_sensitivity": tau_sensitivity(sw),
                "leakage_check_passes": leakage_check(sw)["passes"],
            }
        blocks["mixed_triples"] = triples
        blocks["mixed_triples_note"] = (
            "Eight component-wise assignments of a family to each component, built ENTIRELY "
            "from the two declared family sets -- a re-combination, not an extension. BBB is "
            "the base set and AAA the adversarial one; the other six are three-column "
            "distortion models an analyst could equally have declared."
        )
        blocks["raw_columns_normalised"] = {
            f"{fs}:{COMPONENTS[k]}": {
                "h_values": list(H_VALUES),
                "columns_by_h": [[float(x) for x in (cols[(fs, hi, k)][name] / sd)]
                                 for hi in range(len(H_VALUES))],
            }
            for fs in FAMILY_SETS for k in range(K)
        }

        for key, sweep in sweeps.items():
            a = analyse(sweep)
            sv = a["singular_values_at_representative_h"]
            blk: dict[str, Any] = {
                "n_columns": int(a["dimensions"]["K"]),
                "spectrum": describe_spectrum(sv, TAU),
                "plateau": a["plateau"],
                "singular_value_range_across_plateau": a["singular_value_range_across_plateau"],
                "singular_value_variation_factor": a["singular_value_variation_factor"],
                "resolved": a["resolved"],
                "numerical_rank": a["numerical_rank"],
                "condition_number": a["condition_number"],
                "column_norms": a["column_norms"],
                "invisible_components": a["invisible_components"],
                "coherence_flagged_pairs": a["coherence_flagged_pairs"],
                "pairwise_coherence": a["pairwise_coherence"],
                "near_null_directions": a["near_null_directions"],
                "inseparable": a["inseparable"],
                "verdict": "INSEPARABLE" if a["inseparable"] else "separable",
                "reason": a["inseparable_reason"],
                "tau_sensitivity": tau_sensitivity(sweep),
                "kappa_branch": kappa_branch_exploration(sweep),
                "leakage_check": leakage_check(sweep),
            }
            disagreements = check_kappa_algebra(blk["kappa_branch"])
            blk["kappa_branch"]["algebra_agrees_with_production_rule"] = not disagreements
            blk["kappa_branch"]["algebra_disagreements"] = disagreements
            if key == "six_columns":
                blk["near_null_classification"] = [
                    classify_near_null(d) for d in a["near_null_directions"]
                ]
                blk["column_labels"] = list(SIX_COLUMN_LABELS)
            else:
                blk["column_labels"] = [f"{key}:{c}" for c in COMPONENTS]
                blk["reproduction_check"] = reproduction_check(name, key, sv)
            blocks[key] = blk

        doc["summary_sets"][name] = blocks
        b3 = blocks["base"]
        a3 = blocks["adversarial"]
        s6 = blocks["six_columns"]
        print(f"\n{name} (d={blocks['d']}):", flush=True)
        print(f"  base K=3:  {['%.4g' % x for x in b3['spectrum']['singular_values']]} "
              f"-> {b3['verdict']} (kappa {b3['condition_number']:.4g})", flush=True)
        print(f"  adv  K=3:  {['%.4g' % x for x in a3['spectrum']['singular_values']]} "
              f"-> {a3['verdict']} (kappa {a3['condition_number']:.4g})", flush=True)
        print(f"  union K=6: {['%.4g' % x for x in s6['spectrum']['singular_values']]} "
              f"-> {s6['verdict']} (kappa {s6['condition_number']:.4g}, "
              f"spread {s6['spectrum']['spread_decades_over_positive_singular_values']})",
              flush=True)
        print("  mixed triples (B = base family, A = adversarial family, per component):",
              flush=True)
        for code, blk in blocks["mixed_triples"].items():
            print(f"    {code} {'*' if blk['is_a_declared_family_set'] else ' '} "
                  f"rank {blk['numerical_rank']['rank_certain']}/{K} "
                  f"kappa {blk['condition_number']:.4g} -> {blk['verdict']}"
                  + (f"   class {blk['equivalence_classes']}" if blk['equivalence_classes'] else ""),
                  flush=True)
        for cl in s6.get("near_null_classification", []):
            print(f"    near-null: {cl['kind']} {cl['mechanisms_in_class']} "
                  f"energy {({k: round(v, 3) for k, v in cl['mechanism_energy'].items()})}",
                  flush=True)

    OUT.mkdir(parents=True, exist_ok=True)
    path = out_path
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, width=100)
    print(f"\nwrote {path.relative_to(REPO)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
