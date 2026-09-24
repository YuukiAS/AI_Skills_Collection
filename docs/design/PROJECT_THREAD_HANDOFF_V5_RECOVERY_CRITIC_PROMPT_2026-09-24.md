# Project Thread Handoff V5 — PTH-06 Critic Recheck

你继续作为 AI Research Stack 的长期独立 Critic，只复核
`Project Thread Handoff` V5 对唯一 blocker `PTH-06` 的关闭情况，以及 amendment 是否引入新的直接风险。

不要实现 source，不要创建 branch/worktree，不要更新 personal Plugin，不要调用 paid API。

## Active Review Context

target_repo:
`YuukiAS/AI_Skills_Collection`

target_plugin_or_domain:
standalone Skill / science communication

design_topic_or_task_key:
`science-communication--project-thread-handoff-recovery`

source_branch_or_ref:
`main`

review_stage:
`PRODUCTION_REFINEMENT_DESIGN_RECHECK_AFTER_PTH_06`

Prior reviewed proposal:
`docs/design/PROJECT_THREAD_HANDOFF_V4_RECOVERY_PROPOSAL_2026-09-24.md`

Prior reviewed commit:
`330e07526c388be76a8fef81e260094f4231deef`

Prior verdict:
`REVISE`

Only blocker:
`PTH-06 — Target-conversation provenance / same-Project attribution 不够可验证`

Current proposal:
`docs/design/PROJECT_THREAD_HANDOFF_V5_RECOVERY_PROPOSAL_2026-09-24.md`

proposal version:
V5

V5 planning baseline before docs commit:
`9e63c443ab9204cbf7619b8f0fdd8a81effbafc2`

Already accepted and not to reopen without new direct evidence:

- one Skill / two modes；
- Mode A；
- Mode B hydrate current new thread；
- explicit-only；
- authority/recency；
- thread-only delta；
- canonical repo/artifact authority；
- no MCP/database/CURRENT/transcript exporter/browser extension/state machine；
- no second Recovery Skill；
- no global Plugin Creator redesign；
- existing private/user-scope skills-only wrapper；
- canonical icon reuse；
- G1/G2/G3；
- standalone 0.1 -> 0.2；
- repository 5.1.0 -> 5.1.1 PATCH；
- central Plugins NO_BUMP。

## 1. Mandatory reads

