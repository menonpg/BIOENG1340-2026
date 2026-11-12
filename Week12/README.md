# Week 12 — Nuclear Imaging, SPECT/PET & Project Methods Review

**Lecture 1 (Nov 10)** opened with a review of project-analysis notebooks from Week 11, then developed nuclear imaging from radiotracer physics through SPECT/PET acquisition, reconstruction, and image fusion. The notebook locations now reflect the material used in this lecture.

## Contents

| File | Description |
|------|-------------|
| [NuclearImaging_PET_SPECT.ipynb](NuclearImaging_PET_SPECT.ipynb) | Radiotracer decay and activity; emission tomography and Poisson counting; SPECT Anger cameras vs PET coincidence detection; count/SNR trade-offs; and functional–anatomical fusion. Includes a PET line-of-response simulation. |
| [SegmentationQuantification.ipynb](SegmentationQuantification.ipynb) | Convert a labeled 3-D mask into physical volume and shape descriptors using voxel spacing, SimpleITK, and scikit-image; includes export of a labeled NIfTI volume. |
| [Ultrasound_MMode.ipynb](Ultrasound_MMode.ipynb) | Build an M-mode image from a scan line through B-mode frames over time, then estimate periodic wall motion / heart rate with frequency analysis. |

## Lecture notes

### Review: segmentation measurements

A segmentation is a labeled voxel volume. For isotropic or anisotropic voxel spacing, physical volume is the foreground voxel count times the voxel volume:

$$V = N_{\mathrm{vox}}\,\Delta x\,\Delta y\,\Delta z.$$

The mask can be represented as a SimpleITK image with spacing metadata and exported as NIfTI or VTK for ITK-SNAP / ParaView. Shape descriptors such as elongation, roundness, flatness, and sphericity help distinguish blob-like from tubular objects. Connected-component labeling can assign a separate label to each disconnected island so each object can be measured independently. These steps are useful for hippocampal, left-ventricular, and vessel projects.

### Review: ultrasound M-mode

B-mode is a 2-D brightness image repeated over time. M-mode follows one scan line through those frames and stacks the line profiles, producing a depth-by-time image. The time series of a moving wall can then be analyzed (for example, with a power spectrum) to estimate a dominant motion frequency or heart rate.

### Nuclear imaging: emission and reconstruction

Nuclear imaging detects radiation emitted by an administered radiotracer. This makes its signal source **active**, unlike CT transmission or ultrasound echo. Projections can be organized as a sinogram and reconstructed with CT-like methods such as filtered back-projection. Emission events are relatively sparse, however, so projections are count-limited and noisy.

Radioactive nuclei decay exponentially:

$$N(t)=N_0\,2^{-t/T_{1/2}},\qquad A=\lambda N,$$

where $T_{1/2}$ is the half-life and activity $A$ is measured in becquerels (decays/s). Common examples discussed were Tc-99m for SPECT (about 6 hours) and F-18, commonly administered as FDG, for PET (about 110 minutes). Tracer choice balances biology, detectability, radiation exposure, and practical imaging logistics; shorter half-life is not automatically better in every context.

### SPECT and PET

- **SPECT** detects single gamma photons. A collimator in an Anger scintillation camera provides directional information as detector views are collected around the patient.
- **PET** detects pairs of 511 keV photons from positron annihilation. Coincident detections around a detector ring define lines of response, providing electronic collimation.
- In myocardial perfusion SPECT, viable perfused myocardium takes up tracer; low uptake can indicate a perfusion defect or scar. Short-axis slices may be summarized as a polar map from apex to base.
- PET interpretation depends on the tracer. FDG uptake can highlight tumors and other glucose-avid tissue; PET does not have one universal bright/dark interpretation opposite to SPECT.

For Poisson-limited data, noise scales approximately as $\sqrt{N}$ and SNR therefore improves approximately as $\sqrt{N}$ as detected counts increase. Longer acquisition can improve precision, but also gives patient motion more opportunity to blur or distort the reconstruction.

### Functional–anatomical fusion

PET/SPECT provide functional information but limited anatomical detail, so they are commonly fused with CT or MRI. Registration is an ill-posed problem: many transformations may appear plausible. Similarity objectives such as mutual information can help optimize alignment, but correct clinical correspondence still requires validation. Motion between acquisitions is one source of mismatch.

## Practical project workflow

1. Inspect the source volume and confirm its format and voxel spacing.
2. Visualize it in ITK-SNAP or ParaView, then create or load a segmentation.
3. Export masks and large derived volumes in a suitable format, but avoid committing bulky/generated data; use `.gitignore` and approved storage such as course or lab drives where appropriate.
4. Quantify volume and shape, or construct an M-mode representation for time-varying ultrasound, and validate the resulting measurements against the image.

## Environment

The notebooks use Python with **NumPy**, **SciPy**, **scikit-image**, **SimpleITK**, and **matplotlib**.
