# 最终用户阅读层终审架构提案

- 版本：`v0.2`
- 日期：`2026-10-06`
- 最新 `main` 已核对：`720e6042ff8105f4b6fd5ff0952d2073b4c492f6`
- 设计分支起点：`36e854fe06779400e2e1279083a34803c7c62a48`
- 前一版设计：`v0.1`，提交 `04b88cbc54390222d01ae5768f920a66ccb75588`
- 跟踪：`#13`
- 状态：`READY_FOR_CRITIC_REVIEW`
- 范围：只做研究、架构和验收设计；不授权实现、发布、线上插件修改、付费接口、自动化或真实 Project 改写。

## 0. 核心判断

这个问题的中央负责人应是现有 Clear Writing 插件 `writing-style`，而不是 Project Instructions Editor，也不应再创建一个顶级插件。建议在 Clear Writing 内新增一个职责窄、可单独验收的技能：

```text
reader-layer-finalization
```

它负责普通聊天回答的最后用户阅读层：把已经形成的事实、判断和动作重新组织成符合当前语言合同、自然连续、低机器味且语义保真的最终可见回答。它不负责科研、工程、统计、权限、安全或产品事实本身。

当前 ChatGPT Web 的公开产品能力没有提供可依赖的通用发送前钩子、确定的技能调用顺序、技能调用技能的接口，或无需额外凭据的独立第二次模型调用。因此，这个技能只能建立同一模型轮次内的逻辑终审阶段，不能被描述成机械隔离的第二次生成。正常入口采用多层防护：

1. 安装可在 ChatGPT Web 使用的 Clear Writing 技能型插件；
2. 用技能元数据争取相关性自动调用；
3. 对需要高可靠性的 Project，仅保留一条短激活桥；
4. Project 外可用全局 Custom Instructions 作为低强度兜底；
5. 用真实首答、成对对照和冻结的未见样本验证，而不是相信“已调用”的自我声明。

短激活桥只是路由防线，不是主能力。若同样的短桥在没有候选技能时已经达到相同效果，说明新增技能没有被证明有增量价值，应返回 Planner 简化方案，而不是发布一个名义上的终审技能。

## 1. 问题定义

真实失败不是单纯“不会翻译”，而是模型在读取英文仓库、论文、技能、插件、日志和治理材料后，把来源表达误当成用户必须看到的正式表达。常见后果包括：

- 普通技术、科研和流程词继续用英文；
- 来源标题、阶段名、机制名和内部角色成为正文概念；
- 先讲内部审计，再讲用户真正需要的结论；
- 一句话一段、单字段成段、状态块和列表堆叠；
- 裸日志、路径、提交和字段替代经过消化的判断；
- 同一结论被多套状态重复；
- 为了中文自然而误改事实、权限、完成状态或不确定性。

成熟需求合同已经存在于 AI Research Stack 的“面向用户的输出规范”。缺口不是继续扩写语义，而是建立清楚的负责人、正常入口、消费证据和阻断性验收。

## 2. 旧路线已经证明什么

C5–C11 共同建立了四项架构约束：

1. 规则写入同一次生成，不等于最终输出会可靠执行；
2. 同轮读取多个技能，不等于独立阶段分离；
3. 语言重写可能恢复已删除内容、弱化权限或错误升级完成状态；
4. 文件、字符串扫描、自检、局部样例和测试通过，不能替代普通 ChatGPT Web 的完整首答。

C11 的最终审查已经明确停止继续增加同义基线、自检和精确性说明，并禁止创建 C12。关键身份保持为：

```text
C11_CANDIDATE = 187212887bc8f7a339cd43097384df35c1e71baf
C11_EVIDENCE = 9824d0501dea233442d3f0aca85e319f757bbe27
C11_CRITIC_STOP = 1325ffba51be6ecbe46cde7e46492f9e69284c4c
```

本提案吸收这些失败，但不延续 PIE 的实现编号和机制。

## 3. 当前产品现实

截至 `2026-10-06`，OpenAI 官方资料支持以下事实：

