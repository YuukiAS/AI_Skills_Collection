# Project Thread Handoff — V3 Proposal

日期：2026-09-21  
阶段：pre-implementation design review  
状态：AWAITING_INDEPENDENT_CRITIC_RECHECK  
Target repo：`YuukiAS/AI_Skills_Collection`  
Source branch：`main`  
Prior proposal：`docs/design/PROJECT_THREAD_HANDOFF_V2_PROPOSAL_2026-09-21.md`  
Prior package commit：`22fd8e5330cd669c19ba7edf3a523bdb27f84bb4`  
V3 planning baseline：`main@d6bf0a6c11f9cce82a538bb542349035e4f10905`  
Bridge reference baseline：`YuukiAS/GPT_Codex_AI_Bridge_Kit main@9d2da9f485f26ca51842a1909a276cb44f73351a`  
Design topic：`project-thread-handoff`

本文件是完整 V3 设计。它不是 implementation Plan，不授权修改 production Skill source。

## 1. 本轮 source drift 核对

从 V2 package commit `22fd8e5330cd669c19ba7edf3a523bdb27f84bb4` 到本轮 planning baseline
`d6bf0a6c11f9cce82a538bb542349035e4f10905`，AI_Skills main 新增 4 个 docs-only 文件，
全部属于另一个 `scientific-pdf-rendering` 设计/Goal/Kickoff/Critic handoff。

没有修改：

- Project Thread Handoff V2；
- `AGENTS.md`；
- Planner/Critic Role Contract；
- Plugin Capability Gate Policy；
- Skill authoring / metadata contract；
- skill taxonomy；
- production Skill source。

因此没有与本方案直接相关的实质 drift，不重新做 full-repo audit。角色合同仍是
`PLANNER_ROLE_CONTRACT.md` v1.4 与 `CRITIC_ROLE_CONTRACT.md` v1.4。

## 2. 本轮变更边界

上一轮已关闭并保持关闭：

- `PTH-01` authority / recency；
- `PTH-02` metadata placement；
- `PTH-03` DII/CARE normal-entry semantics；
- repo-write boundary；
- Bridge Kit boundary；
- taxonomy / name / slug。

本轮只修正三个 product-surface 问题：

1. 撤销“Pro Web 原生 standalone Skill 当前不可用”的过度结论；
2. 不再把 Codex 的 `$skill` 语法硬编码成 ChatGPT regular Chat 唯一入口；
3. 把最终 normal-entry evidence 明确绑定到用户当前 Pro 账号的 **ChatGPT regular Chat**。

不新增新的架构组件。

## 3. 产品目标

Project Thread Handoff 只解决：

> 长期科研/工程项目旧 thread 快到上下文或线程长度边界时，用户在当前普通 Chat 中显式调用一次 Skill，旧 thread 直接输出一份最小充分的新 thread 初始化 Prompt。

典型项目：CAT-TRACE、Distributed Imaging Inference（DII）、CardiacNexus。

用户正常路径：

```text
已有长期 ChatGPT regular Chat thread
        ↓
通过当前账号实际提供的正式显式 Skill 入口
选择/调用 Project Thread Handoff
        ↓
Skill 读取当前 thread 已有上下文
        ↓
一次性输出新 thread 初始化 Prompt
```

正常情况：

- 不要求用户重新粘贴历史；
- 不问第二轮确认；
- 不写 repo；
- 不自动创建新 thread；
- 不切到 Work 或 Codex 来替代普通 Chat。

## 4. Target-account product availability：A / B / C 分离

### A. 当前账号能否创建/上传 Skill

**当前 target account：YES。**

用户当前 Pro 账号已经直接看到：

`Plugins -> Skills`

并且 Skills 页面存在：

- 通过聊天创建；
- 通过编辑器创建；
- 从电脑上传。

这是本目标账号的直接 UI 证据。通用套餐表不能反向否定该账号已经实际暴露的入口。

A 只证明“可创建/上传/安装候选”，不证明普通 Chat 中一定能在当前长 thread 调用。

### B. 当前账号的 ChatGPT regular Chat 能否显式调用已安装 Skill

**设计阶段：待 target-surface smoke。**

