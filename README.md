# AI Skills Collection

这是面向 Codex 的个人科研与工程技能库。它不替代官方插件：官方能力负责文件、浏览器、GitHub、Notion、PDF、Presentation/Slides、LaTeX、前端构建等执行层；本仓库负责长期工作流、科研写作规则、领域判断、安装 profile、来源记录和验收标准。

## 二选一快速开始

### Codex App / Codex CLI 插件市场

适合普通 Codex App 或 CLI 用户。添加 Git marketplace，安装需要的插件；安装或升级后启动新会话，让 Codex 稳定加载新技能。

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Ref: main
Sparse paths:
.agents/plugins
plugins/codex/plugins
```

CLI 等价命令：

```bash
codex plugin marketplace add https://github.com/YuukiAS/AI_Skills_Collection.git --ref main --sparse .agents/plugins --sparse plugins/codex/plugins
codex plugin marketplace list
codex plugin marketplace upgrade
```

### Source CLI / repo-local profile

适合服务器、HPC、repo-local profile、可编辑开发或需要 symlink 的环境。

```bash
git clone https://github.com/YuukiAS/AI_Skills_Collection.git
python3 -m pip install --no-build-isolation -e AI_Skills_Collection
cd /path/to/project
ai-skills install --target repo --profile research-main --mode symlink --write-agents-md
```

`v4.0.0` 起中央插件版本与 CLI package 版本同步；此前 `setup.py` 的 `0.1.0` 只表示早期本地命令包装器版本。

## 先决定装什么

| 场景 | 本仓库插件或 profile | 同时使用的官方能力 |
|---|---|---|
| 所有主力 Codex 环境 | `workflow-core`、`writing-style` 或 `global-baseline` | GitHub、文件工具 |
| 医学影像项目 | `medical-imaging-project` | PDF、GitHub、前端构建 |
| 生物信息项目 | `bioinformatics-project` | GitHub、文献/数据库工具 |
| Slurm compute node | `server-research-baseline` 或 `ai-skills environment apply` | 站点已有 Slurm、TeX、Python |
| 维护本仓库 | `ai-skills-core` 或 `ai-skills-maintainer` | GitHub，必要时 Notion |


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

## 中央服务器插件集

| 插件 | 用户可见入口 |
|---|---|
| `workflow-core` | `codex-workflow-protocol` |
| `ai-skills-core` | `project-skill-installer`、`ai-skills-repository-maintainer` |
| `writing-style` | `writing-fidelity`、`scientific-prose`、`chinese-prose` |
| `research-writing` | `research-reporting`、`research-paper-workflow`、`literature-and-citations` |
| `bioinformatics` | `bioinformatics-workflows` |
| `medical-imaging` | `medical-imaging-workflows`、`ai-ml-imaging` |

`cardiacnexus` 不再是中央通用插件。CardiacNexus 项目专用技能已经迁移到 CardiacNexus 仓库的 `.agents/skills/`，中央仓库不再保留导出包。

## Profile 安装

```bash
ai-skills install --target user --profile global-baseline --mode symlink
ai-skills install --target repo --profile research-main --mode copy --write-agents-md
ai-skills install --target repo --profile presentation-desktop --mode copy --write-agents-md
ai-skills install --target repo --profile frontend-research-product --mode copy --write-agents-md
ai-skills install --target repo --profile server-research-baseline --mode copy --write-agents-md
```

完整 domain 安装仍支持。`profiles/README.md` 记录当前推荐 profile 和保留的兼容 `codex-*` profile；`audit` 的 active skill 数量或描述长度提示是上下文预算提醒，不是安装失败。

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
ai-skills environment doctor --site cuhk-central-cluster
ai-skills environment apply --site cuhk-central-cluster --target user
ai-skills environment diff --site cuhk-central-cluster --target user
```

`plan` 只读；`doctor` 默认不提交 Slurm 作业；`apply` 先 staging 再替换。只有用户明确要求并提供认证环境时，才做真实登录、Codex App sparse install、CUHK/UNC 远端检查或 Slurm smoke job。

服务器本地安装烟测使用临时 Codex home，不登录、不 SSH、不打开 Codex App、不提交 Slurm 作业：

```bash
ai-skills verify-server-installation
python3 scripts/verify_server_installation.py --profile server-research-baseline --json
```

这个 gate 验证 profile 能安装到 Codex home 形状目录、安装后的 `SKILL.md` 与 icon 引用自洽、generated marketplace payload 路径有效，并报告本机 TeX/Slurm/PPTX 等可选工具是否存在。可选工具缺失默认只作为 warning；真正阻断的是安装或 payload 结构错误。

更多本地配置说明见 `docs/LOCAL_CONFIGURATION.md`。

## Presentation 与 CUHK 模板


CUHK 模板材料位于：

```text
skills/tools/documents-media/presentations/shared/templates/cuhk/
```

其中保留 Beamer 源、样式、必要 PNG、`design-tokens.json`、PPTX reference deck、生成脚本和本地资源 importer；`.vscode`、XCF、样例 Fig/Table 等 zip 非必要资源不提交。仓库测试会检查 CUHK payload 结构和 PPTX zip 有效性；完整 PDF/PPTX render 还要求宿主安装 TeX 包、Times New Roman 兼容字体和 `python-pptx`。

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
python scripts/verify_server_installation.py --json
```
