# Project Thread Handoff V3 — Critic Recheck Prompt

你继续作为 AI Research Stack 的独立 Critic，复核 standalone Skill
`Project Thread Handoff` 的 pre-implementation design V3。

不要实现代码，不要修改 production Skill source，不要创建 Plugin、MCP、database、
CURRENT、state machine、browser extension 或新的 distribution system。

## Active Review Context

target_repo:
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain:
standalone Skill / science communication

design_topic_or_task_key:
`project-thread-handoff`

source_branch_or_ref:
`main`

review_stage:
pre-implementation design recheck after product-surface / invocation correction

prior proposal:
`docs/design/PROJECT_THREAD_HANDOFF_V2_PROPOSAL_2026-09-21.md`

prior package commit:
`22fd8e5330cd669c19ba7edf3a523bdb27f84bb4`

current proposal:
`docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md`

proposal version:
V3

V3 planning baseline before docs commit:
`d6bf0a6c11f9cce82a538bb542349035e4f10905`

Bridge reference baseline:
`YuukiAS/GPT_Codex_AI_Bridge_Kit main@9d2da9f485f26ca51842a1909a276cb44f73351a`

上一轮保持关闭：
- PTH-01 authority / recency；
- PTH-02 metadata placement；
- PTH-03 DII/CARE semantics。

不要无新证据重新打开这些 finding。

## 1. 强制读取

按 Critic Role Contract 先读取 AI_Skills 最新 main 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/SKILL_AUTHORING.md`
- `skills/core/codex-system/system-skills/skill-creator/references/openai_yaml.md`
- V3 proposal

检查 V3 package commit 之后 latest main 是否有与本设计直接相关的 production/contract drift。
没有则不要 full-repo audit。

## 2. 独立复核本轮 web evidence

不要只接受 Planner 摘要。至少独立核查以下来源或等价原始页面：

### OpenAI Developer Community

1.
`Custom Skill stopped executing in ChatGPT and Codex after August 20, 2026 — possible Skill runtime issue?`

https://community.openai.com/t/custom-skill-stopped-executing-in-chatgpt-and-codex-after-august-20-2026-possible-skill-runtime-issue/1391582

重点核实：
Pro 用户是否明确报告过此前在 ChatGPT Web 与 Codex 正常运行自定义 Skills。

2.
`@ and + shortcuts for skills not working in chat sidebar on one Plus account, but works on another. Bug?`

https://community.openai.com/t/and-shortcuts-for-skills-not-working-in-chat-sidebar-on-one-plus-account-but-works-on-another-bug/1395288

重点核实：
同设备不同 Plus 账号是否出现 regular Chat Skill invocation 差异。

3.
`Feature Request: Make "/skill" the Canonical Invocation Syntax for ChatGPT Skills`

https://community.openai.com/t/feature-request-make-skill-the-canonical-invocation-syntax-for-chatgpt-skills/1393711

重点核实：
ChatGPT `@` invocation 与 desktop slash-command 的 surface 差异。

### Reddit / community surface fragmentation

至少检查近期关于：
- regular Chat vs Work；
- web/iOS/local/cloud；
- account-specific Skills availability
的讨论。

Planner 参考：
- https://www.reddit.com/r/ChatGPT/comments/1w916l2/and_shortcuts_for_skills_not_working_in_chat/
- https://www.reddit.com/r/ChatGPT/comments/1vy26sy/why_are_skills_limited_to_chatgpt_work_on_web_and/

不要把 Reddit 当 universal product truth，只用于判断 rollout fragmentation 是否真实存在。

### 独立 Plus / Pro 实测

检查：

- https://note.com/tk_ax/n/n99650b498688
- https://www.auditit.app/template-skill
- https://lauvibecoding.substack.com/p/how-i-created-a-chatgpt-skill-for

重点核实是否真实出现：
- Personal Skill；
- Upload from your computer；
- Try in chat；
- Plus / Pro rollout。

### OpenAI source

检查：

- https://openai.com/academy/skills/
- https://academy.openai.com/public/clubs/work-users-ynjqu/resources/skills
- https://help.openai.com/en/articles/20001066
- https://developers.openai.com/zh-Hans/docs/build-skills

特别区分：
- 通用 Help Center plan wording；
- target account direct UI evidence；
- product/surface-specific availability；
- Codex `$skill` 语法；
- ChatGPT regular Chat 的 explicit invocation。

## 3. 本轮关键判断一：standalone Skill 方向是否继续成立

用户当前 Pro account 已直接显示：

`Plugins -> Skills`

且存在：
- 通过聊天创建；
- 通过编辑器创建；
- 从电脑上传。

这属于 target account 的直接 UI 证据。

请判断 V3 是否正确处理：

A. target account 创建/上传能力：
当前 direct evidence = YES。

B. target account ChatGPT regular Chat explicit invocation：
必须由 implementation 后 final candidate 的 target-surface smoke 验证；
不能因 rollout 不一致预先判 NO。

C. Work / Codex：
不是产品目标替代品。

如果你认为 standalone Skill 仍不成立，必须给出新的直接证据说明 target account
为什么即使有 Skills 创建/上传 UI，也无法合理进入 implementation 验证。
不要恢复旧的“现在做一个不能用的 Skill vs 等未来开放”二选一，除非有新的 target-account 证据。

## 4. 本轮关键判断二：invocation contract 是否 surface-correct

保持：

`agents/openai.yaml`

```yaml
policy:
  allow_implicit_invocation: false
