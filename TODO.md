# TODO v3：完成 v2 缺口，并建立可同步的服务器环境 Overlay 系统

## 0. 任务结论与执行边界

本文件替代 `TODO v2`，作为下一轮 Codex 重构的唯一根目录任务说明。

先给出审计结论：**v2 已完成中央插件拓扑的主要重构，但没有彻底达到 v2 自己定义的最终验收标准。** 当前状态不能标记为“v2 全部完成”；v3 必须先关闭已确认的 v2 缺口，再实现 CUHK/UNC 服务器环境的额外加载、同步和验证能力。

本轮只修改源层和生成器，不手工维护：

```text
.agents/plugins/marketplace.json
plugins/codex/plugins/
```

上述目录继续由 Marketplace builder 生成。

本轮后续还要为从 Notion 读取、审查并合并其他人的 Skill/规范做好基础设施，但**不要在不知道具体 Notion 页面内容、权限和许可的情况下预先复制或虚构任何来源内容**。

---

## 1. v2 完成度审计：实施前必须重新验证

以下判断基于当前 `main`，实现者必须在开始编码后重新读取真实文件和最新 commit；不得仅依赖本 TODO 的摘要。

### 1.1 已基本实现的部分

- [x] 中央 Marketplace 已重构为九个通用插件：
  - `workflow-core`
  - `ai-skills-core`
  - `writing-style`
  - `research-writing`
  - `presentations`
  - `web-development`
  - `statistical-modeling`
  - `bioinformatics`
  - `medical-imaging`
- [x] `presentations` 在 App-facing 层拆成 `research-presentations` 和 `business-presentations`。
- [x] `research-writing` 的中央发布层不再直接发布旧 `pptx` 和 `scientific-slides`。
- [x] `web-development` 的 App-facing 定位已收敛到参考研究、视觉系统和科研产品前端补充层。
- [x] Marketplace builder 已支持 plugin-level shared payload 和插件图标复制。
- [x] README 已增加初步安装矩阵和官方插件协作说明。
- [x] 旧 cloned-source inventory 已迁入 `docs/provenance/INTEGRATION_HISTORY.md`。
- [x] 中央 `cardiacnexus` 插件已从 Marketplace 配置移除。

### 1.2 尚未彻底实现的部分

以下项目均为 v3 的阻断性前置工作。

#### A. CardiacNexus 迁移未完成

当前只是把四个项目 Skill 放进：

```text
exports/cardiacnexus-repo-local/
```

CardiacNexus 仓库自身仍使用旧 `.codex/skills/`，并仍把中央 `AI_Skills_Collection` 视为 canonical upstream。因此：

- [ ] 将四个 CardiacNexus Skill 真正合并到 `YuukiAS/CardiacNexus/.agents/skills/`。
- [ ] 更新 CardiacNexus `AGENTS.md`，以 repo-local `.agents/skills/` 为唯一项目事实源。
- [ ] 删除旧 `.codex/skills` 路由说明和过时中央目录路径。
- [ ] 在 CardiacNexus repo 运行路由、内容和项目测试。
- [ ] 提交 CardiacNexus commit 后，在中央 integration history 记录真实 commit。
- [ ] 删除中央 `exports/cardiacnexus-repo-local/`。
- [ ] `INTEGRATION_HISTORY.md` 中 CardiacNexus 行不得继续是 `pending`。

#### B. 旧 Presentation 入口仍然是 active source Skill

当前源层的 `pptx` 仍有“任何 `.pptx`、deck、slides、presentation 都触发”的宽泛描述；旧 `scientific-slides` 仍是 active，并继续声明 `OPENROUTER_API_KEY` 和整页 AI 图片路径。虽然它们已从中央 App-facing 插件移除，但仍可能被旧 profile、domain 或 repo-local 安装带入，从而与新 Presentation 路由冲突。

- [ ] 审计所有 profile、domain、catalog 和安装路径，确认谁仍会安装 `pptx` 或 `scientific-slides`。
- [ ] 将有价值的底层兼容资料留作非默认 reference/archive；不得保留 broad active trigger。
- [ ] 旧 `scientific-slides` 中有价值的结构、时长、引用和 QA 内容迁入新 Skill 后，标记 deprecated/inactive/archive。
- [ ] 删除不存在的脚本、模板和默认 OpenRouter/Nano Banana 依赖声明。
- [ ] 为“普通 PPTX 小编辑只调用官方 Presentation/Slides”的负例增加 trigger eval。

