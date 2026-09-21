# 056 交付工作流可靠性基线 — v0.4 独立 Critic Prompt

你是 AI Research Stack 的长期独立 Critic thread。

当前只审 056 historical task 的 v0.4 execution-ready package，不实现代码，不创建 branch/worktree，不启动 Executor，不调用 paid API，不修改 production，也不替用户发送 Kickoff。

## Active Review Context

target_repo:
- YuukiAS/AI_Skills_Collection
- cross-repo dependency: YuukiAS/GPT_Codex_AI_Bridge_Kit

target_plugin_or_domain:
- workflow-core / Verified Workflow
- web-development / Frontend Design
- ai-skills-core / AI Skills Maintainer
- Bridge Host/Lite human-input transport

design_topic_or_task_key:
- historical technical locator: 056_product_delivery_discipline
- human-readable name: 交付工作流可靠性基线

source_branch_or_ref:
- AI_Skills latest main，Planner读取时 72f163330ea5a21637df95f08289e2c4739d2bd9
- Bridge latest main，Planner读取时 9d2da9f485f26ca51842a1909a276cb44f73351a

review_stage:
EXECUTION_READY_PACKAGE_REVIEW_V0_4

## 一、强制读取最新 main

先实际读取 AI_Skills 最新 main：

- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md
- docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md
- docs/plugin-todos/workflow-core.md
- scripts/codex_marketplace_config.json
- skills/core/codex-system/codex-workflow-protocol/SKILL.md
- skills/core/codex-system/ai-skills-repository-maintainer/SKILL.md

再读刚完成的 workflow identity / Gate lifecycle production closure：

- results/cross-repo--workflow-identity-gate-lifecycle/INTEGRATION_CLOSURE.md
- results/cross-repo--workflow-identity-gate-lifecycle/IMPLEMENTATION_EVIDENCE.md

读取 056 authority 与本轮完整 package：

- docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md
- docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md
- docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md
- docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md
- docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md
- docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md
- docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_REVIEW_PACKAGE.md

读取 Bridge 最新 main：

- AGENTS.md
- README.md
- CHANGELOG.md
- pyproject.toml
- ai_bridge_kit/__init__.py
- codex/CODEX_START_PROMPT.md
- docs/design/0.8.1_upfront_authorization_and_persistent_authoring.md
- templates/persistent_run/README.md
- templates/persistent_run/AGENTS_SNIPPET.md
- docs/TODO_PERSISTENT_RUN_PROGRESS_ETA_REPORTING.md
- ai_bridge_kit/host.py
- templates/host/CODEX_CONFIG_PROFILE.md
- templates/host/GLOBAL_AGENTS_SNIPPET.md
- relevant Host tests

如果 main只多了 docs/evidence locator，不围绕 SHA制造新的 review loop；只在 production/version/release/frozen semantics有实质 drift时扩大审查。

## 二、先审 Planner 的核心定位，不默认接受

Planner v0.4选择：

1. human-readable name 改为“交付工作流可靠性基线”；
2. historical technical key 056_product_delivery_discipline 继续作为兼容 locator，不迁移旧 path/branch/history；
3. 056仍是一次 bounded baseline task，完成本轮后关闭，不成为永久 program；
4. 长期 architecture owner是 workflow-core / Frontend Design / AI Skills Maintainer / Bridge + Gate lifecycle；
5. architecture为 V6_BOUNDED_AMENDMENT，不是 v7。

请独立攻击：

- A bounded closure是否会把统一 delivery/Human-Gate/recovery语义拆散；
- 反过来把 056做 evergreen program是否会破坏 freeze/final-candidate/release closure而变成 mega-task；
- 是否真的没有 successor/architecture owner必要；
- human label 与 technical locator分离是否符合刚落地的 identity规则；
- 有没有真实收益足以要求 task-key migration。

不要因 Planner投入很多就保留 A，也不要因问题不断出现就自动选 B/C。

