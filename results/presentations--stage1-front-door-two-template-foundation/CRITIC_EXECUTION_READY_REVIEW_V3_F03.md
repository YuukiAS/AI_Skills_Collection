# Presentations Stage 1 v1.1 — Narrow F03 Execution-Ready Critic Re-Review

Date: **2026-09-29**  
Review stage: **STAGE1_EXECUTION_READY_F03_REVIEW**  
Target repo: **YuukiAS/AI_Skills_Collection**  
Target plugin/domain: **presentations**  
Task key: **presentations--stage1-front-door-two-template-foundation**

## Reviewed package

Execution package:

`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md`

Package commit:

`049847f4638bb339229c748d3b8f97bd41fae72d`

Prior execution-ready review:

`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V2.md`
@ `9a656214b61206221d8d93c19f67488e43d842c5`

Dependency record:

`results/presentations--stage1-front-door-two-template-foundation/F03_BRIDGE_DEPENDENCY.md`

Current AI_Skills main reviewed:

`a7028195f3e97d32d51c32ef8c87f658f92048e5`

Bridge formal release closure:

`YuukiAS/GPT_Codex_AI_Bridge_Kit`
`results/reviewed-handoff--first-remote-publication/FORMAL_RELEASE_CLOSURE.md`
@ `5a640ec02a20106c778a35ba94eb2164d2b91537`

Bridge formal release target:

`9dad0ba4bfa54e251f345091c5151ae991251ec9`
version `0.9.3`

## User-readable closure

The two original Stage 1 execution blockers remain closed:

- `PRES-S1-ER-F01`: bootstrap stops at `PLAN_REQUESTED / RUN_GPT_PLANNER`; the task-local V2 Plan is Planner-owned and production implementation begins only after `PLAN_FROZEN / RUN_CODEX_EXECUTOR`.
- `PRES-S1-ER-F02`: the exact bootstrap includes `--ci-required` and the implementation candidate must use the legal CI-required Reviewed Handoff chronology.

The only remaining blocker from the prior review was `PRES-S1-ER-F03`: Bridge lacked a bounded normal entry for first remote publication of a brand-new Reviewed task.

That dependency is now closed by Bridge 0.9.3:

- production command exists: `ai-bridge reviewed-handoff task publish-first --task-key <task_key> --expected-repo <owner/repo>`;
- it was independently pre-final reviewed after repair;
- FP-G1 through FP-G6 passed on the repaired final candidate;
- a fresh AI_Skills real consumer successfully created an absent reviewed branch through the installed command without raw `git push -u` or a second ordinary approval;
- Bridge `refs/heads/release` now points to exact candidate `9dad0ba4bfa54e251f345091c5151ae991251ec9`;
- formal distribution closure records `FORMAL_DISTRIBUTION_COMPLETE=YES`.

The current Presentations v1.1 wording already delegates first-bootstrap metadata publication to the repository's “currently authorized bounded publication route.” This is compatible with the released `task publish-first` command and does not require the Kickoff to name a different command or change authorization semantics.

Therefore no Presentations v1.2 amendment is required. No product architecture, routing, Gate, version, or scope change is introduced by closing F03.

## Stable blocker re-check

```text
PRES-S1-ER-F01=CLOSED
PRES-S1-ER-F02=CLOSED
PRES-S1-ER-F03=CLOSED
NEW_BLOCKERS=NONE
```

## F03 direct evidence

The prior F03 minimum closure required an implemented, tested, actually available bounded first-publication normal entry for brand-new Reviewed tasks that:

- derives the exact reviewed branch from task identity;
- publishes only the exact same-name branch;
- validates repo/task/worktree/base/remote/transport/lineage and first-state metadata;
- does not expose arbitrary new branch/refspec/force/tag/delete authority;
- proves remote SHA equals captured local HEAD;
- requires no second user approval after the exact task/branch/worktree Kickoff.

Bridge 0.9.3 satisfies that contract. The repaired candidate's fresh AI_Skills FP-G6 additionally proved the normal entry against a real AI_Skills Reviewed task.

No consumer-specific Git wrapper, raw push fallback, generic publisher widening, branch/worktree change, or Presentations product workaround was introduced.

## Package amendment decision

```text
PRESENTATIONS_V1_1_PACKAGE_CHANGE=NO
PRESENTATIONS_V1_2_REQUIRED=NO
PLAN_CHANGE=NO
GOAL_CHANGE=NO
KICKOFF_CHANGE=NO
```

The current v1.1 text “currently authorized bounded publication route” is intentionally generic and correctly resolves to the released Bridge normal entry at execution time.

## Verdict

