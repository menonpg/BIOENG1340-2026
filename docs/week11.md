---
title: "Week 11 — CT Artifacts, Contrast Agents, Dosimetry & Group Statistics"
---

Finishing CT with **artifacts** and **contrast agents**, then covering **radiation dosimetry** and the statistical comparison of patient and control groups. Nuclear imaging and the segmentation / M-mode project-method notebooks were reviewed in Week 12 and are now organized there.

[Browse this week on GitHub](https://github.com/menonpg/BIOENG1340-2026/tree/main/Week11)

## Notebooks

### [Week 11 — CT Artifacts]({{ '/notebooks/week11-ctartifacts/' | relative_url }})

Real CT images are rarely perfect. This notebook simulates the artifacts discussed in class and shows **why** they arise and **which go away with more projections** and which do not.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week11/CTArtifacts.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week11/CTArtifacts.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week11/CTArtifacts.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week11/CTArtifacts.ipynb)

### [Week 11 — Comparing Two Groups (Patients vs Controls)]({{ '/notebooks/week11-comparingtwogroups/' | relative_url }})

Most imaging projects end with the same question: **is a measured metric different between two groups?** (e.g. hippocampal volume in Alzheimer's vs controls). Choosing the **right statistical test** depends on whether the data are **normally distributed**. This notebook walks the full decision:

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week11/ComparingTwoGroups.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week11/ComparingTwoGroups.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week11/ComparingTwoGroups.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week11/ComparingTwoGroups.ipynb)

### [Week 11 — Contrast Agents (CT & MRI)]({{ '/notebooks/week11-contrastagents/' | relative_url }})

Many structures (blood vessels, tumors, inflamed tissue) have almost the **same** native attenuation or relaxation as their surroundings, so they are invisible. **Contrast agents** are injected to *temporarily* change a tissue property and make those structures stand out.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week11/ContrastAgents.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week11/ContrastAgents.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week11/ContrastAgents.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week11/ContrastAgents.ipynb)

### [Week 11 — Radiation Dosimetry]({{ '/notebooks/week11-radiationdosimetry/' | relative_url }})

Ionizing-radiation imaging (X-ray, CT, fluoroscopy, nuclear) carries a **dose** cost. Dosimetry is the science of **measuring** it. This notebook defines the units and simulates the key quantities.

[View on GitHub](https://github.com/menonpg/BIOENG1340-2026/blob/main/Week11/RadiationDosimetry.ipynb) · [nbviewer](https://nbviewer.org/github/menonpg/BIOENG1340-2026/blob/main/Week11/RadiationDosimetry.ipynb) · [Open in Colab](https://colab.research.google.com/github/menonpg/BIOENG1340-2026/blob/main/Week11/RadiationDosimetry.ipynb) · [Download](https://raw.githubusercontent.com/menonpg/BIOENG1340-2026/main/Week11/RadiationDosimetry.ipynb)

<p class="backlinks"><a href="{{ '/' | relative_url }}">← Home</a> · <a href="{{ '/notebooks/' | relative_url }}">All notebooks</a></p>