#### C. Presentations 目前只是骨架

当前两个 Skill 和 compatibility 文档过短，尚未形成可执行的完整工作流。

- [ ] 在当前 Codex 环境真实读取官方 Presentation/Slides 与 LaTeX 插件 manifest/Skill，记录实际名称、触发方式、输入输出、编辑/渲染/notes/charts 支持和限制。
- [ ] compatibility 文档必须是实测结论，不能只写泛化职责列表。
- [ ] 实现 `deck-plan` 的版本化 schema、验证器、示例和错误信息。
- [ ] 实现 Markdown/Asteria/TRACE 输入适配器，保留公式、图表、引用、脚注和 source anchors。
- [ ] 加入一份脱敏 Asteria/Marked TRACE fixture 和端到端回归测试。
- [ ] 生成可编辑 PPTX、PDF/images 预览、deck plan 和 QA 报告；不能只测试文件存在。

#### D. CUHK 模板不满足 v2 的最小发布要求

当前 README 明确把完整 `CUHK Template.zip` 源树提交进 payload，其中包含 `.vscode`、XCF 和样例 Fig/Table；当前 PPTX builder 只生成标题、单一内容页和 closing 三页，未提供 v2 要求的完整 layout 集。

- [ ] 重新审计 CUHK ZIP 的运行时依赖、样例、编辑器文件、XCF、logo 和许可。
- [ ] Marketplace payload 只保留运行时必要、许可明确的最小文件。
- [ ] `.vscode`、未使用 XCF、样例 Fig/Table 和空 bibliography 不得默认发布。
- [ ] 如 CUHK logo/校名再分发许可不明确，公共仓库只保留合法 token/layout 和本地导入器。
- [ ] PPTX reference deck 至少覆盖：title、section divider、standard content、equation/model、process/method、full figure、figure + interpretation、comparison、table、references、closing、backup。
- [ ] 所有关键对象可编辑，并通过渲染与视觉检查。
- [ ] Beamer 与 PPTX 使用同一 token 事实源，但允许格式特定布局。

#### E. 图标只完成了插件层的最小版本

当前 `icon_audit.py`：

- 对 active source Skill 没有资产时直接跳过；
- 没有检查 100% 覆盖；
- `--contact-sheet` 仍只是 reserved；
- 没有完整检查 `agents/openai.yaml`、small/large icon、尺寸、哈希、外部资源、字体、`foreignObject`、近重复和浅/深色可读性。

因此 v2 的 P1 和 App-facing Skill 图标验收尚未完成。

- [ ] 中央九插件全部保留合法插件图标。
- [ ] 所有 App-facing active Skill 必须有 `agents/openai.yaml`、`icon_small`、`icon_large`、`brand_color`、`display_name` 和默认 prompt。
- [ ] 所有 `status: active` 源 Skill 最终达到 100% 图标覆盖，或先明确分阶段并把缺失设为 hard failure 的目标日期。
- [ ] 实现真实 contact sheet。
- [ ] 图标 audit 对缺失资产不得继续静默跳过。

#### F. Provenance/Notion intake 仍是框架，不是完整实现

当前 `external_source_intake.py` 只创建一个 README；`provenance_audit.py` 没有验证 integration commit 是否存在、target 是否存在、历史是否 append-only、直接来源 frontmatter 是否完整，也没有阻断 `pending`/`pre-v2` 这类无法验证的完成记录。

- [ ] 加强 history schema 和 audit。
- [ ] `integration_commit` 必须是可验证 commit，或使用明确的 `legacy-unresolved` 状态并列入失败/警告清单。
- [ ] target Skill/插件/项目路径必须存在。
- [ ] 直接合并的外部内容必须有 frontmatter provenance 和必要 LICENSE/NOTICE。
- [ ] Notion intake 支持接收页面 title、稳定 ID/URL、`last_edited_time`、读取日期、权限/所有权基础和目标。
- [ ] 私有 Notion 正文不得进入公开 history。
- [ ] 为后续 Notion 页面合并建立真实 dry-run/plan/apply/cleanup 流程。

#### G. Profile 和 README 仍有旧架构残留

README 与 `profiles/README.md` 仍列出旧 profile 体系；`codex-research-writing` 仍声称包含 PDF、slides 等旧广义能力；`codex-cardiacnexus` 仍存在中央安装叙事。

