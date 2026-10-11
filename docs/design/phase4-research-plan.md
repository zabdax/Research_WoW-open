# WoW! Signal — Phase 4 Research Plan & Stop-Criterion Analysis

## 1. Phase 4 Research Plan

This plan limits further open-ended archival or mathematical exploration. Every task is bounded by currently existing evidence or clear mathematical endpoints.

### Task List & Classification

1. **Resolve 1.42% vs 1.78% H5 Discrepancy**  
   *Question:* What is the mathematical origin of the discrepancy between the published stochastic repeater MAP likelihood (1.78%) and the independent emulator (1.42%)?  
   *Classification:* **CORE**  
   *Stop Condition:* Two implementations (Faithful Reproduction and Independent Math) are documented, the exact mathematical difference is characterized, and its effect on the interpretation is quantified.

2. **Quantify Usable 1998/99 Hobart H5 Information**  
   *Question:* What partial bound or conditional likelihood can be derived from the Gray & Ellingsen 2002 published non-detection?  
   *Classification:* **CORE**  
   *Stop Condition:* A likelihood, interval, or bound is produced; or a mathematical proof is written showing why it cannot be.

3. **Determine Information Content of 2010–2014 Archive**  
   *Question:* What geometric or timing constraints can be extracted from the 2010–2014 archive without the Bob Gray thresholds?  
   *Classification:* **CORE**  
   *Stop Condition:* The strongest justifiable inference (e.g., exposure constraints) is documented without fabricating a selection function.

4. **H3 Physical Parameter Bounding**  
   *Question:* Is there a physically viable region of H3 (maser/cloud) parameter space capable of producing $\geq 256$ Jy?  
   *Classification:* **CORE**  
   *Stop Condition:* The minimum required brightness temperature, column density, and energetic constraints are documented based on Arecibo II parameters.

5. **H2 Cometary Geometric/Physical Check**  
   *Question:* Does any proposed comet (e.g., 335P) satisfy the established J2000 Big Ear coordinates and timing?  
   *Classification:* **VALUABLE**  
   *Stop Condition:* The geometric intersection is tested against the established constraint.

6. **H1 Mechanism Constraint Table**  
   *Question:* Can specific local RFI mechanisms (e.g., satellites, aircraft) quantitatively reproduce the 72-second transit profile and lack of harmonics?  
   *Classification:* **VALUABLE**  
   *Stop Condition:* The mechanism-level constraints are tabulated based on current direct evidence.

7. **H4 Conditional Constraints**  
   *Question:* What transmitter power / beam divergence is required at relevant distances to produce $\geq 256$ Jy?  
   *Classification:* **OPTIONAL**  
   *Stop Condition:* The physical parametric equation is written. (No ETI priors).

8. **Contact Bob Gray for 2010-2014 Thresholds**  
   *Question:* What were the search outcomes and candidate lists?  
   *Classification:* **EXTERNAL DEPENDENCY**  
   *Stop Condition:* Sent request. Do not wait for reply to finish Phase 4.

9. **Decompile/Reverse-Engineer MPSLPP Fortran Kernels**  
   *Question:* Exactly what FFT/windowing was run in 1998?  
   *Classification:* **DEAD END** (Do not pursue; effort vastly exceeds scientific gain).


## 2. Dependency / Identifiability Graph

```text
                         WOW! SIGNAL ORIGIN (5-Way Posterior)
                                          |
                                   [BLOCKED BY GATES]
                                          |
       +--------------------+--------------------+--------------------+--------------------+
       |                    |                    |                    |                    |
      H1 (RFI)             H2 (Comet)           H3 (Maser)           H4 (Beam)            H5 (Beacon)
       |                    |                    |                    |                    |
 [NOT REQUIRED]       [IN PROGRESS]        [IN PROGRESS]        [OPTIONAL]           [IN PROGRESS]
       |                    |                    |                    |                    |
  Mech. Constraints    Ephemeris match      Energetics/Flux       Tx Power Req      Stochastic Likelihood
  (Valuable)           (Valuable)           (Core)                (Optional)           (Core)
                                                 |                                         |
                                         Arecibo II bounds                     +-----------+-----------+
                                         [COMPLETE]                            |                       |
                                                                        K&G 2022 Reprod.         Hobart Metadata
                                                                        [IN PROGRESS]         [EXT. DEPENDENT]
                                                                               |                       |
                                                                        Resolve 1.42%         2010-2014 S.F.
                                                                        [CAN START]        [NON-IDENTIFIABLE]
```