- 安装后的技能可在模型判断有帮助时自动使用；模型先看到技能名称与描述，匹配后才加载完整说明；
- 一个插件可以包含多个技能，ChatGPT 会在相关时自动使用已安装插件，也可用 `@` 明确选择；
- 官方资料没有承诺多个技能按确定顺序执行，也没有公开技能调用技能的接口；
- 插件生命周期钩子属于 Codex 运行环境；网页安装插件不会部署这些脚本，普通 Chat 不应依赖钩子；
- Project instructions 只在对应 Project 内生效，并覆盖全局 Custom Instructions；
- Workspace Agent 需要专用访问令牌并由外部系统触发，不是普通聊天中的透明第二阶段。

因此，产品合同必须明确：

```text
INDEPENDENT_SECOND_MODEL_CALL = NOT_AVAILABLE_IN_NORMAL_PATH
UNIVERSAL_PRE_SEND_HOOK = NOT_DOCUMENTED
DETERMINISTIC_SKILL_CHAIN = NOT_DOCUMENTED
AUTO_RELEVANCE_ROUTING = AVAILABLE_BUT_NOT_A_GUARANTEE
```

本轮还核对了当前已认证个人 ChatGPT 的私有插件列表：已经存在多个个人技能型插件，但没有独立安装的 Clear Writing。也就是说，仓库中存在 `writing-style` 生产身份，不等于普通个人 Web 表面已经拥有该能力。后续实现必须把“构建并安装同一产品身份的个人或工作区插件候选”列为正式交付，而不能只改仓库源文件。

## 4. 职责归属比较

| 路线 | 决定 | 主要原因 |
|---|---|---|
| A. PIE 继续负责 | 拒绝 | PIE 负责编辑长期 Project instructions，不拥有每次回答的最终表达；C5–C11 已反证继续强化同一规则层。 |
| B. 扩展 Clear Writing | 采用 | 现有 `chinese-prose` 已拥有中文成稿能力，`writing-fidelity` 已拥有保真能力，`#13` 已将它定位为跨项目语言层。 |
| C. 新独立技能 | 不设顶级独立产品；在 Clear Writing 内新增窄技能 | 独立安装会制造两个中央来源；插件内窄技能能形成清晰路由和验收面。 |
| D. 新顶级插件 | 拒绝 | 换壳不会产生发送前钩子，只增加安装、版本和路由竞争。 |
| E. Project 顶部短硬门 | 仅作防线 | 仍然是自然语言指令，不能单独证明消费；但可提供语言和绕过上下文，并提高相关性路由概率。 |
| F. ChatGPT Web 的插件/技能入口 | 采用但不夸大 | 自动相关性调用和明确选择是真实入口，但没有每条回答必经保证。 |
| G. 钩子、Workspace Agent、外部第二次调用 | 不进入正常路径 | 能提供更强隔离，但需要不同运行表面、脚本、令牌、托管或额外成本。 |
| H. 不新增技能，只修改各领域调用架构 | 不足以单独成立 | 会在多个领域重复同一规则，也无法证明普通 Web 实际消费；但领域能力需要在交付语义后让出表达层。 |

## 5. 推荐架构

### 5.1 中央产品身份

```text
PLUGIN_SLUG = writing-style
DISPLAY_NAME = Clear Writing
NEW_BUNDLED_SKILL = reader-layer-finalization
NEW_TOP_LEVEL_PLUGIN = NO
NEW_STANDALONE_PRODUCT_IDENTITY = NO
```

个人或工作区中的私有插件安装只是同一 Clear Writing 产品的分发形态，不是另一个产品身份。

### 5.2 职责分层

领域能力负责形成可靠语义，包括事实、证据、判断、权限、动作和不确定性。`reader-layer-finalization` 只负责将这些内容实现为最终用户可读表达。Project instructions 只提供当前语言、数学排版、机器输出和局部偏好；它不复制完整终审合同。全局 Custom Instructions 只为 Project 外聊天兜底，不能覆盖 Project instructions。

逻辑流程为：

```text
领域任务形成语义结果
→ 识别本次受保护语义
→ 形成目标语言和输出模式下的最终可见回答
→ 发送前核对语义与精确标识
```

这只是同一模型轮次内的逻辑边界，不得声称为独立模型调用或真实发送前脚本。

