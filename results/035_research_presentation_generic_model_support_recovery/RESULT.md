---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 035_research_presentation_generic_model_support_recovery
executor: Codex
implementation_commit: d44adaef2949d18843d5c8b22b78357345e3ab62
status: WAITING_FOR_CI
ci_status: PENDING
---

# 035 Research Presentation Generic Model Support Recovery - Result

## Implemented

- Rebalanced only the shared `STATISTICAL_MODEL` slide path after Review 1: the formula, source-backed annotation, and existing `Model components` / `Interpretation` blocks now use more of the page and larger presentation text.
- Kept model support source-driven: support blocks still consume only `scientific_objects` and `key_message`; missing support fields still produce no filler block or internal production language.
- Preserved shared/plugin parity by applying the same renderer change in the presentations plugin mirror.
- Made medical semantic overlay rendering deterministic in the same shared/plugin renderer so regeneration does not create unrelated slide 7 pixel/hash drift.
- Regenerated the task-local Stage 4 engineering bundle and visual-review inputs for implementation commit `d44adaef2949d18843d5c8b22b78357345e3ab62`.

Generated task-local artifacts:

```text
results/035_research_presentation_generic_model_support_recovery/generated/
results/035_research_presentation_generic_model_support_recovery/visual_review/visual_inputs.json
```

## Local Verification

Passed locally:

```text
python -m pytest tests/test_presentations.py -k "statistical_model_support_copy_is_source_driven_for_unrelated_model or one_call_production"
python -m pytest tests/test_presentations.py
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle skills/tools/documents-media/presentations/shared/fixtures/stage4_engineering_research_bundle/bundle.json --out-dir results/035_research_presentation_generic_model_support_recovery/generated --task-key 035_research_presentation_generic_model_support_recovery --implementation-commit d44adaef2949d18843d5c8b22b78357345e3ab62 --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/035_research_presentation_generic_model_support_recovery/generated --task-key 035_research_presentation_generic_model_support_recovery
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python scripts/icon_audit.py --scope marketplace --check
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
python -m unittest discover -s tests
pdfinfo results/035_research_presentation_generic_model_support_recovery/generated/cuhk_production_build/main.pdf
python scripts/skills.py doctor
ai-bridge visual-review preflight --target /home/yuukias/AI_Skills_Collection
git diff --check
```

Observed local results:

```text
targeted presentation regression: 2 passed
full presentation regression: 32 passed
production generation: MECHANICAL_PASS, render_status=ok
strict rendered validator: passed
skills validate: validated 149 active skills, 18 profiles, templates, and trigger eval scaffolds
marketplace validate/check/path-report: plugins=10 active_skills=25 over_budget=0
icon audit: passed
Reviewed Handoff validation passed
full unittest: Ran 141 tests, OK
pdfinfo: Pages=7
visual-review preflight: enabled, 035 listed, workflow present, secret metadata present
git diff --check: passed
```

Local rendered visual inspection:

```text
slide_2_statistical_model: formula remains primary; annotation and source-backed support panels are larger, readable, and non-overlapping.
slide_3_real_data_application: unchanged rendered page hash 4c609896aff98b3d8dc24941ace84690b9e858d370af330682500e735df6af2d.
slide_4_experiment_design: unchanged rendered page hash e1775c71ddee184155cd69bc7c9858a5967be5c6a220cd0c6c25b33e372f69f1.
slide_5_negative_result: unchanged rendered page hash daf79c0f303860e8d4c01fe6bb810ef80a4f0d454bc681d100e017e02c45eb06.
slide_6_next_experiment: unchanged rendered page hash 0fc4574ecbb5deb5ffac2cecbddcdd66967e2301c3199a931ffe06507f1e95aa.
slide_7_medical_image_comparison: unchanged rendered page hash af5b29da99fe6aef8464023383e7634f0cc40f2df32ead582d584b96d5d9e000 after deterministic overlay ordering.
deck_contact_sheet: regenerated with updated slide 2 and unchanged slides 3-7.
```

Current generated identities:

```text
render_input_identity_sha256: b6d7e55ec16a0a5d4140fcb322a2fb6b165fb4ad82420148f1edb6ccfa1bbed1
rendered_pixel_identity_sha256: 1bab501f9986710211824c33702814608a32e89910fb65f6cae56e3ddca8ca9f
deck_contact_sheet_sha256: e47b99e2c698574f000ae668c41aea33ae7a974baf4761fc2f871be2d75577a8
slide_2_statistical_model_sha256: 18260a71aef6d59a0e02ffa87e5defb4bc03b44d0235984c2cc6eceebe7f9123
```

## Remaining Gates

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` remains `PENDING` and the task is left in `WAITING_FOR_CI` for watcher publication and real GitHub checks.

Because slide 2 pixels changed, fresh task-local Terra evidence is still required after publication. The previous `VISUAL_REVIEW.json` is stale for this implementation because it binds implementation `5501edce262254547bbcefbe04a0827172a73861`; the current manifest is ready at:

```text
results/035_research_presentation_generic_model_support_recovery/visual_review/visual_inputs.json
```
