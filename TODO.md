# TODO v3.1：关闭 v2 核心缺口，重构 Workflow Core，并建立服务器环境 Overlay

## 0. 本版结论

本文件替代上一版 `TODO v3`，作为下一轮 Codex 重构的根目录任务说明。

本版固定以下架构决定：

1. 中央 Codex Marketplace 继续保持 **9 个通用插件**，不新增 Slurm/PDF 插件。
2. `workflow-core` 继续保留，并建议作为主力 Codex 环境的全局基础插件；但必须重写为纯流程层，不再把 PDF、LaTeX、tmux、Slurm 等具体技术名称当作触发条件或操作规范。
3. `render-chinese-math-pdf` 与新的 `slurm-workflows` 是**独立可安装 Skill**，由服务器 profile 安装到用户级，不单独包装成 Marketplace 插件，因此不新增插件卡片和插件 SVG。
4. `writing-style` 只负责表达层；从 App-facing `chinese-prose` 中移除 `render-chinese-math-pdf`，避免文字润色自动进入文件编译流程。
5. CardiacNexus 导出包继续保留在当前仓库，供用户后续逐步 merge；可以修复包内问题，但未经用户明确确认不得删除。CardiacNexus 实际 merge 不再是 v3 的阻断项。
6. Notion 不需要专门建设一套复杂 intake CLI。允许用户让 Codex 在独立 thread 中读取 Notion 并直接修改仓库；仓库只保留最小的来源记录、许可检查和 history 规则。
7. `bundles/`、旧 installer、旧 profile 和旧 broad-trigger Skill 仍需做一次 legacy 审计；确认无活动依赖后进入受版本控制的 archive，而不是继续处于“声明 deprecated 但仍在主路径”的状态。
8. 两个服务器 ZIP 是临时迁移输入。v3 应从中提炼通用能力与站点差异，然后建立可同步的 Site Profile/Local Override 系统。

生成层继续只能由 builder 产生：

```text
.agents/plugins/marketplace.json
plugins/codex/plugins/
```

不得手工维护。

---

## 1. 中央 Marketplace：固定九个插件

目标插件：

| 插件 | 用户可见职责 | 默认安装建议 |
|---|---|---|
| `workflow-core` | 复杂任务的事实源、计划、门槛、验证、集成与诚实状态 | 所有主力 Codex 环境 |
| `ai-skills-core` | 本仓库 profile、registry、catalog、Marketplace 和维护 | 只在使用或维护本仓库的机器 |
| `writing-style` | 忠实改写、中文技术表达、局部科学表达 | 用户级全局 |
| `research-writing` | Repo 报告、论文、文献、引用和科研成果组织 | 主力科研环境 |
| `presentations` | `research-presentations` 与 `business-presentations` | 做 PPT/Slides 的桌面环境 |
| `web-development` | 前端参考、视觉系统、科研产品约束，补充官方 `build-web-apps` | 前端/研究产品环境 |
| `statistical-modeling` | 统计、贝叶斯、数据分析和科学可视化 | 主力科研环境 |
| `bioinformatics` | 生物信息学和组学工作流 | 按领域/项目 |
| `medical-imaging` | 医学影像、CMR、DICOM/NIfTI 与影像机器学习 | 按领域/项目 |

要求：

- [ ] Marketplace 配置和 README 都明确：9 是当前仓库策划预算，不是假定的 Codex 产品上限。
- [ ] `render-chinese-math-pdf` 与 `slurm-workflows` 不加入中央 Marketplace。
- [ ] CardiacNexus 不重新加入中央 Marketplace。
- [ ] 所有 App-facing Skill 保持唯一名称和清楚 trigger。

---

## 2. `workflow-core`：保留，但重写边界

### 2.1 为什么仍需要

`workflow-core` 解决的不是某个技术领域，而是 Codex 在复杂任务中的通用失误：

- 未先找到事实源就开始改；
- 把计划、启动、提交作业或生成第一版误报为完成；
- 子 Agent 结果未集成验证；
- 只跑 smoke test，不检查最终成果；
- 忽略 dirty tree、生成层、当前 live state 或验收标准；
- 遇到弱结果时直接停止或偷工减料。

