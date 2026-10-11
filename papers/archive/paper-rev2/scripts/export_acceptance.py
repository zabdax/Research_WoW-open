"""Export all 7 manuscript figures in acceptance formats (EPS + 600-dpi TIFF).

Run: .\\.venv\\Scripts\\python.exe papers/archive/paper-rev2/scripts/export_acceptance.py
Out: papers/archive/paper-rev2/ija_manuscript/eps/fig1..fig7.eps
     papers/archive/paper-rev2/ija_manuscript/tiff/fig1..fig7.tiff
Review PDFs in figures/ and ija_manuscript/ are untouched (Fig. 2 already
rebuilt by rebuild_figB.py); EPS/TIFF are regenerated from the same code paths.
Verifies: %!PS header for EPS, TIFF magic (II*/MM) + sizes.
"""
import json
import math
import os
import subprocess
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif",
                      "font.sans-serif": ["DejaVu Sans"]})
import numpy as np

ROOT = os.getcwd()
EPS = os.path.join(ROOT, "papers", "archive", "paper-rev2", "ija_manuscript", "eps")
TIFF = os.path.join(ROOT, "papers", "archive", "paper-rev2", "ija_manuscript", "tiff")
os.makedirs(EPS, exist_ok=True)
os.makedirs(TIFF, exist_ok=True)
PY = os.path.join(ROOT, ".venv", "Scripts", "python.exe")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout[-400:] if r.stdout else "", r.stderr[-300:] if r.stderr else "")
    assert r.returncode == 0, cmd


def pair(stem_in, num):
    """Regenerate figure `num` (figN) via its generator into EPS+TIFF."""
    run([PY, stem_in, os.path.join(EPS, num + ".eps")])
    run([PY, stem_in, os.path.join(TIFF, num + ".tiff")])


# ---- A, B, C, G through their own generators (argv = out path) ----
# NOTE: file numbers match PRINTED figure order (HI4PI is Fig. 4).
pair("audit/supervisor-fixes-2026-10-08/scripts/regen_figA.py", "fig1")
pair("papers/archive/paper-rev2/scripts/rebuild_figB.py", "fig2")
pair("audit/supervisor-fixes-2026-10-08/scripts/regen_figC.py", "fig3")
pair("audit/supervisor-fixes-2026-10-08/scripts/plot_hi4pi.py", "fig4")

# ---- D, E: rev2 code path, savefig duplicated to EPS/TIFF ----
sys.path.insert(0, os.path.join(ROOT, "papers", "archive", "paper-rev2", "scripts"))
import reproduce_figures_de as de
_orig_savefig = plt.savefig


def multi(path, **kw):
    p = str(path)
    stem = os.path.basename(p)[:-4] if p.endswith(".pdf") else None
    num = {"figD_h5_likelihood": "fig5",
           "figE_h5_convergence": "fig6"}.get(stem)
    if num is not None:
        _orig_savefig(os.path.join(EPS, num + ".eps"), format="eps", **kw)
        _orig_savefig(os.path.join(TIFF, num + ".tiff"), format="tiff",
                      dpi=600, **kw)
        print("saved", num + ".eps + .tiff")
        return
    return _orig_savefig(path, **kw)


plt.savefig = multi
de.generate_figure_d()
de.generate_figure_e()
plt.savefig = _orig_savefig

# ---- F: faithful replot from frozen rev2 main_numbers.json ----
mn = json.load(open("papers/archive/paper-rev2/scripts/main_numbers.json"))
TH_H = mn["Hobart_2010_2014"]["total_span_hours"]
TH_D = mn["Hobart_2010_2014"]["total_span_days"]
L_osu = mn["H5_selection_demo"]["lam_day"]
lam = np.logspace(math.log10(math.exp(-4.0)), math.log10(math.exp(2.0)), 400)
ratio = np.exp(-lam * TH_D)
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
fig.savefig(os.path.join(EPS, "fig7.eps"), format="eps")
fig.savefig(os.path.join(TIFF, "fig7.tiff"), format="tiff", dpi=600)
plt.close(fig)
print("fig7 done")

# ---- verify ----
for i in range(1, 8):
    for p, magic in ((os.path.join(EPS, f"fig{i}.eps"), b"%!PS"),
                     (os.path.join(TIFF, f"fig{i}.tiff"), None)):
        with open(p, "rb") as f:
            head = f.read(8)
        size = os.path.getsize(p)
        if magic:
            assert head.startswith(magic), p
        else:
            assert head[:2] in (b"II", b"MM"), p
        print(f"{os.path.basename(p)} {size}B OK")
print("ALL ACCEPTANCE EXPORTS OK")
