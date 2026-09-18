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

### Review admission、Human Gate 与真实交付止损
status: PROMOTED
source: 2026-09-13 to 2026-09-15 official ChatGPT Data Export audit covering Mica, Bobbio, Lucerna, Asteria plus secondary projects; strengthened by Lucerna 01033/01034/01035, the 056 persistent-user-input host probe, Bridge Kit local-repo source-resolution feedback, and CUHK Date Questionnaire V4 real-project failures
evidence: [Planner v6 proposal](../design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md), [post-probe addendum](../design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md), [probe result](../design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md), [CUHK Date feedback](../design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md). The private historical export audit parsed all 27 `conversations-*.json` shards with 0 parse failures and produced curated high-signal project threads; its automatic incident classifier is not treated as ground truth.
problem: 真实项目反复暴露的是执行机制没有把“producer 自己做完、真实入口证明、只有真正 human-only 才问人、失败后不盲重跑”变成正常入口，而不是缺更多口号。典型表现包括：半成品过早交 GPT Work/用户；mock/browser/helper PASS 冒充真实 surface；用户被当 integration/UI debugger；agent 可解决的 repo/source/environment friction 被包装成 Human Gate；Default-mode prompt 自动过期；broad tests 绿但 catalog/locale/provider/interaction/material branch/hosted lifecycle 未闭环；rewrite 又破坏已接受 interaction。
project-specific context: Lucerna provider/Longleaf、Bobbio Zotero/Figma、Mica authenticated ChatGPT DOM、Asteria graph grammar、CUHK Programme/GeoNames/YuNet/provider names 等只作为 evidence；通用 workflow 不编码项目产品细节。

维护者处理要求（当前是已过 v6 architecture review 后的 implementation candidate；仍须按 056 post-probe Critic/implementation package 冻结后才可改 production）：

- **Acceptance Review Admission / Vertical Closure**：只对 acceptance/release/user-ready review 设硬 gate；advisory/diagnostic/design/architecture review 可在 candidate 未完成时发生，但不得输出 readiness/completion。进入 acceptance review 前，按当前 frozen feature/milestone 的适用链直接证明 source/contract -> runtime/backend -> state/persistence（若适用）-> normal entry -> real target behavior -> failure/recovery -> targeted regression -> risk-matched actual surface。UI shell、handler、placeholder、setup card、`IMPLEMENTED_WHEN_*`、schema 字段或 broad suite 不能单独算 capability complete。
- **Human-Gate Eligibility / dependency triage**：任何 user-input request 前先区分 `HUMAN_ONLY`、`AGENT_RESOLVABLE`、`UNSUPPORTED_WITH_EVIDENCE`、`OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE`、`SAFETY_OR_AUTHORITY_BLOCKER`。只有不可代理的 secret/login/OS/physical/user-decision 等 `HUMAN_ONLY` 才进入普通 Human Gate；repo/remote source/clone/sync/environment/tests/config generation/diagnostics 等可解决事项由 Executor 自己处理；unsupported interface truthful close；optional enhancement 不冒充 blocker。
- **Default-mode durable wait/resume，不能再声称 native persistent prompt**：056 probe 在 `codex-cli 0.142.0`、Default mode、feature enabled/tool available 下 114 秒返回空答案并 auto-resolve，`NATIVE_DEFAULT_PERSISTENT_PROMPT=FAIL`；同-thread `DURABLE_TRANSCRIPT_WAIT_RESUME=PASS`。当前 upstream handler 仍按 `mode == Plan` 决定 blocking，当前没有受支持的 Default-mode config timeout/always-wait setting。因此 HUMAN_ONLY gate 的主路线是 visible plain-text question + recorded resume point + stop dependent execution + explicit same-thread reply 后 exact-once resume；不 polling、不 default inference、不自动继续。到明确 deadline / 当前 run boundary 仍无答案时，必须报告 recoverable Goal blocked / achieved=no / complete=no / user-ready=no，并保留同一 Goal 的恢复点；这不是 impossible/STOP，也不新建 `BLOCKED` enum。Bridge Kit 056 候选把 managed `features.default_mode_request_user_input` 设为 false 以 fail-closed，避免 Default tool 被误用于 required gate；不得把 transcript fallback 重命名成 native prompt。
- **Human action 与 acceptance 分离 / post-action closure**：secret 输入、OAuth/OS 授权、网页登录、设备确认等只是 execution checkpoint。用户动作后 Executor 自动继续同一 Goal，完成 validation、persistence/runtime consumption、normal state、failure safety、targeted regression 等适用 closure；只有新的 final candidate 重新达到 Review Admission 才进入 acceptance。
- **Exact failure + faithful evidence**：feature/behavior/bug fix 使用风险匹配验证；deterministic bug 尽量 old-bad/new-good。unit/synthetic/browser/native/live/user evidence 只证明对应 surface，pre-human 不证明 post-human，旧 candidate 不能拼给新 candidate。
- **Representative coverage when the claim contains breadth**：只有 frozen objective 明确包含 catalog breadth、多 locale、material product branches、多 provider/variant 等时，W1 使用小型 representative coverage。schema/handler/sample list/source count 不能证明 breadth；单 happy path 不能证明所有 material branches。普通小任务不得因此继承全矩阵。
- **Fallback != primary capability**：fallback/recovery 只能证明 recoverability；除非 Goal 明确接受为等价产品结果，否则自由文本、`Needs setup`、manual review queue 等不能证明 primary search/catalog/automatic moderation/provider capability complete。
- **Hosted/external provider claim -> real configured evidence**：mock adapter tests 仍有价值，但 hosted capability claim 需要安全、bounded、实际 configured target evidence 和 normal entry confirmation；不因这条自动引入不必要 paid calls。
- **Interaction sequence fidelity**：controlled number input、typeahead、rank/drag、多步 selection、autosave 等在 intermediate state 会被转换时，验证真实 user sequence，而不只 final-value schema。例如 `1 -> 17 -> 178`、paste、backspace/replace、blur/commit。
- **State lifecycle closure**：对 upload/save/setup/configured 等持久 user state，风险需要时验证 action -> visible result -> navigation -> refresh/re-entry -> same authoritative state，而不是只看 mutation immediate success。
- **Repeat-failure circuit breaker / human-time budget**：相同症状再次出现、测试一直绿但真实路径再次失败、同一 reviewer/user 再次指出同类问题、或 active rule 再次被违反时，先核 candidate identity、rule/plugin loading、fixture fidelity、evidence surface、root cause；没有新信息不得重复 full suite/Atlas/GPT Work/真人验收。
- **Protect accepted / adjacent behavior**：修共享 UI/state/runtime 或 rewrite 组件时保护已接受行为；不能未经明确产品决策把成熟 structured interaction 降级为 generic/free-text fallback。具体视觉一致性由 Frontend Design。
- **Source discovery 必须优先复用正确本地 source**：task 指向已知 repo 时先定位 existing canonical checkout/worktree/clone，核 branch/ref/origin/dirty state。unrelated dirty work 要保护，但不能仅因 dirty 就默认另起 `/tmp` clone；需要 isolation 时优先 canonical local repo 的 clean worktree或机器上已有正确 clone；确实没有可用 local source 才 network clone。不要通过 local clone -> remote remap 制造额外 provenance/授权风险；修改 Git remote 仍需独立授权。这是 existing source-discovery refinement，不新增 workflow capability。
- 设计完整性、Figma 往返、图标/motion/design-system/localization surface quality 由 Frontend Design；科学图示语义由 Scientific Visualization；workflow-core 负责 gate、routing、evidence 与 completion semantics，不决定具体 style。
- final report 以“用户当前真正获得什么能力、哪些边界未验证”为中心，不以 tests/logs/process state 数量为中心。