这些约束跨 CARE、TRACE、CardiacNexus、论文、前端、服务器和插件维护均适用，因此应继续保持独立全局插件。

### 2.2 新触发边界

触发依据必须是**任务复杂度与风险**，而不是具体文件格式或工具名。

应触发：

- 多阶段实现；
- 跨文件/跨系统变更；
- 有明确验收门槛；
- 需要委派、长时间运行、发布、提交或 live-state 验证；
- 错误会造成数据、代码、科研结论或发布风险；
- 用户要求完整执行和证据，而非单次解释。

不应仅因用户提到以下词就触发：

```text
PDF, LaTeX, tmux, Slurm, GitHub, frontend, training
```

简单编译、简单排版、一个 Slurm header、一个 tmux 命令或普通文字润色，应直接路由到相应专门 Skill 或普通回答。

### 2.3 纯流程职责

`workflow-core` 只拥有：

1. 事实源发现；
2. 任务边界与已有工作保护；
3. 阶段计划和 acceptance gates；
4. Specialist Skill 路由；
5. 执行过程监督；
6. 集成、验证和最终状态；
7. 失败升级和需用户决定的边界。

它不拥有：

- TeX/Pandoc/字体/引用编译方法；
- Slurm header、partition、QOS 或 race 策略；
- tmux 的具体命令；
- PDF、PPTX、前端、统计或医学影像的领域 QA；
- 项目路径和项目 schema。

具体技术规则必须由 specialist Skill 提供。Workflow Core 只要求“找到并遵守 specialist Skill，并验证它定义的最终门槛”。

### 2.4 需要修改的文件

- [ ] 重写 `skills/core/codex-system/codex-workflow-protocol/SKILL.md` 的 description、trigger boundary 和示例。
- [ ] 将 `references/live-state-delegation.md` 中 Slurm/tmux/frontend 的具体检查迁入对应 specialist references；Workflow Core 只保留通用 live-state 原则。
- [ ] 检查 `verification-matrix.md`、`task-template.md`、`escalation-rules.md`，删除领域实现细节和过度绝对化要求。
- [ ] 增加 Specialist Routing Contract：流程层不能覆盖 specialist 的技术规则，specialist 不能弱化全局完成门槛。
- [ ] 增加 `agents/openai.yaml` 和 App-facing 图标元数据。
- [ ] 保持 `allow_implicit_invocation: true`，但只对真正复杂任务隐式触发。

### 2.5 路由测试

正例：

- “按照 TODO 完整重构仓库、测试并推送。”
- “执行一轮训练、监督到结束、比较结果并决定下一步。”
- “让多个 Agent 分工实现并由主 Agent 最终验收。”

负例：

- “给我一个 Slurm header。”
- “这个 tmux 命令是什么意思？”
- “把这段中文润色一下。”
- “编译这个已有 `.tex` 文件。”

组合例：

- 复杂 Slurm 项目：`workflow-core` 管阶段和验收，`slurm-workflows` 管资源与调度。
- 复杂 PDF 交付：`workflow-core` 管完成门槛，`render-chinese-math-pdf` 管编译与 PDF QA。

---

## 3. Writing、PDF 与服务器 Skill 边界

### 3.1 `writing-style`

App-facing 结构保持：

```text
writing-style
├── writing-fidelity
├── scientific-prose
└── chinese-prose
```

要求：

- [ ] 从 `chinese-prose` aggregate 中移除 `render-chinese-math-pdf`。
- [ ] 普通中文/科学表达任务不得因 PDF 渲染器的 `executes_code`、TeX 依赖或服务器规则而扩大上下文。
- [ ] `writing-style` 可以提出“需要渲染为 PDF”，但文件实现由官方 LaTeX/PDF 或独立 render Skill 完成。

### 3.2 `render-chinese-math-pdf`

长期位置：

```text
skills/tools/documents-media/render-chinese-math-pdf/
```

它是独立 source Skill，不是独立 Marketplace 插件。主要通过以下方式安装：

```text
server-research-baseline profile
CUHK/UNC Site Profile
精确 skill selector
```

