"""HI4PI beam-coupling test across elongated-source geometries (Sec. 6.5).

Derivation. A source of total flux S (Jy) and uniform brightness over solid
angle Omega_src has brightness temperature T_fil = S*c^2/(2*k*nu^2*Omega_src).
A Gaussian HI4PI beam (FWHM 16.2', solid angle Omega_beam, peak-normalized
response P) measures the beam-averaged temperature
  T_meas = T_fil * (1/Omega_beam) * int_{source} P dOmega.
Assumed morphology: uniform-brightness elliptical filament with RA full width
fixed at the OBSERVED 1.9' (Big Ear transit constraint) and Dec full width
theta_Dec free (unconstrained by Big Ear). The 2D overlap integral is done
numerically (no small-source approximation). Spectral cases for the fixed
observed 256 Jy per 10-kHz Big Ear channel (2.11 km/s; HI4PI 1.288 km/s/ch):
the 256 Jy is a per-channel spectral flux density, so a broader line does
NOT raise the per-channel value. narrow: line << HI4PI channel -> all flux
in one channel (share 1.0); resolved: line fills the Big Ear channel ->
peak HI4PI channel share = 1.288/2.11 ~= 0.61.
Compares against measured <0.10 K/channel at all ten sampled positions.

Run from repo root: .venv/Scripts/python.exe papers/archive/paper-rev2/scripts/hi4pi_geometry_test.py
"""
import math

import numpy as np

C = 299792458.0
KB = 1.380649e-23
NU = 1420726000.0
S_JY = 256.0
FWHM = math.radians(16.2 / 60.0)
SIG = FWHM / 2.355
OMEGA_BEAM = 1.133 * FWHM ** 2
DV_BIGEAR = 2.11      # km/s per 10 kHz Big Ear channel
DV_HI4PI = 1.2882     # km/s per HI4PI channel
TH_RA = 1.9           # arcmin, observed (fixed)


def degree(x):
    return math.degrees(x)


def beam_avg_temperature(theta_dec_am, line_case):
    """Central-beam HI4PI temperature (K/channel) for a filament of Dec
    extent theta_dec_am, given the observed 256 Jy in one Big Ear channel."""
    a = math.radians(TH_RA / 2 / 60.0)
    b = math.radians(theta_dec_am / 2 / 60.0)
    omega_src = math.pi * a * b
    # spectral factor: share of the 256 Jy channel value landing in the peak
    # HI4PI channel (a broader line does not raise the per-channel value)
    if line_case == "narrow":
        peak_share = 1.0
    elif line_case == "resolved":
        peak_share = DV_HI4PI / DV_BIGEAR
    else:
        raise ValueError(line_case)
    t_fil = S_JY * 1e-26 * C ** 2 / (2 * KB * NU ** 2 * omega_src)
    # numerical 2D overlap of the uniform ellipse with the Gaussian beam
    n = 801
    xs = np.linspace(-a, a, n)
    ys = np.linspace(-b, b, n)
    dx = xs[1] - xs[0]
    dy = ys[1] - ys[0]
    xx, yy = np.meshgrid(xs, ys)
    inside = (xx / a) ** 2 + (yy / b) ** 2 <= 1.0
    p = np.exp(-0.5 * (xx ** 2 + yy ** 2) / SIG ** 2)
    overlap = float(np.sum(p[inside])) * dx * dy
    return t_fil * overlap / OMEGA_BEAM * peak_share


print("theta_Dec  Omega_src(sr)   T_fil(K)  T_central-beam(K/ch): narrow/resolved")
for td in (1.9, 4.09, 6.54, 20.0, 40.0):
    a = math.radians(TH_RA / 2 / 60.0)
    b = math.radians(td / 2 / 60.0)
    om = math.pi * a * b
    tf = S_JY * 1e-26 * C ** 2 / (2 * KB * NU ** 2 * om)
    tn = beam_avg_temperature(td, "narrow")
    tr = beam_avg_temperature(td, "resolved")
    print(f"{td:8.2f}'  {om:.3e}  {tf:9.0f}  {tn:8.1f} / {tr:8.1f}")
print("measured: <=0.10 K/channel at all ten positions")
