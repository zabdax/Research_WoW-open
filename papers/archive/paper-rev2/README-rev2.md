# paper-rev2 — supervisor-fix suite (DO NOT SUBMIT AS-IS)
Base: `papers/archive/paper-rev1/main.tex` (95647 B). All changes logged below with verification sources.
Audit record: `audit/supervisor-fixes-2026-10-08/SUPERVISOR_FIXES.md`; scripts `audit/supervisor-fixes-2026-10-08/scripts/`; fixed FigA `audit/.../outputs/figA_architecture_FIXED.pdf` (copied to `figures/figA_architecture.pdf` here).

## Changes rev1 → rev2 (verified)
1. Sec 5.2: NAAPO-reliance paragraph REPLACED with our JPL-Horizons calculation (266P −3191/−3364 s RA, −24′ Dec, r=4.73 AU; 335P −2749/−2922 s, −160′ Dec, r=4.56 AU; formal 3σ + back-integration caveat; adopted J2000 coords + galactic-typo note). NAAPO kept as <1′ cross-check.
2. 266P activity sentence: water-only qualifier + CO/CO₂ citation (`gicquel2023` added to refs).
3. "Three physical objections, each decisive" → two physical + one methodological (dB).
4. "Hours in beam" kinematics paragraph REPLACED (Earth-rotation transit 35.8 s FWHM; second horn does the work; rates ~11–13″/hr).
5. H2 status quotes (3 places) + Sec 9 matrix sentence + Conclusion: candidate-specific exclusion (no "falsified/falsification").
6. Elongation: floor 560→585 K (factor 20); thresholds 4→4.09′, 6→6.54′, twice-RA 3.8′.
7. Sec 6: beam sentence added (13.4 ″/s; 36 s vs 72 s vs 1.9′/73.4 s deconvolution).
8. Sec 7.2: band frame token (rest 1420.4056 vs instantaneous 1420.246–1420.736, contains 1420.726); H4 tension labelled qualitative/non-likelihood.
9. Seldemo: T-overlap + upper-limit acknowledgment added.
10. "Decisive rather than decorative" (2 places: intro + discussion) → identifiability-decisive + (0.65, ΔlnE −0.43).
11. Discussion Fifth: joint width/dilution numbers + HI4PI measurement (Fig G).
12. Abstract rewritten 511→184 words, results-first, Kipping "verified; emulator relative-only".
13. Sec 9.1 byte fix: literal `\n\n` bytes → real blank line (was invalid `\n` control sequence).
14. Refs: `ehman1997` → gray-literature URL entry; `gicquel2023` added; Kipping DOI corrected `stac1846`→`stac1807` (verified OpenAlex; `stac1846` is an unrelated SN paper); `references_harvard.tex` generated (23 entries, full journal names, titles) via `audit/.../scripts/build_harvard_refs.py` for the IJA-template manuscript.
15. Acknowledgments: Cambridge-fields AI disclosure added (tool/version/dates/description; human accountability retained).
16. Figures: fixed FigA swapped in (S/ν→Level B, conditional C/D text, wrapped); fixed FigC regenerated (raw `\u2013` legend → real en dash; curve re-verified TB_min=17206.72 K).
17. IJA conversion: DONE mechanically (`ija_manuscript/`: CSL front matter, fig1–7, 3 deluxetables→tabular, Harvard `thebibliography`, AI disclosure, HUMAN comments) — COMPILES CLEAN, see BUILD STATUS. Figs for acceptance still need EPS/TIFF export (review embeds PDFs, accepted per IJA).

## BUILD STATUS 2026-10-09/10 — COMPILES CLEAN (TinyTeX TeX Live 2026, 2× pdflatex)
`ija_manuscript/manuscript.pdf`: 18 pages, 587,638 bytes. Zero `!` errors, zero undefined citations, zero rerun warnings.
Remaining log items (all cosmetic/accepted): one 1.16pt overfull (h5 table), float underfulls, CSL font-size substitutions, hyperref empty-link warnings. Tables 1–5 + Figs 1–7 verified visually in-PDF.
Pipeline lesson learned: never pipe a generating script through `Select-Object -First` (it kills the writer mid-file); rerun scripts to files instead.

