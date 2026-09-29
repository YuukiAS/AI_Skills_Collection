# Presentations Stage 1 — Codex Kickoff Draft v1.3

**Status:** DRAFT FOR EXECUTION-READY CRITIC REVIEW / NOT YET EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`

Do not execute this draft unless an independent execution-ready Critic returns \`PASS / READY_FOR_CODEX=YES\` for the exact v1.3 package and reproduces this Kickoff verbatim.

The user's later act of sending the approved Kickoff is the bounded current-user execution authorization.

---

你现在只执行 Presentations 已批准架构的 **Stage 1 — front door + routing + two-template adapter foundation**。

本 v1.3 额外关闭两个 execution-readiness blocker：

- F04：Presentations 不再硬编码机器 render/font/TeX 路径，两个 Beamer adapter 统一消费 \`render-chinese-math-pdf\` 的 portable environment/resource contract；
- F05：G5 exact private Chapter1 通过一个明确的 non-paid、direct-pixel ChatGPT evidence handoff完成，Scheduled GPT Reviewer只消费 hash-bound evidence，不假称自己看过 private pixels。

不要重新设计 Presentations。

## 1. Authority

Repository:

\`YuukiAS/AI_Skills_Collection\`

Architecture authority:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md\`
@ \`f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Stage 1 Plan v1.3:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_3_2026-09-29.md\`

Canonical Goal v1.3:

\`docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_3.md\`

Latest Critic revision basis:

\`results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V4.md\`
@ \`faae612ea90aa1e7db948ae29837e699b8d13e25\`

完整 scope / render owner / G1 / G5 / private review / stop conditions以上述 Plan + Goal 为准。

---

## 2. Exact task authorization

Canonical checkout:

\`/home/yuukias/AI_Skills_Collection\`

Task key:

\`presentations--stage1-front-door-two-template-foundation\`

Derived branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

No alternate task/branch/worktree is authorized.

---

## 3. Bridge runtime preflight

Use current formal Bridge 0.9.3+ normal entry.

Before bootstrap verify:
- compatible Bridge runtime;
- \`ai-bridge reviewed-handoff task publish-first --help\` exists;
- current Reviewed Handoff/Host validation passes.

If machine runtime is stale:

\`BLOCKED_BRIDGE_RUNTIME_STALE\`

Do not use raw Git workaround.

---

## 4. Bootstrap with CI required

From canonical checkout:

1. read current \`AGENTS.md\`;
2. read exact Critic-approved v1.3 package;
3. fetch/sync \`origin/main\`;
4. record exact post-sync \`origin/main\` OID;
5. verify no conflicting task branch/worktree;
6. run:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement approved Presentations Stage 1 v1.3 only." \
  --ci-required
\`\`\`

Do not add:
- \`--visual-review-required\`;
- \`--text-review-required\`.

Expected initial state:

\`\`\`text
PLAN_REQUESTED
RUN_GPT_PLANNER
ci_required = true
plan_revision = 0
\`\`\`

Do not edit Presentations production source yet.

---

## 5. First remote publication

Inside the exact derived worktree:

- commit only first-bootstrap \`REQUEST.md\` / \`CURRENT.json\`;
- no PLAN;
- no production source;
- no template source;
- no unrelated files.

Then:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection
\`\`\`

No raw \`git push -u\`.
No manual second authorization as the normal route.

Then stop Executor work and hand to GPT Planner.

---

## 6. Planner-owned initial freeze

External GPT Planner reads:
- task REQUEST/CURRENT;
- architecture authority;
- Stage 1 Plan v1.3;
- Goal v1.3;
- exact execution-ready Critic PASS;
- current PLAN template/contracts.

Planner writes task-local:

\`automation/reviewed_handoff/tasks/presentations--stage1-front-door-two-template-foundation/PLAN.md\`

using:

\`AI_BRIDGE_REVIEWED_PLAN_V2\`

and transitions:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

Only after this may Executor edit production source.

Executor must never freeze its own Plan.

---

## 7. Required capabilities after PLAN_FROZEN

Use:

- \`workflow-core\`;
- \`ai-skills-core\` / AI Skills Maintainer;
- \`presentations\`;
- \`render-chinese-math-pdf\` as the render environment/resource owner.

Do not expand scope.

---

## 8. Implement only Stage 1

Must implement:

- unified Presentations front door;
- Marketplace/plugin interface routing;
- research/business source-skill boundary;
- shared routing;
- presentation-desktop consistency;
- local-edit fast path;
- business/editable route preservation;
- cuhk-research adapter foundation;
- course-standard adapter foundation;
- #49 structural/navigation identity;
- course-standard 4:3 default + explicit 16:9 variant;
- portable Beamer render environment integration;
- generated-layer parity;
- G1;
- G5;
- required regression and CI.

Keep exactly two built-in templates.

---

## 9. Routing invariants

\`\`\`text
research/group meeting/seminar/QE/oral/defense, no format
-> cuhk-research Beamer

Tutorial/lecture/teaching, no ratio
-> course-standard 4:3

teaching, explicit 16:9
-> course-standard 16:9, same template identity

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides
-> official editable adapter

existing deck/local edit
-> preserve current format/template/ratio

external locked template
-> pass-through

plan-only
-> no artifact claim
\`\`\`

Local edit remains lightweight.

---

## 10. #49 only; #50–#53 remain deferred

Implement template-level:
- sparse title/opening frame;
- section-aware navigation/state;
- PDF outline/bookmarks;
- appropriate nonintrusive top navigation;
- normal-Beamer bottom navigation/action affordances where appropriate;
- stable footline/page number;
- distinct title/content/section-aware/closing states;
- canonical closing-frame primitive.

Do **not** choose semantic closing type.

Do not implement:
- #50 presenter-learning companion;
- #51 lecture/source pointer behavior;
- #52 assessment semantics/answer-leakage;
- #53 semantic closing choice;
- Stage 2–6 capabilities.

---

## 11. Render portability — mandatory F04 implementation

Current Presentations source has legacy host-specific constants. Remove the reusable host binding.

### Single owner

For both Beamer adapters:

\`render-chinese-math-pdf\`

owns:
- resource-root discovery;
- local/env/namespace/home/ancestor override resolution;
- TeX environment/cache strategy;
- font-resource discovery;
- canonical PDF QA.

Presentations owns only template-specific requirements and adapter behavior.

### Forbidden reusable paths

Reusable Presentations source/generated payload must not contain:
- \`/home/yuukias\`;
- \`/overflow\`;
- \`/users\`;
- private TinyTeX/TeXLive absolute bin paths;
- private font/resource absolute paths.

Runtime receipts may record the resolved path actually used.

### Canonical resolver

Consume the existing render-skill probe/resolution contract, including:

\`skills/tools/documents-media/render-chinese-math-pdf/scripts/probe_pdf_render_env.py\`

or its current canonical equivalent.

Do not clone a second resolver into Presentations.

### TeX environment

Use the render-owner-resolved environment for:
- \`TEXMFHOME\`;
- \`TEXMFVAR\`;
- \`TEXMFCONFIG\`;
- \`TEXMFCACHE\`;
- \`TEXINPUTS\`;
- \`OSFONTDIR\`;
- compiler discovery.

Template-local source directories may be appended as template inputs, but machine resource roots must come from the render owner.

### Missing dependency

Missing required font/package/resource/compiler/required QA tool:

\`blocked_missing_dependency\`

with exact missing dependency.

No formal PASS via:
- system font guess;
- arbitrary Times/Windows mount;
- DejaVu/Liberation/Fandol substitute;
- Chromium;
- unrelated renderer;
- rasterized substitute;
- lower-fidelity template.

### Font gate

Template-declared fonts are requirements.

Unexpected font fallback must fail canonical render/G5 QA even if compilation exits 0.

---

## 12. F04 regression gates

Run direct evidence:

### RP-G1
Same unmodified source renders from two different valid configured resource roots using supported resolver configuration.

### RP-G2
Scan:
- \`skills/tools/documents-media/presentations/**\`;
- generated \`plugins/codex/plugins/presentations/**\`;

and prove no forbidden private host path remains in reusable payload.

Historical results/evidence do not need rewriting.

### RP-G3
Controlled missing required dependency -> typed \`blocked_missing_dependency\`; no substitute PASS artifact.

### RP-G4
Unexpected font fallback -> canonical render/G5 failure.

### RP-G5
Both built-in Beamer adapter manifests record:
- \`render-chinese-math-pdf\` owner;
- resolved route/profile;
- no second Presentations-owned discovery route.

If current render skill itself proves defective, stop:

\`NEEDS_GPT_PLANNER\`

Do not silently redesign it.

---

## 13. Exact private Chapter1

Before course-standard work/review, directly use exact:

\`Chapter1.pdf\`

Expected:

\`\`\`text
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Preferred execution-machine input:

\`/home/yuukias/AI_Skills_Collection/private/exports/presentations--stage1-front-door-two-template-foundation/inputs/Chapter1.pdf\`

Do not commit/push it.
Do not copy annotated STAT5060 PDF.
Do not substitute OCR/text summary for visual fidelity.

Missing/mismatch:

\`BLOCKED_REFERENCE_UNAVAILABLE\`

---

## 14. G1

Use exact committed candidate in a fresh supported runtime with installed candidate Presentations plugin and natural prompts.

Helper/fixture/route receipt alone cannot PASS.

Beamer routes:
- real source;
- real PDF;
- real render;
- portable render-owner contract.

Editable routes:
- real official Presentation/Slides surface.

If unavailable:

\`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`

