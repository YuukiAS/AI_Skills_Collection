---
name: cardiacnexus-feature-contracts
description: Project-specific guidance for CardiacNexus phenotype outputs. Use when adding, renaming, validating, aggregating, or documenting CSV/NPZ/QC outputs, units, column schemas, cross-modality features, or downstream-facing phenotype contracts.
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: project
metadata:
  short-description: Maintain phenotype output contracts
---
# CardiacNexus feature contracts

Use this skill whenever a change can alter the shape, meaning, location, or naming of phenotype outputs.

## Use this skill when

- Editing `src/feature_extraction/**/*.py`
- Editing `scripts/aggregate_csv.py`
- Adding new phenotypes or derived combined features
- Changing units, column names, folder names, or QC outputs
- Reviewing whether a feature change needs documentation or regression tests

## Workflow

1. Identify the produced artifacts:
   - CSV files
   - aggregated CSV
   - `timeseries/*.npz`
   - `visualization/*`
   - `landmark/*`
   - feature-tracking intermediates
2. Write down the contract before changing code:
   - subject key
   - column names
   - units
   - missing-value behavior
   - required upstream files
3. Preserve or intentionally version the contract.
4. If aggregation is touched, validate:
   - missing columns
   - duplicate `eid`
   - dtype drift
   - empty files
   - incompatible partial outputs
5. If documentation exists for the phenotype, update it or at minimum note the doc debt explicitly.
6. Add at least a smoke or schema test for the changed output.

## Hard constraints

- Every tabular output must contain `eid`.
- Units must be visible either in column names or in tightly coupled metadata.
- Do not silently change column naming conventions.
- Do not silently drop rows or columns during aggregation.
- Do not let QC output paths drift unpredictably across refactors.

## Cross-links

- For core pipeline changes, also use `cardiacnexus-pipeline-refactor`.
- For docs updates in `docs/`, also use `cardiacnexus-docs-markdoc`.

## References

- Output and validation checklist: [references/output-contracts.md](references/output-contracts.md)
