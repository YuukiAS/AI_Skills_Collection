# TODO v2：插件架构、图标、演示文稿、外部来源整合与安装文档重构

## 0. 任务定位

本文件替代上一版根目录 `TODO.md`，作为下一轮 Codex 重构 `AI_Skills_Collection` 的主要执行说明。目标不是简单增加一个 Presentation 插件或批量补图标，而是把整个仓库整理成一套边界清楚、可按机器和项目安装、能与 OpenAI 官方插件协作、可以持续吸收外部 Skill/规范且保留来源历史的系统。

必须遵守以下总原则：

1. `skills/`、`profiles/`、`shared/` 和发布配置是源层；`.agents/plugins/marketplace.json` 与 `plugins/codex/plugins/` 是生成层，不得手工维护。
2. OpenAI 官方插件负责通用执行后端，例如 Presentation/Slides、LaTeX、PDF、GitHub、Notion、Zotero、BioRender 和 `build-web-apps`；本仓库负责用户特有的科研工作流、写作规则、设计知识、领域知识、项目约束和验收标准。
3. 官方插件与本仓库插件可以同时使用，但必须按职责串联，不得用多个宽泛 trigger 竞争同一任务。
4. 项目专用知识与项目代码同版本维护；通用插件不应长期携带 CardiacNexus、CARE、TRACE 或 Asteria 的易变项目事实。
5. 外部 Skill、GitHub 仓库、Notion 页面或其他规范只能先审查、再提炼合并；不允许把外部目录永久 clone 到本仓库后长期保留。
6. 所有长期保留的外部来源必须可追踪；临时 clone/export 删除后，统一历史中保留一条简洁记录，目标 Skill 的 provenance 继续记录直接来源。
7. 修改后必须更新 README、生成 Marketplace、运行测试、路径预算、图标审计、provenance 审计和真实安装检查。

---

## 1. 目标架构

### 1.1 中央 Marketplace：九个通用插件

中央 `AI_Skills_Collection` Marketplace 的目标用户可见插件为：

| 插件 | 核心职责 | 典型安装范围 |
|---|---|---|
| `workflow-core` | 复杂任务的事实源发现、计划、执行、验证和完成门槛 | 所有实际运行 Codex 的主力环境 |
| `ai-skills-core` | 本仓库的 profile 安装、更新、registry、catalog、Marketplace 和维护 | 需要使用或维护 AI_Skills_Collection 的机器 |
| `writing-style` | 忠实改写、中文技术表达、科学表达和局部文本质量 | 用户级全局安装 |
| `research-writing` | Repo 报告、研究文档、正式论文、文献与引用工作流 | 主力科研环境 |
| `presentations` | 独立的科研/技术演示与商业演示工作流 | 主要制作 PPT/Slides 的桌面环境 |
| `web-development` | 前端参考研究、视觉系统和科研产品前端约束，补充官方 `build-web-apps` | 有网站、Dashboard 或研究产品任务的环境 |
| `statistical-modeling` | 统计模型、贝叶斯方法、数据分析和科学可视化 | 主力科研环境 |
| `bioinformatics` | 通用生物信息学与组学工作流 | 按领域或项目安装 |
| `medical-imaging` | 医学影像、CMR、DICOM/NIfTI 和影像机器学习 | 按领域或项目安装 |

`cardiacnexus` 不再作为中央通用 Marketplace 插件。中央插件数仍为九，但这是目标架构的结果，不是为了迎合当前 `MAX_MARKETPLACE_PLUGINS = 9`。必须确认该限制只是仓库内部预算，并把产品限制、仓库预算和测试断言分开表达。

### 1.2 项目层

项目专用 Skill 以项目仓库为 canonical source：

```text
<Project Repo>/
  AGENTS.md
  .agents/
    skills/
      <project-skill>/
        SKILL.md
        agents/openai.yaml
        references/
        scripts/
        assets/
```

项目层至少覆盖：

- CardiacNexus：pipeline、feature contracts、strain/registration、docs/website。
- CARE：当项目形成稳定专用协议后再在 CARE repo 中创建，不提前把易变规则放进中央插件。
- TRACE/Asteria：模型版本、符号、数据流、论文状态和导出格式在相应 repo 中维护。

中央仓库可以保留项目 profile、来源索引、安装/检查入口和迁移历史，但不能同时维护另一份独立可编辑的完整项目 Skill 副本。

### 1.3 与 OpenAI 官方插件的关系

实现前先读取当前 Codex App/CLI 环境中已安装的官方插件 manifest 和 Skill，记录实际名称、触发器、输入输出、文件格式和调用方式，不得凭记忆硬编码 `$presentation`、`$latex`、`$build-web-apps` 等调用名。

