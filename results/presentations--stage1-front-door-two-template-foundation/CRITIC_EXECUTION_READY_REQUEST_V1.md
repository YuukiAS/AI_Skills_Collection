# Execution-Ready Critic Request — Presentations Stage 1 v1.0

你是 AI Research Stack 的独立 Critic thread。本轮不是重新审 V1.1 architecture，而是审查 **Stage 1 execution package 是否已经可以交给 Codex**。

只做 execution-ready review。
不要实现代码。
不要创建 Reviewed Handoff task/branch/worktree。
不要运行付费 review。
不要修改 production plugin。
不要发布。

## Active Review Context

\`\`\`text
target_repo = YuukiAS/AI_Skills_Collection
target_plugin_or_domain = presentations
design_topic_or_task_key = presentations--stage1-front-door-two-template-foundation
review_stage = stage1_execution_ready_review
source_branch_or_ref = main

approved_architecture =
docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md
@ f71e97c06938ab2ce175ccf3b4ac19da9309fda1

architecture_critic_pass =
results/presentations--two-template-production-redesign/CRITIC_REVIEW_V2.md
@ ef2f1488b5e7479a4dd504f02ac2bd02b8825c07

stage1_package_manifest =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_0.md
@ ccc6a1153d6ef3b41d1bc118e0dac454b11151d9

stage1_plan =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_0_2026-09-29.md
first_commit = 5faa14e3ff618a85e8842a07f9d3f3956979b8bc

stage1_goal =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_0.md
first_commit = fce5d84bbdc917b226a2c9f5dac38cf593e44826

stage1_kickoff_draft =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_0.md
first_commit = e7d86cfc3baf32b68524c8beca81f596a274b0e9

execution_task = NOT_CREATED
execution_branch = NOT_CREATED
execution_worktree = NOT_CREATED
paid_review = NOT_AUTHORIZED
production_release = NOT_AUTHORIZED
\`\`\`

The package snapshot for approval is the manifest commit:
\`ccc6a1153d6ef3b41d1bc118e0dac454b11151d9\`.

Later commits that only add this Critic request do not modify the three execution-package objects.

## Required source reads

Read latest AI_Skills \`main\` and at minimum:

- \`AGENTS.md\`
- \`docs/workflows/PLANNER_ROLE_CONTRACT.md\`
- \`docs/workflows/CRITIC_ROLE_CONTRACT.md\`
- \`docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md\`
- \`docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md\`
- \`docs/workflows/CANDIDATE_PLUGIN_REPLAY.md\`
- \`docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md\`
- \`docs/plugin-todos/presentations.md\`
- \`scripts/codex_marketplace_config.json\` Presentations entry
- \`profiles/presentation-desktop.json\`
- research/business source skills
- shared presentation routing
- relevant current presentation tests
- approved V1.1 architecture + Critic PASS
- Stage 1 package manifest
- **all three Stage 1 package objects in full**

Because the Kickoff freezes Reviewed Handoff branch/worktree/bootstrap semantics, also read latest \`YuukiAS/GPT_Codex_AI_Bridge_Kit\`:
- \`AGENTS.md\`
- current Reviewed Handoff normal-entry docs/source sufficient to verify \`task bootstrap\` semantics.

Do not use old Bridge syntax from historical design docs if current source/README differs.

## Review the package as one object

Execution-ready PASS is legal only if the same version of all three is acceptable:

1. Proposal / Plan
2. Canonical Goal
3. Kickoff Draft

If any one requires a substantive change, return REVISE. Do not PASS the Plan and then invent a different Kickoff yourself.

---

## A. Stage 1 scope fidelity

Verify the package implements only:

- unified Presentations front door;
- Marketplace/plugin interface routing;
- research/business source skill boundary;
- shared routing;
- presentation-desktop consistency;
- local-edit fast path;
- business/editable route preservation;
- CUHK canonical adapter identity/provenance;
- course-standard reconstruction adapter foundation;
- generated layer via existing generator only;
- G1;
- G5 actual consumption + visual fidelity foundation.

Verify it does **not** enter:
- Stage 2 semantic sequence;
- Stage 3 composition;
- Stage 4 citation/language;
- Stage 5 existing-deck runtime;
- Stage 6 final generalization/release;
- universal IR/schema;
- third template;
- new top-level presentation skill/plugin;
- implicit-invocation workaround;
- new geometry engine;
- #44–#48 promotion;
- Bridge Kit changes;
- new workflow/state machine;
- paid review;
- production release/install;
- main integration.

A scope boundary that cannot be implemented without one of these exclusions is a real blocker and must fail closed.

---

## B. Reviewed Handoff / authorization review

Independently verify the current Bridge normal entry.

The package expects:

\`\`\`text
canonical checkout:
/home/yuukias/AI_Skills_Collection

task_key:
presentations--stage1-front-door-two-template-foundation

branch:
reviewed/presentations--stage1-front-door-two-template-foundation

worktree:
/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation

base:
post-sync origin/main OID
\`\`\`

Kickoff uses current repo-local:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <post-sync origin/main OID> \
  --objective "Implement only approved Presentations Stage 1: unified front door/routing and two-template adapter foundation."
\`\`\`

Check against latest Bridge source:
- repo-local cwd semantics;
- branch/worktree derivation;
- no caller \`--branch\`;
- no raw worktree fallback;
- expected-base-commit semantics;
- task bootstrap authorization behavior.

Check the Kickoff authorization envelope:
- user sending the **approved** Kickoff authorizes only exact task/branch/worktree, task edits/tests/renders/candidate replay, exact private reference scope, durable private evidence and ordinary non-force reviewed-branch publication;
- no main merge, release, paid call, production install, force/destructive Git or Bridge mutation is smuggled in.

If execution placement/syntax is stale, REVISE the package; do not substitute an unreviewed Kickoff.

---

## C. Normal-entry / routing review

The package freezes:

\`\`\`text
natural request
-> installed Presentations plugin discovery/intake
-> mode + deliverable + template decision
-> shared core OR local-edit fast path
-> official Presentation/Slides OR Beamer adapter
-> artifact/render QA
\`\`\`

Verify the package gives a feasible causal path through real current source/consumer layers:
- Marketplace config/plugin interface;
- research/business source skills;
- shared routing;
- presentation-desktop profile;
- generated plugin payload.

The following must remain invariant:

- research/group meeting/seminar/QE/oral/defense, no format -> \`cuhk-research\` Beamer;
- Tutorial/lecture/teaching, no format -> \`course-standard\` Beamer;
- business/executive/product/strategy/client, no format -> editable PPTX/Slides;
- explicit PPTX/Slides -> official editable adapter;
- existing deck/local edit -> preserve current format/template;
- external locked template -> pass-through, not built-in registry;
- plan-only -> no fake artifact completion.

Check local-edit:
- it must still enter Presentations intake;
- it must skip full planning;
- it must preserve current template/format;
- Stage 1 may route/escalate but may not implement Stage 5 revision runtime.

If current real plugin discovery cannot support this using approved surfaces, confirm the package correctly stops with \`BLOCKED_DISCOVERY_CONSUMER\` rather than inventing a new top-level skill/implicit-invocation/control plane.

---

## D. G1 review

G1 cannot PASS on:
- helper;
- fixture;
- route receipt;
- direct script;
- config/file presence.

The package requires an exact committed candidate loaded into a fresh supported runtime and natural user prompts.

Review whether G1 evidence is strong enough for each distinct route branch:
- research no-format;
- teaching no-format;
- business no-format;
- explicit editable;
- existing-deck revision routing;
- local edit;
- external locked template;
- plan-only.

Check adapter evidence:
- Beamer routes must actually produce source + PDF + render.
- Editable routes must use a real supported official Presentation/Slides surface.
- \`python-pptx\`, a reconstructed PDF or route-only receipt is explicitly prohibited.
- If the official editable surface cannot be exercised, package fails closed as \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`.