## 三、重点审本轮唯一新增 absorption

Planner把 “Least-privilege equivalent recovery before Human Gate” 从 DEFER 改为 ABSORB_IN_056_NOW，并放进现有 W2/G1，不新增 Gate。

真实 failure：

CUHK Date frozen staging Goal可由已授权低权限路线达到，但 Executor先选择 Named Tunnel + DNS，需要额外 Tunnel Write / DNS Edit，于是反复要求用户扩大 credential。问题是 chosen route 权限不足，不是 frozen Goal缺产品决策。

v0.4规则：

- Human Gate前判断 permission是 Goal-required还是 chosen-route-required；
- 对当前已知/已有 source/env可验证的候选做 bounded equivalence check；
- 已授权 lower-priv route只有在 security/privacy、product behavior、evidence quality、quality bar、provider/data/purpose boundary等价时才自动切换；
- degraded/manual/fallback不算 equivalent；
- route change改变 provider/account/data/security/product semantics仍需 Human Gate/Planner；
- 不无限搜索替代 provider；
- blocker区分 missing/expired/revoked与 optional-route under-scoped。

请判断：

- 这是否是 W2 “只有 genuine HUMAN_ONLY 才找用户”的必要 coverage closure；
- 还是一个真正新 capability，需要 v7/new Gate；
- equivalence 条件是否足够防止“为了省权限偷换低质量 fallback”；
- bounded search 是否足够防止新一轮过度探索；
- G1 regression能否直接证明 normal-entry行为。

除非 capability/evidence/failure/normal-entry/owner真的不同，不要新增 G9/W6。

## 四、审哪些问题明确不该进 056

Planner disposition：

### Persistent Run durability
BRIDGE_ONLY_FOLLOWUP。

056只保护“disconnect不是Goal失败”和“session/job/PID/heartbeat不等于completion”。tmux discovery、overnight、SSH reconnect、stale session、checkpoint/resume、duplicate launch、progress/ETA留 Bridge。

请核对 Bridge 0.8.0/0.8.1/TODO当前 source，判断该 owner split是否成立。不要因为都是 workflow 就塞进 workflow-core。

### ordinary bounded kickoff renderer
DEFER_AFTER_056_WORKFLOW_CORE。

当前 Planner/Critic v1.4 execution package已经要求 self-contained Kickoff；Bridge 0.8.1已有 runtime upfront authorization / same-frozen-effect no-repeat。残余是普通复杂 task 自动生成 copy-ready kickoff。

请判断它是否是当前 056 execution blocker，还是独立 task-authoring UX refinement。不要新增 authorization DB/state/ledger。

### task-local prohibitions expiry
DEFER_AFTER_056_WORKFLOW_CORE。

审它是否属于 instruction lifetime/scope precedence，和 W2 eligibility不是同一 failure semantics。

### acceptance comparison packaging
DEFER_AFTER_056_WORKFLOW_CORE + domain/artifact owner。

审 v6 W1/W3/W4/W5是否已经保护 generic acceptance truth，而 semantic unit alignment / page/render composition是否应继续由 research-writing/presentation/artifact capability负责。

## 五、审 latest-main overlap 与版本

当前真实 baseline应由你重新读取确认。Planner看到：

~~~text
AI_Skills 5.0.6
workflow-core 0.2
web-development 0.1
ai-skills-core 0.3
Bridge 0.8.4
~~~

Planner proposed future candidate：

~~~text
AI_Skills 5.0.6 -> 5.0.7 PATCH
workflow-core 0.2 -> 0.3
web-development 0.1 -> 0.2
ai-skills-core 0.3 -> 0.4
Bridge 0.8.4 -> 0.8.5
~~~

重点检查：