## 3. H5 Statistical Audit

**A1. Freeze Source:**
- Kipping, D. & Gray, R. (2022). "Could the 'Wow' signal have originated from a stochastic repeating beacon?" *MNRAS* 515(1):1122-1129. arXiv:2206.08374.

**A2. Mathematical Model:**
- **Stochastic Process:** Poisson point process of top-hat signals.
- **Parameters:** $T$ (duration, seconds), $\lambda$ (event rate, day$^{-1}$).
- **Likelihood:** $P(\text{data} | T, \lambda)$.
- **Probability vs. Likelihood:** The reported "1.78%" is a **MAP likelihood** across the $(T, \lambda)$ grid, *not* a posterior probability.

**A3. Reproduction Status:**
- Big Ear-only result: **Source-code emulation** (Grid simulation).
- Hobart contribution: **Exact reproduction** (Analytical penalty $e^{-84\lambda / 24}$).
- META/ATA: **Exact reproduction** (Analytical penalty $e^{-108\lambda / 24}$).
- Final reported result (1.78%): **Numerical approximation discrepancy** (Project emulator yields ~1.42%).


## 4. H5 Identifiability Ledger

| Quantity Needed for H5 | Status / Constraint | Missing Bob Gray Info | Identifiability |
| ---------------------- | ------------------- | --------------------- | --------------- |
| 1998/99 Threshold      | Published (5.9$\sigma$) | Verification data | PUBLISHED-ONLY |
| 1998/99 Non-Detections | Yes (for $P<14$ hr) | Actual candidates | PUBLISHED-ONLY |
| 2010-2014 Thresholds   | UNAVAILABLE | $P_e$ / SNR thresholds | **NON-IDENTIFIABLE** |
| 2010-2014 Candidates   | UNAVAILABLE | Lists of rejected hits | **NON-IDENTIFIABLE** |
| Selection Function     | UNAVAILABLE | The above two metrics | **BLOCKED** |


## 5. H3 Physical Feasibility Plan

**Objective:** Evaluate if cold HI clouds can produce the observed signal.
**Observationally Established:** 
- $\nu = 1420.726 \pm 0.005$ MHz
- Flux $\geq 256 \pm 63$ Jy
- Angular size $\leq 1.9'$
- $v_{helio} \approx -84$ km/s

**Task:** Compute required brightness temperature ($T_B$) using the inverse solid angle scaling.
**Stop Condition:** Publish the $T_B$ and energetic pumping requirements. Do not attempt a full HI4PI galactic cloud population simulation yet.


## 6. H2 Constraint Status

**Objective:** Evaluate geometric intersection of proposed comets.
**Current Constraint:** The source must align with the Big Ear positive horn RA/Dec at the exact recorded transit time.
**Task:** Use `research/models/h2_geometry.py` to test 335P/Gibbs. 
**Stop Condition:** Publish the angular separation (or rejection) at transit. Do not model unproposed comet populations.


## 7. H4 Conditional Constraint Status

**Objective:** Evaluate artificial beam physical requirements.
**Current Constraint:** Flux $\geq 256$ Jy.
**Task:** Express transmitter EIRP as a function of distance $d$. 
**Stop Condition:** Publish the conditional equation. Do not invent an ETI distance prior.


## 8. H1 Mechanism Constraint Status