社区、近期独立实测与 OpenAI Academy 已证明 regular Chat 的 explicit Skill invocation
在部分 Plus/Pro 账号真实存在，但账号级 rollout / session availability 仍有差异。

因此 V1 不预先判 YES，也不预先判 NO。最终由 G1/G2 在用户当前 Pro 账号的
**ChatGPT regular Chat** 实测。

### C. Work / Codex 是否也能调用

这不是 V1 产品目标的替代品。

- Work/Codex 可以做开发或兼容性 smoke；
- Work PASS 不能替代 regular Chat PASS；
- Codex `$skill` PASS 不能替代 regular Chat PASS。

## 5. 针对性网络核查与采用结论

本轮 external research 全部是 `REFERENCE_ONLY`，不 vendoring、不引入 runtime dependency。

### 5.1 OpenAI Developer Community：Pro 用户 ChatGPT Web + Codex 实际运行过自定义 Skills

检查：
`Custom Skill stopped executing in ChatGPT and Codex after August 20, 2026 — possible Skill runtime issue?`

URL：
https://community.openai.com/t/custom-skill-stopped-executing-in-chatgpt-and-codex-after-august-20-2026-possible-skill-runtime-issue/1391582

2026-08-21 的 Pro 用户明确报告：自定义 Skills 在 8 月 20 日前长期正常运行于
ChatGPT web 与 Codex，随后出现 runtime regression。

采用：
- 证明 Personal Pro 账号上 ChatGPT Web Skill execution 确实出现过；
- 同时证明“安装可见”与“当前 session 真能执行”必须分开验收。

不采用：
- 不把单一社区帖子当作所有 Pro 账号普遍 availability 的证明。

### 5.2 OpenAI Developer Community：Plus 账号之间 regular Chat invocation 行为不一致

检查：
`@ and + shortcuts for skills not working in chat sidebar on one Plus account, but works on another. Bug?`

URL：
https://community.openai.com/t/and-shortcuts-for-skills-not-working-in-chat-sidebar-on-one-plus-account-but-works-on-another-bug/1395288

同一设备的两个 Plus 账号出现：
- 一个 regular Chat 的 Skill picker / mention 正常；
- 另一个 regular Chat 不显示；
- 部分用户只在 Work 正常。

采用：
- regular Chat Skill capability 确实存在；
- rollout/account/session behavior 不能靠 plan table 推断；
- final smoke 必须绑定 target account + target surface。

### 5.3 Reddit：Chat / Work / web / iOS / account fragmentation

检查：

1. https://www.reddit.com/r/ChatGPT/comments/1w916l2/and_shortcuts_for_skills_not_working_in_chat/
2. https://www.reddit.com/r/ChatGPT/comments/1vy26sy/why_are_skills_limited_to_chatgpt_work_on_web_and/

近期讨论同时存在：
- regular Chat 可用的账号；
- 只在 Work 可用的账号；
- web/iOS/local/cloud Skill library / invocation fragmentation 的报告。

采用：
- 只把它作为 rollout fragmentation 的社区证据；
- 支持“按目标账号实测”的验收方式。

不采用：
- 不据此断言所有 Plus/Pro 都可用或都不可用。

### 5.4 独立 Plus 实测：Personal Skill + Try in chat

检查：
`ChatGPT Plus Skill Feature is Working! Hands-on Verification Report`

URL：
https://note.com/tk_ax/n/n99650b498688

2026-08-04 的 Plus 实机报告：
- 创建 SKILL.md；
- 注册 Personal Skill；
- 出现 `Try in chat`。

采用：
- 证明 Personal Plus rollout 至少已在部分账号发生；
- 支持 V1 继续走 standalone Skill。

### 5.5 独立 Pro 实测与近期教程

检查：

- https://www.auditit.app/template-skill
- https://lauvibecoding.substack.com/p/how-i-created-a-chatgpt-skill-for
- https://www.tonyreviewsthings.com/how-to-use-skills-in-chatgpt/

其中近期实测/教程报告了：
- tested Pro account 出现 `Upload from your computer`；
- Skill 页面 `Try in chat`；
- Plus / Pro Personal Skills rollout；
- Skills 位于 Plugin Directory，UI/availability 会因 surface/account 而异。