### 5.3 受保护语义

终审不得改变：

- 事实、数值、公式、引用和归因；
- 否定、比较、因果和条件关系；
- 结论强度、证据强度、不确定性和限制；
- 必须/可选、允许/禁止、授权/未授权；
- 安全、隐私和权限边界；
- 当前/过去/未来、已完成/未完成；
- 用户明确纠正、删除、拒绝和接受的决定；
- 需要复制、执行、搜索或唯一定位的精确标识。

### 5.4 阅读层职责

终审同时处理：

- 普通概念使用当前目标语言，来源为英文不构成保留理由；
- 标题、列表、表格、总结和结论同样执行语言合同；
- 来源标题、阶段名和内部字段只有在用户任务本身讨论它们时才保留；
- 先给实际结论、是否需要动作和下一步，再给必要证据；
- 段落按真实信息结构形成，不按字段或每句话机械换行；
- 同一结论不以多套状态块重复；
- 必须原样保留的代码、命令、路径、字段、主机名、端口和正式身份与解释正文分层；
- 纯 JSON、纯日志、纯代码、逐字引用和严格机器协议进入绕过模式；混合任务只重写解释层；
- 当前消息明确要求英文、双语或其他语言时，只覆盖当前回复，不永久修改 Project 合同。

不采用禁词表、英文比例、固定段数、固定三段式或关键词评分器。

## 6. 正常入口与增量价值验证

候选必须在四种条件下比较：

| 条件 | 设置 | 用途 |
|---|---|---|
| A | 候选 Clear Writing 已安装，不放 Project 短桥 | 判断插件元数据能否独立承担自动路由；通过则短桥可降为可选。 |
| B | 候选已安装，并放入获批短桥 | 目标高可靠正常入口；用户不提技能、不再次提醒。 |
| C | 同样短桥，但禁用候选技能或使用不含该技能的上一版本 | 排除“只是短提示词又一次偶然成功”。 |
| D | `@Clear Writing` 明确调用 | 只用于候选身份与能力诊断，不计正常入口通过。 |

最低产品成功条件是 B 在冻结的完整首答验收中通过，并且相对 C 显示候选依赖的稳定增量。若 B 与 C 无可辨别差异，应返回 Planner，重新评估是否只需要更短的 Project 合同；若只有 D 通过，则产品只能算显式工具，不能宣称解决普通使用。

若产品界面不显示技能调用记录，证据结论只能是“候选依赖的可观察行为得到支持”，不能写成“已证明内部按某顺序调用”。

建议短桥保持为一条、一次性配置：

```text
发送面向用户的解释性正文前，使用已安装的 Clear Writing 完成最后阅读层。按本 Project 的语言与格式合同表达，只改措辞和信息组织，不改事实、数值、条件、权限、安全、证据强度、不确定性、完成状态、时间关系或精确标识。本条消息明确要求其他语言、双语或纯机器内容时，仅对本次切换或跳过。
```

它不要求用户每个 thread 重复提醒，也不得扩写成 C11 的长基线。核心能力稳定后，PIE 可在创建或整理 Project instructions 时一次性保留这条桥，但该适配不是本轮最小实现的前置条件。

## 7. 跨 Project 行为

- AI Research Stack：默认自然中文，科研和工程语义由对应领域能力负责，必要机器身份原样保留；
- Server+VPS：中文判断与主机、端口、路径、服务、权限和主备状态严格分层；
- CAT-TRACE：公式、符号、定理状态、统计结论和引用保持精确；
- 前端/Figma/代码：组件、节点、文件、函数和代码身份保持精确，产品判断使用目标语言；
- 英文 Project：终审仍处理结构、日志腔和重复，但目标语言为自然英文；
- 双语 Project：只执行已声明的双语边界，不擅自扩大双语范围；
- 当前消息覆盖：仅影响当前回复，下一轮恢复持久合同；
- 机器专用请求：不增加解释，不改字段、顺序、代码、日志或逐字内容。

## 8. 五遍预检

### 产品

用户直接提出领域问题，第一条完整回答已经是可阅读结论，不再需要补一句“说中文”“不要状态块”或 `@Clear Writing`。对当前个人 Web，正式交付还必须包括可安装的同身份 Clear Writing 私有插件候选。

