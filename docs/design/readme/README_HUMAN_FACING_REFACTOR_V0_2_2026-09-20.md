# README Human-Facing Refactor Proposal v0.2

日期：2026-09-20  
状态：PROPOSAL — 设计修订，未批准、未执行  
对象：`YuukiAS/AI_Skills_Collection` 根 `README.md`  
上一版：`docs/design/readme/README_HUMAN_FACING_REFACTOR_V0_1_2026-09-20.md`  
本轮 source snapshot：`main@2b6a5b50d75488298fb2206a6eebe92b3748ede2`

## 1. 结论

根 README 应继续按 v0.1 的主方向收敛：从“安装手册 + 维护手册 + workflow 操作指南 + 插件目录”的混合文档，改成真正面向人的项目首页。

最终首页只承担几个简单任务：

1. 一眼看明白这个仓库是什么；
2. 一眼看见当前十个中央插件；
3. 每个插件看见名称、当前版本和一句用途；
4. 看见当前 Repository / CLI release；
5. 需要进一步使用或维护时，能顺着少量具体链接进入对应文档。

README 不再承担 Planner / Critic 运行手册、真实项目 refinement 教程、Server/HPC 命令手册、Presentation/CUHK 运行合同、目录说明或提交前验证清单。

本轮 v0.2 接受 Critic 的两个 blocker：保留当前 Repository / CLI version；两列插件 gallery 保持首选，但不把它冻结成不可替代的唯一布局。

## 2. Critic finding 处理

### README-R1 — ACCEPT：保留当前 Repository / CLI version

Critic 指出，`docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md` 仍明确规定：

- `VERSION` 是 Repository / CLI version 的 canonical source；
- README 当前 repository release 必须与 `VERSION` 一致。

本轮重新核对 `VERSION`，当前值为：

`5.0.5`

因此 v0.2 修改设计：

- README 保留一个很轻量的人类可读版本信息，例如 `Repository / CLI 5.0.5`；
- 实施时必须从 `VERSION` 核对，而不是沿用旧 README 的手写值；
- 不恢复 repository 版本历史；
- 不恢复 maturity 表；
- 不把内部 release 流程重新塞回 README；
- 不修改版本政策；
- 本次 Repository bump 仍为 `NONE`；
- 十个中央 plugin 均为 `NO_BUMP`。

这关闭 README-R1，同时不改变 v0.1 的“README 只保留当前有用信息”的原则。

### README-R2 — ACCEPT：两列 gallery 是首选，不是不可替代的强制布局

两列本地 SVG 插件 gallery 仍是首选，因为它比普通长表更有辨识度，并且可以直接复用现有图标资产。

但 v0.2 不再把“两列”写成最终必须保持的结构。原因是 GitHub README 最终受 GitHub 自己的 Markdown/HTML 渲染约束；本轮也明确不允许为了响应式布局引入自定义 CSS 或额外构建系统。

因此执行合同应允许在同一批准范围内做以下**纯呈现降级**：

- 首选：两列 gallery；
- 如果真实 GitHub 宽屏/窄屏或浅色/深色显示出现明显挤压、横向滚动、图标比例失衡、文字阅读性下降；
- 则可退为一列 gallery；
- 若一列 gallery 仍不自然，可进一步退为更简单的 GitHub 原生 Markdown/HTML 布局；
- 这种退回只改变排版，不改变信息结构、插件内容、版本来源或 README 职责，因此不需要新架构设计。

无论采用哪种最终布局，都禁止因为视觉问题引入：

- 外部 badge 服务；
- 自定义 CSS；
- README generator；
- 新 schema；
- 新 build chain；
- 新的 README 专用 runtime。

GitHub 官方文档确认 README 支持相对图片路径，GitHub Flavored Markdown 也允许一定范围的 HTML；同时 GFM 对 `<style>` 等标签进行过滤，说明本轮应依赖 GitHub 原生渲染，而不是把自定义响应式 CSS 当成稳定方案。

这关闭 README-R2。

## 3. 当前问题：已验证事实

当前根 `README.md` 约 515 行、15.9k 字符，同时面向多类完全不同的读者：

- 第一次访问仓库的人；
- 想安装插件或 profile 的用户；
- AI_Skills 维护者；
- Planner / Critic；
- Server/HPC 用户；
- Presentation/CUHK 模板用户；
- 提交前运行验证的开发者。

其中已经存在明显职责漂移：