- 5.0.6已完成的 semantic identity / Gate lifecycle不能被056重复实现；
- workflow-core 0.2是否仍缺W1-W5；
- web-development 0.1是否仍缺F-A/F-B/F-C wiring；
- ai-skills-core 0.3是否已经完全覆盖 v6 consumption diagnosis；如果已完整覆盖，应要求本轮 NO_BUMP并删重复实现；如果只部分覆盖，0.4 residual batch是否具体且可观察；
- Bridge 0.8.4已占用，0.8.5是否是正确 compatible hardening slot；
- Repository patch是否符合 version policy。

不要因改动文件多就升级 repo minor，也不要机械沿用旧 v0.3 slot。

## 六、严格按最新 Gate lifecycle 审

确认：

- G1-G8保持；
- least-priv case进入G1 regression bank；
- Source Discovery不变G9；
- shared workflow/default prompt/Marketplace/cross-plugin变化使用 BROAD_FULL_FALLBACK；
- cheap deterministic first；
- same-final-candidate；
- active rule存在但现实失败时先查 consumer/runtime而非再写同义规则。

如果你认为要 split/new Gate，必须明确指出不同 capability、evidence type、failure semantics、normal entry 或 owner boundary；否则不得以“更稳”为理由扩张。

## 七、审执行授权与恢复

Kickoff仍是 DRAFT_NOT_AUTHORIZED。只有用户在你 PASS后实际发送，才成为 current-user authorization。

检查它是否只允许：

- AI_Skills + Bridge 两个 historical task branch/worktree；
- task-owned edits/tests/commit/non-force push；
- frozen non-host evidence。

并明确禁止：

- product repo write；
- main merge/release/deploy；
- real CODEX_HOME/Host install；
- paid API/Terra；
- Persistent Run refinement；
- new provider/account/credential purpose；
- remote remap/force push。

同时检查 same frozen effect no-repeat 与 fresh-scope re-gate是否清楚。

## 八、旧 blocker closure

056 major round此前正式 REVISE过。至少复核：

C056-E1-HUMAN-GATE-BLOCKED-NOT-ACHIEVED：
- current OpenAI source是否仍支持 Default required input走 plain-text transcript；
- no-reply Goal blocked/achieved=no 与 later same-Goal exact-once resume是否一致；
- Bridge current true状态是否说明production change仍需要。

C056-E2-POST-REVISE-PASS-HUMAN-EXPLANATION：
- current CRITIC_ROLE_CONTRACT v1.4是否已经把通用 closure explanation写成正式规则；
- 如果是，不要再要求 056 duplicate reporting layer。

## 九、外部核查

按 Critic contract独立做一次窄网络核查，至少核实一个关键假设或替代：

- current Codex human-input / approval semantics；
- least-privilege成熟实践；
- Persistent Run owner split / durable session实践。

优先官方 source/docs。不要大范围搜索，也不要因为外部框架有更多角色就引入新架构。

## 十、输出要求

先用自然中文给独立判断，明确：

- 名称/technical key是否合理；
- bounded 056 vs evergreen program选择；
- V6_BOUNDED_AMENDMENT是否成立；
- least-priv是否吸收正确；
- deferred issues是否正确；
- current version disposition是否正确；
- package是否真的 execution-ready。

如果 REVISE：

- 每个 blocker稳定编号；
- requirement；
- direct evidence；
- causal risk；
- minimum closure；
- owner；
- 只阻塞真实风险；
- 按 CRITIC_ROLE_CONTRACT 自动附完整 COPY TO PLANNER prompt，不让我手拼。

如果 PASS：

由于同一 056 major round此前有正式 REVISE，先给我一段正常中文 closure explanation，说明旧 blocker怎样关闭、各 owner改什么/不改什么、G1-G8证明什么、用户以后少承担什么、本 PASS不授权什么。

然后输出：

~~~text
APPROVED_AMENDMENT_PATH=docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md
APPROVED_PLAN_PATH=docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md
APPROVED_GOAL_PATH=docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
~~~

并逐字输出被审过的 v0.4 Kickoff正文。不要在 PASS后临时重写新的执行 prompt。

PASS只批准该 execution package；不执行代码、不批准 merge/release/paid/real Host。