## STILL HUMAN (in priority order)
- EPS/TIFF figure export for acceptance (review embeds PDFs; accepted). Say the word and it runs.
- Submit at https://mc.manuscriptcentral.com/submit_ija (single-blind). APC waiver: request at submission (Research Articles eligible). Preprint allowed (own site/repo/archive); arXiv category author choice.
- Zenodo DOI for the reproducibility script; cite it.

## DONE 2026-10-08/09 — HI4PI check (was pending)
CDS J/A+A/594/A116 HPX_121.fits (247,213,440 B, SHA256 BC8E93…, nside=1024 Ring file 121/192; 16.2′ beam, 1.2882 km/s LSRK channels): pos-horn T(−76..−72)=[0.01,−0.01,0.01,0.01] K (rms 0.044), neg-horn [0.05,0.02,0.02,0.01] K (rms 0.040). No persistent emission at VLSR −74±2 km/s down to ~0.1 K at either horn (predicted persistent thermal filament: ~230 K/channel). Added Fig G (`figures/figG_hi4pi_spectrum.pdf`) + Discussion/abstract/conclusion updates. Scripts: `audit/.../scripts/{extract,analyze,plot}_hi4pi.py`; data: `audit/.../hi4pi/`.

## FIX ROUND 2026-10-10 — supervisor pre-submission list (all applied, build clean)
Base for edits: `ija_manuscript/manuscript.tex`. Build: TinyTeX TeX Live 2026, 2× pdflatex → `manuscript.pdf` 17 pages, **0 `!` errors, 0 undefined citations, 0 `??`**.
1. **Title block:** added missing `\maketitle` (+ `\Fpagebreak` at end of Introduction, `shcup_black_mono.pdf` logo copied from the IJA template dir). Page 1 now shows title/authors/abstract/keywords. `\uat` keywords replaced with plain text (`\uat` is AASTeX-only and would have errored once `\maketitle` expands).
2. **Cross-refs:** `\setcounter{secnumdepth}{2}` + repaired CSL `\@sect` (the class wraps the counter name in `\textcolor` before `\@seccntformat`, which errors when numbering is on; fixed by identical override in the preamble, class file untouched). All 24 `\ref`s resolve; hard-coded `Sec.~5.2` replaced with `\ref{sec:h2_ephem}` (new label on the ephemeris subsection; verified it is §5.2).
3. **H2 language:** subsection renamed to “Geometric, Kinematic, and Emission Constraints”; Table 5 H2 row “Falsified … / Falsified” → “Candidates excluded; class strongly constrained / Strongly constrained”; “excluded from further consideration” → named-candidate set-aside wording.
4. **Fig. 2:** caption + Sec. 3 text now state 36-s FWHM vs ~72–80-s full detectable extent (2×2.6σ at S/N≈30); new canonical generator `scripts/rebuild_figB.py` draws the 35.80-s FWHM Gaussian with 12-s samples, full-extent bracket AND half-maximum FWHM bracket; `ija_manuscript/fig2.pdf` refreshed. Fig. 1 widened to `0.95\textwidth` (was tiny at 0.45).
5. **H4 hedges:** “none single out” / “no engineering reason” / “no optimization singles out” → “the engineering literature considered here does not identify …”; dropped “Only H4”, added the H1 protected-band coincidence.
6. **HI4PI in H3:** new `Sec. 6 \ref{sec:hi4pi}` subsection (data source, horn l/b + 1.4′/1.0′ pixel seps, ±20′/±40′ offset pixels, −76..−72 km/s window, in-band rms 0.01–0.05 K, geometry-independent 164 K/channel vs ≤0.10 K measured). Extension script `scripts/extend_hi4pi.py` + `scripts/hi4pi_extended.json` (all 10 pixels ≤0.10 K; cross-checked against the 2026-10-09 horn values). Table 5 H3 row cites the non-detection. `hi4pi2016` bibitem added.
7. **Citations:** thebibliography reordered alphabetically (25 entries); Kipping paper/code → 2022a/2022b; two-author labels fixed (Kipping and Gray, Condon and Ransom, Gray and Marvel/Ellingsen, Cocconi and Morrison, Oliver and Billingham, Cordes and Lazio); `cordes1991` now cited in H3 (propagation background, no model invoked); Méndez entry marked Preprint (still preprint-only per 2026-10-10 check; Kipping DOI stac1807 re-confirmed). Cite/bib cross-check `scripts/check_ija_refs.py`: 25 cited = 25 entries, 0 broken refs, abstract 189 words.
8. **Cuts:** intro five-result paragraph ~330→~130 words; Discussion Principal Findings items compressed to quantitative headlines; Conclusion paragraphs compressed. 18→17 pages.
9. **Tables/equations:** Table 5 merged Selection+Population-prior columns, `\small` (1.16pt overfull remains, cosmetic); EIRP equation split over 3 lines (98pt overfull eliminated). Number format already uniform ($1.72\times10^4$). Fig. 7 legend (lower-left) vs red annotation (top-right): no overlap in current build, unchanged. All figures DejaVu Sans (D/E/F use matplotlib defaults = sans).
10. **Acceptance exports:** `scripts/export_acceptance.py` → `ija_manuscript/eps/fig1–7.eps` + `ija_manuscript/tiff/fig1–7.tiff` (600 dpi), all headers verified. Note: rev2 `reproduce_figures_de.py` points FIGDIR at paper-rev1 (pre-existing); the export hooks by basename so review PDFs were written there — byte-deterministic, no content change.

