#!/usr/bin/env python3
"""Deterministic source audit of Kipping & Gray's released waiting-count estimator.

This does not compile wow.f90 and does not claim to reproduce its unseeded
realizations or MCMC chains. It combines literal-source parsing, the exact
finite-baseline probability already implemented in the independent H5 audit,
and exact expectations for the source's capped geometric waiting-count rule.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
_repo_source = ROOT / "data/kipping_master_dl/wow-main"
_packaged_source = HERE / "reference_source"
SOURCE_DIR = _repo_source if (_repo_source / "wow.f90").is_file() else _packaged_source
SOURCE = SOURCE_DIR / "wow.f90"
GRID = SOURCE_DIR / "output_grid.dat"
NOTEBOOK = SOURCE_DIR / "mcmc.nb"
OUT = ROOT / "results/h5_estimator_audit.json" if (ROOT / "results").is_dir() else HERE / "h5_estimator_audit.json"
_repo_crosscheck = ROOT / "publication/IJA/overleaf_upload_2026-11-16/h5_revised/reproducibility/h5_numerical_crosscheck.json"
_packaged_crosscheck = HERE / "h5_numerical_crosscheck.json"
INDEPENDENT_RESULT = _repo_crosscheck if _repo_crosscheck.is_file() else _packaged_crosscheck
BASELINE_DAYS = 2673.0
WINDOW_DAY = 72.0 / 86400.0


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def interval_partition(intervals: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
    """Finite event-center union and exclusive lengths on [0, baseline]."""
    arr = np.asarray(intervals, float).copy()
    arr[:, 0] = np.maximum(arr[:, 0], 0.0)
    arr[:, 1] = np.minimum(arr[:, 1], BASELINE_DAYS)
    arr[:, 1] = np.maximum(arr[:, 1], arr[:, 0])
    cuts = np.unique(arr.ravel())
    exclusive = np.zeros(len(arr)); union = 0.0
    for a, b in zip(cuts[:-1], cuts[1:]):
        if b <= a: continue
        active = np.flatnonzero((arr[:, 0] < (a+b)/2) & ((a+b)/2 < arr[:, 1]))
        if active.size:
            union += b-a
            if active.size == 1: exclusive[active[0]] += b-a
    return union, exclusive, arr


def code_probability(rate: float, duration: float, gap_s: float,
                     days: np.ndarray) -> float:
    """Exact probability under the source's finite PP and first overshoot."""
    centers = np.r_[days, days+gap_s/86400.0]
    half = (duration-WINDOW_DAY)/2
    intervals = np.column_stack((centers-half, centers+half))
    union, exclusive, clipped = interval_partition(intervals)
    q0 = float(np.sum(np.exp(-rate*(union-exclusive)) *
                      (-np.expm1(-rate*exclusive))))
    future = np.column_stack((np.maximum(intervals[:, 0], BASELINE_DAYS), intervals[:, 1]))
    future[:, 1] = np.maximum(future[:, 1], future[:, 0])
    points = np.unique(np.r_[BASELINE_DAYS, future.ravel()])
    q = 0.0
    for a, b in zip(points[:-1], points[1:]):
        if b <= a: continue
        mid = (a+b)/2
        ids = np.flatnonzero((future[:, 0] < mid) & (mid < future[:, 1]))
        mass = math.exp(-rate*(a-BASELINE_DAYS))-math.exp(-rate*(b-BASELINE_DAYS))
        if ids.size == 0: q += mass*q0
        elif ids.size == 1: q += mass*math.exp(-rate*(union-exclusive[ids[0]]))
    q += math.exp(-rate*(float(points[-1])-BASELINE_DAYS))*q0
    return q


def extract_float(pattern: str, text: str, label: str) -> float:
    match = re.search(pattern, text, re.I)
    if not match:
        raise RuntimeError(f"Could not read {label} from wow.f90")
    return float(match.group(1).replace("D", "E").replace("d", "e"))


