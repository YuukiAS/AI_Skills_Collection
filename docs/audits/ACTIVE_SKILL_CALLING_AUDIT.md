# 活跃技能调用审计
## 范围与结论
本次是 Reviewer blocker 的定向返修，不进入第二阶段，也不改任何现有技能实现。源技能覆盖仍为 `149/149`。原始技能内容冻结在 `157552aae0d4871a4a333ed14fd1e56a000472ee`；本次返修基于 `ad1bdee51e1c29df8119ba7c91ffdcee06cc695d`。

## 安装可达性与自然调用性分离
上一版把 插件市场 暴露、profile/domain/单技能安装和 description 触发能力混成一个入口状态。本版改为两个独立维度：
- **安装可达性**：能力能否通过插件市场、推荐 profile、兼容 profile、domain 安装或单技能安装进入运行环境。
- **自然调用性**：假设技能已经安装并可见，用户只描述真实任务、不说内部 skill 名时，description 是否足以让模型选择该技能。

### 安装可达性结果
- 插件市场 可见：`35` 个源技能。
- 插件市场 不可见：`114` 个源技能。这里不能直接推导“没有入口”或“必须知道内部名”。
- 不在 插件市场 但推荐 profile 可达：`24`。
- 不在 插件市场 且主要靠兼容 profile/domain/单技能安装：`90`。
- 没有已知安装路径：`0`。

### 自然调用性结果
- 自然清晰：`64`。
- 边界模糊：`65`。
- 描述过窄：`1`。
- 依赖工具/产品名：`13`。
- 被宽技能遮蔽：`6`。
- 证据不足：`0`。

### 只是安装覆盖问题，不是调用说明问题的代表技能
这些技能不在 6 个 插件市场 插件中，但 description 本身已经覆盖自然任务语义；第二阶段不能仅凭 插件市场 不可见就要求改 description：
- `mcp-builder`：构建 MCP server；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `plugin-creator`：创建 Codex plugin；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `skill-creator`：创建或更新 Codex skill；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `skill-installer`：技能安装与 profile 设置；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `skill-library-analysis`：AI_Skills_Collection 维护与技能引入审计；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `bayesian-ppl-diagnostics`：统计建模、贝叶斯分析与仿真；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `pymc`：统计建模、贝叶斯分析与仿真；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `simpy`：统计建模、贝叶斯分析与仿真；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `statistical-analysis`：统计建模、贝叶斯分析与仿真；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `statsmodels`：统计建模、贝叶斯分析与仿真；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `esm`：生物信息数据库、单细胞、组学与基因组文件工作流；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `etetoolkit`：生物信息数据库、单细胞、组学与基因组文件工作流；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `flowio`：生物信息数据库、单细胞、组学与基因组文件工作流；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `neuropixels-analysis`：生物信息数据库、单细胞、组学与基因组文件工作流；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `phylogenetics`：生物信息数据库、单细胞、组学与基因组文件工作流；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `zarr-python`：生物信息数据库、单细胞、组学与基因组文件工作流；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `neurokit2`：临床医学证据、报告与安全边界文档；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `pyhealth`：临床医学证据、报告与安全边界文档；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `scikit-survival`：临床医学证据、报告与安全边界文档；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `consciousness-council`：科研构思、实验规划与策略推演；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `experiment-execution`：科研构思、实验规划与策略推演；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `hypogenic`：科研构思、实验规划与策略推演；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `hypothesis-generation`：科研构思、实验规划与策略推演；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `scientific-brainstorming`：科研构思、实验规划与策略推演；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `scientific-critical-thinking`：科研构思、实验规划与策略推演；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `what-if-oracle`：科研构思、实验规划与策略推演；自然调用证据：description 覆盖自然任务表达；未发现必须依赖内部名称的证据。
- `modal`：AI/ML 框架、实验与模型工程；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `pufferlib`：AI/ML 框架、实验与模型工程；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `stable-baselines3`：AI/ML 框架、实验与模型工程；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。
- `timesfm-forecasting`：AI/ML 框架、实验与模型工程；自然调用证据：description 给出了任务语义，用户不必说内部 skill 名。