---

## 15. G5

For both built-in templates prove independently:

1. actual canonical source consumption;
2. visual fidelity.

course-standard 4:3:
- exact Chapter1 reference/default fidelity;
- structural/navigation fidelity.

course-standard 16:9:
- actual 16:9;
- same identity;
- coherent navigation/footline/opening/closing;
- no clipping.

CUHK:
- exact canonical source/fidelity unchanged.

All Beamer evidence must pass F04 portable dependency/font QA.

---

## 16. Prepare exact G5 private review bundle — F05

After product source/tests stabilize:

1. freeze exact \`implementation_commit\`;
2. generate all G5 candidate probes from that commit;
3. write tracked metadata:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_REVIEW_INPUTS.json\`

Required identities:
- task key;
- implementation commit;
- Chapter1 expected SHA;
- course template source identity;
- CUHK source identity;
- 4:3/16:9/CUHK PDF and contact-sheet hashes;
- render identities;
- render-owner route/profile.

4. copy actual files for user-visible direct review to:

\`private/exports/presentations--stage1-front-door-two-template-foundation/g5-review-bundle/\`

Include:
- exact Chapter1 or stable exact locator;
- course 4:3 candidate PDF/contact sheet;
- course 16:9 candidate PDF/contact sheet;
- CUHK candidate PDF/contact sheet where needed;
- manifest copy.

Do not commit private Chapter1/pages.

Report:

\`PRIVATE_G5_REVIEW_PENDING\`

This is an evidence-wait label, not a new CURRENT state.

---

## 17. CI chronology

After exact implementation candidate/RESULT are ready:

\`\`\`text
EXECUTING
-> WAITING_FOR_CI
ci_status = PENDING
-> real GitHub CI
-> CI PASS
-> READY_FOR_GPT_REVIEW
\`\`\`

Local tests are not CI truth.

\`visual_review_required=false\`
\`text_review_required=false\`

No paid Visual Review/Terra/Text Review.

---

## 18. Private G5 evidence handoff

The private visual evidence surface is the user-visible Presentations long-term ChatGPT Planner thread with file-upload + GitHub connector access.

When candidate bundle is ready, stop semantic review until the user provides/uploads to that thread:

- exact Chapter1.pdf;
- exact current candidate render files;
- G5_REVIEW_INPUTS.json if needed.

The thread must:
- recompute hashes;
- compare to manifest/implementation commit;
- directly inspect pixels;
- reject mismatched/stale files;
- evaluate G5 visual criteria;
- not issue overall implementation PASS.

Then it writes on the exact reviewed branch:

\`results/presentations--stage1-front-door-two-template-foundation/g5_private_review/G5_PRIVATE_VISUAL_REVIEW.md\`

Required metadata:

\`\`\`text
schema = PRESENTATIONS_G5_PRIVATE_VISUAL_REVIEW_V1
task_key
implementation_commit
review_surface = USER_VISIBLE_CHATGPT_FILE_UPLOAD
direct_private_pixel_access = YES
chapter1_sha256
candidate file hashes
render identities
decision = PASS | REVISE | BLOCKED_PRIVATE_G5_REVIEW_ACCESS
criteria/findings
private_pixels_committed = NO
\`\`\`

No private pages/screenshots are committed.

If this user-visible review surface cannot access the exact files after bounded retry:

\`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`

