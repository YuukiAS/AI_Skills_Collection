# 056 交付工作流可靠性基线 — Execution Package Review v0.4

- Review object：v0.4 bounded amendment
- Historical task key：056_product_delivery_discipline
- Human-readable name：交付工作流可靠性基线
- Review stage：EXECUTION_READY_PACKAGE_REVIEW
- AI_Skills source locator：main@72f163330ea5a21637df95f08289e2c4739d2bd9
- Bridge source locator：main@9d2da9f485f26ca51842a1909a276cb44f73351a
- Amendment：docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md
- Plan：docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md v0.4
- Goal：docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md v0.4
- Kickoff：docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md v0.4
- Status：AWAITING_INDEPENDENT_CRITIC

## 1. 为什么 v0.3 不可直接执行

v0.3 的 architecture direction 没有被推翻，但其 execution baseline 已经实质过期：

- AI_Skills 已从 5.0.4 前进到 5.0.6；
- workflow-core 已从 0.1 前进到 0.2；
- ai-skills-core 已从 0.2 前进到 0.3；
- Bridge 已从 0.8.3 前进到 0.8.4；
- 最新 main 已把 semantic task identity / Gate lifecycle / regression-bank / broad-full fallback 接入 production；
- CUHK Date 又提供了一个直接击穿 W2 Human-Gate eligibility 的 least-privilege failure。

因此 v0.4 不是 locator refresh，而是 bounded execution-package amendment。

## 2. 不重开 v6

Critic 已经审过 v6 architecture 与 post-probe方向。本轮没有证据要求 v7。

保持：

- Lite L1-L6；
- W1-W5；
- F-A/F-B/F-C；
- Maintainer consumption diagnosis；
- Bridge transport/recovery boundary；
- G1-G8；
- Source Discovery regression不是 G9。

本轮新 case 只进入 W2/G1 regression coverage。

## 3. 名称 / identity decision 待审

Planner选择：

- Human-readable name：交付工作流可靠性基线；
- historical technical key：056_product_delivery_discipline 保留；
- 旧文件/path/history不迁移；
- 056仍是一次 bounded baseline implementation，完成后关闭；
- 长期演进由 workflow-core / Frontend Design / AI Skills Maintainer / Bridge + Gate lifecycle拥有，而不是让 056变永久 program。

Critic应攻击这一判断是否过简或过重，但不要仅因为新 semantic-key规则存在就要求迁移历史 056。

## 4. v0.4 新实质 amendment

唯一新纳入 production scope 的 failure 是：

least-privilege equivalent recovery before Human Gate。

它不创建新 capability/Gate，而补全 W2 的 eligibility：

permission gap -> 先判断 Goal-required vs chosen-route-required -> 若已有授权 lower-priv route且 frozen completion等价，agent自行恢复 -> 否则才 Human Gate。

等价必须保留 security/privacy/product behavior/evidence quality/quality bar/provider-data-purpose boundary；degraded fallback不算。

对应只增加 G1 regression，不增加 G9。

## 5. 明确 defer

- Persistent Run durability：Bridge-only followup；
- ordinary complex task bounded kickoff renderer：post-056 workflow-core；
- task-local prohibition expiry：post-056 workflow-core；
- acceptance comparison packaging：post-056 workflow-core + domain/artifact owners。

Critic应检查这些 defer 是否会让当前 056 claim失真；如果不会，不应以“更保险”为由扩大本轮。

## 6. Latest-main overlap / version review

Planner当前 candidate disposition：

~~~text
AI_Skills repository 5.0.6 -> 5.0.7 PATCH
workflow-core         0.2 -> 0.3
web-development       0.1 -> 0.2
ai-skills-core        0.3 -> 0.4
Bridge                0.8.4 -> 0.8.5
~~~

重点审：

- workflow-core 0.2 已有 Gate lifecycle，但没有 W1-W5，因此 0.3是否合理；
- web-development 0.1仍未完成 v6 wiring；
- ai-skills-core 0.3 已覆盖部分 gate/consumer principles，v0.4只允许 residual consumption-diagnosis，禁止重复 0.3 work；是否仍足以形成 0.4 user-visible batch；
- Bridge 0.8.5 是 existing Host/Human-Gate compatible hardening，不应升新 minor；
- repository patch而非 minor。

版本只是 future candidate identity，当前 docs-only planning commit不改 version source。

## 7. Pending historical Critic findings

v0.3 中 C056-E1 / C056-E2 尚需 Critic正式关闭：

### C056-E1

当前 upstream仍支持 Planner response：Default-mode request_user_input is_blocking 只在 Plan；Default instruction明确 required explicit user input使用 plain-text question，permission escalation不能依赖 request_user_input。Bridge production仍是 true，因此 056 residual work仍存在。

Planner维持 ACCEPT；Critic需决定是否关闭。

### C056-E2

最新 CRITIC_ROLE_CONTRACT v1.4 已把“同一 major round曾 REVISE后，最终 PASS先给用户可读 closure explanation”写成通用正式规则。Planner认为原 requirement已经由 current main覆盖，不需要 056再造 reporting mechanism。

Critic需正式关闭，不应再要求 duplicate 056-specific reporting layer。

## 8. Gate lifecycle review

v0.4 本身必须服从 latest policy：

- least-priv -> G1 existing regression；
- no new Gate；
- broad/full fallback；
- same-final-candidate；
- cheap deterministic first；
- active rule exists but consumer fails -> repair consumer/runtime, not duplicate text。

## 9. Authorization review

Kickoff必须被视为 DRAFT_NOT_AUTHORIZED。

Critic需要检查其 future user authorization envelope是否：

- 只授权两个历史 task branch/worktree与 task-owned ordinary push；
- 不把 repo Goal当 current-user auth；
- 不授权 product repos、main merge、release/deploy、real Host、paid API；
- same frozen effect以后不重复询问；
- 新 provider/resource/purpose仍需 fresh gate；
- least-priv recovery不会被用来静默改 provider/data/security/product semantics。

## 10. Source-drift rule

本 package 不要求 future docs/evidence-only SHA advance触发全面 re-review。只有 production/version/release/frozen semantics overlap 才返回 Planner/Critic。

## 11. Critic expected output

如果 REVISE：

- 只提出来自 v0.4真实新增/遗漏风险的 blocker；
- 每条给 requirement、direct evidence、causal risk、minimum closure；
- 自动生成完整 Planner prompt。

如果 PASS：

- 由于 056 major round历史上已有 REVISE，先按 Critic Contract v1.4用自然中文解释旧 blocker如何关闭、v0.4各 owner改什么/不改什么、G1-G8真正证明什么、用户以后少承担什么、本 PASS不授权什么；
- 然后给 approved paths / package identity；
- READY_FOR_CODEX=YES；
- 原样输出被审过的 v0.4 Kickoff正文；
- NEXT_HANDOFF=CODEX。

PASS只批准 execution package，不执行 056，不授权 merge/release/paid/real Host。
