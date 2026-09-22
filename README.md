# AI Skills Collection

给 Codex 使用的科研与工程技能库。它把常用的写作、汇报、统计、医学影像、前端设计和仓库维护经验整理成可安装的插件，让日常任务更稳、更容易验收。

Repository / CLI release: `5.0.7`

## 中央插件

|  |  |
|---|---|
| <img src="./assets/codex/plugin-icons/workflow-core/composer.svg" width="40" alt="Verified Workflow icon"> | <strong>Verified Workflow</strong><br><code>workflow-core</code> · v`0.3`<br>复杂任务的执行、验证与可靠收尾。 |
| <img src="./assets/codex/plugin-icons/ai-skills-core/composer.svg" width="40" alt="AI Skills Maintainer icon"> | <strong>AI Skills Maintainer</strong><br><code>ai-skills-core</code> · v`0.4`<br>维护本仓库的插件、版本、生成层与回归证据。 |
| <img src="./assets/codex/plugin-icons/writing-style/composer.svg" width="40" alt="Clear Writing icon"> | <strong>Clear Writing</strong><br><code>writing-style</code> · v`0.3`<br>在保留事实与原意的前提下，改善中英文科研和技术表达。 |
| <img src="./assets/codex/plugin-icons/research-writing/composer.svg" width="40" alt="Research Authoring icon"> | <strong>Research Authoring</strong><br><code>research-writing</code> · v`0.1`<br>支持研究报告、论文、文献、引用和证据组织。 |
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
Ref: main
Sparse paths:
.agents/plugins
plugins/codex/plugins
```

安装或升级后开启新的 Codex 会话，让插件按最新版本加载。

## 更多入口

- [Profiles](profiles/README.md)：选择适合项目或机器环境的安装组合。
- [本地配置](docs/LOCAL_CONFIGURATION.md)：配置服务器、本地工具和机器差异。
- [TODO](TODO.md)：查看当前维护入口和真实项目反馈。
- [CHANGELOG](CHANGELOG.md)：查看 repository release 历史。
