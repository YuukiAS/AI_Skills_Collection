# TODO：为全部 Skill 补齐图标，并建立与 OpenAI Presentation 协作的独立演示文稿插件

## 0. 任务定位

这是当前最高优先级的仓库工作。需要同时完成两个互相关联但应独立验收的工作流：

1. 为 Codex Marketplace 中的插件、应用层 active skill，以及最终所有 `status: active` 的源 skill 建立可维护、可追踪、可验证的图标体系。
2. 建立一个独立的 `presentations` 插件，使 Codex 能把 Markdown、论文、已有 PPTX 和项目材料转换为专业演示文稿，同时与 OpenAI 已安装的官方 Presentation/Slides 能力协作，而不是复制或争夺同一层职责。

本任务不是简单地批量放若干 PNG，也不是把现有 `pptx` 与 `scientific-slides` 原样重新打包。必须先理清发布层、触发边界、模板资产、来源许可、输入规范和 QA，再实施。

## 1. 当前事实与约束

### 1.1 仓库层级

- `skills/` 是正式源层；行为、参考材料和模板应优先在这里修改。
- `scripts/codex_marketplace_config.json` 是 Codex App 发布配置。
- `.agents/plugins/marketplace.json` 与 `plugins/codex/plugins/` 是生成发布层，不得手工维护。
- 任何源层或发布配置变更都必须重新运行 Marketplace builder，并提交生成结果。
- 当前 builder 对插件数量设置了 `MAX_MARKETPLACE_PLUGINS = 9`，测试也固定断言当前九个插件；新增 `presentations` 前必须解决这个约束，而不是让测试失效后绕过。
- 当前 builder 还执行 active skill 数量上限、跨插件名称冲突检查和 140 字符 Windows 路径预算；新增模板和图标不得破坏这些 gate。

### 1.2 当前演示文稿能力的问题

- `skills/tools/documents-media/pptx/` 是一套较完整的底层 PPTX 读写、OOXML、PptxGenJS 与渲染 QA 说明。它与 OpenAI 官方 Presentation/Slides 能力在“文件实现层”明显重叠。
- `skills/science/communication/scientific-slides/SKILL.md` 目前把 Nano Banana Pro/OpenRouter 生成整页图片作为默认路径，并引用了仓库中并不存在的 `scripts/generate_slide_image.py`、`references/beamer_guide.md`、若干模板和资源。它不能直接作为新插件的可靠基础。
- 当前 `research-writing` 插件中的聚合 skill `research-documents` 同时发布 `pptx` 和 `scientific-slides`。如果再增加一个广义 presentation skill，会造成触发边界重复。
- 新插件必须保留可编辑、可复现、可审计的演示文稿工作流，不能把整页 AI 图片冒充可编辑 PPTX，也不能依赖未声明的第三方 API key。

### 1.3 当前图标能力的问题

- Marketplace 生成的插件 manifest 目前只写固定 `brandColor`，没有生成 `composerIcon` 或 `logo`。
- 大多数源 skill 没有 `agents/openai.yaml`，或者没有 `icon_small`、`icon_large`。
- 现有 icon design reference 引用了缺失的 Gemini 图标生成脚本，不能作为唯一实现。
- `pptxgenjs.md` 中已经使用 `react-icons` 作为图标来源示例。用户提到的“Reicon”可能是 React Icons，也可能是另一套图标库；实现前先确认名称，不要把猜测写进正式来源记录。
- CardiacNexus 等项目可能已有 favicon、logo 或可复用视觉资产。必须先在对应项目仓库中查找和验证，不能仅凭文件名猜测路径。

## 2. 总体设计原则

### 2.1 演示文稿职责分层

新插件负责“演示文稿思考层”，包括：

- 分析输入材料；
- 判断商业模式或科学/工程模式；
- 确定受众、时长、叙事与信息密度；
- 从 Markdown、论文、图表和已有 deck 中提取可信内容；
- 生成结构化 deck plan；
- 选择模板、版式、视觉语言和引用策略；
- 把 deck plan 交给官方 Presentation/Slides 能力完成 PPTX 的底层构造、编辑、导出和渲染；
- 执行来源忠实度、内容和视觉 QA。

OpenAI 官方 Presentation/Slides 能力负责“文件实现层”，包括：

- 创建或编辑 `.pptx`；
- PptxGenJS、OOXML、PowerPoint 对象、导出和渲染等底层机制；
- 具体 slide 对象、文本框、图表、图片和布局写入。