## Zenodo record — MINTED 2026-10-11: 10.5281/zenodo.23301440 (concept: 10.5281/zenodo.23301439). Cite the version DOI in the paper. The "(DOI to be inserted)" placeholders are resolved in both manuscripts.
- Submit at https://mc.manuscriptcentral.com/submit_ija; APC waiver at submission; competing-interests + keywords + ORCID + authority at ScholarOne.
- Preprint (allowed); arXiv category author choice.

## FIX ROUND 2, 2026-10-10 — second supervisor pre-submission list (all applied, build clean)
Build: TinyTeX TeX Live 2026, 2x pdflatex → `manuscript.pdf` 17 pages, **0 `!` errors, 0 undefined citations, 0 `??`**.
1. **Title page:** `\jname{International Journal of Astrobiology}`, emptied `\cambridgeurl` and `\copyright@line` (class file untouched; overrides in preamble). Verified in PDF: no "Journal name", no "cambridge.org/", no EMA copyright. `\Fpagebreak` moved to right after `\maketitle` (title block = p1; two-column body from p2; the mid-body forced eject before Sec. 2 is gone). Note: with this fixed template + 189-word abstract, opening text cannot flow onto p1 — the title block fills it by design (same as the template's own sample layout). The 701pt overfull vbox at p1 shipout is the class's own sidebar-as-header construction, cosmetic.
2. **Fig. 7:** annotation now "persistent source predicts $\gtrsim164$ K/channel (off scale)" at top-left (was ~230 K top-right); figure block moved from Discussion into Sec. 6.5 (`\ref{sec:hi4pi}`); width 0.85 textwidth.
3. **Abstract:** H2 offsets now "RA offsets of 46–56 min of time (11–14°)"; "keep this escape conditional" replaced with the actual exclusion result; coincidence kept at $5\times10^{-6}$ and Sec. 7.2 unified to $\sim5\times10^{-6}$ (was ~10⁻⁵). Abstract 195 words (IJA limit 300).
4. **Sec. 8.3:** dangling clause deleted (prose only; emulator untouched per stop rule).
5. **Cordes & Lazio:** sentence + bibitem deleted (nothing else cited it). Cite/bib check: 24 cited = 24 entries, 0 broken refs.
6. **Availability:** Zenodo placeholder "(DOI to be inserted at acceptance)"; upload package staged at `papers/archive/paper-rev2/zenodo/` (script + JSON + upload README with metadata/steps). Minting is a human step.
7. **Proofreading:** "Mendez II" → "Méndez II"; "contextual contradiction" → "tension". The reported "published1.78% / factor0.65 / flat(ln T" gluings and "Observatory , NAAPO" do not exist in the IJA source (all instances properly spaced/tilde-separated) — likely seen in an older render; no change needed.
8. **Email:** correspondence address left as-is — choosing a neutral address is a human decision (flagged below).
9. **Figures:** Fig. 2 now plots the real 6EQUJ5 values (6/14/26/30/19/5σ × 8.5 Jy; peak 30 matches 30.1σ; verified against `research/data/mendez_evidence_vector.yaml` channel-2 rows 58-63) on the 36-s FWHM curve; legend moved lower-right, FWHM label left of bracket, in-figure title dropped. Fig. 1 labels are math text, title dropped, height tightened (2.8→2.3). All in-figure titles dropped (C/D/E/F-review/G-suptitle); all figures DejaVu Sans ≥8.5pt. Fig. 7 legend (lower-left) vs annotation (top-left): no overlap.
10. **Hygiene (no science change):** rev2 `reproduce_figures_de.py` / `reproduce_main_numbers.py` FIGDIR and the json OUT path repointed paper-rev1 → paper-rev2 (they were overwriting the frozen rev1 snapshot; outputs are byte-deterministic so rev1 content is unchanged). `main_numbers.json` regenerated: all values identical (stop rule honored — Eq. 18, emulator, Hobart treatment untouched).
11. **Acceptance exports regenerated** (`export_acceptance.py`): eps/ + tiff/ (600 dpi) all verified.
12. **Overleaf bundle:** `ija_manuscript/overleaf_upload.zip` (tex + cls + fig1–7.pdf + logo, 229 KB) — proven by an isolated clean-room build (17pp, 0 errors).

## FIX ROUND 3, 2026-10-10 — third supervisor pre-submission list (all applied, build clean)
Build: TinyTeX TeX Live 2026, 2x pdflatex → `manuscript.pdf` 17 pages, **0 `!` errors, 0 undefined citations, 0 `??`**.
1. **Fig. 1:** boxes ~20% taller, red Boundary label raised clear above the boxes, all example labels math text, in-figure title dropped. Visually verified via raster render: no overlaps, "Δt ≥ 73.4 s" fully inside its box. Added "Figure 1 summarizes…" sentence in Sec. 2.1 (first-ever in-text citation of Fig. 1).
2. **Fig. 2:** extent arrow moved low (y ≈ 26 Jy), FWHM arrow at half-maximum with left-side label, legend lower-right clear of the peak; caption now gives the decoded values (6, 14, 26, 30, 19, 5σ — verified against `research/data/mendez_evidence_vector.yaml` channel-2 rows 58–63) and keeps "schematic" (the 161.5-Jy sample sits above the curve). Visually verified via raster render.
3. **Sec. 6.1:** rewritten — θ and Δt attributed to the Méndez II profile fit (not the 72-s sample span), plus the 72-s vs 73.4-s definitional sentence.
4. **Zenodo:** NOT minted (requires a human account) — staged at `papers/archive/paper-rev2/zenodo/` with upload README; Sec. 12 keeps "(DOI to be inserted at acceptance)" AND now names every script file. Note for the supervisor: "deposit before submitting" is a human click-through; nothing further the agent can do without account access.
5. **Donor:** Sec. 12 item (iii) now names Simon Ellingsen (University of Tasmania) with an access sentence ("shared with the authors for this analysis; inquiries about access should be directed to the authors") plus a `% HUMAN` gate requiring his consent before submitting; Acknowledgement thanks him for supplying the archive.
6. **Typos:** NAAPO natbib label fixed (`[NAAPO(2017)]` — was rendering "Observatory , NAAPO"); PDF now shows "(NAAPO, 2017)". "Society6(9)" and "Observatory ," do not exist in source or PDF (Perez entry correctly spaced) — likely an older render.
7. **Page 1:** no stray `\newpage`/`\clearpage` exists — the break is the class-required `\Fpagebreak`, now placed after the first intro paragraph so the Introduction OPENS on page 1 (verified in PDF text: p1 ends with the Ehman paragraph, p2 continues). The 701pt overfull vbox is the class's own sidebar-as-header construction, cosmetic only.
8. **Abstract:** exact count 195 words (IJA limit 300, single paragraph) — already at the requested ~200; no trim applied.
9. **Declarations:** CSL.cls and the IJA template define NO funding/contribution macros — competing interests (already a `% HUMAN` TODO in the ack), funding, and author contributions are ScholarOne-form items at submission; nothing to add in-TeX.
10. **Safeguard rerun:** new `scripts/verify_all_numbers.py` — 28/28 PASS in the repo environment: TB bounds, elongation thresholds, beam kinematics, H5 demo (5.62→2.52, 0.65), chains (32.3/3.3/1.78), kmax sweep, EIRP constant, coincidence 5.1e-6, HI4PI 164.1 K + all band values + rms, and a LIVE JPL-Horizons requery reproducing -3191/-3364/-2749/-2922 s and r = 4.73/4.56 AU exactly (`scripts/horizons_recheck.py`). Limitation disclosed: run in the project's pinned venv, not a fresh container. Notable find: numeric id 90001326 no longer resolves to 335P (returns a different object); the script queries by designation and the manuscript cites solution descriptors, so the paper is unaffected.
11. Exports (eps/tiff) and `overleaf_upload.zip` regenerated from the final files; targeted pytest 34/34 pass. Eq. 18, emulator math, and Hobart treatment untouched throughout.

## FIX ROUND 4, 2026-10-10 — fourth supervisor pre-submission list (all applied, build clean)
Build: TinyTeX TeX Live 2026, 2x pdflatex → `manuscript.pdf` 17 pages, **0 `!` errors, 0 undefined citations, 0 `??`**.
1. **Fig. 1:** boxes taller again with rebalanced text stack; raster-render verified — titles fully inside boxes with padding, nothing clipped or overlapping.
2. **Zenodo:** Sec. 12 now says ALL scripts/values are archived there (no internal filenames — "figure-generation scripts, one per figure"); `zenodo/` staging holds all 10 scripts + both JSONs + upload README. Minting remains a human account step (also required by PRD F1.3's "prepare but do not submit" scope).
3. **Méndez caveat:** Sec. 3.1 states the preprint status with propagation scope (Secs. 5–8); draft cover letter at `ija_manuscript/cover_letter_DRAFT.md` repeats it plus a submit-day re-check instruction. Journal status re-verified today via OpenAlex + Crossref: still preprint-only (no journal record for either Wow! I or II).
4. **"Society6(9)":** added a comma ("Society, 6(9)") — source already had the space and the PDF already rendered it; now unambiguous either way.
5. **Abstract:** dropped the parenthetical numeric vector as suggested; rendered count 242→213 words (source tokens 187), IJA limit 300. The "270" was likely estimated from the pre-trim render.
6. **Clean-environment rerun:** brand-new venv (fresh pip install numpy/astropy/scipy/astroquery/matplotlib/pillow) ran `verify_all_numbers.py` end to end: 28/28 PASS including live Horizons. Referee-rerunnable via the same script.
7. Exports, PDF, and Overleaf zip regenerated; cite/bib 24/24, refs 26/26 resolve.

## FIX ROUND 5, 2026-10-10 — final pre-submit list (all applied, build clean)
Build: TinyTeX TeX Live 2026, 2x pdflatex → `manuscript.pdf` 17 pages, **0 `!` errors, 0 undefined citations, 0 `??`**.
1. **Perez comma reverted** to "Society 6(9)" (space, no comma) — verified in the fresh PDF.
2. **Zenodo reserve:** cannot be done by the agent (requires a human Zenodo login; reservation happens in the draft-deposit UI). Exact steps are in `zenodo/README_zenodo_upload.md`; Sec. 12 placeholder stays until the human pastes the reserved DOI. Note: reserving pre-publication is standard and does not publish the record.
3. **Clean run:** fresh-venv `verify_all_numbers.py` re-run after all edits — 28/28 PASS.
4. **Méndez:** re-checked today against the live arXiv record (v1 only, "To be submitted to ApJ", no journal ref) — still preprint; the X post about an ApJ acceptance refers to Wow! I (2408.08513), not the Wow! II vector source. Sentence + cover-letter draft stand.
5. **Full referee read** (compiled PDF, pp. 1–17): no new defects. Noted consequence of the requested Fig. 7 move: LaTeX numbers floats in source order, so printed numbers are now HI4PI = Fig. 4, H5 surface = Fig. 5, convergence = Fig. 6, Hobart = Fig. 7 — every in-text reference uses `\ref` and is consistent (verified 0 `??`). Filenames (fig1–7.pdf) intentionally unchanged.
## FIX ROUND 6, 2026-10-11 — two citations (tex only, build clean)
[Round-6 detail superseded; see round 7 below. mendez2024 + hi4pi2016 cited per spec review.]

## HUMAN FINAL TEX, 2026-10-11 — `wow_signal_final.tex` adopted verbatim
Author-humanized rewrite installed as `ija_manuscript/manuscript.tex` (prior agent version kept as `manuscript_agent_r12.bak`). Audit of the adopted file: 25:25 cites, 0 broken refs, envs balanced, abstract 223 words, no forbidden phrasings (only deliberate "lowers by a factor of 2.2", direction unmistakable). Source-related comments honored: cities kept as public info (no invented postal details); empty `\keywords{}` kept for the class. IJA zip repacked with the adopted tex.
## FIX ROUND 12, 2026-10-11 — final pre-submission correction pass (IJA only)
"Evidence factor" → "grid-integrated likelihood ratio" everywhere (abstract/intro/8.5/10.1/11); 8.5 gloss now "likelihood integrated over the adopted flat grid". "Factor of 2.2" → "2.2-fold reduction in the emulator maximum" (8.5/9.2/10.1). 1998-vs-2010 comparison softened (no duration-guarantee). H4 "counter-productive" → sightline-dependent losses; discussion/conclusion now "conditional illustration", matching abstract. H1 (1/32)^6 attributed to Méndez et al. as model-conditional heuristic. Comet universals narrowed (single validated-mechanism sentence; water strongly suppressed + volatiles open). Table 6 H3/H4 prior cells explicit. Fig 7 legend + axis L_S1/L_S2 (curve untouched). Table 4 rebuilt with p-widths + tabcolsep (visually verified); Table 1 respaced (verified). H2 Table status kept candidate-specific.
Verified: 18pp/0 errors build; all tables + Figs 2/4/7 visually inspected; extended gate ALL PASS; round-12 spec review passed. IJA zip repacked.
H5 rerun ruled out (no gfortran; follow-up lives in Mathematica .nb, not wow.f90) → fallback wording: 5.62→2.52/0.65 stated as emulator-specific illustration; "evidence factor" replaced by "integrated-likelihood ratio" everywhere (definition kept once in 8.5).
## FIX ROUND 11, 2026-10-11 — referee-attack round, IJA Overleaf package only
Fig6 ylabel fixed (L_S1/L_S2) in both generators; fig files renamed to print order (fig4=HI4PI … fig7=Hobart) + tex includes + eps/tiff updated.
HI4PI: field-map script (824 pixels ≤45′, max 0.1459 K, 0 ≥1 K) + coupling equation + LSRK-vs-kinematic sentence + adjacent-channel sentence (~240 Jy vs 8.5 Jy noise) in 6.5.
H4: 5e-6 out of abstract; selection-effect sentence in 7.2. Intro: non-exhaustive H1–H5 sentence. Sec 12: public/on-request/restricted split. Freeze versions in 3.1 (v1 2025-08-14 / frozen 2026-08-23 / Hobart 2026-08-25+29). Table 6 cells fixed. Jeffreys→scale prior + S_min condition. Abstract uniform-disk signpost. H1 attribution sentence. Ack competing-interests + ChatGPT/postal HUMAN flags. Cover letter discloses both preprints.
MANIFEST (number_figure_manifest.md) staged in scripts/ + zenodo/. Verified: extended gate ALL PASS, 25:25 cites, 0 broken refs, round-11 spec review passed. IJA zip repacked.
## FIX ROUND 10, 2026-10-11 — H5 bound logic + H3 profile convention (IJA only)
H5: Sec 8.5 no longer claims both approximations overstate the penalty — span overstates usable time, pre-window overlap understates the interval; exp(−λT_H) is illustrative, not a rigorous upper bound. "Aggressive" fully removed (0 occurrences).
H3: Gaussian-profile sensitivity added (1/ln2≈1.44 → 1.19e4 K nominal, 0.81e4 K floor; elongation pair 2.83′/4.53′; non-thermal robust except doubly conservative corner). Méndez II Gaussian-fit methodology cited from frozen TeX. Disk-convention numbers untouched everywhere.
Verified: extended gate ALL PASS (new Gaussian checks included); round-10 spec review passed after closing 1 wording gap. IJA zip repacked; verify script re-synced to zenodo/.

Round-10 ported to AASTeX main.tex (H5 bound rewrite + Gaussian paragraph + elongation pair); AASTeX zip repacked with verified contents.
## FIX ROUND 9, 2026-10-11 — targeted review set, IJA Overleaf package only
P1: 450–870 K clause DELETED (reviewer correct: per-channel flux density cannot grow by broadening); replaced with channel-width limiting case (2.11 vs 1.29 km/s, factor ≤1.64; resolved reads ~51–100 K). Exclusion holds at every elongation (lowest prediction 51 K vs 0.1 K measured).
P2: covered by existing audit (no manuscript change).
P3: convention fixed — 164.0 K = point-source limit, ~163 K = finite 1.9′ model; caption + Fifth + 6.5 updated.
P4: great-circle separations 11.83/12.47/10.43/11.04 → printed 11.8/12.5/10.4/11.0; abstract range 10.4–12.5.
Plus: 9.1 generic-class narrowing; conclusion water-volatiles + H2-plural fixes; 7.2 "prior-dependent" doubling removed; abstract/9.2/10.1 114.1-h upper-limit wording; Table 6 H3 geometry qualifier; 6.4 "reference compact-source constraint"; Sec 8.5 S2-zero blurring fixed; competing-interests line + postal HUMAN flags.
Verified code-level: 25:25 cites, 0 broken refs, envs balanced, extended gate ALL PASS, round-9 spec review passed (1 self-found gap + 1 reviewer gap, both closed). IJA zip repacked.
## FIX ROUND 8, 2026-10-11 — supervisor priorities 1–4 (both IJA + AASTeX)
P1: `scripts/hi4pi_geometry_test.py` — explicit beam-coupling (uniform elliptical filament, RA fixed 1.9', 2D Gaussian overlap, 3 spectral cases): central-beam ~163 K compact / ~160 K at 4–6.5' / ~130 K at 20' / ~84 K at full 40' beam; broad thermal line ~450–870 K/ch. Conclusion SURVIVES all elongations (stronger result). Sec 6.5 rewritten with derivation; claims narrowed to tested range + 1977-epoch caveat (survey constrains sampled velocity/epoch).
P2: `scripts/h5_independent_audit.py` — event-level MC (fixed seed) vs exact closed form + evidence ratio on independent 120-grid/trapezoid: 0.6516 vs 0.6528 (measure+bounds consistent); truncation gap quantified (+0.169% OSU-only). Audit caught and fixed two harness bugs (172.37s offset, e-power grid bounds, premature k-break). Sec 9.2 "exactly zero" → "no update (unity)". Evidence defined once in 8.5.
P3: abstract/10.1/11 persistent-filament claims scoped to tested range; H4 already conditional.
P4: `zenodo/` expanded (all scripts, both JSONs, campaign_exposure.csv, dependency_versions.txt, step-by-step README, Hobart shared/restricted note). DOI mint = human step.
Verified: extended gate ALL PASS (incl. clean fresh-venv run); round-8 spec review passed after closing 2 main.tex gaps. Eq./values/figures/refs untouched except sanctioned additions.
## FIX ROUND 7, 2026-10-11 — supervisor claim-calibration set (both IJA + AASTeX)
New scripts: `scripts/sep_on_sky.py` (on-sky 10.55–12.50 deg), `scripts/freq_prior_compare.py` (uniform 5.05e-6 vs log-uniform 7.64e-5, 15.1x). New mapping table `tab:emulator_map` + `sec:h3_geometry` label in both manuscripts. Verified code-level (no PDF): 25:25 cite:bib both files, 0 broken refs, envs balanced, round-7 spec review passed. Both Overleaf zips repacked. Eq./values/figures/references untouched except the two computed additions; stop-rule science (Eq. 18, emulator, Hobart treatment) unchanged.
- **Wow! I cited:** new `mendez2024` bibitem (Méndez, Ortiz Ceballos & Zuluaga 2024, arXiv:2408.08513, Preprint — content verified against the frozen in-repo TeX + live arXiv record: magnetar/SGR-triggered brightening of cold-HI lines via maser/superradiance). Cited where H3 begins (Sec. 6.1) and in Sec. 6.5 with the careful transient-only wording (consistent with, does not test their model). Cover letter discloses both preprints.
- **Big Ear instrument facts:** Wow! I comparison table (frozen `awowi-v1.tex` l.188–202) confirms Big Ear 50 channels, 10 kHz/channel, 500 kHz total, 12 s integration, HPBW 8×40 arcmin. `mendez2024` now co-cited with `ehman1997` for the HPBW sentence and for the 12-s cadence (both arXiv-only + gray lit, stated plainly).
- **Perez:** restructured to "Society,} \textbf{6} (9)" (comma + split volume) — byte-verified 0x20 spaces throughout.
- Cite/bib 25/25, 0 broken refs; isolated Overleaf-bundle build: 17pp, 0 errors.

## AASTeX BUNDLE, 2026-10-11 — `aastex_overleaf_upload.zip` (316 KB)
`main.tex` ported to the finalized IJA content (all six fix rounds + Wow! I cites) in AASTeX idiom (\ion, \nameref, deluxetable, BibTeX); `references.bib` gained `mendez2024` + `hi4pi2016` (BibTeX auto-handles 2022a/b and two-author labels). Bundle: main.tex + aastex701.cls + aasjournalv7.bst + references.bib + orcid-ID.png + figures/figA–figG.pdf. Verified by two independent reviewer passes (spec 17/17 + quality): 25:25 cite:bib, all labels resolve, envs balanced, no stale IJA constructs, no duplicate floats. Executed via subagent-driven development (implement → spec review → quality review per task).