采用：
- 作为 target-account UI 证据的外部交叉支持；
- 不把教程中的套餐概括升级成官方 universal guarantee。

### 5.6 OpenAI Academy / Help Center / Developer docs

检查：

- https://openai.com/academy/skills/
- https://academy.openai.com/public/clubs/work-users-ynjqu/resources/skills
- https://help.openai.com/en/articles/20001066
- https://developers.openai.com/zh-Hans/docs/build-skills

OpenAI Academy 当前说明：
- 可以在 ChatGPT 中创建、安装 Skill；
- enabled Skill 可以自动使用，也可通过 `@` mention 显式选择；
- Skills 用于跨 chats / use cases 的可复用 workflow。

Help Center 当前同时仍写有较窄的 eligible-plan 文案，但也正式记录：
- `Plugins -> Skills`；
- create with chat；
- create with editor；
- upload from computer；
- availability / installation / syncing 可以因 product/surface 不同。

Developer docs 对 `agents/openai.yaml` 明确：
- `policy.allow_implicit_invocation: false`；
- Codex 仍可用 `$skill` explicit invocation。

采用：
- metadata contract 保持；
- ChatGPT explicit invocation 不强绑 Codex 的 `$` 语法；
- target account + target surface smoke 是最终 authority。

### 5.7 Invocation syntax 仍在演化

检查：
`Feature Request: Make "/skill" the Canonical Invocation Syntax for ChatGPT Skills`

URL：
https://community.openai.com/t/feature-request-make-skill-the-canonical-invocation-syntax-for-chatgpt-skills/1393711

2026-09 社区与 OpenAI Support 回复显示：
- ChatGPT 当前存在 `@`-based Skill invocation；
- desktop slash-command list 也能显示 enabled Skills；
- 入口语法并非所有 surface 完全统一。

采用：
- V1 contract 应绑定“正式显式 Skill 入口”，而不是某个字符。

## 6. 架构选择与替代比较

### 选择：standalone Skill

原因：
- 用户真实需求本质就是可复用的“旧 thread -> 初始化 Prompt”工作流；
- 当前 target Pro account 已直接出现 Skill 创建/上传 UI；
- 不需要外部数据服务、数据库或动作系统；
- Skill 足以表达判断与输出 contract。

### 不选：继续纯手工 Prompt

可行但不能解决重复解释 handoff 规则、entity-role 混淆、authority/recency 漂移。

### 不选：Plugin / MCP / distribution system

当前没有必要。新增它们会增加安装、权限和维护面，而 target account 已具备 standalone Skill 入口。

### 不选：CURRENT / handoff database / history

会把项目自己的 repo/实验/Deep Research 之外再造一套 truth，和“最小 handoff”目标相反。

## 7. Skill 位置与文件边界

名称：
`Project Thread Handoff`

slug：
`project-thread-handoff`

source：
`skills/science/communication/project-thread-handoff/`

V1 source 预计：

```text
SKILL.md
agents/openai.yaml
evals/trigger_queries.json
```

实现时仅在确有需要时增加最小 test fixture；不预设 scripts/reference/assets。

standalone Skill，不复制到中央 Plugin。

## 8. Authority / recency contract（PTH-01 保持关闭）

### 8.1 决策语义

优先级：

1. 最新用户明确决定、纠正或冻结决定；
2. 较早仍有效的用户/冻结决定；
3. 用户明确采纳的 assistant 建议；
4. assistant brainstorming / exploration。

更晚的 assistant brainstorming 不能仅凭“更晚”覆盖用户已经明确决定的方向。

### 8.2 工程/实验事实

当前 canonical repo / artifact / report 是工程、实验、数值和运行事实 authority。

聊天里的计划或解释不能把尚未运行的实验变成“已完成”。

### 8.3 thread-only delta

如果 thread 中存在比 repo 更新、尚未持久化的明确决定：

- 必须带入 handoff；
- 明确其尚未持久化；
- 可以对研究意图、路线、命名、下一步暂时 supersede repo 中较旧计划；
- 不覆盖真实实验数字、代码状态或运行事实。

### 8.4 信息裁剪