不得在新 skill 中复制一份完整官方 Presentation skill。可以保留少量兼容说明、模板接口和失败时的受控 fallback，但不能维护两套等价底层引擎。

### 2.2 图标职责分层

- 插件图标用于 Marketplace 卡片与 composer：每个用户可见插件至少有 `composerIcon`、`logo` 和 `brandColor`。
- Skill 图标用于 skill 列表、chip 或入口：每个应用层 active skill 至少有 `icon_small`、`icon_large`、`brand_color` 和明确的 `display_name`。
- 源 skill 图标属于源层；生成聚合 skill 的图标由 Marketplace builder 从发布配置生成。
- 生成发布层只复制和生成，不作为手工修改来源。

### 2.3 默认模板规则

除非用户明确指定其他模板，所有演示文稿默认使用本任务引入的 CUHK 模板视觉体系。这里的“使用模板”包括：

- 默认 PPTX：使用与上传 Beamer 模板视觉一致、但适配标准 16:9 和 PowerPoint 编辑能力的 CUHK PPTX 模板。
- 明确要求 Overleaf、Beamer、LaTeX 或数学原生 PDF：使用 CUHK Beamer 模板生成 `.tex` 和 `.pdf`。
- 明确提供公司、课程、会议或项目模板：用户模板优先。
- 项目仓库已有专用模板时，项目模板优先于全局 CUHK 默认。

商业演示与科学演示的叙事和内容规范不同，但在未指定其他品牌模板时，二者都可以使用 CUHK 默认视觉体系。

## 3. 工作流 A：图标系统

## 3.1 覆盖范围与优先级

按两个阶段实施，但最终不能停在第一阶段。

### P0：Codex App 用户可见层

- [ ] 当前全部 Marketplace 插件。
- [ ] 新增的 `presentations` 插件。
- [ ] 每个插件发布的全部 active skill，包括 generated aggregate skill。
- [ ] 生成后的 `plugin.json` 和 `agents/openai.yaml` 均能解析并引用存在的资产。

### P1：完整源 skill 层

- [ ] 以 `registry.json` 和 source frontmatter 为事实来源，覆盖全部 `status: active` 的源 skill。
- [ ] archived、inactive 或仅作为 `_src` snapshot 的说明文件不计入强制覆盖。
- [ ] 为 CLI 安装到 repo/user 的 skill 同样保留图标元数据和资产。
- [ ] 最终把完整覆盖设为硬 gate，而不是永久停留在 report-only。

## 3.2 图标来源优先级

对每个插件或 skill 按以下顺序选择：

1. **已有项目/产品资产**：例如项目 favicon、logo 或已发布视觉标识。CardiacNexus 作为首个审计对象，但必须记录真实仓库、路径、commit/ref、许可和哈希。
2. **许可清晰的图标库**：优先从 React Icons 所汇集的具体图标集、Lucide、Heroicons、Material Symbols、Remix Icon、Bootstrap Icons 等中选择。必须记录“具体图标集”的许可证，不能只写 React Icons。
3. **Codex 直接绘制的简单 SVG**：仅在没有合适现成图标、或项目需要独特符号时使用。SVG 应是可审查的文本资产，不依赖外部生成 API。
4. **禁止默认使用**：来源不明的搜索结果图片、带水印资产、从网站截图裁出的品牌标识、无法确认许可的图标包、嵌入字体或脚本的 SVG。

不要把整套第三方 icon library vendoring 到仓库，只复制实际使用的少量图标，并保留必要 attribution。

## 3.3 统一风格规范

- [ ] 优先使用单色或双色矢量图标；不同插件可有品牌色，但线条、留白和视觉重量应统一。
- [ ] 小图标默认 `viewBox="0 0 24 24"`，无文本、无嵌入字体、无脚本、无外部 URL。
- [ ] SVG 必须有可理解的 `<title>` 或由对应 YAML 提供可访问名称。
- [ ] 同一插件内的 active skills 应形成视觉家族，但不能全部使用无法区分的同一图形。
- [ ] 在 16、24、48、128 和 512 像素下检查清晰度。
- [ ] 同时检查浅色和深色界面；不能依赖透明度过低的细线。
- [ ] 可共享同一图标的 skill 必须在 provenance 中显式说明原因；禁止意外重复。

## 3.4 建议目录与配置

插件源资产建议放在：

```text
assets/codex/plugin-icons/<plugin-name>/
  composer.svg
  logo.png
  source.json
```

