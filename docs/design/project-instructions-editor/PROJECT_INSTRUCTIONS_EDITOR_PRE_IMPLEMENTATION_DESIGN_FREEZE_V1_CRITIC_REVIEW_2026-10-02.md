# Project Instructions Editor — 实现前最终设计冻结 Critic Review v1

Date: 2026-10-02  
Result: `PASS`  
Design freeze: `PASS`  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch/ref: `main`  
Main observed before this review: `613cf2d7399ecacc360809f4e58f48ad7870df61`  
Reviewed proposal: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`  
Freeze version: `v1`  
Freeze proposal + canonical TODO package commit: `f1cace3d44870ff98d352698b8e9aa23621655df`  
Freeze proposal blob: `520879d23b84ec5879a4eb2f49181a1cf4d72d20`  
Approved architecture: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`  
Approved architecture review: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_CRITIC_REVIEW_2026-10-02.md`  
Architecture Critic review commit: `b2da311519bf29713f0681245a7aab62fa81dadd`  
Tracking: `#93`  
Review stage: pre-implementation final design freeze review

```text
CRITIC_RESULT=PASS
DESIGN_FREEZE=PASS
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
NEXT_HANDOFF=PLANNER
```

## 1. 结论

实现前最终产品合同已经足够冻结。

通过本 Proposal 后，后续 implementation 不需要再决定这个 Skill “到底是什么”。产品职责、正常触发边界、相邻 owner、三种 edit mode、输入缺失降级、semantic ownership 与 effective enforcement、locator 边界、protected absence、bounded/full rewrite、no-op、用户交付形式以及 Capability Gate 的能力含义都已经明确。

剩余未定项属于正常实现决策：Skill 目录内怎样组织、`SKILL.md` 怎样表述、description 精确措辞、是否需要纯机械字符/diff helper、trigger eval 的具体 query、fixture、test command、安装/验证和后续 release/version 细节。这些不需要继续停留在产品架构阶段。

当前 freeze 没有重新打开 v2 已关闭的 B1–B4，也没有引入新的数据库、ledger、daemon、watcher、history service 或状态机。

本次 PASS 只冻结产品/架构设计，不授权实现。

## 2. 职责与非职责

`PASS`.

冻结后的唯一产品 owner 足够清楚：

- 长期 ChatGPT Project instructions 的 semantic placement/editing；
- live setting、相关历史、canonical source 和 budget 协调；
- bounded/full edit；
- effective enforcement；
- protected absence；
- safe user delivery。

明确排除 generic prompt optimization、global Custom Instructions 编辑、普通 prose polishing、scientific document structural rewrite、AI_Skills repo maintenance、复杂 workflow execution/control、后台 history service、GitHub Project sync、数据库/ledger/daemon/watcher/state machine。

后续实现不应再合理地出现“generic system prompt 是否也属于该 Skill”“global Custom Instructions 是否一起支持”这类产品决策；答案已经冻结为 NO。

## 3. Normal entry / near-miss

`PASS`.

正常触发边界已经足以实现：

当目标对象明确是长期 ChatGPT Project instructions / Project setting，并且用户要求创建、修改、压缩、同步或重构其长期语义时，进入该 Skill。

混合请求也有明确 owner：

- Project setting semantic/placement edit + 中文润色：Project editor 主导，`chinese-prose` 后置辅助；
- 已经选定的一两句 instruction 只做措辞润色，不改变 resident/locator/budget/history/authority：不必进入完整 Project editor reasoning。

near-miss owner 已覆盖真正相邻能力，而没有无限枚举：

- ordinary Chinese prose -> `chinese-prose`
- ordinary writing fidelity -> `writing-fidelity`
- scientific/technical structural rewrite -> `scientific-rewrite`
- AI_Skills repository maintenance -> `ai-skills-core`
- complex process/control -> `workflow-core`
- generic agent/system prompt -> outside this Skill
- global Custom Instructions -> outside this Skill

具体 description 和 trigger eval 文案仍可在实现阶段决定，但不得改变上述触发语义。

## 4. 三种 edit mode

`PASS`.

### preservation-sensitive

已有 setting 且用户未授权丢弃未涉及语义时，完整替换、删除和全局重排必须有足够完整的 live baseline。拿不到 baseline 时只能降级 advice/local clause/placement suggestion，不能 false-safe full replacement。

### greenfield

setting 已确认为空时，可以生成完整初始 setting，不要求不存在的旧 baseline，也不得声称保留旧规则。

### explicit reset

