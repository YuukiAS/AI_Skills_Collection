---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 034_research_presentation_render_identity_ci_recovery
executor: Codex
implementation_commit: fc0b8908b865de464c0d1ddf4475a9e57c11bbd5
status: WAITING_FOR_CI
ci_status: PENDING
---

# 034 Research Presentation Render Identity CI Recovery - Result

## Implemented

- Repaired the audience-facing title chain by replacing the engineering subtitle with a research-facing study description.
- Added a generic metadata anti-leak gate for normal production title/subtitle fields, backed by regression coverage for `production regression` / `source bundle` language.
- Preserved the 034 dual identity contract: every render attempt still records render-input identity from actual generated TeX/CUHK/assets, while rendered-pixel identity remains strict and nullable.
- Repaired the `STATISTICAL_MODEL` page density by carrying existing source-grounded `key_message` and `scientific_objects` into production specs and rendering compact model-role / calibration-link support blocks.
- Kept the equation as the primary scientific object, preserved recipe-derived geometry mutation behavior, and kept shared/plugin presentation script and fixture parity.

Generated task-local artifacts:

```text
results/034_research_presentation_render_identity_ci_recovery/generated/
results/034_research_presentation_render_identity_ci_recovery/visual_review/visual_inputs.json
```

## Key Identities

```text
implementation_commit=fc0b8908b865de464c0d1ddf4475a9e57c11bbd5
render_status=ok
rendered_png_count=7
render_input_identity_sha256=a960ec005fc46f12fccb396bda639535e911273f7592dfa91f4494af5d8b5118
rendered_pixel_identity_sha256=d9048ee78d41e307821d1bb52a9430c05c212fea8c653f4d621a145e5eafd2c1
deck_identity_sha256=ad09c78061797eb547237df6f07e43a9661b48914fd243aa14d4664bce981737
pdf_sha256=f55c396428cd1e11657717b0a8b64ddc73e6637c860bb5745a2327905e49470b
deck_contact_sheet_sha256=5ba36bbd97f465e5bd05729113dc5f570243f5ec371e705758f98f747d55065a
```

Rendered content-page SHA values:

```text
slide_2_statistical_model=fa2cbb20122692ea9d8517d8ad19d7bb8568a814608acd5b3521d6f451800ee2
slide_3_real_data_application=4c609896aff98b3d8dc24941ace84690b9e858d370af330682500e735df6af2d
slide_4_experiment_design=e1775c71ddee184155cd69bc7c9858a5967be5c6a220cd0c6c25b33e372f69f1
slide_5_negative_result=daf79c0f303860e8d4c01fe6bb810ef80a4f0d454bc681d100e017e02c45eb06
slide_6_next_experiment=0fc4574ecbb5deb5ffac2cecbddcdd66967e2301c3199a931ffe06507f1e95aa
slide_7_medical_image_comparison=6a095ca7983eeafe285a2b491b3288d21f1b5deaa10b4f7877fa969df0d21d76
```

Current quality-loop state:

```text
deck_level_decision=WAITING_FOR_DECK_VISUAL_REVIEW
repair_cycle_count=0
final_decision=null
render_identity_kind=render_input_identity_sha256
```

Fresh task-local visual review input manifest:

```text
inputs=7
build_manifest_sha256=cf597c03c7b8ecd5419c4262d3c782b00e7db884e1051df40bcc91ff43979c99
deck_sequence_summary_sha256=883731e996f79010002d16db8106c6b00fc52dab46298f64d7284b6ef9d5bf88
quality_loop_state_sha256=82d6835c53f9ac134a9eb78e5d2c6e3c52bf0c800a5f863723d595ce3fa48353
```

## Local Verification

Passed locally:

```text
python -m unittest discover -s tests -p 'test_presentations.py' -k 'cuhk_scientific_layout_stage3_contract'
python -m unittest discover -s tests -p 'test_presentations.py' -k 'research_presentation_one_call_production_entry' -k 'research_presentation_deck_quality_loop_consumes_review_and_fails_closed'
python -m unittest discover -s tests
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle skills/tools/documents-media/presentations/shared/fixtures/stage4_engineering_research_bundle/bundle.json --out-dir results/034_research_presentation_render_identity_ci_recovery/generated --task-key 034_research_presentation_render_identity_ci_recovery --implementation-commit fc0b8908b865de464c0d1ddf4475a9e57c11bbd5 --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/034_research_presentation_render_identity_ci_recovery/generated --task-key 034_research_presentation_render_identity_ci_recovery
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/034_research_presentation_render_identity_ci_recovery/generated --task-key 034_research_presentation_render_identity_ci_recovery --allow-missing-render
python scripts/skills.py validate
python scripts/skills.py doctor
python scripts/build_codex_marketplace.py --validate
python scripts/build_codex_marketplace.py --check
python scripts/build_codex_marketplace.py --path-report
python scripts/icon_audit.py --scope marketplace --check
pdfinfo results/034_research_presentation_render_identity_ci_recovery/generated/cuhk_production_build/main.pdf
ai-bridge reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
```

Observed local results:

```text
targeted unittest: 1 passed for Stage 3 contract; 2 passed for 034 identity/quality-loop tests
full unittest: 140 tests passed
skills validate: validated 149 active skills, 18 profiles, templates, and trigger eval scaffolds
marketplace validate/check/path-report: plugins=10 active_skills=25 over_budget=0
icon audit: passed
production generation: MECHANICAL_PASS, render_status=ok
strict rendered validator: passed
allow-missing-render validator: passed
pdfinfo: Pages=7, File size=1064777 bytes
Reviewed Handoff validation passed
shared/plugin parity: generator_cmp=0 stage3_cmp=0 validator_cmp=0 bundle_cmp=0
```

Local rendered visual inspection:

```text
title page: no production-regression/source-bundle subtitle leak; title remains source-specific
slide_2_statistical_model: formula, annotation, model-role block, and calibration-link block render without overlap
deck_contact_sheet: seven rendered pages present, with the statistical-model page no longer formula-only
```

## Remaining Gates

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` is left as `PENDING` and this task is left in `WAITING_FOR_CI` for watcher publication and real GitHub checks.

The prior Terra evidence has been preserved at `results/034_research_presentation_render_identity_ci_recovery/visual_review/VISUAL_REVIEW_68cc193ec09d29617a8f2642dac49615a0c5df76_STALE.json` because it belongs to the prior implementation/review target. Fresh task-local Terra visual review still needs to be collected after CI using the updated manifest:

```text
results/034_research_presentation_render_identity_ci_recovery/visual_review/visual_inputs.json
```
