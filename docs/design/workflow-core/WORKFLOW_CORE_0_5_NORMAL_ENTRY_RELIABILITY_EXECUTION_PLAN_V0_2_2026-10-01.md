# workflow-core 0.5 正常入口可靠性执行 Plan v0.2

日期：2026-10-01  
角色：AI Research Stack Planner  
状态：EXECUTION PACKAGE REVISION — WAITING FOR EXECUTION-READY CRITIC  
目标仓库：`YuukiAS/AI_Skills_Collection`  
目标插件：`workflow-core / Verified Workflow`  
设计主题：`workflow-core--normal-entry-reliability`

设计 authority：

- Approved Proposal：`docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md`
- Approved Proposal commit：`de66a18123059f76fd0ead4aa715f84ad066c62b`
- Design Critic：PASS
- `WC05-D1`–`WC05-D7`：CLOSED

上一 execution package：

- Plan v0.1 / Goal v0.1 / Kickoff v0.1
- reviewed package commit：`a649bdd5ebd75fb36f84206d692938a08d3028c1`
- execution-ready Critic：REVISE
- open execution blockers：`WC05-ER1`、`WC05-ER2`

本 Plan 只修 execution topology 与 authorization envelope，不改 V0.4 的 production architecture、G1–G5 或 Maintenance Board 语义。

## 1. 冻结 production scope

仍只实现：

1. 精确且克制的 normal-entry discovery / trigger；
2. specialist-first targeted capability discovery；
3. 六维全满足、fail-closed fallback equivalence。

保持不变：

- specialist-contained hard negative；
- G4 single-run positive chain；
- true capability-absent contrast；
- same-final-candidate release evidence；
- no task-specific hardcode；
- source/generated scope；
- two-stage `0.4 qualification -> exactly-once 0.5 bump -> final candidate rerun G1–G5`；
- no paid API；
- no Longleaf / STAT5060 / render-specialist / Bridge runtime mutation；
- maturity unchanged。

## 2. 四个 owner 与职责

### AI Research Stack Planner

负责：

- 本 package 与 V0.4 语义；
- Reviewed Handoff 的 Planner transaction；
- 把已批准 package **机械 materialize** 成每个阶段自己的 Bridge `PLAN.md`；
- 若执行事实要求改变 architecture、Gate、scope、version policy、authority 或 recovery，重新规划。

不得冒充 Critic 或 Reviewer。

### AI Research Stack Critic

负责两次独立只读 checkpoint：

1. Stage A Reviewed Reviewer PASS 后的 **pre-final Critic**；
2. Stage B Reviewed Reviewer PASS 后、正式 integration/release 前的 **final Critic**。

Critic 不写 Reviewed Handoff `CURRENT.json`，不伪造 `PASS/REVISE` Reviewer transaction，不负责 CI state transition。

### Reviewed Handoff Reviewer

使用 repository canonical prompt：

`automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md`

负责：

- `ci_required=true` 时读取 GitHub 当前 task branch 的真实 CI；
- CI PASS 后拥有 `WAITING_FOR_CI -> READY_FOR_GPT_REVIEW` transaction；
- 对当前 Stage 的 frozen Bridge `PLAN.md` 做真正 Reviewer review；
- 只写 Bridge 合法的 Reviewer artifacts/state。

若 execution preflight 证明 exact task-bound Scheduled Reviewer 已存在且绑定正确 task+branch，可使用；否则使用独立人工 Reviewed Reviewer thread，按同一 canonical prompt执行。不得让 AI Research Stack Critic代替。

### Codex Executor

使用 repository canonical prompt：

`automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`

负责实现 frozen Bridge Plan，写 task-owned implementation/result/evidence，并按当前 Stage 的 `ci_required=true` 合法交棒到 `WAITING_FOR_CI`。

不得修改 Planner/Reviewer authority，不能用假 `REVISE` 当阶段标记。

## 3. 为什么改为两个串行 Reviewed task

Bridge 0.9.3 的合法 state graph 没有“外部 Critic PASS 后从同一 `WAITING_FOR_CI/READY_FOR_GPT_REVIEW/PASS` 无 finding 地恢复 Executor”的状态。

因此 v0.2 不再试图把 Phase E pre-final Critic 塞进一个 Reviewed task 中。改为**同一总体 Goal、同一 task branch lineage 上的两个串行 Reviewed task**：

- Stage A：实现与开发验证；其 Reviewer PASS 是该 Stage 的真实 terminal PASS；
- AI Research Stack Critic：在两个 Stage 之间做 pre-final checkpoint，不修改 Bridge state；
- Stage B：在 Stage A 已通过的 exact candidate lineage 上执行 final qualification、version bump、final rerun 与 release readiness。