```text
RESULT=PASS
REVIEW_STAGE=STAGE1_EXECUTION_READY_F03_REVIEW

REVIEWED_PACKAGE=
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_1.md

REVIEWED_PACKAGE_COMMIT=
049847f4638bb339229c748d3b8f97bd41fae72d

APPROVED_PROPOSAL_PATH=
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_1_2026-09-29.md

APPROVED_GOAL_PATH=
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_1.md

APPROVED_KICKOFF_PATH=
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_1.md

PRES-S1-ER-F01=CLOSED
PRES-S1-ER-F02=CLOSED
PRES-S1-ER-F03=CLOSED
NEW_BLOCKERS=NONE

BRIDGE_RELEASE_VERSION=0.9.3
BRIDGE_RELEASE_TARGET=9dad0ba4bfa54e251f345091c5151ae991251ec9
BRIDGE_FORMAL_DISTRIBUTION_COMPLETE=YES

READY_FOR_CODEX=YES
USER_KICKOFF_REQUIRED=YES
PRESENTATIONS_PRODUCTION_IMPLEMENTATION_AUTHORIZED_BY_CRITIC=NO
MAIN_INTEGRATION_AUTHORIZED=NO
PRESENTATIONS_RELEASE_AUTHORIZED=NO

NEXT_HANDOFF=CODEX
```

This PASS closes only the Stage 1 execution-readiness package. It does not claim Stage 1 implementation PASS, main integration, plugin release, maturity promotion, or completion of the full Presentations V1.1 redesign.

## Maintenance Board pending mutation

Project mutation is not claimed from this Critic surface.

```text
Project = AI Skills Maintenance
Area = presentations
Issues = #29-#48
Status = DOING
Current execution anchor =
  results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V3_F03.md
Next action =
  user sends the exact approved Stage 1 v1.1 Kickoff;
  Codex starts the bounded Reviewed Handoff Stage 1 task
Resolution commit = unset
Source maturity/status = unchanged
Issues remain open
Do not mark PROMOTED/DONE or close issues
```

## Exact approved Codex Kickoff

# Presentations Stage 1 — Codex Kickoff Draft v1.1