职责边界：

| 工作 | 本仓库负责 | 官方插件负责 |
|---|---|---|
| PPT/Slides | 受众、叙事、deck plan、模板、引用、内容与视觉 QA | `.pptx`/Google Slides 的创建、编辑、对象操作、导出和渲染 |
| LaTeX/Beamer | 论文或演示内容、模板选择、中文/数学规则、完成标准 | `.tex`、宏包、编译、日志修复和 PDF 构建 |
| 前端 | 外部参考、视觉方向、科研产品约束、设计 brief | 代码实现、框架最佳实践、浏览器测试和部署 |
| GitHub | 本仓库或项目工作流规则 | 文件、提交、PR、Issue 和 Actions 操作 |
| Notion | 如何审查、提炼、合并和记录来源 | 页面搜索、读取和元数据获取 |
| Zotero/BioRender/PDF | 科研工作流、引用/图示使用规则 | 实际连接器或文件工具能力 |

不得复制官方插件全文。兼容性文档只保存公开接口、已验证行为、协作顺序和已知缺口。

---

## 2. 插件边界与应用层 Active Skills

### 2.1 `workflow-core` 与 `ai-skills-core`

两者保持独立。

`workflow-core` 是通用执行纪律，负责：

- 先发现 source of truth；
- 区分设计、实现、验证和交付；
- 复杂任务建立阶段门槛；
- 不把启动子 Agent、提交作业或生成第一版当作完成；
- 读取 repo 的 `AGENTS.md`、TODO、handoff、测试和既有约束；
- 诚实报告未完成项和证据不足。

`ai-skills-core` 是 AI_Skills_Collection 管理入口，目标只暴露本仓库独有能力，例如：

```text
ai-skills-core
├── project-skill-profile-installer
└── ai-skills-repository-maintainer
```

要求：

- [ ] 不再重复发布 OpenAI 官方 `skill-creator`、`skill-installer` 或 `plugin-creator` 的通用实现。
- [ ] `project-skill-profile-installer` 负责选择 profile、安装 repo-local Skill、更新 manifest，并同步项目 `AGENTS.md`。
- [ ] `ai-skills-repository-maintainer` 负责 registry、catalog、provenance、Marketplace、图标和发布层维护。
- [ ] `ai-skills-repository-maintainer` 默认 `allow_implicit_invocation: false`，普通编码任务不得自动注入仓库维护流程。
- [ ] README 明确：`ai-skills-core` 不是所有机器必装，只在使用中央 CLI/profile 或维护本仓库时安装。

### 2.2 `writing-style` 与 `research-writing`

必须在 Skill description、README 和测试中明确以下边界：

`writing-style` 解决：

```text
已有语义内容 → 更清楚、更自然、更一致、符合目标风格的表达
```

它可以做忠实改写、中文技术表达、局部科学表达、术语统一、标点与中英文混排、数学排版和语言压缩；原则上不搜索文献、不决定论文结构、不新增研究结论、不判断证据是否足以支撑主张。

`research-writing` 解决：

```text
项目证据、研究目标与文献 → 结构完整、可追踪的科研成果
```

它负责 repo 报告、milestone/实验复盘、研究设计文档、正式论文、supplement、rebuttal、grant、literature review、claim–evidence–citation 关系和章节组织，并在需要时调用 `writing-style` 做最终语言处理。

目标应用层 Active Skills：

```text
writing-style
├── writing-fidelity
├── chinese-prose
└── scientific-prose

research-writing
├── research-reporting
├── research-paper-workflow
└── literature-and-citations
```

要求：

- [ ] 现有 source skills 可以继续作为内部工作流，但 App-facing trigger 必须收敛到以上边界。
- [ ] `scientific-prose` 只负责表达，不得与 `research-paper-workflow` 竞争整篇论文任务。
- [ ] `research-reporting` 覆盖 repo 内 Markdown 报告、里程碑总结、结果复盘和技术文档。
- [ ] `research-paper-workflow` 覆盖正式论文、Methods/Results/Discussion、supplement、rebuttal 和 grant。
- [ ] `literature-and-citations` 覆盖文献检索、综述、引用核验、BibTeX 和 Zotero 协作。
- [ ] PDF/DOCX/LaTeX 的底层文件实现优先交给官方能力；本插件保留内容和科研流程控制。

### 2.3 `presentations`：两个互不干扰的 Skill

目标结构：

```text
presentations
├── research-presentations
└── business-presentations
```

`research-presentations` 触发范围：组会、学术报告、seminar、conference、journal club、答辩、方法/模型/实验汇报，以及从论文、科研 Markdown、Asteria 导出、代码结果或已有 deck 制作技术演示。

