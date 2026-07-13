# AI Skills Collection

这是面向 Codex 的个人科研与工程技能库。它不是通用官方插件的替代品：官方插件负责文件、浏览器、GitHub、Notion、PDF、Slides、LaTeX、前端构建等执行后端；本仓库负责我的长期工作流、科研写作规则、领域判断、安装 profile、来源记录和验收标准。

## 先决定装什么

| 场景 | 安装本仓库插件 | 同时使用的官方能力 |
|---|---|---|
| 所有主力 Codex 环境 | `workflow-core`、`writing-style` | GitHub、文件工具 |
| 主力科研机器 | `research-writing`、`statistical-modeling` | Zotero、PDF、LaTeX、GitHub |
| 经常做 PPT 的桌面环境 | `presentations` | Presentation/Slides；需要 Beamer 时加 LaTeX |
| 前端网站或科研产品 | `web-development` | `build-web-apps`、Figma、GitHub |
| 医学影像项目 | `medical-imaging`，需要时加项目 repo-local skills | PDF、GitHub、前端构建 |
| 生物信息项目 | `bioinformatics` | GitHub、数据库/文献工具 |
| 维护本仓库 | `ai-skills-core` | GitHub、必要时 Notion |
| 纯 Slurm compute node 或训练容器 | 通常不装全局插件 | 只保留项目必要脚本 |

`ai-skills-core` 不是所有机器必装。只有在使用本仓库 CLI、安装 profile、更新 registry/catalog/marketplace、处理 provenance 或维护插件发布层时才需要。

## Codex App 插件市场

推送到 `main` 后，等待 GitHub Actions 的 `Codex Marketplace` 工作流完成。工作流会重新生成并验证：

- `.agents/plugins/marketplace.json`
- `plugins/codex/plugins/`

在 Codex App 中添加 Git 插件市场：

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Ref: main
Sparse paths:
.agents/plugins
plugins/codex/plugins
```

CLI 等价命令：

```bash
codex plugin marketplace add \
  https://github.com/YuukiAS/AI_Skills_Collection.git \
  --ref main \
  --sparse .agents/plugins \
  --sparse plugins/codex/plugins
```

生成层不要手工编辑。改 `skills/`、`profiles/`、`scripts/codex_marketplace_config.json` 或 `assets/codex/plugin-icons/` 后，重新生成发布层。

## 中央九个插件

| 插件 | 用户可见入口 |
|---|---|
| `workflow-core` | `codex-workflow-protocol` |
| `ai-skills-core` | `project-skill-installer`、`ai-skills-repository-maintainer` |
| `writing-style` | `writing-fidelity`、`scientific-prose`、`chinese-prose` |
| `research-writing` | `research-reporting`、`research-paper-workflow`、`literature-and-citations` |
| `presentations` | `research-presentations`、`business-presentations` |
| `web-development` | `frontend-reference-research`、`frontend-visual-systems`、`research-product-frontend` |
| `statistical-modeling` | `bayesian-modeling`、`data-analysis-python`、`scientific-visualization` |
| `bioinformatics` | `bioinformatics-workflows` |
| `medical-imaging` | `medical-imaging-workflows`、`ai-ml-imaging` |

`cardiacnexus` 不再是中央通用插件。CardiacNexus 的项目专用技能应合并进 CardiacNexus repo 的 `.agents/skills/`，当前短期导出包在 `exports/cardiacnexus-repo-local/`。

## 典型组合

| 任务 | 本仓库负责 | 官方能力负责 |
|---|---|---|
| repo report、milestone、实验复盘 | `workflow-core` + `research-writing` + `writing-style` + 领域/项目 skill | GitHub；需要 PDF 时用 PDF/LaTeX |
| Asteria/TRACE Markdown 到组会 PPT | repo-local skill + `research-presentations` + `statistical-modeling` | Presentation/Slides；Beamer 时用 LaTeX |
| 正式论文 | repo-local skill + `research-paper-workflow` + `literature-and-citations` + `writing-style` | LaTeX、PDF、Zotero、GitHub |
| 前端网站或科研产品 | repo-local skill + `web-development` | `build-web-apps`、Figma、GitHub |
| 商业或公司 deck | `business-presentations` | Presentation/Slides |
| CardiacNexus pipeline/docs | CardiacNexus repo-local skills + `medical-imaging` | GitHub、`build-web-apps` |
| 外部 Skill/Notion 规范整合 | `ai-skills-core` + `workflow-core` | Notion、GitHub |

## 本地 CLI

`ai-skills` CLI 适合服务器、HPC、repo-local 安装、用户级安装和维护任务。

默认安装位置：

- repo-local：`<project>/.agents/skills/`
- 用户级：`$HOME/.agents/skills/`
- 旧兼容目标：`${CODEX_HOME:-$HOME/.codex}/skills/`

新机器设置：

```bash
git clone <repo-url> AI_Skills_Collection
python3 -m pip install --no-build-isolation -e AI_Skills_Collection
```

如果没有安装短命令：

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py --help
```

