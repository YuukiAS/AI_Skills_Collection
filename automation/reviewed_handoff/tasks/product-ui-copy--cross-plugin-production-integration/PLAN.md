---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: product-ui-copy--cross-plugin-production-integration
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan — Product UI Copy Cross-Plugin Production Integration

## Objective and value

Implement the already approved Product UI Copy cross-plugin workflow without reopening architecture.

Canonical authorities:

- Proposal v0.2:
  `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md`
  @ `a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67`
- Execution Plan v0.2:
  `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_2_2026-09-28.md`
- Canonical Goal v0.2:
  `docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_2.md`
- Kickoff v0.2:
  `docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_2.md`
- Approved execution package commit:
  `926fc059ad5b7460fcb91074bd1d3aadb5717432`
- Durable execution-ready Critic PASS:
  `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`
  @ main commit `def5ea15f8c28601d8324b3fd6a00275c0a795ee`
  with `RESULT=PASS`, `READY_FOR_CODEX=YES`, `PUC-ER-01=CLOSED`.

This task-local Plan is only the Bridge runtime translation of those approved authorities. It must not create a second architecture. If this Plan conflicts with the approved v0.2 execution package, stop and return to Planner rather than treating the task-local text as a new authority.

Exact task identity:

```text
task_key = product-ui-copy--cross-plugin-production-integration
branch = reviewed/product-ui-copy--cross-plugin-production-integration
worktree = /home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration
base_branch = main
base_commit = def5ea15f8c28601d8324b3fd6a00275c0a795ee
```

The user-visible value is a real normal workflow in which Frontend Design decides UI content architecture, Clear Writing realizes natural locale-specific Product UI Copy under protected meaning, and Frontend then validates the copy in the rendered interface. Frontend discovery must work for browser extension, web, desktop/WebView and mobile/Compose UI work without requiring the user to repeatedly name Frontend Design.

## Frozen decisions

1. **Three-owner boundary**
   - Product/domain/legal authority owns product truth, product state, eligibility, user consequence, consent/privacy/legal/safety/trust facts.
   - Frontend Design owns whether text belongs on the surface, placement, UI role, amount, hierarchy, duplication, progressive disclosure and final rendered acceptance.
   - Clear Writing / Product UI Copy owns natural-language realization under frozen meaning, locale/register, short-copy naturalness and first-pass linguistic page rhythm.

2. **Dedicated Clear Writing sibling**
   - Add `skills/writing/core/product-ui-copy/`.
   - Do not create a new top-level plugin.
   - Do not turn `chinese-prose` into the Product UI Copy engine.

3. **Trigger metadata is production routing**
   - `product-ui-copy` frontmatter must positively cover product-interface copy such as labels, CTA, status, help, empty/loading/error, onboarding, settings, trust/privacy, landing microcopy and locale-specific UI wording.
   - `chinese-prose` frontmatter description must be narrowed so reports/README/technical docs/ordinary Chinese prose stay there while Product UI microcopy does not.
   - Preserve the existing `chinese-prose` long-form mechanism.
   - `writing-style` plugin metadata/package must expose Product UI Copy through description, default prompt and packaged Skill list.

4. **Lightweight Frontend → Writing handoff**
   Use the approved prompt-level fields:
   `SURFACE`, `UI_ROLE`, `PRODUCT_STATE`, `USER_JOB`,
   `USER_CONSEQUENCE_OR_NEXT_ACTION`, `NEIGHBORING_VISIBLE_COPY`,
   `LOCALE`, `PROTECTED_MEANING`, `DISCLOSURE_LEVEL`,
   `LENGTH_OR_VIEWPORT_CONSTRAINT`, with optional `DESIGN_AUTHORITY`
   and `TERMINOLOGY_OR_BRAND_TOKENS`.
   Do not create a schema/database/ledger/state machine for this handoff.

5. **Reasoning taxonomy**
   Preserve:
   `KEEP`, `WORDING/NATURALNESS`, `LOCALE/REGISTER`,
   `CONTENT ARCHITECTURE`, `PRODUCT SEMANTICS`,
   `LEGAL/TRUST/SAFETY`.
   This is reasoning structure, not a machine enum.

