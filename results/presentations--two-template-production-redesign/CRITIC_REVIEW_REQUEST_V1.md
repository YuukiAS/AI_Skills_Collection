# Critic Review Request — Presentations 双模板生产架构重设计 V1.0

你是 AI Research Stack 的独立 Critic thread。本轮只做架构与 Capability Gate 审查，不实现代码、不修改 production plugin、不创建 Executor task、不运行付费 review、不发布。

## Active Review Context

```text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = presentations
design_topic_or_task_key = presentations--two-template-production-redesign
review_stage = architecture_and_capability_gate_review
source_branch_or_ref = main
proposal_path_and_version = docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0_2026-09-28.md @ V1.0
proposal_commit = 78901482243a877cdcec3150ca229b3fa58b7173
previous_design_context = docs/design/PRESENTATIONS_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md
historical_bounded_implementation_context = automation/reviewed_handoff/tasks/045_presentations_real_use_regression_hardening/PLAN.md
execution_branch = NOT_CREATED
execution_worktree = NOT_CREATED
```

## 必须先实际读取

从最新 `main` 读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/plugin-todos/presentations.md`
- `docs/plugin-changelogs/presentations.md`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/business-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/template-routing.md`
- `skills/tools/documents-media/presentations/shared/ppt-skill-routing.md`
- `profiles/presentation-desktop.json`
- `skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/**`
- 本轮 V1.0 Plan

旧 V0.2 与 045 只作为证据和迁移背景，不是默认正确答案。

## 已冻结的用户决策

1. 以后任何 PPT/deck/Beamer/Slides 创建或返修任务都必须先进入 `presentations` plugin；小编辑可以走轻量路径，但不能绕过前门。
2. 仓库只维护两个内置模板：
   - `cuhk-research`；
   - 根据用户课程 PDF 重建的 `course-standard`。
3. 用户或 venue 明确给出的模板只作为 external locked input，不进入内置模板库。
4. V1.0 必须覆盖当前 `docs/plugin-todos/presentations.md` 的全部有效 TODO：tracking `#29`–`#48`，包括 #29 内的独立失败项。
5. 本轮只审设计，不授权实现、付费调用或发布。

用户提供的模板参考没有提交到普通 repo payload。Plan 中记录了来源 hash 与已核实事实：`Chapter1.pdf` 是 4:3 标准 Beamer，黑色顶部带、蓝色 frame-title、白色正文、Nimbus Sans + Computer Modern、右下页码；彩色高亮是 PDF annotations，不属于模板。Critic 不得假装已经看到未提供给本线程的私有 PDF；若你认为架构判断必须读取完整源文件，明确说明最小缺口，但先审查现有可验证设计。

## 独立外部核查

按角色合同做少量针对性网络核查，优先官方来源。至少独立核对：

- 当前 Beamer 的正式版本、template system 和许可；
- LaTeX tagged PDF / Beamer 的现实边界，避免 Plan 错误宣称 PDF/UA；
- 是否存在比当前“两模板 + shared core”更成熟、明显更简单的现实替代。

记录采用/不采用理由；不要用无限检索替代决策。

## 审查任务

请攻击而不是复述 V1.0，重点回答：

### A. 产品与正常入口

- “任何 PPT 必须调用 presentations”是否通过 `new-deck / existing-deck-revision / local-edit / plan-only` 避免把小任务做重？
- 新 deck 默认 `.tex + PDF + render`、显式 PPTX/Slides 再委托官方 adapter，是否与现有入口兼容？
- teaching 作为 shared-core mode 而不是新 plugin/skill，是否方向正确？

### B. 双模板架构

- `cuhk-research` 与 `course-standard` 的职责、场景和视觉合同是否足够明确？
- external locked input 是否仍保持“内置模板只有两个”，还是事实上形成了隐藏第三路线？
- 模板是否被限制为 adapter，而没有偷偷决定 storyline、page types 或科学内容？
- `course-standard` 的来源保真、版权边界、annotation 排除、字体与 4:3 合同是否可执行？

