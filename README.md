# AI Skills Collection

这是一个面向 Codex 和其他 agent 的技能库。普通 Codex App 用户优先安装生成好的插件市场；服务器、HPC、仓库本地安装、用户级安装和技能维护场景，继续使用 `ai-skills` CLI。

## Codex App 安装插件市场

把最新改动推送到 `main` 后，先等待 GitHub Actions 里的 `Codex Marketplace` 工作流执行完成。工作流会重新生成并验证 `plugins/codex/`；如果生成层有变化，它会用带有 `[skip codex-marketplace]` 的提交自动写回 `main`，避免循环触发。

工作流变绿后，在 Codex App 里添加 Git 插件市场：

- 来源：`https://github.com/YuukiAS/AI_Skills_Collection.git`
- Git 引用：`main`
- 稀疏路径：`plugins/codex`

`plugins/codex/` 是自包含的生成发布层。Codex App 只需要拉取这个 sparse path，就可以安装里面的插件；安装后不需要再运行 `ai-skills`。

## Codex App 可安装插件

| 插件 | 包含的 active skills |
|---|---|
| `ai-skills-core` | `project-skill-installer`, `skill-creator`, `skill-installer` |
| `workflow-core` | `codex-workflow-protocol` |
| `writing-style` | `chinese-prose`, `scientific-prose`, `writing-fidelity` |
| `web-development` | `frontend-product-design`, `frontend-testing-debugging`, `frontend-visual-assets`, `react-tailwind-ui`, `figma-design-to-code` |
| `research-writing` | `research-documents`, `research-paper-workflow`, `citation-management`, `research-lookup`, `literature-review` |
| `statistical-modeling` | `bayesian-modeling`, `data-analysis-python`, `scientific-visualization` |
| `bioinformatics` | `bioinformatics-workflows` |
| `medical-imaging` | `ai-ml-imaging`, `medical-imaging-workflows` |
| `cardiacnexus` | `cardiacnexus-workflows` |

其中一部分是聚合 skill：它们在 Codex App 里只暴露一个触发入口，但会把多个源工作流复制到插件内的 `references/source-skills/`。直接复制的 skill 会保留原始 frontmatter，包括来源字段。

## 原始来源记录

本仓库从现在开始要求外部适配的 skill 记录来源，不再只记录作者名。来源信息保存在这些位置：

- 源 skill 的 `SKILL.md` frontmatter：`provenance`, `source_repo_url`, `source_path`, `source_ref`, `source_imported_at`, `source_license`, `source_note`。
- `registry.json`：机器可读注册表，会保留每个 skill 的来源字段。
- `docs/SKILL_PROVENANCE.md`：由脚本生成的来源汇总，按用户原创、外部适配、外部原样引入、生成内容和历史未知来源分类。
- `docs/provenance/CLONED_SKILL_SOURCES.md` 和 `docs/provenance/cloned_skill_sources.json`：记录本轮 clone 过、审查过、适配过或排除过的外部仓库。

历史上没有可靠来源记录的 skill 保持 `provenance: unknown`，不猜测 GitHub URL、commit 或 license。新导入或大幅适配的外部 skill 必须填写完整来源字段。

## 本地 CLI 适用场景

`ai-skills` CLI 仍然是开发者和本地部署入口，适合：

- 给当前仓库安装 repo-local skills；
- 安装到用户级 skills 目录；
- 在服务器、HPC、SSH、tmux 环境中用非交互命令部署；
- 显式使用旧的 `codex-home` 兼容路径；
- 创建、审查、验证和发布 skill。

默认安装位置：

- 仓库本地：`<project>/.agents/skills/`
- 用户级：`$HOME/.agents/skills/`
- 显式旧兼容路径：`${CODEX_HOME:-$HOME/.codex}/skills/`

如果省略 `--target`，`ai-skills install` 默认等同于 `--target repo`，写入当前 Git 仓库的 `.agents/skills/`。除非显式使用 `--target codex-home`，新安装不会写入 `.codex/skills/`。

`ai-skills install ...` 是部署命令：它读取本仓库，只写入选定目标。会修改本仓库的命令是维护命令，例如 `ai-skills new`、`ai-skills registry --write`、`ai-skills catalog --write`。

## CLI 一次性设置

在新服务器上，先 clone 本仓库并安装短命令：

```bash
git clone <repo-url> AI_Skills_Collection
python3 -m pip install --no-build-isolation -e AI_Skills_Collection
```

之后可以在任意仓库中使用：

```bash
ai-skills --help
ai-skills doctor
ai-skills select
ai-skills list --domain bayesian
```

如果没有安装短命令，可以用长命令：

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py --help
```

这是从本地 checkout 做 editable install，不是 PyPI 包。请保留这个 checkout；`--mode symlink` 会指回这个中心库，目标仓库必须自包含时再使用 `--mode copy`。

## 源层和生成层

- `skills/`：正式 skill 源码。
- `profiles/`：CLI 使用的组合安装方案。
- `scripts/codex_marketplace_config.json`：Codex App 插件市场配置。
- `plugins/codex/`：由脚本生成的 Codex App 发布层，不要手工编辑。

修改 `skills/`、`profiles/` 或 marketplace 配置后，运行：

```bash
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
```

## 常用 CLI 命令

查看帮助和环境：

```bash
ai-skills --help
ai-skills install --help
ai-skills doctor
```

浏览 skill：

```bash
ai-skills list --domain bayesian
ai-skills list --domain bioinformatics
ai-skills list --scope writing
ai-skills catalog --write
```

交互选择：

```bash
ai-skills select
```

安装到当前仓库：

```bash
ai-skills install --target repo --domain bayesian --mode symlink --write-agents-md
```

安装完整 domain：

```bash
ai-skills install --target repo --domain bioinformatics --mode symlink --write-agents-md
```

安装单个 skill：

```bash
ai-skills install --target repo --skill domain/bayesian/pymc --mode symlink --write-agents-md
```

安装多个 skill：

```bash
ai-skills install --target repo \
  --skill domain/bayesian/pymc \
  --skill domain/bayesian/bayesian-ppl-diagnostics \
  --mode symlink --write-agents-md
