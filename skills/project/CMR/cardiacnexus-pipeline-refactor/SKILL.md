---
name: cardiacnexus-pipeline-refactor
description: Project-specific guidance for refactoring the CardiacNexus UKB CMR pipeline. Use when touching config.py, step1-4 orchestration, Slurm script generation, segmentation wrappers, feature extraction boundaries, packaging, or any MONAI-first migration of the core pipeline.
metadata:
  short-description: Refactor the core CardiacNexus pipeline
---

# CardiacNexus pipeline refactor

Use this skill for repository-specific refactors. This skill is narrower and more actionable than the generic imaging skills: it assumes the current CardiacNexus layout, legacy constraints, and the roadmap in `TODO.md`.

## Use this skill when

- Refactoring `config.py` or replacing hard-coded paths with layered configuration.
- Changing `step1_prepare_data_cmr.py`, `step2_segment.py`, `step3_extract_feature_separate.py`, or `step4_extract_feature_combined.py`.
- Unifying segmentation backends, Slurm generation, or modality dispatch.
- Moving logic out of scripts into reusable `src/` modules.
- Planning a MONAI-first migration while keeping current outputs compatible.

## Workflow

1. Read `TODO.md`, `config.py`, the relevant `step*.py` file, and any touched `utils/*` helper before proposing structure changes.
2. Classify the change:
   - configuration
   - orchestration
   - segmentation backend
   - feature extraction
   - registration / strain
   - docs / deployment side effects
3. Preserve the public contract first:
   - filenames
   - visit1 / visit2 conventions
   - output folder layout
   - Slurm entrypoint expectations
4. Prefer adapter layers over direct rewrites of legacy code.
5. Move toward:
   - environment variable or config-file based settings
   - packaged imports instead of `sys.path.append`
   - `subprocess.run(..., check=True)` instead of `os.system`
   - reusable services in `src/`
6. If the change touches phenotype outputs, also use the `cardiacnexus-feature-contracts` skill.
7. If the change touches strain or deformable registration, also use the `cardiacnexus-strain-registration` skill.

## Hard constraints

- Do not assume the old absolute paths in `config.py` are valid.
- Do not introduce more modality-specific copy-paste branches for `nnUNet` / `UMamba`.
- Do not spread TensorFlow 1 inference code into new business logic.
- Do not change output filenames casually.
- Do not refactor tagged MRI first unless the task explicitly requires it.

## Recommended order

1. `sa`
2. `la`
3. other segmentation wrappers
4. shared output / feature I/O
5. strain registration backends
6. tagged MRI

## References

- Architecture map: [references/architecture-map.md](references/architecture-map.md)
