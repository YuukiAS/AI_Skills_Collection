# Design Assurance 与 Delivery Assurance 插件 0.1：设计记录

## 工作边界

- 仓库：`YuukiAS/AI_Skills_Collection`
- 分支：`design/assurance-plugins-0.1-pro-b`
- 允许写入：`docs/design/assurance/plugin-0.1-pro-b/`
- 身份：D3 独立设计者 B
- 没有读取任何 `design/assurance-plugins-0.1-pro-*` 其他设计者分支，没有切换到 `main`，没有合并或建立 PR。
- 公开仓库产物只使用公开流程、仓库名、分支和路径；没有写入私有项目正文、数据、账号、凭据或私有证据。

写入探针 `WRITE_PROBE.md` 已在正式设计前成功创建。正式交付提交将同时写入四个产物并删除探针；远端回读用于确认清理结果。

## 实际读取的仓库材料

### AI_Skills_Collection

读取基线提交：`80f2c10d95418bdc239f18d3c52dbcb72199f2c1`，目标分支 `design/assurance-plugins-0.1-pro-b`。

- `docs/design/assurance/ASSURANCE_PROCESS_V0_1_20261110.md`：完整流程 0.1，作为角色、负责人、档次、冻结合同、修订、验收器和打包的唯一流程依据。
- `docs/design/assurance/ASSURANCE_PROCESS_V6_20261110.svg`：读取 SVG 源以核对角色和连线；同时确认同目录 PNG 文件存在。当前连接器没有把 PNG 作为可放大光栅图交给本轮设计，因此没有声称对 PNG 像素或视觉排版做过验收；流程语义仍以 Markdown 为准。
- `docs/plugin-todos/design-assurance.md`
- `docs/plugin-todos/delivery-assurance.md`
- `docs/plugin-todos/assurance-sources-20261109.md`
- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `plugins/codex/plugins/workflow-core/.codex-plugin/plugin.json`
- `plugins/codex/plugins/workflow-core/skills/workflow/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`
- `skills/writing/core/response-clarity/SKILL.md`
- `scripts/codex_marketplace_config.json`
- `scripts/build_codex_marketplace.py` 的仓库检索片段，用于确认 Marketplace 配置是生成源之一。

用户要求中的“`skills/` 下两个现有插件或技能”没有唯一指定对象。本轮选择了一个通用工作流源技能、一个仓库维护源技能和一个较小的写作技能，分别观察复杂流程、维护闭环和普通 `SKILL.md` 结构；没有把生成目录当成权威源。

### 反降级研究

读取提交：`5350cce73614a2ed36076f3f3001c561dc5ae817`，分支 `research/delivery-anti-degradation-20261109`。

- `YuukiAS/AI_Research_Toolkit`
- `docs/research/delivery-anti-degradation-20261109/REPORT.md`

采用的主要结论是：冻结完成语义而不是锁死每个测试脚本；验收器用正例、坏例、缺证据例校准；证据绑定当前最终候选；隐藏用例必须有真实权限边界；X1 是唯一交付签发者。

### Asteria Blueprint

读取提交：`307fc8e1b41eb9f2751aa5f4482377aa82ddaa62`，分支 `draft/blueprint-round7-20261107`。

- `docs/planner-guide.md`
- `docs/content-model.md`
- `content/blueprint.schema.json`
- `content/schema.ts`
- `content/template.json`

没有读取任何 `test/` 开头的分支。`blueprint.json` 按 v3 的需求、节点、连接、证据、四环境走查、系统失败和版本快照结构编写；每个叶节点落到具体设计或开放问题，没有把未实现内容标成真实实现。

## 外部原始资料

查阅日期：2026-11-10。

- OpenAI 插件构建：`https://developers.openai.com/plugins/build/plugins`
- OpenAI 技能构建：`https://developers.openai.com/plugins/build/skills`
- OpenAI API 插件指南：`https://platform.openai.com/docs/guides/plugins`
- Anthropic Agent Skills 概览：`https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview`
- Anthropic 托管代理技能：`https://platform.claude.com/docs/en/managed-agents/skills`

这些资料支持便携插件、`SKILL.md` 和 Claude 技能发现的格式判断；它们没有证明 GPT Work 会自动扫描任意 GitHub `skills/` 目录。因此 0.1 只把“给出固定提交和精确路径后完整读取”作为可交付路线，自动发现保留为开放问题。

## 路径与结构发现

- 用户列出的主要路径均存在，没有需要替换的材料路径。
- 当前仓库的权威编辑顺序是：先改 `skills/` 与 `scripts/codex_marketplace_config.json`，再生成 `plugins/codex/plugins/`；生成目录不能手改。
- 现有 Codex 生成插件使用 `.codex-plugin/plugin.json`。OpenAI 便携插件资料描述的网页端包采用根 `plugin.json` 与 `skills/`；本设计把二者分为当前 Codex 生成层与未来 ChatGPT 网页端适配，不宣称格式已经统一。
- 当前 `marketplacePluginBudget` 为 10，现有顶级插件也正好有 10 个。两个新插件的源设计可以完成，但公开 Marketplace 入口需要 D1 和用户决定容量；详见 `QUESTIONS.md`。

## 已做的本地产物检查

本轮没有目标仓库终端，因此没有运行仓库脚本、Asteria 官方检查器、`pytest`、构建器、安装器或任何验收器，也没有把设计阶段的命令字段冒充实际输出。

对本地生成的四个交付文件只做了以下无副作用检查：

- `blueprint.json` 可以由标准 JSON 解析器读取；
- 需求、节点、连接、端口、证据、关卡和失败路径的编号无重复；
- 需求路线、连接两端、端口、证据引用、失败路径与验收器引用均能在当前文件中解析；
- 顶层当前设计与版本快照内容一致；
- `SPEC.md` 覆盖用户要求的十项设计、D1–D8 与 X1–X5 全角色卡；
- `QUESTIONS.md` 只保留会改变产品入口、打包或 D5 实现的决定。

这些检查只能证明文件可解析和内部引用基本一致，不能替代 D5–D8、正式 Capability Gate、真实安装或正常入口试跑。

## 仍然不确定的判断

1. 两个新插件如何在已用满的 Marketplace 预算下公开发布。
2. 两个插件能否安全复用同名规划技能，还是需要两个薄入口。
3. Asteria Blueprint 检查器应作为固定依赖还是选择性移植。
4. GPT Work 是否存在本轮未能核实的自动技能发现或上传入口。

以上问题都集中在 `QUESTIONS.md`。它们不影响状态、调度、角色、冻结合同、验收治理和证据格式的设计完整性，但第 1 项会阻塞正式 Marketplace 上架，第 3 项会阻塞 D5 的正式可用声明。

## 本轮未做的仓库维护动作

本任务只允许写产出目录，因此没有更新插件 TODO、README、版本、变更记录、Marketplace 配置、维护看板或 tracking Issue。正式实现进入 AI_Skills 维护范围时，D1/X1 应按仓库现行规则绑定或复用真实 tracking Issue，并记录 `tracking: #N`；本轮没有凭空编造编号，也没有声称看板已同步。