```

该 metadata finding 已关闭，不重开。

只审 V3 是否正确取消了：

> ChatGPT normal entry 必须是 `$project-thread-handoff`

V3 现在定义 ChatGPT normal entry 为：

> 用户在当前 ChatGPT surface 中，通过该账号实际提供的正式显式 Skill
> 选择 / mention / invocation 入口调用已安装 Skill。

可能出现的真实入口包括：
- Skill picker；
- `@Project Thread Handoff`；
- Try in chat；
- desktop slash command；
- target account 当时实际暴露的其他正式显式入口。

Codex `$project-thread-handoff` 只能证明 Codex surface。

请判断这是否比固定字符语法更正确、也更容易真实验收。

## 5. 本轮关键判断三：G1 / G2 / G3 是否最小且足够

### G1 — Installation / Explicit Invocation Boundary

必须最终证明：

1. final candidate 可按 AI_Skills source-first 规则生成并 package；
2. invocation metadata 正确；
3. target Pro account 能上传/安装；
4. target ChatGPT regular Chat 能通过真实显式入口选择 Skill；
5. ordinary summary / ordinary project chat 不因 implicit routing 自动进入。

不要要求预先选定 `$` / `@` / `/`。

### G2 — Core Handoff Semantics / DII Target-Surface Replay

这必须是真正用户消费路径：

- target = 用户当前 Pro ChatGPT regular Chat；
- final candidate 已安装；
- 在已有较长上下文的普通 Chat 中显式调用；
- Skill 直接使用该 thread 已有上下文；
- 用户不重新粘贴整个历史。

必须验证：

- DII 是当前方法学项目；
- CARE 是数据/数据来源；
- CARE challenge models 不恢复为当前方法候选；
- 最新用户决定覆盖较早 assistant exploration；
- thread-only delta 正确携带；
- repo 可恢复事实以 locator 为主；
- 只输出一份初始化 Prompt；
- 不要求第二轮确认；
- 不写项目 repo。

如果 regular Chat 无法调用或 Skill 无法读取当前 thread context：

`G2 = FAIL`

必须返回 Planner/Critic，不得换 Work/Codex 偷换目标。

### G3 — Generalization / Should-not-change

CAT-TRACE：
后期冻结决定覆盖早期探索。

CardiacNexus：
代码/pipeline/实验数字重新读取 current repo；
handoff 只传最近判断、open question、下一步。

同时验证：
- 不 hardcode DII/CARE；
- 不依赖 Bridge Kit。

确认删除了与 G1/G2 重复的 ordinary-summary 与 no-repo-write 重测。

请判断：
- 三个 Gate 是否已经最小充分；
- 是否仍有重复；
- 是否有一个当前三 Gate 无法覆盖的真实用户能力缺口。

不要无直接风险新增 G4/G5。

## 6. 用户操作负担

V3 要求 Executor 在用户动手前先完成：

- Skill source；
- agents/openai.yaml；
- trigger eval；
- contract tests；
- registry/catalog/provenance/generated parity；
- upload-ready final Skill package；
- 本地/支持 runtime 开发验证；
- G3；
- final candidate freeze。

之后只请求用户一次：

> 在当前 ChatGPT Skills 页面上传/安装 final candidate，
> 然后在当前普通 Chat 中用实际可见的显式 Skill 入口调用一次。

请重点判断：
- 这是否满足“先把东西做完整，再让用户验收”；
- 是否还有不必要的用户往返；
- 是否错误要求用户承担开发调试。

不要为了更保险添加多轮 UI smoke。

## 7. 保持不变的设计边界

除非 V3 自己引入直接回归，不要重开：

- standalone Skill；
- no Plugin；
- no MCP；
- no database/CURRENT/history/state machine；
- no repo write / no opt-in write；
- no automatic new thread；
- no extra confirmation；
- one invocation -> one init Prompt；
- canonical source 由新 thread 重读；
- thread-only delta 只覆盖决策语义；
- entity-role disambiguation；
- locator non-fabrication；
- minimal sufficient information；
- 800–1800 只作经验范围；
- `skills/science/communication/project-thread-handoff/`；
- Bridge Kit 只作 source-role convention。

## 8. 输出

先用自然中文给总体判断。

然后：

`VERDICT = PASS | REVISE`

如果 PASS：

- 明确这是 `pre-implementation design PASS`；
- 明确 standalone Skill 方向是否继续成立；
- 明确 ChatGPT / Work / Codex surface 是否已正确区分；
- 明确 target-account regular Chat smoke 是否已经成为最终 normal-entry evidence；
- 明确 PASS 不代表 G1/G2 已运行，也不授权 implementation；
- 不新增 blocker；
- 按 Critic Role Contract 自动生成 `NEXT_HANDOFF=PLANNER` 的完整 prompt，
  要求 Planner 准备同版本：
  - Implementation Plan；
  - Canonical Goal；
  - Kickoff Draft；
  再交 execution-ready review。

如果 REVISE：

每条 blocker 必须：
- stable finding ID；
- requirement；
- direct evidence；
- causal risk；
- minimum closure；
- owner。

不得因为 Help Center 的一般套餐文字重新制造已被 target-account 直接 UI evidence 否定的
“Pro 一定不能用”结论。

不得因为 Work/Codex 可用就降低 regular Chat 产品目标。