源 skill 资产继续放在各自目录：

```text
skills/.../<skill-name>/
  agents/openai.yaml
  assets/
    icon-small.svg
    icon-large.png
```

其中 `source.json` 或统一的 `scripts/icon_sources.json` 至少包含：

```json
{
  "target_type": "plugin-or-skill",
  "target_id": "cardiacnexus",
  "source_type": "repo-asset | icon-library | generated-svg",
  "source_repository": "owner/repo or null",
  "source_path": "path or null",
  "source_ref": "commit/tag or null",
  "source_url": "canonical project page or null",
  "icon_set": "specific icon set or null",
  "icon_name": "icon identifier or null",
  "license": "SPDX or reviewed text",
  "attribution": "required attribution or null",
  "sha256": "asset hash",
  "notes": "why this icon represents the target"
}
```

具体采用分散 `source.json` 还是统一 manifest，由实现者在不重复数据的前提下选择；但最终必须可机器审计和生成人类可读汇总。

## 3.5 扩展 Marketplace 配置和 builder

- [ ] 为 `scripts/codex_marketplace_config.json` 中的 plugin entry 增加可配置的 `brandColor`、`composerIcon`、`logo`。
- [ ] `build_plugin_json()` 不再对所有插件硬编码 `#2563EB`，而是读取配置并输出相对路径。
- [ ] builder 把插件图标复制到生成插件的 `assets/`，并在 `.codex-plugin/plugin.json` 中写入 `interface.composerIcon` 与 `interface.logo`。
- [ ] copy skill 优先保留源目录中的 `agents/openai.yaml` 和 `assets/`。
- [ ] aggregate skill entry 增加应用层 interface 元数据，builder 生成：

```text
plugins/codex/plugins/<plugin>/skills/<artifact-id>/
  SKILL.md
  agents/openai.yaml
  assets/icon-small.svg
  assets/icon-large.png
  _src/...
```

- [ ] aggregate skill 的 `openai.yaml` 至少包含 `display_name`、`short_description`、`icon_small`、`icon_large`、`brand_color`、`default_prompt`。
- [ ] 不得把短 artifact id 当作用户可见 display name 或 provenance。
- [ ] 所有新增路径继续满足 140 字符预算。

## 3.6 图标审计工具

新增一个机器可运行的审计入口，例如：

```bash
python3 scripts/icon_audit.py --scope marketplace
python3 scripts/icon_audit.py --scope active-skills
python3 scripts/icon_audit.py --contact-sheet build/icon-contact-sheet.png
python3 scripts/icon_audit.py --check
```

工具至少检查：

- [ ] P0/P1 覆盖率及缺失清单。
- [ ] 所有 YAML/JSON 引用路径存在且位于允许目录。
- [ ] 扩展名、文件尺寸、PNG 像素尺寸和 SVG viewBox。
- [ ] SVG 不含脚本、远程资源、嵌入字体、`foreignObject` 或明显不安全内容。
- [ ] source/provenance 字段完整，哈希与文件一致。
- [ ] 近重复或完全重复图标，并区分“有意共享”和“意外重复”。
- [ ] 生成带名称标签的联系表供人工检查。

不要依赖 ImageMagick 或平台特有 GUI；优先使用仓库可声明的 Python/Node 依赖，并在 CI 中可重复运行。

## 3.7 图标测试与验收

- [ ] 为 plugin manifest 图标字段增加 builder 单元测试。
- [ ] 为 aggregate skill `agents/openai.yaml` 生成增加测试。
- [ ] 缺失图标、错误相对路径、非法 SVG、未知 license、哈希漂移时测试失败。
- [ ] 当前真实 Marketplace 生成一次并通过 icon audit 与 path report。
- [ ] Codex App 中人工安装 Marketplace，确认每个插件卡片显示正确 logo/composer icon。
- [ ] 逐个检查应用层 active skill 的图标、名称与描述，没有空白图标或错误继承。
- [ ] P1 完成后，`status: active` 源 skill 图标覆盖率为 100%。

## 4. 工作流 B：独立 `presentations` 插件

## 4.1 先检查官方 Presentation/Slides 能力

开始编码前必须在当前 Codex App/CLI 环境中读取已安装的 OpenAI 官方 Presentation/Slides skill 或插件，记录：

