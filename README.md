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
| [Week07](Week07/) | Spatial localization & k-space | Frequency/phase encoding, k-space, projection/Radon reconstruction, and the gradient-echo pulse sequence. See [Week07/README.md](Week07/README.md). |

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