# TODO v3.5.1：收口 Notion intake、安装体验与 AI Skills Core

## 当前判断

`v3.5.0` 的总体架构与合并方向正确：领域内容进入对应 source skill，中央 Marketplace 保持 9 个插件，官方工具继续负责实际文件、Figma、Notion、GitHub、Presentation/Slides 等执行层。本轮不应推翻现有结构，而应补齐 intake 闭环、CLI onboarding、本地配置引导和维护 SOP。

## P0：完成 AI Resources intake 闭环

- [ ] 建立逐项 intake 状态表，覆盖 Notion `AI Resources` 中全部 14 个 `Type != Research` 页面。每项至少记录：Notion 页面、类型、可读取证据、公开来源核验、处理决定、目标 skill/reference、实际 integration commit、是否允许将 `Utilized` 设为 true。
- [ ] 使用明确状态，而不是统一写成 `merge-selected`：`merged`、`partially-merged`、`reference-only`、`reviewed-not-adopted`、`unresolved-asset`、`rejected`。
- [ ] 在 `skills/tools/frontend/frontend-reference-research/references/2026-ai-frontend-resources.md` 中显式补记 `2026最强AI组合之一：Codex + Figma`，说明可复用的 Figma-to-code handoff 原则、官方 Figma 工具边界和不可复制内容。
- [ ] 重新核对两个证据不足的页面：
  - `常用生信分析流程Skill` 当前主要是“需付费”截图，若无法获得足够可验证内容，应记为 `reviewed-not-adopted`，不要把它与 GWAS 数据库页面一起笼统视为已合并。
  - `这些 PPT skill 你们都用过吗` 主要依赖图片；确认两张本地截图实际提供了哪些可复用结论，并将证据范围写入 provenance。
- [ ] `docs/provenance/INTEGRATION_HISTORY.md` 保持 append-only；新增 closure 行，将 `pending-v3.5` 与 `pending-v3.5-followup` 对应到实际提交 `299017f95e07bb7bc86907b32a47530edc3633c3` 和 `90504f1487b2e09972e0ec98d644867968f516eb`，并纠正“2 个 Bioinformatics 页面均已 merge-selected”的过度概括。
- [ ] 只有在“内容决定已记录、source layer 已更新、生成层已重建、验证通过、提交已存在”后，才通过 Notion connector 或人工把对应页面的 `Utilized` 改为 true。当前 14 项不应继续长期全部为 false，也不应未经逐项核对后一次性全部设为 true。

## P0：把 AI Skills Core 固化为维护控制面

- [ ] 扩展 `ai-skills-repository-maintainer`，加入正式的 `Notion/GitHub intake -> source skill -> provenance -> generated layer -> validation -> commit -> Notion reconciliation` 工作流。
- [ ] 明确该 skill 只负责仓库维护控制面，不负责判断前端设计、生物信息、PPT、统计或医学影像内容本身。内容判断必须同时调用相应领域插件或官方工具。
- [ ] 建议的 intake 顺序：
  1. 读取 Notion 数据库 schema，并查询目标页面集合；
  2. 读取文本、图片和附件，明确哪些证据实际可访问；
  3. 对公共项目、产品行为、许可和版本使用官方或原始来源核验；
  4. 判断应更新现有 skill、增加 reference、创建新 skill，还是不采纳；
  5. 先改 `skills/`、`profiles/`、provenance 和测试，再重建 registry/catalog/marketplace；
  6. 运行完整验证；
  7. 提交后再同步 Notion `Utilized`。
- [ ] 保持 `allow_implicit_invocation: false`。维护中央仓库时应显式调用 AI Skills Core；普通科研、写作或工程任务不应触发它。
- [ ] 更新 `project-skill-installer`：示例优先使用 v3.5 profile 名称，例如 `research-main`、`frontend-research-product`、`medical-imaging-project`、`bioinformatics-project`、`ai-skills-maintainer`；旧 `codex-*` 名称仅作为兼容说明。

## P1：降低 Codex App 与 CLI 的首次安装成本

- [ ] 在根 `README.md` 顶部增加“二选一快速开始”：
  - Codex App / Codex CLI 插件市场：添加 Git marketplace，安装所需插件，安装或升级后启动新会话；
  - source CLI / repo-local profile：clone、editable install、选择 profile、写入 `.agents/skills/` 和 `AGENTS.md`。
