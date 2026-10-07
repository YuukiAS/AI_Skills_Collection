# Project Instructions Editor — Simple Formal Core Closure

Date: 2026-10-06

Base evidence tip before this repair:

```text
afb36cff556ebb432d8ebae69875f0feec4e0172
```

## Terminal Route Adjudication

```text
FINAL_ROUTE=SIMPLE_FORMAL_CORE
ADVANCED_INDEPENDENT_MULTI_CALL_FINALIZATION=UNSUPPORTED
```

The C11 external finalizer / OpenAI Responses API route is not adopted as a formal runtime dependency.

The formal Project Instructions Editor runtime is the ordinary ChatGPT Web / Project chat Skill contract. It must not require:

- MCP finalizer;
- `OPENAI_API_KEY`;
- hosting;
- separate API billing;
- external model provider;
- deployed model service.

The removed tracked experiment was:

```text
services/project-instructions-editor-finalizer/
tests/test_project_instructions_finalizer_service.py
tests/fixtures/project_instructions_editor/c11_f10_known_case.json
tests/fixtures/project_instructions_editor/c11_fieldops_source_omission_negative.json
```

Historical commits and evidence still preserve the experiment. The current production tree no longer carries it as a deployable/runtime dependency.

## Preserved Formal Core

The production Skill contract continues to cover:

- preservation-sensitive / greenfield / explicit reset modes;
- live baseline preservation;
- R5 protected absence;
- R6 no-op eligibility;
- source ownership and locator placement;
- authorization / privacy / safety / evidence strength;
- budget and headroom;
- natural-Chinese reading-layer consistency;
- final whole-candidate consistency pass.

The Skill no longer claims independent Stage B/C realization or raw-source verification.

## Local Validation

```text
python scripts/skills.py registry --write
PASS

python scripts/skills.py catalog --write
PASS

python scripts/audit_skill_provenance.py --write
PASS

python scripts/skills.py validate
PASS

python scripts/skills.py audit --all
PASS

python scripts/build_codex_marketplace.py --write --validate --check --path-report
PASS

python -m unittest tests.test_project_instructions_editor_contract
PASS: Ran 11 tests

python -m unittest tests.test_standalone_skill_baselines
PASS: Ran 4 tests

python -m unittest discover -s tests
PASS: Ran 339 tests
```

The first non-escalated full unittest attempt failed only because the execution sandbox could not write repo-local generated test artifacts under this exact worktree. The same suite passed when run with write access to the exact task worktree.

## Normal Web Acceptance Candidate

Suggested public-safe normal-entry prompt for real ChatGPT Web / Project chat acceptance:

```text
请检查并完善当前 ChatGPT Project 的 instructions。
目标是让长期设置清晰、精简、稳定、可维护。
自行判断是否缺规则、重复、位置不合理、不必要英文、过度实现细节或错误归属。
允许 no-op、局部修改或有限整理。
优先做最小必要修改。
```

Acceptance should use a real Project with live Project instructions visible to the model and no extra API key, hosting, MCP finalizer, or external model service. A passing response must directly use the Project Instructions Editor Skill contract in ordinary ChatGPT Web / Project chat and must not claim independent Stage B/C or raw-source verifier execution.

## Current Closure Status

```text
READY_FOR_LOCAL_REVIEW=YES
READY_FOR_WEB_USER_ACCEPTANCE=YES
REAL_CHATGPT_WEB_ACCEPTANCE=NOT_RUN_BY_CODEX
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
ISSUE_93_STATUS=DOING
```

README / CHANGELOG final reader-facing release closure and Issue #93 closure remain intentionally pending until real ChatGPT Web acceptance succeeds. Local tests must not be relabeled as that acceptance.
