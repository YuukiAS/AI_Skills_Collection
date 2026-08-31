# AI Skills Collection

这是一个给 Codex 用的个人科研与工程技能库。它主要解决两件事：一是让 Codex 在科研、写作、Presentation、统计、医学影像、前端和服务器等任务里知道该怎么做；二是把真实项目里反复出现的问题慢慢整理成更好的插件。

它不替代官方文件、浏览器、GitHub、PDF、Presentation/Slides、LaTeX 等工具。官方工具负责“做事”，这个仓库主要负责“怎么做才对、怎么验收、以后怎么少犯同样的问题”。

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

当前整个仓库 / CLI 版本是 `5.0.0`。

仓库版本和插件版本是两回事。仓库现在是 `5.0.0`，十个中央插件各自从 `0.1` 开始独立记版本。以后可能出现 `AI_Skills_Collection 5.0.3`、`presentations 0.4`、`research-writing 0.2` 这样的组合，这是正常的。

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

`.agents/plugins/marketplace.json` 和 `plugins/codex/plugins/` 是自动生成的，不要手改。应该先改 `skills/`、`profiles/`、`scripts/codex_marketplace_config.json` 等源文件，再重新生成。

## 中央插件

| Plugin | Version | Status | 主要用途 | Changelog |
|---|---:|---|---|---|
| `workflow-core` | `0.1` | `unclassified` | 复杂任务的执行顺序、检查和收尾 | [workflow-core](docs/plugin-changelogs/workflow-core.md) |
| `ai-skills-core` | `0.1` | `unclassified` | 安装 profile、维护 registry/catalog、发布 Marketplace | [ai-skills-core](docs/plugin-changelogs/ai-skills-core.md) |
| `writing-style` | `0.1` | `unclassified` | 保留原意，改善中文和英文科研表达 | [writing-style](docs/plugin-changelogs/writing-style.md) |
| `research-writing` | `0.1` | `unclassified` | 报告、论文、文献和引用 | [research-writing](docs/plugin-changelogs/research-writing.md) |
| `presentations` | `0.1` | `baseline` | 科研组会、研究汇报、商务 Presentation 的规划和返修 | [presentations](docs/plugin-changelogs/presentations.md) |
| `scientific-visualization` | `0.1` | `unclassified` | 科研图、配色、示意图、海报和图形检查 | [scientific-visualization](docs/plugin-changelogs/scientific-visualization.md) |
| `web-development` | `0.1` | `unclassified` | 前端参考、视觉系统和科研产品界面 | [web-development](docs/plugin-changelogs/web-development.md) |
| `statistical-modeling` | `0.1` | `unclassified` | Bayesian、数据分析、诊断和统计可视化 | [statistical-modeling](docs/plugin-changelogs/statistical-modeling.md) |
| `bioinformatics` | `0.1` | `unclassified` | 生物信息数据库、GWAS、单细胞、组学等工作流 | [bioinformatics](docs/plugin-changelogs/bioinformatics.md) |
| `medical-imaging` | `0.1` | `unclassified` | 医学影像、CMR、DICOM/NIfTI、分割、配准和影像 AI | [medical-imaging](docs/plugin-changelogs/medical-imaging.md) |

`cardiacnexus` 不再是中央通用插件。CardiacNexus 项目专用技能已经迁移到 CardiacNexus 自己的仓库。

## 真实项目怎么反过来改进插件

这是这个仓库以后最重要的长期用法。

假设你正在 TRACE 里继续改 CAT-TRACE PPT，并且说：

> 记录 repo 并保存到合适的地方。

Codex **先记录到 TRACE 自己的仓库**，而不是马上跑来改 AI_Skills_Collection。

应该放哪里，按问题本身来选：

- 这是项目长期还要做的事：放进这个项目已有的 `TODO`、`ROADMAP` 或同类长期计划。
- 这是某一次具体任务、返修或实验发生的问题：放进这一轮已有的 `result.md`、review、revision note 或同类记录。
- 这是已经确定的长期科学/产品决定：放进项目已有的 decision / design 文档。
- 如果仓库已经有合适位置，就用原来的位置；不要为了“记录一下”再发明一套新目录或新格式。

### 如果这个问题可能是插件本身的问题

例如你在 TRACE 里发现：

- PPT 箭头又穿过文字；
- 已经接受的页面被局部返修时意外改坏；
- 导师报告又变成了运行日志；
- 某个统计插件把真实数据问题处理错了。

项目 Codex 仍然先在**当前项目**记录真实情况。最好在同一个 task result / review 里加一个很短的 `AI_Skills feedback` 小节，只写四件事：

```text
可能相关的 plugin: presentations
实际问题: 用户真正看到的错误是什么
evidence: 对应 PDF / render / result / review 在项目里的路径
项目专属部分: 哪些内容只属于 CAT-TRACE / CARE / 当前数据集
```

这里不要急着写“以后所有 PPT 都必须怎样”。项目 Codex 的任务是把事实记清楚，不是替中央插件制定永久规则。

之后再到 AI_Skills_Collection，由这里的 Planner / maintainer 做第二步：

