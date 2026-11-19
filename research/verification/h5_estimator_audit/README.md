# Kipping–Gray estimator audit

This folder contains the deterministic source/grid audit, its JSON result, a compiled single-cell diagnostic summary, the separate exact-probability numerical cross-check, and the upstream source/grid files needed to rerun the audit. The bundled upstream source is licensed under the accompanying LICENSE.

Run from this directory with Python 3 and NumPy:

\`\`\`powershell
python audit_h5_estimator.py
\`\`\`

The audit reads \`reference_source/wow.f90\`, \`reference_source/output_grid.dat\`, and \`reference_source/mcmc.nb\`. It does not reproduce the complete released grid or MCMC chains. The source loop covers 150 duration indices by 160 rate indices while the released grid has 160 by 160 rows. The grid's coordinate values are natural logarithms despite log10-oriented headers/plot labels.

The corrected branch audit finds 10,600 of 24,000 source cells enter the Monte Carlo branch and 13,400 use a fixed \`0.000999\` value. At the released-grid maximum cell, 30 compiled repeated runs gave estimates from 0.143 to 0.455 (mean 0.259, sample SD 0.059); the exact coverage probability under the audited event rule is 0.315 and the released grid stores 0.5. This is a finite stochastic single-cell diagnostic, not proof of a release/source mismatch and not a full estimator reproduction.

The exact interval-union probability is an independent model comparison, not a validation of Kipping & Gray's released likelihood or posterior. Donor-restricted Hobart raw observations are not included. File hashes are in SHA256SUMS.txt.
