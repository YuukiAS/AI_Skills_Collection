# README Human-Facing Refactor — Canonical Goal

- Execution package version: `v0.1`
- Exact task: `readme_human_facing_refactor`
- Exact repository: `YuukiAS/AI_Skills_Collection`
- Exact branch: `reviewed/readme_human_facing_refactor`
- Exact worktree: `/tmp/ai-skills-readme-human-facing-refactor`
- Approved design authority: `docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_2_2026-09-20.md` v0.2
- Approved design commit: `f3e7ec12db8c1704d919e6124c9875babd67bb97`
- Execution Plan: `docs/design/readme/README_HUMAN_FACING_REFACTOR_EXECUTION_PLAN_V0_1_2026-09-20.md` v0.1
- Kickoff Draft: `docs/operations/prompts/README_HUMAN_FACING_REFACTOR_V0_1_KICKOFF.md` v0.1
- State before execution-ready Critic PASS: `DO_NOT_EXECUTE`

本文件是本任务的顶层 completion contract。只有独立 Critic 对同版 Plan + Goal + Kickoff 给出 execution-ready PASS，且用户实际发送获批 Kickoff 后，才允许开始 implementation。

## 1. 最终交付目标

把根 `README.md` 重构为简洁、美观、真正给人看的项目首页，而不是内部 workflow、维护和命令手册。

最终 README 必须让访问者快速看见：

- 项目是什么；
- 当前 Repository / CLI version；
- 十个中央 plugin；
- 每个 plugin 的显示名、当前版本和一句自然中文用途；
- 一个最小使用入口；
- 2–4 个真正有用的现有文档入口。

## 2. 唯一允许修改的文件

最终 tracked diff 只能包含：

1. `README.md`
2. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
3. `docs/workflows/CRITIC_ROLE_CONTRACT.md`

任何第四个 tracked 文件变化都必须先停止并回 Planner。

## 3. README 必须完成的内容

### 3.1 Hero

项目名 + 一句自然中文说明。避免长篇品牌文案和内部 workflow 术语。

### 3.2 Repository / CLI current version

必须从执行时 `VERSION` 核对并显示当前值。

当前 design/package 快照中为 `5.0.5`，但执行时 `VERSION` 才是 authority。

只保留当前版本，不恢复历史版本、maturity 或 release process。

### 3.3 十个中央 plugin gallery

必须覆盖全部十个中央 plugin。

每个 plugin 至少展示：

- 本地 SVG；
- `displayName`；
- `version`；
- 一句自然中文用途。

`displayName` 和 `version` 必须来自执行时 `scripts/codex_marketplace_config.json`。

一句用途不得扩大实际能力，不得为了 marketing 写成超出 Marketplace/真实 source 的能力承诺。

### 3.4 布局

优先两列 gallery。

若真实 GitHub render 显示两列在宽/窄或 light/dark 下不自然，Executor 必须在同一范围内自行退回：

`two-column -> one-column -> simpler native Markdown/HTML`

不需要为这种普通呈现调整回 Planner。

禁止引入：

- 外部 badge；
- 自定义 CSS；
- README generator；
- 新 schema；
- 新 build chain；
- README 专用 runtime。

### 3.5 最小使用入口

只保留一个短入口，例如 Marketplace source 或 Profiles/安装链接。不能重新形成安装教程。

### 3.6 Documentation footer

只链接 2–4 个已有具体入口。优先考虑：

- `profiles/README.md`
- `docs/LOCAL_CONFIGURATION.md`
- `TODO.md`
- `CHANGELOG.md`

不得新建 docs portal/index。

## 4. README 必须移除的内容

最终 README 不再承载：

- 真实项目 refinement 长教程；
- NEW TODO 模板；
- “项目 thread 要写多复杂”等内部流程说明；
- Planner / Critic 初始化或复制 prompt；
- handoff / multi-plugin / incident 教程；
- Profile 完整命令墙；
- Server/HPC 命令墙；
- Presentation/CUHK 详细运行合同；
- 目录逐项说明；
- 提交前验证命令墙；
- 重复 Marketplace 安装说明；
- repository 历史版本、maturity 表与内部 release 流程。