- [ ] 统一 README、profiles、registry、catalog 和 App-facing 插件命名。
- [ ] 建立清晰的推荐 profile：
  - `global-baseline`
  - `research-main`
  - `presentation-desktop`
  - `frontend-research-product`
  - `medical-imaging-project`
  - `bioinformatics-project`
  - `ai-skills-maintainer`
- [ ] 旧 profile 若保留兼容别名，必须标记 deprecated 并有迁移说明。
- [ ] CardiacNexus 项目 Skill 不得再由中央 profile 复制；中央 profile 只能安装通用支持 Skill。

#### H. 缺少 v2 规定的路由和端到端测试

- [ ] `writing-style` 与 `research-writing` 的正例、反例、组合例。
- [ ] `research-presentations` 与 `business-presentations` 的互斥路由。
- [ ] 小型 PPTX 编辑不触发 orchestration。
- [ ] `web-development` 与官方 `build-web-apps` 的串联路由。
- [ ] Asteria/TRACE → deck plan → editable PPTX → render → QA。
- [ ] 真实 Codex App sparse Marketplace 安装。
- [ ] CardiacNexus repo-local Skill 路由。

### 1.3 v2 Closure Report

实现者必须创建：

```text
docs/audits/TODO_V2_COMPLETION_AUDIT.md
```

每个 v2 最终验收项标记：

```text
PASS | PARTIAL | FAIL | NOT_APPLICABLE
```

并列出：实现路径、测试、commit 和剩余问题。只有全部阻断项为 PASS 后，才能进入 v3 环境系统的最终验收。

---

## 2. v3 新输入：两个服务器 Skill ZIP

当前仓库根目录新增：

```text
skills-CUHK.zip
skills-UNC.zip
```

来源 commit：`b7f981e7d7937be4211e76c057f9ecbf8cc8e210`。

初步中央目录审计显示，两包都混合了通用写作 Skill、中文数学 PDF Skill 和站点 Slurm Skill，但命名和内容存在差异。

### 2.1 已识别的顶层内容

`skills-CUHK.zip` 至少包含：

```text
writing-core-writing-fidelity/
writing-core-scientific-prose/
writing-core-chinese-prose/
slurm-partition-routing/
render-chinese-math-pdf/
```

其中 `writing-core-chinese-prose/` 还包含旧 `TODO.md`；该文件不能直接合入正式源层。

`skills-UNC.zip` 至少包含：

```text
tools-documents-media-render-chinese-math-pdf/
writing-core-chinese-prose/
writing-core-scientific-prose/
writing-core-writing-fidelity/
slurm-routing-partition/
```

### 2.2 ZIP 处理规则

这两个 ZIP 是**临时 legacy intake**，不是长期 source of truth。

- [ ] 在未跟踪目录中解压，例如 `.tmp/skill-intake/server-zips/`。
- [ ] 计算 SHA256，并记录 ZIP 名称、commit、哈希和读取日期。
- [ ] 先扫描私钥、token、邮箱、用户名、绝对路径、account、QOS、hostname、内部 URL、代理和其他敏感配置。
- [ ] 如发现凭据或秘密，立即停止合并，报告用户并提出轮换；不得只从最新 commit 删除后假装历史安全。
- [ ] 若需要清理 Git 历史，必须先单独说明影响并获得用户明确批准。
- [ ] 比较 ZIP 中每个 Skill 与当前中央源 Skill，生成本地差异报告。
- [ ] 通用写作 Skill 只合并真实增量；不得用服务器旧副本覆盖 v2 后中央版本。
- [ ] ZIP 内旧 `TODO.md`、部署产物、缓存、绝对路径和重复文件不进入正式源层。
- [ ] 合并完成后删除解压目录。
- [ ] 在 `INTEGRATION_HISTORY.md` 为 CUHK、UNC 各追加一行。
- [ ] 最终从仓库根目录删除两个 ZIP；正式代码、结构化 profile、provenance 和必要许可保留。

---

## 3. v3 目标：通用 Skill + Site Profile + Local Override + Repo-local Skill

### 3.1 为什么不能继续复制完整全局 Skill

禁止继续把 CUHK 和 UNC 用户目录中的完整 Skill 当作两份独立源码维护。目标模型：

```text
AI_Skills_Collection 中的通用 Skill
        +
当前站点的结构化 Site Profile
        +
当前机器未跟踪的 Local Override
        +
当前项目的 Repo-local Skill
        ↓
部署到 ~/.agents/skills/ 的可追踪安装结果
```

