# Week 13 — Ultrasound Image Formation, Doppler & Midterm Project Presentations

**Lecture 1 (Nov 17)** settled the end-of-semester schedule and final-project deliverables, then continued **ultrasound image formation**: what a pressure wave is (longitudinal vs transverse), how a piezoelectric transducer generates it, beam formation as interference of spherical wavelets, 3-D ultrasound, **Doppler** velocimetry, speckle and speckle tracking, and a walkthrough of the A-line / B-mode simulation notebook. The class ended with a short project stand-up. **Lecture 2 (Nov 19)** was the four teams' **midterm project presentations**, followed by a tour of the new Week 13 notebooks on beamforming, Doppler, and speckle filtering/tracking.

## Contents

| File | Description |
|------|-------------|
| [Ultrasound_Impedance_Attenuation.ipynb](Ultrasound_Impedance_Attenuation.ipynb) | Acoustic impedance $Z=\rho c$ and the reflection coefficient at boundaries; Beer–Lambert attenuation and the resolution/penetration trade-off; build an A-line and a B-mode image of a phantom (cyst, stone), with time-gain compensation, shadowing, posterior enhancement, and a frequency comparison. Introduced in Week 12 and reviewed this week. |
| [Ultrasound_Beamforming_Aperture.ipynb](Ultrasound_Beamforming_Aperture.ipynb) | The transmit beam as the **Fourier transform of the aperture** (width vs beam width, apodization vs side lobes, grating lobes), **delay laws** for plane, steered, focused, and diverging waves with simulated pressure fields, focal width $\approx1.2\lambda F/D$, and a 2-D aperture showing coarse elevation (slice-thickness) resolution. |
| [Ultrasound_Doppler.ipynb](Ultrasound_Doppler.ipynb) | Doppler shift $f_d=2f_0v\cos\theta/c$ and angle errors; pulsed-wave slow-time sampling, Nyquist velocity and **aliasing** (sweep and spectrogram); a **color Doppler** map of an arch vessel with a jet (red/blue coding, zero band at $90^\circ$, aliasing mosaic); **CW vs PW** spectra. |
| [Ultrasound_Speckle_Tracking.ipynb](Ultrasound_Speckle_Tracking.ipynb) | **Speckle** as Rayleigh statistics (SNR $\approx1.91$), a simulated B-mode phantom, **median vs Gaussian filtering** (CNR vs resolution), **compounding** ($\sqrt N$ gain), and **speckle tracking** by normalized cross-correlation block matching to recover displacement and strain. |

Related: [Week12/Ultrasound_PSF_Convolution.ipynb](../Week12/Ultrasound_PSF_Convolution.ipynb) (the teardrop point spread function of a swept scan line) and [Week12/Ultrasound_MMode.ipynb](../Week12/Ultrasound_MMode.ipynb).

## Lecture 1 notes (Nov 17)

### Schedule and final-project logistics

- **Midterm presentations: this Thursday (Nov 19).** Two to four slides at most: the problem you set out to solve, the hypothesis and aims, and how far along you are on each aim with illustrations. Show statistics if you have them; otherwise show the methods completed so far.
- **No class Thanksgiving week.** The remaining classes are **Dec 1, Dec 3, Dec 8, and Dec 10**.
- Per the academic calendar, the last day of undergraduate classes is **Dec 4**, reading day is **Dec 5**, and final exams begin **Dec 7**; the term officially ends Dec 12 (the deadline for entering grades).
- **Final project presentations: Thursday Dec 3**, all four teams the same day, about **15–20 minutes per team** including questions, showing slides plus the poster or report and a demo if you have one.
- **Final submission: Dec 10**, but aim for **Sunday Dec 6** (before exams) so there is time to grade and return corrections. Material submitted before the presentation can be updated through Dec 10. This extension also covers the outstanding assignments (Assignment 3 part 2 has no hard due date but is due by then).
- **Deliverables:** a **poster** or an **IEEE/ASME-style paper** (poster-or-report is the option for graduate students; Xinyue may do a poster if it helps a conference submission), the **final slide deck**, **datasets in Google Drive**, and **code in GitHub**. GitHub was previously optional; it is now expected and still carries **20 bonus points**.

