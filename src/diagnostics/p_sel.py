"""Direct Monte Carlo measurement of ``p_sel`` -- session G6, Phase 1.

WHAT IS BEING MEASURED, QUOTED RATHER THAN RESTATED
----------------------------------------------------
``audit/MMC_COMPOSITION_SPEC.md`` §4, verbatim::

    p_sel(theta) = P(k-hat(y) = k | theta, eta = 0) = probability a null draw lands in the
    observed selection cell

and, on which value of it the cost depends (§4, point 1)::

    p_sel is worst-case, not average-case. The cost is governed by min over theta of
    p_sel(theta) across the searched set, not by its value at a plausible theta. A nuisance
    value that makes the observed selection unlikely is exactly the one the maximiser is
    drawn toward, because that is where the p-value is largest.

``k-hat`` is supplied by ``src/attribution/selection.py``, which had to be written because
the specification defers ``T_k`` (§6) and ``p_sel`` is a property of the cell ``T_k``
defines. ``DEVIATIONS.md`` **D-14**.

EVERYTHING BELOW IS PRE-REGISTERED: it is committed before this script is run for the first
time, in the same way ``src/diagnostics/k6_spectrum.py`` was committed at ``a8159f8`` before
it produced a number, and for the same reason.

THE DESIGN, AND WHY EACH NUMBER IN IT IS THE SIZE IT IS
-------------------------------------------------------
**What a draw costs, and why the counts below are as large as they are.** ``p_sel`` is a
property of the null, so every draw this script takes has ``eta = 0``. At ``eta = 0`` and a
fixed ``theta`` the simulator's entire deterministic core -- the RK4 integration, the delay
convolution, the reporting-fraction multiplier -- produces the same array for every seed, and
the seed enters only through the observation noise. :func:`null_summaries` therefore performs
that core ONCE per nuisance point and applies the noise ``n`` times, which is **bit-identical
to calling ``simulate`` ``n`` times** and is asserted to be in ``tests/test_p_sel.py``. The
marginal cost of a draw falls from a Python RK4 loop to a vector of normals, so the counts
here are set by the precision the gate needs rather than by what the machine can afford.

**Stage A -- ``theta_0``, the base specification.** ``N_THETA0`` draws. This is the cost the
composition would pay if the nuisance parameters were KNOWN, which they are not; it is
reported as the floor and never as the headline. Sizing: the cost gate's decision boundaries
in ``p_sel`` are ``M*N/1e8`` for each declared ``(M, N)``, i.e. from ``9.9e-4`` to ``9.99e-2``
(see ``src/diagnostics/cost_gate.py``). At ``N_THETA0 = 100000`` a proportion near ``1/3``
carries a standard error of ``0.0015``, so a 95% interval is ``+/-0.003`` -- far inside the
gap between boundaries. **The requirement is stated as a flag, not as an intention:**
``ci_decides_the_gate`` reads FALSE if the gate verdict differs at the two ends of the
interval, and the run reports it either way.

**Stage B1 -- the nuisance box, screened.** ``Omega_0`` is a relative box around ``theta_0``
on the five nuisance coordinates the specification names in §1 (``beta``, ``gamma``, ``rho``,
``I0``, and the observation-noise scale). Four nested half-widths are measured,
``BOX_HALF_WIDTHS``, so that the reader sees the cost as a function of how wide the nuisance
set is rather than one number resting on one arbitrary box. **The headline box is
``HEADLINE_BOX``, declared here before any number exists.** Each box contributes its 32
corners and its 10 axis endpoints: a box's minimum over a smooth response is attained at an
extreme point, and corners are where two coordinates conspire.

**Stage B2 -- the minimum, re-measured on independent draws.** The smallest of 168 noisy
estimates is biased low, which would overstate the cost. The ``N_REFINE_POINTS`` lowest points
are re-drawn with fresh seeds at ``N_REFINE_DRAWS`` each, and the refined value is the one
that enters the gate. Re-measuring a selected extremum with independent draws is the
de-biasing, not a second look at the same one. At ``N_REFINE_DRAWS = 100000`` a point with no
acceptances at all carries a 95% upper bound of ``3e-5``, which is decisive against every
declared ``(M, N)`` corner rather than only the expensive ones.

**Every stage draws under ``eta = 0`` and under ``families="base"``**, because the two family
sets are bit-identical at ``eta = 0`` -- asserted at run time, not assumed. So one set of
draws serves both family assignments: only the SELECTION RULE differs between ``AAA`` and
``BBB``, not the data. ``BBB`` therefore costs nothing extra to measure.

WHAT THIS MEASUREMENT CANNOT DO, STATED BEFORE IT IS RUN
---------------------------------------------------------
* **A grid understates the minimum.** ``min`` over 42 points of a box is an upper bound on
  ``min`` over the box, so the cost computed from it is a LOWER bound on the cost a
  continuous derivative-free maximiser would pay. A PASS is therefore weaker than it looks
  and a FAIL is stronger.
* **It says nothing about power.** ``p_sel`` is a property of the null. Whether the selection
  rule attributes correctly under an alternative is a different measurement and is not taken
  here.
* **It is one simulator, one summary set, one base parameter point.** The same limitation
  every Jacobian in this repository carries.
* **It does not implement, test, or price the maximiser.** ``M`` is taken from the
  specification's own table and is not measured. Nothing here is the composition.

UNDER WHAT CONDITION DOES EACH FLAG THIS SCRIPT WRITES READ FALSE? (S4)
------------------------------------------------------------------------
``normalisation_reproduces``  -- FALSE when the prior-predictive mean and sd recomputed here
    from the recorded settings differ from the values recorded in
    ``results/jacobian_rank.S_B.yaml`` by more than ``NORM_TOL`` relatively. Reachable: a
    different NumPy or a changed seed would trip it, and the run aborts rather than
    proceeding in inconsistent coordinates.
``jacobian_reproduces``       -- FALSE when the spectrum of the Jacobian rebuilt from
    ``results/robustness/k6_spectrum.yaml`` disagrees with the singular values that file
    records for the same triple. Reachable: picking the wrong step size trips it, which is
    how the representative ``h`` is identified here rather than assumed.
``family_sets_agree_at_zero`` -- FALSE when the base and adversarial branches of the
    simulator produce different output at ``eta = 0``, which would mean the two family
    assignments do not share one set of null draws.
``z_is_centred_at_theta0``    -- FALSE when the mean of the normalised discrepancy at
    ``theta_0`` is further than ``Z_CENTRED_TOL`` standard errors from zero in any
    coordinate. Reachable: it is exactly what would happen if ``m0`` were taken from a
    different parameter point than the draws.
``ties_are_negligible``       -- FALSE when any exact tie in the top two ``T_k`` is observed.
    Dufour's Proposition 4.1 assumes ties have probability zero (§2.2); this is that
    assumption measured rather than asserted.
``rule_inverts_its_jacobian``  -- FALSE when ``max |J^+ J - I|`` exceeds ``1e-9``. This is
    the flag that actually tests the RULE, and it is separated deliberately from the
    attribution sanity check below. An earlier version of this script used "does the rule
    name the planted component at the smallest magnitude" as the flag, and it read FALSE for
    a reason having nothing to do with the rule: the reference point ``m0`` is a 2000-
    replicate estimate, so it carries Monte Carlo error of order ``1/sqrt(2000) = 0.022``
    normalised summary units, which lands as an offset of roughly ``0.005`` to ``0.014``
    normalised units in ``eta-hat`` **before any distortion is planted at all**. A flag that
    reads FALSE for a reason other than the one it names is ``DEVIATIONS.md`` D-8's failure
    mode, and it is recorded here rather than quietly fixed. The offset itself is measured
    and reported as ``reference_point_offset``, because it is a floor on what the selection
    rule can attribute and G7 needs to know it exists.
"""

