# Product UI Copy Cross-Plugin — Execution-Ready Critic Prompt v0.1

You are the independent execution-ready Critic for:

`YuukiAS/AI_Skills_Collection`

Task:

`product-ui-copy--cross-plugin-production-integration`

This is **not** a new architecture review.

Approved architecture:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md`

Architecture commit:

`a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67`

Architecture Critic PASS:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_REVIEW_V0_2_2026-09-28.md`

Execution package v0.1:

- Plan:
  `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_1_2026-09-28.md`
- Goal:
  `docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_1.md`
- Kickoff:
  `docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_1.md`

Exact reviewed package commit:

`3a447c5cfeb2cee11ec4a37693ffb4ee7e19ec02`

Durable execution-ready review artifact you own:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-28.md`

Do not implement production behavior.

Except for writing your actual durable review artifact, keep this review read-only.

## 1. Mandatory current-source reads

Read latest `AI_Skills_Collection/main`:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- Proposal v0.2
- architecture Critic PASS v0.2
- Execution Plan v0.1
- Goal v0.1
- Kickoff v0.1

Then read latest `YuukiAS/GPT_Codex_AI_Bridge_Kit/main`:

- `AGENTS.md`
- `templates/reviewed_handoff/README.md`
- `templates/reviewed_handoff/templates/PLAN.md`
- `templates/reviewed_handoff/schema.json`
- current first-bootstrap / resume / `PLAN_REQUESTED` / `PLAN_FROZEN` / `NEEDS_GPT_PLANNER` implementation as needed.

Do not rely on old Bridge behavior.

## 2. Minimal external reality check

Independently verify current OpenAI Skills/plugin guidance relevant to:

- Skill discovery by `name` / `description`;
- focused Skill boundaries;
- direct/indirect/negative/boundary activation tests;
- complete installed-plugin testing.

Use official OpenAI developer sources.

The current Planner checked:

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/connect-chatgpt

This check is to validate execution mechanics, not reopen architecture.

## 3. Package parity

Plan / Goal / Kickoff must agree on:

```text
task_key =
  product-ui-copy--cross-plugin-production-integration

branch =
  reviewed/product-ui-copy--cross-plugin-production-integration

expected canonical checkout =
  /home/yuukias/AI_Skills_Collection

expected sibling worktree =
  /home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration
```

They must also agree on:

- Proposal authority;
- G1–G8;
- H0→H4;
- no paid review authorization;
- no consumer-repo writes;
- versions;
- no main merge/release ref;
- no maturity promotion;
- durable execution-ready review path.

Only semantic mismatch is a blocker.

## 4. Bridge first-bootstrap and worktree review

The package assumes the execution machine's canonical checkout is:

`/home/yuukias/AI_Skills_Collection`

and therefore current Bridge first bootstrap should derive:

`/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration`

Review whether this is safe.

The package explicitly requires execution-time verification of that canonical checkout before bootstrap and says a mismatch must stop before branch/worktree creation.

Check:

- no caller-chosen worktree arg is invented;
- bootstrap command matches current Bridge CLI;
- exact task key derives exact `reviewed/<task_key>`;
- new task starts `PLAN_REQUESTED / RUN_GPT_PLANNER`;
- Executor cannot begin before task-local V2 Plan freeze;
- second bootstrap/raw worktree add are forbidden;
- future recovery uses artifact-bound resume;
- no Bridge Kit modification is needed.

If the absolute-path assumption is not sufficiently execution-ready despite the fail-closed preflight, state the minimum correction rather than redesigning the workflow.

## 5. Initial Planner transaction

The package requires:

```text
first bootstrap
→ PLAN_REQUESTED / RUN_GPT_PLANNER
→ external Planner reads approved package + durable execution-ready PASS
→ writes task-local AI_BRIDGE_REVIEWED_PLAN_V2
→ self-checks current template
→ PLAN_REQUESTED -> PLAN_FROZEN
→ plan_revision remains 0
→ RUN_CODEX_EXECUTOR
```

Verify this exactly matches current Bridge.

Executor must not self-freeze Plan.

## 6. Implementation scope review

Check that the allowed source is neither too broad nor too narrow.

### Clear Writing

Expected bounded changes:

- new `skills/writing/core/product-ui-copy/**`;
- `writing-fidelity` narrow semantic-fidelity handoff;
- `chinese-prose` frontmatter narrowing + minimal route note;
- Clear Writing plugin metadata/package;
- direct routing tests.

### Frontend Design

Expected bounded changes:

- `frontend-visual-systems`;
- `product-ux-planning`;
- `responsive-accessibility-review`;
- surface-agnostic trigger/routing tests;
- Frontend plugin metadata.

The coordinator-first topology itself must not be reopened.

### Profiles

Only `codex-webdev` / `frontend-research-product` if actually required.

### Generated layer

Generator-owned only.

Review whether any required approved behavior is missing from the allowed surface.

## 7. Candidate replay helper decision

Current `scripts/candidate_plugin_replay.py` is proven in Frontend Design 0.3 but supports one candidate plugin per run.

The package says a repository-level cross-plugin workflow requires one same-session proof that both:

- `web-development@ai-skills-candidate`
- `writing-style@ai-skills-candidate`

were actually consumed.

Preferred path:

- reuse the existing helper;
- minimally extend it to accept/stage/install multiple candidate plugins from the same commit if no equivalent supported route already exists;
- prove consumption of both paths;
- clean up all candidate identities;
- prove production installs unchanged;
- preserve single-plugin behavior.

Review:

1. Is same-session two-plugin consumption actually necessary for the release claim?
2. Is a minimal extension to the existing helper the smallest realistic route?
3. Does the Plan preserve backward compatibility and avoid creating a second replay framework?
4. Is any additional permission or installation risk missing?

Do not require a new replay service if the existing helper can be extended safely.

## 8. Gate Matrix review

Review G1–G8 against the current Capability Gate policy.

### G1
Discovery / activation / packaging.

Must prove actual selected Skill/plugin identity, not only good prose.

### G2
Ownership / handoff / protected meaning.

Must prove semantic safety and escalation.

### G3
Naturalness / locale / linguistic page rhythm.

Must include qualitative review and KEEP behavior.

### G4
Rendered acceptance.

Must inspect actual rendered artifacts and remain honest about browser fixture vs native claims.

### G5
Should-not-change.

Must protect Clear Writing long-form/scientific routes, Frontend 0.3, generator/parity and single-plugin candidate replay.

### G6
Same-session cross-plugin normal entry + Lucerna/Mica/SeminarArc compatibility.

Must prove both candidate plugins consumed and preserve SeminarArc platform authority.

### G7
Fresh H0→H4.

Must not leak exact final prompts before candidate/rubric freeze.

### G8
Release/version/CI/README/review closure.

Must use the same final candidate.

Check for duplicated gates, proxy PASS, missing normal-entry evidence, or an unrealistically heavy matrix.

## 9. Fresh-holdout / Bridge revision design

This is the most important execution-specific design question.

The package intentionally uses the single Bridge plan revision as the H3 freshness boundary:

```text
H0:
  freeze coverage/rubric only

H1:
  Executor development on known evidence

H2:
  version closure + exact final candidate + reviewer criteria freeze

Executor:
  EXECUTING -> NEEDS_GPT_PLANNER

H3 external Planner:
  author exact repo-safe holdout batch only after H2
  bind exact candidate/rubric/holdout locator
  make no production change
  revise task-local PLAN only for holdout identity
  NEEDS_GPT_PLANNER -> PLAN_FROZEN
  plan_revision 0 -> 1

H4 Executor:
  run complete batch once
```

Review against current Bridge:

- `EXECUTING -> NEEDS_GPT_PLANNER` is legal;
- `NEEDS_GPT_PLANNER -> PLAN_FROZEN` consumes exactly one plan revision;
- no second automatic revision remains;
- this does not create a new role/state machine;
- exact holdout is unavailable to Executor before H2;
- H4 failure cannot trigger automatic fresh-batch chasing.

If this misuse of `NEEDS_GPT_PLANNER` would conflict with current Bridge semantics, return REVISE with the smallest existing-role alternative. Do not propose a new workflow.

## 10. H0 batch-size review

The Plan recommends a bounded final fresh batch of 8 scenarios.

The number is not meant as a mechanical quality metric. It is proposed because the final batch needs to cover:

- zh-Hans;
- zh-Hant-HK;
- KEEP;
- wording;
- page rhythm;
- content-architecture escalation;
- product-semantic escalation;
- legal/trust/safety escalation.

Scenarios may cover multiple dimensions.

Review whether 8 is risk-proportionate and not benchmark bloat.

If a different small range is materially better, state why. Do not demand more samples merely for “confidence”.

## 11. Real-project replay and privacy/authority

The Kickoff draft authorizes a bounded read-only compatibility replay using the minimum frozen source needed from:

- Lucerna;
- Mica for ChatGPT;
- SeminarArc.

Check whether this authorization is sufficiently bounded by:

- purpose;
- repos;
- read-only status;
- source minimization;
- no unrelated private data;
- no consumer writes;
- no external redistribution.

SeminarArc positive replay must not name expected routing.

SeminarArc negative must remain non-UI.

None of these replays count toward maturity.

## 12. Rendered acceptance without paid Visual Review

The package deliberately does **not** set Bridge:

- `visual_review_required=true`;
- `text_review_required=true`;

because the user has not authorized paid Text/Visual Review/Terra in this execution package.

Instead it requires repo-safe rendered screenshots and independent Reviewer access.

Review whether this satisfies the required qualitative evidence **if and only if** the Scheduled GPT Reviewer can actually access the images.

The package already fails closed if the Reviewer surface cannot inspect them.

Do not silently authorize paid review.

If current repository/Reviewer reality makes visual inspection impossible without the Bridge Visual Review extension, return a blocker that says so and identify the minimum additional authorization needed.

## 13. Version review

Frozen planned release under current baseline:

```text
Repository bump decision: MINOR
5.3.1 -> 5.4.0

Affected plugins:
- web-development: 0.3 -> 0.4
- writing-style: 0.3 -> 0.4
- all others: NO_BUMP

Maturity:
- unchanged / unclassified
```

Architecture Critic already passed this direction.

Only reopen it if current source changed or the execution package no longer creates the approved repository-level cross-plugin workflow.

Check chronology:

- no bump at bootstrap;
- once only after development gates stabilize;
- H2 final candidate includes release metadata;
- no second bump after repair;
- all final gates use same production candidate.

## 14. Maintenance tracking review

The package treats wrong source tracking locators #73 and #20 as closure defects.

Kickoff authorizes exactly two replacement tracking Issues plus related source/Project updates, subject to the repository Clear Writing rule.

Check:

- Issue #17 preserved;
- Issue #13 dependency-only;
- unrelated #73/#20 not mutated as if they belonged here;
- reader-facing tracking copy must use installed Clear Writing;
- Project mutation unavailable → exact pending mutation, no false sync;
- central release may end in ADAPTING while consumer hard bindings remain.

Do not require consumer repo changes in this task.

## 15. Permissions review

Kickoff after PASS would authorize:

- exact reviewed branch/worktree bootstrap;
- bounded AI_Skills production edits;
- generated updates;
- CI;
- candidate replays;
- minimum read-only source transmission for Lucerna/Mica/SeminarArc compatibility;
- exactly two Product UI Copy tracking Issue creations/rebindings.

It would not authorize:

- consumer writes;
- paid review;
- Bridge changes;
- main merge;
- release ref;
- public deploy;
- destructive Git;
- successor tasks.

Check this is sufficient and not overbroad.

## 16. Durable execution-ready review requirement

Write your full actual review to:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-28.md`

on `AI_Skills_Collection/main`.

That review artifact is the only repo mutation allowed in this Critic task.

It must record:

```text
REVIEWED_OBJECT = Product UI Copy Cross-Plugin execution package
REVIEWED_PACKAGE_VERSION = v0.1
REVIEWED_PACKAGE_COMMIT = 3a447c5cfeb2cee11ec4a37693ffb4ee7e19ec02
RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO

APPROVED_PLAN = docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_1_2026-09-28.md
APPROVED_GOAL = docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_1.md
APPROVED_KICKOFF = docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_1.md

APPROVED_TASK_KEY = product-ui-copy--cross-plugin-production-integration
APPROVED_BRANCH = reviewed/product-ui-copy--cross-plugin-production-integration
APPROVED_WORKTREE = /home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration

ARCHITECTURE_AUTHORITY =
docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md @ a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67
```

If REVISE, keep the same fields but set `READY_FOR_CODEX=NO` and do not fabricate approval language.

## 17. Blocker standard

REVISE only for a direct execution risk such as:

- package contradicts current Bridge;
- exact task/worktree bootstrap is unsafe or ambiguous;
- H3 freshness transition is illegal/misowned;
- two-plugin candidate replay cannot actually prove the repository-level claim;
- rendered review evidence cannot reach the independent Reviewer;
- gate matrix can PASS through proxies;
- holdout is visible during tuning;
- permissions are insufficient or overbroad;
- version/closure chronology contradicts policy;
- Plan/Goal/Kickoff materially disagree.

Do not REVISE for:

- wording preferences;
- desire for more gates/samples;
- wanting JSON instead of lightweight handoff;
- wanting another consumer project;
- reopening already-passed Product UI Copy ownership;
- reopening Frontend Design 0.3;
- wanting a new workflow/service/database.

Each blocker must state:

```text
FINDING_ID
Requirement
Direct evidence
Causal risk
Minimal closure condition
Owner
```

## 18. Required final verdict

Return:

```text
RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO

REVIEWED_PACKAGE_VERSION = v0.1
REVIEWED_PACKAGE_COMMIT = 3a447c5cfeb2cee11ec4a37693ffb4ee7e19ec02

BRIDGE_BOOTSTRAP = PASS | REVISE
INITIAL_PLANNER_TRANSACTION = PASS | REVISE
IMPLEMENTATION_SCOPE = PASS | REVISE
MULTI_PLUGIN_CANDIDATE_REPLAY = PASS | REVISE
GATE_MATRIX = PASS | REVISE
H3_PLANNER_REVISION = PASS | REVISE
FRESH_HOLDOUT = PASS | REVISE
REAL_PROJECT_REPLAY = PASS | REVISE
RENDERED_REVIEW_PATH = PASS | REVISE
VERSION_CLOSURE = PASS | REVISE
TRACKING_CLOSURE = PASS | REVISE
PERMISSIONS = PASS | REVISE

IMPLEMENTATION_AUTHORIZED = NO
NEXT_STEP = user sends approved Kickoff only after PASS
```

A PASS only makes the v0.1 Kickoff eligible for the user's later explicit authorization.

It does not:

- create the branch/worktree;
- start Executor;
- modify production source;
- run paid review;
- merge main;
- move release;
- mutate consumer repos.
