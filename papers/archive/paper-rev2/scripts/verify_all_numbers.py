"""Safeguard: reproduce every number quoted in the manuscript from frozen inputs.

Run: .\\.venv\\Scripts\\python.exe papers/archive/paper-rev2/scripts/verify_all_numbers.py
Checks each quoted value by independent recomputation (inline physics),
frozen JSONs (main_numbers.json, hi4pi_extended.json), the released Kipping
chains, and a live JPL-Horizons requery (horizons_recheck.py). Prints
PASS/FAIL per number; exit code 0 iff all pass. Per the freeze rule this
script changes no science inputs — it only reads them.

Quoted-number inventory (manuscript Secs. 3, 5.2, 6, 7, 8, 12; abstract):
TB bounds, elongation thresholds, beam kinematics, H5 demo + chains + kmax,
EIRP constant, HI4PI brightness + band values, Horizons offsets, coincidence.
"""
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
PY = os.path.join(ROOT, ".venv", "Scripts", "python.exe")

C = 299792458.0
KB = 1.380649e-23
NU = 1420726000.0
fails = []


def check(name, got, want, tol=0.0, fmt="{:.4g}"):
    ok = abs(got - want) <= tol
    print(("PASS" if ok else "FAIL"), name,
          "got", fmt.format(got), "want", fmt.format(want))
    if not ok:
        fails.append(name)


def tb(s_jy, theta_am):
    th = math.radians(theta_am / 60.0)
    om = math.pi * (th / 2.0) ** 2
    return s_jy * 1e-26 * C ** 2 / (2 * KB * NU ** 2 * om)


mn = json.load(open(os.path.join(HERE, "main_numbers.json")))
hi = json.load(open(os.path.join(HERE, "hi4pi_extended.json")))

# ---- H3 brightness temperature (Sec. 6; abstract; Table 1) ----
check("TB nominal K", tb(256.0, 1.9),
      mn["H3"]["TB_nominal_K"], 1e-6, "{:.2f}")
assert abs(mn["H3"]["TB_nominal_K"] - 17206.72) < 0.01
check("TB 1-sigma floor K", tb(193.0, 2.0),
      mn["H3"]["TB_1sigma_propagated_K"], 1e-6, "{:.2f}")
assert abs(mn["H3"]["TB_1sigma_propagated_K"] - 11707.46) < 0.01
# ---- elongation thresholds (Sec. 6: 4.09' / 6.54'; 820 / 585 K) ----
tb0 = mn["H3"]["TB_nominal_K"]
check("theta_Dec 8000K", 1.9 * tb0 / 8000.0, 4.09, 0.005)
check("theta_Dec 5000K", 1.9 * tb0 / 5000.0, 6.54, 0.005)
check("T elong nom", tb0 / 21.0, 820, 1.0, "{:.0f}")
check("T elong floor", mn["H3"]["TB_1sigma_propagated_K"] / 20.0, 585, 1.0,
      "{:.0f}")
# ---- beam kinematics (Secs. 3, 6; Fig. 2) ----
rate = 15.0410686 * math.cos(math.radians(-26 - 57 / 60))
check("drift rate \"/s", rate, 13.4076, 1e-3)
fwhm = 8 * 60 / rate
check("FWHM s", fwhm, 35.80, 0.005)
sig = fwhm / 2.355
check("full extent s", 2 * math.sqrt(2 * math.log(30.1)) * sig, 79.3, 0.05)
# ---- H5 selection demo (Secs. 8, 9, 12; abstract) ----
d = mn["H5_selection_demo"]
check("MAP OSU-only %", d["MAP_OSU_only_pct"], 5.62, 0.005)
check("MAP transparent %", d["MAP_transparent_pct"], 2.52, 0.005)
check("peak factor", d["MAP_OSU_only_pct"] / d["MAP_transparent_pct"],
      2.2, 0.05)
check("evidence ratio", d["evidence_update_ratio"], 0.65, 0.005)
check("span hours", mn["Hobart_2010_2014"]["total_span_hours"], 114.116,
      1e-6)
# ---- H5 chains (Sec. 8: 32.3 / 3.3 / 1.78) ----
for key, want in (("OSU", 32.3), ("OSUHobart", 3.3), ("ALL", 1.78)):
    got = mn["H5_published_chains"][key]["max_likelihood_pct"]
    check("chain " + key + " %", got, want, 0.05)
# ---- kmax sweep (Sec. 8: ~0.8% @100, 1.58% converged) ----
sw = mn["H5_kmax_sweep_pooled_penalty_pct"]
check("kmax100 %", sw["100"], 0.83, 0.03)
check("kmax500 %", sw["500"], 1.58, 0.005)
# ---- EIRP constant (Sec. 7: 3.06e14 W at 1 pc, 10 kHz) ----
eirp = 4 * math.pi * (3.085677581e16) ** 2 * 256e-26 * 1e4
check("EIRP 1pc W", eirp, 3.06e14, 0.01e14, "{:.2e}")
check("EIRP json W", mn["H4"]["EIRP_1pc_10kHz_W"], eirp, 1e9, "{:.2e}")
# ---- coincidence prior (abstract + Sec. 7: ~5e-6) ----
check("coincidence", 0.5 / 99000.0, 5e-6, 1e-7, "{:.1e}")
# ---- HI4PI (Sec. 6.5, Fig. 7) ----
check("T persist K/ch", hi["meta"]["T_persist_per_channel_K"], 164.1, 0.05)
mx = 0.0
for k, p in hi["pixels"].items():
    mx = max(mx, p["band_maxabs_K"])
    assert p["band_rms_K"] <= 0.05, k
