"""Is the count-observation CRN failure a genuine degeneracy, or an artefact of the sampler?

WHAT IS BEING TESTED
--------------------
`audit/S3_REPORT.md` §4.1 and every results file assert:

  *"Under common random numbers a count-valued observation layer (Poisson, negative binomial)
  is a STEP function of eta: the difference quotient is either exactly 0 or O(1/h) and no
  derivative exists at any h ... shrinking h makes the first case more likely, so the
  estimator converges confidently to zero."*

Those are two different claims with different consequences. **A genuine degeneracy** is a real
and citable property of common random numbers with a discrete output. **A numerical artefact
of NumPy's Poisson sampler** would be a bug. This script separates them, and it separates them
by construction rather than by argument, using three couplings of the SAME deterministic mean:

  * ``lognormal``  -- the continuous multiplicative layer the diagnostic actually uses;
  * ``poisson_numpy`` -- exactly what ``sir3.simulate(noise_model="poisson")`` does;
  * ``poisson_inversion`` -- the count layer under the *best possible* coupling,
    ``y = F^{-1}_lambda(u)`` with the uniform ``u`` frozen by the seed and independent of
    ``lambda``. This is the monotone coupling; NumPy's does not use it for ``lambda >= 10``,
    where it switches to transformed rejection and the number of uniforms consumed depends on
    ``lambda`` itself.

**If the failure is a sampler artefact, the inversion coupling repairs it. If the failure is
the discreteness, the inversion coupling fails too — differing only in how badly.** That is the
discriminator, and it is why the third coupling exists.

WHY THE TEST STATISTIC IS ``final_size``
----------------------------------------
``final_size = sum_t y_t`` is LINEAR in the observed series, so ``E[s(y)] = s(E[y]) = s(mu)``
exactly. The quantity the estimator is supposed to recover is therefore available in closed
form as the difference quotient of the deterministic mean, with no Monte Carlo error at all. A
nonlinear summary would leave the reference itself uncertain and the comparison would prove
nothing.

WHY THIS IS CHEAP
-----------------
The deterministic mean ``mu(eta)`` is computed ONCE per step size — two simulator runs — and
every replicate then applies its own noise to those same two vectors. That is not only fast; it
isolates the observation layer exactly, holding the deterministic core fixed, which is what the
claim is about.

    python -m src.diagnostics.crn_count_check
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import yaml
from scipy.stats import poisson as poisson_dist

from ..provenance import header, now_iso
from ..simulators.sir3 import BASE, ETA_SCALE, K, simulate
from .jacobian_rank import H_VALUES

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "results" / "robustness"

SEED0 = 20260820
R_SMALL = 128       # the replicate count the reported diagnostic actually used
R_LARGE = 20_000    # enough to see whether the estimator is unbiased despite the variance
COMPONENT = 0       # transmission; the claim is about the observation LAYER, not the family


def _apply(kind: str, mu: np.ndarray, seed: int, sigma: float) -> np.ndarray:
    """One noise realisation on a given mean vector, under the named coupling."""
    if kind == "lognormal":
        z = np.random.default_rng(seed).standard_normal(mu.size)
        return mu * np.exp(sigma * z - 0.5 * sigma * sigma)
    if kind == "poisson_numpy":
        return np.random.default_rng(seed).poisson(np.maximum(mu, 0.0)).astype(float)
    if kind == "poisson_inversion":
        u = np.random.default_rng(seed).random(mu.size)
        return poisson_dist.ppf(u, np.maximum(mu, 0.0)).astype(float)
    raise ValueError(kind)


def _pathwise_step_census(h_native: float, n_points: int = 4001) -> dict[str, Any]:
    """Walk eta finely at ONE fixed seed and count how the pathwise map actually behaves.

    This is the claim "eta |-> y(eta; omega) is a step function" checked directly, rather than
    inferred from a difference quotient. The mean is smooth by construction; the question is
    what the coupling does to it.
    """
    etas = np.linspace(-h_native, h_native, n_points)
    mus = []
    for e in etas:
        eta = np.zeros(K)
        eta[COMPONENT] = e
        mus.append(simulate(eta, seed=SEED0, stochastic=False).reported)
    mus = np.asarray(mus)
    out: dict[str, Any] = {"eta_range": [float(-h_native), float(h_native)],
                           "n_points": int(n_points)}
    for kind in ("lognormal", "poisson_numpy", "poisson_inversion"):
        vals = np.array([float(_apply(kind, m, SEED0, BASE.obs_sigma).sum()) for m in mus])
        diffs = np.diff(vals)
        out[kind] = {
            "n_distinct_values": int(np.unique(vals).size),
            "n_points": int(n_points),
            "fraction_of_adjacent_pairs_exactly_equal": float(np.mean(diffs == 0.0)),
            "n_jumps": int(np.count_nonzero(diffs)),
            "largest_jump": float(np.abs(diffs).max()),
            "total_variation": float(np.abs(diffs).sum()),
            "endpoint_change": float(vals[-1] - vals[0]),
        }
    return out


def main() -> int:
    started = now_iso()
    sigma = BASE.obs_sigma

    print("pathwise step census at one fixed seed ...")
    census = _pathwise_step_census(h_native=1e-1 * ETA_SCALE)
    for kind in ("lognormal", "poisson_numpy", "poisson_inversion"):
        c = census[kind]
        print(f"  {kind:<18s} distinct values {c['n_distinct_values']:>6d}/{c['n_points']}, "
              f"jumps {c['n_jumps']}, flat fraction {c['fraction_of_adjacent_pairs_exactly_equal']:.4f}")

    print("\ndifference quotients across the pre-registered h sweep ...")
    rows = []
    for h in H_VALUES:
        step = h * ETA_SCALE
        ep, em = np.zeros(K), np.zeros(K)
        ep[COMPONENT], em[COMPONENT] = step, -step
        mu_p = simulate(ep, seed=SEED0, stochastic=False).reported
        mu_m = simulate(em, seed=SEED0, stochastic=False).reported
        # The reference: exact, because final_size is linear so E[s(y)] = s(mu).
        truth = float((mu_p.sum() - mu_m.sum()) / (2 * h))

        row: dict[str, Any] = {"h": float(h), "exact_derivative_of_the_mean": truth}
        for kind in ("lognormal", "poisson_numpy", "poisson_inversion"):
            dq = np.array([
                (_apply(kind, mu_p, SEED0 + r, sigma).sum()
                 - _apply(kind, mu_m, SEED0 + r, sigma).sum()) / (2 * h)
                for r in range(R_LARGE)
            ])
            small = dq[:R_SMALL]
            row[kind] = {
                "mean_over_R_large": float(dq.mean()),
                "relative_bias_over_R_large": float((dq.mean() - truth) / truth) if truth else None,
                "sd_of_one_replicate": float(dq.std(ddof=1)),
                "se_of_the_mean_over_R_small": float(dq.std(ddof=1) / np.sqrt(R_SMALL)),
                "fraction_of_replicates_exactly_zero": float(np.mean(dq == 0.0)),
                "estimate_at_R_small": float(small.mean()),
                "relative_error_at_R_small": float((small.mean() - truth) / truth) if truth else None,
                "sample_sd_at_R_small_is_exactly_zero": bool(small.std(ddof=1) == 0.0),
            }
        rows.append(row)
        print(f"  h={h:<8g} truth={truth:12.6g} | " + " | ".join(
            f"{k.split('_')[0][:4]}: est {row[k]['estimate_at_R_small']:.4g}, "
            f"zero-frac {row[k]['fraction_of_replicates_exactly_zero']:.3f}"
            for k in ("lognormal", "poisson_numpy", "poisson_inversion")))

    doc: dict[str, Any] = {
        "provenance": header(script="src/diagnostics/crn_count_check.py",
                             command="python -m src.diagnostics.crn_count_check",
                             seed=SEED0, started=started),
        "what_this_is": (
            "Session G4 adversarial pass, finding 3. Tests whether the count-observation CRN "
            "failure reported in audit/S3_REPORT.md §4.1 is a genuine degeneracy of common "
            "random numbers with a discrete output, or an artefact of NumPy's Poisson sampler. "
            "Does not modify anything in results/. See audit/G3_ADVERSARIAL_REVIEW.md."
        ),
        "test_statistic": (
            "final_size = sum_t y_t. Chosen because it is LINEAR, so E[s(y)] = s(mu) exactly "
            "and the target derivative is available in closed form from the deterministic mean "
            "with no Monte Carlo error."
        ),
        "the_discriminator": (
            "poisson_inversion is the count layer under the MONOTONE coupling y = F^{-1}_lambda(u) "
            "with u frozen by the seed. If the failure were an artefact of NumPy's sampler -- "
            "which uses transformed rejection for lambda >= 10, so the number of uniforms it "
            "consumes depends on lambda -- the inversion coupling would repair it. If the "
            "failure is the discreteness of the output, inversion fails too."
        ),
        "settings": {"seed0": SEED0, "R_small": R_SMALL, "R_large": R_LARGE,
                     "component_perturbed": COMPONENT, "eta_scale": ETA_SCALE,
                     "obs_sigma": sigma, "h_values": list(H_VALUES)},
        "pathwise_step_census": census,
        "difference_quotients": rows,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "crn_count_check.yaml"
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, default_flow_style=False, width=100)
    print(f"\nwrote {path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
