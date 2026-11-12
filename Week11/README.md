# Week 11 — CT Artifacts, Contrast Agents, Dosimetry & Group Statistics

Finishing CT with **artifacts** and **contrast agents**, then covering **radiation dosimetry** and
the statistical comparison of patient and control groups. Nuclear imaging and the segmentation / M-mode
project-method notebooks were reviewed in Week 12 and are now organized there.

## Contents

| File | Description |
|------|-------------|
| [CTArtifacts.ipynb](CTArtifacts.ipynb) | Simulated CT artifacts: **metal / high-density** streak & **star** artifacts (persist with any number of views), **beam-hardening cupping**, **motion** blur/ghosting, **ring** artifacts (detector miscalibration), and **photon-counting / thermal noise** — plus the rule that *missing-data* streaks fade with more views while *corrupted-data* artifacts do not. |
| [ContrastAgents.ipynb](ContrastAgents.ipynb) | How contrast agents work: **iodine** raising Hounsfield units (CT), the iodine **K-edge** (33.2 keV) and why low kVp boosts contrast, the **time–attenuation (bolus)** curve and scan timing, and **gadolinium** shortening $T_1$ to brighten $T_1$-weighted MRI. |
| [RadiationDosimetry.ipynb](RadiationDosimetry.ipynb) | Units of radiation: **becquerel** (activity $A=\lambda N$), **gray** (absorbed dose), **sievert** (equivalent $H=w_R D$ and effective $E=\sum w_T H_T$), the **entrance skin dose** (inverse-square + backscatter), **cumulative fluoroscopy** dose vs skin-injury thresholds, and typical **effective doses** vs background. |
| [ComparingTwoGroups.ipynb](ComparingTwoGroups.ipynb) | Comparing a continuous metric between patients and controls: **Shapiro–Wilk** normality → **t-test** (parametric) vs **Mann–Whitney / Wilcoxon** (non-parametric), **Cohen's $d$** effect size, and the tie back to **power / cohort size**. |

## Key concepts

### CT artifacts & contrast agents
- **Artifacts**: **metal/high-density** → streak/**star** (persist regardless of views) + shadowing;
  **beam hardening** → **cupping**; **motion** → blur/ghosting; detector miscalibration → **rings**;
  low dose → **photon-counting/thermal noise**. *Missing-data* artifacts improve with more views;
  *corrupted-data* artifacts do not.
- **Contrast agents**: **iodine** raises $\mu$/HU (CT; K-edge at 33.2 keV favors low kVp); **bolus
  timing** separates arterial/venous phases; **gadolinium** shortens $T_1$ → bright on $T_1$-weighted MRI.

### Dosimetry
- **Becquerel** (decays/s), **gray** (J/kg absorbed), **sievert** (harm-weighted: $w_R$ radiation type,
  $w_T$ tissue sensitivity).
- **Entrance skin dose** follows the **inverse-square law** + **backscatter**; long **fluoroscopy** can
  cross deterministic skin-injury thresholds (erythema ~2 Gy → burn >15 Gy). **Effective dose** compares
  exams against ~3 mSv/yr background (**ALARA**).

### Group statistics
- **Two-group comparison**: **Shapiro–Wilk** → normal? **t-test** : **Mann–Whitney**; pair the
  $p$-value with **Cohen's $d$**, and size the cohort with the Week 09 power analysis.

For **segmentation quantification**, **ultrasound M-mode**, and **nuclear imaging (SPECT/PET)**, see
[Week 12](../Week12/README.md), where these notebooks were reviewed and used in Lecture 1.

## Environment

Uses Python with **NumPy**, **SciPy**, **scikit-image**, **SimpleITK**, and **matplotlib**.
