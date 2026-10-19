# ChatGPT Web PASS 可信度与用户控制修复 — Proposal v0.3

日期：2026-10-19  
任务键：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`work/chatgpt-web--pass-integrity`  
当前 main 核实：`9740a593c1622bce61401c8215c621f8cdb7d93a`  
上一版：`docs/workflows/CHATGPT_WEB_PASS_INTEGRITY_PROPOSAL_V0_2_2026-10-19.md`  
阶段：DESIGN_PROPOSAL / CRITIC_REQUIRED / NO_IMPLEMENTATION

## 1. 本轮只关闭什么

Proposal v0.2 的主体方向保留。本轮接受独立 Critic 的三个 blocker，并同时纳入用户刚刚明确的读者体验要求：

- PI-01：保留实现后的独立最终评估安全门，但该阶段不再使用 Critic PASS；
- PI-02：端到端验证必须覆盖风险匹配的关键失败链，不能只测成功路径；
- PI-03：唯一 execution-ready PASS 之后若必须改变用户承诺、架构、权限、验收或恢复语义，原批准立即失去当前效力，并在同一 task 内进入新的修订闭环；
- 用户新增明确要求：**任何 Planner/Critic 轮次都必须让用户在不阅读内部 finding 和 handoff prompt 的情况下，知道这一轮到底发现了什么、改了什么、现在离 Codex 还有多远。**

本轮不新增第三角色、状态机、数据库、watcher、daemon、requirements ledger 或新的顶级工作流。

## 2. 冻结的用户承诺基线

1. Critic 级 `PASS` 在一个有效设计—执行闭环中只允许出现一次，只能出现在最终 execution-ready 审查，并与 `READY_FOR_CODEX=YES` 同时成立。
2. 设计中间轮次只能给 `PROCEED` 或 `REVISE`；它们不授权 Codex。
3. 最终 execution-ready 审查必须重新对照完整用户承诺、当前 Proposal/Plan/Goal/Kickoff 和完整正常用户路径，不能被 Planner 生成的窄 prompt 缩成“只看上一轮 blocker”。
4. 唯一 PASS 表示所有会影响产品行为、架构、配置归属、调用关系、权限、验收和恢复的决定已经闭合；Codex 只能决定普通实现细节。
5. 如果用户在唯一 PASS 后通过一句自然追问就能发现核心设计缺口，则该 PASS 本身不合格。
6. 核心能力必须有正向发生要求；`UNKNOWN`、fallback、未配置和失败关闭不能单独证明能力成立。
7. 跨组件用户承诺必须有完整端到端验证；关键安全/失败语义必须有风险匹配的边界失败验证。
8. 普通实现缺陷默认留在同一 Codex 任务修复，不因为失败本身退回 Planner。
9. 用户不承担内部审查翻译工作。每轮必须先给可独立阅读的自然中文摘要，再给机器交接 prompt。
10. 用户可见摘要必须经过 Clear Writing 最终表达检查；但 Clear Writing 只负责语言质量，不能替代本 Proposal 规定的“必须解释什么”。

## 3. Critic 结论模型

### 3.1 设计与执行包形成阶段

只允许：

- `PROCEED`：当前对象足以进入下一设计阶段，但整个执行闭环尚未完成；
- `REVISE`：存在真实 blocker。

不得出现 Critic `PASS`。

### 3.2 唯一 execution-ready 审查

只允许：

- `PASS`：唯一一次，同时 `READY_FOR_CODEX=YES`，并直接交付最终可发送的 Codex handoff；
- `REVISE`：仍有任何会改变用户承诺、架构、权限、验收、恢复或执行语义的空白。

禁止 `PASS BUT`、`PASS_WITH_CONDITIONS`、先 PASS 再让 Codex 探索关键设计。

### 3.3 Codex 实现以后

不再使用 Critic PASS。使用与阶段一致的用户级结论：

- `RETURN_TO_CODEX`：批准范围内实现缺陷，回同一 Codex 任务修；
- `CANDIDATE_ACCEPTED`：最终候选的 required Gate 与正常入口证据成立；
- `RELEASE_READY`：发布前条件闭合；
- `RELEASED`：正式发布/安装身份核实。

这些名称是用户层结论，不新增 Project、Reviewed Handoff 或其他持久状态机字段。

## 4. PI-01：保留实现后的独立最终评估安全门

v0.2 中“Codex 实现后不再给第二次 Critic PASS”保持不变，但不能因此取消当前 1.6 中实现后、不可继续调优的最终评估前独立 Critic 检查。

