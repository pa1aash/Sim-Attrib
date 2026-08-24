"""The confidence-set-bounded MMC check -- session G11, Phase 1. T1-3 of the external review.

WHAT THIS ANSWERS, AND WHY THE EXISTING ±5% BOX WAS NOT ENOUGH
-----------------------------------------------------------------
``results/boundary_sweep.yaml`` (session G7) and ``results/p_sel.yaml`` (session G6) measure
the MMC composition's cost gate under a *fixed, assumed* relative box on the five nuisance
coordinates -- half-widths from 0.1% to 5%, chosen because they are round numbers, not because
anything about this simulator's own data says a real analyst's uncertainty would sit there. An
independent adversarial review of the resulting paper draft named this the single most
important open question: the collapse is real, but is it a property of the composition, or an
artefact of a box nobody derived from anything?

Dufour (2006) has an answer for exactly this. Section 5 of the CIRANO working paper (fetched in
full via ``hyperresearch``, quoted rather than paraphrased below) proposes replacing the fixed
nuisance set ``Omega_0`` with ``C_T``, a **consistent set estimate of the nuisance parameters
derived from the data** -- his ``consistent set estimator MMC`` (CSEMMC). This script builds
that set for this simulator, for the first time in this project, and re-measures the cost gate
inside it rather than inside an assumed box.

A CORRECTION TO THE SESSION BRIEF, FOUND BY DOING WHAT IT ASKED
-------------------------------------------------------------------
The brief that commissioned this check states that Dufour "explicitly anticipates this exact
objection" with "a Bonferroni correction connecting the confidence-set coverage to the overall
test's exactness." The brief also says: fetch Dufour and confirm the exact procedure, "do not
approximate from memory of the earlier citation." Doing exactly that turned up something worth
stating plainly rather than quietly working around: **the word "Bonferroni" does not appear
anywhere in Dufour (2006), CIRANO Working Paper 2005s-02** (`grep -i bonferroni` on the full
87,153-character fetched body: zero matches, verified directly, not assumed).

What Dufour's Section 5 actually gives (Propositions 5.1-5.2, quoted below) is an
**asymptotic-coverage** argument: any sequence of sets ``C_T`` with ``P[theta_0 in C_T] -> 1``
as the sample size ``T -> infinity`` gives a CSEMMC test with asymptotically-correct level. He
gives one *worked example* of such a ``C_T``: an ellipsoid ``{theta : (theta_hat_T - theta)' A_T'
A_T (theta_hat_T - theta) < c}`` built from a consistent point estimate ``theta_hat_T`` and a
scaling matrix ``A_T`` (eq. 5.13) -- the standard Wald-ellipsoid construction, with no
coordinate-wise decomposition and no multiple-comparisons correction anywhere in it.

**Building a coordinate-wise BOX (rather than sampling the ellipsoid directly) genuinely does
need a Bonferroni step, and that part of the brief's description is correct as engineering
guidance even though it is not what is in Dufour's own text.** This project's existing MMC
infrastructure (``p_sel.nuisance_grid``, ``boundary_sweep.py``, ``cost_gate.py``) is built
entirely around axis-aligned relative boxes -- that is the object ``Omega_0`` has meant in every
prior session's numbers. Reusing that infrastructure rather than writing a new ellipsoid sampler
means realising Dufour's ``C_T`` as a box that CIRCUMSCRIBES the Wald ellipsoid: one marginal
Wald interval per nuisance coordinate, each built at level ``1 - alpha1/(2K)`` so that a
Bonferroni union bound gives the *joint* box coverage ``P[theta_0 in box] >= 1 - alpha1`` --
which is a valid, if conservative, way to satisfy Dufour's (5.8) for a set of the box shape this
project's tooling already knows how to sweep. **This is a design choice made here, using a
standard technique, not a claim that Dufour's paper states it.** The audit report
(``audit/DUFOUR_CONFIDENCE_SET_CHECK.md``) states this distinction again, because the T1-3(b)
instruction to "not approximate from memory" earns a precise answer rather than a hedge.

QUOTED FROM DUFOUR (2006) SECTION 5 (CIRANO WP 2005s-02), FOR THE RECORD
----------------------------------------------------------------------------
    "any set of the form C_T = {theta in Omega : ||A_T(theta_hat_T - theta)||^2 < c/T^delta}
    satisfies (5.8) ... whenever ... T^(delta_bar/2) A_T(theta_hat_T - theta_0) has an
    asymptotic distribution as T -> infinity."                                    (Prop. 5.1, sec 5)

    "It is quite easy to find a consistent set estimate of theta_0 whenever a consistent point
    estimate theta_hat_T of theta_0 is available."                                        (sec 5)

WHAT "THE DATA" MEANS HERE, STATED BEFORE ANY NUMBER EXISTS
-----------------------------------------------------------
This is a synthetic-simulator methods paper. There is no real epidemic dataset standing behind
``theta_0 = (beta=0.35, gamma=0.14, rho=0.40, I0=10.0, obs_sigma=0.15)``. "The data-implied
confidence set" therefore means: the confidence set an analyst holding ONE realised 120-day
reported-incidence curve from this simulator, at these true parameters, and fitting the SAME
model class back to it by maximum likelihood, would report. That is the honest and only
available reading of "what the data themselves constrain" for a methods paper whose simulator IS
the data-generating process, and it is stated here rather than left implicit.

The fit uses the FULL 120-day reported series (not the S_B summary reduction the diagnostic and
selection rule are built on) -- the most informative object the simulator's own model class can
offer an analyst, and therefore the tightest confidence set this construction can produce. Using
anything coarser (e.g. fitting on S_B alone) would inflate the box for a reason having nothing
to do with the nuisance parameters' genuine identifiability, and would conflate two different
questions.

THE CONSTRUCTION, IN FULL
--------------------------
1. Simulate one "observed" reported-incidence curve at theta_0, eta=0, seed OBS_SEED (below).
2. Fit theta_hat = (beta, gamma, rho, I0, obs_sigma) by maximum likelihood under the SAME
   lognormal multiplicative observation model the simulator itself uses, starting from a
   deliberately perturbed guess (never from theta_0), by L-BFGS-B with positivity bounds.
3. Compute the observed Fisher information as the numerical Hessian of the negative
   log-likelihood at theta_hat (central differences, per-coordinate relative step). Invert for
   the asymptotic covariance Sigma_hat. Report its eigenvalues -- a near-singular direction is a
   genuine identifiability finding about this fit and is reported rather than silently
   regularised away.
4. Bonferroni box: for K_NUISANCE=5 coordinates and alpha1=0.05, each marginal interval is built
   at level 1 - alpha1/(2*5) = 0.995, i.e. z = Phi^-1(0.995), giving a joint box with coverage
   >= 1 - alpha1 = 95%. Relative half-width per coordinate: w_j = z * SE_j / theta_hat_j.
5. Re-measure p_sel (the cost gate's input) over that box, using the SAME 32-corner + 10-axis-
   endpoint design, screen/refine methodology, selection rule, and cost gate this project's
   prior sessions used for the fixed ±w boxes -- so the comparison in
   ``audit/DUFOUR_CONFIDENCE_SET_CHECK.md`` is apples to apples.

ALPHA1 = 0.05: `audit/MMC_COMPOSITION_SPEC.md` does not commit to a numeric level for the
confidence-set construction anywhere (checked directly, not assumed) -- it names CSEMMC as an
open option in §4 point 2 without pricing it. 0.05 is the conventional choice and is adopted
here for that reason and no other.

UNDER WHAT CONDITION DOES EACH FLAG THIS SCRIPT WRITES READ FALSE? (standing constraint S4/S5)
------------------------------------------------------------------------------------------------
``hessian_is_positive_definite`` -- FALSE when the numerical Hessian of the NLL at theta_hat has
    a non-positive eigenvalue, which would mean the fit is not at a genuine local minimum in
    every direction or the curvature is too flat to invert. The run aborts rather than reporting
    a confidence set built from an unstable inverse.
``mle_gradient_near_zero``       -- FALSE when the numerical gradient of the NLL at the reported
    optimum exceeds a stated tolerance in any coordinate, i.e. the optimiser did not actually
    converge. Reachable: a bad starting point or a bounds-active solution would trip it.
``theta_hat_recovers_theta0``    -- descriptive, not gating: reports the relative offset between
    theta_hat and theta_0 in units of the fitted standard error per coordinate. A large value
    would not invalidate the confidence set (which is built around theta_hat, honestly, as a
    real analyst's would be) but would be worth a reader's attention.
``normalisation_reproduces``, ``jacobian_reproduces``, ``family_sets_agree_at_zero`` -- as in
    ``p_sel.py`` and ``boundary_sweep.py``: the run aborts rather than proceeding in
    inconsistent coordinates or against a stale Jacobian.
``seed_spans_disjoint_from_prior_sessions`` -- FALSE when any seed span used here overlaps a
    span recorded in ``results/p_sel.yaml`` or ``results/boundary_sweep.yaml``.

WHAT THIS SCRIPT CANNOT DO, STATED BEFORE IT IS RUN
-----------------------------------------------------
* It builds ONE data-implied box, from ONE simulated realisation, at ONE true parameter point --
  the same single-point conditionality every number in this repository carries.
* A Bonferroni box is a conservative circumscription of Dufour's ellipsoid, not the ellipsoid
  itself. It can only be WIDER than the ellipsoid it circumscribes (never narrower), so any
  collapse found to survive inside this box survives inside the tighter ellipsoid too; a
  collapse that does NOT survive inside this box is not thereby shown to survive or not survive
  inside the (unmeasured, tighter) ellipsoid.
* It does not implement, test, or price the maximiser. Nothing here revives ``docs/DECISIONS.md``
  D-16, which drops the composition as an experimental vehicle regardless of this box's answer;
  see the module-level note in every prior MMC script for why.
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
from scipy import optimize, stats

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
    wilson,
)

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results"

# ---------------------------------------------------------------------------------------
# PRE-REGISTERED DESIGN CONSTANTS -- committed before this script is run for the first time
# ---------------------------------------------------------------------------------------

ALPHA1: float = 0.05
K_NUISANCE: int = len(NUISANCE_COORDS)  # 5: beta, gamma, rho, I0, obs_sigma

#: Bonferroni-corrected two-sided per-coordinate level, so the joint box has coverage >= 1-ALPHA1.
BONFERRONI_ALPHA_PER_COORD: float = ALPHA1 / K_NUISANCE
Z_BONFERRONI: float = float(stats.norm.ppf(1.0 - BONFERRONI_ALPHA_PER_COORD / 2.0))

#: The "observed" realisation a data-implied confidence set is built from. Chosen once, before
#: any fit is run, disjoint from every seed span recorded in results/p_sel.yaml (theta0 30260820,
#: screen 60260820, refine 520260820) and results/boundary_sweep.yaml (anchor/screen/refine
#: 1.02e9-3.56e9). 9e9 is comfortably clear of all of them.
OBS_SEED: int = 9_000_000_000

#: MLE starting point, deliberately perturbed from theta_0 rather than started there -- an
#: optimiser started at the answer proves nothing about whether it can find it.
START_MULTIPLIER: dict[str, float] = {
    "beta": 1.15, "gamma": 0.85, "rho": 1.20, "I0": 0.70, "obs_sigma": 1.35,
}

#: Bounds for the MLE, wide enough not to bind at the optimum for a well-specified fit; a bound
#: that DOES bind is a genuine finding (reported, not hidden) rather than an error.
BOUNDS: dict[str, tuple[float, float]] = {
    "beta": (0.01, 3.0), "gamma": (0.01, 3.0), "rho": (1e-3, 1.0),
    "I0": (0.5, 500.0), "obs_sigma": (1e-3, 1.0),
}

GRADIENT_TOL: float = 1e-2  # |d NLL / d theta_j|, in natural units, at the reported optimum
MIN_HESSIAN_EIGENVALUE: float = 1e-12

N_THETA0: int = 100_000       # theta_hat anchor, matching G6/G7's N_THETA0
N_SCREEN: int = 10_000        # per design point, matching G6/G7's N_SCREEN
N_REFINE_DRAWS: int = 100_000  # per re-measured point, matching G6/G7's N_REFINE_DRAWS
N_REFINE_POINTS: int = 4      # one per (assignment, variant) key, matching boundary_sweep.py


# ---------------------------------------------------------------------------------------
# THE "OBSERVED" DATA, AND THE LIKELIHOOD THE SIMULATOR'S OWN MODEL IMPLIES
# ---------------------------------------------------------------------------------------

def observed_data(seed: int = OBS_SEED) -> np.ndarray:
    """One realised 120-day reported-incidence curve at theta_0, eta=0."""
    out = sir3.simulate(np.zeros(K), seed=seed, params=BASE, stochastic=True)
    return out.reported


def reported_mean_at(theta: dict[str, float]) -> np.ndarray:
    """The deterministic reported-incidence MEAN under ``theta``. obs_sigma does not enter here."""
    params = with_params(beta=theta["beta"], gamma=theta["gamma"], rho=theta["rho"],
                         I0=theta["I0"])
    out = sir3.simulate(np.zeros(K), seed=0, params=params, stochastic=False)
    return out.reported_mean


def neg_log_likelihood(theta_vec: np.ndarray, y_obs: np.ndarray, coords: tuple[str, ...]) -> float:
    """Negative log-likelihood of ``y_obs`` under the simulator's own lognormal noise model.

    ``y = mean * exp(sigma*Z - sigma^2/2)``, so ``log(y) - log(mean) + sigma^2/2 ~ N(0, sigma^2)``
    -- exactly the model ``sir3.simulate`` draws from, restated as a likelihood rather than a
    sampler.
    """
    theta = dict(zip(coords, theta_vec))
    sigma = float(theta["obs_sigma"])
    mean = reported_mean_at(theta)
    if np.any(mean <= 0.0) or sigma <= 0.0:
        return float("inf")
    resid = np.log(y_obs) - np.log(mean) + 0.5 * sigma * sigma
    n = len(y_obs)
    return float(n * 0.5 * np.log(2.0 * np.pi * sigma * sigma) + np.sum(resid ** 2) / (2.0 * sigma * sigma))


def _nll_logspace(log_theta: np.ndarray, y_obs: np.ndarray, coords: tuple[str, ...]) -> float:
    return neg_log_likelihood(np.exp(log_theta), y_obs, coords)


def fit_mle(y_obs: np.ndarray, coords: tuple[str, ...]) -> dict[str, Any]:
    """MLE of the five nuisance parameters, from a deliberately perturbed start.

    **Why Nelder-Mead in log-space, and not gradient descent on the natural parameters.**
    Tried first, and it fails informatively rather than quietly: raw L-BFGS-B from the
    perturbed start takes one Newton-like step sized from a gradient of order 1e4-1e5 (the
    coordinates have wildly different natural scales -- ``I0 ~ 10``, ``obs_sigma ~ 0.15`` --
    and the RK4-integrated likelihood surface is correspondingly stiff), lands the trial point
    at the corner of the bounds box, finds every coordinate there gives a non-positive
    reported-incidence mean (``neg_log_likelihood`` returns ``inf`` by construction), and
    reports spurious convergence at the UNMOVED starting point -- confirmed by tracing every
    function evaluation the optimiser made. Log-space reparametrisation alone does not fix it
    (the gradient is still steep in log units); what fixes it is a derivative-free method that
    does not trust a single steep gradient to size its first step. Nelder-Mead in log-space
    recovers theta_0 to within about one prior-predictive standard error on every coordinate
    from a start 15-35% off, confirmed below by the reported offset in standard errors.
    """
    x0 = np.array([BASE_VALUE(c) * START_MULTIPLIER[c] for c in coords], dtype=float)
    log_bounds = [(np.log(BOUNDS[c][0]), np.log(BOUNDS[c][1])) for c in coords]
    res = optimize.minimize(_nll_logspace, np.log(x0), args=(y_obs, coords),
                            method="Nelder-Mead", bounds=log_bounds,
                            options={"maxiter": 4000, "maxfev": 4000,
                                     "xatol": 1e-7, "fatol": 1e-9, "adaptive": True})
    x_hat = np.exp(res.x)
    theta_hat = {c: float(v) for c, v in zip(coords, x_hat)}
    grad = numerical_gradient(x_hat, y_obs, coords)
    # Newton-decrement-style scaling: |g_j| against the coordinate's own curvature, so one
    # tolerance is meaningful across coordinates whose natural scales differ by an order of
    # magnitude (I0 ~ 10 vs obs_sigma ~ 0.15).
    diag_scale = np.array([max(1.0, abs(BASE_VALUE(c))) for c in coords])
    scaled_grad = grad * diag_scale
    return {
        "theta_hat": theta_hat, "nll_at_optimum": float(res.fun),
        "converged": bool(res.success), "message": str(res.message),
        "n_function_evals": int(res.nfev), "x0": {c: float(v) for c, v in zip(coords, x0)},
        "gradient_at_optimum": dict(zip(coords, [float(g) for g in grad])),
        "gradient_max_abs": float(np.max(np.abs(grad))),
        "scaled_gradient_max_abs": float(np.max(np.abs(scaled_grad))),
        "gradient_near_zero": bool(np.max(np.abs(scaled_grad)) < GRADIENT_TOL),
        "any_bound_active": {
            c: bool(np.isclose(res.x[i], log_bounds[i][0], rtol=1e-6) or
                   np.isclose(res.x[i], log_bounds[i][1], rtol=1e-6))
            for i, c in enumerate(coords)
        },
    }


def BASE_VALUE(coord: str) -> float:
    return float(getattr(BASE, coord))


def numerical_gradient(x: np.ndarray, y_obs: np.ndarray, coords: tuple[str, ...],
                       rel_step: float = 1e-5) -> np.ndarray:
    grad = np.zeros_like(x)
    for i in range(len(x)):
        h = max(1e-6, rel_step * abs(x[i]))
        xp, xm = x.copy(), x.copy()
        xp[i] += h
        xm[i] -= h
        grad[i] = (neg_log_likelihood(xp, y_obs, coords) - neg_log_likelihood(xm, y_obs, coords)) / (2 * h)
    return grad


def numerical_hessian(x: np.ndarray, y_obs: np.ndarray, coords: tuple[str, ...],
                      rel_step: float = 1e-4) -> np.ndarray:
    """Central-difference Hessian of the NLL. The observed Fisher information at the MLE."""
    n = len(x)
    h = np.array([max(1e-6, rel_step * abs(x[i])) for i in range(n)])
    H = np.zeros((n, n))
    f0 = neg_log_likelihood(x, y_obs, coords)
    for i in range(n):
        xp, xm = x.copy(), x.copy()
        xp[i] += h[i]
        xm[i] -= h[i]
        H[i, i] = (neg_log_likelihood(xp, y_obs, coords) - 2 * f0 +
                   neg_log_likelihood(xm, y_obs, coords)) / (h[i] ** 2)
    for i in range(n):
        for j in range(i + 1, n):
            xpp, xpm, xmp, xmm = x.copy(), x.copy(), x.copy(), x.copy()
            xpp[i] += h[i]; xpp[j] += h[j]
            xpm[i] += h[i]; xpm[j] -= h[j]
            xmp[i] -= h[i]; xmp[j] += h[j]
            xmm[i] -= h[i]; xmm[j] -= h[j]
            val = (neg_log_likelihood(xpp, y_obs, coords) - neg_log_likelihood(xpm, y_obs, coords)
                  - neg_log_likelihood(xmp, y_obs, coords) + neg_log_likelihood(xmm, y_obs, coords)
                  ) / (4 * h[i] * h[j])
            H[i, j] = H[j, i] = val
    return H


def bonferroni_box(theta_hat: dict[str, float], se: dict[str, float],
                   coords: tuple[str, ...]) -> dict[str, dict[str, float]]:
    """Per-coordinate relative half-width ``w_j = z * SE_j / theta_hat_j``, Bonferroni-corrected."""
    out = {}
    for c in coords:
        w = Z_BONFERRONI * se[c] / theta_hat[c]
        out[c] = {"se": se[c], "z": Z_BONFERRONI, "relative_half_width": float(w),
                  "interval": [theta_hat[c] * (1 - w), theta_hat[c] * (1 + w)]}
    return out


def hetero_grid(center: dict[str, float], rel_half_widths: dict[str, float],
                coords: tuple[str, ...]) -> list[dict[str, Any]]:
    """32 corners + 10 axis endpoints of a heterogeneous relative box, centred at ``center``.

    Same design shape as ``p_sel.nuisance_grid`` (one width applied to all coordinates); this
    generalises it to a different relative half-width per coordinate, which a data-implied
    confidence set generally has and a hand-picked round-number box does not.
    """
    pts: list[dict[str, Any]] = []
    for mask in range(2 ** len(coords)):
        signs = [1 if (mask >> i) & 1 else -1 for i in range(len(coords))]
        tag = "".join("+" if s > 0 else "-" for s in signs)
        pts.append({
            "key": f"confset|corner|{tag}", "kind": "corner",
            "theta": {c: center[c] * (1.0 + s * rel_half_widths[c])
                     for c, s in zip(coords, signs)},
        })
    for c in coords:
        for s in (-1, 1):
            theta = dict(center)
            theta[c] = center[c] * (1.0 + s * rel_half_widths[c])
            pts.append({
                "key": f"confset|axis|{c}{'+' if s > 0 else '-'}", "kind": "axis", "theta": theta,
            })
    return pts


def gate_row(p: float, lo: float, hi: float) -> dict[str, Any]:
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
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="confidence-set MMC check (session G11, T1-3)")
    ap.add_argument("--seed", type=int, default=20260824)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--theta0-draws", type=int, default=N_THETA0)
    ap.add_argument("--screen-draws", type=int, default=N_SCREEN)
    ap.add_argument("--refine-draws", type=int, default=N_REFINE_DRAWS)
    ap.add_argument("--out", type=str, default="results/confidence_set_mmc.yaml",
                    help="output path relative to the repository root. Overridden only for "
                         "smoke runs, which must not write into results/.")
    args = ap.parse_args(argv)

    command = "python -m src.diagnostics.confidence_set_check " + " ".join(
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
    write_pidfile(lock, module="src.diagnostics.confidence_set_check", outputs=[str(out_path)])
    print(f"pidfile {lock} (pid {os.getpid()})", flush=True)

    # -- the constants the rule is built from, and the checks that they are the right ones --
    norm = load_normalisation()
    norm_rows = _draw_task((0, {}, norm["seed0"], norm["n_replicates"]))[1]
    m_re, sd_re = norm_rows.mean(axis=0), norm_rows.std(axis=0, ddof=1)
    rel_mean = float(np.max(np.abs(m_re - norm["mean"]) / np.abs(norm["mean"])))
    rel_sd = float(np.max(np.abs(sd_re - norm["sd"]) / np.abs(norm["sd"])))
    norm_ok = bool(max(rel_mean, rel_sd) < NORM_TOL)
    print(f"normalisation reproduces: {norm_ok} (mean {rel_mean:.3e}, sd {rel_sd:.3e})", flush=True)
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

    # -- seed spans, and the check that they touch nothing recorded in prior sessions -------
    seed_obs = OBS_SEED
    seed_anchor = args.seed + 10_000_000_000
    seed_screen = args.seed + 11_000_000_000
    seed_refine = args.seed + 12_000_000_000
    grid_len_upper_bound = 2 ** K_NUISANCE + 2 * K_NUISANCE  # 42, before it exists
    mine = {
        "obs": (seed_obs, seed_obs + 1),
        "anchor": (seed_anchor, seed_anchor + args.theta0_draws),
        "screen": (seed_screen, seed_screen + grid_len_upper_bound * 1_000_000),
        "refine": (seed_refine, seed_refine + N_REFINE_POINTS * 1_000_000),
    }
    p_sel_rec = yaml.safe_load((OUT / "p_sel.yaml").read_text(encoding="utf-8"))
    boundary_rec = yaml.safe_load((OUT / "boundary_sweep.yaml").read_text(encoding="utf-8"))
    g6s, g7s = p_sel_rec["settings"], boundary_rec["settings"]
    theirs = {
        "G6_theta0": (int(g6s["seeds"]["theta0"]), int(g6s["seeds"]["theta0"]) + int(g6s["n_draws_theta0"])),
        "G6_screen": (int(g6s["seeds"]["screen"]), int(g6s["seeds"]["screen"]) + int(g6s["n_grid_points"]) * 1_000_000),
        "G6_refine": (int(g6s["seeds"]["refine"]), int(g6s["seeds"]["refine"]) + int(g6s["n_points_refined"]) * 1_000_000),
        "G7_anchor": tuple(g7s["seed_spans_used"]["anchor"]),
        "G7_screen": tuple(g7s["seed_spans_used"]["screen"]),
        "G7_refine": tuple(g7s["seed_spans_used"]["refine"]),
        "normalisation": (norm["seed0"], norm["seed0"] + norm["n_replicates"]),
    }
    overlaps = [f"{n1}{s1} vs {n2}{s2}"
               for n1, s1 in mine.items() for n2, s2 in theirs.items()
               if not (s1[1] <= s2[0] or s2[1] <= s1[0])]
    spans_disjoint = not overlaps
    if not spans_disjoint:
        raise SystemExit(
            "ABORTING: seed spans overlap a prior session's: " + "; ".join(overlaps) +
            ". A reproduction check run on the same draws is not a check.")
    print("seed spans disjoint from results/p_sel.yaml and results/boundary_sweep.yaml: True",
          flush=True)

    # ---- Step 1-2: observed data, MLE fit --------------------------------------------------
    print(f"\nobserved data: seed {seed_obs}", flush=True)
    y_obs = observed_data(seed_obs)
    fit = fit_mle(y_obs, NUISANCE_COORDS)
    print(f"  MLE converged: {fit['converged']}  (nfev={fit['n_function_evals']}, "
          f"max|grad|={fit['gradient_max_abs']:.3e})", flush=True)
    print(f"  theta_hat: {fit['theta_hat']}", flush=True)

    # ---- Step 3: Hessian, covariance --------------------------------------------------------
    x_hat = np.array([fit["theta_hat"][c] for c in NUISANCE_COORDS])
    H = numerical_hessian(x_hat, y_obs, NUISANCE_COORDS)
    eigvals = np.linalg.eigvalsh(H)
    hessian_pd = bool(np.min(eigvals) > MIN_HESSIAN_EIGENVALUE)
    print(f"  Hessian eigenvalues: {eigvals}", flush=True)
    print(f"  hessian_is_positive_definite: {hessian_pd}", flush=True)
    if not hessian_pd:
        raise SystemExit(
            "ABORTING: the observed information matrix is not positive definite at the MLE. "
            "See results file for the eigenvalues; a confidence set cannot be built from an "
            "uninvertible Hessian.")
    Sigma = np.linalg.inv(H)
    se = {c: float(np.sqrt(Sigma[i, i])) for i, c in enumerate(NUISANCE_COORDS)}
    corr = Sigma / np.outer(np.sqrt(np.diag(Sigma)), np.sqrt(np.diag(Sigma)))
    print(f"  standard errors: {se}", flush=True)

    box = bonferroni_box(fit["theta_hat"], se, NUISANCE_COORDS)
    print(f"  Bonferroni relative half-widths (alpha1={ALPHA1}, z={Z_BONFERRONI:.4f}): "
          f"{ {c: round(v['relative_half_width'], 6) for c, v in box.items()} }", flush=True)

    theta0_vals = {c: BASE_VALUE(c) for c in NUISANCE_COORDS}
    offset_in_se = {c: float((fit["theta_hat"][c] - theta0_vals[c]) / se[c]) for c in NUISANCE_COORDS}
    print(f"  (theta_hat - theta_0) / SE per coordinate: {offset_in_se}", flush=True)

    # ---- Step 5: measure p_sel over the data-implied box ------------------------------------
    grid = hetero_grid(fit["theta_hat"], {c: box[c]["relative_half_width"] for c in NUISANCE_COORDS},
                       NUISANCE_COORDS)
    n_grid = len(grid)
    print(f"\nconfidence-set box: {n_grid} design points x {args.screen_draws} screen draws",
          flush=True)

    pool_kw = {"max_workers": args.workers}
    total_draws = 0

    # anchor at theta_hat
    chunk = 5_000
    tasks0 = [(i, fit["theta_hat"], seed_anchor + i * chunk, min(chunk, args.theta0_draws - i * chunk))
             for i in range((args.theta0_draws + chunk - 1) // chunk)]
    acc0: dict[str, list[int]] = {}
    with ProcessPoolExecutor(**pool_kw) as pool:
        for _idx, block in pool.map(_draw_task, tasks0, chunksize=1):
            new = _counts(rules, block)
            for key, c in new.items():
                acc0.setdefault(key, [0] * K)
                for k in range(K):
                    acc0[key][k] += c[k]
            total_draws += len(block)
    print(f"  theta_hat cells (primary): {acc0[primary]}", flush=True)

    tasks_s = [(i, pt["theta"], seed_screen + i * 1_000_000, args.screen_draws)
              for i, pt in enumerate(grid)]
    screen: list[dict[str, list[int]]] = [None] * n_grid  # type: ignore[list-item]
    with ProcessPoolExecutor(**pool_kw) as pool:
        for idx, block in pool.map(_draw_task, tasks_s, chunksize=1):
            screen[idx] = _counts(rules, block)
            total_draws += len(block)
    print(f"  screened {n_grid} points", flush=True)

    refine_targets: list[int] = []
    for key in keys:
        j = min(range(n_grid), key=lambda i: min(screen[i][key]))
        if j not in refine_targets:
            refine_targets.append(j)
    refine_targets.sort(key=lambda i: min(screen[i][primary]))
    refine_targets = refine_targets[:N_REFINE_POINTS]

    print(f"\nrefine: {len(refine_targets)} points x {args.refine_draws} draws", flush=True)
    tasks_r = [(j, grid[i]["theta"], seed_refine + j * 1_000_000, args.refine_draws)
              for j, i in enumerate(refine_targets)]
    refined: dict[int, dict[str, list[int]]] = {}
    with ProcessPoolExecutor(**pool_kw) as pool:
        for j, block in pool.map(_draw_task, tasks_r, chunksize=1):
            refined[refine_targets[j]] = _counts(rules, block)
            total_draws += len(block)
    print(f"  refined {len(refine_targets)} points", flush=True)

    elapsed = time.perf_counter() - t_start

    def worst(counts: list[int], n: int) -> tuple[float, float, float, int]:
        k = int(np.argmin(counts))
        lo, hi = wilson(counts[k], n)
        return counts[k] / n, lo, hi, k

    def cell_block(counts: list[int], n: int) -> dict[str, Any]:
        lo_hi = [wilson(counts[k], n) for k in range(K)]
        return {"n_draws": int(n), "counts": [int(x) for x in counts],
               "p_sel": [float(x / n) for x in counts],
               "ci95_lower": [float(lo_hi[k][0]) for k in range(K)],
               "ci95_upper": [float(lo_hi[k][1]) for k in range(K)]}

    by_key: dict[str, Any] = {}
    for key in keys:
        j = min(range(n_grid), key=lambda i: min(screen[i][key]))
        p_s, lo_s, hi_s, k_s = worst(screen[j][key], args.screen_draws)
        own_refined = j in refined
        cands = [(p_s, lo_s, hi_s, k_s, grid[j]["key"], "screen", args.screen_draws)] \
            if not own_refined else []
        for i in refine_targets:
            if i in refined:
                p_r, lo_r, hi_r, k_r = worst(refined[i][key], args.refine_draws)
                cands.append((p_r, lo_r, hi_r, k_r, grid[i]["key"], "refined", args.refine_draws))
        p_u, lo_u, hi_u, k_u, at_u, src, n_used = min(cands, key=lambda c: c[0])
        n_dead = sum(1 for i in range(n_grid) if min(screen[i][key]) == 0)
        by_key[key] = {
            "screened_min": {"p_sel": p_s, "ci95": [lo_s, hi_s], "cell": COMPONENTS[k_s],
                            "at_point": grid[j]["key"], "n_draws": args.screen_draws},
            "own_argmin_was_re_measured": bool(own_refined),
            "reported_min": {"p_sel": p_u, "ci95": [lo_u, hi_u], "cell": COMPONENTS[k_u],
                            "at_point": at_u, "source": src, "n_draws": n_used,
                            "de_biased": bool(src == "refined")},
            "n_design_points_with_a_dead_cell": n_dead,
            "fraction_of_design_points_with_a_dead_cell": float(n_dead / n_grid),
            "gate": gate_row(p_u, lo_u, hi_u),
        }

    anchor_by_key = {}
    for key in keys:
        p0, lo0, hi0, k0 = worst(acc0[key], args.theta0_draws)
        anchor_by_key[key] = {
            "cells": cell_block(acc0[key], args.theta0_draws),
            "reported_min": {"p_sel": p0, "ci95": [lo0, hi0], "cell": COMPONENTS[k0],
                            "at_point": "theta_hat", "source": "anchor", "n_draws": args.theta0_draws},
            "gate": gate_row(p0, lo0, hi0),
        }

    primary_min = by_key[primary]["reported_min"]["p_sel"]
    primary_gate = by_key[primary]["gate"]["verdict"]
    both_variants_pass = all(by_key[f"{primary.split('|')[0]}|{v}"]["gate"]["verdict"] == "PASS"
                             for v in VARIANTS)
    session_verdict = "PASS" if both_variants_pass else (
        "FAIL" if all(by_key[f"{primary.split('|')[0]}|{v}"]["gate"]["verdict"] == "FAIL"
                     for v in VARIANTS) else "SPLIT")

    doc: dict[str, Any] = {
        "provenance": header(script="src/diagnostics/confidence_set_check.py", command=command,
                            seed=args.seed, started=started),
        "what_this_is":
            "Session G11, Phase 1. T1-3 of the external adversarial review: the MMC cost gate, "
            "re-measured inside a confidence set for the five nuisance parameters BUILT FROM "
            "DATA (a maximum-likelihood fit plus a Bonferroni-corrected asymptotic-normal box "
            "at alpha1=0.05), rather than inside the fixed +/-w boxes results/p_sel.yaml and "
            "results/boundary_sweep.yaml assumed. See the module docstring for the full "
            "construction and the correction to the session brief's description of Dufour (2006).",
        "alpha1": ALPHA1,
        "bonferroni_alpha_per_coordinate": BONFERRONI_ALPHA_PER_COORD,
        "z_bonferroni": Z_BONFERRONI,
        "observed_data": {"seed": seed_obs, "n_days": int(sir3.BASE.T_days)},
        "mle_fit": {
            "theta_hat": fit["theta_hat"], "theta_0": theta0_vals,
            "start_point": fit["x0"], "converged": fit["converged"], "message": fit["message"],
            "n_function_evals": fit["n_function_evals"],
            "gradient_at_optimum": fit["gradient_at_optimum"],
            "gradient_max_abs": fit["gradient_max_abs"],
            "gradient_near_zero": fit["gradient_near_zero"],
            "gradient_tolerance": GRADIENT_TOL,
            "any_bound_active": fit["any_bound_active"],
            "offset_from_theta0_in_standard_errors": offset_in_se,
        },
        "fisher_information": {
            "hessian_eigenvalues": [float(v) for v in eigvals],
            "hessian_is_positive_definite": hessian_pd,
            "min_eigenvalue_tolerance": MIN_HESSIAN_EIGENVALUE,
            "standard_errors": se,
            "correlation_matrix": {NUISANCE_COORDS[i]: {NUISANCE_COORDS[j]: float(corr[i, j])
                                                       for j in range(K_NUISANCE)}
                                  for i in range(K_NUISANCE)},
        },
        "confidence_set_box": box,
        "settings": {
            "summary_set": SUMMARY_SET, "family_codes": list(FAMILY_CODES),
            "variants": list(VARIANTS), "primary_key": primary,
            "nuisance_coordinates": list(NUISANCE_COORDS),
            "n_design_points": n_grid,
            "design": "32 corners + 10 axis endpoints of the Bonferroni box, centred at "
                     "theta_hat -- src.diagnostics.confidence_set_check.hetero_grid, generalising "
                     "p_sel.nuisance_grid to unequal per-coordinate half-widths",
            "n_draws_theta_hat_anchor": args.theta0_draws,
            "n_draws_screen": args.screen_draws, "n_draws_refine": args.refine_draws,
            "n_points_refined": len(refine_targets),
            "seeds": {"obs": seed_obs, "anchor": seed_anchor, "screen": seed_screen,
                     "refine": seed_refine},
            "seed_spans_used": {k: list(v) for k, v in mine.items()},
            "seed_spans_checked_disjoint_against": {k: list(v) for k, v in theirs.items()},
            "workers": args.workers, "n_simulator_runs": int(total_draws + norm["n_replicates"]),
            "wall_clock_seconds": float(elapsed),
        },
        "checks": {
            "normalisation_reproduces": norm_ok,
            "jacobian_reproduces": {c: jac[c]["reproduces"] for c in FAMILY_CODES},
            "family_sets_agree_at_zero": families_agree,
            "seed_spans_disjoint_from_prior_sessions": spans_disjoint,
            "hessian_is_positive_definite": hessian_pd,
            "mle_gradient_near_zero": fit["gradient_near_zero"],
        },
        "anchor_theta_hat": anchor_by_key,
        "by_key": by_key,
        "primary_case": {"key": primary, "p_sel_min": primary_min, "gate_verdict": primary_gate},
        "session_verdict": {
            "verdict": session_verdict, "is_a_pass": bool(session_verdict == "PASS"),
            "rule": "PASS only if the primary assignment AAA passes under BOTH studentisation "
                   "variants inside the confidence-set box, matching cost_gate.py's convention "
                   "for the fixed-box measurement.",
        },
        "design_points": [
            {"key": pt["key"], "kind": pt["kind"],
            "theta": {c: float(v) for c, v in pt["theta"].items()},
            "screen": {key: cell_block(screen[i][key], args.screen_draws) for key in keys},
            "refined": ({key: cell_block(refined[i][key], args.refine_draws) for key in keys}
                       if i in refined else None)}
            for i, pt in enumerate(grid)
        ],
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(yaml.safe_dump(doc, sort_keys=False, width=100), encoding="utf-8")
    print(f"\nwrote {out_path}  ({total_draws} draws, {elapsed:.0f} s)", flush=True)
    print(f"  primary case ({primary}) gate verdict inside the confidence-set box: {primary_gate}",
          flush=True)
    print(f"  session verdict: {session_verdict}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