Recovery owner:

\`USER + GPT PLANNER\`

Do not enable paid review as fallback.

---

## 19. Scheduled GPT Reviewer contract for F05

Scheduled GPT Reviewer remains final implementation-review authority.

It must read:
- frozen Plan;
- RESULT;
- diff;
- CI;
- \`G5_REVIEW_INPUTS.json\`;
- \`G5_PRIVATE_VISUAL_REVIEW.md\`.

It must verify:
- evidence \`implementation_commit\` matches CURRENT;
- candidate hashes match current manifest;
- private review decision is PASS for G5 visual portion.

It must explicitly state it **consumed hash-bound direct-pixel evidence** and did **not** itself view private Chapter1 pixels.

If G5 private evidence is missing/stale/mismatched:
- leave CURRENT unchanged in \`READY_FOR_GPT_REVIEW\`;
- no \`REVIEW_<n>.md\`;
- no review_round consumption;
- wait on \`PRIVATE_G5_REVIEW_PENDING\`.

If private G5 evidence says REVISE, Scheduled GPT may issue normal frozen-requirement REVISE.

Executor may not self-review.

---

## 20. Validation

At minimum run current canonical equivalents of:

- targeted Presentations tests;
- course-standard 4:3 + 16:9 compile/render;
- opening/navigation/bookmark/footline/closing checks;
- RP-G1–RP-G5;
- source/generated parity;
- Marketplace generator write/validate/check/path-report;
- skills validation;
- broad/risk-matched repo regression;
- Reviewed Handoff validation;
- \`git diff --check\`;
- G1;
- G5 bundle generation;
- real GitHub CI.

Mechanical PASS cannot replace G1/G5.

---

## 21. Strict out of scope

Do not:

- implement Stage 2–6;
- implement #50–#53;
- create third template;
- create new top-level skill/plugin;
- create universal IR/schema/state machine;
- redesign render-chinese-math-pdf;
- modify Bridge Kit;
- enable paid review;
- production install/release Presentations;
- bump version;
- PR/merge main;
- modify STAT5060 repo.

---

## 22. Git / authorization boundary

If the user later sends this exact Critic-approved Kickoff, authorize only:

- exact Reviewed bootstrap with \`--ci-required\`;
- exact first REQUEST/CURRENT commit;
- exact Bridge \`task publish-first\`;
- Planner-owned V2 Plan transaction;
- task-owned Stage 1 implementation after PLAN_FROZEN;
- render-owner integration;
- tests/renders/candidate replay;
- exact Chapter1 private read;
- durable private G5 bundle writes;
- task-owned commits;
- bounded same-branch publication needed for Planner/CI/Reviewer.

Not authorized:
- alternate branch/worktree;
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

## 23. Stop / recovery

Fail closed on:

- \`BLOCKED_BRIDGE_RUNTIME_STALE\`;
- \`BLOCKED_REVIEWED_FIRST_BOOTSTRAP\`;
- \`BLOCKED_FIRST_PUBLICATION\`;
- \`BLOCKED_PLANNER_FREEZE\`;
- \`BLOCKED_CI_STATE\`;
- \`BLOCKED_DISCOVERY_CONSUMER\`;
- \`BLOCKED_REFERENCE_UNAVAILABLE\`;
- \`BLOCKED_REAL_EDITABLE_ADAPTER_SURFACE\`;
- \`BLOCKED_RENDER_ENVIRONMENT\`;
- \`blocked_missing_dependency\`;
- \`BLOCKED_UNEXPECTED_FONT_FALLBACK\`;
- \`BLOCKED_GENERATOR_ARCHITECTURE\`;
- \`PRIVATE_G5_REVIEW_PENDING\` as normal nonterminal evidence wait;
- \`BLOCKED_PRIVATE_G5_REVIEW_ACCESS\`;
- \`NEEDS_GPT_PLANNER\`.

No lower-fidelity fallback.

---

## 24. Release boundary

\`\`\`text
Repository bump decision = NONE
presentations = NO_BUMP
\`\`\`

No main integration.
No production release/install.
No maturity promotion.

Stage 1 PASS does not authorize Stage 2.

