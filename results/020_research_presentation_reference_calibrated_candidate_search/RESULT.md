---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 020_research_presentation_reference_calibrated_candidate_search
implementation_commit: e37d7bd228853f5c385f81e9915baeebf8f91dc1
---

# 020 Research Presentation Reference-Calibrated Candidate Search - Executor Result

## Implementation commit

Current implementation commit: `e37d7bd228853f5c385f81e9915baeebf8f91dc1`.

Control-plane compatibility repair before implementation: `98bf15c` appended schema-required report sections to the 019 final report without changing 019 semantics or the 020 plan.

## Implemented

Added an internal reference-calibrated candidate-search layer:

- `skills/tools/documents-media/presentations/shared/references/research_slide_candidate_request.schema.json`
- `skills/tools/documents-media/presentations/shared/references/research_slide_candidate_manifest.schema.json`
- `skills/tools/documents-media/presentations/shared/scripts/generate_reference_calibrated_candidates.py`
- `skills/tools/documents-media/presentations/shared/scripts/validate_reference_candidate_manifests.py`
- `docs/audits/research_presentation_candidate_search/requests/statistical_estimator_request.json`
- `docs/audits/research_presentation_candidate_search/requests/medical_image_comparison_request.json`
- `docs/audits/research_presentation_candidate_search/generated/...`
- `docs/audits/RESEARCH_PRESENTATION_CANDIDATE_SEARCH_REPORT.md`

For each request, the generator produces exactly three 16:9 PNG preview candidates:

- `reference_faithful`
- `alternative_composition`
- `controlled_wildcard`

The generator imports and calls the 019 composition selector, reads `research_slide_composition_index.json`, and selects compatible records dynamically from request page function, evidence type, scientific object terms, content modes, layout family, and composition distance. The shared generator does not hard-code fixed `RRL-xxx` lists or fixed fixture-to-family mappings.

## Regression requests

The statistical estimator request uses existing deterministic statistical fixture content, including a rendered cluster-robust sandwich covariance equation asset. It generated the `equation-dominant`, `split-visual-explanation`, and `result-with-callout` candidate families.

The medical image comparison request uses existing deterministic medical-imaging fixture assets, including synthetic input, overlay, prediction, and error images. It generated the `aligned-multi-panel`, `horizontal-process-flow`, and `split-visual-explanation` candidate families.

The previews contain real scientific content rather than wireframes. Audience-facing preview text does not contain candidate strategies, `RRL-` IDs, reference retrieval text, provenance IDs, repo paths, QA labels, or implementation metadata.

## Geometry transfer and distinctness

Each candidate manifest records:

- candidate strategy and layout family;
- selected source reference IDs and source composition families;
- normalized candidate regions;
- primary scientific object area;
- reading flow;
- content bindings;
- source region to candidate region transfer trace;
- adaptation type and reason;
- renderer-neutral distinctness signature;
- preview artifact path and SHA.

The deterministic validator checks exact three-candidate output, matching content payload, distinct preview SHA values, at least two families, non-identical signatures, complete transfer traces, primary-object presence and area, equation/image page semantics, clean audience text, and absence of source reference pixels.

## Plugin mirror

The generated/plugin mirror under `plugins/codex/plugins/presentations/shared/` was synchronized for the new schemas and scripts.

## Visual inspection

I inspected both internal comparison sheets:

- statistical estimator: equation-dominant, split visual explanation, and result-with-callout previews are compositionally distinct and use the same rendered equation content.
- medical image comparison: aligned multi-panel, horizontal process flow, and split visual explanation previews are compositionally distinct and use the same local synthetic image evidence.

The comparison sheets are internal audit artifacts, not full-deck contact sheets and not comparative Terra evidence.

## Deliberately unchanged

- No changes to active `research-presentations/SKILL.md`.
- No changes to Terra, Bridge Kit, reference corpus records, PPTX renderer, or Beamer renderer.
- No Source Scout, corpus expansion, comparative Terra review, winner selection, deck design-system lock, full-deck rhythm gate, holdout benchmark, or `ONE_SHOT_QUALITY_PASS` claim was made.
- Existing statistical and medical fixtures were used only as deterministic regression content.

## Verification

- `python skills/tools/documents-media/presentations/shared/scripts/validate_reference_candidate_manifests.py docs/audits/research_presentation_candidate_search/generated/statistical_estimator_cluster_robust_variance/candidate_manifest.json docs/audits/research_presentation_candidate_search/generated/medical_image_lesion_overlay_comparison/candidate_manifest.json` - PASS, 2 manifests
- `python -m unittest tests.test_presentations` - PASS, 19 tests
- `python -m unittest discover -s tests` - PASS, 115 tests
- `python scripts/skills.py validate` - PASS
- `python scripts/build_codex_marketplace.py --validate --check --path-report` - PASS
- `PYTHONPATH=/home/yuukias/GPT_Codex_AI_Bridge_Kit python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection` - PASS
- `git diff --check` - PASS

## Deviations / blockers

None for the frozen 020 plan.

## CI handoff

`ci_required=true`; `CURRENT.ci_status` remains `PENDING`.

This handoff moves 020 to `WAITING_FOR_CI`. Planner review remains independent; this RESULT does not declare the long-term Presentation quality goal complete.