- [ ] 实际插件名和可调用 skill 名；不要凭记忆硬编码 `$slides`、`$presentation` 等名称。
- [ ] 支持的输入、输出与模板方式。
- [ ] 是否以 PptxGenJS、artifact tool、OOXML 或其他机制实现。
- [ ] 是否支持编辑现有 PPTX、speaker notes、charts、images、PDF preview 与 visual QA。
- [ ] 官方能力明确拥有的职责，以及本仓库需要补充的缺口。

将兼容性结论写入：

```text
skills/tools/documents-media/presentation-workflows/references/openai-presentation-compatibility.md
```

该文件只记录公开接口和协作方式，不复制官方 skill 全文。

## 4.2 新插件与 skill 结构

建议建立一个用户可见插件和一个主要 active skill：

```text
presentations
└── presentation-workflows
```

源层建议：

```text
skills/tools/documents-media/presentation-workflows/
  SKILL.md
  agents/openai.yaml
  assets/
    icon-small.svg
    icon-large.png
    templates/
      cuhk/
        README.md
        design-tokens.json
        beamer/
        pptx/
  references/
    openai-presentation-compatibility.md
    business-presentations.md
    scientific-presentations.md
    markdown-ingestion.md
    deck-plan-schema.md
    template-routing.md
    source-fidelity-and-citations.md
    visual-qa.md
  scripts/
    ingest_markdown.py
    validate_deck_plan.py
    validate_template_assets.py
```

实际脚本数量可以减少，但不得把核心输入解析、schema 验证和模板完整性完全留给自然语言临场发挥。

只暴露一个广义 orchestration skill，商业和科学模式作为内部路由，不要再创建多个互相竞争的“business-ppt”“scientific-ppt”“pptx”触发器。

## 4.3 解决第十个插件的位置

当前 Marketplace 由仓库代码固定为九个插件。按以下顺序处理：

1. [ ] 先验证 Codex App 当前是否真实限制最多九个插件。
2. [ ] 如果九是本仓库人为预算而非产品限制，把上限提高到至少十，更新测试、文档与真实安装测试。
3. [ ] 如果产品确实限制九个插件，优先把 `workflow-core` 作为 active skill 合并进 `ai-skills-core` 插件，保持原 skill 名称和功能，腾出一个用户可见插件位置。
4. [ ] 不要为了省一个位置把 `presentations` 隐藏回 `research-writing`；用户需要一个可独立安装、可明确识别的演示文稿插件。
5. [ ] 不得删除任何核心 workflow，只允许调整其插件归属。

## 4.4 清理现有触发冲突

- [ ] 从 Codex App 的 `research-writing` → `research-documents` aggregate 中移除 `pptx` 与 `scientific-slides` 的应用层发布。
- [ ] 保留 PDF、DOCX、MarkItDown 和科学示意图等研究文档能力。
- [ ] `skills/tools/documents-media/pptx/` 可以保留为 CLI/兼容 fallback 或归档参考，但其 broad trigger 不再与新插件同时发布。
- [ ] `skills/science/communication/scientific-slides/` 进行迁移审计：
  - 有价值的叙事、时长、科学引用和视觉 QA 内容迁入新 skill 的 references；
  - 删除或改写对不存在脚本、模板和 OpenRouter/Nano Banana 默认路径的依赖；
  - 标记 deprecated/archive，或把它缩减为指向新 workflow 的迁移说明；
  - 不得继续作为 Codex App active skill 发布。
- [ ] 更新 catalog、domain 文档和 provenance，避免同一能力在三个位置继续声称自己是默认入口。

## 4.5 触发边界

`presentation-workflows` 的触发描述应覆盖：

- 从 Markdown、Asteria 导出、论文、报告、代码结果、现有 PPTX 或 PDF 创建或重构演示文稿；
- 研究组会、学术报告、答辩、journal club、技术汇报、商业汇报和一般公司 presentation；
- 用户需要决定 deck 结构、叙事、受众、模板、图表、引用、speaker notes 或信息密度；
- 用户需要使用本仓库的默认 CUHK 模板。

它不应声称自己直接实现所有 PowerPoint 文件操作。执行过程中在需要 `.pptx` 文件时，明确联合调用官方 Presentation/Slides 能力。

## 4.6 中间表示：`deck-plan`

所有非微小编辑任务先生成一个结构化中间表示，再构建 PPTX。建议采用 YAML，schema 至少包括：

