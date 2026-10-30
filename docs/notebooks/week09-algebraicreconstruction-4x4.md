---
title: "Week 09 — Algebraic Reconstruction: solving for the $\mu$'s"
week: Week09
---

*Week09 · 9 code cells*

Last week we saw that a radiograph is a **projection** — the line integral of the linear attenuation coefficient along a beam. This week we do what **Hounsfield's EMI scanner** did: treat each **pencil X-ray beam** as one **Beer–Lambert equation** and *solve the linear system* for every inside a hypothetical **4×4 image** (16 unknowns).

## Open this notebook

- [View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week09/AlgebraicReconstruction_4x4.ipynb) — rendered with outputs
- [Open in nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week09/AlgebraicReconstruction_4x4.ipynb) — clean static render
- [Open in Google Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week09/AlgebraicReconstruction_4x4.ipynb) — run it in the browser
- [Download .ipynb](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week09/AlgebraicReconstruction_4x4.ipynb)

[← Week 09 — Algebraic CT Reconstruction & Study Design](week09.md) · [All notebooks](notebooks.md) · [Home](index.md)
