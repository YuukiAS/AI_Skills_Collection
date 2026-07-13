---
name: medical-imaging-workflows
description: Medical imaging workflows for CMR, DICOM/NIfTI, classical features, deep learning, and pathology imaging.
status: active
provenance: generated
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/domains/medical-imaging/cardiac-mri
  - skills/domains/medical-imaging/pydicom
  - skills/domains/medical-imaging/medical-imaging-classical-features
  - skills/domains/medical-imaging/medical-imaging-deep-learning
  - skills/domains/medical-imaging/pathml
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
default_prompt:
---

# medical-imaging-workflows

## Trigger Boundary

Medical imaging workflows for CMR, DICOM/NIfTI, classical features, deep learning, and pathology imaging.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `cardiac-mri`: Use for cardiac MRI / CMR domain knowledge, cine SAX/LAX, ED/ES timing, LV/RV function, myocardial strain, tagged MRI, feature tracking, and cardiac phenotype validation independent of any single project. Reference: `_src/cmr/source.md`
- `pydicom`: Python library for working with DICOM (Digital Imaging and Communications in Medicine) files. Applies to tasks involving medical image analysis, PACS systems, radiology workflows, and healthcare imaging applications. Reference: `_src/dicom/source.md`
- `medical-imaging-classical-features`: Use when enforcing reproducible medical-imaging preprocessing, physical-space geometry, classical registration baselines, radiomics protocols, or DICOM SEG/SR provenance. Reference: `_src/classic/source.md`
- `medical-imaging-deep-learning`: Use for medical-imaging deep learning tasks involving segmentation, MONAI/nnU-Net baselines, registration or warping, temporal/video imaging, missing-modality fusion, proposal/cascade/refinement models, external method adaptation, and validation evidence gates. Reference: `_src/dl/source.md`
- `pathml`: Full-featured computational pathology toolkit. Use for advanced WSI analysis including multiplexed immunofluorescence (CODEX, Vectra), nucleus segmentation, tissue graph construction, and ML model training on pathology data. Supports 160+ slide formats. For simple tile extraction from H&E slides, histolab may be simpler. Reference: `_src/pathml/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
