"""Reproduce the headline numbers of the Wow! forensic-bounds paper.

Verified inputs (frozen):
  * data/kipping_master_dl/wow-main/  -- public release of Kipping & Gray
    (2022, MNRAS 515, 1122): wow.f90, output_grid.dat, and three thinned
    MCMC chains (OSU / OSUHobart / ALL).
  * research/sources/ellingsen_hobart/extracted/campaign_exposure.csv --
    frozen 2010-2014 Hobart session exposure table.

Outputs: console report (main_numbers.json) + selection-function
demonstration figure (figF_hobart_selection.pdf).
"""
import csv
import json
import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[4]
WOW = ROOT / "data" / "kipping_master_dl" / "wow-main"
EXPOSURE_CSV = (ROOT / "research" / "sources" / "ellingsen_hobart" /
                "extracted" / "campaign_exposure.csv")
FIGDIR = ROOT / "papers" / "archive" / "paper-rev2" / "figures"

report = {}

# ----------------------------------------------------------------------
# 1. H3 brightness temperature: nominal and 1-sigma-propagated bound
# ----------------------------------------------------------------------
c = 299792458.0
k_B = 1.380649e-23
nu = 1420.726e6


def tb(S_jy, theta_arcmin):
    """Brightness temperature for a uniform disk of angular diameter theta."""
    theta_rad = theta_arcmin * (math.pi / 180.0) / 60.0
    Omega = math.pi * (theta_rad / 2.0) ** 2
    return (S_jy * 1e-26) * c ** 2 / (2.0 * k_B * nu ** 2 * Omega)


report["H3"] = {
    "Omega_max_sr": math.pi * (1.9 * math.pi / 10800.0 / 2.0) ** 2,
    "TB_nominal_K": tb(256.0, 1.9),
    "TB_1sigma_propagated_K": tb(256.0 - 63.0, 1.9 + 0.1),
}

# ----------------------------------------------------------------------
# 2. H4 conditional EIRP requirement
# ----------------------------------------------------------------------
S_jy = 256.0
PC = 3.0856775814913673e16


def eirp_W(d_pc, dnu_hz, s_jy=S_jy):
    return 4.0 * math.pi * (d_pc * PC) ** 2 * (s_jy * 1e-26) * dnu_hz


report["H4"] = {
    "EIRP_1pc_10kHz_W": eirp_W(1.0, 1e4),
    "EIRP_100AU_10kHz_W": eirp_W(100.0 / 206264.806, 1e4),
    "EIRP_1.3pc_10kHz_W": eirp_W(1.3, 1e4),
    "EIRP_10pc_10kHz_W": eirp_W(10.0, 1e4),
    "EIRP_100pc_10kHz_W": eirp_W(100.0, 1e4),
    "EIRP_1kpc_10kHz_W": eirp_W(1000.0, 1e4),
}

# ----------------------------------------------------------------------
# 3. H5 published implementation: chain maxima from the released files
# ----------------------------------------------------------------------
chains = {}
for name in ("OSU", "OSUHobart", "ALL"):
    d = np.loadtxt(WOW / f"mcmc_chain_thinner_{name}.dat", skiprows=3)
    i = int(np.argmax(d[:, 2]))
    chains[name] = {
        "n_samples": len(d),
        "max_logL": float(d[i, 2]),
        "max_likelihood_pct": float(np.exp(d[i, 2]) * 100.0),
        "lnT": float(d[i, 0]), "lnlam": float(d[i, 1]),
    }
report["H5_published_chains"] = chains

