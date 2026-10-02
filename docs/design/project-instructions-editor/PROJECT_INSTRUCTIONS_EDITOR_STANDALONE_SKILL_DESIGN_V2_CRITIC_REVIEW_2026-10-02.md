# Project Instructions Editor — Standalone Skill Design v2 Critic Review

Date: 2026-10-02  
Result: `PASS`  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch/ref: `main`  
Main observed before this review: `5163b43538f9611cc0d61fa8b62b99760e43d918`  
Reviewed proposal: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`  
Proposal version: `v2`  
Proposal + canonical TODO package commit: `d9a6d782fe3374fe260a276ec06f2c1b206d421a`  
Proposal blob on reviewed main: `dad4f3315a42819e158bebe78ef2ce75789bc3c6`  
Prior Critic review: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_CRITIC_REVIEW_2026-10-02.md`  
Prior Critic review commit: `e6ee48e9c84d5e79803b497e6a5774dc31271465`  
Tracking: `#93`  
Review stage: standalone Skill product/design v2 review after prior REVISE

```text
CRITIC_RESULT=PASS
B1=CLOSED
B2=CLOSED
B3=CLOSED
B4=CLOSED
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

## 1. 结论

v2 已经充分关闭 v1 的 B1–B4，且没有因为返修引入新的实质架构风险。

Standalone Skill 方向仍成立。当前产品核心已经能用一个相对轻量的推理链描述：先确认编辑模式和真实基线，再只读取与当前修改相关的历史/事实来源，分别判断语义归属与当前 Project 的实际生效位置，默认选择最小修改范围，保护既有语义和“缺席语义”，最后在真实字符预算下去重或使用定位入口，并输出可审修改与完整候选（仅在安全时）。

这仍是一个 Skill 级语义判断能力，不需要新的 Plugin、数据库、历史账本、守护进程、监控器、后台同步服务或第二套状态机。

本次 PASS 只批准继续后续 standalone Skill 设计与实现前冻结准备。它不授权当前实现，不创建 implementation Goal 或 Kickoff，也不批准发布、安装、版本、Marketplace、profile 或生产入口变化。

## 2. B1 closure — replacement mode

`CLOSED`.

v2 已经把两种原本混在一起的完整输出语义拆开。

### preservation-sensitive replacement

已有 Project setting，且用户没有明确授权丢弃未涉及语义时：

- 必须取得完整可编辑、语义足够精确的 live baseline；
- 未授权区域默认保留；
- 完整替换稿必须从该 baseline 推导；
- 拿不到 baseline 时只能给建议、局部 clause 或 placement/locator 建议，不能声称完整替换保留了未知旧语义。

### greenfield / explicit-reset replacement

Project setting 已确认为空，或当前用户明确决定废弃旧 setting、从零重建且不要求旧 Project-setting 语义保真时：

- 可以在没有旧 baseline 的情况下生成完整 setting；
- 不能声称保留了未知旧规则；
- reset 只解除当前 Project-setting 的 preservation obligation，不覆盖 system/workspace/repo authority、安全、权限或当前其他有效要求。

关键边界也已经补齐：模糊的“重新写得更好”不会被自动解释成 reset；当 edit mode 的差异会改变 preservation obligation 时，只要求最小澄清。

未来 Case I 能直接暴露两种相反失败：合法 greenfield/reset 被机械挡住，或含糊重写被误判为 reset。

因此 B1 已关闭。

## 3. B2 closure — semantic ownership vs effective enforcement placement

`CLOSED`.

v2 已经把两个不同问题明确拆开：

1. canonical / semantic ownership：详细、当前、可维护的真相由哪里拥有；
2. effective enforcement placement：为了让当前 Project 实际受到约束，Project setting 是否仍需直接常驻语义、短 bridge/trigger，或可以完全留在外部 source。

这解决了 v1 的关键漏洞：规则在概念上属于 global/user/repo 层，不代表它可以从 Project setting 删除。

v2 对 ownership/routing、authority/permission、safety/privacy/distribution、evidence/completion、用户阅读/输出契约及 lookup-before-action 语义都要求优先判断实际生效位置；locator substitution 只有在 lookup 不会太晚、Project 保留必要 trigger、且移出 detail 不削弱 mandatory/optional、authority、安全、证据和不确定性时才成立。

Future Case J 也直接要求观察实际 Project behavior，而不是只验证候选文本里是否出现某句话。

因此 B2 已关闭。

## 4. B3 closure — protected absence under partial history

`CLOSED`.

v2 保留 targeted history，没有把每次编辑升级成全 Project history audit。

同时新增的 protected absence 足以覆盖上一轮指出的真实失败：

当相关历史不可得或只有部分结果时，如果一条 durable rule：

- 当前 live baseline 中不存在；并且
- 只出现在旧 Candidate / Reference / summary / historical generated setting 中，

则当前 edit 默认保持 absent，不能仅凭旧 evidence 恢复。

允许突破这个默认的只有两类当前授权：

1. current user explicit add/re-adopt；
2. 当前任务明确要求同步 named canonical source，且该 source 的当前 authority/content 直接支持该项，并且同步范围覆盖该项。

这没有演化成 tombstone registry。分类只服务当前 edit，不持久化；bounded edit 的未涉及区域保持原样，也不会因为 protected absence 反而扩大历史搜索。

此外，B2 的 effective placement 判断仍继续约束 canonical sync：即使某 canonical source 拥有详细规则，也不等于该 detail 自动应该重新常驻 Project。

Future Case K 能直接暴露 old-only removed rule 被复活的问题。

因此 B3 已关闭。

## 5. B4 closure — normal entry and near-miss routing

`CLOSED`.

v2 不再只验证“Skill 已经被强制调用以后是否做对”。

Future Case L 明确要求：

- 普通用户自然请求编辑 Project instructions，不点名 `project-instructions-editor`，也应从正常入口进入正确能力；
- forced invocation 不能替代 normal-entry 证明；
- 邻近任务继续由原 owner 处理：
  - 普通中文润色 -> `chinese-prose`
  - 普通写作保真 -> `writing-fidelity`
  - 科学/技术文档结构重写 -> `scientific-rewrite`
  - AI_Skills_Collection 仓库维护 -> `ai-skills-core`
  - 复杂任务过程控制 -> `workflow-core`

Future Reviewer 还必须看到完整自然 user request、编辑任务所需的完整 live/history/source/budget 输入、完整候选或完整 no-op/advice result，并做定性判断。route receipt、字符数、diff、关键词不能单独证明产品能力。

当前阶段没有提前写 trigger eval，也没有规定固定样本数或机械 Gate 数量，这与 `docs/SKILL_AUTHORING.md` 和 Capability Gate policy 的方向一致。

因此 B4 已关闭。

## 6. v1 已成立方向复核

没有发现 v2 对已成立设计造成回归。

继续成立：

- standalone Skill 有独立产品价值；
- bounded edit 默认；
- full rewrite 只能由真实跨范围原因或明确 reset/greenfield 语义触发；
- recent thread 不因 recency 自动获得更多 instruction budget；
- exact identifier 与普通语言分层；
- locator 不能移走 lookup 前必须生效的关键治理语义；
- 约 8,000 字符只作为历史 Project 使用约束，不是统一产品常数；
- budget 按实际限制、semantic density 和 Project-specific headroom 判断；
- 不设固定 reserve 百分比或 scope 比例；
- no-op 是合法结果；
- qualitative full-output review 是必要证据；
- A–L 只是未来 regression/task-family directions，不是固定 12 个 Capability Gates；
- 不创建 database / ledger / daemon / watcher / history state machine。

现有 Skill owner 边界也仍然清楚，没有新证据支持把该能力合并回 `chinese-prose` 或 `writing-fidelity`。

## 7. 独立外部核查

2026-10-02 重新核对了 OpenAI 当前官方资料：

- OpenAI Help Center — Projects in ChatGPT  
  https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Help Center — ChatGPT Custom Instructions  
  https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions
- OpenAI Help Center — Memory in ChatGPT  
  https://help.openai.com/en/articles/8590148-memory-in-chatgpt

核查结论：

1. Project instructions 只在对应 Project 内适用，并覆盖 global custom instructions。v2 的 effective-enforcement 设计与当前产品行为一致。
2. Projects 的 memory/context 行为取决于 memory mode、plan/workspace setting 等条件。Project-only memory 下，同一 Project 的 chats 可以相互引用，但官方同时明确 Project memory 不提供类似个人 Memory 的完整“记忆列表”。因此“targeted history + honest degradation”是合理设计；不能假设 Skill 可以穷尽枚举全部历史。
3. 当前官方 Projects 文档的 instructions / plans-and-limits 内容没有给出一个可验证的统一 Project-instruction 字符上限。正确表述仍然是“当前未从官方 Projects 文档核实到统一上限”，不是“官方证明不存在限制”。
4. 当前官方 global Custom Instructions 文档单独给出其字符限制；这是不同产品表面，不能推导成 Project instructions 的限制。

没有外部事实要求修改 v2。

## 8. 复杂度判断

v2 没有过重。

B1–B4 的返修都落在同一条短 reasoning sequence 内，没有新增 persistent schema、数据库、历史索引、tombstone registry、守护进程或控制面。

当前合理的最小序列是：

```text
确认 edit mode / baseline obligation
-> 定向读取相关 history/source
-> 判断 semantic ownership + effective enforcement
-> 选择最小 mutation radius
-> 保护 invariants + protected absence
-> 在真实 budget 下去重/locator 化
-> 输出可审 edit + clean candidate（仅在安全时）
```

不需要继续为了“更保险”添加新阶段。

## 9. Maintenance state

Current main 已确认：

- canonical TODO 含 `tracking: #93`；
- Issue #93 仍为 open；
- labels 为：
  - `maintenance-track`
  - `kind:new-capability`
  - `scope:standalone-skill`
  - `area:standalone-skill`