只有当前用户明确决定废弃旧 Project setting、从零重建且不要求旧 Project-setting semantics 保真时成立。模糊的“重写一下”“大改一下”不能自动解释成 reset。

reset 只解除 Project-setting preservation obligation，不覆盖 system/workspace/repo authority、安全、权限或当前其他有效用户要求。

这三类已经可以直接作为 future implementation contract。

## 5. 输入与缺失降级

`PASS`.

五类输入已经冻结：

- current edit request；
- live Project setting；
- relevant targeted Project history；
- canonical project sources；
- instruction budget。

降级边界足够明确：

- preservation-sensitive + no live baseline -> 不给 safe full replacement；
- history partial/unavailable -> 不升级 exhaustive audit，old-only absent durable rule 走 protected absence；
- canonical source unavailable -> 不发明 current fact，只阻塞受影响局部；若缺口决定完整治理架构，则不能声称完整同步可靠；
- hard budget unknown -> 可以报告 current/candidate length 与 delta，不得声称符合未知硬限制。

这避免了“为了保险把所有 history 都翻一遍”的过重路线。

## 6. Semantic ownership / effective enforcement / locator

`PASS`.

freeze 正确冻结了两个不同问题：

1. semantic ownership：详细、current、maintainable truth 由哪里拥有；
2. effective enforcement placement：为了让当前 Project 实际受约束，Project setting 是否需要 direct rule、bridge/trigger、source-only、task/thread-only、another verified layer 或 omit/no-change。

global/user ownership 不自动允许从 Project 删除；repo ownership 也不自动允许 Project 不留 trigger。

locator substitution 只有在 locator 稳定、lookup 不会太晚、Project 保留必要 trigger、被移出的 detail 无需 lookup 前生效，并且 mandatory/optional、authority、安全、证据与不确定性均保持时才成立。

这个边界已经足以阻止“为了省字符把关键治理语义全部移出去”。

## 7. Protected absence

`PASS`.

history partial/unavailable 时：

- live baseline 中不存在；
- 且只存在于旧 Candidate / Reference / summary / historical generated setting；

的 durable rule 默认保持 absent。

只有 current user explicit add/re-adopt，或 current task 明确授权 named canonical-source synchronization、且 source authority/content 与同步 scope 直接支持该项时，才可重新引入。

它仍然只是当前 edit 的 provenance/diff 默认原则，不是 tombstone registry、history database 或 exhaustive-history requirement。bounded edit 未涉及区域继续保持原样。

## 8. Bounded edit / full rewrite

`PASS`.

bounded edit 仍是真实默认。

full rewrite/restructure 只有以下真实理由：

- 用户明确要求并授权；
- local edit 无法关闭 cross-cutting contradiction；
- copied workflow detail 普遍污染；
- multi-scope 实质失衡；
- 必要 durable semantics 无法在 budget 内通过 local dedup/locator 容纳；
- source ownership/locator 系统性漂移或冲突。

recent thread 最近讨论最多、整体重写更整齐、实现者觉得重写方便，都不是充分理由。

preservation-sensitive full rewrite 继续要求 live baseline。

## 9. 用户交付合同

`PASS`.

交付已经按风险比例冻结，而不是统一生成大型 audit package。

- small bounded edit：简短判断 + 清楚改动 + 短理由 + invariants + length/delta + 安全时 clean setting；
- medium edit：按风险增加 scope/locator/enforcement/balance/budget margin；
- full replacement：明确 edit mode、placement changes、hard rules/bridges、invariants、budget changes 与 clean replacement；
- missing input：只给安全 advice，指出唯一真正缺失输入，不把可自动定位工作甩给用户；
- no-op：明确“不需要改 Project setting”，并指出正确 owner/locator。

用户能够知道“到底改了什么”，同时小修改不会被迫产生复杂审计包。

## 10. Capability Gate family

`PASS`.

四个 Gate family 的粒度合适，不需要为了“更保险”继续拆成第五、第六 Gate。

### Gate 1 — Normal entry / routing boundary

证明普通用户从真实生产入口触发正确 Skill，near-miss 仍由原 owner 处理，并排除 forced invocation 冒充正常入口。

### Gate 2 — Core Project editing semantics

证明三 edit modes、输入降级、ownership/enforcement、bounded/full/no-op、budget、locator、protected absence 等核心专业判断成立。

### Gate 3 — Fidelity / authority / should-not-change

证明目标修改虽然完成，但 mandatory/optional、authorization、safety、permission、evidence strength、uncertainty、exact identifier、user correction/deletion 与 unrelated live scope 没有被静默破坏。

