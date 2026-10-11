"""Animated Wow! transit: 36-s FWHM beam response with 6EQUJ5 samples.

Saves paper/preview/wow-transit.gif (used in the public repo README).
Run from repo root: .venv/Scripts/python.exe papers/archive/paper-rev2/scripts/make_transit_gif.py
"""
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "C:/Windows/Temp/opencode/wow-transit.gif"

RATE = 15.0410686 * math.cos(math.radians(-26 - 57 / 60))
FWHM = 8 * 60 / RATE
SIG = FWHM / 2.355
SIG6 = np.array([6, 14, 26, 30, 19, 5], dtype=float)
TS = np.arange(45, 106, 12)
JY = SIG6 * 8.5

plt.rcParams.update({"font.family": "sans-serif",
                      "font.sans-serif": ["DejaVu Sans"], "font.size": 11,
                      "text.usetex": False})
fig, ax = plt.subplots(figsize=(8, 5))
t = np.linspace(0, 150, 600)
profile = 256 * np.exp(-0.5 * ((t - 75) / SIG) ** 2)
ax.set_xlim(0, 150)
ax.set_ylim(0, 310)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Flux Density (Jy)")
ax.fill_between(t, 0, profile, color="#cce5ff", alpha=0.6)
(line,) = ax.plot([], [], "k-", lw=2.2)
ax.axhline(256, color="red", ls="--", lw=1.5)
pts = ax.plot([], [], "ro", ms=8)[0]
txt = ax.text(75, 285, "", ha="center", fontsize=12, fontweight="bold",
              bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray"))
CODE = "6EQUJ5"


def frame(i):
    tc = 20 + i * (130 / 79)
    m = t <= tc
    line.set_data(t[m], profile[m])
    shown = TS <= tc
    pts.set_data(TS[shown], JY[shown])
    s = "".join(c if ok else "\u00b7" for c, ok in zip(CODE, shown))
    txt.set_text(f"6EQUJ5:  {s}")
    return line, pts, txt


FuncAnimation(fig, frame, frames=80, interval=60, blit=False).save(
    OUT, writer="pillow", fps=14, dpi=80)
print("wrote", OUT, os.path.getsize(OUT) // 1024, "KB")
