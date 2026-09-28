# Product UI Copy Cross-Plugin — Execution-Ready Critic Re-review Prompt v0.2

You remain the independent execution-ready Critic for:

`YuukiAS/AI_Skills_Collection`

Task:

`product-ui-copy--cross-plugin-production-integration`

This is a **minimal re-review** of one chronology amendment.

Do not reopen Product UI Copy Proposal v0.2 architecture.
Do not reopen Frontend Design 0.3.
Do not redesign Bridge Kit.
Do not implement production behavior.

## 1. Prior review

Prior execution package:

`v0.1 @ 3a447c5cfeb2cee11ec4a37693ffb4ee7e19ec02`

Prior durable review:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-28.md`

review commit:

`c1982a3ffddeafbc906087ff1da40e5bcfc43e46`

Prior verdict:

```text
RESULT = REVISE
READY_FOR_CODEX = NO
```

All v0.1 findings were PASS except:

`PUC-ER-01 — RELEASE-CRITICAL G1–G6 RUN BEFORE THE VERSIONED H2 FINAL CANDIDATE`

The v0.1 review already passed:

- Bridge bootstrap;
- initial Planner transaction;
- implementation scope;
- same-session multi-plugin candidate replay;
- H3 Planner revision;
- fresh holdout design;
- real-project replay;
- rendered review path;
- tracking closure;
- permissions;
- version bump **direction/class**.

Only final-candidate gate chronology remains under review.

## 2. Current review object

Execution package v0.2:

- Plan:
  `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_2_2026-09-28.md`
- Goal:
  `docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_2.md`
- Kickoff:
  `docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_2.md`

Exact reviewed package commit:

`926fc059ad5b7460fcb91074bd1d3aadb5717432`

Architecture authority remains:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md`
@ `a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67`

Architecture Critic PASS remains:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_REVIEW_V0_2_2026-09-28.md`

## 3. Required current-source read

Read latest `AI_Skills_Collection/main`:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- v0.2 Proposal;
- prior v0.1 execution Critic review;
- v0.2 Plan / Goal / Kickoff.

Then read latest `YuukiAS/GPT_Codex_AI_Bridge_Kit/main`:

- `AGENTS.md`
- current Reviewed Handoff README;
- current PLAN V2 template;
- current schema;
- current state-transition implementation only if needed to verify that the amendment did not break H3 behavior.

The Planner's current Bridge checkpoint is:

`f85622fd26fa1b8648d957e20b4f047a671e999f`

If main advanced, inspect the new current source rather than trusting that locator.

## 4. External reality check

Do one narrow current official OpenAI check for the final-packaged-plugin testing assumption.

Relevant current official guidance:

- complete installed plugin should be tested after packaging;
- activation evaluation should include direct, indirect, negative and boundary cases;
- Skill discovery depends on metadata such as name/description.

Current primary sources:

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/connect-chatgpt

Do not use this check to reopen Product UI Copy ownership.

## 5. PUC-ER-01 closure target

The old defect was:

```text
pre-version candidate:
  G1–G6 PASS

then:
  version bump + regenerate

post-version H2 candidate:
  H4 / CI / G8 PASS

=> release PASS assembled from different candidate identities
```

That violates the same-final-candidate rule because G1–G6 are explicitly marked final-candidate gates.

v0.2 must now freeze:

```text
pre-H2 G1–G6
  = DEVELOPMENT EVIDENCE ONLY

development stable
→ apply approved version bump exactly once
→ regenerate packaged plugins / Marketplace
→ freeze exact versioned H2 candidate + reviewer criteria

exact H2 candidate
→ rerun all release-critical G1–G6 directly
→ all PASS

only then
→ NEEDS_GPT_PLANNER
→ H3 exact fresh batch freeze
→ PLAN_FROZEN, plan_revision=1
→ H4 on unchanged H2 candidate
→ CI / Reviewer / G8
```

If any exact-H2 G1–G6 gate fails:

```text
repair within approved scope
→ keep same selected release versions
→ do NOT bump again
→ regenerate
→ freeze new H2 candidate
→ rerun ALL release-critical G1–G6
→ remain before H3 until full PASS
```

No pre-H2 gate result may be spliced into release PASS.

## 6. Exact files to check

### Execution Plan v0.2

Verify:

- Gate Matrix explicitly says pre-H2 G1–G6 is development evidence only.
- G1–G6 remain marked final-candidate as before.
- G7 H2 section explicitly requires direct H2 rerun of release-critical G1–G6.
- Phase F performs:
  version bump → regenerate → H2 freeze → exact-H2 G1–G6 rerun.
- Phase G cannot start until exact-H2 G1–G6 PASS.
- failed H2 gate repair keeps the selected version and creates a new H2 commit without another bump.
- Reviewer later reads exact-H2 G1–G6 evidence plus H4/G8.

### Canonical Goal v0.2

Verify:

- same chronology;
- pre-H2 evidence cannot count for release;
- H3 only follows exact-H2 G1–G6 PASS;
- H2 repair keeps the same selected release version;
- workflow chronology lists exact-H2 rerun before H3.

### Kickoff v0.2

Verify:

- Section 11 applies version bump/regenerate then freezes exact versioned H2.
- Section 12 mandates exact-H2 G1–G6 rerun.
- H3 is gated behind that PASS.
- failure before H3 repairs same version, re-freezes H2, reruns all G1–G6.
- H4 and CI remain bound to the unchanged successful H2 candidate.

## 7. Amendment regression check

Check only direct regressions introduced by this chronology amendment.

Do not reopen already-passed v0.1 findings unless v0.2 now directly contradicts them.

At minimum ensure unchanged:

```text
task_key =
product-ui-copy--cross-plugin-production-integration

