# AI Skills Collection

这是面向 Codex 的个人科研与工程技能库。它不替代官方插件：官方能力负责文件、浏览器、GitHub、Notion、PDF、Presentation/Slides、LaTeX、前端构建等执行层；本仓库负责长期工作流、科研写作规则、领域判断、安装 profile、来源记录和验收标准。

## 先决定装什么

| 场景 | 本仓库插件或 profile | 同时使用的官方能力 |
|---|---|---|
| 所有主力 Codex 环境 | `workflow-core`、`writing-style` 或 `global-baseline` | GitHub、文件工具 |
| 科研主力机器 | `research-writing`、`statistical-modeling` 或 `research-main` | Zotero、PDF、LaTeX、GitHub |
| 经常做 PPT 的桌面环境 | `presentations` 或 `presentation-desktop` | Presentation/Slides；Beamer 用 LaTeX |
| 前端网站或科研产品 | `web-development` 或 `frontend-research-product` | `build-web-apps`、Figma、GitHub |
| 医学影像项目 | `medical-imaging-project` | PDF、GitHub、前端构建 |
| 生物信息项目 | `bioinformatics-project` | GitHub、文献/数据库工具 |
| Slurm compute node | `server-research-baseline` 或 `ai-skills environment apply` | 站点已有 Slurm、TeX、Python |
| 维护本仓库 | `ai-skills-core` 或 `ai-skills-maintainer` | GitHub，必要时 Notion |

`v3.1` 是仓库重构任务标签。中央 Marketplace 的 9 个插件当前发布版本为 `3.0.0`。

## Codex App 插件市场

推送到 `main` 后，GitHub Actions 会重新生成并验证：

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

生成层不要手改。改 `skills/`、`profiles/`、`scripts/codex_marketplace_config.json` 或 `assets/codex/` 后，重新生成发布层。

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

`cardiacnexus` 不再是中央通用插件。CardiacNexus 项目专用技能保留在短期导出包 `exports/cardiacnexus-repo-local/`，后续合并进目标 repo 的 `.agents/skills/` 后删除该导出包。

## Profile 安装

```bash
ai-skills install --target user --profile global-baseline --mode symlink
ai-skills install --target repo --profile research-main --mode copy --write-agents-md
ai-skills install --target repo --profile presentation-desktop --mode copy --write-agents-md
ai-skills install --target repo --profile frontend-research-product --mode copy --write-agents-md
ai-skills install --target repo --profile server-research-baseline --mode copy --write-agents-md
```

完整 domain 安装仍支持。`audit` 的 active skill 数量或描述长度提示是上下文预算提醒，不是安装失败。

## Server Overlay

服务器环境使用 public-safe site profile 加本地 override。Git 中只保存公共约束；账号、hostname、私有路径、partition、QOS、token、module 私有路径都放在：

```text
~/.config/ai-skills/local-overrides.toml
```

常用命令：

```bash
ai-skills environment init
ai-skills environment list-sites
ai-skills environment detect
ai-skills environment plan --site cuhk-central-cluster --target user
ai-skills environment apply --site cuhk-central-cluster --target user
ai-skills environment doctor --site cuhk-central-cluster
```

`plan` 只读；`apply` 先 staging 再替换；`doctor` 默认不提交 Slurm 作业，只有显式 `--submit-smoke-job` 才允许进入提交路径。

## Presentation 与 CUHK 模板

`presentations` 只负责 deck plan、叙事、模板路由、来源忠实度和 QA。PPTX/Google Slides 对象操作交给官方 Presentation/Slides；明确要求 Beamer/Overleaf/LaTeX 时交给 LaTeX 能力。

CUHK 模板材料位于：

```text
skills/tools/documents-media/presentations/shared/templates/cuhk/
```

其中保留 Beamer 源、样式、必要 PNG、`design-tokens.json`、PPTX reference deck、生成脚本和本地资源 importer；`.vscode`、XCF、样例 Fig/Table 等 zip 非必要资源不提交。

## 目录边界

- `skills/`：源层，正式可维护 skill。
- `profiles/`：CLI 安装组合。
- `site-profiles/`：public-safe 服务器 overlay。
- `schemas/`：profile 和 overlay 的结构约束。
- `assets/codex/`：插件图标、app-facing 图标和来源记录。
- `scripts/codex_marketplace_config.json`：中央 Marketplace 源配置。
- `.agents/plugins/marketplace.json`：生成层，不手改。
- `plugins/codex/plugins/`：生成层，不手改。
- `archive/legacy-bundles/`：tracked legacy bundle 归档。
- `.tmp/skill-intake/`、`.tmp/archive/`、`.codex_tmp_notion_images/`：本地临时区，不提交。
- `docs/provenance/INTEGRATION_HISTORY.md`：外部来源 canonical history。

## 验证

Windows 上如果 `python` 不在 `PATH`，使用 Codex runtime Python：

```powershell
& "$HOME\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts\skills.py validate
```

提交前运行：

```bash
python scripts/skills.py registry --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python scripts/provenance_audit.py --check
python scripts/icon_audit.py --scope marketplace --check
python -m unittest discover -s tests
```
