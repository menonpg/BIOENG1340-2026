# Week 07 — Spatial Localization in MRI: k-space & Image Formation

In-plane spatial localization: how MRI resolves position *within* a selected slice using
frequency/phase encoding, k-space, the projection/Radon view, and the gradient-echo pulse sequence.

## Contents

| File | Description |
|------|-------------|
| [LectureNotes_SpatialLocalization.ipynb](LectureNotes_SpatialLocalization.ipynb) | Lecture notes with runnable illustrations: 2D k-space (FFT of a phantom), sinogram + inverse-Radon reconstruction, Cartesian vs radial k-space trajectories, and gradient-echo formation (dephase/rephase → echo at TE). |

## Key concepts

- A readout gradient makes each recorded signal a **line/projection in k-space**.
- **k-space ↔ image** via the 2D Fourier transform; center = contrast (low freq), edges = detail (high freq).
- **Projection-reconstruction (Radon)**: rotate the gradient, stack projections into a sinogram, inverse-Radon → slice.
- **Cartesian traversal**: $k_x=\frac{\gamma}{2\pi}G_x t$ (frequency encode), $k_y=\frac{\gamma}{2\pi}A_y$ (phase encode).
- **Gradient echo**: reversing the readout gradient rephases spins to form an echo; **TE/TR** set timing.

## Environment

Uses Python with **NumPy**, **matplotlib**, and **scikit-image** (phantom, `radon`/`iradon`),
installed into the notebook kernel on first run.