from __future__ import annotations

import argparse
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
from ..simulators.summaries import SUMMARY_SETS
from .jacobian_rank import KAPPA_MAX, TAU
from .k6_spectrum import triple_columns, triple_label

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results"

# ---------------------------------------------------------------------------------------
# PRE-REGISTERED DESIGN CONSTANTS -- committed before the first run
# ---------------------------------------------------------------------------------------

#: The summary set. `audit/MMC_COMPOSITION_SPEC.md` §5 nominates S_B and G4's correction
#: block removes S_A as the alternative. Not a choice made here.
SUMMARY_SET = "S_B"

#: Component-wise family assignments. AAA is the primary case -- the worst validated
#: assignment of G5's eight-assignment sweep, at kappa = 64.62. BBB is the contrast.
FAMILY_CODES: tuple[str, ...] = ("AAA", "BBB")

#: The nuisance coordinates, named in `audit/MMC_COMPOSITION_SPEC.md` §1 and not chosen here.
NUISANCE_COORDS: tuple[str, ...] = ("beta", "gamma", "rho", "I0", "obs_sigma")

#: Nested relative half-widths of the nuisance box Omega_0.
BOX_HALF_WIDTHS: tuple[float, ...] = (0.05, 0.10, 0.20, 0.50)

#: The box whose minimum is the headline. Declared before any p_sel exists.
HEADLINE_BOX: float = 0.20

