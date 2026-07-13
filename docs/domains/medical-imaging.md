# medical-imaging

Active skills: 6

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain medical-imaging --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill domain/medical-imaging/cardiac-mri --skill domain/medical-imaging/medical-imaging-classical-features --skill domain/medical-imaging/medical-imaging-deep-learning --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `cardiac-mri` (`skills/domains/medical-imaging/cardiac-mri`): Use for cardiac MRI / CMR domain knowledge, cine SAX/LAX, ED/ES timing, LV/RV function, myocardial strain, tagged MRI, feature tracking, and cardiac phenotype validation independent of any single project.
- `medical-imaging-classical-features` (`skills/domains/medical-imaging/medical-imaging-classical-features`): Use when enforcing reproducible medical-imaging preprocessing, physical-space geometry, classical registration baselines, radiomics protocols, or DICOM SEG/SR provenance.
- `medical-imaging-deep-learning` (`skills/domains/medical-imaging/medical-imaging-deep-learning`): Use for medical-imaging deep learning tasks involving segmentation, MONAI/nnU-Net baselines, registration or warping, temporal/video imaging, missing-modality fusion, proposal/cascade/refinement models, external method adaptation, and validation evidence gates.
- `medical-imaging-terminology-measurement` (`skills/domains/medical-imaging/medical-imaging-terminology-measurement`): Use medical imaging terminology and measurement conventions with source checks, modality-specific caveats, structured reporting boundaries, and uncertainty language.
- `pathml` (`skills/domains/medical-imaging/pathml`): Full-featured computational pathology toolkit. Use for advanced WSI analysis including multiplexed immunofluorescence (CODEX, Vectra), nucleus segmentation, tissue graph construction, and ML model training on pathology data. Supports 160+ slide formats. For simple tile extraction from H&E slides, histolab may be simpler.
- `pydicom` (`skills/domains/medical-imaging/pydicom`): Python library for working with DICOM (Digital Imaging and Communications in Medicine) files. Applies to tasks involving medical image analysis, PACS systems, radiology workflows, and healthcare imaging applications.

## Main References

- `skills\domains\medical-imaging\cardiac-mri\references\source-notes.md`
- `skills\domains\medical-imaging\medical-imaging-classical-features\references\reference.md`
- `skills\domains\medical-imaging\medical-imaging-deep-learning\references\reference.md`
- `skills\domains\medical-imaging\medical-imaging-terminology-measurement\references\measurement-checklist.md`
- `skills\domains\medical-imaging\pathml\references\source-notes.md`
- `skills\domains\medical-imaging\pydicom\references\source-notes.md`
