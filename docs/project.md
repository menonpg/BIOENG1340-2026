---
title: "Team Project"
---

Working space and notes for the BIOENG 1340/2340 **final group project**. This page tracks the
project framework and the running record of team / topic discussions held in class.

## Project framework

- **Teams:** 1–3 people (working solo is allowed). Declare your team on the class roster sheet by
  setting your *in a team* column to **Y**, then fill in team members, a tentative topic, project
  type, and dataset on the *Final Group Project 2026* sheet.
- **Project type:** *analysis*, *software development*, or *both*.
  - *Analysis* — reconstruct/visualize medical images in 3D, extract objects, make measurements,
    collect and compare data (e.g. patients vs controls).
  - *Development* — implement or adapt an algorithm / open-source tool to process images.
- **Deliverable (Assignment 4):** a one-page **specific-aims** proposal (background → hypothesis →
  2–3 aims with subtasks) plus a process flowchart; later a poster and final presentation.
- **Project management:** 4-week performance period tracked on a **Kanban board**
  (kanbanflow.com) with To-Do → In-Progress → Testing → Complete swim lanes (agile workflow).

## Suggested workflow for every project

1. Find and **download** a sample dataset; confirm format (DICOM / NIfTI / VTK / video).
2. **Visualize** it (ParaView / ITK-SNAP) and confirm you can work with it.
3. Note the **image-formation method** (modality, systems model) — a teachable part of the project.
4. Characterize **baseline SNR / CNR**.
5. Develop an algorithm to **quantify a metric** that distinguishes groups or characterizes disease.

## Dataset sources

- Prior-year project sheets (2023–2025) — richest source of vetted datasets and ideas.
- Public repositories: Zenodo, OSF/OSIRIX, Google Dataset Search, the Human Connectome Project,
  Stanford (e.g. EchoNet echocardiography), and your own lab/research data.

## First discussion (Oct 13) — emerging topics

| Team | Topic | Data / notes |
|------|-------|--------------|
| Retinal vasculature | 3D multi-photon microscopy of whole eye-back vasculature; segment vessels and quantify **density**, **branching**, and **orientation** (glaucoma / IOP deformation). | Private lab 3D data; aim toward VTK/NIfTI → ParaView volume rendering + vessel enhancement (e.g. Frangi vesselness), targeting a conference abstract. |
| Echocardiography | Analyze cardiac **ultrasound** (echo) videos/images; segmentation or a cohort metric. | Stanford EchoNet (~10k echocardiograms); likely Python + ParaView/ITK-SNAP. |
| Segmentation (TBD) | Accessible imaging dataset; segmentation or image-formation characterization. | Dataset selection in progress. |

Project scope guidance: an **N-of-1/N-of-2** proof-of-concept (one or two cases, novel method) is
acceptable, as is a small **cohort** study (apply a validated method across hand-selected cases).

## Second discussion (Oct 29) — data review & refined aims

Each team showed sample image data and refined their aims. Deadlines set: Assignment 4 **first draft
Nov 1**, final **Nov 3**. Everyone posts their **Kanban board** link in the class sheet.

| Team | Topic & refined aims | Data / tools |
|------|----------------------|--------------|
| Ashvin & Harrison | **Alzheimer's brain MRI** — compare the **ventricles** (around the hippocampus) in Alzheimer's vs healthy. Candidate metrics: shape of the mid-slice "X" ventricle, and **volume of high-density tissue** (amyloid-related) above a threshold in gray/white matter. | OpenNeuro MRI (`.img`/NIfTI, already **skull-stripped**); FSL preprocessing, ITK-SNAP segmentation, ParaView slice filter for 2D/3D. |
| Jen Hu & Yosi | **fMRI functional connectivity** — developmental **prosopagnosia** (face blindness) vs controls watching Game-of-Thrones clips; test whether DP shows greater **inter-individual variability** in FC of face-selective / higher-order regions. 10 subjects (5/5), ages 18–24. | OpenNeuro (FSL-preprocessed time series); further motion / confound-regression / B0 correction; ROI around **hippocampus** (original study used caudate); 3D visualization in ParaView. |
| Xinyue & Shiqi | **Retinal vasculature** (multiphoton microscopy of the optic-nerve canal) — segment vessels and quantify **density** and **orientation** (coronal vs vertical) relevant to glaucoma risk. Pivoted to a **cross-species** comparison (limited human samples). | AI vessel segmentation (~95% precision vs manual labels) + **skeletonization / centerline**; **downsampling** for whole-volume analysis; texture features (**GLCM / entropy**, pyradiomics) as appearance proxies. |
| Christian | **Echocardiography** — a novel idea to **concatenate the time series as a Z-axis** for echo videos (treat time as a third spatial dimension for volumetric analysis). | Echo video data; aims to be defined. |

**Analysis techniques discussed (applicable across projects):**

- **Texture / appearance features** via the **gray-level co-occurrence matrix (GLCM)** —
  contrast, correlation, and **entropy** quantify heterogeneity (e.g. dense vessel networks → high
  entropy). The **PyRadiomics** library computes shape, intensity, and texture features in 2D and 3D;
  these act as *proxies* for hard-to-measure clinical properties (tortuosity, perfusion).
- **Vessel analysis**: Frangi **vesselness** filtering → threshold → binary mask → **morphological
  thinning / skeletonization** → parametric centerline network (branching, diameter).
- **Brain MRI**: **skull stripping** (FSL deterministic algorithms), ventricle segmentation, and
  high-density-tissue quantification; slicing in ParaView.
- **Scale strategies**: **downsampling** for very large volumes, or tessellating into cubes for
  piecewise analysis and recombination.

> The instructor will also publish an **HTML project page** (GitHub Pages) consolidating each team's
> topic, data, and ideas so all project work is viewable in one place.

[Browse the project folder on GitHub](https://github.com/menonpg/BIOENG1340-2026/tree/main/Project)

[← Home](index.md)