## 重点冲突组
| 冲突组 | 涉及源技能 | 冲突类型 | 当前证据 | 可能调用后果 |
|---|---|---|---|---|
| 论文写作、论文流程与评审边界 | `scientific-writing`, `paper-workflow-orchestrator`, `nature-manuscript-workflow`, `peer-review`, `scholar-evaluation` | 宽技能与窄技能边界模糊 | 这些技能都覆盖论文文本、主张-证据、投稿准备、审稿意见或接受风险检查。 | 宽泛的“帮我改论文/审论文”可能需要先判断是正文写作、流程编排还是评审诊断。 |
| 文献检索、引用核验与数据库提供商边界 | `literature-review`, `citation-verification`, `citation-management`, `research-lookup`, `arxiv-database`, `biorxiv-database`, `pubmed-database`, `openalex-database`, `valyu-scientific-search`, `bgpt-paper-search`, `pyzotero` | 工作流与提供商工具竞争 | Research Writing 聚合入口含文献、引用、引用管理和 research-lookup；多个数据库技能也能直接响应检索。 | 自然检索请求可能先落到提供商，而不是先判断综述、证据卡或引用核验目标。 |
| OCR、PDF、DOCX 与通用转换边界 | `academic-paper-writer-pro`, `ocr-kb`, `markitdown`, `pdf` | 相邻任务边界模糊 | academic-paper-writer-pro 与 ocr-kb 都覆盖扫描 PDF/OCR 恢复和 DOCX/Markdown 交付；markitdown/pdf 覆盖更通用的转换。 | 扫描论文清理可能被当作普通 PDF 转换，而不是 OCR 质量恢复或学术交付修复。 |
| 图、流程图、科学插图与图片生成边界 | `markdown-mermaid-writing`, `drawio-diagrams`, `d2-diagrams`, `plantuml-diagrams`, `excalidraw-diagrams`, `scientific-schematics`, `scientific-visualization`, `scientific-figure-qa`, `generate-image`, `imagegen`, `canvas-design`, `infographics` | 输出媒介与任务目的竞争 | 文本图 DSL、可编辑图、科学插图、图像生成、信息图和静态设计都响应可视化请求。 | 用户说“画个图/做个 figure”时，需要第二阶段判断是结构图、出版图、位图还是信息图。 |
| 前端规划、实现与验收链路 | `product-ux-planning`, `visual-direction`, `design-system-tokens`, `implementation-react-tailwind`, `responsive-accessibility-review`, `webapp-testing`, `research-product-frontend`, `frontend-reference-research`, `frontend-visual-systems`, `figma-design-to-code`, `motion-interaction` | 安装入口主要在 profile，内部链路边界较长 | 前端技能在 profile/direct 可达，但不在 6 个 插件市场 插件中；自然任务从规划到实现到验收跨度大。 | 这是插件市场覆盖缺口，不等于 description 不可调用；第二阶段应判断是否需要更清晰的上游入口。 |
| 生物信息聚合能力与具体工具边界 | `bioinformatics-database-retrieval`, `biopython`, `pubmed-database`, `pysam`, `tiledbvcf`, `zarr-python`, `polars-bio`, `gtars`, `geniml`, `deeptools`, `arboreto`, `scanpy`, `scvi-tools`, `anndata`, `scvelo` | 聚合入口与命名工具边界 | Bioinformatics 聚合覆盖 10 个核心技能，另有多个专门工具、平台和数据结构 active 技能通过 profile/domain/direct 可达。 | 常见生信任务有聚合入口，专门平台或工具请求仍可能需要说出工具名或由聚合入口二次路由。 |
| 医学影像聚合覆盖与术语测量边界 | `cardiac-mri`, `pydicom`, `medical-imaging-classical-features`, `medical-imaging-deep-learning`, `pathml`, `medical-imaging-terminology-measurement` | 聚合覆盖缺口 | Medical Imaging 插件聚合 CMR/DICOM/features/deep learning/pathology，但 active 的 terminology-measurement 不在插件聚合源列表中。 | 术语、测量约定、结构化报告边界请求可能不从 插件市场 医学影像入口自然进入。 |
| 临床医学证据与安全边界 | `clinical-guideline-checking`, `medical-literature-evidence-review`, `clinical-reports`, `clinical-decision-support`, `treatment-plans`, `medical-safety-boundaries` | 插件市场覆盖缺口与安全边界风险 | 临床技能 active 且可通过 domain/单技能安装，但不在 6 个 插件市场 插件中。 | 这不是全库不可达；问题是 插件市场 没有临床顶级入口，安装后仍需确保安全边界技能不被泛科研写作遮蔽。 |
| 数据科学工具相邻边界 | `polars`, `dask`, `vaex`, `geopandas`, `networkx`, `scikit-learn`, `shap`, `umap-learn`, `aeon`, `pymoo`, `sympy`, `matlab`, `exploratory-data-analysis` | 自然任务与工具选择边界 | 多数 description 有任务语义，不只是库名；但加速、分布式、超大表格、地理数据、网络、解释性、降维等边界相邻。 | 没有 插件市场 统计/数据科学入口是安装覆盖问题；已安装后的主要风险是工具选择边界，而非必须知道内部名。 |
| AI/ML 框架曝光不均 | `pytorch-lightning`, `transformers`, `torch-geometric`, `langchain`, `llamaindex`, `opencv`, `fastai`, `timesfm-forecasting` | 插件暴露与通用 AI/ML 任务边界不一致 | Medical Imaging 插件通过 ai-ml-imaging 暴露 PyTorch Lightning 和 Transformers，其他 AI/ML 技能主要依赖 profile/domain/direct。 | 通用模型工程任务可能被误认为只属于医学影像插件；但如 timesfm-forecasting 的 description 本身可自然触发单变量预测任务。 |
| 演示、海报与论文转传播材料边界 | `research-presentations`, `business-presentations`, `latex-posters`, `pptx-posters`, `paper-2-web` | 受众和格式边界相邻 | presentation-desktop profile 覆盖研究/商业 deck，海报和 paper-to-media 技能另行 active。 | 用户请求 slides/poster/web summary 时，需要区分受众、格式和是否来自论文。 |
| OpenAI 文档与系统构建辅助技能 | `openai-docs`, `mcp-builder`, `skill-creator`, `plugin-creator` | description 宽窄不均 | mcp-builder、skill-creator、plugin-creator 有明确构建任务语义；openai-docs description 更强调 openai docs workflow 名称。 | 这里不应整体判为内部名依赖；真正需要复查的是 openai-docs 的自然任务覆盖是否过窄。 |

