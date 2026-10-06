# 最终用户阅读层终审 v0.2：Critic 审查提示词

你是 AI Research Stack 的独立 Critic。本轮只审查一个新的跨 Project 架构设计，不实现代码，不创建 Executor，不修改正式插件，不启动付费接口、外部模型、自动化或发布。

## 审查对象

仓库：

```text
YuukiAS/AI_Skills_Collection
```

设计分支：

```text
planner/reader-layer-finalization-v0.1
```

不可变设计包提交：

```text
011d141d788cd3030930c06bf9b17aa2f92786a8
```

草稿 PR：

```text
#100
```

跟踪：

```text
#13
```

只审查以下 `v0.2` 文件；`v0.1` 是已被本轮补强取代的历史设计，不得混用版本：

```text
docs/design/clear-writing/USER_READER_LAYER_FINALIZATION_PROPOSAL_V0_2_2026-10-06.md
docs/design/clear-writing/USER_READER_LAYER_FINALIZATION_PLAN_V0_2_2026-10-06.md
docs/design/clear-writing/USER_READER_LAYER_FINALIZATION_GATE_MATRIX_V0_2_2026-10-06.md
```

## 一、先读取治理合同

从最新 `main` 实际读取：

```text
AGENTS.md
docs/workflows/PLANNER_ROLE_CONTRACT.md
docs/workflows/CRITIC_ROLE_CONTRACT.md
docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md
docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
```

审查必须按 Critic Role Contract 工作。阻塞项必须同时给出对应要求、直接证据、因果风险和最小关闭条件；不要用偏好、格式洁癖或“更保险”阻塞，也不要因为不确定感要求无界扩张。

## 二、读取真实失败史与当前能力

至少读取：

```text
results/project-instructions-editor--standalone-skill-implementation/C11_READER_BASELINE_GATE_CRITIC_REVIEW.md
skills/writing/core/chinese-prose/SKILL.md
skills/writing/core/writing-fidelity/SKILL.md
docs/plugin-todos/writing-style.md
scripts/codex_marketplace_config.json
```

C11 停止审查按以下提交读取：

```text
1325ffba51be6ecbe46cde7e46492f9e69284c4c
```

关键历史身份：

```text
C11_CANDIDATE = 187212887bc8f7a339cd43097384df35c1e71baf
C11_EVIDENCE = 9824d0501dea233442d3f0aca85e319f757bbe27
C11_CRITIC_STOP = 1325ffba51be6ecbe46cde7e46492f9e69284c4c
```

还要核对 C5–C10 中与本轮直接相关的真实证据，尤其是：

- 规则存在但完整回答仍泄漏普通英文；
- 自检声称通过而最终文本违反合同；
- C7 的“为了重写而恢复已删除/已拒绝内容”；
- C10-B3 证明同轮读取多个技能不等于独立阶段，只有真正分离的多轮传递才通过；
- C11 已禁止继续增加同义提示词、创建 C12 或恢复旧 MCP/API finalizer。

不要把这些历史重新解释成 PIE 的小 bug，也不要要求再次用同一批输入证明同一提示词终于稳定。

## 三、独立核查当前 OpenAI 产品能力

只用最新 OpenAI 官方资料核查：

1. ChatGPT Web 中技能的自动相关性调用与明确调用；
2. 插件内多个技能的消费边界；
3. 是否存在技能调用技能的公开接口或确定执行顺序；
4. 是否存在普通 ChatGPT Web 可依赖的通用发送前钩子；
5. Project instructions 与全局 Custom Instructions 的作用范围和覆盖关系；
6. 个人或工作区技能型插件的安装与资格边界；
7. 是否存在无需额外令牌、托管、接口费用或用户操作的透明独立第二次模型调用；
8. Workspace Agent、Codex 钩子和外部模型为何不等于普通聊天正常入口。

找不到公开能力时，应写“官方公开资料没有提供或没有找到”，不要把缺少文档夸大成数学意义上的不存在；反过来，也不得用推测补出平台保证。

## 四、必须独立攻击的核心决策

### 1. 中央负责人

判断 Clear Writing（`writing-style`）是否确实应成为唯一中央负责人。比较 PIE、扩展现有 `chinese-prose`、新增插件、只使用 Project 短桥和不新增技能等替代方案。

重点检查：新增 `reader-layer-finalization` 是否具有独立产品职责，还是与 `chinese-prose` / `writing-fidelity` 重复；若重复，指出更小的成熟方案。

### 2. 是否真正跳出 C11

新方案仍处于同一模型轮次，不能靠命名为“终审”就冒充独立阶段。检查它相对 C11 的真实新增机制是否只有：

- 正确的中央负责人；
- 可安装、可路由、可单独验收的技能产品面；
- 个人/工作区插件分发；
- Project 短桥作为路由防线；
- 候选依赖的成对对照；
- 真实普通 Web 完整回答验收。

若这些仍不足以产生可观察增量，应 `REVISE`；但不要因为平台不支持机械 100% 保证就直接否定所有现实改进路线。

### 3. 目标表面与分发

