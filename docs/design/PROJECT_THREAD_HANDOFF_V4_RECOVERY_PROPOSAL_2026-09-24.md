# Project Thread Handoff — V4 Same-Project Recovery Proposal

日期：2026-09-24  
阶段：production refinement design / pre-implementation review  
状态：AWAITING_INDEPENDENT_CRITIC_REVIEW  
Target repo：`YuukiAS/AI_Skills_Collection`  
Target：standalone Skill / science communication  
Design task key：`science-communication--project-thread-handoff-recovery`  
Source branch：`main`  
Planning baseline：`main@b211db38bdcff8772c1be493d81b95a5b04a9059`  
Current Skill：`project-thread-handoff` v0.1  
Canonical Skill path：`skills/science/communication/project-thread-handoff/`  
Prior approved design：`docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md`  
Prior production integration：`7b76e94ad29cf3bd8547026b942553068754d51f`  
Standalone version/icon closure：`7c7083015c04a898c2536f7c60ffa79f5bccef1a`

本提案是已有 Project Thread Handoff v0.1 的 bounded production refinement。它不推翻 V3 已通过的
authority/recency、entity-role、canonical locator、read-only、explicit invocation 或 distribution
边界。新增能力只有一个：**当旧 thread 已经达到长度上限、来不及主动 handoff 时，新 thread 可以从
同一 ChatGPT Project 的真实旧 conversation 恢复足够的认知状态并继续。**

本轮只做设计，不实现 source，不更新 personal Plugin，不创建 execution branch/worktree。

## 1. Current reality

### 1.1 v0.1 已正式存在

当前 main 的 canonical Skill：

`skills/science/communication/project-thread-handoff/`

已有：

- `SKILL.md`
- `agents/openai.yaml`
- `evals/trigger_queries.json`
- `assets/app-facing.svg`

当前 Skill metadata：

- version `0.1`
- explicit-only
- `requires_network=false`
- `writes_files=false`
- `executes_code=false`
- no MCP / database / history store

从 icon/version closure commit `7c708301...` 到 planning baseline 的 9 个 main commits 没有
Project Thread Handoff source/icon/version-related drift；主要是其他任务 docs。

### 1.2 当前 ChatGPT regular Chat distribution reality

现有 V1 closure 已经证明：

- standalone ZIP 可上传、Skills 页面可识别；
- Work 能加载 standalone Skill；
- 当前用户 Pro regular Chat 的 bare standalone Skill runtime 没有稳定加载；
- 将 canonical Skill 原样包装成 **PRIVATE / USER-scope / skills-only personal Plugin** 后，
  regular Chat 实际调用 PASS；
- wrapper 没有 MCP / connector / external API / database / app / state。

因此 canonical source 仍是 standalone Skill，但当前 regular Chat 的已验证 distribution wrapper 是
现有 personal Plugin。V4 不新建中央 Plugin，也不创建第二份 Skill source。

## 2. 本轮真实用户 failure

用户连续遇到长期 Project thread 突然达到长度上限，旧 thread 已无法再发送消息，因此即使
Project Thread Handoff 已安装，也可能**来不及在旧 thread 调用 Mode A**。

这暴露出 v0.1 的真实缺口：

```text
旧 thread 仍可写
-> v0.1 可以 handoff

旧 thread 已达到长度上限
-> 无法在旧 thread 调 Skill
-> v0.1 没有 recovery path
```

这不是理论风险，已经在实际长期科研/工程 Project 中发生。

## 3. Same-Project conversation recovery 的现实证据

本轮用户要求专门验证“同一个 ChatGPT Project 的旧 conversation”，并明确排除用 Memory 冒充。

在当前 `AI Research Stack` Project 的新 thread 中，对另一条真实旧 thread 做 targeted recovery 时，
系统能够恢复该 thread 的关键语义，例如：

- Bridge Kit 本身不依赖 SSH；
- SSH 是 publisher compatibility gate 的一部分；
- 当前 WSL 未配置 GitHub SSH identity 不等于 Bridge product failure；
- 不应该为了过 gate 改用户实际 HTTPS 开发环境；
- 更合理的是把 SSH compatibility 与当前 host credential 状态分开判断。

