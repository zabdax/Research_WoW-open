"""Frequency-coincidence priors over 1-100 GHz for a ~500 kHz window (Sec. 7.2).

Uniform-in-frequency:  P = window / range.
Log-uniform in frequency over [lo, hi] with window [a, b] fully inside:
P = ln(b/a) / ln(hi/lo). Window centred at the 1420.726 MHz channel.
Run from the repo root: .venv/Scripts/python.exe papers/archive/paper-rev2/scripts/freq_prior_compare.py
"""
import math

LO, HI = 1e9, 100e9          # 1-100 GHz design space
FC, W = 1420.726e6, 0.5e6    # receiver window centre/width (Hz)
a, b = FC - W / 2, FC + W / 2

p_uni = W / (HI - LO)
p_log = math.log(b / a) / math.log(HI / LO)
print(f"uniform-in-frequency : {p_uni:.2e}")
print(f"log-uniform          : {p_log:.2e}")
print(f"ratio (log/uni)      : {p_log / p_uni:.1f}x")
