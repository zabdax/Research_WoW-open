# WoW! Signal Project — Manuscript Architecture

## 1. Manuscript Objective
To present a rigorous forensic audit of the historical evidence for the 1977 Wow! signal, prioritizing strict epistemic control and establishing exactly what the surviving observational data can quantitatively constrain for five primary hypotheses, and precisely where statistical identifiability ends.

## 2. Central Scientific Narrative
The paper will eschew the formulation of a heuristic "winner" among hypotheses. Instead, the narrative maps the progression of information across four levels: Direct Observational Evidence (Level A), Reconstructed Quantities (Level B), Physical Inference (Level C), and Population/Statistical Inference (Level D). The central conclusion is that the surviving evidence supports strong quantitative physical bounds on individual hypotheses (e.g., extreme brightness temperatures for H3), but does not contain sufficient selection-function metadata or population priors to construct a defensible common probabilistic framework (a five-way posterior comparison).

## 3. Complete Section/Subsection Architecture
### 1. Introduction
- 1.1 The Wow! signal
- 1.2 The problem of heterogeneous historical evidence
- 1.3 Objective and scope of this work
### 2. Evidence, Provenance, and Identifiability Framework
- 2.1 Evidence freeze and provenance classes
- 2.2 Direct observations versus reconstruction
- 2.3 Censored quantities and missing metadata
- 2.4 Selection functions and likelihood identifiability
### 3. Observational and Archival Evidence (Level A)
- 3.1 Big Ear observations and Arecibo II parameter reconstruction
- 3.2 1998/99 Hobart archival follow-up
- 3.3 2010–2014 Hobart archival pointing constraints
### 4. H1 — Instrumental/RFI Origin
- 4.1 Required signal characteristics
- 4.2 Instrumental/RFI mechanisms considered
- 4.3 Quantitative constraints and unidentifiable parameters
### 5. H2 — Cometary Origin
- 5.1 Geometric and temporal requirements
- 5.2 Status of the 335P/Gibbs ephemeris test
- 5.3 Identifiability limitations
### 6. H3 — Interstellar HI Cloud / Maser Flare
- 6.1 Frozen Arecibo II constraints
- 6.2 Brightness-temperature lower-bound derivation
- 6.3 Thermal HI versus non-thermal emission physical inference
### 7. H4 — Artificial Power-Beam Leakage
- 7.1 Radiometric requirements
- 7.2 EIRP conditional feasibility
- 7.3 Absence of a population prior
### 8. H5 — Stochastic Repeating ETI Beacon
- 8.1 The Kipping & Gray (2022) model
- 8.2 Historical numerical implementation and grid truncation
- 8.3 Independent mathematical reconstruction and discrepancy
- 8.4 Hobart 2010–2014 selection-function identifiability
### 9. Cross-Hypothesis Comparison and Statistical Identifiability
- 9.1 Missing likelihoods and population priors
- 9.2 Selection-function dependence
- 9.3 Why a five-way Bayesian posterior is not reported
### 10. Discussion
- 10.1 What this study establishes and does not establish
- 10.2 Importance of provenance in historical SETI analysis
- 10.3 Future decisive observations
### 11. Conclusion

## 4. Section-by-Section Scientific Content Plan
- **Section 2:** Define how the project enforces strict bounds (e.g., $S_\nu \geq 256$ Jy). Explain that an absent candidate list does not equate to zero candidates. 
- **Section 3:** Establish the Arecibo II frozen parameters (C-OBS-01). Clearly distinguish between the published 1998/99 null result and the locally reconstructable exposure times from the 2010-2014 campaign.
- **Section 4:** H1 is characterized by the 72s transit profile and narrowband nature. No specific RFI mechanism has quantitative support, leaving it unresolved, but not ruled out (C-H1-01).
- **Section 5:** Discuss the J2000 horn geometries. Conclude that 335P is untested because an authoritative ephemeris cache is missing (C-H2-01).
- **Section 6:** Present the derivation $T_B = \frac{S_\nu c^2}{2k_B\nu^2\Omega} \geq 1.7 \times 10^4$ K. Discuss the absolute physical requirement for non-thermal (maser) amplification (C-H3-01).
- **Section 7:** Present the EIRP equation as a function of distance. Note that this cannot be translated to a probability (C-H4-01).
- **Section 8:** Explain the MAP likelihood of the stochastic repeater model. Contrast the published 1.78% with the independent ~1.4–1.6% (C-H5-01). Attribute the difference to the `kmax=100` normalization truncation. State explicitly why the 2010-2014 Bob Gray data cannot update this likelihood.
- **Section 9:** Synthesize the identifiability matrix. Emphasize that while physical and geometric bounds exist, the lack of selection functions and population priors prevents a unified posterior.
- **Section 10 & 11:** Highlight the necessity of rigorous forensic control in SETI. Clarify that the signal remains unexplained.

