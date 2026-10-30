# BIOENG1340-2026

Course materials and coursework for **BIOENG 1340/2340 (Fall 2026)**: medical
image processing and analysis using MATLAB, Python (SimpleITK), and 3D
visualization tools (ITK-SNAP, ParaView).

## Repository structure

| Folder | Topic | Details |
|--------|-------|---------|
| [Week01](Week01/) | DICOM loading & first scripts | Reading a cardiac DICOM stack in MATLAB and Python, basic image processing, and writing a VTK volume. See [Week01/README.md](Week01/README.md). |
| [Week02](Week02/) | Least-squares fitting & VTK export | Ordinary least squares (OLS) line fitting in MATLAB and a reusable VTK volume writer. See [Week02/README.md](Week02/README.md). |
| [Week03](Week03/) | Image filtering & convolution as a linear operator | Filtering/deconvolution in MATLAB, building the convolution matrix ($Ax=b$), and k-space / derivative operators. See [Week03/README.md](Week03/README.md). |
| [Week04](Week04/) | SNR & CNR | Synthetic two-circle images, per-region SNR/CNR, statistical tests, and signal averaging. See [Week04/README.md](Week04/README.md). |
| [Week05](Week05/) | MR physics: Larmor, Bloch & slice selection | Gyromagnetic ratio, Bloch-equation relaxation ($T_1/T_2$), tumor-vs-normal contrast, and z-gradient slice selection. See [Week05/README.md](Week05/README.md). |
| [Week06](Week06/) | MRI image formation quiz solutions | Worked answers on precession, FID, Bloch equations, relaxation, and slice selection. See [Week06/README.md](Week06/README.md). |
| [Week07](Week07/) | Spatial localization, pulse sequences & k-space | Frequency/phase encoding, k-space & Radon reconstruction, gradient/spin echo, contrast (T1/T2/PD), and BOLD/fMRI. See [Week07/README.md](Week07/README.md). |
| [Week08](Week08/) | X-ray & CT image formation | Beer–Lambert attenuation, energy/wavelength, beam hardening, CT reconstruction via the Radon transform, plus X-ray physics (polyenergetic spectra, ionization, half-value layer, mass attenuation) and Hounsfield units. See [Week08/README.md](Week08/README.md). |
| [Week09](Week09/) | Algebraic CT reconstruction & study design | Algebraic reconstruction of a 4×4 image from pencil-beam Beer–Lambert projections ($A\boldsymbol\mu=\mathbf p$, rank/orientations, the null-space "ghost", least-squares vs ART/Kaczmarz, Poisson noise), and **cohort/sample-size determination** for a patient–control study. See [Week09/README.md](Week09/README.md). |
| [Week10](Week10/) | CT image formation, reconstruction & artifacts | CT **scanner generations**, the **sinogram**/Radon transform and **back-projection** (laminogram vs ramp filter); **Fourier theory** (Parseval + the Fourier Slice Theorem) behind CT; a head-to-head **comparison** of direct-Fourier, filtered back-projection, and algebraic (SART) reconstruction; simulated **CT artifacts** (metal/star, beam-hardening cupping, motion, rings, noise); and **contrast agents** (iodine/HU, K-edge, bolus timing, gadolinium/$T_1$). See [Week10/README.md](Week10/README.md). |
| [Project](Project/) | Team project topic discussions | Project framework, dataset sources, and the running record of team/topic discussions. See [Project/README.md](Project/README.md). |

## Working with the data

- The `Week01/images/` folder contains the sample **pig cardiac MRI** dataset
  (DICOM stack, NIfTI, VTK, STL, and ParaView state files).
- Large installers (e.g. the ITK-SNAP `.dmg`) are **not** tracked in git; see
  [.gitignore](.gitignore). Download tools directly from their official sites.

## Tools used

- **MATLAB** — DICOM I/O, image processing, VTK export
- **Python** with **SimpleITK** — DICOM series reading and processing
- **ITK-SNAP** — segmentation
- **ParaView** — 3D volume / surface visualization