# ----------------------------------------------------------------------
# 4. Hobart 2010-2014 frozen exposure (session spans)
# ----------------------------------------------------------------------
spans = []
with open(EXPOSURE_CSV, newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        if row["campaign"] in ("2010_followup", "2013_followup",
                               "2013_tests", "2014_followup"):
            spans.append(float(row["usable_duration"].split("_")[0]))
T_HOBART_H = sum(spans)
T_HOBART_DAYS = T_HOBART_H / 24.0
report["Hobart_2010_2014"] = {
    "n_sessions": len(spans), "total_span_hours": T_HOBART_H,
    "total_span_days": T_HOBART_DAYS,
}

# ----------------------------------------------------------------------
# 5. H5 independent emulator (frozen project implementation)
# ----------------------------------------------------------------------
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
BASELINE = dates[-1] - dates[0] + 1.0  # 2673 days


def prob_single(T_s):
    """Per-event Wow-like-hit and any-hit probabilities (K&G geometry)."""
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


def likelihood_finitesum(T_s, lam, kmax=500, followup_days=0.0):
    """Analytic finite-sum emulator. Conditioning: exactly one Wow-like hit
    day and zero other recognizable events; optionally multiplied by an
    exponential follow-up non-detection factor exp(-lambda*T_follow)."""
    if T_s < 72.0:
        return 0.0
    p_wow, p_any = prob_single(T_s)
    mu = lam * BASELINE
    total = 0.0
    for k in range(1, kmax + 1):
        prob_k = k * p_wow * (1.0 - p_any) ** (k - 1)
        log_p = -mu + k * math.log(mu) - math.lgamma(k + 1.0)
        total += prob_k * math.exp(log_p)
    if followup_days > 0.0:
        total *= math.exp(-lam * followup_days)
    return total


# Grid identical to the published implementation (wow.f90)
NG = 60
T_grid = np.logspace(np.log10(72.0), np.log10(math.exp(-1.0) * 86400.0), NG)
L_grid = np.logspace(np.log10(math.exp(-4.0)), np.log10(math.exp(2.0)), NG)


def map_of(followup_days, kmax=500):
    best_v, best_T, best_L = 0.0, None, None
    for T in T_grid:
        for L in L_grid:
            v = likelihood_finitesum(T, L, kmax=kmax,
                                     followup_days=followup_days)
            if v > best_v:
                best_v, best_T, best_L = v, T, L
    return best_v, best_T, best_L


# a) OSU 1977 data only (no follow-up constraint)
v_osu, T_osu, L_osu = map_of(0.0)
# b) + 2010-14 Hobart as a transparent null (full exposure as effective null)
v_trans, T_trans, L_trans = map_of(T_HOBART_DAYS)
report["H5_selection_demo"] = {
    "MAP_OSU_only_pct": v_osu * 100, "T_s": T_osu, "lam_day": L_osu,
    "MAP_transparent_pct": v_trans * 100, "T_s_trans": T_trans,
    "lam_day_trans": L_trans,
    "update_ratio_at_MAP": math.exp(-L_osu * T_HOBART_DAYS),
}

# kmax sweep for the convergence figure (with the pooled 192-hr penalty)
penalty_days = 192.0 / 24.0
sweep = {}
for km in (10, 50, 100, 200, 300, 400, 500, 1000):
    best = 0.0
    for T in T_grid:
        for L in L_grid:
            best = max(best, likelihood_finitesum(
                T, L, kmax=km, followup_days=penalty_days))
    sweep[km] = best * 100.0
report["H5_kmax_sweep_pooled_penalty_pct"] = sweep

# Untruncated Monte Carlo variant of the same likelihood.
# Samples k ~ Poisson(mu); the estimator averages k*pw*(1-pa)^(k-1),
# whose expectation over the Poisson distribution equals the finite sum.
rng = np.random.default_rng(20260919)
v_mc, T_mc, L_mc = 0.0, None, None
for T in T_grid:
    pw, pa = prob_single(T)
    for L in L_grid:
        mu = L * BASELINE
        k = rng.poisson(mu, size=2000).astype(float)
        log_terms = (np.log(k, out=np.full_like(k, -np.inf), where=(k > 0))
                     + math.log(pw) + (k - 1.0) * math.log1p(-pa))
        v = float(np.mean(np.exp(log_terms))) * math.exp(-L * penalty_days)
        if v > v_mc:
            v_mc, T_mc, L_mc = v, T, L
report["H5_monte_carlo_pct"] = v_mc * 100

# Evidence (likelihood integrated over the flat lnT, lnlambda grid prior):
# how much the 2010-14 exposure updates the H5 evidence under each of the
# two plausible selection functions.
lnt = np.log(T_grid)
lnl = np.log(L_grid)
Z_osu = 0.0
Z_trans = 0.0
for T in T_grid:
    for L in L_grid:
        base = likelihood_finitesum(T, L, kmax=500, followup_days=0.0)
        Z_osu += base
        Z_trans += base * math.exp(-L * T_HOBART_DAYS)
report["H5_selection_demo"]["evidence_osu_only"] = Z_osu
report["H5_selection_demo"]["evidence_transparent"] = Z_trans
report["H5_selection_demo"]["evidence_update_ratio"] = Z_trans / Z_osu


# ----------------------------------------------------------------------
# 6. Selection-function demonstration figure (figF)
# ----------------------------------------------------------------------
FIGDIR.mkdir(parents=True, exist_ok=True)
lam = np.logspace(math.log10(math.exp(-4.0)), math.log10(math.exp(2.0)), 400)
ratio = np.exp(-lam * T_HOBART_DAYS)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(lam, ratio, "b-", lw=2,
        label=r"Transparent/opaque likelihood ratio $L_{\rm S1}/L_{\rm S2}=e^{-\lambda T_{\rm H}}$")
ax.axvline(L_osu, color="purple", ls=":", lw=2,
           label="OSU-only max-likelihood rate "
                 r"$\lambda^\ast$ = " + f"{L_osu:.2f} " + r"day$^{-1}$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel(r"$\lambda$ (day$^{-1}$)")
ax.set_ylabel(r"Likelihood-update ratio  $L_{\rm S1}(\lambda)/L_{\rm S2}(\lambda)$")
ax.grid(True, alpha=0.4)
ax.legend(loc="best")
plt.savefig(FIGDIR / "figF_hobart_selection.pdf", bbox_inches="tight")
plt.close()

# ----------------------------------------------------------------------
out = ROOT / "papers" / "archive" / "paper-rev2" / "scripts" / "main_numbers.json"
with open(out, "w", encoding="utf-8") as fh:
    json.dump(report, fh, indent=2, default=str)

print(json.dumps(report, indent=2, default=str))