- active working hypothesis：仍影响下一步才保留，并标为待验证；
- open question：保留真正未解决项；
- assistant exploration：未采纳且非当前 open question 时删除；
- rejected route with recurrence risk：最多一行防复发；
- stale / naturally superseded history：删除；
- chat noise：删除。

DII/CARE 的角色：
- DII 是当前方法学项目；
- CARE 是当前数据/数据来源；
- CARE challenge models 不是当前 DII 方法候选。

## 9. Canonical locator contract

能从外部 source 可靠恢复的事实优先给短 locator：

```text
<repo/source> @ <branch/ref if known> : <path if known> — 用于恢复 <事实类型>
```

规则：

- 已知就写清；
- exact commit 只用于需要冻结版本的 artifact/result；
- 当前状态优先让新 thread 读当前绑定 branch；
- 不知道精确 path/SHA 时不得编造；
- 可写真实定位策略，如“先读当前 AGENTS / README / results index”；
- handoff 不为了补 locator 做 full-repo audit；
- 新 thread 负责重新读取 canonical source。

## 10. Output contract

默认只输出一份可直接作为新 thread 第一条消息的初始化 Prompt。

必须让新 thread 能恢复：

1. 当前项目 / 当前续接目标；
2. 最新有效决定与 thread-only delta；
3. 当前立即下一步；
4. canonical fact-recovery guidance / locators。

按需加入：

- 易混淆实体角色；
- 理解下一步必需的当前进度；
- active hypothesis / open question；
- recurrence guard。

不强制固定八段模板。

长度：
- 800–1800 中文字是经验范围；
- 不设最低字数；
- 约 2500 字是默认软上限；
- 必须携带的未落盘公式、精确 Prompt、关键约束可突破。

## 11. Invocation contract（PTH-02 修订为 surface-neutral）

保持：

```yaml
policy:
  allow_implicit_invocation: false
```

它必须位于：
`agents/openai.yaml`

不写进普通 `SKILL.md` frontmatter。

但 V1 不再规定 ChatGPT normal entry 必须是 `$project-thread-handoff`。

### ChatGPT regular Chat normal entry

定义为：

> 用户在当前 ChatGPT surface 中，通过该账号实际提供的正式显式 Skill
> 选择 / mention / invocation 入口，调用已安装的 Project Thread Handoff。

候选 UI 可能包括：

- Skill picker；
- `@Project Thread Handoff`；
- Skill 页面 `Try in chat`；
- desktop slash-command entry；
- 其他当时 target account 正式暴露的显式入口。

不预先规定字符。

### Codex

Codex 的 `$project-thread-handoff` 只能证明 Codex explicit invocation。

它不能证明 ChatGPT regular Chat normal entry。

## 12. Repo / Bridge Kit boundary

V1 完全 read-only：

- 不写科研 repo；
- 不写 `docs/wiki/`；
- 不写 `docs/notes/`；
- 不写 `prompts/tasks/`；
- 不 commit/push 用户项目；
- 不提供 opt-in repo-write mode。

Bridge Kit 只作为已有项目的 source-role convention。

如果目标项目已确认安装 Bridge Kit，新 thread 可先读：
- 项目自己的 `AGENTS.md`；
- `prompts/CHATGPT_RULES.md`；
- 再按需要读取项目实际存在的 wiki / notes / tasks / results。

不得假设这些路径存在，不依赖 Reviewed Handoff 状态机。

## 13. Capability Gate Matrix：只保留 G1 / G2 / G3

### G1 — Installation / Explicit Invocation Boundary

证明的用户能力：
最终候选可以在 target Pro account 被安装，并在 ChatGPT regular Chat 通过真实显式 Skill 入口被选择，同时普通对话不因 implicit routing 自动进入。

Evidence：

1. final candidate 按 AI_Skills source-first 规则完成 source/generated/provenance parity；
2. `agents/openai.yaml` invocation metadata 正确；
3. 可上传 final Skill package 已生成并本地/支持 runtime 验证；
4. 用户当前 Pro account 成功上传/安装 final candidate；
5. target ChatGPT regular Chat 中实际出现可用显式入口；
6. ordinary summary / ordinary project chat 不隐式进入。