1. 看项目里记录的真实问题；
2. 看这个插件现在是不是已经有同样的规则；
3. 看 `docs/plugin-todos/<plugin>.md` 里是不是已经有同一个问题；
4. 看别的真实项目有没有遇到过类似问题；
5. 决定这是项目自己的问题、已有规则没有真正执行，还是一个值得插件学习的新问题。

只有这一步做完，真正能推广的问题才进入对应的中央插件 TODO。

所以一句话：

> **项目仓库记录“发生了什么”；AI_Skills_Collection 再整理“插件应该学到什么”。**

### TODO 到底放在哪里

AI_Skills_Collection 根目录有一个 [TODO.md](TODO.md)，它只是总入口，像根 `CHANGELOG.md` 一样负责导航，不重复维护具体问题。

真正的插件待办在：

```text
docs/plugin-todos/<plugin>.md
```

例如 Presentation 的长期问题在：

```text
docs/plugin-todos/presentations.md
```

已经正式解决并发布的变化则写到：

```text
docs/plugin-changelogs/<plugin>.md
```

整个仓库每次正式发布改了什么，看根 [CHANGELOG.md](CHANGELOG.md)。

因此这几个文件的分工很简单：

- 项目 repo 的 TODO / result / review：这次真实项目发生了什么、接下来项目自己还要做什么。
- `TODO.md`：AI_Skills_Collection 的待办总入口。
- `docs/plugin-todos/<plugin>.md`：某个插件以后要解决哪些通用问题。
- `docs/plugin-changelogs/<plugin>.md`：某个插件已经在哪个版本解决了什么。
- `CHANGELOG.md`：整个 AI_Skills_Collection 每次发布改了什么。

详细维护规则在：

- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/plugin-todos/README.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

这些文件给维护者看；普通使用时记住上面那句“项目先记事实，中央再提炼”就够了。

## Profile 安装

```bash
ai-skills install --target user --profile global-baseline --mode symlink
ai-skills install --target repo --profile research-main --mode copy --write-agents-md
ai-skills install --target repo --profile presentation-desktop --mode copy --write-agents-md
ai-skills install --target repo --profile frontend-research-product --mode copy --write-agents-md
ai-skills install --target repo --profile server-research-baseline --mode copy --write-agents-md
```

完整 domain 安装仍支持。`profiles/README.md` 记录当前推荐 profile。`audit` 如果提示 active skill 太多或描述太长，主要是在提醒上下文可能太重，不等于安装失败。

## Server / HPC

服务器环境使用公开的 site profile 加本地私有配置。Git 中只保存可以公开的规则；账号、hostname、私有路径、partition、QOS、token 等放在：

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

`plan` 只看准备怎么做，不会真正修改；`doctor` 默认不提交 Slurm 作业；`apply` 才真正应用配置。只有用户明确要求并且当前环境有权限时，才做真实远端检查或 Slurm smoke job。

服务器本地安装检查使用临时 Codex home，不登录、不 SSH、不打开 Codex App、不提交 Slurm 作业：

```bash
ai-skills verify-server-installation
python3 scripts/verify_server_installation.py --profile server-research-baseline --json
```

更多本地配置说明见 `docs/LOCAL_CONFIGURATION.md`。

## Presentation 与 CUHK 模板

`presentations` 当前独立版本是 `0.1`。科研组会、导师讨论和研究进展汇报会先弄清楚“这页要说明什么、证据在哪里”，再决定用图、公式、表、医学图像、实验设计还是讨论页。

如果用户是在**继续返修已经存在的 PPT/Beamer**，默认应该修改现有版本，而不是从头再生成一套。已经被用户接受的页面和元素要尽量保持，局部返修不能顺手把别的页改坏。最后要看真实 PDF / PNG render，不能因为源码能编译就宣布完成。

这条路线明确不接受用空表格、圆角卡片、装饰图标、泛泛的箭头或大段文字去冒充科研内容。真实组会如果很急，优先保证一个可靠、能讲的版本，不让插件实验阻塞实际汇报。

CUHK 模板材料位于：

```text
skills/tools/documents-media/presentations/shared/templates/cuhk/
```

更详细的 Presentation 版本历史看 `docs/plugin-changelogs/presentations.md`，不要在 README 里堆旧版本内部实现细节。

## 目录说明

- `skills/`：真正维护的 skill 源文件。
- `profiles/`：一组组安装组合。
- `site-profiles/`：服务器/HPC 的公开环境规则。
- `schemas/`：配置文件结构。
- `assets/codex/`：插件图标和相关资源。
- `scripts/codex_marketplace_config.json`：中央 Marketplace 的源配置。
- `.agents/plugins/marketplace.json`：自动生成，不手改。
- `plugins/codex/plugins/`：自动生成，不手改。
- `TODO.md`：整个仓库待办的导航首页。
- `docs/plugin-todos/`：各插件真正的长期待办。
- `docs/plugin-changelogs/`：各插件已经发布的版本变化。
- `archive/legacy-bundles/`：旧 bundle 归档。
- `.tmp/` 一类目录：本地临时文件，不提交。

## 验证

Windows 上如果 `python` 不在 `PATH`，可以使用 Codex runtime Python：

```powershell
& "$HOME\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts\skills.py validate
```

提交前常用检查：

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