- [ ] 将 `docs/INSTALLATION.md` 中的 `git clone <repo-url>` 改为可直接复制的真实仓库地址，并提供 Linux/macOS、PowerShell、WSL 三个最小命令块。
- [ ] 文档补充 marketplace 刷新命令：`codex plugin marketplace list`、`codex plugin marketplace upgrade`，并说明插件更新后需要重新开始会话才能稳定加载新技能。
- [ ] 决定并记录版本策略：当前插件版本是 `3.5.0`，而 `setup.py` 中 CLI package 版本是 `0.1.0`。可以独立版本化，但必须在 README 中解释；否则将 CLI 版本与仓库 release 对齐。
- [ ] 评估是否增加现代 `pyproject.toml` 与 `pipx`/`uv tool` 安装方式。继续支持 editable install，因为 symlink 模式依赖长期存在的 source checkout。

## P1：补齐本地服务器配置模板和引导 Prompt

- [ ] 扩充 `site-profiles/local-overrides.example.toml`：为每个字段写明用途、是否必填、示例格式、优先级和禁止提交的敏感信息；区分 account、partition、QOS、scratch、module init、TeX/Python 路径等概念。
- [ ] 增加 `docs/LOCAL_CONFIGURATION.md`，解释 public site profile 与 private local override 的合并边界，以及 `init -> plan -> doctor -> apply -> diff -> sync/uninstall` 的完整流程。
- [ ] 改进 `ai-skills environment init`：允许 `--site` 只生成目标站点段落；默认不覆盖已有文件；输出下一步命令。
- [ ] 改进 `environment doctor`：不仅检查文件与命令是否存在，还要报告空字段、未知字段、路径不可访问、站点不匹配、可能缺失的 account/QOS/module 配置。仍然不得自动提交 Slurm 作业。
- [ ] 在文档中提供可复制给 Codex 的配置 Prompt，至少包含以下约束：

```text
请为当前机器配置 AI_Skills_Collection 的本地环境 overlay。先读取 README、目标 site profile、local-overrides.example.toml 和 docs/LOCAL_CONFIGURATION.md；运行 environment detect/plan，只询问无法从机器安全检测出的 account、QOS、partition、scratch、module 和私有路径。不得猜测或提交任何账号、主机名、token、私有路径。先生成或更新 ~/.config/ai-skills/local-overrides.toml，再运行 doctor 和 dry-run；只有在我确认计划后才执行 apply。最后报告安装位置、实际使用的 site、仍缺失的字段和回滚命令。
```

## P1：增加发布与安装烟雾测试

- [ ] 在 CI 中增加 Linux 与 Windows 的 editable-install smoke test：创建隔离环境，安装本仓库，运行 `ai-skills --help`、`ai-skills list` 和一个 `install --dry-run`。
- [ ] 为 `environment init`、空/非法 local override、未知字段、站点不匹配和 doctor 输出增加单元测试。
- [ ] 保留现有 Marketplace build、Windows sparse checkout、9-plugin budget、profile、CUHK template 和 update-manifest 测试。
- [ ] 增加 intake consistency 检查：provenance 中不得长期保留已发布版本对应的 `pending-*` 而没有 closure 行；逐项 intake 状态必须能映射到现有 source path 或明确的不采纳决定。
- [ ] 确认 GitHub Actions 在最新 `main` 提交上实际运行并可见；若连接器或仓库设置导致 status 不可见，在 README 标明本地完整 gate 是发布前的事实依据。

## P2：元数据与命名清理

- [ ] 更新 `figma-design-to-code` 的 `last_reviewed` 和 provenance，反映 2026-07-13 的实际整合；不要保留 `provenance: unknown` 而同时宣称已经完成来源审查。
- [ ] 将测试名 `test_v31_profiles_exist_and_server_profile_carries_overlay_skills` 改为当前版本语义，避免 v3.1/v3.5 混淆。
- [ ] 检查 README、profile 示例、插件 default prompt 与生成层是否仍引用已迁移或仅兼容的旧名称。

## 完成标准

- 14 个 Notion 非 Research 页面均有逐项可审计决定，Notion `Utilized` 与仓库事实一致。
- AI Skills Core 能作为显式维护入口完成一次端到端 intake，但不会替代领域插件或官方工具。
- 新机器可根据 README 在 Codex App/CLI Marketplace 或 source CLI 两条路径中任选一条完成安装。
- 本地 overlay 不需要用户自行猜测 TOML 字段；doctor 能指出缺失与错误配置。
- Linux、Windows、Marketplace、profile、provenance、registry/catalog 和单元测试完整通过。
