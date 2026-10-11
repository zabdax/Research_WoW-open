"""Great-circle on-sky separations for the four candidate/horn pairs (Sec. 5.2).

Exact spherical haversine (NOT the flat-sky RA*cos(dec) approximation) between
the frozen Mendez II Table 4 horn coordinates and the Horizons ephemeris
positions quoted in Sec. 5.2. RA in h:m:s, Dec in deg (negative south).

Run from repo root: .venv/Scripts/python.exe papers/archive/paper-rev2/scripts/sep_on_sky.py
"""
import math

HORNS = {"pos": ((19, 25, 2.0), -(26 + 57 / 60 + 18 / 3600)),
         "neg": ((19, 27, 55.0), -(26 + 57 / 60 + 13 / 3600))}
CANDS = {"266P": ((18, 31, 50.7), -(27 + 21.7 / 60)),
         "335P": ((18, 39, 12.5), -(29 + 37.0 / 60))}


def deg(ra_hms, dec_d):
    h, m, s = ra_hms
    return (h + m / 60 + s / 3600) * 15.0, dec_d


def haversine(ra1, dc1, ra2, dc2):
    r1, d1, r2, d2 = map(math.radians, (ra1, dc1, ra2, dc2))
    h = (math.sin((d2 - d1) / 2) ** 2 + math.cos(d1) * math.cos(d2)
         * math.sin((r2 - r1) / 2) ** 2)
    return 2 * math.asin(math.sqrt(h)) * 180.0 / math.pi


for cn, (cra, cdc) in CANDS.items():
    ra_c, dc_c = deg(cra, cdc)
    for hn, (hra, hdc) in HORNS.items():
        ra_h, dc_h = deg(hra, hdc)
        print(f"{cn}-{hn}: great-circle sep "
              f"{haversine(ra_c, dc_c, ra_h, dc_h):.2f} deg")
