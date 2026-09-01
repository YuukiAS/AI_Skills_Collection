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

当前整个仓库 / CLI 版本是 `5.0.2`。

Repository / CLI release: `5.0.2`.

仓库版本和插件版本是两回事。仓库现在是 `5.0.2`，中央插件各自独立记版本。以后可能出现 `AI_Skills_Collection 5.0.3`、`presentations 0.4`、`research-writing 0.2` 这样的组合，这是正常的。

`ai-skills-core` 是内部 plugin slug，保持不变。用户界面里它显示为 `AI Skills Maintainer`，意思是维护中央插件时伴随加载的维护同伴，而不是一个替代 `presentations`、`writing-style`、`statistical-modeling` 等专业插件的领域插件。

## 先决定装什么

| 场景 | 本仓库插件或 profile | 同时使用的官方能力 |
|---|---|---|
| 所有主力 Codex 环境 | `workflow-core`、`writing-style` 或 `global-baseline` | GitHub、文件工具 |
| 医学影像项目 | `medical-imaging-project` | PDF、GitHub、前端构建 |
| 生物信息项目 | `bioinformatics-project` | GitHub、文献/数据库工具 |
| Slurm compute node | `server-research-baseline` 或 `ai-skills environment apply` | 站点已有 Slurm、TeX、Python |
| 维护本仓库或改进中央插件 | `workflow-core` + `ai-skills-core`（显示为 `AI Skills Maintainer`）+ 目标 plugin，或 `ai-skills-maintainer` | GitHub，必要时 Notion |

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
| `ai-skills-core` | `0.2` | `unclassified` | `AI Skills Maintainer`：中央插件改进的维护同伴，检查来源、待办、生成层、回放、回归、版本和 changelog | [ai-skills-core](docs/plugin-changelogs/ai-skills-core.md) |
| `writing-style` | `0.1` | `unclassified` | 保留原意，改善中文和英文科研表达 | [writing-style](docs/plugin-changelogs/writing-style.md) |
| `research-writing` | `0.1` | `unclassified` | 报告、论文、文献和引用 | [research-writing](docs/plugin-changelogs/research-writing.md) |
| `presentations` | `0.2` | `baseline` | 科研组会、研究汇报、商务 Presentation 的规划和返修 | [presentations](docs/plugin-changelogs/presentations.md) |
| `scientific-visualization` | `0.1` | `unclassified` | 科研图、配色、示意图、海报和图形检查 | [scientific-visualization](docs/plugin-changelogs/scientific-visualization.md) |
| `web-development` | `0.1` | `unclassified` | 前端参考、视觉系统和科研产品界面 | [web-development](docs/plugin-changelogs/web-development.md) |
| `statistical-modeling` | `0.1` | `unclassified` | Bayesian、数据分析、诊断和统计可视化 | [statistical-modeling](docs/plugin-changelogs/statistical-modeling.md) |
| `bioinformatics` | `0.1` | `unclassified` | 生物信息数据库、GWAS、单细胞、组学等工作流 | [bioinformatics](docs/plugin-changelogs/bioinformatics.md) |
| `medical-imaging` | `0.1` | `unclassified` | 医学影像、CMR、DICOM/NIfTI、分割、配准和影像 AI | [medical-imaging](docs/plugin-changelogs/medical-imaging.md) |

`cardiacnexus` 不再是中央通用插件。CardiacNexus 项目专用技能已经迁移到 CardiacNexus 自己的仓库。

## 真实项目怎么反过来改进插件

这是这个仓库以后最重要的长期用法。

以后你在 TRACE、CARE、Distributed Imaging 或别的项目里用某个 plugin，发现结果不好，并且说：

> 记录 repo 并保存到合适的地方。

Codex 先判断：**这是项目本身的问题，还是 plugin 自己的问题？**

### 项目本身的问题，留在项目 repo

例如 TRACE 里：

- 下一步还要补什么实验；
- theorem 到底怎么写；
- 某个数据集怎么解释；
- 模型要不要增加新部分；
- TRACE 自己的代码有 bug。

这些当然继续写 TRACE 的 `ROADMAP.md`、模型/数据文档、任务记录等合适位置。

### 用 plugin 时暴露的问题，直接写回这个仓库

例如你在 TRACE 里用 `presentations` 返修 CAT-TRACE PPT，发现：

