---
title: "Week 12 — Nuclear Imaging, SPECT/PET & Project Methods Review"
---

**Lecture 1 (Nov 10)** opened with a review of project-analysis notebooks from Week 11, then developed nuclear imaging from radiotracer physics through SPECT/PET acquisition, reconstruction, and image fusion. The notebook locations now reflect the material used in this lecture.

[Browse this week on GitHub](https://github.com/menonpg/BIOENG1340-2026/tree/main/Week12)

## Notebooks

### [Week 12 — Nuclear Imaging: Scintigraphy, SPECT & PET]({{ '/notebooks/week12-nuclearimaging-pet-spect/' | relative_url }})

After MRI, CT, and ultrasound we turn to **nuclear imaging** (scintigraphy). A **radiotracer** is administered; its distribution reflects tracer-specific physiology, and it **emits** radiation that we detect from outside. This notebook builds the key ideas and simulates them.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week12/NuclearImaging_PET_SPECT.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week12/NuclearImaging_PET_SPECT.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week12/NuclearImaging_PET_SPECT.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week12/NuclearImaging_PET_SPECT.ipynb)

### [Week 12 — Quantifying a Segmentation: Volume & Shape]({{ '/notebooks/week12-segmentationquantification/' | relative_url }})

Once you have a **3-D segmentation mask** (from ITK-SNAP, ParaView, or an AI model), the next step is to turn it into **numbers**: a physical **volume** and **shape descriptors**. This is the core measurement step for several class projects (hippocampus volume, left-ventricle volume over time, optic-nerve-head vessel morphology).

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week12/SegmentationQuantification.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week12/SegmentationQuantification.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week12/SegmentationQuantification.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week12/SegmentationQuantification.ipynb)

### [Week 12 — Ultrasound M-mode (a scan line over time)]({{ '/notebooks/week12-ultrasound-mmode/' | relative_url }})

A preview of ultrasound imaging, motivated by the echocardiography project (stacking video frames into a 3-D volume). Standard **B-mode** ultrasound is a 2-D image that updates in time (a video). **M-mode** (“motion mode”) instead takes a **single scan line** and plots it **over time** — depth on one axis, time on the other — giving very high temporal resolution for moving structures (heart valves, vessel walls, chamber walls).

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_MMode.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_MMode.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_MMode.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week12/Ultrasound_MMode.ipynb)

<p class="backlinks"><a href="{{ '/' | relative_url }}">← Home</a> · <a href="{{ '/notebooks/' | relative_url }}">All notebooks</a></p>