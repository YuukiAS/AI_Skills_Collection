---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 036_research_presentation_process_page_projection_recovery
executor: Codex
implementation_commit: 6045675e94d829dd4aa1cf47c0a7cd368002e4cc
status: WAITING_FOR_CI
ci_status: PENDING
---

# 036 Research Presentation Process Page Projection Recovery - Repair Result

## Implemented

- Repaired the Review 1 source-fidelity blocker in the shared `EXPERIMENT_DESIGN` and `NEXT_EXPERIMENT` process-page emitters.
- Replaced hardcoded clustered-fixture labels/copy with source-backed page-job objects:
  - `EXPERIMENT_DESIGN` section labels now derive from `spec["nodes"]`.
  - The hierarchy caption now derives from the same source-backed node role instead of `Subject records nested inside each center; 400 reps per cell`.
  - `NEXT_EXPERIMENT` evidence caption now derives from the page-job evidence node instead of `coverage shortfall at high ICC`.
- Kept the projection-scale geometry from the first 036 implementation: enlarged process regions, readable labels, left-to-right process order, and existing capacity fail-closed behavior.
- Updated the bounded generic regression so an unrelated acquisition/measurement-noise page-job proves that current clustered fixture terms do not leak into normal production output.
- Preserved shared/plugin parity for generator and validator files.
- Regenerated the task-local Stage 4 engineering bundle and `visual_review/visual_inputs.json` for implementation commit `6045675e94d829dd4aa1cf47c0a7cd368002e4cc`.

Generated task-local artifacts:

```text
results/036_research_presentation_process_page_projection_recovery/generated/
results/036_research_presentation_process_page_projection_recovery/visual_review/visual_inputs.json
```

## Local Verification

Passed locally:

```text
python -m pytest tests/test_presentations.py::PresentationSharedTests::test_process_page_projection_scale_is_page_job_generic -q
python -m pytest tests/test_presentations.py -q
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python scripts/icon_audit.py --scope marketplace --check
python skills/tools/documents-media/presentations/shared/scripts/generate_research_presentation_production_entry.py --input-bundle skills/tools/documents-media/presentations/shared/fixtures/stage4_engineering_research_bundle/bundle.json --out-dir results/036_research_presentation_process_page_projection_recovery/generated --task-key 036_research_presentation_process_page_projection_recovery --implementation-commit 6045675e94d829dd4aa1cf47c0a7cd368002e4cc --write-result-visual-inputs
python skills/tools/documents-media/presentations/shared/scripts/validate_research_presentation_production_entry.py --out-dir results/036_research_presentation_process_page_projection_recovery/generated --task-key 036_research_presentation_process_page_projection_recovery
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
ai-bridge visual-review preflight --target /home/yuukias/AI_Skills_Collection
git diff --check
```

Observed local results:

```text
targeted process projection regression: 1 passed
full presentation regression: 33 passed
full unittest: Ran 142 tests, OK
skills validate: validated 149 active skills, 18 profiles, templates, and trigger eval scaffolds
marketplace validate/check/path-report: plugins=10 active_skills=25 over_budget=0
icon audit: passed
production generation: MECHANICAL_PASS, render_status=ok
production strict rendered validator: passed
Reviewed Handoff validation passed
visual-review preflight: enabled, 036 listed, workflow present, secret metadata present
git diff --check: passed
```

Additional local checks:

```text
No matches in current generated deck/manifest for:
DGP stress grid
Center hierarchy
Subject records nested inside each center
400 reps per cell
coverage shortfall at high ICC
```

Local rendered visual inspection:

```text
slide_4_experiment_design: source-backed node labels remain projection-readable; no duplicate annotation or observed text/connector overlap.
slide_6_next_experiment: failure evidence, source-backed evidence caption, sampling choices, comparator arms, and decision rule remain projection-readable without repeating the full failure sentence.
deck_contact_sheet: slides 4 and 6 retain the repaired process-page scale relative to the rest of the deck.
slide_7_medical_image_comparison: unchanged by this repair, preserving Review 1's out-of-scope medical/storyline boundary.
```

Current generated identities:

```text
render_input_identity_sha256: eef1037690a953c78fdcb290907ee795bef9e6b7bbb5b0a6f564b9d2fc8f1e7b
rendered_pixel_identity_sha256: 0b2a489ca3c7f0cdb3a14d0de7d76adcc582b7e6027d3e491ea024d585a66443
deck_contact_sheet_sha256: 75bf60339ba39b5b61ced0ad358401e9e3b2bea9d93bbbba4113b8033c10b434
slide_2_statistical_model_sha256: 18260a71aef6d59a0e02ffa87e5defb4bc03b44d0235984c2cc6eceebe7f9123
slide_4_experiment_design_sha256: 608d79cb5c2858255b28f97c4f3296adac08803827a9007a9b0a27485ada501c
slide_6_next_experiment_sha256: 19f261a6bff83351b5cb59f972d8433692a32708c506c0b055f02605c445d4bb
slide_7_medical_image_comparison_sha256: af5b29da99fe6aef8464023383e7634f0cc40f2df32ead582d584b96d5d9e000
```

## Remaining Gates

GitHub CI is required and is not claimed locally. Per protocol, `ci_status` remains `PENDING` and this task is left in `WAITING_FOR_CI` for watcher validation/publication and real GitHub checks.

Fresh task-local Terra evidence is still required for the new `6045675e94d829dd4aa1cf47c0a7cd368002e4cc` identity after publication. The existing `VISUAL_REVIEW.json` is prior evidence and must not be used as closure for this repair.

Expected fresh visual evidence output:

```text
results/036_research_presentation_process_page_projection_recovery/visual_review/VISUAL_REVIEW_6045675.json
```