```yaml
metadata:
  title: ""
  subtitle: ""
  author: ""
  affiliation: ""
  date: ""
  audience: "specialist | mixed | general | executive"
  mode: "scientific | business"
  purpose: "group-meeting | conference | defense | journal-club | company | other"
  duration_minutes: 15
  language: "en | zh | mixed"
  template: "cuhk-default"
  output: "pptx"
  source_files: []

slides:
  - id: "s01"
    title: ""
    purpose: ""
    source_anchors: []
    key_message: ""
    content: []
    equations: []
    visuals: []
    layout_hint: ""
    citations: []
    speaker_notes: ""
    backup: false
```

要求：

- [ ] schema 有版本号和验证脚本。
- [ ] 每页只有一个主要信息目标，但不能机械地把每个 Markdown heading 映射成一页。
- [ ] `source_anchors` 能回溯到原 Markdown section、页码、图号、代码结果或现有 slide。
- [ ] 数学公式保留 LaTeX 原文；不能在解析时丢失反斜杠、上下标或 equation numbering。
- [ ] 图片、表格、引用、脚注和 speaker notes 有明确字段。
- [ ] 任何新增事实、数字或结论都必须能追溯到输入或经允许的检索来源。
- [ ] deck plan 作为最终交付物的一部分保留，便于后续迭代。

## 4.7 输入适配器

至少支持：

### 通用 Markdown

- [ ] 解析 frontmatter、标题层级、段落、列表、代码块、LaTeX、图片、表格、脚注和引用。
- [ ] 根据时长、受众、内容复杂度和视觉素材分块，而不是一标题一页。
- [ ] 过长段落先压缩为“主结论 + 支撑证据 + speaker notes”，不能直接把全文塞进 slide。

### Asteria / Marked TRACE v3 Markdown

这是高优先级真实用例：从 Asteria 导入 Marked TRACE v3 的 Markdown，制作导师能快速理解的组会 PPT。

- [ ] 先取得一份真实、可脱敏的 Marked TRACE v3 Markdown fixture；没有 fixture 时不得声称完整支持。
- [ ] 识别模型定义、版本变化、符号表、公式、假设、设计动机、结果、未解决问题和 reviewer/导师标记。
- [ ] 将长篇方法文档转换为适合口头汇报的结构，而不是复刻 Asteria 阅读界面。
- [ ] 对公式密集部分保留关键公式，次要推导放 speaker notes 或 backup slides。
- [ ] 生成“本周变化、为什么改变、证据、风险、需要导师决定什么”的组会主线。
- [ ] 建立 golden fixture 和 end-to-end regression test。

### 论文/PDF

- [ ] 提取标题、研究问题、方法、主要图表、结果、局限和引用。
- [ ] 使用图号、页码或 section 作为 source anchor。
- [ ] 论文中的复杂多面板图应重新排版为可读 slide，不要缩成不可辨识的整页截图。

### 现有 PPTX

- [ ] 使用官方 Presentation/Slides 能力读取和编辑。
- [ ] 保留用户明确要求保留的母版、图表和 speaker notes。
- [ ] 先做 visual inventory，再决定复用、重排或重建。

## 4.8 科学/工程模式

默认适用于组会、seminar、答辩、方法报告和 TRACE/CardiacNexus/CARE 等研究项目。重点是让听众快速理解“为什么做、做了什么、结果说明什么、差距在哪里、下一步需要什么决定”。

建议的组会默认叙事：

1. 标题与一句话进展。
2. 上次会议后的目标和上下文。
3. 本次最重要的变化。
4. 问题定义与当前模型/系统。
5. 方法或架构的关键机制。
6. 必要公式、符号与假设。
7. 实验、验证或当前证据。
8. 结果解释，而不只是图表陈列。
9. 失败、局限、不可替代性尚未证明之处。
10. 需要导师讨论或决定的问题。
11. 下一步与预期验收。
12. 推导、额外实验和完整表格放 backup。

科学模式要求：

- [ ] 公式、统计量、图表和单位准确。
- [ ] 一页主结论明确，图题和坐标可在投影环境阅读。
- [ ] 结果图优先使用真实输出；禁止生成看似真实的假数据图。
- [ ] 引用用简短 author-year 或编号放页脚，完整参考文献保留在末页或附录。
- [ ] 区分已完成结果、计划、假设和推测。
- [ ] 为复杂方法提供概念图，但概念图不能替代正式模型说明。

## 4.9 商业模式

默认适用于一般公司、非理工专业、项目提案、执行汇报和决策 deck。它不是科学模式换一套颜色。