其主线是：

```text
为什么做 → 做了什么 → 关键机制 → 证据说明什么 → 失败/局限 → 需要讨论什么 → 下一步
```

`business-presentations` 触发范围：公司汇报、executive summary、项目提案、产品/运营/市场/组织汇报、pitch、决策 deck，以及明确面向非技术业务受众的演示。

其主线是：

```text
结论/请求 → 问题或机会 → 证据与影响 → 方案 → 资源与风险 → 决策和下一步
```

避免冲突：

- [ ] 仅修改现有 PPTX/Google Slides 的文字、颜色、对齐或对象时，直接使用官方 Presentation/Slides，不触发本仓库两个 orchestration Skill。
- [ ] 来自科研 repo、论文、模型、实验或 Asteria 的输入默认 `research-presentations`。
- [ ] 明确 company/executive/market/product/client/strategy/pitch/operations 语境时使用 `business-presentations`。
- [ ] 两者共用 deck-plan schema、输入适配器、模板路由、来源忠实度和 visual QA，但拥有独立 trigger、叙事、信息密度和验收规则。
- [ ] 从 `research-writing` 的 App-facing `research-documents` 中移除 `pptx` 和旧 `scientific-slides`，避免三处争夺 presentation 任务。

建议源层结构：

```text
skills/tools/documents-media/presentations/
  shared/
    deck-plan.schema.json
    markdown-ingestion.md
    template-routing.md
    source-fidelity.md
    visual-qa.md
    compatibility/
      openai-presentation.md
      openai-latex.md
    templates/
      cuhk/
        design-tokens.json
        beamer/
        pptx/
  research-presentations/
    SKILL.md
    agents/openai.yaml
    references/
  business-presentations/
    SKILL.md
    agents/openai.yaml
    references/
```

Marketplace builder 需要支持插件级共享 payload，或提供等价且不复制两套共享材料的生成方案。不得使用 symlink。

### 2.4 官方 LaTeX 插件

建议在需要论文/Beamer 的主力环境安装官方 LaTeX 插件，但本仓库不再创建另一套通用 LaTeX 插件。

调用边界：

- [ ] 正式论文的结构、论证、引用和内容由 `research-writing` 主导；`.tex`、宏包、编译和日志由官方 LaTeX 完成。
- [ ] 研究演示的叙事和 deck plan 由 `research-presentations` 主导；明确要求 Beamer/Overleaf/LaTeX/PDF 时由官方 LaTeX 完成文件实现。
- [ ] 普通 Markdown 报告或 PPTX 不因含有公式而自动触发 LaTeX。
- [ ] 先审计实际官方插件名称和功能，再写 compatibility 文档和依赖声明。

### 2.5 `web-development` 作为官方前端插件的补充

不得删除 `web-development`。其目标不是复制官方 `build-web-apps` 的实现闭环，而是吸收更广、更快更新的设计参考和科研产品知识。

目标 Active Skills：

```text
web-development
├── frontend-reference-research
├── frontend-visual-systems
└── research-product-frontend
```

`frontend-reference-research` 负责：

- 小红书帖子、用户截图、GitHub 新 UI 库、Figma Community、设计案例和其他新资料的审查；
- 记录访问时间、来源、适用场景和可复用模式；
- 将案例抽象成 pattern，而不是复制整页或永久保存来源不明图片。

`frontend-visual-systems` 负责：

- design tokens、品牌、配色、图标、排版、页面节奏、信息密度和可执行 design brief；
- 把外部参考转化成当前项目可实现的视觉规则。

`research-product-frontend` 负责：

- 医学影像浏览器、phenotype explorer、模型比较、实验历史、provenance、统计图表、公式和科研证据界面的特殊约束；
- Asteria、CARE、CardiacNexus 等高信息密度研究产品。

标准协作顺序：

```text
外部参考/用户截图
→ frontend-reference-research
→ frontend-visual-systems 或 research-product-frontend
→ 形成 design brief/视觉约束
→ OpenAI build-web-apps 实现、浏览器测试和部署
```

要求：

- [ ] 当前 `frontend-product-design`、`react-tailwind-ui`、`frontend-testing-debugging` 等与官方实现高度重叠的 App-facing trigger 重新收敛。
- [ ] 原 source skills 可以保留供 CLI/内部参考，但用户可见入口必须体现“补充层”定位。
- [ ] 不把小红书、Dribbble 等完整第三方图片或帖子内容直接提交到公开仓库；保留链接、模式摘要、访问日期和必要的许可/用途说明。
- [ ] 对用户私有截图或 Notion 页面，默认只在本地 intake 区使用；未经确认不得进入公开仓库。

