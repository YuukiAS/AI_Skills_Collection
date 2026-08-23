# Research Presentation Composition Representation Report

Reviewed Handoff task: `019_research_presentation_exemplar_composition_representation`

## Summary

019 adds a small, renderer-neutral composition layer for inspected research-slide exemplars. It converts selected reference pages from prose-only lessons into structured records that a future generator can query before proposing a layout.

This task does not generate a deck, change active Presentation rules, modify Terra, run a holdout benchmark, or claim `ONE_SHOT_QUALITY_PASS`.

## Added Artifacts

- `skills/tools/documents-media/presentations/shared/references/research_slide_composition.schema.json`
- `skills/tools/documents-media/presentations/shared/references/RESEARCH_COMPOSITION_FAMILIES.md`
- `skills/tools/documents-media/presentations/shared/references/research_slide_composition_index.json`
- `skills/tools/documents-media/presentations/shared/scripts/validate_reference_compositions.py`
- `skills/tools/documents-media/presentations/shared/scripts/select_reference_compositions.py`
- `docs/audits/research_presentation_composition_debug_montage.svg`

## Seed Coverage

The initial composition index contains 13 records from 8 source IDs:

- `SRC-001`
- `SRC-005`
- `SRC-006`
- `SRC-013`
- `SRC-054`
- `SRC-055`
- `SRC-057`
- `SRC-058`

It covers these scientific page jobs and composition needs:

- estimator / equation explanation: `RRL-014`, `RRL-028`
- statistical model reveal: `RRL-034`
- quantitative result / interval figure: `RRL-023`, `RRL-030`, `RRL-039`
- method or experiment flow: `RRL-019`, `RRL-002`
- medical image / aligned-panel comparison: `RRL-022`, `RRL-013`
- negative result / model check: `RRL-025`, `RRL-041`
- open problem / next-step decision: `RRL-031`

The selected records include statistics, biostatistics, and medical-imaging reference pages. They are all drawn from existing `verification_status=inspected` rows in `research_slide_reference_index.csv`; no new source corpus entries were added.

## Inspection Method

Each record is based on a real rendered reference page. The relevant source PDFs were downloaded to the ignored local cache at `.cache/research-presentation-reference-library/sources/`, rendered with `pdftoppm` at 140 dpi, and inspected as page images during 019.

The committed records do not store those rendered images, source screenshots, public deck pixels, clinical images, or source visual identity. They store only:

- normalized page geometry (`x`, `y`, `w`, `h` in `[0, 1]`);
- semantic region roles;
- primary scientific object region and area ratio;
- alignment groups;
- visual hierarchy;
- abstract color-role summary;
- portable composition lessons;
- reuse boundary.

The records bind to the canonical `rendered_page_sha256` already present in `research_slide_reference_index.csv`. A few source pages rendered to a different PNG hash in the current environment than the historical index, so the seed set prioritizes pages whose current rendering and index identity were consistent enough for manual inspection while preserving the canonical index SHA in the committed representation.

## Measured Versus Abstract Fields

Measured or manually annotated from the rendered page:

- region bounding boxes;
- primary scientific object area ratio;
- visible region hierarchy;
- alignment relationships;
- reading-flow ordering.

Copied from the inspected RRL index:

- `reference_id`;
- `source_id`;
- `actual_page_number`;
- `page_function`;
- `scientific_object`;
- `evidence_type`;
- `rendered_page_sha256`.

Abstracted from inspection:

- `layout_family`;
- `color_role_summary`;
- `portable_composition_lessons`;
- `reuse_boundary`.

The abstractions intentionally avoid source-specific fonts, exact colors, institutional layouts, decorative assets, screenshots, or public figure pixels.

## What This Solves

The composition layer gives future Presentation tasks a concrete object for:

- selecting exemplars by scientific job and evidence type;
- carrying primary object area and placement into a candidate layout;
- distinguishing equation-dominant, result-dominant, aligned-panel, flow, model-check, and decision compositions;
- validating that reference lessons are not only prose footers or RRL IDs.

## Current Limits

019 is only the reference-to-composition layer. It cannot yet:

- generate candidate slides;
- choose among multiple candidate designs;
- compare a generated slide against reference exemplars;
- validate deck-level rhythm;
- improve PPTX or Beamer layout engines;
- prove one-shot quality on real holdout material.

Those steps require later frozen tasks. The new selector deliberately returns composition records and primary geometry only; it does not generate slide layouts or call Terra.

## Debug Montage

`docs/audits/research_presentation_composition_debug_montage.svg` provides an abstract QA view of the 13 records. It draws only normalized region boxes, role labels, primary-object outlines, layout family, and reading flow. It does not embed source images or binary assets.

## Validation Boundary

The deterministic validator checks schema shape, RRL linkage, inspected status, canonical rendered SHA, normalized bbox bounds, primary area consistency, family vocabulary, minimum coverage, selector inputs, and debug montage pixel-leak boundaries.

This is a mechanical guardrail. It does not replace later visual judgment about whether a generated deck looks mature.