这不增加 workflow/state/schema/watcher/daemon。两个 Stage 不并行；Stage B 只有在 Stage A Reviewed Reviewer PASS + AI Research Stack Critic PASS 后才允许初始化。

## 4. 冻结 Git / Reviewed identity

Canonical repo：

`YuukiAS/AI_Skills_Collection`

Canonical checkout：

`/home/yuukias/AI_Skills_Collection`

### Stage A — development task

- task key：`workflow-core--normal-entry-reliability`
- branch：`reviewed/workflow-core--normal-entry-reliability`
- worktree：`/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability`
- `ci_required=true`
- `max_review_rounds=2`
- text/visual review：false
- base：bootstrap 时 post-sync `origin/main`

Stage A 使用 Bridge deterministic sibling bootstrap。

### Stage B — finalization task

- task key：`workflow-core--normal-entry-reliability-release`
- branch：`reviewed/workflow-core--normal-entry-reliability-release`
- worktree：继续使用 Stage A 已验证的同一物理 worktree  
  `/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability`
- `ci_required=true`
- `max_review_rounds=2`
- text/visual review：false
- base commit：Stage A exact approved branch tip，必须同时有 Stage A Reviewed Reviewer PASS 与 AI Research Stack pre-final Critic PASS。

Stage B **不使用 brand-new bootstrap from main**，因为那会丢掉尚未正式集成的 Stage A candidate。它使用 Bridge 现有 `task init` 在一个新 exact reviewed branch 上初始化新的 task state：

1. 在 Stage A worktree clean 且两个 PASS 均已确认后，从 exact Stage A approved tip 创建并切换到  
   `reviewed/workflow-core--normal-entry-reliability-release`；
2. 这是 Kickoff 明确授权的一次 exact branch create/switch，不是任意 branch authority；
3. 在该 branch/worktree 运行 `ai-bridge reviewed-handoff task init --ci-required`；
4. 在首个 control commit 中把 generated `REQUEST.md` 的 reviewed-worktree placeholder 机械绑定为上面的 exact worktree locator；不改变 objective/产品语义；
5. 首个 commit 只包含 Stage B `REQUEST.md/CURRENT.json` 初始化，随后用 `ai-bridge reviewed-handoff task publish-first` 发布 exact Stage B branch；
6. 此后 Stage B branch 与 task key 匹配，若同一 worktree需要恢复，按当前 Bridge artifact-bound resume contract处理；不得改成 `/tmp`、second clone 或其他 branch。

若 Stage B exact branch creation、task init、publish-first 或 resume 不能在当前 Bridge/Host policy 下合法执行，停止回 Planner；不得回退到 raw worktree/new clone。

## 5. Stage A brand-new bootstrap 与同步

执行前从 canonical checkout：

1. `git fetch --all --prune`
2. 读取 post-sync `origin/main` OID；
3. 确认该 OID 包含本 Critic-approved execution package；
4. 检查 ordinary single-origin profile、Review 已安装、exact Stage A branch/worktree 尚无冲突；
5. 使用：

`ai-bridge reviewed-handoff task bootstrap --task-key workflow-core--normal-entry-reliability --expected-repo YuukiAS/AI_Skills_Collection --expected-base-commit <post-sync-origin-main-oid> --ci-required --max-review-rounds 2 --objective <bounded objective>`

6. bootstrap 后首份 `REQUEST/CURRENT` commit 使用 `ai-bridge reviewed-handoff task publish-first`。

不得把 v0.1 的 `git fetch origin main` 继续当本 brand-new bootstrap 的 canonical sync；这里按当前 Bridge README 使用 `git fetch --all --prune`。

## 6. Bridge PLAN materialization contract

每个 Stage 的 `PLAN.md` 都必须是 `AI_BRIDGE_REVIEWED_PLAN_V2`，由 AI Research Stack Planner 在 `PLAN_REQUESTED` 时根据本 package机械 materialize。

两个 PLAN 都必须显式写：

```text
Maintenance companion: ai-skills-core
Domain owner: workflow-core
```

含义：

- `ai-skills-core` 负责中央 plugin maintenance closure；
- `workflow-core` 是本次被修改的 domain/behavior owner；
- 具体 regression 中的 render/statistics/browser specialist只提供既有专业合同，不成为被修改 owner。

Planner 写 `PLAN.md` 后重新读取当前模板与写出的 PLAN，自检 required sections，最后才写 `CURRENT.state=PLAN_FROZEN`。

## 7. 完整人工 role/state handoff

不假设 task-bound Scheduled Planner/Reviewer 已存在。

Execution preflight 先检查 exact task-bound automation；**只有真实验证已存在并绑定正确 task+branch 时才能用**。否则使用以下人工 handoff。generic watcher 不得冒充 task-bound automation。

### 7.1 PLAN_REQUESTED -> Planner -> PLAN_FROZEN

Owner：AI Research Stack Planner。