- “真实项目怎么反过来改进插件”属于维护流程；
- “项目 thread 要写多复杂？不用复杂”属于内部 workflow 指导；
- “Planner / Critic 双线程：直接复制这些指令”是一整套内部角色操作手册；
- Profile、Server/HPC、Presentation/CUHK、验证命令都有更合适的专门文档位置；
- Marketplace 安装说明在当前 README 中重复出现。

这与当前 `AGENTS.md` 的明确原则一致冲突：根 README 应始终写给人看，不应继续成为内部流程日志或控制面手册。

## 4. Planner / Critic 的真实读取链

当前正常读取链不需要 README 承担角色模板 authority。

在 AI Research Stack 项目会话中，高层治理要求由项目设置提供；进入实质 Planner / Critic 轮次时，再按当前合同读取最新 main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`

因此根 README 中现有的 Planner/Critic 初始化模板和 handoff 教程可以删除。

但当前 repo 仍有两处旧依赖需要在未来实施时一起修：

- `PLANNER_ROLE_CONTRACT.md` §10.1 仍写“以 README 中 Planner/Critic 模板为骨架”；
- `CRITIC_ROLE_CONTRACT.md` §6.2 仍写同类依赖。

最小修复是让这两段规则自包含：下一角色 prompt 依据“当前项目设置 + 对应 Role Contract + Active Design/Review Context + 当前 review/package locator”自动生成，不再读取 README 模板。

这仍是本轮唯一允许伴随 README 修改的 workflow contract 清理；不新增状态、schema、Bridge Kit 机制或自动化。

## 5. 最终 README 的信息架构

最终 README 建议只保留五个视觉层次。

### 5.1 Hero

只包含：

- 项目名；
- 一句自然中文说明；
- 可选的一句非常短的英文副标题，但只有确实改善首页观感时才保留。

不写长篇“使命宣言”，不写内部工作流术语。

### 5.2 当前 Repository / CLI release

用极轻量的一行显示当前版本。

例如：

`Repository / CLI 5.0.5`

实际值必须实施时从 `VERSION` 核对。

这不是 release dashboard，不展开版本历史、maturity 或 release policy。

### 5.3 Plugin Gallery

这是 README 的主体。

每个中央插件只展示：

- 现有本地 SVG 图标；
- UI display name；
- 当前 plugin version；
- 一句自然中文用途；
- 必要时用弱化的小字保留 plugin slug，方便维护者定位，但不能抢占视觉主层级。

首选两列；真实 GitHub render 不合适时允许按 §2 README-R2 的边界退为一列或更简单的原生布局。

### 5.4 最小使用入口

只保留一个非常短的“怎么开始”入口，不把 README 重新写成安装手册。

候选方式：

- 一行 Codex Marketplace source；或
- 一个“安装 / Profiles”链接。

最终选哪一个由实施时基于页面整体观感决定，但只保留最小必要信息，不重复完整 CLI 命令墙。

### 5.5 Documentation footer

吸收 Critic 的非阻塞建议：当前 repo 没有 `docs/README.md`，本轮不为了 README 重构再造一个 docs portal。

footer 只链接少量已经存在、真正给人用的具体入口。优先候选：

- `profiles/README.md` — 安装组合；
- `docs/LOCAL_CONFIGURATION.md` — 本地 / Server 配置；
- `TODO.md` — 当前维护入口；
- `CHANGELOG.md` — repository release 历史。

实施时可根据最终首页长度保留其中 2–4 个，不建立新的索引系统，也不把 workflow contract 文件直接暴露成普通用户的第一层导航。

## 6. Plugin Gallery 的 canonical 内容来源

插件显示名与版本不从旧 README 手工复制，而以：

`scripts/codex_marketplace_config.json`

作为当前 canonical 来源。

当前十个中央插件为：

| UI 名称 | Version | Plugin slug | README 一句话用途 |
|---|---:|---|---|
| Verified Workflow | 0.1 | `workflow-core` | 复杂任务的执行、验证与可靠收尾 |
| AI Skills Maintainer | 0.2 | `ai-skills-core` | 维护和迭代本仓库的插件、版本与生成层 |
| Clear Writing | 0.3 | `writing-style` | 保留事实与原意，改善中英文科研和技术表达 |
| Research Authoring | 0.1 | `research-writing` | 研究报告、论文、文献与引用工作流 |
| Presentations | 0.3 | `presentations` | 科研组会、研究汇报与商务演示文稿 |
| Scientific Visualization | 0.1 | `scientific-visualization` | 科研图、配色、示意图、海报与视觉检查 |
| Frontend Design | 0.1 | `web-development` | 前端参考、视觉系统与科研产品界面设计 |
| Statistical Modeling | 0.1 | `statistical-modeling` | 统计建模、Bayesian 工作流、诊断与数据分析 |
| Bioinformatics | 0.1 | `bioinformatics` | 生物信息数据库、单细胞、GWAS 与组学工作流 |
| Medical Imaging | 0.1 | `medical-imaging` | 医学影像、DICOM/NIfTI、分割、配准与影像 AI |

正式实施时一句用途允许做小幅中文润色，但不能改变 plugin 实际能力边界。

图标同样复用当前 Marketplace config 指向的本地 SVG；实施前核对路径存在，不新增另一套 README 专用 icon。

## 7. 从根 README 删除什么

以下内容继续按 v0.1 从根 README 移除，而不是折叠起来保留：

- “真实项目怎么反过来改进插件”的长篇维护流程；
- “项目 thread 要写多复杂？不用复杂”及 NEW TODO 模板；
- Planner / Critic 全部复制模板与 handoff 教程；
- 多插件并行、incident triage 等内部流程说明；
- Profile 安装的完整命令列表；
- Server/HPC 完整环境命令；
- Presentation/CUHK 模板详细运行原则；
- 目录逐项解释；
- 提交前完整验证命令清单；
- 重复 Marketplace 安装说明；
- repository 历史版本；
- maturity 表和内部 release 流程。

唯一从版本体系保留到首页的是**当前 Repository / CLI version**，用于满足 README-R1 和现行版本合同。

## 8. 实施范围

若后续设计获得 Critic PASS 并另行进入 execution package，实施范围仍只允许：

1. `README.md`
2. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
3. `docs/workflows/CRITIC_ROLE_CONTRACT.md`

后两项只允许去除 README-template dependency，并保持现有角色职责、handoff 语义和输出格式不变。

明确不改：

- `AGENTS.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `VERSION`
- `scripts/codex_marketplace_config.json`
- Marketplace/generated payload
- skills
- profiles
- plugin production behavior
- Bridge Kit
- Reviewed Handoff schema/state
- provider / paid API / automation