`~/.agents/skills/` 是部署层，不是 canonical source。

### 3.2 四层职责

#### A. 通用 Skill 源层

位于当前公共仓库，保存跨机器通用逻辑：

```text
skills/tools/documents-media/render-chinese-math-pdf/
skills/tools/hpc/slurm-workflows/
```

`slurm-workflows` 是 v3 的统一名称。必须从 CUHK 的 `slurm-partition-routing` 和 UNC 的 `slurm-routing-partition` 中提炼通用策略，不保留两份完整 Skill。

#### B. Site Profile

保存 CUHK/UNC 环境事实和站点策略，例如：

- TeX Live 发现方式、module 命令、推荐引擎、字体策略；
- Slurm partition、QOS、account 约束、资源上限、优先级和 race policy；
- 推荐 scratch、日志目录规范和 read-only discovery 命令；
- `last_verified`、验证依据和配置版本。

Site Profile 可以来自：

1. 当前仓库中的 `public-safe` profile；
2. 一个私有 companion repo 的本地 checkout；
3. 一个本地未跟踪目录。

CLI 必须支持多个 profile roots。不得把 Git 凭据或私有仓库 token 写入配置。

#### C. Local Override

只保存当前机器事实或秘密，例如：

- 个人 TeX 路径；
- 用户名或 account；
- 仅本机存在的字体；
- 临时 scratch 路径；
- 私有 module 初始化；
- 不能进入 Git 的值。

默认位置：

```text
~/.config/ai-skills/local-overrides.toml
```

该文件不得被复制进报告、history、插件 payload 或日志。

#### D. Repo-local Skill

项目事实继续位于：

```text
<repo>/.agents/skills/
```

例如 CardiacNexus、CARE、TRACE/Asteria。项目可以请求资源和选择策略，但不得绕过站点硬限制。

---

## 4. 配置合并模型：不要用一个简单的“最后覆盖全部”

环境字段必须分类处理。

### 4.1 字段类别

```text
capabilities   运行时探测得到的可用命令、分区、字体和工具
constraints    站点硬限制；项目和 local override 不得削弱
policy         站点策略，例如 partition race 是否允许
preferences    通用默认 < 站点默认 < 项目请求
local_paths    local override 可提供最终机器路径
secrets        只允许 local override 或环境变量
```

### 4.2 冲突规则

- `constraints`：Site Profile 权威；后续层只能更严格，不能更宽松。
- `policy`：Site Profile 权威；如项目请求冲突，明确报错。
- `preferences`：项目可在站点允许范围内调整。
- `local_paths`：本机 override 优先，但必须通过存在性和可执行性验证。
- `secrets`：禁止进入生成 Skill、manifest 明文、history 和日志。
- 自动探测结果与配置冲突时，`doctor` 必须报告 drift；不得静默继续。

---

## 5. Site Profile Schema

新增建议结构：

```text
environment/
  schemas/
    site-profile.schema.json
    local-overrides.schema.json
    environment-manifest.schema.json
  examples/
    public-safe-site.example.yaml
    local-overrides.example.toml
  templates/
    generated-site-reference.md.j2
```

实际目录可调整，但必须有单一 schema 事实源。

### 5.1 Site Profile 最小字段

```yaml
schema_version: 1
site_id: cuhk
name: CUHK Server
visibility: private | public-safe
profile_version: 1

detect:
  hostname_patterns: []
  required_commands: []
  environment_markers: {}

skills:
  include:
    - render-chinese-math-pdf
    - slurm-workflows

tex:
  discovery_commands:
    - command -v latexmk
    - command -v xelatex
    - kpsewhich -var-value=TEXMFROOT
  module_commands: []
  preferred_engine: xelatex
  bibliography_backend: biber
  required_capabilities: []
  constraints: {}

slurm:
  discovery_commands:
    - sinfo
    - scontrol show partition
    - squeue --me
  partitions: []
  qos: []
  constraints: {}
  defaults: {}
  partition_priority: []
  race_policy:
    allowed: false
    cancel_losers: true
    output_isolation_required: true

verification:
  last_verified: null
  methods: []
```

具体真实值必须从 ZIP 和当前服务器验证后填写，不能从旧聊天猜测。

### 5.2 Public/Private 划分

