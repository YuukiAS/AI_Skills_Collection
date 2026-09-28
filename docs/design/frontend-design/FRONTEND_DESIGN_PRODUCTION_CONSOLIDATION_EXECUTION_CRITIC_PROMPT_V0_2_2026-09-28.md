# Frontend Design Production Consolidation — Recovery Execution-Ready Critic Prompt v0.2

你继续担任 `YuukiAS/AI_Skills_Collection` 的 Frontend Design execution-ready 独立 Critic。

当前不是重新设计 Frontend Design，也不是重新审 Proposal v0.3。v0.3 architecture 已 PASS，v0.1 execution package 也曾 execution-ready PASS；本轮只审 v0.2 recovery 是否正确修复 Bridge normal-entry 对齐事故。

除创建/更新本轮唯一 durable Critic review artifact 外，保持只读：不要修改 production Skill、generator、Bridge Kit、Clear Writing、TODO、version，不创建 task/worktree，不启动 Executor，不 merge/release。

---

## 1. Review object

Repository:

`YuukiAS/AI_Skills_Collection`

Task:

`web-development--frontend-design-production-consolidation`

Architecture authority:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md`

Architecture commit:

`effa02b4e7e02f012ea24bda1683857609a09fe1`

Recovery execution package:

- Plan: `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_2_2026-09-28.md`
- Goal: `docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_2.md`
- Kickoff: `docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_2.md`

Exact reviewed package commit:

`3d8669f52680f63f76ce537335fbee6019e4d5a9`

Individual creation locators:

- Plan: `f07caef2b7d62228fe3a8f7a097ecc3a1f18b0b5`
- Goal: `0dc555a1b711756b0db4eade2b724f3c95a5413e`
- Kickoff/package tip: `3d8669f52680f63f76ce537335fbee6019e4d5a9`

Durable review artifact you own:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`

---

## 2. First read current authority

Read latest `AI_Skills_Collection/main`:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- Proposal v0.3
- Plan v0.2
- Goal v0.2
- Kickoff v0.2

Then read latest `YuukiAS/GPT_Codex_AI_Bridge_Kit/main`:

- `AGENTS.md`
- `docs/V0_5_REVIEWED_HANDOFF_IMPLEMENTATION_SPEC.md`
- `templates/reviewed_handoff/README.md`
- `templates/reviewed_handoff/templates/PLAN.md`
- `templates/reviewed_handoff/schema.json`
- relevant current `ai_bridge_kit/reviewed_handoff.py` implementation for:
  - `task bootstrap`
  - `_repo_local_bootstrap_worktree`
  - `materialize-worktree --mode resume`
  - `PLAN_REQUESTED / RUN_GPT_PLANNER`
  - `AI_BRIDGE_REVIEWED_PLAN_V2`
  - `PLAN_REQUESTED -> PLAN_FROZEN`

Do not rely on old Bridge design docs when current shipped source/spec says otherwise.

Do one minimal external reality check if useful; do not use it to reopen Frontend architecture.

---

## 3. Incident facts and recovery target

The first v0.1 Kickoff has already been sent to Codex.

Observed task state from the execution machine:

```text
task_key = web-development--frontend-design-production-consolidation
branch = reviewed/web-development--frontend-design-production-consolidation
worktree = /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation
CURRENT.state = PLAN_REQUESTED
CURRENT.next_action = RUN_GPT_PLANNER
```

Codex has not begun Frontend implementation.

v0.1 had three control-plane errors:

1. it froze a caller-chosen `/tmp` worktree even though current Bridge first bootstrap fixes a sibling worktree;
2. it did not explain how an externally approved execution package becomes Bridge task-local V2 PLAN and then PLAN_FROZEN without Executor impersonating Planner;
3. previous execution-ready PASS had no durable repo review artifact.

v0.2 must fix only these three things.

---

## 4. Recovery finding R1 — worktree

