# Project Instructions Editor — 实现前最终设计冻结 Proposal v1

Date: 2026-10-02  
Status: DRAFT_FOR_CRITIC_REVIEW  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch: `main`  
Approved product architecture: `PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`  
Approved architecture review: `PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_CRITIC_REVIEW_2026-10-02.md`  
Tracking: #93  
Design topic: `project-instructions-editor--standalone-skill-design`  
Candidate future standalone Skill: `project-instructions-editor`

```text
DESIGN_FREEZE_CANDIDATE=YES
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

本 Proposal 不重新设计 v2。它把已经通过独立 Critic 的产品架构收敛成实现前的最终产品合同：以后如果用户另行授权实现，Executor/实现 Planner 不再自行决定 Skill 的职责、触发边界、编辑模式、输入降级、Project 内实际生效位置、修改半径、交付合同或能力验收方向。

本轮仍然是 planning-only。不得创建 Skill、Plugin、`SKILL.md`、`agents/openai.yaml`、trigger eval、implementation Goal/Kickoff、README/VERSION/registry/catalog/Marketplace/profile/release 产物，也不授权 Codex implementation。

## 1. Planner 判断：已经成熟到进入最终设计冻结审查

当前没有继续阻止设计冻结的产品事实缺口。

理由：

1. v2 已经由独立 Critic PASS，B1–B4 全部关闭；
2. 用户目标、正常入口、输入模型、修改语义、降级边界、相邻 Skill owner、交付形式和真实验收方向都已经明确；
3. 当前剩余未定项主要是实现细节，例如 Skill 文件结构、最终 description 文案、是否需要机械字符计数/diff helper、具体 trigger eval 样本、安装/发布细节；这些不应反向阻塞产品设计冻结；
4. 不存在需要 database、history service、watcher、daemon、ledger 或新状态机才能成立的产品假设；
5. OpenAI 当前 Projects / Memory 产品事实没有出现要求修改 v2 的新证据。

因此本轮应提交最终设计冻结候选给 Critic，而不是继续增加抽象层。

## 2. 冻结后的唯一产品职责

`project-instructions-editor` 是长期 ChatGPT Project instruction surface 的语义编辑能力。

它负责：

- 判断当前任务是在创建、局部修改、压缩、同步还是重构 Project instructions；
- 在需要保留既有语义时，使用真实 live Project setting 作为基线；
- 只检索与当前修改有关的历史决定和 canonical sources；
- 区分一条规则的 semantic ownership 与它在当前 Project 中真正需要的 enforcement placement；
- 判断哪些语义应长期常驻 Project setting，哪些只需要短 bridge/locator，哪些应留在 canonical source、task/thread 或其他实际有效层；
- 默认执行最小充分 bounded edit；
- 保护用户已接受、已删除、已纠正和当前未授权修改的语义；
- 在有限字符预算下提高长期语义密度，而不是机械追求更短；
- 在输入不足时诚实降级，而不是编造安全的完整替换；
- 给用户可审查的变化说明与安全时可直接复制的完整 Project setting；
- 在正确结果是“不改 Project setting”时返回 no-op。

它不负责通用 Prompt 优化，也不负责普通文档写作。

## 3. 明确非职责

以下不属于该 Skill 的产品职责：

- 普通中文润色；
- 普通写作保真；
- 科学/技术文档结构重写；
- generic system prompt / agent prompt 优化；
- global Custom Instructions 编辑；
- AI_Skills_Collection 仓库维护；
- 复杂任务的过程控制、Planner/Critic 状态或执行收口；
- 自动同步 GitHub Project；
- 持久化 Project history；
- 建立删除项 tombstone registry；
- 自动监控 Project 变化；
- 后台同步、守护进程、数据库、ledger 或新状态机；
- 通过禁词、英文比例、固定字符比例、段落数、标题数或公式数判断质量。

相邻 owner 保持：

- `chinese-prose`：自然中文表达与最终中文可读性；
- `writing-fidelity`：一般写作保真 guardrail；
- `scientific-rewrite`：科学/技术文档结构性重写；
- `workflow-core`：复杂任务过程、验证与完成语义；
- `ai-skills-core`：以后该 Skill 在 AI_Skills_Collection 中的实现、生成、回归、版本和发布维护。

## 4. 普通用户触发边界

### 4.1 应触发的自然请求

用户不需要说 `project-instructions-editor`。

只要目标对象明确是长期 ChatGPT Project instructions / Project setting，并且用户要求以下任一真实编辑行为，就属于候选 normal entry：

- 新建 Project instructions；
- 在现有 setting 上新增、删除或纠正长期规则；
- 压缩 Project setting 以满足实际字符预算；
- 合并重复规则；
- 把 detail 移回 canonical source 并保留必要 bridge；
- 校准多个 scope 在同一 Project 中的长期权重；
- 根据当前 repo/history/live setting 安全更新 Project instructions；
- 全局重构已有 Project instructions，前提是满足本 Proposal 的 rewrite 边界。

### 4.2 near-miss：不应抢走的任务

以下任务即使文本中出现“instructions”“设置”“规则”等普通词，也不能自动归入该 Skill：

- “把这段中文改自然一点” -> `chinese-prose`；
- “保留数字/引用/公式帮我改写”且不涉及 Project instruction architecture -> `writing-fidelity` 或对应写作 route；
- “把这篇技术文档重新组织” -> `scientific-rewrite`；
- “维护 AI_Skills_Collection 的 source / release / registry” -> `ai-skills-core`；
- “设计/执行一个复杂任务工作流” -> `workflow-core`；
- “帮我优化这个 agent/system prompt”但目标不是 ChatGPT Project instructions -> 不属于本 Skill；
- “修改我的 global Custom Instructions” -> 不属于本 Skill。

### 4.3 混合请求的主 owner

若用户既要求改变 Project setting 的长期语义/placement，又要求文字更自然：

- `project-instructions-editor` 是主 owner；
- `chinese-prose` 可以在语义/placement 冻结后做表达实现或终审；
- `writing-fidelity` 可以作为保真 guardrail。

若用户只是对已经选定的一两句话做局部措辞润色，不改变 resident/locator/budget/history/authority 语义，则由写作 Skill 处理，不必启用 Project editor 的完整 reasoning。

这个边界防止 standalone Skill 因名字包含 “instructions” 而吞掉普通写作任务。

## 5. 三种冻结的编辑模式

### 5.1 preservation-sensitive

适用：

- 已有 Project setting；
- 用户没有明确授权废弃未涉及语义；
- 用户要求修改、补充、压缩、重排或“完整更新但保留现有正确内容”。

合同：

- live setting 是完整替换和删除/全局重排的必要基线；
- 未授权区域默认保持；
- 不能用旧 repo Candidate/Reference 替代 live setting；
- 拿不到足够完整 baseline 时，不输出“安全完整替换稿”。

允许的降级：

- placement 建议；
- 新 clause；
- bounded advice；
- 请求取得 live setting。

### 5.2 greenfield

仅当 Project instructions 已确认为空/不存在。

合同：

- 可以直接生成完整初始 setting；
- 不要求不存在的旧 baseline；
- 不声称保留旧规则；
- 仍然要按 current request、canonical sources、有效 product constraints 和实际 budget 判断。

### 5.3 explicit reset

仅当当前用户明确决定废弃旧 Project setting、从零重建，并且不要求保留旧 Project-setting semantics。

合同：

- 旧 baseline 不再作为 preservation gate；
- reset 只解除本次 Project-setting preservation obligation；
- system/workspace/repo authority、安全/权限、当前用户其他有效要求仍然生效；
- “重新写得更好”“大改一下”不自动等于 explicit reset。

当 edit mode 不明确且差异会改变 preservation obligation 时，只问最小澄清问题。

## 6. 输入合同与缺失降级

### 6.1 current edit request

始终必需。

它定义：

- 用户现在要增加/删除/纠正/压缩/同步/重构什么；
- 是否明确 reset；
- 哪些范围被授权改变。

它不自动授权修改无关 scope。

### 6.2 live Project setting

preservation-sensitive 的完整替换、删除和全局重排必须取得足够完整、语义可恢复的 live baseline。

greenfield / explicit reset 不把旧 baseline 当 preservation gate。

“Project context 存在”不自动等于 exact live setting 已经可编辑；只有当前工具/上下文真实暴露完整设置文本时才可以据此做 preservation claim。

### 6.3 relevant Project history

只做 targeted retrieval，不做 exhaustive history audit。

需要优先查：

- explicit acceptance；
- explicit deletion / rejection；
- repeated correction；
- durable ownership / authority decision；
- 明确 temporary 的要求。

缺失时：

- 不声称穷尽历史；
- 不扩大搜索范围只为“更保险”；
- 对 old-only absent rule 应用 protected absence。

### 6.4 canonical project sources

当当前 edit 涉及 repo/document owned 的：

- ownership；
- workflow/policy；
- dynamic fact；
- Goal/TODO/design；
- 当前状态或 locator；

则读取 current canonical source。

无法读取时：

- 不发明 current fact；
- 不把旧 candidate 当新 source；
- 如果缺口只影响一个局部同步，则只阻止该局部；
- 如果缺口决定整个新 setting 的关键治理事实，则不能声称完整设计已可靠同步。

### 6.5 instruction budget

区分：

- current length；
- actual hard limit（真实可得时）；
- user/project planning budget；
- candidate length；
- delta；
- observable remaining margin；
- user/project 指定的 headroom（如有）。

未知 hard limit 时：

- 可以优化语义密度；
- 可以报告 current/candidate length 与 delta；
- 不能声称符合未知硬限制。

约 8,000 字符只保留为历史真实 Project 的 planning evidence，不成为产品常数。

## 7. semantic ownership 与 effective enforcement placement

任何受当前 edit 影响的 durable rule，都必须分别回答两个问题。

### 7.1 semantic ownership

这条规则的详细、当前、可维护真相由哪里拥有？

可能是：

- Project setting 本身；
- global/user preference；
- canonical repo 的 AGENTS/policy/Goal/TODO/design；
- institution/workspace policy；
- current task/thread；
- 其他稳定 source。

### 7.2 effective enforcement placement

为了让当前 Project 在真正使用时受到约束，这条规则必须出现在哪里？

允许的当前 edit disposition：

1. Project-resident direct semantic rule；
2. Project-resident short bridge/trigger + canonical source；
3. canonical/source only；
4. task/thread only；
5. another verified effective layer；
6. omit / no change。

这些是当前 edit 的 reasoning labels，不是持久 schema。

### 7.3 不能只靠 semantic ownership 移出 Project

尤其对：

- ownership/routing；
- authority/permission；
- safety/privacy/distribution；
- evidence/completion；
- user-reading/output contract；
- lookup-before-action rule；

即使详细 source 在外部层，也必须确认当前 Project 内是否仍需 direct subset 或 bridge。

OpenAI 当前官方 Projects 文档仍明确说明 Project instructions 在对应 Project 内生效，并覆盖 global custom instructions，因此“global owns it”不是删除 Project-local control 的充分条件。

## 8. locator substitution 冻结边界

detail 只有在以下条件全部成立时才能从 Project setting 移到 canonical locator：

- locator 稳定、可解析；
- 相关任务在行动前确实会触发 lookup；
- 被移出的 detail 不需要在 lookup 前直接约束；
- Project 保留必要短 trigger/bridge；
- mandatory/optional、authority、安全、证据、不确定性不被削弱；
- 这项 detail 的 canonical owner 确实在外部 source。

locator 的目的不是“把字都赶出 Project”，而是把可可靠恢复的 detail 放回真正维护它的 source，同时在 Project 留下足以保证正确路由和约束的最小语义。

## 9. protected absence

当 relevant history 不可得或只部分可得时，一条 durable rule 如果：

- 当前 live baseline 中不存在；
- 只存在于旧 Candidate、Reference、summary、historical generated setting；

则当前 edit 默认保持 absent。

允许重新加入只有：

1. current user explicit add/re-adopt；
2. current task 明确要求同步 named canonical source，且该 source 当前 authority/content 支持，并且同步 scope 覆盖该项。

这只是当前 edit 的保守 provenance/diff 原则：

- 不形成永久 tombstone；
- 不建立 history registry；
- 不要求 exhaustive search；
- 不让 old candidate 自动补全 live setting。

bounded edit 的未涉及区域继续保持原样。

## 10. bounded edit 与 full rewrite

### 10.1 默认 bounded edit

只要局部修改可以在不破坏其他语义的情况下满足请求，就保持最小修改。

recent thread 不因 recency 获得更多字符预算。

### 10.2 full rewrite/restructure 只有以下真实理由

- 用户明确要求并授权；
- 存在局部修复无法关闭的跨范围矛盾；
- copied workflow detail 已经普遍污染整个 setting；
- multi-scope 出现实质失衡；
- 必要长期语义无法在当前预算内通过局部去重/locator substitution 容纳；
- 多处 source ownership / locator 已经系统性漂移或冲突。

“可以写得更整齐”“现在这部分聊得最多”“完整重写更方便”都不是充分理由。

### 10.3 preservation-sensitive full rewrite 的额外门禁

- live baseline 必须可得；
- relevant current facts 必须可验证到足以支持受影响语义；
- protected absence 继续生效；
- 未授权语义不得被压缩成更弱的规则。

greenfield / explicit reset 不受旧 baseline 门禁，但仍受 current scope、canonical source、权限和实际 budget 约束。

## 11. 必须保护的语义不变量

任何压缩、中文化、重组、locator 化和 full rewrite 都不能静默改变：

- mandatory / optional；
- trigger / escalation condition；
- authority / permission / authorization；
- safety / privacy / distribution boundary；
- evidence strength / completion claim；
- role ownership；
- uncertainty / negative finding；
- current-versus-future status；
- exact machine/formal identity；
- current user explicit correction / rejection / acceptance；
- partial-history 条件下的 protected absence。

exact identifier 与 ordinary language 分开判断。

路径、命令、字段、repo、版本、固定状态、机器 token 等需要精确匹配的内容保持精确；普通工程/管理/统计描述不因来自英文 source 就自动获得 exact protection。

## 12. 字符预算冻结策略

目标不是“最短 setting”，而是长期语义密度和可维护余量。

优先驻留：

- Project purpose/scope；
- durable ownership/routing；
- authority/permission/safety；
- evidence/completion；
- durable product/research philosophy；
- 必须 Project-local enforcement 的 response contract；
- stable trigger/bridge/locator。

优先移回 canonical source / task：

- detailed SOP；
- build commands；
- exhaustive tool inventories；
- current branch/job/version status；
- duplicated review checklists；
- volatile facts；
- single-thread implementation detail；
- 只为解释已有 rule 的例子。

不使用：

- 固定 reserve 百分比；
- 固定 scope 配额；
- 英文比例；
- 行数/标题数/段落数；
- 机械“越短越好”评分。

若局部新增只有通过删除无关语义才能塞进预算，这是需要更大重构判断的证据，而不是静默删减许可。

## 13. 最终用户交付合同

交付与 edit 风险成比例，不制造庞大审计包。

### 13.1 小型 bounded edit

默认提供：

- 简短结构/语义判断；
- 清楚的新增/删除/替换内容；
- 每个实质修改的短理由；
- 关键保持不变语义；
- current/candidate length 与 delta（能取得 baseline 时）；
- 安全时给完整可复制 setting。

### 13.2 medium edit

按风险额外说明：

- scope impact；
- locator/bridge substitution；
- effective enforcement；
- multi-scope balance；
- budget margin。

### 13.3 full replacement

明确说明 edit mode：

- preservation-sensitive；
- greenfield；
- explicit reset。

并给：

- 为什么 bounded edit 不足，或为什么是 greenfield/reset；
- 主要 placement 改变；
- 关键 direct Project rules / bridges；
- semantic invariants；
- budget 变化；
- 完整 clean replacement；
- 必要时 regression prompt / 验证建议。

### 13.4 missing-input output

当输入不足以安全生成完整 replacement：

- 不伪造 full setting；
- 说明当前可安全完成的 bounded advice；
- 指出唯一真正需要补的输入；
- 不把 repo 定位或可自动取得的信息甩给用户。

### 13.5 no-op

如果请求已经被覆盖、应由 canonical source/task owner 处理，或新增只会重复现有 rule，则明确返回“不需要改 Project setting”，并说明正确 owner/locator。

## 14. 实现后必须证明的真实用户能力

本节冻结的是用户能力，不冻结具体 test fixture 数量。

### Capability 1 — Normal entry 与邻近边界

普通用户不点名 Skill 也能从自然 Project-instruction 编辑请求进入正确能力。

同时：

- 普通中文润色不被抢走；
- 普通写作保真不被抢走；
- scientific/technical document rewrite 不被抢走；
- AI_Skills repo maintenance 不被抢走；
- complex workflow control 不被抢走；
- generic prompt/global Custom Instructions 任务不被误路由。

### Capability 2 — Project-surface 核心编辑判断

能够正确处理：

- preservation-sensitive / greenfield / explicit reset；
- live/history/canonical source/budget 输入；
- missing-input degradation；
- semantic ownership vs effective enforcement；
- bounded edit / full rewrite；
- locator substitution；
- protected absence；
- no-op。

### Capability 3 — 语义保真、权限与 should-not-change

编辑后必须保留：

- mandatory/optional；
- authority/permission/safety；
- evidence/completion strength；
- uncertainty；
- exact identifiers；
- explicit user deletions/corrections；
- 未授权 scope；
- 邻近 Skills 的正常 owner。

### Capability 4 — 代表性完整 Project 任务

不能只验证 clause 或小片段。

至少应覆盖真实完整 Project setting 家族中的：

- stale Candidate vs live setting；
- multi-scope finite-budget Project；
- source-drift-controlled comparison；
- language-independent placement problem；
- greenfield/reset 或 partial-history 等高风险模式。

具体 task 数量由最终 implementation blast radius 与 Critic 决定，不在设计阶段固定。

### Capability 5 — 完整用户产物的定性质量

未来 Reviewer 必须看到：

- 完整 user request；
- 判断所需 live/history/source/budget 输入；
- 完整候选 setting 或完整 no-op/advice；
- 原始/候选之间需要保护的语义。

字符数、diff、关键词、route receipt、schema、tests 只能证明机械事实，不能单独证明 Project setting 的语义质量。

## 15. 风险匹配的 Capability Gate 设计方向

A–L 继续作为 regression/task-family bank，不机械变成 12 个 Gate。

实现前正式 Plan 应以以下四个 Gate family 为起点；只有 implementation 事实证明 capability/evidence/failure semantics 明显不同，才允许 split。

### Gate 1 — Normal entry / routing boundary

**证明**：普通用户真实入口能发现并触发该 Skill，同时 near-miss 继续由正确 owner 处理。

**独立性**：即使编辑逻辑本身正确，如果用户触发不到或抢错普通写作任务，产品仍失败。

**未来证据**：

- 正常未点名 Skill 的 Project editing request；
- near-miss owner 行为；
- 实际安装/生产 route identity；
- 完整 user-visible response，而不只 route receipt。

**失败**：

- 只能 forced invocation；
- near-miss 被抢路由；
- 正确 route 但未进入真实 production identity。

### Gate 2 — Core Project editing semantics

**证明**：Skill 能执行冻结的编辑合同，而不是只会一种 rewrite。

覆盖：

- 三 edit modes；
- input degradation；
- ownership/enforcement；
- bounded/full/no-op；
- budget；
- locator；
- protected absence。

**独立性**：这是产品核心专业判断，不等同于“route 正确”或“文字好看”。

**未来证据**：

- A/B/E/F/G/H/I/J/K 中与核心机制直接相关的真实/公开安全任务；
- 必要 source/history/budget 完整输入；
- semantic decision 与最终 candidate 一致。

### Gate 3 — Fidelity / authority / should-not-change

**证明**：编辑不会以压缩、重写或 locator 化为理由破坏用户已经拥有的治理语义，也不会损坏相邻能力。

重点：

- authorization / safety / permission；
- mandatory/optional；
- evidence strength；
- user corrections/deletions；
- exact identifier；
- protected absence；
- unrelated live scope；
- near-miss owner compatibility。

**独立性**：一个候选可以“完成了目标修改”但同时静默削弱关键规则；这个风险与核心 edit success 不同。

**未来证据**：

- old-bad/new-good semantic comparison；
- should-not-change cases；
- C/D/J/K 等高风险回归；
- Reviewer 直接对照 baseline/source，而不是只看候选。

### Gate 4 — Representative complete task + qualitative final artifact

**证明**：同一个最终候选在代表性完整 Project 上，从 normal entry 到完整可复制 setting/no-op/advice 都成立，且完整产物经过定性评审。

**覆盖**：

- long/multi-scope complete setting；
- fixed source/ref；
- budget/placement/semantic preservation 一起出现的真实任务；
- final candidate identity；
- qualitative full-output review；
- risk-matched fresh generalization。

**独立性**：前面 Gate 可以用针对性 regression 证明局部机制；本 Gate 防止“所有小测试都过，但完整 Project 仍不好用”。

**未来证据**：

- 同一 final candidate；
- 完整任务输入与完整 output；
- Reviewer 可访问全部需要对照的 source；
- fresh evidence 在开发回归冻结后按风险决定，不固定样本数。

### Gate lifecycle 原则

- 新 regression 优先归入上述既有 Gate；
- 只有真正不同 capability/evidence/failure semantics/normal entry 才 split；
- cheap deterministic regression bank 先跑；
- 最终 qualitative/fresh gate 在 final candidate 稳定后运行；
- 所有 release claim 必须来自同一 final candidate；
- 不创建 gate registry/database/ledger；
- 不因为一个机械 helper PASS 就升级产品 maturity；
- paid/external reviewer 不是产品合同的默认依赖，若以后 Plan 需要必须另按 paid policy 证明其新增价值。

## 16. A–L regression bank 与 Gate family 的关系

A–L 保留为已知真实回归/设计任务族，不等于 Gate 数。

大致归属：

- Gate 1：L normal entry + near-miss；
- Gate 2：A、B、E、F、G、H、I、J、K 中的核心编辑语义；
- Gate 3：C、D、J、K 以及所有 should-not-change；
- Gate 4：A/B/H 等可形成完整 Project 任务的代表性组合，并加入最终冻结后的 fresh task。

同一个 case 可以为多个 Gate 提供 evidence，但每个 Gate 仍必须证明自己的 capability claim；不能用“一次综合 PASS”掩盖未实际观察的风险。

## 17. 实现阶段仍可决定、但不得改变的边界

最终设计冻结后，后续 implementation Planner/Executor 可以决定：

- Skill 目录内具体文件布局；
- 最终 `SKILL.md` 的自然语言组织；
- description 的精确措辞；
- 是否需要一个只做字符计数/diff 的 deterministic helper；
- trigger eval 的具体 query 文本与数量；
- regression fixture 的公开安全替代材料；
- 具体测试命令；
- 安装/验证步骤；
- release/version/package 细节（按后续正式维护合同）。

但不得自行改变：

- standalone Skill 的职责/非职责；
- normal entry/near-miss owner；
- 三 edit modes；
- live/history/source/budget 输入与降级语义；
- semantic ownership vs effective enforcement；
- locator 前置约束；
- protected absence；
- bounded/full rewrite；
- no-op；
- 用户交付合同；
- 四个 Gate family 的能力含义；
- qualitative full-output evidence requirement。

如果 implementation 发现这些合同无法成立，必须回 Planner/Critic，不得通过测试特判或缩小产品声明绕过。

## 18. 本阶段通过后新增的真实确定性

v2 PASS 证明“产品架构方向是对的”。

本次 final design freeze PASS 将进一步证明：

- 实现团队不再需要决定这个 Skill 到底负责什么；
- 不再需要决定哪些自然请求应该触发、哪些必须留给邻近 Skill；
- 不再需要决定缺 live/history/source/budget 时应该怎样降级；
- 不再需要自行选择 resident / bridge / locator 的基本语义；
- 不再需要自行判断何时可 full rewrite；
- 不再需要自行发明 user deliverable；
- 不再需要把 A–L 临时拼成测试体系；
- 后续 Capability Gate 可以围绕四个不同用户能力 family 设计，而不是机械复制所有回归。

也就是说，后续若用户明确授权实现，实现阶段的任务将收缩为“把已经冻结的产品合同正确落到 Skill runtime、trigger 和测试”，而不是继续做产品架构设计。

这个新增确定性是本轮存在的价值；它不是 implementation readiness 或发布 readiness。

## 19. 当前外部产品事实复核

2026-10-02 本轮定向复核了当前 OpenAI 官方资料，没有发现要求重新打开 v2 的新产品事实。

当前官方 Projects 文档仍说明：

- Project instructions 只在对应 Project 内生效，并覆盖 global custom instructions；
- Project memory/context 行为受 memory mode、plan/workspace 等条件影响；
- Project-only memory 可以让同一 Project 的 chats 相互引用，但不能据此假设 Skill 可以穷尽枚举全部历史；
- 当前 Projects 文档仍未给出一个可验证的统一 Project-instruction 字符上限。

因此继续采用：

- effective-enforcement placement；
- targeted history + honest degradation；
- budget 由 actual Project/user/UI 提供；
- 不把 global Custom Instructions 的限制映射为 Project limit。

## 20. Maintenance state

Canonical TODO 继续使用：

```text
tracking: #93
```

Issue #93 当前已核实：

```text
state = open
labels =
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
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md
```

当前 runtime 没有 GitHub Project field mutation surface，因此以上仍是 exact pending Project mutation，不能声称已同步，也不要求用户手工拖卡片。

Issue #93 reader-facing body 仍落后于当前设计。

`AI_SKILLS_MAINTENANCE_BOARD.md` 要求实质修改 Issue copy 前真实调用当前安装的 Clear Writing（`writing-style`）。当前可调用工具中仍没有可验证 Clear Writing invocation surface，因此：

```text
CLEAR_WRITING_UNAVAILABLE
```

本轮不得修改 Issue body。

待真正可调用 Clear Writing 的 maintenance action 更新为：

```text
问题：
设计一个可跨 Project 复用的长期 Project instructions 编辑能力，安全处理 live setting、相关历史、canonical source、Project 内实际生效层级、有限字符预算和 bounded/full edit。