### 2.6 领域插件

`statistical-modeling`、`bioinformatics` 和 `medical-imaging` 继续提供领域判断，不承担通用写作、PPT 文件实现或前端工程。

- `statistical-modeling` 检查模型、公式、估计、诊断、实验设计和科学图表。
- `bioinformatics` 处理组学、数据库、单细胞和生物信息学工具链。
- `medical-imaging` 处理 CMR、DICOM/NIfTI、分割、配准、影像特征和医学影像机器学习。

它们可以与 `research-writing`、`research-presentations` 或官方前端插件组合，但不得替代项目 repo-local 事实。

---

## 3. README 与安装模型

README 必须从“列出命令”升级为“先告诉用户该装什么、装在哪里、为什么”。至少加入以下内容。

### 3.1 安装层级

#### A. 所有主力 Codex 环境建议用户级全局安装

```text
workflow-core
writing-style
```

说明：`workflow-core` 约束执行质量；`writing-style` 体现用户长期表达规则。纯 Slurm compute node、训练容器或不运行 Codex 的机器不需要安装。

#### B. 主力科研环境建议安装

```text
research-writing
statistical-modeling
```

桌面或经常制作演示的机器再安装：

```text
presentations
OpenAI 官方 Presentation/Slides
OpenAI 官方 LaTeX（需要论文或 Beamer 时）
```

有网站、Dashboard 或研究产品开发时安装：

```text
web-development
OpenAI build-web-apps
```

#### C. 按领域/项目安装

```text
medical-imaging
bioinformatics
```

这些插件可以用户级安装在长期从事对应领域的环境，也可以通过 project profile 仅安装到相关 repo。README 必须给出两种方式的区别。

#### D. 仅在使用或维护本仓库时安装

```text
ai-skills-core
```

适用于：有 `AI_Skills_Collection` checkout、运行 `ai-skills` CLI、更新 profile、维护 registry/catalog/Marketplace 的机器。

不适用于：只从 Codex App Marketplace 使用普通插件的机器、纯计算节点、无维护需求的临时容器。

### 3.2 README 必须提供的场景矩阵

至少写清楚：

| 场景 | 本仓库插件 | 官方插件/后端 |
|---|---|---|
| Repo 内 report/milestone/实验复盘 | `workflow-core` + `research-writing` + `writing-style` + 领域/项目 Skill | GitHub；需要 PDF 时加 LaTeX/PDF |
| Asteria/TRACE Markdown → 组会 PPT | repo-local TRACE/Asteria + `research-presentations` + `statistical-modeling` | Presentation；Beamer 时加 LaTeX |
| 正式论文 | repo-local 项目 Skill + `research-paper-workflow` + `literature-and-citations` + `writing-style` + 领域插件 | LaTeX、PDF、Zotero、GitHub |
| 前端网站/科研产品 | repo-local 项目 Skill + `web-development` | `build-web-apps`、Figma、GitHub |
| 商业/公司 PPT | `business-presentations` | Presentation/Google Slides |
| CardiacNexus pipeline/docs | CardiacNexus repo-local Skills + `medical-imaging`，需要时加 `research-writing`/`web-development` | GitHub、`build-web-apps` |
| 外部 Skill/Notion 规范整合 | `ai-skills-core` + `workflow-core` | Notion/GitHub |

### 3.3 README 命令和平台说明

- [ ] Codex App Marketplace：继续写清 source、ref 和两条 sparse paths。
- [ ] CLI：分别给出 user、repo 和显式兼容目标的命令。
- [ ] 给出推荐 profile：`global-baseline`、`research-main`、`presentation-desktop`、`frontend-research-product`、`medical-imaging-project`、`bioinformatics-project`、`ai-skills-maintainer`。
- [ ] 每个 profile 说明会安装哪些插件/Skill、目标目录、是否修改 `AGENTS.md`。
- [ ] Windows、Linux/HPC 和纯 compute node 分开说明。
- [ ] 不要求普通用户频繁删除重装全局 Skill；优先使用 manifest 驱动的 `ai-skills update`。
- [ ] README 明确 generated layer 不手工编辑，push 到 `main` 后由现有 Marketplace workflow 生成/验证/写回。

---

## 4. CardiacNexus 的迁移和长期位置

### 4.1 Canonical source

CardiacNexus 项目专用 Skill 的长期位置：

```text
YuukiAS/CardiacNexus
  AGENTS.md
  .agents/skills/
    cardiacnexus-pipeline-refactor/
    cardiacnexus-feature-contracts/
    cardiacnexus-strain-registration/
    cardiacnexus-docs-markdoc/
```

