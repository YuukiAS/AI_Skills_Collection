# Project Instructions Editor — Standalone Skill Design Planner Proposal v2

Date: 2026-10-02  
Status: DRAFT_FOR_CRITIC_REVIEW  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch: `main`  
Reviewed predecessor: `PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_PLANNER_PROPOSAL_2026-10-01.md`  
Prior Critic review: `PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V1_CRITIC_REVIEW_2026-10-02.md`  
Prior Critic result: `REVISE`  
Tracking: #93  
Design topic: `project-instructions-editor--standalone-skill-design`  
Candidate future standalone Skill: `project-instructions-editor`

```text
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

本文件是完整 v2 Proposal，取代 v1 作为当前 standalone Skill 产品/架构设计锚点。它只处理 Critic 对 v1 的 B1–B4，并保留 v1 已成立的主架构；不授权 Skill 实现、Plugin、trigger eval、README/VERSION/registry/catalog/Marketplace/profile/release、implementation Goal 或 Kickoff。

## 0. Planner 对 B1–B4 的正式回应

### B1 — ACCEPT

Critic 指出 v1 把“需要保留已有语义的完整替换”和“新建/明确重置后的完整生成”混成一个门禁，这是成立的。

v2 明确拆分：

1. **preservation-sensitive replacement**：已有 Project setting，用户要求修改但未授权丢弃其余语义。此时必须取得足够精确、语义完整的当前 live baseline，才能生成并声称“未授权部分被保留”的完整替换稿。
2. **greenfield / explicit-reset replacement**：Project 已确认没有既有 setting，或用户当前明确要求废弃旧 Project setting、从零重建，且不要求旧语义保真。此时可以生成完整 setting，不需要旧 baseline 作为 preservation gate，但不得声称保留了未知旧规则。

这里的“足够精确”是指当前 live setting 的完整可编辑内容足以逐项恢复和保护其语义，不要求为无语义差异的空白/序列化格式建立字节级比较协议。

新增未来验收方向 I，用于验证 greenfield / explicit-reset 不会被错误挡住，同时不削弱 preservation-sensitive replacement 的 baseline 门禁。

### B2 — ACCEPT

Critic 对“语义归属”和“实际生效位置”的区分是必要补充。

OpenAI 当前官方 Projects 文档明确说明：Project instructions 只在对应 Project 内应用，并覆盖 global custom instructions。因此一条规则即使在概念上属于 global/user 层，也不能仅凭 semantic ownership 被移出 Project；如果它仍必须在当前 Project 中约束行为，Project setting 可能需要保留直接语义、短 bridge 或 lookup trigger。

v2 新增两个独立问题：

- **canonical / semantic ownership**：详细真相由哪个 source/layer 维护；
- **effective enforcement placement**：为了让当前 Project 实际受约束，哪些语义必须常驻 Project setting，哪些可只保留短 bridge/trigger，哪些才可以完全留在外部 source。

这只是当前 edit 的语义判断，不新增数据库、schema、ledger 或状态机。

新增未来验收方向 J，覆盖 global preference 与 Project instructions 发生 precedence/override 时的实际控制边界。

### B3 — ACCEPT

v1 的 targeted history 原则继续保留，但 Critic 指出的“历史不可得时，过去被删除的规则可能通过旧 Candidate/Reference 被复活”是真实风险。

v2 增加 **protected absence**：

当 relevant history 不可得或只部分可得时，只要一条 durable rule：

- 当前 live baseline 中不存在；并且
- 仅出现在旧 Candidate、Reference、summary 或其他历史派生材料中，

它在当前 edit 中默认视为受保护的“缺席语义”，不得仅凭旧 evidence 重新加入。

只有两类明确授权可以打破该默认：

1. 当前用户明确要求或重新决定加入该规则；
2. 当前任务明确要求同步某个 canonical source，且该 source 确实拥有这项当前规则/事实，并且同步范围授权覆盖该项。

这不是永久 tombstone，也不要求穷尽历史。bounded edit 的未涉及部分继续保持不动。

新增未来验收方向 K，覆盖 history unavailable + old candidate contains removed rule。

### B4 — ACCEPT

v1 的 A–H 主要测试“Skill 已经在处理 Project instruction edit 后做得对不对”，没有证明 standalone Skill 的普通入口和邻近任务边界。

v2 保留 A–H，并新增未来验收方向 L：

- 普通用户用自然语言要求编辑 Project instructions，不点名 `project-instructions-editor`，应能进入正确能力；
- 普通中文润色继续属于 `chinese-prose`；
- 普通写作保真继续属于 `writing-fidelity`；
- 科学/技术文档结构重写继续属于 `scientific-rewrite`；
- AI_Skills_Collection 仓库维护继续属于 `ai-skills-core`；
- 复杂任务流程控制继续属于 `workflow-core`。

现在不写 trigger eval、不实现 routing、不规定固定样本数，也不建立正式 Capability Gate Matrix。未来 route receipt、字符数、diff 或关键词只能是机械证据，不能单独证明 normal-entry 产品能力；Reviewer 必须能看到判断所需的完整输入和完整候选，并做定性评审。

## 1. v2 产品结论

standalone Skill 主方向不变。

`project-instructions-editor` 的核心产品不是“把 Project instructions 写得更好看”，而是：

> 在一个长期 ChatGPT Project 中，根据当前编辑意图，协调实际 live Project setting、相关历史决定、canonical project sources、Project 内真实生效层级和有限字符预算，决定哪些长期语义应该驻留、哪些应该变成 locator/bridge、哪些应该留在 task/thread/global/canonical source，并以最小充分修改保护未授权语义。

现有证据仍来自至少两个性质不同的真实 Project family：

1. shared STAT5050/STAT5060 Project：局部新增导致多 scope 失衡、详细 workflow 复制、字符预算压力；
2. AI Research Stack：旧 repo Candidate 落后于 live setting，可能覆盖后来已接受的治理语义；反复围绕中文可读性微调还显示了单题过拟合和边际收益下降。

这两个 failure family 都超出普通 prose polishing 或单一 fidelity guardrail。

因此当前最轻且足够完整的产品形态仍是一个 standalone Skill，而不是新 Plugin、daemon、watcher、数据库、历史账本或第二套 Project 控制面。

## 2. 当前事实边界

### 2.1 OpenAI Projects 的当前行为

2026-10-02 重新核对官方资料：

- OpenAI Help Center 的 “Projects in ChatGPT” 明确说明 Project instructions 只在该 Project 内应用，并覆盖 global custom instructions。
- 同一官方文档说明 Projects 可以使用 chats/files 作为持续上下文；Project-only memory 下，同一 Project 内 chats 可以相互引用，Project 外对话不能进入该 Project 的上下文。
- Project memory、plan/workspace 和具体可用上下文存在产品表面差异，因此 Skill 不得把“所有历史一定能枚举”当作前提。

设计影响：

- B2 的 effective enforcement placement 是必要产品判断；
- history 只能是与当前 edit 相关的 targeted retrieval + honest degradation，不能假设完整历史读取永远可用。

### 2.2 字符限制

截至本轮核查，官方 Projects 文档没有给出一个可验证的统一 Project-instruction 字符限制。

这只能支持：

> 当前没有从官方 Projects 文档核实到统一 Project-instruction 上限。

它不能被升级为“官方证明 Project instructions 没有字符限制”。

OpenAI 当前对 global Custom Instructions 单独公布字符限制；该产品表面的限制不能作为 Project instructions 的上限证据。

因此 v2 继续把 budget 作为 active Project/user/actual UI 输入：

- 已知真实上限时：使用该上限；
- 用户给出规划预算时：按该 Project 的规划预算处理；
- 最大值未知时：只报告 current length、candidate length、delta 和可观察 margin，不声称符合未知硬限制。

约 8,000 字符继续只作为过去真实 Project 使用约束的 evidence，不是统一常数。

## 3. 与现有 Skills / Plugins 的边界

### 3.1 `chinese-prose`

负责已确定语义后的自然中文实现与最终可读性。

不负责：

- Project resident / locator / task-local placement；
- live setting 与历史的权威协调；
- 多 scope instruction budget；
- replacement safety；
- global semantic ownership 与 Project effective placement 的差异。

`project-instructions-editor` 可以在中文交付阶段使用其表达能力，但 placement 决策必须先由 Project editor 完成。

### 3.2 `writing-fidelity`

负责编辑过程中的事实、纠正、版本 authority、exact span、artifact identity 等保真。

它仍然不负责：

- 多来源中谁拥有 Project-level placement；
- 是否把一条 rule 留在 Project、改成 locator 或留 task-local；
- multi-scope budget；
- live/history/canonical-source reconciliation；
- Project/global precedence 下的 enforcement placement。

v2 复用其“保护已有明确纠正和语义强度”的原则，但不把 Project placement owner 塞入 fidelity Skill。

### 3.3 `scientific-rewrite`

负责已有科学/技术材料的 source-faithful 结构重写。其对象是 reader-facing scientific/technical document，不是长期 Project control surface。

Project instructions 中若塞入长 scientific document，优先判断它是否应移回 canonical source，而不是把 Meaning Map / Reader Plan 等重写架构搬入 Project editor。

### 3.4 `workflow-core`

只在当前 Project editing task 本身复杂或高风险时拥有过程、routing、gate、evidence 与 completion semantics。

它不判断具体 instruction 该常驻、locator 化还是移出 Project。

### 3.5 `ai-skills-core`

只负责以后在 AI_Skills_Collection 中实现、生成、回归、版本、changelog、Marketplace/profile 和 release 维护。

它不是普通用户编辑 Project instructions 的 runtime domain owner。

### 3.6 独立性结论

职责划分保持：

- 写作 Skills：怎样表达；
- fidelity：不能破坏什么；
- workflow-core：复杂任务怎样执行/验证；
- ai-skills-core：AI_Skills repo 怎样维护/发布；
- project-instructions-editor：长期 Project instruction surface 应保存什么、从哪里读取、当前 Project 中怎样实际生效，以及在有限预算下怎样安全修改。

因此没有新的证据支持把 standalone Skill 合并回现有写作 Skill。

## 4. v2 输入模型

v2 仍使用五类 primary inputs，不创建持久 schema。

| 输入 | preservation-sensitive edit | greenfield / explicit reset | 获取与缺失处理 |
|---|---|---|---|
| 当前 live Project setting | 必需；完整替换/删除/跨段重排前必须取得足够精确、语义完整的 baseline | greenfield 已确认空时不需要旧 baseline；explicit reset 不以旧 baseline 作为 preservation gate | 优先使用真实 Project setting surface；否则用户提供 exact text/export。拿不到时只能 bounded advice/local clause，不能声称保留未知旧语义。 |
| relevant Project history | 对受影响的 durable decision 做 targeted lookup；高风险删除/重构时更重要 | greenfield 通常无旧 history obligation；explicit reset 不保护已明确废弃的旧 Project-setting semantics，但仍尊重当前用户指令和更高层约束 | 获取不到时使用 protected-absence rule，并诚实标记非 exhaustive。 |
| canonical project sources | 当 edit 涉及 repo-owned ownership/policy/workflow/current fact 时必需 | 构建新 setting 时同样按需读取 | 无法读取时不发明 current rule；保留/生成时明确未验证 locator/fact。 |
| current edit request | 总是必需 | 总是必需；explicit reset 必须是当前明确决定 | 定义 mutation scope，不能静默扩大成 unrelated rewrite。 |
| instruction budget | 有 hard-limit/headroom claim 时必需 | 同样 | 未知最大值时只报 current/candidate length 与 delta，不声称符合未知上限。 |

另外临时形成一个当前 edit 的 scope/authority/enforcement map，用于推理，不持久化为 database/ledger/state machine。

## 5. replacement semantics：关闭 B1

### 5.1 preservation-sensitive replacement

满足任一情形时属于此类：

- 已有 setting，用户要求“修改/补充/优化”；
- 用户没有明确授权丢弃未涉及规则；
- 输出将被描述为“保留现有正确内容”“安全替换”“完整更新版”；
- edit 需要删除、移动或重排现有 rule。

要求：

1. 取得当前 live setting 的完整可编辑基线；
2. 将 current request 的 mutation scope 与其余语义分开；
3. 未授权区域默认 preservation；
4. relevant history 部分不可得时应用 protected absence；
5. full clean replacement 必须从该 baseline 推导。

没有 baseline 时：

- 可以解释应该怎样改；
- 可以给一段新 clause；
- 可以给 locator/placement 建议；
- 可以要求用户提供 current setting；
- 不能声称完整替换稿保留了未知现有语义。

### 5.2 greenfield replacement

只有 Project setting 已确认为空/不存在时适用。

允许：

- 根据 current request、canonical sources、必要 Project context 和实际 budget 直接生成完整初始 setting；
- 不需要旧 baseline 作为 preservation gate。

不得声称：

- “保留了旧规则”；
- “没有删掉任何旧语义”；

因为没有旧语义需要证明。

### 5.3 explicit-reset replacement

只有当前用户明确表达类似以下产品决定时适用：

- 废弃当前 Project setting；
- 从零重建；
- 不要求保存旧 Project-setting 语义。

这不是通过模糊意图推断得到的许可。

即使 explicit reset：

- system/workspace/repo authority 和当前用户的其他有效要求仍然存在；
- reset 只改变本次 Project-setting preservation obligation；
- 不代表可以绕过安全、权限或更高层产品约束；
- 输出不得声称“保留了未知旧 Project rules”。

若用户说“重新写得更好”但同时要求保留已有规则，这仍是 preservation-sensitive，不是 reset。

## 6. canonical ownership 与 effective enforcement placement：关闭 B2

每条受影响的 durable rule 都回答两个独立问题。

### 6.1 canonical / semantic ownership

问：

> 这条规则的详细、当前、可维护真相由哪里拥有？

可能是：

- current Project setting 本身；
- global/user preference；
- canonical repo 的 AGENTS/policy/Goal/TODO/design；
- institution/workspace policy；
- 当前 task/thread；
- 其他稳定 source。

这个判断解决“以后去哪里更新”和“详细内容是否应该重复复制”。

### 6.2 effective enforcement placement

再问：

> 为了让当前 Project 在真正使用时受到约束，这条语义必须出现在哪里？

可能结果：

1. **Project-resident full/compact semantic rule**  
   在任何 source lookup 前就必须影响行为，且不能依赖外部层仍然有效。
2. **Project-resident bridge/trigger + canonical source**  
   Project 必须常驻一个短 trigger，确保在相关情形先读取/遵循 canonical source；详细 rule 留 source。
3. **Canonical/source only**  
   当前 Project 无需在 lookup 前受这条 rule 约束，或已验证另一个实际层仍能有效约束；Project 可不复制。
4. **Task/thread only**  
   只属于一次任务，不应永久污染 Project。
5. **No placement**  
   重复、过期、被拒绝、unsupported。

### 6.3 必须优先检查 effective placement 的语义

尤其包括：

- ownership/routing；
- authority/permission；
- safety/privacy/distribution；
- evidence/completion strength；
- 用户阅读/输出契约；
- 任何决定“先不先 lookup / 可不可以行动”的前置规则。

典型例：

- 一个详细 workflow 的 canonical owner 在 repo，但 Project 必须保留“遇到 X 时先读取 Y，并在读取前不要执行 Z”的 bridge。
- 一个用户全局阅读偏好在 semantic ownership 上属于 global instructions，但当前官方产品行为显示 Project instructions 会覆盖 global custom instructions，因此若该偏好在当前 Project 仍是 hard requirement，Project 需要保留必要 bridge/semantic subset，而不能仅写“见 global preference”。

### 6.4 locator substitution 的限制

locator 只有在以下条件同时成立时才能替换 detail：

- locator 稳定且可解析；
- lookup 本身不会发生得太晚；
- 被移出的 detail 不需要在 lookup 前直接约束；
- Project 内保留了必要 trigger；
- 删除 detail 不会改变 mandatory/optional、authority、安全、证据或不确定性。

## 7. targeted history 与 protected absence：关闭 B3

### 7.1 targeted history 保持不变

不做 exhaustive Project-history audit。

只检索与当前 mutation 直接有关的：

- explicit acceptance；
- explicit deletion/rejection；
- repeated correction；
- durable ownership/authority decision；
- 明确标为 temporary 的旧要求。

搜索范围由当前 edit 决定，不由“整个 Project 很重要”决定。

### 7.2 protected absence

当 relevant history 无法取得或只有部分结果时，使用当前 edit 的保守 provenance/diff 规则：

若 durable rule 同时满足：

- live baseline 中不存在；
- 只在旧 Candidate / Reference / summary / historical generated setting 中出现；

则默认：

```text
PROTECTED_ABSENCE_FOR_CURRENT_EDIT
```

这只是 Proposal 中的人类可读语义，不是未来必须实现的状态 token/schema。

默认行为：不重新加入。

允许引入只有：

1. current user explicit add/re-adopt；
2. current task explicitly requests synchronization with a named canonical source，并且该 source 的当前内容和 authority 能直接支持这项 rule/fact。

“它以前看起来很有用”“旧 proposal 写过”“summary 还记得”都不够。

### 7.3 bounded edit 的保护

与本次 edit 无关的区域：

- 不主动重新解释 absence；
- 不为“确保没有遗漏”扩大 history 搜索；
- 不从旧 candidate 恢复缺失条目；
- 保持 live baseline 原样。

### 7.4 full rewrite 中的保护

preservation-sensitive full rewrite 即使需要全局去重/relocation，也不能把 historical generated material 当“缺失规则补全库”。

如果 history partial：

- 现存 live semantics 可以 reorganize，但必须保持强度；
- old-only absent rule 默认不引入；
- canonical source 同步仅限当前明确同步 scope。

## 8. 核心编辑决策模型 v2

v2 仍保持短 reasoning sequence，不增加第二工作流。

### Step 0 — 确认 edit mode

先判定：

- preservation-sensitive；
- greenfield；
- explicit reset。

无法判断且差异会改变 preservation obligation 时，才需要最小澄清。

### Step 1 — 取得 baseline 或确认 baseline 不需要

- preservation-sensitive：必须有 live baseline；
- greenfield：确认空；
- explicit reset：确认当前 reset 决定。

### Step 2 — 定向读取 relevant history / canonical source

只读取能改变当前 edit 的 evidence。

history 不完整时启用 protected absence，不升级成 full-history audit。

### Step 3 — 对受影响语义同时判断 ownership 与 enforcement

先确认 canonical owner，再确认当前 Project 中必须常驻的控制语义。

### Step 4 — 选择 placement

当前 edit 中每个语义单位只作一次临时 disposition：

- Project resident；
- Project bridge/trigger + locator；
- canonical/source only；
- task/thread only；
- another effective layer；
- omit/no change。

不持久化这些分类。

### Step 5 — 选择 mutation radius

默认 bounded edit。

只有真实跨范围原因才升级 full rewrite/restructure；v1 的触发条件保持不变。

### Step 6 — 保护 invariants 与 protected absence

检查：

- mandatory/optional；
- triggers/escalation；
- permission/authorization；
- safety/privacy/distribution；
- evidence/completion；
- role ownership；
- uncertainty/negative result；
- exact identifiers；
- explicit accepted/deleted decisions；
- partial-history 下的 absence。

### Step 7 — 在真实 budget 下去重/locator 化

优先：

- 删除真正重复；
- 提升跨 scope 的共享 durable rule；
- 把可检索 detail 移回 canonical source；
- 保留有效 bridge；
- 不用削弱强制语义换字符。

### Step 8 — 交付 proportional diff + clean candidate

只有在安全时给完整 clean setting。

## 9. 字符预算策略

v1 保持不变，仅收紧事实表述。

每次 edit 区分：

- current length；
- known actual hard limit（若真实可得）；
- user/project planning budget；
- desired headroom（若用户或 Project 有实际要求）；
- candidate length；
- delta；
- remaining observable margin。

不使用：

- 固定 8,000；
- 固定 reserve 百分比；
- 固定各 scope 百分比；
- “越短越好”评分。

优先长期驻留：

- Project purpose/scope；
- durable ownership/routing；
- authority/permission/safety；
- evidence/completion；
- durable product/research philosophy；
- 必须 Project-local enforcement 的 response contract；
- stable bridge/locator。

优先移出：

- repo 已有的详细 SOP；
- build commands；
- exhaustive tool inventory；
- current branch/job/version status；
- repeated review checklist；
- volatile facts；
- 单一 thread 的实现细节；
- 只是演示已有 rule 的 examples。

如果一个小增加只有删除无关语义才能塞进 budget，不能静默删；这才是“需要更大重构/重新分配”证据。

## 10. bounded edit / full rewrite 边界

v1 继续成立。

### 10.1 bounded edit 默认

适用于：

- 局部新增/删除/纠错；
- live baseline 可得（preservation-sensitive 时）；
- 不产生跨 scope 矛盾；
- 可通过 local dedup / locator substitution 解决；
- 现有整体架构仍可用。

### 10.2 full rewrite/restructure 可提出

仅当：

- current user 明确要求；
- 存在局部修复无法关闭的跨范围矛盾；
- copied workflow detail 已经普遍污染；
- multi-scope 实质失衡；
- budget 只有通过全局去重/relocation 才能满足必要 durable semantics；
- 多处 source ownership / locator 已经漂移或冲突。

### 10.3 full rewrite 仍被阻止的条件

对于 preservation-sensitive：

- live baseline 不可得；
- 关键 current facts 无法验证；
- 当前要求不足以授权全局 mutation。

对于 greenfield / explicit reset，旧 baseline 缺失本身不再是 blocker；但 current scope、canonical sources 和实际 budget 仍应按任务需要确认。

## 11. 多来源关系 v2

不使用“单一总排名”解决所有冲突，而是按角色处理：

1. **current user request**：定义当前 edit 和当前新决定；
2. **live Project setting**：preservation-sensitive edit 的 concrete baseline；
3. **relevant explicit history**：解释 accepted/rejected/temporary/durable decisions；
4. **canonical current source**：拥有 repo/document detail、dynamic facts 和 source-owned policy；
5. **old candidate/reference/summary**：只作 supporting evidence，且在 partial history 下受 protected absence 限制。

新增一层判断：

6. **effective product precedence**：即使 semantic owner 在外部层，也必须确认当前 Project 实际是否还能受到它约束；不能只因 ownership “更干净”就移出 Project。

冲突规则：

- current explicit user decision 可以改变当前 Project-setting rule；
- old candidate 不能覆盖 live baseline；
- explicit deleted/rejected history 不能被旧 evidence 复活；
- history partial 时 old-only absent rule 默认保持缺席；
- canonical source 同步必须在 current task scope 内明确授权；
- recent thread 不因 recency 自动获得更多 budget；
- global semantic ownership 不等于 Project effective enforcement；
- exact product behavior 不确定时，不声称某外部层一定生效。

## 12. 用户交付形式

v1 的 proportional delivery 保留。

### 小型 bounded edit

默认给：

- 一段结构/语义判断；
- 清楚的删/增/改范围；
- 每个实质修改一条短理由；
- current/candidate length 与 delta；
- 关键 invariant 保持说明；
- preservation-sensitive 且 baseline 完整时，再给完整可复制 setting。

### medium edit

仅按风险增加：

- scope impact；
- locator/bridge substitution；
- effective enforcement 说明；
- multi-scope balance 变化；
- budget margin。

### full rewrite candidate

说明：

- edit mode：preservation-sensitive / greenfield / explicit reset；
- 为什么 bounded edit 不足，或为什么这是 greenfield/reset；
- 哪些 detail 转为 locator；
- 哪些 bridge 仍需 Project-resident；
- 重要 delete/add/move；
- semantic preservation boundary；
- budget 变化；
- clean replacement；
- 必要时小型 regression plan。

### no-op

继续是合法结果：

- 已被 live rule 覆盖；
- 应更新 canonical source 而不是 Project；
- 只属于 current task；
- 新增只会复制已有 locator-backed rule。

## 13. 未来真实验收设计

A–H 保留为 task families / regression directions，不等于八个 Capability Gates。

### A — stale repo candidate vs newer live setting

验证 live baseline 不被旧 Candidate 覆盖。

### B — multi-scope finite budget

使用 shared STAT5050/STAT5060 evidence，验证 scope balance、shared durable rule lifting、locator substitution 与真实 planning budget。

### C — explicit rejected/deleted rule resurrection

history 可得时，明确 deleted rule 不得复活。

### D — exact identity vs ordinary language

验证 exact machine/formal identity 与 ordinary explanation 分离。

### E — source-drift-controlled setting effect

固定相关 source commit/snapshot，区分 source drift 与 setting effect。

### F — missing live setting

preservation-sensitive edit 缺 baseline 时，必须降级为 advice/local clause，不伪造安全 replacement。

### G — no-op / should-not-change

已覆盖或不应 Project-resident 的请求，不制造无意义修改。

### H — language-independent placement

至少一个主要问题是 authority/budget/scope，而不是中文可读性，防止产品退化成 Chinese style editor。

### I — greenfield / explicit-reset complete setting

输入：

- Project 已确认为空；或
- 用户当前明确要求 discard old Project setting and rebuild。

要求：

- 允许生成完整 setting；
- 不要求旧 live baseline；
- 不虚假声称 preservation of unknown old rules；
- 仍遵守 current canonical source / budget / higher-level constraints。

失败：

- 机械要求旧 baseline 导致合法 greenfield/reset 被阻止；
- 把含糊“重写”误判为 reset，绕过 preservation。

### J — cross-layer precedence / effective enforcement

构造真实 Project where：

- 某 durable user preference 在 semantic ownership 上属于 global/user layer；
- Project instructions 有覆盖/优先作用；
- current Project 仍要求该 preference 有效。

要求：

- 不因 ownership 在 global 层就完全移出；
- Project 保留必要 direct semantic subset 或 bridge；
- canonical detail 不必全复制。

失败：

- “归属正确”但 Project 内实际失效。

### K — partial/unavailable history + old removed rule

输入：

- live baseline 不含 durable rule；
- relevant history 无法完整获取；
- old Candidate/Reference/summary 含该 rule。

要求：

- 默认保持 absence；
- 除非 current user explicit add/re-adopt，或 current task explicit canonical sync 且 source authority 支持。

失败：

- 仅凭 old evidence 重新加入。

### L — normal entry + near-miss routing boundary

正向：

普通用户自然说“帮我把这个 Project 的 instructions 更新一下，只补这条规则，不要弄坏原来的设置”之类，不点名 Skill，应进入 Project instruction editing capability。

near-miss / should-not-change：

- 普通中文润色 -> `chinese-prose`；
- 普通写作保真 -> `writing-fidelity`；
- scientific/technical document structural rewrite -> `scientific-rewrite`；
- AI_Skills_Collection repository maintenance -> `ai-skills-core`；
- complex task process/control -> `workflow-core`。

当前不规定 future eval query 文本、数量或固定比例。

未来 Reviewer 必须：

- 能看到 route decision 所依据的完整 user request；
- 对 editing case 能看到必要 live/history/source/budget inputs；
- 能看到完整候选或完整 no-op/advice result；
- 对 near-miss 检查实际 owner 是否正确；
- 做定性判断。

route receipt、字符数、diff、关键词扫描不能单独证明 route quality。

## 14. 验收纪律

未来实现阶段才设计正式 Capability Gate Matrix。

当前只冻结以下原则：

- normal entry 必须可用，不能只 forced invocation；
- known regression 可用于开发；
- final candidate 使用冻结输入/source refs；
- qualitative full-output review 必须真正看完整产物；
- semantic preservation、placement correctness、budget use、route correctness 分开判断；
- deterministic character/diff helper 只证明机械事实；
- 不挑 stochastic winner；
- 不用固定 sample count 代替风险判断；
- 当继续加规则在代表性任务上没有可辨识边际收益时停止微调。

## 15. Non-goals

v1 全部保留。

本 Skill 不是：

- Chinese prose polisher；
- banned-word/translation dictionary；
- keyword/English-ratio/paragraph/title/formula linter；
- style scorer；
- generic prompt optimizer；
- canonical repo policy generator；
- history database/tombstone database；
- decision ledger；
- watcher/daemon/scheduler/background sync；
- Planner/Critic state machine；
- GitHub Project sync service；
- Plugin/release tool；
- global custom instructions editor；
- 通过 route receipt 或 diff 冒充产品能力的 wrapper。

`protected absence` 只是当前 edit 的默认 provenance/diff 原则，不变成永久 tombstone registry。

## 16. 更简单的现实替代

### A. 继续纯手工编辑

对单一且很少变化的 Project 仍可行。

但当前已经出现跨两个 Project family 的重复 failure：live/repo drift、scope budget、history rejection、locator placement、effective enforcement。纯手工会重复同一类判断错误。

不作为长期唯一机制。

### B. 扩展 `chinese-prose` / `writing-fidelity`

仍不采用。

B2/B3 进一步表明问题涉及 Project effective precedence 和 historical absence provenance，不是 style/fidelity 本体。

这些 guardrail 可以被复用，但不应变成 Project placement owner。

### C. 只做 checklist/reference

可以作为未来 Skill 的 reference，但无法在实际 editing task 中协调 live setting、history、canonical source、Project precedence 和 budget。

不能替代用户入口。

### D. 新 control plane / history service

明确拒绝。

没有证据需要 database、ledger、daemon、watcher、persistent history index 或 Project state machine。

### v2 最小架构

未来若获 Critic PASS + 用户另行实现授权：

- 一个 standalone Skill；
- host model 做 semantic reasoning；
- 使用现有可用 Project/history/repo tools；
- 需要时复用 `writing-fidelity` / `chinese-prose`；
- 复杂 task 才由 `workflow-core` 管过程；
- AI_Skills repo 实现/发布才由 `ai-skills-core` 管维护；
- deterministic helper 如有必要最多负责 character count / diff，不负责 semantic keep/delete/placement。

## 17. 风险与降级

### live baseline 不可得

preservation-sensitive：停止 full replacement claim，降级 advice/local clause。

greenfield/reset：按对应 mode 继续，但不得声称旧语义保真。

### history partial/unavailable

启用 protected absence；不扩大成 exhaustive search。

### canonical source 不可达

不发明 current fact/rule；指出未验证边界。

### semantic owner 与 effective placement 不一致

以实际 Project enforcement requirement 决定是否保留 Project bridge/direct subset；不为了层级“干净”牺牲当前行为。

### hard budget 未知

只报 length/delta，不声称 hard-limit compliance。

### route ambiguity

只有确实会改变 product owner 时请求最小澄清；future normal-entry acceptance 要证明 near-miss 不被抢路由。

### full rewrite 开始吞掉 unrelated semantics

回到 bounded edit；除非已满足 full-rewrite trigger 或 explicit reset。

## 18. 本轮外部来源与采用决定

2026-10-02 定向核查官方 OpenAI sources：

1. OpenAI Help Center — Projects in ChatGPT  
   https://help.openai.com/en/articles/10169521-projects-in-chatgpt

   实际采用：
   - Project instructions only apply within the project and override global custom instructions；
   - Project chats/files can contribute context；
   - project-only memory changes cross-project context boundaries。

2. OpenAI Help Center — ChatGPT Custom Instructions  
   https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions

   实际采用：
   - global Custom Instructions 有自己的当前字符限制；
   - 该限制不被移植为 Project-instruction limit。

3. OpenAI Help Center — Memory in ChatGPT  
   https://help.openai.com/en/articles/8590148-memory-faq

   实际采用：
   - memory/context availability varies by product configuration；
   - 不把完整 history enumeration 作为 Skill 可用性的前提。

不采用：

- 任何将 global Custom Instructions 字符上限映射为 Project instructions 上限的推断；
- “官方未给 Project limit” => “Project 一定没有 limit”的推断；
- “Project 可以使用历史” => “Skill 一定能枚举全部历史”的推断。

## 19. Maintenance state

Canonical TODO 已含：

```text
tracking: #93
```

Issue #93 当前 labels 已核实：

```text
maintenance-track
kind:new-capability
scope:standalone-skill
area:standalone-skill
```

目标 Project lifecycle 仍为：

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current design anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md
```