### GitHub for your project

- Notebooks render directly in a GitHub repository. Notebooks developed in Google Colab are fine: Copilot can add an **Open in Colab** link to each one.
- A **public repository** is evidence of your skill set; **pin** the repositories you want visitors to see first on your profile. Repositories can be public or private.
- A visual result can be hosted as a **GitHub Pages** app (`<handle>.github.io/<repository>`). As an example, the instructor showed an **intravascular ultrasound (IVUS)** to coronary angiogram co-registration tool: the IVUS probe is threaded through the vessel, and its position is mapped onto the vessel trajectory from fluoroscopy so a blockage seen in the ultrasound can be located on the angiogram and a stent deployment planned.
- You can point Copilot at the course repository and ask for an equivalent project page; it is a prompting exercise, not a manual one.

### Waves and the transducer

- A wave is a **compression or rarefaction** that propagates through a medium, passing momentum between neighboring particles. The particles themselves do not travel with the wave; like a buoy bobbing as an ocean wave passes, they oscillate about a fixed position.
- In a **transverse** wave the particle displacement is perpendicular to the direction of propagation (light and surface water waves). In a **longitudinal** wave the displacement is parallel to the propagation direction. **Sound, including medical ultrasound, is a longitudinal pressure wave.**
- A **piezoelectric** crystal flexes when a voltage is applied, producing a pressure wave, and produces a voltage when it is flexed by a returning echo, so the same element both **actuates and senses**. The effect was discovered in the 1880s. A probe contains many elements in an array, so it converts electrical signals to mechanical energy and back.
- The transducer has three coordinates: **axial** (range or depth), **lateral** (in the image plane), and **elevation** (slice thickness, out of plane).
- The transducer can transmit a **pulse** or a **continuous wave**; the two modes suit different measurements (the ultrasound analogue of choosing an MRI pulse sequence).
- Pressure in 3-D obeys the scalar **wave equation**, $\nabla^2 p = \frac{1}{c^2}\,\partial^2 p/\partial t^2$, a partial differential equation in $(x,y,z,t)$. (It was referred to as a Poisson-type equation in class; strictly it is the wave equation, whose time-independent form is the Helmholtz equation.)

### Echo physics recap

The speed of sound differs between media, so there is an **acoustic impedance** mismatch at a boundary: some energy is reflected, some transmitted, and some absorbed. The larger the impedance difference, the stronger the reflection. The return time is proportional to twice the distance to the reflector, and amplitude falls off according to Beer–Lambert with a round trip of $2d$. Scatterers in the field of view act as small pressure sources that send a wave back to the transducer. Attenuation per unit depth and per MHz is larger in denser tissue (bone more than soft tissue).

Spatial detail depends on the **beam width and focus**, the **pulse duration and bandwidth**, and the **slice thickness**.

### Beam formation and Fourier theory

- Many **spherical wavelets** from closely spaced elements interfere to form an approximately **planar wavefront**, which is the ideal beam for imaging.
- For a flat rectangular array of equal elements, the transmitted beam is not an ideal plane wave: it is planar near the middle and less so farther away. The beam pattern is the **Fourier transform of the aperture** (the shape of the element grid), so Fourier theory governs beam formation.
- Delaying the pulses across the elements lets the array form a **plane**, **diverging**, or **converging (focused)** wave. The slide on the teardrop point spread function and its Fourier-space counterpart (the transfer function) ties back to the Week 12 PSF notebook.
- **3-D ultrasound** sweeps a plane rather than a line, either angularly or in another pattern. It is used for heart valves (for example tricuspid/aortic valve imaging), fetal, and uterine imaging, giving high-resolution views of a small field of view.

### Doppler imaging

- Beyond **B-mode** (brightness) and **M-mode** (depth over time), **color and power Doppler** overlay a functional map of flow on a structural image. The probe can only tell whether something is moving **toward** or **away from** it. The Doppler shift is
  $$f_d = \frac{2 f_0\, v \cos\theta}{c},$$
  where $\theta$ is the angle between the beam and the flow, so flow perpendicular to the beam ($\theta\approx90^\circ$) produces no signal. Doppler therefore needs the beam at an acute angle to the flow.