这台 Windows 机器上 `python` 可能不在 `PATH`，可使用 Codex runtime Python：

```powershell
& "$HOME\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts\skills.py validate
```

## 推荐 profile

| profile | 适用场景 | 目标 |
|---|---|---|
| `codex-workflow-core` | 所有主力 Codex 环境 | user |
| `codex-writing-style` | 长期写作风格 | user |
| `codex-research-writing` | 科研写作主力机 | user 或 repo |
| `codex-webdev` | 前端或科研产品 repo | repo |
| `codex-bioinformatics-light` | 生信项目 | repo |
| `codex-bayesian-jsdm` | 贝叶斯/统计项目 | repo |
| `codex-cardiacnexus` | CardiacNexus 支撑技能 | repo，项目技能另从导出包合并 |
| `codex-skill-maintenance` | 维护本仓库 | repo |

示例：

```bash
ai-skills install --target user --profile codex-workflow-core --mode symlink
ai-skills install --target user --profile codex-writing-style --mode symlink
ai-skills install --target repo --profile codex-webdev --mode copy --write-agents-md
ai-skills install --target repo --profile codex-cardiacnexus --mode copy --write-agents-md
```

完整 domain 安装仍然支持。若 `audit` 报 active skill 数量或描述长度偏高，把它当作上下文预算提醒，不是安装失败。

## 目录边界

- `skills/`：源层，正式可维护 skill。
- `profiles/`：CLI 安装组合。
- `shared/`：跨 skill 共用材料。
- `assets/codex/plugin-icons/`：中央插件图标和来源记录。
- `scripts/codex_marketplace_config.json`：中央 marketplace 源配置。
- `.agents/plugins/marketplace.json`：生成层，不手改。
- `plugins/codex/plugins/`：生成层，不手改。
- `exports/cardiacnexus-repo-local/`：短期 CardiacNexus 迁移包，合并进目标 repo 后删除。
- `docs/provenance/INTEGRATION_HISTORY.md`：外部来源 canonical history。
- `archive/`、`.tmp/skill-intake/`、`build/skill-intake/`：本地临时区，已加入 `.gitignore`。
- `bundles/` 和 `scripts/install_bundle.py`：legacy compatibility，只为旧流程保留；新文档和新安装优先用 profiles、domains 或 precise skill selectors。

## Presentation 与 CUHK 模板

`presentations` 插件只负责 deck plan、叙事、模板路由、来源忠实度和 QA。底层 PPTX/Google Slides 对象操作交给官方 Presentation/Slides；明确要求 Beamer/Overleaf/LaTeX 时交给 LaTeX 能力。

CUHK 模板材料位于：

```text
skills/tools/documents-media/presentations/shared/templates/cuhk/
```

其中：

- `beamer/source/` 是从本地 `CUHK Template.zip` 提交的完整模板源。
- `design-tokens.json` 是统一视觉 token。
- `beamer/main.tex` 是最小可编译派生模板。
- `pptx/build_reference_deck.py` 可生成可编辑 16:9 reference deck。
- `pptx/cuhk-reference-deck.pptx` 是已生成的可编辑参考 deck。

## 外部来源

外部 GitHub、Notion、网页、截图或文档先进入临时 intake，不直接长期提交原始目录：

```bash
python3 scripts/external_source_intake.py --source <url-or-id> --dry-run
```

每次整合只在 `docs/provenance/INTEGRATION_HISTORY.md` 追加一行，目标 skill 的 frontmatter 继续保留直接来源字段。旧 scratch inventory 已迁出 tracked docs；详细临时证据只放本地 `archive/` 或 `.tmp/skill-intake/`。

## 验证

提交前运行：

```bash
python3 scripts/skills.py registry --write
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
python3 scripts/skills.py catalog --write
python3 scripts/provenance_audit.py --check
python3 scripts/icon_audit.py --scope marketplace --check
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
python3 scripts/build_codex_marketplace.py --path-report
python3 -m unittest discover -s tests
```

Windows 上用 Codex runtime Python 替换 `python3` 即可。
