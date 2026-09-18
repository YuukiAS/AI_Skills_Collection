# 056 Product Delivery Discipline — Codex Kickoff Draft

- Execution package version: `v0.3`
- Task: `056_product_delivery_discipline`
- Plan: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.3
- Goal: `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.3
- Post-057 revalidation: `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_POST_057_SOURCE_DRIFT_REVALIDATION_2026-09-18.md`
- Status: `DRAFT_NOT_AUTHORIZED`

Only after an independent Critic reviews this exact v0.3 Plan + Goal + Kickoff, closes or revises C056-E1/E2, and returns `READY_FOR_CODEX=YES` does the user sending the approved `## Kickoff` text authorize execution.

## Kickoff

执行 `056_product_delivery_discipline` 的 **v0.3 post-057 implementation stage**。严格按 v0.3 frozen Plan/Goal；不要重新设计已经通过的 v6 architecture。

### 1. Current authority and source preflight

056 architecture authority remains:

- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_POST_057_SOURCE_DRIFT_REVALIDATION_2026-09-18.md`

At Planner revalidation:

- AI_Skills main = `f68e800fb604850c20a29cb3c7572e4f1a119236`;
- Bridge main = `e1d6b781ad7e56d567bed419001069baf439d0a5`, current source version `0.8.3`.

Before editing, fetch/re-read current source and verify repo identity, remote identity, branch/ref freshness and dirty ownership. Do not use old chat/ref snapshots as current source.

If AI_Skills main has advanced only by this approved v0.3 package, use kickoff-time latest compatible main. If relevant production source has changed, stop and report rather than silently adapting architecture.

For Bridge, expected implementation base is `e1d6b781ad7e56d567bed419001069baf439d0a5`. If Bridge main has advanced with relevant Host/Lite semantics, stop for bounded revalidation.

### 2. Authorized writable repositories

#### AI_Skills_Collection

Create exactly:

- branch: `reviewed/056_product_delivery_discipline`
- task-owned worktree: `AI_Skills_Collection-056-product-delivery-discipline`

Prefer the verified existing local canonical source; do not network-clone merely because another checkout is dirty.

Allowed task-owned changes only:

- workflow-core W1-W5 + existing Source Discovery enforcement;
- web-development / Frontend Design F-A/F-B/F-C;
- canonical marketplace wiring/generation for existing Figma-handoff + motion skills;
- ai-skills-core production-consumption diagnosis;
- focused/full tests and G1-G8/source-discovery fixtures;
- affected TODO/changelog/version-candidate/generated/release metadata;
- 056 evidence/results.

Current next candidate slots, only when the candidate is actually formed under the repo version contract:

```text
AI_Skills repository 5.0.4 -> 5.0.5 PATCH
workflow-core         0.1 -> 0.2
web-development       0.1 -> 0.2
ai-skills-core        0.2 -> 0.3
```

Do not bump unrelated plugins.

#### GPT_Codex_AI_Bridge_Kit

Create exactly:

- branch: `reviewed/056_product_delivery_discipline`
- task-owned worktree: `GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`

Allowed task-owned changes only:

- Lite L1-L6;
- managed desired `features.default_mode_request_user_input=false`;
- supported-key vs desired-state validation;
- HUMAN_ONLY transcript blocked/recovery guidance;
- current Host/Lite source, tests and docs;
- version/changelog/README candidate metadata required by this frozen change.

Preserve the integrated 057 behavior:

- fresh-repo root AGENTS scaffold;
- existing-root raw-byte/newline preservation;
- one managed Bridge block;
- Lite fallback versioning;
- no existing-repo automatic scaffold migration;
- no Lite duplication in root.

Bridge `0.8.3` is already the canonical 057 identity. The next distinct compatible 056 candidate slot is `0.8.4`. Do not reuse `0.8.3` for a different user-consumable candidate and do not jump to a minor/major version without new authority.

### 3. Product repositories are ZERO WRITE

Do not modify, branch, commit or push:

- Bobbio;
- Lucerna;
- Mica-for-ChatGPT;
- Asteria;
- SeminarArc;
- CUHK Date;
- CARE/EAT;
- Server/VPS;
- Longleaf_Bridge;
- Scientific Visualization production.

Bobbio's old 056 locator task is already completed by 057. Bobbio may be read only as G6 canonical-design evidence.

CUHK Date now has a root AGENTS, but `NO_GENERIC_056_AGENTS_COPY` still applies. Current Questionnaire V4 product work is evidence/reference only, not 056 scope.

### 4. Frozen architecture

Keep exactly:

```text
Lite: L1-L6
workflow-core: W1-W5
Frontend Design: F-A / F-B / F-C
AI Skills Maintainer: one production-consumption diagnosis capability
Capability Gates: G1-G8
Source Discovery regression: existing capability, not G9
```

Do not add W6/W7, G9/G10, Control, watcher, daemon, ledger, second state machine/review engine, new top-level plugin or Codex fork.

### 5. HUMAN_ONLY hard contract

Before asking the user, classify the dependency:

`HUMAN_ONLY / AGENT_RESOLVABLE / UNSUPPORTED_WITH_EVIDENCE / OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE / SAFETY_OR_AUTHORITY_BLOCKER`.

Only genuine `HUMAN_ONLY` enters this contract.

Default required HUMAN_ONLY must not use native `request_user_input`. Use:

```text
preserve current Goal/resume point/prompt identity
-> one concise plain-text user question
-> stop all dependent execution immediately
```

Waiting authority:

1. use an explicit human-response deadline/hard deadline/run-lifetime already frozen by the task/workflow;
2. otherwise, if the question ends the current interactive run/turn, run-end is the handoff boundary;
3. native request-user-input auto-resolution is not transcript timeout authority;
4. External GPT Planner/Reviewer normal waiting is a different contract and remains unchanged.

No answer at the boundary must report:

```text
GOAL_BLOCKED=YES
GOAL_ACHIEVED=NO
COMPLETE=NO
READY_FOR_USER_REVIEW=NO
DEPENDENT_EXECUTION_BLOCKED=YES
```

Use an existing legal human-required/recovery machine state. Do not invent a BLOCKED enum.

A later explicit in-scope answer:

```text
reread current Goal/resume point/prompt identity
-> confirm still current
-> consume answer once
-> exact-once resume same Goal
-> complete post-action closure
-> only then reconsider acceptance/completion
```

No successor, duplicate prompt, polling, default inference, auto retry or timeout-continuation.

### 6. Acceptance / evidence contract

Do not present an acceptance/release/user-ready candidate before applicable producer-local implementation, focused regression, source/generated parity, target-surface evidence and candidate identity are closed.

Advisory/diagnostic/design/architecture review may occur earlier but cannot claim ready/complete.

Preserve:

- mock/provider evidence only proves its actual surface;
- hosted/external claims require bounded configured-target evidence;
- interaction sequences must be tested when intermediate states matter;
- breadth/locale/material-branch claims need representative coverage when those claims are frozen;
- fallback/recovery does not automatically prove primary capability;
- accepted/adjacent behavior must not silently regress.

### 7. G1-G8

Implement and collect authorized evidence for the frozen G1-G8.

G1 must include:

- reply path: question -> no dependent work -> explicit answer -> same Goal exact-once resume;
- no-reply path: faithful bounded fixture -> deadline/run-end -> Goal blocked/achieved=no -> later explicit recovery -> same Goal exact-once resume;
- AGENT_RESOLVABLE does not prompt;
- UNSUPPORTED closes truthfully;
- candidate desired Default flag is false;
- Plan-mode native blocking semantics remain valid.

Do not use grep-only evidence for G1-B.

G2-G8 remain exactly as frozen in v0.3 Plan/Goal.

### 8. Current Host boundary — no real Host install

This Kickoff does **not** authorize:

- mutation of the user's real `$CODEX_HOME`;
- real Host Policy install/update;
- real-user `ai-bridge host install`;
- the final live `W2_RESUME_056_FINAL` user smoke.

Bridge source/unit/fixture tests may exercise Host logic in isolated temporary test fixtures as part of the test suite, but must not write the real user Codex identity.

The final real-host application/fresh-session smoke, if still required after independent implementation review, is a later separately authorized integration step.

Therefore do not claim final release-critical G1 PASS or overall 056 achieved from isolated fixture evidence alone.

### 9. Validation and candidate identity

Run the smallest focused tests first, then the appropriate full repository validation once the candidate is stable.

AI_Skills must prove source/generated/Marketplace/version/changelog parity and that Frontend Design production payload actually consumes the existing Figma-handoff + motion capability.

Bridge must run focused Host/Lite tests plus its full unit suite once on the stable implementation candidate, while preserving the 057 scaffold/raw-byte/versioning regressions.

Before handoff, freeze and report:

- exact AI_Skills implementation candidate commit;
- generated workflow/web/maintainer hashes;
- exact Bridge implementation candidate commit;
- Bridge next candidate version identity (`0.8.4` when formed);
- exact read-only reference refs used;
- which G1-G8 evidence passed at the authorized non-host surface;
- real-host integration evidence still pending because this Kickoff does not authorize it.

### 10. Git / side-effect boundary

Allowed:

- ordinary fetch/read-only inspection;
- creation/use of the two exact authorized task branches/worktrees;
- task-owned stage/commit/non-force push to those exact task branches.

Forbidden:

- merge to AI_Skills or Bridge main;
- any product-repo write/commit/push;
- remote remap;
- force push/history rewrite;
- PR creation;
- branch deletion;
- tag/GitHub Release/package publish/deployment;
- real Host install/update;
- paid/external model API/Terra;
- unrelated product work.

Protect unrelated dirty user work; do not stash/reset/clean/overwrite it merely to continue 056.

### 11. End state

Complete implementation/self-QA/authorized tests and non-host gate evidence, commit/push both exact task branches, freeze the implementation tuple, and stop at:

`NEXT_HANDOFF = INDEPENDENT_IMPLEMENTATION_REVIEW`

Report any still-unverified real-host/release boundary explicitly.

Do not announce overall 056 achieved.
