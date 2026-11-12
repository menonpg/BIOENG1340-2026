---
title: "Week 12 — Nuclear Imaging, Ultrasound Physics & Project Stand-ups"
---

**Lecture 1 (Nov 10)** opened with a review of project-analysis notebooks from Week 11, then developed nuclear imaging from radiotracer physics through SPECT/PET acquisition, reconstruction, and image fusion. **Lecture 2 (Nov 12)** began with the first Kanban-style project stand-ups, then introduced **ultrasound** physics and image formation: pressure-wave echoes, the swept-beam teardrop point spread function, acoustic impedance, and Beer–Lambert attenuation. Lecture 1 notebooks: NuclearImaging_PET_SPECT, SegmentationQuantification, Ultrasound_MMode. Lecture 2 notebooks: Ultrasound_PSF_Convolution, Ultrasound_Impedance_Attenuation.

[Browse this week on GitHub](https://github.com/menonpg/BIOENG1340-2026/tree/main/Week12)

## Notebooks

### [Week 12 — Nuclear Imaging: Scintigraphy, SPECT & PET]({{ '/notebooks/week12-nuclearimaging-pet-spect/' | relative_url }})

After MRI, CT, and ultrasound we turn to **nuclear imaging** (scintigraphy). A **radiotracer** is administered; its distribution reflects tracer-specific physiology, and it **emits** radiation that we detect from outside. This notebook builds the key ideas and simulates them.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week12/NuclearImaging_PET_SPECT.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week12/NuclearImaging_PET_SPECT.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week12/NuclearImaging_PET_SPECT.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week12/NuclearImaging_PET_SPECT.ipynb)

### [Week 12 — Quantifying a Segmentation: Volume & Shape]({{ '/notebooks/week12-segmentationquantification/' | relative_url }})

Once you have a **3-D segmentation mask** (from ITK-SNAP, ParaView, or an AI model), the next step is to turn it into **numbers**: a physical **volume** and **shape descriptors**. This is the core measurement step for several class projects (hippocampus volume, left-ventricle volume over time, optic-nerve-head vessel morphology).

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week12/SegmentationQuantification.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week12/SegmentationQuantification.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week12/SegmentationQuantification.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week12/SegmentationQuantification.ipynb)

### [Week 12 — Ultrasound image formation: acoustic impedance and Beer–Lambert attenuation]({{ '/notebooks/week12-ultrasound-impedance-attenuation/' | relative_url }})

A scanning ultrasound probe collects **line data**: it sends a pressure pulse down one scan line and records the echoes that return. Two physical ideas decide what those echoes look like.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_Impedance_Attenuation.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_Impedance_Attenuation.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_Impedance_Attenuation.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week12/Ultrasound_Impedance_Attenuation.ipynb)

### [Week 12 — Ultrasound M-mode (a scan line over time)]({{ '/notebooks/week12-ultrasound-mmode/' | relative_url }})

A preview of ultrasound imaging, motivated by the echocardiography project (stacking video frames into a 3-D volume). Standard **B-mode** ultrasound is a 2-D image that updates in time (a video). **M-mode** (“motion mode”) instead takes a **single scan line** and plots it **over time** — depth on one axis, time on the other — giving very high temporal resolution for moving structures (heart valves, vessel walls, chamber walls).

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_MMode.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_MMode.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_MMode.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week12/Ultrasound_MMode.ipynb)

### [Week 12 — Ultrasound point spread function: why a swept scan line gives a teardrop]({{ '/notebooks/week12-ultrasound-psf-convolution/' | relative_url }})

Every imaging system blurs. If is the true image (the tissue reflectivity we would like to see) and the system has a convolution kernel (its **point spread function**, PSF), the measured, digitized image is

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_PSF_Convolution.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_PSF_Convolution.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week12/Ultrasound_PSF_Convolution.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week12/Ultrasound_PSF_Convolution.ipynb)

<p class="backlinks"><a href="{{ '/' | relative_url }}">← Home</a> · <a href="{{ '/notebooks/' | relative_url }}">All notebooks</a></p>