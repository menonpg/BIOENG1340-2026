---
title: "Week 04 — SNR & CNR"
nav_order: Week04
---

Signal-to-noise ratio (SNR) and contrast-to-noise ratio (CNR): building synthetic images, measuring per-region SNR/CNR, testing statistical distinguishability, and recovering contrast by signal averaging.

[Browse this week on GitHub](https://github.com/menonpg/BIOENG1340-2026/tree/main/Week04)

## Notebooks

### [Synthetic Two-Circle Image with SimpleITK](notebooks/week04-generatetwocircles-supernoisy.md)

Generate a sample image from scratch (no DICOM needed) containing **two circles**, each with a different int8 intensity ("color"). We then add **different noise to each region** and save both the clean and noisy images. Every step is parameterized in the config cell below.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week04/GenerateTwoCircles-SuperNoisy.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week04/GenerateTwoCircles-SuperNoisy.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week04/GenerateTwoCircles-SuperNoisy.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week04/GenerateTwoCircles-SuperNoisy.ipynb)

### [Synthetic Two-Circle Image with SimpleITK](notebooks/week04-generatetwocircles.md)

Generate a sample image from scratch (no DICOM needed) containing **two circles**, each with a different int8 intensity ("color"). We then add **different noise to each region** and save both the clean and noisy images. Every step is parameterized in the config cell below.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week04/GenerateTwoCircles.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week04/GenerateTwoCircles.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week04/GenerateTwoCircles.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week04/GenerateTwoCircles.ipynb)

### [Optimizing SNR and CNR](notebooks/week04-optimizingsnr-cnr.md)

This notebook illustrates the imaging lesson on **signal-to-noise ratio (SNR)** vs **contrast-to-noise ratio (CNR)**, and how to choose the optimal measurement time when the signal decays exponentially.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week04/OptimizingSNR_CNR.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week04/OptimizingSNR_CNR.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week04/OptimizingSNR_CNR.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week04/OptimizingSNR_CNR.ipynb)


[← Home](index.md)