建议主线：

1. Executive summary。
2. 问题或机会。
3. 证据与规模。
4. 用户/市场/组织影响。
5. 方案与选择依据。
6. 实施路径与资源。
7. 风险、依赖和缓解措施。
8. 决策请求与下一步。

商业模式要求：

- [ ] 先结论后证据，减少方法细节。
- [ ] 不伪造市场规模、增长率、财务预测、用户反馈或 KPI。
- [ ] 图表必须标明数据来源和假设。
- [ ] 使用可编辑 diagram、chart 和简洁视觉，不把装饰性图片当作论证。
- [ ] 当用户没有公司模板时仍使用 CUHK 默认视觉；有公司模板时品牌模板优先。

## 5. CUHK 默认模板

## 5.1 输入资产

本任务对应的本地输入文件：

```text
/mnt/data/CUHK Template.zip
/mnt/data/CUHK Template.pdf
```

当前文件哈希：

```text
CUHK Template.zip
sha256: 5cbe4a545d8abbab007f5f0aceec405138f8035b9dcb09c617e1e7cf7b525ee9

CUHK Template.pdf
sha256: a62a4bb5ec2296b875ffe9ff8c1d850b88797e27a74aac7d64f576abb91daa7e
```

实现时先重新计算哈希并确认输入未变化。

ZIP 中有运行时所需的 Beamer 源文件、theme、背景和 logo，也有示例图片、XCF 源文件、`.vscode` 和空 bibliography。不要无选择地把全部 1:1 复制进 Marketplace。

## 5.2 模板审计

- [ ] 列出 ZIP 内容和引用关系，区分 runtime-required、authoring-source、sample-only 和 editor-only。
- [ ] 运行时至少审计 `main.tex`、`styles/beamerthemesintef.sty`、`styles/sintefcolor.sty`、背景与 logo。
- [ ] 示例 `Fig*`、`Table*`、`.vscode` 和未被使用的 XCF 不进入默认发布 payload，除非有明确理由。
- [ ] 保留原 theme 中对 SINTEF/Sapienza 派生来源和 GPL 条款的说明。
- [ ] 单独检查 CUHK logo、校名和品牌资产是否允许在公开 GitHub 仓库与可安装插件中再分发。
- [ ] 如果 logo/品牌再分发许可不清晰，不要静默提交：
  - 提供本地 `import_cuhk_template.py` 或用户模板路径配置；
  - 公共 repo 只保存可合法分发的 layout/token 和导入说明；
  - 在用户本地导入后仍可成为默认模板。
- [ ] 不提交任何字体文件。模板依赖系统字体时，记录 fallback，并在 CI 中验证。

## 5.3 共享设计 token

从 Beamer 模板抽取单一事实来源，例如：

```json
{
  "name": "cuhk-default",
  "primary": "#72256D",
  "accent": "#D4AF37",
  "background": "#FFFFFF",
  "text": "#222222",
  "muted": "#6B6B6B",
  "title_style": "split-purple",
  "navigation_style": "top-section-progress"
}
```

颜色值必须以实际源文件为准重新核对。Beamer 与 PPTX 共同读取或至少由同一 token 文件生成，避免两套视觉长期漂移。

## 5.4 双模板交付

### CUHK Beamer

- [ ] 整理最小可编译模板目录。
- [ ] 以 XeLaTeX/`latexmk` 为标准编译路径，并记录系统依赖。
- [ ] 保留标题页右侧紫色几何背景、CUHK 标识、顶部 section navigation、页码和结束页视觉。
- [ ] 补充研究常用 frame 示例：公式、双栏、全图、图加解释、方法流程、表格、references 和 backup。
- [ ] 不把示例研究内容当成模板的一部分。

### CUHK PPTX

- [ ] 新建真正可编辑的 16:9 `.pptx` 模板或 reference deck，而不是把 Beamer PDF 每页放成背景图。
- [ ] 使用与 Beamer 相同的设计 token 和视觉语言，但允许为标准 16:9 做必要重排。
- [ ] 原 Beamer 页面尺寸约为 20cm × 11cm，并非严格标准 16:9；PPTX 版本应明确使用标准 16:9，不要通过非等比拉伸复刻。
- [ ] 至少提供以下 layout：
  - title；
  - section divider；
  - standard content；
  - equation/model；
  - process/method；
  - full figure；
  - figure + interpretation；
  - comparison；
  - table；
  - references；
  - closing；
  - backup。