Check current Bridge source independently.

Expected conclusion if source matches Planner reading:

- first bootstrap derives `reviewed/<task_key>`;
- sibling worktree is `<repo-parent>/<repo-dir>-<task_key>`;
- for canonical checkout `/home/yuukias/AI_Skills_Collection`, the incident sibling path is exactly:
  `/home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation`;
- existing task artifacts should be resumed/adopted, not second-bootstrapped;
- later rematerialization uses artifact-bound `materialize-worktree --mode resume`;
- wrong base/path/lineage/dirty ownership fails closed.

Review whether Plan/Goal/Kickoff correctly:

- abandon v0.1 `/tmp` authority;
- adopt the existing sibling worktree only after local recovery preflight;
- do not falsely claim Planner GitHub surface independently inspected machine-local cleanliness;
- prohibit move/remove/recreate/reset/clean destructive recovery;
- prohibit second first-bootstrap.

Do not require a Bridge Kit code change if shipped behavior already supports this.

---

## 5. Recovery finding R2 — task-local PLAN

Check that current Bridge really initializes a new task as:

`PLAN_REQUESTED / RUN_GPT_PLANNER`.

Check current V2 freeze contract.

v0.2 freezes authority as:

```text
approved Proposal/Execution Plan/Goal + durable Critic PASS
→ GPT Planner writes task-local AI_BRIDGE_REVIEWED_PLAN_V2
→ Planner re-reads current template and self-checks
→ Planner writes CURRENT last:
   PLAN_REQUESTED -> PLAN_FROZEN
   next_action = RUN_CODEX_EXECUTOR
→ Executor starts
```

Review whether this correctly preserves role authority:

- task-local PLAN is a runtime translation, not a second architecture;
- it cannot weaken/expand canonical package;
- it carries Positive completion / Non-substitutable semantics / G1–G7 / scope / replay / version;
- initial freeze does not consume plan_revision;
- Executor does not create/freeze PLAN;
- if branch metadata is not yet remote, Codex may publish only REQUEST/CURRENT control metadata and then stop for Planner.

Any proposed alternative must be justified by current Bridge source, not preference.

---

## 6. Recovery finding R3 — durable execution-ready PASS

