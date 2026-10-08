# Week 07 — Spatial Localization, Pulse Sequences & k-space

In-plane spatial localization and image formation: frequency/phase encoding, k-space, the
projection/Radon view, gradient- and spin-echo pulse sequences, image contrast, and functional MRI.

## Contents

| File | Description |
|------|-------------|
| [LectureNotes_SpatialLocalization.ipynb](LectureNotes_SpatialLocalization.ipynb) | **Lecture 1.** 2D k-space (FFT of a phantom), sinogram + inverse-Radon reconstruction, Cartesian vs radial k-space trajectories, and gradient-echo formation (dephase/rephase → echo at TE). |
| [LectureNotes_PulseSequences_and_kSpace.ipynb](LectureNotes_PulseSequences_and_kSpace.ipynb) | **Lecture 2.** Spin echo vs gradient echo (180° refocusing → $T_2$), T1/T2/PD contrast via TR/TE, inversion recovery (STIR), k-space theory (FOV/resolution, cropping → blur, undersampling → aliasing, filtering = convolution), and BOLD/fMRI; plus notes on phase-contrast 4D flow, DTI, spectroscopy, and gadolinium. |

## Key concepts

- A readout gradient makes each recorded signal a **line/projection in k-space**.
- **k-space ↔ image** via the 2D Fourier transform; center = contrast (low freq), edges = detail (high freq).
- **Projection-reconstruction (Radon)**: rotate the gradient, stack projections into a sinogram, inverse-Radon → slice.
- **Cartesian traversal**: $k_x=\frac{\gamma}{2\pi}G_x t$ (frequency encode), $k_y=\frac{\gamma}{2\pi}A_y$ (phase encode).
- **Gradient echo**: reversing the readout gradient rephases spins to form an echo; **TE/TR** set timing.
- **Spin echo**: a 180° RF pulse refocuses field-inhomogeneity dephasing → echo follows true $T_2$.
- **Contrast**: $S\propto\rho(1-e^{-TR/T_1})e^{-TE/T_2}$ — TR/TE select T1-, T2-, or PD-weighting; inversion recovery (STIR/FLAIR) nulls a tissue.
- **k-space**: cropping the center blurs (low-pass = convolution), undersampling aliases/folds over, boosting the periphery sharpens edges.
- **BOLD/fMRI**: a $T_2^*$ effect — oxyhemoglobin (diamagnetic) raises signal where neurons activate.

## Environment

Uses Python with **NumPy**, **matplotlib**, and **scikit-image** (phantom, `radon`/`iradon`),
installed into the notebook kernel on first run.
