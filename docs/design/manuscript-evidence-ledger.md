# WoW! Signal Project — Manuscript Evidence Ledger & Claim Audit

## 1. Authoritative Manuscript Evidence Ledger

| Claim ID | Hyp. | Claim | Value/Result | Provenance | Source | Calculation | Assumptions | Uncertainty | Permitted Wording | Forbidden Wording | Reviewer Vulnerability |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **C-H5-01** | H5 | K&G stochastic repeater MAP likelihood reproduction | ~1.4–1.6% | REPRODUCED | `src/kg_validation.py`, `archive/exploratory/run_h5_a.py` | Exact grid integration / Un-truncated Monte Carlo | Poisson process, uniform baseline | Grid-resolution dependent variation | "An independently reconstructed implementation yields a MAP likelihood in the approximately 1.4–1.6% range, compared with the published 1.78%, with the discrepancy attributable to finite truncation in the historical numerical implementation." | "The K&G result is wrong and corrected to 1.42%" | "Numerical precision does not alter the core scientific conclusion" |
| **C-H3-01** | H3 | Minimum required brightness temperature | $T_B \geq 17,206$ K | PHYSICAL INFERENCE | `H3_PHYSICAL_BOUNDS.md` | Rayleigh-Jeans with upper-limit $\Omega$ and lower-limit $S_\nu$ | Circular source geometry limit | Strict mathematical lower bound | "Under the observed geometric and flux constraints, the source requires a brightness temperature $T_B \geq 1.7 \times 10^4$ K, mandating a non-thermal emission mechanism." | "H3 is proven to be a maser" / "The flux requires an enhancement factor of $2.5 \times 10^5$" | "The geometric upper limit might overestimate the true solid angle, making the true $T_B$ even larger" |
| **C-H2-01** | H2 | 335P/Gibbs geometric intersection | UNTESTED | UNKNOWN | `H2_GEOMETRY_RESULT.md` | N/A | N/A | Missing authoritative ephemeris | "The proposed comet candidate 335P/Gibbs remains geometrically untested from the surviving authoritative data." | "335P is ruled out" / "The comet hypothesis is ruled out globally" | "Why not just use an external ephemeris tool for the paper?" (Violates strict evidence freeze) |
| **C-H1-01** | H1 | Terrestrial RFI mechanism | UNRESOLVED | UNKNOWN | `PHASE4_IDENTIFIABILITY_FINAL.md` | N/A | N/A | Unconstrained parameter space | "No specific RFI mechanism capable of reproducing the narrowband 72-second transit profile without harmonics has been quantitatively demonstrated." | "RFI is ruled out" | "Just because a specific mechanism isn't modeled doesn't mean RFI is unlikely" |
| **C-H4-01** | H4 | Artificial beam EIRP | Conditional | CONDITIONAL | `PHASE4_IDENTIFIABILITY_FINAL.md` | Radiometric distance relation | N/A | Unconstrained distance prior | "An artificial beam origin would require an EIRP scaling quadratically with distance to produce the observed $\geq 256$ Jy flux." | "The probability of an ETI beam is X" | "This is a trivial restatement of the inverse square law" |
| **C-OBS-01** | ALL | Arecibo II parameter bounds | $\nu=1420.726$ MHz, $S_\nu \geq 256$ Jy, $\theta \leq 1.9'$ | DIRECT | `mendez_evidence_vector.yaml` | Extracted from Mendez 2025 | N/A | Strictly censored flux limit | "The Arecibo II parameters establish a frequency of 1420.726 MHz and a strictly censored flux lower bound of $\geq 256$ Jy." | "The Wow signal flux was 256 Jy" | "Mendez 2025 might have calibration uncertainties not fully captured" |

---

## 2. H5 Claim Audit

**Discrepancy Characterization:**
The manuscript must explicitly distinguish between the published K&G result (1.78%), the project's exact Fortran-emulated reproduction showing the `kmax=100` normalization distortion, and the independent mathematical implementations (yielding ~1.4–1.6% depending on grid resolution).