Review the fixed locator:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`

The goal is simple: after your review, Codex must be able to inspect the repository and establish whether this exact package is approved.

The review artifact must contain, at minimum:

```text
REVIEWED_OBJECT = Frontend Design Production Consolidation execution package
REVIEWED_PACKAGE_VERSION = v0.2
RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO
REVIEWED_PACKAGE_COMMIT = 3d8669f52680f63f76ce537335fbee6019e4d5a9
APPROVED_PLAN = <v0.2 Plan path if PASS>
APPROVED_GOAL = <v0.2 Goal path if PASS>
APPROVED_KICKOFF = <v0.2 Kickoff path if PASS>
APPROVED_TASK_KEY = web-development--frontend-design-production-consolidation
APPROVED_BRANCH = reviewed/web-development--frontend-design-production-consolidation
APPROVED_WORKTREE = /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation
ARCHITECTURE_AUTHORITY = Proposal v0.3 @ effa02b4e7e02f012ea24bda1683857609a09fe1
```

Also preserve your actual reasoning and any non-blocking notes.

This is ordinary Markdown review evidence. Do not create schema, ledger, database, hash graph, new workflow or Bridge change.

Planner must not write your verdict for you.

---

## 7. Package parity

Plan / Goal / Kickoff v0.2 must agree on:

- task key;
- reviewed branch;
- sibling worktree;
- existing-task recovery path;
- no second bootstrap;
- PLAN_REQUESTED -> Planner V2 PLAN -> PLAN_FROZEN;
- durable Critic review locator;
- allowed/forbidden scope;
- G1–G7;
- Bobbio/Lucerna/Asteria only;
- Product UI Copy / Clear Writing deferred;
- version target;
- no main merge / release-ref authorization.

Only real semantic mismatch is blocker. Editorial differences are not.

---

## 8. Do not reopen product architecture

Do not reopen:

- coordinator-first;
- P0–P4;
- F-A/F-B/F-C/F-D;
- S1/S2/S3;
- generator design;
- #52/#62/#69 semantics;
- handoff action reachability product rule;
- Bobbio/Lucerna/Asteria attribution;
- no fourth synthetic replay;
- maturity = unclassified;
- release direction.

G1–G7 product semantics should be identical to v0.1; only recovery/control mechanics may differ.

---

## 9. Version check

Current main at package preparation still has:

```text
Repository = 5.3.0
web-development = 0.2
```

If implementation kickoff base remains this:

```text
Repository release = 5.3.1
web-development = 0.3
all other central plugins = NO_BUMP
maturity = unclassified
```

If main has an intervening formal release, apply current version policy:

- repository = then-current compatible PATCH;
- web-development = then-current next two-part version.

v0.2 recovery docs themselves do not bump. There is no legal “completed production implementation but NO_BUMP” path.

---

## 10. Permissions

This recovery package must still forbid:

- Frontend production implementation before PLAN_FROZEN;
- Bridge Kit modification;
- Clear Writing modification;
- Product UI Copy expansion;
- version bump during recovery itself;
- closing #52–#72;
- merge to main;
- release ref update;
- destructive Git;
- deletion/move/recreation of existing task worktree;
- successor task.

After legal PLAN_FROZEN, original reviewed-branch Executor scope resumes exactly as approved; integration still requires later authorization.

---

## 11. Blocker standard

REVISE only for a real recovery risk, for example:

- sibling worktree recovery contradicts current Bridge;
- task-local PLAN authority is ambiguous enough that Executor could self-authorize;
- branch metadata publication could accidentally start implementation;
- durable review locator cannot prove this exact package was approved;
- Plan/Goal/Kickoff disagree materially;
- recovery silently changes Frontend architecture or release target.

Do not REVISE because:

- you prefer another docs filename;
- a fourth replay feels safer;
- worktree could theoretically live elsewhere;
- the prior architecture could be redesigned better;
- more governance metadata could be added.

Each blocker must include:

- FINDING_ID
- requirement
- direct evidence
- causal risk
- minimal closure condition
- owner

---

## 12. Required final action

Return:

```text
RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO
REVIEWED_PACKAGE_VERSION = v0.2
REVIEWED_PACKAGE_COMMIT = 3d8669f52680f63f76ce537335fbee6019e4d5a9
```

Then **write your full review result** to:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`

on `AI_Skills_Collection/main`.

That review artifact is the only allowed repo mutation in this Critic task.

If PASS, it must explicitly include:

```text
RESULT = PASS
READY_FOR_CODEX = YES
APPROVED_EXECUTION_PACKAGE_VERSION = v0.2
APPROVED_PLAN = docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_2_2026-09-28.md
APPROVED_GOAL = docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_2.md
APPROVED_KICKOFF = docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_2.md
APPROVED_TASK_KEY = web-development--frontend-design-production-consolidation
APPROVED_BRANCH = reviewed/web-development--frontend-design-production-consolidation
APPROVED_WORKTREE = /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation
APPROVED_PACKAGE_COMMIT = 3d8669f52680f63f76ce537335fbee6019e4d5a9
ARCHITECTURE_AUTHORITY = docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md @ effa02b4e7e02f012ea24bda1683857609a09fe1
```

If REVISE, write the REVISE findings to the same durable path with `READY_FOR_CODEX = NO`; do not fabricate approval fields.

After writing the review artifact, report its Git commit locator.

PASS authorizes the user to send Kickoff v0.2 for **existing-task recovery**. It does not itself create/freeze task-local PLAN, start Executor, merge main, update release ref, close TODOs, or change maturity.
