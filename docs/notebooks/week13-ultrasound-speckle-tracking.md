---
title: "Week 13 — Ultrasound speckle: statistics, median filtering, compounding, and speckle tracking"
week: Week13
---

*Week13 · 6 code cells*

Tissue contains many sub-resolution scatterers. Their echoes interfere inside every resolution cell, producing **speckle**: a granular texture that is **not** an image of the anatomy, but it is **stable** between frames when the tissue moves only slightly. That makes speckle both

## Open this notebook

- [View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Speckle_Tracking.ipynb) — rendered with outputs
- [Open in nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Speckle_Tracking.ipynb) — clean static render
- [Open in Google Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Speckle_Tracking.ipynb) — run it in the browser
- [Download .ipynb](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week13/Ultrasound_Speckle_Tracking.ipynb)

<p class="backlinks"><a href="{{ '/week13/' | relative_url }}">← Week13</a> · <a href="{{ '/notebooks/' | relative_url }}">All notebooks</a> · <a href="{{ '/' | relative_url }}">Home</a></p>