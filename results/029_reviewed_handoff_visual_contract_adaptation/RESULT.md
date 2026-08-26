---
schema: AI_BRIDGE_REVIEWED_RESULT_V1
task_key: 029_reviewed_handoff_visual_contract_adaptation
executor: Codex
implementation_commit: 9f067118efe528241e45c425555a6061fa342d41
status: WAITING_FOR_CI
ci_status: PENDING
---

# 029 Reviewed Handoff Visual Contract Consumer Adaptation - Result

## Implementation Commit

`9f067118efe528241e45c425555a6061fa342d41`

## Implemented

- Added `scripts/resolve_reviewed_handoff_visual_target.py`, a deterministic push-mode resolver for task-local Reviewed Handoff visual-review targets.
- Updated `.github/workflows/ai-bridge-visual-review.yml` so `workflow_dispatch` explicit inputs remain the manual recovery/debug priority path, while push events use the resolver instead of repository-level fixed manifest/output vars.
- Updated the Bridge Kit visual-review extra pin to `647f63c49ccea828a0ac76a6e9adce026531c906`.
- Documented the AI_Skills_Collection consumer contract in `docs/AI_BRIDGE_VISUAL_REVIEW.md`.

## Consumer Contract

For push events, a task is eligible only when its tracked `CURRENT.json` has:

- `visual_review_required=true`;
- `state=READY_FOR_GPT_REVIEW`;
- repository-relative `visual_review_manifest_path` and `visual_review_evidence_path`;
- a real parseable manifest whose `task_key`, `workflow_type=reviewed_handoff`, `identity_bindings.task_key`, and `identity_bindings.implementation_commit` match `CURRENT.json`;
- no fresh evidence already matching the same manifest identity and implementation commit.

Resolver outcomes are deterministic:

- 0 eligible tasks: write `AI_BRIDGE_VISUAL_REVIEW_SKIP=1` and no-op normally;
- exactly 1 eligible task: export task-local manifest/output paths for `ai-bridge visual-review run`;
- more than 1 eligible task, illegal path, missing/invalid manifest, or identity conflict: exit nonzero and fail closed.

Fresh evidence is detected from `VISUAL_REVIEW.json` by matching `input_manifest.manifest_sha256` plus `input_manifest.identity_bindings.task_key` and `implementation_commit`; stale or malformed evidence does not suppress a pending review.

## Verification

Passed locally:

```text
python -m unittest tests.test_reviewed_handoff_visual_target
python -m unittest discover -s tests
python scripts/skills.py validate
python scripts/build_codex_marketplace.py --validate --check --path-report
python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection
python -c 'import yaml; yaml.safe_load(open(".github/workflows/ai-bridge-visual-review.yml", encoding="utf-8")); print("workflow yaml parsed")'
python scripts/resolve_reviewed_handoff_visual_target.py --target .
python -m py_compile scripts/resolve_reviewed_handoff_visual_target.py
git diff --check
```

Observed results:

- targeted resolver/workflow tests passed: 11 tests;
- full unittest suite passed: 133 tests;
- skills validation passed: 149 active skills, 18 profiles;
- marketplace validation/check/path-report passed with 10 plugins, 25 active skills, and `over_budget=0`;
- Reviewed Handoff validation passed for 29 tasks;
- workflow YAML parsed successfully;
- current repository state has no pending task-local visual review, so resolver returned `status=none`, `eligible_count=0`.

## Deviations / blockers

GitHub CI is required for this task and was not claimed locally. Per protocol, `ci_status` remains `PENDING` and the task is left in `WAITING_FOR_CI` for watcher publication and real GitHub checks.

`actionlint` and `ruby` were not installed on this host; workflow syntax validation used the available Python `PyYAML` parser plus workflow contract regression tests.
