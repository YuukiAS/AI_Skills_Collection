# 独立设计 A：来源、核查与边界

本轮已经完成指定分支的真实写入测试，并完整读取用户认可的流程 0.1。当前工作是 D2 的独立候选设计；它不构成 D1 汇总、D5–D8 通过、用户批准冻结或插件已实现。本文件随规格完善继续更新。

## 工作边界与写入事实

- 唯一远端写入位置：`YuukiAS/AI_Skills_Collection`，分支 `design/assurance-plugins-0.1-pro-a`，目录 `docs/design/assurance/plugin-0.1-pro-a/`。
- 写入探针提交：`c1054e2976fdc5e447820cec1ff289f9826762d1`。已从同一分支回读 `WRITE_PROBE.md`，正文为用户指定的 `GPT Pro write probe passed.`。
- 所有本轮源资料以该分支的读取快照为准。没有切换或写入 `main`，没有读取另一位本轮设计者的分支，没有合并或创建 PR。
- 两个外部仓库只读；没有读取任何 `test/` 开头的分支。私有来源在公开产物中仅保留仓库、分支和路径，不复制其项目数据、代码或具体案例。
- 使用了本地终端读取材料和查看已有流程图。没有运行插件、项目产品、Blueprint 官方检查器、冻结命令或真实安装验收。任何后续实际执行的文件级诊断将在本文件单独记录。

## 当前依据

唯一流程语义依据是 [流程 0.1](../ASSURANCE_PROCESS_V0_1_20261110.md)。已完整读取正文，并查看对应的 `ASSURANCE_PROCESS_V6_20261110.png`，核对 D1/X1 两个负责人、独立设计、四个冻结关卡、验收提案和返修线路。图像辅助理解，出现歧义以正文为准。

已读取本分支的两份插件 TODO 与来源索引中有关验收器归属、历史冻结和实际运行边界的条目。索引是定位资料，不是本轮逐项复测报告；没有重新打开全部历史分支。旧材料与当前流程冲突的地方，以当前流程为准，尤其不继承旧的交付负责人、接口版本或历史通过结论。

已读取 `AGENTS.md`、两份角色合同、能力关卡政策和维护看板规则。当前用户明确将本轮绑定为 D2，并把流程 0.1 指定为唯一依据，因此不在本轮另开旧 Planner–Critic 流程，不代替后续 D1 汇总与冻结。仓库既有维护、真实证据、生成物不可手改等要求仍作为后续实施约束。本轮限定目录之外的 TODO、Issue、看板、README、插件和配置均未修改。

| 来源 | 分支 | 已读取内容及用途 |
|---|---|---|
| `YuukiAS/AI_Skills_Collection` | `design/assurance-plugins-0.1-pro-a` | `docs/design/assurance/ASSURANCE_PROCESS_V0_1_20261110.md` 与对应流程图：唯一流程依据 |
| 同上 | 同上 | `docs/plugin-todos/design-assurance.md`、`docs/plugin-todos/delivery-assurance.md`、`docs/plugin-todos/assurance-sources-20261109.md`：历史差异与来源索引 |
| 同上 | 同上 | `AGENTS.md`、`docs/workflows/PLANNER_ROLE_CONTRACT.md`、`docs/workflows/CRITIC_ROLE_CONTRACT.md`、`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`、`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`：维护与阶段边界 |
| 同上 | 同上 | `plugins/codex/plugins/workflow-core/`、`skills/core/codex-system/codex-workflow-protocol/SKILL.md`、`skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`：现有技能及生成插件结构 |
| 同上 | 同上 | `skills/README.md`、`scripts/codex_marketplace_config.json`、`scripts/build_codex_marketplace.py`、`docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`：源码归属、生成机制、现有容量和版本规则 |
| `YuukiAS/AI_Research_Toolkit` | `research/delivery-anti-degradation-20261109` | `docs/research/delivery-anti-degradation-20261109/REPORT.md`：反降级依据；被流程 0.1 改定的负责人和强制角色以新流程为准 |
| `YuukiAS/Asteria-Blueprint` | `draft/blueprint-round7-20261107` | `docs/planner-guide.md`、`docs/content-model.md`、`content/blueprint.schema.json`、`content/template.json`：结构、起稿、终点、验收与版本格式 |
| 同上 | 同上 | `content/schema.ts`、`content/validation.ts`、`content/check.mjs`、`content/freeze.mjs`、`content/round7.ts`、`content/readability.ts`、`content/package.json`：确认检查器边界与通用适配缺口 |

资料核查助手只承担本设计 A 内部的来源核实；它们不是另一位独立设计者、正式冻结关卡或批准者。

## 平台原始资料

查阅日期均为 2026-11-10。外部资料用于核实文件格式与分发边界，不证明本轮插件已安装或实际运行。

1. Anthropic，[Extend Claude with skills](https://code.claude.com/docs/en/skills)：`SKILL.md`、YAML 元信息、支持文件及新上下文能力。上下文独立不等于文件权限隔离。
2. OpenAI，[Build skills](https://developers.openai.com/plugins/build/skills)：技能目录和支持资源；用同一正文复用规划规则，不推导自动选择模型或自动新建网页线程。
3. OpenAI，[Package your plugin](https://developers.openai.com/plugins/build/plugins)：现有 `.codex-plugin/plugin.json` 布局仍受支持；本轮建议复用仓库生成器。
4. OpenAI，[Plugin submission errors](https://developers.openai.com/plugins/deploy/submission-errors)：技能目录和普通文件要求，供后续网页端打包复核。

采用状态：上述平台文档为 `REFERENCE_ONLY`；现有仓库生成器建议成为后续实现的复用对象，本轮尚未接入。Blueprint 格式用于本候选，正式检查器适配仍须 D1 裁决。

## 已发现的兼容问题

Blueprint 起稿指南要求首次填写保留 `versions: []`，而完整结构定义要求存在冻结版本；本轮将保留未冻结草稿，不伪造历史。现有检查入口还绑定读者记录与特定项目的疑问位置，必须明确通用接入办法。验收运行结构目前没有“无法判断”，候选与证据记录必须独立保留第三态，不能用失败或通过冒充。

本仓库现有市场配置已用满 10 个插件和 30 个技能的预算。新增两个正式插件、各一个执行入口，需要 D1 收敛发布容量调整，不能挤掉旧功能或假装当前预算足够。

冻结后小修订如何继承旧批准，以及小修正文变化与读者记录的关系，将集中写入 `QUESTIONS.md`。已明确的角色、档次、验收器分级和返回条件不会重新设为未决。

## 维护跟踪待办

本轮用户只授权在指定设计目录写入，因此没有修改维护看板或对应 TODO 的跟踪字段。交回 D1 后，由有相应写入范围的维护线程查找并复用已有条目，将当前执行锚点指向本目录、进度保持设计进行中，下一步写为“比较两份独立候选并收敛，再进入冻结关卡”。不得把本轮候选交回记成插件完成，也不要求用户手工维护看板。

README checked: no update required。当前没有正式入口、名称、发布版本、安装方式或已实现能力变化；后续正式实施仍须按实际改动同步 README。
