# Project Thread Handoff — V5 Same-Project Recovery Proposal

日期：2026-09-24  
阶段：production refinement design / pre-implementation review revision  
状态：AWAITING_INDEPENDENT_CRITIC_RECHECK  
Target repo：`YuukiAS/AI_Skills_Collection`  
Target：standalone Skill / science communication  
Design task key：`science-communication--project-thread-handoff-recovery`  
Source branch：`main`  
Prior reviewed proposal：`docs/design/PROJECT_THREAD_HANDOFF_V4_RECOVERY_PROPOSAL_2026-09-24.md`  
Prior reviewed commit：`330e07526c388be76a8fef81e260094f4231deef`  
Critic verdict：`REVISE`  
Only blocker：`PTH-06 — Target-conversation provenance / same-Project attribution 不够可验证`  
Planning baseline：`main@9e63c443ab9204cbf7619b8f0fdd8a81effbafc2`  
Current Skill：`project-thread-handoff` v0.1  
Canonical Skill path：`skills/science/communication/project-thread-handoff/`

本文件是完整 V5 设计，不是对 V4 的局部 diff。它只修 PTH-06，不重新设计 Critic 已接受的双模式
architecture、G1/G2/G3、version、wrapper、icon、read-only 或 authority 边界。

本轮不实现 production source，不创建 execution branch/worktree，不更新 personal Plugin，不调用 paid API。

## 1. Latest-main drift

Critic 审 V4 时 latest main 为 `330e075...`。本轮 Planner 实际检查到 latest main 已推进至
`9e63c443...`。二者之间只有三个 Slurm Workflows design/review docs：

- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_3_2026-09-24.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_PROMPT_V0_3_2026-09-24.md`
- `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_3_2026-09-24.md`

没有 Project Thread Handoff source/version/icon/distribution、Skill authoring、Planner/Critic contract、
Capability Gate policy 或 version-policy overlap。因此 V4 已接受部分保持有效，不重做 full-repo audit。

## 2. Planner disposition

`PTH-06 = ACCEPT`

没有 REBUT。

Critic 指出的关键逻辑缺口成立：V4 把“通过 ChatGPT memory/past-chat retrieval infrastructure 找到的
目标旧 chat”与“generic Saved Memory / profile summary / 无来源 semantic recall”混成了一个
“Memory 不是 authority”的表述。

V5 改成：

> **底层由什么 retrieval/memory infrastructure 提供不重要；是否能把关键 recovered claim 归因到目标
> past chat 才决定它能不能作为 conversation evidence。**

因此：

- identifiable target past-chat source = conversation evidence；
- generic Saved Memory/profile/unsourced recall = 不是 target-thread authority。

## 3. Current product model：保持一个 Skill / 两种模式

### Mode A — Handoff current thread

不变：

```text
旧 thread 仍可写
-> 用户显式调用 Project Thread Handoff
-> Skill 使用当前 thread 已有上下文
-> 输出一份新 thread initialization Prompt
-> stop
```

Mode A 仍是最高保真路径。

### Mode B — Recover previous thread in this Project

不变：

```text
旧 thread 已满/不可继续
-> 用户在同一 ChatGPT Project 新开 thread
-> 显式调用 Project Thread Handoff recovery mode
-> 通过平台 past-chat retrieval 找到目标旧 conversation
-> 恢复关键认知状态
-> canonical facts 回 repo/results/report/Deep Research
-> hydrate 当前新 thread
```

Mode B 不要求用户重贴完整旧 thread，也不要求生成 Prompt 后再贴回当前 thread。

如果 invocation 同时包含 `Recover X and continue Y`，bounded recovery 完成后同一回复继续 Y；
正常情况不增加第二轮确认。

## 4. PTH-06：Target-conversation provenance contract

### 4.1 核心规则

Mode B 的 strong recovery 不以“模型觉得自己记得”为证据，而以：

> **关键 recovered decision 能否归因到目标旧 conversation**

为准。

可接受的 target-conversation provenance 使用当前产品实际暴露的正式 past-chat source 机制，例如：

- Memory Sources / Sources 中明确出现目标 past chat；
- 可打开或可识别的 target conversation title / source card / chat link；
- 其他正式 product surface 暴露的 past-chat source metadata。

V5 不冻结某一个 UI 字段名称，因为产品 surface 可以演化；但必须有**可识别的 target past-chat source**，
不能只有模型内部的无来源 recall。

### 4.2 哪些 claim 必须有 provenance

至少以下会改变后续方向的 recovered claim 必须 target-chat-backed：

- 最新用户明确决定 / 纠正；
- 冻结 route / rejected route 的当前状态；
- entity role；
- thread-only delta；
- 当前 open question；
- immediate next step；
- 用户明确采纳的 assistant proposal。

纯背景性、不影响 route 的 remembered context 即使出现，也不能升级为上述 authority。

### 4.3 Identifiable past chat 即使由 Memory infrastructure 提供，也算 conversation evidence

V5 不再写“Memory 不是 recovery authority”这种过宽表述。

正确表述：

- **past-chat source**：如果产品通过 memory/history retrieval 找到并标出目标旧 chat，它属于
  conversation evidence；
- **generic Saved Memory / profile summary / unsourced semantic recall**：即使内容看起来合理，也不是
  target-thread authority；
- **canonical file/repo/artifact**：继续负责工程/实验事实；
- **model prior knowledge**：不能替代以上任何 source。

## 5. Strong recovery vs limited attribution-unverified recovery

V5 不新增 machine state/schema，但在输出 claim 上区分两种情况。

### Strong recovery

只有当继续任务所需的关键 decision 都至少能由目标 past-chat source支持时，才可以说：

> 已从目标旧 thread 恢复当前 continuation state。

不要求每句话都 source card，也不要求 raw transcript。

### Limited / attribution-unverified recovery

如果 runtime 只能给出 unsourced semantic recall：

- 可以给一个明确标注的 limited recovery summary；
- 不得说“这就是目标旧 thread 的决定”；
- 不得把 unsourced recall 当 authoritative thread-only delta；
- 不得把 paraphrase 写成 direct quote；
- exact formula / prompt / frozen contract 若无 exact past-chat text或 canonical source，必须标 exact wording 未验证；
- 不得用 generic Saved Memory/profile summary 补成 strong recovery。

如果缺失的正是继续任务所必需的关键 decision：

- fail closed on that decision；
- 优先尝试 target locator clue / source identification；
- 仍无法取得 provenance 时，明确指出哪一项无法可靠恢复；
- 只在这项决定确实阻止继续时，允许一次最小用户 clarification；
- 不猜、不自动选 route、不进入确认循环。

## 6. OpenAI product reality

本轮 Planner 再做 targeted official-source check。

### Projects

OpenAI Academy 当前说明：

- Projects 是包含 chats/files/instructions/context 的持续工作空间；
- project-only memory 下，同 Project chat 可以引用其他同 Project conversation；
- Project 外 conversation 不可引用。

OpenAI Projects / Critic 已核实的 Plus/Pro default-memory behavior：

- Project 内 past chats 可被引用，并优先 Project chats/files；
- 但 default-memory runtime 仍可能接触 general chats / other Projects。

因此 V5 **不再声称“处于当前 Project 就保证所有 context 只来自当前 Project”**。

产品边界改为：

> Mode B 只接受 target same-Project conversation evidence 作为 recovery authority；default-memory runtime
> 可能暴露 Project 外 context，所以无法归因的信息不能升级为 recovery authority。

Project-only memory 是 stronger isolation，可提高边界清晰度，但不是 V0.2 使用前置条件，也不要求用户改设置。

### Memory Sources / past-chat sources

OpenAI 2026 release notes / Memory FAQ 当前说明：

- Plus/Pro 可以更可靠地从 past chats 找特定信息；
- 用于回答的 past chats 可以作为 source 出现并打开原 context；
- Sources 可显示 past chat / saved memory / custom instruction 等不同 source 类型；
- Sources 视图**可能不展示影响回答的每一个因素**。

采用结论：

- past-chat source card/locator 可以成为 PTH-06 provenance；
- 不能因为 Sources UI 没列出所有内部因素，就声称 transcript-level isolation；
- Gate 应验证关键 recovery claim 有 target-chat backing，而不是要求所有 token 都有 provenance。

External adoption：`REFERENCE_ONLY`。

## 7. Target locator / candidate identification

V4 的 title/topic/date/unique phrase/project-task clue 保持，但语义修正为：

> 这些是引导 ChatGPT past-chat retrieval / candidate identification 的 clue，不是 deterministic
> conversation-database query key。

可以使用：

- conversation title；
- topic/project/task name；
- approximate date；
- unique phrase；
- distinctive user correction；
- known artifact/task clue。

流程：

1. 用 clue 引导 past-chat retrieval；
2. 查看产品提供的 candidate/source provenance；
3. 如果 target source 可以唯一归因，直接 recovery；
4. 如果多个真实 candidate 都可能匹配，且选错会改变 route，最多一次最小澄清；
5. 如果只有模型“感觉应该是这一条”而没有 target-source provenance，不得声称唯一定位成功。

## 8. Authority split：保持 V4/V3

### Conversation evidence

只对可归因到目标 old conversation 的内容恢复：

- explicit user decision/correction；
- accepted proposal；
- intent；
- entity role；
- thread-only delta；
- open question；
- next step；
- recurrence guard。

仍保持：

`latest explicit user/frozen decision > assistant brainstorming`

### Canonical source

repo / artifacts / results / reports / Deep Research 负责：

- code；
- experiments；
- numbers；
- runtime facts；
- reports/results/TODO。

conversation 中“计划执行”不得恢复成“已经完成”。

如果 conversation 和记载事实的 canonical source冲突：

- research/product intent 依照最新明确 decision；
- code/experiment/runtime fact 依照 current canonical source；
- 不用 past-chat source覆盖更新后的 artifact facts。

## 9. Semantic recovery，不是 raw transcript

不变：

Mode B 不声称：

- full transcript dump；
- every-turn access；
- verbatim reconstruction；
- lossless recovery。

正常 recovery 优先：

1. target source attribution；
2. recent decisive user turns / corrections / accepted decisions；
3. 理解最新状态所需的最小向前追溯；
4. stale brainstorming pruning；
5. 达到“足够正确继续”即停止。

如果只得到 summarized past-chat content，只能作为 semantic evidence使用；没有 exact source text时不引用成逐字原文。

## 10. Cross-Project boundary

V5 default product boundary 仍是：

`current ChatGPT Project -> target old conversation in that same Project`

不得主动：

- 使用另一个 Project conversation补当前 Mode B；
- 使用 Project 外 regular Chat补 route；
- 用 Saved Memory做跨 Project bridge；
- 混合多个 Project 的 thread-only delta。

但 V5 不声称 default-memory runtime 在底层绝不会搜索到 Project 外 context；它只规定：

> **Project 外 / 无法归因 context 不能作为 Mode B recovery authority。**

G3 不要求另建另一个私有 Project 做 live leakage test。理由：

- OpenAI 官方已说明 default-memory 与 project-only memory的 scope不同；
- real cross-project leakage test会增加私有数据暴露/用户负担；
- 关键产品能力是 target-chat provenance，而不是证明平台底层检索绝对 isolation。

V0.2 用 contract regression + actual target-chat source evidence 覆盖即可。

## 11. Mode B output contract

如果 provenance 足够：

默认输出 compact recovered continuation state：

- target old conversation identity（只保留用户可理解的 title/topic/date/locator，不泄漏内部无用 metadata）；
- current objective；
- latest effective decisions；
- thread-only delta；
- entity-role guard；
- canonical source recovery guidance；
- immediate next step。

然后当前新 thread直接继续。

如果只有 limited/unverified recovery：

- 明确说明哪些部分有 target-chat source；
- 哪些只是 unsourced recall，不能当 authoritative decision；
- 如果不影响继续，可在 bounded uncertainty 下继续；
- 如果影响 route，停止在那个 decision 并请求一次最小 clarification。

## 12. Architecture / non-goals

保持 V4：

不新增：

- MCP；
- database；
- CURRENT；
- transcript exporter；
- browser extension；
- state machine；
- second Recovery Skill；
- history store；
- Project-wide full transcript scan；
- periodic checkpoint requirement；
- automatic new thread；
- global Plugin Creator redesign；
- Bridge Kit dependency；
- external API。

仍是一个显式 standalone Skill 的两个模式。

## 13. Existing personal Plugin wrapper / canonical icon

保持 Critic 已接受的 V4 contract。

Canonical icon：

`skills/science/communication/project-thread-handoff/assets/app-facing.svg`

Existing PRIVATE / USER-scope / skills-only personal Plugin wrapper 更新时必须：

- preserve same Plugin identity；
- no MCP；
- bundle current canonical Skill；
- bundled `assets/app-facing.svg` 与 canonical source byte-equivalent；
- manifest `composerIcon` / `logo` 优先引用 canonical asset；
- target surface 明确不支持 SVG 时才允许 deterministic conversion；
- conversion 必须记录 canonical SVG source，不 redesign icon。

Implementation 时更新：

`docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md`

使 Plugin Creator 明确复用当前 icon。

不修改 global Plugin Creator architecture。

## 14. Capability Gate Matrix：只保留 G1/G2/G3

### G1 — Distribution / Explicit Invocation / Visual Identity

保持 V4：

- canonical Skill v0.2 source/generated parity；
- explicit-only；
- existing personal wrapper identity preserved；
- skills-only / no MCP；
- canonical icon reused；
- target Pro regular Chat actual explicit invocation。

G1 不证明 handoff/recovery semantics。

### G2 — Current-Thread Handoff Regression

保持 V4：

- target Pro regular Chat；
- current long thread；
- final candidate Mode A；
- current context consumed；
- latest user/frozen precedence；
- entity-role；
- thread-only delta；
- locator；
- one initialization Prompt；
- no second confirmation；
- no repo write。

DII/CARE 继续作为 regression语义，但 production Skill 不 hardcode项目名。

### G3 — Same-Project Recovery / Generalization + PTH-06 provenance

这是 V0.2 关键 Gate。

Target：

- user current Pro account；
- ChatGPT regular Chat；
- `AI Research Stack` Project；
- new thread；
- same Project target old conversation；
- preferably 已因长度上限不可继续的真实 old thread；
- final candidate installed through current verified wrapper route。

真实 Bridge/SSH replay：

用户不重新粘贴旧回答。

至少恢复正确语义：

- Bridge Kit 本身不依赖 SSH；
- SSH 是 publisher compatibility/safety相关 transport；
- WSL GitHub SSH identity未配置不等于 Bridge product failure；
- 不应仅为 gate 改用户真实 HTTPS开发环境；
- 更接近 compatibility acceptance/evidence 问题。

**新增 PTH-06 provenance criterion：**

对于上述决定性 recovered semantics，必须观察到：

- target Bridge/SSH old conversation 作为 past-chat source / equivalent identifiable target-chat provenance；
- target source 可以被用户/Reviewer辨识为目标 conversation；
- generic Saved Memory/profile/无来源 recall不能替代它。

如果关键 recovered decision 无法归因到 target conversation：

`G3 strong PASS = NO`

只允许 limited/unverified recovery claim；如果缺失 decision 阻止继续，则 fail closed。

G3 另外验证：

- semantic recovery 不冒充 verbatim transcript；
- Sources 可能不展示每个影响因素，因此 final claim只写：
  `target-conversation-backed semantic recovery verified; no observed cross-project substitution`
- 不声称 transcript-level or absolute retrieval isolation；
- unique target 正常不确认；
- ambiguous-target public-safe fixture最多一次 clarification；
- canonical facts回 current repo/artifact；
- existing CAT-TRACE/CardiacNexus public-safe fixtures继续验证 generalization；
- no DB/MCP/Bridge dependency；
- cross-Project contract regression通过；
- 不要求另一个私有 Project live leakage test。

G1/G2/G3 仍绑定同一个 final candidate，不新增 G4/G5。

## 15. Target-surface evidence / privacy

G3 可以记录：

- target Project name/type；
- target old conversation title or redacted source locator；
- source type = past chat；
- criterion-level semantic recovery result；
- whether Memory Sources / equivalent source UI exposed target chat；
- final claim boundary。

不得提交：

- 旧 thread 全文；
- private chat URL if sensitive；
- private personal Plugin URL/ID；
-完整 recovery output；
- unrelated Memory Sources。

如果 source UI locator本身包含私密 title，可在 repo evidence里做最小 redaction，但 Reviewer/用户
target-surface 验收时必须实际看到足以判断“这是目标 old conversation”的 provenance。

## 16. Expected implementation scope after design PASS

保持 V4：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
tests/fixtures/project_thread_handoff/...   # public-safe only
docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md
tests/test_standalone_skill_baselines.py
```