- 箭头穿过文字；
- 图还是太小，投影时看不清；
- 已经接受的页面被这轮返修顺手改坏；
- 公式页层次很差；
- 你明明要求“继续改现有 PPT”，它却重新生成了一套。

这些本质上是 `presentations` 的问题，所以**不要再把它们当成 TRACE 的科研 TODO 保存一份**。直接读：

```text
TODO.md
docs/plugin-todos/presentations.md
```

然后把这次真实问题记到 `presentations.md`。

报告插件的问题写 `docs/plugin-todos/research-writing.md`；统计插件的问题写 `docs/plugin-todos/statistical-modeling.md`；医学影像插件的问题写 `docs/plugin-todos/medical-imaging.md`。其他 plugin 同理。

一个很实用的判断是：

> 换成另一个真实项目，这个 plugin 还可能犯同样的错吗？

如果答案大概率是“会”，就应该优先记到 plugin TODO，而不是项目 TODO。

### 项目 thread 要写多复杂？不用复杂

真实项目 thread 不负责直接制定“以后所有项目都必须遵守的规则”。它只需要把这次真实失败写清楚。

如果目标 plugin 的 TODO 里没有同一问题，就加一个 `NEW`：

```text
### <简短的问题标题>
status: NEW
source: <真实项目 / 当前任务>
evidence: <实际输出的路径、链接、commit 或 render>
problem: <用户实际看到的问题>
project-specific context: <哪些细节只属于当前项目，不应该变成通用规则>
```

例如：

```text
### Existing-deck revision changed an accepted slide
status: NEW
source: TRACE / CAT-TRACE group-meeting revision
evidence: <实际 PDF / render / task 路径>
problem: 用户只要求修改 P10，但上轮已经接受的 P9 也发生了明显变化。
project-specific context: P9/P10 的 CAT-TRACE 科学内容本身不应该变成通用规则。
```

这里先记“发生了什么”，不要急着写“以后所有 PPT 必须怎样”。

### 谁负责把这些问题整理成真正的插件规则？

AI_Skills_Collection 的 Planner / maintainer 负责。

它会再检查：

1. 这个 plugin 现在是不是已经有同样的规则；
2. 对应 plugin TODO 里是不是已经有同一个问题；
3. 别的真实项目有没有遇到过类似问题；
4. 哪些细节只是当前项目自己的内容。

然后再决定：

- 已经有同一个 TODO → 把这次真实案例合进去，不重复新建；
- 插件本来已经有规则但还是做错 → 重点查为什么实际没有执行；
- 只是这个项目特殊 → 不把它升级成通用规则；
- 确实是新的通用问题 → 整理成长期候选；
- 证据已经足够 → 再单独开一轮真正修改 plugin。

所以整套流程其实只有一句话：

> **项目自己的问题留在项目 repo；plugin 自己的问题直接记回对应 plugin TODO；中央 Planner 再负责去重和提炼。**

### TODO 到底放在哪里

AI_Skills_Collection 根目录有一个 [TODO.md](TODO.md)，它只是总入口，像根 `CHANGELOG.md` 一样负责导航，不重复维护十份具体问题。

真正的插件待办在：

```text
docs/plugin-todos/<plugin>.md
```

已经正式解决并发布的变化写到：

```text
docs/plugin-changelogs/<plugin>.md
```

整个仓库每次正式发布改了什么，看根 [CHANGELOG.md](CHANGELOG.md)。

简单分工：

- 项目 repo：项目自己的研究、产品、代码和实验事情。
- `TODO.md`：AI_Skills_Collection 的待办总入口。
- `docs/plugin-todos/<plugin>.md`：某个 plugin 真实暴露了哪些问题、以后要改什么。
- `docs/plugin-changelogs/<plugin>.md`：某个 plugin 已经在哪个版本解决了什么。
- `CHANGELOG.md`：整个 AI_Skills_Collection 每次正式发布改了什么。

详细维护规则在：

- `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
- `docs/plugin-todos/README.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

普通使用时记住上面的那句话就够了。

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

`presentations` 当前独立版本是 `0.2`。科研组会、导师讨论和研究进展汇报会先弄清楚“这页要说明什么、证据在哪里”，再决定用图、公式、表、医学图像、实验设计还是讨论页。

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