通用职责：

- 中文/中英混排数学 Markdown/LaTeX 到 PDF；
- 引用清理和引用保真；
- Pandoc + XeLaTeX、直接 XeLaTeX/LuaLaTeX；
- 可写 TeX cache；
- 页数、文本提取、字体和渲染 QA；
- 失败时报告准确依赖。

站点路径、module、字体和 TeX Live 位置只由 Site Profile/Local Override 提供。

### 3.3 `slurm-workflows`

长期位置：

```text
skills/tools/hpc/slurm-workflows/
```

它也是独立 source Skill，不是 Marketplace 插件。

通用职责：

- Slurm header；
- CPU/GPU/job array；
- 资源估计；
- 日志与 scratch；
- `squeue`、`sacct`、`scontrol` 诊断；
- 失败分类和重提交流程；
- partition routing 的通用算法；
- race 的安全执行与 loser cancellation 机制。

站点 profile 决定：partition、优先级、QOS/account、GPU 类型、资源上限、race 是否允许、module、scratch 和日志规范。

### 3.4 为什么不创建 `research-computing` 插件

v3 不创建额外插件，原因：

- 两个能力主要发生在 SSH/HPC Codex CLI，而不是桌面 Marketplace 浏览；
- Site Profile 需要 CLI materialization，插件安装不能替代环境配置；
- `render` 与 Slurm 的 trigger 不相同，强行包装为一个 App-facing aggregate 反而扩大上下文；
- 不增加第十个插件卡片和额外插件 SVG。

未来只有在桌面 Codex App 对研究计算入口有明确高频需求时，再单独评估 `research-computing` 插件。

---

## 4. 两个服务器 ZIP 的提炼

当前输入：

```text
skills-CUHK.zip
skills-UNC.zip
```

它们是 legacy migration input，不是长期事实源。

### 4.1 安全与差异审计

- [ ] 在 `.tmp/skill-intake/server-zips/` 解压。
- [ ] 固定 SHA256、来源 commit 和读取日期。
- [ ] 扫描私钥、token、邮箱、用户名、绝对路径、account、QOS、hostname、内部 URL 和代理。
- [ ] 如发现秘密，停止并报告；需要清理历史时先取得用户批准。
- [ ] 比较两包中的 writing、render 和 Slurm Skill 与当前中央版本。
- [ ] 通用 Skill 只吸收真实增量，不能用服务器旧版本覆盖 v2 新版本。
- [ ] 旧 TODO、缓存、部署产物和重复文件不进入正式源层。

### 4.2 分类输出

每条差异必须归为：

```text
generic-skill
site-profile
local-override
obsolete-or-duplicate
secret-do-not-store
```

输出：

- 唯一中央 `render-chinese-math-pdf`；
- 唯一中央 `slurm-workflows`；
- CUHK Site Profile 候选；
- UNC Site Profile 候选；
- Local Override 模板；
- 本地差异报告；
- Integration History 各一行。

完成并验证后，可删除两个服务器 ZIP；与 CardiacNexus 导出包不同，服务器 ZIP 不承担长期人工 merge 作用。

---

## 5. Site Profile 与 Local Override

### 5.1 运行模型

```text
中央通用 Skill
+ 当前 Site Profile
+ 当前机器 Local Override
+ 当前项目 Repo-local Skill
→ materialize 到 ~/.agents/skills/
```

`~/.agents/skills/` 是部署层，不是源码层。

### 5.2 配置来源

Site Profile 可以来自：

1. 当前仓库中的 public-safe profile；
2. 私有 companion repo checkout；
3. 本地未跟踪目录。

Local Override 默认：

```text
~/.config/ai-skills/local-overrides.toml
```

Local Override 可以存个人路径、account、仅本机字体和私有 module 初始化；秘密不得进入 Git、生成 Skill、manifest 明文、history 或日志。

### 5.3 合并规则

字段分为：

```text
capabilities
constraints
policy
preferences
local_paths
secrets
```

规则：