先读取 latest main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/SKILL_AUTHORING.md`

然后 targeted read：

- V4 proposal；
- V5 proposal；
- current Project Thread Handoff `SKILL.md`；
- `agents/openai.yaml`；
- current result/MANIFEST；
- `PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md`。

检查 V5 package commit 之后 latest main drift。无相关 production/version/icon/distribution overlap就不要 full-repo audit。

## 2. 独立外部核查

请独立检查 current OpenAI official sources，不只接受 Planner摘要。

### Projects

- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://openai.com/academy/projects/

核对：

- project-only memory：same Project chats可以互相引用；
- project-only：Project外 conversation不可引用；
- Plus/Pro default-memory Project：Project内 past chats可用并优先，但并不形成绝对 Project隔离。

### Memory / past-chat sources

- https://help.openai.com/en/articles/8590148-memory-faq
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes

重点核对：

- Plus/Pro reference chat history可以查 past chats；
- past chat可以作为 Source出现并打开原 context；
- Sources可以区分 past chat / saved memory 等 source类型；
- Sources可能不展示影响回答的每一个因素。

请判断 V5 是否正确利用这些事实，而没有把底层叫“Memory”就错误拒绝真正 past-chat source。

## 3. PTH-06 核心修订

V5 现在明确：

> 底层 retrieval mechanism 的产品名称不决定 authority；
> 关键 recovered claim 能否归因到 target old conversation 才决定 authority。

因此：

### Conversation evidence

以下算合法 target-thread evidence：

- Memory Sources / Sources中明确目标 past chat；
- identifiable target conversation source card/title/link；
- 其他 product正式暴露的 target past-chat metadata。

即使这些由 ChatGPT memory/history retrieval infrastructure提供，也算 conversation evidence。

### 非 target-thread authority

以下不能替代 target old conversation：

- generic Saved Memory；
- profile summary；
- unsourced semantic recall；
- 无法归因到 target conversation 的 remembered context；
- model prior knowledge。

请判断这是否真正关闭 V4 wording缺陷。

## 4. Strong vs limited recovery

V5 不新增 machine state/schema，只限制 claim。

### Strong recovery

关键 route-changing recovered decisions 都有 target past-chat backing时，可以说已恢复 target old thread continuation state。

### Limited attribution-unverified recovery

只有 unsourced recall时：

- 可以给 limited summary；
- 不能声称是目标 old thread决定；
- 不能作为 authoritative thread-only delta；
- paraphrase不能冒充 quote；
- exact formula/prompt/contract若无 exact source必须标未验证。

如果缺失的是继续任务所必需的关键 decision：

- fail closed on that decision；
- 先尝试 target locator/source identification；
- 仍无 provenance时说明缺哪项；
- 仅当确实阻止继续时才允许一次最小 clarification；
- 不猜 route。

请判断：

- 这是否足够 fail-closed；
- 是否又变得过重；
- 是否需要额外状态机（Planner认为不需要）。

## 5. Default-memory Project claim

V5 已删除：

> 当前处在这个 Project，所以来源一定只来自这个 Project。

现在只声称：

> Mode B product boundary只接受 target same-Project conversation evidence；
> default-memory runtime可能暴露 Project外 context，因此未归因信息不能作为 recovery authority。

Project-only memory只是可选 stronger isolation，不是前置条件。

请判断这是否与官方 Projects/Memory docs一致。

## 6. Target locator contract

V5 保留：

- title；
- topic；
- date；
- unique phrase；
- project/task clue。

但改成：

> retrieval/candidate-identification clues

而不是：

> deterministic conversation database lookup keys。

流程要求：

- source可唯一归因 -> direct recovery；
- 多个真实 candidate 且选错会改变任务 -> 一次最小 clarification；
- 没有 source provenance时不得因为“模型觉得像这一条”就声称唯一定位。

请判断这个 contract是否足够可执行且不虚构产品 API。

## 7. G3 PTH-06 closure

G1/G2保持不变。

G3 现在增加 provenance criterion。

真实 target：

- current Pro regular Chat；
- AI Research Stack Project；
- new thread；
- same Project Bridge/SSH old conversation；
- final candidate；
- 用户不重新粘贴旧回答。

至少恢复：

- Bridge Kit本身不依赖 SSH；
- SSH是 publisher compatibility/safety相关 transport；
- WSL GitHub SSH identity未配置不等于 Bridge failure；
- 不应只为 gate改变实际 HTTPS开发环境；
- 更接近 compatibility acceptance/evidence问题。

同时必须观察：

- target Bridge/SSH old conversation作为 past-chat source或等价 identifiable target-chat provenance；
- target source足以让用户/Reviewer判断这是目标 conversation；
- generic Saved Memory/profile/unsourced recall不能替代该 source。

如果关键 recovered decision不能归因：

`G3 strong PASS = NO`

允许 limited recovery，但不能作为 release-critical strong recovery PASS。

Final claim只允许：

`target-conversation-backed semantic recovery verified; no observed cross-project substitution`

不得声称：

- raw transcript recovery；
- every-factor provenance；
- absolute retrieval isolation。

请判断这一 Gate是否足以关闭 PTH-06，而且没有新增 G4/G5 的必要。

## 8. Cross-Project boundary

V5 不要求另一个私有 Project做 live leakage test。

它依靠：

- official project memory scope；
- target-source provenance；
- contract regression；
- actual same-Project normal-entry replay。

请判断是否足够。

只有你能指出一个**如果不做跨 Project live test就可能错误宣称用户能力**的具体 failure，才可以提出 blocker；
不要因为“更保险”要求访问另一私有 Project。

## 9. 保持接受的 icon / wrapper / version

确认 V5 没改变：

Canonical icon：
`skills/science/communication/project-thread-handoff/assets/app-facing.svg`

Existing wrapper：
- same private Plugin identity；
- skills-only；
- no MCP；
- bundle canonical Skill；
- bundled icon byte-equivalent；
- composerIcon/logo优先 canonical；
- only deterministic conversion if target不支持 SVG；
- no redesign；
- Project Thread Handoff-specific update prompt，no global Plugin Creator redesign。

Version：
- Skill `0.1 -> 0.2`
- repo `5.1.0 -> 5.1.1 PATCH`
- all central Plugins `NO_BUMP`
- private wrapper runtime读取 current version/release id后 compatible increment。

不要无新证据重开版本或 wrapper architecture。

## 10. Amendment regression check

确认 V5 只改变：

- PTH-06 source/provenance wording；
- strong vs limited recovery claim；
- target locator phrasing；
- G3 provenance criterion；
- official Memory Sources evidence。

没有改变：

- Mode A；
- Mode B；
- output UX；
- authority split；
- scope；
- Gate count；
- icon；
- version；
- Plugin distribution strategy。

## 11. Output

先用自然中文说明：

- PTH-06是否真正关闭；
- past-chat source与generic Memory是否已正确区分；
- default-memory Project边界是否诚实；
- G3 provenance是否足够直接；
- V5是否只做bounded amendment；
- 是否有新direct risk。

然后：

`VERDICT = PASS | REVISE`

`PTH-06 = CLOSED | OPEN`

如果 REVISE：

每条 blocker必须包含：

- stable finding ID；
- requirement；
- direct evidence；
- causal risk；
- minimum closure；
- owner。

不要重新打开已接受的 V4 architecture，除非 V5 自己引入direct regression。

按 Critic Role Contract自动输出：

`NEXT_HANDOFF=PLANNER`

和完整 COPY TO PLANNER prompt。

如果 PASS：

明确：

`PRE_IMPLEMENTATION_DESIGN_PASS=YES`

并解释：

- PASS批准的是V5 design；
- 不表示G3已经运行；
- 不授权implementation；
- 不授权personal Plugin update；
- 不授权paid call。

然后：

`NEXT_HANDOFF=PLANNER`

并生成完整 COPY TO PLANNER prompt，要求 Planner准备同一V5 authority下：

- Implementation Plan；
- Canonical Goal；
- Kickoff Draft；

三者同版后再交 execution-ready Critic review。