该安全门继续检查：

- 完整产物和正常入口证据是否真的存在；
- 所有 release-critical evidence 是否来自同一最终候选；
- 最终评估输入、标准和 Reviewer 可访问性是否冻结；
- 付费/未见评估预算是否仍有效；
- 失败后的恢复条件是否明确；
- 关键正向能力与关键失败链是否已经在最终候选上得到直接验证。

该阶段结论只能是：

- `PROCEED_TO_FINAL_EVALUATION`：允许进入不可继续调优的最终评估；
- `REVISE`：仍有阻塞条件。

不得产生第二次 Critic PASS，也不得新增第三套工作流。

## 5. PI-02：端到端承诺同时覆盖成功链和关键失败链

Capability Gate Policy 新规则分两部分。

### 5.1 正向能力与跨组件成功链

如果产品声称某个用户可见能力会发生，至少一个最终候选的正常入口必须真实观察到该行为。

如果承诺跨组件，例如：

`Persistent Run → shared Notifier → one-shot Clear Writing → transport`

则至少一个场景必须直接覆盖整条链。

### 5.2 风险匹配的关键失败链

如果用户承诺包含 fail-closed、安全阻断、恢复或“不允许危险下游动作发生”的语义，则最高风险、且能代表真实事故的边界失败必须从正常入口直接验证。

例如 Slurm：

`Codex tool call → Hook 启动失败`

此时必须直接证明危险底层 `scancel` 没有执行，而不是只证明 Hook checker 单测失败。

数量按风险决定，不固定要求所有故障组合，也不建立 fault matrix。只验证能够代表冻结安全承诺的高价值边界失败。

## 6. PI-03：唯一 PASS 失效后的重开语义

唯一 execution-ready PASS 之后，如果后续证据表明必须改变以下任一内容：

- 用户承诺；
- 产品/架构边界；
- canonical owner；
- 权限、数据、费用或外部副作用边界；
- Capability Gate 的成功定义；
- recovery semantics；

则原冻结 package 及其 PASS 不再对当前修改后的语义有效。

处理方式：

1. 保持同一 `task_key`，除非任务目标本身真的变成另一个产品目标；
2. 不建立 successor task 作为默认动作；
3. 不新增 epoch、ledger、状态机；
4. 回 Planner 做最小必要修订；
5. 重新经过设计阶段的 `PROCEED/REVISE`；
6. 新闭环仍只有一次最终 Critic PASS。

普通实现 bug、漏接调用、配置 scope 错、runtime/loader 启动失败、普通测试或已批准 Gate failure，不触发 PASS 失效；默认 `RETURN_TO_CODEX`。

## 7. 用户可读审查输出：不再让用户机械搬运而不知道发生了什么

这是 v0.3 相对 v0.2 新增的强制用户体验合同。

### 7.1 每轮 Planner/Critic 回复分成两层

**第一层：用户摘要。**

必须能够脱离后面的 prompt 独立阅读。正常情况下控制在一屏内，用自然连续中文说明：

1. 这一轮的结论：可以继续还是需要返修；
2. 相比上一轮到底改变了什么；
3. 这些变化对实际产品意味着什么；
4. 当前还剩什么真实问题；
5. 用户现在是否需要做任何事情；
6. 下一步是谁接手、目的是什么。

如果是 `REVISE`，不能只把 PI-01、F02 等编号翻译一遍；必须先把多个 blocker 消化成用户能理解的产品含义。

如果是 `PROCEED`，必须说明“哪些决定现在已经稳定、哪些仍未闭合”。

如果是唯一 `PASS`，还必须给完整的一屏真实架构说明：配置归属、谁调用谁、默认行为、可配置项、正常成功、关键失败/恢复和仍需未来单独授权的外部动作。

**第二层：机器交接。**

完整 finding ID、路径、commit、状态字段和下一角色 prompt 放在用户摘要之后。它用于复制和精确定位，不承担向用户解释“发生了什么”的职责。

用户即使完全不阅读第二层，也必须知道这一轮发生了什么。

### 7.2 “本轮变化”必须显式，不允许只给最终状态

每轮至少用一句自然中文回答：

> 相比上一轮，这次真正改变的是……

若有 1–3 个关键变化，直接说清楚；若内部 finding 很多，应按共同原因合并解释，不把用户暴露给十几个内部编号。

这样用户不会只负责把 Critic prompt 复制回 Planner，却不知道 Planner 到底要改什么。

### 7.3 Clear Writing 的角色

Clear Writing **必须作为用户可见摘要的最后表达检查**，但它不是这套机制的核心保证。