**Scientific Effect:** 
The discrepancy does **not** alter the overarching scientific interpretation. The hypothesis remains mildly supported by the Big Ear event but heavily penalized by subsequent null detections.

**Publication-Safe Wording:** 
> "An independently reconstructed implementation yields a MAP likelihood in the approximately 1.4–1.6% range, compared with the published 1.78%, with the discrepancy attributable to finite truncation in the historical numerical implementation."

**Forbidden Wording:**
Do not use the phrase "corrected K&G result." Do not claim the discrepancy changes the scientific conclusion.

---

## 3. H3 Claim Audit

**Brightness Temperature Logic:**
- **Observed:** Flux density $\geq 256$ Jy, Angular size $\leq 1.9'$.
- **Derived:** Using the Rayleigh-Jeans approximation, because the solid angle is an upper limit and flux is a lower limit, the resulting brightness temperature is a strict lower bound ($T_B \geq 17,206$ K).
- **Physical Inference:** Standard thermal emission from cold HI gas yields $T_k \sim 100$ K. A requirement of $\geq 1.7 \times 10^4$ K physically mandates non-thermal stimulated emission (maser/superradiance).
- **Population Inference:** Determining the likelihood of such extreme transient masers requires a population prior, which is currently unconstrained.

**Forbidden Elements:**
- Do not convert the physical requirement into an H3 posterior probability.
- Do not include the internal illustrative `$2.5 \times 10^5$` enhancement factor in the main manuscript conclusions, as its reference configuration (1 mJy at 400 pc) lacks independent astrophysical justification.

---

## 4. H2 Claim Audit

**Geometric Status:**
The project deliberately refused to generate an unverified ephemeris for candidate 335P/Gibbs. Because an authoritative JPL Horizons cache for August 15, 1977, was not present in the frozen evidence vector, the intersection check remains `blocked`.

**Publication-Safe Wording:**
> "The proposed comet candidate 335P/Gibbs remains untested from the surviving authoritative project data."

**Forbidden Wording:**
Do not write "335P is ruled out." Do not write "The comet hypothesis is ruled out."

---

## 5. H1 Claim Audit

**RFI Status:**
No specific instrumental or terrestrial RFI mechanism has been quantitatively demonstrated to produce the exact 72-second sidereal tracking profile, narrowband nature, and lack of harmonics.

**Publication-Safe Wording:**
> "No specific RFI mechanism has been quantitatively demonstrated to reproduce the exact observed characteristics."

**Forbidden Wording:**
Do not equate "no specific mechanism demonstrated" with "RFI is ruled out."

---

## 6. H4 Claim Audit

**Conditional Status:**
H4 physical feasibility relies purely on conditional radiometric equations (required EIRP as a function of assumed distance and beam divergence). 

**Publication-Safe Wording:**
State the physical feasibility requirements conditionally.

**Forbidden Wording:**
Do not assign an ETI population probability or a Bayesian likelihood to H4.

---

## 7. H5 Follow-up Data Audit

**1998/99 Hobart:**
- *Published:* Gray & Ellingsen 2002 explicitly bounds non-detections for periods $<14$ hr at a 5.9$\sigma$ threshold.
- *Reconstructable:* The published non-detection constraint is statistically usable.
- *Unusable:* The raw data cannot be end-to-end processed locally due to missing 1998 Fortran kernels.

**2010–2014 Hobart:**
- *Survives:* Pointing geometries and exposure durations.
- *Missing:* The detection thresholds ($P_e$, SNR) and the candidate lists evaluated by Bob Gray.
- *Conclusion:* Because we do not know what constituted a "detection," the surviving exposure information is **insufficient to construct the required selection function**.

---

## 8. Why a Five-Way Posterior is Not Reported