branch =
reviewed/product-ui-copy--cross-plugin-production-integration

worktree =
/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration
```

And unchanged:

- first bootstrap through current Bridge;
- initial PLAN_REQUESTED → Planner V2 PLAN → PLAN_FROZEN;
- initial `plan_revision=0`;
- H3 uses the one later revision;
- same-session two-candidate replay;
- no paid review;
- no consumer-repo writes;
- SeminarArc positive/negative;
- tracking scope;
- no main merge/release ref;
- no maturity promotion.

## 8. Version direction

Do not reopen the approved release class unless current source now directly contradicts it.

Under unchanged baseline:

```text
Repository: 5.3.1 -> 5.4.0
web-development: 0.3 -> 0.4
writing-style: 0.3 -> 0.4
all other central plugins: NO_BUMP
maturity: unchanged / unclassified
```

The amendment changes only **when final gates run**, not the version direction.

## 9. Durable re-review artifact

Write your actual full review to:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`

on `AI_Skills_Collection/main`.

This is the only repo mutation allowed in this Critic task.

The artifact must bind:

```text
REVIEWED_OBJECT = Product UI Copy Cross-Plugin execution package
REVIEWED_PACKAGE_VERSION = v0.2
REVIEWED_PACKAGE_COMMIT = 926fc059ad5b7460fcb91074bd1d3aadb5717432

RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO

APPROVED_PLAN =
docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_2_2026-09-28.md

APPROVED_GOAL =
docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_2.md

APPROVED_KICKOFF =
docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_2.md

APPROVED_TASK_KEY =
product-ui-copy--cross-plugin-production-integration

APPROVED_BRANCH =
reviewed/product-ui-copy--cross-plugin-production-integration

APPROVED_WORKTREE =
/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration

ARCHITECTURE_AUTHORITY =
docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md
@ a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67
```

If REVISE, set `READY_FOR_CODEX=NO` and do not fabricate approval.

## 10. Blocker standard

First explicitly report:

```text
PUC-ER-01 = CLOSED | OPEN
```

REVISE only if:

- PUC-ER-01 is still not closed; or
- v0.2 directly introduces a new execution blocker.

Do not create a new blocker for:

- wording preference;
- wanting more gates;
- wanting another replay project;
- wanting paid review;
- wanting a second fresh batch;
- wanting to redesign Bridge;
- reopening Product UI Copy ownership;
- reopening Frontend Design 0.3.

Any new blocker must state:

```text
FINDING_ID
Requirement
Direct evidence
Causal risk
Minimal closure condition
Owner
```

Do not move the goalposts.

## 11. Required final verdict

Return:

```text
RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO

REVIEWED_PACKAGE_VERSION = v0.2
REVIEWED_PACKAGE_COMMIT = 926fc059ad5b7460fcb91074bd1d3aadb5717432

PUC-ER-01 = CLOSED | OPEN

BRIDGE_BOOTSTRAP = PASS
INITIAL_PLANNER_TRANSACTION = PASS
IMPLEMENTATION_SCOPE = PASS
MULTI_PLUGIN_CANDIDATE_REPLAY = PASS
GATE_MATRIX = PASS | REVISE
H3_PLANNER_REVISION = PASS
FRESH_HOLDOUT = PASS
REAL_PROJECT_REPLAY = PASS
RENDERED_REVIEW_PATH = PASS
VERSION_CLOSURE = PASS | REVISE
TRACKING_CLOSURE = PASS
PERMISSIONS = PASS

IMPLEMENTATION_AUTHORIZED = NO
NEXT_STEP = user sends approved v0.2 Kickoff only after PASS
```

A PASS makes the v0.2 Kickoff eligible for later explicit user authorization.

It does not create the task, branch, worktree, production edits, paid review, main merge, release movement, or consumer-repo changes.
