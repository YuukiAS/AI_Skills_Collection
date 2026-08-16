---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 004_current_library_acceptance
decision: PLAN_FROZEN
---

# 004 Current Library Acceptance — Plan

## 目标

在 001–003 完成后，对当前技能库做最终验收。这里的“完成”不是理论上再也不能改，而是：当前仓库已有内容没有明显用户级阻断问题，主要入口和高频能力可自然调用，source/profile/plugin/generated 层一致，README/安装路径可用，版本与 CHANGELOG 完整，真实 GitHub Actions 通过，而且用户能够从最终 `main` 实际安装本轮发布的新版能力。

本阶段同时负责把本轮整改收尾成正式 `4.1.0`。只有发布、远端检查和真实安装 smoke 都通过，才能宣布 `ACHIEVED`。

## Planner 必须重新读取

至少重新检查：

- `README.md`
- `AGENTS.md`
- `CHANGELOG.md`
- `setup.py`
- `registry.json`
- `profiles/README.md` 与当前推荐 profiles
- `scripts/codex_marketplace_config.json`
- 6 个 marketplace plugin 的当前生成结果
- `.agents/plugins/marketplace.json`
- `docs/audits/ACTIVE_SKILL_CAPABILITY_MAP.md`
- `docs/audits/ACTIVE_SKILL_CALLING_AUDIT.md`
- 001–003 的冻结计划、真实实现 diff、结果/复核记录
- 001–003 实际修改过的 source skills 和测试
- 当前 GitHub Actions / checks

不要依赖 Codex 自己的总结代替真实文件、diff、workflow 和安装结果。

## 什么算阻断问题

只有以下问题可以继续要求返修：

1. **调用明显错误**：用户用正常自然语言提出高频任务，仍然容易进入错误 skill/aggregate，或必须知道内部 skill 名才能完成本来应该自然可达的任务。
2. **公开承诺与实际行为矛盾**：README、profile、plugin 或 skill 说明承诺一种工作流，但实际路由规则相反。例如“editable PPTX”与实际默认 Beamer 冲突。
3. **高频能力边界仍互相吞噬**：尤其是科研写作/评审/文献、writing-style、Presentation 三块在 001–003 后仍有明显同义触发。
4. **source / generated 不一致**：手工源文件、registry、catalog、marketplace/plugin 生成层互相矛盾或未更新。
5. **安装路径不可用**：README 推荐的主要 profile/plugin/CLI 路线明显失效，或实际 smoke 无法从最终 `main` 安装。
6. **用户可见质量门槛缺失**：例如写作“技术上完成但仍像日志”、PPT“文件生成但未 render/QA”、最终报告不能解释用户实际获得了什么。
7. **安全边界明显回归**：当前 clinical/medical 等已有安全约束被高层入口遮蔽或删除。
8. **版本发布不一致**：CLI、6 个 Marketplace 插件、生成层、CHANGELOG 或 README 对本轮正式版本说法不一致。
9. **GitHub Actions / tests 失败或工作树不干净**。
10. **真实安装验收未完成**：不能证明新版 `writing-style`、`research-writing` Marketplace 插件和 `presentation-desktop` profile 从最终 `main` 可安装。

以下不能阻断：

- 理论上可以再拆一个 skill；
- 某个冷门 provider skill 以后可以有更好的 aggregate；
- 可以增加更多示例、更多文档或更漂亮的架构；
- 新的 Notion / Research / 外部 repo 候选尚未处理；
- 未来新增能力需要新的 profile/plugin。

## 最终全库抽查

不要求重新人工逐字审完 149 个 skill，但必须利用现有 149/149 审计结果，对高风险类别做抽查：

- 论文写作、审稿、投稿
- 文献搜索、引用核验、BibTeX/Zotero
- writing-style：保真、中文自然表达、英文科研表达
- research/business presentations
- PDF/OCR/文档转换边界
- visualization/diagram/image 的明显入口冲突
- medical imaging
- bioinformatics
- data science/statistics
- frontend
- clinical medicine 安全边界
- skill/plugin/profile 维护路径

如果现有审计中某项只是“插件市场未覆盖”，不能自动当成调用失败；继续区分安装可达性和已安装后的自然调用性。

## 4.1.0 发布要求

当前中央插件和 Source CLI package 是 `4.0.0`。本轮冻结正式版本为 `4.1.0`。

Codex 必须在本阶段完成：

- `setup.py` → `4.1.0`；
- `scripts/codex_marketplace_config.json` 中 6 个中央插件全部 → `4.1.0`；
- 使用现有生成脚本刷新 Marketplace / plugin generated layer；
- `CHANGELOG.md` 增加明确的 `4.1.0` 发布记录，日期使用实际发布日期，并把原 `Unreleased` 中已完成的 server-local installation smoke 改进纳入该版本；
- CHANGELOG 还必须概括本轮 001–003 的用户可见变化：科研写作/文献路由、writing-style 中文“说人话”与英文科研表达、Presentation editable PPTX/Beamer 路由与 render/visual QA；
- README 或安装文档如需要说明新版行为，做最小同步；
- 不创建新的顶级 plugin，`marketplacePluginBudget=6` 保持不变。

这是一次 minor release，不是 breaking release；不得借版本升级扩大技能拓扑。

## 真实安装验收

必须在隔离临时环境实际执行，不接受纯静态检查替代。

### Marketplace

从最终 `main` 添加或刷新 Git marketplace，并实际安装/升级：

