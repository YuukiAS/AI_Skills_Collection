# Presentations Stage 1 — Codex Kickoff Draft v1.2

**Status:** DRAFT FOR EXECUTION-READY CRITIC REVIEW / NOT YET EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`

Do not execute this draft unless an independent execution-ready Critic returns \`PASS / READY_FOR_CODEX=YES\` for the exact v1.2 package and reproduces this Kickoff verbatim.

The user's later act of sending that approved text is the bounded current-user authorization.

---

你现在只执行 Presentations 已批准架构的 **Stage 1 — front door + routing + two-template adapter foundation**，并包含本轮唯一新推广项：\`#49 course-standard structural/navigation + ratio-aware template foundation\`。

不要重新设计 Presentations。

## 1. Authority

Repository:

\`YuukiAS/AI_Skills_Collection\`

Architecture authority:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md\`
@ \`f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Stage 1 Plan v1.2:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_2_2026-09-29.md\`

Canonical Goal v1.2:

\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_2.md\`

完整 scope / G1 / G5 / ratio / Bridge / stop conditions 以上述 Plan + Goal 为准。

---

## 2. Bridge Kit prerequisite

本任务使用当前已正式发布的 Bridge Kit 0.9.3 first-bootstrap / first-publication normal entry。

Formal release target:

\`9dad0ba4bfa54e251f345091c5151ae991251ec9\`

开始前必须确认当前执行环境实际提供兼容的：
- \`reviewed-handoff task bootstrap\`;
- \`reviewed-handoff task publish-first\`;
- current Reviewed Handoff validation / Machine Policy。

至少确认：

\`ai-bridge reviewed-handoff task publish-first --help\`

可用，并确认加载的 Bridge runtime 是 0.9.3 或 later compatible。

若当前机器仍是旧 Bridge、没有 \`publish-first\`，返回：

\`BLOCKED_BRIDGE_RUNTIME_STALE\`

不要恢复旧 \`PRES-S1-ER-F03\` wording，不要 raw \`git push -u\`，不要修改 Presentations 或 Bridge 规避。

---

## 3. Exact task authorization

Canonical checkout:

\`/home/yuukias/AI_Skills_Collection\`

Task key:

\`presentations--stage1-front-door-two-template-foundation\`

Derived branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

No other task/branch/worktree is authorized.

If canonical checkout/repo identity differs, stop before bootstrap.

No raw worktree creation.
No alternate clone.
No second bootstrap.

---

## 4. First bootstrap with CI required

From canonical checkout:

1. read current \`AGENTS.md\`;
2. read current approved v1.2 package;
3. sync/fetch current \`origin/main\`;
4. resolve exact post-sync \`origin/main\` OID;
5. verify no conflicting task branch/worktree;
6. run:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement approved Presentations Stage 1 v1.2 only: unified front door/routing plus two-template adapter foundation, including promoted course-standard structural/navigation and 4:3/16:9 support." \
  --ci-required
\`\`\`

Do **not** add:
- \`--visual-review-required\`;
- \`--text-review-required\`.

Successful bootstrap must leave:

\`\`\`text
PLAN_REQUESTED
RUN_GPT_PLANNER
ci_required = true
plan_revision = 0
\`\`\`

Do not edit Presentations production source yet.

---

## 5. First REQUEST/CURRENT publication through Bridge 0.9.3

Inside the exact derived worktree:

- verify first-bootstrap \`REQUEST.md\` / \`CURRENT.json\`;
- commit only that first-bootstrap metadata;
- no PLAN;
- no presentation source;
- no template source;
- no unrelated files.

Then use the current bounded first-publication normal entry:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection
\`\`\`

Do not use:
- raw \`git push -u\`;
- raw \`--set-upstream\`;
- alternate branch;
- generic publisher as a first-branch creator;
- manual second approval as the normal path.

After successful first publication, stop Executor/product work and hand ownership to GPT Planner.

---

## 6. Planner-owned initial freeze

External GPT Planner must read:
- task \`REQUEST.md\`;
- task \`CURRENT.json\`;
- architecture authority;
- Stage 1 Plan v1.2;
- Goal v1.2;
- execution-ready Critic PASS for this exact package;
- current \`automation/reviewed_handoff/templates/PLAN.md\`;
- current Planner/Reviewed Handoff contracts.

Planner writes task-local:

\`automation/reviewed_handoff/tasks/presentations--stage1-front-door-two-template-foundation/PLAN.md\`

using:

\`AI_BRIDGE_REVIEWED_PLAN_V2\`

Then legally transition:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

Publish this Planner transaction through the normal existing-branch bounded publication path.

Executor must never write/freeze its own Plan.

Only after remote/current task truth is:

\`\`\`text
PLAN_FROZEN
RUN_CODEX_EXECUTOR
\`\`\`

may implementation begin.

---

## 7. Required capabilities after PLAN_FROZEN

Use:
- \`workflow-core\`;
- \`ai-skills-core\` / AI Skills Maintainer;
- \`presentations\`.

Do not use them to expand scope.

---

## 8. Required private reference

Before implementing course-standard, directly read exact private:

\`Chapter1.pdf\`

Expected:

\`\`\`text
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Preferred durable locator:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

本 Kickoff授权该 exact private reference 仅用于 course-standard implementation 和 G5 fidelity review，并允许在 task-owned durable private path 保存必要 reference render / candidate render / review bundle。

不得：
- commit/push private pages/content;
- 根据 Planner prose / screenshot / OCR summary / memory 重建;
- 把本轮 STAT5060 annotated PDF复制进 AI_Skills；
- 把 STAT5060具体例子/页码/HW内容写成 runtime rule。

Missing/hash mismatch:

\`BLOCKED_REFERENCE_UNAVAILABLE\`

---

## 9. Implement only Stage 1 + #49

必须完成：

- unified Presentations front door;
- Marketplace/plugin interface routing;
- research/business source-skill boundary;
- shared routing;
- presentation-desktop consistency;
- local-edit fast path;
- business/editable route preservation;
- cuhk-research canonical adapter foundation;
- course-standard canonical adapter foundation;
- **#49 structural/navigation template identity**;
- **course-standard 4:3 default + explicit 16:9 variant**;
- generated layer only through canonical generator;
- G1;
- amended G5;
- required tests/render/CI.

### course-standard visual identity

- black top band;
- blue frame-title band;
- white body;
- restrained academic Beamer;
- ordinary blue bullets;
- sparse teaching hierarchy;
- lower-right page number;
- sans body + compatible math;
- no highlight replication;
- no CUHK branding.

### course-standard structural identity

Template-level support for:

- canonical sparse title/opening frame;
- section-aware navigation/state;
- PDF outline/bookmarks;
- nonintrusive top navigation where appropriate;
- normal-Beamer bottom navigation/action affordances where appropriate;
- stable footline/page number;
- distinct title/content/section-aware/closing states;
- canonical closing-frame primitive.

The closing primitive may hold recap/question/Q&A/thanks, but **Stage 1 must not decide which semantic closing every teaching deck uses**.

---

## 10. Aspect-ratio contract

Routing:

\`\`\`text
teaching, no ratio
-> course-standard 4:3 default

teaching, explicit 16:9
-> course-standard 16:9

existing deck/local edit
-> preserve current ratio

external locked template
-> preserve locked ratio
\`\`\`

16:9 is not a third template.

Do not route teaching 16:9 to CUHK merely because CUHK is wide.

No universal ratio schema/state machine.

---

## 11. Keep #50–#53 out of Stage 1

Do not implement:

- #50 instructor/presenter learning companion;
- #51 teaching source/lecture pointers;
- #52 assessment-introduction semantics or answer-leakage logic;
- #53 semantic closing choice.

Also do not pull in:
- full responsive-layout intelligence;
- table/list/paragraph semantic selection;
- simulation explanation framework;
- natural-language rewriting;
- slide-specific STAT5060 repairs.

---

## 12. Routing invariants

Still preserve:

\`\`\`text
research/group meeting/seminar/QE/oral/defense, no format
-> cuhk-research Beamer

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides
-> official editable adapter

existing deck/local edit
-> preserve format/template/ratio

external locked template
-> pass-through

plan-only
-> no artifact claim
\`\`\`

Local edit remains lightweight.

---

## 13. G1

Use exact committed candidate in a fresh supported runtime with installed candidate Presentations plugin and natural prompts.

Helper/fixture/route receipt/direct script alone cannot PASS.

Add explicit ratio route evidence:
- teaching no ratio -> course-standard 4:3;
- teaching explicit 16:9 -> same course-standard 16:9.

Beamer route:
- real source;
- real PDF;
- real render.

Editable route:
- real supported official Presentation/Slides surface.

If unavailable:

\`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`

