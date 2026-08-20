"""Three-component compartmental SIR simulator with per-component distortion families.

WHAT THIS IS FOR, IN THIS PROJECT'S CURRENT FRAMING
---------------------------------------------------
The project is building toward a *composition* paper: Dufour's maximized Monte Carlo
composed with a selection event, for component-level misspecification attribution. That
composition is only meaningful to run where component attribution is well-posed at all,
i.e. where the summary Jacobian satisfies the rank condition of Kahl et al. (2019).

This simulator, together with `summaries.py` and `src/diagnostics/jacobian_rank.py`,
exists to answer whether it does. The rank diagnostic is **infrastructure that is cited
and used, not a claimed method contribution** -- see `docs/DECISIONS.md` D-6 and
`audit/R2_THREAT_CHECK.md`. The rank-and-condition-number screen is Cintron-Arias, Banks,
Capaldi & Lloyd (2009); finite differencing under simulation noise is More & Wild (2012).
Nothing in this module claims either as new.

THE THREE COMPONENTS (K = 3)
-----------------------------
The decomposition is a modelling commitment, declared here in code as well as in prose:

  1. TRANSMISSION   -- the force-of-infection term, base form  beta * S * I / N
  2. PROGRESSION    -- the removal term,           base form  gamma * I
  3. OBSERVATION    -- reporting fraction, reporting delay, and observation noise

The observation process is included deliberately. It is the component most likely to be
collinear with the other two -- an amplitude error in reporting mimics an amplitude error
in transmission for any summary that scales with case counts -- and that is what makes the
diagnostic informative rather than decorative.

THE DISTORTION FAMILIES, AND WHY EACH HAS THE FORM IT HAS
----------------------------------------------------------
Each component k carries a one-parameter family delta_k(.; eta_k), eta_k in R, with

    delta_k(.; 0) == the base simulator, EXACTLY,

and smooth through zero. "Exactly" is tested numerically in `tests/test_sir3.py` before
anything else runs, and smoothness is tested by finite-differencing the family itself.

A *distortion* is not a parameter error. The point of the project is misspecification --
a component whose functional FORM is wrong -- so two of the three families deform the
functional form rather than rescaling a rate constant. The three are deliberately of
three different qualitative kinds, so that the Jacobian's columns are not similar by
construction:

  eta_1  TRANSMISSION -- saturating incidence.

             beta * S * I / N   ->   beta * S * I / N  *  1 / (1 + eta_1 * (I/N) / p_ref)

         The simplest named structural alternative to mass-action incidence: the force of
         infection saturates as prevalence rises (contact-limited mixing). eta_1 = 0
         recovers mass action identically. p_ref is the base model's peak prevalence
         fraction, a fixed normalisation constant (see `peak_prevalence_fraction`), which
         makes eta_1 = 1 mean "incidence at the peak is halved". This family is a
         PREVALENCE NONLINEARITY: it changes the curve's shape, most strongly near the peak.

  eta_2  PROGRESSION -- log-linear drift in the removal hazard.

             gamma  ->  gamma * exp(eta_2 * (t / T_days - 0.5))

         The base model's constant removal hazard is equivalent to an exponential
         infectious period. The simplest structural alternative that preserves the state
         dimension is a hazard that drifts over the observation window (improving
         treatment, changing case definition). The modulation is MEAN-CENTRED on the
         window -- (t/T - 0.5) integrates to zero -- so that to first order eta_2 is not
         a constant rescaling of gamma. That is deliberate: an uncentred version would
         alias progression onto a pure rate change and would make the diagnostic's answer
         a consequence of the parameterisation rather than of the model. This family is a
         TIMING/TREND distortion.

  eta_3  OBSERVATION -- reporting-fraction multiplier.

             rho  ->  rho * exp(eta_3)

         Deliberately the SIMPLEST of the three, and deliberately a pure amplitude error.
         The diagnostic's sharpest question is whether an amplitude error in the
         observation process can be told apart from a mechanism error, and a pure
         multiplier is the cleanest way to ask it. The reporting delay kernel and the
         observation noise scale are held at base values under this family; a different
         choice of observation distortion (perturbing the delay instead) would produce a
         different third column and possibly a different rank verdict. That is a real
         limitation of the design and it is recorded in the results files, not only here.

NORMALISATION -- and the trap it exists to avoid
-------------------------------------------------
The rank of J is NOT scale-invariant. Rescaling a summary or reparametrising eta_k changes
the singular values and can change the numerical rank. Both normalisations are fixed by
`docs/THRESHOLDS.md` §0, which was written before any singular value existed:

  * summaries are divided by their prior-predictive standard deviation (estimated here by
    `prior_predictive_sd`, from undistorted replicates);
  * each eta_k is divided by a fixed relative perturbation scale, ETA_SCALE, identical
    across k so that one normalised unit means the same fractional deformation for every
    component.

ETA_SCALE = 0.1 -- one normalised unit is a 10% relative deformation of the component.
Each family above is constructed so that eta_k = 1 is an O(1)-in-log deformation of its
component at the base trajectory's peak, so a common scale is meaningful across k. 10% is
small enough that the linearisation is a good approximation of the distortion's effect,
which is the condition under which the Jacobian is the right object at all.

Because ETA_SCALE is COMMON across k, multiplying it by any constant multiplies J by that
constant, hence leaves the normalised singular-value spectrum, the numerical rank at a
relative tolerance, and the condition number all UNCHANGED. Only the column-norm
("invisible component") test of THRESHOLDS §1.5 depends on the absolute value. That
invariance is asserted in `tests/test_jacobian_rank.py`.

THE OBSERVATION NOISE MODEL DETERMINES WHETHER J IS ESTIMABLE AT ALL
---------------------------------------------------------------------
This is a real constraint and not a detail of implementation.

Under common random numbers a stochastic simulator becomes a deterministic function of eta
for a fixed seed, and the finite difference differentiates that function. If the
observation layer is COUNT-VALUED (Poisson, negative binomial), that function is a step
function of eta: the simulated count is an integer that jumps, so the difference quotient
is either exactly 0 or O(1/h), and no derivative exists at any h. There is no plateau to
find, because there is nothing to resolve.

If the observation layer is CONTINUOUS and multiplicative -- here lognormal,
`mean * exp(sigma*Z - sigma^2/2)` with Z frozen by the seed -- the noise multiplies the
derivative instead of quantising it, the realisation is smooth in eta, and the finite
difference is well posed. Averaging over replicate seeds then estimates the derivative of
the mean, with Monte Carlo error that does NOT vanish as h -> 0.

Both models are implemented. `lognormal` is the default and is what the reported
diagnostics use; `poisson` exists as a NEGATIVE CONTROL, to demonstrate the failure mode
rather than to assert it.

REPRODUCIBILITY
---------------
`simulate(...)` is a pure function of (eta, seed, params, stochastic, noise_model). The
same arguments give bit-identical output. The deterministic core is fixed-step RK4 -- not
an adaptive solver -- because adaptive step selection changes discontinuously with
parameters and is itself a classical source of the computational noise that would destroy
the finite difference (More & Wild 2011).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, replace
from typing import Literal, Sequence

import numpy as np

__all__ = [
    "COMPONENTS",
    "K",
    "ETA_SCALE",
    "SIR3Params",
    "BASE",
    "SimOutput",
    "simulate",
    "peak_prevalence_fraction",
    "prior_predictive_sd",
]

#: The component decomposition, in the order the Jacobian's columns are laid out.
COMPONENTS: tuple[str, str, str] = ("transmission", "progression", "observation")

#: Number of components. K = 3 throughout; the random-attributor floor is 1/K.
K: int = len(COMPONENTS)

#: Fixed relative perturbation scale for every eta_k (THRESHOLDS §0). See module docstring.
ETA_SCALE: float = 0.1

NoiseModel = Literal["lognormal", "poisson"]


@dataclass(frozen=True)
class SIR3Params:
    """Base (undistorted) simulator parameters.

    These are the *specification*. A distortion eta_k != 0 does not change them; it
    changes the functional form of component k, leaving this record intact.
    """

    N: float = 100_000.0          # population size
    I0: float = 10.0              # initial infectious count
    beta: float = 0.35            # transmission rate, per day
    gamma: float = 0.14           # removal rate, per day  (R0 = beta/gamma = 2.5)
    T_days: int = 120             # observation window, days
    substeps: int = 24            # fixed RK4 substeps per day (hourly)
    rho: float = 0.40             # base reporting fraction
    delay_mean: float = 3.0       # reporting delay, mean days
    delay_shape: float = 3.0      # reporting delay, gamma shape
    delay_len: int = 21           # delay kernel support, days
    obs_sigma: float = 0.15       # lognormal observation noise scale

    def __post_init__(self) -> None:
        if self.N <= 0 or self.I0 <= 0 or self.I0 >= self.N:
            raise ValueError("require 0 < I0 < N")
        if self.beta <= 0 or self.gamma <= 0:
            raise ValueError("require beta > 0 and gamma > 0")
        if self.T_days < 2 or self.substeps < 1:
            raise ValueError("require T_days >= 2 and substeps >= 1")
        if not 0.0 < self.rho <= 1.0:
            raise ValueError("require 0 < rho <= 1")


#: The base specification used everywhere unless a caller overrides it.
BASE = SIR3Params()


@dataclass(frozen=True)
class SimOutput:
    """One simulator run.

    Attributes
    ----------
    days:
        Integer day index, ``0 .. T_days - 1``.
    true_incidence:
        New infections per day, from the deterministic core. Never observed.
    reported_mean:
        Expected reported incidence per day: ``true_incidence`` convolved with the delay
        kernel and scaled by the (possibly distorted) reporting fraction. This is the
        deterministic observation-layer output.
    reported:
        What the diagnostic actually sees. Equal to ``reported_mean`` when
        ``stochastic=False``; otherwise ``reported_mean`` perturbed by the observation
        noise model.
    """

    days: np.ndarray
    true_incidence: np.ndarray
    reported_mean: np.ndarray
    reported: np.ndarray


def _delay_kernel(p: SIR3Params) -> np.ndarray:
    """Discretised gamma reporting-delay kernel, normalised to sum to one.

    Part of the base OBSERVATION component. Held fixed under every distortion family,
    including the observation family -- see the module docstring for why, and for the
    limitation that entails.
    """
    shape = p.delay_shape
    scale = p.delay_mean / shape
    edges = np.arange(p.delay_len + 1, dtype=float)
    # Regularised lower incomplete gamma, evaluated by a series that needs no SciPy.
    cdf = np.array([_gamma_cdf(e, shape, scale) for e in edges])
    w = np.diff(cdf)
    total = w.sum()
    if total <= 0:
        raise RuntimeError("degenerate delay kernel")
    return w / total


def _gamma_cdf(x: float, shape: float, scale: float) -> float:
    """Regularised lower incomplete gamma P(shape, x/scale), by series expansion.

    Written out rather than imported so the simulator's deterministic core has no
    dependency whose version could silently change the base specification.
    """
    if x <= 0.0:
        return 0.0
    z = x / scale
    # Series representation, adequate here since z stays modest (z <= delay_len/scale).
    term = 1.0 / shape
    total = term
    for n in range(1, 500):
        term *= z / (shape + n)
        total += term
        if abs(term) < 1e-16 * abs(total):
            break
    return total * math.exp(-z + shape * math.log(z) - math.lgamma(shape))


def _rhs(t: float, y: np.ndarray, p: SIR3Params, eta: np.ndarray, p_ref: float) -> np.ndarray:
    """Right-hand side of the distorted SIR system.

    State is ``(S, I, C)`` with ``C`` the cumulative infection count, so that daily
    incidence is a difference of ``C``.
    """
    S, I, _C = y

    # --- component 1: TRANSMISSION, with saturating-incidence distortion -------------
    denom = 1.0 + eta[0] * (I / p.N) / p_ref
    if denom <= 0.0:
        raise ValueError(
            f"transmission distortion eta_1={eta[0]!r} drives the saturation denominator "
            f"non-positive (denom={denom!r}); the family is not defined there"
        )
    incidence = (p.beta * S * I / p.N) / denom

    # --- component 2: PROGRESSION, with mean-centred log-linear hazard drift ---------
    gamma_t = p.gamma * math.exp(eta[1] * (t / p.T_days - 0.5))
    removal = gamma_t * I

    return np.array([-incidence, incidence - removal, incidence])


def _integrate(p: SIR3Params, eta: np.ndarray, p_ref: float) -> np.ndarray:
    """Fixed-step RK4 over the observation window. Returns daily true incidence."""
    dt = 1.0 / p.substeps
    y = np.array([p.N - p.I0, p.I0, 0.0])
    cumulative = np.empty(p.T_days + 1)
    cumulative[0] = 0.0
    t = 0.0
    for day in range(p.T_days):
        for _ in range(p.substeps):
            k1 = _rhs(t, y, p, eta, p_ref)
            k2 = _rhs(t + dt / 2, y + dt / 2 * k1, p, eta, p_ref)
            k3 = _rhs(t + dt / 2, y + dt / 2 * k2, p, eta, p_ref)
            k4 = _rhs(t + dt, y + dt * k3, p, eta, p_ref)
            y = y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            t += dt
        cumulative[day + 1] = y[2]
    return np.diff(cumulative)


_P_REF_CACHE: dict[tuple, float] = {}


def peak_prevalence_fraction(params: SIR3Params = BASE) -> float:
    """Base model's peak prevalence as a fraction of N. The constant ``p_ref``.

    Used only to normalise the TRANSMISSION distortion family so that ``eta_1 = 1`` means
    "incidence at the peak is halved". It is computed from the UNDISTORTED simulator, where
    the distortion term it normalises is inert, so there is no circularity: at ``eta = 0``
    the value of ``p_ref`` cannot affect the trajectory it is derived from.

    Deterministic, cached, and recorded in every results file as a normalisation constant.
    """
    key = (params.N, params.I0, params.beta, params.gamma, params.T_days, params.substeps)
    if key in _P_REF_CACHE:
        return _P_REF_CACHE[key]
    dt = 1.0 / params.substeps
    y = np.array([params.N - params.I0, params.I0, 0.0])
    peak_I = params.I0
    t = 0.0
    zero = np.zeros(K)
    for _ in range(params.T_days * params.substeps):
        k1 = _rhs(t, y, params, zero, 1.0)
        k2 = _rhs(t + dt / 2, y + dt / 2 * k1, params, zero, 1.0)
        k3 = _rhs(t + dt / 2, y + dt / 2 * k2, params, zero, 1.0)
        k4 = _rhs(t + dt, y + dt * k3, params, zero, 1.0)
        y = y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += dt
        peak_I = max(peak_I, float(y[1]))
    value = peak_I / params.N
    _P_REF_CACHE[key] = value
    return value


def simulate(
    eta: Sequence[float] = (0.0, 0.0, 0.0),
    *,
    seed: int,
    params: SIR3Params = BASE,
    stochastic: bool = True,
    noise_model: NoiseModel = "lognormal",
) -> SimOutput:
    """Run the simulator under distortion ``eta``.

    Parameters
    ----------
    eta:
        Distortion vector in NATIVE units, ordered as :data:`COMPONENTS`. ``eta = 0``
        reproduces the base simulator exactly, for every component, by construction.
    seed:
        Fixes the observation-noise realisation. Passing the same seed at ``eta + h`` and
        ``eta - h`` is the common-random-numbers construction the Jacobian estimator
        requires; without it the difference quotient is contaminated by simulation noise
        that is indistinguishable from the signal being measured.
    stochastic:
        Whether to apply the observation noise layer at all. ``False`` gives the
        deterministic observation output and is used as a control.
    noise_model:
        ``"lognormal"`` (default, continuous, differentiable under CRN) or ``"poisson"``
        (count-valued, NOT differentiable under CRN -- a negative control only).

    Returns
    -------
    SimOutput
    """
    eta_arr = np.asarray(eta, dtype=float)
    if eta_arr.shape != (K,):
        raise ValueError(f"eta must have shape ({K},), got {eta_arr.shape}")
    if not np.all(np.isfinite(eta_arr)):
        raise ValueError(f"eta must be finite, got {eta_arr!r}")

    p_ref = peak_prevalence_fraction(params)
    true_incidence = _integrate(params, eta_arr, p_ref)

    # --- component 3: OBSERVATION -----------------------------------------------------
    kernel = _delay_kernel(params)
    delayed = np.convolve(true_incidence, kernel)[: params.T_days]
    rho_eff = params.rho * math.exp(eta_arr[2])
    if rho_eff > 1.0:
        # Not an error: rho is a reporting fraction of a modelled quantity and the
        # distortion is allowed to push it past 1. Recorded rather than clipped, because
        # clipping would introduce a kink at the clip point and destroy differentiability.
        pass
    reported_mean = rho_eff * delayed

    if not stochastic:
        reported = reported_mean.copy()
    elif noise_model == "lognormal":
        rng = np.random.default_rng(seed)
        z = rng.standard_normal(params.T_days)
        s = params.obs_sigma
        reported = reported_mean * np.exp(s * z - 0.5 * s * s)
    elif noise_model == "poisson":
        rng = np.random.default_rng(seed)
        reported = rng.poisson(np.maximum(reported_mean, 0.0)).astype(float)
    else:
        raise ValueError(f"unknown noise_model {noise_model!r}")

    return SimOutput(
        days=np.arange(params.T_days),
        true_incidence=true_incidence,
        reported_mean=reported_mean,
        reported=reported,
    )


def prior_predictive_sd(
    summary_fn,
    *,
    n_replicates: int,
    seed0: int,
    params: SIR3Params = BASE,
    noise_model: NoiseModel = "lognormal",
) -> tuple[np.ndarray, np.ndarray]:
    """Prior-predictive mean and standard deviation of a summary map, at ``eta = 0``.

    THRESHOLDS §0 requires each summary statistic to be divided by its prior-predictive
    standard deviation, estimated from undistorted replicates, and requires the estimate
    and the replicate count to be recorded in every results file.

    Returns ``(mean, sd)``, each of length ``d``. Seeds used are ``seed0 .. seed0+n-1``;
    the estimator is therefore reproducible from the recorded ``seed0`` alone.
    """
    if n_replicates < 2:
        raise ValueError("need at least 2 replicates for a standard deviation")
    rows = [
        summary_fn(simulate(np.zeros(K), seed=seed0 + r, params=params,
                            stochastic=True, noise_model=noise_model))
        for r in range(n_replicates)
    ]
    arr = np.asarray(rows, dtype=float)
    return arr.mean(axis=0), arr.std(axis=0, ddof=1)


def with_params(**kwargs) -> SIR3Params:
    """Convenience: a copy of :data:`BASE` with fields overridden."""
    return replace(BASE, **kwargs)
