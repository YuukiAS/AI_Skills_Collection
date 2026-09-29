# Canonical Goal — Presentations Stage 1 Front Door + Two-Template Foundation

**Goal version:** 1.2  
**Status:** DRAFT FOR EXECUTION-READY CRITIC REVIEW / NOT YET USER EXECUTION AUTHORIZATION  
**Task key:** \`presentations--stage1-front-door-two-template-foundation\`  
**Repository:** \`YuukiAS/AI_Skills_Collection\`

## Authority

Architecture authority:

\`docs/design/PRESENTATIONS_TWO_TEMPLATE_PRODUCTION_REDESIGN_PLAN_V1_1_2026-09-28.md @ f71e97c06938ab2ce175ccf3b4ac19da9309fda1\`

Bounded Stage 1 amendment:

\`docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_2_2026-09-29.md\`

This Goal supersedes Stage 1 Goal v1.1 only for:
- promoted TODO #49 course-standard structural/navigation + ratio-aware template foundation;
- current Bridge Kit 0.9.3 execution-control semantics.

All other Stage 1 product boundaries remain unchanged.

## 1. Goal

Implement only Presentations Stage 1:

> a unified Presentations front door with preserved editable/business/local-edit behavior and exactly two built-in Beamer template adapters, where course-standard now has a real teaching-template structural identity and explicit 4:3/16:9 ratio support.

Do not implement teaching intelligence beyond the template foundation.

## 2. Two built-in templates

Exactly:
- \`cuhk-research\`
- \`course-standard\`

No third template.

### cuhk-research

No contract change.

### course-standard

Reference/default visual family comes from exact private \`Chapter1.pdf\`.

Required visual identity:
- black top band;
- blue frame-title band;
- white body;
- restrained academic Beamer;
- ordinary blue bullets;
- sparse teaching hierarchy;
- lower-right page number;
- sans body + compatible math;
- no annotation/highlight replication;
- no CUHK research branding.

Required structural identity:
- canonical sparse opening/title frame;
- section-aware navigation/state;
- PDF outline/bookmarks;
- top navigation only where reference-consistent and nonintrusive;
- bottom navigation/action affordances through normal Beamer mechanisms where appropriate;
- stable footline + page-number behavior;
- distinct title/content/section-aware/closing frame states;
- canonical closing-frame primitive.

The closing-frame primitive may hold recap, integrative question, Q&A or thanks, but Stage 1 does not choose which semantic job a teaching deck should use.

## 3. Aspect-ratio policy

For new course-standard decks:

\`\`\`text
no explicit ratio -> 4:3 reference/default
explicit 16:9 -> course-standard 16:9 variant
\`\`\`

Precedence:
1. existing deck / external locked template ratio;
2. explicit user ratio;
3. default 4:3.

16:9 is an adapter variant, not another template.

G5 must judge:
- 4:3 candidate against exact Chapter1 visual/reference geometry;
- 16:9 candidate for correct ratio and invariant course-standard identity, not exact 4:3 dimensions.

## 4. Routing invariants

Unchanged:

\`\`\`text
research/group meeting/seminar/QE/oral/defense, no format
-> cuhk-research Beamer

Tutorial/lecture/teaching, no format
-> course-standard Beamer (default 4:3)

teaching, explicit 16:9
-> course-standard 16:9

business/executive/product/strategy/client, no format
-> editable PPTX/Slides

explicit PPTX/Slides
-> official editable adapter

existing deck/local edit
-> preserve current format/template/ratio

external locked template
-> pass-through

plan-only
-> plan only
\`\`\`

Local edit remains lightweight.

## 5. TODO disposition

\`#49\`:
- canonical status = \`PROMOTE_NOW\`;
- this Stage 1 implements only template-level structural/navigation and ratio-aware support.

Deferred without Stage 1 mechanisms:
- #50 presenter-learning companion;
- #51 teaching lecture/source cross-reference;
- #52 assessment-introduction guardrails;
- #53 closing semantic choice.

Also do not pull #35/#38/#40/#47/#48 into this amendment.

## 6. Bridge Kit 0.9.3 execution contract

Verified formal Bridge release:

\`\`\`text
BRIDGE_KIT_VERSION = 0.9.3
formal release target =
9dad0ba4bfa54e251f345091c5151ae991251ec9
FORMAL_DISTRIBUTION_COMPLETE = YES
\`\`\`

Historical Presentations blocker \`PRES-S1-ER-F03\` is closed.

Execution-machine preflight must verify compatible 0.9.3+ runtime and current command availability. If stale:

\`BLOCKED_BRIDGE_RUNTIME_STALE\`

### Exact task topology

Canonical checkout:

\`/home/yuukias/AI_Skills_Collection\`

Task:

\`presentations--stage1-front-door-two-template-foundation\`

Derived branch:

\`reviewed/presentations--stage1-front-door-two-template-foundation\`

Derived sibling worktree:

\`/home/yuukias/AI_Skills_Collection-presentations--stage1-front-door-two-template-foundation\`

### First bootstrap

Use current Bridge with \`--ci-required\`:

\`\`\`bash
ai-bridge reviewed-handoff task bootstrap \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection \
  --expected-base-commit <POST_SYNC_ORIGIN_MAIN_OID> \
  --objective "Implement approved Presentations Stage 1 v1.2 only." \
  --ci-required
\`\`\`

Expected state:

\`\`\`text
PLAN_REQUESTED
RUN_GPT_PLANNER
ci_required = true
plan_revision = 0
\`\`\`

No production edits yet.

### First metadata publication

Commit only the exact first-bootstrap REQUEST/CURRENT metadata and run:

\`\`\`bash
ai-bridge reviewed-handoff task publish-first \
  --task-key presentations--stage1-front-door-two-template-foundation \
  --expected-repo YuukiAS/AI_Skills_Collection
\`\`\`

No raw \`git push -u\` fallback.

### Planner initial freeze

External GPT Planner writes task-local \`AI_BRIDGE_REVIEWED_PLAN_V2\` and transitions:

\`\`\`text
PLAN_REQUESTED -> PLAN_FROZEN
next_action = RUN_CODEX_EXECUTOR
plan_revision = 0
\`\`\`

Only then may Executor implement product changes.

Later publication uses the existing-branch bounded publication path.

## 7. Private reference contract

Exact private input:

\`\`\`text
Chapter1.pdf
sha256 =
ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7
pages = 50
\`\`\`

Executor and implementation Reviewer must directly inspect the exact file.

Do not commit it.
Do not use the annotated STAT5060 PDF as plugin runtime input.
Do not copy STAT5060-specific content/rules into the plugin.

## 8. G1

Unchanged product Gate:
- exact committed candidate;
- installed candidate Presentations plugin;
- natural user request;
- actual candidate consumption;
- correct route/deliverable/template/ratio.

Add explicit ratio cases:
- teaching default 4:3;
- teaching explicit 16:9.

Beamer routes must actually compile/render.
Editable routes still require official editable surface.

## 9. G5

For both templates:
- actual canonical source consumption;
- independent visual fidelity.

For course-standard, G5 additionally verifies structural identity:
- opening;
- section state/navigation;
- bookmarks/outline;
- stable footline/page number;
- distinguishable closing primitive.

4:3:
- compare reference/default geometry and visual identity to Chapter1.

16:9:
- verify actual 16:9 output;
- verify invariant course-standard identity;
- ensure no clipping/broken navigation/safe-area regression;
- do not fail merely because dimensions differ from the 4:3 reference.

## 10. CI / visual-review requirement

CI:

\`CURRENT.ci_required = true\`

Real GitHub CI required.

Bridge automated visual-review flag:

\`CURRENT.visual_review_required = false\`

No \`--visual-review-required\`.
No \`--text-review-required\`.
No paid review is authorized.

But:

\`G5 independent pixel-level visual review = REQUIRED\`

Reviewer must directly inspect renders and exact Chapter1 reference. Lack of visual access is an evidence blocker.

## 11. Implementation scope

Allowed source remains bounded to:
- Marketplace Presentations source config;
- research/business source skill boundaries;
- shared routing;
- presentation-desktop profile consistency;
- canonical CUHK adapter foundation;
- new course-standard template source;
- directly relevant tests;
- existing generator outputs via canonical generator.

Do not create:
- universal schema/IR;
- teaching-content engine;
- new plugin/skill;
- new workflow/state machine;
- third template.

## 12. Validation

Require:
- targeted routing tests;
- 4:3 + 16:9 course-standard compile/render probes;
- section/navigation/bookmark/footline/opening/closing checks;
- source/generated parity;
- skills validation;
- broad/risk-matched tests;
- Reviewed Handoff validation;
- \`git diff --check\`;
- real CI;
- G1;
- G5.

## 13. Release boundary

This is an unreleased Stage 1 candidate.

\`\`\`text
Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
\`\`\`

No production install/release.
No main integration.
No maturity promotion.
No Stage 2+.

## 14. Maximum completion claim

After implementation Reviewer PASS, maximum claim:

> the exact Stage 1 candidate implements and validates the approved unified front door/routing and two-template adapter foundation, including promoted #49 structural/navigation and ratio-aware course-standard support, under G1/G5 with required CI.

It does not claim:
- full teaching intelligence;
- #50–#53 completion;
- full Presentations redesign completion;
- release readiness.

Until a new independent execution-ready Critic approves this v1.2 package and the user sends the exact approved Kickoff:

\`READY_FOR_CODEX = NO\`