- [ ] 为每个字段标记是否适合公开。
- [ ] 绝对个人路径、用户名、account、内部 host、私有 URL 和秘密默认不进入公共 repo。
- [ ] 如果 CUHK/UNC 配置无法安全公开，生成一个可提交到私有 companion repo 的迁移包，并要求用户指定该 repo/local checkout。
- [ ] 当前公共仓库必须仍可在没有私有 profile 的情况下运行通用验证和 fixture 测试。

---

## 6. `ai-skills environment` CLI

在现有 CLI 内增加正式子命令，不另建互不兼容脚本。

### 6.1 命令

```bash
ai-skills environment init
ai-skills environment list-sites
ai-skills environment detect
ai-skills environment plan
ai-skills environment apply
ai-skills environment sync
ai-skills environment diff
ai-skills environment doctor
ai-skills environment uninstall
```

### 6.2 本机配置

建议：

```toml
# ~/.config/ai-skills/environment.toml
schema_version = 1
site = "cuhk"
public_skills_root = "/path/to/AI_Skills_Collection"
site_profile_roots = ["/path/to/private-or-local-environment-profiles"]
local_override = "~/.config/ai-skills/local-overrides.toml"
```

不得把示例绝对路径写成所有用户默认值。

### 6.3 行为要求

#### `init`

- 创建本机配置模板；
- 不覆盖已有配置；
- 不写 token；
- 提示用户选择明确 site 或启用 detect。

#### `detect`

- 使用只读 hostname/env/command marker；
- 多个 site 同时匹配时必须报 ambiguous；
- 无匹配时要求显式 `--site`，不能猜测；
- 输出依据。

#### `plan`

- 列出将安装/更新/删除的 Skill；
- 列出 generic source commit、site profile revision、local override hash；
- 列出生成的 overlay 文件；
- 默认不写磁盘。

#### `apply`

- 只使用 copy/materialize 模式，不用 symlink 叠加环境文件；
- 在 staging 目录构建；
- 注入结构化生成的 site reference；
- 验证后原子替换目标 Skill；
- 不修改无关 user Skills；
- 失败时保持原安装可用；
- 支持 `--dry-run`、`--site`、`--target user` 和 `--yes`。

#### `sync`

- 默认只同步已有本地 checkout 和 manifest，不隐式处理 Git 凭据；
- 可选 `--update-sources` 才运行明确的 `git pull --ff-only`；
- 公共 Skill 更新后保留 site 配置；
- Site Profile 更新后重新 materialize affected Skills；
- 结果幂等。

#### `diff`

比较：

```text
canonical generic source
+ resolved site profile
+ local override hash
vs
installed environment manifest
```

输出 drift，不泄漏秘密值。

#### `doctor`

执行只读验证和可选 smoke test，详见第 9 节。

#### `uninstall`

只删除当前 environment manifest 管理的路径，不清理整个 `~/.agents/skills/`。

---

## 7. Overlay Materialization Contract

为避免 Codex 无法稳定跨 Skill 自动读取另一个配置 Skill，环境 profile 必须 materialize 到受影响 Skill 内部。

目标部署示例：

```text
~/.agents/skills/render-chinese-math-pdf/
  SKILL.md
  references/
    ...
    _generated/
      site-profile.md

~/.agents/skills/slurm-workflows/
  SKILL.md
  references/
    ...
    _generated/
      site-profile.md
```

要求：

- [ ] 通用 source tree 不被修改。
- [ ] `_generated/site-profile.md` 由结构化数据模板生成，不直接拼接任意未审查文本。
- [ ] `SKILL.md` 明确：先读通用工作流，再读 `_generated/site-profile.md`。
- [ ] 生成文件顶部记录 site id、profile revision、generated_at 和非秘密配置 hash。
- [ ] manifest 记录每个文件来源和 hash。
- [ ] 不在生成文件中写 secret。
- [ ] 环境 apply 使用 atomic staging/swap。
- [ ] 可选生成一个轻量 `site-environment` Skill 用于 doctor 和通用环境查询，但它不能替代每个 affected Skill 内的 overlay。

---

## 8. 通用 Skill 重构

### 8.1 `render-chinese-math-pdf`

当前中央版本已经有可移植的探测、编译、引用清理和 PDF QA 思路。v3 要求：

