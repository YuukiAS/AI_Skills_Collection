# 056 Product Delivery Discipline — Review Package

状态：`AWAITING_EXECUTION_PACKAGE_CRITIC_REVIEW`

## Task identity

- Task key: `056_product_delivery_discipline`
- Review stage: v6 architecture + post-probe direction passed; execution package v0.1 drafted and awaiting independent Critic review
- Architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Post-probe authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- Probe result: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- CUHK Date evidence: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- Implementation Plan: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.1
- Canonical Goal: `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.1
- Kickoff Draft: `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.1
- Primary maintenance inbox: `docs/plugin-todos/workflow-core.md`

本 package 目前仍只是 review object。没有创建 execution branch/worktree，没有修改 production plugin/skill、Bridge Kit production 或产品 repo AGENTS，也没有授权 Executor。只有独立 Critic 对同版 Plan + Goal + Kickoff 给出 `READY_FOR_CODEX=YES`，且用户之后实际发送获批 Kickoff，才允许执行。

## Review history

### Round 1 — v5

Review object:

`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`

Decision: `RESULT = REVISE`

Stable blockers:

- `C056-B1-PERSISTENT-PROMPT-CAPABILITY`
- `C056-B2-REVIEW-ADMISSION-SCOPE`
- `C056-B3-ACTIVE-RULE-CONSUMPTION`
- `C056-B4-LAYER-DUPLICATION`

### Round 2 — v6 architecture / probe draft

Review object:

`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`

Independent Critic gave architecture `PASS`; v6 substantially closed the four blockers, but transport implementation remained intentionally unfrozen until the host capability probe.

### Capability probe

The tested Default-mode installation returned an empty answer after 114 seconds, so native Default `request_user_input` failed the persistence requirement. Same-thread durable transcript fallback resumed exactly once. Canonical evidence is:

`docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`

### Post-probe short review

The user relayed the independent Critic decision:

```text
RESULT = PASS
V6_ARCHITECTURE_STILL_VALID = YES
W2_TRANSPORT = DURABLE_TRANSCRIPT_WAIT_RESUME
DEFAULT_MODE_REQUEST_USER_INPUT_FLAG = DISABLE
SOURCE_DISCOVERY_REFINEMENT = PASS
CUHK_DATE_REFINEMENTS = PASS
READY_FOR_IMPLEMENTATION_PLAN_DRAFT = YES
```

This freezes the implementation direction but is **not** execution authorization.

## Frozen implementation direction

Architecture count remains:

```text
Lite baseline             6
workflow-core             5 capabilities
Frontend Design           3 production gates
AI Skills Maintainer      1 consumption-diagnosis capability
Bridge Kit                Lite distribution + host input transport/wait/recovery only
repo AGENTS               project-specific invariant/locator only
```

### W2 transport

Default `HUMAN_ONLY` gate uses `DURABLE_TRANSCRIPT_WAIT_RESUME`:

```text
preserve resume point
-> one plain-text question
-> DEPENDENT_EXECUTION_BLOCKED=YES
-> TERMINAL_BLOCKED=NO
-> no answer: no dependent work / polling / default / retry / timeout-continue / completion
-> same-thread explicit reply
-> reread current task/resume point
-> exact-once resume
-> post-action closure
```

Default native `request_user_input` is not used for HUMAN_ONLY.

### Bridge Kit fail-closed

Managed config target:

```toml
[features]
default_mode_request_user_input = false
```

Implementation must separate upstream feature/key presence from Bridge desired enabled state. `supported + desired false + actual false` is configured; stale true is drift. Plan-mode legitimate `request_user_input` remains upstream-owned and must not be broken by this Default-only flag.

### Source Discovery

Existing canonical local checkout/worktree/clone is discovered before network clone. Unrelated dirty work is protected but does not automatically invalidate the repo. Isolation reuses existing correct source or an explicitly authorized worktree. No normal `local clone -> remote remap` route.

### CUHK Date evidence

No W6/W7 or extra Lite rule. Representative breadth/material branches/state lifecycle/fallback semantics strengthen W1; hosted-provider and interaction-sequence fidelity strengthen W3; accepted structured interactions strengthen W5; localization/design consistency strengthens Frontend F-B/F-C. G7 preserves negative controls for small nonvisual work.

## Execution package v0.1

The current Critic review object is the **same-version bundle**:

1. `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.1
2. `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.1
3. `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.1

The execution package proposes:

- Bridge Kit `0.8.2 -> 0.8.3` only after source tests/current-host gates pass;
- AI_Skills repository `5.0.4 -> 5.0.5` PATCH only after production replay/release gates pass;
- `workflow-core 0.1 -> 0.2`;
- `web-development 0.1 -> 0.2`;
- `ai-skills-core 0.2 -> 0.3`;
- Bobbio runtime version unchanged; only current Figma handoff locator in `develop` AGENTS;
- no paid API/Terra;
- no modification to Lucerna/Mica/Asteria/SeminarArc/CUHK Date/CARE/EAT/Server-VPS/Longleaf_Bridge production;
- no main integration until implementation evidence for the exact final tuple receives independent review.

## Current Critic question

The independent Critic must now review the execution-ready package rather than redesign v6. In particular verify:

- file/repo ownership is correct and no central rule is duplicated into product repos;
- Branch/worktree/source strategy actually enforces local-first source discovery without inventing new authorization;
- Bridge Kit `false` config + validator semantics + Host/Lite wording + rollback are sufficient and not overbroad;
- Frontend Design production wiring actually exposes Figma/motion source in the generated plugin rather than editing unused source only;
- G1–G8 prove normal behavior, especially one final transcript HUMAN_ONLY smoke after all non-human QA;
- CUHK-Date-like coverage is risk-triggered, not a universal form checklist;
- version/release decisions follow canonical policy;
- final-candidate identity and no-main-merge boundary are strong enough for later implementation audit.

## Expected next-step boundary

If and only if independent Critic returns:

```text
RESULT = PASS
READY_FOR_CODEX = YES
```

then Planner returns the exact approved Kickoff to the user. Execution still begins only when the user actually sends that Kickoff.

Until then:

`NEXT_HANDOFF = CRITIC`
