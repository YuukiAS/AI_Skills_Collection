# Product UI Copy Cross-Plugin — Canonical Goal v0.2

Status: `DRAFT_FOR_EXECUTION_READY_CRITIC`  
Architecture authority: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md` @ `a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67`  
Architecture Critic PASS: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_REVIEW_V0_2_2026-09-28.md`  
Execution Plan: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_2_2026-09-28.md`  
Prior execution-ready review: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md` @ `c1982a3ffddeafbc906087ff1da40e5bcfc43e46` — only `PUC-ER-01` remained.  
Implementation authorization: **NO until v0.2 execution-ready Critic PASS + explicit user Kickoff**

## 1. Exact task identity

```text
task_key = product-ui-copy--cross-plugin-production-integration
branch = reviewed/product-ui-copy--cross-plugin-production-integration
expected canonical checkout = /home/yuukias/AI_Skills_Collection
expected sibling worktree =
  /home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration
```

Bridge first bootstrap must derive this sibling worktree from the exact canonical checkout.

If the execution machine's canonical checkout is not exactly `/home/yuukias/AI_Skills_Collection`, do not invent another path. Stop before bootstrap and return to Planner.

No task branch/worktree exists at Goal-writing time.

## 2. Product goal

Create one normal, installable AI_Skills workflow in which:

```text
Frontend Design
  decides whether/where/how much UI text belongs on a surface
→ freezes UI role + product state + protected meaning
→ hands wording/localization to Clear Writing Product UI Copy
→ receives natural locale-specific copy
→ validates the copy in the actual rendered page/screen
```

The user should not have to repeatedly say “use Frontend Design” for user-facing interface work merely because the product is a browser extension, desktop app, WebView app or Android/Compose app.

## 3. Frozen ownership

### Product/domain/legal authority

Owns product truth, state, eligibility, consent/privacy/legal/safety/trust facts and actual user consequence.

### Frontend Design

Owns:

- whether text is needed;
- placement;
- UI role;
- amount;
- hierarchy;
- duplicate payload;
- progressive disclosure;
- final rendered page/screen acceptance.

### Clear Writing / Product UI Copy

Owns:

- wording under frozen meaning;
- Product UI microcopy naturalness;
- locale/register;
- zh-Hans / zh-Hant-HK independent realization;
- first-pass linguistic page rhythm;
- fidelity-preserving escalation.

No owner may silently take another owner's final decision.

## 4. Required production behavior

### Clear Writing

Add one sibling Skill:

`skills/writing/core/product-ui-copy/`

Normal UI copy must be discoverable through its frontmatter metadata.

Narrow `chinese-prose` **frontmatter description** so Product UI microcopy no longer competes with its report/README/technical-prose route.

Preserve existing `chinese-prose` long-form behavior.

Expose Product UI Copy from the `writing-style` plugin description/default prompt/package.

Keep `writing-fidelity` as the protected-meaning layer.

### Frontend Design

Keep Frontend Design 0.3 coordinator-first topology.

Extend normal trigger/discovery from web-page framing to product-interface work across:

- browser extension;
- web;
- desktop/Tauri/Electron/native-WebView;
- mobile/Android/Compose.

Do not trigger for backend/runtime/data/docs-only tasks with no user-interface work.

Add the approved content-architecture → Product UI Copy handoff and rendered acceptance.

### Locale / page rhythm

zh-Hans and zh-Hant-HK are independent realizations from one protected meaning.

Writing owns first-pass linguistic rhythm.

Frontend owns final rendered rhythm.

## 5. Non-substitutable semantics

The task is not complete if any of these are replaced by a weaker proxy:

- adding a `product-ui-copy` file without fixing `chinese-prose` metadata competition;
- source prose without packaged plugin discovery;
- two separate plugin replays instead of proving both candidate plugins are consumed in one cross-plugin normal-entry runtime;
- keyword counts instead of naturalness judgment;
- character conversion instead of locale realization;
- polished wording that hides unresolved product/legal semantics;
- static string review without rendered copy/layout acceptance;
- metadata/synthetic mobile trigger tests without read-only SeminarArc positive + negative normal-entry replay;
- known regressions relabeled as fresh holdout;
- fresh holdout exposed before final candidate freeze;
- CI/tests standing in for qualitative text/render review;
- consumer hard-binding claims without actual consumer-repo adaptation.