当前进度：
Standalone Skill 产品架构 v2 已获独立 Critic PASS；实现前最终设计冻结 Proposal 已提交，等待 Critic 审查。当前仍未授权实现。

当前执行锚点：
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md

下一步：
Critic 审查最终职责/触发边界、三种编辑模式、输入降级、ownership/enforcement、protected absence、交付合同和四个 Capability Gate family。PASS 也不授权 implementation；实现必须等用户另行明确开启。
```

以上只是 pending copy source；真正 mutation 前仍必须真实调用 Clear Writing。

## 21. Critic 审查请求

Critic 本轮不应重新打开 v2 已关闭的 B1–B4，除非出现新的直接证据或本 Proposal 引入了真实回归。

请重点判断：

1. 产品职责/非职责是否已经足够具体，后续 implementation 不需要再做产品取舍；
2. trigger 与 near-miss 是否足够清楚，又没有把 Skill 触发面写得过宽；
3. preservation-sensitive / greenfield / explicit reset 是否可以直接作为实现合同；
4. missing live/history/source/budget 的降级是否足以避免 false-safe replacement；
5. semantic ownership / effective enforcement / locator 的边界是否可执行；
6. bounded/full rewrite 和 protected absence 是否没有互相冲突；
7. 用户交付合同是否比例化，而不是每次制造大型审计报告；
8. 四个 Capability Gate family 是否覆盖 normal entry、核心行为、fidelity/authority/should-not-change、代表性完整任务和 qualitative artifact review；
9. Gate family 是否过多或过少，是否有两个实际上证明同一能力；
10. 本轮是否确实新增“implementation 不再自行设计产品合同”的执行确定性。

若 PASS，本对象只进入“设计已冻结、等待用户未来授权 implementation planning/implementation”的状态。

Critic PASS 仍不得创建 Skill、Goal、Kickoff 或任何 release/package 产物。

```text
DESIGN_FREEZE_CANDIDATE=YES
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```
