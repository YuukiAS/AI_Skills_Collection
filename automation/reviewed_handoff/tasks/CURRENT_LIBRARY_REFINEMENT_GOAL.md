# 当前技能库有限整改 Goal

本文件定义本轮一次性的现有技能库整改范围。它不是长期 watcher 或持续 intake 流程；但本轮整改期间保留 GPT Planner 定时复核，让 Planner 在 Codex 每次推送后读取真实远端、GitHub Actions 和用户可见行为，决定 PASS、精确返修或推进到下一批。Planner 看不到明确阻断问题后即停止继续扩大范围。

目标是在当前仓库已有内容基础上，集中完成几轮 Planner → 实现 → 独立复核 → 精确返修，使当前高频能力和已有技能库达到可直接使用、边界清楚、文档与生成层一致的状态，并作为一次可安装的正式版本收尾。本轮不处理新的 Notion 候选、外部 repo 或 Type=Research 候选。

## 执行顺序

1. `001_research_writing`：科研论文写作、文献检索和引用边界。其冻结计划位于 `automation/reviewed_handoff/tasks/001_research_writing/PLAN.md`。
2. `002_writing_style`：整理 `writing-style`，把保真、中文“说人话”、降低 AI 味、科研英文表达三层边界和调用方式理顺。
3. `003_presentations`：整理研究/商业演示工作流，修正当前“学术默认 Beamer”与桌面可编辑 PPTX/Slides 工作流之间的矛盾，并把叙事、写作终审、可编辑性和视觉验收接起来。
4. `004_current_library_acceptance`：不再主动扩展能力，只检查前三批修改后的整个当前仓库是否还有明显阻断问题；发现明确问题时做有限返修，没有明显问题时进入版本发布与真实安装验收。

## Planner 与 Codex 的阶段交接

本轮不使用常驻 watcher。Planner 与同一个 Codex Goal 通过 GitHub tracked files 交接，避免 Codex 自己兼任 Planner。

每个阶段 `<task_key>` 使用：

- 冻结合同：`automation/reviewed_handoff/tasks/<task_key>/PLAN.md`
- Codex 执行结果：`results/<task_key>/RESULT.md`
- GPT Planner 当前审阅：`results/<task_key>/PLANNER_REVIEW.md`

Codex 完成一个阶段实现后必须先 push `main`，再写/更新 `RESULT.md`，至少记录：

- 本阶段实现前的基线提交；
- 实际实现提交；
- 具体修改了什么；
- 本地测试/生成/安装检查结果；
- 仍然已知的限制；
- 当前是否等待 Planner。

定时 GPT Planner 只在看到新的 `RESULT.md` / 新实现提交后做审阅。它必须读取真实 diff、相关 source、测试和 GitHub Actions，而不是照抄 RESULT。审阅写入 `PLANNER_REVIEW.md`，至少包含：

- `reviewed_commit`；
- `decision: PASS | REVISE | WAIT_CI | BLOCKED | ACHIEVED`；
- 如果 `REVISE`，每个 blocker 的冻结依据、真实证据、最小修复和修复后验收方式；
- 如果 `PASS`，明确下一阶段 task_key；
- `004` 只有满足版本、CHANGELOG、真实安装与 GitHub Actions 门槛后才允许 `ACHIEVED`。

Codex 不能在等待 Planner 时自行宣布 PASS。它只能：

- `REVISE` → 只修 Planner 列出的 blocker，重新验证、push、更新 RESULT；
- `PASS` → 进入下一阶段冻结 PLAN；
- `WAIT_CI` → 不改源码，等待 Planner 下一轮读取远端 Actions；
- `BLOCKED` → 停止并报告用户；
- `ACHIEVED` → 结束整个 Goal。

为避免无意义 token 消耗，Codex 等待 Planner 时不得反复重新分析整个仓库；只需要低频检查远端 `PLANNER_REVIEW.md` 是否针对新的实现提交发生变化。Planner 也不得在没有新实现、CI 状态变化或实际 blocker 的情况下重复写相同 review。

## 复核方式

每个批次都必须先按对应 `PLAN.md` 实现，再由与实现步骤分离的 GPT Planner/Reviewer 定时检查真实远端 diff、当前技能说明、用户自然语言调用案例、GitHub Actions 和完整测试。复核只允许阻断：

- 冻结计划没有实现；
- 用户自然表达仍明显会走错能力；
- 修改引入已有行为回归；
- 文档、profile、plugin、生成层与 source 不一致；
- 用户可见产物或最终报告仍然难读、像日志或无法说明实际变化；
- 当前发布版本、CHANGELOG、生成层版本或安装结果不一致；
- GitHub Actions / 必需检查失败；
- 从最终 `main` 无法实际安装或升级本轮主要用户入口。

“还可以更优雅”“可以再加一个新抽象”“以后可能扩展”不能作为继续返修的理由。

整个 Goal 最多进行 8 次 Planner review/repair 循环，不要求用满。任何阶段 Planner 已看不到明确阻断问题就结束该阶段；`004` 完成正式版本与安装验收后整个 Goal 立即结束。