Canonical prompt locator：

`automation/reviewed_handoff/prompts/PLANNER.md`

Stage A manual handoff：

```text
请按当前 branch 的 automation/reviewed_handoff/prompts/PLANNER.md，
只处理 task workflow-core--normal-entry-reliability。
读取 Critic-approved execution package v0.2，
把它机械 materialize 成 AI_BRIDGE_REVIEWED_PLAN_V2。
必须写 Maintenance companion: ai-skills-core；
Domain owner: workflow-core。
不得改变 approved architecture/G1-G5/scope。
最后自检 PLAN，并合法推进 CURRENT 到 PLAN_FROZEN。
```

Stage B 同样使用该 prompt locator，只处理  
`workflow-core--normal-entry-reliability-release`，且其 Positive completion 是 final qualification/version/release readiness，不重新设计 architecture。

### 7.2 PLAN_FROZEN -> Executor -> WAITING_FOR_CI

Owner：Codex Executor。

Canonical prompt locator：

`automation/reviewed_handoff/prompts/CODEX_EXECUTOR.md`

人工模式下，Goal 明确指定 task-bound publication contract：Executor完成合法 implementation/control commits、working tree clean 且 `CURRENT` 已进入 `WAITING_FOR_CI` 后，只允许通过：

`ai-bridge host publish-current-branch --expected-repo YuukiAS/AI_Skills_Collection --expected-branch <exact current reviewed branch>`

发布该 exact branch。不得 raw push；不得启动 generic watcher只为充当 publisher。

若当前机器已经验证有**真正 task-bound** Executor transport，可使用；否则直接由用户启动的 Codex thread按 canonical Executor prompt运行。

### 7.3 WAITING_FOR_CI -> Reviewed Reviewer

Owner：Reviewed Handoff Reviewer，不是 Critic。

Canonical prompt locator：

`automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md`

Reviewer从 GitHub读取 exact task branch真实 CI：

- pending/running：NO WRITE；
- PASS：Reviewer transaction设置 `ci_status=PASS`、`state=READY_FOR_GPT_REVIEW`，随后可在同一 reviewer run继续真实 review；
- FAIL：按 Bridge contract产生真实 `REVISE`，不能把 CI FAIL忽略成阶段状态。

人工模式 exact handoff：

```text
请按当前 branch 的
automation/reviewed_handoff/prompts/REVIEWER_SCHEDULED_TASK.md，
只处理 exact task key 与 exact branch。
先处理 WAITING_FOR_CI 的真实 GitHub CI transaction；
只有 CI PASS 后才进入 READY_FOR_GPT_REVIEW 并执行独立 Reviewer review。
不得把 AI Research Stack Critic 当 Reviewer，也不得为推进阶段制造假 REVISE。
```

### 7.4 Stage A Reviewer PASS -> pre-final Critic

Stage A Bridge PLAN 的 Positive completion 只到：

- source-first implementation；
- development replay；
- broad regression；
-真实 consumption evidence；
- Reviewer确认 Stage A candidate满足该阶段 frozen Plan。

它**不**包含 version bump、final qualification、integration或release。

因此 Stage A Reviewer PASS 是真实的 Stage A terminal PASS，不是假 pre-final标记。Bridge正常到 `PASS -> AWAIT_HUMAN_DECISION` 后，Stage A state 保持terminal。

随后 owner切到 AI Research Stack Critic。Critic只读：

- exact Stage A candidate；
- GATE_CASES；
- development evidence；
- CI；
- Reviewed Reviewer finding；
- V0.4 / execution package。

Critic不改 Stage A `CURRENT`。

如果 Critic = REVISE：总体 Goal停止并回 Planner冻结 recovery；不得用 Stage A human REJECT / Reviewer REVISE 伪装成阶段唤醒。

如果 Critic = PASS：Stage A branch不集成 main、不删除、不cleanup；按本 Kickoff已有 bounded authorization进入 Stage B setup。

### 7.5 pre-final Critic PASS -> Stage B PLAN_REQUESTED

这是**新 Reviewed task 的开始**，不是 Stage A state transition。

由 Codex/bootstrap owner按 §4 创建 exact Stage B branch，初始化 Stage B task并发布 first metadata。Stage A `CURRENT` 保持历史 terminal state，不改写。

然后 owner回到 AI Research Stack Planner，按 §7.1冻结 Stage B PLAN。

### 7.6 Stage B Executor / CI / Reviewer

Stage B Executor在一个 frozen Plan内顺序完成：

1. `workflow-core 0.4` qualification G1–G5；
2. qualification全部 PASS 后才允许 exactly-once `0.4 -> 0.5`；
3. repository按当时真实版本推进一个 PATCH；
4. regenerate；
5. 冻结 version-bumped final candidate；
6. 同一 final candidate重新直接跑 G1–G5；
7. broad tests / CI handoff。