## 12 组冲突的成对边界样例
### 论文写作、论文流程与评审边界
- 区分 `scientific-writing` 与 `paper-workflow-orchestrator`：
  - 应进入 `scientific-writing`：把 Results 第一节改成完整论文段落，保留统计量和图号。
  - 应进入 `paper-workflow-orchestrator`：先帮我规划这篇论文的主张-证据骨架、每节职责和图文同步检查。
  - 真实模糊边界：这篇论文结构有点乱，帮我改到能投稿。
- 区分 `peer-review` 与 `scholar-evaluation`：
  - 应进入 `peer-review`：按审稿人视角指出这篇稿子的主要拒稿风险和 rebuttal 准备点。
  - 应进入 `scholar-evaluation`：按一套评分维度系统评价这篇工作的研究质量、方法、分析和写作。
  - 真实模糊边界：帮我判断这篇论文质量够不够。
### 文献检索、引用核验与数据库提供商边界
- 区分 `literature-review` 与 `research-lookup`：
  - 应进入 `literature-review`：围绕这个方向做相关工作梳理，按方法路线和研究空白组织。
  - 应进入 `research-lookup`：帮我现在查几篇最新论文，给出题名、年份和链接。
  - 真实模糊边界：找一些论文并总结现状。
- 区分 `citation-verification` 与 `pubmed-database`：
  - 应进入 `citation-verification`：检查这条 PMID/DOI 是否真实存在，并确认正文主张有没有被引用支持。
  - 应进入 `pubmed-database`：用 PubMed MeSH 布尔查询检索这类疾病的临床研究。
  - 真实模糊边界：查一下这篇医学论文引用是否可靠。
### OCR、PDF、DOCX 与通用转换边界
- 区分 `ocr-kb` 与 `markitdown`：
  - 应进入 `ocr-kb`：这份扫描 PDF 有公式和表格，按页 OCR 成可编辑 Markdown 并做质量核查。
  - 应进入 `markitdown`：把这个 DOCX、PPTX 和网页批量转成 Markdown。
  - 真实模糊边界：把这个 PDF 转成 Markdown。
- 区分 `academic-paper-writer-pro` 与 `pdf`：
  - 应进入 `academic-paper-writer-pro`：修复这篇扫描论文的版式、参考文献和断点，交付 DOCX/Markdown。
  - 应进入 `pdf`：合并这几个 PDF 并提取其中的图片。
  - 真实模糊边界：处理这篇 PDF 论文，最后给我可编辑版本。
### 图、流程图、科学插图与图片生成边界
- 区分 `markdown-mermaid-writing` 与 `drawio-diagrams`：
  - 应进入 `markdown-mermaid-writing`：在 Markdown 报告里加一个 Mermaid 流程图说明数据流。
  - 应进入 `drawio-diagrams`：做一个可编辑 draw.io 架构图，后面我要手工改节点。
  - 真实模糊边界：给这个流程画个图。
