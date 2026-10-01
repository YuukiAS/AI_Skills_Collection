# workflow-core 0.5 — Execution-ready Critic Re-review Prompt v0.2

你继续作为 AI Research Stack 的独立 Critic thread，对 `workflow-core / Verified Workflow 0.5` execution package 做复核。

这是 `EXECUTION_READY_REVIEW_R2`。  
不要实现代码，不要修改 production source，不要创建 branch/worktree，不要启动 paid API。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `workflow-core`
- design_topic_or_task_key: `workflow-core--normal-entry-reliability`
- source_branch_or_ref: `main`
- review_stage: `EXECUTION_READY_REVIEW_R2`
- approved design: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md`
- approved design commit: `de66a18123059f76fd0ead4aa715f84ad066c62b`
- revised Plan: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_2_2026-10-01.md`
- revised Goal: `docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_2_2026-10-01.md`
- revised Kickoff: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_2_2026-10-01.md`
- exact package commit containing Proposal + Plan + Goal + Kickoff: `c7fb7488d3847855609d86fb0307bfeea824e078`
- previous package commit: `a649bdd5ebd75fb36f84206d692938a08d3028c1`
- previous result: `REVISE`
- open blockers to re-check first: `WC05-ER1`, `WC05-ER2`
- design findings `WC05-D1`–`WC05-D7`: CLOSED
- implementation state: `NOT STARTED`

只审 package commit `c7fb7488d3847855609d86fb0307bfeea824e078`。其余上一轮已通过内容只有新版直接引入回归时才能重新打开。

## 必须读取

从最新 main 读取当前 rules：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

从 package commit 读取：

- approved Proposal V0.4
- Execution Plan V0.2
- Canonical Goal V0.2
- Kickoff Draft V0.2

Reviewed Handoff 必须独立核对 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 当前 main：

- `AGENTS.md`
- `templates/reviewed_handoff/schema.json`
- `templates/reviewed_handoff/README.md`
- `templates/reviewed_handoff/prompts/PLANNER.md`
- `templates/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- `templates/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md`
- `ai_bridge_kit/reviewed_handoff.py` 中 task bootstrap / task init / publish-first / human record 相关实现。

## 优先复核 WC05-ER1

上一 package 的问题是：单一 Reviewed task 无法合法表达“development candidate -> AI Research Stack pre-final Critic -> 无 finding 恢复 Executor继续 final qualification”。

V0.2 改成两个**串行** Reviewed tasks，同一总体 Goal、同一 candidate lineage，但不新增 Bridge state/workflow。

### ER1-A — 四个 owner 是否清楚

确认以下 owner 不互相冒充：

- AI Research Stack Planner：package authority + Bridge Planner transaction；
- AI Research Stack Critic：Stage A pre-final + Stage B final，只读，不改 CURRENT；
- Reviewed Handoff Reviewer：真实 GitHub CI + Reviewer transaction；
- Codex Executor：实现 frozen Stage PLAN并合法交棒。

Critic不能代 Reviewer推进 `WAITING_FOR_CI`；Executor不能写 Reviewer decision；Reviewer不能拿假 `REVISE` 当阶段唤醒。

### ER1-B — Stage A state chain

Stage A exact identity：

- task `workflow-core--normal-entry-reliability`
- branch `reviewed/workflow-core--normal-entry-reliability`
- worktree `/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability`
- `ci_required=true`

V0.2 要求 brand-new bootstrap前：

`git fetch --all --prune`

然后取 post-sync `origin/main` OID 并用 current Bridge `task bootstrap`。

核对正常状态链是否合法：

```text
PLAN_REQUESTED
-> Planner writes PLAN_V2
-> PLAN_FROZEN
-> Executor
-> WAITING_FOR_CI
-> Reviewed Reviewer reads actual CI
-> READY_FOR_GPT_REVIEW
-> real Reviewer review
-> PASS / AWAIT_HUMAN_DECISION
-> AI Research Stack pre-final Critic read-only
```

Stage A Positive completion明确只到 development candidate；没有把 Reviewer PASS冒充 final release PASS。

如果 pre-final Critic REVISE，V0.2要求回 Planner，不用 human REJECT / fake Reviewer REVISE唤醒同一个 Executor。

如果 pre-final Critic PASS，Stage A CURRENT仍保持 terminal；Stage B是新的 Reviewed task，不伪造 Stage A transition。

### ER1-C — Stage B setup 是否是 Bridge 0.9.3 合法已有能力

Stage B：

- task `workflow-core--normal-entry-reliability-release`
- branch `reviewed/workflow-core--normal-entry-reliability-release`
- physical worktree继续使用 Stage A worktree
- base = exact Stage A approved tip
- `ci_required=true`

V0.2 不从 main重新 bootstrap，也不新建第二 worktree。它要求：

1. 两个 Stage A PASS 条件成立；
2. clean Stage A worktree 从 exact approved tip 创建/切换 exact Stage B branch；
3. 运行 current Bridge `task init --ci-required`；
4. 首个metadata commit只机械填 REQUEST的 exact reviewed-worktree locator；
5. `publish-first` 首次发布 exact Stage B branch；
6. Stage B以后按正常 PLAN_REQUESTED -> PLAN_FROZEN -> Executor -> CI -> Reviewer状态运行。

请独立核对 current Bridge `task init` / `publish-first` 是否支持这种 existing-worktree、new exact reviewed branch、one metadata commit 的路径，以及 REQUEST locator / branch/task identity 是否满足 publish-first和后续resume contract。