## 5. Claim-to-Section Traceability Matrix

| Claim ID | Manuscript Section | Figure | Table | Equation | Source/Code |
| -------- | ------------------ | ------ | ----- | -------- | ----------- |
| C-H5-01  | 8.3, 8.4           | Fig D, E | Table 3 | Eq 2, 3  | `archive/exploratory/run_h5_a.py`, `kg_validation.py` |
| C-H3-01  | 6.2, 6.3           | Fig C  | Table 1 | Eq 1     | `H3_PHYSICAL_BOUNDS.md` |
| C-H2-01  | 5.2                | None   | None  | None     | `H2_GEOMETRY_RESULT.md` |
| C-H1-01  | 4.3                | None   | None  | None     | `PHASE4_IDENTIFIABILITY_FINAL.md` |
| C-H4-01  | 7.2                | None   | None  | Eq 4     | `PHASE4_IDENTIFIABILITY_FINAL.md` |
| C-OBS-01 | 3.1                | Fig B  | Table 1 | None     | `mendez_evidence_vector.yaml` |

## 6. Figure Inventory
- **Figure A: Evidence/provenance architecture.** Schematic showing the pipeline from observations to identifiability boundaries.
- **Figure B: Wow! observational constraints.** A visual representation of the horn transit, censored flux, and frequency.
- **Figure C: H3 brightness-temperature constraint.** A plot of angular size vs. $T_B$, with a shaded exclusion region for thermal emission, marking the allowed $\geq 1.7 \times 10^4$ K parameter space.
- **Figure D: H5 likelihood reconstruction.** The likelihood surface (contour plot) in $(\lambda, T)$ space showing the MAP peak.
- **Figure E: H5 numerical discrepancy.** A 1D slice or convergence plot showing likelihood variation against $k_{max}$, illustrating the source of the 1.78% vs ~1.4-1.6% discrepancy.
- **Figure G: Five-way identifiability matrix.** A grid representing physical feasibility, observational constraints, likelihood availability, selection functions, and priors for H1-H5.

## 7. Figure-Generation Task List
- **Fig A (Architecture Schematic):** Class D (Draft in TikZ or drawing tool).
- **Fig B (Observational Constraints):** Class D (Draft via drawing tool or matplotlib patch visualization).
- **Fig C (H3 $T_B$ Plot):** Class B (Script required. Requires matplotlib script to plot $T_B = \frac{S_\nu c^2}{2k_B\nu^2\Omega}$ vs $\theta$, keeping $S_\nu=256$).
- **Fig D (H5 Likelihood Surface):** Class B (Script required. Use the independent mathematical implementation in Python to plot the 2D contour).
- **Fig E (H5 Discrepancy Convergence):** Class B (Script required. Run Implementation A for various $k_{max}$ and plot the MAP likelihood asymptote).
- **Fig G (Identifiability Matrix):** Class D (Draft as a visually styled LaTeX table or TikZ matrix).

## 8. Table Inventory
- **Table 1: Frozen observational/evidence vector.** Frequency, Flux, Angular size, etc., strictly citing Mendez (2025).
- **Table 2: Hypothesis identifiability matrix.** Status of H1-H5 regarding constraints, likelihoods, and priors.
- **Table 3: H5 numerical reconstruction.** Comparing published 1.78% against historical emulator and exact independent math.
- **Table 4: Archive/follow-up evidence status.** Distinguishing published limits (1998/99) from non-identifiable campaigns (2010-2014).