- By convention red marks flow toward the probe and blue away. A mosaic of colors indicates a **jet** (very high velocity). Example: a transesophageal echo showed a jet across the septum between the ventricles in a pediatric patient with a ventricular septal defect.
- **Aliasing** occurs when the velocity is too high for the Doppler shift to be measured unambiguously; the colors wrap around. A pulsed-wave trace at the mitral valve showed jets that exceed the measurable range, typical of a valve that does not fully close and may warrant repair or replacement.
- **Pulsed-wave Doppler** measures velocity at a **specific depth** (for example across a septal defect or a valve plane). **Continuous-wave Doppler** measures all velocities along the beam but with **no depth information**. M-mode is often shown alongside Doppler to relate wall displacement to velocity.

### Speckle, tracking, and tagging

- Reflectors in the field of view are also called **speckle**; speckle helps form the image, but it appears as noise afterward. A **median filter** (a simple statistical filter over a sliding window, effective on salt-and-pepper noise) is a common post-processing step to smooth speckle and improve SNR; see [Ultrasound_Speckle_Tracking.ipynb](Ultrasound_Speckle_Tracking.ipynb).
- **Speckle tracking** follows the speckle pattern between frames to estimate **2-D strain**, tissue biomechanics, and flow in the heart and vessels. The instructor described a 3-D example: tracking the surface of the left atrial appendage across cardiac phases, with point-to-point surface correspondences (each point matched to the nearest triangle on the next phase's surface) to make heat maps of regional contractile function.
- **MRI tagging** is the analogue: in a short-axis black-blood T1-weighted spin-echo cine, a grid of dark tag lines is written into the tissue and fades over the cardiac cycle, showing twisting (torsion) of the heart. Each frame is gated across many heartbeats (for example about 50 cycles). Torsion, strain, and hoop stress estimated from the tags are relevant to conditions such as hypertrophic cardiomyopathy. The instructor wrote a plugin for tagging visualization. In ultrasound, a "tagged" PSF with multiple point-spread regions supports the same kind of strain and torsion estimate, though less obviously than in MRI.

### Where ultrasound stands

Ultrasound is **inexpensive and radiation-free**, with fairly low resolution, limited depth of penetration, and a small field of view. It is very useful for preoperative and intraoperative guidance, structural heart disease (valves), and fetal imaging.

### Notebook walkthrough: A-lines to B-mode

[Ultrasound_Impedance_Attenuation.ipynb](Ultrasound_Impedance_Attenuation.ipynb) simulates the whole image-formation chain:

1. build a pulse and an **acoustic impedance map** along depth;
2. compute round-trip attenuation and the energy lost at each boundary;
3. form the simulated **RF echo signal** (not intuitive to read compared with an idealized spherical-wave picture), then envelope-detect, log-compress, and apply **time-gain compensation**;
4. repeat for many scan lines to make a **B-mode image** of a phantom, with and without time-gain compensation;
5. compare 2.5, 5, and 10 MHz: **2.5 MHz** reaches about 24 cm in liver but has coarse lateral detail; **5 and 10 MHz** show the cyst boundary more clearly and with less speckle but lose depth to attenuation. Higher frequency buys resolution at the cost of penetration.

The beam-formation, Doppler, and speckle material above is simulated in the three new notebooks listed in the Contents table. The course returns to image-processing topics after ultrasound.

## Lecture 2 notes (Nov 19)

### Midterm project presentations

All four teams presented their progress and Kanban boards; the full record, with feedback, is in [Project/README.md](../Project/README.md) ("Sixth discussion"). In brief:

- **Retinal vasculature:** VesselFM (a 3-D vessel segmentation foundation model) reaches about 95% overlap with a manual label; skeletonization and MATLAB analysis follow.
- **Echocardiography:** a MedSAM foundation model fine-tuned on the provided masks now gives usable left-ventricle masks, stacked over time and visualized in ParaView.
- **Alzheimer's:** switched from hippocampus to **ventricles** (volume within 6% of the voxel count on a practice run) and reduced the cohort to 16 or 32 subjects.
- **fMRI connectivity (developmental prosopagnosia):** eight ROIs defined; connectivity extraction under way, with the 14 DP and 22 control participants preprocessed.

**Final presentation expectations (Dec 3):** same format as today, with more on the imaging modality (at least one slide on the physics of image formation, what it is used for, and the pulse sequence if MRI), practical methods with an illustration or demo, the data collected, findings with a visualization of the statistics, a conclusion, and your Git repository and artifacts (including a draft report or poster if not finished). All artifacts are due **Dec 10** and whatever is in the repository then is what is assessed. There is **no Assignment 5** (Canvas lists one, but it will not be given).

### Notebook walkthrough

The week's slides were turned into notebooks, so we do not need to become ultrasound experts; the aim is to see how an ultrasound image is simulated, how its beam is formed, and how its noise can be improved.

**[Ultrasound_Beamforming_Aperture.ipynb](Ultrasound_Beamforming_Aperture.ipynb)**

- **Near field vs far field:** in the near field spherical wavelets from the elements interact strongly. In the far field the wavefront becomes planar (or converging, for a focused beam). The far field is where the useful beam is, and its shape is the **Fourier transform of the aperture** for a uniform grid of elements.
- Parameters: $c$ in soft tissue, a 3 MHz centre frequency, then the wavelength.
- **More elements, sharper beam; fewer elements, wider central lobe.** Summing spherical waves explicitly matches the FFT of the aperture exactly, which validates the statement.
- **Aperture weights (apodization)** suppress side lobes. Steering and grating lobes were not covered in class.
- **Delay laws** produce plane, steered-plane, focused, and diverging beams, drawn as images in a field of view by the continuous-wave field function.
- A 2-D aperture gives both lateral and elevation resolution (section 6).

**[Ultrasound_Doppler.ipynb](Ultrasound_Doppler.ipynb)**

- The **frequency shift is proportional to the velocity component along the beam**. With no component along the beam there is no signal, so the beam needs an acute angle to the flow; the Doppler shift falls toward zero as the angle approaches $90^\circ$ and the velocity error grows with it. Using Doppler therefore needs some knowledge of the flow direction.
- Nyquist sampling and aliasing (sections 2–3) were not covered in class.
- The **color Doppler** simulation of a curved vessel with a jet is the one worth trying: change parameters and see how the flow image changes.
- **Pulsed-wave** Doppler gives the velocities at one chosen depth (for example the valve plane); **continuous-wave** gives all velocities along the beam with **no range resolution**, so the depth of each velocity must be inferred.

**[Ultrasound_Speckle_Tracking.ipynb](Ultrasound_Speckle_Tracking.ipynb)**

- Scatterers (speckles) in the field of view create the returning wavelets that form the signal; the notebook simulates a B-mode image with speckle.
- **Median filtering** (non-linear, statistical) vs **Gaussian filtering** (convolution with a low-pass kernel): the raw image has a contrast-to-noise ratio of **4.11**; the median filter raises it by removing outlier intensities (salt-and-pepper-like speckle) within a sliding window, with a partial blurring effect but better edge preservation. A Gaussian filter also improves SNR but removes detail. **Edge-preserving smoothing** is a whole field, and the median filter is one of many non-linear filters used for it.
- **Averaging $N$ images** of a static object improves SNR by about $\sqrt N$ when the noise is well behaved; relevant to ultrasound of static objects and to low-count nuclear imaging.
- **Speckle tracking** estimates a displacement map from the motion of speckle, a route to strain and deformation. The lecturer described his own first attempt as not working; the version in this notebook was checked numerically (strain recovered to within 0.0002 of the true value) and now overlays the true and estimated arrows so agreement can be seen.
- The impedance/attenuation notebook and the Beer–Lambert material were covered earlier.

### Next

- **No class Tue Nov 24 or Thu Nov 26** (Thanksgiving). Finish projects and assignments.
- **Tue Dec 1:** theory in image processing: **image registration** and 2-D image processing from the standpoint of **edge-preserving smoothing**, partly as slides, tying together the segmentation, registration, and filtering concepts from earlier weeks.
- **Thu Dec 3:** final project presentations.

## Environment

The notebooks use Python with **NumPy**, **SciPy**, **scikit-image** (block matching), and **matplotlib**.
