"""The selection rule ``k-hat``, and the discrepancy statistic ``T_k`` it maximises.

WHY THIS FILE HAD TO BE WRITTEN BEFORE ``p_sel`` COULD BE MEASURED
------------------------------------------------------------------
``audit/MMC_COMPOSITION_SPEC.md`` §4 defines the quantity the cost gate turns on::

    p_sel(theta) = P( k-hat(y) = k | theta, eta = 0 )

-- the probability that a draw from the null lands in the observed selection cell. That
definition is complete except for one thing: ``k-hat`` is ``argmax_j T_j(y)``, and §6 of the
same specification leaves ``T_k`` **"not specified"** and **"deferred"**. ``OUTSTANDING.md``
**O-16** records the consequence in one line: *"One thing must be specified before it can be
measured at all."*

**So this module is not an implementation of the composition.** The composition is the
rejection sampler inside Dufour's nuisance maximisation, and none of it is written here or
anywhere else in this repository. This module is the one deferred ingredient the cost
measurement cannot proceed without, and it is deliberately the whole of what session G6
added. ``DEVIATIONS.md`` **D-14** records the choice, its timing, and what a different
choice would do to the number.

THE FOUR CONSTRAINTS THE SPECIFICATION PUTS ON ``T_k``, AND WHERE EACH IS MET
-----------------------------------------------------------------------------
These are quoted from the specification rather than invented here.

1. §3.2 -- ``T_k`` *"must be built from a summary set under which the components are actually
   separable -- otherwise the test is well-calibrated about a quantity that is not
   identified."*  MET: the rule is built on ``S_B``, the only summary set the specification
   nominates (§5) and the only one that survives both declared family sets.
2. §5 condition 4 -- *"The chosen set's ``T_k`` must be computable from summaries only, since
   the rejection sampler evaluates ``k-hat`` on every replicate and cannot afford anything
   expensive."*  MET: one summary evaluation and one ``K x d`` matrix-vector product.
3. §3.4 -- *"The selection rule ``k-hat(.)`` must be a **fixed, deterministic function of the
   data**, the same one applied to ``y_obs`` and to every replicate. Any data-dependent
   tuning of ``T_k`` (a bandwidth, a normalisation estimated from ``y_obs``) breaks it."*
   MET, and this is the constraint that shapes the whole construction: every constant in the
   rule -- the reference mean, the summary normalisation, the Jacobian, the studentisation
   scale -- is fixed in advance from the BASE specification. Nothing is estimated from the
   data the rule is applied to, and nothing depends on ``theta``.
4. §6 -- ``T_k`` *"must be sensitive to eta_k and insensitive to eta_j, which is a statement
   about the same Jacobian the diagnostic estimates."*  MET exactly, and by construction:
   the rule is the Moore-Penrose pseudo-inverse of that Jacobian, whose defining property
   ``J^+ J = I`` IS "sensitive to eta_k and insensitive to eta_j" written as an equation.

THE RULE
--------
Fix, once, from the base specification:

  * ``m0``, ``sd`` -- the prior-predictive mean and standard deviation of the summary map at
    ``eta = 0`` and the base ``theta``. Recorded in ``results/jacobian_rank.S_B.yaml``, which
    is where these are read from rather than recomputed, so the rule sits in the same
    normalised coordinates as the Jacobian.
  * ``J`` -- the normalised summary Jacobian ``ds/d(eta/ETA_SCALE)`` at the representative
    step size, for a stated component-wise family assignment. Recorded in
    ``results/robustness/k6_spectrum.yaml``.

Then, for observed data ``y``::

    z(y)       = ( s(y) - m0 ) / sd            normalised summary discrepancy, in units of
                                               prior-predictive standard deviations
    eta-hat(y) = J^+ z(y)                      least-squares component attribution, in units
                                               of ETA_SCALE (a 10% relative deformation)
    T_k(y)     = | eta-hat_k(y) | / c_k        the per-component discrepancy statistic
    k-hat(y)   = argmax_k T_k(y)

``eta-hat`` is the **rank-conditioned** step: ``J^+`` exists and is unique for any ``J``, but
it recovers ``eta`` only when ``J`` has full column rank, and the error it makes is amplified
by the condition number. That is precisely the quantity ``results/jacobian_rank.*.yaml``
measures, and it is why the diagnostic was a precondition rather than a side-quest.

THE STUDENTISATION ``c_k``, WHICH IS A REAL CHOICE AND IS REPORTED AS ONE
-------------------------------------------------------------------------
Two variants are implemented, and **both are measured**, because the choice between them
changes ``p_sel`` and therefore the cost:

  ``studentised`` (PRIMARY)  ``c_k = || J^+[k, :] ||_2``
      The standard deviation of ``eta-hat_k`` under the null when ``z`` has identity
      covariance -- so ``T_k`` asks *"how surprising is this component's estimated
      deformation, in units of its own null variability?"*  It is a pure function of ``J``:
      no data, no ``theta``, no Monte Carlo.

  ``plain``                  ``c_k = 1``
      ``T_k`` asks *"which component's estimated relative deformation is largest?"*
      Meaningful because ``ETA_SCALE`` is common across components by construction
      (``src/simulators/sir3.py``), so one unit means the same fractional deformation of
      every component.

**Why ``studentised`` is nominated primary, stated before any ``p_sel`` exists.** The three
components of ``eta-hat`` have unequal null variances, and the inequality is exactly the
conditioning of ``J``: a component the summaries see weakly is estimated noisily. Under
``plain`` the argmax is then dominated by whichever component is estimated worst, so the
rule selects the same component almost regardless of the data -- which is a bad attributor
before it is anything else. Studentising is what an analyst designing this rule would do.

**And the choice is favourable to the cost gate, which is why it is disclosed here rather
than in a footnote.** Equalising the three cells' probabilities raises the smallest of them,
and the cost is ``1 / min p_sel``. That is an argument for measuring both and reporting
both, which is what ``src/diagnostics/p_sel.py`` does; it is not an argument for pretending
the choice was forced.

UNDER WHAT CONDITION DOES THIS RULE MISBEHAVE? (standing constraint S4)
-----------------------------------------------------------------------
``select`` returns a component for every input, so it has no failure flag of its own and
cannot be vacuous in that sense. What it *can* be is wrong, in two ways worth naming:

  * **If ``J`` is rank-deficient**, ``J^+`` silently returns the minimum-norm solution and
    the attribution is a statement about an equivalence class rather than a component. The
    constructor therefore refuses to build a rule from a Jacobian that fails the
    pre-registered rank and condition-number criteria of ``docs/THRESHOLDS.md`` §1.3, rather
    than building one that looks fine and answers a question the data cannot.
  * **If the distortion is large**, the linearisation ``s(y) - m0 ~ J eta`` is a poor model
    and ``eta-hat`` is biased. The rule is still a fixed function of the data and still
    defines a valid selection event -- validity does not depend on the linearisation being
    good -- but its *power* does. Nothing here claims otherwise.

LEAKAGE (``src/attribution/README.md``, hard constraint)
---------------------------------------------------------
:meth:`AttributionRule.select` takes a summary vector and nothing else. It has no argument,
global, filename or side channel by which the identity of a knocked-off component could
reach it, and ``tests/test_selection.py`` asserts that the rule's output is unchanged by any
information other than the summary vector itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Sequence

import numpy as np

__all__ = ["Variant", "VARIANTS", "AttributionRule", "build_rule"]

Variant = Literal["studentised", "plain"]

#: The two studentisation variants, primary first. Both are measured; see the module docstring.
VARIANTS: tuple[Variant, Variant] = ("studentised", "plain")


@dataclass(frozen=True)
class AttributionRule:
    """A fixed, deterministic selection rule ``k-hat`` over the ``K`` components.

    Every field is a constant fixed from the base specification before any datum is seen.
    Nothing here is estimated from the data the rule is applied to (specification §3.4).
    """

    summary_set: str
    family_code: str
    variant: Variant
    m0: np.ndarray            # (d,) prior-predictive mean at eta = 0, base theta
    sd: np.ndarray            # (d,) prior-predictive standard deviation, same point
    J: np.ndarray             # (d, K) normalised Jacobian at the representative step size
    Jplus: np.ndarray         # (K, d) Moore-Penrose pseudo-inverse of J
    scale: np.ndarray         # (K,) the studentisation constants c_k
    component_labels: tuple[str, ...]

    @property
    def K(self) -> int:
        return int(self.J.shape[1])

    def eta_hat(self, summary: Sequence[float]) -> np.ndarray:
        """Least-squares component attribution, in units of ``ETA_SCALE``."""
        s = np.asarray(summary, dtype=float)
        if s.shape != self.m0.shape:
            raise ValueError(f"summary has shape {s.shape}, expected {self.m0.shape}")
        return self.Jplus @ ((s - self.m0) / self.sd)

    def t_statistics(self, summary: Sequence[float]) -> np.ndarray:
        """``T_k`` for every component. Takes the summary vector and nothing else."""
        return np.abs(self.eta_hat(summary)) / self.scale

    def select(self, summary: Sequence[float]) -> int:
        """``k-hat`` -- the selected component index.

        Ties are broken toward the lower index by :func:`numpy.argmax`. Specification §2.2
        notes that Dufour's Proposition 4.1 assumes ties have zero probability and that
        Proposition 4.2 is the one to cite otherwise; for an argmax over three continuous
        statistics a tie has probability zero, and :func:`tie_fraction` below is how that is
        checked on real draws rather than asserted.
        """
        return int(np.argmax(self.t_statistics(summary)))

    def select_many(self, summaries: np.ndarray) -> np.ndarray:
        """Vectorised :meth:`select` over an ``(n, d)`` block of summary vectors."""
        s = np.asarray(summaries, dtype=float)
        z = (s - self.m0) / self.sd
        t = np.abs(z @ self.Jplus.T) / self.scale
        return np.argmax(t, axis=1)

    def tie_fraction(self, summaries: np.ndarray) -> float:
        """Fraction of rows whose top two ``T_k`` are equal to floating point.

        Reported rather than assumed, because "ties have zero probability" is an assumption
        Dufour's Proposition 4.1 needs and this project has a habit of checking those.
        """
        s = np.asarray(summaries, dtype=float)
        z = (s - self.m0) / self.sd
        t = np.abs(z @ self.Jplus.T) / self.scale
        srt = np.sort(t, axis=1)
        return float(np.mean(srt[:, -1] == srt[:, -2]))


def build_rule(
    *,
    summary_set: str,
    family_code: str,
    variant: Variant,
    m0: Sequence[float],
    sd: Sequence[float],
    J: np.ndarray,
    component_labels: Sequence[str],
    tau: float,
    kappa_max: float,
) -> AttributionRule:
    """Construct a rule, refusing to build one on a Jacobian that fails the rank criteria.

    ``tau`` and ``kappa_max`` are the pre-registered pair of ``docs/THRESHOLDS.md`` §1.3 and
    are passed in rather than imported so that this module states no threshold of its own.

    **Under what condition does this refuse?** When the numerical rank of ``J`` at ``tau`` is
    less than ``K``, or when its condition number exceeds ``kappa_max``. Both are reachable:
    ``S_C`` fails the first by construction (``d = 2 < K``) and ``S_A`` under the adversarial
    families fails at ``kappa = 136.7``. ``tests/test_selection.py`` builds a rule from each
    and requires the refusal.
    """
    Jm = np.asarray(J, dtype=float)
    d, K = Jm.shape
    sv = np.linalg.svd(Jm, compute_uv=False)
    sv_full = np.zeros(K)
    sv_full[: len(sv)] = sv
    rank = int(np.sum(sv_full >= tau * sv_full[0])) if sv_full[0] > 0 else 0
    kappa = float(sv_full[0] / sv_full[-1]) if sv_full[-1] > 0 else float("inf")
    if rank < K or kappa > kappa_max:
        raise ValueError(
            f"refusing to build a selection rule on {summary_set}/{family_code}: "
            f"rank {rank}/{K} at tau={tau}, kappa={kappa:.4g} against ceiling {kappa_max}. "
            f"A pseudo-inverse of a rank-deficient Jacobian returns the minimum-norm "
            f"solution and would attribute to a component the data cannot separate."
        )
    Jplus = np.linalg.pinv(Jm)
    if variant == "studentised":
        scale = np.linalg.norm(Jplus, axis=1)
    elif variant == "plain":
        scale = np.ones(K)
    else:
        raise ValueError(f"unknown variant {variant!r}")
    return AttributionRule(
        summary_set=summary_set,
        family_code=family_code,
        variant=variant,
        m0=np.asarray(m0, dtype=float),
        sd=np.asarray(sd, dtype=float),
        J=Jm,
        Jplus=Jplus,
        scale=np.asarray(scale, dtype=float),
        component_labels=tuple(component_labels),
    )
