# Frontend Design Production Consolidation — Recovery Execution-Ready Critic Prompt v0.3

你继续担任 `YuukiAS/AI_Skills_Collection` 的 Frontend Design execution-ready 独立 Critic。

当前不是重新设计 Frontend Design。Proposal v0.3 architecture 继续保持 PASS。

上一轮 recovery execution-ready review：

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`

review commit：

`d2a7dcd4c153256df1b221c3365ec9875cffd4ba`

上一轮结果：

```text
RESULT = REVISE
READY_FOR_CODEX = NO
```

上一轮只有两个 blocker：

- `FD-ER-R01 EXISTING_TASK_RECOVERY_STILL_AUTHORIZES_CREATION`
- `FD-ER-R02 V02_PACKAGE_STILL_POINTS_TO_SUPERSEDED_V01_PLAN`

本轮只复核这两个 blocker 与 v0.3 amendment 直接引入的回归。不要重新打开已关闭的 recovery 机制，不要重新审 coordinator-first、P0–P4、F-A–F-D、G1–G7、replay、maturity、版本方向或 Bridge Kit architecture。

除写入本轮唯一 durable Critic review artifact 外，保持只读：不要修改 production Skill、generator、Bridge Kit、Clear Writing、TODO、version；不要启动 Executor、创建/删除/move worktree、merge main 或创建 successor。

---

## 1. Review object

Repository:

`YuukiAS/AI_Skills_Collection`

Task key:

`web-development--frontend-design-production-consolidation`

Architecture authority:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md`

Architecture commit:

`effa02b4e7e02f012ea24bda1683857609a09fe1`

Recovery execution package version:

`v0.3`

Execution Plan:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_3_2026-09-28.md`

Canonical Goal:

`docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_3.md`

Kickoff Draft:

`docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_3.md`

Exact reviewed package commit:

`7d441a9997d6cff2e292066de202321a54bef2b8`

Exact existing task identity:

```text
task_key = web-development--frontend-design-production-consolidation
branch = reviewed/web-development--frontend-design-production-consolidation
worktree = /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation
```

Next durable review artifact that you own:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-28.md`

---

## 2. Required source reads

Read latest `AI_Skills_Collection/main`:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- approved Proposal v0.3
- Execution Plan v0.3
- Canonical Goal v0.3
- Kickoff Draft v0.3
- previous durable Critic Review v0.2

Then read latest `YuukiAS/GPT_Codex_AI_Bridge_Kit/main`:

- `AGENTS.md`
- current Reviewed Handoff spec
- current Review README
- current PLAN template
- current Review schema
- only the implementation needed to verify first-bootstrap sibling worktree, existing-task resume and PLAN freeze behavior.

Do not use old chat or old Bridge design assumptions over current source.

---

## 3. Already closed recovery points — do not reopen

The previous Critic already accepted these recovery mechanics:

1. Bridge first bootstrap canonical sibling worktree identification is correct.
2. Existing task must not second-bootstrap.
3. Existing worktree future rematerialization uses artifact-bound `materialize-worktree --mode resume`.
4. External approved package
   → GPT Planner task-local `AI_BRIDGE_REVIEWED_PLAN_V2`
   → `PLAN_REQUESTED -> PLAN_FROZEN`
   → Executor
   is the correct role/state flow.
5. Initial freeze does not consume `plan_revision`.
6. Executor must not write/freeze PLAN.
7. Durable Critic review locator is the correct minimal handoff mechanism.
8. Bridge Kit itself needs no modification.

Only reopen one of these if v0.3 directly contradicts current source and creates a concrete execution risk.

---

## 4. Blocker FD-ER-R01 closure check

Requirement:

v0.3 is existing-task recovery. It must never authorize creation of the task branch/worktree again.

Verify all three v0.3 package files:

- Plan opening no longer says Critic PASS permits creating branch/worktree.
- Goal Executor phase does not contain `创建 exact branch` or `创建 exact worktree`.
- Instead, Goal/Kickoff authorize **continuing** the recovery-preflight-adopted exact branch/worktree.
- Existing worktree loss can only route to current Bridge artifact-bound `materialize-worktree --mode resume`.
- No second bootstrap.
- No raw `git worktree add`.
- No move/remove/recreate.
- Release-baseline wording no longer says “创建 execution branch 时”.

Run a targeted search over the v0.3 Plan / Goal / Kickoff for at least:

```text
允许创建上述分支/工作树
创建 exact branch
创建 exact worktree
创建 execution branch 时
```

Any normative hit is a blocker unless it is an explicit quoted historical finding in a non-executable history section.

Do not require deletion of historical v0.1/v0.2 documents.

---

## 5. Blocker FD-ER-R02 closure check

Requirement:

v0.3 Plan / Goal / Kickoff must be one same-version execution authority.

Verify:

