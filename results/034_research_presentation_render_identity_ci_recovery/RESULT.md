---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 034_research_presentation_render_identity_ci_recovery
executor: Codex
implementation_commit: 68cc193ec09d29617a8f2642dac49615a0c5df76
status: WAITING_FOR_CI
ci_status: PENDING
---

# 034 Research Presentation Render Identity CI Recovery - Result

## Implemented

- Added a dual evidence identity contract for the normal `research-presentations` production path.
- Every render attempt now records `render_input_identity_sha256` from the actual files sent into the render chain: generated `main.tex`, generated `scientific_layouts.tex`, copied scientific assets, and the copied canonical CUHK support/style/assets.
- Pixel evidence remains strict: rendered pages, the contact sheet, and `rendered_pixel_identity_sha256` are present only when real PNG render succeeds. No-render artifacts keep pixel fields null and mark `pixel_evidence_status.status=UNAVAILABLE_RENDER_NOT_OK`.
- The deck quality loop now records that legacy `initial_render_identity` / `repaired_render_identity` are render-input identities, and also stores explicit `initial_render_input_identity`, `repaired_render_input_identity`, and nullable rendered-pixel identities.
- The deterministic `ADJUST_TRANSITION_CUE` repair test now proves both render-input identity and actual `main.tex` SHA change across initial and repaired production inputs.
- Shared/plugin parity was preserved for the generator, validator, and `deck_quality_loop.py`.

Generated task-local artifacts:

```text
results/034_research_presentation_render_identity_ci_recovery/generated/
results/034_research_presentation_render_identity_ci_recovery/visual_review/visual_inputs.json
```

## Key Identities

```text
implementation_commit=68cc193ec09d29617a8f2642dac49615a0c5df76
render_status=ok
rendered_png_count=7
render_input_identity_sha256=c4129f2b2e2f7c3a7e65af93e5c663ea63d08aef9b1d844d0355291c6d32831b
rendered_pixel_identity_sha256=ebd4e6ac8e1176f8e99d458d49fca980c0260488751642ade5be6004bb9a4bf9
deck_identity_sha256=7736bda04aeada434f474d96f1e5704859b65d5fba4e4b9577fde9ac9d66fdd0
pdf_sha256=ff4e842a6b5466b2c56494c89f3ecb89a9fe7fb73cf57a2021b2be967f24a8db
deck_contact_sheet_sha256=83d88d572e648d2b32b0bb368faba1be536f7a3f23917c4260464233e090c71c
```

Rendered content-page SHA values:

```text
slide_2_statistical_model=489c286b74f9b4cf0ea74338e0e0fb7dd0a6da1d8fdb9bb0f80583881a71aa0e
slide_3_real_data_application=4c609896aff98b3d8dc24941ace84690b9e858d370af330682500e735df6af2d
slide_4_experiment_design=e1775c71ddee184155cd69bc7c9858a5967be5c6a220cd0c6c25b33e372f69f1
slide_5_negative_result=daf79c0f303860e8d4c01fe6bb810ef80a4f0d454bc681d100e017e02c45eb06
slide_6_next_experiment=0fc4574ecbb5deb5ffac2cecbdd66967e2301c3199a931ffe06507f1e95aa
slide_7_medical_image_comparison=af5b29da99fe6aef8464023383e7634f0cc40f2df32ead582d584b96d5d9e000
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
build_manifest_sha256=a5689079e98046f118f78b74f6dd2cc1012f2e418340d8b8e7828c06013f3a0d
deck_sequence_summary_sha256=6bf81dc6cbfe5530da36a99d26132ebf90e1230c6bc0f5e33b9c0b7b1cb60180
quality_loop_state_sha256=9e08c79f546283a2ae67470a1397b9741e552ecfde552812d7d78cf920eb74c1
```

## Local Verification

Passed locally:

```text
python -m pytest tests/test_presentations.py -k "research_presentation_one_call_production_entry or research_presentation_deck_quality_loop_consumes_review_and_fails_closed"
python -m py_compile skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py skills/tools/documents-media/presentations/shared/scripts/deck_quality_loop.py skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py plugins/codex/plugins/presentations/shared/scripts/generate_research_presentation_production_entry.py plugins/codex/plugins/presentations/shared/scripts/deck_quality_loop.py plugins/codex/plugins/presentations/shared/scripts/validate_research_presentation_production_entry.py tests/test_presentations.py
python scripts/validate_skills.py
python scripts/build_codex_marketplace.py --validate
python scripts/build_codex_marketplace.py --check
python scripts/build_codex_marketplace.py --path-report
python -m unittest discover -s tests
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle skills/tools/documents-media/presentations/shared/fixtures/stage4_engineering_research_bundle/bundle.json --out-dir results/034_research_presentation_render_identity_ci_recovery/generated --task-key 034_research_presentation_render_identity_ci_recovery --implementation-commit 68cc193ec09d29617a8f2642dac49615a0c5df76 --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/034_research_presentation_render_identity_ci_recovery/generated --task-key 034_research_presentation_render_identity_ci_recovery
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/034_research_presentation_render_identity_ci_recovery/generated --task-key 034_research_presentation_render_identity_ci_recovery --allow-missing-render
pdfinfo results/034_research_presentation_render_identity_ci_recovery/generated/cuhk_production_build/main.pdf
ai-bridge reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
```

Observed local results:

```text
targeted pytest: 2 passed
full unittest: 140 tests passed
skills validate: validated 149 active skills, 18 profiles, templates, and trigger eval scaffolds
marketplace validate/check/path-report: plugins=10 active_skills=25 over_budget=0
production generation: MECHANICAL_PASS, render_status=ok
strict rendered validator: passed
allow-missing-render validator: passed
pdfinfo: Pages=7, File size=1062735 bytes
Reviewed Handoff validation passed
```

## Remaining Gates

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` remains `PENDING` and this task is left in `WAITING_FOR_CI` for watcher publication and real GitHub checks.

Fresh task-local Terra visual review evidence is not present yet at:

```text
results/034_research_presentation_render_identity_ci_recovery/visual_review/VISUAL_REVIEW.json
```

The visual input manifest is ready and bound to the implementation commit, render-input identity, rendered pixel identity, PDF, page PNGs, contact sheet, deck sequence summary, and quality-loop state.