当前工具表没有 GitHub Project field mutation surface，因此以上 Project mutation 仍是 exact pending mutation；不得声称已同步，也不要求用户手工拖卡片。

Issue #93 reader-facing body 仍落后于 standalone Skill design。

`AI_SKILLS_MAINTENANCE_BOARD.md` 要求实质修改 Issue copy 前真实调用当前安装的 Clear Writing（`writing-style`）。本轮 runtime 的可调用工具中没有 Clear Writing / `writing-style` / `chinese-prose` invocation surface，因此：

```text
CLEAR_WRITING_UNAVAILABLE
```

本轮不修改 Issue body。

待下一个真正可调用 Clear Writing 的 maintenance action 执行的 exact Issue-copy mutation：

```text
问题：
设计一个可跨 Project 复用的 Project instructions 编辑能力。核心不是中文润色，而是在 live setting、相关历史、canonical source、当前 Project 实际生效层级和有限字符预算之间做安全的 placement 与 bounded edit。

当前进度：
Standalone Skill 产品/架构 Proposal v2 已提交；Planner 已 ACCEPT 并关闭设计层面的 B1–B4，等待独立 Critic 复核。

当前执行锚点：
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md

下一步：
Critic 优先复核 B1–B4：replacement mode、semantic ownership vs effective enforcement、partial-history protected absence、normal-entry/near-miss acceptance。即使 PASS，也不得直接开始 Skill implementation。
```