### 现实

平台支持安装、相关性自动调用和明确选择，但不支持本项目可以依赖的通用发送前钩子、确定技能链或透明第二次模型调用。方案只承诺可观察的高可靠行为。

### 替代

更简单方案是只保留短 Project 合同；更强方案是外部第二次调用或专门客户端。前者必须在条件 C 中比较，后者因凭据、托管、费用和入口变化不进入正常路径。

### 反证

最终验收必须主动检查：安装但未消费、短桥偶然成功、同轮多技能伪装阶段分离、首答失败后靠第二轮修正、来源英文重新泄漏、语义漂移、精确标识误改、语言覆盖污染后续轮次、纯机器输出被润色，以及候选只在明确调用时工作。

### 执行合同

独立 Critic 必须先确认负责人、分发入口、平台边界、增量对照和验收矩阵。Critic PASS 只允许进入后续实现，不代表已经可用、已发布或获得用户发布授权。

## 9. 最小成熟实现

Critic PASS 后的最小实现只包含：

1. `skills/writing/core/reader-layer-finalization/` 的正式源；
2. 紧凑运行合同、反例和回归输入；
3. 打包进现有 `writing-style`；
4. 可在目标 ChatGPT Web 表面安装的同身份候选，包括当前个人用户范围的分发路线；
5. 一条短 Project 激活桥和 Project 外兜底说明；
6. 条件 A–D 的成对对照；
7. 多领域、跨语言、机器绕过和多轮完整回答验收；
8. 独立阅读质量与语义保真审查；
9. 版本、变更记录、候选身份和回退闭环。

明确不包括：新顶级插件、新 MCP、旧 finalizer、OpenAI API key、外部模型托管、Workspace Agent、Codex 钩子、C12、批量改写全部 Project、禁词评分器或自动发布。

## 10. 停止条件

以下任一成立即返回 Planner：

- 目标 Web 表面无法安装或自动使用候选技能；
- 正常入口只能靠每轮 `@` 或用户再次提醒；
- 条件 B 相对 C 没有证明新增技能的增量价值；
- 完整回答继续系统性复现 C11 的来源英文和状态块泄漏；
- 语义、权限、完成状态、不确定性或精确标识发生漂移；
- 方案必须依赖额外接口密钥、托管、费用或不同客户端；
- 评估只能靠挑选赢家、追加样本或替换失败题目才能通过。

## 11. Planner 决议

```text
PROPOSAL_RESULT = READY_FOR_CRITIC_REVIEW
PRIMARY_OWNER = writing-style / Clear Writing
NEW_TOP_LEVEL_PLUGIN = NO
NEW_STANDALONE_PRODUCT = NO
NEW_BUNDLED_SKILL = reader-layer-finalization
TARGET_NORMAL_ENTRY = INSTALLED_CLEAR_WRITING + ONE_TIME_PROJECT_BRIDGE
NO_BRIDGE_MODE = REQUIRED_DIAGNOSTIC
BRIDGE_ONLY_BASELINE = REQUIRED_COUNTERFACTUAL
GUARANTEED_INDEPENDENT_SECOND_CALL = NO
UNIVERSAL_PRE_SEND_HOOK = NO
PAID_API_OR_HOSTING_IN_MINIMUM_PATH = NO
PIE_PRIMARY_OWNER = NO
PIE_C12 = NO
PRODUCTION_IMPLEMENTATION_AUTHORIZED = NO
TRACKING_ISSUE = #13
NEXT_ACTION = INDEPENDENT_CRITIC_REVIEW_OF_V0_2
```

## 12. 官方资料

- OpenAI Help：Skills in ChatGPT
- OpenAI Developers：Skills – Plugins
- OpenAI Help：Plugins in ChatGPT
- OpenAI Developers：Package your plugin
- OpenAI Developers：Submit your Claude Code plugin to OpenAI
- OpenAI Help：Projects in ChatGPT
- OpenAI Help：ChatGPT Custom Instructions
- OpenAI Developers：Workspace Agents
- OpenAI Developers：Authenticate with Workspace Agent access tokens