## 版本与发布门槛

当前中央 Marketplace 插件与 Source CLI package 版本均为 `4.0.0`。本轮包含科研写作路由、写作风格和 Presentation 用户可见行为的明显增强，但不破坏现有六插件拓扑，因此冻结本轮目标版本为：

`4.1.0`

最终阶段必须：

- 将 `setup.py` 的 CLI package 版本更新为 `4.1.0`；
- 将 `scripts/codex_marketplace_config.json` 中 6 个中央 Marketplace 插件版本统一更新为 `4.1.0`；
- 通过既有生成流程刷新 `.agents/plugins/marketplace.json` 与 `plugins/codex/plugins/`，不得手改生成层来伪造版本；
- 将 `CHANGELOG.md` 的 `Unreleased` 内容整理进 `4.1.0` 发布记录，并明确写入本轮科研写作、writing-style、Presentation 路由/QA 变化以及已有 server-install smoke 改进；
- README / 安装文档如仍展示旧版本语义或与实际安装方式冲突，必须同步修正；
- 不创建新顶级 plugin，仅发布现有 6 个中央插件的新版本。

## 真实安装验收

“源码测试通过”不等于本轮 Goal 完成。最终 `main` 必须能被用户实际安装。

至少做以下干净环境 smoke test：

1. **Marketplace 插件路径**：使用临时、隔离的 `CODEX_HOME` 或仓库现有等价 smoke 环境，从最终 `main` 添加/刷新 Git marketplace，并实际安装或升级本轮最相关的 `writing-style` 与 `research-writing`；确认安装到的插件版本为 `4.1.0`，技能文件完整、路径有效、生成 payload 可读。
2. **Presentation profile 路径**：使用 Source CLI 在临时目标中实际安装 `presentation-desktop`，确认 `research-presentations`、`business-presentations`、`writing-fidelity`、`scientific-prose`、`chinese-prose` 及 secondary skills 按 profile 进入目标环境，并通过仓库已有安装验证。
3. 如果仓库已有 `ai-skills verify-server-installation` 或等价安装 smoke 命令，应纳入最终验收，而不是只做静态文件检查。

不得把“脚本理论上可以安装”当作成功；必须执行真实安装 smoke，并在最终报告中写清命令、结果和安装到的版本。

## GitHub Actions 完成门槛

每个重要 push 后都要查看真实 GitHub Actions。最终 `ACHIEVED` 前：

- 当前 `main` 的所有与本仓库相关的必需 workflow/check 必须完成且成功；
- 不允许用本地测试代替远端 Actions；
- 如果 workflow 仍 pending，不能宣布完成；
- 如果失败是本轮修改造成的，必须继续修复并重新推送；
- 如果确属 GitHub 服务外部故障，必须报告 `BLOCKED`，不能伪造 `PASS`。

## 本轮明确不做

- 不处理新的 Notion / AI Resources 候选。
- 不处理新的外部 skill repo。
- 不处理尚未进入本轮计划的 Research 候选。
- 不为了填满插件市场而新建顶级 plugin；`marketplacePluginBudget=6` 保持不变。
- 不建立新的长期 watcher、新状态机或新的长期自动化框架。
- 不因为 Provider/库名很多就大规模删除现有 active skill。

## 最终用户报告必须长什么样

最终报告首先是给人看的，不是提交记录或测试日志。正文必须先用自然中文说明：

1. **这轮到底修了什么**：按科研写作、写作风格、Presentation 等用户能力分组说明。
2. **以前哪里不好用，现在有什么变化**：描述用户可感知的行为差异，不只列文件名。
3. **现在怎么用**：给出一组真实 `example usage`，包括正常应该触发的请求，以及至少几个容易混淆的反例。
4. **哪些方案没有采用，为什么**：例如没有新增 skill/plugin、没有继续使用某个默认路线时，要说清理由。
5. **还有什么限制或回归风险**：如果没有明显风险，也要明确说明核查范围。
6. **这次发布了什么版本、如何证明能安装**：明确 `4.1.0`、Marketplace 插件真实安装结果、`presentation-desktop` profile 安装结果和 GitHub Actions 状态。

技术附录再列 commit、修改文件、版本文件、CHANGELOG、测试、CI、安装 smoke、生成命令和最终 `git status`。不能让用户必须读技术附录才能知道本轮是否真正变好。

只有同时满足以下条件才允许最终输出 `PLANNER_PASS / ACHIEVED`：

- 001–003 的用户级问题通过 Planner 复核；
- 004 全库抽查无明确 blocker；
- `4.1.0` 版本和 CHANGELOG 已落地；
- source / registry / catalog / Marketplace 生成层一致；
- 最终 GitHub Actions 全部成功；
- `writing-style`、`research-writing` 的 Marketplace 真实安装/升级 smoke 成功；
- `presentation-desktop` 的 Source CLI 真实安装 smoke 成功；
- `HEAD = origin/main` 且 working tree clean；
- 最终用户报告已经生成且包含 example usage、before → after 和安装说明。