## 6. Required evidence gates

The release candidate must satisfy Execution Plan G1–G8 on the same final candidate.

Any G1–G6 results gathered before version bump/regeneration are **development evidence only**. Release PASS requires the exact versioned H2 candidate to directly rerun and PASS every G1–G6 gate marked final-candidate before H3 begins:

- G1 Discovery / activation / packaging
- G2 Ownership / handoff / protected meaning
- G3 Naturalness / locale / linguistic page rhythm
- G4 Frontend rendered acceptance
- G5 Should-not-change regressions
- G6 Same-session cross-plugin normal entry + Lucerna/Mica/SeminarArc compatibility
- G7 Fresh generalization H0→H4
- G8 Release / CI / README / review closure

## 7. H0→H4 fresh-evidence contract

Before implementation:

- freeze only families, coverage, rubric, batch size, locale balance and reviewer criteria;
- do not expose exact final holdout prompts.

After implementation/known regressions/rendered acceptance are stable:

1. apply release metadata exactly once;
2. regenerate packaged plugins/Marketplace;
3. freeze the versioned H2 final candidate;
4. freeze reviewer criteria;
5. directly rerun all release-critical G1–G6 on that exact H2 candidate.

Only after the exact H2 candidate has G1–G6 PASS:

```text
EXECUTING
→ NEEDS_GPT_PLANNER
→ external Planner freezes exact H3 holdout batch
→ Planner updates task-local PLAN only with exact holdout/candidate binding
→ PLAN_FROZEN with plan_revision = 1
→ Executor runs complete H4 batch once
```

If an H2 G1–G6 gate fails before H3:

- repair without another version bump;
- freeze a new H2 candidate commit;
- rerun all release-critical G1–G6 on that candidate;
- do not reveal/freeze H3 until one exact H2 candidate has all G1–G6 PASS.

Pre-H2 G1–G6 cannot be spliced with post-H2 H4/CI evidence.

If H4 fails:

- preserve the failed batch;
- no replacement/chasing;
- same batch becomes known if used for repair;
- do not claim release readiness;
- no second automatic fresh batch.

## 8. Real-project compatibility

Read-only final-candidate replays:

### Lucerna

Desktop/native-WebView Product UI Copy compatibility.

### Mica for ChatGPT

Browser-extension normal-entry and diagnostic-vs-user language compatibility.

### SeminarArc

Positive:

natural Compose/UI task must enter Frontend Design without naming it and preserve `android-lead` / `compose-expert` implementation authority.

Negative:

Room/WorkManager/data-only task must not activate Frontend Design.

No consumer repository may be modified.

These replays do not promote maturity.

## 9. Candidate runtime requirement

One same-session replay must prove actual consumption of both:

- `web-development@ai-skills-candidate`
- `writing-style@ai-skills-candidate`

from the same candidate commit.

If necessary, minimally extend the existing `scripts/candidate_plugin_replay.py` rather than create a second replay framework.

Single-plugin replay compatibility must remain intact.

## 10. Rendered acceptance

Representative repo-safe Product UI fixtures must be actually rendered.

At minimum inspect:

- wide/desktop viewport;
- narrow/mobile viewport;
- multi-block page rhythm;
- trust/help disclosure;
- already-good control.

Reviewer must actually access the images.

If the available Reviewer surface cannot inspect them, return an evidence-access blocker. Do not substitute filenames/OCR/Executor prose.

Paid Visual Review/Text Review/Terra is **not authorized** by this Goal.

## 11. Version contract

If release baseline remains unchanged:

```text
Repository bump decision: MINOR
Repository: 5.3.1 -> 5.4.0

Affected plugins:
- web-development: 0.3 -> 0.4
- writing-style: 0.3 -> 0.4
- all other central plugins: NO_BUMP

Maturity:
- web-development: unclassified
- writing-style: unclassified
```

Why MINOR:

The collection gains a previously absent normal cross-plugin workflow:

`Frontend content architecture → protected Product UI Copy → locale realization → rendered Frontend acceptance`.

If another formal release advances main first, recalculate concrete numbers from then-current source without changing the approved release class/affected-plugin intent unless a real source conflict requires Planner/Critic review.

Do not bump during planning/bootstrap.

Do not bump twice after a repair.