N_THETA0: int = 100_000       # stage A draws
N_SCREEN: int = 10_000        # stage B1 draws per theta point
N_REFINE_DRAWS: int = 100_000  # stage B2 draws per re-measured point
N_REFINE_POINTS: int = 20     # how many points are re-measured
N_LOWEST_PER_CELL: int = 4    # per (assignment, variant, cell), before dedup and the cap
N_GAUSS: int = 200_000        # linearised cross-check sample (no simulator calls)

#: Planted-distortion magnitudes for the attribution sanity check, in NORMALISED units
#: (one unit = ETA_SCALE = a 10% relative deformation of the component).
ETA_MULTIPLIERS: tuple[float, ...] = (0.01, 0.05, 0.1, 0.25, 0.5, 1.0)

NORM_TOL: float = 1e-3        # abort above this relative disagreement in the normalisation
Z_CENTRED_TOL: float = 6.0    # standard errors, for the z-is-centred flag


def nuisance_grid(widths: tuple[float, ...]) -> list[dict[str, Any]]:
    """The deterministic design: per width, 32 corners and 10 axis endpoints."""
    base = {c: float(getattr(BASE, c)) for c in NUISANCE_COORDS}
    pts: list[dict[str, Any]] = []
    for w in widths:
        for mask in range(2 ** len(NUISANCE_COORDS)):
            signs = [1 if (mask >> i) & 1 else -1 for i in range(len(NUISANCE_COORDS))]
            tag = "".join("+" if s > 0 else "-" for s in signs)
            pts.append({
                "key": f"w{w:g}|corner|{tag}", "width": float(w), "kind": "corner",
                "theta": {c: base[c] * (1.0 + s * w) for c, s in zip(NUISANCE_COORDS, signs)},
            })
        for c in NUISANCE_COORDS:
            for s in (-1, 1):
                theta = dict(base)
                theta[c] = base[c] * (1.0 + s * w)
                pts.append({
                    "key": f"w{w:g}|axis|{c}{'+' if s > 0 else '-'}", "width": float(w),
                    "kind": "axis", "theta": theta,
                })
    return pts


def null_summaries(theta: dict[str, float], seed0: int, n: int) -> np.ndarray:
    """``n`` null draws at one ``theta``, as an ``(n, d)`` block of summary vectors.

    **Bit-identical to calling ``simulate(eta=0, seed=seed0+r, params)`` ``n`` times**, and
    ``tests/test_p_sel.py::test_null_summaries_are_bit_identical_to_calling_simulate``
    requires it to be, at several ``theta`` and several seeds. It is written this way because
    the identity makes the measurement affordable by three orders of magnitude:

    ``simulate`` is a deterministic RK4 integration followed by a delay convolution, a
    reporting-fraction multiplier and a noise layer. **At ``eta = 0`` and fixed ``theta``,
    everything before the noise layer is the same array for every seed** -- the seed enters
    only through ``rng.standard_normal(T_days)``. So the 11,520 Python-level RHS evaluations
    that dominate a run are performed ONCE per nuisance point rather than once per draw.

    This is memoisation of an identity, not an approximation, and it is the reason a
    hundred thousand draws per point is affordable where a thousand would not have been. It
    is valid ONLY at ``eta = 0``, which is exactly where ``p_sel`` is defined; the attribution
    sanity check, which needs ``eta != 0``, calls ``simulate`` directly.
    """
    params = with_params(**theta)
    fn = SUMMARY_SETS[SUMMARY_SET]
    core = sir3.simulate(np.zeros(K), seed=seed0, params=params, stochastic=False)
    mean = core.reported_mean
    s = float(params.obs_sigma)
    rows: list[np.ndarray] = []
    for r in range(n):
        z = np.random.default_rng(seed0 + r).standard_normal(params.T_days)
        rep = mean * np.exp(s * z - 0.5 * s * s)
        rows.append(fn(sir3.SimOutput(days=core.days, true_incidence=core.true_incidence,
                                      reported_mean=mean, reported=rep)))
    return np.asarray(rows, dtype=float)


def _draw_task(task: tuple[int, dict[str, float], int, int]) -> tuple[int, np.ndarray]:
    """:func:`null_summaries` as a pool task. ``families="base"`` throughout, because the two
    family sets are the identity at ``eta = 0`` -- checked in :func:`main`, not assumed."""
    idx, theta, seed0, n = task
    return idx, null_summaries(theta, seed0, n)


def _counts(rules: dict[tuple[str, str], Any], block: np.ndarray) -> dict[str, list[int]]:
    """Selection-cell counts for every (family assignment, variant) rule on one block."""
    out: dict[str, list[int]] = {}
    for (fc, variant), rule in rules.items():
        sel = rule.select_many(block)
        out[f"{fc}|{variant}"] = [int(np.sum(sel == k)) for k in range(K)]
    return out


def _merge(acc: dict[str, list[int]], new: dict[str, list[int]]) -> None:
    for key, counts in new.items():
        if key not in acc:
            acc[key] = [0] * K
        for k in range(K):
            acc[key][k] += counts[k]


