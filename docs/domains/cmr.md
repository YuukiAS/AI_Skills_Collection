# cmr

Active skills: 4

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain cmr --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill project/cmr/cardiacnexus-docs-markdoc --skill project/cmr/cardiacnexus-feature-contracts --skill project/cmr/cardiacnexus-pipeline-refactor --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `cardiacnexus-docs-markdoc` (`skills/projects/cmr/cardiacnexus-docs-markdoc`): Project-specific guidance for the CardiacNexus documentation site in docs/. Use when editing Markdoc pages, navigation, metadata, Next.js static export settings, phenotype documentation, or preparing the site for static publishing behind Cloudflared and cardiacnexus-ukb.org.
- `cardiacnexus-feature-contracts` (`skills/projects/cmr/cardiacnexus-feature-contracts`): Project-specific guidance for CardiacNexus phenotype outputs. Use when adding, renaming, validating, aggregating, or documenting CSV/NPZ/QC outputs, units, column schemas, cross-modality features, or downstream-facing phenotype contracts.
- `cardiacnexus-pipeline-refactor` (`skills/projects/cmr/cardiacnexus-pipeline-refactor`): Project-specific guidance for refactoring the CardiacNexus UKB CMR pipeline. Use when touching config.py, step1-4 orchestration, Slurm script generation, segmentation wrappers, feature extraction boundaries, packaging, or any MONAI-first migration of the core pipeline.
- `cardiacnexus-strain-registration` (`skills/projects/cmr/cardiacnexus-strain-registration`): Project-specific guidance for CardiacNexus strain and registration refactors. Use when editing eval_strain_lax.py, eval_strain_sax.py, cardiac_utils motion/contour code, MIRTK integrations, or when introducing ANTsPy or VoxelMorph backends for deformation-sensitive phenotype extraction.

## Main References

- `skills/projects/cmr/cardiacnexus-docs-markdoc/references/site-architecture.md`
- `skills/projects/cmr/cardiacnexus-feature-contracts/references/output-contracts.md`
- `skills/projects/cmr/cardiacnexus-pipeline-refactor/references/architecture-map.md`
- `skills/projects/cmr/cardiacnexus-strain-registration/references/benchmark-plan.md`