The version bump/regeneration changes final plugin identity. Therefore the exact versioned H2 candidate must directly pass release-critical G1–G6 before fresh H3/H4. Any repaired H2 candidate keeps the same selected release versions and must rerun all release-critical G1–G6.

## 12. Allowed scope

Allowed production/refinement areas are exactly those in Execution Plan §4.

Use:

`workflow-core + ai-skills-core + web-development + writing-style`.

Generated payload is generator-owned.

Evidence goes under:

`results/product-ui-copy--cross-plugin-production-integration/**`

## 13. Forbidden scope

No:

- Bridge Kit modification;
- Host Policy change;
- consumer-repo edits;
- CUHK Date edits;
- new top-level plugin;
- new orchestrator;
- broad writing-style #13 implementation;
- Frontend 0.3 architecture redesign;
- paid review without separate authorization;
- maturity promotion;
- successor task;
- destructive Git;
- main merge/release-ref mutation before later explicit authorization.

## 14. Maintenance tracking

Before final central release closure:

- keep Issue #17 as valid Product UI Copy tracking;
- keep Issue #13 dependency-only;
- replace collided Frontend `#73` with a unique Issue;
- replace collided writing-style `#20` with a unique Issue;
- invoke installed Clear Writing before reader-facing Issue/Project mutation;
- update canonical `tracking: #N`;
- Project = DOING during central implementation;
- if known consumer hard bindings remain outstanding after central release, lifecycle becomes ADAPTING rather than falsely DONE.

If the execution surface cannot mutate Project fields, write exact pending mutations for a Project-capable maintainer; do not ask the user to maintain the board manually.

## 15. Workflow chronology

1. Proposal v0.2 PASS — complete.
2. Execution package v0.2 — current stage.
3. Independent execution-ready Critic re-review.
4. User sends approved Kickoff.
5. Bridge first bootstrap exact task/branch/sibling worktree.
6. GPT Planner writes task-local `AI_BRIDGE_REVIEWED_PLAN_V2`.
7. Initial `PLAN_REQUESTED -> PLAN_FROZEN`, `plan_revision=0`.
8. Executor H0 + implementation + G1–G6 **development** evidence.
9. Version closure + regenerate + versioned H2 candidate freeze.
10. Exact H2 candidate directly reruns and passes all release-critical G1–G6.
11. If any H2 G1–G6 gate fails: repair same release version, freeze new H2, rerun all release-critical G1–G6; remain before H3.
12. Only after exact-H2 G1–G6 PASS: intentional `NEEDS_GPT_PLANNER`.
13. Planner H3 exact holdout freeze; `plan_revision=1`.
14. Executor H4 one-shot on unchanged H2 candidate.
15. H4 PASS → RESULT + WAITING_FOR_CI.
16. Real GitHub CI.
17. Independent Reviewer verifies exact-H2 G1–G6 + H4/G8 evidence.
18. User final acceptance.
19. Later separately authorized integration/release.
20. Later consumer adaptation for project-local hard bindings.

## 16. Completion semantics

Central task candidate completion requires:

- G1–G8 PASS;
- H4 fresh PASS;
- CI PASS;
- independent Reviewer PASS;
- human acceptance.

Released completion additionally requires separately authorized integration and release-ref closure.

This Goal does not claim the six known consumer repositories are hard-bound after central release.

Overall user-facing adaptation remains outstanding until separate project-local bindings are applied and the Maintenance Board can truthfully leave ADAPTING.

## 17. Durable execution-ready Critic review

Expected review artifact:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`

It must record:

```text
RESULT = PASS | REVISE
READY_FOR_CODEX = YES | NO
REVIEWED_PACKAGE_VERSION = v0.2
APPROVED_PLAN = docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_2_2026-09-28.md
APPROVED_GOAL = docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_2.md
APPROVED_KICKOFF = docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_2.md
APPROVED_PACKAGE_COMMIT = ...
APPROVED_TASK_KEY = product-ui-copy--cross-plugin-production-integration
APPROVED_BRANCH = reviewed/product-ui-copy--cross-plugin-production-integration
APPROVED_WORKTREE = /home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration
ARCHITECTURE_AUTHORITY = Proposal v0.2 @ a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67
```

Planner must not pre-fill a PASS.

Until that review is PASS and the user sends the approved Kickoff:

`GOAL_ACHIEVED = NO`