然后 `WAITING_FOR_CI` 交给 Reviewed Reviewer，Reviewer按 §7.3处理真实 CI与最终 Stage B review。

### 7.7 Stage B Reviewer PASS -> final Critic -> integration/release

Stage B Reviewer PASS 后，AI Research Stack Critic做独立 final review；不改 `CURRENT`。

- Critic REVISE：停止回 Planner冻结 recovery；不清理 branch/worktree，不强行 integration。
- Critic PASS：未来用户发送本 package Kickoff 已明确条件授权 exact final integration/release envelope，因此可以进入 §12 的 final closure。

若 Bridge需要把 Stage B PASS human gate机械记录为 ACCEPT，本 Kickoff仅在**Stage B Reviewed Reviewer PASS + AI Research Stack final Critic PASS**同时成立时授权对 exact Stage B task执行一次 `human record --decision ACCEPT`；不适用于其他 task或REJECT route。

## 8. Exact source / generated scope

与 v0.1 保持不变：

source authority：

- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md`
- `skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml`
- `skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json`

target regression：

- 新建 `tests/test_workflow_core_normal_entry_reliability.py`
- 必要时最小修改 `tests/test_workflow_core_reviewed_handoff_routing.py`

默认不改 `verification-matrix.md` / `task-template.md`；需要时回 Planner。

generated workflow-core payload、release metadata、task evidence范围与 v0.1相同。

## 9. G1–G5 与实现顺序

G1–G5 semantics 完全沿用 V0.4。

Stage A 只做 development/known-regression/broad-precheck，不消耗 final qualification identity。

Stage B 在 pre-final Critic PASS 后：

1. 冻结 qualification inputs；
2. 0.4 candidate完整 G1–G5；
3. PASS 后 exactly-once bump；
4. 冻结 version-bumped final candidate；
5. final candidate重新完整 G1–G5；
6. CI；
7. Reviewed Reviewer；
8. final Critic；
9. integration/release。

任何不同 candidate/run拼 G4 evidence = FAIL。

## 10. Maintenance Board

完全沿用 approved V0.4，不新增 consumer-machine adaptation。

- `HISTORICAL_RESOLVED` 只作 bootstrap/coverage disposition；
- canonical TODO vocabulary含 `PROMOTED`；
- #5/#6/#11 的 DONE仍服从适用 ADAPTING consumer closure；
- 当前没有合法 Project/Clear Writing surface时只记录 exact pending mutation，不要求用户手工维护。

## 11. Stop / recovery

立即停回 Planner/Critic：

- V0.4 architecture/G1–G5需变化；
- Stage A 或 Stage B exact branch/worktree/state无法合法建立；
- task-bound manual handoff不能按 canonical prompt继续；
- 需要 Bridge/Host Policy改动；
- 需要 fake Reviewer decision/fake REVISE才能推进；
- pre-final Critic REVISE；
- final Critic REVISE；
- task-specific hardcode；
- paid API成为必要条件；
- version/shared-source drift使 PATCH target或candidate lineage不清楚。

普通 implementation bug可在当前 frozen Stage Plan内修；若改变机制则回 Planner。

## 12. Final integration / release authorization boundary

只有以下全部满足：

- Stage A Reviewed Reviewer PASS；
- pre-final Critic PASS；
- Stage B qualification PASS；
- exactly-once version bump；
- version-bumped final candidate G1–G5 PASS；
- Stage B真实 CI PASS；
- Stage B Reviewed Reviewer PASS；
- AI Research Stack final Critic PASS；
- source/generated/version/changelog/README parity成立；

才允许：

- exact final candidate integration到 canonical AI_Skills `main`；
- ordinary non-force publication；
- approved repository PATCH formal release；
- 当前 canonical maintainer contract要求时的 fast-forward-only `release` ref closure；
- exact workflow-core production identity / install-update smoke。

本 Kickoff明确**不授权**：

- Stage A或Stage B reviewed branch deletion；
- reviewed worktree remove/prune；
- arbitrary cleanup；
- force push / force-with-lease作为普通发布；
- destructive Git；
- arbitrary branch/worktree；
- stable tag创建/移动，除非未来另有明确授权；
- consumer-machine adaptation。

正式 product/release closure允许在 reviewed branches 与当前 worktree继续保留的情况下完成。需要 cleanup 时以后单独取得 bounded authorization。

## 13. Version / maturity

当前 package：

```text
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
implementation = NOT STARTED
maturity = unchanged
```

只有 Stage B qualification全部 PASS后才允许 bump；release claim只绑定 bump后final candidate。

## 14. 本 Plan 不授权 implementation

本文件仍只是待 execution-ready Critic审查的 Plan。只有用户未来发送同版 Critic-approved Kickoff，才形成 current-user execution authorization。