CardiacNexus repo 是唯一可编辑 canonical source。Skill 与 pipeline、schema、website 和测试同 commit 演进。

### 4.2 中央仓库保留什么

`AI_Skills_Collection` 仅保留：

- CardiacNexus 项目 profile 或安装检查描述；
- 外部/项目来源索引与 integration history；
- 指向 CardiacNexus repo、commit/ref 和 Skill 路径的记录；
- 必要的迁移脚本或“确认 repo-local Skill 已存在”的检查器；
- 不包含完整可编辑副本。

### 4.3 迁移步骤

- [ ] 审计当前中央 `skills/projects/cmr/cardiacnexus-*` 与 CardiacNexus repo 内实际规则。
- [ ] 以内容更完整、与当前代码一致的一方为基础，在 CardiacNexus `.agents/skills/` 建立 canonical Skills。
- [ ] 更新 CardiacNexus `AGENTS.md`，从旧 `.codex/skills` 和中央 canonical 路径迁移到 `.agents/skills`。
- [ ] 在 CardiacNexus repo 运行项目测试和 Skill 路由检查。
- [ ] 从中央 `scripts/codex_marketplace_config.json` 移除 `cardiacnexus` 插件。
- [ ] 将中央完整副本删除或转换为轻量 external-project descriptor；不能保留两份可编辑来源。
- [ ] 在 integration history 中记录迁移日期、CardiacNexus commit、源路径、目标路径和中央删除 commit。
- [ ] README 写清楚：CardiacNexus 用户应在项目 repo 中使用 repo-local Skills，而不是全局安装中央 `cardiacnexus`。
- [ ] 如确有 UI 需求，可由 CardiacNexus repo 自己发布 repo-scoped marketplace；不要重新放回中央通用 Marketplace。

---

## 5. 外部 GitHub/Notion Skill 与规范的整合

### 5.1 适用来源

后续 Codex 可能读取：

- 用户在 Notion 中维护的页面；
- 别人分享的 Skill、Prompt、规范或 checklist；
- GitHub 仓库、插件或单个 `SKILL.md`；
- 用户提供的网页、截图、文档和代码片段。

所有来源进入同一 intake 流程，不因来源是 Notion 就绕过许可、隐私、重复和 provenance 检查。

### 5.2 Notion 读取规则

- [ ] 使用官方 Notion 连接器/插件读取页面和必要的子页面；不得要求用户先把整套 Notion 导出后永久提交。
- [ ] 读取时记录 page title、稳定页面标识/URL、`last_edited_time`、读取日期、页面所有者或权限基础（能确认时）和目标用途。
- [ ] Notion 页面可能包含私密、未公开或第三方内容；默认不得把原文、截图或完整导出提交到公开仓库。
- [ ] 用户拥有或明确获准再利用的页面可以提炼合并；许可不清的第三方页面只能作为思路参考，必须独立改写，不能复制其完整 Skill 文本、代码或资产。
- [ ] 同一页面后续更新并再次整合时，新增一条 integration event，记录新 revision/`last_edited_time`，不得篡改旧历史。

### 5.3 临时 intake 区

临时 clone/export 必须放到未跟踪目录，例如：

```text
.tmp/skill-intake/<source-id>/
build/skill-intake/<source-id>/
```

要求：

- [ ] 加入 `.gitignore`。
- [ ] 禁止继续使用 tracked `todo/<cloned-repo>/` 作为长期源目录。
- [ ] clone 时固定 commit/ref；Notion 读取时固定页面 revision/last edited time。
- [ ] intake 区只服务于比较、审查和合并，不能被 Marketplace builder 引用。
- [ ] 合并和验证完成后删除临时 clone/export。

### 5.4 审查与合并流程

每个来源按以下顺序处理：

1. 记录来源身份、版本、许可/权限和拟整合目标。
2. 列出可用内容：trigger、工作流、checklist、脚本、参考资料、测试、资产。
3. 与现有目录做重复/冲突分析：相同能力不得再建一个宽泛 Skill。
4. 分类决定：`merge`、`merge-selected`、`reference-only`、`project-local`、`rejected`。
5. 将有价值内容提炼进现有或新目标 Skill，保持本仓库术语、frontmatter、目录和触发边界。
6. 为直接采用或实质改写的内容更新目标 Skill provenance；保留必要的许可和 attribution。
7. 运行 Skill validation、测试、catalog、Marketplace 和路径检查。
8. 在统一 history 中追加一条记录。
9. 删除临时 clone/export 和详细 intake 报告，只保留合并后的内容、必要法律文件、Skill provenance 和一行 history。

不得先批量复制外部目录再“以后整理”。

### 5.5 统一 Integration History