6. **Fidelity**
   `writing-fidelity` remains the protected-meaning guardrail.
   Product state/availability, eligibility, verification meaning, consent, privacy/data use/retention/deletion, safety claims, pricing/payment/subscription, action consequence, reversibility/destructiveness, visibility to others/systems, required legal/trust disclosure and exact product/brand/technical identities must not silently drift.

7. **Page rhythm**
   - Writing owns first-pass linguistic page rhythm.
   - Frontend owns final rendered page/screen rhythm.
   - There is no second final owner.

8. **Locale**
   `zh-Hans` and `zh-Hant-HK` are independent realizations from one protected meaning. Character conversion alone is not localization acceptance.

9. **Frontend discovery remains coordinator-first**
   Do not redesign Frontend Design 0.3 topology.
   Extend normal product-interface discovery across browser extension, web, desktop/Tauri/Electron/native-WebView and Android/Compose/mobile.
   Do not trigger Frontend for backend/API/math, runtime/provider/network, Room/WorkManager/data-layer, docs-only README or other no-UI work.

10. **Platform/domain authority stays local**
    SeminarArc `android-lead` / `compose-expert` retain Android/Compose implementation authority after generic Frontend product-interface coordination.

11. **Consumer hard bindings are later adaptation**
    Do not modify Mica, CUHK Date, Asteria, Bobbio, Lucerna or SeminarArc in this task.

12. **Versions**
    Under the frozen baseline:
    ```text
    Repository: 5.3.1 -> 5.4.0
    web-development: 0.3 -> 0.4
    writing-style: 0.3 -> 0.4
    all other central plugins: NO_BUMP
    maturity: unchanged / unclassified
    ```
    If another formal main release changes the arithmetic before release closure, follow the approved current version policy without changing the approved repository-level MINOR / affected-plugin intent unless a real source conflict requires Planner/Critic review.

13. **No paid review in this task**
    `visual_review_required` and `text_review_required` remain unset. Repo-safe screenshots/text evidence must be directly inspectable by the independent Reviewer. If evidence is inaccessible, fail closed rather than silently enabling paid review.

14. **Fresh evidence uses the one scheduled re-plan**
    H3 exact fresh-holdout text is intentionally unavailable during implementation. After the exact H2 versioned candidate has direct G1–G6 release-critical PASS, Executor transitions to `NEEDS_GPT_PLANNER`. Planner then freezes the exact H3 batch and re-freezes Plan. This is the only scheduled plan revision and consumes `plan_revision: 0 -> 1`.

## Positive completion

This task is complete only when one same final production candidate provides all of the following observable outcomes:

1. Ordinary Product UI Copy requests route to the new `product-ui-copy` Skill, while long-form Chinese, scientific rewrite and other existing Clear Writing routes remain correct.
2. Frontend Design normal discovery works for browser extension, web, desktop/WebView and mobile/Compose UI tasks without the user naming Frontend Design, while backend/runtime/data/docs negatives do not misroute.
3. The cross-plugin normal path actually performs:
   `Frontend content architecture -> protected handoff -> Product UI Copy -> returned wording -> rendered Frontend acceptance`.
4. Product/legal/trust semantics are preserved or escalated rather than cosmetically rewritten.
5. zh-Hans and zh-Hant-HK outputs are independently natural and semantically equivalent, not mechanical conversions.
6. Already-good copy can remain `KEEP`; the system does not rewrite every line to demonstrate activity.
7. Actual rendered evidence shows acceptable wide/narrow layout, page rhythm, trust/help disclosure and CTA relationship.
8. One same-session candidate runtime proves actual consumption of both `web-development@ai-skills-candidate` and `writing-style@ai-skills-candidate` from the same candidate commit.
9. Read-only Lucerna, Mica and SeminarArc compatibility replays pass; SeminarArc mobile UI enters Frontend while Room/WorkManager/data-only work does not, and project-local Android/Compose owners remain authoritative.
10. The exact versioned H2 candidate directly passes all release-critical G1–G6 gates after version bump/regeneration, then passes the one-shot H4 fresh batch unchanged.
11. Full required repository validation and real GitHub CI pass.
12. Independent Reviewer directly inspects the real text/render evidence and returns PASS.
13. Release metadata, both plugin changelogs, root CHANGELOG, README, VERSION, generated manifests and version/parity truth agree.
14. Tracking collision repair is handled truthfully, and central completion does not falsely claim consumer project bindings are already done.

Maximum supported claim before separately authorized integration:

> The reviewed branch candidate implements and validates the approved Product UI Copy cross-plugin workflow for the frozen scope and evidence set.

This does not prove either plugin is mature/stable, does not prove every future interface/platform, and does not mean consumer repositories are hard-bound.

## Non-substitutable semantics

- A `product-ui-copy` file existing in source is not sufficient if normal routing still selects `chinese-prose`.
- Good-looking prose from the wrong Skill/plugin route is not a routing PASS.
- Separate single-plugin replays are not equivalent to one same-session proof that both candidate plugins are consumed.
- Tests/CI/schema/generated-file existence cannot substitute for naturalness, fidelity or rendered-interface judgment.
- Browser-rendered fixtures do not prove native platform behavior.
- Character conversion is not locale validation.
- Product/legal/trust uncertainty must be escalated; Writing cannot invent the missing truth.
- `KEEP` is a valid outcome and must be preserved.
- Frontend Design must not replace SeminarArc platform owners or other project-local domain authority.
- CUHK Date, Lucerna, Mica and SeminarArc development/real-project cases are known/compatibility evidence, not fresh maturity evidence.
- Exact fresh H3 prompts must remain unavailable until after H2 candidate + reviewer criteria freeze.
- Pre-H2 G1–G6 are development evidence only. They cannot be spliced into release PASS.
- Version bump + regeneration happen before H2. The exact versioned H2 candidate must directly rerun and pass every release-critical G1–G6 gate before H3.
- If an H2 G1–G6 gate fails, repair within approved scope without another version bump, regenerate, freeze a new H2 candidate, and rerun all release-critical G1–G6 before H3.
- H4 runs once on the unchanged H2 candidate that already passed release-critical G1–G6. Failed H4 prompts cannot be replaced/chased.
- No consumer repo write, paid review, main merge or release-ref movement is implied by local implementation PASS.

## Implementation scope

Use the required maintenance stack:

`workflow-core + ai-skills-core + web-development + writing-style`.

Allowed production/refinement areas:

### Clear Writing

- `skills/writing/core/product-ui-copy/**`
- `skills/writing/core/writing-fidelity/SKILL.md` — narrow Product UI Copy semantic-fidelity handoff
- `skills/writing/core/chinese-prose/SKILL.md` — frontmatter narrowing + minimal matching route note
- directly necessary Product UI Copy / Clear Writing routing tests/fixtures
- `scripts/codex_marketplace_config.json` for `writing-style` description/default prompts/packaging/version

Do not change `scientific-rewrite` or `scientific-prose` semantics unless a direct regression shows the new routing broke them; a required semantic redesign returns to Planner.

### Frontend Design

- `skills/tools/frontend/frontend-visual-systems/SKILL.md`
- `skills/tools/frontend/product-ux-planning/SKILL.md`
- `skills/tools/frontend/responsive-accessibility-review/SKILL.md`
- directly necessary Frontend trigger/routing tests/fixtures
- `scripts/codex_marketplace_config.json` for `web-development` discovery/default prompts/version

Coordinator-first topology remains frozen.

### Profiles

Review/change only if required by approved companion exposure:

- `profiles/codex-webdev.json`
- `profiles/frontend-research-product.json`

Do not create a new dependency manager/profile solely for Product UI Copy.

### Candidate replay helper

Reuse `scripts/candidate_plugin_replay.py`.

If no equivalent current route exists, minimally generalize it so one isolated run can stage/install both candidate plugins from the same candidate commit, prove both installed Skill paths were actually consumed, remove both candidate identities, prove production same-name installs unchanged, and preserve existing single-plugin behavior.

Do not create another replay framework.

### Generated/release/evidence surfaces

Generated files remain generator-owned:

- `.agents/plugins/marketplace.json`
- `plugins/codex/plugins/**`
- registry/catalog generated output as required.

Evidence:

`results/product-ui-copy--cross-plugin-production-integration/**`

Release closure may update:

- `docs/plugin-todos/web-development.md`
- `docs/plugin-todos/writing-style.md`
- `docs/plugin-changelogs/web-development.md`
- `docs/plugin-changelogs/writing-style.md`
- `CHANGELOG.md`
- `README.md`
- `VERSION`
- directly related version/parity tests.

Tracking mutations are bounded to this task and must obey the repository Clear Writing rule before reader-facing Issue/Project copy is written.

