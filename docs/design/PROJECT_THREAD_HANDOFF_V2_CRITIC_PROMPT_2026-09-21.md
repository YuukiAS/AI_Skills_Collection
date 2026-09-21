# Project Thread Handoff V2 — Critic Recheck Prompt

你继续作为 AI Research Stack 的独立 Critic，对 standalone Skill `Project Thread Handoff` 做同一 pre-implementation design review 的复核。

不要开始实现，不要修改 production source，不要创建 Plugin/MCP/database/state machine，不要启动 paid evaluator。

## Active Review Context

target_repo: `YuukiAS/AI_Skills_Collection`  
target_plugin_or_domain: standalone Skill / science communication  
design_topic_or_task_key: `project-thread-handoff`  
source_branch_or_ref: `main`  
review_stage: pre-implementation design recheck after `APPROVE_WITH_CHANGES`  
reviewed baseline before V2 docs commit: `9f1c0d32abf49e674bcc7cab0e7287ed714a1199`  
Bridge reference baseline: `YuukiAS/GPT_Codex_AI_Bridge_Kit main@9d2da9f485f26ca51842a1909a276cb44f73351a`  
proposal: `docs/design/PROJECT_THREAD_HANDOFF_V2_PROPOSAL_2026-09-21.md`  
proposal version: V2  
prior review: chat-transferred Critic verdict `APPROVE_WITH_CHANGES`  
stable blocker IDs: `PTH-01`, `PTH-02`, `PTH-03`

先按 `CRITIC_ROLE_CONTRACT.md` v1.4 读取 AI_Skills 最新 main 的：

- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `AGENTS.md`
- `docs/SKILL_AUTHORING.md`
- `skills/core/codex-system/system-skills/skill-creator/references/openai_yaml.md`
- V2 proposal

只核对 latest main 是否出现与本方案直接相关的实质 drift；没有则不要 full-repo audit。

同时独立核查当前 OpenAI 官方 Skill metadata / invocation contract，尤其 `agents/openai.yaml` 的 `policy.allow_implicit_invocation`。如果产品 availability 与 Planner 的描述不同，请基于当前官方 source 明确指出。

## 本轮优先复核旧 blocker

### PTH-01 — authority / recency contract

检查 V2 是否真正关闭以下风险：

1. 最新用户明确决定/冻结决定不会被更晚 assistant brainstorming 覆盖；
2. thread-only delta 能对“研究意图/路线”暂时 supersede 旧 repo 计划，但不会伪造实验/代码事实；
3. working hypothesis、open question、assistant exploration、rejected recurrence risk、stale history 的处理足够清楚且不过重；
4. locator contract 能给 repo/source、branch/ref、path、事实责任范围，同时禁止编造未知 locator；
5. authority 是否按 claim type 区分，而不是再退回“最后一句赢”。

### PTH-02 — explicit invocation metadata

检查：

- V1 是否仍坚持 explicit invocation only；
- `allow_implicit_invocation: false` 是否只放在 `agents/openai.yaml -> policy`；
- `SKILL.md` 是否不再把它当普通 frontmatter；
- normal entry 是否明确为 skill picker / `$project-thread-handoff`；
- trigger eval 是否与“显式调用”一致，而不是一边禁止 implicit、一边把 bare “handoff”当正向自动触发；
- 正常 handoff 是否仍保持一次调用直接输出，不增加第二轮确认。

### PTH-03 — actual normal-entry regression

检查 V2 的 G2 是否足够直接验证真实失败：

- CARE 是 DII 当前使用的数据/数据来源，不是 DII 当前方法体系；
- 不因为历史 CARE discussion 恢复/推荐 CARE 模型；
- 最新有效决定覆盖早期 exploration；
- canonical source 可恢复事实主要给 locator；
- 最终只有一份初始化 Prompt；
- 无 repo-write side effect；
- 使用最终候选真实 skill identity / explicit normal entry，而不是只跑 helper/fixture；
- 不扩大成大型 benchmark、付费 evaluator 或新 Gate framework。

请同时判断 G1/G2/G3 三个 gate 是否已经是最小且足够，是否还有重复 gate 应删除。

## 保持已接受边界，不要无新证据重开

除非 V2 引入了真实回归，否则继续保持：

- standalone Skill，不做 Plugin；
- 不做 MCP/database/CURRENT/handoff history；
- 不做 repo-write mode，包括 opt-in write；
- Bridge Kit 仅作 source-role convention，不作 runtime dependency；
- handoff 不重新 audit 整个项目 repo；
- 新 thread 负责重新读取 canonical source；
- `Project Thread Handoff` / `project-thread-handoff` 命名保持；
- source path `skills/science/communication/project-thread-handoff/` 保持；
- 最小充分信息优先，800–1800 仅经验范围；
- 不新增确认阶段、状态机或自动知识整理。

## 额外需要你独立判断的现实边界

Planner 新增了一个产品 availability 说明：当前官方 Help Center 把 ChatGPT personal Skills 的创建/安装列给 Business、Enterprise、Healthcare、Edu，而用户当前是 Pro；因此 V2 不声称 `CHATGPT_PRO_NATIVE_ENTRY_VERIFIED`。

请判断这个边界是否处理正确：

- 它是否只是诚实的 surface availability 限制，不应迫使 V1 变成 Plugin；
- 是否需要修改当前 Skill 设计本身；
- V1 closure 是否应把“standalone skill behavior ready”和“ChatGPT Pro native entry verified”分开。

不要因为这一产品 availability 限制顺手设计新的 distribution system。若它确实让用户当前核心目标无法交付，请明确说明最小的产品决策点，而不是要求 Planner自行猜。

## 输出

先给自然中文结论，然后：

`VERDICT = PASS | REVISE`

逐项输出：

- `PTH-01 = CLOSED | OPEN`
- `PTH-02 = CLOSED | OPEN`
- `PTH-03 = CLOSED | OPEN`

若仍 REVISE：
- 只保留旧 blocker 未关闭部分，或 V2 真正引入的新直接风险；
- 每条给 requirement、direct evidence、causal risk、minimum closure、owner；
- 不换措辞移动终点；
- 按 Critic Role Contract 自动生成完整 COPY TO PLANNER prompt。

若 PASS：
- 明确这是 **pre-implementation design PASS**，不是 execution authorization；
- 说明这份 PASS 证明什么、不证明什么；
- 如果下一步需要 Planner 准备 implementation Plan + Canonical Goal + Kickoff Draft，则按 Critic Role Contract 自动输出 `NEXT_HANDOFF=PLANNER` 的完整 prompt；
- 不自行开始实现。