建立一个 canonical history，例如：

```text
docs/provenance/INTEGRATION_HISTORY.md
```

每个来源或每次重新整合只保留一行 Markdown 表格记录：

```text
| date | source_type | source | revision | permission/license | decision | target | integration_commit | note |
```

示例仅说明格式：

```text
| 2026-07-13 | notion | <page title + stable id> | <last_edited_time> | user-owned | merge-selected | research-presentations | <commit> | deck planning rules |
| 2026-07-13 | github | owner/repo | <commit sha> | MIT | merge | frontend-visual-systems | <commit> | temporary clone deleted |
```

要求：

- [ ] 一条记录必须足以回答“用了谁的什么、哪个版本、合并到哪里、在哪个 commit 完成”。
- [ ] history 是 append-only；发现错误时追加 correction 行，不静默改写已经发生的整合事实。
- [ ] 目标 Skill 的 frontmatter 继续保留 `provenance`、`source_repo_url`/page id、`source_path`、`source_ref`、`source_imported_at`、`source_license` 和 `source_note` 等直接来源信息。
- [ ] 历史只保留一行不等于可以删除法律要求的 LICENSE/NOTICE/attribution；必要法律文件继续保留。
- [ ] 不在 history 中写私密 Notion 正文；私有来源使用稳定 ID、标题摘要和权限说明，不泄漏敏感内容。

### 5.6 迁移现有 clone 记录

当前 `docs/provenance/CLONED_SKILL_SOURCES.md` 和 `cloned_skill_sources.json` 含大量 scratch inventory。重构时：

- [ ] 将每个已完成来源转换为 `INTEGRATION_HISTORY.md` 中一行。
- [ ] 保留远端、commit、许可、decision、target 和最终 integration commit。
- [ ] 删除长期无价值的 `scratch_path`、文件计数和临时证据清单。
- [ ] 对仍未完成整合的来源先标记 pending，不得在未确认目标和 commit 前删除证据。
- [ ] 完成迁移后，旧文件可以归档或删除；README/provenance 文档只指向新的 canonical history。

### 5.7 自动化与验证

新增或扩展工具，例如：

```bash
python3 scripts/provenance_audit.py --check
python3 scripts/provenance_audit.py --history docs/provenance/INTEGRATION_HISTORY.md
python3 scripts/external_source_intake.py --source <url-or-notion-id> --dry-run
```

至少检查：

- history 列完整、日期/revision/commit 格式有效；
- `integration_commit` 存在；
- 目标 Skill 存在；
- 直接外部来源的 frontmatter provenance 完整；
- 临时 intake 路径未被 tracked；
- generated Marketplace 未引用 `.tmp/`、`build/` 或外部 clone；
- 未知许可、权限不明、私密页面或大段逐字复制时阻断合并。

---

## 6. 图标系统

### 6.1 覆盖范围

P0：中央九个插件和其全部 App-facing Active Skills。

P1：`registry.json` 中全部 `status: active` 的源 Skill。

项目层：CardiacNexus 等 repo-local Skills 在各自仓库中维护图标；中央 history/index 可以记录来源，但不复制项目图标形成第二套来源。

### 6.2 来源优先级

1. 已有项目/产品 favicon 或 logo，确认仓库路径、commit、许可和用途。
2. 许可清晰的具体图标集，例如 React Icons 聚合下的 Font Awesome、Material、Heroicons、Bootstrap Icons，或 Lucide、Remix Icon 等；记录具体 icon set，不只写 React Icons。
3. Codex 直接绘制的简单可审查 SVG。
4. 禁止：来源不明搜索图片、带水印资产、无法确认许可的品牌图、嵌入脚本/字体/远程 URL 的 SVG。

### 6.3 目录和配置

插件图标建议：

```text
assets/codex/plugin-icons/<plugin>/
  composer.svg
  logo.png
  source.json
```

源 Skill：

```text
skills/.../<skill>/
  agents/openai.yaml
  assets/icon-small.svg
  assets/icon-large.png
```

Marketplace config 增加 `brandColor`、`composerIcon`、`logo`；aggregate Skill config 增加 `display_name`、`short_description`、`brand_color`、`icon_small`、`icon_large`、`default_prompt`。

### 6.4 审计

新增：

```bash
python3 scripts/icon_audit.py --scope marketplace
python3 scripts/icon_audit.py --scope active-skills
python3 scripts/icon_audit.py --contact-sheet build/icon-contact-sheet.png
python3 scripts/icon_audit.py --check
```

检查覆盖率、路径、尺寸、SVG 安全、来源/许可、哈希、浅色/深色可读性和意外重复。

---

## 7. Presentation 插件与 CUHK 默认模板