- 区分 `scientific-schematics` 与 `generate-image`：
  - 应进入 `scientific-schematics`：按论文方法画一张源事实一致的机制示意图，用于投稿前讨论。
  - 应进入 `generate-image`：生成一张产品 hero 背景图，偏写实插画风格。
  - 真实模糊边界：帮我生成一张方法图。
### 前端规划、实现与验收链路
- 区分 `product-ux-planning` 与 `implementation-react-tailwind`：
  - 应进入 `product-ux-planning`：先把这个实验平台的信息架构、导航、状态和核心流程规划清楚。
  - 应进入 `implementation-react-tailwind`：直接实现一个 React/Tailwind 表格和筛选面板，接到现有数据。
  - 真实模糊边界：帮我做一个实验结果 dashboard。
- 区分 `responsive-accessibility-review` 与 `webapp-testing`：
  - 应进入 `responsive-accessibility-review`：检查这个页面移动端、键盘访问、对比度和文字溢出问题。
  - 应进入 `webapp-testing`：用 Playwright 跑一下本地 app，截图并抓 console error。
  - 真实模糊边界：验收一下这个前端页面。
### 生物信息聚合能力与具体工具边界
- 区分 `bioinformatics-database-retrieval` 与 `scanpy`：
  - 应进入 `bioinformatics-database-retrieval`：查这些基因、通路和疾病关联，整理数据库证据。
  - 应进入 `scanpy`：对这个 h5ad 做单细胞 QC、聚类和 marker gene 分析。
  - 真实模糊边界：分析这些单细胞基因表达结果。
- 区分 `pysam` 与 `tiledbvcf`：
  - 应进入 `pysam`：读取 BAM/CRAM 的指定区域并计算覆盖度。
  - 应进入 `tiledbvcf`：把大规模 VCF 样本集合导入 TileDB 并做并行查询。
  - 真实模糊边界：处理这些变异和比对文件。
### 医学影像聚合覆盖与术语测量边界
- 区分 `cardiac-mri` 与 `medical-imaging-terminology-measurement`：
  - 应进入 `cardiac-mri`：解释 CMR cine SAX 的 ED/ES 选择和 LV/RV 功能指标。
  - 应进入 `medical-imaging-terminology-measurement`：核对这份影像报告里的术语、测量单位和不确定性表述是否规范。
  - 真实模糊边界：检查这份 CMR 结果写法是否准确。
- 区分 `pydicom` 与 `medical-imaging-classical-features`：
  - 应进入 `pydicom`：读取 DICOM 并保留 spacing、orientation 和 tag provenance。
  - 应进入 `medical-imaging-classical-features`：设计可复现的物理空间预处理、配准 baseline 和 radiomics 协议。
  - 真实模糊边界：帮我核查医学影像预处理流程。
### 临床医学证据与安全边界
- 区分 `clinical-guideline-checking` 与 `medical-literature-evidence-review`：
  - 应进入 `clinical-guideline-checking`：核对这条指南推荐在当前年份、地区和人群里是否仍成立。
  - 应进入 `medical-literature-evidence-review`：按证据等级综述这种治疗在目标人群中的研究结果。
  - 真实模糊边界：帮我查这个临床建议有没有依据。
- 区分 `clinical-reports` 与 `treatment-plans`：
  - 应进入 `clinical-reports`：把这些去标识化信息整理成病例报告摘要。
  - 应进入 `treatment-plans`：起草一份需要临床医生复核的治疗计划文档，列目标、干预和监测。
  - 真实模糊边界：帮我写一份病人的临床文档。
### 数据科学工具相邻边界
- 区分 `polars` 与 `dask`：
  - 应进入 `polars`：这个 30GB parquet 能进内存，帮我把 pandas ETL 改成更快的 Polars lazy pipeline。
  - 应进入 `dask`：这个数据超出单机内存，需要把 pandas/NumPy 工作流扩到集群并行。
  - 真实模糊边界：这个表格分析太慢，帮我优化。
- 区分 `geopandas` 与 `networkx`：
  - 应进入 `geopandas`：读取 shapefile/GeoJSON，做空间 join 并画交互地图。
  - 应进入 `networkx`：分析这个节点-边关系网络的中心性和社区结构。
  - 真实模糊边界：分析这些位置和连接关系。
- 区分 `shap` 与 `scikit-learn`：
  - 应进入 `shap`：解释这个训练好模型的特征贡献，生成 SHAP summary plot。
  - 应进入 `scikit-learn`：建立 sklearn pipeline，做交叉验证、预处理和模型选择。
  - 真实模糊边界：帮我分析这个模型为什么表现这样。