## 5. Role Contract cleanup

只允许做两处语义等价的 authority cleanup：

- `PLANNER_ROLE_CONTRACT.md` §10.1：不再说下一条 Critic prompt 以 README 模板为骨架；
- `CRITIC_ROLE_CONTRACT.md` §6.2：不再说下一条 Planner prompt 以 README 模板为骨架。

改后应明确下一角色 prompt 由当前项目设置、对应 Role Contract、Active Context 和当前 package/review locator 自包含生成。

必须保持：

- 自动附下一角色 prompt 的要求；
- prompt 必须填当前真实上下文；
- 不把定位工作甩给用户；
- PASS/REVISE 与角色职责；
- 既有 handoff machine-readable 形态。

不得顺手修改其他治理语义。

## 6. 直接验收

全部完成条件：

1. `README.md` 明显短于当前版本，并成为人类首页而不是维护手册。
2. README 当前 Repository / CLI version == `VERSION`。
3. README 恰好覆盖当前十个中央 plugin。
4. 每个 plugin display name/version == `scripts/codex_marketplace_config.json`。
5. 用途文案自然、简短、没有能力扩张。
6. 所有引用的本地 SVG 路径存在且在 GitHub 页面实际显示。
7. README 中不再出现批准移除的 Planner/Critic prompt、incident、HPC、Presentation、验证命令墙等内容。
8. 两个 Role Contract 不再依赖 README template。
9. 两个 Role Contract 的 handoff 职责与语义保持不变。
10. `git diff --name-only` 仅包含三个批准文件。
11. Repository bump = `NONE`。
12. 所有中央 plugin = `NO_BUMP`。
13. 没有 production/generated/profile/Bridge Kit 变化。

## 7. 真实 GitHub 视觉验收

最终 candidate 必须直接在已 push 的 exact task branch 上查看真实 GitHub README 页面，而不是只看本地 Markdown。

至少留下足够证据判断：

- 宽窗口；
- 较窄窗口；
- 浅色主题；
- 深色主题。

真实 GitHub 页面若显示布局问题，Executor 在允许的 fallback 内自行修正并重新观察，直到合格。

Markdown syntax、CI、本地 HTML 或自制 renderer 不能替代这一验收。

如果执行环境完全缺乏访问/观察真实 GitHub 页面的浏览能力，明确报告 environment blocker；不得伪造 visual PASS，也不要把普通排版判断直接甩给用户。

## 8. Git / 授权边界

用户发送经 Critic PASS 的 Kickoff 后，允许：

- ordinary fetch/read；
- 从合法 base 创建 exact branch `reviewed/readme_human_facing_refactor`；
- 创建 exact task-owned worktree `/tmp/ai-skills-readme-human-facing-refactor`；
- 只修改三个批准文件；
- 为本任务运行必要的内容检查、现有 tests、真实 GitHub render/check；
- ordinary stage/commit；
- ordinary non-force push 到 exact task branch。

不允许：

- merge `main`；
- force push / history rewrite；
- 修改其他 branch/tag；
- paid API；
- provider/credential/private artifact；
- plugin production/generated mutation；
- Bridge Kit mutation；
- 新外部 side effect。

## 9. 版本决策

Repository bump decision: `NONE`

所有中央 plugin：`NO_BUMP`

本任务不得修改 `VERSION`、Marketplace plugin versions 或 versioning policy。

## 10. 完成与停止

满足全部内容、diff 与真实 GitHub视觉验收后：

- commit/push exact task branch；
- 报告 final candidate commit；
- 报告最终布局类型；
- 报告 VERSION / Marketplace parity；
- 给出真实 GitHub wide/narrow + light/dark visual evidence locator；
- 停止等待独立 implementation review。

不得 merge main，不得自行宣称 repository release 或总体项目完成。

若需要修改三个文件以外的 source、改变 Role Contract 实质语义、引入新构建链、修改 plugin icon/source，或出现无法从当前 authority 裁定的冲突，停止并回 Planner。
