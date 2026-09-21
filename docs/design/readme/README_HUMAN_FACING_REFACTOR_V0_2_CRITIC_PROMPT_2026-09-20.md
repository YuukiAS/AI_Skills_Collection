# README Human-Facing Refactor v0.2 — Critic Re-review Prompt

你是 AI Research Stack 的长期独立 Critic thread。

继续同一个 README Human-Facing Refactor 设计轮次。本轮只复审 v0.2 是否关闭上一轮两个稳定 blocker；不要实现 README，不修改 Role Contract，不创建 Reviewed Handoff task/branch/worktree，不启动 Codex Executor，不调用 paid API，不修改 plugin production source、generated layer、profiles、AGENTS.md、Bridge Kit、Capability Gate Policy 或 Versioning Policy。

## Active Review Context

target_repo = `YuukiAS/AI_Skills_Collection`  
target_plugin_or_domain = repository human-facing README / workflow-doc dependency cleanup  
design_topic_or_task_key = `readme-human-facing-refactor`  
source_branch_or_ref = latest `main`  
review_stage = design re-review

reviewed_proposal = `docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_2_2026-09-20.md`  
reviewed_proposal_version = v0.2  
reviewed_proposal_commit = `f3e7ec12db8c1704d919e6124c9875babd67bb97`

previous_proposal = `docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_1_2026-09-20.md`  
previous_proposal_commit = `13667f59cb60a199d9c0ce518b4ff66806370968`

上一轮 Critic review 未写入 repo。正式 blocker 由用户原样转交：

- `README-R1` — 保留当前 Repository / CLI version；
- `README-R2` — 两列 card gallery 改为 preferred，而不是强制唯一布局。

## 先实际读取

按 Critic contract 重新读取最新 main，至少包括：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `README.md`
- `VERSION`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `scripts/codex_marketplace_config.json`
- v0.1 proposal
- v0.2 proposal

并做一次独立、针对性的外部核查，优先 GitHub 官方 README / Markdown / GFM 文档。不要只复述 v0.2 的外部研究。

## 只优先复核原 blocker

### README-R1

上一轮要求：

- README 保留轻量的人类可读 current Repository / CLI version；
- 以 `VERSION` 为依据；
- 不恢复版本历史、maturity 表、内部 release 流程；
- 不修改版本政策；
- Repository bump = NONE；
- 所有 plugin = NO_BUMP。

v0.2 的处理：

- 重新核对当前 `VERSION = 5.0.5`；
- 最终 README 信息架构新增一行轻量 `Repository / CLI 5.0.5`；
- 明确 implementation 时必须从 `VERSION` 核对；
- 版本历史、maturity 与内部 release 流程继续不进入首页；
- Versioning Policy 本身不改；
- Repository bump / plugin bump 均保持 NONE / NO_BUMP。

请判断 README-R1 是否关闭，不要额外把 README 重新扩张成 release dashboard，除非当前用户要求或现行合同确实产生新的不可忽略冲突。

### README-R2

上一轮要求：

- 两列 gallery 保持首选；
- GitHub wide/narrow + light/dark render 不佳时，同一范围内可退一列或更简单原生布局；
- 不为此新增 badge/CSS/generator/schema/build chain；
- 必须直接查看真实 GitHub render 并留视觉证据。

v0.2 的处理：

- 两列改成 preferred；
- 写明具体 fallback 顺序：两列 -> 一列 -> 更简单原生布局；
- 定义横向滚动、卡片过窄、比例失衡、窄屏层级崩坏、light/dark 对比异常为退回条件；
- 退回只属于呈现调整，不触发新架构设计；
- 明确禁止外部 badge、自定义 CSS、README generator、schema/build chain；
- 最终验收要求真实 GitHub wide/narrow + light/dark 视觉证据；
- 外部研究补充 GitHub GFM 对 raw HTML 与 `<style>` filtering 的官方依据。

请判断 README-R2 是否关闭，重点检查 fallback 是否足够真实、不过重。

## 非阻塞建议

上一轮建议 documentation footer 不要依赖不存在的 `docs/README.md`。

v0.2 处理为：

- 不新建 docs portal；
- 只从现有的 `profiles/README.md`、`docs/LOCAL_CONFIGURATION.md`、`TODO.md`、`CHANGELOG.md` 中挑 2–4 个具体入口；
- 不新增 index/generator。

请确认这保持为轻量导航，而不是重新把 README 变成长文档入口墙。

## 其余已通过方向不要重新设计

除非 v0.2 引入新的实质风险，否则继续保留上一轮已通过方向：

- README = 项目首页 + plugin gallery；
- 十个中央 plugin 的显示名和版本来自 `scripts/codex_marketplace_config.json`；
- 复用现有本地 SVG；
- 删除真实项目 refinement 长说明、NEW 模板、Planner/Critic 复制模板、incident 教程、HPC 命令墙、Presentation/CUHK 详细说明、目录逐项说明、验证命令墙；
- Planner/Critic authority 不再依赖 README；
- 未来 implementation 只修 `PLANNER_ROLE_CONTRACT.md` §10.1 与 `CRITIC_ROLE_CONTRACT.md` §6.2 的 README-template dependency；
- 不改 AGENTS、Capability Gate Policy、Versioning Policy、Marketplace source/generated payload、plugins、profiles 或 Bridge Kit。

这是 docs / README 设计，不是 production plugin refinement，不机械要求 Plugin Capability Gate Matrix。

## 输出要求

先用正常中文说明：

1. README-R1 是否关闭，为什么；
2. README-R2 是否关闭，为什么；
3. 非阻塞 footer 处理是否合适；
4. v0.2 是否仍然满足“README 给人读、非常美观、核心展示插件名/版本/用途”的用户目标；
5. 当前 PASS/REVISE 只证明设计，不授权 implementation。

然后输出：

`RESULT = PASS | REVISE`

`REVIEW_OBJECT = docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_2_2026-09-20.md / v0.2 / f3e7ec12db8c1704d919e6124c9875babd67bb97`

若 REVISE：

- 保留稳定 finding 编号；
- 说明证据、因果风险与最小关闭条件；
- 按 `CRITIC_ROLE_CONTRACT.md` 自动附上下一条完整 Planner prompt。

若 PASS：

- 这是 design-stage PASS，不是 execution-ready PASS；
- 下一步应回 Planner 准备最小 execution package；
- 按 `CRITIC_ROLE_CONTRACT.md` 自动附上完整 Planner prompt；
- 不要自己开始实施或生成未经 Planner 整理的 Codex kickoff。
