# workflow-core — Long-Term TODO

Canonical maintenance inbox for the `workflow-core` plugin.

## Open candidates

### Keep AI_Skills workflow rules separate from Bridge Kit runtime bugs
status: PROMOTE_NOW
source: 042/043 Reviewed Handoff pause; 044 writing-style production replay
evidence: AI_Skills validation previously exposed a stale-review/implementation binding blocker for 042; task 044 then exposed a second generic runtime problem when an otherwise authorized plugin replay had to launch a fresh `codex exec` on a private local artifact and the Host Policy approval reviewer stopped it before the plugin could be tested. The generic runtime source of truth is `YuukiAS/GPT_Codex_AI_Bridge_Kit`; the bounded Host Policy design is now recorded there in `docs/design/host_policy_plugin_replay_authorization.md`.
target layer: external-runtime
problem: project workflows can be tempted to patch local history, add project-specific approval exceptions, or duplicate generic Reviewed Handoff / Host Policy runtime code when the defect actually belongs to Bridge Kit. Plugin-repair tasks also need a stable production-replay path; raw nested `codex exec` should not become an ad hoc per-task approval negotiation.
candidate action: keep generic validator and Host Policy fixes in Bridge Kit. For plugin production replay, use the Bridge-owned bounded replay path once implemented, rather than broad raw `codex exec` allow rules or AI_Skills-local Host Policy copies. After the Bridge Kit behavior is stable, make the AI_Skills Executor guidance prefer that path for plugin-repair replay without changing Planner/Reviewer authority.
promotion gate: Bridge Kit regression proving legal `PLANNER_DECISION` terminalization where relevant, plus a generic plugin-replay smoke showing an explicitly selected private local input can be processed by a fresh production Codex/plugin runtime and written to a local private replay directory without repeated approval, while dangerous Git/branch/remote actions remain protected.

### Real-task-driven Reviewed Handoff batches
status: PROMOTE_NOW
source: user decision after presentation Stage-5 loop
evidence: `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`
target layer: routing/qa
problem: an automation can become an endless synthetic recovery chain even after the product has reached a useful baseline.
candidate action: require explicit real blocker / plugin TODO source for long-running refinement batches and stop the watcher when the batch is closed or user redirects to real workflow refinement.
promotion gate: apply to the next AI_Skills maintenance batch without creating a second state machine.

### Review admission、持续用户提示与真实交付止损
status: NEW
source: 2026-09-13 to 2026-09-15 official ChatGPT Data Export audit covering Mica, Bobbio, Lucerna, Asteria plus secondary projects; strengthened by the 2026-09-15 Lucerna OpenAI Usage Monitor incident and the user's explicit correction separating pre-review completeness from persistent user prompts
evidence: [Planner v5 proposal](../design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md)；private local export audit parsed all 27 `conversations-*.json` shards with 0 parse failures and produced curated high-signal project threads. High-confidence evidence includes Mica repeated real-site failures after green synthetic/E2E gates, Bobbio whole-screen/Figma drift, Lucerna repeated UI/provider integration repairs after code/tests were presented as ready for the next user step, and Asteria obvious visual defects reaching late review. The automatic 173-incident classifier is not treated as ground truth.
problem: 两类问题必须分开处理。第一，producer 没有先把自己能完成、测试、观察和修复的实现/设计/actual-surface问题彻底收口，就过早把 candidate 交给 GPT Work 或用户，形成 `做一点 -> 验收 -> 暴露明显问题 -> 返修 -> 再验收` 的高成本循环。第二，Goal 明知后续需要用户做一个不可替代动作时，prompt 可能只是普通消息/短暂提示，或等待被外层 runner 当成 timeout/BLOCKED；用户要求的是 pending 到明确回应的 persistent blocking prompt。
project-specific context: Lucerna provider onboarding、Bobbio Zotero/Figma、Mica authenticated ChatGPT DOM、Asteria graph grammar 等只作为证据；通用 workflow 不编码具体 UI、provider、设备或视觉风格。

维护者处理要求（尚未实施，须经独立 Critic 审核）：

