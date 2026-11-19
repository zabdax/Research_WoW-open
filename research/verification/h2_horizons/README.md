# Exact-epoch JPL Horizons ephemeris verification

This self-contained package archives the exact-epoch ephemeris check for 266P/Christensen and 335P/Gibbs at 1977-08-16 03:16:06 UTC. It includes geocentric and OSU Big Ear topocentric queries, raw unmodified JPL Horizons and Lookup API responses, and the parsed JSON summary.

Run from this directory with Python 3 and network access to the official Horizons API:

```powershell
python scripts/verify_h2_horizons.py
```

The script reads and writes files under `data/` and `results/`, matching the paths recorded in the JSON. The formal 3-sigma POS RSS uncertainties are 4.075 arcsec (266P) and 10.140 arcsec (335P). These formal orbit-fit uncertainties do not constitute a complete error budget for multi-decade backward propagation or non-gravitational effects.

`results/h2_SHA256SUMS.txt` lists SHA-256 hashes for the script and data/result payloads. The manifest does not hash itself or this README.