若不支持，ER1仍应 REVISE；不得假设。

### ER1-D — manual handoff 是否完整

不假设 Scheduled Planner/Reviewer已存在。

Execution preflight若真实验证 exact task-bound automation存在且绑定正确 task+branch，可以用；否则人工模式必须使用 canonical prompt locator：

- Planner：`automation/reviewed_handoff/prompts/PLANNER.md`
- Executor：`automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`
- Reviewer：`automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md`

V0.2已给出每个状态的 owner和handoff wording。

核对：

- `ci_required=true` 后由 Reviewer读取 GitHub真实 CI；
- manual mode exact branch publication使用 bounded `ai-bridge host publish-current-branch`，不依赖generic watcher；
- generic watcher不被冒充task-bound automation；
- Planner/Reviewer GitHub transaction后，本地下一角色会先同步验证；
- Bridge PLAN必须写：
  - `Maintenance companion: ai-skills-core`
  - `Domain owner: workflow-core`

### ER1-E — pre-final checkpoint是否真正解决

关键问题：

Stage A已经terminal，Critic pre-final PASS后启动Stage B这个新 task，因此不需要：

- Critic改CURRENT；
- Executor伪造decision；
- Reviewer提前final integration；
- fake `REVISE` 唤醒；
- 新 state/schema。

判断这是否真正关闭上一 blocker，而不是换一种方式绕过 state machine。

## 优先复核 WC05-ER2

V0.2 final envelope只有在：

- Stage A Reviewer PASS；
- pre-final Critic PASS；
- Stage B 0.4 qualification PASS；
- exactly-once 0.5 bump；
- final candidate G1–G5 PASS；
- Stage B CI PASS；
- Stage B Reviewer PASS；
- AI Research Stack final Critic PASS；
- version/generated/changelog/README parity；

全部成立后才允许：

- exact final candidate integration到 canonical AI_Skills `main`；
- ordinary non-force publication；
- approved repository PATCH formal release；
- current canonical contract要求时 fast-forward-only `release` ref closure；
- exact workflow-core production identity / install-update smoke。

明确仍不授权：

- Stage A/Stage B branch deletion；
- worktree remove/prune；
- arbitrary cleanup；
- force/destructive Git；
- arbitrary branch/worktree；
- stable tag创建/移动；
- consumer-machine adaptation。

正式 release允许 branches/worktree保留。cleanup以后另授权。

请确认这已消除 v0.1 “integration scope与禁止 destructive cleanup混在一起”的冲突。

## 其余已通过内容只做回归检查

只有 V0.2 直接引入回归才允许重开：

- V0.4 三项 production change；
- G1–G5 semantics；
- specialist-contained hard negative；
- G4 single-run + true-absent；
- six-dimension equivalence；
- source/generated scope；
- regression provenance / anti-hardcode；
- two-stage version qualification/final-candidate rerun；
- Maintenance Board disposition；
- no paid API；
- no Longleaf/STAT5060/render specialist/Bridge runtime mutation；
- maturity unchanged。

特别检查 Stage B的两-stage Reviewed topology没有改变 same-final-candidate release requirement：最终 release claim仍只能由 version-bumped Stage B final candidate直接通过G1–G5。

## Kickoff逐字审查

Kickoff V0.2未来由用户实际发送后才形成授权。

确认它只授权：

- exact Stage A branch/worktree bootstrap；
- exact Stage B branch create/switch + same worktree task init/publish-first；
- zero-paid tests/replay/CI/smoke；
- exact task-owned publication；
- qualification PASS后的exactly-once version bump；
- final candidate全PASS后的bounded integration/release。

还要确认 Kickoff不会把 Stage A terminal PASS 当成总体 complete，也没有给 arbitrary cleanup/destructive权限。

## Version boundary

当前：

```text
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
implementation = NOT STARTED
execution branches/worktree = NONE / NOT AUTHORIZED until user sends approved Kickoff
maturity = unchanged
```

Critic review本身不得修改这些状态。

## 输出要求

给出：

`RESULT = PASS` 或 `RESULT = REVISE`

若 REVISE：

- 优先沿用 `WC05-ER1` / `WC05-ER2` finding IDs，必要时加稳定子 finding；
- requirement/source；
- direct evidence；
- causal risk；
- minimum closure condition；
- owner；
- 按 Critic Role Contract自动附完整Planner返修prompt。

若 PASS：

1. 先用用户可读中文说明：
   - ER1为什么已关闭，两个串行Reviewed task怎样合法跨过pre-final Critic checkpoint；
   - ER2为什么已关闭，final integration与cleanup权限怎样分离；
   - 哪些production/Gate设计没有改变。
2. 明确：
   - `READY_FOR_CODEX=YES`
   - PASS只批准 package commit `c7fb7488d3847855609d86fb0307bfeea824e078`
   - implementation/release仍未开始。
3. 按 Critic Role Contract逐字输出 package commit中的 Kickoff V0.2：

```text
APPROVED_PROPOSAL_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md
APPROVED_PLAN_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_2_2026-10-01.md
APPROVED_GOAL_PATH=docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_2_2026-10-01.md
APPROVED_KICKOFF_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_2_2026-10-01.md
APPROVED_COMMIT=c7fb7488d3847855609d86fb0307bfeea824e078
READY_FOR_CODEX=YES
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim Kickoff V0.2 from package commit>
=== APPROVED CODEX KICKOFF END ===
```

不要在PASS后另写一份语义不同的kickoff。
