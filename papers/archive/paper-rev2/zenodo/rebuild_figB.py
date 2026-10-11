"""Fig. 2 (canonical rev2 generator): 35.8-s FWHM Gaussian beam response.

Physics (frozen): 8-arcmin RA beam at dec -27 deg -> sidereal rate
15.0410686*cos(dec) = 13.4076 "/s -> FWHM = 480"/13.4076 = 35.80 s.
At S/N = 30.1 the full detectable extent is 2*sqrt(2*ln(SNR))*sigma = 79.4 s,
consistent with the recorded 6 x 12 s = 72 s sequence: 72 s is the full
detectable extent, NOT the FWHM. theta <= 1.9' comes from the Mendez profile
fit (see manuscript Sec. 6), not from the 72 s.

Run: .\\.venv\\Scripts\\python.exe papers/archive/paper-rev2/scripts/rebuild_figB.py
Out: papers/archive/paper-rev2/figures/figB_observational_constraints.pdf
     papers/archive/paper-rev2/ija_manuscript/fig2.pdf (copies)
"""
import math
import os
import shutil
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.normpath(os.path.join(HERE, "..", "figures"))
IJADIR = os.path.normpath(os.path.join(HERE, "..", "ija_manuscript"))

RATE = 15.0410686 * math.cos(math.radians(-26 - 57 / 60))  # "/s
FWHM = 8 * 60 / RATE          # 35.80 s
SIG = FWHM / 2.355
SNR = 30.1                    # Arecibo II peak S/N
PEAK_JY = 256.0               # flux lower bound
FULL = 2 * math.sqrt(2 * math.log(SNR)) * SIG  # full detectable extent, s
print(f"rate={RATE:.4f} FWHM={FWHM:.2f} s sigma={SIG:.2f} s "
      f"full-detectable={FULL:.1f} s (recorded 72 s)")

plt.rcParams.update({"font.family": "sans-serif",
                      "font.sans-serif": ["DejaVu Sans"],
                      "font.size": 11, "axes.labelsize": 13,
                      "axes.titlesize": 14, "legend.fontsize": 10,
                      "figure.dpi": 300, "savefig.dpi": 300,
                      "savefig.bbox": "tight", "text.usetex": False})
fig, ax = plt.subplots(figsize=(8, 5))
t = np.linspace(0, 150, 600)
profile = PEAK_JY * np.exp(-0.5 * ((t - 75) / SIG) ** 2)
ax.fill_between(t, 0, profile, color="#cce5ff", alpha=0.6, zorder=1)
ax.plot(t, profile, "k-", lw=2.2,
        label="36 s FWHM beam response (8$'$ beam)", zorder=2)
# Recorded 6EQUJ5 printout values (intensity code 0-9/A-Z -> S/N), scaled by
# the Arecibo II channel noise sigma_ch = 8.5 Jy (frozen evidence vector:
# channel-2 rows 58-63; peak U = 30 matches SNR = 30.1 within uncertainties)
SIG6 = np.array([6, 14, 26, 30, 19, 5], dtype=float)
SIGMA_CH = 8.5
ts = np.arange(45, 106, 12)
ax.plot(ts, SIG6 * SIGMA_CH, "ro", ms=7, zorder=4,
        label=r"6EQUJ5 printout values ($\times 8.5$ Jy)")
ax.axhline(PEAK_JY, color="red", ls="--", lw=2,
           label=r"Flux lower limit ($S_\nu \geq 256$ Jy)", zorder=3)
ax.fill_between(t, PEAK_JY, 310, color="red", alpha=0.08, zorder=0)
# Full detectable-extent bracket placed low (near y = 26 Jy), clear of the curve
ax.annotate("", xy=(75 - 36, 26), xytext=(75 + 36, 26),
            arrowprops=dict(arrowstyle="<->", color="blue", lw=2))
ax.text(37, 26, "Full extent ~72 s",
        ha="right", va="center", color="blue", fontweight="bold",
        fontsize=10.5)
# FWHM bracket at half maximum (peak/2 = 128 Jy), label to the left
hm = PEAK_JY / 2
half = SIG * math.sqrt(2 * math.log(2))  # half of FWHM = 17.9 s
ax.annotate("", xy=(75 - half, hm), xytext=(75 + half, hm),
            arrowprops=dict(arrowstyle="<->", color="black", lw=1.6))
ax.text(75 - half - 3, hm, "FWHM 35.8 s", ha="right", va="center",
        fontsize=9.5, color="black")
ax.text(130, 240, r"$\nu = 1420.726$ MHz", ha="right", va="bottom",
        fontsize=11,
        bbox=dict(boxstyle="round,pad=0.3", fc="lightyellow", ec="gray"))
ax.set_xlim(0, 150)
ax.set_ylim(0, 310)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Flux Density (Jy)")
ax.legend(loc="lower right", framealpha=0.95)
out = os.path.join(FIGDIR, "figB_observational_constraints.pdf")
fig.savefig(out)
print("wrote", out)
shutil.copy(out, os.path.join(IJADIR, "fig2.pdf"))
print("copied to ija_manuscript/fig2.pdf")
for extra in sys.argv[1:]:
    fig.savefig(extra, dpi=600 if extra.lower().endswith((".tif", ".tiff")) else "figure")
    print("wrote", extra)