**Status:** DRAFT FOR EXECUTION-READY CRITIC RE-REVIEW / NOT YET EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`

Do not use this Kickoff unless an independent execution-ready Critic has returned \`PASS / READY_FOR_CODEX=YES\` for the exact Stage 1 v1.1 package and has reproduced this Kickoff verbatim.

The user's later act of sending the Critic-approved text is the current-user authorization for the bounded scope below.

---

你现在只启动并执行 Presentations 已批准架构的 **Stage 1 — Front door + routing + two-template adapter foundation**，严格遵守 Reviewed Handoff 当前正常入口。

## Authority

Repository:

\`YuukiAS/AI_Skills_Collection\`

Approved architecture:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md\`
@ \`f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Architecture Critic PASS:

\`results/presentations--two-template-production-redesign/CRITIC_REVIEW_V2.md\`
@ \`ef2f1488b5e7479a4dd504f02ac2bd02b8825c07\`

Stage 1 Plan:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_1_2026-09-29.md\`

Canonical Goal:

\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_1.md\`

Prior execution-ready review that this package repairs:

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V1.md\`
@ \`c4fd2c64b3211529a61a33e5f80eb7afc2e2960a\`

完整产品范围、G1/G5、private reference、停止条件和恢复边界以 Stage 1 Plan v1.1 + Goal v1.1 为准。不要重新设计。

---

## 1. Exact task authorization

Canonical checkout expected on execution machine:

\`/home/yuukias/AI_Skills_Collection\`

Task key:

\`presentations--stage1-front-door-two-template-foundation\`

Bridge-derived branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Bridge-derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

No other task/branch/worktree is authorized.

If the canonical checkout path or repo identity differs, stop before bootstrap and report the mismatch.

Do not substitute another checkout.
Do not use raw \`git worktree add\`.
Do not second-bootstrap an existing task.

---

## 2. First bootstrap — control plane only

From the exact canonical checkout:

1. read current repo \`AGENTS.md\`;
2. read current Bridge Reviewed Handoff normal-entry rules;
3. verify the canonical worktree is safe for fetch/bootstrap;
4. run the normal approved fetch/sync preflight;
5. resolve exact post-sync \`origin/main\` OID;
6. confirm the task branch/worktree are not conflicting;
7. run:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement only approved Presentations Stage 1: unified front door/routing and two-template adapter foundation." \
  --ci-required
\`\`\`

Do not add \`--visual-review-required\` or \`--text-review-required\`.
No paid Text Review / Visual Review / Terra is authorized.

Successful first bootstrap must initialize:

\`\`\`text
CURRENT.state = PLAN_REQUESTED
CURRENT.next_action = RUN_GPT_PLANNER
CURRENT.ci_required = true
plan_revision = 0
\`\`\`

This is the expected state.

**Do not start Presentations production implementation yet.**

---

## 3. Publish first-bootstrap control metadata, then stop Executor work

After successful first bootstrap:

- work only in the exact Bridge-derived sibling worktree;
- verify \`REQUEST.md\` / \`CURRENT.json\` match this task and base;
- commit/publish only the first-bootstrap task-owned control metadata required for the external GPT Planner to read the task;
- do not add Presentations production source changes;
- do not create or modify task-local \`PLAN.md\`;
- keep:
  \`PLAN_REQUESTED / RUN_GPT_PLANNER\`;
- stop Executor/product implementation and hand ownership to GPT Planner.

This publication is control-plane handoff, not Stage 1 product implementation.

Use only the repository's currently authorized bounded publication route. If first remote publication cannot be done through the current legal route, stop and report the exact control-plane blocker. Do not raw-push, choose another branch or modify Bridge Kit.

Executor must never write/freeze its own task-local Plan.

---

## 4. Planner-owned initial transaction

The next owner is GPT Planner.

Planner must read from the exact reviewed branch/worktree:

- task \`REQUEST.md\`;
- task \`CURRENT.json\`;
- approved Presentations V1.1 architecture;
- Stage 1 Plan v1.1;
- Stage 1 Goal v1.1;
- the durable execution-ready Critic PASS for this exact v1.1 package;
- current \`automation/reviewed_handoff/templates/PLAN.md\`;
- current Planner / Reviewed Handoff contracts.

Planner writes:

\`automation/reviewed_handoff/tasks/presentations--stage1-front-door-two-template-foundation/PLAN.md\`

using:

\`AI_BRIDGE_REVIEWED_PLAN_V2\`

The task-local Plan is a faithful execution freeze of the already approved package. It is not a new architecture design.

Planner must self-check the current required Plan sections and legally transition:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
CURRENT.next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

Then publish that Planner transaction on the exact reviewed branch.

The initial freeze does not consume the later re-plan budget.

Only after the repository state is actually:

\`\`\`text
PLAN_FROZEN
RUN_CODEX_EXECUTOR
\`\`\`

may Executor begin production implementation.

If the external Planner is not immediately available, remain in the normal external-Planner waiting state. Do not convert waiting into a product blocker and do not ask the user to reauthorize the already bounded Stage 1 task.

Existing-task recovery later must use artifact-bound:

\`ai-bridge reviewed-handoff materialize-worktree --mode resume\`

Never second-bootstrap.

---

## 5. Required capabilities after PLAN_FROZEN

Use:

- \`workflow-core\`
- \`ai-skills-core\` / AI Skills Maintainer
- \`presentations\`

They do not expand the frozen scope.

---

## 6. Required private reference

Before substantive \`course-standard\` implementation, directly read the exact user-provided:

\`Chapter1.pdf\`

Expected SHA-256:

\`ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7\`

Expected pages:

\`50\`

Preferred durable locator:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

我发送这段经 Critic 批准的 Kickoff，即授权本 Stage 1 为 \`course-standard\` implementation 与 G5 review 读取这一个 exact private reference，并在 task-owned durable \`private/exports\` 范围保存必要 reference render / candidate render / review bundle。

不得打印、commit、push private reference正文或页面内容。

If unavailable/hash mismatch:

\`BLOCKED_REFERENCE_UNAVAILABLE\`

Stop substantive implementation.

Do not reconstruct from Planner prose, screenshots, OCR summaries or memory.

CUHK canonical authority remains:

\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

---

## 7. Implement only Stage 1

Only after \`PLAN_FROZEN / RUN_CODEX_EXECUTOR\`, implement:

- Presentations unified front door;
- Marketplace/plugin interface routing;
- research/business source skill boundary;
- shared routing;
- \`presentation-desktop\` consistency;
- \`local-edit\` fast path;
- business/editable route preservation;
- \`cuhk-research\` canonical adapter identity/provenance;
- \`course-standard\` canonical reconstruction adapter foundation;
- generated layer only through existing generator;
- G1;
- G5 actual consumption + visual fidelity foundation;
- targeted + broad regression required by the Plan.

Routing invariants:

\`\`\`text
research/group meeting/seminar/QE/oral/defense, no format
-> cuhk-research Beamer

Tutorial/lecture/teaching, no format
-> course-standard Beamer

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides
-> official editable adapter

existing deck / local edit
-> preserve current format/template

external locked template
-> pass-through; never third built-in template

plan-only
-> plan only; never claim a generated deck
\`\`\`

Local edit must still enter Presentations intake but immediately use the lightweight fast path. Do not run a full semantic storyboard.

---

## 8. G1 / G5 are product gates, not helper gates

### G1

Use the exact committed candidate in a fresh supported runtime with the installed candidate Presentations plugin and natural requests.

Helper/fixture/direct script/route receipt/config presence cannot alone PASS G1.

Exercise the route families frozen in Goal/Plan.

Beamer route:
- real \`.tex\`;
- real PDF compile;
- real render.

Editable route:
- real supported official Presentation/Slides surface;
- no \`python-pptx\`, reconstructed PDF or route receipt substitute.

If unavailable:

\`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`