## Acceptance and regression gates

All release-critical evidence must bind to the same final candidate. G1–G6 may be used during development, but only the post-version exact H2 rerun counts toward release PASS.

### G1 — Discovery / activation / packaging

Prove:

- Product UI Copy direct/indirect requests select `product-ui-copy`;
- long-form Chinese near-misses remain on `chinese-prose`;
- heavy structural scientific rewrite remains on `scientific-rewrite`;
- browser extension/web/desktop/mobile UI requests enter Frontend;
- backend/runtime/data/docs negatives do not;
- packaged plugin metadata/default prompts/generated payload are correct;
- actual selected Skill/plugin identity is recorded.

### G2 — Ownership / handoff / protected meaning

Cover `KEEP`, wording, locale, content architecture, product semantics, legal/trust/safety, S1/S2/S3 and protected-proposition move/delete rules.

Writing must not invent product/legal truth; Frontend must not become the wording owner.

### G3 — Naturalness / locale / linguistic page rhythm

Use CUHK Date known regression, Lucerna known case, Mica read-only cases and good `KEEP` controls during development.

Final-candidate evidence must show:

- natural Product UI Copy;
- independent zh-Hans / zh-Hant-HK realization;
- no rewrite-everything behavior;
- no phrase-ban/AI-detector shortcut;
- acceptable page-set linguistic rhythm;
- independent qualitative judgment.

### G4 — Frontend rendered acceptance

Create repo-safe representative UI fixtures and actual screenshots covering:

- wide/desktop;
- narrow/mobile;
- multi-block page rhythm;
- trust/help disclosure;
- already-good copy control.

Bind screenshots to exact H2 copy/layout source and viewport. Reviewer must actually access the images.

### G5 — Should-not-change

Preserve:

- Clear Writing report/README route;
- scientific-rewrite route;
- English scientific prose;
- writing-fidelity-only route;
- Frontend 0.3 coordinator-first behavior;
- S1/S3;
- Figma/no-Figma;
- browser/native evidence boundaries;
- generator/Marketplace parity;
- candidate helper single-plugin compatibility if helper changes;
- full repository unit tests.

### G6 — Same-session cross-plugin normal entry + real-project compatibility

One isolated run must prove both candidate plugins from the same candidate commit are consumed:

- `web-development@ai-skills-candidate`
- `writing-style@ai-skills-candidate`

Required replay families:

- generic cross-plugin Product UI Copy;
- Lucerna read-only desktop/native-WebView;
- Mica read-only browser extension;
- SeminarArc read-only Compose/UI positive;
- SeminarArc Room/WorkManager/data-only negative.

Prompts must be neutral and not state the expected plugin/Skill route.

The approved Kickoff authorizes only the minimum frozen read-only source needed from Lucerna, Mica and SeminarArc for this compatibility purpose; no consumer writes or unrelated private data.

These replays do not promote maturity.

### G7 — Fresh generalization H0 → H4

**H0 before implementation**

Freeze only:

- task families;
- coverage matrix;
- batch size = 8;
- locale balance;
- outcome classes;
- rubric;
- reviewer criteria.

Do not create/expose exact final holdout prompts.

Coverage must collectively include zh-Hans, zh-Hant-HK, CTA/action, state/help/error, landing/page rhythm, KEEP, CONTENT ARCHITECTURE escalation, PRODUCT SEMANTICS escalation and LEGAL/TRUST/SAFETY escalation. Natural scenarios may cover more than one dimension.

**H1 development**

Use known/synthetic/development evidence from G1–G6 only.

**H2 versioned final candidate**

After implementation and development evidence stabilize:

1. reread current version source/policy;
2. apply the approved version changes exactly once;
3. update changelogs/README/VERSION/tests/generated output;
4. regenerate;
5. freeze the exact versioned H2 candidate + reviewer criteria;
6. record final candidate identity;
7. directly rerun all release-critical G1–G6 on that exact H2 candidate.

If any exact-H2 G1–G6 gate fails, repair without another version bump, regenerate, freeze a new H2 candidate and rerun all release-critical G1–G6. Stay before H3 until one H2 candidate has complete PASS.

**H3 Planner-owned fresh batch**

Only after exact-H2 G1–G6 PASS:

- Executor transitions `EXECUTING -> NEEDS_GPT_PLANNER`;
- external Planner verifies H2 identity + H0 rubric;
- Planner writes exactly one repo-safe exact batch to:
  `results/product-ui-copy--cross-plugin-production-integration/fresh_holdout/final_holdout_batch.json`;
- Planner binds candidate/rubric/holdout identity in the task-local Plan;
- no production source changes;
- Planner transitions `NEEDS_GPT_PLANNER -> PLAN_FROZEN`;
- `plan_revision: 0 -> 1`.

No second automatic Planner revision remains.

**H4 one-shot**

Executor runs the complete H3 batch once on the unchanged H2 candidate.

No replacement, cherry-picking, prompt substitution, easy-case padding or production repair before verdict.

If H4 fails, preserve the batch; if used for repair it becomes known regression. No new fresh batch is allowed in this workflow without separate future authorization.

### G8 — Release / CI / README / independent review closure

Under unchanged baseline:

```text
Repository: 5.3.1 -> 5.4.0
web-development: 0.3 -> 0.4
writing-style: 0.3 -> 0.4
all other central plugins: NO_BUMP
maturity: unchanged / unclassified
```

After H4 PASS:

- `RESULT.md` must bind `implementation_commit` to the exact H2 candidate that passed release-critical G1–G6 and H4;
- transition to `WAITING_FOR_CI / ci_status=PENDING`;
- real GitHub CI must pass;
- independent Reviewer must inspect exact-H2 G1–G6 evidence, H4, real two-plugin consumption, screenshots, diff and release metadata;
- README/changelogs/VERSION/generated/version tests must agree;
- tracking closure must be truthful;
- user final acceptance is still required;
- main merge and release-ref movement require separate later authorization.

## Natural-language usage / routing expectations

Representative normal-use expectations:

- “这个设置页中文都能看懂，但读起来很像 AI，帮我把状态说明和按钮文案改自然。”  
  → Frontend Design classifies content architecture/UI role → Product UI Copy handles wording/locale → Frontend validates rendered page rhythm.

- “把这个浏览器插件 popup 的状态文案整理一下，别把内部工程词直接给用户。”  
  → Product-interface route; Mica-like browser-extension surface is a valid Frontend target.

- “这个 Tauri 桌面设置页的帮助说明太啰嗦，按钮关系也不清楚。”  
  → Frontend handles disclosure/layout; Product UI Copy handles natural wording; browser-only evidence cannot be mislabeled native if native behavior is claimed.

- “SeminarArc 列表页层级太平，主操作不突出，帮我规划 Compose UI 修复。”  
  → Frontend generic coordinator activates; SeminarArc `android-lead` / `compose-expert` keep implementation authority.

- “把 SeminarArc 的后台清理任务迁到 WorkManager，保持 Room 状态和 retry 语义，UI 不变。”  
  → Frontend Design must not activate.

- “把 README 这段中文写自然一点。”  
  → stays on `chinese-prose`, not Product UI Copy.

- “重新组织这份中文科研报告，但数字、公式、引用和结论强度不能变。”  
  → stays on `scientific-rewrite`, not Product UI Copy.

## Out of scope

Do not:

- redesign Product UI Copy Proposal v0.2;
- reopen Frontend Design 0.3 coordinator-first architecture or #52–#72;
- modify Bridge Kit, Host Policy or execpolicy;
- modify CUHK Date, Mica, Lucerna, SeminarArc, Bobbio or Asteria;
- implement consumer project-local hard bindings;
- create a new top-level plugin, orchestrator, dependency manager, schema, database, ledger or state machine;
- broadly implement writing-style #13 or unrelated writing-style TODOs;
- change scientific-rewrite/scientific-prose semantics without a direct regression requiring Planner review;
- use phrase blacklists, AI-detector evasion, deliberate errors/slang/random variation as naturalness mechanisms;
- promote either plugin maturity;
- enable paid Text Review, Visual Review or Terra without separate explicit authorization;
- create another fresh batch after H4 failure;
- create successor task;
- create another branch/worktree or second-bootstrap this task;
- merge `main`, move `release`, create a PR, publish/deploy, delete task branch/worktree, force-push, rebase published history, reset/clean/restore user work.

At central implementation/review completion, consumer hard bindings may remain outstanding; Maintenance Board should use `ADAPTING` rather than falsely declaring the whole cross-project adoption finished.