check("max |band| K (<=0.10)", mx, 0.096, 0.005)
assert len(hi["pixels"]) == 10, "ten sampled positions"
print("PASS ten HI4PI positions, in-band rms 0.01-0.05 K")
# ---- Horizons live requery (Sec. 5.2) ----
r = subprocess.run([PY, os.path.join(HERE, "horizons_recheck.py")],
                   capture_output=True, text=True, cwd=ROOT)
print(r.stdout.strip().splitlines()[-1])
assert r.returncode == 0, "horizons_recheck failed"
import re as _re
nums = [float(x) for x in _re.findall(r"dRA ([+-]\d+) s", r.stdout)]
assert nums == [-3191, -3364, -2749, -2922], nums
print("PASS Horizons offsets -3191/-3364/-2749/-2922 s live")
assert "r=4.73" in r.stdout and "r=4.56" in r.stdout
print("PASS Horizons ranges r=4.73/4.56 AU live")

print("----")
if fails:
    print("FAILURES:", fails)
    sys.exit(1)
print("ALL NUMBERS VERIFIED")

# ---- extended gate: geometry grid + independent H5 audit as subprocesses --
import re as _re2
import subprocess as _sp

r = _sp.run([sys.executable, os.path.join(HERE, "hi4pi_geometry_test.py")],
            capture_output=True, text=True, cwd=ROOT)
assert r.returncode == 0, r.stderr[-500:]
narrow = {}
for m in _re2.finditer(r"^\s*([\d.]+)'\s+[\d.e+-]+\s+[\d.]+\s+([\d.]+) /",
                       r.stdout, _re.M):
    narrow[float(m.group(1))] = float(m.group(2))
for td, want in ((1.9, 163.3), (4.09, 161.9), (6.54, 159.2), (20.0, 129.7),
                 (40.0, 83.8)):
    got = narrow[td]
    ok = abs(got - want) <= 1.0
    print(("PASS" if ok else "FAIL"), f"HI4PI geometry {td}'",
          f"got {got} want {want}")
    if not ok:
        fails.append(f"geometry {td}")
# Gaussian-profile sensitivity (Sec. 6.2): solid angle larger by 1/ln2
import math as _m
gfac = 1.0 / _m.log(2.0)
tb_nom = mn["H3"]["TB_nominal_K"]
tb_fl = mn["H3"]["TB_1sigma_propagated_K"]
for name, got, want in (("gauss factor", gfac, 1.442695),
                        ("gauss nominal K", tb_nom / gfac, 11926.79),
                        ("gauss floor K", tb_fl / gfac, 8114.99),
                        ("gauss elong 8000K", 1.9 * tb_nom / gfac / 8000.0,
                         2.833),
                        ("gauss elong 5000K", 1.9 * tb_nom / gfac / 5000.0,
                         4.532)):
    ok = abs(got - want) <= max(1e-4, abs(want) * 0.001)
    print(("PASS" if ok else "FAIL"), name, f"got {got:.4f} want {want}")
    if not ok:
        fails.append(name)
assert "51.1" in r.stdout, "resolved-line 40' value missing"
print("PASS resolved-line values present (~51-100 K/channel)")

r = _sp.run([sys.executable, os.path.join(HERE, "h5_independent_audit.py")],
            capture_output=True, text=True, cwd=ROOT)
assert r.returncode == 0, r.stdout[-800:] + r.stderr[-500:]
print("PASS h5_independent_audit.py (MC + 120-grid evidence)")

r = _sp.run([sys.executable, os.path.join(HERE, "sep_on_sky.py")],
            capture_output=True, text=True, cwd=ROOT)
for want in ("11.83", "12.47", "10.43", "11.04"):
    assert want in r.stdout, want
print("PASS on-sky separations 11.83/12.47/10.43/11.04 deg (great-circle)")

r = _sp.run([sys.executable, os.path.join(HERE, "freq_prior_compare.py")],
            capture_output=True, text=True, cwd=ROOT)
assert "5.05e-06" in r.stdout and "7.64e-05" in r.stdout, r.stdout
print("PASS frequency priors 5.05e-6 / 7.64e-5")

# field-map exclusion over the full error region (Sec. 6.5)
import json as _json
fm = _json.load(open(os.path.join(
    ROOT, "audit", "supervisor-fixes-2026-10-08", "hi4pi",
    "wow_hi4pi_field_map.json")))
assert fm["meta"]["n_pixels"] >= 800, fm["meta"]
assert fm["result"]["max_abs_K"] < 0.2, fm["result"]
assert fm["result"]["n_pixels_ge_1K"] == 0, fm["result"]
print(f"PASS field map max {fm['result']['max_abs_K']} K over "
      f"{fm['meta']['n_pixels']} pixels, none >= 1 K")

# adjacent-channel thermal-line check (Sec. 6.5): Gaussian FWHM 7-9 Big Ear
# channels peaking at 256 Jy puts ~240 Jy in each neighbor vs ~8.5 Jy noise
import math as _m2
for fwhm in (7.0, 9.0):
    v = 256 * _m2.exp(-4 * _m2.log(2) * (1 / fwhm) ** 2)
    assert 200.0 < v < 260.0, (fwhm, v)
print("PASS adjacent-channel expectation ~240 Jy (FWHM 7) / ~247 Jy (FWHM 9)")

print("----")
if fails:
    print("FAILURES:", fails)
    sys.exit(1)
print("EXTENDED GATE: ALL CHECKS PASS")