职责分开：

- Planner/Critic 先按上述语义合同决定“必须告诉用户哪些事实”；
- 然后对用户摘要实际调用当前正式安装的 Clear Writing；
- Clear Writing 只改善中文自然度、段落组织和去除内部机器语言泄漏；
- 不允许改变结论、风险、finding 严重性、用户承诺、权限或下一入口；
- `COPY TO PLANNER / CRITIC / CODEX` 等机器交接块保持原始精确内容，不经 Clear Writing 改写。

如果当前 surface 不能实际调用 Clear Writing，不得声称已经调用；仍必须按 Project setting 的阅读层规则手工整理用户摘要。是否因调用不可用而阻塞整个审查，由最终合同实施时根据真实 ChatGPT Plugin 可用性做最小可执行处理；不得让语言工具故障掩盖或改变技术结论。

因此，**真正防止“我不知道这一轮改了什么”的是用户摘要合同；Clear Writing 负责让这份摘要像人写的，而不是用 Clear Writing 去猜应该解释哪些内容。**

## 8. 最终 execution-ready PASS 的强语义

唯一 PASS 必须同时证明：

- 用户承诺基线逐项得到冻结设计覆盖；
- 关键配置层级明确；
- 跨组件调用关系明确；
- 默认值和逐任务覆盖明确；
- 正常成功行为明确；
- 关键风险失败与恢复行为明确；
- Capability Gate 能直接验证正向能力、完整成功链和风险匹配失败链；
- 实现后最终评估安全门和预算/恢复要求明确；
- 尚需用户单独授权的真实外部动作已隔离；
- Codex 不需要再做产品、架构、权限、验收或恢复选择。

允许 Codex 自行决定的仅是不会改变上述语义的普通实现细节。

## 9. 修改后的正常工作流

```text
用户给目标
→ Planner 冻结用户承诺
→ Critic：PROCEED / REVISE
→ Planner 形成完整 Proposal + Plan + Goal + Kickoff
→ Critic 最终 execution-ready 审查
   ├─ REVISE
   └─ PASS（唯一一次）+ READY_FOR_CODEX=YES + Codex handoff
→ Codex 实现
   ├─ 普通实现失败：RETURN_TO_CODEX
   └─ 需要改变冻结语义：原 PASS 失效，同 task 回 Planner
→ 实现后最终评估前独立安全门
   ├─ REVISE
   └─ PROCEED_TO_FINAL_EVALUATION
→ 最终候选/评估：CANDIDATE_ACCEPTED
→ RELEASE_READY
→ RELEASED
```

每个 Planner/Critic 人工轮次都先给一屏用户摘要，再给机器交接。用户不需要读内部 prompt 才知道任务发生了什么。

## 10. 拟修改的 canonical owner

若 v0.3 获 Critic `PROCEED`，Planner 下一步形成正式合同修改执行包，只修改：

1. `docs/workflows/PLANNER_ROLE_CONTRACT.md`
2. `docs/workflows/CRITIC_ROLE_CONTRACT.md`
3. `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
4. AI Research Stack Project setting 候选
5. `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md`

不修改 Bridge Kit、Slurm Workflows、Delivery Assurance、workflow-core 或 Clear Writing 产品实现。

## 11. Critic 本轮审查问题

本轮仍只是设计审查，因此结论只能是 `PROCEED` 或 `REVISE`，不得给 PASS。

必须判断：

1. PI-01 是否被关闭，同时没有取消现行实现后最终评估前的独立安全门；
2. PI-02 是否同时覆盖正向能力、跨组件成功链和风险匹配的关键失败链，又没有膨胀成全故障矩阵；
3. PI-03 是否给出了唯一 PASS 失效后的明确重开语义，同时没有新增 successor、epoch 或状态机；
4. 用户摘要 + 机器交接双层输出，是否足以让用户不再机械复制而不知道这一轮发生了什么；
5. Clear Writing 是否被放在正确位置：作为用户摘要的最后表达检查，而不是替代技术语义合同；
6. v0.3 是否仍然保持轻量，没有新增不必要治理层；
7. Bridge 与 Slurm 两类真实事故是否都会被新合同更早发现。

## 12. 当前权限与下一步

本轮只提交 Proposal v0.3，不修改正式合同、不修改当前 ChatGPT Web Project setting、不实施任何产品代码。

维护看板当前仍未实际同步；不要求用户手工维护。

下一入口：独立 Critic 对 v0.3 做设计复核，结论只能为 `PROCEED` 或 `REVISE`。