def wilson(x: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    """Wilson score interval. Correct at the boundary, where the normal interval is not.

    The boundaries are pinned exactly rather than left to floating point: at ``x = 0`` the
    lower limit is analytically zero, and a residue of order ``1e-19`` there would turn "no
    acceptances at all" into a finite cost bound by arithmetic accident. Zero acceptances is
    the case ``audit/MMC_COMPOSITION_SPEC.md`` §3.4 singles out, and it should read as
    exactly what it is.
    """
    if n == 0:
        return 0.0, 1.0
    p = x / n
    denom = 1.0 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    lo = 0.0 if x == 0 else float(max(0.0, centre - half))
    hi = 1.0 if x == n else float(min(1.0, centre + half))
    return lo, hi


def load_normalisation() -> dict[str, Any]:
    """Prior-predictive mean and sd, and the settings that produced them, from the record."""
    rec = yaml.safe_load((OUT / f"jacobian_rank.{SUMMARY_SET}.yaml").read_text(encoding="utf-8"))
    norm = rec["normalisation"]["summaries"]
    return {
        "source": f"results/jacobian_rank.{SUMMARY_SET}.yaml",
        "n_replicates": int(norm["n_replicates_R_norm"]),
        "seed0": int(norm["seed0"]),
        "mean": np.asarray(norm["prior_predictive_mean"], dtype=float),
        "sd": np.asarray(norm["prior_predictive_sd"], dtype=float),
        "labels": list(norm["coordinate_labels"]),
    }


def load_jacobian(code: str) -> dict[str, Any]:
    """The normalised Jacobian for one family assignment, from G5's recorded columns.

    The representative step size is not assumed: it is IDENTIFIED as the step whose spectrum
    reproduces the singular values the same file records for this triple, and the achieved
    agreement is returned so a reader can see the check that was made.
    """
    rec = yaml.safe_load((OUT / "robustness" / "k6_spectrum.yaml").read_text(encoding="utf-8"))
    block = rec["summary_sets"][SUMMARY_SET]
    cols = block["raw_columns_normalised"]
    hs = cols["base:transmission"]["h_values"]
    want = np.asarray(block["mixed_triples"][code]["spectrum"]["singular_values"], dtype=float)
    keys = [f"{fs}:{COMPONENTS[k]}" for fs, k in triple_columns(code)]
    best, best_rel, best_J = None, float("inf"), None
    for hi, h in enumerate(hs):
        J = np.column_stack([np.asarray(cols[key]["columns_by_h"][hi], dtype=float) for key in keys])
        sv = np.linalg.svd(J, compute_uv=False)
        rel = float(np.max(np.abs(sv - want) / np.abs(want)))
        if rel < best_rel:
            best, best_rel, best_J = hi, rel, J
    return {
        "source": "results/robustness/k6_spectrum.yaml",
        "code": code, "families": triple_label(code),
        "representative_h": float(hs[best]), "representative_h_index": int(best),
        "max_relative_difference_to_recorded_spectrum": best_rel,
        "reproduces": bool(best_rel < 1e-10),
        "columns": keys, "J": best_J,
        "recorded_condition_number": float(block["mixed_triples"][code]["condition_number"]),
    }


def attribution_sanity(rules: dict[tuple[str, str], Any], norm: dict[str, Any]) -> dict[str, Any]:
    """Does the rule name the component that was actually distorted? Noiseless, no noise draws.

    **This is a power check, not a validity check, and the difference matters.** ``p_sel`` is
    a property of the null and is unaffected by anything here: the selection event is a fixed
    function of the data whether or not the linearisation behind it is any good. What this
    measures is whether the cell the data lands in is the RIGHT one -- which is what the
    composition would eventually be used to make a statement about.

    Three quantities, and only the first is a pass/fail flag:

    * ``rule_inverts_its_jacobian`` -- ``max |J^+ J - I|``. The rule is the pseudo-inverse of
      the Jacobian and this is the property that makes it "sensitive to eta_k and insensitive
      to eta_j" (specification §6). A FALSE here means the rule is wrong.
    * ``reference_point_offset`` -- ``eta-hat`` evaluated on NOISELESS undistorted output.
      Ideally zero. It is not, because the reference ``m0`` is an average over ``R_norm``
      replicates and therefore carries Monte Carlo error of order ``1/sqrt(R_norm)`` per
      normalised coordinate. **This is a floor on what the rule can attribute**, it is a
      property of the recorded normalisation rather than of the simulator, and G7 can lower
      it only by re-estimating ``m0`` with more replicates.
    * the recovery table -- which component is named at six planted magnitudes. Descriptive.
      The Jacobian is a derivative at ``eta = 0`` estimated at a step of ``1e-4`` normalised
      units; whether ``J^+`` still recovers a distortion three or four orders of magnitude
      further out is an empirical question about the simulator, not something the
      construction guarantees.

    Costs ``len(FAMILY_CODES) * (K * len(ETA_MULTIPLIERS) + 1)`` deterministic simulator runs.
    """
    fn = SUMMARY_SETS[SUMMARY_SET]
    inverts = {}
    offset = {}
    for (code, variant), rule in rules.items():
        inverts[f"{code}|{variant}"] = float(
            np.max(np.abs(rule.Jplus @ rule.J - np.eye(rule.K))))
    for code in FAMILY_CODES:
        fam = "base" if code == "BBB" else "adversarial"
        s0 = fn(sir3.simulate(np.zeros(K), seed=1, params=with_params(families=fam),
                              stochastic=False))
        z0 = (s0 - norm["mean"]) / norm["sd"]
        for variant in VARIANTS:
            offset[f"{code}|{variant}"] = {
                "eta_hat_at_zero_distortion": [float(x)
                                               for x in rules[(code, variant)].eta_hat(s0)],
                "norm_of_z_at_zero_distortion": float(np.linalg.norm(z0)),
                "one_over_sqrt_R_norm": float(1.0 / np.sqrt(norm["n_replicates"])),
                "selected_with_no_distortion_planted":
                    COMPONENTS[rules[(code, variant)].select(s0)],
            }
    rows = []
    for code in FAMILY_CODES:
        fam = "base" if code == "BBB" else "adversarial"
        for k in range(K):
            for mult in ETA_MULTIPLIERS:
                eta = np.zeros(K)
                eta[k] = mult * sir3.ETA_SCALE
                s = fn(sir3.simulate(eta, seed=1, params=with_params(families=fam),
                                     stochastic=False))
                row = {"family_code": code, "planted_component": COMPONENTS[k],
                       "eta_normalised_units": float(mult), "selected": {}, "eta_hat": {},
                       "relative_error_of_eta_hat": {}}
                for variant in VARIANTS:
                    rule = rules[(code, variant)]
                    eh = rule.eta_hat(s)
                    want = np.zeros(K)
                    want[k] = mult
                    row["selected"][variant] = COMPONENTS[rule.select(s)]
                    row["eta_hat"][variant] = [float(x) for x in eh]
                    row["relative_error_of_eta_hat"][variant] = float(
                        np.linalg.norm(eh - want) / mult)
                row["correct"] = {v: bool(row["selected"][v] == COMPONENTS[k])
                                  for v in VARIANTS}
                rows.append(row)

    def recovered_at(code: str, variant: str, m: float) -> bool:
        return all(r["correct"][variant] for r in rows
                   if r["family_code"] == code and r["eta_normalised_units"] == m)

    return {
        "what_this_is":
            "Whether the rank-conditioned rule names the component that was actually "
            "distorted, on noiseless data, at six planted magnitudes. A POWER check. It "
            "does not bear on p_sel, which is a property of the null.",
        "rule_inverts_its_jacobian": bool(max(inverts.values()) < 1e-9),
        "max_abs_Jplus_J_minus_identity": inverts,
        "reference_point_offset": offset,
        "why_the_offset_is_not_zero":
            "m0 is the prior-predictive mean over R_norm replicates recorded in "
            "results/jacobian_rank.S_B.yaml, so it carries Monte Carlo error of order "
            "1/sqrt(R_norm) per normalised summary coordinate. That error propagates through "
            "pinv(J) into eta_hat and is a FLOOR on what the selection rule can attribute. It "
            "is a property of the recorded normalisation, not of the simulator, and it is "
            "reported because a planted distortion smaller than this floor cannot be "
            "recovered by any amount of care elsewhere.",
        "magnitudes_at_which_every_component_is_recovered": {
            f"{code}|{variant}": [m for m in ETA_MULTIPLIERS if recovered_at(code, variant, m)]
            for code in FAMILY_CODES for variant in VARIANTS},
        "rows": rows,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="p_sel measurement (session G6, Phase 1)")
    ap.add_argument("--seed", type=int, default=20260820)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--theta0-draws", type=int, default=N_THETA0)
    ap.add_argument("--screen-draws", type=int, default=N_SCREEN)
    ap.add_argument("--refine-draws", type=int, default=N_REFINE_DRAWS)
    ap.add_argument("--out", type=str, default="results/p_sel.yaml",
                    help="output path, relative to the repository root. Overridden only for "
                         "smoke runs, which must not write into results/.")
    args = ap.parse_args(argv)

    command = "python -m src.diagnostics.p_sel " + " ".join(
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
    write_pidfile(lock, module="src.diagnostics.p_sel", outputs=[str(out_path)])
    print(f"pidfile {lock} (pid {os.getpid()})", flush=True)

    # -- the constants the rule is built from, and the checks that they are the right ones --
    norm = load_normalisation()
    print(f"normalisation from {norm['source']} "
          f"(R_norm={norm['n_replicates']}, seed0={norm['seed0']}); recomputing to check ...",
          flush=True)
    norm_rows = null_summaries({}, norm["seed0"], norm["n_replicates"])
    m_re, sd_re = norm_rows.mean(axis=0), norm_rows.std(axis=0, ddof=1)
    rel_mean = float(np.max(np.abs(m_re - norm["mean"]) / np.abs(norm["mean"])))
    rel_sd = float(np.max(np.abs(sd_re - norm["sd"]) / np.abs(norm["sd"])))
    norm_ok = bool(max(rel_mean, rel_sd) < NORM_TOL)
    print(f"  max relative difference: mean {rel_mean:.3e}, sd {rel_sd:.3e} "
          f"-> normalisation_reproduces={norm_ok}", flush=True)
    if not norm_ok:
        raise SystemExit(
            f"ABORTING: the recorded normalisation does not reproduce here "
            f"(mean {rel_mean:.3e}, sd {rel_sd:.3e} against NORM_TOL={NORM_TOL}). The "
            f"selection rule would sit in different coordinates from the Jacobian.")

    # The two family sets must be the identity at eta = 0, or one set of null draws cannot
    # serve both assignments. Checked, not assumed.
    a = sir3.simulate(np.zeros(K), seed=7, params=with_params(families="adversarial"))
    b = sir3.simulate(np.zeros(K), seed=7, params=with_params(families="base"))
    families_agree = bool(np.array_equal(a.reported, b.reported))
    if not families_agree:
        raise SystemExit("ABORTING: the family sets differ at eta = 0; one set of null draws "
                         "cannot serve both assignments.")

    jac = {code: load_jacobian(code) for code in FAMILY_CODES}
    for code, j in jac.items():
        print(f"  J[{code}] at h={j['representative_h']:g}: spectrum agrees to "
              f"{j['max_relative_difference_to_recorded_spectrum']:.3e}", flush=True)
        if not j["reproduces"]:
            raise SystemExit(f"ABORTING: no step size reproduces the recorded spectrum for {code}.")

    rules = {
        (code, variant): build_rule(
            summary_set=SUMMARY_SET, family_code=code, variant=variant,
            m0=norm["mean"], sd=norm["sd"], J=jac[code]["J"],
            component_labels=COMPONENTS, tau=TAU, kappa_max=KAPPA_MAX)
        for code in FAMILY_CODES for variant in VARIANTS
    }

    # -- seeds, disjoint by construction and asserted so ----------------------------------
    seed_a = args.seed + 10_000_000
    seed_b1 = args.seed + 40_000_000
    seed_b2 = args.seed + 500_000_000
    grid = nuisance_grid(BOX_HALF_WIDTHS)
    span_a = (seed_a, seed_a + args.theta0_draws)
    span_b1 = (seed_b1, seed_b1 + len(grid) * 1_000_000)
    span_norm = (norm["seed0"], norm["seed0"] + norm["n_replicates"])
    span_jac = (args.seed, args.seed + 100_000)
    spans = {"theta0": span_a, "screen": span_b1, "normalisation": span_norm, "jacobian": span_jac}
    for n1, s1 in spans.items():
        for n2, s2 in spans.items():
            if n1 < n2 and not (s1[1] <= s2[0] or s2[1] <= s1[0]):
                raise SystemExit(f"ABORTING: seed ranges {n1} and {n2} overlap: {s1} {s2}")

    pool_kw = {"max_workers": args.workers}
    total_draws = 0

    # ---- STAGE A -----------------------------------------------------------------------
    print(f"\nstage A: theta_0, {args.theta0_draws} draws, {args.workers} workers", flush=True)
    chunk = 5_000
    tasks = [(i, {}, seed_a + i * chunk, min(chunk, args.theta0_draws - i * chunk))
             for i in range((args.theta0_draws + chunk - 1) // chunk)]
    acc_a: dict[str, list[int]] = {}
    blocks: list[np.ndarray] = [None] * len(tasks)  # type: ignore[list-item]
    with ProcessPoolExecutor(**pool_kw) as pool:
        for idx, block in pool.map(_draw_task, tasks, chunksize=1):
            blocks[idx] = block
            _merge(acc_a, _counts(rules, block))
            total_draws += len(block)
            print(f"  theta_0 chunk {idx + 1}/{len(tasks)}", flush=True)
    block_a = np.vstack(blocks)
    z_a = (block_a - norm["mean"]) / norm["sd"]
    z_mean = z_a.mean(axis=0)
    z_se = z_a.std(axis=0, ddof=1) / np.sqrt(len(z_a))
    z_centred = bool(np.all(np.abs(z_mean / z_se) < Z_CENTRED_TOL))
    corr = np.corrcoef(z_a, rowvar=False)
    off = float(np.max(np.abs(corr - np.eye(corr.shape[0]))))
    ties = {f"{fc}|{v}": rules[(fc, v)].tie_fraction(block_a) for fc, v in rules}
    ties_negligible = bool(all(t == 0.0 for t in ties.values()))
    print(f"  z centred: {z_centred}; max |off-diagonal correlation|: {off:.4f}; "
          f"ties: {max(ties.values()):.3g}", flush=True)

    # ---- STAGE B1 ----------------------------------------------------------------------
    print(f"\nstage B1: {len(grid)} nuisance points x {args.screen_draws} draws", flush=True)
    tasks_b = [(i, pt["theta"], seed_b1 + i * 1_000_000, args.screen_draws)
               for i, pt in enumerate(grid)]
    screen: list[dict[str, list[int]]] = [None] * len(grid)  # type: ignore[list-item]
    z_means: list[list[float]] = [None] * len(grid)  # type: ignore[list-item]
    with ProcessPoolExecutor(**pool_kw) as pool:
        for idx, block in pool.map(_draw_task, tasks_b, chunksize=1):
            screen[idx] = _counts(rules, block)
            z_means[idx] = [float(x) for x in ((block - norm["mean"]) / norm["sd"]).mean(axis=0)]
            total_draws += len(block)
            print(f"  point {idx + 1}/{len(grid)}  {grid[idx]['key']}", flush=True)

    # ---- STAGE B2: re-measure the lowest points on independent draws --------------------
    lowest: dict[int, float] = {}
    for key in screen[0]:
        for k in range(K):
            order = sorted(range(len(grid)), key=lambda i: screen[i][key][k])
            for i in order[:N_LOWEST_PER_CELL]:
                p = screen[i][key][k] / args.screen_draws
                lowest[i] = min(lowest.get(i, 1.0), p)
    chosen = sorted(lowest, key=lambda i: lowest[i])[:N_REFINE_POINTS]
    print(f"\nstage B2: re-measuring {len(chosen)} points x {args.refine_draws} draws",
          flush=True)
    tasks_r = [(j, grid[i]["theta"], seed_b2 + j * 1_000_000, args.refine_draws)
               for j, i in enumerate(chosen)]
    refined: dict[int, dict[str, list[int]]] = {}
    with ProcessPoolExecutor(**pool_kw) as pool:
        for j, block in pool.map(_draw_task, tasks_r, chunksize=1):
            refined[chosen[j]] = _counts(rules, block)
            total_draws += len(block)
            print(f"  refine {j + 1}/{len(chosen)}  {grid[chosen[j]]['key']}", flush=True)

    # ---- the attribution sanity check: deterministic, no noise draws --------------------
    print("\nattribution sanity check (noiseless, planted distortions) ...", flush=True)
    sanity = attribution_sanity(rules, norm)
    total_draws += len(FAMILY_CODES) * (K * len(ETA_MULTIPLIERS) + 1)
    print(f"  rule_inverts_its_jacobian: {sanity['rule_inverts_its_jacobian']}", flush=True)
    print(f"  magnitudes at which every component is recovered: "
          f"{sanity['magnitudes_at_which_every_component_is_recovered']}", flush=True)

    # ---- the linearised cross-check: no simulator calls ---------------------------------
    rng = np.random.default_rng(args.seed + 999)
    zg = rng.standard_normal((N_GAUSS, len(norm["mean"])))
    gauss = {}
    for (fc, variant), rule in rules.items():
        t = np.abs(zg @ rule.Jplus.T) / rule.scale
        sel = np.argmax(t, axis=1)
        gauss[f"{fc}|{variant}"] = [float(np.mean(sel == k)) for k in range(K)]

    elapsed = time.perf_counter() - t_start

    # ---- assemble ------------------------------------------------------------------------
    def cell_block(counts: dict[str, list[int]], n: int) -> dict[str, Any]:
        out = {}
        for key, c in counts.items():
            lo_hi = [wilson(c[k], n) for k in range(K)]
            out[key] = {
                "n_draws": int(n),
                "counts": [int(x) for x in c],
                "p_sel": [float(x / n) for x in c],
                "ci95_lower": [float(lo_hi[k][0]) for k in range(K)],
                "ci95_upper": [float(lo_hi[k][1]) for k in range(K)],
                "se": [float(np.sqrt((c[k] / n) * (1 - c[k] / n) / n)) for k in range(K)],
            }
        return out

    doc: dict[str, Any] = {
        "provenance": header(script="src/diagnostics/p_sel.py", command=command,
                             seed=args.seed, started=started),
        "what_this_is":
            "Session G6, Phase 1. Direct Monte Carlo measurement of p_sel, the probability "
            "that a draw from the simulator's null lands in the observed selection cell, as "
            "defined in audit/MMC_COMPOSITION_SPEC.md section 4. It measures ONLY that. No "
            "part of the MMC composition is implemented, run, or priced by simulation here: "
            "the maximiser's evaluation count M is taken from the specification's own table "
            "and the cost is assembled in src/diagnostics/cost_gate.py.",
        "scope_assumption_D14":
            "docs/DECISIONS.md D-14 (DECIDED, operator, 2026-08-20): every claim this project "
            "makes about component separability and attribution is scoped to a distortion "
            "model that assigns AT MOST ONE one-parameter distortion family to each "
            "component. Inside that scope S_B separates under all eight declarable family "
            "assignments; outside it, the six-column union is INSEPARABLE at kappa = 628.9 "
            "with a progression-observation confound. The selection rule measured here is a "
            "K = 3 object and is meaningful only under that restriction.",
        "selection_rule": {
            "source": "src/attribution/selection.py",
            "why_it_had_to_be_written":
                "audit/MMC_COMPOSITION_SPEC.md section 6 leaves T_k 'not specified' and "
                "'deferred'. p_sel is a property of the cell T_k defines, so it cannot be "
                "measured until T_k is chosen. DEVIATIONS.md D-14.",
            "definition":
                "z = (s(y) - m0)/sd; eta_hat = pinv(J) z; T_k = |eta_hat_k| / c_k; "
                "k_hat = argmax_k T_k. All of m0, sd, J and c are fixed constants of the base "
                "specification: nothing is estimated from the data the rule is applied to.",
            "variants": {
                "studentised": "c_k = ||pinv(J)[k,:]||, the null standard deviation of "
                               "eta_hat_k when z has identity covariance. PRIMARY.",
                "plain": "c_k = 1. Components compared on the common ETA_SCALE.",
            },
            "studentisation_constants": {
                f"{fc}|{v}": [float(x) for x in rules[(fc, v)].scale] for fc, v in rules},
            "component_labels": list(COMPONENTS),
        },
        "settings": {
            "summary_set": SUMMARY_SET,
            "family_codes": list(FAMILY_CODES),
            "nuisance_coordinates": list(NUISANCE_COORDS),
            "theta_0": {c: float(getattr(BASE, c)) for c in NUISANCE_COORDS},
            "box_half_widths": list(BOX_HALF_WIDTHS),
            "headline_box_half_width": HEADLINE_BOX,
            "n_grid_points": len(grid),
            "n_draws_theta0": args.theta0_draws,
            "n_draws_screen": args.screen_draws,
            "n_draws_refine": args.refine_draws,
            "n_points_refined": len(chosen),
            "seeds": {"theta0": seed_a, "screen": seed_b1, "refine": seed_b2,
                      "disjoint_from_normalisation_and_jacobian_seeds": True},
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
            "jacobian_detail": {c: {kk: vv for kk, vv in jac[c].items() if kk != "J"}
                                for c in FAMILY_CODES},
            "family_sets_agree_at_zero": families_agree,
            "z_is_centred_at_theta0": z_centred,
            "z_mean_over_se_at_theta0": [float(x) for x in (z_mean / z_se)],
            "z_max_abs_off_diagonal_correlation": off,
            "ties_are_negligible": ties_negligible,
            "tie_fraction": {k: float(v) for k, v in ties.items()},
        },
        "attribution_sanity_check": sanity,
        "stage_A_theta0": cell_block(acc_a, args.theta0_draws),
        "linearised_gaussian_prediction": {
            "what_it_is":
                "Cell probabilities under z ~ N(0, I), i.e. under the linearisation the "
                "selection rule is built on, computed from J alone with no simulator calls. "
                "A disagreement with stage A is a statement about the linearisation, not "
                "about the Monte Carlo.",
            "n_gaussian_draws": N_GAUSS,
            "p_sel": gauss,
        },
        "stage_B_nuisance_box": [
            {
                "key": pt["key"], "width": pt["width"], "kind": pt["kind"],
                "theta": {c: float(v) for c, v in pt["theta"].items()},
                "z_mean": z_means[i],
                "screen": cell_block(screen[i], args.screen_draws),
                "refined": (cell_block(refined[i], args.refine_draws) if i in refined else None),
            }
            for i, pt in enumerate(grid)
        ],
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(yaml.safe_dump(doc, sort_keys=False, width=100), encoding="utf-8")
    print(f"\nwrote {out_path}  ({total_draws} draws, {elapsed:.0f} s)", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