- Site `constraints` 不能被项目或 local override 放宽；
- Site `policy` 权威，例如 race 是否允许；
- 项目只可在允许范围内调整 preferences；
- local path 可覆盖，但必须验证存在性和可执行性；
- 自动探测与配置冲突时必须报告 drift。

### 5.4 Materialization

部署后示例：

```text
~/.agents/skills/render-chinese-math-pdf/
  SKILL.md
  references/_generated/site-profile.md

~/.agents/skills/slurm-workflows/
  SKILL.md
  references/_generated/site-profile.md
```

要求：

- [ ] 不修改中央 source tree。
- [ ] `_generated/site-profile.md` 由 schema 数据生成，不拼接任意文本。
- [ ] 生成文件记录 site id、profile revision、时间和非秘密 hash。
- [ ] Skill 明确读取生成的站点 reference。
- [ ] staging 构建、验证后原子替换。
- [ ] manifest 只管理自己安装的文件。

---

## 6. `ai-skills environment` CLI

在现有 `ai-skills` CLI 中增加：

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

核心契约：

- `detect`：只读证据；多匹配报 ambiguous；无匹配要求显式 `--site`。
- `plan`：展示安装、更新、删除、source commit、site revision、override hash；不写磁盘。
- `apply`：copy/materialize；staging + atomic swap；失败保留旧安装。
- `sync`：更新通用 source 后重新注入当前站点配置；不混淆 CUHK 与 UNC。
- `diff`：比较 canonical source + site + override hash 与安装 manifest。
- `doctor`：验证 TeX、Slurm、profile、manifest 和 drift；默认只读。
- `uninstall`：只删除 manifest 管理的内容。

增加 profile：

```text
server-research-baseline
```

包含：

- `codex-workflow-protocol`；
- writing-style 三个纯表达 Skill；
- 必要的 research-reporting 支持；
- `render-chinese-math-pdf`；
- `slurm-workflows`；
- `ai-skills-core` 作为可选维护组件。

---

## 7. Environment Doctor

### TeX/PDF

检查：

- `latexmk`、`xelatex`、`lualatex`、`pandoc`、`kpsewhich`；
- profile/local path；
- 字体和 TeX cache；
- 中文 + 数学 + citation fixture；
- `pdfinfo`、`pdftotext`、`pdffonts` 和渲染预览。

### Slurm

检查：

- `sbatch`、`sinfo`、`squeue`、`scontrol`；
- partition/QOS 可见性；
- 默认资源是否超限；
- GPU partition；
- race policy；
- header 生成。

默认不提交作业。只有显式 `--submit-smoke-job` 且用户确认时才提交极小 smoke job。

---

## 8. CardiacNexus 导出包：保留并允许修复

当前包：

```text
exports/cardiacnexus-repo-local/
```

新规则：

- [ ] 保持 CardiacNexus 不出现在中央 Marketplace。
- [ ] 导出包继续作为 staging/handoff package 保留。
- [ ] 可以修复包内路径、frontmatter、README、AGENTS append 说明和自包含性问题。
- [ ] 不要求 v3 自动修改 CardiacNexus repo。
- [ ] 不要求 v3 删除导出包。
- [ ] README 明确：包内 Skill 最终应在用户逐步 merge 后，以 CardiacNexus repo-local 版本为 canonical source。
- [ ] `INTEGRATION_HISTORY.md` 将状态从模糊 `pending` 改为明确 `deferred-user-merge`。
- [ ] 用户完成 merge 并确认后，再单独决定是否删除中央导出包。

v3 验收只要求：中央插件不发布 CardiacNexus、导出包可用且不被误认为中央 canonical source。

---

## 9. Notion：保留最小治理，不建设强制 Intake 系统

用户可以直接让 Codex 在独立 thread 中：

1. 使用官方 Notion 连接器读取页面；
2. 比较当前仓库 Skill；
3. 决定 merge、merge-selected、reference-only、project-local 或 reject；
4. 修改目标 Skill 和测试；
5. 在 `INTEGRATION_HISTORY.md` 追加一行；
6. 删除临时正文/export。

v3 不再强制实现：

```text
Notion 专用 intake manifest
Notion dry-run/plan/apply CLI
复杂的 Notion 本地缓存体系
```

