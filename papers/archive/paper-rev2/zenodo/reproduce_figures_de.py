"""Regenerate figures D and E of the Wow! forensic-bounds paper.

Figure D: emulator likelihood surface in (ln T, ln lambda) with the pooled
192-hr follow-up non-detection factor.
Figure E: emulator maximum likelihood versus event-count truncation kmax,
with the maxima recomputed from the released published chains (OSU+Hobart:
3.27%, ALL: 1.78%) as reference lines.

Terminology: the plotted quantity is the maximum likelihood of the
stochastic-repeater parameter likelihood, not a posterior probability.
"""
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[4]
WOW = ROOT / "data" / "kipping_master_dl" / "wow-main"
FIGDIR = ROOT / "papers" / "archive" / "paper-rev2" / "figures"


def get_dates():
    return np.array([
        0.5, 1.5, 2.5, 4.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5,
        42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 52.5, 78.5, 240.5,
        241.5, 247.5, 254.5, 255.5, 256.5, 257.5, 258.5, 261.5, 262.5,
        380.5, 381.5, 382.5, 383.5, 384.5, 385.5, 386.5, 387.5, 1968.5,
        1969.5, 1970.5, 1973.5, 1979.5, 1981.5, 1988.25, 1988.75, 1989.5,
        1990.5, 1991.5, 1994.5, 1995.5, 1999.25, 1999.75, 2001.5, 2002.5,
        2003.5, 2004.5, 2009.5, 2011.5, 2012.5, 2013.5, 2014.5, 2015.5,
        2016.5, 2017.5, 2018.5, 2019.5, 2020.5, 2021.5, 2022.5, 2023.5,
        2024.5, 2025.5, 2026.5, 2032.5, 2033.5, 2034.5, 2037.5, 2038.5,
        2039.5, 2045.5, 2046.5, 2048.5, 2051.5, 2053.5, 2054.5, 2082.5,
        2095.5, 2672.5,
    ])


dates = get_dates()
BASELINE = dates[-1] - dates[0] + 1.0


def prob_single(T_s):
    tau = 72.0 / 86400.0
    offset = 172.37 / 86400.0
    if T_s < 72.0:
        return 0.0, 0.0
    W = T_s / 86400.0 - tau
    if W <= offset:
        len_1, len_3 = W, 0.0
    else:
        len_1, len_3 = offset, W - offset
    p_wow = (2.0 * len_1) * len(dates) / BASELINE
    p_any = (2.0 * len_1 + len_3) * len(dates) / BASELINE
    return p_wow, p_any


def likelihood_exact(T_s, lam, followup_days=8.0):
    """Exact Poisson emulator: exactly one Wow-like hit day, zero others."""
    if T_s < 72.0:
        return 0.0
    p_wow, p_any = prob_single(T_s)
    mu = lam * BASELINE
    mu_wow = mu * p_wow
    mu_other = mu * (p_any - p_wow)
    return mu_wow * math.exp(-mu_wow) * math.exp(-mu_other) \
        * math.exp(-lam * followup_days)


def likelihood_kmax(T_s, lam, kmax=100, followup_days=8.0):
    if T_s < 72.0:
        return 0.0
    p_wow, p_any = prob_single(T_s)
    mu = lam * BASELINE
    total = 0.0
    for k in range(1, kmax + 1):
        prob_k = k * p_wow * (1.0 - p_any) ** (k - 1)
        log_p = -mu + k * math.log(mu) - math.lgamma(k + 1.0)
        total += prob_k * math.exp(log_p)
    return total * math.exp(-lam * followup_days)


def chain_max_pct(name):
    d = np.loadtxt(WOW / f"mcmc_chain_thinner_{name}.dat", skiprows=3)
    return float(np.exp(d[:, 2].max()) * 100.0)

def generate_figure_d():
    NG = 60
    T_grid = np.logspace(np.log10(72.0), np.log10(math.exp(-1) * 86400), NG)
    L_grid = np.logspace(np.log10(math.exp(-4)), np.log10(math.exp(2)), NG)
    X, Y = np.meshgrid(T_grid, L_grid)
    Z = np.zeros_like(X)
    for i in range(NG):
        for j in range(NG):
            Z[i, j] = likelihood_exact(X[i, j], Y[i, j]) * 100

    fig, ax = plt.subplots(figsize=(8, 6))
    cp = ax.contourf(np.log(X), np.log(Y), Z, levels=20, cmap="viridis")
    cbar = fig.colorbar(cp)
    cbar.set_label("Maximum likelihood (%)")
    ax.set_xlabel(r"$\ln(T)$ (Event Duration in seconds)")
    ax.set_ylabel(r"$\ln(\lambda)$ (Event Rate in day$^{-1}$)")
    max_idx = np.unravel_index(np.argmax(Z, axis=None), Z.shape)
    ax.plot(np.log(X[max_idx]), np.log(Y[max_idx]), "rx", markersize=10,
            label=f"Maximum ({Z[max_idx]:.2f}%)")
    ax.legend()
    plt.savefig(FIGDIR / "figD_h5_likelihood.pdf", bbox_inches="tight")
    plt.close()
    print(f"figD: emulator maximum likelihood = {Z[max_idx]:.2f}%")


def generate_figure_e():
    kmax_list = [10, 50, 100, 200, 300, 400, 500, 1000]
    T_grid = np.logspace(np.log10(72.0), np.log10(math.exp(-1) * 86400), 40)
    L_grid = np.logspace(np.log10(math.exp(-4)), np.log10(math.exp(2)), 40)
    maxima = []
    for km in kmax_list:
        best = 0.0
        for T in T_grid:
            for L in L_grid:
                v = likelihood_kmax(T, L, kmax=km)
                if v > best:
                    best = v
        maxima.append(best * 100)
        print(f"  kmax={km}: {best * 100:.2f}%")

    all_pct = chain_max_pct("ALL")
    osuh_pct = chain_max_pct("OSUHobart")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(kmax_list, maxima, "bo-", lw=2,
            label="Independent analytic emulator")
    ax.axhline(all_pct, color="r", linestyle="--",
               label=f"Published chain, ALL constraints ({all_pct:.2f}%)")
    ax.axhline(osuh_pct, color="darkorange", linestyle="-.",
               label=f"Published chain, OSU+Hobart ({osuh_pct:.2f}%)")
    ax.set_xscale("log")
    ax.set_xlabel(r"Truncation parameter $k_{\rm max}$")
    ax.set_ylabel("Emulator maximum likelihood (%)")
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.5)
    plt.savefig(FIGDIR / "figE_h5_convergence.pdf", bbox_inches="tight")
    plt.close()
    print(f"figE: chain maxima OSU+Hobart={osuh_pct:.2f}%, ALL={all_pct:.2f}%")


if __name__ == "__main__":
    FIGDIR.mkdir(parents=True, exist_ok=True)
    generate_figure_d()
    generate_figure_e()
    print("Done.")

