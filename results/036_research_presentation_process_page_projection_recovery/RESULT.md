---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 036_research_presentation_process_page_projection_recovery
executor: Codex
implementation_commit: b061ecc99c549bf90f2de0ad80e4379a3bd59451
status: WAITING_FOR_CI
ci_status: PENDING
---

# 036 Research Presentation Process Page Projection Recovery - Result

## Implemented

- Rebalanced only the shared `EXPERIMENT_DESIGN` and `NEXT_EXPERIMENT` process-page layout/emission path.
- Expanded both process-page primary diagram regions to the full CUHK safe content width with a taller projection-scale body region.
- Raised process-page headings, labels, endpoint copy, failure evidence, comparator labels, decision text, and annotation text away from `\tiny` / `\scriptsize` emission.
- Reflowed process objects with generic count-based row spacing, preserving the source-backed experiment factors, procedures, endpoints, failure evidence, sampling choices, comparators, and decision criterion.
- Kept existing capacity fail-closed behavior and shared/plugin parity.
- Regenerated the task-local Stage 4 engineering bundle and visual-review inputs for implementation commit `b061ecc99c549bf90f2de0ad80e4379a3bd59451`.

Generated task-local artifacts:

```text
results/036_research_presentation_process_page_projection_recovery/generated/
results/036_research_presentation_process_page_projection_recovery/visual_review/visual_inputs.json
```

## Local Verification

Passed locally:

```text
python -m pytest tests/test_presentations.py -k "process_page_projection_scale_is_page_job_generic or cuhk_scientific_layout_stage3_contract"
python -m pytest tests/test_presentations.py
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python scripts/icon_audit.py --scope marketplace --check
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
git diff --check
ai-bridge visual-review preflight --target /home/yuukias/AI_Skills_Collection
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle skills/tools/documents-media/presentations/shared/fixtures/stage4_engineering_research_bundle/bundle.json --out-dir results/036_research_presentation_process_page_projection_recovery/generated --task-key 036_research_presentation_process_page_projection_recovery --implementation-commit b061ecc99c549bf90f2de0ad80e4379a3bd59451 --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/036_research_presentation_process_page_projection_recovery/generated --task-key 036_research_presentation_process_page_projection_recovery
```

Observed local results:

```text
targeted process/stage3 regression: 2 passed
full presentation regression: 33 passed
full unittest: Ran 142 tests, OK
production generation: MECHANICAL_PASS, render_status=ok
strict rendered validator: passed
skills validate: validated 149 active skills, 18 profiles, templates, and trigger eval scaffolds
marketplace validate/check/path-report: plugins=10 active_skills=25 over_budget=0
icon audit: passed
Reviewed Handoff validation passed
visual-review preflight: enabled, 036 listed, workflow present, secret metadata present
git diff --check: passed
```

Local rendered visual inspection:

```text
slide_4_experiment_design: process diagram now uses full-width safe region, larger nodes/endpoint labels, and no observed text/connector overlap in local PNG inspection.
slide_6_next_experiment: failure evidence, sampling choices, comparator arms, and decision rule are larger and use the full process-page region in local PNG inspection.
deck_contact_sheet: slides 4 and 6 no longer show the prior undersized central process-object pattern relative to the rest of the deck.
```

Current generated identities:

```text
render_input_identity_sha256: 424386beec49171891b6a158df3601f113d64f0ad83b1fd4573f7243e72e3b3a
rendered_pixel_identity_sha256: 0fb039c9c714e2577dc78694a66599e76ef2d9c55d1c9ec43959f41896c50fc1
deck_contact_sheet_sha256: a5abd59489f224c94506ba1830a429fc631f3d043732480af785bfd8fcf57a93
slide_2_statistical_model_sha256: 18260a71aef6d59a0e02ffa87e5defb4bc03b44d0235984c2cc6eceebe7f9123
slide_4_experiment_design_sha256: d2cea85a95b24d0788db0024d14374cda340637006da382c726fe3c48573b678
slide_6_next_experiment_sha256: 94621c2e7296b98cdd670932f16e53e47624b69b5f0147a64b4fa0fc5991f475
```

## Remaining Gates

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` remains `PENDING` and the task is left in `WAITING_FOR_CI` for watcher validation/publication and real GitHub checks.

Fresh task-local Terra evidence is still required after publication. The current visual-review manifest is ready at:

```text
results/036_research_presentation_process_page_projection_recovery/visual_review/visual_inputs.json
```
