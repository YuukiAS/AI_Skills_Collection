# README Human-Facing Refactor Proposal v0.1

日期：2026-09-20  
状态：PROPOSAL — 未批准、未执行  
对象：`YuukiAS/AI_Skills_Collection` 根 `README.md`

## 1. 结论

根 README 应从“安装手册 + 维护手册 + workflow 操作指南 + 插件目录”的混合文档，收敛为一个真正面向人的项目首页。

目标不是让 README 承担所有文档职责，而是让访问仓库的人在几十秒内看明白：

1. 这个仓库是什么；
2. 现在有哪些中央插件；
3. 每个插件叫什么、版本是多少、主要用来做什么。

最终 README 以视觉清晰、短、可扫读为第一目标。复杂安装、HPC、维护、Planner/Critic、验证命令、TODO 流程等都离开根 README，继续由已有专门文档承担。

## 2. 当前问题：已验证事实

当前 `README.md` 共约 515 行、15.9k 字符，混合了至少以下几类完全不同的读者：

- 第一次访问仓库的人；
- 想安装 Codex plugin/profile 的用户；
- AI_Skills 维护者；
- Planner / Critic 两个长期线程；
- Server/HPC 使用者；
- Presentation/CUHK 模板使用者；
- 提交前运行验证的开发者。

其中存在明显的职责漂移：

- “真实项目怎么反过来改进插件”已经是维护流程说明；
- “项目 thread 要写多复杂？不用复杂”属于内部 workflow 指导，不适合项目首页；
- “Planner / Critic 双线程：直接复制这些指令”是一整套控制流程与 prompt 模板，不适合 README；
- Profile、Server/HPC、Presentation/CUHK、验证命令等详细说明都有更合适的现有文档位置；
- Codex Marketplace 安装说明在 README 中重复出现。

这也与当前 `AGENTS.md` 的现行原则冲突：根 README 明确被定义为“永远写给人看”，不能继续变成内部流程日志或维护手册。

## 3. GPT 现在到底从哪里读取 Planner / Critic 规则

