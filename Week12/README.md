# Week 12 — Nuclear Imaging, Ultrasound Physics & Project Stand-ups

**Lecture 1 (Nov 10)** opened with a review of project-analysis notebooks from Week 11, then developed nuclear imaging from radiotracer physics through SPECT/PET acquisition, reconstruction, and image fusion. **Lecture 2 (Nov 12)** began with the first Kanban-style project stand-ups, then introduced **ultrasound** physics and image formation: pressure-wave echoes, the swept-beam teardrop point spread function, acoustic impedance, and Beer–Lambert attenuation. Lecture 1 notebooks: `NuclearImaging_PET_SPECT`, `SegmentationQuantification`, `Ultrasound_MMode`. Lecture 2 notebooks: `Ultrasound_PSF_Convolution`, `Ultrasound_Impedance_Attenuation`.

## Contents

| File | Description |
|------|-------------|
| [NuclearImaging_PET_SPECT.ipynb](NuclearImaging_PET_SPECT.ipynb) | Radiotracer decay and activity; emission tomography and Poisson counting; SPECT Anger cameras vs PET coincidence detection; count/SNR trade-offs; and functional–anatomical fusion. Includes a PET line-of-response simulation. |
| [SegmentationQuantification.ipynb](SegmentationQuantification.ipynb) | Convert a labeled 3-D mask into physical volume and shape descriptors using voxel spacing, SimpleITK, and scikit-image; includes export of a labeled NIfTI volume. |
| [Ultrasound_PSF_Convolution.ipynb](Ultrasound_PSF_Convolution.ipynb) | Simulate a swept-sector ultrasound scan to show why the point spread function is teardrop-shaped, using $J = I * H$ in beam coordinates, scan conversion to the display, a blurred phantom, and axial vs lateral resolution vs depth. |
| [Ultrasound_Impedance_Attenuation.ipynb](Ultrasound_Impedance_Attenuation.ipynb) | Acoustic impedance $Z=\rho c$ and the reflection coefficient at boundaries; Beer–Lambert attenuation and the resolution/penetration trade-off; build an A-line and a B-mode image of a phantom (cyst, stone), with time-gain compensation, shadowing, posterior enhancement, and a frequency comparison. |
| [Ultrasound_MMode.ipynb](Ultrasound_MMode.ipynb) | Build an M-mode image from a scan line through B-mode frames over time, then estimate periodic wall motion / heart rate with frequency analysis. |

## Lecture 1 notes (Nov 10)

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

## Lecture 2 notes (Nov 12)

### Project stand-ups and course web pages

Class opened with a short **agile-style stand-up** for each project team: share the Kanban board, then say what is in progress this week, what is planned next, and any blockers. The three weeks that remain include Thanksgiving, so a formal **midterm project review** will be scheduled for next Thursday or the first class of the last week of November. Team summaries and guidance are recorded in [Project/README.md](../Project/README.md). Every lecture and week also has a page on the course GitHub Pages site (`<github handle>.github.io/<repository name>`), with notebook viewer and Colab links; use Cmd/Ctrl+Shift+R to refresh after an update.

### Ultrasound among the four modalities

As framed in lecture, CT and ultrasound measure a **passive** phenomenon: in CT the regional linear attenuation of X-rays passing through the object, in ultrasound the scatterers in the field of view reflecting, transmitting, and absorbing a pressure wave. MRI (precession of protons) and scintigraphy (photon counting from radiotracers) measure an **active** phenomenon. An ultrasound **transducer** is both the source and the detector: a piezoelectric element converts an electrical input into a pressure wave and converts the returning echo back into an electrical signal.

### Ultrasound basics

- **Frequency ranges.** Ultrasound is sound above the range of human hearing (above about 20 kHz); infrasound is below it. Medical ultrasound is typically **1–10 MHz**, up to about **18 MHz** for joints and breast and roughly **70 MHz** for ophthalmology. Fetal imaging is typically about 3–5 MHz.
- **Frequency choice.** Higher frequency resolves smaller structures (the lecture intuition) because the wavelength $\lambda=c/f$ is shorter, but it is attenuated faster and so reaches only shallow depths. Lower frequency penetrates deeper but with coarser resolution. Ultrasound is non-ionizing and well below ionizing photon energies, hence its safety.
- **Probes.** An array of elements forms a **beam**; the beam pattern is governed by Fourier theory (it is related to the Fourier transform of the aperture shape), which we will return to. Some probes give a 3-D field of view; others produce a single scan line that is **swept in an arc** to make a sector image.
- **Views.** In a transthoracic four-chamber view the probe sits on the chest and the apex of the heart is nearest the probe. In a transesophageal echo the probe is swallowed and views the heart from behind, so the left ventricle apex is away from the probe, at the far (pointed) end of the sector, and the image looks upside down by comparison.
- **History.** SONAR was developed around World War II and medical ultrasound followed in the 1950s, in the same period as the Fourier-based revolution in CT and MRI. Transducer arrays (1980s), Doppler flow imaging (1980s), and real-time 3-D ultrasound followed.

