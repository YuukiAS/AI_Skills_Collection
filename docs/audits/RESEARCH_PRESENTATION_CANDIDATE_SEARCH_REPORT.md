# Research Presentation Candidate Search Report

Reviewed Handoff task: `020_research_presentation_reference_calibrated_candidate_search`

## Summary

020 adds an internal reference-calibrated candidate-search layer. For the same scientific content, it produces three compositionally distinct 16:9 preview candidates and records how each candidate transfers geometry from inspected composition exemplars.

This task does not choose a winning candidate, call Terra, lock a deck-wide design system, create final PPTX/Beamer slides, run a real holdout benchmark, or declare `ONE_SHOT_QUALITY_PASS`.

## Added Artifacts

- `skills/tools/documents-media/presentations/shared/references/research_slide_candidate_request.schema.json`
- `skills/tools/documents-media/presentations/shared/references/research_slide_candidate_manifest.schema.json`
- `skills/tools/documents-media/presentations/shared/scripts/generate_reference_calibrated_candidates.py`
- `skills/tools/documents-media/presentations/shared/scripts/validate_reference_candidate_manifests.py`
- `docs/audits/research_presentation_candidate_search/requests/statistical_estimator_request.json`
- `docs/audits/research_presentation_candidate_search/requests/medical_image_comparison_request.json`
- `docs/audits/research_presentation_candidate_search/generated/...`

The generated artifacts include six PNG candidate previews, two candidate manifests, and two internal comparison sheets.

## How Candidate Search Consumes 019 Records

The generator imports the 019 selector and reads `research_slide_composition_index.json`. It queries by:

- `page_function`;
- optional `evidence_type`;
- `scientific_object` keywords;
- content-mode compatibility such as equation or medical image.

The shared search logic does not hard-code fixed RRL IDs or fixed fixture-to-family mappings. Tests verify that the production candidate generator does not contain literal `RRL-xxx` selections.

The `REVIEW_1` repair adds a compatibility gate before composition-distance ranking. Medical-image requests only use inspected medical-image comparison compositions, and estimator requests only use inspected equation/estimator-compatible compositions. Generic terms such as `and` or `with` cannot make an unrelated source eligible for wildcard selection.

## Candidate Strategies

Each request produces exactly three candidates:

- `reference_faithful`: uses the highest-ranked compatible composition exemplar as the primary geometry prior.
- `alternative_composition`: selects a different composition family when available, or a different topology when a second family is not directly available.
- `controlled_wildcard`: selects the feasible composition direction with the largest simple composition distance from the first two candidates.

Strategy names are internal manifest metadata only. They are not drawn into individual preview pixels.

When fewer than three strongly compatible source records exist, the wildcard remains inside the compatible source set and uses a source-derived alternate topology, rather than falling back to an unrelated page function.

## Geometry Transfer

Each candidate manifest records:

- source `reference_id`;
- source region and role;
- source normalized bbox;
- candidate region and content slot;
- candidate normalized bbox;
- adaptation type;
- concise adaptation reason.

This makes the reference-to-candidate link auditable: Reviewer can see whether a candidate preserved, scaled, translated, or otherwise adapted the real exemplar composition.

Candidate bboxes are derived from the selected source record's title, primary scientific object, equation, secondary object, and legend bboxes. The generator performs small renderer-neutral operations such as split, scale, translate, and reorder while recording the actual operation in `geometry_transfer`; it does not choose a family name and then apply a fixed family coordinate template.

## Regression Requests

### Statistical Estimator

Request: `statistical_estimator_cluster_robust_variance`.

Content uses existing deterministic statistical fixture assets, including the rendered cluster-robust sandwich covariance equation. The three generated families are:

- `equation-dominant`;
- `split-visual-explanation`;
- `split-visual-explanation-reordered-callout`.

The preview contains a real rendered equation asset and concise interpretation/caption text. It is not ASCII math and not a wireframe.

### Medical Image Comparison

Request: `medical_image_lesion_overlay_comparison`.

Content uses existing deterministic medical-imaging fixture assets: synthetic input, overlay, prediction, and error images. The three generated families are:

- `aligned-multi-panel`;
- `aligned-multi-panel`;
- `aligned-multi-panel-focus-callout`.

The preview contains real image/overlay evidence from local synthetic fixtures. It does not use source reference screenshots or clinical source pixels.

## Preview Rendering

Previews are deterministic PNGs rendered with Pillow at 1600 x 900. They use one restrained neutral regression skin so differences come from composition and scientific hierarchy, not color swaps.

The internal comparison sheets are for Reviewer inspection of candidate distinctness. They are not full-deck contact sheets and do not implement comparative Terra adjudication.

## Distinctness Check

The validator checks:

- exactly three candidates per request;
- same content payload SHA across candidates;
- distinct preview SHA values;
- at least two composition families;
- non-identical geometry signatures;
- complete source-to-candidate transfer traces;
- primary scientific object presence and area;
- estimator preview contains equation content;
- medical preview contains image content;
- candidate sources pass the page-function/content-mode compatibility gate;
- audience-facing preview text has no candidate strategy, RRL, QA, provenance, repo path, or implementation metadata;
- preview/comparison artifacts are PNGs with matching SHA values.

The distance is a simple renderer-neutral signature over layout family, primary bbox center/area, region topology, and reading flow. It is a distinctness guard, not a visual quality score.

Regression tests also call the generator directly with two same-family medical-image records and assert that their different source bboxes produce different candidate geometry. This proves source normalized geometry enters candidate layout calculation.

## Current Limits

020 proves that the system can create multiple reference-calibrated candidates from the same content. It still cannot decide which candidate is better.

The next task should implement comparative reference-calibrated visual review: the reviewer must compare candidate previews against matched exemplar compositions and decide which direction, if any, is mature enough to drive a final deck layout. It should not blindly promote candidate A, B, or C as final output.

## Scope Boundary

020 did not expand the reference corpus, modify 019 records, change active Presentation skill routing, change Terra or Bridge Kit, implement winner selection, add a user style picker, lock a deck design system, start a holdout benchmark, or touch PPTX/Beamer renderers.