随后用户提供了旧 thread 的完整原文，对比后确认上述 recovered semantics 与原文的核心判断一致。
但 cross-thread recovery 并没有可靠提供完整 raw transcript / 逐字全文。

因此 V4 的产品目标是 **semantic continuity**，不是 transcript export。

## 4. External reality check

本轮 targeted external check 采用：

1. OpenAI Academy — Using Projects  
   https://openai.com/academy/projects/
   - Projects 共享 chats/files/instructions/context；
   - project-only memory 下，chat 可以引用同一 Project 内其他 conversation。

2. OpenAI Help Center — Projects in ChatGPT  
   https://help.openai.com/en/articles/10169521-projects-in-chatgpt
   - project-only memory：同 Project chat 可互相引用，Project 外不可引用；
   - Plus / Pro default memory：ChatGPT 可以引用 Project 内过去 chats，并优先 Project chats/files；
   - default memory 在部分 plan 上仍可能允许 Project 外历史，因此“当前 Project 优先”不等于
     “严格 Project-only”。

3. OpenAI Academy — Using Skills  
   https://openai.com/academy/skills/
   - Skill 是在 ChatGPT 中复用 workflow 的轻量 instruction/resource layer；
   - Projects 是共享 context/files/conversations 的长期工作空间；
   - 两者是互补 product surface。

采用结论：

- same-Project recovery 是现有 ChatGPT Project context 能力上的 Skill workflow，不需要 MCP；
- 不声称 Skill 能获取完整 raw transcript；
- 不声称 default-memory Project 自动隔离 Project 外 conversation；
- V4 必须显式把 recovery authority 限制到当前 Project 的目标 conversation，而不是泛用 Memory。

External source adoption：`REFERENCE_ONLY`。没有 vendoring/runtime dependency。

## 5. Product model：一个 Skill，两种显式模式

仍然只有一个 Skill：

`Project Thread Handoff`

不新增 `project-thread-recovery` Skill，不新增 Plugin product，不新增 database。

### Mode A — Handoff current thread

保持 v0.1 行为：

```text
旧 thread 仍可写
-> 用户显式调用 Project Thread Handoff
-> Skill 读取当前 thread
-> 输出一份可复制到新 thread 的 initialization Prompt
```

Mode A 继续是最高保真的默认 handoff。

### Mode B — Recover previous thread in this Project

新增：

```text
旧 thread 已满/不可继续
-> 用户在同一 ChatGPT Project 新建 thread
-> 显式调用 Project Thread Handoff，并要求 recover previous/project thread
-> Skill 定位同一 Project 的目标旧 conversation
-> 恢复关键认知状态
-> 重新把 canonical facts 交给 repo/results/DR 等 source
-> 当前新 thread 直接获得 continuation state
```

Mode B 不是要求用户把旧 transcript 再粘一次。

## 6. Mode selection

Skill 继续 explicit-only；不启用 implicit invocation。

Mode A：

- 用户明确要求 handoff current thread / generate continuation prompt；
- 或在当前长 thread 中显式选择 Skill 且意图明显是迁移当前 thread。

Mode B：

- 用户明确说旧 thread 满了、无法继续；
- 或明确要求 recover / resume 某个同 Project thread；
- 用户可给 title、主题、日期、独特短语、项目名等 locator clue。

如果 target thread 在当前 Project 中能唯一定位，直接恢复，不再确认。

只有存在**两个以上真实候选 thread，且选错会改变当前研究方向/任务状态**时，允许问一次最小澄清，例如：

> 是昨天的 DII 方法 thread，还是 CARE 实验 thread？

这是 Mode B 唯一允许的 bounded disambiguation，不扩展成表单/确认循环。

## 7. Recovery authority contract

### 7.1 当前 Project 的真实旧 conversation

用于恢复：

- 最新明确用户决定与纠正；
- 用户明确采纳的 assistant 建议；
- 当前研究/产品意图；
- entity role；
- thread-only delta；
- open question；
- immediate next step；
- 容易复发的 rejected route。

仍然遵守 V3：

`latest explicit user/frozen decision > assistant brainstorming`

### 7.2 Canonical repo / artifact / report / Deep Research

用于恢复：

- code state；
- experiment result；
- numeric facts；
- runtime fact；
- formal report/result；
- source-controlled TODO / decision。

