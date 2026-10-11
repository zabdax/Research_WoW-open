"""Plot HI4PI spectra at Wow! horns around -74 km/s. Out: audit/.../outputs/figG_hi4pi_spectrum.pdf (copy to rev2 figures)."""
import json
import matplotlib
matplotlib.use("Agg")
import sys as _s
plot_hi4pi_out = _s.argv[1] if len(_s.argv) > 1 else "audit/supervisor-fixes-2026-10-08/outputs/figG_hi4pi_spectrum.pdf"
import matplotlib.pyplot as plt
import numpy as np

d = json.load(open("audit/supervisor-fixes-2026-10-08/hi4pi/wow_hi4pi_spectra.json"))
v = (np.arange(933) + 1 - 466.92163) * 1288.215 / 1000.0
m = (v >= -120) & (v <= 20)

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"], "font.size": 11, "figure.dpi": 300,
                     "savefig.dpi": 300, "savefig.bbox": "tight", "text.usetex": False})
fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
for ax, name, horn in zip(axes, ["pos", "neg"], ["positive (19:25:02)", "negative (19:27:55)"]):
    s = np.array(d[name]["spectrum_K"])
    ax.step(v[m], s[m], "k-", lw=1.2, where="mid")
    ax.axvspan(-76, -72, color="red", alpha=0.15, label="Wow! VLSR $-74\\pm2$ km/s")
    ax.axhline(0, color="gray", lw=0.8)
    ax.set_ylabel(r"$T_B$ (K)")
    ax.set_title(f"HI4PI at Wow! {horn} horn (l={d[name]['l_deg']:.2f}, b={d[name]['b_deg']:.2f})")
    ax.set_ylim(-0.5, 3.0)
    ax.legend(loc="lower left", fontsize=9)
    ax.text(0.03, 0.92, "persistent source predicts $\\gtrsim164$ K/channel (off scale)",
            transform=ax.transAxes, fontsize=8.5, color="red", ha="left", va="top")
axes[1].set_xlabel(r"$V_{\rm LSRK}$ (km/s)")
fig.savefig(plot_hi4pi_out)
print("wrote", plot_hi4pi_out)