Fail closed.

### G5

For both built-in templates separately prove:

1. canonical source actually consumed;
2. rendered visual fidelity.

These evidence streams cannot compensate for each other.

For course-standard, Reviewer must directly access:
- exact private \`Chapter1.pdf\`;
- candidate render.

For CUHK, Reviewer must verify canonical exact identity remains intact.

---

## 9. Strict out of scope

Do not implement:

- Stage 2 semantic sequence;
- Stage 3 composition;
- Stage 4 citation/language;
- Stage 5 existing-deck runtime;
- Stage 6 final generalization/release;
- universal IR/schema;
- third built-in template;
- new top-level presentation skill/plugin;
- implicit-invocation hack;
- geometry engine;
- #44–#48 promotion;
- Bridge Kit changes;
- new workflow/state machine/ledger/database;
- paid API/model review;
- production plugin install/sync/release;
- version bump;
- PR/main merge/integration.

If Stage 1 requires any of these, stop and return \`NEEDS_GPT_PLANNER\` with direct evidence.

---

## 10. Validation and evidence

After legal \`PLAN_FROZEN\`, run cheap/deterministic checks before product gates.

At minimum follow the current repo contract for:

- targeted Presentations tests;
- Marketplace generator write/validate/check/path-report;
- skills validation;
- full/risk-matched repo regression;
- Reviewed Handoff validation;
- \`git diff --check\`;
- G1 natural installed-candidate evidence;
- G5 source-consumption + real render evidence.

Candidate replay must bind to the exact committed candidate. Replay receipts prove identity/consumption only, not the whole product gate.

Future-required private artifacts must be durably copied before worktree cleanup to:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/\`

with necessary hashes/locators.

---

## 11. Mandatory CI chronology

This task was bootstrapped with:

\`--ci-required\`

Therefore after the exact implementation candidate is ready and published:

- write valid \`RESULT.md\`;
- bind the implementation candidate;
- enter:

\`\`\`text
WAITING_FOR_CI
CURRENT.ci_status = PENDING
\`\`\`

- wait for real GitHub CI;
- only after CI PASS may the current external GPT implementation review proceed through the legal Reviewed Handoff transition.

Do not claim CI PASS from local tests.
Do not change \`ci_required\` to false.
Do not use RESULT prose as a second CI truth.

---

## 12. Git / side-effect authorization

我发送这段经 Critic 批准的 Kickoff，仅授权：

- exact Reviewed first bootstrap with \`--ci-required\`;
- exact first-bootstrap control metadata publication needed for Planner;
- Planner-owned task-local V2 Plan transaction;
- exact reviewed-worktree task-owned Stage 1 source edits **after PLAN_FROZEN**;
- tests, local rendering, candidate replay;
- exact Chapter1 private reference read;
- task-owned durable private evidence writes;
- exact reviewed branch ordinary commits;
- exact reviewed branch ordinary non-force publication required for Planner/CI/Reviewer.

Not authorized:

- alternate branch/worktree;
- raw worktree fallback;
- force/destructive Git;
- PR;
- main merge/integration;
- tag/release;
- production plugin install/sync;
- version bump;
- paid model/API;
- credential/provider changes;
- Bridge Kit mutation.

---

## 13. Fail closed / recovery

Current released \`presentations 0.3\` / latest released plugin remains rollback boundary.

Fail closed on:

- \`BLOCKED_REVIEWED_FIRST_BOOTSTRAP\`
- \`BLOCKED_PLANNER_FREEZE\`
- \`BLOCKED_CI_STATE\`
- \`BLOCKED_DISCOVERY_CONSUMER\`
- \`BLOCKED_REFERENCE_UNAVAILABLE\`
- \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`
- \`BLOCKED_TEMPLATE_PROVENANCE\`
- \`BLOCKED_GENERATOR_ARCHITECTURE\`
- \`NEEDS_GPT_PLANNER\`

Do not bypass.

---

## 14. Completion boundary

Stage 1 implementation/Reviewer PASS may claim only:

> the exact Stage 1 candidate implements and validates the approved unified front door/routing and two-template adapter foundation under G1/G5 with required CI.

It does not authorize or prove:
- Stage 2;
- full Presentations V1.1 completion;
- main integration;
- release;
- version bump;
- maturity promotion;
- all TODOs solved.

Stop at the current Reviewed Handoff human/review boundary after implementation review.