进入实施前/实施后的 normal-entry capability replay 至少应覆盖：

1. producer-local implementation/test/actual-surface evidence 不足时，acceptance handoff 被拒绝；advisory review 不被错误阻止；
2. `HUMAN_ONLY` 在 Default mode 走 durable transcript wait/resume，用户未回答时 dependent execution 不继续、不 terminal BLOCKED；用户明确回复后 same-goal exact-once resume；
3. `AGENT_RESOLVABLE` local repo/source/environment issue 不 prompt 用户；`UNSUPPORTED_WITH_EVIDENCE` truthful close；
4. user action 后由 Executor 完成 integration closure，human action 本身不算 feature completion；
5. 原真实失败由 faithful targeted validation 捕获，修复后 final candidate 通过对应 surface；
6. CUHK-Date-like candidate 即使 broad tests 绿，只要存在 demo catalog 冒充 breadth、mock-only hosted provider、material branch 缺失、raw locale token、interaction sequence bug、fallback-only primary feature或hosted config 未消费 backend capability，`READY_FOR_USER_REVIEW` 必须失败；
7. rewrite 场景保护已有 accepted structured interaction；
8. existing canonical local repo + unrelated dirty state 时复用 local source/clean worktree，不重复 clone/remap remote；
9. docs-only/server-only/small nonvisual fix 不被强制进入 locale/catalog/provider/Figma/GPT Work/full E2E。

### Task-local prohibitions must expire with their task instead of becoming accidental global policy
status: NEW
source: Lucerna 01037 product-polish continuation, 2026-09-17
evidence: the current objective explicitly required creating `01037_product_polish_closure` task/result artifacts, but execution was repeatedly blocked because a prior task's local instruction said not to create a successor Goal; the user had to explicitly authorize that the current objective superseded the stale old boundary
problem: Historical task-local prohibitions are being treated as indefinitely persistent safety constraints even after the task that introduced them has ended and a newer user-approved objective explicitly requires the opposite action. This turns stale context into a false Human Gate, forces the user to resolve non-substantive instruction history, and can cause repeated approval loops even when the current task scope is clear.
project-specific context: The exact `01037` filenames and Lucerna successor-Goal wording are project-specific. The reusable workflow issue is instruction lifetime and scope: task-local restrictions need an explicit expiry/scope model, while true repository-level, persistent safety, security, destructive-action, or user-preference constraints must remain durable until explicitly changed.

