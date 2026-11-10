# 独立设计 A：来源、实际核查与不确定性

本轮已在指定分支写入完整D2候选：`blueprint.json`、`SPEC.md`、`QUESTIONS.md`及本文件。写入探针已成功回读并删除。候选的职责、字段、模板、失败处理与打包方案已经展开，但三个需要负责人收敛的问题仍保持开放；本轮不构成D1汇总、D5–D8通过、用户批准冻结或插件实现完成。

## 工作边界与真实写入

唯一远端写入位置是 `YuukiAS/AI_Skills_Collection`，分支 `design/assurance-plugins-0.1-pro-a`，目录 `docs/design/assurance/plugin-0.1-pro-a/`。没有切到或写入 `main`，没有读取本轮另一位独立设计者的分支、产物或摘要，没有合并或创建PR。两个外部仓库只读，没有读取任何 `test/` 开头的分支。公开产物只保留私有来源的仓库、分支和路径，不复制其项目数据、代码或具体实验内容。

写入测试提交为 `c1054e2976fdc5e447820cec1ff289f9826762d1`，从同一分支回读的探针正文严格为 `GPT Pro write probe passed.`。结束前再次核对原内容，再于提交 `44c72249a5b5b2e8c743205a356054e4980721be` 删除；随后读取同路径得到不存在，确认没有留下探针。

本轮使用了本地终端整理文件、查看已有流程图，并实际执行了下述普通文件诊断。没有运行新增插件、项目产品、Blueprint官方检查器、冻结命令、真实安装验收或正式D5–D8。资料助手只为设计A核实来源和检查文件；它们不是另一位独立设计者、冻结关卡或批准者。

所有用户指定的必读路径均在允许分支中找到，不需要用其他分支或替代材料补齐。额外按真实依赖读取了检查器、生成器及技能元信息说明；具体范围如下。

## 已读取材料及用途

唯一流程语义依据是[流程0.1](../ASSURANCE_PROCESS_V0_1_20261110.md)。正文已完整读取；对应的 `ASSURANCE_PROCESS_V6_20261110.png` 已实际查看，用于核对两位负责人、独立设计、四个冻结关卡及交付返修连线。PNG足以辨认角色与连线，没有以SVG内容另行推定流程规则；图与正文冲突时以正文为准。

| 仓库与分支 | 实际读取范围 | 对本候选的作用 |
|---|---|---|
| `YuukiAS/AI_Skills_Collection`，`design/assurance-plugins-0.1-pro-a` | `docs/design/assurance/ASSURANCE_PROCESS_V0_1_20261110.md`、`ASSURANCE_PROCESS_V6_20261110.png` | 角色、档次、必跑条件、冻结、验收分级、告知、退回和本轮位置 |
| 同上 | `docs/plugin-todos/design-assurance.md`、`docs/plugin-todos/delivery-assurance.md`；`docs/plugin-todos/assurance-sources-20261109.md`中与验收器归属、历史冻结、试跑定位及真实运行边界有关的条目 | 追溯历史差异；没有重新打开索引中的全部历史分支 |
| 同上 | `AGENTS.md`、`docs/workflows/PLANNER_ROLE_CONTRACT.md`、`docs/workflows/CRITIC_ROLE_CONTRACT.md`、`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`；`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`中责任、状态和维护范围规则 | 确认仓库维护与能力证据要求；不在本轮重新叠加旧角色流程 |
| 同上 | `plugins/codex/plugins/workflow-core/.codex-plugin/plugin.json`、其中实际技能；`skills/core/codex-system/codex-workflow-protocol/SKILL.md`、`skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md`、`skills/README.md` | 核对源技能、生成插件和既有维护职责 |
| 同上 | `scripts/codex_marketplace_config.json`、`scripts/build_codex_marketplace.py`、`docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md` | 核对共用资源复制、执行技能名称、两段版本及现有10插件/30技能容量 |
| 同上 | `skills/core/codex-system/system-skills/skill-creator/references/openai_yaml.md` | 确认 `policy.allow_implicit_invocation` 和默认提示词字段，避免照抄旧示例顶层字段 |
| 同上 | `setup.py`、`scripts/validate_skills.py`、`ai_skills_cli/`中对应验证路径与现有 `schemas/` 目录 | 在所查范围未找到可直接复用的通用JSON记录检查入口；现有技能元信息检查不等同于任务记录结构检查 |
| `YuukiAS/AI_Research_Toolkit`，`research/delivery-anti-degradation-20261109` | `docs/research/delivery-anti-degradation-20261109/REPORT.md` | 读取反降级调研；其已被流程0.1改定的负责人和独立角色建议不沿用 |
| `YuukiAS/Asteria-Blueprint`，`draft/blueprint-round7-20261107` | `docs/planner-guide.md`、`docs/content-model.md`、`content/blueprint.schema.json`、`content/template.json` | 采用指定候选格式、终点、接口、需求、验收与草稿约定 |
| 同上 | `content/schema.ts`、`content/validation.ts`、`content/validation-round5.ts`、`content/check.mjs`、`content/freeze.mjs`、`content/round7.ts`、`content/readability.ts`、`content/package.json` | 核实真实检查入口、草稿与冻结耦合、第三态缺口、读者记录和跨引用规则；没有运行这些入口 |

