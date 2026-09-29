---
schema: PRESENTATIONS_STAGE1_A_PHASE_COMPLETION_AUDIT_V1
task_key: presentations--stage1-front-door-two-template-foundation
audited_candidate_commit: a49bece0da6911da54e74a066502a0868c9c07a9
status: A_PHASE_COMPLETE_WAITING_FOR_CANONICAL_COURSE_STANDARD
---

# A-Phase Completion Audit

This audit is task-local evidence for the revised `plan_revision=1` split. It
does not claim final Stage 1 PASS, final G1, final G5, CI completion, or
Reviewer approval.

## Current State

- Reviewed Handoff state remains `PLAN_FROZEN`.
- `CURRENT.next_action` remains `RUN_CODEX_EXECUTOR`.
- `CURRENT.plan_revision` remains `1`.
- `ci_required` remains `true`; real GitHub CI has not been started for a final
  integrated candidate.
- The only missing dependency for final course-standard adapter integration is
  the independent canonical standard-Beamer owner supplying:
  - exact canonical `course-standard` source path;
  - exact candidate commit;
  - allowed consumption boundary;
  - verified source identity.
- Private G5 reference preflight on 2026-09-29 found that the preferred
  execution-machine input is not currently present at
  `private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf`
  in the canonical checkout or the task worktree. This does not change the
  A-phase routing/render-owner evidence, but final G5 must not proceed until
  the exact `Chapter1.pdf` with SHA-256
  `ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7`
  and 50 pages is available; otherwise the final integration/review path must
  use `BLOCKED_REFERENCE_UNAVAILABLE`.

## A-Phase Evidence Map

| Plan A item | Current evidence |
|---|---|
| unified Presentations front door | `skills/tools/documents-media/presentations/shared/scripts/stage1_front_door.py` |
| Marketplace/plugin routing | `scripts/codex_marketplace_config.json`; generated `plugins/codex/plugins/presentations/.codex-plugin/plugin.json` |
| research / teaching / business routing infrastructure | `stage1_front_door.py`; `tests.test_presentations.PresentationSharedTests.test_stage1_front_door_freezes_routing_matrix` |
| editable PPTX/Slides preservation | `test_stage1_front_door_normalizes_explicit_editable_output_extensions`; `test_business_and_shared_routes_connect_chinese_writing_handoff` |
| local-edit fast path | `test_stage1_front_door_freezes_routing_matrix` |
| external locked template pass-through | `test_stage1_front_door_freezes_routing_matrix` |
| plan-only route and no artifact claim | `test_stage1_front_door_freezes_routing_matrix` |
| exactly-two-template registry while course-standard is unresolved | `built_in_template_manifest()` and `test_course_standard_source_is_waiting_on_canonical_template_task` |
| presentation-desktop consistency | `profiles/presentation-desktop.json`; `test_business_and_shared_routes_connect_chinese_writing_handoff` |
| source/generated authority cleanup and generator parity | `python scripts/build_codex_marketplace.py --write --validate --check --path-report`; `test_research_presentation_todo_consolidation_and_promotions` |
| render-chinese-math-pdf owner integration | `skills/tools/documents-media/presentations/shared/scripts/render_owner.py`; CUHK generator render-owner calls |
| reusable host-path assumptions removed | `test_stage1_render_owner_contract_removes_private_host_paths`; RP-G2 scan over source and generated payload |
| CUHK adapter integration with render owner | `generate_cuhk_scientific_layout_stage3.py`; `render_owner.adapter_manifest()` evidence |
| typed blocked_missing_dependency | `render_owner.blocked_missing_dependency()` and `test_stage1_render_owner_contract_gates_missing_dependency_and_font_fallback` |
| forbidden fallback/font QA | `render_owner.font_contract_gate()` and `test_stage1_render_owner_contract_gates_missing_dependency_and_font_fallback` |
| RP-G1/RP-G5 infrastructure independent of final course-standard source | `render_owner.profile_identity()`; `adapter_manifest()` records owner route/profile for CUHK and pending course-standard |
| G5_REVIEW_INPUTS/private bundle plumbing | `prepare_g5_private_review.py`; `test_g5_private_review_plumbing_waits_for_canonical_course_standard` |
| routing tests | `tests.test_presentations.PresentationSharedTests.test_stage1_front_door_*` |
| Marketplace/generator tests | generator command above plus `test_presentations_marketplace_front_door_interface` |
| broad/risk-matched tests not requiring final course-standard pixels | `python -m unittest tests.test_presentations`; `python scripts/skills.py validate`; `git diff --check` |

## Explicit Non-Claims

- No `skills/tools/documents-media/presentations/shared/templates/course-standard`
  source body exists in this task.
- No temporary or task-local course-standard source is treated as canonical.
- Final teaching route artifacts are not claimed.
- Final RP-G1/RP-G5 two-adapter evidence is not claimed.
- Final G1/G5, exact Chapter1 private-reference consumption, private G5
  direct-pixel evidence, real GitHub CI, and Scheduled GPT implementation
  review remain pending.

## Dependency Wait

The current lawful wait label is:

```text
WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE
```

This is a scoped dependency wait, not a Reviewed Handoff `CURRENT.state`.
Executor should resume final integration only after Planner/user provides the
canonical `course-standard` source path, commit, and allowed consumption
boundary from the independent standard-Beamer owner.
