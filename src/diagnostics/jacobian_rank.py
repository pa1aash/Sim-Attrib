"""Rank and coherence diagnostic for the summary-statistic Jacobian J = ds/deta.

WHAT THIS IS, AND WHAT IT IS NOT
---------------------------------
This is INFRASTRUCTURE, not a claimed method contribution. ``docs/DECISIONS.md`` D-6 and
``audit/R2_THREAT_CHECK.md`` record why: the rank-and-condition-number screen on a
sensitivity matrix is Cintron-Arias, Banks, Capaldi & Lloyd (2009), *J. Inverse Ill-posed
Problems* 17(6), which runs it on an epidemic model; finite differencing under simulation
noise is More & Wild (2012), *ACM TOMS* 38(3), whose difference parameter is provably
near-optimal and is a stronger result than the h-sweep here. Neither is claimed as new.

What the diagnostic is FOR is the composition the project is building toward: maximized
Monte Carlo (Dufour 2006) composed with a selection event, for component-level
misspecification attribution. That composition is only meaningful to run where component
attribution is well posed -- where the summary Jacobian satisfies the rank condition. This
module decides, for THIS simulator and THIS closed list of summary sets, whether it does.

The one seam ``audit/R2_THREAT_CHECK.md`` §2 identifies -- that nobody carries an estimated
noise level forward into the rank TOLERANCE -- is deliberately NOT occupied here. The
tolerance tau used below comes from ``docs/THRESHOLDS.md`` §1.2, where it is derived from a
compute budget (separation costs n ~ kappa^2 draws), not from a noise level. Occupying the
seam would mean re-deriving tau after the thresholds were pre-registered, which D-6 forbids
without a ``DEVIATIONS.md`` entry.

LEAKAGE
-------
The diagnostic never receives a component index, a ground-truth label, or any indication of
which component is "really" responsible for anything. Its entire input is (i) the simulator
as a callable, (ii) the distortion basis -- that is, the fact that there are K
one-parameter families and that perturbing family k means setting eta_k -- and (iii) the
resulting summary vectors. It computes a property of the map, not a guess about a hidden
truth, so there is no hidden truth available to leak.

**Until session G4 that argument was recorded in every results file as
``leakage_checked: true``, and nothing computed it.** It was a hard-coded literal: there was
no condition under which the field could have read ``false``, which is the defect class
``DEVIATIONS.md`` D-8 exists to name. The argument above was and is sound; the field claiming
it had been checked was not a check.

:func:`leakage_check` replaces it with one that can fail. The testable content of the claim is
**equivariance under relabelling the components**: if the diagnostic really treats the K
columns symmetrically and holds no privileged knowledge about which is which, then permuting
the columns must leave the singular values, the numerical rank and the condition number
unchanged, and must permute the column norms, the coherence matrix and the right singular
vectors correspondingly. Any component-indexed special case -- a threshold applied to one
column, an assumption that column 2 is the observation component -- breaks that and is caught.
It is a necessary condition rather than a proof of no leakage, and it is stated as one.

THE ESTIMATOR
-------------
For each component k and each step size h (in NORMALISED units; the native step is
``h * ETA_SCALE``):

    J[:, k]  =  ( 1/R ) * sum_r  [ s(+h e_k ; seed_r) - s(-h e_k ; seed_r) ] / (2h) / sigma

with the SAME replicate seeds ``seed_r`` used at ``+h`` and ``-h``. That is the
common-random-numbers construction, and it is not optional. Without it the two evaluations
draw independent observation noise, the difference quotient inherits noise of order
``sigma_obs / h``, and at small h that term swamps the signal completely: the finite
difference then measures the simulator's randomness rather than its response. With common
random numbers the noise realisation is frozen, the difference differentiates a fixed
smooth function of eta, and averaging over R replicates estimates the derivative of the
mean with Monte Carlo error that does not blow up as h -> 0.

``crn=False`` is available and is used as a NEGATIVE CONTROL, to show the failure rather
than assert it.

H IS A LIST, NOT A SCALAR
-------------------------
A rank computed at one arbitrary h is not a result. ``estimate_jacobian`` therefore takes
``h_values`` as a sequence and rejects a scalar, so that a single-h call is not expressible.
``docs/THRESHOLDS.md`` §1.4 fixes the sweep at ``{1e-1 ... 1e-6}`` and requires the PLATEAU
to be reported.

THE PLATEAU RULE IS NEW THIS SESSION AND IS STATED HERE
--------------------------------------------------------
``docs/THRESHOLDS.md`` §1.4 pre-registered the *resolution* criterion -- a singular value
is resolved if it varies by less than a factor of :data:`RESOLVE_FACTOR` across the
identified plateau -- but did not say how the plateau is identified. That rule is fixed
here, before any singular value existed in this repository, and is stated so it can be
disagreed with:

    The plateau is the longest contiguous run of h values over which the estimated
    Jacobian itself has stopped moving, i.e. over which every adjacent pair satisfies
        ||J(h_{i+1}) - J(h_i)||_F / ||J(h_i)||_F  <  PLATEAU_REL_TOL.

The criterion is stated on J rather than on the singular values on purpose. Using "the
singular values are stable" to define the region in which one then tests whether the
singular values are stable would be circular; the Frobenius criterion is on the estimate,
and the resolution test is then a genuine test applied inside the region it identifies.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Sequence

import numpy as np

from ..simulators.sir3 import BASE, ETA_SCALE, K, SIR3Params, NoiseModel, simulate

__all__ = [
    "leakage_check",
    "TAU",
    "KAPPA_MAX",
    "COLNORM_INVISIBLE",
    "COHERENCE_FLAG",
    "VK_MIN",
    "RESOLVE_FACTOR",
    "PLATEAU_REL_TOL",
    "H_VALUES",
    "estimate_jacobian",
    "analyse",
]

# --- Thresholds pre-registered in docs/THRESHOLDS.md -------------------------------------
# These are NOT to be revised after seeing a singular value. Revising any of them requires a
# DEVIATIONS.md entry stating what changed, what result prompted it, and why the change is
# not motivated by that result.

#: Numerical-rank tolerance, relative to sigma_1. THRESHOLDS §1.2. Derived from the study's
#: simulation budget (separation costs n ~ kappa^2 draws), not from machine epsilon.
TAU: float = 1e-2

#: Condition-number ceiling above which a summary set is "inseparable". THRESHOLDS §1.3.
KAPPA_MAX: float = 100.0

#: Column-norm floor below which a component is "invisible" to a summary set -- a DIFFERENT
#: failure from collinearity, kept separate because rank alone conflates them. THRESHOLDS §1.5.
COLNORM_INVISIBLE: float = 0.1

#: Pairwise-coherence level at which a column pair is FLAGGED for inspection. Deliberately
#: NOT the decision rule; the decision rule is on the singular values. THRESHOLDS §2.2.
COHERENCE_FLAG: float = 0.98

#: Component k joins the equivalence class named by a near-null right singular vector v
#: iff |v_k| >= this. THRESHOLDS §2.1.
VK_MIN: float = 0.3

#: A singular value is RESOLVED if it varies by less than this factor across the plateau.
#: An unresolved singular value is reported as unresolved and counted toward the rank in
#: NEITHER direction. THRESHOLDS §1.4.
RESOLVE_FACTOR: float = 2.0

#: The pre-registered step-size sweep, in NORMALISED units. THRESHOLDS §1.4.
H_VALUES: tuple[float, ...] = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6)

# --- Fixed this session (G3), before any singular value existed --------------------------

#: Relative Frobenius change between adjacent h below which the Jacobian estimate counts as
#: having stopped moving. Fixes the plateau-identification rule that THRESHOLDS §1.4 left
#: open. See the module docstring.
PLATEAU_REL_TOL: float = 0.05


@dataclass(frozen=True)
class JacobianSweep:
    """Normalised Jacobian estimates across the h sweep, for one summary set."""

    summary_set: str
    h_values: tuple[float, ...]
    jacobians: tuple[np.ndarray, ...]  # each (d, K), normalised
    sd: np.ndarray                     # (d,) prior-predictive standard deviations used
    n_replicates: int
    seed0: int
    crn: bool
    eta_scale: float
    n_simulations: int
    extras: dict[str, Any] = field(default_factory=dict)


def estimate_jacobian(
    summary_fns: Mapping[str, Callable],
    sd_map: Mapping[str, np.ndarray],
    *,
    h_values: Sequence[float],
    n_replicates: int,
    seed0: int,
    params: SIR3Params = BASE,
    eta_scale: float = ETA_SCALE,
    noise_model: NoiseModel = "lognormal",
    crn: bool = True,
    stochastic: bool = True,
) -> dict[str, JacobianSweep]:
    """Estimate the normalised Jacobian for every summary set, across the whole h sweep.

    All summary sets are computed from the SAME simulator runs. That is not only cheaper --
    it means the three sets are compared on identical noise realisations, so a difference
    between them is a property of the summaries and not of which draws they happened to get.

    Parameters
    ----------
    summary_fns:
        Mapping ``name -> callable(SimOutput) -> ndarray``.
    sd_map:
        Mapping ``name -> ndarray`` of prior-predictive standard deviations, one per
        summary coordinate. Required, not optional: an unnormalised rank is uninterpretable
        (THRESHOLDS §0).
    h_values:
        The step-size sweep, in normalised units. A scalar is REJECTED -- a rank computed at
        one arbitrary h is not a result.
    n_replicates:
        Replicates ``R`` averaged at each evaluation. Seeds are ``seed0 .. seed0+R-1``.
    crn:
        Common random numbers across the ``+h`` and ``-h`` evaluations. ``False`` is the
        negative control.

    Returns
    -------
    dict[str, JacobianSweep]
    """
    if np.isscalar(h_values) or isinstance(h_values, (float, int)):
        raise TypeError(
            "h_values must be a sequence of step sizes, not a scalar: a rank computed at "
            "one arbitrary h is not a result (docs/THRESHOLDS.md §1.4)"
        )
    h_list = [float(h) for h in h_values]
    if len(h_list) < 2:
        raise ValueError("need at least 2 step sizes to identify a plateau")
    if any(h <= 0 for h in h_list):
        raise ValueError("step sizes must be positive")
    if n_replicates < 1:
        raise ValueError("n_replicates must be >= 1")
    missing = set(summary_fns) - set(sd_map)
    if missing:
        raise ValueError(f"no prior-predictive sd supplied for summary set(s): {sorted(missing)}")
    for name, sd in sd_map.items():
        if np.any(np.asarray(sd) <= 0):
            raise ValueError(
                f"summary set {name!r} has a coordinate with zero prior-predictive sd; it is "
                f"degenerate under the base simulator and must be dropped, with the drop "
                f"recorded (docs/THRESHOLDS.md §0)"
            )

    # A seed offset used ONLY when crn=False, to force independent noise across +h and -h.
    non_crn_offset = 10_000_000

    n_sims = 0
    # columns[name][h_index] -> list of K column vectors
    columns: dict[str, list[list[np.ndarray]]] = {
        name: [[] for _ in h_list] for name in summary_fns
    }

    for hi, h in enumerate(h_list):
        step = h * eta_scale
        for k in range(K):
            acc = {name: [] for name in summary_fns}
            for r in range(n_replicates):
                seed_plus = seed0 + r
                seed_minus = seed0 + r if crn else seed0 + r + non_crn_offset
                eta_p = np.zeros(K)
                eta_p[k] = step
                eta_m = np.zeros(K)
                eta_m[k] = -step
                out_p = simulate(eta_p, seed=seed_plus, params=params,
                                 stochastic=stochastic, noise_model=noise_model)
                out_m = simulate(eta_m, seed=seed_minus, params=params,
                                 stochastic=stochastic, noise_model=noise_model)
                n_sims += 2
                for name, fn in summary_fns.items():
                    acc[name].append((fn(out_p) - fn(out_m)) / (2.0 * h))
            for name in summary_fns:
                col = np.mean(np.asarray(acc[name], dtype=float), axis=0)
                columns[name][hi].append(col / np.asarray(sd_map[name], dtype=float))

    return {
        name: JacobianSweep(
            summary_set=name,
            h_values=tuple(h_list),
            jacobians=tuple(np.column_stack(cols) for cols in columns[name]),
            sd=np.asarray(sd_map[name], dtype=float),
            n_replicates=n_replicates,
            seed0=seed0,
            crn=crn,
            eta_scale=eta_scale,
            n_simulations=n_sims // len(summary_fns) if summary_fns else 0,
        )
        for name in summary_fns
    }


def _find_plateau(jacobians: Sequence[np.ndarray], rel_tol: float) -> tuple[int, int]:
    """Longest contiguous index run over which the Jacobian estimate has stopped moving.

    Returns ``(lo, hi)`` inclusive index bounds. Falls back to the whole sweep when no
    adjacent pair meets the criterion, which is itself reported: a "plateau" spanning the
    whole sweep because nothing was stable is not the same as one because everything was,
    and :func:`analyse` distinguishes them via ``plateau_found``.
    """
    rels = []
    for a, b in zip(jacobians[:-1], jacobians[1:]):
        denom = np.linalg.norm(a, "fro")
        rels.append(np.linalg.norm(b - a, "fro") / denom if denom > 0 else np.inf)
    best = (0, 0)
    lo = 0
    for i, rel in enumerate(rels):
        if rel < rel_tol:
            if (i + 1 - lo) > (best[1] - best[0]):
                best = (lo, i + 1)
        else:
            lo = i + 1
    return best


def analyse(
    sweep: JacobianSweep,
    *,
    tau: float = TAU,
    kappa_max: float = KAPPA_MAX,
    colnorm_invisible: float = COLNORM_INVISIBLE,
    coherence_flag: float = COHERENCE_FLAG,
    vk_min: float = VK_MIN,
    resolve_factor: float = RESOLVE_FACTOR,
    plateau_rel_tol: float = PLATEAU_REL_TOL,
) -> dict[str, Any]:
    """Turn an h-sweep into the reportable diagnostic.

    Every threshold is a PARAMETER of this function, not a constant inside it, so a reader
    can re-apply their own. The full singular-value table across the whole sweep is
    returned as well, so a reader who rejects every threshold here can still recompute.
    """
    Js = list(sweep.jacobians)
    hs = list(sweep.h_values)
    d, kk = Js[0].shape

    def _svd_padded(M: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Singular values padded to length K, and the full K x K right-singular basis.

        ``full_matrices=True`` matters. For the impoverished set S_C, ``d = 2 < K = 3``, and
        the economy SVD would return only two singular values and two right singular
        vectors -- silently omitting the EXACT null direction, which is the entire content
        of that positive control. Padding the spectrum with structural zeros and keeping the
        full V reports the deficiency instead of hiding it.
        """
        _u, s_raw, vt = np.linalg.svd(M, full_matrices=True)
        s = np.zeros(kk)
        s[: len(s_raw)] = s_raw
        return s, vt

    per_h = []
    sv_all = []
    for h, J in zip(hs, Js):
        sv_h, _vt_h = _svd_padded(J)
        sv_all.append(sv_h)
        per_h.append({"h": float(h), "singular_values": [float(x) for x in sv_h]})

    rel_changes = []
    for i in range(len(Js) - 1):
        denom = np.linalg.norm(Js[i], "fro")
        rel_changes.append(
            float(np.linalg.norm(Js[i + 1] - Js[i], "fro") / denom) if denom > 0 else float("inf")
        )

    lo, hi = _find_plateau(Js, plateau_rel_tol)
    plateau_found = hi > lo
    idx = list(range(lo, hi + 1))
    rep = idx[len(idx) // 2]  # representative h: middle of the plateau

    sv_plateau = np.array([sv_all[i] for i in idx])  # (n_plateau, K)
    sv_min = sv_plateau.min(axis=0)
    sv_max = sv_plateau.max(axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        # A structurally-zero singular value (d < K) is exactly 0 at every h, so it does not
        # "vary" and is RESOLVED -- resolved as zero. Only a positive value with an unstable
        # ratio is unresolved.
        variation = np.where(sv_max == 0.0, 1.0, np.where(sv_min > 0, sv_max / sv_min, np.inf))
    resolved = [bool(v < resolve_factor) for v in variation]

    J = Js[rep]
    sv, Vt = _svd_padded(J)
    sv1 = float(sv[0])

    # --- numerical rank, honouring the unresolved rule ------------------------------------
    # THRESHOLDS §1.4: an unresolved singular value is counted toward the rank in NEITHER
    # direction. So the rank is reported as an interval when any borderline sigma is
    # unresolved, and as a number only when every sigma that matters is resolved.
    above = [bool(s >= tau * sv1) for s in sv]
    rank_certain = sum(1 for i, a in enumerate(above) if a and resolved[i])
    rank_possible = sum(1 for i, a in enumerate(above) if a or not resolved[i])
    rank_determined = rank_certain == rank_possible

    kappa = float(sv[0] / sv[-1]) if sv[-1] > 0 else float("inf")

    col_norms = [float(np.linalg.norm(J[:, k])) for k in range(kk)]
    invisible = [bool(c < colnorm_invisible) for c in col_norms]

    coherence = np.zeros((kk, kk))
    for i in range(kk):
        for j in range(kk):
            ni, nj = col_norms[i], col_norms[j]
            coherence[i, j] = abs(float(J[:, i] @ J[:, j])) / (ni * nj) if ni > 0 and nj > 0 else np.nan
    flagged_pairs = [
        [i, j] for i in range(kk) for j in range(i + 1, kk)
        if np.isfinite(coherence[i, j]) and coherence[i, j] >= coherence_flag
    ]

    # --- near-null right singular vectors, with |v_k| RANGES across the plateau ----------
    near_null = []
    for i, s in enumerate(sv):
        if s > tau * sv1:
            continue
        vk_across = np.asarray([np.abs(_svd_padded(Js[j])[1][i]) for j in idx])
        members, borderline = [], []
        for k in range(kk):
            lo_k = float(vk_across[:, k].min())
            hi_k = float(vk_across[:, k].max())
            if lo_k >= vk_min:
                members.append(k)          # unambiguously in the class across the plateau
            elif hi_k >= vk_min:
                borderline.append(k)       # |v_k| crosses the threshold within the plateau
        near_null.append(
            {
                "index": int(i),
                "singular_value": float(s),
                "sigma_ratio_to_sigma1": float(s / sv1) if sv1 > 0 else float("inf"),
                "right_singular_vector_at_representative_h": [float(x) for x in Vt[i]],
                "abs_vk_range_across_plateau": [
                    [float(vk_across[:, k].min()), float(vk_across[:, k].max())] for k in range(kk)
                ],
                "equivalence_class_members": members,
                "borderline_members": borderline,
                "degeneracy_kind": "exact" if s == 0.0 else "near",
            }
        )

    inseparable = (not rank_determined) or (rank_certain < kk) or (kappa > kappa_max)

    return {
        "dimensions": {"d": int(d), "K": int(kk)},
        "h_sweep": per_h,
        "relative_frobenius_change_between_adjacent_h": rel_changes,
        "plateau": {
            "rule": (
                "longest contiguous run of h with "
                "||J(h_{i+1})-J(h_i)||_F / ||J(h_i)||_F < plateau_rel_tol"
            ),
            "plateau_rel_tol": float(plateau_rel_tol),
            "found": bool(plateau_found),
            "h_range": [float(hs[lo]), float(hs[hi])],
            "h_indices": [int(lo), int(hi)],
            "n_h_in_plateau": int(len(idx)),
            "representative_h": float(hs[rep]),
            # A plateau that runs to the edge of the pre-registered sweep is CENSORED there:
            # the sweep stopped, not the plateau. Reporting it as a bounded plateau would
            # claim knowledge of where the truncation or cancellation branch begins, which
            # this sweep does not have.
            "censored_at_large_h": bool(lo == 0),
            "censored_at_small_h": bool(hi == len(hs) - 1),
        },
        "singular_values_at_representative_h": [float(x) for x in sv],
        "singular_value_range_across_plateau": [
            [float(a), float(b)] for a, b in zip(sv_min, sv_max)
        ],
        "singular_value_variation_factor": [float(x) for x in variation],
        "resolved": resolved,
        "resolve_factor": float(resolve_factor),
        "numerical_rank": {
            "tau": float(tau),
            "rule": "rank = #{ i : sigma_i >= tau * sigma_1 }, with unresolved sigma counted in neither direction",
            "rank_certain": int(rank_certain),
            "rank_possible": int(rank_possible),
            "determined": bool(rank_determined),
            "full_column_rank": bool(rank_determined and rank_certain == kk),
        },
        "condition_number": kappa,
        "kappa_max": float(kappa_max),
        "column_norms": col_norms,
        "colnorm_invisible_threshold": float(colnorm_invisible),
        "invisible_components": [i for i, v in enumerate(invisible) if v],
        "pairwise_coherence": [[float(x) for x in row] for row in coherence],
        "coherence_flag_threshold": float(coherence_flag),
        "coherence_flagged_pairs": flagged_pairs,
        "right_singular_vectors_at_representative_h": [[float(x) for x in row] for row in Vt],
        "near_null_directions": near_null,
        "vk_min": float(vk_min),
        "inseparable": bool(inseparable),
        "inseparable_reason": (
            "rank undetermined (an unresolved singular value straddles the tolerance)"
            if not rank_determined
            else "rank deficient at tau"
            if rank_certain < kk
            else f"condition number {kappa:.4g} exceeds kappa_max {kappa_max:g}"
            if kappa > kappa_max
            else "separable: full column rank at tau and condition number within ceiling"
        ),
    }


def leakage_check(
    sweep: JacobianSweep,
    *,
    tol: float = 1e-10,
    **analyse_kwargs: Any,
) -> dict[str, Any]:
    """Test the leakage claim by relabelling the components, instead of asserting it.

    Runs :func:`analyse` on the sweep and on every non-identity permutation of its columns,
    and requires that

      * the singular values, the numerical rank and the condition number are UNCHANGED;
      * the column norms and the pairwise coherence matrix PERMUTE with the labels;
      * each near-null right singular vector permutes with them too, up to sign, which the SVD
        does not fix.

    Under what condition does this read ``false``? Any component-indexed behaviour anywhere in
    the analysis path: a per-column threshold, a hard-coded "column 2 is the observation
    component", an ordering assumption in the equivalence-class rule. The check is run against
    a deliberately label-dependent analysis in ``tests/test_jacobian_rank.py`` to confirm it
    detects one, per D-8's rule that a check should be seen giving the opposite answer.

    **What it does not establish.** Equivariance is necessary, not sufficient: a leak that
    treated all components symmetrically would survive it. The prose claim above is the
    argument; this is the part of it that is mechanically checkable.
    """
    from itertools import permutations

    base = analyse(sweep, **analyse_kwargs)
    kk = base["dimensions"]["K"]
    worst: dict[str, float] = {"singular_values": 0.0, "condition_number": 0.0,
                               "column_norms": 0.0, "coherence": 0.0,
                               "near_null_vectors": 0.0}
    failures: list[dict[str, Any]] = []

    for perm in permutations(range(kk)):
        if perm == tuple(range(kk)):
            continue
        permuted = JacobianSweep(
            summary_set=sweep.summary_set,
            h_values=sweep.h_values,
            jacobians=tuple(J[:, list(perm)] for J in sweep.jacobians),
            sd=sweep.sd,
            n_replicates=sweep.n_replicates,
            seed0=sweep.seed0,
            crn=sweep.crn,
            eta_scale=sweep.eta_scale,
            n_simulations=sweep.n_simulations,
        )
        other = analyse(permuted, **analyse_kwargs)

        d_sv = float(np.max(np.abs(np.asarray(other["singular_values_at_representative_h"])
                                   - np.asarray(base["singular_values_at_representative_h"]))))
        b_k, o_k = base["condition_number"], other["condition_number"]
        d_k = 0.0 if (b_k == o_k) else float(abs(o_k - b_k))
        d_cn = float(np.max(np.abs(np.asarray(other["column_norms"])
                                   - np.asarray(base["column_norms"])[list(perm)])))
        d_co = float(np.max(np.abs(np.asarray(other["pairwise_coherence"])
                                   - np.asarray(base["pairwise_coherence"])[np.ix_(list(perm), list(perm))])))

        d_nn = 0.0
        if len(other["near_null_directions"]) != len(base["near_null_directions"]):
            d_nn = float("inf")
        else:
            for nb, no in zip(base["near_null_directions"], other["near_null_directions"]):
                vb = np.asarray(nb["right_singular_vector_at_representative_h"])[list(perm)]
                vo = np.asarray(no["right_singular_vector_at_representative_h"])
                d_nn = max(d_nn, float(min(np.max(np.abs(vo - vb)), np.max(np.abs(vo + vb)))))

        worst["singular_values"] = max(worst["singular_values"], d_sv)
        worst["condition_number"] = max(worst["condition_number"], d_k)
        worst["column_norms"] = max(worst["column_norms"], d_cn)
        worst["coherence"] = max(worst["coherence"], d_co)
        worst["near_null_vectors"] = max(worst["near_null_vectors"], d_nn)

        same_rank = (other["numerical_rank"]["rank_certain"] == base["numerical_rank"]["rank_certain"]
                     and other["numerical_rank"]["rank_possible"] == base["numerical_rank"]["rank_possible"])
        if not same_rank or max(d_sv, d_k, d_cn, d_co, d_nn) > tol:
            failures.append({"permutation": list(perm), "rank_unchanged": bool(same_rank),
                             "max_singular_value_change": d_sv, "condition_number_change": d_k,
                             "max_column_norm_mismatch": d_cn, "max_coherence_mismatch": d_co,
                             "max_near_null_vector_mismatch": d_nn})

    return {
        "what_is_checked": (
            "component-label equivariance: permuting the K columns must leave the singular "
            "values, the numerical rank and the condition number unchanged, and must permute "
            "the column norms, the coherence matrix and the near-null right singular vectors "
            "(up to sign) correspondingly"
        ),
        "why_this_is_the_testable_content_of_the_leakage_claim": (
            "the diagnostic is given no component index and no ground-truth label, so it must "
            "treat the K columns symmetrically. Any component-indexed special case breaks "
            "equivariance and is caught here. Necessary, not sufficient: a leak that treated "
            "all components symmetrically would survive this."
        ),
        "n_permutations_tested": int(len(list(permutations(range(kk)))) - 1),
        "tolerance": float(tol),
        "worst_discrepancy": worst,
        "failures": failures,
        "passes": bool(not failures),
    }
