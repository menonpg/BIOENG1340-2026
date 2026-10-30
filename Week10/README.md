# Week 10 — CT Image Formation, Reconstruction & Artifacts

How a CT scanner **acquires** projections, **reconstructs** an image, and where it goes wrong. Notebooks
cover scanner generations + the sinogram/back-projection, the **Fourier theory** behind CT, a
head-to-head **comparison** of the three reconstruction families, the common **artifacts**, and
**contrast agents**.

## Contents

| File | Description |
|------|-------------|
| [CTScanners_Sinogram_BackProjection.ipynb](CTScanners_Sinogram_BackProjection.ipynb) | **CT scanner generations** (pencil → fan → ring → multi-slice → helical) and the **C-arm / fluoroscopy** dose motivation; the **sinogram** by **rotate-and-sum**; the **Radon transform** (a point → a sinusoid) and **Radon = Hough** line detection; and **back-projection** — the unfiltered **laminogram** halo vs the **ramp-filtered** FBP, and image build-up **sweep by sweep**. |
| [FourierTheory_Parseval_CT.ipynb](FourierTheory_Parseval_CT.ipynb) | The Fourier basis of CT: 1D/2D Fourier transforms and k-space, **Parseval's theorem** (energy conservation, verified to round-off) and its meaning for SNR/filtering, the **Fourier Slice Theorem** (1D FFT of a projection = a radial line of the image's 2D FFT), and why polar sampling forces the **ramp filter** in FBP. |
| [ReconstructionMethods_Compare.ipynb](ReconstructionMethods_Compare.ipynb) | Head-to-head of three reconstructions on a Shepp–Logan phantom: **direct Fourier** (gridding), **filtered back-projection**, and **algebraic (SART)** — compared with full views, **sparse views** (where SART beats FBP's streaks), and **noisy** projections, with RMSE metrics and a speed-vs-robustness trade-off table. |
| [CTArtifacts.ipynb](CTArtifacts.ipynb) | Simulated CT artifacts: **metal / high-density** streak & **star** artifacts (persist with any number of views), **beam-hardening cupping**, **motion** blur/ghosting, **ring** artifacts (detector miscalibration), and **photon-counting / thermal noise** — plus the rule that *missing-data* streaks fade with more views while *corrupted-data* artifacts do not. |
| [ContrastAgents.ipynb](ContrastAgents.ipynb) | How contrast agents work: **iodine** raising Hounsfield units (CT), the iodine **K-edge** (33.2 keV) and why low kVp boosts contrast, the **time–attenuation (bolus)** curve and scan timing, and **gadolinium** shortening $T_1$ to brighten $T_1$-weighted MRI. |

## Key concepts

- **Acquisition**: scanner generations trade mechanical motion for speed/dose (pencil → fan → detector
  **ring** → **multi-slice** → **helical**); the **sinogram** is projections vs angle (rotate-and-sum);
  the **Radon transform** sends a point to a **sinusoid** and, for binary images, *is* the **Hough**
  line detector.
- **Back-projection**: plain back-projection over-weights low frequencies → a **laminogram halo**; the
  **ramp filter** $|k|$ corrects it, and the image sharpens **sweep by sweep**.
- **Parseval's theorem**: total energy is conserved between the spatial and frequency domains
  ($\sum|x_n|^2=\tfrac1N\sum|X_k|^2$) — the basis for reasoning about SNR and how filtering removes a
  measurable fraction of image energy.
- **Fourier Slice Theorem**: the 1D FFT of a projection at angle $\theta$ is a **radial line** of the
  image's 2D FFT. Many angles fill k-space → inverse 2D FFT returns the image.
- **Ramp filter**: projections sample k-space in polar form, oversampling the center ($\sim1/|k|$); the
  ramp $|k|$ cancels this — the analytic core of **filtered back-projection**.
- **Method trade-off**: **direct Fourier** and **FBP** are fast (FBP accurate and lowest RMSE with
  dense, clean data; naive Fourier shows gridding artifacts), while iterative **ART/SART** avoids FBP's
  **streak** artifacts and is more robust to **sparse views** and **noise** — the reason modern
  scanners use iterative reconstruction.
- **Artifacts**: **metal/high-density** → streak/**star** (persist regardless of views) + shadowing;
  **beam hardening** → **cupping**; **motion** → blur/ghosting; detector miscalibration → **rings**;
  low dose → **photon-counting/thermal noise**. *Missing-data* artifacts improve with more views;
  *corrupted-data* artifacts do not.
- **Contrast agents**: **iodine** raises $\mu$/HU (CT; K-edge at 33.2 keV favors low kVp); **bolus
  timing** separates arterial/venous phases; **gadolinium** shortens $T_1$ → bright on $T_1$-weighted MRI.

## Prerequisites

Builds on Week 09: [AlgebraicReconstruction_4x4.ipynb](../Week09/AlgebraicReconstruction_4x4.ipynb)
— the $A\boldsymbol\mu=\mathbf p$ pencil-beam system that the algebraic (SART) reconstruction scales up.

## Environment

Uses Python with **NumPy**, **SciPy**, **scikit-image**, and **matplotlib**.
