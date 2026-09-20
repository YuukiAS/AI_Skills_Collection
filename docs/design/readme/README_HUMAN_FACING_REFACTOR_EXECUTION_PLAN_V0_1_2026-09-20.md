# README Human-Facing Refactor — Execution Plan

- Execution package version: `v0.1`
- Task key: `readme_human_facing_refactor`
- Status: `READY_FOR_EXECUTION_CRITIC_REVIEW`
- Approved design authority: `docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_2_2026-09-20.md` v0.2
- Approved design commit: `f3e7ec12db8c1704d919e6124c9875babd67bb97`
- Design Critic result: `PASS`（由用户转交；未单独写入 repo）
- Closed findings: `README-R1`, `README-R2`
- Source snapshot rechecked for this package: `main@7ff00f9fafb8e8e71686ce3fb1f65bc9a2abe8f2`
- Canonical Goal: `docs/goals/README_HUMAN_FACING_REFACTOR_V0_1_GOAL.md`
- Kickoff Draft: `docs/operations/prompts/README_HUMAN_FACING_REFACTOR_V0_1_KICKOFF.md`

本 Plan 只把已经通过独立 Critic 设计审查的 v0.2 转成可执行合同，不重开 README 架构。本文件不授权 implementation。只有独立 Critic 对本 v0.1 Plan + Goal + Kickoff 同版给出 execution-ready PASS，且用户实际发送获批 Kickoff 后，才允许开始执行。

## 1. 产品目标

把根 `README.md` 从内部流程、安装说明和维护教程混杂的长文档，收敛成真正给人看的项目首页。首页必须短、清楚、视觉上有辨识度，并让第一次访问仓库的人快速理解：

1. 这个仓库是什么；
2. 当前 Repository / CLI release；
3. 十个中央 plugin 的显示名、当前版本和一句自然中文用途；
4. 从哪里开始使用；
5. 需要更多信息时去哪里找。

不把 README 继续当 Planner / Critic prompt 仓库、HPC 手册、Presentation 运行合同、验证命令清单或 plugin refinement 教程。

## 2. Exact execution identity

后续若本 package 获 execution-ready PASS，用户发送获批 Kickoff 时授权：

- repository: `YuukiAS/AI_Skills_Collection`
- task: `readme_human_facing_refactor`
- base: 届时最新、仍包含本获批 execution package 且没有相关语义漂移的 `origin/main`
- branch: `reviewed/readme_human_facing_refactor`
- task-owned worktree: `/tmp/ai-skills-readme-human-facing-refactor`

若 exact branch 已存在且 ownership 不清，或 worktree 路径已被非本任务内容占用，停止并回 Planner；不得自行换 branch 名或复用未知 worktree。

## 3. 唯一允许修改的 tracked 文件

只允许修改：

1. `README.md`
2. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
3. `docs/workflows/CRITIC_ROLE_CONTRACT.md`

两个 Role Contract 只允许删除对 README prompt template 的依赖，使其改为依据当前项目设置、对应 Role Contract、Active Context 和当前 package/review locator 自动生成下一角色 prompt。

必须保持：

- Planner / Critic 的职责边界不变；
- handoff 语义不变；
- PASS / REVISE 语义不变；
- 自动生成下一角色 prompt 的要求不变；
- 现有 machine-readable handoff 形态不变。

不得借此重写 Role Contract 其他章节。

## 4. 明确禁止修改

不得修改：

