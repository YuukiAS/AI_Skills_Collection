# 056 Final Integration / Release — Critic Prompt v0.2

你是 AI Research Stack 的长期独立 Critic thread。

继续 historical task：

`056_product_delivery_discipline`

人类可读名称：

交付工作流可靠性基线

当前 review stage：

`FINAL_INTEGRATION_AND_RELEASE_EXECUTION_READY_PACKAGE_V0_2`

这不是重新设计 056。

## 1. Review object

v0.2 exact package commit：

`16fb59741be9b56525e6caefce895244a3f8399f`

v0.2 paths：

- `docs/design/056_FINAL_INTEGRATION_RELEASE_PLAN_V0_2_2026-09-22.md`
- `docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_2.md`
- `docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md`
- `docs/design/056_FINAL_INTEGRATION_RELEASE_REVIEW_PACKAGE_V0_2_2026-09-22.md`

Previous package：

`a90b92bc4931b3f1d8cca62fa9d67ba084ee1a66`

Previous Critic handoff source：

`f997baaf55f70df6f7077e7193300b8b9173acc8`

Stable blocker under recheck：

`C056-F1-APPROVED-KICKOFF-SELF-BLOCKS`

## 2. Frozen candidate identities

AI_Skills:

- repo: `YuukiAS/AI_Skills_Collection`
- reviewed branch: `reviewed/056_product_delivery_discipline`
- reviewed HEAD: `b6f675869449df8daa86a6abcf527fbb72c66e64`
- production candidate: `33c30bbe0dd528031a23d379905cd00d6b65bc1f`
- target release:
  - repository 5.0.7
  - workflow-core 0.3
  - web-development 0.2
  - ai-skills-core 0.4

Bridge:

- repo: `YuukiAS/GPT_Codex_AI_Bridge_Kit`
- reviewed branch: `reviewed/056_product_delivery_discipline`
- candidate: `96a8ea1b58ebe6f9b7c5c46c43995666251911fe`
- target release: 0.8.5

## 3. Must read

Actual latest AI_Skills main:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

Then read the four v0.2 package files at exact commit
`16fb59741be9b56525e6caefce895244a3f8399f`.

Only if necessary to compare the blocker, read the corresponding v0.1 files at
`a90b92bc4931b3f1d8cca62fa9d67ba084ee1a66`.

## 4. Planner disposition

Planner response to:

`C056-F1-APPROVED-KICKOFF-SELF-BLOCKS`

is:

`ACCEPT`

The Planner agrees v0.1 had a real execution-package defect.

v0.1 exact Kickoff contained:

`Status: DRAFT_NOT_AUTHORIZED`

and the Goal carried the same marker.

That created a direct contradiction with the intended post-Critic user workflow:
the user would send the approved Kickoff as current-user authorization, while the
same execution object still told the Executor it was not authorized.

This already reproduced in the prior Real Host integration round, where Codex
stopped after read-only preflight and searched for an additional repo-local
Critic PASS artifact even though the user had already sent the approved Kickoff.

## 5. v0.2 changes — only authorization presentation

The v0.2 package does not alter:

- 056 architecture
- G1-G8
- Source Discovery
- candidate identities
- AI merge strategy
- Bridge fast-forward strategy
- candidate-equivalence rule
- focused parity checks
- release versions
- repo-local formal-release semantics
- push order
- partial integration recovery
- normal Bridge upgrade
- permanent Host target/scope
- branch cleanup
- forbidden boundaries

The only change is the consumer-facing execution authorization contract.

### Goal

Now:

`Status: READY_FOR_USER_AUTHORIZATION`

The Goal explicitly says:
- it records the frozen completion contract;
- the Goal itself is not execution authorization;
- after Critic PASS, the user may send the exact v0.2 Kickoff;
- once that Kickoff is received as the current user message, it is the bounded authorization;
- no separate repo-local Critic PASS artifact is required;
- historical planning/review metadata does not become a second authorization gate;
- only genuinely new target/scope/destructive/provider/account/credential/cost effects require fresh authorization.

### Kickoff

Now:

`Status: READY_FOR_USER_AUTHORIZATION`

The canonical Kickoff contains no `DRAFT_NOT_AUTHORIZED` marker.

Its authorization header states, directly in the user-sent body:

- Critic PASS approves the execution package but does not execute it;
- the user sends the exact Kickoff only after PASS;
- if this exact Kickoff is present as the current user message, that message itself is the current-user-visible bounded authorization for every explicitly listed effect;
- Executor must not require an additional repo-local Critic PASS artifact;
- Executor must not stop merely because Plan/Goal/Review/historical repo metadata still reflects planning/review state;
- only genuinely new target/scope/destructive/provider/account/credential purpose/cost reopens authorization.

No PASS receipt schema, authorization DB, state machine, ledger, watcher or new Gate was added.

## 6. Priority recheck

First answer:

`C056-F1-APPROVED-KICKOFF-SELF-BLOCKS = CLOSED | OPEN`

To close it, verify directly in the v0.2 canonical Goal/Kickoff that:

1. neither file contains `DRAFT_NOT_AUTHORIZED`;
2. the exact Kickoff is independently executable after the user sends it;
3. current user message is explicitly the authorization surface;
4. no repo-local Critic PASS artifact is required;
5. planning/review metadata cannot override the current exact Kickoff;
6. same frozen effect does not cause repeat authorization;
7. genuinely new effects still require fresh authorization.

Do not rely on an explanation outside the Kickoff to rescue it.

The exact contents of:

`docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md`

are the user-facing object that must work standalone after PASS.

## 7. Amendment-impact check only

After checking F1, inspect whether the authorization wording accidentally broadened the already accepted v0.1 effects.

It must NOT newly authorize:

- arbitrary branch creation/deletion;
- arbitrary main mutation;
- force push;
- remote remap;
- history rewrite;
- arbitrary CODEX_HOME;
- other provider/account/credential purpose;
- paid API/Terra;
- product repo writes;
- Git tag/GitHub Release/package publish/deploy;
- production repair;
- new Gate/successor/Persistent Run work.

If the bounded effects remain identical to v0.1, do not reopen the already accepted integration/release design.

## 8. Already accepted — do not reopen without new direct evidence

Critic R1 already accepted:

- AI merge-commit strategy;
- Bridge fast-forward strategy;
- exact drift/conflict audit;
- candidate byte-equivalence Gate reuse;
- focused parity checks;
- no full-suite rerun;
- no repeated Human Gate or Plan smoke;
- no Terra/paid review;
- repository-local release without inventing Git tag/GitHub Release/package publish;
- push ordering and partial-integration recovery;
- normal Bridge 0.8.5 upgrade;
- permanent exact CODEX_HOME Host install;
- successful permanent Host state is not restored;
- exact reviewed branches are deleted only at the end;
- existing frozen candidate/version/authorization boundaries.

Do not move the endpoint by restating these as new blockers.

## 9. Output

If REVISE:

- prioritize `C056-F1-APPROVED-KICKOFF-SELF-BLOCKS`;
- only add a new blocker if v0.2 itself creates a new direct integration/release authorization risk;
- for each blocker give:
  - STABLE_ID
  - REQUIREMENT
  - DIRECT_EVIDENCE
  - CAUSAL_RISK
  - MINIMUM_CLOSURE
  - OWNER
- automatically append a complete `COPY TO PLANNER` prompt with:
  - v0.2 package commit
  - exact blocker IDs
  - exact package paths
  - candidate identities
  - limited revision scope.

If PASS:

Because this major round previously had formal REVISEs, first give a concise
human-readable closure explanation.

At minimum explain:
- why C056-F1 is now closed;
- why the exact v0.2 Kickoff no longer self-blocks;
- that the current user message, not a hidden repo artifact, is the bounded authorization surface;
- that integration/release/Host scope itself did not change;
- which effects remain forbidden.

Then output:

```text
C056-F1-APPROVED-KICKOFF-SELF-BLOCKS=CLOSED
APPROVED_PACKAGE_COMMIT=16fb59741be9b56525e6caefce895244a3f8399f
APPROVED_PLAN_PATH=docs/design/056_FINAL_INTEGRATION_RELEASE_PLAN_V0_2_2026-09-22.md
APPROVED_GOAL_PATH=docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_2.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md
APPROVED_REVIEW_PACKAGE_PATH=docs/design/056_FINAL_INTEGRATION_RELEASE_REVIEW_PACKAGE_V0_2_2026-09-22.md
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

Finally reproduce the exact v0.2 Kickoff verbatim from commit
`16fb59741be9b56525e6caefce895244a3f8399f`.

Do not rewrite another Kickoff after PASS.
