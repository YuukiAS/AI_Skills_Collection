你是 AI Research Stack 的长期独立 Critic thread。

当前继续任务：

TASK_KEY = `056_product_delivery_discipline`

本轮审查对象：

- Repository: `YuukiAS/AI_Skills_Collection`
- Review package: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_REVIEW_PACKAGE.md`
- Proposal: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Probe draft: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_DRAFT.md`
- Review stage: Planner REVISE response / pre-implementation architecture review

上一轮你对 v5 给出 `RESULT = REVISE`，blocker 为：

- `C056-B1-PERSISTENT-PROMPT-CAPABILITY`
- `C056-B2-REVIEW-ADMISSION-SCOPE`
- `C056-B3-ACTIVE-RULE-CONSUMPTION`
- `C056-B4-LAYER-DUPLICATION`

本轮请复核这些原 blocker 是否真正被 v6 响应。不要因为 Planner 声称“RESPONDED”就自动关闭；只有你独立核对证据后才能关闭。

你只做审查：不实现 production skill/plugin，不修改 Bridge Kit production，不修改 Bobbio/Lucerna/Mica/Asteria/SeminarArc AGENTS，不启动 Executor，不创建 implementation Goal/Kickoff/branch，不运行 paid API，不执行 persistent-prompt probe，不代用户授权。

==================================================
一、强制读取最新 main
==================================================

先实际读取 AI_Skills_Collection 最新 main：