Canonical icon bytes预期不改：

`skills/science/communication/project-thread-handoff/assets/app-facing.svg`

按 existing source-first generator更新 registry/catalog/provenance/domain docs。

不修改中央 Plugin production source。

## 17. Version / release：保持已接受结论

不因 PTH-06 重开版本类别。

Standalone Skill：

`project-thread-handoff 0.1 -> 0.2`

Repository：

`5.1.0 -> 5.1.1 PATCH`

Central Plugins：

全部 `NO_BUMP`

Private personal wrapper：

implementation 时读取 current private version / release id 后 compatible increment；
public repo不写 private identity/version。

## 18. README / changelog closure

正式 V0.2 release 时：

- root README standalone card：v0.1 -> v0.2；
- 简短补充“旧 thread 已满时可在同 Project 新 thread recovery”；
- 不把 wrapper当中央 Plugin；
- root CHANGELOG记录 same-Project recovery；
- `skills/README.md` explicit check；taxonomy不变时预期
  `README checked: no update required`。

## 19. Alternatives：PTH-06 后重新确认

### A. 要求 project-only memory

不采用为 V0.2 前置条件。它提供更强 isolation，但用户当前 default-memory Project 也能做
target-chat-backed recovery，只要 provenance contract严格。

### B. 要求 raw transcript