为什么独立：
G1 只证明“安装、发现、显式调用边界”，不证明 handoff 内容正确。

失败：
- package 无法安装；
- Skill 在 regular Chat 不可选；
- 必须切 Work/Codex 才可调用；
- ordinary chat 仍隐式触发。

### G2 — Core Handoff Semantics / DII Target-Surface Replay

这是 V1 最关键的 normal-entry gate。

Target：
**用户当前 Pro ChatGPT regular Chat。**

必须：

- final candidate 已实际安装；
- 在一个已经存在较长上下文的普通 Chat 中显式调用；
- Skill 直接消费当前 thread 已有上下文；
- 不要求用户重新粘贴整个历史；
- history 含真实 DII/CARE failure semantics。

PASS 必须同时看到：

- DII 是当前方法学项目；
- CARE 是数据/数据来源；
- CARE challenge models 不恢复为当前方法候选；
- 最新用户决定覆盖早期 assistant exploration；
- thread-only delta 被带走；
- repo 可恢复事实主要给 locator；
- 输出只有一份新 thread 初始化 Prompt；
- 不问第二轮确认；
- 不写项目 repo。

如果：

- regular Chat 无法真实调用；
- Skill 不能读取当前 thread context；
- 只能 Work/Codex 工作；

则：
`G2 = FAIL`

返回 Planner/Critic判断真实产品限制。不得静默换 surface 后宣布 PASS。

为什么独立：
G2 证明用户真正消费的 semantic capability，不由安装/metadata 或 fixture 代替。

### G3 — Generalization / Should-not-change

CAT-TRACE：
- 后期冻结的模型/符号/数据决定覆盖早期探索；
- 不把过时路线重新列为当前选择。

CardiacNexus：
- 代码、pipeline、实验数字主要让新 thread 从 current repo 恢复；
- handoff 主要传递最近认知判断、open question、下一步。

同时证明：
- 不 hardcode DII/CARE；
- 不依赖 Bridge Kit。

G3 不重复验证：
- ordinary summary trigger；
- no-repo-write。

这些分别已由 G1/G2覆盖。

G3 可以在开发期的支持 runtime / representative fixture 上完成，不要求用户额外做三次 UI smoke；最终 target-account 用户动作只用于 G1/G2。

三个 release-critical gate 绑定同一 final candidate，不新增 G4/G5。

## 14. Implementation 后的用户动作：一次最小请求

在要求用户操作前，Executor 必须先完成：

- Skill source；
- `agents/openai.yaml`；
- trigger eval；
- contract tests；
- registry/catalog/provenance/generated parity；
- 可上传 final Skill package；
- 本地或支持 runtime 的开发验证；
- G3 开发回归；
- final candidate freeze。

只有 final candidate 已完整准备好，才请求用户一次：

> 在当前 ChatGPT Skills 页面上传/安装这个 final candidate，然后回到当前普通 Chat，
> 用界面实际可见的显式 Skill 入口调用一次 Project Thread Handoff。

这是一次 bounded target-surface acceptance 请求，不允许：

```text
上传一半
→ 用户发现 package 不完整
→ 返回修
→ 再上传
→ 再让用户测试
```

如果 target account 的正式产品入口允许系统直接安装且无需用户账户级确认，可使用正常入口；
如果上传/安装/选择必须由用户本人完成，只请求上述一次最小动作。

用户 target-surface smoke 前，不能声称 G1/G2 final PASS。

## 15. Implementation scope（Critic PASS 后才准备 execution package）

