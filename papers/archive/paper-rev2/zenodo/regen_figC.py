"""Regenerate FigC (H3 brightness temperature) fixing the raw '\\u2013' legend text.
Run: .\.venv\Scripts\python.exe audit\supervisor-fixes-2026-10-08\scripts\regen_figC.py
Out: papers/archive/paper-rev2/figures/figC_h3_brightness_temperature.pdf (overwrites rev1 file)
Curve: Tb(theta) for S=256 Jy at 1420.726 MHz, circular uniform disk (recomputed inline).
"""
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import sys as _s
OUT = _s.argv[1] if len(_s.argv) > 1 else r"papers/archive/paper-rev2/figures/figC_h3_brightness_temperature.pdf"
c, kB, nu, Snu = 299792458.0, 1.380649e-23, 1420726000.0, 256e-26

theta_am = np.logspace(np.log10(0.05), np.log10(10), 800)
theta_rad = theta_am / 60.0 * np.pi / 180.0
T_B = Snu * c ** 2 / (2 * kB * nu ** 2 * (np.pi * (theta_rad / 2.0) ** 2))
th_max = 1.9 / 60.0 * np.pi / 180.0
TB_min = Snu * c ** 2 / (2 * kB * nu ** 2 * (np.pi * (th_max / 2.0) ** 2))
print(f"TB_min check: {TB_min:.2f} K (expect ~17206.72)")
assert abs(TB_min - 17206.721063518387) < 1.0

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"], "font.size": 11, "axes.labelsize": 13,
                     "axes.titlesize": 14, "legend.fontsize": 9.5, "figure.dpi": 300,
                     "savefig.dpi": 300, "savefig.bbox": "tight", "text.usetex": False})
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(theta_am, T_B, "k-", lw=2.2, label=r"$T_B(\theta)$ for $S_\nu = 256$ Jy")
ax.axvline(1.9, color="royalblue", ls="--", lw=2,
           label=r"Angular size upper bound ($\theta \leq 1.9'$)")
ax.axhline(TB_min, color="red", ls="--", lw=2, label=r"$T_B \geq 1.72 \times 10^4$ K")
mask = theta_am <= 1.9
ax.fill_between(theta_am[mask], T_B[mask], 1e12, color="green", alpha=0.12,
                label="Required non-thermal parameter space")
ax.axhspan(1, 300, color="gray", alpha=0.25,
           label="Cold thermal HI (Tk ~10\u2013300 K)")
ax.plot(1.9, TB_min, "ro", ms=8, zorder=5)
ax.annotate(r"$T_B \geq 1.72 \times 10^4$ K", xy=(1.9, TB_min), xytext=(3.0, 5e5),
            fontsize=11, color="red", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="red", lw=1.5))
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.05, 10)
ax.set_ylim(1, 1e10)
ax.set_xlabel(r"Angular Size $\theta$ (arcmin)")
ax.set_ylabel(r"Brightness Temperature $T_B$ (K)")
ax.legend(loc="upper right", framealpha=0.95, fontsize=9.5)
fig.savefig(OUT)
plt.close(fig)
print("wrote", OUT)