- [ ] 所有文本、图表、形状和占位区域可编辑。
- [ ] 使用官方 Presentation/Slides 能力创建和维护该模板；仓库 skill 只记录模板接口和选择规则。

## 5.5 默认输出规则

- 用户说“做 PPT”“做组会汇报”“从 Asteria Markdown 做 slides”：默认输出 `.pptx`，同时导出 `.pdf` 或 slide images 用于 QA。
- 用户明确说 Overleaf/Beamer/LaTeX/PDF：输出 `.tex`、必要资产和 `.pdf`。
- 用户需要两种格式：从同一 deck plan 生成 PPTX 与 Beamer，允许布局有差异，但内容、来源和 slide id 对齐。
- 最终保留：输入清单、`deck-plan.yaml`、可编辑源、最终文件、渲染预览和 QA 报告。

## 6. QA 与验证闭环

## 6.1 内容 QA

- [ ] 标题、作者、单位、日期、页序和 section 正确。
- [ ] 输入中的主要结论没有丢失或被反转。
- [ ] 公式、符号、数值、单位和引用可追溯。
- [ ] 没有残留 placeholder、示例图、模板作者信息或虚构数据。
- [ ] 每页 key message 与 speaker notes 一致。
- [ ] 科学 deck 明确区分结果、假设、计划和未解决问题。
- [ ] 商业 deck 明确区分数据、假设、预测和建议。

## 6.2 视觉 QA

每次生成都必须：

1. 渲染 PPTX/Beamer 为 PDF。
2. 把每页转为图片。
3. 生成 contact sheet 和单页检查图。
4. 列出问题，至少完成一次修复—重渲染—复查循环。

检查：

- [ ] 溢出、裁切、重叠和边距。
- [ ] 投影环境下的字号、公式和坐标轴可读性。
- [ ] 标题换行后装饰元素仍对齐。
- [ ] 引用、页码、顶部导航和内容不冲突。
- [ ] 图像没有不必要的拉伸、裁切或低分辨率。
- [ ] 深浅背景对比满足可读性。
- [ ] 不使用整页截图掩盖不可编辑内容。

## 6.3 自动测试

至少增加：

- [ ] CUHK Beamer 最小编译 smoke test。
- [ ] CUHK PPTX 打开/渲染 smoke test。
- [ ] 通用 Markdown → `deck-plan.yaml` snapshot test。
- [ ] 公式、表格、图片、引用和 footnote 解析测试。
- [ ] 真实脱敏 Asteria Marked TRACE v3 fixture → deck plan → PPTX end-to-end test。
- [ ] business fixture 与 scientific fixture 各一套 golden deck。
- [ ] template asset 引用完整性和哈希检查。
- [ ] Marketplace plugin/skill icon 生成与路径测试。
- [ ] 视觉回归使用容忍度或结构检查，不对 PDF 二进制做脆弱的逐字节相等。

## 7. 文档、发布与迁移

- [ ] 更新 `README.md` 的插件列表和安装说明。
- [ ] 更新 `docs/CODEX_MARKETPLACE.md`，说明 `presentations`、图标字段和官方 Presentation 协作边界。
- [ ] 更新 `docs/domains/documents-media.md`。
- [ ] 更新 `docs/domains/research-communication.md`。
- [ ] 更新 `docs/SKILL_CATALOG.md`、`registry.json` 和 provenance 汇总。
- [ ] 为旧 `pptx`/`scientific-slides` 的应用层入口写 migration note。
- [ ] 说明默认 CUHK 模板、模板覆盖优先级、品牌/许可限制和本地导入方式。
- [ ] 所有生成文档通过仓库现有生成命令更新，不手工修补生成结果。

发布前运行：

```bash
python3 scripts/skills.py registry --write
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
python3 scripts/skills.py catalog --write
python3 scripts/icon_audit.py --check
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
python3 scripts/build_codex_marketplace.py --path-report
python3 -m unittest discover -s tests
```

如果实际 CLI 短命令已安装，可以使用等价 `ai-skills ...` 命令，但 CI 应采用仓库内稳定入口。

## 8. 建议实施顺序

### Phase 1：审计和契约

- [ ] 读取官方 Presentation/Slides skill，形成 compatibility matrix。
- [ ] 审计 `pptx`、`scientific-slides`、research-writing aggregate 的重复与缺失。
- [ ] 审计九插件限制是否为产品限制。
- [ ] 审计 CUHK ZIP、PDF、theme 来源和品牌许可。
- [ ] 审计全部 P0/P1 图标目标和已有资产。
- [ ] 提交架构说明、deck-plan schema 和 icon provenance schema；暂不大规模生成资产。

