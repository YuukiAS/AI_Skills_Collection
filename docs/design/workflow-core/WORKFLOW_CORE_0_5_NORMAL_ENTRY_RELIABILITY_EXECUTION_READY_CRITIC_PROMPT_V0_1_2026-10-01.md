# workflow-core 0.5 — Execution-ready Critic Review Prompt v0.1

你继续作为 AI Research Stack 的独立 Critic thread。设计阶段已经 PASS；现在只审查 execution package 是否真的可交给 Codex 执行。

不要实现代码，不要修改 production source，不要创建 branch/worktree，不要启动 paid API。

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: `workflow-core`
- design_topic_or_task_key: `workflow-core--normal-entry-reliability`
- source_branch_or_ref: `main`
- review_stage: `EXECUTION_READY_REVIEW`
- approved design: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md`
- approved design commit: `de66a18123059f76fd0ead4aa715f84ad066c62b`
- execution Plan: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_1_2026-10-01.md`
- Canonical Goal: `docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_1_2026-10-01.md`
- Kickoff Draft: `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_1_2026-10-01.md`
- package commit containing Proposal + Plan + Goal + Kickoff: `a649bdd5ebd75fb36f84206d692938a08d3028c1`
- design findings `WC05-D1`–`WC05-D7`: CLOSED
- current implementation state: NOT STARTED

只审这个 package commit；不要把后续 main 漂移混进被审对象。

## 必须读取

从最新 main 读取当前 rules，再从 package commit 读取被审三件套：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- approved V0.4 Proposal
- Execution Plan v0.1
- Canonical Goal v0.1
- Kickoff Draft v0.1

Reviewed Handoff / authorization 部分必须读取 `YuukiAS/GPT_Codex_AI_Bridge_Kit` 当前 main 的：

- `AGENTS.md`
- `templates/reviewed_handoff/README.md`
- 相关 bootstrap/resume/publish-first implementation contract。

## 审查重点

### ER1 — 设计忠实度

确认 Plan/Goal/Kickoff 没有重开或改写已批准 architecture：

1. precision normal-entry trigger；
2. specialist-first targeted discovery；
3. six-dimension fail-closed fallback equivalence。

G1–G5、specialist-contained hard negative、true-absent contrast、single-run G4、same-final-candidate requirement 必须与 V0.4 一致。

若 execution package 偷加 #7/#8/#9/#10 专属逻辑、新 runtime/state/schema 或更宽 owner scope，应 REVISE。

### ER2 — exact source / generated / maintenance scope

确认 source-first 文件范围足够且不过宽：

- workflow-core `SKILL.md`
- `references/escalation-rules.md`
- `agents/openai.yaml`
- `evals/trigger_queries.json`
- target regression tests
- canonical generated workflow-core payload
- release 阶段必要 version/changelog/README/registry/catalog/Marketplace metadata。

检查默认禁止改 `verification-matrix.md` / `task-template.md` 是否合理；若实现真的需要它们，应回 Planner而不是 Executor扩 scope。

确认 `workflow-core + ai-skills-core` maintenance companion 被显式要求，且 source read 不冒充 production invocation。

### ER3 — Reviewed Handoff 是否真的 executable

Package 选择：

- canonical checkout：`/home/yuukias/AI_Skills_Collection`
- task key：`workflow-core--normal-entry-reliability`
- branch：`reviewed/workflow-core--normal-entry-reliability`
- worktree：`/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability`
- `ci_required=true`

核对这些 locator 与 Bridge 当前 deterministic sibling contract 一致。

重点判断 package 的人工 handoff 设计是否合法：

- Planner owner 已明确为当前长期 Planner thread；
- Critic owner 已明确；
- package **没有假装 task-bound Scheduled Planner/Reviewer 已存在**；
- 如果 Bridge bootstrap 后必须由外部 Planner/Reviewer 做真实 state transition，package 是否已经给出合法、无新产品设计的恢复路径；
- 若没有自动 transport，是否能按人工 handoff继续而不要求 Executor伪造 Planner/Reviewer decision；
- generic watcher 不能冒充 task-bound automation。

如果仅凭这份 Kickoff 仍无法合法走到 Executor，且缺少的角色动作不是纯机械 materialization，请 REVISE；不要给 READY_FOR_CODEX=YES 后才第一次发现。

同时检查 package 对 canonical checkout 的处理：它是一个冻结 execution locator，但执行前必须真实验证；路径不成立时停止回 Planner，不能自动替换。这不得被误写成“已经验证机器健康”。

### ER4 — bounded authorization envelope

逐字审 Kickoff Draft。

发送该 Kickoff 后，只应授权：

- exact repo/task/branch/worktree 的 Bridge bootstrap/resume；
- task-owned commits；
- `publish-first` + exact reviewed branch 的普通 non-force publication；
- zero-paid tests/candidate replay/CI/production-compatible smoke；
- qualification G1–G5 PASS 后的 workflow-core `0.4 -> 0.5`；
- repository 当时真实版本的下一 PATCH metadata；
- final candidate 全部 PASS + independent review PASS 后的 canonical AI Skills Maintainer integration/release closure。

不得授权：