- [ ] 比较 CUHK/UNC ZIP 版本，提取仍有价值的差异。
- [ ] 通用 Skill 不含 CUHK/UNC 绝对路径、用户名、module 名或固定字体假设。
- [ ] 站点路径和模块命令只进入 Site Profile/local override。
- [ ] 保留引用、公式、表格和中文内容；不能通过删除内容解决编译失败。
- [ ] 运行时先读取 `_generated/site-profile.md`，再执行通用 probe。
- [ ] 支持 Pandoc + XeLaTeX、直接 XeLaTeX/LuaLaTeX、项目自带 render route。
- [ ] 完成状态必须包含 PDF 页数、文本提取、字体/视觉检查。
- [ ] 写作风格与文件渲染边界重新收敛：`writing-style/chinese-prose` 不应因为普通中文润色自动触发 PDF 执行。
- [ ] 从 App-facing `chinese-prose` aggregate 中移除 PDF 渲染器，或提供严格触发边界，避免表达层与文件执行层混合。

### 8.2 `slurm-workflows`

新增统一通用 Skill，吸收两个 ZIP 中的可复用部分：

- 正确 Slurm header；
- CPU/GPU/array 资源请求；
- `--time`、`--mem`、`--cpus-per-task`、`--gres`；
- job name、日志、环境加载、scratch 生命周期；
- `squeue`、`sacct`、`scontrol` 诊断；
- 资源估计、失败分类和重提交流程；
- 登录节点安全；
- partition routing 的通用算法；
- partition race 的通用执行与 loser cancellation 机制。

站点 profile 决定：

- 分区名称与优先级；
- QOS/account；
- GPU 类型和限制；
- 是否允许 partition race；
- race 可用的分区；
- 默认 walltime/memory；
- module、scratch 和日志规范。

禁止：

- [ ] 在通用 `SKILL.md` 硬编码 CUHK/UNC partition。
- [ ] 在站点不允许时擅自 race。
- [ ] race 时复用同一输出目录导致损坏。
- [ ] 两个 race 作业均启动后不取消 loser。
- [ ] 在登录节点运行重计算。

### 8.3 Server Baseline Profile

增加通用 CLI profile，例如：

```text
server-research-baseline
```

包含：

- `workflow-core` 对应的通用 Skill；
- `writing-style` 的纯表达 Skill；
- `research-writing` 的必要 repo/report 支持；
- `render-chinese-math-pdf`；
- `slurm-workflows`；
- `ai-skills-core` 仅在需要同步/维护时可选。

Site Profile 再通过 `skills.include/exclude` 调整，不复制完整 profile。

---

## 9. Environment Doctor

### 9.1 通用检查

- site detection 是否唯一；
- generic source、site profile 和 manifest revision 是否一致；
- local override 权限是否过宽；
- 安装文件是否 drift；
- secrets 是否意外出现在生成文件或日志中。

### 9.2 TeX/PDF 检查

- `latexmk`、`xelatex`、`lualatex`、`pandoc` 是否存在；
- `kpsewhich` 能否定位 TeX；
- profile/local override 路径是否真实；
- 推荐字体是否存在；
- 可写 TeX cache；
- 最小中文 + 数学 + citation fixture 是否可编译；
- `pdfinfo`、`pdftotext`、`pdffonts`、render preview 检查；
- 输出 PASS/WARN/FAIL 和准确证据。

### 9.3 Slurm 检查

- `sbatch`、`sinfo`、`squeue`、`scontrol` 是否存在；
- profile 中 partition/QOS 是否可见；
- 默认资源是否超过站点限制；
- GPU partition 是否有 GPU；
- race policy 是否一致；
- header 生成是否合法；
- 默认只做 read-only doctor；
- 只有显式 `--submit-smoke-job` 才提交极小作业，并要求用户确认。

### 9.4 验证时间

Site Profile 记录：

```yaml
verification:
  last_verified: 2026-07-13
  methods:
    - sinfo
    - scontrol
    - latex-smoke-test
```

超过可配置期限时 doctor 警告，不自动把旧配置当作当前事实。

---

## 10. Manifest、更新和回滚

环境安装 manifest 建议位置：

```text
~/.agents/.ai-skills-environment-manifest.json
```

至少记录：

```json
{
  "schema_version": 1,
  "site_id": "cuhk",
  "public_source": {"path": "...", "commit": "..."},
  "site_profile_source": {"path": "...", "revision": "..."},
  "local_override_sha256": "...",
  "installed_at": "...",
  "skills": [],
  "generated_files": [],
  "previous_snapshot": "..."
}
```