```

安装用户级核心 skill：

```bash
ai-skills install --target user --profile codex-core-global --mode symlink
ai-skills install --target user --profile codex-workflow-core --mode symlink
ai-skills install --target user --profile codex-writing-style --mode symlink
```

刷新已有安装：

```bash
ai-skills update --manifest /path/to/.ai-skills-collection-manifest.json --dry-run
ai-skills update --scan-root /path/to/projects --dry-run --json
```

`update` 会读取已有 manifest，复用上次安装的 target、profile/domain/skill、copy/symlink、AGENTS.md 和 prune 设置。正式执行前先用 `--dry-run` 看清楚会写入哪些 root。

显式使用旧的 `codex-home` 兼容目标：

```bash
ai-skills install --target codex-home --profile codex-core-global --mode symlink --dry-run
```

提交前验证：

```bash
ai-skills registry --write
ai-skills validate
ai-skills audit --all
ai-skills catalog --write
```

## 安装模型

`profiles` 是面向项目或全局启动的组合；`domains` 是完整领域集合；单个 skill selector 用于精确安装。

完整 domain 安装是支持的。如果 `audit` 提示描述长度或 active skill 数量偏高，把它当作上下文预算提醒，不是安装错误。

示例：

```bash
ai-skills install --target repo --profile codex-bayesian-jsdm --mode symlink --write-agents-md
ai-skills install --target repo --domain bayesian --mode symlink --write-agents-md
ai-skills install --target user --profile codex-workflow-core --mode symlink --dry-run
ai-skills install --target user --profile codex-writing-style --mode symlink --dry-run
ai-skills install --target codex-home --profile codex-core-global --mode symlink --dry-run
```

`--target codex-home` 是显式、旧兼容、高级入口。CLI 会在安装前打印检测到的 `CODEX_HOME`、解析后的 codex home、目标 skills root、`config.toml` 状态和可写性。

后续更新推荐流程：

```bash
cd /overflow/htzhu/mingcheng_new/AI_Skills_Collection
git pull --ff-only
ai-skills update \
  --scan-root /overflow/htzhu/mingcheng_new/.codex-global \
  --scan-root /overflow/htzhu/mingcheng_new/.codex-home \
  --scan-root /overflow/htzhu/mingcheng_new/CardiacNexus \
  --scan-root /overflow/htzhu/mingcheng_new/Bioinformatics \
  --scan-root /overflow/htzhu/mingcheng_new/MONAILabel \
  --dry-run
```

跨用户或 CARE 路径需要显式指定对应 root；不要扫描或写入 `/nas`。
`--scan-root` 默认只扫 4 层目录，避免进入缓存、session 或数据目录；如果 manifest 不在常规 `<repo>/.agents/skills/` 深度，再显式加 `--scan-depth`。

## 仓库结构

根目录：

- `skills/`：中心 skill 库，正式可安装 skill 的主要来源。
- `profiles/`：常用全局或项目组合。
- `bundles/`：旧 bundle 定义，保留给 `scripts/install_bundle.py` 兼容使用；新设计优先用 profiles 或 domains。
- `docs/`：用户文档和生成文档，包括安装、迁移、作者指南、skill catalog 和 domain 页面。
- `scripts/`：CLI 和维护脚本。`scripts/skills.py` 是主 CLI，`ai-skills` 是安装后的短命令。
- `shared/`：多个 skill 共用的材料，包括 `AGENTS.md` 模板和前端 UI/UX reference pack。
- `palette/`：设计和可视化 skill 使用的机器可读调色板数据。
- `registry.json`：生成的机器可读注册表。
- `setup.py` 和 `ai_skills_cli/`：提供 `ai-skills` 命令的 editable install 包装。

skill 目录：

- `skills/domains/`：完整领域集合，例如 `bayesian`、`bioinformatics` 和医学相关 domain。
- `skills/tools/`：跨项目工具能力，例如数据科学、前端、文档和可视化。
- `skills/writing/`：写作 skill，包括全局写作守则和科研写作流程。
- `skills/science/`：科研发现、交流和构思流程。
- `skills/projects/`：项目专用 skill。
- `skills/core/`：skill 库维护、安装器和系统 skill。
- `skills/archive/`：不参与默认 registry 的归档、外部或迁移参考内容。
- `skills/**/references/`：较长的领域知识、来源笔记、清单、公式和历史材料。

## 验证

提交前运行：

```bash
ai-skills registry --write
ai-skills validate
ai-skills audit --all
ai-skills catalog --write
```

Codex App 发布层还需要运行：

```bash
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
python3 -m unittest discover -s tests
```

## 文档索引

- `docs/INSTALLATION.md`：CLI 安装模式、SSH/HPC、symlink/copy、Windows/WSL、user 与 codex-home。
- `docs/CODEX_MARKETPLACE.md`：Codex App 插件市场发布层和发布工作流。
- `docs/REPOSITORY_BOUNDARY.md`：活动 skill、生成发布层和外部来源材料之间的边界。
- `docs/MIGRATION.md`：从旧 `.codex/skills` manifest 迁移到 `.agents/skills`。
- `docs/SKILL_AUTHORING.md`：创建 skill、domain、references、description、profiles 和触发 eval。
- `profiles/README.md`：profile、domain 和单 skill 选择方式。
