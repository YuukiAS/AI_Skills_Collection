# AI Skills Collection

给 Codex 使用的科研与工程技能库。它把常用的写作、汇报、统计、医学影像、前端设计和仓库维护经验整理成可安装的插件，让日常任务更稳、更容易验收。

Repository / CLI release: `5.3.0`

## 可单独安装的技能

这些是 Standalone Skills：可以按单个 Skill 安装和使用，不是中央 Marketplace Plugins。

|  |  |
|---|---|
| <img src="./skills/science/communication/project-thread-handoff/assets/app-facing.svg" width="40" alt="Project Thread Handoff icon"> | <strong>Project Thread Handoff</strong><br><code>project-thread-handoff</code> · v`0.1`<br>用于长期项目聊天的上下文交接与新 thread 续接。 |
| <img src="./skills/tools/documents-media/render-chinese-math-pdf/assets/app-facing.svg" width="40" alt="Chinese Math PDF icon"> | <strong>Chinese Math PDF</strong><br><code>render-chinese-math-pdf</code> · v`0.2`<br>用于中文、中英混合和数学密集型科研 PDF 的可靠渲染与检查。 |
| <img src="./skills/tools/hpc/slurm-workflows/assets/slurm-workflows.svg" width="40" alt="Slurm Workflows icon"> | <strong>Slurm Workflows</strong><br><code>slurm-workflows</code> · v`0.2`<br>用于 Slurm/HPC 集群任务的可移植规划、路由、监控、诊断和可复用容量管理。 |

`Project Thread Handoff` 也可以通过一个 `skills-only` ChatGPT personal Plugin wrapper 使用；这个 wrapper 不含 MCP，也不是第二份能力 source。更新说明见：[docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md](docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md)。

## 中央插件

|  |  |
|---|---|
| <img src="./assets/codex/plugin-icons/workflow-core/composer.svg" width="40" alt="Verified Workflow icon"> | <strong>Verified Workflow</strong><br><code>workflow-core</code> · v`0.4`<br>复杂任务的执行、验证与可靠收尾。 |
| <img src="./assets/codex/plugin-icons/ai-skills-core/composer.svg" width="40" alt="AI Skills Maintainer icon"> | <strong>AI Skills Maintainer</strong><br><code>ai-skills-core</code> · v`0.5`<br>维护本仓库插件，也负责用短请求同步当前机器上的 AI_Skills 与 Bridge Kit 正式发布版本。 |
| <img src="./assets/codex/plugin-icons/writing-style/composer.svg" width="40" alt="Clear Writing icon"> | <strong>Clear Writing</strong><br><code>writing-style</code> · v`0.3`<br>在保留事实与原意的前提下，改善中英文科研和技术表达。 |
| <img src="./assets/codex/plugin-icons/research-writing/composer.svg" width="40" alt="Research Authoring icon"> | <strong>Research Authoring</strong><br><code>research-writing</code> · v`0.2`<br>支持研究报告、论文、文献、引用和证据组织；正式 PDF 会交给配套渲染器处理。 |
| <img src="./assets/codex/plugin-icons/presentations/composer.svg" width="40" alt="Presentations icon"> | <strong>Presentations</strong><br><code>presentations</code> · v`0.3`<br>规划和返修科研组会、研究汇报与商务演示文稿。 |
| <img src="./assets/codex/plugin-icons/scientific-visualization/composer.svg" width="40" alt="Scientific Visualization icon"> | <strong>Scientific Visualization</strong><br><code>scientific-visualization</code> · v`0.1`<br>处理科研图、配色、示意图、海报和视觉检查。 |
| <img src="./assets/codex/plugin-icons/web-development/composer.svg" width="40" alt="Frontend Design icon"> | <strong>Frontend Design</strong><br><code>web-development</code> · v`0.2`<br>整理前端参考、视觉系统和科研产品界面设计。 |
| <img src="./assets/codex/plugin-icons/statistical-modeling/composer.svg" width="40" alt="Statistical Modeling icon"> | <strong>Statistical Modeling</strong><br><code>statistical-modeling</code> · v`0.1`<br>支持统计建模、Bayesian 工作流、诊断和数据分析。 |
| <img src="./assets/codex/plugin-icons/bioinformatics/composer.svg" width="40" alt="Bioinformatics icon"> | <strong>Bioinformatics</strong><br><code>bioinformatics</code> · v`0.1`<br>覆盖数据库、单细胞、GWAS 和组学分析工作流。 |
| <img src="./assets/codex/plugin-icons/medical-imaging/composer.svg" width="40" alt="Medical Imaging icon"> | <strong>Medical Imaging</strong><br><code>medical-imaging</code> · v`0.1`<br>支持 DICOM/NIfTI、分割、配准和影像 AI 工作流。 |

## 开始使用

在 Codex App 或 Codex CLI 的 Git marketplace 中添加这个来源，然后安装需要的插件：

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Ref: release
Sparse paths:
.agents/plugins
plugins/codex/plugins
```

稳定使用默认跟随 `release`。需要参与开发或测试未发布内容时，才显式选择 `main`。安装或升级后开启新的 Codex 会话，让插件按最新版本加载。

安装 AI Skills Maintainer 后，日常同步可以直接说：`update presentations`、`update workflow-core`、`update AI Skills`、`update Bridge Kit` 或 `sync this machine`。它会先发现当前机器、Marketplace、插件和 Bridge 状态，再按正式发布说明决定是否只更新一个插件、同步必要配套组件，或交给 Bridge Kit 的 `ai-bridge` 命令处理运行时/Host 相关工作。

## 研究报告 PDF

如果要从研究报告生成正式 PDF，优先安装 [research-main](profiles/research-main.json) profile。它同时包含 Research Authoring 和 `render-chinese-math-pdf`，可以先整理研究内容，再用 Pandoc/XeLaTeX 渲染中文、英文和数学公式。

单独安装 Marketplace 里的 Research Authoring 插件时，它只负责研究文档的内容和结构，不会假装自带 PDF 渲染器。遇到正式 PDF 请求而缺少 `render-chinese-math-pdf` 时，应先安装这个配套技能，而不是静默改用浏览器导出。

## 更多入口

- [Profiles](profiles/README.md)：选择适合项目或机器环境的安装组合。
- [本地配置](docs/LOCAL_CONFIGURATION.md)：配置服务器、本地工具和机器差异。
- [TODO](TODO.md)：查看当前维护入口和真实项目反馈。
- [CHANGELOG](CHANGELOG.md)：查看 repository release 历史。