Conversation recovery 不能把聊天里“准备做”升级成 repo 中“已经完成”。

### 7.3 Memory 不是 recovery authority

Mode B 不得把 Saved Memory / profile summary / generic remembered fact 当作旧 thread 内容的替代品。

尤其在 Plus/Pro default-memory Project 中，即使平台可能提供 Project 外 conversation/memory，
也必须：

- 只使用能够归因于**当前 Project 目标旧 conversation**的聊天信息作为 recovery evidence；
- 不因为模型“记得用户曾做 CARE / CAT-TRACE / Bridge”就当作旧 thread 的当前状态；
- 如果某个关键 claim 无法判断是否来自目标 Project conversation，则不把它当作 recovered decision。

Project-only memory 可以提供更强平台隔离，但 V4 不要求用户改变 Project 设置。

## 8. Semantic retrieval，不要求 raw transcript

Mode B 不要求：

- dump 整个旧 thread；
- 逐字还原每条消息；
- 获取完整 transcript；
- 引用全部历史。

优先做 bounded recovery：

1. 用 thread title / topic / recency / unique phrase 定位目标 conversation；
2. 优先恢复最近 decisive user turns、corrections、accepted decisions、open questions；
3. 只在理解最新状态需要时向前追溯；
4. 不因为旧内容很多就把 brainstorming 全部带回；
5. 以“足够继续正确工作”为停止条件。

如果 runtime 只提供 semantic recall / summarized prior-chat content：

- 可以用来恢复语义；
- 不得把 paraphrase 冒充逐字 quote；
- 对必须逐字保真的 formula/prompt/contract，如果没有 direct exact text 或 canonical source，
  明确标记 exact wording 未验证，而不是编造。

## 9. Mode B output contract

Mode A 继续：

> 输出一份新 thread initialization Prompt，然后停止。

Mode B 已经发生在**新 thread**，因此不要求用户再复制一份 Prompt 到同一个 thread。

默认输出：

1. 一个简短的 recovered continuation state；
2. 当前目标；
3. 最新有效决定/thread-only delta；
4. 必要 entity-role guard；
5. canonical source recovery guidance；
6. immediate next step。

然后该 state 自然成为当前新 thread 的上下文。

如果用户在同一次 explicit invocation 中写了具体 continuation request，例如：

> Recover yesterday's DII thread and continue the unresolved transfer-weight question.

则 Skill 在完成 bounded recovery 后**同一回复直接继续该请求**，不再要求一次确认或重新 paste。

## 10. Cross-Project boundary

V4 的 recovery mode 只处理**当前 ChatGPT Project**。

不得：

- 主动去其他 Project 找相似 thread；
- 用 Project 外 regular chat 补齐缺失状态；
- 用 Saved Memory 当作跨 Project bridge；
- 把多个 Project 的 conversation 混成一个 recovered state。

如果用户明确要从另一个 Project 搬内容，那是另一项显式迁移任务，不属于 Mode B 默认行为。

如果 runtime 无法可靠归因候选 conversation 是否属于当前 Project，则 Mode B 必须限制 claim，
不能假装已完成 same-Project recovery。

## 11. Architecture / non-goals

V4 保持轻量，不新增：

- MCP；
- database；
- CURRENT；
- handoff history；
- checkpoint daemon；
- browser extension；
- automation/watcher；
- Project transcript cache；
- Bridge Kit dependency；
- external API；
- repo write mode。

本轮基于 same-Project recovery 的真实能力，**不把 periodic checkpoint 设为 V0.2 requirement**。
Mode A 仍可在重要节点主动使用，但不增加自动 checkpoint 系统。

## 12. Distribution wrapper 与 canonical icon

Canonical product identity 仍是 standalone Skill。

当前 regular Chat 已验证入口是 existing PRIVATE / USER-scope / skills-only personal Plugin wrapper。
V0.2 release 应更新**现有 wrapper identity**，不创建新 personal Plugin，不变成中央 Marketplace Plugin。

现有 canonical icon 已完成并进入 source：

`skills/science/communication/project-thread-handoff/assets/app-facing.svg`

它也是：

- `SKILL.md -> icon_small`
- `SKILL.md -> icon_large`
- README standalone Skill card
- icon audit / contact sheet

的 canonical visual identity。

