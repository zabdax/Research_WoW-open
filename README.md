# The Wow! Signal: forensic bounds and limits of inference

This repository contains source material, data references, and reproducibility artifacts for an independent research project examining competing explanations of the 1977 Wow! signal. The analysis is deliberately cautious: it does not identify a unique cause or produce a normalized five-hypothesis posterior where the underlying quantities are not commensurate.

## Repository status

The Zenodo v1.0.0 record and manuscript files already present in the repository are earlier snapshots. The current manuscript revision is still under author review and has not been deposited as a new Zenodo version. The audit materials added in this branch document recent H2 (comet ephemeris) and H5 (repeating-beacon estimator) checks. They do not constitute a full reproduction of the released Kipping–Gray MCMC chains or a new observational data release.

## Recent verification artifacts

### H2: exact-epoch comet ephemerides

`research/verification/h2_horizons/` contains the query script, raw geocentric and Big Ear topocentric JPL Horizons responses, lookup responses, structured output, and SHA-256 manifest for 266P/Christensen and 335P/Gibbs at 1977-08-16 03:16:06 UTC.

The archived calculation gives formal 3-sigma POS RSS uncertainties of 4.075 arcsec and 10.140 arcsec, respectively, and horn separations of 10.428–12.530 degrees. These are formal orbit-fit uncertainties; they do not provide a complete uncertainty budget for multi-decade backward propagation or non-gravitational effects. See the folder README and JSON for details.

### H5: Kipping–Gray estimator audit

`research/verification/h5_estimator_audit/` contains the source/grid audit, upstream files needed by the audit, numerical cross-checks, compiled single-cell diagnostic, and JSON outputs.

The audit identifies a 150-by-160 source loop versus a 160-by-160 released grid, and a mismatch between log-column labels and the natural-log coordinate values. Its compiled check is a repeated, stochastic diagnostic at one grid cell. The full released grid and MCMC chains have not been independently reproduced. The exact interval-union calculation in this project is a separate model and should not be mistaken for a validation of the published chain estimator.

## Reproducibility

The H2 script requires Python 3 and network access to the official JPL Horizons API:

```powershell
python research/verification/h2_horizons/scripts/verify_h2_horizons.py
```

The H5 source audit requires Python 3 and NumPy:

```powershell
python research/verification/h5_estimator_audit/audit_h5_estimator.py
```

See each folder's README for inputs, output locations, limitations, and checksums. Raw Hobart detection products and donor-restricted records are not included; only previously shared session-span metadata may be present elsewhere in the repository.

## Manuscript files

The manuscript copies currently in the repository are historical snapshots. They should not be treated as the current submission candidate. The latest local review package is not included in this update because its corresponding-author block contains a residential address and telephone number. A public manuscript copy should be prepared with those details removed or replaced before release.

## Citation

For the earlier archived software release, see [Zenodo v1.0.0](https://doi.org/10.5281/zenodo.23301789). That record predates the current audit artifacts and should not be cited as their archival deposit.

No result in this repository establishes a definitive attribution of the Wow! signal.
