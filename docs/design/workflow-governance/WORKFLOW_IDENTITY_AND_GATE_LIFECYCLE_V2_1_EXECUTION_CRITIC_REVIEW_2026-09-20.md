# 工作流命名与插件回归机制完善（AI_Skills + Bridge）— Execution-ready Critic Review v2.1

- Date: 2026-09-20
- Review role: independent Critic
- Review stage: EXECUTION_READY_PACKAGE_REVIEW
- Human-readable name: **工作流命名与插件回归机制完善（AI_Skills + Bridge）**
- Technical task key: `cross-repo--workflow-identity-gate-lifecycle`
- Approved Proposal: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md` v2.1
- Proposal commit: `ba2fc85f9c58b9b332eb07f821d1756b417fe1d1`
- Implementation Plan: `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md` v2.1
- Canonical Goal: `docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md` v2.1
- Kickoff Draft: `docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md` v2.1
- Package content commit: `0f2b9adb3f00e520ca18c941c37c20a04e2111e8`
- AI_Skills latest main checked: `93250206646c615d770161b54e83f0ed600d6945`
- Bridge latest main checked: `afb2414b6fbe4b2b03292d3b1437d4dd22277fd0`
- Decision: **REVISE**
- Complexity: **APPROPRIATE**
- Scope: execution-package review only; no implementation authorization

## 1. Overall judgment

The execution package is substantially faithful to the approved v2.1 design.

It correctly keeps Bridge limited to lexical/legacy compatibility, canonical semantic creation, generic validation and identity propagation; keeps AI_Skills responsible for scope semantics and Gate lifecycle; keeps workflow-core out of task-key parsing; preserves domain-plugin ownership; preserves 001–057; retains G1–G7 and same-final-candidate; pre-classifies this cross-cutting change as `BROAD_FULL_FALLBACK`; keeps human labels separate from technical locators; and does not add a registry, database, ledger, controller, watcher, state machine, title service or docs-layout migration.

The one-time cutover bootstrap is also legitimate. The current Bridge canonical task initializer still rejects semantic keys, so this implementation cannot honestly create itself through the post-change semantic task normal entry. Using the Critic-approved Plan/Goal/Kickoff plus two exact semantic Git branches, then proving the new normal entry only in isolated fixture repositories after the candidate exists, avoids both a fake semantic CURRENT and an unnecessary numeric successor. The first ordinary production semantic task remains post-integration/release work.

The proposed branch `reviewed/cross-repo--workflow-identity-gate-lifecycle` is compatible with Git ref naming rules: its slash/hyphen structure does not use any of Git's prohibited ref patterns. The package does not need another branch naming mechanism.

Two execution-package defects remain. Both are narrow and can be fixed without reopening the approved architecture.

## 2. Design closure remains intact

The prior design findings remain closed:

- `C-WIGL-01-SCOPE-PRECEDENCE = CLOSED`
- `C-WIGL-02-IMPACT-FALLBACK-BOUNDARY = CLOSED`
- `C-WIGL-03-IDENTITY-CUTOVER-COVERAGE = CLOSED`
- `C-WIGL-04-HUMAN-READABLE-WORKFLOW-LABEL = CLOSED`

No package change reviewed here justifies reopening them.

## 3. Package fidelity and normal-entry review

### Bridge scope

The planned Bridge changes are proportionate:

- one canonical task-key lexical authority;
- semantic-only canonical new creation;
- legacy + semantic existing-workspace validation;
- propagation through task/result/control/review/text/visual/runner consumers;
- minimum authoring-doc updates;
- focused and full regression tests.

It explicitly forbids AI_Skills semantic ownership in Bridge and does not change Review states/schema/roles.

### AI_Skills scope

The package correctly maps the approved design into actual consumers rather than leaving it only in policy prose:

- Gate lifecycle in `PLUGIN_CAPABILITY_GATE_POLICY.md`;
- minimal repository/Planner/Critic consumer rules;
- workflow-core execution semantics and reusable task authoring guidance;
- AI Skills Maintainer regression/scope/release maintenance behavior;
- generated plugin parity;
- candidate plugin replay.

It does not alter domain-plugin professional behavior.

### G1–G7

The acceptance mapping is sufficient in principle:

- G1 uses candidate Bridge canonical CLI normal entry;
- G2 covers all mandatory identity surfaces, including Text/Visual Review and task-bound consumers;
- G3 and G5 use the installed/generated AI Skills Maintainer candidate rather than policy text alone;
- G4 proves legacy + semantic coexistence;
- G6 uses this task itself as broad/full and also proves narrow-vs-fallback semantics through Verified Workflow;
- G7 checks the actual diff for governance bloat.

Two fixed candidate replay **scenarios** are sufficient to cover the independent AI_Skills runtime claims: Verified Workflow owns release-selection execution, while AI Skills Maintainer owns scope/regression triage. More scenarios are not justified.

### Version and 056 overlap

Current source confirms:

- AI_Skills repository `5.0.5`;
- workflow-core `0.1`;
- ai-skills-core `0.2`;
- Bridge `0.8.3`;
- current 056 remains awaiting execution-package Critic review and overlaps workflow-core / ai-skills-core / Bridge.

The proposed AI_Skills repository patch plus two plugin version bumps are consistent with the repository policy: this is a compatible improvement inside the existing collection workflow, while workflow-core and ai-skills-core each gain a user-observable production behavior batch.

Bridge `0.8.4` is a compatible next candidate within its current 0.8.x line and is protected by the stale-slot rule. If 056 or another task consumes overlapping source/version slots first, the Executor must stop before mutation rather than inventing later versions.

The no-concurrency rule with 056 is correct and must stay.

## 4. Blocking findings

### C-WIGL-E1-REMOTE-IDENTITY-PREFLIGHT

**Requirement / contract**

Execution authorization is bound to exactly two canonical repositories:

- `YuukiAS/AI_Skills_Collection`
- `YuukiAS/GPT_Codex_AI_Bridge_Kit`

The package authorizes creation and ordinary non-force push of a new exact reviewed branch in each repository. Current project rules require repository/remote identity to be verified from the actual environment rather than inferred from a local folder name or a remote called `origin`.

**Observed package**

Plan/Goal/Kickoff require a kickoff-time “verified compatible `origin/main`” source/version preflight, but they do not explicitly require checking the effective canonical fetch destination and all effective push destinations before branch creation/push.

The recent 057 integration recovery established the concrete failure mode: a remote name alone does not prove push destination identity because fetch URL and one or more push URLs can differ.

**Causal risk**

The package could be semantically correct and still create/push the approved branch to the wrong repository or an extra configured push destination. Because this execution spans two repositories and creates new remote branches, destination identity is part of the authorization boundary, not a cosmetic Git check.

**Minimum closure**

Without adding any registry/state:

1. before branch/worktree creation and before any fetch/push mutation, perform a read-only remote identity gate in each repository;
2. confirm the current local Git repository is the intended canonical repo;
3. inspect effective `origin` fetch URL and **all** effective push URLs / pushurl values;
4. normalize equivalent GitHub SSH/HTTPS forms and require every effective destination to resolve only to the declared `YuukiAS/<repo>`;
5. extra destination, mismatch or ambiguity -> stop before mutation and return to Planner/user as appropriate;
6. explicitly forbid remote remap / `git remote set-url` / Git-config rewrite to make the check pass.

This should be a small Preflight/Kickoff addition only. Do not create a remote registry or controller.

**Owner**

Planner, in Plan + Goal + Kickoff alignment.

### C-WIGL-E2-REPLAY-COUNT-SEMANTICS

**Requirement / contract**

The package must bound candidate replay cost/time while still allowing a legitimate defect found by a frozen replay case to be repaired and re-tested. It must also prohibit adaptive sample chasing.

**Observed package**

Plan/Goal/Kickoff use both of these statements:

- “at most two / 最多两次 candidate plugin replay”; and
- if one replay fails, repair within frozen architecture and rerun the affected replay.

Taken literally, the first is a total invocation cap of two, while the second can require a third invocation after a valid repair.

The intended architecture is otherwise clear: there are two fixed public-safe **replay scenarios**, not an open-ended sample search.

**Causal risk**

Executor can either stop prematurely after a repair because the two-call wording was exhausted, or exceed the stated authorization because a rerun seems allowed. This is an avoidable execution-contract ambiguity.

**Minimum closure**

Make Plan/Goal/Kickoff say one thing consistently:

- exactly **two fixed replay scenarios/cases** are authorized: Verified Workflow and AI Skills Maintainer;
- each scenario may be rerun only after a concrete bounded repair to the frozen architecture;
- no additional/new replay scenario may be added adaptively;
- no “run until PASS” behavior;
- replay reruns are local/public-safe and not a paid-call budget;
- if repeated failure indicates architecture/ownership/Gate semantics must change, stop and return to Planner/Critic.

Do not introduce a replay ledger or fixed arbitrary retry count unless a real runtime constraint requires one.

**Owner**

Planner, in Plan + Goal + Kickoff alignment.

## 5. Non-blocking observations

1. The current `candidate_plugin_replay.py` path is adequate for the two AI_Skills runtime claims: it stages the exact committed generated plugin, adds it under a temporary candidate marketplace, launches a fresh Codex child, verifies actual SKILL consumption, removes the candidate and verifies the production same-name plugin identity was preserved. No Terra/OpenAI Responses call is required.
2. If the pinned candidate replay runtime is missing at execution time, the package should use the existing bounded replay setup path or report the infrastructure prerequisite truthfully; it must not silently broaden provider/data scope. This does not require an architecture change.
3. No plugin TODO update is required merely for audit trail. The allowed TODO scope should be used only if execution reveals a genuine unresolved maintenance item; otherwise leave TODOs unchanged.
4. Final release closure remains later work. Candidate replay is pre-release evidence and does not by itself substitute for any final released/production-identity install/upgrade smoke required by the then-current release contract.

## 6. Complexity

`COMPLEXITY=APPROPRIATE`

The package is not too simple: it reaches canonical creation/validation, installed/generated plugin consumers, all G1–G7 evidence, full regressions and exact cross-repo candidate identity.

It is not too complex: no new control infrastructure, identity registry, display-name model, Gate registry or paid matrix is introduced.

The two blockers above reduce execution ambiguity and destination risk without changing architecture.

## 7. Decision

```text
REVIEWED_PROPOSAL_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md
REVIEWED_PROPOSAL_VERSION=v2.1
REVIEWED_PLAN_PATH=docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md
REVIEWED_GOAL_PATH=docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md
REVIEWED_KICKOFF_PATH=docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md
REVIEWED_PACKAGE_COMMIT=0f2b9adb3f00e520ca18c941c37c20a04e2111e8
DECISION=REVISE
COMPLEXITY=APPROPRIATE
C-WIGL-01=CLOSED
C-WIGL-02=CLOSED
C-WIGL-03=CLOSED
C-WIGL-04=CLOSED
BLOCKERS=C-WIGL-E1-REMOTE-IDENTITY-PREFLIGHT,C-WIGL-E2-REPLAY-COUNT-SEMANTICS
NON_BLOCKING=TODO_ONLY_IF_REAL_UNRESOLVED_ITEM;FINAL_PRODUCTION_IDENTITY_SMOKE_REMAINS_LATER_RELEASE_CLOSURE
READY_FOR_CODEX=NO
NEXT_HANDOFF=PLANNER
```

This REVISE does not reopen the approved design. It requires only a narrow execution-package amendment.
