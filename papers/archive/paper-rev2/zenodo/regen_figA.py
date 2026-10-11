"""FigA redo: full-width five-box strip, >=8pt text, single sans-serif family.
Usage: .\.venv\Scripts\python.exe audit\supervisor-fixes-2026-10-08\scripts\regen_figA.py [outpath]
Content verified: Level A = printout observables; Level B = reconstructed bounds;
Level C = conditional Tb bound; Level D = verified H5 maxima (no MAP term).
"""
import sys as _s

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import textwrap

OUT = (_s.argv[1] if len(_s.argv) > 1
       else "audit/supervisor-fixes-2026-10-08/outputs/figA_architecture_FIXED.pdf")


def wrap(lines, w=24):
    out = []
    for ln in lines:
        out.extend(textwrap.wrap(ln, width=w) or [""])
    return "\n".join(out)


plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"],
                     "font.size": 9, "figure.dpi": 300, "savefig.dpi": 300,
                     "savefig.bbox": "tight", "text.usetex": False})
fig, ax = plt.subplots(figsize=(10, 3.0))
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(0, 1)
ax.axis("off")

titles = ["Direct\nObservations", "Reconstructed\nQuantities", "Physical\nInference",
          "Statistical\nLikelihood", "Population\nInference"]
levels = ["Level A", "Level B", "Level C", "Level D", "Level E"]
examples = [
    wrap(["6EQUJ5 sequence", "12-s cadence", "one channel", "one horn"]),
    wrap([r"$S_\nu\geq256$ Jy", r"$\nu=1420.726$ MHz", r"$\theta\leq1.9'$", r"$\Delta t\geq73.4$ s"]),
    wrap([r"$T_B\geq1.7\times10^4$ K", "compact circular", "(geometry-cond.)"]),
    wrap(["H5 maximum:", "1.78% chain", "1.58% emulator"]),
    wrap(["Missing priors", "& selection", "functions"]),
]
colors = ["#d4edda", "#d1ecf1", "#fff3cd", "#f8d7da", "#e2e3e5"]
bw, bh, y0, gap = 0.168, 0.66, 0.06, 0.012
for i in range(5):
    x0 = 0.01 + i * (bw + gap)
    ax.add_patch(FancyBboxPatch((x0, y0), bw, bh,
                                boxstyle="round,pad=0.012",
                                facecolor=colors[i], edgecolor="black", linewidth=1.4))
    ax.text(x0 + bw / 2, y0 + bh - 0.07, titles[i],
            ha="center", va="center", fontweight="bold", fontsize=10)
    ax.text(x0 + bw / 2, y0 + bh - 0.19, levels[i],
            ha="center", va="center", fontsize=9, fontstyle="italic", color="#555555")
    ax.text(x0 + bw / 2, y0 + bh - 0.26, examples[i],
            ha="center", va="top", fontsize=8.5, color="#333333")
    if i < 4:
        ax.annotate("",
                    xy=(x0 + bw + gap, y0 + bh / 2),
                    xytext=(x0 + bw, y0 + bh / 2),
                    arrowprops=dict(arrowstyle="-|>", lw=1.8, color="black"))
bnd_x = 0.01 + 3 * (bw + gap) + bw + gap / 2
ax.plot([bnd_x, bnd_x], [y0 - 0.04, y0 + bh + 0.04],
        color="red", ls="--", lw=2.2, zorder=5)
ax.text(bnd_x, y0 + bh + 0.22, "Identifiability Boundary",
        ha="center", va="center", fontweight="bold", fontsize=10.5, color="red",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=1.2))
ax.text(bnd_x, y0 + bh + 0.135, "(Missing priors & selection functions)",
        ha="center", va="center", fontsize=8.5, color="red")
fig.savefig(OUT)
print("wrote", OUT)
