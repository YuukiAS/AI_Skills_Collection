# Project Instructions Editor — Implementation Goal v0.1

Status: DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
Task key: `project-instructions-editor--standalone-skill-implementation`  
Implementation Plan: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md`

## Goal

Implement and validate the frozen standalone Skill `project-instructions-editor` without redesigning the approved product contract.

The Executor must deliver one final candidate that:

1. exists at `skills/core/codex-system/project-instructions-editor/`;
2. naturally triggers for long-lived ChatGPT Project-instruction editing requests;
3. preserves the frozen near-miss ownership boundaries;
4. implements preservation-sensitive / greenfield / explicit-reset modes;
5. handles live setting, targeted history, canonical sources, character budget, missing-input degradation, semantic ownership/effective enforcement, locator safety, protected absence, bounded/full edit and no-op;
6. produces proportional user-facing edits/candidates rather than audit-heavy output;
7. passes the four frozen capability families on the same final candidate;
8. is source/generated/provenance/install/version/README/changelog consistent as a standalone Skill release candidate;
9. is packaged for independent review;
10. stops before `main` merge or formal release publication.

## Frozen product authority

Do not redesign:

- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`
- `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_DESIGN_FREEZE_CLOSURE_2026-10-02.md`

If implementation evidence contradicts these contracts, return to Planner/Critic.

## Exact implementation identity

```text
repository = YuukiAS/AI_Skills_Collection
task_key = project-instructions-editor--standalone-skill-implementation
branch = work/project-instructions-editor--standalone-skill-implementation
worktree = ../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation
```

## Required source

Create:

```text
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/agents/openai.yaml
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
skills/core/codex-system/project-instructions-editor/evals/trigger_queries.json
skills/core/codex-system/project-instructions-editor/assets/app-facing.svg
tests/test_project_instructions_editor_contract.py
```

Update `tests/test_standalone_skill_baselines.py`.

Do not create runtime scripts unless a new Planner/Critic decision explicitly authorizes changing the frozen instruction-only capability.

## Required metadata

The standalone Skill starts at version `0.1`.

Capability identity:

```text
provenance = user-authored
trusted = false
requires_network = false
writes_files = false
executes_code = false
secrets_needed = []
recommended_scope = global
```

Natural invocation must be allowed. Static trigger metadata alone is not Gate PASS.

## Positive completion

The implementation is positively complete only when a normal installed fresh Codex session can use the final candidate on realistic Project-instruction editing tasks and the resulting complete setting/edit/no-op demonstrates the frozen semantics.

Tests, registry/catalog generation, character counts, diff output, trigger receipts, file existence and CI are necessary evidence where relevant but cannot by themselves establish product completion.

Maximum Executor claim:

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

The Executor may not claim release/publication completion.

## Non-substitutable semantics

Do not replace or weaken:

- bounded edit as default;
- three edit modes;
- live-baseline requirement for preservation-sensitive full replacement;
- targeted history, not exhaustive history;
- protected absence;
- semantic ownership versus effective enforcement;
- Project-resident bridge when lookup-before-action semantics require it;
- no-op as valid;
- missing-input honest degradation;
- exact identifier protection;
- authorization/safety/evidence-strength preservation;
- natural normal entry and near-miss owners;
- full-output qualitative review.

Do not substitute blacklist/rule-count/English-ratio/keyword scoring for semantic judgment.

## Capability gates

### G1 — Normal entry / routing

Use an actual installed final candidate in a fresh normal Codex session. Natural prompts must trigger the Skill without naming it, while near-miss tasks stay with their frozen owners.

### G2 — Core editing semantics

Exercise the three modes, missing inputs, ownership/enforcement, locator, protected absence, budget, bounded/full/no-op using real historical repo evidence and public-safe equivalents.

### G3 — Fidelity / authority / should-not-change

Directly compare baseline/source/output for authorization, safety, mandatory/optional, evidence strength, uncertainty, exact identifiers, deletions/corrections and unrelated scope.

### G4 — Representative complete task + qualitative final artifact

Use the same final candidate on complete representative Project settings. Freeze source/ref. An independent Reviewer must read full inputs and full output; deterministic proxies are insufficient. Fresh evidence is risk-matched and not fixed-count.

A–L are regression/task families, not Gate count.

## Validation

At minimum run the current repository equivalents of:

```bash
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_project_instructions_editor_contract
python -m unittest tests.test_standalone_skill_baselines
python -m unittest discover -s tests
```

Also perform a task-local standalone install and fresh-session normal-entry verification.

## Release-candidate closure

Planning version decision:

```text
Repository bump decision: MINOR
Expected if origin/main remains 5.4.0: 5.4.0 -> 5.5.0
Affected central plugins: all NO_BUMP
project-instructions-editor standalone version: 0.1
```

If `origin/main:VERSION` changes before release-candidate metadata is written, stop that portion with `VERSION_DRIFT` and return to Planner.

Update README standalone card, root CHANGELOG, VERSION/parity sources, registry/catalog/provenance and standalone baseline evidence. Do not add a central Plugin or profile.

## Evidence

Write public-safe evidence under:

```text
results/project-instructions-editor--standalone-skill-implementation/
```

Required:

```text
RESULT.md
MANIFEST.md
G1_NORMAL_ENTRY.md
G2_CORE_SEMANTICS.md
G3_FIDELITY.md
G4_COMPLETE_TASK_REVIEW.md
```

Generate:

```text
private/exports/project-instructions-editor-v0.1.zip
```

with only the Skill runtime directory, and record SHA-256/file list in MANIFEST.

## Privacy and source safety

Do not commit private ChatGPT Project threads or private Project settings. Use already public repo evidence and public-safe fixtures/equivalents.

No paid API/model review is authorized.

## Stop point

Commit and ordinary non-force push the exact task branch after all pre-review evidence is complete.

Stop at:

```text
FINAL_CANDIDATE_READY_FOR_INDEPENDENT_REVIEW=YES
```

Do not merge `main`, advance `release`, tag, publish, create a GitHub Release, create a Plugin wrapper, or claim repository `5.5.0` is released.

```text
READY_FOR_CODEX=NO
```
