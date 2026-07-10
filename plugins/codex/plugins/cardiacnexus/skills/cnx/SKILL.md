---
name: cardiacnexus-workflows
description: CardiacNexus feature contracts, pipeline refactors, strain registration, and documentation workflows.
status: active
provenance: generated
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/projects/cmr/cardiacnexus-feature-contracts
  - skills/projects/cmr/cardiacnexus-pipeline-refactor
  - skills/projects/cmr/cardiacnexus-strain-registration
  - skills/projects/cmr/cardiacnexus-docs-markdoc
---

# cardiacnexus-workflows

## Trigger Boundary

CardiacNexus feature contracts, pipeline refactors, strain registration, and documentation workflows.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `cardiacnexus-feature-contracts`: Project-specific guidance for CardiacNexus phenotype outputs. Use when adding, renaming, validating, aggregating, or documenting CSV/NPZ/QC outputs, units, column schemas, cross-modality features, or downstream-facing phenotype contracts. Reference: `_src/contracts/source.md`
- `cardiacnexus-pipeline-refactor`: Project-specific guidance for refactoring the CardiacNexus UKB CMR pipeline. Use when touching config.py, step1-4 orchestration, Slurm script generation, segmentation wrappers, feature extraction boundaries, packaging, or any MONAI-first migration of the core pipeline. Reference: `_src/pipeline/source.md`
- `cardiacnexus-strain-registration`: Project-specific guidance for CardiacNexus strain and registration refactors. Use when editing eval_strain_lax.py, eval_strain_sax.py, cardiac_utils motion/contour code, MIRTK integrations, or when introducing ANTsPy or VoxelMorph backends for deformation-sensitive phenotype extraction. Reference: `_src/strain/source.md`
- `cardiacnexus-docs-markdoc`: Project-specific guidance for the CardiacNexus documentation site in docs/. Use when editing Markdoc pages, navigation, metadata, Next.js static export settings, phenotype documentation, or preparing the site for static publishing behind Cloudflared and cardiacnexus-ukb.org. Reference: `_src/docs/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