当前 AI Research Stack 项目设置会在项目会话中直接提供高层角色与治理要求；对实质性的 Planner / Critic 轮次，又强制要求实际读取仓库最新 main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`

因此，根 README 不应再承担 Planner / Critic 初始化模板的职责。

但当前仓库仍有一个需要伴随清理的旧依赖：

- `PLANNER_ROLE_CONTRACT.md` §10.1 仍写着“以 README 中 Planner/Critic 模板为骨架”；
- `CRITIC_ROLE_CONTRACT.md` §6.2 仍写着同类依赖。

如果只删除 README 中的模板而不改这两处，合同就会指向已经不存在的模板。因此本次实施应把这两处改成自包含规则：Planner / Critic 按“项目设置 + 当前角色合同 + Active Context”自动生成下一角色 prompt，不再依赖 README 文本。

这是本次唯一需要伴随 README 修改的 workflow contract 修复；不扩展到新的状态、schema、Bridge Kit 或自动化。

## 4. 设计方向

### 4.1 选择：项目首页 + 插件画廊

最终 README 建议只保留四个视觉层次：

1. **Hero**  
   项目名 + 一句自然中文说明。可居中，但不做大段品牌文案。

2. **Plugin Gallery**  
   README 的主体。十个中央插件使用现有本地 SVG 图标，做成两列卡片式展示。每张卡只显示：
   - UI 名称；
   - 版本；
   - 一句人话用途；
   - 必要时用很小的文字保留 plugin slug，方便定位。

3. **最小使用入口**  
   只保留一个非常短的入口，例如 Codex Marketplace source / 安装文档链接。不能重新展开成安装手册。

4. **Documentation**  
   最底部用一行链接把维护者引向已有 `docs/`、`profiles/README.md`、`TODO.md` 等专门页面。README 自己不解释这些流程。

### 4.2 为什么不用普通长表格

纯 Markdown 表格最容易维护，但十个插件的名称、版本、用途会变成一块密集的“数据库视图”，视觉效果一般。

当前仓库已经为每个中央插件维护独立 SVG 图标和品牌色，直接复用这些资产可以明显提升辨识度，而且不需要新依赖。

因此首选使用 GitHub 支持的 HTML table 进行两列卡片排版，每张卡内部只包含本地图标、名称、版本与一句说明。

### 4.3 为什么不做复杂 banner / badge 系统

不建议本轮新增：

- 外部 badge 服务依赖；
- 自定义 CSS；
- 自动生成 README 的新脚本；
- 大型 hero banner；
- 新的 README metadata/schema。

原因很简单：这会让“把 README 变简单”反过来变成新的维护系统。

优先复用仓库已有 SVG，并使用 GitHub 原生 Markdown / HTML 能稳定渲染的能力。

## 5. Plugin Gallery 的内容来源

名称和版本不从旧 README 手工猜，而以当前 Marketplace 源配置：

`scripts/codex_marketplace_config.json`

作为实施时的直接依据。

当前十个中央插件为：

| UI 名称 | Version | Plugin slug | README 中的一句话用途 |
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

这些用途会在 README 中进一步压缩成自然、对称的一句话，不照搬 Marketplace 中偏机器路由的长 description。

## 6. 从根 README 删除什么

以下内容应全部移出根 README，而不是折叠起来继续保留：

- “真实项目怎么反过来改进插件”的长篇维护流程；
- “项目 thread 要写多复杂？不用复杂”及相关 NEW TODO 模板；
- 全部 Planner / Critic 复制模板与 handoff 操作教程；
- 多插件并行、incident triage 等内部流程说明；
- Profile 安装的完整命令列表；
- Server/HPC 完整环境命令；
- Presentation/CUHK 模板的详细运行原则；
- 根目录结构逐项解释；
- 提交前完整验证命令清单；
- 重复出现的 Marketplace 安装说明；
- 历史版本、maturity、内部状态等首页不需要的信息。

这些内容不删除对应能力，只是不再放在根 README。已有专门文档继续作为真实 authority。

## 7. 最小伴随修改

实施时预计只允许修改：

1. `README.md`
2. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
3. `docs/workflows/CRITIC_ROLE_CONTRACT.md`

其中后两项只做“去除 README prompt template 依赖”的最小合同修复，不重写角色体系。

明确不改：

- `AGENTS.md`
- `PLUGIN_CAPABILITY_GATE_POLICY.md`
- `scripts/codex_marketplace_config.json`
- Marketplace/generated plugin files
- skills / profiles / plugin production behavior
- Bridge Kit
- Reviewed Handoff schema/state
- 任何 provider / paid API / automation

## 8. 验收

这次不是“Markdown 语法没报错就算完成”。实施后至少直接检查：

1. **GitHub 实际渲染**：README 在 GitHub 页面中真实查看，而不是只读源码。
2. **视觉**：桌面宽屏与较窄窗口下都不出现卡片严重挤压、图标失真或长段文字墙；浅色/深色主题都自然。
3. **内容完整**：十个中央插件全部出现，显示名与版本与 `scripts/codex_marketplace_config.json` 一致。
4. **人类可读**：每个用途用一句自然中文表达，不出现 workflow 内部术语堆砌。
5. **去流程化**：根 README 不再出现可复制 Planner/Critic prompt、incident 操作手册、HPC 命令墙、验证命令墙。
6. **合同不悬空**：两个 Role Contract 不再依赖 README 中不存在的模板。
7. **边界**：Git diff 只涉及批准的三个文件；插件 production/source/generated layer 为零改动。

## 9. 版本与发布判断

这是 README 与 workflow 文档的整理，不改变任何中央 plugin 的 production behavior。

建议：

- Repository release bump：NONE
- Plugin version bump：全部 NO_BUMP
- Role Contract 文档自身若保留显式版本号，可从 1.3 更新为 1.4，表示去除了 README 模板依赖；这不是 plugin release version。

## 10. 现实替代比较

### A. 保留现有 README，只把内部流程折叠进 `<details>`

不采用。视觉上仍然很长，也继续让 README 承担错误职责；只是把混乱藏起来。

### B. 全部改成一个普通 Markdown 表

可行且最简单，但视觉表现普通，不符合“非常美观”的目标。

### C. 两列插件卡片 + 极短首页

采用。它直接利用现有插件图标与品牌色，既能展示名称/版本/用途，又不引入新系统。

### D. 新做大型品牌 banner、徽章与自动生成系统

暂不采用。维护成本与本轮目标不成比例；若未来确实需要 public-facing branding，可另作独立设计，不绑在本轮 README 清理中。

## 11. 外部依据

GitHub 官方把 README 定位为访问者首先看到的项目入口，建议 README 说明项目做什么、为什么有用、如何开始；更长的说明应放到更合适的文档中。GitHub 也明确支持 README 使用相对链接与相对图片路径，因此可以直接复用仓库已有 plugin SVG，而不依赖外部图床。

参考：

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github

## 12. 当前状态与下一步

本文件只是待审设计，不授权修改 README 或 Role Contract。

下一步：

1. 独立 Critic 审本 v0.1，重点检查是否仍然过重、是否删掉了 README 真正需要的信息、以及两处 Role Contract 伴随修复是否是最小必要范围；
2. 用户确认最终方向；
3. 两者都通过后，再进入 bounded implementation；
4. 实施完成后直接看 GitHub 真实渲染效果，再决定是否需要一轮纯视觉微调。