未来 Plugin Creator 更新/重新打包 Project Thread Handoff 时必须：

1. 读取并复用 canonical `assets/app-facing.svg`；
2. 不重新设计、生成另一套或随机替换 icon；
3. wrapper bundled Skill 内的 `assets/app-facing.svg` 必须与 canonical source byte-equivalent；
4. 如果 wrapper/plugin manifest 有 `composerIcon` / `logo` 等 UI icon 字段，优先直接引用
   bundled canonical icon；
5. 如果某个 target surface 明确不接受 SVG，才允许从 canonical SVG 做 deterministic format
   conversion；不得改变图形设计，且要记录 derivative source；
6. 更新现有
   `docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md`
   时明确写入上述规则，让 Plugin Creator 不再自行发明 icon。

这只是现有 wrapper 的 visual-identity preservation，不修改 Plugin Creator 的全局 architecture。

## 13. Expected source scope after design PASS

预计 production refinement：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
tests/fixtures/project_thread_handoff/...   # 只做 public-safe recovery/regression fixtures
docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md
tests/test_standalone_skill_baselines.py     # version/icon baseline adjustment
```

现有 canonical icon 本身预期 **不修改 bytes**：

`skills/science/communication/project-thread-handoff/assets/app-facing.svg`

Generated parity 按现有 source-first generator 更新 registry/catalog/provenance/domain docs。

不修改任何中央 Plugin source。

## 14. Capability Gate Matrix

仍保持小型三 Gate，不新增 G4/G5。

### G1 — Distribution / Explicit Invocation / Visual Identity

证明：

- canonical standalone Skill v0.2 source/generated parity；
- explicit-only metadata；
- current regular Chat distribution wrapper 更新的是 existing personal Plugin identity；
- wrapper remains skills-only / no MCP；
- canonical `app-facing.svg` 被原样复用，不重新生成 icon；
- target Pro regular Chat 可以通过实际正式显式入口调用 final candidate。

Why distinct：
只证明 install/distribution/invocation/identity，不证明 handoff/recovery 语义。

### G2 — Current-Thread Handoff Regression

用 final candidate 在 target Pro regular Chat 的现有长 thread 实际调用 Mode A。

证明 v0.1 能力不回归：

- current thread context 被消费；
- latest user/frozen decision precedence；
- entity role；
- thread-only delta；
- canonical locator；
- one initialization Prompt；
- no confirmation loop；
- no repo write。

已有 DII/CARE failure semantics 继续作为代表性 regression；不 hardcode 项目名。

### G3 — Same-Project Recovery / Generalization

这是 V0.2 新 capability 的关键 Gate。

Target surface：

- 用户当前 Pro ChatGPT regular Chat；
- 当前 `AI Research Stack` Project；
- 一个新 thread；
- 目标是同 Project 中已经存在、最好已经无法继续发送的旧 thread。

至少用本轮真实 Bridge/SSH旧 thread 做 normal-entry recovery replay。

用户**不重新粘贴完整旧回答**。

Recovered state 至少应正确恢复核心语义：

- Bridge Kit 本身不依赖 SSH；
- SSH 是 publisher compatibility/safety acceptance 的相关 transport；
- 当前 WSL GitHub SSH identity 未配置不等于 Bridge product failure；
- 不应仅为 gate 改变用户真实 HTTPS 开发环境；
- 当前问题更接近 acceptance contract / compatibility evidence，而不是 Bridge runtime dependency。

同时验证：

- 不把 semantic recovery 冒充 verbatim transcript；
- 不用 Memory/profile facts 冒充目标 thread evidence；
- 如果存在明确 target locator，正常情况不要求确认；
- ambiguous-target fixture 只允许一次最小 disambiguation；
- canonical engineering facts 仍回到 current repo/artifact；
- existing CAT-TRACE/CardiacNexus representative fixtures继续证明 latest-decision/generalization；
- no cross-Project recovery by default；
- no Bridge Kit dependency / no transcript database。

Why distinct：
G3 证明跨 conversation 的 same-Project continuity，是 Mode A/G2 完全不同的 product capability。

### Final-candidate / user-action policy

G1/G2/G3 release-critical evidence 必须来自同一 final candidate。

实现阶段先自行完成 source/tests/generated parity/public-safe fixtures/plugin-wrapper package/update
准备，再让用户做一次 bounded target-surface acceptance session。

可以在同一次已安装 final wrapper 下完成：

1. Mode A current-thread invocation；
2. Mode B 在同一 Project 新 thread 的 recovery invocation。

不因为两个 mode 要求用户重复安装 wrapper。

## 15. Version / release decision

已实际读取当前 `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`。

### Standalone Skill

`project-thread-handoff: 0.1 -> 0.2`

Reason：
同一个 standalone Skill 新增明确 user-facing capability：旧 thread 已满时，从同 Project 旧
conversation 做 semantic recovery。这不是 docs/tests-only change。

### Repository

Current repository：`5.1.0`

Proposed release：`5.1.0 -> 5.1.1 PATCH`

Reason：
Project Thread Handoff 已经是 5.1.0 的正式 standalone capability；V0.2 是该现有 workflow 的兼容增强，
不是 collection-level 新系统能力。

### Central Plugins

全部：`NO_BUMP`

本任务不修改中央 Marketplace Plugin production behavior。

### Personal Plugin wrapper

wrapper manifest/version 按 existing personal Plugin current release 做一次 compatible increment；
执行时先读取 current plugin identity/version/release id，不在 repo 中预写用户私有 Plugin version。

## 16. README / changelog closure

正式 V0.2 release 时：

- root README standalone Skill card 从 v0.1 -> v0.2；
- 用一句人话补充“旧 thread 已满时可在同 Project 新 thread 恢复”；
- 不把 personal Plugin wrapper伪装成中央 Marketplace Plugin；
- root CHANGELOG 记录 Project Thread Handoff v0.2 same-Project recovery；
- `skills/README.md` 显式检查；taxonomy 没变时预期
  `README checked: no update required`。

## 17. Privacy / evidence boundary

不得把以下内容提交 repo：

- 真实旧 thread 全文；
- 用户私有 Project conversation dump；
- Personal Plugin URL/ID；
- 完整 private handoff/recovery output。

可以提交：

- public-safe synthetic fixtures；
- criterion-level PASS/FAIL；
- target Project / surface 类型；
- redacted recovery semantics；
- source/plugin candidate identity；
- icon/package hashes。

## 18. Alternatives

### A. 不改 Skill，只继续要求提前 Mode A handoff

拒绝作为唯一方案：已经有真实“thread 突然满掉、来不及 handoff”的失败。

### B. 周期 checkpoint / 自动持久化

V0.2 不采用。需要用户维护额外状态，且 same-Project conversation recovery 已显著降低灾难性丢失风险。

### C. database / transcript exporter / browser extension / Mica

V0.2 不采用。解决方案明显重于问题，并会制造第二套 conversation truth。

### D. 新建第二个 Recovery Skill

V0.2 不采用。两个模式都属于同一个“Project thread continuity”用户目标；拆成两个 Skill 会增加入口和触发冲突。

选择：

**一个 Project Thread Handoff Skill，显式双模式。**

## 19. Red-team

重点防以下失败：

1. 新 thread 看到 generic Memory 中的 CARE/Bridge 信息，就假装恢复了旧 thread；
2. default-memory Project 把另一个 Project 的 conversation 混进来；
3. semantic retrieval 被写成“原文说……”；
4. 为了“完整”读取大量旧 thread，重新复活 stale brainstorming；
5. target thread 有歧义却静默选错；
6. recovery 后不重新读取 canonical repo，继续使用旧实验数字；
7. Mode B 加入后破坏 Mode A 的 single-prompt UX；
8. personal Plugin update 重新生成一套 icon，导致现有 visual identity 漂移；
9. wrapper update 变成新的 central Plugin/MCP architecture；
10. 为防 thread 满掉引入 database/checkpoint daemon，过度工程化。

G2/G3、scope boundary和 icon packaging contract分别覆盖这些风险。

## 20. Completion boundary

本 V4 Critic PASS 只批准设计，不授权 implementation。

后续如果 V4 design PASS：

Planner 再准备同版：

- Implementation Plan；
- Canonical Goal；
- Kickoff Draft；

然后做 execution-ready Critic review。

在 final candidate 的 G1/G2/G3 未全部通过前，不允许声称：

`PROJECT_THREAD_HANDOFF_V0_2_READY=YES`