Decide whether this is a realistic execution gate rather than an impossible proxy requirement. If the current Codex execution environment cannot invoke that official surface at all, identify the exact product/tool boundary and minimum legal recovery; do not silently weaken G1.

---

## E. G5 / Chapter1 reference review

The package deliberately does **not** claim course-standard fidelity is already known.

Required exact private reference:

\`\`\`text
Chapter1.pdf
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Preferred durable input locator:
\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

Review these semantics:

1. Executor must directly read the exact reference before substantive course-standard implementation.
2. Missing/mismatched file -> \`BLOCKED_REFERENCE_UNAVAILABLE\`.
3. It may not reconstruct from Planner prose, screenshots, OCR summary or memory.
4. Course content/highlight annotations must not be copied as template identity.
5. Private reference must not be committed/pushed.
6. Future-required private comparison artifacts must have durable canonical-checkout copies before worktree cleanup.

G5 has two non-compensating streams for both templates:

A. canonical source actually consumed;
B. rendered visual fidelity.

A PASS/B FAIL or A FAIL/B PASS => G5 FAIL.

For course-standard, implementation Reviewer must directly access both exact \`Chapter1.pdf\` and candidate render.

For CUHK, canonical authority remains:
\`skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/\`

Architecture Critic explicitly left Chapter1 fidelity for Stage 1 artifact review. Do not treat the lack of current implementation render as an execution-package blocker if the package gives a valid direct-read/render/review path; do block if the path/authorization is not actually viable.

---

## F. Source/generated/packaging review

Verify the allowed source scope is minimal and real.

Canonical source should remain:
- Marketplace config;
- source research/business skills;
- shared routing;
- profile;
- CUHK canonical source;
- new course-standard source;
- relevant tests.

Generated:
- \`plugins/codex/plugins/**\`
- \`.agents/plugins/marketplace.json\`
- existing generator-owned mirrors

must be rebuilt by the existing generator, never hand-edited.

The conditional generator exception is only:
- direct evidence that the existing generic shared-payload mechanism cannot package the new template;
- smallest generic compatibility fix;
- no second/presentation-specific generator.

If this exception is too broad, require the smallest execution-package revision now.

---

## G. Blast radius / regression review

Stage 1 changes:
- shared routing;
- Marketplace/default prompts;
- profile;
- source skill boundaries;
- generated plugin payload;
- template source.

Therefore verify the package correctly requires broad/risk-matched regression, not only narrow tests.

Check should-not-change:
- current CUHK research route;
- explicit editable route;
- business no-format editable route;
- external locked template;
- existing deck format/template preservation;
- plan-only;
- local-edit fast path;
- production plugin identity outside the candidate.

Mechanical CI/tests are evidence, not product PASS.

---

## H. Release / version / README boundary

Stage 1 is an unreleased intermediate candidate.

Package says:
- repository bump = NONE;
- presentations = NO_BUMP;
- no production release/install;
- no maturity change;
- final README user-facing update deferred to approved Stage 6 release closure.

Review whether this is consistent with current repo policy **given that Stage 1 must remain on a reviewed branch and not integrate into production main**.

If partial Stage 1 integration would make current users consume the new behavior without a version/release closure, the package must stop before that integration rather than silently release.

---

## I. Maintenance Board

Canonical Issues #29–#48 keep their current source maturity.

Lifecycle remains:
\`DOING\`

Current Stage 1 package anchor should be:

\`results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_0.md\`
@ \`ccc6a1153d6ef3b41d1bc118e0dac454b11151d9\`

Next action:
execution-ready Critic review of all three Stage 1 package objects.

If you cannot mutate the Project because the required real Clear Writing invocation is unavailable:
- do not claim sync;
- do not ask user to drag cards;
- output the exact pending mutation.

Do not mark PROMOTED/DONE or close issues.

---

## J. External check

Perform only targeted current external verification that affects execution readiness.

At minimum verify from official sources, if relevant:
- current OpenAI plugin/skill discovery/install/runtime semantics enough to assess G1 feasibility;
- Beamer current status if template/runtime assumptions may have changed.

Do not re-run open-ended architecture research already settled by V1.1.

---

## K. Blocker standard

REVISE only for a real execution blocker with:
1. requirement;
2. direct evidence;
3. causal user/product/execution risk;
4. minimum closure condition.

Do not block merely because:
- more tests could be added;
- wording could be clearer;
- Stage 2–6 are not implemented;
- Chapter1 visual fidelity has not yet been executed;
- a recoverable ordinary coding detail remains for Executor.

---

## Expected output

First give a concise user-readable execution-readiness judgment.

Then:

\`\`\`text
RESULT = PASS | REVISE
REVIEW_STAGE = STAGE1_EXECUTION_READY

REVIEWED_PACKAGE =
results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_0.md

REVIEWED_PACKAGE_COMMIT =
ccc6a1153d6ef3b41d1bc118e0dac454b11151d9

APPROVED_PROPOSAL_PATH =
docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_0_2026-09-29.md

APPROVED_GOAL_PATH =
docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_0.md

APPROVED_KICKOFF_PATH =
docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_0.md

SCOPE_VERDICT = ...
AUTHORIZATION_VERDICT = ...
NORMAL_ENTRY_G1_VERDICT = ...
TEMPLATE_G5_VERDICT = ...
PRIVATE_REFERENCE_VERDICT = ...
REGRESSION_VERDICT = ...
RECOVERY_VERDICT = ...
RELEASE_BOUNDARY_VERDICT = ...

READY_FOR_CODEX = YES | NO
\`\`\`

If REVISE:
- use stable blocker IDs;
- modify none of the package yourself;
- return a complete Planner prompt according to Critic Role Contract.

If PASS:
- \`APPROVED_COMMIT=ccc6a1153d6ef3b41d1bc118e0dac454b11151d9\`;
- \`READY_FOR_CODEX=YES\`;
- reproduce the exact reviewed Kickoff Draft **verbatim** between:

\`\`\`text
=== APPROVED CODEX KICKOFF BEGIN ===
<verbatim file contents of APPROVED_KICKOFF_PATH>
=== APPROVED CODEX KICKOFF END ===
\`\`\`

Do not rewrite or improve the Kickoff after PASS.

This PASS would authorize only the package for later user execution. The user must still send the approved Kickoff before any task/branch/worktree/implementation action is authorized.