### 7.1 共享中间表示

所有非微小任务先生成版本化 `deck-plan.yaml`，至少包含：

```yaml
schema_version: 1
metadata:
  title: ""
  author: ""
  affiliation: ""
  audience: "specialist | mixed | general | executive"
  mode: "research | business"
  purpose: "group-meeting | conference | defense | journal-club | company | other"
  duration_minutes: 15
  language: "en | zh | mixed"
  template: "cuhk-default"
  output: "pptx"
  source_files: []
slides:
  - id: "s01"
    title: ""
    key_message: ""
    source_anchors: []
    content: []
    equations: []
    visuals: []
    layout_hint: ""
    citations: []
    speaker_notes: ""
    backup: false
```

要求：

- 每页一个主要信息目标；
- 不把 Markdown heading 机械映射成 slide；
- 公式保留 LaTeX；
- `source_anchors` 可回溯到 Markdown section、PDF 页码、图号、代码结果或已有 slide；
- 区分已完成结果、计划、假设和推测；
- deck plan 与最终文件一起保留。

### 7.2 输入适配器

支持：

- 通用 Markdown；
- Asteria/Marked TRACE v3 Markdown；
- 论文/PDF；
- 现有 PPTX/Google Slides；
- repo 中 figures、tables、results、logs 和 notes。

Asteria/TRACE 高优先级验收：取得脱敏 fixture，识别模型定义、版本变化、符号、公式、设计动机、结果、未解决问题和导师/reviewer 标记；主线围绕“本周变化、为什么改变、证据、风险、需要导师决定什么”。

### 7.3 CUHK 模板

本地输入：

```text
/mnt/data/CUHK Template.zip
/mnt/data/CUHK Template.pdf
```

要求：

- [ ] 审计 ZIP 内容、引用、许可和运行时必需文件。
- [ ] 从模板提取单一 `design-tokens.json`。
- [ ] 建立最小可编译 CUHK Beamer 模板。
- [ ] 建立真正可编辑、标准 16:9 的 CUHK PPTX/reference deck；不得把 PDF 页面作为不可编辑背景图。
- [ ] 保留标题页紫色几何视觉、顶部 section navigation、页码和 closing 语言，但允许适配 PowerPoint 16:9。
- [ ] 未明确指定其他模板时，科研和商业演示均使用 CUHK 默认视觉体系；公司/课程/会议/项目模板优先。
- [ ] 明确要求 Overleaf/Beamer/LaTeX/PDF 时输出 `.tex` 和 `.pdf`；普通“做 PPT/组会汇报”默认 `.pptx`，并导出 PDF/images 做 QA。
- [ ] 不提交字体文件；CUHK logo/校名等品牌资产再分发许可不清时，改用本地 import 脚本，不静默公开提交。

### 7.4 清理旧能力

- [ ] `skills/tools/documents-media/pptx/` 保留为兼容/内部参考或 archive，但不再作为中央 App-facing broad trigger。
- [ ] 审计 `scientific-slides`：把有价值的叙事、时长、引用和 visual QA 迁入 `research-presentations`；删除不存在脚本和默认 OpenRouter/Nano Banana 整页图片路径；不再发布为 Active Skill。
- [ ] 不把生成的整页 AI 图片冒充可编辑 PPTX。
- [ ] 官方 Presentation/Slides 能力不可用时，只允许明确标记的 fallback，不维护第二套等价引擎。

---

## 8. Marketplace、Builder 和测试

### 8.1 配置

- [ ] 将中央插件列表更新为本文件定义的九个通用插件。
- [ ] 移除中央 `cardiacnexus`，加入 `presentations`。
- [ ] `web-development` 更新为补充层三个 Active Skills。
- [ ] `research-writing` 和 `writing-style` 按边界收敛 Active Skills。
- [ ] `ai-skills-core` 不再复制官方通用 creator/installer。
- [ ] 对 plugin-level shared payload、图标和 interface metadata 增加 builder 支持。
- [ ] `MAX_MARKETPLACE_PLUGINS` 改成有解释的仓库预算或配置项；测试不再把“九”写成假定的 Codex 产品限制。

### 8.2 保持既有 gate

不得破坏：

- active skill 名称唯一；
- 140 字符 Windows 路径预算；
- 无 symlink 的自包含发布层；
- secret 声明；
- `[TODO:` placeholder 检查；
- deterministic build；
- root `.agents/plugins/marketplace.json` 和 `plugins/codex/plugins/` 两条 sparse path；
- GitHub Actions 自动生成、验证和 `[skip codex-marketplace]` 写回机制。

### 8.3 新增测试

至少覆盖：

