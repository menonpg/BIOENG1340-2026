---
title: "Week 09 — Algebraic CT Reconstruction & Study Design"
nav_order: Week09
---

Topics: (1) reconstructing a hypothetical **4×4 attenuation image** (16 unknown 's) from **pencil X-ray beam** projections, exactly as **Hounsfield's EMI scanner** did — each ray is one **Beer–Lambert equation**, and the stack of rays forms a linear system that we solve; and (2) **cohort (sample) size determination** for a patient–control study.

[Browse this week on GitHub](https://github.com/menonpg/BIOENG1340-2026/tree/main/Week09)

## Notebooks

### [Week 09 — Algebraic Reconstruction: solving for the $\mu$'s](notebooks/week09-algebraicreconstruction-4x4.md)

Last week we saw that a radiograph is a **projection** — the line integral of the linear attenuation coefficient along a beam. This week we do what **Hounsfield's EMI scanner** did: treat each **pencil X-ray beam** as one **Beer–Lambert equation** and *solve the linear system* for every inside a hypothetical **4×4 image** (16 unknowns).

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week09/AlgebraicReconstruction_4x4.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week09/AlgebraicReconstruction_4x4.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week09/AlgebraicReconstruction_4x4.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week09/AlgebraicReconstruction_4x4.ipynb)

### [Week 09 — Cohort (Sample) Size Determination for a Patient–Control Study](notebooks/week09-cohortsizedetermination.md)

How many patients and controls do we actually need to enroll? Too **few** and a real effect is missed (wasted study, ethical cost of exposing participants for nothing); too **many** and we waste time, money, and expose more people than necessary. **Sample-size (power) analysis** finds the smallest cohort that can reliably detect an effect of a pre-specified size.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week09/CohortSizeDetermination.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week09/CohortSizeDetermination.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week09/CohortSizeDetermination.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week09/CohortSizeDetermination.ipynb)


[← Home](index.md)
