# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Execution-ready Critic Review R2 v2.1

- Date: 2026-09-20
- Review role: independent Critic
- Review stage: EXECUTION_READY_PACKAGE_REVIEW_R2
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Approved Proposal: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md` v2.1
- Proposal commit: `ba2fc85f9c58b9b332eb07f821d1756b417fe1d1`
- Implementation Plan: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md`
- Canonical Goal: `docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md`
- Kickoff Draft: `docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md`
- Reviewed package commit: `1d13a6ebdc81fa8be2c3726d2025165c611ce96b`
- Prior execution Critic review: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_EXECUTION_CRITIC_REVIEW_2026-09-20.md`
- Prior Critic review commit: `9cc8731be314546ae6901e28dd35e17f73670a0c`
- Decision: **PASS**
- Complexity: **APPROPRIATE**
- READY_FOR_CODEX: **YES**
- Scope: execution-ready approval only; no execution occurs in this review

## 1. Closure

The revised package closes both execution-package findings without changing the approved v2.1 design.

### C-WIGL-E1-REMOTE-IDENTITY-PREFLIGHT — CLOSED

Plan, Goal and Kickoff now consistently require a read-only remote identity gate before any branch/worktree creation and before any fetch/push action in either repository.

The gate now:

- verifies a real local Git top level selected for the declared canonical repository;
- reads the effective `origin` fetch URL;
- reads all effective push URLs / configured `pushurl` values;
- normalizes supported GitHub HTTPS, scp-style SSH and `ssh://` forms to owner/repo identity;
- requires AI_Skills to resolve uniquely to `YuukiAS/AI_Skills_Collection`;
- requires Bridge to resolve uniquely to `YuukiAS/GPT_Codex_AI_Bridge_Kit`;
- fails before mutation on extra push destination, mismatch, missing origin, unsupported/ambiguous identity;
- forbids remote remapping or Git config edits to make the gate pass;
- introduces no registry/state/schema/controller.

This is aligned with Git's own remote model: `remote.<name>.pushurl` overrides the normal remote URL for push, and multiple configured push URLs are all push destinations. Inspecting the complete effective push destination set is therefore the correct bounded safety check.

### C-WIGL-E2-REPLAY-COUNT-SEMANTICS — CLOSED

Plan, Goal and Kickoff now consistently define exactly two fixed replay **scenarios**, not a total invocation cap:

1. Verified Workflow;
2. AI Skills Maintainer.

Each scenario input/intent is frozen before first run. A failed fixed scenario may be rerun only after a concrete bounded in-scope repair to the frozen architecture. No third scenario/new input, adaptive winner search, blind rerun or run-until-PASS is allowed. Replay reruns are explicitly not a paid-call budget. Repeated failure that requires changing Gate taxonomy, ownership, parser responsibility or state/recovery semantics returns to Planner/Critic.

No replay counter/ledger or arbitrary retry budget was added.

## 2. Direct regression check

The R2 amendment does not change:

- technical task key;
- human-readable name;
- cutover bootstrap;
- two-repository scope;
- G1–G7;
- `BROAD_FULL_FALLBACK`;
- final candidate tuple semantics;
- current version slots;
- 056 non-concurrency/stale-slot rule;
- paid/private/Host boundaries;
- integration/release prohibitions;
- no-governance-bloat constraints;
- docs layout deferral.

The revised package files at commit `1d13a6eb...` are unchanged on latest main except for later Critic-prompt documentation.

## 3. Complexity

`COMPLEXITY=APPROPRIATE`

The package is sufficiently strict to prevent wrong-repository push and replay sample chasing, while still avoiding new Git provenance infrastructure or replay-control machinery.

## 4. Decision

```text
APPROVED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
APPROVED_PLAN_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md
APPROVED_GOAL_PATH=docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md
APPROVED_PACKAGE_COMMIT=1d13a6ebdc81fa8be2c3726d2025165c611ce96b
DECISION=PASS
COMPLEXITY=APPROPRIATE
C-WIGL-E1-REMOTE-IDENTITY-PREFLIGHT=CLOSED
C-WIGL-E2-REPLAY-COUNT-SEMANTICS=CLOSED
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

This PASS approves only the reviewed execution package. It does not itself create branches/worktrees, mutate production, run replay/tests, use paid APIs, merge/release/deploy, or authorize any scope beyond the verbatim approved Kickoff once the user sends it.
