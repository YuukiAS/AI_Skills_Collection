# AI Skills Collection 当前工作版图

这轮以最新取得的 `origin/main`（[`ff5be718a533bf603dc375b52d7dd9f7b6136119`](https://github.com/YuukiAS/AI_Skills_Collection/commit/ff5be718a533bf603dc375b52d7dd9f7b6136119)）为基线。主线有 **10 个正式中央插件、3 个已确定产品方向的计划插件、156 个注册为 active 的 Skill**。5 个有长期维护入口的独立 Skill 方向里，3 个已有可安装实现，另外 2 个有研究或领域流程候选。156 是注册目录里的源条目数，其中包括中央插件打包消费的 Skill。各口径不能相加。

六个方向由六个独立子代理分别研究 **Reasoned Decision、Clear Writing、Design Assurance、Delivery Assurance、Presentations、Research Authoring**。其他维护事项按既有 owner 回到普通修复、证据积累或交付回归。研究线的含义及先后见 [NEXT_ROUNDS.md](NEXT_ROUNDS.md)。

## 正式中央插件

当前仓库发布版本为 `5.5.2`。正式版本和 10 个插件的 manifest 与 [稳定发布分支](https://github.com/YuukiAS/AI_Skills_Collection/tree/f4517798a73adf29d3484306d60845488739f1fc) 一致。插件名称与版本以 [Marketplace](../../../.agents/plugins/marketplace.json) 对应安装包的 manifest 和 [发布记录](../../../CHANGELOG.md) 交叉核对。下表的“下一步”是研究判断。

| 插件 | 主线版本 | 现有职责 | 建议下一步与原始入口 |
| --- | --- | --- | --- |
| workflow-core | 0.5 | 一般执行、正常入口、权限、安全恢复、验收与交接 | 用正常入口回放路由误判、权限与最小恢复。#107 保留消费接口，产品交付判断由 Delivery Assurance 研究。[TODO](../../plugin-todos/workflow-core.md) · [正常入口任务](../../../results/workflow-core--reviewed-first-bootstrap-normal-entry/RESULT.md) |
| AI Skills Maintainer（ai-skills-core） | 0.5 | 中央插件维护与当前机器更新，消费正式发布和独立验收证据 | 聚焦已安装版本和实际调用证明。已有 machine update、规则失效先查真实消费等机制，日后用具体失败决定修哪里。[TODO](../../plugin-todos/ai-skills-core.md) |
| Clear Writing（writing-style） | 0.5 | 普通回复、中文与科学长文、改写保真、UI 短文案 | 用近期短答和跨来源长文检验现有单入口方案。0.6 单入口已有候选，#13 接下来需证明正式账号和 Web 路径。[TODO](../../plugin-todos/writing-style.md) · [研究](WORKSTREAMS/CLEAR_WRITING.md) |
| Research Authoring（research-writing） | 0.2 | 科研报告、论文、文献和科研文档 | 继续核实 #99 既有实现分支及正式发布门槛。课程文档作为有正反样本的领域路线，科研学习笔记独立取证。[TODO](../../plugin-todos/research-writing.md) · [研究](WORKSTREAMS/RESEARCH_AUTHORING.md) |
| presentations | 0.4 | 科研、教学及商务演示的策划、制作与返修 | 沿已有双端设计评审。把教学模板、既有 deck 冻结返修、独立视觉验收分成可观察行为。[TODO](../../plugin-todos/presentations.md) · [研究](WORKSTREAMS/PRESENTATIONS.md) |
| scientific-visualization | 0.1 | 科研图、科学示意图、海报和视觉验收 | 先取真实专家图与交互科学图证据。图是否传达科学结果由本插件判断，布局和交互另有 owner。[TODO](../../plugin-todos/scientific-visualization.md) |
| Frontend Design（web-development） | 0.4 | 界面信息架构、视觉系统、真实渲染验收 | 用 #89 的内容准入和 #97 的原生交互证据做窄修复。第二个专业产品样本到位后，再评估专业迁移能力。[TODO](../../plugin-todos/web-development.md) |
| statistical-modeling | 0.1 | 建模、推断目标、诊断、数值实验 | 将 #75–78 收敛为一个可执行统计方案的实例研究，优先验证算法选择、误差分解、随机性归属和中途可观察性。[TODO](../../plugin-todos/statistical-modeling.md) |
| bioinformatics | 0.1 | 数据库、组学与基因组工作流 | 从真实参考数据库/数据格式问题取一个小能力，核对成熟实现、版本和复现，#84 保持取证。[TODO](../../plugin-todos/bioinformatics.md) |
| medical-imaging | 0.1 | 医学影像 I/O、配准、分割、测量和模型工作流 | #79 用真实困难病例检验发现、归因和成熟组件复用，#85 继续取证。病例和数据约定由项目管理。[TODO](../../plugin-todos/medical-imaging.md) |

## 计划中的独立插件

| 方向 | 当前可核实状态 | 下一道判断 |
| --- | --- | --- |
| Reasoned Decision | 有冻结的 v0.1 设计、专属 TODO 和近期失败样本。历史独立 Skill 目录是证据入口，Marketplace 没有独立安装包。 | 送独立 Critic 审现有设计及新回归，重点看如何查原生路径、判断风险、及时停止和交接。[TODO](../../plugin-todos/reasoned-decision.md) · [研究](WORKSTREAMS/REASONED_DECISION.md) |
| Design Assurance | 独立插件方向已确定。Asteria 的执行包问题落在 workflow-core TODO。科研、课件和文档各有设计准备证据。 | 形成正式 Proposal，证明设计能被另一执行者落实，项目和领域团队继续决定专业内容。[Asteria 原始记录](../../plugin-todos/workflow-core.md#design-assurance-在要求用户运行执行包前必须给出可审阅的关键变化与落实点) · [研究](WORKSTREAMS/DESIGN_ASSURANCE.md) |
| Delivery Assurance | 独立插件方向已确定。主线已有 056 工作流底座与个别交付能力，#107 和外部研究存在版本差，中央 Marketplace 暂无独立包。 | 先核对当前外部设计与实际消费者，再审领域证据如何成为用户交付准入条件。[#107](https://github.com/YuukiAS/AI_Skills_Collection/issues/107) · [研究](WORKSTREAMS/DELIVERY_ASSURANCE.md) |

## 独立 Skill 的维护入口

| 方向 | 当前状态与源位置 | 处置 |
| --- | --- | --- |
| Project Instructions Editor | 已发布 0.2，已关闭 #93/#102。#108 的 0.3 研究涉及仓库 AGENTS 权威、预览和边界。[源码](../../../skills/core/codex-system/project-instructions-editor/SKILL.md) · [TODO](../../skill-todos/project-instructions-editor.md) | 保持独立安装。补真仓库配置定位和投影证据再审，避免引入跨项目同步服务。 |
| Slurm Workflows | 已发布 0.5。#95/#96/#109 各有不同验收边界。历史 live retain 仍为 `NOT_RUN`，正式发布记录有明确豁免。[源码](../../../skills/tools/hpc/slurm-workflows/SKILL.md) · [TODO](../../skill-todos/slurm-workflows.md) | 现有回归留作安全基线。今后按复现修正常入口或真实运行时。 |
| render-chinese-math-pdf | Pandoc/XeLaTeX、数学保真与首次 PDF 交付已有相关发布。视觉字体一致性只部分处理，跨插件自动交接仍需验证。[源码](../../../skills/tools/documents-media/render-chinese-math-pdf/SKILL.md) · [TODO](../../skill-todos/render-chinese-math-pdf.md) | 保持独立渲染能力，先复验 #83 和上游真实调用。 |
| course-assessment-authoring | 有主 TODO、学生受众补充和工作流推进说明。相关 runbook 位于 Research Authoring 安装包，未见独立 `SKILL.md` 或独立发布。[TODO](../../skill-todos/course-assessment-authoring.md) · [领域流程](../../../plugins/codex/plugins/research-writing/shared/student-assessment-end-to-end-pre-execution-runbook.md) | 先验证领域消费者，保留课程独立入口候选。 |
| artifact-content-design | 有 CAT-TRACE、Atlas 与专家图案例及 Artifact Director 概念，未见独立 `SKILL.md` 或独立发布。[TODO](../../skill-todos/artifact-content-design.md) | 暂以共享研究候选保留。先核实内容准入能否由现有领域插件和 Design Assurance 共同消费。 |
| Reasoned Decision 历史 seed | 旧 standalone TODO 文件标为 superseded，仍存放原始人工样本。[历史证据](../../skill-todos/reasoned-decision.md) | 计入计划插件一次。 |

## 尚待验证的候选能力

- **跨载体内容准入**。先确定读者需要哪些内容、正文位置与操作信息，再交文案和渲染。Atlas 的内容准入、课程材料的读者信息预算与专家图选择可互为反例，但每类载体仍保留自己的证据标准。归入 Design Assurance 和领域插件的接口研究。
- **科研学习笔记**。能重建推导、说明变量与假设、帮助读者真正学会方法。和面向导师的结果汇报属于不同读者任务。先做 Research Authoring 内的单家族取证。
- **科研图结果先行与交互图边的科学语义**。前者已有明确候选，后者先核对第二个真实科学图案例。组件、原生交互与动效由 Frontend Design 承担。
- **领域 QA 到交付准入**。复用领域自己的内容、图像、交互或模型验证，交付侧只要求可定位的判定、同一候选身份和可用交付物。
- **真实 AGENTS 权威定位与可审阅差异**。沿 Project Instructions Editor #108，小范围验证包含继承、冲突和私有用户配置的真实仓库。
- **领域课程驱动能力补足**。统计、影像、生信和科学可视化各自选一个有真实输入的窄问题。通用调研方法共享，产出和验收留在原插件。

## 盘点范围

- 枚举主线的 18 份插件 TODO/补充设计、8 份 Skill TODO/补充材料，另读 1 份目录说明。扫描 `docs/design/` 的 354 个 tracked 路径、`results/` 的 79 个顶层条目及 55 份主线 Reviewed Handoff `CURRENT.json`。历史材料按归属和近期真实问题选读。已发布、候选和项目使用证据分别计。
- 通过 GitHub 读取 99 个当前可见 Issue，并用私有维护看板只读校对关键条目。公开报告保留公开 Issue、提交和现有文档定位。GitHub Issue 的 open/closed、Project 生命周期及 Markdown maturity 各有独立含义。
- 对近期有正式推进迹象的独立分支单独核对远端 commit，不把它们混入主线发布计数。来源冲突及后续候选动作见 [CANDIDATE_CANONICAL_EDITS.md](CANDIDATE_CANONICAL_EDITS.md)。

## Skill 源目录索引

以 [registry.json](../../../registry.json) 的注册条目链接到每个 `SKILL.md`，按源目录分组。目录有 195 个 tracked Skill 文件，其中 156 个进入注册目录。剩余 39 个是 17 个归档目录条目和 22 个在原分类下标记 archived 的条目。这个索引按源文件去重，安装包中的重命名、组合与复用另以 Marketplace 生成层为准。

<details>
<summary>156 个 active 源 Skill</summary>

- **core/codex-system（13）** [ai-skills-repository-maintainer](../../../skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md)、[bridge-kit-maintainer](../../../skills/core/codex-system/bridge-kit-maintainer/SKILL.md)、[codex-workflow-protocol](../../../skills/core/codex-system/codex-workflow-protocol/SKILL.md)、[machine-update-orchestrator](../../../skills/core/codex-system/machine-update-orchestrator/SKILL.md)、[mcp-builder](../../../skills/core/codex-system/mcp-builder/SKILL.md)、[project-instructions-editor](../../../skills/core/codex-system/project-instructions-editor/SKILL.md)、[project-skill-installer](../../../skills/core/codex-system/project-skill-installer/SKILL.md)、[skill-library-analysis](../../../skills/core/codex-system/skill-library-analysis/SKILL.md)、[imagegen](../../../skills/core/codex-system/system-skills/imagegen/SKILL.md)、[openai-docs](../../../skills/core/codex-system/system-skills/openai-docs/SKILL.md)、[plugin-creator](../../../skills/core/codex-system/system-skills/plugin-creator/SKILL.md)、[skill-creator](../../../skills/core/codex-system/system-skills/skill-creator/SKILL.md)、[skill-installer](../../../skills/core/codex-system/system-skills/skill-installer/SKILL.md)
- **domains/bayesian（5）** [bayesian-ppl-diagnostics](../../../skills/domains/bayesian/bayesian-ppl-diagnostics/SKILL.md)、[pymc](../../../skills/domains/bayesian/pymc/SKILL.md)、[simpy](../../../skills/domains/bayesian/simpy/SKILL.md)、[statistical-analysis](../../../skills/domains/bayesian/statistical-analysis/SKILL.md)、[statsmodels](../../../skills/domains/bayesian/statsmodels/SKILL.md)
- **domains/bioinformatics（24）** [biopython](../../../skills/domains/bioinformatics/biology-toolkits/biopython/SKILL.md)、[esm](../../../skills/domains/bioinformatics/biology-toolkits/esm/SKILL.md)、[etetoolkit](../../../skills/domains/bioinformatics/biology-toolkits/etetoolkit/SKILL.md)、[phylogenetics](../../../skills/domains/bioinformatics/biology-toolkits/phylogenetics/SKILL.md)、[scikit-bio](../../../skills/domains/bioinformatics/biology-toolkits/scikit-bio/SKILL.md)、[bioinformatics-database-retrieval](../../../skills/domains/bioinformatics/databases/bioinformatics-database-retrieval/SKILL.md)、[pysam](../../../skills/domains/bioinformatics/genomics-io/pysam/SKILL.md)、[tiledbvcf](../../../skills/domains/bioinformatics/genomics-io/tiledbvcf/SKILL.md)、[zarr-python](../../../skills/domains/bioinformatics/genomics-io/zarr-python/SKILL.md)、[arboreto](../../../skills/domains/bioinformatics/omics-analysis/arboreto/SKILL.md)、[deeptools](../../../skills/domains/bioinformatics/omics-analysis/deeptools/SKILL.md)、[flowio](../../../skills/domains/bioinformatics/omics-analysis/flowio/SKILL.md)、[geniml](../../../skills/domains/bioinformatics/omics-analysis/geniml/SKILL.md)、[gtars](../../../skills/domains/bioinformatics/omics-analysis/gtars/SKILL.md)、[polars-bio](../../../skills/domains/bioinformatics/omics-analysis/polars-bio/SKILL.md)、[pydeseq2](../../../skills/domains/bioinformatics/omics-analysis/pydeseq2/SKILL.md)、[dnanexus-integration](../../../skills/domains/bioinformatics/platforms/dnanexus-integration/SKILL.md)、[lamindb](../../../skills/domains/bioinformatics/platforms/lamindb/SKILL.md)、[latchbio-integration](../../../skills/domains/bioinformatics/platforms/latchbio-integration/SKILL.md)、[anndata](../../../skills/domains/bioinformatics/single-cell/anndata/SKILL.md)、[scanpy](../../../skills/domains/bioinformatics/single-cell/scanpy/SKILL.md)、[scvelo](../../../skills/domains/bioinformatics/single-cell/scvelo/SKILL.md)、[scvi-tools](../../../skills/domains/bioinformatics/single-cell/scvi-tools/SKILL.md)、[neuropixels-analysis](../../../skills/domains/bioinformatics/specialized/neuropixels-analysis/SKILL.md)
- **domains/medical-imaging（6）** [cardiac-mri](../../../skills/domains/medical-imaging/cardiac-mri/SKILL.md)、[medical-imaging-classical-features](../../../skills/domains/medical-imaging/medical-imaging-classical-features/SKILL.md)、[medical-imaging-deep-learning](../../../skills/domains/medical-imaging/medical-imaging-deep-learning/SKILL.md)、[medical-imaging-terminology-measurement](../../../skills/domains/medical-imaging/medical-imaging-terminology-measurement/SKILL.md)、[pathml](../../../skills/domains/medical-imaging/pathml/SKILL.md)、[pydicom](../../../skills/domains/medical-imaging/pydicom/SKILL.md)
- **domains/medicine-clinical（9）** [clinical-decision-support](../../../skills/domains/medicine-clinical/clinical-decision-support/SKILL.md)、[clinical-guideline-checking](../../../skills/domains/medicine-clinical/clinical-guideline-checking/SKILL.md)、[clinical-reports](../../../skills/domains/medicine-clinical/clinical-reports/SKILL.md)、[medical-literature-evidence-review](../../../skills/domains/medicine-clinical/medical-literature-evidence-review/SKILL.md)、[medical-safety-boundaries](../../../skills/domains/medicine-clinical/medical-safety-boundaries/SKILL.md)、[neurokit2](../../../skills/domains/medicine-clinical/neurokit2/SKILL.md)、[pyhealth](../../../skills/domains/medicine-clinical/pyhealth/SKILL.md)、[scikit-survival](../../../skills/domains/medicine-clinical/scikit-survival/SKILL.md)、[treatment-plans](../../../skills/domains/medicine-clinical/treatment-plans/SKILL.md)
- **science/communication（8）** [latex-posters](../../../skills/science/communication/latex-posters/SKILL.md)、[paper-2-web](../../../skills/science/communication/paper-2-web/SKILL.md)、[pptx-posters](../../../skills/science/communication/pptx-posters/SKILL.md)、[project-thread-handoff](../../../skills/science/communication/project-thread-handoff/SKILL.md)、[publication-figure-palettes](../../../skills/science/communication/publication-figure-palettes/SKILL.md)、[scientific-figure-qa](../../../skills/science/communication/scientific-figure-qa/SKILL.md)、[scientific-schematics](../../../skills/science/communication/scientific-schematics/SKILL.md)、[scientific-visualization](../../../skills/science/communication/scientific-visualization/SKILL.md)
- **science/discovery（9）** [arxiv-database](../../../skills/science/discovery/arxiv-database/SKILL.md)、[bgpt-paper-search](../../../skills/science/discovery/bgpt-paper-search/SKILL.md)、[biorxiv-database](../../../skills/science/discovery/biorxiv-database/SKILL.md)、[citation-management](../../../skills/science/discovery/citation-management/SKILL.md)、[openalex-database](../../../skills/science/discovery/openalex-database/SKILL.md)、[pubmed-database](../../../skills/science/discovery/pubmed-database/SKILL.md)、[pyzotero](../../../skills/science/discovery/pyzotero/SKILL.md)、[research-lookup](../../../skills/science/discovery/research-lookup/SKILL.md)、[valyu-scientific-search](../../../skills/science/discovery/valyu-scientific-search/SKILL.md)
- **science/ideation（7）** [consciousness-council](../../../skills/science/ideation/consciousness-council/SKILL.md)、[experiment-execution](../../../skills/science/ideation/experiment-execution/SKILL.md)、[hypogenic](../../../skills/science/ideation/hypogenic/SKILL.md)、[hypothesis-generation](../../../skills/science/ideation/hypothesis-generation/SKILL.md)、[scientific-brainstorming](../../../skills/science/ideation/scientific-brainstorming/SKILL.md)、[scientific-critical-thinking](../../../skills/science/ideation/scientific-critical-thinking/SKILL.md)、[what-if-oracle](../../../skills/science/ideation/what-if-oracle/SKILL.md)
- **tools/ai-ml（7）** [modal](../../../skills/tools/ai-ml/modal/SKILL.md)、[pufferlib](../../../skills/tools/ai-ml/pufferlib/SKILL.md)、[pytorch-lightning](../../../skills/tools/ai-ml/pytorch-lightning/SKILL.md)、[stable-baselines3](../../../skills/tools/ai-ml/stable-baselines3/SKILL.md)、[timesfm-forecasting](../../../skills/tools/ai-ml/timesfm-forecasting/SKILL.md)、[torch-geometric](../../../skills/tools/ai-ml/torch-geometric/SKILL.md)、[transformers](../../../skills/tools/ai-ml/transformers/SKILL.md)
- **tools/data-science（13）** [aeon](../../../skills/tools/data-science/aeon/SKILL.md)、[dask](../../../skills/tools/data-science/dask/SKILL.md)、[exploratory-data-analysis](../../../skills/tools/data-science/exploratory-data-analysis/SKILL.md)、[geopandas](../../../skills/tools/data-science/geopandas/SKILL.md)、[matlab](../../../skills/tools/data-science/matlab/SKILL.md)、[networkx](../../../skills/tools/data-science/networkx/SKILL.md)、[polars](../../../skills/tools/data-science/polars/SKILL.md)、[pymoo](../../../skills/tools/data-science/pymoo/SKILL.md)、[scikit-learn](../../../skills/tools/data-science/scikit-learn/SKILL.md)、[shap](../../../skills/tools/data-science/shap/SKILL.md)、[sympy](../../../skills/tools/data-science/sympy/SKILL.md)、[umap-learn](../../../skills/tools/data-science/umap-learn/SKILL.md)、[vaex](../../../skills/tools/data-science/vaex/SKILL.md)
- **tools/documents-media（11）** [docx](../../../skills/tools/documents-media/docx/SKILL.md)、[get-available-resources](../../../skills/tools/documents-media/get-available-resources/SKILL.md)、[markitdown](../../../skills/tools/documents-media/markitdown/SKILL.md)、[open-notebook](../../../skills/tools/documents-media/open-notebook/SKILL.md)、[parallel-web](../../../skills/tools/documents-media/parallel-web/SKILL.md)、[pdf](../../../skills/tools/documents-media/pdf/SKILL.md)、[perplexity-search](../../../skills/tools/documents-media/perplexity-search/SKILL.md)、[business-presentations](../../../skills/tools/documents-media/presentations/business-presentations/SKILL.md)、[research-presentations](../../../skills/tools/documents-media/presentations/research-presentations/SKILL.md)、[render-chinese-math-pdf](../../../skills/tools/documents-media/render-chinese-math-pdf/SKILL.md)、[xlsx](../../../skills/tools/documents-media/xlsx/SKILL.md)
- **tools/frontend（12）** [brand-creative-assets](../../../skills/tools/frontend/brand-creative-assets/SKILL.md)、[design-system-tokens](../../../skills/tools/frontend/design-system-tokens/SKILL.md)、[figma-design-to-code](../../../skills/tools/frontend/figma-design-to-code/SKILL.md)、[frontend-reference-research](../../../skills/tools/frontend/frontend-reference-research/SKILL.md)、[frontend-visual-systems](../../../skills/tools/frontend/frontend-visual-systems/SKILL.md)、[implementation-react-tailwind](../../../skills/tools/frontend/implementation-react-tailwind/SKILL.md)、[motion-interaction](../../../skills/tools/frontend/motion-interaction/SKILL.md)、[product-ux-planning](../../../skills/tools/frontend/product-ux-planning/SKILL.md)、[research-product-frontend](../../../skills/tools/frontend/research-product-frontend/SKILL.md)、[responsive-accessibility-review](../../../skills/tools/frontend/responsive-accessibility-review/SKILL.md)、[visual-direction](../../../skills/tools/frontend/visual-direction/SKILL.md)、[webapp-testing](../../../skills/tools/frontend/webapp-testing/SKILL.md)
- **tools/hpc（1）** [slurm-workflows](../../../skills/tools/hpc/slurm-workflows/SKILL.md)
- **tools/visualization（12）** [canvas-design](../../../skills/tools/visualization/canvas-design/SKILL.md)、[d2-diagrams](../../../skills/tools/visualization/d2-diagrams/SKILL.md)、[drawio-diagrams](../../../skills/tools/visualization/drawio-diagrams/SKILL.md)、[excalidraw-diagrams](../../../skills/tools/visualization/excalidraw-diagrams/SKILL.md)、[generate-image](../../../skills/tools/visualization/generate-image/SKILL.md)、[infographics](../../../skills/tools/visualization/infographics/SKILL.md)、[markdown-mermaid-writing](../../../skills/tools/visualization/markdown-mermaid-writing/SKILL.md)、[matplotlib](../../../skills/tools/visualization/matplotlib/SKILL.md)、[plantuml-diagrams](../../../skills/tools/visualization/plantuml-diagrams/SKILL.md)、[plotly](../../../skills/tools/visualization/plotly/SKILL.md)、[seaborn](../../../skills/tools/visualization/seaborn/SKILL.md)、[theme-factory](../../../skills/tools/visualization/theme-factory/SKILL.md)
- **writing/core（6）** [chinese-prose](../../../skills/writing/core/chinese-prose/SKILL.md)、[product-ui-copy](../../../skills/writing/core/product-ui-copy/SKILL.md)、[response-clarity](../../../skills/writing/core/response-clarity/SKILL.md)、[scientific-prose](../../../skills/writing/core/scientific-prose/SKILL.md)、[scientific-rewrite](../../../skills/writing/core/scientific-rewrite/SKILL.md)、[writing-fidelity](../../../skills/writing/core/writing-fidelity/SKILL.md)
- **writing/research（13）** [academic-paper-writer-pro](../../../skills/writing/research/academic-paper-writer-pro/SKILL.md)、[citation-verification](../../../skills/writing/research/citation-verification/SKILL.md)、[latex-paper-authoring](../../../skills/writing/research/latex-paper-authoring/SKILL.md)、[literature-review](../../../skills/writing/research/literature-review/SKILL.md)、[nature-manuscript-workflow](../../../skills/writing/research/nature-manuscript-workflow/SKILL.md)、[ocr-kb](../../../skills/writing/research/ocr-kb/SKILL.md)、[paper-workflow-orchestrator](../../../skills/writing/research/paper-workflow-orchestrator/SKILL.md)、[peer-review](../../../skills/writing/research/peer-review/SKILL.md)、[research-grants](../../../skills/writing/research/research-grants/SKILL.md)、[research-reporting](../../../skills/writing/research/research-reporting/SKILL.md)、[scholar-evaluation](../../../skills/writing/research/scholar-evaluation/SKILL.md)、[scientific-writing](../../../skills/writing/research/scientific-writing/SKILL.md)、[venue-templates](../../../skills/writing/research/venue-templates/SKILL.md)

</details>

<details>
<summary>39 个未进入当前注册目录的源 Skill</summary>

- [archive/documents-media/pptx](../../../skills/archive/documents-media/pptx/SKILL.md)
- [archive/experimental/dhdna-profiler](../../../skills/archive/experimental/dhdna-profiler/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/create-database-row](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/create-database-row/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/create-page](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/create-page/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/create-task](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/create-task/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/database-query](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/database-query/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/find](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/find/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/knowledge-capture](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/knowledge-capture/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/meeting-intelligence](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/meeting-intelligence/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/research-documentation](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/research-documentation/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/search](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/search/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/spec-to-implementation](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/spec-to-implementation/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/tasks-build](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/tasks-build/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/tasks-explain-diff](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/tasks-explain-diff/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/tasks-plan](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/tasks-plan/SKILL.md)
- [archive/integrations/notion/notion-workspace-skills-codex/tasks-setup](../../../skills/archive/integrations/notion/notion-workspace-skills-codex/tasks-setup/SKILL.md)
- [archive/science-communication/scientific-slides](../../../skills/archive/science-communication/scientific-slides/SKILL.md)
- [domains/bioinformatics/alphafold-database](../../../skills/domains/bioinformatics/alphafold-database/SKILL.md)
- [domains/bioinformatics/bioservices](../../../skills/domains/bioinformatics/bioservices/SKILL.md)
- [domains/bioinformatics/cellxgene-census](../../../skills/domains/bioinformatics/cellxgene-census/SKILL.md)
- [domains/bioinformatics/depmap](../../../skills/domains/bioinformatics/depmap/SKILL.md)
- [domains/bioinformatics/ena-database](../../../skills/domains/bioinformatics/ena-database/SKILL.md)
- [domains/bioinformatics/ensembl-database](../../../skills/domains/bioinformatics/ensembl-database/SKILL.md)
- [domains/bioinformatics/gene-database](../../../skills/domains/bioinformatics/gene-database/SKILL.md)
- [domains/bioinformatics/geo-database](../../../skills/domains/bioinformatics/geo-database/SKILL.md)
- [domains/bioinformatics/gget](../../../skills/domains/bioinformatics/gget/SKILL.md)
- [domains/bioinformatics/gnomad-database](../../../skills/domains/bioinformatics/gnomad-database/SKILL.md)
- [domains/bioinformatics/gtex-database](../../../skills/domains/bioinformatics/gtex-database/SKILL.md)
- [domains/bioinformatics/gwas-database](../../../skills/domains/bioinformatics/gwas-database/SKILL.md)
- [domains/bioinformatics/interpro-database](../../../skills/domains/bioinformatics/interpro-database/SKILL.md)
- [domains/bioinformatics/jaspar-database](../../../skills/domains/bioinformatics/jaspar-database/SKILL.md)
- [domains/bioinformatics/kegg-database](../../../skills/domains/bioinformatics/kegg-database/SKILL.md)
- [domains/bioinformatics/monarch-database](../../../skills/domains/bioinformatics/monarch-database/SKILL.md)
- [domains/bioinformatics/opentargets-database](../../../skills/domains/bioinformatics/opentargets-database/SKILL.md)
- [domains/bioinformatics/reactome-database](../../../skills/domains/bioinformatics/reactome-database/SKILL.md)
- [domains/bioinformatics/string-database](../../../skills/domains/bioinformatics/string-database/SKILL.md)
- [domains/bioinformatics/uniprot-database](../../../skills/domains/bioinformatics/uniprot-database/SKILL.md)
- [domains/medicine-clinical/clinicaltrials-database](../../../skills/domains/medicine-clinical/clinicaltrials-database/SKILL.md)
- [writing/research/content-generation](../../../skills/writing/research/content-generation/SKILL.md)

</details>