### Gate 4 — Representative complete task + qualitative final artifact

证明同一个 final candidate 能在完整、代表性的长期 Project setting 上，从 normal entry 到完整 setting/no-op/advice 成立，并由能访问完整输入/source/output 的 Reviewer 做定性完整产物审查。

Gate 4 同时承担 long/multi-scope、fixed source/ref、final-candidate identity 和 risk-matched fresh generalization 是合理的：这些共同回答“完整产品是否在最终候选上真实成立”，不是另一个独立 domain capability。

Gate 1 与 Gate 3 都会碰到 near-miss，但不是同一 claim：Gate 1 证明 routing owner 选对；Gate 3 证明编辑行为没有破坏邻近 owner/should-not-change。未来实现应避免无意义重复执行，同一 evidence 可以在确实支持两个不同 claim 时被复用，但不能用一个笼统综合 PASS 掩盖未观察能力。

A–L 继续只是 regression/task-family bank，不是固定 Gate 数量。

## 11. Gate lifecycle

`PASS`.

已冻结的 lifecycle 足够：

- 新 regression 优先归已有 Gate；
- cheap deterministic regression 先跑；
- qualitative/fresh gate 在 final candidate 稳定后跑；
- release evidence 绑定同一 final candidate；
- 不拼接多个 candidate PASS；
- fresh 数量按风险决定；
- 不创建 Gate registry/database/ledger；
- paid/external review 不是默认依赖；
- deterministic helper 只能负责字符计数/diff 等机械事实，不能做 semantic keep/delete/placement 判断。

这与当前 Capability Gate policy 一致。

## 12. 外部产品事实复核

2026-10-02 独立复核 OpenAI 当前官方资料：

- OpenAI Help Center — Projects in ChatGPT  
  https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Help Center — ChatGPT Custom Instructions  
  https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions
- OpenAI Help Center — Memory in ChatGPT  
  https://help.openai.com/en/articles/8590148-memory-in-chatgpt

当前事实仍支持冻结合同：

1. Project instructions 只在对应 Project 内适用，并覆盖 global custom instructions，因此 effective-enforcement placement 仍有产品意义。
2. Project memory/context 可用性依赖 memory mode、plan/workspace 等条件；Project memory 也没有一个可供穷尽审计的完整 memory list。因此不能把“完整枚举全部 Project history”当成 Skill 前提。
3. 当前官方 Projects 文档没有给出一个可验证的统一 Project-instruction 字符上限。正确结论只能是“当前未从官方 Projects 文档核实到统一上限”，不能写成“官方证明不存在上限”。
4. global Custom Instructions 有单独的字符限制，这是不同产品表面，不能映射为 Project instructions 上限。

没有新外部事实要求重新打开已批准架构。

## 13. Maintenance state

Current main 已确认：

- canonical TODO 含 `tracking: #93`；
- Issue #93 为 open；
- labels 为：
  - `maintenance-track`
  - `kind:new-capability`
  - `scope:standalone-skill`
  - `area:standalone-skill`
- reader-facing Issue body 仍落后于当前设计冻结阶段。

当前没有可验证的已安装 Clear Writing / `writing-style` invocation surface，因此本轮不修改 Issue body：

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
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md
```

不要求用户手工拖 Project 卡片。

## 14. 本轮新增确定性与 PASS 边界

本次 PASS 新增的真实确定性是：

以后 implementation 不再自行决定：

- Skill 职责/非职责；
- normal entry / near-miss owner；
- 三 edit modes；
- live/history/source/budget 输入与降级；
- semantic ownership / effective enforcement；
- locator 边界；
- protected absence；
- bounded/full rewrite；
- no-op；
- 用户交付形式；
- 四个 Gate family 的能力含义；
- qualitative full-output evidence requirement。

implementation 仍可以决定：

- Skill 目录内文件布局；
- `SKILL.md` 的具体自然语言组织；
- description 精确措辞；
- 是否需要纯机械 character/diff helper；
- trigger eval 具体 query；
- regression fixture；
- test commands；
- install/validation implementation；
- 后续正式 version/release 细节。

因此当前设计已经足够冻结。

本次 PASS 只表示产品/架构设计冻结，等待用户未来明确授权 implementation planning / implementation。

它不授权：

- 创建 Skill；
- 创建 implementation Goal；
- 创建 Kickoff；
- 写 trigger eval；
- 创建 Plugin；
- release/package；
- 安装；
- Codex execution。

```text
CRITIC_RESULT=PASS
DESIGN_FREEZE=PASS
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
NEXT_HANDOFF=PLANNER
```