仓库只需要：

- [ ] `INTEGRATION_HISTORY.md` 可记录 source title、稳定 ID/URL、revision、permission、target 和 integration commit。
- [ ] 私有 Notion 正文不进入公开 repo/history。
- [ ] 直接采用或实质改写的内容更新目标 Skill provenance。
- [ ] 许可不清时只提炼思想并独立表达。
- [ ] `provenance_audit.py` 检查 history 行格式、target 存在性和明确状态。

当前 `external_source_intake.py`：

- 若 GitHub/本地来源仍有实际用途，可保留为可选 helper；
- 若没有调用者或测试价值，移动到 archive；
- 它不是 v3 完成条件。

---

## 10. Legacy 与 Archive 清理

当前 `bundles/` 和 `scripts/install_bundle.py` 仍在主路径；README 只把它们称为 legacy，不等于已经归档。

### 10.1 先做引用审计

检查：

- README/docs；
- tests/CI；
- setup/entry points；
- profiles；
- 用户级 manifest 兼容；
- 其他脚本调用。

### 10.2 目标归档结构

Skill 类 deprecated 内容：

```text
skills/archive/
```

非 Skill legacy 内容：

```text
archive/legacy-bundles/
archive/legacy-installers/
archive/legacy-profiles/
```

本地临时材料改放：

```text
.tmp/archive/
```

因此：

- [ ] 调整 `.gitignore`，允许受版本控制的根 `archive/`；本地临时 archive 使用 `.tmp/archive/`。
- [ ] 将 bundle JSON 移入 `archive/legacy-bundles/`。
- [ ] 将 bundle installer 的完整实现移入 `archive/legacy-installers/`。
- [ ] 顶层 `scripts/install_bundle.py` 可保留一个短期兼容 shim，只打印 deprecated 和等价 profile/domain 命令，不继续维护第二套安装逻辑。
- [ ] 旧 profile 若有用户价值，转换为新 profile；否则移入 `archive/legacy-profiles/`。
- [ ] 旧 `pptx` 和 `scientific-slides` 的有价值资料迁移后，移入 `skills/archive/` 并从 active registry/profile/domain 排除。
- [ ] Archive 不进入 Marketplace，不参与默认 registry，不被安装器默认扫描。

不得直接删除仍有兼容依赖的文件；先提供迁移说明和至少一轮 shim。

---

## 11. 仍需关闭的 v2 核心缺口

### Presentations

- [ ] 官方 Presentation/Slides 与 LaTeX compatibility 文档必须来自当前环境实测，而不是泛化描述。
- [ ] 完成 deck-plan schema、验证器、Markdown/Asteria/TRACE adapter 和 source anchors。
- [ ] 加入脱敏 fixture 和 end-to-end：Markdown → deck plan → editable PPTX → render → QA。
- [ ] CUHK PPTX reference deck覆盖 title、section、content、equation、process、figure、interpretation、comparison、table、references、closing、backup。
- [ ] CUHK payload 去掉 `.vscode`、无用 XCF、样例 Fig/Table 和不必要文件；品牌许可不清时使用本地 importer。

### 图标

- [ ] 中央九插件和所有 App-facing Skill 有完整 metadata/icon。
- [ ] `icon_audit.py` 不再静默跳过缺失 App-facing 资产。
- [ ] 实现 contact sheet。
- [ ] 全部 149 个 active source Skill 的图标覆盖可作为后续 P1；v3 阻断范围先固定为中央插件与 App-facing Skill，避免环境系统被大规模装饰性工作阻塞。

### Profiles/README

建立并说明：

```text
global-baseline
research-main
presentation-desktop
frontend-research-product
medical-imaging-project
bioinformatics-project
server-research-baseline
ai-skills-maintainer
```

旧 profile 要么迁移，要么 archive；`codex-cardiacnexus` 只能是通用支持 profile，不能复制项目专用 Skill。

### v2 Closure Report

创建：

```text
docs/audits/TODO_V2_COMPLETION_AUDIT.md
```

状态：

```text
PASS | PARTIAL | FAIL | DEFERRED_USER_ACTION | NOT_APPLICABLE
```

