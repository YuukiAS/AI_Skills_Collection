---
name: cardiacnexus-strain-registration
description: Project-specific guidance for CardiacNexus strain and registration refactors. Use when editing eval_strain_lax.py, eval_strain_sax.py, cardiac_utils motion/contour code, MIRTK integrations, or when introducing ANTsPy or VoxelMorph backends for deformation-sensitive phenotype extraction.
metadata:
  short-description: Refactor strain and registration safely
---

# CardiacNexus strain and registration

This skill exists because strain and deformable registration are the highest-risk parts of the pipeline. A successful refactor here is not just a cleaner API; it must preserve phenotype validity.

## Use this skill when

- Editing `src/feature_extraction/Long_Axis_20208/eval_strain_lax.py`
- Editing `src/feature_extraction/Short_Axis_20209/eval_strain_sax.py`
- Editing MIRTK-dependent functions in `utils/cardiac_utils.py`
- Introducing ANTsPy, VoxelMorph, or another registration backend
- Designing regression tests for strain outputs

## Workflow

1. Read the current caller and backend together:
   - `eval_strain_lax.py` or `eval_strain_sax.py`
   - the relevant motion / contour functions in `utils/cardiac_utils.py`
   - the MIRTK config path from `config.py`
2. Separate concerns:
   - backend invocation
   - contour propagation / resampling
   - strain computation
   - smoothing / post-processing
   - plotting / QC
3. Introduce a backend interface before replacing implementation details.
4. Keep MIRTK as a fallback until benchmarks are stable.
5. Compare old and new backends on the same cases before changing defaults.

## Minimum benchmark set

- global strain
- segmental strain
- ED / ES timing derived from timeseries
- contour or warped-segmentation consistency
- deformation plausibility:
  - folding / Jacobian sanity for deformable methods
  - temporal smoothness

## Hard constraints

- Do not replace MIRTK with VoxelMorph or ANTsPy based on a single visual success case.
- Do not optimize for Dice alone when the downstream phenotype is strain.
- Do not entangle backend selection with plotting or CSV writing.
- Do not break current output filenames until validation is complete.

## Cross-links

- Use `medical-imaging-deep-learning` for MONAI / VoxelMorph positioning.
- Use `medical-imaging-classical-features` for ANTsPy / classical registration guidance.

## References

- Benchmark and backend notes: [references/benchmark-plan.md](references/benchmark-plan.md)