- Goal says final candidate must pass **Execution Plan v0.3** G1–G7.
- Kickoff generator contract says implement according to **Execution Plan v0.3**.
- Kickoff broad-regression locator points to **Execution Plan v0.3 Phase D**.
- task-local PLAN alignment points to v0.3 Plan + v0.3 Goal.
- durable review contract points to v0.3 Plan / Goal / Kickoff.

Run a targeted search over the v0.3 package for normative:

```text
Plan v0.1
Execution Plan v0.1
按 Plan v0.1
见 Plan v0.1 Phase D
```

Normative hits must be zero.

Historical text may mention v0.1 only when explicitly describing the superseded accident; it must not act as implementation/gate/validation authority.

Also check that remaining `v0.2` mentions are historical, specifically prior recovery/review evidence, not current normative execution authority.

Do not change G1–G7 product semantics merely because the package version moved.

---

## 6. Direct amendment regression check

Plan / Goal / Kickoff v0.3 must still agree on:

- task key;
- existing reviewed branch;
- canonical sibling worktree;
- `PLAN_REQUESTED -> GPT Planner V2 PLAN -> PLAN_FROZEN -> Executor`;
- no Executor self-freeze;
- durable v0.3 Critic review locator;
- allowed / forbidden scope;
- G1–G7;
- Bobbio / Lucerna / Asteria replay set only;
- Product UI Copy / Clear Writing deferred;
- no Bridge Kit modification;
- no main merge / release-ref authorization;
- version release target.

Current version baseline remains:

```text
repository = 5.3.0
web-development = 0.2
```

If that baseline remains when the existing task continues:

```text
repository = 5.3.1
web-development = 0.3
all other central plugins = NO_BUMP
maturity = unclassified
```

If a formal main release advances first, use then-current compatible PATCH and then-current next two-part web-development version.

Recovery docs themselves do not bump.

---

## 7. No architecture re-review

Do not reopen:

- frontend-visual-systems coordinator-first;
- opt-in coordinator-first aggregate generation;
- P0–P4;
- F-A/F-B/F-C/F-D;
- S1/S2/S3 + authority/surface modifiers;
- conditional Figma / no-Figma;
- browser/native evidence boundary;
- handoff action reachability product rule;
- P1/P2/P3 producer admission;
- #52/#62/#69 retained semantics;
- Bobbio/Lucerna/Asteria capability attribution;
- no fourth synthetic replay;
- maturity = unclassified;
- release version direction.

This Critic round is a control-contract parity review, not a Frontend architecture review.

---

## 8. Blocker standard

Return REVISE only if:

- FD-ER-R01 is not actually closed;
- FD-ER-R02 is not actually closed;
- the v0.3 amendment directly creates a new execution-authority contradiction;
- the package commit/path/version binding is not durable or not uniquely verifiable.

Do not create a new blocker for:

- wording preference;
- desire for another replay;
- desire for more governance metadata;
- speculative Bridge redesign;
- unrelated latest-main advance;
- already closed recovery mechanics.

Every blocker must include:

- FINDING_ID
- requirement
- direct evidence
- causal risk
- minimal closure condition
- owner

---

## 9. Required verdict and durable writeback

Return:

```text
RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO
REVIEWED_PACKAGE_VERSION = v0.3
REVIEWED_PACKAGE_COMMIT = 7d441a9997d6cff2e292066de202321a54bef2b8
```

Then write your **full actual review result** to:

`docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-28.md`

on `AI_Skills_Collection/main`.

That review artifact is the only repo mutation allowed in this Critic task.

If PASS, it must explicitly record:

```text
REVIEWED_OBJECT = Frontend Design Production Consolidation execution package
REVIEWED_PACKAGE_VERSION = v0.3
RESULT = PASS
READY_FOR_CODEX = YES
APPROVED_EXECUTION_PACKAGE_VERSION = v0.3
APPROVED_PLAN = docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_3_2026-09-28.md
APPROVED_GOAL = docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_3.md
APPROVED_KICKOFF = docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_3.md
APPROVED_TASK_KEY = web-development--frontend-design-production-consolidation
APPROVED_BRANCH = reviewed/web-development--frontend-design-production-consolidation
APPROVED_WORKTREE = /home/yuukias/AI_Skills_Collection-web-development--frontend-design-production-consolidation
APPROVED_PACKAGE_COMMIT = 7d441a9997d6cff2e292066de202321a54bef2b8
ARCHITECTURE_AUTHORITY = docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_PROPOSAL_V0_3_2026-09-27.md @ effa02b4e7e02f012ea24bda1683857609a09fe1
```

If REVISE, write the REVISE findings to the same v0.3 review path with `READY_FOR_CODEX = NO`; do not fabricate approval fields.

After writing the review artifact, report its Git commit locator.

PASS only authorizes the user to send Kickoff v0.3 to continue the **existing task**. It does not create a new task/worktree, does not itself write/freeze Bridge task-local PLAN, does not start Executor, merge main, update release ref, close TODOs or change maturity.
