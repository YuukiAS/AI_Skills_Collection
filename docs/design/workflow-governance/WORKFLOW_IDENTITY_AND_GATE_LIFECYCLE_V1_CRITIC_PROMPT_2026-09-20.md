# Workflow Identity & Capability Gate Lifecycle — Critic Prompt v1

你是 AI Research Stack 的长期独立 Critic thread。

这是一个新的实质设计轮次。只审方案，不实现代码，不创建 Reviewed Handoff task，不新建 branch/worktree，不启动 Codex Executor，不运行 paid API，不修改任何 production plugin / Bridge Kit runtime。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = AI Skills Maintainer + workflow-core + Bridge Kit Reviewed Handoff
design_topic_or_task_key = workflow-identity-and-gate-lifecycle
review_stage = DESIGN_PROPOSAL
source_branch_or_ref = AI_Skills_Collection main
proposal_path = docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_PROPOSAL_2026-09-20.md
proposal_version = v1
proposal_commit = deddff2e4903cfaef0dc2a7e4d9d7ebdc91330c3
execution_branch/worktree = NONE
```

本轮用户目标有两个：

1. 解决成熟插件随着真实失败增加时 Capability Gate 是否会无限增长的问题：不能为了省事随便删 Gate，也不能让每个新 failure 都新增 Gate；要形成长期可维护、能防回归、又不会把每次 release 变成无限 manual/paid matrix 的机制。
2. 重构后续 workflow identity：新任务不再使用 `055/056/057` 这类 0xx 作为主要身份。并行任务可能乱序完成，用户需要从 task/branch/path 名字本身看出“这是哪个插件/什么范围/做什么”。同时必须处理 056 这种跨插件、且还涉及 Bridge Kit 支撑层的复杂任务，不能只设计单插件 happy path。

## 一、强制读取当前真实 source

首先读取 AI_Skills_Collection 最新 main，并实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/PLUGIN_MATURITY.md`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_PROPOSAL_2026-09-20.md`

然后按问题需要 targeted read，而不是全仓 dump：

- 055 Clear Writing 当前 Proposal / execution review / Reviewed Handoff identity；
- `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` 当前版本，确认 056 实际跨插件/跨 repo 边界；
- `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md` 和当前 057 integration/recovery 相关 source，确认 057 为什么可以先于 055/056推进；
- `PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md` 中“不新增 G9/G10、把新场景并入已有 gates”的真实先例；
- Reviewed Handoff task/branch/result 目录和当前 `task_key` consumer。

必须另外读取 GPT_Codex_AI_Bridge_Kit 当前最新 main，至少：

- `ai_bridge_kit/reviewed_handoff.py`
- `ai_bridge_kit/cli.py` 中 task-key validation
- `scripts/validate_handoff_workspace.py` 中 task-key validation
- `templates/reviewed_handoff/` 与 branch/task-key 直接相关的必要 docs/tests
- `docs/design/reviewed_handoff_parallel_task_branches.md`

重点独立核实 Planner 的事实判断：当前 Bridge Kit 是否真的硬编码了 numeric task key；如果没有 Bridge 修改，AI_Skills 是否能合法采用非数字 task key。

不要依赖旧聊天或 Planner 摘要替代上述 source。

## 二、必须做独立外部研究

针对两个设计问题做少量高价值检索，不要只复述 Planner 的链接。

至少独立核查：

1. 成熟 AI/agent eval 如何区分 capability/quality eval 与 regression eval，已通过的 capability 如何转为长期 regression；
2. 大型 regression suite 如何在“变更影响选择”和“安全 full fallback”之间平衡；
3. workflow / issue / job identity 是否通常把 human-readable semantic identity 与创建顺序/状态分开，哪些做法值得借鉴、哪些不适合本 repo。

优先：

- Anthropic 原文；
- OpenAI 官方 eval 资料；
- Microsoft / GitHub /其他成熟系统官方文档。

记录实际采用/不采用什么，以及它是否改变你的判断。

## 三、不要礼貌性审查：同时攻击“过简”和“过重”

### A. 攻击 Gate lifecycle 是否过简

重点检查：

- “新 failure 优先进入已有 gate 的 regression bank”会不会导致一个 gate 越来越宽，最后什么都能塞进去，失去独立能力含义；
- “unaffected gate 只做 final-candidate canary”是否太松，是否可能让 shared prompt/runtime/model 变化造成的旧能力回归漏掉；
- Planner 对“impact known / impact uncertain”的分界是否足够可执行，是否需要更明确的 full-fallback 条件；
- cheap deterministic bank、qualitative cases、fresh evidence、paid review 的关系是否清楚；
- gate merge/split/retirement 是否会被用来偷偷降低验收标准；
- same-final-candidate 约束是否真正保留，而不是被 risk-based selection 稀释；
- maturity 提升时是否应有更强而非更弱的 regression expectation。

### B. 攻击 Gate lifecycle 是否过重

重点检查：

- 是否不必要地创造了“Capability Gate Charter / Regression Bank / Release Selection”三套新的机器概念；
- 是否应该只作为 policy 语义，而不新增 schema、ledger、registry；
- 是否会把每个 plugin 都强制成固定数量、固定层级的 eval framework；
- 是否会让每个小 patch 都跑过多人工/模型/paid review；
- 是否把普通 tests 和 capability gates 重复维护两遍。

如果更简单的现有结构就能达到用户目标，要求 Planner删掉多余机制。

## 四、独立攻击 semantic task-key 方案

Planner 提议新 task key：

```text
<scope>--<goal>
```

scope 候选：

```text
plugin-<canonical-plugin-slug>
cross-plugin
repo
cross-repo
```

你必须检查：

1. 这四类是否足够，还是会让 056 这种“AI_Skills 多插件 + Bridge 可写 + 产品 repo 只读”的任务产生新的分类歧义；
2. 是否应该按 primary product scope、owner、mutable repo 数量或别的维度命名；
3. 单插件使用 canonical plugin slug 是否正确；
4. 为什么不能继续 `055_clear_writing...` 只依靠后面的 slug；
5. 为什么不使用日期、GitHub issue number、UUID、owner-based key、层级 slash key；
6. `--` 分隔符、kebab-case、长度限制对 Git branch / worktree / filesystem / CURRENT / evidence identity 是否安全；
7. semantic key collision 如何关闭，是否需要不透明唯一后缀；若需要，最小机制是什么；
8. review round / integration / recovery 是否确实应保持同一 task key；
9. new creation semantic-only + legacy validation dual-format 是否是最小、安全 migration；
10. 当前 001–057 是否必须完全不迁移。

特别独立判断 Planner 把当前 056 映射成：

`cross-plugin--product-delivery-discipline`

是否合理。如果你认为 056 应是 `cross-repo`、owner-based 或其他形式，请说明因果理由，而不是只提出偏好。

## 五、审 ownership，不允许职责错位

Proposal 当前职责划分：

- AI Skills Maintainer：AI_Skills gate lifecycle、regression intake、plugin scope/version/release maintenance；
- target domain plugin：专业 gate 语义；
- workflow-core：AI_Skills 执行和 release-selection/fallback 语义；
- Bridge Kit Reviewed Handoff：cross-repo task-key parser / validation / legacy compatibility。

请独立判断：

- task-key syntax 是否确实是 Bridge Kit cross-repo reusable capability，而不是 AI_Skills 私有规则；
- AI Skills Maintainer 是否适合承担 gate lifecycle maintenance，还是这应更主要属于 workflow-core / policy；
- workflow-core 是否会因此变成第二个 task-key parser；
- domain plugin 的专业判断是否被 Maintainer/Workflow 吞掉；
- 是否真的需要修改 Bridge Kit production，还是存在更小的 adapter 路线；
- 如果需要 Bridge 修改，AI_Skills Proposal 是否已经把它限制在最小 cross-repo capability，而没有把单一 repo 需求塞进 Bridge。

## 六、审文件组织提议是否值得

Planner 还提出新任务以后使用：

```text
docs/design/<task_key>/...
docs/goals/<task_key>/GOAL.md
docs/operations/prompts/<task_key>/KICKOFF.md
```

旧文件不迁移。

这不是用户最初明确要求的核心，所以你必须特别审：

- 它是否确实降低 056/057 这种大量 flat files 的认知负担；
- 还是不必要目录迁移/文档 churn；
- 是否影响现有脚本、链接、review prompt；
- 是否应作为 non-blocking follow-up，而不是本轮 production scope。

可以 PASS semantic key 但要求删除这个子提议。

## 七、审 Capability Gate Matrix

逐项审 Proposal 的 G1–G7，不能只看有没有 gate 名：

- G1 Semantic identity
- G2 Identity propagation
- G3 Scope clarity
- G4 Legacy compatibility
- G5 Gate lifecycle
- G6 Release regression safety
- G7 No governance bloat

检查：

- 是否证明真实 normal entry，而不是 Markdown 里写了规则；
- 是否有重复 gates；
- 是否遗漏 current numbered task coexistence；
- 是否遗漏 branch/result/text-review/visual-review identity；
- 是否遗漏“新任务不用数字，但旧任务继续可跑”的真实 cutover；
- 是否遗漏 mature plugin regression-bank growth 和 safe fallback；
- 是否把 tests/regex/schema PASS 冒充用户实际可理解 workflow identity。

## 八、审迁移边界

用户当前同时还有 055/056/057 在运行。本方案若最终实现，不得为了“统一”破坏它们。

Critic 必须确认或提出更小替代：

- 001–057 不 rename；
- 当前 active branches/results/evidence 不搬迁；
- historical PASS/FAIL 不重写；
- cutover 只影响新的 task creation；
- validator 同时接受 legacy + semantic；
- 不利用新 task naming 创建 successor 链；
- 不把 055/056/057 的完成顺序重新解释成数字顺序。

## 九、Complexity verdict 必须明确

你必须明确回答：

- 方案是否 **TOO_SIMPLE / APPROPRIATE / TOO_COMPLEX**；
- 哪些机制应保留；
- 哪些机制应删除；
- 如果需要新增 blocker，每个 blocker 给：
  - stable ID；
  - 对应用户要求/contract；
  - 当前 source/evidence；
  - 因果风险；
  - 最小关闭条件；
  - owner。

偏好建议与 blocker 分开。

不要为了“更严谨”引入：

- 新 controller；
- watcher；
- database；
- task registry；
- ACTIVE_WORK ledger；
- 新状态机；
- GitHub Issues 强依赖；
- migration of all historical tasks；
- 为每个 gate 固定 fresh/paid 样本数。

## 十、输出与保存

如果审查需要保存 repo 文件，只允许新增/更新你的审查文档，不修改 Proposal、不修改 production、不修改 Bridge Kit。

建议审查文件：

`docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_CRITIC_REVIEW_2026-09-20.md`

最终回复先用自然中文说明：

1. 这套设计实际解决了什么；
2. 最大的过简/过重风险是什么；
3. task-key 方案是否真的优于 0xx；
4. Gate 会不会以后继续无限增长；
5. AI Skills Maintainer / workflow-core / Bridge Kit 的职责是否正确。

然后给：

```text
REVIEWED_PROPOSAL_PATH=
REVIEWED_PROPOSAL_VERSION=v1
REVIEWED_PROPOSAL_COMMIT=deddff2e4903cfaef0dc2a7e4d9d7ebdc91330c3
DECISION=PASS|REVISE
COMPLEXITY=TOO_SIMPLE|APPROPRIATE|TOO_COMPLEX
BLOCKERS=...
NON_BLOCKING=...
READY_FOR_EXECUTION_PLAN=YES|NO
```

本轮是 design review。即使 PASS，也只允许返回 Planner 整理 execution package；不授权 Codex、不授权 production 修改、不授权 Bridge release。

按照 `CRITIC_ROLE_CONTRACT.md`，在结尾自动生成下一条 Planner prompt：

```text
NEXT_HANDOFF=PLANNER
=== COPY TO PLANNER BEGIN ===
...
=== COPY TO PLANNER END ===
```