### Post-056 acceptance artifact packaging / comparison-review fidelity
status: DEFER_UNTIL_056_COMPLETE
source: Clear Writing 055 final user-acceptance artifact failures, 2026-09-17
evidence: the user repeatedly requested a readable Original-vs-C6 acceptance artifact, but successive attempts were too short, mixed report/gate material into the acceptance surface, mechanically split content into hundreds of misaligned pages, confused preview/render claims, and repeatedly surfaced temporary paths. This exposed both a generic workflow packaging gap and a research-document semantic-alignment gap.
target layer: workflow-core release/user-acceptance closure. Research-document semantics belong to `research-writing`; slide/page composition and render quality belong to the relevant artifact/presentation capability.
scope boundary: **record only for now. Do not amend or reopen the already-reviewed 056 architecture, Plan, Goal, Kickoff, Gate taxonomy, or current implementation package. Finish 056 first. After 056 completes, Planner/Critic should map this evidence against what 056 actually delivered and add only genuinely uncovered behavior.**

Ownership split after triage:

- **workflow-core owns** acceptance admission, freezing the user-visible delivery contract, preventing gate/report evidence from masquerading as the review object, durable repo-local delivery, truthful artifact identity, minimum real-open validation, repeat-failure stop rules, cost discipline, and handoff/resume semantics.
- **research-writing owns** the scientific/report semantics of a research-document comparison: which source and rewritten units correspond, how section/claim/evidence/table/formula/code/limitation/future-work units are grouped, and how citation/reference scope is interpreted without breaking scientific attribution. This is now recorded in `docs/plugin-todos/research-writing.md` rather than duplicated here.
- **artifact/presentation capability owns** actual slide/page layout, typography, pagination, clipping/overlap, and format-specific render QA.

Follow-up requirements to assess after 056 completion:

1. **Freeze the acceptance-artifact specification before bulk generation.** Record the review object, included/excluded source and candidate ranges, target format, comparison mode, and the target domain's review-unit plan. Workflow freezes the contract; it does not invent research-specific paragraph/citation semantics.
2. **Acceptance artifact != report/gate dump.** The main review surface should contain the product output the user must judge. Workflow evidence, Gate history, render proof, paid-review receipts, and review packets belong in appendix/manifest unless explicitly requested as review content.
3. **Respect the domain-owned comparison plan.** Bulk packaging must consume the semantic units supplied by the relevant domain capability; it must not replace them with character-count, sentence-count, or arbitrary page slicing.
4. **Readability and actual surface outrank page count.** More pages are acceptable only when they improve legibility and correspondence. Hundreds of pages are not evidence of completeness if individual pages are sparse, misaligned, clipped, or difficult to compare.
5. **Final user-facing artifacts must use the canonical repo path.** `/tmp` is intermediate-only. Final acceptance artifacts must live under the task's repo-owned `private/exports/...` or another frozen repo-local delivery path, and handoff must give that canonical locator.
6. **PASS needs minimum real-open/content validation.** At minimum verify the artifact opens, expected page/slide count, major section coverage, key pages, and obvious clipping/misalignment. If every page was not visually checked, state `ALL_PAGES_VISUALLY_CHECKED=NO`; do not imply full visual QA.
7. **User feedback is not a normal QA loop.** After the first material acceptance-artifact failure, fix the generator/alignment/spec mechanism before regenerating. A second same-class failure triggers the existing repeat-failure circuit breaker: re-check input identity, domain comparison plan, delivery spec, and actual review surface before another bulk run.
8. **Artifact-only repair should minimize cost.** If source/final candidate/G7/rubric do not change, keep repair to layout/alignment/packaging; do not rerun the model or paid review. Before a large regeneration, generate a small representative section/sample and self-check it first.
9. **Handoff must name the artifact truthfully.** Distinguish complete candidate, comparison deck, gate evidence, render preview, and QA manifest. Do not call a preview page the acceptance artifact, and do not claim PPT/Office render QA merely because a same-source PDF rendered successfully.

Expected mapping after 056 completion, to verify rather than assume:

- W1 / Acceptance Review Admission: frozen user-acceptance artifact specification and review-surface readiness.
- W3 / Evidence Fidelity: artifact claims match the actual file/render/coverage surface.
- W4 / Repeat-failure Circuit Breaker: stop blind bulk regeneration after repeated packaging/alignment failure.
- W5 / Should-not-change: acceptance packaging must not mutate the already-certified product candidate/source/G7/rubric.
- Actual-Surface capability: PPT/PDF/Beamer or equivalent user-consumed artifact receives format-appropriate opening/render checks.
- AI Skills Maintainer / production consumption diagnosis: if repo-output/path rules already exist but delivery still escapes them, inspect the real producer/consumer path instead of adding another duplicate rule.

## Do not do

- Do not duplicate Bridge Kit core Reviewed Handoff implementation in this repo.
- Do not use workflow-core to make domain judgments for writing, Presentation, statistics or imaging.
- Do not add watcher/polling daemon/Persistent Run/tmux/Control/ledger/new state machine to simulate a persistent user prompt.
- Do not maintain a custom Codex fork as the default solution when the supported transcript wait/resume path suffices.