本轮只读核查已经发现：当前已认证个人 ChatGPT 中存在多个私有技能型插件，但没有独立 Clear Writing。检查执行方案是否正确把“构建并安装同一 `writing-style` 产品身份的个人或工作区候选”列为正式交付，而不是只修改仓库源文件。

检查 Research Authoring 附带的 Clear Writing 支持技能是否被正确区分，不能把它冒充跨 Project 独立安装。

### 4. 正常入口与短桥

检查一次性 Project 短桥是否只是防线和上下文，不是换名后的 C11 主机制。方案不得要求用户每个 thread 再提醒，也不得声称全局 Custom Instructions 能覆盖 Project instructions。

判断“已安装候选 + 一次性短桥”是否是可接受的最低正常入口；同时检查无短桥模式是否被保留为必要诊断，以决定未来能否进一步减少 Project 配置。

### 5. 候选增量对照

重点审查验收矩阵中的 A–D：

```text
A = 候选已安装，无短桥
B = 候选已安装，有短桥
C = 不含候选技能的上一版本或禁用候选，有相同短桥
D = 明确 @Clear Writing
```

确认这组对照能发现：

- Skill 安装了但没有实际消费；
- 只是短提示词偶然成功；
- 只有明确调用才工作；
- 同轮多技能被误报为独立后处理。

若界面没有技能调用记录，检查设计是否诚实地把结论限制为“候选依赖的可观察行为”，而不是虚构内部调用顺序。

### 6. 语义保真

检查受保护语义是否覆盖：事实、数值、公式、引用、条件、否定、比较、因果、结论强度、证据强度、不确定性、必须/可选、允许/禁止、授权、安全、隐私、时间、完成状态、精确标识，以及用户明确纠正、删除、拒绝和接受的决定。

必须检查反例，防止为了中文自然把“未完成”改成“已完成”、把“可选”改成“必须”、把来源未来工作改成当前计划，或翻译主机名、路径、命令和字段。

### 7. 阅读层完整性

检查能力是否同时处理：非必要英文、来源标签、内部治理字段、机械换行、单字段成段、状态块、无结构列表、裸日志、内部审计先于用户结论、重复结论和机器内容未分层。

不得把它退化成禁词表、英文比例、固定模板或所有回答三段式。

### 8. 跨 Project 与语言

核对 AI Research Stack、Server+VPS、CAT-TRACE、前端/Figma/代码、英文 Project、双语 Project、临时语言覆盖和机器专用输出。当前消息的临时要求不得永久污染 Project 合同。

### 9. 验收真实性

检查能力验收矩阵是否要求：

- 普通 ChatGPT Web；
- 第一条完整回答；
- 冻结候选和未见样本；
- 预定尝试次数；
- 禁止换题、挑赢家和无限补样本；
- C5–C11 只作回归；
- 独立阅读质量和命题级保真审查；
- 候选身份、安装身份和完整产物可追溯。

不要用固定 Gate 数量做形式审查；判断每个 Gate 是否对应真实失败模式。

### 10. 范围、成本与回退

确认最小实现没有新顶级插件、MCP、外部托管、接口密钥、Workspace Agent、Codex 钩子、C12、批量改写全部 Project 或自动发布。确认失败时能卸载候选、删除试点短桥并恢复上一正式 Clear Writing，而不恢复旧 finalizer。

## 五、审查结论规则

只有架构、正常入口、分发、增量对照、语义保真、平台边界和真实验收都足以进入有限实现时才给 `PASS`。

`PASS` 只批准 `v0.2` 设计进入后续实现规划，不代表已经实现、可用、发布或获得任何写入/付费/自动化授权。

若返回 `REVISE`，先复核已有阻塞项，再提出真正阻断执行的最小关闭条件。不要把可选改进写成阻塞，不要创建 Executor，不要直接修改设计文件。

## 六、要求的输出格式

先用自然中文给出一段经过消化的核心判断，再给结构化结论。不要用裸日志和大量状态字段代替分析。

结尾必须包含：

```text
CRITIC_RESULT = PASS | REVISE
REVIEWED_DESIGN_VERSION = v0.2
REVIEWED_DESIGN_COMMIT = 011d141d788cd3030930c06bf9b17aa2f92786a8
PRIMARY_OWNER_DECISION = ...
NEW_BUNDLED_SKILL_DECISION = ...
NORMAL_ENTRY_DECISION = ...
PERSONAL_OR_WORKSPACE_DISTRIBUTION_DECISION = ...
BRIDGE_ONLY_COUNTERFACTUAL_DECISION = ...
PLATFORM_LIMITS_DECISION = ...
SEMANTIC_FIDELITY_DECISION = ...
GATE_MATRIX_DECISION = ...
PRODUCTION_IMPLEMENTATION_AUTHORIZED = NO
NEXT_ACTION = ...
```

每个阻塞项必须写清：

```text
要求：
直接证据：
因果风险：
最小关闭条件：
```

若 `PASS`，明确冻结获批范围并说明下一阶段新增的真实能力；若 `REVISE`，明确返回 Planner，不得启动实现。