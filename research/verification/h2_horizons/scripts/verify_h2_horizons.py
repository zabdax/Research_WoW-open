#!/usr/bin/env python3
"""Reproducibly query JPL Horizons for the two named Wow! comet candidates.

The event epoch is the adopted archival time 1977-08-16 03:16:06 UTC.
Horizons formal uncertainties describe the current fitted orbit solution; they
do not include all long-baseline model or non-gravitational uncertainties.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESULTS = ROOT / "results"
API = "https://ssd.jpl.nasa.gov/api/horizons.api"
LOOKUP_API = "https://ssd.jpl.nasa.gov/api/horizons_lookup.api"
EPOCH = "1977-08-16 03:16:06"
OBJECTS = {
    "266P": {"name": "266P/Christensen", "lookup_spkid": "1002425", "command": "DES=266P;CAP"},
    "335P": {"name": "335P/Gibbs", "lookup_spkid": "1003007", "command": "DES=335P;CAP"},
}
CENTERS = {
    "geocentric": {"CENTER": "500@399"},
    # Geodetic site coordinates are east-positive longitude, latitude, km.
    "big_ear_topocentric": {
        "CENTER": "coord@399",
        "COORD_TYPE": "GEODETIC",
        "SITE_COORD": "-83.0391666667,40.0027777778,0.26",
    },
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def query(object_name: str, center: dict[str, str]) -> bytes:
    params = {
        "format": "text",
        # CAP selects the latest-apparition solution for the stated designation.
        "COMMAND": f"'{object_name}'",
        "OBJ_DATA": "'YES'",
        "MAKE_EPHEM": "'YES'",
        "EPHEM_TYPE": "'OBSERVER'",
        **{k: f"'{v}'" for k, v in center.items()},
        "TLIST": f"'{EPOCH}'",
        "TIME_TYPE": "'UT'",
        "QUANTITIES": "'1,19,20,36,37,38,47'",
        "CSV_FORMAT": "'YES'",
        "ANG_FORMAT": "'HMS'",
        "EXTRA_PREC": "'YES'",
    }
    url = API + "?" + urlencode(params)
    req = Request(url, headers={"User-Agent": "WowSignalProvenanceAudit/1.0"})
    with urlopen(req, timeout=60) as response:
        payload = response.read()
    text = payload.decode("utf-8", errors="replace")
    if "$$SOE" not in text or "$$EOE" not in text:
        raise RuntimeError(f"Horizons returned no ephemeris table for {object_name}:\n{text[:2000]}")
    return payload


def lookup(target: dict[str, str], label: str) -> tuple[bytes, dict]:
    params = {"sstr": label, "group": "com"}
    req = Request(LOOKUP_API + "?" + urlencode(params), headers={"User-Agent": "WowSignalProvenanceAudit/1.0"})
    with urlopen(req, timeout=60) as response:
        payload = response.read()
    data = json.loads(payload.decode("utf-8"))
    matches = [row for row in data.get("result", []) if row.get("pdes") == label]
    if len(matches) != 1 or matches[0].get("spkid") != target["lookup_spkid"]:
        raise RuntimeError(f"Unexpected JPL lookup result for {label}: {data}")
    return payload, data


def parse_ephemeris(raw: bytes) -> dict[str, object]:
    text = raw.decode("utf-8", errors="replace")
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if "$$SOE" in line) + 1
    end = next(i for i, line in enumerate(lines[start:], start) if "$$EOE" in line)
    rows = list(csv.reader(io.StringIO("\n".join(lines[start:end]))) )
    if not rows or len(rows[0]) < 2:
        raise RuntimeError("Could not parse Horizons CSV ephemeris row")
    # Horizons CSV output is a single event row. Preserve raw cells as well as
    # their positional order because optional quantities may be unavailable.
    cells = [x.strip() for x in rows[0]]
    if len(cells) < 19:
        raise RuntimeError(f"Expected 19 CSV fields including sky motion, received {len(cells)}: {cells}")
    parsed = {
        "cells": cells,
        "utc": cells[0],
        "ra_j2000_hms": cells[3],
        "dec_j2000_dms": cells[4],
        "ra_deg": hms_to_deg(cells[3]),
        "dec_deg": dms_to_deg(cells[4]),
        "r_au": float(cells[5]),
        "rdot_km_s": float(cells[6]),
        "delta_au": float(cells[7]),
        "deltadot_km_s": float(cells[8]),
        "ra_3sigma_arcsec": float(cells[9]),
        "dec_3sigma_arcsec": float(cells[10]),
        "pos_smaa_3sigma_arcsec": float(cells[11]),
        "pos_smia_3sigma_arcsec": float(cells[12]),
        "pos_theta_deg": float(cells[13]),
        "pos_area_3sigma_arcsec2": float(cells[14]),
        "pos_rss_3sigma_arcsec": float(cells[15]),
    }
    parsed["sky_motion_arcsec_per_hour"] = float(cells[16]) * 60
    parsed["sky_motion_position_angle_deg"] = float(cells[17])
    parsed["relative_velocity_angle_deg"] = float(cells[18])
    return parsed


def hms_to_deg(value: str) -> float:
    fields = value.strip().split()
    if len(fields) != 3:
        raise ValueError(f"Expected HMS/DMS triple, got {value!r}")
    h, m, s = map(float, fields)
    sign = -1.0 if fields[0].startswith("-") else 1.0
    return sign * (abs(h) + m / 60 + s / 3600) * 15


def dms_to_deg(value: str) -> float:
    fields = value.strip().split()
    if len(fields) != 3:
        raise ValueError(f"Expected DMS triple, got {value!r}")
    d, m, s = map(float, fields)
    sign = -1.0 if fields[0].startswith("-") else 1.0
    return sign * (abs(d) + m / 60 + s / 3600)


def sky_separation_arcmin(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    a1, d1, a2, d2 = map(math.radians, (ra1, dec1, ra2, dec2))
    cos_sep = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(a1 - a2)
    return math.degrees(math.acos(max(-1.0, min(1.0, cos_sep)))) * 60


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)
    result: dict[str, object] = {
        "source": API,
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "event_epoch_utc": EPOCH + " UTC",
        "site": {"latitude_deg": 40 + 10 / 3600,
                 "longitude_east_deg": -(83 + 2 / 60 + 21 / 3600), "elevation_km": 0.26},
        "comparison_coordinates": {
            "arecibo_ii_table4_positive_horn": {"ra_hms": "19 25 02", "dec_dms": "-26 57 18"},
            "arecibo_ii_table4_negative_horn": {"ra_hms": "19 27 55", "dec_dms": "-26 57 13"},
            "public_summary_ra_only": ["19 25 26", "19 28 18"],
        },
        "objects": {},
        "caution": "Horizons formal 3-sigma errors are solution-dependent and do not capture every long-baseline or non-gravitational model uncertainty.",
    }
    for label, target in OBJECTS.items():
        object_name, lookup_spkid, command = target["name"], target["lookup_spkid"], target["command"]
        lookup_raw, lookup_json = lookup(target, label)
        lookup_path = DATA / f"horizons_lookup_{label}.json"
        lookup_path.write_bytes(lookup_raw)
        obj: dict[str, object] = {"requested_name": object_name, "lookup_spkid": lookup_spkid,
                                  "horizons_command": command,
                                  "lookup_file": str(lookup_path.relative_to(ROOT)),
                                  "lookup_sha256": sha256(lookup_path),
                                  "lookup_result": lookup_json["result"], "queries": {}}
        for center_name, center in CENTERS.items():
            raw = query(command, center)
            response_text = raw.decode("utf-8", errors="replace")
            if object_name.split("/")[0] not in response_text or "Target body name:" not in response_text:
                raise RuntimeError(f"Horizons command {command} did not resolve to {object_name}:\n{response_text[:1400]}")
            suffix = "" if center_name == "geocentric" else "_topocentric"
            out = DATA / f"horizons_{label}_19770816{suffix}.txt"
            out.write_bytes(raw)
            parsed = parse_ephemeris(raw)
            obj["queries"][center_name] = {
                "file": str(out.relative_to(ROOT)),
                "sha256": sha256(out),
                "parsed": parsed,
            }
            time.sleep(0.25)
        table = result["comparison_coordinates"]
        comparisons = {}
        for horn in ("arecibo_ii_table4_positive_horn", "arecibo_ii_table4_negative_horn"):
            ref = table[horn]
            rra, rdec = hms_to_deg(ref["ra_hms"]), dms_to_deg(ref["dec_dms"])
            comparisons[horn] = {
                "angular_separation_arcmin": {
                    name: sky_separation_arcmin(values["ra_deg"], values["dec_deg"], rra, rdec)
                    for name, values in ((name, data["parsed"]) for name, data in obj["queries"].items())
                },
                "delta_ra_seconds_time": {
                    name: (values["ra_deg"] - rra) * 240
                    for name, values in ((name, data["parsed"]) for name, data in obj["queries"].items())
                },
                "delta_dec_arcmin": {
                    name: (values["dec_deg"] - rdec) * 60
                    for name, values in ((name, data["parsed"]) for name, data in obj["queries"].items())
                },
            }
        obj["separations_from_arecibo_ii_horns"] = comparisons
        qgeo = obj["queries"]["geocentric"]["parsed"]
        qtopo = obj["queries"]["big_ear_topocentric"]["parsed"]
        obj["topocentric_minus_geocentric"] = {
            "angular_parallax_arcsec": 60 * sky_separation_arcmin(qgeo["ra_deg"], qgeo["dec_deg"],
                                                                    qtopo["ra_deg"], qtopo["dec_deg"]),
            "delta_ra_seconds_time": (qtopo["ra_deg"] - qgeo["ra_deg"]) * 240,
            "delta_dec_arcsec": (qtopo["dec_deg"] - qgeo["dec_deg"]) * 3600,
        }
        summary_ra = table["public_summary_ra_only"][0 if label == "266P" else 1]
        public_ra_deg = hms_to_deg(summary_ra)
        obj["public_summary_ra_only_sensitivity"] = {
            "public_ra_hms": summary_ra,
            "delta_ra_seconds_time_geocentric": (qgeo["ra_deg"] - public_ra_deg) * 240,
            "delta_ra_seconds_time_topocentric": (qtopo["ra_deg"] - public_ra_deg) * 240,
            "note": "The cited public summary provides RA only; no two-dimensional angular separation is inferred from it.",
        }
        result["objects"][label] = obj
    output = RESULTS / "h2_ephemeris_verification.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    generated = [output, *DATA.glob("horizons_*_19770816*.txt"), *DATA.glob("horizons_lookup_*.json")]
    manifest = RESULTS / "h2_SHA256SUMS.txt"
    manifest.write_text("".join(f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}\n"
                                for path in sorted([Path(__file__), *generated])), encoding="utf-8")
    print(json.dumps({"summary": "Retrieved four exact-epoch Horizons responses", "result": str(output),
                      "sha256_manifest": str(manifest),
                      "sha256": {str(p.relative_to(ROOT)): sha256(p) for p in
                                 sorted([Path(__file__), *generated, manifest])}}, indent=2))


if __name__ == "__main__":
    main()
