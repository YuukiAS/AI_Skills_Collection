---
name: cardiac-mri
description: Use for cardiac MRI / CMR domain knowledge, cine SAX/LAX, ED/ES timing, LV/RV function, myocardial strain, tagged MRI, feature tracking, and cardiac phenotype validation independent of any single project.
status: active
provenance: user-authored
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-03
profile_tags:
  - medical-imaging
  - cmr
recommended_scope: project
---
# Cardiac MRI / CMR

## Trigger Boundary

Use this skill for cardiac MRI domain reasoning that should transfer across projects. This includes cine short-axis and long-axis imaging, ED/ES timing, LV/RV function, myocardial strain, tagged MRI, feature tracking, and cardiac phenotype validation.

Do not use this skill for CardiacNexus repo paths, UKB folder layout, local scripts, or docs routes; those belong in CardiacNexus project skills.

## Workflow inheritance

For complex tasks, first apply the global `codex-workflow-protocol` skill. This skill only adds domain-specific cardiac MRI knowledge, gates, and validation requirements. It must not weaken the global completion, escalation, or verification rules.

## Workflow

1. Identify the CMR acquisition and view: cine SAX/LAX, tagged MRI, phase contrast, mapping, or derived segmentation/feature tracking output.
2. State the cardiac structure and timing target: LV, RV, LA, RA, myocardium, ED, ES, peak systole, diastole, or frame-wise time series.
3. Preserve geometry and timing assumptions before comparing algorithms or phenotypes.
4. Validate phenotype meaning, not only image overlap or visual plausibility.

## Domain gates

- LV/RV function tasks should report ED/ES frame handling, volumes, EF/SV where applicable, and segmentation/contour consistency.
- Strain tasks should distinguish global and segmental longitudinal, circumferential, or radial strain and check timing landmarks.
- Cine or time-series tasks should verify temporal smoothness and frame-to-frame consistency, not only one reference frame.
- Tagged MRI and feature tracking tasks should validate tracking quality and downstream phenotype bias.
- Registration tasks that affect cardiac phenotypes should consider warped segmentation/contour consistency, Jacobian/folding for deformable methods, and downstream strain or volume bias.
- Dice or a single overlay is insufficient for deformation-sensitive cardiac phenotype acceptance.

## Cross-links

- Use `medical-imaging-deep-learning` for MONAI, nnU-Net, VoxelMorph, and learning-based registration or segmentation evidence.
- Use `medical-imaging-classical-features` for physical-space geometry, ANTs/SyN, elastix, SimpleITK, radiomics, and DICOM provenance.
- Use project-specific CMR skills only for repo-local paths, scripts, output contracts, and validation commands.
- Read `references/source-notes.md` before making clinical, publication, or current-standard claims.
