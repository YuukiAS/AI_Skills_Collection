---
name: medical-imaging-classical-features
description: Use when enforcing reproducible preprocessing, registration baselines, radiomics protocols, or DICOM SEG/SR provenance in CardiacNexus.
status: active
provenance: unknown
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: project
license: Apache-2.0
metadata:
  skill-author: CardiacNexus maintainers
allowed-tools:
---
# Medical imaging classical features and engineered preprocessing

## Overview

This skill is **not** a “legacy methods collection.” It defines a **classical-and-engineered** pipeline:

- **Geometry-aware preprocessing** (orientation, affine, spacing, origin, interpolation discipline).  
- **Registration / normalization** with **selective** use of **ANTsPy** (high-quality paths only).  
- **Handcrafted radiomics** with **IBSI-aligned** definitions and **CLEAR-aligned** reporting when studies are published or reviewed.  
- **DICOM-semantic I/O** (SEG/SR) where **coded concepts, UIDs, frame of reference, and provenance** matter as much as pixels.

**ANTsPy** is **selective**: use for **demanding registration, template construction, or biologically constrained normalization**—not “default every task.”

Canonical anchors: [references/reference.md](references/reference.md).

## When to Use This Skill

Use when you:

- Build **preprocessing** that must match **deep learning** tensors 1:1 in physical space.  
- Extract **radiomics** for statistics or downstream Bayes—**protocol sensitivity** is part of the design.  
- Read/write **DICOM** with **audit-ready metadata** (multi-frame, orientation, FoR).  
- Compare **classical registration** baselines (**ANTs/SyN**, **elastix**) and **bias correction** (**N4ITK**).

## Core Tooling / Preferred Stack

| Tool | Responsibility |
|------|----------------|
| **SimpleITK** | Image I/O (often via file readers), **filtering**, **resampling**, **transforms**, and ITK-style **registration primitives**; enforce physical-space consistency. |
| **PyRadiomics** | **Handcrafted radiomic** feature extraction from aligned image + mask under a **frozen parameter file**. |
| **pydicom** | Low-level **DICOM parsing**, tag access, de-identification hooks, raw pixel pathways. |
| **highdicom** | Higher-level **DICOM objects** (e.g., SEG, SR patterns) with **semantic** coding support—use when outputs must be **standards-compliant**, not “just numpy masks.” |
| **ANTsPy** | Python binding to **ANTs**; **SyN**-class deformable registration, **template-building** workflows, paired with CLI/scripted ANTs tools when needed. |

### Classical algorithm / preprocessing anchors (not always installed libraries)

| Anchor | Role |
|--------|------|
| **elastix** | Widely used **intensity-based registration** toolbox—**second classical line** next to ANTs/SyN for fair comparisons. |
| **N4ITK** | **MRI bias-field correction** anchor—call via **SimpleITK** (`N4BiasFieldCorrectionImageFilter` pattern) in pipelines that need it. |
| **SyN / ANTs** | Diffeomorphic registration lineage—understand connection when using **ANTsPy** APIs. |

## Workflow / Decision Rules

### Geometry and interpolation

- **Never** silently change **origin / direction / spacing**; log them on every derived volume.  
- Choose **interpolation** explicitly: **linear** for resampled intensities in many radiomics settings; **nearest** for labels; document deviations.  
- **ROI / mask**: define **morphological handling** (re-segmentation after resampling, boundary voxels, hollow structures).

### Registration / normalization

- **Default mindset:** know **both** **ANTs/SyN (via ANTsPy)** and **elastix** as **classical** comparators—pick per modality/task with **documented rationale**.  
- **MRI bias:** if intensity non-uniformity is plausible, **plan for N4** (or justify omission per protocol).  
- **ANTsPy** for **high-stakes alignment** (template construction, longitudinal alignment) — **not** for every trivial rigid step unless justified.

### Radiomics (PyRadiomics + IBSI)

- **PyRadiomics ≠ automatic IBSI compliance.** Treat **IBSI** as the **standardization target**: resampling, interpolation, intensity discretization/binning, re-segmentation, ROI definition, aggregation, and harmonization.  
- **IBSI website / phantom benchmarks** ([https://theibsi.github.io/](https://theibsi.github.io/)) are **calibration resources**, not optional reading.  
- Studies without **IBSI/CLEAR context** carry **elevated reproducibility risk**—state limitations explicitly.

### DICOM semantics and provenance

- **Do not** only export mask pixels. For **SEG/SR**: maintain **coded concepts**, **UIDs**, **frame of reference**, **algorithm identification**, and **provenance** suitable for audit.  
- Validate **metadata completeness** before batch processing (missing orientation, inconsistent series descriptions, mixed FoR).

### Reporting / QC (CLEAR)

- For radiomics **study design, manuscripts, or internal QA**, apply **CLEAR** as a **default reporting checklist** (endorsed guideline—see references).

## Classical baselines and standardization (reproducibility anchors)

**Hard rules:**

1. **Registration:** besides **ANTsPy**, know **elastix** as a **classic alternative baseline** when comparing pipelines.  
2. **MRI preprocessing:** **N4ITK** is the default **bias correction anchor**—acknowledge when skipped.  
3. **Radiomics:** **IBSI-compliant** preprocessing/feature definition is a **priority**, not an appendix.  
4. **PyRadiomics parameters** must be **version-controlled**; document **resampling, interpolation, binning, re-segmentation, ROI rules, aggregation, harmonization**.  
5. **Outputs without IBSI/CLEAR discipline** → treat **reproducibility risk** as **high** by default.  
6. **Classical pipeline** = **geometry + preprocessing provenance + features + DICOM semantics**—not “run one extractor.”

## Common Pitfalls / Validation Notes

- **Domain shift** across scanners/protocols/reconstruction kernels without **harmonization** or **explicit limitation** in reporting.  
- **Radiomics** on **misregistered** masks or **inconsistent** intensity scales.  
- **Saving SEG** without **meaningful concept codes** and **FoR** linkage.  
- Using **ANTsPy everywhere** “because it’s strong”—**costly**, may be **unnecessary** for simple rigid steps.  
- Assuming **highdicom** removes the need for **domain expert review** of coded attributes.

## References

Canonical and anchor literature is maintained in [references/reference.md](references/reference.md).