预计 production source：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
tests/fixtures/project_thread_handoff/...   # 仅在最小 acceptance fixture 实际需要时
```

并按仓库现有机制生成/更新：

- registry；
- catalog；
- provenance；
- 其他现有 generated parity。

另生成最终可上传 Skill package。若不适合版本控制，按 AI Research Stack 约定保留在 repo 内
`private/exports/`，不放 `/tmp`。

不修改：

- Bridge Kit production source；
- CAT-TRACE / DII / CardiacNexus production repo；
- 中央 Plugin source；
- Mica；
- browser extension。

## 16. Trigger / contract tests

Trigger eval 与 V1 explicit-only 语义一致：

positive：
- 明确通过 installed Skill 的正式显式入口调用；
- 用户在同一 invocation 中可附“继续 DII”等 target。

negative / near-miss：
- “总结一下当前项目”；
- “我们现在做到哪了”；
- “帮我继续研究”；
- “handoff 是什么意思”。

Contract test 检查：

- authority / recency rules；
- thread-only delta；
- locator non-fabrication；
- read-only；
- single-prompt output；
- no confirmation loop；
- invocation policy 位于 `agents/openai.yaml`；
- normal-entry contract 不硬编码 `$` / `@` / `/`。

机械 test 不替代 G2 target-surface replay。

## 17. README / version closure

README：
implementation/release closure 必须显式检查根 README 与 skills README。

如果 standalone Skill 的加入没有改变中央 Plugin 表格或用户公开安装入口：
`README checked: no update required`

版本：
本设计不提前决定 repository bump。

implementation/release Plan 必须按当前
`PLUGIN_VERSIONING_AND_CHANGELOGS.md`
读取真实 source 后做版本决策。

本 standalone Skill 不自动 bump 任何现有中央 Plugin version。

Bridge Kit version 不变。

## 18. Failure / recovery boundary

若 implementation 暴露以下任一事实，停止并返回 Planner/Critic：

- target regular Chat 无法选择已安装 Skill；
- Skill 在 regular Chat 无法消费已有 thread context；
- 必须切换 Work/Codex 才能运行；
- 必须新增 Plugin/MCP 才能实现；
- 必须写用户项目 repo；
- 必须引入持久状态；
- 必须依赖 Bridge Kit；
- final candidate package 不能在不反复打扰用户的情况下准备完整。

不得自行用别的 surface 或更重架构“修成 PASS”。

## 19. 产品 availability 的最终表述

V3 不再写：

> ChatGPT Pro native standalone Skill entry 当前不可用。

也不写：

> 所有 Plus / Pro 用户现在都一定有 Skills。

当前证据只支持：

- Personal Plus / Pro 已存在真实 rollout；
- 当前用户 Pro account 已直接暴露 Skills 创建/上传 UI；
- 社区存在 Plus/Pro 在 ChatGPT Web regular Chat 使用 Skills 的真实案例；
- 不同账号、Chat/Work、web/desktop/local/cloud 的 rollout、invocation、同步仍有差异；
- 因此最终能力按 **target account + target surface** 实测。

## 20. 五遍预检结论

### Product

通过后用户新增的真实能力：
长期科研旧 thread 只需一次显式调用，即可生成可靠 continuation Prompt；不再每次重新教 GPT 怎么 handoff。

### Reality

当前 target account 已有 Skill 创建/上传 UI；regular Chat invocation 仍需 final-candidate target-surface smoke。

### Alternatives

纯手工 Prompt 可继续用但重复成本高；Plugin/MCP/数据库明显过重；standalone Skill 与当前能力和需求最匹配。

### Red Team

主要真实失败：
- 只在 Codex PASS；
- 只在 Work PASS；
- Skill 不能读取已有 thread；
- 用户决定被 assistant 后续探索覆盖；
- CARE 数据被误当 CARE 方法；
- locator 编造；
- 用户被要求多轮上传/调试。

G1–G3 与一次最小用户 smoke 直接覆盖这些风险。

### Execution

设计 PASS 后再准备 Implementation Plan + Canonical Goal + Kickoff Draft。
本 V3 仍不授权实现。

## 21. V1 completion claim

同一 final candidate 只有在以下条件都满足时才可以声明：

`PROJECT_THREAD_HANDOFF_V1_READY=YES`

- G1 PASS：target Pro account 安装 + regular Chat explicit entry；
- G2 PASS：target Pro regular Chat DII/CARE normal-entry replay；
- G3 PASS：CAT-TRACE / CardiacNexus generalization；
- Skill 能消费当前 thread context；
- output 只有一份初始化 Prompt；
- no second confirmation；
- no repo write；
- source/generated/provenance/registry/catalog parity；
- README closure；
- version decision 按当前 policy 完成。

Work/Codex compatibility 可以另报，但不替代上述 completion claim。