### C. 核心架构

- semantic storyboard 与 page composition 的权责是否真正分离，还是仍然存在重复字段和第二套 `deck-plan.yaml` 风险？
- shared core、现有 research/business trigger 兼容和 teaching mode 是否是最小足够设计？
- domain / Clear Writing / scientific-visualization / renderer 的责任是否清楚？
- gold/reference library 从 hard gate 降为可选提示是否会造成新风险？

### D. TODO 全覆盖

逐项核对 tracking `#29`–`#48` 和 #29 子项：

- 是否每个条目都有真实机制、Gate、阶段或合理的 evidence-gated disposition；
- 是否存在同义重复、遗漏、错误 owner 或为了“全覆盖”而堆字段；
- #44 保持 evidence-gated 而不预建 geometry engine 是否合理；
- 045 已推广但后来仍回归的能力是否进入 regression bank，而不是被错误视为关闭。

### E. Capability Gate Matrix

独立审查 G1–G10：

- 是否覆盖 discovery/routing、核心语义、完整 artifact、两模板真实消费、citation/text layer、revision preservation、自然语言、review scope、fresh generalization 和 production identity；
- 是否有 gate 主要重复同一件事，应该合并；
- 是否漏掉关键用户能力或 should-not-change；
- normal entry、证据、明确失败、回归边界、final-candidate requirement 是否可执行；
- 是否可能被 schema、packet、测试特判、只跑最好一次、换候选或 reviewer 自签钻空子。

### F. 分期、风险与恢复

- Package A/B/C 是否仍然过大、顺序错误或隐含 architecture drift；
- 每包通过后新增的是真实能力还是更多 control artifacts；
- 现有 `presentations 0.3` 回滚边界、private source、generated layer、README/version/maturity closure 是否完整；
- 是否需要把某些项从当前 major round 拆成后续 amendment；不能仅因不安而拆，也不能把真实高风险塞进一个过大任务。

## Blocker 标准

只在满足 Critic Role Contract 的 blocker 条件时 REVISE：要求依据、直接证据、因果风险和最小关闭条件必须齐全，并涉及真实用户功能、证据/质量、数据/权限/费用/安全、破坏现有能力或执行合同缺口。不要因“更保险”、文档措辞偏好、可能有更多测试或可恢复的小风险单独阻塞。

## 期望输出

先用自然中文给用户可读的结论，再输出：

```text
RESULT = PASS | REVISE
REVIEW_OBJECT = PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0
REVIEWED_PATH = docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_0_2026-09-28.md
REVIEWED_COMMIT = 78901482243a877cdcec3150ca229b3fa58b7173
ARCHITECTURE_VERDICT = ...
TWO_TEMPLATE_VERDICT = ...
TODO_COVERAGE_VERDICT = ...
CAPABILITY_GATE_VERDICT = ...
MIGRATION_AND_RECOVERY_VERDICT = ...
READY_FOR_EXECUTION_PACKAGE = YES | NO
```

若 `REVISE`：

- 使用稳定 finding IDs；
- 每个 blocker 给要求、证据、风险和最小关闭条件；
- 区分 blocker 与 non-blocking note；
- 按 Critic contract 自动附完整 Planner prompt，要求 Planner 提交完整 V1.1，而不是零散补丁。

若 `PASS`：

- 明确 PASS 只批准 V1.0 架构与 Gate，不授权实现；
- 指出下一步应由 Planner 准备 Package A/B/C 的 execution package、Canonical Goal 与 Kickoff Draft，并重新送 execution-ready review；
- 不临场生成一个未被审查的新 Executor kickoff。

## Maintenance Board

当前 source entries 已有 tracking `#29`–`#48`。本线程若没有 GitHub Project mutation surface，不要声称已同步；请给 exact pending Project mutation，至少写清当前 Plan/commit 作为执行锚点、下一步 Critic/Planner handoff，以及哪些 issue 应保持当前生命周期。