---

## 14. G5

For both built-in templates prove independently:

1. canonical source actually consumed;
2. visual fidelity.

For course-standard also verify structural identity.

### 4:3

Directly compare candidate to exact Chapter1 reference for:
- ratio/reference geometry;
- visual identity;
- opening;
- section state/navigation;
- bookmarks;
- footline/page number;
- closing primitive.

### explicit 16:9

Do not demand 4:3 pixel dimensions.

Verify:
- actual 16:9;
- invariant course-standard visual/structural identity;
- navigation/footline/bookmarks/opening/closing remain coherent;
- no clipping/safe-area regression.

Consumption PASS cannot compensate for visual FAIL, and vice versa.

---

## 15. Visual-review and CI truth

Bridge task:

\`ci_required = true\`

Real GitHub CI is mandatory.

Bridge automated/payed visual review:

\`visual_review_required = false\`

Do not add paid Visual Review/Text Review/Terra.

However:

\`G5 independent pixel-level visual review = REQUIRED\`

The implementation Reviewer must directly access the actual candidate renders and exact Chapter1 reference.

If Reviewer cannot access required visual evidence, fail closed; do not use OCR/text summary as substitute.

---

## 16. Validation

At minimum run current canonical equivalents of:

- targeted Presentations routing/template tests;
- course-standard 4:3 compile/render;
- course-standard 16:9 compile/render;
- title/section navigation/bookmark/footline/closing structural checks;
- Marketplace generator write/validate/check/path-report;
- skills validation;
- broad/risk-matched repo regression;
- Reviewed Handoff validation;
- \`git diff --check\`;
- G1;
- G5.

After exact candidate is ready:

\`\`\`text
EXECUTING
-> WAITING_FOR_CI
ci_status = PENDING
-> real GitHub CI
-> CI PASS
-> external implementation review
\`\`\`

Local tests are not CI truth.

---

## 17. Strict out of scope

Do not:

- implement Stage 2–6;
- create universal IR/schema;
- create third built-in template;
- create new top-level presentation skill/plugin;
- create geometry engine;
- implement #50–#53;
- promote #44–#48 other than already-authorized #49;
- modify Bridge Kit;
- create new workflow/state machine;
- run paid review;
- production install/release Presentations;
- bump version;
- PR/merge main;
- modify STAT5060 repo.

---

## 18. Git / authorization boundary

我发送这段 Critic-approved Kickoff，仅授权：

- exact bootstrap with \`--ci-required\`;
- exact first REQUEST/CURRENT commit;
- exact Bridge 0.9.3 \`task publish-first\`;
- Planner-owned V2 Plan transaction;
- Stage 1 v1.2 task-owned implementation after PLAN_FROZEN;
- tests/render/candidate replay;
- exact Chapter1 private read;
- durable task-private evidence;
- ordinary task-owned commits;
- bounded same-branch publication required for Planner/CI/Reviewer.

Not authorized:

- alternate task/branch/worktree;
- raw first push;
- force/destructive Git;
- PR/main integration;
- tag/release;
- production install/sync;
- version bump;
- paid API/model review;
- credential/provider changes;
- Bridge mutation.

---

## 19. Completion boundary

Stage 1 Reviewer PASS may claim only:

> the exact Stage 1 v1.2 candidate implements the unified front door/routing and two-template adapter foundation, including #49 structural/navigation identity and ratio-aware course-standard support, under G1/G5 with required CI.

It does not authorize Stage 2, release, main integration or maturity promotion.
