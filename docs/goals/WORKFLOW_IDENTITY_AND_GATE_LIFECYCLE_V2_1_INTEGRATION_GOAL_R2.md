# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Integration Canonical Goal R2

- Goal version: `integration-r2`
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Plan: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_PLAN_R2_2026-09-21.md`
- Prior integration Critic R1: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_CRITIC_REVIEW_R1_2026-09-21.md`
- Scope: integration/release planning only

## Goal

Prepare an execution-ready integration/release package for the approved v2.1 implementation tuple without changing the approved production candidates.

Approved tuple:

```text
AI_SKILLS_MAIN_FOR_PRODUCTION_DRIFT=0a38519ed051cf01503ba3ed02b5a33b787b9c99
AI_SKILLS_APPROVED_PRODUCTION_CANDIDATE=ce63f50238555849a48256068e6fa0d46e21a97b
AI_SKILLS_APPROVED_EVIDENCE_TIP=871489ee227dee773c8fff3c161bd5743da739c7
BRIDGE_MAIN=afb2414b6fbe4b2b03292d3b1437d4dd22277fd0
BRIDGE_APPROVED_PRODUCTION_CANDIDATE=7f2707dd4020951650d561303c82a17e22b27317
BRIDGE_APPROVED_EVIDENCE_TIP=d09306f180634aa4d4ad4ec3ee46295a8b20945b
```

The package is complete only when it explains how to:

1. preserve AI_Skills current-main README/refactor/review/TODO work;
2. merge approved candidate history without rebase, squash, cherry-pick rewrite, reset or force;
3. resolve the four known AI_Skills overlap files from the real merge base:
   - `README.md`;
   - `docs/workflows/PLANNER_ROLE_CONTRACT.md`;
   - `docs/workflows/CRITIC_ROLE_CONTRACT.md`;
   - `tests/test_codex_marketplace.py`;
4. keep Bridge integration exact and non-destructive;
5. run pre-push source/generated/version/changelog parity and focused/full tests;
6. freeze exact integrated commit/tree before any main push;
7. request separate user authorization for merge/push main;
8. run separately authorized production-identity install/upgrade smoke after main push;
9. define smoke failure recovery without reset, force push or history rewrite;
10. keep tag/release/publish/deploy as a later separately authorized phase.

## Hard Boundaries

Do not:

- redesign v2.1;
- modify production candidates;
- create a successor task;
- create new branches/worktrees during planning;
- merge main;
- tag, release, publish or deploy;
- run paid API;
- start or modify 056;
- add another duplicate-approval rule, Gate or same-meaning TODO.

`START_056_NOW=NO`.

## Success Criteria

This planning round succeeds when:

- the Integration Plan R2 explicitly closes `C-WIGL-INT1-MAIN-DRIFT-OVERLAP-COVERAGE`;
- the Integration Plan R2 explicitly closes `C-WIGL-INT2-MAIN-AS-PRODUCTION-RECOVERY`;
- the Kickoff Draft names exact smoke target, Codex identity, install/upgrade path, expected versions, side effects, restoration boundary, network/API boundary, and separate authorization points;
- the next Critic prompt asks Critic to review only INT1, INT2 and direct regressions introduced by this amendment;
- no production/source/generated candidate files are changed.

## Next Owner

```text
NEXT_OWNER=INTEGRATION_RELEASE_CRITIC_REVIEW_R2
READY_FOR_MAIN_MERGE=NO
READY_FOR_RELEASE=NO
START_056_NOW=NO
```