- `writing-style`
- `research-writing`

验收：

- 安装成功；
- 安装到的 plugin metadata 版本为 `4.1.0`；
- 生成 skill 文件与 source 一致；
- 关键 artifact 路径有效；
- 不依赖开发 checkout 中偶然存在的文件。

如果当前 Codex CLI 的具体 plugin 命令与 README 不同，以本机真实 `codex plugin --help` / 当前官方 CLI 行为为准，必要时同步 README，但不得伪造安装成功。

### Presentation profile

通过 Source CLI 在干净临时目录实际安装：

`presentation-desktop`

验收至少确认以下能力进入目标环境：

- `research-presentations`
- `business-presentations`
- `writing-fidelity`
- `scientific-prose`
- `chinese-prose`
- profile 定义的 secondary skills

并运行仓库已有安装验证/smoke 检查。若 `ai-skills verify-server-installation` 适用于该路径，纳入验证。

## 完整验证

必须运行当前仓库要求的完整验证链，至少包括：

- registry/catalog 重新生成与一致性检查
- `python3 scripts/skills.py validate`
- `python3 scripts/skills.py audit --all`
- marketplace build/validate/check
- provenance/icon 现有检查
- `python3 -m unittest discover -s tests`
- `git diff --check`
- 上述真实安装 smoke
- GitHub Actions/CI
- 最终 `git status` clean
- 最终 `HEAD = origin/main`

如果命令在当前环境需要其他兼容入口，可以使用当前仓库真实命令，但不能降低检查范围。

## GitHub Actions 规则

Planner 必须读取当前最终 `main` 对应的真实 workflow/check 状态。

- pending/running：不能 PASS，等待下一次 Planner 复核；
- failure：如果由本轮修改造成，给 Codex 明确最小返修项；
- 外部服务故障且无法可靠判断：BLOCKED，不得伪造 PASS；
- 只有最终 required workflows/checks 成功，才进入最后安装/发布结论。

本地 validation 通过不能代替 GitHub Actions。

## 达标与停止规则

Planner/Reviewer 对当前 HEAD 做独立复核：

- 若发现上述明确阻断问题：输出最小、具体、可验证的 repair list，Codex 只修这些问题，然后再复核。
- 若没有明确阻断问题，但 GitHub Actions 仍未成功或真实安装 smoke 未完成：继续保持未达标，不得输出 `ACHIEVED`。
- 只有 001–003 通过、全库抽查通过、`4.1.0`/CHANGELOG 完整、GitHub Actions 全绿、Marketplace 与 `presentation-desktop` 真实安装 smoke 成功后，结论才允许是 `PLANNER_PASS` / `ACHIEVED`。
- 不得因为“还可以继续优化”而保持 Goal 活跃。
- 整个有限整改 Goal 的 Planner review/repair 总轮数上限为 8；达到上限仍有阻断时，停止并把未解决问题明确列给用户，不得无限循环。

## 最终报告格式

最终报告必须先写给用户看，再写技术附录。正文顺序固定为：

### 1. 这轮修了什么

按用户能力分组，不按 commit 分组。至少覆盖：

- 科研写作与文献
- 写作风格 / 中文“说人话” / 英文科研表达
- Presentation
- 其他在最终验收中实际修到的明显问题

### 2. 以前哪里不好用，现在有什么变化

每一组都要解释可感知的 before → after。例如：

- 以前“帮我评价论文”可能在 peer review 和 rubric evaluation 之间抢入口；现在如何分。
- 以前中文报告容易出现普通英文流程词和日志先行；现在如何处理。
- 以前 research presentation 因“学术”默认 Beamer；现在格式如何按实际交付需求选择。

### 3. Example usage

必须给真实自然语言示例，不得只写 skill 名。至少包括 9 个示例，覆盖：

- 写论文/改 Results
- 整篇论文结构规划
- 投稿前 reviewer-style 检查
- 找最新论文
- 核验引用
- 中文报告“说人话”
- 英文科研文字去模板腔
- 做可编辑组会 PPT
- 明确要求 Beamer 的情况

每个示例简要说明预期入口/行为和用户会得到什么。

### 4. 没采用什么，为什么

例如：

- 为什么没有新增 humanizer skill；
- 为什么没有新增 presentation plugin；
- 为什么没有把所有相邻 skill 直接 merge/delete；
- 为什么没有继续处理新的 Notion/Research 候选。

### 5. 发布与安装结果

必须明确写：

- 正式版本 `4.1.0`；
- `writing-style` Marketplace 安装/升级 smoke 结果；
- `research-writing` Marketplace 安装/升级 smoke 结果；
- `presentation-desktop` Source CLI 安装 smoke 结果；
- 最终 GitHub Actions 状态。

### 6. 剩余限制与风险

区分真正限制和未来优化建议。不能为了显得完整制造无意义 backlog。

### 7. 技术附录

最后再列：

- 最终 HEAD
- 重要 commits
- 修改文件范围
- 版本文件 / CHANGELOG
- 生成命令
- tests/CI
- 安装 smoke 命令和结果
- final `git status`

用户不读技术附录也必须能理解这轮是否达标、修了什么、现在怎么用。

## 本任务不做

- 不处理新的外部内容 intake。
- 不为了“全覆盖”新增顶级 plugin。
- 不重构 Reviewed Handoff 本身。
- 不创建长期 watcher 或后台服务。
- 不继续启动下一轮开放式优化。
