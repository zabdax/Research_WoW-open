# Zenodo upload — full analysis reproducibility package (HUMAN ACTION REQUIRED)

The manuscript's Data Availability section cites this upload as
"archived at Zenodo (DOI to be inserted at acceptance)". Minting the DOI
is a human step (requires a Zenodo account + the authors' metadata).

## Files in this directory (upload as-is)

- `reproduce_main_numbers.py` — headline numbers → `main_numbers.json`
  (H3/H4 bounds, H5 chains verification, kmax sweep, selection demo, Fig. 6).
- `reproduce_figures_de.py` — H5 emulator figures (Figs. 4–5).
- `rebuild_figB.py` — Fig. 2 (transit data vs 36-s FWHM model).
- `regen_figA.py`, `regen_figC.py`, `plot_hi4pi.py` — Figs. 1, 3, 7.
- `extend_hi4pi.py` + `hi4pi_extended.json` — Sec. 6.5 HI4PI check
  (reads the public CDS HI4PI pixel file J/A+A/594/A116).
- `horizons_recheck.py` — live JPL-Horizons requery for the Sec. 5.2 offsets.
- `verify_all_numbers.py` — end-to-end safeguard: asserts every number
  quoted in the paper (28 checks; exit 0 iff all pass).

Figure PDFs themselves are in the article source; these scripts regenerate
them from the frozen inputs (pinned environment: Python 3.12, numpy,
astropy, scipy, astroquery, matplotlib, Pillow — see
`dependency_versions.txt`, copied from the repo's environment audit).

External inputs (NOT bundled — fetch as described; all public):
- CDS HI4PI pixel file J/A+A/594/A116 (`HPX_121.fits`, 247,213,440 bytes,
  SHA256 BC8E93…): read by `extend_hi4pi.py`.
- Kipping & Gray chain release (MIT-licensed, ~20 MB):
  https://github.com/davidkipping/wow (`wow.f90`, `output_grid.dat`,
  `mcmc.nb`, three `mcmc_chain_thinner_*.dat` files): read for the
  Sec. 8.2 chain-maxima verification. In-repo mirror (if present):
  `data/kipping_master_dl/wow-main/`.
- JPL Horizons (network query at audit time): `horizons_recheck.py`
  re-queries 266P/335P vectors at the event epoch; needs astroquery +
  network. NOTE: numeric id 90001326 no longer resolves to 335P/Gibbs —
  the script queries by designation; see its header.

## Reproduce the headline results (in order)

1. `python reproduce_main_numbers.py` → writes `main_numbers.json`:
   TB 17206.72 K / floor 11707.46 K; EIRP constant 3.06e14 W;
   chain maxima 32.3 / 3.3 / 1.78%; kmax sweep (~0.8% at 100, 1.58%
   converged); selection demo 5.62% → 2.52%, evidence factor 0.65;
   Hobart span 114.116 h. (Also writes Fig. 6.)
2. `python reproduce_figures_de.py` → Figs. 4–5 (emulator surface,
   kmax convergence; prints the same maxima).
3. `python rebuild_figB.py`, `regen_figA.py`, `regen_figC.py`,
   `plot_hi4pi.py` → Figs. 2, 1, 3, 7 (each takes an optional output path).
4. `python extend_hi4pi.py` → `hi4pi_extended.json` (ten spectra,
   persistent-source 164.1 K/channel; needs the HI4PI FITS above).
5. `python hi4pi_geometry_test.py` → beam-coupling grid over
   1.9′–40′ elongations × narrow/filled/broad line cases (Sec. 6.5).
6. `python horizons_recheck.py` → live Horizons offsets
   (-3191/-3364/-2749/-2922 s) and ranges (4.73/4.56 AU).
7. `python sep_on_sky.py` → on-sky separations 11.9/12.5/10.6/11.2 deg.
8. `python freq_prior_compare.py` → uniform 5.05e-6 vs log-uniform
   7.64e-5 (15.1x).
9. `python verify_all_numbers.py` → 28-check safeguard over items 1–8
   (exit 0 iff all pass); `python h5_independent_audit.py` →
   independent event-level Monte Carlo + 120-grid evidence audit.

## Hobart 2010–2014 archive: what is shared vs restricted

- Shared for verification: `campaign_exposure.csv` (session spans,
  pointings, spectral configurations as preserved).
- Restricted / not preserved: detection thresholds, candidate-generation
  and verification rules, candidate outcome catalogue, and the raw
  reduction products attributed to Bob Gray's analysis layer. Without
  these the exposure cannot be treated as a null experiment (the paper's
  central identifiability point). Access inquiries: via the authors,
  subject to donor consent (see manuscript Sec. 12).

## Upload steps (5 minutes)

1. Log in at https://zenodo.org/ → New upload.
2. Upload the two files above.
3. Suggested metadata:
   - Title: "HI4PI check at the Wow! signal locale — reproduction data
     for Forensic Bounds and Identifiability Limits on the Origin of
     the Wow! Signal"
   - Authors: Zubayer Hasan Shaad; S M Shadman Khan
     (add ORCIDs at upload time)
   - Description: "Reproduction script and extracted HI4PI spectra
     supporting Section 6.5 (HI4PI Check at the Event Velocity).
     Input: CDS catalogue J/A+A/594/A116 file HPX_121.fits
     (247,213,440 bytes, SHA256 BC8E93…)."
   - License: MIT (code) — note the JSON as CC-BY in the description.
4. Publish → copy the DOI → replace "(DOI to be inserted at acceptance)"
   in `ija_manuscript/manuscript.tex` (Data Availability) with the DOI,
   rebuild, and re-verify (2× pdflatex, 0 errors).