The project explicitly disables the unified five-way Bayesian posterior (`confirmatory_comparison_enabled: false`) for the following rigorous epistemic reasons:
- **H5** lacks a reconstructable selection function for the modern Hobart campaigns.
- **H4** lacks a defensible population prior.
- **H2** remains geometrically unresolved for the primary proposed candidate due to missing authoritative ephemeris data.
- **H3** has strict physical constraints but no established population likelihood.
- **H1** lacks a complete mechanism likelihood.

**Conclusion:** 
> **The surviving evidence supports quantitative constraints on individual hypotheses, but does not identify a defensible common probabilistic framework for a five-way posterior comparison.**

---

## 9. "Do Not Overclaim" Table

| Tempting statement | Why it is invalid | Publication-safe alternative |
| :--- | :--- | :--- |
| H3 is favored | No population likelihood | H3 requires extreme non-thermal emission under the adopted constraints |
| 1.42% is the corrected K&G result | Historical implementation discrepancy needs careful characterization | Independent reconstruction gives ~1.4–1.6% |
| 335P is ruled out | Ephemeris unavailable | 335P remains untested from the surviving authoritative data |
| RFI is ruled out | No mechanism likelihood | No specific RFI mechanism has been demonstrated |
| H5 is ruled out | Follow-up selection function incomplete | Surviving follow-up data impose limited/partial constraints |
| Five-way posterior is impossible forever | Future evidence could change identifiability | Five-way posterior is not identifiable from current evidence |

---

## 10. Manuscript-Ready Numerical Table

| Quantity | Value | Uncertainty/Limit | Units | Source | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Wow! Frequency | 1420.726 | $\pm 0.005$ | MHz | Mendez (2025) | Directly Observed / Reconstructed |
| Wow! Flux Density | 256 | $\geq$ (lower bound) | Jy | Mendez (2025) | Directly Observed / Reconstructed |
| Wow! Angular Size | 1.9 | $\leq$ (upper bound) | arcmin | Mendez (2025) | Directly Observed / Reconstructed |
| H3 Brightness Temperature | 17,206 | $\geq$ (lower bound) | K | Project (Phase 4) | Derived / Physical Inference |
| K&G H5 MAP Likelihood | ~1.4–1.6 | bounded range | % | Project (Phase 4) | Derived / Independent Reconstruction |

---

## 11. Final Manuscript Thesis

**What has this project actually established?**

This project has systematically audited the evidentiary foundation of the 1977 Wow! signal, prioritizing rigorous provenance control and strict limitations on historical reconstructions. By freezing the observational parameters derived from recent forensic reconstructions (Arecibo II), we established quantitative physical constraints on the leading hypotheses. Specifically, the strictly censored lower-bound flux ($\geq 256$ Jy) combined with the angular size upper-bound ($\leq 1.9'$) physically mandates that any interstellar hydrogen (H3) origin must arise from extreme non-thermal stimulated emission (maser), as the required brightness temperature ($T_B \geq 1.7 \times 10^4$ K) strictly rules out spontaneous thermal emission from cold HI clouds. 

Furthermore, we conducted an independent mathematical reconstruction of the stochastic repeater hypothesis (H5). While we isolated a numerical integration artifact in the originally published numerical grid that slightly elevates the MAP likelihood, the core statistical interpretation remains robust. Crucially, however, we demonstrate explicit statistical non-identifiability regarding subsequent follow-up campaigns. The absence of specific selection functions (detection thresholds and candidate outcomes) for the 2010–2014 archival campaigns renders those datasets mathematically unusable for updating the Bayesian likelihood. 

Consequently, we formally refuse to manufacture a heuristic five-way Bayesian posterior. The project successfully delineates the precise boundary between what the surviving historical evidence can quantitatively establish (physical bounds and partial likelihoods) and what remains permanently or practically unresolved without new external evidence or astrophysical priors. 

---

## 12. STOP CONDITION

**The `MANUSCRIPT_EVIDENCE_LEDGER.md` is complete.** 
No further scientific investigation, archival searches, literature searches, or hypothesis modifications will be performed. The next step is manuscript architecture and writing.