- Issue reader-facing body 仍停留在较早设计阶段。

Planner 没有在缺少可验证 Clear Writing invocation surface 时实质改写 Issue body，符合 `AI_SKILLS_MAINTENANCE_BOARD.md`。

当前 Critic surface 同样没有可验证的已安装 Clear Writing / `writing-style` 调用入口，因此本轮不修改 Issue body：

```text
CLEAR_WRITING_UNAVAILABLE
```

当前工具也没有 GitHub Project field mutation surface，因此不能声称 Project 已同步。

Exact pending Project mutation：

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current design anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md
```

下一次真正可调用 Clear Writing 的 maintenance action 应把 Issue reader-facing copy 更新到“v2 Critic PASS、进入实现前设计冻结准备”的真实状态；不要要求用户手工维护 Project 卡片。

## 10. PASS boundary and next handoff

本次 PASS 只批准：

- standalone Skill 产品/架构设计 v2；
- 继续后续设计；
- 由 Planner 判断是否已经成熟到进入 implementation-before-freeze / execution-package planning 阶段。

本次 PASS 不批准：

- Skill implementation；
- 创建 Skill directory / `SKILL.md` / `agents/openai.yaml` / trigger eval；
- Plugin；
- implementation Goal；
- Kickoff；
- README / VERSION / registry / catalog / Marketplace / profile / release；
- 安装或生产发布；
- 付费调用；
- 任何新的用户授权。

下一 handoff 仍为 Planner。

```text
CRITIC_RESULT=PASS
B1=CLOSED
B2=CLOSED
B3=CLOSED
B4=CLOSED
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
NEXT_HANDOFF=PLANNER
```