要求：

- [ ] 不记录 local override 明文。
- [ ] 更新只管理 manifest 中列出的文件。
- [ ] 支持 `plan`、`dry-run`、`diff` 和 rollback。
- [ ] 同一输入连续 apply 结果完全一致。
- [ ] 任一验证失败，不替换当前安装。
- [ ] 两台机器共享 generic source 更新，但各自保持 site/local 差异。

---

## 11. Notion 后续整合准备

v3 不需要猜测未来 Notion 页面内容，但必须使后续流程可执行。

### 11.1 Intake Contract

为 Codex/Notion 连接器提供标准 intake manifest：

```yaml
source_type: notion
source_title: ""
source_id: ""
source_url: ""
last_edited_time: ""
read_at: ""
permission_basis: "user-owned | licensed | reference-only | unknown"
intended_targets: []
decision: pending
```

### 11.2 流程

```text
读取页面和必要子页面
→ 记录 revision/权限
→ 与现有 Skill 做重复与冲突分析
→ merge / merge-selected / reference-only / project-local / reject
→ 更新目标 Skill 与测试
→ 追加一行 Integration History
→ 删除临时页面正文/export
```

- [ ] 不在公开仓库保留私有 Notion 正文。
- [ ] 不把别人的完整 Skill 原样复制后只改名字。
- [ ] 许可不清时只能提炼思想并独立表达。
- [ ] 每次再次读取更新后的页面都新增 history event，不修改旧事实。
- [ ] 后续 Notion 批次不得破坏 v3 环境 profile 和插件边界。

---

## 12. README 和运维文档

README 必须增加“服务器环境 Overlay”章节，并清楚区分：

### 12.1 所有主力 Codex 环境

```text
workflow-core
writing-style
```

### 12.2 主力科研环境

```text
research-writing
statistical-modeling
```

### 12.3 桌面 PPT 环境

```text
presentations
官方 Presentation/Slides
按需官方 LaTeX
```

### 12.4 前端环境

```text
web-development
官方 build-web-apps
```

### 12.5 CUHK/UNC 服务器

```text
server-research-baseline
+ current Site Profile
+ local override
+ 当前 repo-local Skills
```

说明：

- 不直接手工编辑 `~/.agents/skills`；
- 不在两台服务器各维护一份完整 Skill；
- 使用 `ai-skills environment sync` 同步通用更新；
- 使用 `doctor` 验证当前站点；
- 纯 compute node 不装 Codex Skill；只在登录/开发环境部署。

### 12.6 CardiacNexus

README 必须在 v3 完成时指向 CardiacNexus repo 的真实 `.agents/skills/`，不得再指向中央 export package。

### 12.7 文档文件

新增或更新：

```text
docs/ENVIRONMENT_PROFILES.md
docs/INSTALLATION.md
docs/CODEX_MARKETPLACE.md
docs/provenance/INTEGRATION_HISTORY.md
profiles/README.md
```

---

## 13. 测试要求

### 13.1 v2 Closure Tests

- 中央九插件精确列表；
- App-facing Skill 边界；
- CardiacNexus repo-local 真实迁移；
- 旧 presentation broad trigger 不再进入默认 profile/domain；
- CUHK 最小合法 payload；
- 完整 PPTX layout 集；
- Asteria/TRACE end-to-end；
- active Skill 图标覆盖和 contact sheet；
- provenance target/commit/frontmatter 验证。

### 13.2 ZIP Intake Tests

- 两个 ZIP 哈希固定；
- 顶层 Skill inventory 可重复；
- secret scanner；
- 通用/站点/本地分类；
- 不复制 ZIP 内旧 TODO；
- 合并后 ZIP 从 tracked root 删除；
- history 各有一行且 target/commit 可验证。

### 13.3 Environment Merge Tests

- 同一 generic source + CUHK profile 与 UNC profile 生成不同 site reference；
- generic Skill 文件除 generated overlay 外完全一致；
- site constraints 不能被项目/local override 放宽；
- local path override 生效且存在性验证；
- secret 不进入输出；
- ambiguous detection 失败；
- unknown site 要求显式选择；
- apply 幂等；
- sync 保留 site 差异；
- drift 可检测；
- rollback 成功；
- uninstall 只删除 manifest 管理内容。

### 13.4 TeX Tests