- `AGENTS.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_REVIEW_PACKAGE.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_DRAFT.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`（仅用于比较 revision，不把 v5 当 current authority）
- `docs/plugin-todos/workflow-core.md`
- `docs/plugin-todos/web-development.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/plugin-todos/scientific-visualization.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `skills/core/codex-system/codex-workflow-protocol/references/task-template.md`
- `skills/core/codex-system/codex-workflow-protocol/references/verification-matrix.md`
- `skills/core/codex-system/codex-workflow-protocol/references/live-state-delegation.md`
- `skills/tools/frontend/figma-design-to-code/SKILL.md`
- `skills/tools/frontend/design-system-tokens/SKILL.md`
- `skills/tools/frontend/visual-direction/SKILL.md`
- `skills/tools/frontend/motion-interaction/SKILL.md`

再独立读取真实项目依据：

### Lucerna current main

至少：

- `AGENTS.md`
- `prompts/tasks/01035_longleaf_extensions_daily_surface.md`
- `results/01033_openai_usage_monitor_shared_vault/result.md`
- `results/01034_openai_proxy_route/result.md`
- `results/01035_longleaf_extensions_daily_surface/result.md`

重点检查 Planner 是否准确理解：

- 01033/01034 主要暴露 faithful sequence / release-path enforcement，而不是缺更多相同 AGENTS 文案；
- 01035 task 已明确授权读取/必要时处理 canonical source、要求完成所有 non-human work 后再问用户，但 result 仍把 local checkout/source/environment friction、unsupported editor probe、UI scaffold/conditional capability 等聚合进 Human Boundary；
- 这是否真实支持 v6 的 `Human-Gate Eligibility / Dependency Triage`、`Vertical Capability Closure` 和高风险多 deliverable Goal 的轻量 closure table。

### Bobbio develop

至少：

- `AGENTS.md`
- `docs/DEVELOPMENT_WORKFLOW.md`
- `docs/PRODUCT_DESIGN_BRIEF.md`
- `docs/design/FIGMA_HANDOFF.md`

确认 current normal frontend/Product Design read-list 是否真的缺 `FIGMA_HANDOFF.md` locator，以及 pre-user native self-QA → GPT Work → user acceptance 是否已经存在，不应再复制中央 checklist。

### Mica current main

- `AGENTS.md`

检查 reproduce real failure、bounded diagnostic、fixture improvement、focused-before-full-E2E、one-short-manual-loop 等 active rules 是否已经覆盖语义；默认优先查 consumption/fidelity，不加同义 repo rule。

### Asteria current main

至少：

- `AGENTS.md`
- `prompts/AGENT_RULES.md`
- `docs/operations/development/DEVELOPER_VISUAL_SELF_QA_CONTRACT.md`
- `docs/design/SCIENTIFIC_GRAPH_VISUAL_SYSTEM.md`

确认 visual self-QA、generic-fix、GPT Work-before-human 已足够强；问题是否主要转为 normal-entry consumption replay。

### SeminarArc current main

- `AGENTS.md`
- 搜索 project-level canonical Figma/design locator

没有直接证据则继续保持 `EVIDENCE_NEEDED`。

### Bridge Kit current main

至少：

- `templates/host/GLOBAL_AGENTS_SNIPPET.md`
- `templates/host/CODEX_CONFIG_PROFILE.md`
- `ai_bridge_kit/host.py`
- `tests/test_host_policy.py`
- request-user-input / wait-resume 相关 source/tests

==================================================
二、必须独立做当前网页 / upstream source 研究
==================================================

每轮实质 Critic 审查必须独立检索，不得只复述 Planner 链接。

至少重新核查：

1. 当前 `openai/codex` source 中：
   - `default_mode_request_user_input` feature status；
   - Default vs Plan 的 `request_user_input` `is_blocking` 语义；
   - `auto_resolution_ms`；
   - 当前 Default-mode instruction 对真正必须用户回答才能继续的指导；
2. 当前公开 issue / 官方证据是否仍支持 Default/Desktop 存在 auto-resolution / timeout 风险；
3. OpenAI 当前关于 AGENTS、human attention、agent self-review / legibility / workflow feedback loop 的公开实践；
4. Figma 当前 Ready for dev / Dev Mode / components / variants / design handoff；
5. 一个成熟 icon system 与 motion/reduced-motion 官方实践，例如 Microsoft Fluent/WinUI，但请独立读取当前资料。

记录实际读取了什么、采用/不采用什么，以及它怎样改变结论。

==================================================
三、复核四个原 blocker
==================================================

### C056-B1 — Persistent Prompt Capability

重点审 v6 是否正确把 native persistent prompt 改为 `PROBE_REQUIRED`，不再当已验证能力。

审查 probe draft 是否最小、可执行、无高风险副作用，并至少检查：

- exact CLI/App version；
- Default mode，不允许偷偷切 Plan；
- feature/tool availability；
- 一次 harmless、确实必须用户回答才能继续的 question；
- unanswered 超过当前已知 auto-resolve window；
- 150 秒是否是合理且诚实的观察窗：只证明超过已知 1–2 分钟窗口，不冒充数学上的“永久”；
- 是否会出现 empty/default answer；
- dependent execution 是否明确暂停；
- explicit answer 后 exact-once resume；
- cancel path；
- terminal BLOCKED / automatic retry / tracked workflow state；
- host probe 没有过度声称完整 Reviewed Handoff counter preservation；
- native FAIL 后的 fallback 是否严格标成 `DURABLE_TRANSCRIPT_WAIT_RESUME`，而非重命名为 native persistent prompt；
- fallback 失败后是否明确 `HOST_CAPABILITY_GAP`；
- 是否禁止 watcher/polling daemon/Persistent Run/tmux/Control/ledger/new state machine。

如果 probe 本身仍有关键缺陷，`PROBE_DRAFT=REVISE`，不能放行执行。

### C056-B2 — Review Admission Scope

确认 v6 是否真正区分：

- acceptance/release/user-ready review：硬 admission gate；
- advisory/diagnostic/design/architecture review：可在未完成 candidate 上进行，但不能声称 readiness/completion。

检查：

- complete 是否仅相对 frozen feature/milestone/review object；
- evidence 是否 risk/surface-scaled；
- ordinary docs/backend/server/tiny fix 是否不会被强制 Figma/GPT Work/full E2E/native smoke；
- self-reported PASS 字段是否不能绕过 final-candidate direct evidence；
- user final acceptance 前的 internal/GPT Work repair loop 是否避免反复把用户拉回来。

### C056-B3 — Active Rule Consumption

逐行审 v6 consumption matrix：Lucerna、Bobbio、Mica、Asteria、SeminarArc。

重点判断：

- Planner 是否误把“规则现在存在”写成“历史失败时一定加载过”；
- Lucerna 默认不加通用 AGENTS 是否正确；
- Bobbio 最小 repo candidate 是否真的只需要 locator，而不是更多 checklist；
- Mica 是否保持 consumption/fidelity-first；
- Asteria 是否保持 replay-first；
- SeminarArc 是否正确保留 `EVIDENCE_NEEDED`。

### C056-B4 — Layer Duplication

审 v6 是否真正收敛到：

```text
Lite 6
workflow-core 5
Frontend Design 3
AI Skills Maintainer 1
Bridge Kit only transport/wait/recovery
repo AGENTS only invariant/locator
```

不要只数条目；判断是否仍存在语义重复。

特别审：

- Human-Gate Eligibility 是否正确并入 W2，而不是新增第六个 workflow capability；
- Vertical Capability Closure / Post-action closure 是否正确并入 W1/W3；
- lightweight Goal Coverage Table 是否只用于高风险/多 deliverable gate 前的 task-local evidence，而不会演变成新 ledger/schema/state machine；
- Frontend F-A/F-B/F-C 是否已经吸收 web-development TODO 重复候选，而不是新增另一套 checklist。

==================================================
四、审 Lucerna 01035 新反馈的因果性
==================================================

请独立判断下面这条是否成立：

> 任何 Human Gate 前必须先证明依赖属于 irreducible HUMAN_ONLY；AGENT_RESOLVABLE 必须由 Executor解决，UNSUPPORTED_WITH_EVIDENCE 应 truthful close，OPTIONAL_NOT_REQUIRED 不阻塞当前 closure，只有 safety/authority 新边界才进入现有 STOP/Planner/approval 路径。

如果你同意，检查分类是否足够、是否互斥、是否容易被 Executor 通过“把 required 标 optional”钻空子。

同时审 W1 的 vertical closure：

```text
authoritative source/contract
-> backend/runtime
-> persistence/state（若适用）
-> normal product entry
-> real target behavior
-> failure/recovery
-> targeted regression
-> actual surface（风险需要时）
```

它是否能防止 `UI shell / handler / placeholder / setup surface / IMPLEMENTED_WHEN_*` 冒充完整 capability，同时又不会让纯 backend library/API-only task 被迫拥有 UI/persistence 等不相关层？

如果需要，要求 Planner 将链条明确写成“适用项 closure”，不能机械全选。

==================================================
五、R1–R10 disposition 与新架构
==================================================

检查 v6 是否充分响应上一轮 disposition：

```text
R1  MOVE_TO_LITE
R2  MERGE_WITH_R5
R3  MERGE_WITH_R4
R4  PROBE_FIRST
R5  MERGE_WITH_R2
R6  MERGE_WITH_R7
R7  MERGE_WITH_R6
R8  KEEP
R9  KEEP
R10 MOVE_TO_FRONTEND_DESIGN
```

如仍不同意某项，给出稳定 finding 与最小修改条件。

==================================================
六、Capability Gate Matrix
==================================================

逐项审 G1–G8 是否证明真实行为，而不是 Markdown/字段存在：

- G1 Human-gate recognition + transport
- G2 Acceptance Admission
- G3 Resume/post-action closure
- G4 Faithful regression
- G5 Evidence/final-candidate
- G6 Frontend design consumption
- G7 Non-overreach
- G8 Consumption-regression diagnosis

特别检查：

- 是否直接验证 agent-resolvable dependency 不会被 prompt；
- unsupported interface 不会被推给用户；
- genuine secret 可以进入 human gate；
- scaffold without canonical backend capability 不能 acceptance-ready；
- active rule 不消费时会暴露 consumption regression；
- docs/server/small nonvisual negative cases 不被升级重流程。

==================================================
七、重新比较现实替代方案
==================================================

至少比较：

A. v5 原样
B. v6 的 6 Lite + 5 workflow + 3 Frontend
C. repo-specific only
D. Bridge-first
E. consumption-only

重点判断 v6 是否是最小充分机制，而不是因为“问题很多”就机械选择最复杂方案。

如果存在更简单、仍能阻止 Lucerna 01033/01034/01035、Bobbio/Mica/Asteria 主要 failure 的路线，必须指出。

==================================================
八、结论格式
==================================================

每条 blocker 给稳定编号，并写：对应要求/合同、直接证据、因果风险、最小关闭条件和 owner。偏好建议与 blocker 分开。

最终必须给：

```text
RESULT = PASS | REVISE
TASK_KEY = 056_product_delivery_discipline
REVIEW_OBJECT = docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md
PROBE_DRAFT = PASS | REVISE
READY_FOR_CAPABILITY_PROBE = YES | NO
READY_FOR_IMPLEMENTATION_PLAN = YES | NO
```

重要：

- 即使 v6 architecture PASS，只要 persistent transport probe 结果仍可能影响 transport implementation，默认 `READY_FOR_IMPLEMENTATION_PLAN=NO`，先完成已审 probe；
- `READY_FOR_CAPABILITY_PROBE=YES` 只表示 probe prompt 本身通过架构/安全审查，**不等于用户已经授权执行**；只有用户实际把 approved probe prompt 发给 Codex，才构成本轮 probe 的执行授权；
- 不得把 probe PASS 预先假定为 native transport PASS。

如果 `REVISE`，按 Critic contract 自动附一段可以直接发回长期 Planner thread 的完整返修 prompt。

如果 `PASS` 且 `PROBE_DRAFT=PASS`，请在正常结论后附上你实际审过的 probe Codex prompt逐字正文，使用：

```text
=== APPROVED 056 CAPABILITY PROBE BEGIN ===
<verbatim prompt from docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_DRAFT.md>
=== APPROVED 056 CAPABILITY PROBE END ===
```

不要重写成另一版未审 prompt。