- `AGENTS.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `VERSION`
- `scripts/codex_marketplace_config.json`
- `.agents/plugins/marketplace.json`
- `plugins/codex/plugins/`
- `skills/`
- `profiles/`
- Bridge Kit
- Reviewed Handoff schema/state
- plugin production behavior
- 任何 provider / credential / paid API / private artifact

本任务不是 production plugin refinement，不设计或执行 Plugin Capability Gate Matrix。

## 5. README 冻结内容合同

### 5.1 Hero

只保留项目名和一句自然中文说明。可以使用非常短的英文副标题，但只有确实改善整体观感时保留。禁止长篇使命宣言和内部流程术语。

### 5.2 当前 Repository / CLI version

README 必须轻量显示当前 Repository / CLI release。

实现时从 `VERSION` 读取并核对。当前已知值是 `5.0.5`，但 Executor 不得把本 Plan 中的值当成比执行时 `VERSION` 更高的 authority。

不恢复版本历史、maturity 表或内部 release 过程。

### 5.3 Plugin Gallery

十个中央 plugin 的：

- `displayName`
- `version`

必须来自执行时当前 `scripts/codex_marketplace_config.json`。

每个 plugin 只显示：

- 现有本地 SVG 图标；
- UI 名称；
- 当前 plugin version；
- 一句自然中文用途；
- 如确有定位价值，可用弱化的小字保留 plugin slug。

用途文案可以为阅读性做轻量中文润色，但不能扩大或改写真实 plugin 能力。

### 5.4 布局策略

首选两列 gallery，但两列不是必须守住的形式。

真实 GitHub render 若出现以下问题，可以在同一批准范围内自行调整：

`two-column -> one-column -> simpler native Markdown/HTML layout`

退回条件包括：

- 横向滚动；
- 卡片挤压到难以阅读；
- 图标或文字比例失衡；
- 较窄窗口下视觉层级崩坏；
- light/dark 任一主题出现明显对比或可读性问题。

不得为了保住两列引入外部 badge、自定义 CSS、README generator、新 schema、新 build chain 或 README runtime。

### 5.5 最小使用入口

只保留一个很短的使用入口。可以是一行 Codex Marketplace source，或一个安装 / Profiles 链接；不得重新展开为完整安装手册或命令墙。

### 5.6 Documentation footer

只从现有真实文档中选择 2–4 个短链接。优先候选：

- `profiles/README.md`
- `docs/LOCAL_CONFIGURATION.md`
- `TODO.md`
- `CHANGELOG.md`

不新增 `docs/README.md`，不新增 docs portal/index/generator。

## 6. 必须从根 README 移出的内容

删除或移出首页，不折叠隐藏：

- “真实项目怎么反过来改进插件”的长维护教程；
- “项目 thread 要写多复杂？不用复杂”及 NEW TODO 模板；
- Planner / Critic 初始化、复制 prompt、handoff 教程；
- 多插件并行和 incident triage 教程；
- Profile 完整安装命令列表；
- Server/HPC 命令墙；
- Presentation/CUHK 模板详细运行合同；
- 目录逐项解释；
- 提交前完整验证命令墙；
- 重复 Marketplace 安装说明；
- repository 历史版本、maturity 表和内部 release 流程。

## 7. 实施顺序

1. 核对当前 branch/base、`VERSION`、Marketplace config、三个允许修改文件及本 package authority。
2. 建 exact task branch/worktree；保护 unrelated dirty state。
3. 先重构 `README.md` 的信息结构和文字，不碰 production/plugin/generated source。
4. 对两个 Role Contract 做最小 dependency cleanup，只替换 README-template authority 表述。
5. 运行内容一致性检查：
   - Repository / CLI version == `VERSION`；
   - 十个 display name/version == Marketplace config；
   - SVG 相对路径存在；
   - README 不再包含已批准移出的内部流程段落；
   - Role Contract 不再引用 README prompt template。
6. ordinary commit + non-force push exact task branch。
7. 在 GitHub 上直接查看该 branch 的真实 README 页面，并采集宽/窄、浅/深视觉证据。
8. 若视觉有普通排版问题，在本 Plan 允许的 fallback 内自行修正、重新 commit/push、重新看真实 GitHub render。
9. 直到内容和视觉都满足 Goal，再提交最终 result/evidence；不 merge main。

## 8. GitHub 实际 render 验收

Markdown syntax、lint、CI 或本地 HTML 不能替代真实 GitHub 页面。

Executor 必须在已经 push 的 exact task branch 上直接查看 GitHub README render，并提供足够证据判断：

- 宽窗口；
- 较窄窗口；
- 浅色主题；
- 深色主题。

可以使用当前执行环境已有的浏览器、Playwright/Chromium、截图或等价浏览能力访问**真实 GitHub branch 页面**；不得为了本任务新增 README renderer 或前端构建链。

若执行环境完全没有可访问真实 GitHub 页面并截图/观察的浏览能力，这是 environment blocker，应明确报告；不得用本地自制 HTML、Markdown parser 截图或 CI PASS 冒充真实 GitHub render。普通布局不美观但浏览能力正常时，Executor 必须自己在批准的 fallback 内调整，不把排版调试甩给用户。

## 9. 验收清单

最终 candidate 必须同时满足：

1. `README.md` 是短、面向人的项目首页，不再像 workflow/维护手册。
2. Repository / CLI current version 与 `VERSION` 完全一致。
3. 十个中央 plugin 全部出现。
4. display name/version 与 `scripts/codex_marketplace_config.json` 完全一致。
5. 每个 plugin 一句自然中文用途不扩大真实能力。
6. 所有使用的本地 SVG 路径存在，并在 GitHub 页面正常显示。
7. 两列/一列/native 最终布局通过真实 GitHub wide/narrow + light/dark 观察。
8. README 不再包含获批移除的 Planner/Critic prompt、incident、HPC、Presentation、验证命令墙等内容。
9. `PLANNER_ROLE_CONTRACT.md` §10.1 与 `CRITIC_ROLE_CONTRACT.md` §6.2 不再依赖 README template。
10. 两个 Role Contract 的其他职责与 handoff 语义没有漂移。
11. 最终 diff 只涉及三个批准文件。
12. 无 plugin production/generated/profile/version policy 变化。

## 10. 版本决策

Repository bump decision: `NONE`  
Reason: README + workflow-doc dependency cleanup；没有新的 repository-level capability 或安装合同变化。

Affected plugins:

- `workflow-core`: `NO_BUMP`
- `ai-skills-core`: `NO_BUMP`
- `writing-style`: `NO_BUMP`
- `research-writing`: `NO_BUMP`
- `presentations`: `NO_BUMP`
- `scientific-visualization`: `NO_BUMP`
- `web-development`: `NO_BUMP`
- `statistical-modeling`: `NO_BUMP`
- `bioinformatics`: `NO_BUMP`
- `medical-imaging`: `NO_BUMP`

Role Contract 自身的文档版本号不作为 repository/plugin release version。除非 Critic 明确要求，否则本 implementation 不因这次 wording cleanup 单独修改其 `版本：1.3` 标记，避免无必要版本噪声。

## 11. 停止条件与恢复

以下情况必须停止并回 Planner，而不是扩大 scope：

- latest main 在 README/Role Contract/version policy/Marketplace config 上出现会改变已批准设计的实质漂移；
- 必须修改批准三个文件之外的 tracked source 才能完成；
- exact branch/worktree ownership 不清；
- 发现需要改变 Role Contract 实质职责或 handoff 语义；
- GitHub render 问题无法在两列 -> 一列 -> 简单原生布局内解决；
- 必须安装新 build chain、修改 plugin icons/source 或引入外部 provider 才能继续。

普通 Markdown/HTML 排版、文字长度和现有 SVG 尺寸调整应在批准范围内自行处理。

## 12. 交付

Executor 完成后必须：

- ordinary commit/push 到 `reviewed/readme_human_facing_refactor`；
- 报告 final candidate commit；
- 报告实际最终布局；
- 报告 VERSION / Marketplace parity；
- 提供真实 GitHub wide/narrow + light/dark visual evidence locator；
- 报告三个文件的 exact diff scope；
- 停止，不 merge `main`，不自行宣布 repository release。