- mock discovery；
- direct XeLaTeX route；
- Pandoc route；
- CJK + math + citation fixture；
- missing font/package 的明确错误；
- page/text/font/render QA。

### 13.5 Slurm Tests

- header schema；
- partition priority；
- constraints；
- race allowed/forbidden；
- output isolation；
- loser cancellation plan；
- GPU/CPU/array 示例；
- mock `sinfo`/`scontrol` 解析；
- 默认 doctor 不提交作业。

### 13.6 CI

- Linux 单元测试；
- Windows Marketplace/path budget；
- 环境 overlay fixture 测试不能依赖真实 CUHK/UNC；
- 私有 profile 缺失时公共 CI 仍通过；
- 真实服务器 smoke test 作为手工/受控验证，不把内部信息输出到公开 Actions 日志。

---

## 14. 推荐执行顺序

### Phase 0：锁定事实

1. 读取当前 main、v2 TODO、实现 commit、README、profiles、registry、builder、tests。
2. 读取 CardiacNexus 当前 main 和 `AGENTS.md`。
3. 在临时目录审计两个服务器 ZIP。
4. 创建 `TODO_V2_COMPLETION_AUDIT.md` 初版。

### Phase 1：关闭 v2 阻断项

1. CardiacNexus 真正 repo-local 迁移。
2. 清理旧 presentation active triggers/profile 残留。
3. 完成官方兼容性审计。
4. 完成 CUHK payload/layout/e2e。
5. 完成图标 P0/App-facing 和 provenance audit。
6. 更新 profile/README。

### Phase 2：提炼服务器 ZIP

1. 比较通用写作 Skill，不覆盖新版本。
2. 合并 `render-chinese-math-pdf` 增量。
3. 建立统一 `slurm-workflows`。
4. 提取 CUHK/UNC site profile/local override 候选。
5. 记录 history，删除 ZIP。

### Phase 3：Environment CLI

1. Schema 和配置解析。
2. detect/plan/apply。
3. materialization/manifest/atomic update。
4. sync/diff/rollback/uninstall。
5. doctor。

### Phase 4：测试和文档

1. 单元/fixture/CI。
2. CUHK 和 UNC 登录环境真实 doctor。
3. README 和安装命令。
4. 最终 v2/v3 completion audit。

### Phase 5：真实部署

在两台服务器分别执行类似：

```bash
ai-skills environment init --site <cuhk-or-unc>
ai-skills environment plan --site <cuhk-or-unc>
ai-skills environment apply --site <cuhk-or-unc> --target user
ai-skills environment doctor --site current
```

后续公共 Skill 更新：

```bash
ai-skills environment sync --site current --dry-run
ai-skills environment sync --site current
ai-skills environment doctor --site current
```

命令细节可在实现中调整，但行为契约不能弱化。

---

## 15. 最终验收标准

只有全部满足，才能声明 v3 完成：

1. `TODO_V2_COMPLETION_AUDIT.md` 中所有阻断项为 PASS。
2. CardiacNexus 四个 Skill 已在 CardiacNexus repo 的 `.agents/skills/`，中央 export 已删除。
3. 旧 `pptx`/`scientific-slides` 不再与新 Presentation 默认路由冲突。
4. `research-presentations`、`business-presentations`、CUHK 双模板和 Asteria/TRACE e2e 真正可执行。
5. App-facing Skill 图标和 metadata 完整；icon audit 不再跳过缺失。
6. provenance audit 能验证 commit、target、frontmatter 和临时 intake；`pending` 不能冒充完成。
7. 两个服务器 ZIP 已审计、提炼、记录并从 root 删除。
8. 中央只维护一份 `render-chinese-math-pdf` 和一份 `slurm-workflows` 通用源。
9. CUHK/UNC 差异位于 Site Profile/local override，而不是复制完整 Skill。
10. `ai-skills environment detect/plan/apply/sync/diff/doctor/uninstall` 有实现、测试和文档。
11. 两台服务器都能同步通用 Skill 更新，同时保持各自站点配置。
12. Local override/secret 不进入 Git、manifest 明文、history 或日志。
13. TeX 和 Slurm doctor 在 fixture 中通过，并在真实服务器完成受控验证。
14. README 清楚写明全局、科研、PPT、前端、领域、服务器和项目 repo-local 的安装组合。
15. Marketplace build、path budget、无 symlink、determinism、registry、catalog、provenance、icons、tests 和 CI 全部通过。