def exact_grid(k1max: int, k2max: int, denominator: int,
               tmin: float, tmax: float, lmin: float, lmax: float,
               gap_s: float, days: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    ts = np.exp(np.log(tmin) + np.arange(k1max) * (np.log(tmax)-np.log(tmin))/denominator)
    rates = np.exp(np.log(lmin) + np.arange(k2max) * (np.log(lmax)-np.log(lmin))/denominator)
    surface = np.empty((k1max, k2max), float)
    for i, duration in enumerate(ts):
        half = (duration - WINDOW_DAY) / 2
        centers = np.r_[days, days+gap_s/86400.0]
        intervals = np.column_stack((centers-half, centers+half))
        union, exclusive, clipped = interval_partition(intervals)
        base = np.exp(-rates[:, None]*(union-exclusive[None, :])) * (-np.expm1(-rates[:, None]*exclusive[None, :]))
        q0 = base.sum(axis=1)
        future = np.column_stack((np.maximum(intervals[:, 0], BASELINE_DAYS), intervals[:, 1]))
        future[:, 1] = np.maximum(future[:, 1], future[:, 0])
        cuts = np.unique(np.r_[BASELINE_DAYS, future.ravel()])
        q = np.zeros_like(rates)
        for a, b in zip(cuts[:-1], cuts[1:]):
            if b <= a: continue
            mid = (a+b)/2
            ids = np.flatnonzero((future[:, 0] < mid) & (mid < future[:, 1]))
            mass = np.exp(-rates*(a-BASELINE_DAYS))-np.exp(-rates*(b-BASELINE_DAYS))
            if ids.size == 0: q += mass*q0
            elif ids.size == 1: q += mass*np.exp(-rates*(union-exclusive[ids[0]]))
        q += np.exp(-rates*(float(cuts[-1])-BASELINE_DAYS))*q0
        surface[i] = q
    return ts, rates, surface


def capped_wait_map(p: np.ndarray, cap: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Limit of the source MAP estimator with censored geometric counts.

    For G~Geometric(p) on {1,2,...}, E[min(G,C)]=(1-(1-p)^C)/p.
    wow.f90 reports n/(n+sum C), with n independent waiting-loop outcomes.
    The reported asymptotic MAP is therefore 1/(1+E[min(G,C)]).
    """
    p = np.asarray(p, float)
    miss = np.exp(cap * np.log1p(-np.minimum(p, 1 - 1e-16)))
    # Stable p->0 limit for the truncated mean.
    mean_censored = -np.expm1(cap * np.log1p(-np.minimum(p, 1 - 1e-16))) / np.maximum(p, 1e-300)
    mean_censored = np.where(p == 0, float(cap), mean_censored)
    map_capped = 1 / (1 + mean_censored)
    map_uncapped = p / (1 + p)
    return mean_censored, map_capped, map_uncapped


def main() -> None:
    src = SOURCE.read_text(encoding="utf-8")
    tmin = extract_float(r"Tmin\s*=\s*([0-9.eEdD+-]+)", src, "Tmin")
    tmax = extract_float(r"Tmax\s*=\s*([0-9.eEdD+-]+)", src, "Tmax")
    lmin = extract_float(r"Lmin\s*=\s*([0-9.eEdD+-]+)", src, "Lmin")
    lmax = extract_float(r"Lmax\s*=\s*([0-9.eEdD+-]+)", src, "Lmax")
    kmax = int(extract_float(r"kmax\s*=\s*(\d+)", src, "kmax"))
    cap = int(extract_float(r"maxcounts\s*=\s*(\d+)", src, "maxcounts"))
    k1max = int(re.search(r"DO\s+k1=1,(\d+)", src, re.I).group(1))
    k2max = int(re.search(r"DO\s+k2=1,(\d+)", src, re.I).group(1))
    days_block = src.split("days = (/")[1].split("/)")[0]
    days = np.array([float(x) for x in re.findall(r"\d+(?:\.\d+)?", days_block)])
    if len(days) != 90: raise RuntimeError(f"Expected 90 dates; found {len(days)}")

    data = np.loadtxt(GRID, skiprows=7)
    if data.shape != (25600, 7):
        raise RuntimeError(f"Expected 25,600 x 7 output grid, found {data.shape}")
    grid_k1 = data[:, 3].astype(int)
    grid_k2 = data[:, 4].astype(int)
    first = data[0]
    natural_log_matches = math.isclose(first[0], math.log(tmin), abs_tol=1e-5) and math.isclose(first[1], math.log(lmin), abs_tol=1e-10)
    base10_matches = math.isclose(first[0], math.log10(tmin), abs_tol=1e-5) and math.isclose(first[1], math.log10(lmin), abs_tol=1e-5)
    output_grid_max = int(np.argmax(data[:, 2]))
    max_row = data[output_grid_max]

    # The source simulates when this inequality is true and uses fixed values
    # when it is false. Keep the two regions explicit to avoid reversing them.
    all_t, all_l, p162 = exact_grid(k1max, k2max, kmax-1, tmin, tmax, lmin, lmax, 162.0, days)
    _, _, p172 = exact_grid(k1max, k2max, kmax-1, tmin, tmax, lmin, lmax, 172.37, days)
    ln_t = np.log(all_t)[:, None]
    ln_l = np.log(all_l)[None, :]
    simulation_region = ln_l <= (-3.057394436628309 - 1.2724645048999665*ln_t)
    hardcoded_region = ~simulation_region
    _, cap162, uncap162 = capped_wait_map(p162, cap)
    _, cap172, uncap172 = capped_wait_map(p172, cap)
    ratio = np.divide(p172, p162, out=np.ones_like(p162), where=p162 > 0)

    # Representative points from the published paper and from the exact peak.
    representative = []
    for T_s, rate, label in [(181.0, 3.69, "published_32p3_peak"), (182.3, 4.44, "exact_surface_peak_neighbour"),
                             (300.0, 0.1, "low_rate"), (7200.0, 0.05, "long_duration")]:
        p162_point = code_probability(rate, T_s/86400, 162.0, days)
        p172_point = code_probability(rate, T_s/86400, 172.37, days)
        mean1000, map1000, mapuncapped = capped_wait_map(np.array([p162_point]), cap)
        representative.append({
            "label": label, "T_s": T_s, "lambda_per_day": rate,
            "exact_literal_code_probability_162s": p162_point,
            "exact_literal_code_probability_172p37s": p172_point,
            "gap_change_fraction_172p37_vs_162": p172_point/p162_point-1 if p162_point else None,
            "expected_capped_wait_count_at_162s": float(mean1000[0]),
            "source_map_limit_capped_162s": float(map1000[0]),
            "source_map_limit_uncapped_162s": float(mapuncapped[0]),
            "correct_geometric_map_limit_uncensored": p162_point,
        })
    independent_json = json.loads(INDEPENDENT_RESULT.read_text(encoding="utf-8"))
    independent_p = independent_json["mc"]["162.0"]["near_short_duration_peak"]["analytic_literal_code"]
    own_p = code_probability(4.44, 182.3/86400, 162.0, days)

    hardcoded_prob = p162[hardcoded_region]
    hardcoded_positive = hardcoded_prob[hardcoded_prob > 0]
    exact_peak = np.unravel_index(np.argmax(p162), p162.shape)
    data_valid_grid = (grid_k1 <= k1max) & (grid_k2 <= k2max)
    grid_k1_max, grid_k2_max = int(max_row[3]), int(max_row[4])
    max_t = math.exp(math.log(tmin)+(grid_k1_max-1)*(math.log(tmax)-math.log(tmin))/(kmax-1))
    max_l = math.exp(math.log(lmin)+(grid_k2_max-1)*(math.log(lmax)-math.log(lmin))/(kmax-1))
    max_simulation_region = math.log(max_l) <= (-3.057394436628309-1.2724645048999665*math.log(max_t))
    max_source_p = float(p162[grid_k1_max-1, grid_k2_max-1])
    positive = p162 > 0
    capped_log10_ratio = np.log10(cap162[positive]) - np.log10(p162[positive])
    uncapped_log10_ratio = np.log10(uncap162[positive]) - np.log10(p162[positive])
    out = {
        "audit_scope": "Deterministic source and exact-model audit; no Fortran compilation or reproduction of unseeded realizations/MCMC chains.",
        "source_and_data_sha256": {str(p.relative_to(ROOT)): digest(p) for p in (SOURCE, GRID, NOTEBOOK)},
        "independent_crosscheck": {
            "existing_separately_implemented_exact_probability_182p3s_4p44day_162s": independent_p,
            "this_audit_exact_probability_same_point": own_p,
            "absolute_difference": abs(independent_p-own_p),
            "agreement_within_1e-12": abs(independent_p-own_p) < 1e-12,
        },
        "source_parameters": {"Tmin_days": tmin, "Tmax_days": tmax, "lambda_min_day": lmin,
                              "lambda_max_day": lmax, "kmax_denominator": kmax-1,
                              "source_grid_shape": [k1max, k2max], "maxcounts": cap},
        "released_grid_audit": {
            "numeric_rows": int(data.shape[0]), "duration_indices": int(np.unique(grid_k1).size),
            "rate_indices": int(np.unique(grid_k2).size),
            "first_row": {"ln_or_log10_T": float(first[0]), "ln_or_log10_lambda": float(first[1]),
                          "reported_log10_likelihood_floor": float(first[2]), "k1": int(first[3]), "k2": int(first[4])},
            "first_row_matches_natural_logs": natural_log_matches,
            "first_row_matches_base10_logs": base10_matches,
            "header_says_log10_but_values_are_ln": bool(natural_log_matches and not base10_matches),
            "notebook_reconstructs_coordinates_from_indices_using_Log": "Log[Tgrid[[k1]]] and Log[lambda_grid[[k2]]]",
            "notebook_plot_axes_label_base10": True,
            "output_grid_max_log10_likelihood": float(max_row[2]),
            "output_grid_max_probability": float(10**max_row[2]),
            "output_grid_max_indices_k1_k2": [grid_k1_max, grid_k2_max],
            "rows_in_current_source_loop_domain": int(data_valid_grid.sum()),
            "rows_beyond_current_source_k1_loop": int((~data_valid_grid).sum()),
            "at_output_grid_max_cell_current_source_simulation_branch_applies": bool(max_simulation_region),
            "at_output_grid_max_cell_current_source_hardcoded_branch_applies": not bool(max_simulation_region),
            "at_output_grid_max_cell_current_source_exact_probability_162s": max_source_p,
            "at_output_grid_max_cell_current_source_hardcoded_map_if_hardcoded_branch": 11/11011 if not max_simulation_region else None,
            "released_grid_max_to_hardcoded_map_ratio": float((10**max_row[2])/(11/11011)) if not max_simulation_region else None,
        },
        "finite_baseline_exact_grid": {
            "grid_shape": [k1max, k2max], "paper_gap_max_probability": float(p172.max()),
            "paper_gap_max_at_T_s_lambda_day": [float(all_t[np.unravel_index(np.argmax(p172), p172.shape)[0]]*86400),
                                                 float(all_l[np.unravel_index(np.argmax(p172), p172.shape)[1]])],
            "source_gap_max_probability": float(p162.max()),
            "source_gap_max_at_T_s_lambda_day": [float(all_t[exact_peak[0]]*86400), float(all_l[exact_peak[1]])],
            "relative_gap_shift_at_source_exact_peak": float(p172[exact_peak]/p162[exact_peak]-1),
            "cells_in_monte_carlo_simulation_branch": int(simulation_region.sum()),
            "cells_hardcoded_to_11_of_11011": int(hardcoded_region.sum()),
            "hardcoded_cells_with_exact_zero_probability": int(np.count_nonzero(hardcoded_prob == 0)),
            "exact_success_probability_minmax_in_hardcoded_cells": [float(hardcoded_prob.min()), float(hardcoded_prob.max())],
            "exact_success_probability_minmax_positive_in_hardcoded_cells": [float(hardcoded_positive.min()), float(hardcoded_positive.max())],
            "hardcoded_source_likelihood": 11/11011,
            "hardcoded_to_exact_log10_ratio_minmax_over_positive_exact_probabilities": [float((math.log10(11/11011)-np.log10(hardcoded_positive)).min()),
                                                                                       float((math.log10(11/11011)-np.log10(hardcoded_positive)).max())],
        },
        "waiting_count_estimator_audit": {
            "observed_source_behavior": "counts increments before each realization; a first-trial success returns C=1; capped non-success returns C=maxcounts; n increments for each returned count; ngaveup is not used in p_mode.",
            "paper_geometric_model": "C is described as number of Bernoulli trials needed to get one success, with likelihood (1-p)^C p per loop.",
            "standard_geometric_support": "If C counts trials including success, P(C=c|p)=(1-p)^(c-1)p; total failures over W loops are sum(C)-W.",
            "source_map_formula": "n/(n+sumcounts), where sumcounts includes the terminal success in every uncensored C.",
            "correct_uncensored_geometric_map_from_trial_counts": "n/sumcounts",
            "uncensored_large_sample_limit_of_source_formula": "p/(1+p), not p",
            "capped_expected_wait_count": "E[min(C,maxcounts)]=(1-(1-p)^maxcounts)/p",
            "capped_large_sample_limit_of_source_formula": "p/(p+1-(1-p)^maxcounts)",
            "capped_limit_log10_ratio_vs_exact_probability_minmax_162s": [float(capped_log10_ratio.min()), float(capped_log10_ratio.max())],
            "uncapped_limit_log10_ratio_vs_exact_probability_minmax_162s": [float(uncapped_log10_ratio.min()), float(uncapped_log10_ratio.max())],
        },
        "representative_points": representative,
        "limitations": [
            "This audit derives exact expected estimator behavior under the geometric model; it does not reproduce the outer precision-stopping distribution or randomized grid values.",
            "The reported released-chain maxima and MCMC posterior are not recomputed here.",
            "The exact finite-baseline probability is for the literal individual-event rule and first post-baseline arrival analyzed in the independent reference script.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUT), "output_sha256": digest(OUT),
                      "highlights": {"output_grid_log_base_mismatch": out["released_grid_audit"]["header_says_log10_but_values_are_ln"],
                                     "monte_carlo_cells": int(simulation_region.sum()),
                                     "hardcoded_cells": int(hardcoded_region.sum()),
                                     "source_exact_peak_probability": float(p162.max()),
                                     "source_estimator_limit_at_peak": float(uncap162[exact_peak])}}, indent=2))


if __name__ == "__main__":
    main()