**Objective:** Evaluate RFI models.
**Current Constraint:** Narrowband ($\leq 10$ kHz), no harmonics, 72s transit profile (sidereal tracking).
**Task:** Document whether satellites or terrestrial sources can quantitatively mimic this profile.
**Stop Condition:** A mechanism-level constraint table is completed.


## 9. Cross-Hypothesis Evidence Matrix

| Evidence | H1 (RFI) | H2 (Comet) | H3 (Maser) | H4 (Beam) | H5 (Beacon) | Class |
| -------- | -- | -- | -- | -- | -- | -- |
| Freq 1420.726 | Weakly disfavors | Disfavors | Favors | Neutral | Neutral | REPRODUCED |
| Flux $\geq 256$ Jy | Favors | Disfavors| Disfavors | Neutral | Neutral | REPRODUCED |
| 72s Transit | Disfavors | Neutral | Neutral | Neutral | Neutral | DIRECT |
| Hobart 1999 Null | Neutral | Neutral | Neutral | Favors | Disfavors | PUBLISHED-ONLY |
| Hobart 2013 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |


## 10. Five-Way Bayesian Gate Specification

To safely enable `confirmatory_comparison_enabled = true`, the following gates must be passed:

- **Gate A (Satisfied):** Observational limits for the 1977 event are frozen and censored correctly.
- **Gate B (Internal):** H2 geometric bounds and H3 energetic bounds are strictly defined.
- **Gate C (External):** A valid Selection Function for the 2010–2014 Hobart campaigns is constructed using recovered Bob Gray thresholds.
- **Gate D (Fundamentally Non-Identifiable):** H4 (Artificial Beam) requires a distance/power prior that cannot be empirically bounded by this project.

*Conclusion:* The five-way posterior cannot be unlocked in Phase 4.


## 11. Explicit STOP/EXIT Criteria

**Phase 4 is complete when:**
1. The mathematical origin of the 1.42% vs 1.78% H5 MAP discrepancy is proven.
2. The H3 physical brightness temperature bounds are calculated from the $\geq 256$ Jy limit.
3. The geometric compatibility of H2 (comets) is tested against the established coordinates.
4. The exact list of missing metadata needed to evaluate the later Hobart campaigns is formalized.
5. **No remaining internal task is expected to materially change these bounds.**

Remaining work is then classified as:
- **EXTERNAL FUTURE WORK:** Obtaining Bob Gray records.
- **NOT WORTH PURSUING:** Decompiling 1998 Fortran binaries; infinite astrophysics literature searches.


## 12. Final Decision Memo

**A. What should we work on next?**
1. Run the H5 mathematical comparison (Implementation A vs B) to resolve the 1.42% vs 1.78% issue.
2. Run the H3 energetics/brightness temperature bounds using the frozen Arecibo parameters.
3. Run the H2 geometric check.

**B. What should we NOT work on?**
- Do not attempt to guess the 2010-2014 Hobart candidate lists.
- Do not build a heuristic five-way posterior.
- Do not survey maser literature beyond basic constraints.

**C. What can be finished without any external response?**
- The H5 implementation discrepancy audit.
- The physical bounds for H2 and H3.

**D. What genuinely requires Bob Gray / external evidence?**
- H5 identifiability (the Selection Function) for the 2010, 2013, and 2014 Hobart campaigns.

**E. What result can we realistically have at the end of Phase 4?**
- A rigorous, peer-reviewable manuscript establishing the physical bounds (H3, H2), the correction to the stochastic likelihood (H5), and the strict epistemic reasons why the later follow-ups fail Bayesian identifiability.

**F. What remains permanently or practically non-identifiable?**
- The H4 artificial beam prior.
- The 1998/99 FFT subroutines (practically non-identifiable).

**G. At what point should we stop researching and write the paper?**
- Immediately after executing the three CORE calculations (H5 math audit, H3 energetics, H2 geometry).

**H. What additional evidence would justify reopening the investigation later?**
- The recovery of Bob Gray's detection thresholds and candidate logs.