本轮 v0.2 本身只提交设计文档，不实施上述三文件修改。

## 9. 最终视觉与内容验收

后续真正实施时，验收必须直接针对用户看到的 README，而不是只看 Markdown 源码。

### 9.1 GitHub 真实 render

必须直接查看 GitHub 上的 README 实际渲染。

至少保存或提供足够的视觉证据，让 Reviewer/Critic 能判断：

- 宽窗口；
- 较窄窗口；
- 浅色主题；
- 深色主题。

如果平台不能一次直接提供四种状态，允许用真实 GitHub 页面分别取得；不能用本地自制 HTML 假装 GitHub render。

### 9.2 布局退回条件

两列 gallery 出现以下任一明显问题时，应在同一批准范围内退为一列或更简单原生布局：

- 明显横向滚动；
- 卡片压缩到难以阅读；
- 图标或文字比例失衡；
- 窄窗口视觉层级崩坏；
- light/dark 中任一主题对比异常。

退回不是失败，也不是新设计轮次；目标是得到稳定、简洁、好看的真实 GitHub 首页，而不是守住“两列”这个形式。

### 9.3 内容完整性

必须直接核对：

- 十个中央 plugin 全部出现；
- display name 与 `scripts/codex_marketplace_config.json` 一致；
- plugin version 与 Marketplace config 一致；
- Repository / CLI version 与 `VERSION` 一致；
- 每个用途是自然中文，并与真实能力边界相符；
- 本地 SVG 均可正常显示。

### 9.4 去流程化

根 README 不得再出现：

- 可复制 Planner/Critic prompt；
- workflow incident 操作教程；
- HPC 命令墙；
- Presentation 运行合同；
- 大段验证命令；
- 内部状态机/评审术语堆砌。

### 9.5 合同一致性

必须确认：

- `PLANNER_ROLE_CONTRACT.md` §10.1 不再依赖 README 中不存在的模板；
- `CRITIC_ROLE_CONTRACT.md` §6.2 不再依赖 README 中不存在的模板；
- 两处改动不改变 handoff 实质语义；
- 其他 Role Contract 规则没有顺手重写。

### 9.6 变更边界

最终 implementation diff 只能落在批准的三个文件。

