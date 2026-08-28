---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 035_research_presentation_generic_model_support_recovery
executor: Codex
implementation_commit: 5501edce262254547bbcefbe04a0827172a73861
status: WAITING_FOR_CI
ci_status: PENDING
---

# 035 Research Presentation Generic Model Support Recovery - Result

## Implemented

- Generalized `STATISTICAL_MODEL` equation support emission so audience-facing support blocks are built only from current spec fields.
- Replaced the unconditional clustered-calibration support copy with neutral labels: `Model components` consumes `scientific_objects`, and `Interpretation` consumes `key_message`.
- Removed the default audience-facing `Calibration link`, fixed ICC/center-variation caption, and `Source-grounded terms` fallback from the shared renderer and the presentations plugin mirror.
- Added an unrelated synthetic Cox-model regression that exercises the same shared model path and proves Cox terms appear without ICC / center variation / interval comparison leakage.
- Regenerated the current Stage 4 engineering bundle for this task and wrote fresh task-local visual-review inputs.

Generated task-local artifacts:

```text
results/035_research_presentation_generic_model_support_recovery/generated/
results/035_research_presentation_generic_model_support_recovery/visual_review/visual_inputs.json
```

## Local Verification

Passed locally:

```text
python tests/test_presentations.py -k test_statistical_model_support_copy_is_source_driven_for_unrelated_model -k test_research_presentation_one_call_production_entry
python tests/test_presentations.py
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python scripts/icon_audit.py --scope marketplace --check
python -m unittest discover -s tests
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
python scripts/skills.py doctor
python scripts/build_codex_marketplace.py --write --validate --check --path-report
git diff --check
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle skills/tools/documents-media/presentations/shared/fixtures/stage4_engineering_research_bundle/bundle.json --out-dir results/035_research_presentation_generic_model_support_recovery/generated --task-key 035_research_presentation_generic_model_support_recovery --implementation-commit 5501edce262254547bbcefbe04a0827172a73861 --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/035_research_presentation_generic_model_support_recovery/generated --task-key 035_research_presentation_generic_model_support_recovery
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/035_research_presentation_generic_model_support_recovery/generated --task-key 035_research_presentation_generic_model_support_recovery --allow-missing-render
pdfinfo results/035_research_presentation_generic_model_support_recovery/generated/cuhk_production_build/main.pdf
ai-bridge visual-review preflight --target /home/yuukias/AI_Skills_Collection
```

Observed local results:

```text
targeted unittest: 2 tests passed
presentation unittest: 32 tests passed
full unittest: 141 tests passed
skills validate: validated 149 active skills, 18 profiles, templates, and trigger eval scaffolds
marketplace validate/check/path-report: plugins=10 active_skills=25 over_budget=0
icon audit: passed
Reviewed Handoff validation passed
production generation: MECHANICAL_PASS, render_status=ok
strict rendered validator: passed
allow-missing-render validator: passed
pdfinfo: Pages=7
visual-review preflight: enabled, 035 listed
```

Local rendered visual inspection:

```text
slide_2_statistical_model: formula remains primary; annotation plus Model components / Interpretation blocks are readable and non-overlapping.
slide_3_real_data_application through slide_6_next_experiment: existing storyline rhythm remains intact.
slide_7_medical_image_comparison: same-case ROI zoom and TP/FP/FN overlay semantics remain visible.
deck_contact_sheet: seven rendered pages present with the expected title-to-model-to-results-to-design-to-failure-to-next-to-medical sequence.
```

## Remaining Gates

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` remains `PENDING` and the task is left in `WAITING_FOR_CI` for watcher publication and real GitHub checks.

The model-page pixels changed, so fresh task-local Terra evidence is still required after publication. The visual-review input manifest is ready at:

```text
results/035_research_presentation_generic_model_support_recovery/visual_review/visual_inputs.json
```