### Phase 2：图标基础设施与 P0

- [ ] 扩展 Marketplace config 和 builder。
- [ ] 实现 icon audit、SVG 安全检查和联系表。
- [ ] 为现有九个插件、新 `presentations` 插件和所有应用层 active skills 补齐图标。
- [ ] 先使 P0 成为 CI 硬 gate。

### Phase 3：Presentation source skill 与模板

- [ ] 建立 `presentation-workflows`。
- [ ] 完成 business/scientific routing、deck-plan schema 和输入适配器。
- [ ] 完成 CUHK Beamer 最小模板与可编辑 CUHK PPTX 模板。
- [ ] 移除应用层旧触发冲突。

### Phase 4：真实用例

- [ ] 使用真实脱敏 Marked TRACE v3 Markdown 生成组会 deck。
- [ ] 验证导师阅读场景：进展、方法、公式、证据、问题和下一步清晰。
- [ ] 使用一份一般商业材料生成 business deck。
- [ ] 两种 deck 均通过内容、视觉和 source-fidelity QA。

### Phase 5：P1 完整图标覆盖

- [ ] 批量映射所有 active source skills。
- [ ] 对项目专用 skill 优先复用项目 favicon/logo。
- [ ] 人工检查 contact sheet，修复含义不符和过度重复。
- [ ] 将 active source skill 100% coverage 设为 CI gate。

### Phase 6：发布验收

- [ ] 全部单元测试、生成层 check、path budget 和 Windows sparse checkout 通过。
- [ ] 在 Codex App 中安装 Marketplace。
- [ ] 插件图标和 skill 图标显示正确。
- [ ] `presentation-workflows` 与官方 Presentation/Slides 同时启用时没有互相覆盖、循环调用或重复生成。
- [ ] 新建 TRACE 组会 PPT 和 business PPT 各一次。
- [ ] README、Marketplace 文档、catalog 和 provenance 与实际生成层一致。

## 9. 不允许的捷径

- 不手工编辑 `plugins/codex/plugins/` 或 `.agents/plugins/marketplace.json`。
- 不把同一个通用图标复制给全部 skill 后声称覆盖完成。
- 不使用来源不明的网页图片或无法确认许可证的 logo。
- 不把第三方完整 icon library 提交进仓库。
- 不提交字体文件。
- 不把 Beamer PDF 每页作为不可编辑背景来伪造 PPTX 模板。
- 不让整页图片生成成为科学 PPT 的默认路径。
- 不继续依赖仓库中不存在的脚本、reference 或 template。
- 不要求用户提供 OpenRouter/Gemini key 才能完成基础演示文稿工作流。
- 不机械地把 Markdown 标题逐个变成 slides。
- 不为补充官方插件而复制一套完整底层 Presentation 实现。
- 不在没有真实 Asteria fixture 的情况下宣布 Marked TRACE v3 已完整支持。
- 不通过删除引用、模板资产或缩短内容来规避路径预算和 QA。

## 10. 完成定义

只有同时满足以下条件，任务才算完成：

1. Codex App 中每个用户可见插件和 active skill 都有正确、可追踪的图标；所有 active 源 skill 最终达到 100% 图标覆盖。
2. 图标来源、许可证、哈希和含义可以机器审计；builder 与 CI 能阻止缺失或非法资产。
3. `presentations` 作为独立插件可安装，且不会与 OpenAI 官方 Presentation/Slides 或旧 repo skills 产生模糊的重复触发。
4. 默认 CUHK 视觉体系同时有可编译 Beamer 与真正可编辑的标准 16:9 PPTX 实现。
5. 未特别指定模板时，科学与商业 deck 都使用 CUHK 默认；用户或项目模板能可靠覆盖默认值。
6. 通用 Markdown、真实脱敏 Marked TRACE v3 Markdown、论文/PDF 和现有 PPTX 有明确输入路径。
7. TRACE 组会 deck 能把长 Markdown 转换为适合导师理解和讨论的汇报，而不是简单复制原文。
8. 科学 deck 与商业 deck 都有真实 fixture、可重复生成、source anchors、渲染预览和至少一轮修复—复查记录。
9. Marketplace builder、tests、icon audit、path report、文档和 Codex App 手工验收全部通过。