注意：以上只是 pending copy source；真正写入 Issue 前仍须实际调用 Clear Writing，不得直接机械粘贴绕过 policy。

## 20. Critic review request

请 Critic 优先复核原 B1–B4 是否真正关闭，不要移动终点。

### B1

检查：

- preservation-sensitive replacement 是否仍严格要求 live baseline；
- greenfield / explicit reset 是否被合法放行；
- 是否存在通过模糊“重写”绕过 preservation 的漏洞。

### B2

检查：

- canonical ownership 与 effective enforcement placement 是否真正分开；
- global semantic ownership 是否仍可能导致 Project hard rule 被误删；
- locator substitution 是否保留 lookup-before-action trigger。

### B3

检查：

- protected absence 是否足以防旧 Candidate 复活未知删除规则；
- 是否仍保持 targeted history，而没有变成隐式 tombstone DB / exhaustive audit；
- explicit current add / explicit canonical sync exception 是否边界合理。

### B4

检查：

- future normal-entry direction 是否证明 standalone trigger surface；
- near-miss 是否覆盖邻近 Skills；
- 是否仍依赖 route receipt/字符/diff 这类机械证据冒充产品能力。

同时复核：

- v2 是否没有因四个 blocker 变成过重架构；
- A–L 是否只是 regression/task-family direction，而不是机械 Gate Matrix；
- no-op、bounded edit、budget、exact identifier、qualitative review 等 v1 已通过方向没有回归。

Critic PASS 只允许继续 future Skill design / 后续准备 implementation Plan。不得解释成 implementation authorization。

```text
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```