- 中央九插件精确列表和安装分类；
- `research-presentations` 与 `business-presentations` trigger eval，不互相误触发；
- 小型 PPTX 编辑只路由官方能力，不触发 orchestration；
- `writing-style` 与 `research-writing` 的正例、反例和组合例；
- `web-development` 与官方 `build-web-apps` 的串联路由；
- `ai-skills-repository-maintainer` 禁止 implicit invocation；
- CardiacNexus 不出现在中央 Marketplace，项目 descriptor 指向 repo-local source；
- Notion/GitHub source history 一行记录、append-only 和 provenance 完整性；
- 临时 clone/export 不被追踪；
- icon manifest、aggregate openai.yaml 和资产路径；
- CUHK 模板完整性、Beamer 编译和 PPTX 渲染；
- Asteria/TRACE Markdown → deck plan → PPTX 的端到端 fixture。

---

## 9. 推荐执行顺序

### Phase 0：现状和官方能力审计

- 读取当前 main、registry、profiles、Marketplace config、builder、tests 和 README。
- 读取已安装官方 Presentation/Slides、LaTeX、Notion 和 `build-web-apps` 的公开接口。
- 生成当前中央/项目 Skill 冲突、重复、安装范围和 provenance 报告。

### Phase 1：架构与安装模型

- 更新中央九插件配置。
- 重构 `workflow-core`、`ai-skills-core`、`writing-style`、`research-writing` 和 `web-development` 的 App-facing 边界。
- 建立 profiles 和 README 安装矩阵。

### Phase 2：CardiacNexus 迁移

- 在 CardiacNexus repo 建立 canonical `.agents/skills`。
- 更新 `AGENTS.md` 和项目测试。
- 从中央 Marketplace 和中央完整 source 副本中迁出。

### Phase 3：Presentations

- 建立两个独立 Skill、共享 foundation、deck-plan 和官方兼容文档。
- 整理 CUHK Beamer/PPTX 双模板。
- 完成 Asteria/TRACE fixture 和 QA 闭环。

### Phase 4：图标

- 先完成中央插件与 App-facing Active Skills。
- 再覆盖全部 active source Skills。
- 运行 contact sheet 人工检查。

### Phase 5：外部来源与 Notion intake

- 建立统一 `INTEGRATION_HISTORY.md` 和 provenance audit。
- 迁移现有 cloned source 记录。
- 支持 Notion 页面/GitHub Skill 的审查、提炼、合并、记录和临时内容清理。

### Phase 6：生成、测试和真实安装

运行：

```bash
python3 scripts/skills.py registry --write
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
python3 scripts/skills.py catalog --write
python3 scripts/provenance_audit.py --check
python3 scripts/icon_audit.py --check
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
python3 scripts/build_codex_marketplace.py --path-report
python3 -m unittest discover -s tests
```

随后在 Codex App 做真实 Marketplace 安装，并分别验证：

- 全局 baseline；
- research main；
- presentation desktop；
- frontend + official `build-web-apps`；
- medical/bioinformatics project profile；
- CardiacNexus repo-local Skills；
- Notion/GitHub 外部来源整合 dry-run。

---

## 10. 最终验收标准

只有同时满足以下条件才可声明本 TODO 完成：

1. 中央 Marketplace 只包含九个通用插件，CardiacNexus 已迁为 repo-local canonical Skills。
2. README 清楚回答：所有机器装什么、主力科研机器装什么、桌面 PPT 环境装什么、前端场景装什么、领域插件何时装、`ai-skills-core` 何时不装、纯 compute node 为什么不装。
3. `writing-style` 与 `research-writing` 有明确边界和 trigger eval。
4. `presentations` 有两个独立 Active Skills，科研和商业场景互不干扰，并与官方 Presentation/LaTeX 协作。
5. `web-development` 作为外部设计参考、视觉系统和科研产品补充，与官方 `build-web-apps` 串联，而不是重复实现。
6. CUHK Beamer 和可编辑 PPTX 模板从同一设计 token 出发，默认路由正确。
7. 中央插件和全部 App-facing Active Skills 均有合法、清晰、可验证的图标；P1 最终覆盖全部 active source Skills。
8. 外部 GitHub/Notion 内容经过审查和提炼；临时 clone/export 删除；统一 history 每次整合只留一行；目标 Skill provenance 和必要 license/attribution 完整。
9. generated layer、路径预算、无 symlink、secret、placeholder、determinism、CI 和 Windows sparse checkout 全部通过。
10. 至少完成一次真实端到端用例：从 Asteria/Marked TRACE v3 Markdown 生成可编辑 CUHK 组会 PPTX、渲染预览、deck plan 和 QA 报告。
