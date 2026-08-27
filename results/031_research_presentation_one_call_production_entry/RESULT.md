---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 031_research_presentation_one_call_production_entry
executor: Codex
implementation_commit: 11509b5e2bf7959433f1616c1d4ad77f77f4000e
status: WAITING_FOR_CI
ci_status: PENDING
---

# 031 Research Presentation One-Call Production Entry - Repair Result

## Implementation Commit

`11509b5e2bf7959433f1616c1d4ad77f77f4000e`

## Repair Scope

- Repaired canonical exact-CUHK rendered identity by restoring the template's visible CUHK crest in the final Beamer headline after the `miniframes` outer theme is loaded. The repair uses the canonical copied `assets/logo_RGB` image and keeps the section navigation and footline geometry.
- Repaired shared medical comparison inspectability by deriving semantic display overlays from the same-case GT, prediction, and error assets. The generated full panels and ROI zoom crops now expose missed-GT (`fn`) in GT, prediction-only (`fp`) in Prediction, and both classes in Error without changing the source case, ROI coordinates, gold selection, or layout family.
- Synchronized the presentation plugin mirror and added deterministic regression assertions for the CUHK headline contract, medical overlay artifacts, and source/plugin mirror parity.

031 still does not claim Stage 4 PASS, `PROGRAM_MATURE`, `ONE_SHOT_QUALITY_PASS`, or final human acceptance.

## Generated Production Evidence

Regenerated exact-CUHK production artifacts:

```text
results/031_research_presentation_one_call_production_entry/generated/
```

Key outputs:

```text
results/031_research_presentation_one_call_production_entry/generated/BUILD_MANIFEST.json
results/031_research_presentation_one_call_production_entry/generated/deck_plan.json
results/031_research_presentation_one_call_production_entry/generated/source_fidelity_map.json
results/031_research_presentation_one_call_production_entry/generated/runtime_trace.json
results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/main.tex
results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/main.pdf
results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/rendered/
```

Generated task-local visual manifest:

```text
results/031_research_presentation_one_call_production_entry/visual_review/visual_inputs.json
```

Manifest bindings:

```text
implementation_commit=11509b5e2bf7959433f1616c1d4ad77f77f4000e
workflow_type=reviewed_handoff
task_key=031_research_presentation_one_call_production_entry
input_count=6
```

Rendered content-page identities:

```text
slide_2_statistical_model              185b02f15bd7c524c3f8fe656f58c0d23882228d996a236730dbeb8c61c860bf
slide_3_real_data_application          ec4bdc7aaefefc57518079b1483790f0ab25d0ab37d494bee9e097a4107196a7
slide_4_experiment_design              ed55c2329a3945e4d46d548dec3315c639d24a0af940507f6752b6979639b8da
slide_5_negative_result                81d14477c77d30f39439cf37d12ac320677da2f2c7768762caa18ff35a54a932
slide_6_medical_image_comparison       5ef013e4431e89eebb51462a8ee41c93e8025d798165a86b5bb01534acdf92c6
slide_7_next_experiment                ddc285ac857251131f3cf6d47a6a14b344dbcf6ae7e6c2793f59d9cfcdc02c85
```

Medical semantic overlay trace:

```text
failure_gt.png       display=stage3_assets/failure_gt_semantic_overlay.png       zoom=stage3_assets/failure_gt_semantic_overlay_roi_zoom.png       visible_error_classes=[fn]
failure_pred.png     display=stage3_assets/failure_pred_semantic_overlay.png     zoom=stage3_assets/failure_pred_semantic_overlay_roi_zoom.png     visible_error_classes=[fp]
failure_error.png    display=stage3_assets/failure_error_semantic_overlay.png    zoom=stage3_assets/failure_error_semantic_overlay_roi_zoom.png    visible_error_classes=[fn, fp]
```

Local render status:

```text
mechanical_qa=MECHANICAL_PASS
render_status=ok
pdf_pages=7
pdf_size=1062008 bytes
```

I inspected the regenerated rendered pixels for the two repair blockers: the content pages now show a visible CUHK crest in the top-left headline, and `slide_6_medical_image_comparison` shows orange GT missed-region pixels, red prediction-only pixels, and red/orange Error pixels in both the full row and ROI zoom row.

## Local Verification

Passed locally:

```text
python -m py_compile skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py
python -m pytest tests/test_presentations.py::PresentationSharedTests::test_research_presentation_one_call_production_entry -q
python -m pytest tests/test_presentations.py::PresentationSharedTests::test_cuhk_template_payload_is_complete_and_reference_deck_is_valid -q
python -m pytest tests/test_presentations.py::PresentationSharedTests::test_research_presentation_todo_consolidation_and_promotions -q
python -m pytest tests/test_presentations.py::PresentationSharedTests::test_cuhk_scientific_layout_stage3_contract -q
python -m pytest tests/test_presentations.py -q
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --implementation-commit 11509b5e2bf7959433f1616c1d4ad77f77f4000e --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py
python skills/tools/documents-media/presentations/shared/scripts/validate_cuhk_scientific_layout_stage3.py --out-dir docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated --task-key 030_stage3_visual_recovery
python -m pytest -q
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
pdfinfo results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/main.pdf
git diff --check
```

Observed local results:

```text
tests/test_presentations.py: 27 passed
full pytest: 135 passed
skills validate: validated 149 active skills, 18 profiles, templates, and trigger eval scaffolds
marketplace validate/check/path-report: plugins=10 active_skills=25 over_budget=0
Reviewed Handoff validation passed
031 strict rendered validator passed
Stage 3 strict rendered validator passed with task_key=030_stage3_visual_recovery
pdfinfo: Pages=7, File size=1062008 bytes
```

The default Stage 3 validator invocation without `--task-key` was not the relevant gate for the currently committed historical Stage 3 artifact: it failed on `task_key mismatch`. The matching invocation above passed.

## Handoff State

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` remains `PENDING` and this task is left in `WAITING_FOR_CI` for watcher publication and real GitHub checks.

The current generated `visual_inputs.json` is bound to implementation commit `11509b5e2bf7959433f1616c1d4ad77f77f4000e`. I did not fabricate a new `VISUAL_REVIEW.json`; the existing file was stale review evidence from the previous implementation and has been removed so the published handoff can wait for fresh task-local visual review after CI.