若为修复 README 视觉需要修改插件图标、Marketplace config、AGENTS、version policy、profiles 或生成层，必须停止并回 Planner，不得扩大本轮范围。

## 10. 版本与发布判断

本轮设计与未来对应实现只整理 README 和两个 workflow 文档引用，不改变中央 plugin 的 production behavior，也不形成新的 Repository / CLI 用户能力。

因此：

Repository bump decision: NONE  
Reason: README / workflow-doc cleanup only; no repository-level capability or install contract change.

Affected plugins:

- `workflow-core`: NO_BUMP
- `ai-skills-core`: NO_BUMP
- `writing-style`: NO_BUMP
- `research-writing`: NO_BUMP
- `presentations`: NO_BUMP
- `scientific-visualization`: NO_BUMP
- `web-development`: NO_BUMP
- `statistical-modeling`: NO_BUMP
- `bioinformatics`: NO_BUMP
- `medical-imaging`: NO_BUMP

当前 Repository / CLI version 继续是 `5.0.5`。

Role Contract 文档自己的显式版本号是否在未来 implementation 中从 1.3 更新为 1.4，可作为同一 docs-only 修改处理；它不是 Repository / plugin version bump。若 Critic 认为没有必要，也可以保持 1.3，避免为编号本身制造变化。

## 11. 现实替代比较

### A. 保留现有 README，只把流程塞进 `<details>`

不采用。职责仍然错误，只是把混乱折叠起来。

### B. 普通 Markdown 长表

可作为最终 fallback，但不作为首选。它稳定、简单，却达不到用户要求的视觉质量。

### C. 两列本地 SVG gallery

首选。充分复用现有资产，信息密度合适，也没有新依赖。

### D. 一列本地 SVG gallery

作为真实 GitHub 窄屏表现不佳时的第一 fallback。保留视觉辨识度，响应式风险更低。

### E. 外部 badge / 自定义 CSS / README generator

不采用。它们增加依赖和维护面，与“把 README 变简单”的目标相反；GitHub 渲染与 GFM sanitization 也不适合把自定义 CSS 作为本轮核心机制。

## 12. 外部研究与采用决定

本轮重新核对 GitHub 官方资料：

1. GitHub Docs — About the repository README file  
   https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes  
   采用：README 是仓库访问者首先消费的入口；继续保持短、导航清楚。

2. GitHub Docs — Basic writing and formatting syntax  
   https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax  
   采用：仓库内图片和链接使用相对路径，适合直接复用现有 SVG；不需要外部图床。

3. GitHub Flavored Markdown Spec  
   https://github.github.com/gfm/  
   采用：GFM 支持表格和 raw HTML，但 GitHub 还会做额外 sanitization；`<style>` 属于过滤标签之一。因此两列 HTML 只能作为原生布局方案，不能依靠自定义 CSS 保证响应式，支持 README-R2 的 fallback 设计。

不采用任何新的前端框架、README renderer、badge provider 或构建工具。

## 13. 非阻塞建议处理

Critic 提醒当前 repo 不存在 `docs/README.md`。

v0.2 接受这个观察，但不新建文档门户。

处理方式：

- footer 直接链接现有具体文档；
- 优先选择 `profiles/README.md`、`docs/LOCAL_CONFIGURATION.md`、`TODO.md`、`CHANGELOG.md` 中最适合的 2–4 个；
- 不新增 `docs/README.md`；
- 不新增 index generator；
- 不扩展到文档信息架构重构。

## 14. 当前状态与下一步

本 v0.2 只是对 Critic README-R1 / README-R2 的设计修订。

本轮没有：

- 修改根 README；
- 修改 Role Contract；
- 创建 execution package；
- 创建 Reviewed Handoff task/branch/worktree；
- 启动 Codex Executor；
- 调用 paid API；
- 修改 plugin production source/generated layer/profile；
- 修改 AGENTS、Bridge Kit、Capability Gate Policy 或 Versioning Policy。

下一步只把本 v0.2 交回独立 Critic，优先复核：

1. README-R1 是否因保留 `VERSION` 对应的当前 Repository / CLI release 而关闭；
2. README-R2 是否因真实 GitHub render 驱动的一列/native fallback 而关闭；
3. 非阻塞 documentation footer 是否保持足够简单；
4. v0.2 是否仍忠实于用户要求的“非常美观，但 README 只做人的首页”。

Critic PASS 之后，才由 Planner 另行准备 execution package；本轮不提前写 Goal / Kickoff。