## 9. Equation Inventory
- **Eq 1 (H3):** $T_B = \frac{S_\nu c^2}{2k_B\nu^2\Omega} \geq \frac{S_{\nu,\min}c^2}{2k_B\nu^2\Omega_{\max}}$
- **Eq 2 (H5):** Poisson event generation $P(k | \mu) = \frac{\mu^k e^{-\mu}}{k!}$ where $\mu = \lambda \times \Delta t$
- **Eq 3 (H5):** Big Ear detection probability logic $p_{wow}$.
- **Eq 4 (H4):** Conditional radiometric distance relation (EIRP).

## 10. AASTeX Structure
```latex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath, graphicx, hyperref}
\begin{document}
\title{Forensic Bounds and Identifiability Limits on the Origin of the Wow! Signal}
\author[0000-0000-0000-0000]{Research Team}
\begin{abstract}
% Strict summary of the evidence freeze, H3 bounds, H5 audit, and lack of a 5-way posterior.
\end{abstract}
\keywords{Extraterrestrial intelligence (522) --- Radio astronomy (1338) --- Bayesian statistics (1900)}
\section{Introduction}
% ...
\section{Evidence, Provenance, and Identifiability Framework}
% ...
% Sections 3 through 10
% ...
\section{Conclusion}
\acknowledgments
\bibliography{references}{}
\bibliographystyle{aasjournal}
\end{document}
```

## 11. Reproducibility Requirements
- All quantitative claims in the text and figures (specifically Fig C, D, E) must be generated by Python scripts reading directly from the frozen parameters (e.g. `256 Jy`) rather than hardcoded magic numbers.
- A `reproduce_figures.py` script must exist to render the PDFs for the LaTeX document.

## 12. Known Manuscript Vulnerabilities
- **H3:** Reviewers may argue that a geometric upper limit ($\theta \leq 1.9'$) artificially forces a high $T_B$. The manuscript must vigorously defend the rigorous application of the inequality.
- **H5:** K&G 2022 authors may dispute the 1.42% correction. The manuscript must carefully present it as a numerical truncation artifact without adversarial language.
- **H2:** Reviewers may ask why we didn't just use JPL Horizons independently. The manuscript must defend the strict evidentiary freeze methodology.

## 13. Explicit List of Things That Must NOT Be Claimed
- Do not claim H1/H2/H3/H4/H5 is "ruled out."
- Do not claim 1.42% is the "corrected K&G probability."
- Do not claim H3 is "confirmed to be a maser."
- Do not manufacture a unified five-way Bayesian posterior.
- Do not convert censored measurements into point estimates.

## 14. Dependencies for the Next Writing Phase
1. Generation of the Python plotting scripts for Figures C, D, and E.
2. Drafting of the `.bib` file based on existing references (Kipping & Gray 2022, Mendez 2025, Gray & Ellingsen 2002).
3. Final population of Tables 1-4 into LaTeX `deluxetable` format.

## 15. Recommended Writing Order
1. Generate Figures C, D, E and compile Tables 1-4.
2. Write Section 2 (Methodology/Provenance framework) and Section 3 (Observational Evidence).
3. Write Section 6 (H3) and Section 8 (H5) around the quantitative figures.
4. Write the remaining descriptive hypothesis sections (H1, H2, H4).
5. Write Section 9 (Cross-Hypothesis Identifiability) leveraging Table 2 and Figure G.
6. Write the Introduction, Discussion, and Conclusion.

## 16. Final Manuscript Production Checklist
- [ ] Python plotting scripts created.
- [ ] Figures C, D, E verified against frozen evidence.
- [ ] Tables 1-4 converted to `deluxetable`.
- [ ] Equations 1-4 embedded.
- [ ] Authoritative text draft completed.
- [ ] Internal technical audit (verification of "Do Not Claim" list).
- [ ] Final author revision.
