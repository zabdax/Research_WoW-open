# Forensic Bounds and Identifiability Limits on the Origin of the Wow! Signal

Reproducibility package for Shaad & Khan, *The Wow! Signal: Exploring the
Boundaries of Evidence and Inference* (submitted to the International
Journal of Astrobiology).

This repository contains the manuscript sources, figures, analysis scripts,
and extracted values needed to regenerate every headline number and figure
from frozen public inputs. It does **not** contain the private Hobart
donor archive (raw data, thresholds, candidate lists) — see
“Data access” below.

## Reproduce the headline results

Requirements: Python 3.12; `pip install numpy astropy scipy astroquery
matplotlib pillow` (pinned versions: `tools/audit/environment/`, staged
as `papers/archive/paper-rev2/zenodo/dependency_versions.txt`).
A network connection is needed only for the live JPL-Horizons requery;
everything else runs offline (the HI4PI check additionally needs the
public CDS file J/A+A/594/A116 `HPX_121.fits`, linked — not bundled).

From the repository root:

1. `python papers/archive/paper-rev2/scripts/reproduce_main_numbers.py`
   → `scripts/main_numbers.json`: brightness-temperature bounds
   (17206.72 K nominal / 11707.46 K floor), EIRP constant, Kipping–Gray
   chain maxima (32.3 / 3.3 / 1.78%), kmax sweep, H5 selection demo
   (5.62% → 2.52%, integrated-likelihood ratio 0.65), Hobart 114.116 h.
2. `python papers/archive/paper-rev2/scripts/reproduce_figures_de.py`
   → Figs. 4–5. Figure generators (`rebuild_figB.py`, `regen_figA.py`,
   `regen_figC.py`, `plot_hi4pi.py`) take an optional output path.
3. `python papers/archive/paper-rev2/scripts/extend_hi4pi.py` (needs the
   HI4PI FITS) → `hi4pi_extended.json`: ten spectra ≤0.10 K/channel and
   the 164.1 K/channel persistent-source expectation.
4. `python papers/archive/paper-rev2/scripts/verify_all_numbers.py` — the
   end-to-end gate: asserts every quoted number (exit 0 iff all pass),
   including `h5_independent_audit.py` (independent event-level Monte
   Carlo + 120-grid evidence check), `horizons_recheck.py` (live JPL
   query: -3191/-3364/-2749/-2922 s; r = 4.73/4.56 AU), `sep_on_sky.py`
   (great-circle 11.83/12.47/10.43/11.04°), and `freq_prior_compare.py`
   (5.05e-6 vs 7.64e-5).
5. Full number↔figure↔script traceability:
   `papers/archive/paper-rev2/scripts/number_figure_manifest.md`.

## Manuscripts

- `papers/archive/paper-rev2/ija_manuscript/manuscript.tex` — IJA (Cambridge
  CSL class) submission source; compile with pdfLaTeX twice. `overleaf_upload.zip`
  is the direct Overleaf bundle (tex + class + figures).
- `papers/archive/paper-rev2/main.tex` — AASTeX mirror (same content,
  `aastex_overleaf_upload.zip` bundles it with class/.bst/.bib/figures).

## Data access

- Public, cited by identifier: HI4PI (CDS J/A+A/594/A116), Kipping–Gray
  code+chains (MIT, mirrored here under `data/kipping_master_dl/wow-main/`
  with original LICENSE), Méndez et al. arXiv e-prints.
- Shared here: Hobart session-span/pointing table
  (`research/sources/ellingsen_hobart/extracted/campaign_exposure.csv`).
- Restricted (not in this repo): detection thresholds, candidate-generation
  rules, candidate lists, raw reduction products. Access inquiries via the
  authors, subject to donor consent.

## License / citation

Code: MIT (`LICENSE`). Data/figures/manuscript text: CC-BY-4.0. When citing,
please cite the paper and the Zenodo record (DOI in `.zenodo.json` once
minted; see `CITATION.cff`).
