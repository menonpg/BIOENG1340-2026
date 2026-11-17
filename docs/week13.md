---
title: "Week 13 — Ultrasound Image Formation, Doppler & Final-Project Logistics"
---

**Lecture 1 (Nov 17)** settled the end-of-semester schedule and final-project deliverables, then continued **ultrasound image formation**: what a pressure wave is (longitudinal vs transverse), how a piezoelectric transducer generates it, beam formation as interference of spherical wavelets, 3-D ultrasound, **Doppler** velocimetry, speckle and speckle tracking, and a walkthrough of the A-line / B-mode simulation notebook. The class ended with a short project stand-up.

[Browse this week on GitHub](https://github.com/menonpg/BIOENG1340-2026/tree/main/Week13)

## Notebooks

### [Week 13 — Ultrasound beamforming: the beam is the Fourier transform of the aperture]({{ '/notebooks/week13-ultrasound-beamforming-aperture/' | relative_url }})

An ultrasound probe is an **array of small piezoelectric elements**. Each element radiates a spherical (here, cylindrical) wavelet; the **interference** of those wavelets is the transmitted beam. Two ideas from lecture are simulated here.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Beamforming_Aperture.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Beamforming_Aperture.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Beamforming_Aperture.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week13/Ultrasound_Beamforming_Aperture.ipynb)

### [Week 13 — Ultrasound Doppler: velocity, aliasing, color flow, pulsed vs continuous wave]({{ '/notebooks/week13-ultrasound-doppler/' | relative_url }})

Moving blood scatters sound with a **frequency shift** proportional to its velocity component along the beam: where is the angle between the beam and the flow. In this notebook:

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Doppler.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Doppler.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Doppler.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week13/Ultrasound_Doppler.ipynb)

### [Week 13 — Ultrasound image formation: acoustic impedance and Beer–Lambert attenuation]({{ '/notebooks/week13-ultrasound-impedance-attenuation/' | relative_url }})

A scanning ultrasound probe collects **line data**: it sends a pressure pulse down one scan line and records the echoes that return. Two physical ideas decide what those echoes look like.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Impedance_Attenuation.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Impedance_Attenuation.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Impedance_Attenuation.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week13/Ultrasound_Impedance_Attenuation.ipynb)

### [Week 13 — Ultrasound speckle: statistics, median filtering, compounding, and speckle tracking]({{ '/notebooks/week13-ultrasound-speckle-tracking/' | relative_url }})

Tissue contains many sub-resolution scatterers. Their echoes interfere inside every resolution cell, producing **speckle**: a granular texture that is **not** an image of the anatomy, but it is **stable** between frames when the tissue moves only slightly. That makes speckle both

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Speckle_Tracking.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Speckle_Tracking.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week13/Ultrasound_Speckle_Tracking.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week13/Ultrasound_Speckle_Tracking.ipynb)

<p class="backlinks"><a href="{{ '/' | relative_url }}">← Home</a> · <a href="{{ '/notebooks/' | relative_url }}">All notebooks</a></p>