CardiacNexus 实际 merge 使用 `DEFERRED_USER_ACTION`，不阻断 v3。

---

## 12. 测试

### Workflow Core

- 复杂任务触发；
- 简单 PDF/Slurm/tmux/润色任务不触发；
- 与 specialist Skill 组合时职责清楚；
- specialist 不能弱化完成门槛；
- Workflow Core 不包含站点路径、partition 或编译命令。

### ZIP/Environment

- 两个 ZIP inventory 和 secret scan；
- generic/site/local 分类；
- CUHK 与 UNC 生成不同 overlay；
- constraints 不能被放宽；
- secret 不进入输出；
- detect ambiguous/unknown 失败；
- apply 幂等、atomic、可回滚；
- sync 保留站点差异；
- doctor 默认不提交 Slurm 作业。

### Marketplace/Archive

- 中央九插件精确列表；
- render/slurm 不作为插件；
- writing-style 不再 aggregate render；
- CardiacNexus 不在中央 Marketplace且导出包仍存在；
- archived skills/bundles 不进入 registry、profile 和 generated layer；
- compatibility shim 给出有效迁移指令。

### Presentation/Provenance

- 两种 presentation route；
- 小编辑负例；
- CUHK layout 和 e2e；
- history target/status 验证；
- Notion 不需要专用 CLI 测试，只测试最小 history/provenance 规则。

---

## 13. 推荐执行顺序

### Phase 0：事实审计

1. 创建 v2 closure audit。
2. 审计 Workflow Core 及 references。
3. 审计 bundles、legacy installer、旧 profiles、旧 PPTX/scientific-slides。
4. 在临时目录审计两个服务器 ZIP。

### Phase 1：边界清理

1. 重写 Workflow Core。
2. 从 writing-style 中移除 render。
3. archive 旧 presentation 和 legacy 安装路径。
4. 更新 profiles、README、registry 和 tests。
5. CardiacNexus 导出包只修复，不迁移、不删除。

### Phase 2：服务器 Skill 与 Overlay

1. 合并 render 增量。
2. 创建 `slurm-workflows`。
3. 建立 Site Profile schema 与 public/private 示例。
4. 实现 environment CLI、materialization、manifest 和 doctor。
5. 在 CUHK/UNC 真实登录环境验证。

### Phase 3：v2 其他核心收尾

1. Presentation compatibility、adapter、CUHK layouts 和 e2e。
2. App-facing icon metadata/contact sheet。
3. 最小 provenance audit。
4. Marketplace/Windows/path/CI。

Notion 页面整合不需要等待 v3：用户可随时在独立 Codex thread 中按最小来源规则执行。

---

## 14. 最终验收

只有满足以下条件，才可声明 v3 完成：

1. 中央 Marketplace 仍为九个通用插件。
2. Workflow Core 仍存在，但已成为纯流程层，不与 PDF/LaTeX/tmux/Slurm specialist 冲突。
3. `render-chinese-math-pdf` 与 `slurm-workflows` 作为独立服务器 Skill，由 profile/overlay 安装，不是插件。
4. writing-style 不再隐式携带 PDF 编译器。
5. 两个服务器 ZIP 已审计、提炼、记录并从根目录移除。
6. Site Profile、Local Override、environment CLI、manifest、sync、diff、doctor、rollback 有实现和测试。
7. CUHK/UNC 能共享通用 Skill 更新并保持站点差异。
8. CardiacNexus 不在中央 Marketplace；导出包保留且可修复，删除时间由用户 merge 后决定。
9. Notion 没有强制专用 intake 架构，但最小 provenance/history 规则可执行。
10. bundles、旧 installer、旧 broad-trigger Skill 和旧 profiles 已经迁移或进入受版本控制 archive，并有兼容说明。
11. Presentation 核心 e2e、CUHK 可编辑模板和 App-facing 图标达到 v3 定义的阻断范围。
12. README 清楚写明插件安装、服务器 profile、项目 repo-local 和官方插件协作。
13. Marketplace build、path budget、无 symlink、determinism、registry、catalog、provenance、tests 和 CI 通过。