### AI/ML 框架曝光不均
- 区分 `timesfm-forecasting` 与 `aeon`：
  - 应进入 `timesfm-forecasting`：不用训练自定义模型，直接预测这条单变量传感器时间序列。
  - 应进入 `aeon`：做时间序列分类、聚类或异常检测实验。
  - 真实模糊边界：分析这些时间序列并预测后续趋势。
- 区分 `pytorch-lightning` 与 `transformers`：
  - 应进入 `pytorch-lightning`：整理训练循环、checkpoint、logger 和多 GPU 配置。
  - 应进入 `transformers`：用预训练 transformer 做文本、图像或多模态推理/微调。
  - 真实模糊边界：帮我训练这个深度学习模型。
### 演示、海报与论文转传播材料边界
- 区分 `research-presentations` 与 `business-presentations`：
  - 应进入 `research-presentations`：把这篇论文和实验结果整理成组会汇报。
  - 应进入 `business-presentations`：做一份给管理层看的产品决策 deck，突出资源和取舍。
  - 真实模糊边界：帮我做一份汇报 PPT。
- 区分 `latex-posters` 与 `pptx-posters`：
  - 应进入 `latex-posters`：做一张会议用 LaTeX beamerposter。
  - 应进入 `pptx-posters`：做一张可导出 PowerPoint/PPTX 的研究海报。
  - 真实模糊边界：帮我做一张科研 poster。
### OpenAI 文档与系统构建辅助技能
- 区分 `mcp-builder` 与 `plugin-creator`：
  - 应进入 `mcp-builder`：为这个外部 API 设计一个 FastMCP server，包括工具 schema 和鉴权边界。
  - 应进入 `plugin-creator`：创建一个 Codex plugin 目录和 plugin.json，打包技能、MCP 或 app 能力。
  - 真实模糊边界：给这个服务做一个 Codex 可用的集成。
- 区分 `skill-creator` 与 `openai-docs`：
  - 应进入 `skill-creator`：把这个重复工作流沉淀成一个新的 Codex skill。
  - 应进入 `openai-docs`：查官方 OpenAI API 文档，确认当前模型和参数怎么用。
  - 真实模糊边界：帮我写一个 OpenAI 相关的 Codex 能力。

## 插件层级审计
- **`workflow-core`**：名称和描述与单一工作流技能一致，主要覆盖复杂执行、核查和完成门槛。
- **`ai-skills-core`**：插件市场只暴露 project-skill-installer 和 ai-skills-repository-maintainer；skill-library-analysis 通过 maintainer profile 可达。
- **`writing-style`**：覆盖 writing-fidelity、scientific-prose、chinese-prose；与 research-writing 在论文/报告润色上相邻。
- **`research-writing`**：覆盖报告、论文流程、文献和引用；内部需要区分正文写作、流程编排、审稿和引用核验。
- **`bioinformatics`**：覆盖 10 个核心生信源技能；若干专门平台、数据库和工具 active 技能不在 插件市场 聚合中。
- **`medical-imaging`**：覆盖 CMR、DICOM、经典特征、深度学习和病理；terminology-measurement 未进入 插件市场 聚合。
- **`marketplace-global`**：前端、数据科学/统计、可视化、文档/OCR、演示、临床医学、HPC、科研构思主要通过 profile/domain/单技能安装可达，而不是 插件市场 顶级插件。

## 第二阶段需要判断的问题
- 插件市场 顶级入口是否需要覆盖 profile/domain 中高价值但当前不可见的能力。
- 研究写作聚合内部是否需要更清晰地区分正文写作、流程编排、审稿诊断和投稿格式。
- OCR、PDF、DOCX 与通用转换请求是否需要按“是否扫描/是否学术交付/是否只转换格式”建立边界。
- 可视化请求是否需要先判断媒介：Mermaid、draw.io、UML、科学插图、位图或信息图。
- 数据科学和 AI/ML 工具是否需要自然任务优先的选择测试，而不是按库名触发。
- 临床医学技能的安全边界是否需要在安装入口和调用入口两层都可见。

## 审计边界确认
- 覆盖：`149/149` active 源技能。
- 冲突组：`12`，均已补成对边界样例。
- 本次没有给出删除、合并、改 description、新增 umbrella、新增 plugin 或调整 profile 的方案。
- 本次没有修改任何现有 `SKILL.md`、profile、plugin、marketplace 配置或生成层。
