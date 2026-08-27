---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 031_research_presentation_one_call_production_entry
executor: Codex
implementation_commit: 93c99427012d771098f4116b81cb7e86e406fbbc
status: WAITING_FOR_CI
ci_status: PENDING
---

# 031 Research Presentation One-Call Production Entry - Result

## Implementation Commit

`93c99427012d771098f4116b81cb7e86e406fbbc`

## What Changed

- Added the normal one-call exact-CUHK production entry:

```text
skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py
```

- Added a strict validator:

```text
skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py
```

- Added a repository-owned public-safe engineering input bundle, mirrored into the presentation plugin, and explicitly marked it ineligible for Stage 5 holdouts:

```text
skills/tools/documents-media/presentations/shared/fixtures/stage4_engineering_research_bundle/
plugins/codex/plugins/presentations/shared/fixtures/stage4_engineering_research_bundle/
```

- Documented the one-call route in `research-presentations/SKILL.md` and added deterministic regression coverage proving the normal route, source-fidelity map, selector/layout path, anti-helper boundary, exact CUHK source use, task-local visual manifest, and source/plugin mirror sync.

031 does not claim Stage 4 PASS, `PROGRAM_MATURE`, `ONE_SHOT_QUALITY_PASS`, or final human acceptance.

## Generated Production Evidence

Generated exact-CUHK production artifacts:

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
implementation_commit=93c99427012d771098f4116b81cb7e86e406fbbc
workflow_type=reviewed_handoff
task_key=031_research_presentation_one_call_production_entry
input_count=6
```

Rendered content-page identities:

```text
slide_2_statistical_model              508d5842483139f703c646efdd1c117eed7323e8d5214c78c29302cf974ad491
slide_3_real_data_application          826c92ebcafe16bec41fa08357b7734360ada9295b547e2c99259b793e8a25d4
slide_4_experiment_design              3d421cdcd5b9eb8f2bf407bbb15947a501811aa37fdd3d9a5a81d1278d9ca671
slide_5_negative_result                ac54cbb287a3208b5a36587cf393936aeb140a5388915784b63d8beb880aac6a
slide_6_medical_image_comparison       f7aebcb3a9af980e4f64817ccd86003db7bcd03d5d812a638477ed2eb3fcad55
slide_7_next_experiment                e4578e43331fa076a8ed65bba4492e076bd3bc1fee1b9b955cd1691ad4a6a63d
```

Local render status:

```text
mechanical_qa=MECHANICAL_PASS
render_status=ok
pdf_pages=7
```

## Local Verification

Passed locally:

```text
python -m pytest tests/test_presentations.py::PresentationSharedTests::test_research_presentation_one_call_production_entry -q
python -m pytest tests/test_presentations.py::PresentationSharedTests::test_cuhk_scientific_layout_stage3_contract tests/test_presentations.py::PresentationSharedTests::test_research_presentation_todo_consolidation_and_promotions tests/test_presentations.py::PresentationSharedTests::test_research_presentation_one_call_production_entry -q
python -m py_compile skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py plugins/codex/plugins/presentations/shared/scripts/generate_research_presentation_production_entry.py plugins/codex/plugins/presentations/shared/scripts/validate_research_presentation_production_entry.py
python -m unittest discover -s tests
python scripts/build_codex_marketplace.py --validate
python scripts/build_codex_marketplace.py --check
python scripts/build_codex_marketplace.py --path-report
python scripts/skills.py validate
python scripts/skills.py audit --all
git diff --check
ai-bridge reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --implementation-commit 93c99427012d771098f4116b81cb7e86e406fbbc --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/031_research_presentation_one_call_production_entry/generated
pdfinfo results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/main.pdf
```

Observed local results: full unittest passed 134 tests; marketplace validation/check/path-report passed with 10 plugins, 25 active skills, and `over_budget=0`; skills validation passed 149 active skills and 18 profiles; Reviewed Handoff validation passed; strict 031 production validator passed; generated PDF has 7 pages and size 644923 bytes. I also inspected a local contact sheet of the 7 rendered PNGs for nonblank pages and obvious overlap.

## Handoff State

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` remains `PENDING` and this task is left in `WAITING_FOR_CI` for watcher publication, real GitHub checks, and subsequent task-local visual-review evidence generation.

No local `VISUAL_REVIEW.json` evidence is claimed or fabricated. At local handoff time, the evidence path remains pending:

```text
results/031_research_presentation_one_call_production_entry/visual_review/VISUAL_REVIEW.json
```