- **Pre-Human Readiness / Review Admission Gate**：在 GPT Work、外部 reviewer 或最终用户验收前，先完成 frozen scope 内所有 agent 自己能够完成的 implementation、targeted regression、known regression、actual-surface smoke、design/visual convergence、diagnostics 和 producer self-QA。禁止把半成品 checkpoint 当 review candidate，也禁止一 patch 一次 human/external acceptance。
- **Human action 与 final acceptance 分离**：secret 输入、OAuth/OS 授权、网页登录、设备确认等可能在任务中途必须由用户执行，但只是 execution checkpoint，不代表进入产品验收。所有不依赖该动作的代码、错误处理、UI、状态机、测试和 diagnostics 应先完成；用户动作后 Executor 自动继续同一 Goal 的 integration closure。
- **Foreseeable human gate 必须由 Goal 预声明**：写明 prompt trigger、最小 user action、reply、safety limit、resume point 和 post-action agent work。不要等运行到一半才临时决定要不要问用户。
- **Persistent blocking prompt**：到达 human gate 后实际调用 host 的 request-user-input/prompt capability；pending until explicit response/cancel，依赖链暂停，不静默轮询，不用 ephemeral notification/普通进度消息冒充，不因等待时间自动转 terminal `BLOCKED`，用户回答后从保存位置继续。同范围已答复/已授权不重复问。
- Bridge Kit/host 已启用 `default_mode_request_user_input`，但必须额外做真实 capability probe 证明 prompt persistence、no-expiry 和 runner wait semantics；规则文本存在不是行为证据。若 host 不支持，不在项目里临时造 polling/watchdog/state machine，回 Planner/Critic 判断最小 fallback。
- **Exact failure + faithful targeted validation**：新功能、行为变化、bug fix 都有风险匹配验证；deterministic bug 尽量 old-bad/new-good，live/native 难自动化时保留真实 failure capture + faithful replay。broad suite PASS 不替代原用户路径。
- **Evidence-surface fidelity**：unit/synthetic/browser/native/live/user evidence 各自只证明对应 surface；pre-human build 不能证明 post-human integration；旧 candidate PASS 不能拼给新 candidate。
- **Producer self-QA before external/human review**：用户和 reviewer 用于最终判断/盲区，不作为第一轮 debugger、设计师或测试员。producer 能自己看到的 obvious defect 必须先清零。
- **Repeat-failure circuit breaker / human-time budget**：相同症状再次出现、测试一直绿但真实路径再次失败、同一 reviewer/user 再次指出同类问题、或 active rule 再次被违反时，先核对 candidate identity、rule/plugin loading、failure hypothesis、fixture fidelity、evidence surface 和 root cause；没有新信息不得再次跑 full suite/Atlas/GPT Work/真人验收。
- **Protect accepted behavior + adjacent consistency**：修共享 UI/state/runtime 时保护既有 accepted behavior；若改 shared component/icon/layout/motion family，检查同族主要实例，不能只修当前截图造成产品内部风格漂移。具体视觉标准归 Frontend Design。
- 设计完整性、Figma 往返、图标来源、motion grammar、whole-screen quality 由 Frontend Design；科学图示语义由 Scientific Visualization；workflow-core 负责 gate、routing 和 completion semantics，不决定具体 icon/style。
- final report 以“用户现在真正能做什么、是否达到原目标”为中心，不以 tests/logs/process state 数量为中心。

进入实施前必须由同一 final candidate 通过至少以下能力 replay：

1. 普通 feature task 在 agent-local implementation/test/actual-surface QA 未绿时不会进入 external/human review；
2. 一个可预见 human-only action 在 Goal 中声明并触发 persistent blocking prompt，用户不回答时 workflow 保持 waiting 而非 timeout/BLOCKED；
3. 用户回答后同一 Goal 自动继续，不把 human action 当 completion；
4. 原失败由 faithful targeted validation 捕获，修复后通过；
5. 相同真实失败第二次出现时无新信息不会再次调用 user/external reviewer；
6. 一个 docs-only / server-only / simple task 不会被强制 Figma/GPT Work/全套 human QA。

## Do not do

- Do not duplicate Bridge Kit core Reviewed Handoff implementation in this repo.
- Do not use workflow-core to make domain judgments for writing, Presentation, statistics or imaging.