不采用。官方没有保证完整 transcript retrieval；产品目标是 semantic continuity。

### C. unsourced recall 也算 strong recovery

拒绝。会重现 Critic指出的核心风险：generic memory/profile context冒充目标 old thread。

### D. 再建 provenance database / transcript ledger

拒绝。问题可由现有 product source metadata + bounded claim contract解决。

## 20. Red-team：PTH-06 关闭后重点

1. source card指向相似但错误 thread；
2. default-memory 提供另一个 Project 的相关信息，模型误当目标 thread；
3. Saved Memory 与 past-chat source混写；
4. only unsourced recall却输出“旧 thread明确决定了...”；
5. Sources没有列出每个背景因素，就反向过度声称绝对隔离；
6. exact formula没有 exact text却被重构成 quote；
7. locator clue被误描述成 deterministic database lookup；
8. provenance不足仍自动继续改变研究路线。

V5 的 target-source provenance + limited-recovery fallback + G3 criterion直接覆盖这些风险。

## 21. Completion boundary

V5 Critic PASS只批准 design。

如果：

`PTH-06=CLOSED`

且无新的 direct blocker，则：

`PRE_IMPLEMENTATION_DESIGN_PASS=YES`

下一步 Planner 才准备同一 V5 authority 下的：

- Implementation Plan；
- Canonical Goal；
- Kickoff Draft；

再交 execution-ready Critic review。

在 execution package Critic PASS + 用户发送 approved Kickoff 前，不实现 production source。