当前用户将本轮明确绑定为D2，并指定流程0.1为唯一依据，因此没有冒充旧Planner/Critic，也没有把资料助手检查当成D3或正式关卡。仓库的源层维护、生成物不可手改、真实能力证据等要求仍保留为实施约束。历史研究中验收器归属的矛盾已按当前流程收敛：X2默认写验收实现，规定情况必须X3，全部资产变化由X1审查，完成语义变化归D1。

Blueprint中的公开仓库事实依据固定到写入探针时的来源快照；设计A自身的具体选择引用已写入的规格快照。私有来源只以本表的仓库、分支、路径定位，不把私有提交或正文复制到公开依据记录。未读取用户提供的其他真实试跑设计成果；SPEC仅保留其允许的定位，不能据此声称已做试跑回放。

## 平台与依赖的原始资料

查阅日期为2026-11-10。资料支持文件格式、接口和分发边界；没有据此推导本轮插件已经安装或可自动控制宿主。

1. Anthropic，[Extend Claude with skills](https://code.claude.com/docs/en/skills)。核对 `SKILL.md`、基础YAML元信息、支持文件和新上下文能力。上下文独立不等于文件权限隔离。
2. OpenAI，[Build skills](https://developers.openai.com/plugins/build/skills)。核对技能目录、支持资源与同源正文复用；不推导自动模型档次或网页线程控制。
3. OpenAI，[Package your plugin](https://developers.openai.com/plugins/build/plugins)。核对既有 `.codex-plugin/plugin.json` 的兼容布局；采用现有仓库生成机制的建议据此成立。
4. OpenAI，[Plugin submission errors](https://developers.openai.com/plugins/deploy/submission-errors)。核对技能资源和普通文件约束，作为未来网页端打包复核材料。
5. OpenAI，[Build skills：optional metadata](https://learn.chatgpt.com/docs/build-skills#optional-metadata)。资料助手核对当前调用策略字段；本线程同时读取了上表中仓库内的明确字段规范。
6. Python jsonschema，[Schema Validation](https://python-jsonschema.readthedocs.io/en/stable/validate/)。核对 `Draft202012Validator`、`check_schema`、`iter_errors`和显式格式检查；缺格式依赖可能使检查失效，不能仅开启一个选项就声称已验证。
7. Python jsonschema，[JSON (Schema) Referencing](https://python-jsonschema.readthedocs.io/en/stable/referencing/)。核对使用预注册本地资源控制引用读取；本设计禁止记录检查时自动获取未知远端结构。
8. Python Package Index，[jsonschema 4.26.0](https://pypi.org/project/jsonschema/4.26.0/)。核对精确版本、Python 3.10以上、MIT许可及格式依赖选项。许可结论只覆盖该项目声明，不代替后续实际锁定依赖集的许可核对。

| 资源 | 本轮采用状态 | 实际消费与边界 |
|---|---|---|
| 平台官方文档、历史研究 | `REFERENCE_ONLY` | 用于设计判断与出处，不复制外部实现；没有由查阅直接宣称功能整合 |
| 本仓库生成器与已有技能 | `REFERENCE_ONLY` | 已核对实际实现；建议实施阶段复用。尚未改源码或生成包 |
| 指定Blueprint格式 | `REFERENCE_ONLY` | 已按其结构实际生成本候选；正式检查入口尚未接入，未复制上游检查代码进插件 |
| jsonschema 4.26.0 | `RUNTIME_DEPENDENCY`，仅用于本轮普通文件诊断 | 使用环境已有版本实际诊断JSON；插件中的只读记录检查仍是设计建议，未创建或运行该插件入口 |

读取公开仓库根 `LICENSE` 得到不存在；允许分支的目录信息显示部分独立资源另有许可文件。本轮没有复制这些资源进新插件或宣称全仓库统一许可。现有生成器拟在同仓库复用；如后续需要对外移植代码，须在具体来源确认许可。两个只读私有仓库没有被当作可任意转载的公开代码来源。

## 实际执行的普通文件诊断

`blueprint.json`当前包含54个节点、47个叶节点，其中44个具体设计终点、3个开放问题；14条需求、48条有向连接、四种环境的正常走查、9条失败路径。所有新插件能力均标为未实现，全部验收保留 `not-run` 和空运行记录，冻结历史保留 `versions: []`。

实际执行了JSON解析和结构诊断。第一次直接使用Python结构库时，其正则表达式引擎不支持上游结构中JavaScript的汉字脚本模式，诊断因此中止，不能据此判断文档对错。随后保留该模式原文，使用Node的Unicode正则表达式求值，其余结构由环境现有 `jsonschema 4.26.0` 检查。对完整原结构定义，唯一报错是空 `versions` 不满足至少一条冻结历史；这与起稿指南形成的已知冲突属于Q1，没有编造历史绕过。

为定位其他草稿错误，仅在内存副本中将上述一条历史数量约束放开，其余结构检查没有报错。上游结构文件未修改；这一步是普通草稿诊断，绝不等于官方检查通过。已实际核对节点与需求承接、全部端口和直接父子引用、连接方向、四环境正常路线、失败路径检测者与反例注入、依据引用、短标签、51个读者检查主体的编号与技术身份。最初发现的一处需求承接漏标和一处会触发占位词检查的引语已经修正；复核没有剩余引用或图一致性报错。

最终诊断对象的SHA-256为 `b367e39e09384c7e8fdfeb5edc0e62ec24fb9c4b2823d74211815271a1215131`。已从指定GitHub分支回读Blueprint并逐字符比较，与本地候选相同。SPEC和QUESTIONS也已回读。普通检查未覆盖正式在线依据校验、真实角色执行、D8独立复述、用户批准、安装调用或专业正确性，不能向这些范围外推。

## 保留的不确定性与实际下一步

三个问题详见[QUESTIONS.md](QUESTIONS.md)。Q1决定上游通用草稿/冻结入口怎样提供，避免首次冻结与完整检查互相等待；Q2决定无语义小修怎样继承批准和原复述记录，不伪造新用户批准或新读者；Q3由D1明确中央市场容量调整是否纳入同一实施合同，不能挤掉旧能力。推荐方案都只是可比较设计，没有偷偷当作已批准前提。

跨宿主可直接读取同源文件有官方格式与现有结构依据，完整包根目录的可见性、实际调用、模型档次选择和新线程能力仍须在对应宿主真实验证。记录中的三态、同一最终候选和亲读要求已经明确，但它们是否在正常使用中可靠生效，要由后续实现与真实验收证明。新会话不形成隐藏用例权限；只读检查脚本不形成授权系统。

本轮只授权写指定设计目录，因此没有修改TODO、Issue、维护看板、README、插件、配置或其他仓库。后续由具备写入范围的维护线程复用已有跟踪项，执行锚点指向本目录，状态保持设计进行中，下一步为“D1比较两份独立候选并收敛，再进入冻结关卡”；不得把候选交回记为插件完成，也无需用户手工维护。

README checked: no update required。当前没有正式入口、名称、发布版本、安装方式或已实现能力变化；正式实施时仍按真实改动同步README。
