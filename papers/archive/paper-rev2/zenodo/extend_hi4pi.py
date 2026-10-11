"""HI4PI extension: spectra at Wow! horns plus declination-offset pixels.

Samples the 40-arcmin Big Ear declination beam at the horn declinations
+/-20' and +/-40' (the source can sit anywhere in the beam), and computes
the geometry-independent persistent-source brightness for a 256-Jy signal
in the 16.2' HI4PI beam.

Run: .\\.venv\\Scripts\\python.exe papers/archive/paper-rev2/scripts/extend_hi4pi.py
In:  audit/supervisor-fixes-2026-10-08/hi4pi/HPX_121.fits (CDS J/A+A/594/A116)
Out: papers/archive/paper-rev2/scripts/hi4pi_extended.json (values quoted in Sec. 6)
Frozen inputs: horn J2000 from Mendez II Table 4; S_nu = 256 Jy; nu = 1420.726 MHz.
"""
import json
import math
import os

import numpy as np
from astropy.coordinates import SkyCoord
from astropy.io import fits
import astropy.units as u

HERE = os.path.dirname(os.path.abspath(__file__))
FITS = os.path.normpath(os.path.join(
    HERE, "..", "..", "..", "..", "audit", "supervisor-fixes-2026-10-08",
    "hi4pi", "HPX_121.fits"))
OUT = os.path.join(HERE, "hi4pi_extended.json")

C = 299792458.0
KB = 1.380649e-23
NU = 1420726000.0
S_JY = 256.0
# HI4PI channel width: v = (i+1-466.92163)*1288.215 m/s (LSRK, radio)
DV = 1288.215 / 1000.0  # km/s
FWHM_ARCMIN = 16.2

# Frozen horn positions (Mendez II Table 4 J2000)
HORNS = {"pos": ("19:25:02", -26 - 57.3 / 60.0),
         "neg": ("19:27:55", -26 - 57.2167 / 60.0)}
OFFSETS_ARCMIN = [0.0, 20.0, -20.0, 40.0, -40.0]
# Event-velocity window VLSR -74 +/- 2 km/s
VLO, VHI = -76.0, -72.0


def vel_array(nch):
    return (np.arange(nch) + 1 - 466.92163) * 1288.215 / 1000.0


def main():
    hdul = fits.open(FITS)
    d = hdul[1].data
    lon, lat, spec = d["GLON"], d["GLAT"], d["DATA"]
    v = vel_array(len(np.asarray(spec[0]).ravel()))
    win = (v >= VLO) & (v <= VHI)

    # Geometry-independent persistent brightness: 256 Jy filling the HI4PI beam
    fwhm_rad = math.radians(FWHM_ARCMIN / 60.0)
    omega = 1.133 * fwhm_rad ** 2  # Gaussian-beam solid angle
    t_persist = S_JY * 1e-26 * C ** 2 / (2 * KB * NU ** 2 * omega)

    res = {"meta": {
        "fits": os.path.basename(FITS),
        "beam_arcmin": FWHM_ARCMIN,
        "channel_kms": DV,
        "window_kms": [VLO, VHI],
        "S_Jy": S_JY,
        "nu_MHz": NU / 1e6,
        "T_persist_per_channel_K": t_persist,
    }, "pixels": {}}
    print(f"persistent 256-Jy brightness in {FWHM_ARCMIN}' beam: {t_persist:.1f} K/channel")

    for horn, (ra_hms, dec0) in HORNS.items():
        for off in OFFSETS_ARCMIN:
            dec = dec0 + off / 60.0
            ra_deg = (int(ra_hms[:2]) + int(ra_hms[3:5]) / 60.0
                      + float(ra_hms[6:]) / 3600.0) * 15.0
            c = SkyCoord(ra_deg * u.deg, dec * u.deg, frame="icrs")
            g = c.galactic
            seps = np.hypot((lon - g.l.deg) * np.cos(np.radians(g.b.deg)),
                            lat - g.b.deg)
            j = int(np.argmin(seps))
            s = np.asarray(spec[j], dtype=float).ravel()
            band = s[win]
            rms = float(np.sqrt(np.mean((band - np.mean(band)) ** 2)))
            key = f"{horn}{off:+.0f}" if off else horn
            res["pixels"][key] = {
                "ra_hms": ra_hms, "dec_deg": dec,
                "l_deg": float(g.l.deg), "b_deg": float(g.b.deg),
                "nearest_arcmin": float(seps[j] * 60.0),
                "band_K": [round(float(x), 4) for x in band],
                "band_rms_K": round(rms, 4),
                "band_maxabs_K": round(float(np.max(np.abs(band))), 4),
            }
            print(f"{key:8s} l={g.l.deg:7.3f} b={g.b.deg:+7.3f} "
                  f"sep={seps[j]*60:.1f}' band={res['pixels'][key]['band_K']} "
                  f"rms={rms:.3f} max|.|={np.max(np.abs(band)):.3f}")

    json.dump(res, open(OUT, "w"), indent=1)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