### Echo formation and the ultrasound Beer–Lambert law

The transducer emits a spherical pressure wave into the sample. Each scatterer (for example the tiny scatterers that make up a tissue wall) acts as a **new pressure source**, reflecting, transmitting, or absorbing the wave; the part that returns to the transducer is recorded. The **time of flight** gives depth, and the echo amplitude carries the reflectivity weighted by the attenuation along the path.

For CT, Beer–Lambert is $I=I_0e^{-\mu\,\Delta x}$. In ultrasound the wave travels from the source to a scatterer at depth $d$ and back, a round trip of $2d$:

$$I = I_0\,e^{-\mu\,2d}.$$

Attenuation therefore limits ultrasound to relatively shallow fields of view, with good spatial resolution but poor contrast-to-noise compared with CT or MRI. On a decibel axis the loss of echo intensity is linear in depth.

### The teardrop point spread function

If $I$ is the original image and the imaging system has convolution kernel $H$, the measured, digitized image is $J = I * H$. A swept scan line gives a **teardrop-shaped** $H$: the lecture intuition is that along each scan line the sampled points are equally spaced, but because the line is swept through an arc, neighboring lines are spread farther apart at greater distance from the probe, so a point farther out is blurred over more lateral space. In the notebook the kernel is built from an axial kernel (the ringing pulse) and a lateral kernel (the focused beam width) in the scanner's $(r,\theta)$ coordinates, and **scan conversion** to the Cartesian display rotates the teardrop with the scan angle so it points away from the apex. The kernel is nearly shift-invariant in $(r,\theta)$ but shift-variant in the displayed $(x,y)$ image.

### Acoustic impedance, attenuation, and image formation

Boundaries along a scan line return echoes because they present an **acoustic impedance** mismatch to the propagating pressure wave:

$$Z=\rho c=\sqrt{\rho K},\qquad R=\frac{Z_2-Z_1}{Z_2+Z_1},\qquad \text{reflected intensity}=R^2,\quad \text{transmitted}=1-R^2,$$

where $K$ is the bulk modulus (the coefficient relating volumetric stress to volumetric strain). Denser media have a higher speed of sound and a higher $Z$, so an abrupt change in $c$ at a boundary is also a change in impedance. Soft-tissue boundaries reflect little, whereas tissue–air and tissue–bone boundaries reflect strongly (the reflection matrix in the notebook reads like a correlation matrix, black meaning no reflection). The round-trip loss in dB is $2\alpha f z$ with $\alpha\approx0.5$ dB/cm/MHz in soft tissue, so signal falls off with depth, which is why ultrasound is used over a relatively small depth. The wavelength (about the axial resolution) shrinks as frequency rises, so a low-frequency beam penetrates deeper but resolves less. Modeling $Z(z)$ and $\alpha(z)$ lets us simulate **A-lines** (amplitude lines) and stack them into a **B-mode** image. The A-line, B-mode phantom, time-gain compensation, and frequency-comparison sections of `Ultrasound_Impedance_Attenuation.ipynb` will be covered next week with accompanying slides.

### Housekeeping

- The slide deck will be uploaded to the class Google Drive folder, including the MR contrast-agent slides (what is dark and bright in MR; how gadolinium contrast works) that were missing from earlier uploads.
- Update the specific-aims cell (H6) in the class Excel workbook if your aims have evolved.
- VS Code tip: if notebooks stop opening after an update, a full quit and restart (or asking Copilot to diagnose it) often fixes extension-host problems.

## Practical project workflow

1. Inspect the source volume and confirm its format and voxel spacing.
2. Visualize it in ITK-SNAP or ParaView, then create or load a segmentation.
3. Export masks and large derived volumes in a suitable format, but avoid committing bulky/generated data; use `.gitignore` and approved storage such as course or lab drives where appropriate.
4. Quantify volume and shape, or construct an M-mode representation for time-varying ultrasound, and validate the resulting measurements against the image.

## Environment

The notebooks use Python with **NumPy**, **SciPy**, **scikit-image**, **SimpleITK**, and **matplotlib**.