- paid API；
- force/destructive Git；
- arbitrary branch/worktree；
- Bridge/Host Policy mutation；
- Longleaf/STAT5060/render-specialist mutation；
- consumer-machine adaptation；
- architecture/gate/scope expansion。

请特别判断最后的 integration/release authorization 是否足够 bounded；如果 canonical release path仍存在不可推导的高影响动作，要求最小收窄，而不是泛化授权。

### ER5 — version / candidate identity

Package 设计了两阶段证据：

1. version仍为 0.4 的 qualification candidate 先通过 G1–G5；
2. 只有 qualification PASS 后才允许 `0.4 -> 0.5` + repository PATCH；
3. version mutation 产生新 candidate，因此 bump 后 final candidate 必须重新直接通过 G1–G5；
4. release claim只绑定 bump 后同一 final candidate。

判断这是否同时满足：
- 用户“先证明再允许 bump”的边界；
- Capability Gate Policy 的 same-final-candidate rule；
- plugin version policy exactly-once bump。

如果存在 circular evidence / old-candidate stitching，请 REVISE。

### ER6 — G1–G5 executable evidence

检查每个 gate 是否已经转成真正可执行/可失败的 contract。

特别检查：

- G1 hard negative 必须让 workflow-core candidate 已安装/可发现但未消费，同时 specialist 实际消费；
- G2 不是大范围 host scan；
- G3 六项必须有逐项 evidence，不能 `equivalent=true`；
- G4 positive 同一 run 完整链，不能两次 replay 拼接；
- G4 absent case 真正 fail closed；
- G5 包含 0.3/0.4 regression、相邻 specialist negative、source/generated/version parity 和 risk-matched broad tests。

source string、schema、tests 数量、静态文件存在不能冒充 production consumption。

### ER7 — original failure 与 anti-hardcode

确认 STAT5060 / Chinese-math-PDF / #8 只作为 regression provenance，production source 不能硬编码项目、Longleaf 路径/module version、case id 或 ctex/Chromium 单例逻辑。

确认实现不会为了过 Gate 去修改 STAT5060、Longleaf、render specialist 或 Bridge。

### ER8 — pre-final/final Critic stop points

确认：

- development candidate 完成后先停给 pre-final Critic；
- pre-final PASS 前不消耗 final release evaluation；
- qualification失败后不能直接 bump；
- final candidate gate失败后不能挑赢家/换题；
- architecture/gate变化必须回 Planner/Critic；
- ordinary bug/test repair 可在冻结 Plan 内处理。

### ER9 — Maintenance Board truth

Package 必须继续遵守 approved V0.4：

- `HISTORICAL_RESOLVED` 仅是 bootstrap/coverage disposition；
- canonical TODO vocabulary含 `PROMOTED`；
- #5/#6/#11 的 DONE 仍要求适用 ADAPTING consumer closure；
- 当前无合法 Project/Clear Writing surface时只保留 exact pending mutation，不伪称同步、不要求用户手工维护。

本 execution package不得偷偷把 consumer-machine adaptation纳入 0.5 implementation scope。

### ER10 — completion / release claim

确认 Canonical Goal 的 complete/released claim只有在：

- final candidate G1–G5 PASS；
- broad regression/CI PASS；
- independent final review PASS；
- source/generated/version/changelog/README parity；
- exact candidate integration；
- production identity/install/update smoke；
- formal release closure

都成立后才允许。

若任一步被 skipped，必须 truthful partial/blocker，不得用 CI/schema/commit存在冒充完成。

## Version boundary

当前 package prep：

```text
workflow-core = 0.4 / NO_BUMP
repository bump = NONE
maturity = unchanged
implementation = NOT STARTED
```

Critic review 本身不得修改这些状态。

## 输出要求

给出：

`RESULT = PASS` 或 `RESULT = REVISE`

如果 REVISE：

- 每个 blocker 给稳定 finding ID；
- requirement/source；
- direct evidence；
- causal risk；
- minimum closure condition；
- owner；
- 按 Critic Role Contract 自动生成完整 Planner返修 prompt。

如果 PASS：

1. 先用自然中文说明 execution package 为什么现在可执行，尤其说明：
   - exact scope；
   - Reviewed Handoff handoff是否合法；
   - G1–G5怎样证明真实能力；
   - version/final-candidate闭环；
   - 哪些权限仍未被批准。
2. 明确：
   - `READY_FOR_CODEX=YES`
   - PASS只批准 package commit `a649bdd5ebd75fb36f84206d692938a08d3028c1`
   - 不代表 implementation/release 已完成。
3. 按 Critic Role Contract 逐字输出被审 Kickoff：

```text
APPROVED_PROPOSAL_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_4_2026-10-01.md
APPROVED_PLAN_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_1_2026-10-01.md
APPROVED_GOAL_PATH=docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_1_2026-10-01.md
APPROVED_KICKOFF_PATH=docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_1_2026-10-01.md
APPROVED_COMMIT=a649bdd5ebd75fb36f84206d692938a08d3028c1
READY_FOR_CODEX=YES
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim kickoff draft from package commit>
=== APPROVED CODEX KICKOFF END ===
```

不要根据 PASS 重新发明另一份 kickoff。
