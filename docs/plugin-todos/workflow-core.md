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

### 普通产品开发的人工交互、真实交付与重复失败止损
status: NEW
source: 2026-09-13 to 2026-09-15 official ChatGPT Data Export audit covering Mica, Bobbio, Lucerna, Asteria plus secondary projects; plus 2026-09-15 Lucerna OpenAI Usage Monitor post-user-setup failure; supersedes the earlier partial-thread evidence basis without claiming the automatic incident classifier is itself ground truth
evidence: [Planner v4 proposal](../design/PRODUCT_DELIVERY_DISCIPLINE_V4_PROPOSAL_2026-09-15.md)；private local export audit parsed all 27 `conversations-*.json` shards with 0 parse failures and produced curated high-signal project threads. Planner manual review found that the automatic 173-incident labels overcounted/misclassified normal status output, so raw frequency is not used as promotion evidence. High-confidence failures come from full-context Mica repeated live retries after green synthetic/E2E gates, Bobbio whole-screen/Figma drift, Lucerna close/refresh regressions despite existing acceptance rules, Asteria obvious connector/render defects reaching late review, and Lucerna Goal `01033_openai_usage_monitor_shared_vault`: pre-human build/tests correctly remained `NEEDS_HUMAN_ACTION`, the user then entered the credential, but the normal UI still showed `Not set up`, forcing follow-up fixes for validation feedback and split endpoint diagnostics. That last case proves prompt/wait alone is insufficient; post-user-action closure must be part of the same Goal.
problem: 需要用户动作时不显式询问，或虽然询问了却把 human step 当成接近完成而没有在用户动作后恢复同一 Goal 做真实闭环；明显可自检的问题反复叫用户验收；以构建、模拟测试、局部截图或自审字段替代真实使用路径；每轮修复缺少 faithful exact regression；同类失败无新信息仍继续重跑；已有规则存在时也可能因为没有实际加载/消费而继续失败。
project-specific context: Lucerna 的 close/hide-to-tray、OpenAI Costs/Usage scope 与 provider semantics，Bobbio 的 Zotero/Windows/Figma 文件，Mica 的 authenticated ChatGPT DOM 与 Atlas，Asteria 的具体箭头/卡片视觉语法都留在项目或领域 owner；不把具体 UI 造型、API scope 和账户/设备限制写成通用 workflow rule。

维护者处理要求（尚未实施，须经独立 Critic 审核）：

- 先检查 active `codex-workflow-protocol`、verification/live-state references、Lite 模板及项目已有规则；已有规则但真实输出仍失败时，按 execution/consumer regression 处理，不再增加同义口号。通用工作流负责何时要求专业证据，不接管专业设计判断。
- **凡 Goal authoring 时可预见需要用户动作，Goal/kickoff 必须显式包含 prompt contract：何时 prompt、用户只做什么、回复什么、禁止什么、收到回复后从哪里继续、post-action acceptance 是什么。** Executor 到达 gate 时必须实际调用当前 host 的 request-user-input/prompt；无 prompt tool 才退化为清晰可见的单步聊天请求。不得静默轮询，也不得仅因一个可恢复用户动作直接结束成不可恢复 `BLOCKED`。
- Human action 只是 checkpoint。用户完成动作后，Executor 必须恢复同一个 Goal 并自己验证 post-action 正向结果；credential/setup/provider 类任务至少验证适用的 accepted/validated/persisted/provider-live/normal-UI/restart-reuse 语义。把“用户已经输入/点击”直接当完成 = FAIL。
- agent 能自行观察/测试的先自己完成；不得复问同范围已获授权。Bridge Kit/host 已有 user-input 能力时先验证实际调用，而不是假定缺功能。
- 为新增功能、行为变化和 bug 修复要求与风险匹配的 targeted validation；deterministic bug 尽量证明 old-bad/new-good，同一 live-only failure 则保留一次真实 failure capture 并构造 faithful replay。broad suite PASS 不能替代原投诉。
- 区分 proxy/synthetic/browser/native/live evidence，claim scope 不得超过 evidence scope；pre-human build/test 不能证明 post-human integration；candidate identity 变化后关键 gate 必须由当前 candidate 直接通过。
- 诊断请求与最终验收分开。用户/外部 reviewer 再次看同一路径前，必须出现新的 root-cause hypothesis、repair 或 replay evidence；否则停止真人/full-suite循环。
- 加入 repeated-failure circuit breaker：相同症状再次出现、同一检查无新信息重复失败、或用户再次拒绝同类结果时，先核对 candidate identity、fixture fidelity、规则是否实际加载与 failure attribution，不自动开下一轮 heavy test / Atlas / external review。
- 每次修复保护 adjacent accepted behavior；真正互斥的新产品/科研选择才升级给用户，普通可逆实现细节由 Executor 自行处理。
- 交付核对原始正向目标、对应环境/版本、完整使用路径、关联既有行为、真实数据与剩余条件；不能因为 tests/logs/process gate PASS 就写产品完成。
- Lite/AGENTS 只保留不依赖 plugin 触发的短 baseline；完整流程由 Verified Workflow 按需提供。设计完整性、Figma 往返、整屏质量由 Frontend Design；科学图示语义由 Scientific Visualization；底层 prompt/wait/runtime 机制归 Bridge Kit。

进入实施前的 capability replay 要求见 v4 Proposal：必须从实际安装/触发入口证明 Goal-level prompt contract、prompt/resume、post-user-action closure、faithful replay、repeat-failure stop、evidence-surface fidelity 和 should-not-change；同时证明纯 docs、只读诊断和非视觉 server task 不会被升级成 Figma/付费 review/全套 human QA。静态检查规则文本存在不是行为 PASS。

## Do not do

- Do not duplicate Bridge Kit core Reviewed Handoff implementation in this repo.
- Do not use workflow-core to make domain judgments for writing, Presentation, statistics or imaging.
