# 003 Presentations — Planner Review

reviewed_commit: `b2ac1b246007ee848ea058bc54bf9eaef1c3e1a0`
current_main_control_commit: `1d47db93dbe317076a483f94a7cd58b0312f93dd`
review_round: 1
decision: REVISE

## 结论

003 的主要目标已经实现：科研/学术内容不再自动等于 Beamer，用户明确要求 PPTX/PowerPoint/可编辑 Slides 时会进入可编辑演示路线；在 `presentation-desktop` 中未指定格式的组会、科研更新、论文报告等也默认按可编辑演示规划；明确要求 Beamer/LaTeX/.tex/学术 PDF 时仍保留 LaTeX 路线。文件生成后的 render + visual QA 也已经成为完成门槛，十插件 Marketplace 拓扑没有回退。

本轮仍有 **1 个阻断问题**，范围很小：冻结计划要求“中文 slide text 必须经过 `writing-fidelity` + `chinese-prose` 的终审，并由 presentation 路由明确表达这种协作”，但当前这一要求只写进了 `research-presentations`；共享 PPT 路由和 `business-presentations` 仍没有把中文演示文案的写作终审接起来。这样用户走 `business-presentations` 做中文管理层/产品/策略 PPT 时，虽然 `presentation-desktop` profile 安装了两个写作 skill，presentation 路由本身却没有要求实际调用它们，形成了同一 profile 内“能力存在但业务路线未接通”的缺口。

## 已通过的冻结要求

### 1. 输出格式已经由交付需求决定

当前 `research-presentations`、`ppt-skill-routing.md` 和 `template-routing.md` 已一致表达：

- “做 10 页组会 PPT，我后面还要自己改” → editable Presentation/Slides；
- “做组会 / research slides”，在 `presentation-desktop` 中未指定格式 → editable Presentation/Slides；
- “给我一份 Beamer / LaTeX slides / .tex / academic PDF” → Beamer/LaTeX；
- 只要故事线或逐页计划 → 可以停在 deck plan。

旧的 `academic/research -> LaTeX plus Beamer by default` 已从 source routing 中移除，没有看到以“科研”作为自动切 Beamer 的残留主规则。

### 2. 可编辑性和 deck-plan 信息已经增强

`deck-plan.schema.json` 现在显式记录 `metadata.editability`，并要求每页具有 `slide_purpose` 和 `visual_intent`。Markdown adapter 默认研究演示计划为 `pptx + editable`，显式 `tex` 则标为 `source-editable`。这满足冻结计划要求的 format/editability expectation、页面目的和视觉意图表达。

### 3. render + visual QA 已成为完成门槛

当前 `research-presentations` 明确要求文件创建后渲染到 PDF/图片并做视觉检查；`visual-qa.md` 明确检查标题信息、裁切/溢出、文字换行、对比度、层级、页面密度、图表/公式可读性、可编辑性和整套叙事连续性，并写明文件存在本身不能视为完成。

### 4. Marketplace / profile / generated layer 一致

`presentations` 仍是当前十个 Marketplace 插件之一；`presentation-desktop` 明确写成 editable PPTX/Slides default routing + writing final passes + visual QA。生成后的 presentations plugin snapshot 已同步本轮 source 修改，没有发现手改 generated layer 代替 source 的情况。

## Blocker 1 — 中文写作终审只接到了 research 路线，没有覆盖 business/shared presentation 路线

### 冻结依据

`003_presentations/PLAN.md` 明确要求：

> 中文 slide text 必须经过 `writing-fidelity` + `chinese-prose` 的终审；英文科研 slide text 可使用 `scientific-prose`。presentation profile 已包含这些能力，路由文档必须明确这是协作关系，不是重复造写作 skill。

### 真实证据

- `research-presentations/SKILL.md` 已明确写出中文 slide text 使用 `writing-fidelity` + `chinese-prose`，这一部分正确。
- `presentation-desktop.json` 确实安装了 `writing-fidelity`、`scientific-prose`、`chinese-prose`。
- 但当前 `business-presentations/SKILL.md` 的 workflow 只要求 deck plan、官方 Presentation/Slides 和 visual QA，没有中文写作终审 handoff。
- 当前共享 `ppt-skill-routing.md` 也没有给出“任何中文 presentation 文案 → writing-fidelity + chinese-prose”的通用协作规则。

因此自然语言请求：

> “给学院管理层做一份中文项目决策 PPT，文字别像 AI 模板，事实和数字不要动。”

会正确进入 `business-presentations`，但 presentation 路由没有把“事实保真 + 中文自然表达终审”接到该路线。依赖用户或执行器自己猜到要额外调用 writing skills，不满足冻结的显式协作合同。

### 最小修复

只修 presentation 内的写作 handoff，不重新打开 002：

1. 在共享 `ppt-skill-routing.md` 增加通用写作协作规则：中文 presentation 文案在相关 writing skills 已安装时，最终文案必须经过 `writing-fidelity` + `chinese-prose`；英文科研 presentation 文案可交给 `scientific-prose`。
2. 在 `business-presentations/SKILL.md` 的 Boundary 或 Workflow 增加一条明确 handoff，使中文 business/executive/strategy deck 同样遵守上述终审规则，而不是只靠 profile 中“恰好安装了这些 skill”。
3. 通过现有 marketplace 生成流程同步 `plugins/codex/plugins/presentations/**`。
4. 在 `tests/test_presentations.py` 增加回归断言，至少覆盖 business/shared route 的中文写作 handoff，防止以后只保留 research 路线。

不要复制 `chinese-prose` 的完整规则进 presentation skill，也不要新增 presentation/writing skill；这里只需要明确调用关系。

### 修复后验收

Planner 需要看到：

- `research-presentations`、`business-presentations` 与共享 routing 对中文 slide final pass 的职责一致；
- `presentation-desktop` 继续安装三项 writing skills；
- generated presentations plugin 同步；
- presentation tests、全库 validate/audit、marketplace build、unittest 和 `git diff --check` 继续通过；
- 修复提交与结果提交对应的 GitHub Actions 成功。

## 远端验证

Executor 报告的本地完整验证链通过：149 active skills、18 profiles、Marketplace build、provenance/icon checks、101 个单元测试和 `git diff --check` 均成功。

Planner 独立核对当前真实 GitHub Actions：

- 实现提交 `b2ac1b246007ee848ea058bc54bf9eaef1c3e1a0` 的 `Codex Marketplace` workflow：`completed / success`；
- 结果提交 `1d47db93dbe317076a483f94a7cd58b0312f93dd` 的 `Codex Marketplace` workflow：`completed / success`。

因此本轮不是 CI 阻断，而是上述单一冻结语义缺口。

## 下一步

保持在 `003_presentations`。Codex 只修 Blocker 1，重新生成、验证、push 并更新 `results/003_presentations/RESULT.md`；不要进入 004，也不要借返修扩大 Presentation 架构。修完后 Planner 再做 003 第二轮复核。
