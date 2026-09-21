# Critic Prompt — Workflow Identity Integration R2

You are the independent Critic for the integration/release planning package:

```text
Task: 工作流命名与插件回归机制完善（AI_Skills + Bridge）
Technical task key: cross-repo--workflow-identity-gate-lifecycle
Review stage: INTEGRATION_RELEASE_CRITIC_REVIEW_R2
Target repo: YuukiAS/AI_Skills_Collection
Planning branch: reviewed/cross-repo--workflow-identity-gate-lifecycle
```

Read latest `origin/main` and the planning branch. Do not assume the user summary is complete.

Required source locators:

```text
Prior integration Critic R1:
docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_CRITIC_REVIEW_R1_2026-09-21.md
commit: a30eec22b0337008ebde6075bf4d558e989e9cd4

Revised Integration Plan:
docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_PLAN_R2_2026-09-21.md

Revised Canonical Goal:
docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_GOAL_R2.md

Revised Kickoff Draft:
docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_KICKOFF_R2.md
```

Approved implementation tuple remains:

```text
AI_SKILLS_APPROVED_PRODUCTION_CANDIDATE=ce63f50238555849a48256068e6fa0d46e21a97b
AI_SKILLS_APPROVED_EVIDENCE_TIP=871489ee227dee773c8fff3c161bd5743da739c7
BRIDGE_APPROVED_PRODUCTION_CANDIDATE=7f2707dd4020951650d561303c82a17e22b27317
BRIDGE_APPROVED_EVIDENCE_TIP=d09306f180634aa4d4ad4ec3ee46295a8b20945b
```

This review is narrow. Review only:

1. whether `C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE` is closed;
2. whether `C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY` is closed;
3. whether this amendment introduces a direct regression in scope, authorization, production-candidate integrity, duplicate-approval handling, 056 isolation, or release/publish boundaries.

Do not reopen v2.1 architecture or implementation PASS unless this integration amendment directly contradicts the approved implementation tuple.

Specific checks:

- AI_Skills overlap audit must cover at least:
  - `README.md`;
  - `docs/workflows/PLANNER_ROLE_CONTRACT.md`;
  - `docs/workflows/CRITIC_ROLE_CONTRACT.md`;
  - `tests/test_codex_marketplace.py`.
- README resolution must preserve main's human-facing gallery/concise structure and apply candidate release values:
  - Repository `5.0.6`;
  - `workflow-core 0.2`;
  - `ai-skills-core 0.3`.
- Planner/Critic role-contract resolution must preserve current-main self-contained handoff prompt rules and candidate v1.4 semantic task-key / Gate lifecycle rules.
- Test resolution must preserve current-main human-facing plugin-gallery regression, candidate version expectations and candidate workflow-identity/Gate-lifecycle regression.
- duplicate-approval TODO commit `9d145db9d04ea366f2cd5c8ded8681a4251a4c31` must be preserved; no new duplicate Gate/rule/TODO should be required.
- The plan must use a clean temporary integration worktree from exact latest main, merge approved candidate history without rebase/squash/rewrite, run pre-push parity/focused/full tests, freeze exact integrated commit/tree, then ask the user before main push.
- The plan must treat post-main production-identity install/upgrade smoke as separately authorized and must define target, Codex identity, install/upgrade path, expected versions, side effects, restoration boundary, and network/API needs.
- Smoke failure recovery must forbid tag/release/publish/deploy and use preserved evidence plus bounded corrective/revert commit or Planner/Critic return; no reset/force/history rewrite.
- Bridge method must be exact for no-drift main and still include post-main smoke/recovery.

Return:

```text
DECISION=PASS | REVISE
COMPLEXITY=...
C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE=CLOSED|OPEN
C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY=CLOSED|OPEN
READY_FOR_INTEGRATION_EXECUTION_PACKAGE=YES|NO
READY_FOR_MAIN_MERGE=NO
READY_FOR_RELEASE=NO
START_056_NOW=NO
NEXT_HANDOFF=PLANNER|EXECUTOR
```

If `REVISE`, list only blockers tied to INT1, INT2, or direct regressions introduced by this amendment, and include a self-contained Planner prompt.
