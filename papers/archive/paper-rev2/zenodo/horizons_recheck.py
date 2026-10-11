"""Live JPL-Horizons recheck for the H2 candidate offsets quoted in Sec. 5.2.

Queries geocentric vectors for 266P/Christensen and 335P/Gibbs at the event
epoch and prints RA/Dec, heliocentric range, and separations from the frozen
Mendez II Table 4 horn positions. Topocentric parallax at ~4 AU is ~2 arcsec
(negligible vs degree-scale offsets), so geocentric (500@399) is used.

Run: .\\.venv\\Scripts\\python.exe papers/archive/paper-rev2/scripts/horizons_recheck.py
Frozen expectation (Sec. 5.2): 266P dRA -3191/-3364 s, dDec -24.3'/-24.4';
335P dRA -2749/-2922 s, dDec -159.7'/-159.8'; r = 4.73/4.56 AU.
"""
from astropy.time import Time
from astroquery.jplhorizons import Horizons
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
out = {}

EPOCH = "1977-08-16 03:16:06"
EPOCH_JD = float(Time(EPOCH, scale="utc").jd)
print("epoch JD:", EPOCH_JD)
# Frozen Mendez II Table 4 horn positions (J2000)
HORNS = {"pos": (19 + 25 / 60 + 2 / 3600, -(26 + 57.3 / 60)),
         "neg": (19 + 27 / 60 + 55 / 3600, -(26 + 57.2167 / 60))}
CANDS = {"266P": 90001240, "335P": "335P"}
# NOTE (2026-10-10 live recheck): numeric id 90001326 no longer resolves to
# 335P/Gibbs (returned RA 01:23, Dec -13.5, r = 8.64 AU — a different object);
# the designation query '335P' reproduces the manuscript values exactly
# (18:39:12.5, -29.6169, r = 4.56 AU). Numeric Horizons ids can be
# reassigned; the manuscript cites solution dates/arc spans instead.


def to_hms(h):
    h %= 24
    return int(h), int((h % 1) * 60), ((h % 1) * 60) % 1 * 60


for name, hid in CANDS.items():
    e = Horizons(id=hid, location="500@399", epochs=EPOCH_JD).ephemerides()
    ra, dec, r = float(e["RA"][0]), float(e["DEC"][0]), float(e["r"][0])
    h, m, s = to_hms(ra / 15.0)
    print(f"{name}: RA {h:02d}:{m:02d}:{s:04.1f} Dec {dec:+.4f} r={r:.2f} AU")
    rec = {"target": str(e["targetname"][0]), "RA_deg": ra, "Dec_deg": dec,
           "r_AU": r, "separations": {}}
    for horn, (rah, dech) in HORNS.items():
        dra_s = (ra / 15.0 - rah) * 3600.0
        ddec_m = (dec - dech) * 60.0
        print(f"  vs {horn}: dRA {dra_s:+.0f} s ({dra_s/60:+.1f} min) "
              f"dDec {ddec_m:+.1f}'")
        rec["separations"][horn] = {"dRA_s": round(dra_s, 1),
                                    "dDec_arcmin": round(ddec_m, 2)}
    out[name] = rec
json.dump({"epoch": EPOCH, "epoch_jd": EPOCH_JD, "location": "500@399",
           "horns": HORNS, "results": out},
          open(os.path.join(HERE, "horizons_recheck.json"), "w"), indent=1)
print("wrote horizons_recheck.json")
print("epoch:", EPOCH)
