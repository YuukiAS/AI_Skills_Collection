# Product UI Copy Cross-Plugin — Execution Plan v0.2

Date: 2026-09-28  
Status: `DRAFT_FOR_EXECUTION_READY_CRITIC_RE_REVIEW`  
Prior execution-ready review: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-28.md` @ `c1982a3ffddeafbc906087ff1da40e5bcfc43e46` — `REVISE / READY_FOR_CODEX=NO`  
Recovery scope: close only `PUC-ER-01` final-candidate chronology; all other v0.1 execution findings remain PASS.  
Repository: `YuukiAS/AI_Skills_Collection`  
Architecture authority: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md` @ `a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67`  
Architecture Critic PASS: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_REVIEW_V0_2_2026-09-28.md`  
Planning baseline: repository `5.3.1`, `web-development 0.3`, `writing-style 0.3`  
Implementation authorization: **NO — requires execution-ready Critic PASS + explicit user Kickoff**

## 1. Task identity and Bridge contract

Human label:

`Product UI Copy 跨插件生产整合`

Reviewed Handoff identity:

```text
task_key = product-ui-copy--cross-plugin-production-integration
branch = reviewed/product-ui-copy--cross-plugin-production-integration
expected canonical checkout = /home/yuukias/AI_Skills_Collection
expected Bridge-derived sibling worktree =
  /home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration
```

Current GitHub preflight found no existing remote branch matching this task key.

The worktree path above is an **execution precondition**, not a license to improvise another path. Current Bridge Kit first bootstrap derives:

`<repo-parent>/<repo-dir>-<task_key>`

and does not accept a caller-chosen worktree path.

Before bootstrap, Codex must verify that the actual canonical checkout on the execution machine is exactly:

`/home/yuukias/AI_Skills_Collection`

and that its `origin` is `YuukiAS/AI_Skills_Collection`.

If that execution-machine checkout path is different, stop before branch/worktree creation and return to Planner. Do not silently choose a different worktree, raw `git worktree add`, move an existing worktree, or edit Bridge Kit.

Bridge source checked for this Plan:

- `YuukiAS/GPT_Codex_AI_Bridge_Kit main @ f85622fd26fa1b8648d957e20b4f047a671e999f`
- current Reviewed Handoff requires `AI_BRIDGE_REVIEWED_PLAN_V2`;
- brand-new first bootstrap derives `reviewed/<task_key>` + sibling worktree;
- new task starts `PLAN_REQUESTED / RUN_GPT_PLANNER`;
- Executor starts only after Planner writes task-local V2 `PLAN.md` and freezes `PLAN_REQUESTED -> PLAN_FROZEN`;
- existing task recovery uses artifact-bound `materialize-worktree --mode resume`;
- initial freeze does not consume `plan_revision`;
- a later `NEEDS_GPT_PLANNER -> PLAN_FROZEN` consumes the single plan revision.

Do not modify Bridge Kit.

## 2. What this execution must add

This task implements one approved repository-level workflow:

```text
Frontend Design
  decides content architecture / UI role / amount / hierarchy
      ↓
protected lightweight handoff
      ↓
Clear Writing / product-ui-copy
  realizes natural locale-specific UI copy
      ↓
Frontend Design
  accepts the rendered page/screen
```

It also expands Frontend Design discovery from “web-like” to **product-interface** work across browser extension, web, desktop/WebView and mobile/Compose, without stealing backend/runtime/data/platform semantics.

The task does not redesign Frontend Design 0.3.

## 3. Frozen architecture decisions

Executor must not reinvent these decisions.

### 3.1 Three owners

Product/domain/legal authority owns:

- product truth;
- product state;
- eligibility;
- user consequence;
- consent/privacy/legal/safety/trust facts.

Frontend Design owns:

- whether a surface needs text;
- where text appears;
- UI role;
- amount and hierarchy;
- duplicate semantic payload;
- progressive disclosure;
- rendered page/screen acceptance;
- final rendered page rhythm.

Clear Writing / Product UI Copy owns:

- natural-language realization under frozen meaning;
- UI-role-aware short copy;
- locale/register;
- zh-Hans / zh-Hant-HK independent realization;
- first-pass linguistic page rhythm;
- fidelity-preserving escalation.

### 3.2 Dedicated sibling Skill

Create:

`skills/writing/core/product-ui-copy/`

It is a sibling inside Clear Writing, not a new central plugin.

Do not turn `chinese-prose` into the Product UI Copy engine.

### 3.3 Trigger metadata is production behavior

The new `product-ui-copy` frontmatter description must positively cover user-visible Product UI roles such as labels, CTA, status, help, empty/loading/error, onboarding, settings, trust/privacy, landing microcopy and locale-specific UI wording.

The existing `chinese-prose` **frontmatter description** must be narrowed so it still owns reports/README/technical docs/ordinary Chinese prose but explicitly excludes Product UI microcopy.

Do not rewrite its long-form mechanism beyond the narrow route seam.

Clear Writing plugin metadata must expose Product UI Copy in:

- plugin description;
- at least one default prompt;
- packaged Skill list.

### 3.4 Lightweight handoff only

Use a prompt-level structured handoff, not a new schema/database/state machine:

```text
SURFACE
UI_ROLE
PRODUCT_STATE
USER_JOB
USER_CONSEQUENCE_OR_NEXT_ACTION
NEIGHBORING_VISIBLE_COPY
LOCALE
PROTECTED_MEANING
DISCLOSURE_LEVEL
LENGTH_OR_VIEWPORT_CONSTRAINT
```

Optional when relevant:

```text
DESIGN_AUTHORITY
TERMINOLOGY_OR_BRAND_TOKENS
```

Writing may return `KEEP`, a wording candidate, locale note, page-rhythm note, architecture recommendation, or escalation.

Writing may recommend DELETE / MERGE / MOVE but Frontend decides the content-architecture change.

### 3.5 Reasoning taxonomy, not machine enum

Preserve:

- KEEP
- WORDING / NATURALNESS
- LOCALE / REGISTER
- CONTENT ARCHITECTURE
- PRODUCT SEMANTICS
- LEGAL / TRUST / SAFETY

Do not add a runtime enum/state machine just to encode this taxonomy.

### 3.6 Fidelity

`writing-fidelity` must gain only the narrow semantic handoff necessary for Product UI Copy.

Protected propositions include at least:

- product state/availability;
- eligibility;
- verification meaning;
- consent;
- privacy/data collection/use/retention/deletion;
- safety promises/limitations;
- pricing/payment/subscription;
- action consequence;
- reversibility/destructiveness;
- visibility to another person/system;
- required legal/trust disclosure;
- exact product/brand/technical identities.

Naturalness cannot silently delete or strengthen these facts.

### 3.7 Page rhythm

Writing owns first-pass **linguistic** rhythm.

Frontend owns final **rendered** rhythm.

No second final owner.

### 3.8 Locale

One protected meaning may produce independent `zh-Hans` and `zh-Hant-HK` realizations.

Do not use character conversion as localization acceptance.

### 3.9 Surface-agnostic Frontend trigger

Frontend Design normal discovery must include user-facing interface work for:

- browser extension;
- web;
- desktop/Tauri/Electron/native-WebView;
- Android/Compose/mobile.

It must not activate merely for:

- backend/API/math;
- runtime/provider/network;
- Room/WorkManager/data-layer;
- docs-only README;
- non-UI performance work.

SeminarArc's `android-lead` and `compose-expert` remain higher authority for Android/Compose implementation semantics after the generic Frontend coordinator has handled product-interface concerns.

### 3.10 Consumer bindings remain later work

Do not modify Mica, CUHK Date, Asteria, Bobbio, Lucerna or SeminarArc.

This release improves central discovery and proves compatibility. Project-local hard bindings are a separate later adaptation stage.

## 4. Allowed implementation surface

### 4.1 Clear Writing

Allowed:

- `skills/writing/core/product-ui-copy/**` — new Skill + evals/resources if needed;
- `skills/writing/core/writing-fidelity/SKILL.md` — narrow Product UI Copy semantic-fidelity handoff;
- `skills/writing/core/chinese-prose/SKILL.md` — frontmatter description narrowing + minimal matching body route note;
- directly necessary Clear Writing routing tests/fixtures;
- `scripts/codex_marketplace_config.json` for `writing-style` description/defaultPrompt/Skill packaging/version.

Do not change scientific-rewrite or scientific-prose semantics unless a direct regression proves the new routing accidentally broke them; if such a semantic change would be required, stop and return Planner rather than expanding scope.

### 4.2 Frontend Design

Allowed:

- `skills/tools/frontend/frontend-visual-systems/SKILL.md`;
- `skills/tools/frontend/product-ux-planning/SKILL.md`;
- `skills/tools/frontend/responsive-accessibility-review/SKILL.md`;
- directly necessary Frontend trigger/routing tests/fixtures;
- `scripts/codex_marketplace_config.json` for `web-development` description/defaultPrompt/version.

The existing coordinator-first aggregate topology stays unchanged unless a strictly mechanical packaging adjustment is necessary to expose approved source text; any semantic topology change returns to Planner.

### 4.3 Profiles

Review and modify only if required for the approved companion exposure:

- `profiles/codex-webdev.json`
- `profiles/frontend-research-product.json`

Do not invent a new dependency manager or a new top-level profile solely for Product UI Copy.

### 4.4 Candidate replay helper

Current `scripts/candidate_plugin_replay.py` supports one candidate plugin at a time.

A repository-level cross-plugin workflow cannot be proven by two disconnected single-plugin replays alone.

Preferred implementation:

- minimally extend the existing helper to support a **repeatable candidate plugin selection** in one isolated run;
- stage/install both `web-development@ai-skills-candidate` and `writing-style@ai-skills-candidate` from the same candidate commit;
- prove actual consumption of both candidate plugin paths in one normal-entry run;
- remove both candidate identities afterward;
- prove same-name production installs remain unchanged;
- preserve current single-plugin CLI behavior and current Frontend 0.3 replay regressions.

If the current helper already has an equivalent supported multi-plugin route at execution time, use it instead of changing the helper.

Do not create a second replay framework.

### 4.5 Generated layer

Generated only through existing generators:

- `.agents/plugins/marketplace.json`
- `plugins/codex/plugins/**`
- registry/catalog generated outputs as normally required.

Do not hand-edit generated payload.

### 4.6 Evidence / closure

Use:

`results/product-ui-copy--cross-plugin-production-integration/**`

for:

- H0 coverage/rubric;
- activation routing evidence;
- known regressions;
- real-project replays;
- rendered acceptance;
- final candidate identity;
- H3/H4 holdout;
- validation;
- independent-review support;
- final report.

Release closure may also update:

- `docs/plugin-todos/web-development.md`
- `docs/plugin-todos/writing-style.md`
- `docs/plugin-changelogs/web-development.md`
- `docs/plugin-changelogs/writing-style.md`
- `CHANGELOG.md`
- `README.md`
- `VERSION`
- version/parity tests.

## 5. Forbidden scope

Do not:

- modify Bridge Kit;
- modify Host Policy / execpolicy;
- modify CUHK Date;
- modify Mica for ChatGPT;
- modify Lucerna;
- modify SeminarArc;
- modify Bobbio;
- modify Asteria;
- create a new top-level plugin;
- create a new orchestrator Skill;
- create schema/database/ledger/state machine for Product UI Copy;
- reopen Frontend Design 0.3 coordinator-first architecture;
- reopen #52–#72;
- broadly implement writing-style #13;
- pull in unrelated writing-style TODOs;
- create AI-detector evasion or phrase-ban logic;
- add deliberate errors/slang/random “humanization”;
- create a fourth/fifth real-project replay merely for maturity;
- promote maturity;
- run paid Text Review / Visual Review / Terra without separate explicit user authorization;
- modify consumer-repo project bindings in this task;
- merge to `main` or move `release` without later explicit integration authorization;
- create successor tasks;
- force push, rebase published history, reset/clean user work, delete branches/worktrees.

## 6. Capability Gate Matrix

All release-critical evidence must bind to the same final candidate production source commit unless a gate explicitly concerns a later control/evidence-only commit.

**v0.2 chronology clarification:** any G1–G6 results collected before version bump/regeneration are development evidence only. They may guide implementation, but they do **not** count as release-critical PASS. After version bump + regenerate, the exact versioned H2 candidate must directly rerun and PASS every G1–G6 gate marked `Final candidate = YES` before H3 fresh-holdout freeze may begin.

### G1 — Discovery / activation / packaging

**Capability / claim**

Users can naturally discover the right owner:

- Product UI Copy requests select `product-ui-copy`;
- long-form Chinese stays on `chinese-prose`;
- heavy scientific rewrite stays on `scientific-rewrite`;
- Frontend UI work activates across browser extension/web/desktop/mobile;
- backend/runtime/data/docs negatives do not misroute.

**Why distinct**

This proves normal-entry discovery, not copy quality.

**Evidence**

- new `product-ui-copy` frontmatter;
- narrowed `chinese-prose` frontmatter;
- Clear Writing plugin description/default prompt/package;
- Frontend Design plugin/Skill metadata;
- direct/indirect/near-miss/negative eval set;
- actual selected Skill/plugin identity in candidate replay;
- generated package parity.

**Failure**

Any required positive route misses, a negative route activates incorrectly, or correct text is produced through the wrong route.

**Regression boundary**

Existing reports, README, scientific rewrite and Frontend 0.3 normal routing remain valid.

**Final candidate**

YES.

### G2 — Ownership / handoff / protected meaning

**Capability / claim**

Frontend → Product UI Copy handoff preserves product truth and owner boundaries.

**Why distinct**

Correct routing can still produce a semantically unsafe rewrite.

**Evidence**

Representative scenarios covering:

- KEEP;
- wording;
- locale;
- content architecture;
- product semantics;
- legal/trust/safety;
- protected proposition move/delete rules;
- S1 lightweight path;
- S2 bounded cluster;
- S3 copy-heavy page.

The candidate must output owner, classification, protected meaning, allowed rewrite/action and escalation where required.

**Failure**

Writing invents/fixes product/legal semantics, Frontend becomes wording owner, or protected meaning drifts.

**Regression boundary**

Current `writing-fidelity` non-UI behavior remains unchanged.

**Final candidate**

YES.

### G3 — Product UI Copy naturalness / locale / page rhythm

**Capability / claim**

The language layer can improve Product UI Copy without over-rewriting.

**Why distinct**

Semantic safety alone does not prove natural, locale-appropriate UI language.

**Evidence**

Development evidence before H2:

- CUHK Date 150-line **known regression** only;
- Lucerna #17 known real regression;
- Mica popup read-only cases;
- already-natural `KEEP` controls;
- independent zh-Hans / zh-Hant-HK realizations;
- page-set review for repeated pronouns/rhetoric/reassurance/internal nouns/sloganization.

Independent qualitative review must judge actual candidate outputs, not keyword counts.

**Failure**

Mechanically converted locale, rewrite-everything behavior, phrase-ban behavior, semantic weakening, or page-level modelish rhythm survives.

**Regression boundary**

No long-form Clear Writing regression.

**Final candidate**

YES for final candidate outputs; CUHK known cases remain known evidence.

### G4 — Frontend rendered acceptance

**Capability / claim**

Copy decisions survive actual layout/render constraints.

**Why distinct**

Natural strings can fail when rendered due to duplication, wrapping, prominence or CTA displacement.

**Evidence**

Repo-safe representative rendered page/screen contexts covering at least:

- desktop/wide;
- mobile/narrow;
- multi-block page rhythm;
- one trust/help disclosure case;
- one already-good copy control.

The evidence must include actual rendered artifacts/screenshots plus the exact copy source and viewport.

This gate proves rendered copy/layout interaction only. It does not claim native platform behavior where only browser-based fixtures were rendered.

**Failure**

Repeated semantic payload, awkward wrap, hidden/displaced primary action, over-promoted reassurance, or mismatch between copy and control remains.

**Regression boundary**

Frontend 0.3 S1/S2/S3, Figma/no-Figma and browser/native evidence boundaries remain intact.

**Final candidate**

YES.

### G5 — Should-not-change regression

**Capability / claim**

The cross-plugin change does not damage existing Frontend or Clear Writing behavior.

**Why distinct**

Shared routing metadata, Marketplace config, profiles and replay helper have broad blast radius.

**Evidence**

At minimum:

- existing Clear Writing Chinese report/README route;
- existing scientific-rewrite route;
- existing English scientific-prose route;
- writing-fidelity-only route;
- Frontend 0.3 coordinator-first regressions;
- S1 local repair;
- S3 redesign;
- Figma/no-Figma;
- browser/native evidence boundary;
- shared Marketplace generator/parity;
- candidate replay helper single-plugin backward compatibility if helper changes;
- full repository unittest suite.

**Failure**

Unrelated route changes, generated drift, old helper broken, or existing accepted capability regresses.

**Final candidate**

YES for release-critical regressions.

### G6 — Same-session cross-plugin normal entry + real-project compatibility

**Capability / claim**

The repository-level workflow actually works through normal installed candidate identities.

**Why distinct**

Source contracts or separate single-plugin replays cannot prove the new cross-plugin workflow.

**Evidence**

One same-session candidate runtime must install/enable both candidate plugins from the same candidate commit and prove actual consumption of both:

`web-development@ai-skills-candidate`

and

`writing-style@ai-skills-candidate`.

Required normal-entry replay families:

1. generic Product UI Copy task:
   Frontend content architecture → protected handoff → Product UI Copy → returned wording → Frontend rendered acceptance criteria;
2. Lucerna read-only desktop/native-WebView compatibility;
3. Mica read-only browser-extension compatibility;
4. SeminarArc read-only mobile/Compose positive;
5. SeminarArc Room/WorkManager/data-only negative.

Neutral prompts must not name expected plugin/Skill routing.

For real-project source transmission, only the frozen minimal source set needed for the replay may be used, read-only, for this compatibility purpose. The later user Kickoff must explicitly authorize this bounded replay transmission.

SeminarArc positive must preserve `android-lead` / `compose-expert` platform ownership.

**Failure**

Only one candidate plugin is consumed, mobile UI misses Frontend, data-only work activates Frontend, or generic Frontend overrides project platform/domain authority.

**Regression boundary**

No consumer repository writes.

**Final candidate**

YES.

Maturity credit:

NO. These real-project replays prove compatibility/discovery only.

### G7 — Fresh generalization H0 → H4

**Capability / claim**

The release is not tuned only to known Product UI Copy cases.

**Why distinct**

Known regressions and real-project replays are visible during development.

**H0 — before implementation**

Freeze only:

- task families;
- coverage matrix;
- batch size;
- locale balance;
- outcome classes;
- rubric;
- reviewer criteria.

Exact final holdout text must not be present in Executor-visible source.

Recommended bounded batch size: **8 scenarios** because the batch must cover two locales, KEEP, wording, page rhythm and three escalation families without turning the final gate into a large benchmark.

Coverage must collectively include:

- zh-Hans;
- zh-Hant-HK;
- CTA/action;
- state/help/error;
- landing/page rhythm;
- already-natural KEEP;
- CONTENT ARCHITECTURE escalation;
- PRODUCT SEMANTICS escalation;
- LEGAL/TRUST/SAFETY escalation.

Do not force every scenario to cover a unique category if a natural scenario covers multiple dimensions.

**H1 — development**

Use only known/synthetic/development evidence from G1–G6.

**H2 — versioned final candidate freeze + mandatory same-candidate release rerun**

After implementation + known regressions + rendered acceptance are stable:

1. apply the release metadata once;
2. regenerate packaged plugins / Marketplace;
3. freeze the exact versioned H2 candidate commit;
4. freeze reviewer criteria;
5. prohibit production tuning while testing that H2 candidate;
6. directly rerun every release-critical G1–G6 gate marked `Final candidate = YES` on that exact H2 candidate;
7. enter H3 only after one exact H2 candidate has complete G1–G6 PASS.

If any H2 G1–G6 gate fails, repair the same selected release version, freeze a new H2 candidate, and rerun all release-critical G1–G6 before H3. Pre-H2 G1–G6 are development evidence only and cannot be spliced into release PASS.

**H3 — independent exact holdout freeze**

Executor transitions to `NEEDS_GPT_PLANNER`.

This is the one intentional scheduled Planner revision in this task.

The external Planner:

- verifies H2 candidate identity and H0 rubric;
- writes one exact repo-safe holdout batch under:
  `results/product-ui-copy--cross-plugin-production-integration/fresh_holdout/final_holdout_batch.json`;
- records exact rubric binding;
- does not change production code;
- updates task-local `PLAN.md` only to bind the exact holdout locator/candidate identity;
- returns `NEEDS_GPT_PLANNER -> PLAN_FROZEN`.

This consumes `plan_revision: 0 -> 1`.

No second automatic Planner revision remains for holdout chasing.

**H4 — one-shot evaluation**

Executor runs the complete H3 batch once against the same H2 candidate.

No replacement, cherry-picking, prompt substitution, easy-case padding or candidate modification is allowed before the release verdict.

If H4 fails:

- preserve the failed batch;
- it becomes known regression if used for repair;
- do not generate a new fresh batch automatically;
- do not claim release readiness;
- route back to Planner/human according to the exhausted plan-revision budget.

A new fresh batch requires a separately authorized future evaluation round after a new candidate freeze.

**Final candidate**

YES — H4 must use H2 unchanged candidate.

### G8 — Release / CI / README / review closure

**Capability / claim**

The same final candidate is a coherent formal repository release.

**Evidence**

If baseline remains:

```text
Repository: 5.3.1 -> 5.4.0
web-development: 0.3 -> 0.4
writing-style: 0.3 -> 0.4
all other central plugins: NO_BUMP
maturity: unchanged / unclassified
```

If another formal release advances `main` before bootstrap/integration, version arithmetic must be recomputed from then-current canonical source while preserving:

- both affected plugins advance exactly once;
- repository release class remains MINOR if the approved cross-plugin workflow is still the released capability;
- no `NO_BUMP` path for completed changed production behavior.

Required closure:

- both plugin changelogs;
- root CHANGELOG;
- README human-facing capability/version update;
- VERSION / registry / Marketplace / generated manifests / version tests;
- TODO resolution only after real implementation/replay/review;
- full required GitHub CI;
- independent Reviewed Handoff Reviewer PASS;
- user final human acceptance;
- later separately authorized integration to `main` + release ref.

**Failure**

Version drift, README stale, TODO closed early, CI missing, review using stale candidate, or main/release mutation without authorization.

**Final candidate**

YES.

## 7. Development chronology

### Phase A — bootstrap and Planner transaction

Only after execution-ready Critic PASS and user sends the approved Kickoff:

1. on canonical checkout, verify exact repo/path and clean state;
2. `git fetch --all --prune`;
3. resolve post-sync `origin/main` OID;
4. confirm no existing task branch/worktree;
5. run current Bridge first bootstrap with:
   - task key above;
   - expected repo `YuukiAS/AI_Skills_Collection`;
   - expected base commit = post-sync `origin/main`;
   - `--ci-required`;
   - **do not enable paid Text Review / Visual Review flags** under this package;
6. first bootstrap must create the exact sibling worktree;
7. publish only task bootstrap metadata if needed;
8. task remains `PLAN_REQUESTED / RUN_GPT_PLANNER`;
9. GPT Planner writes task-local `AI_BRIDGE_REVIEWED_PLAN_V2` from this execution package and durable execution-ready Critic PASS;
10. Planner freezes `PLAN_REQUESTED -> PLAN_FROZEN` with `plan_revision=0`;
11. Executor may then begin.

No second bootstrap.

### Phase B — H0 + implementation

Before production edits, write H0 coverage/rubric only.

Then implement:

- Product UI Copy sibling;
- trigger metadata separation;
- Clear Writing packaging;
- Frontend surface-agnostic discovery;
- content-architecture/handoff/rendered-acceptance contracts;
- tests;
- minimal profile changes if needed;
- minimal multi-plugin candidate replay helper extension if required.

Use:

`workflow-core + ai-skills-core + web-development + writing-style`

with target-domain decisions remaining with Frontend/Clear Writing.

### Phase C — cheap deterministic / known regressions

Run focused tests first.

Then development replays:

- CUHK Date known audit;
- Lucerna known/read-only;
- Mica read-only;
- SeminarArc read-only positive/negative;
- unrelated Clear Writing routes;
- Frontend 0.3 regressions.

Do not call these fresh.

### Phase D — rendered acceptance

Generate representative repo-safe UI fixtures and actual renders/screenshots for G4.

The independent reviewer must be able to inspect the actual images. If the available Reviewer surface cannot access the images, fail closed and return the evidence-access problem. Do not substitute filenames, OCR summaries or Executor prose for visual inspection.

This package does not authorize paid Visual Review.

### Phase E — broad repository validation

Run at least the canonical release validation appropriate to changed surfaces:

```text
python scripts/skills.py registry --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/skills.py catalog --write
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest discover -s tests
```

Also run focused tests for:

- Product UI Copy routing;
- Frontend trigger routing;
- candidate multi-plugin replay helper if changed;
- version/parity rules.

### Phase F — version closure, H2 freeze, and same-candidate G1–G6 release rerun

After **development** G1–G6 evidence and rendered acceptance are stable:

1. reread current version policy and current release source;
2. apply the approved repository/plugin version changes exactly once;
3. update changelogs / README / VERSION / tests / generated output;
4. regenerate the packaged plugins and Marketplace layer;
5. run version/parity validation;
6. freeze the exact **versioned H2 final candidate commit** and reviewer rubric;
7. record `final_candidate_identity.json`;
8. prohibit production-source changes while testing that H2 candidate.

Now rerun **all release-critical G1–G6 gates marked `Final candidate = YES` directly on this exact H2 candidate**, including:

- final packaged/installed discovery + Skill activation for G1;
- protected-meaning / ownership scenarios for G2;
- final-candidate naturalness / locale / linguistic page-rhythm outputs for G3;
- actual rendered acceptance bound to H2 for G4;
- should-not-change regressions and helper/generator compatibility for G5;
- same-session two-plugin candidate consumption plus Lucerna/Mica/SeminarArc compatibility for G6.

Pre-H2 G1–G6 evidence is retained only as development history and cannot be counted toward release PASS.

If any H2 G1–G6 release-critical gate fails:

- repair the candidate **without another version bump**;
- keep the already selected release versions;
- freeze a new H2 candidate commit after the repair;
- rerun **all** release-critical G1–G6 on that new H2 candidate;
- do not enter H3 until one exact H2 candidate has G1–G6 fully PASS.

This repair loop may repeat only within ordinary Executor/review budget and must not consume or expose the fresh H3 batch. Any failure that requires architecture/scope change returns to Planner/Critic.

Only after the exact versioned H2 candidate has direct G1–G6 PASS may the task proceed to H3.

### Phase G — H3 scheduled Planner revision

Executor stops at `NEEDS_GPT_PLANNER` **only after the exact H2 candidate has direct G1–G6 release-critical PASS**.

Planner freezes exact final holdout batch and candidate binding, then performs the one allowed revised freeze:

`NEEDS_GPT_PLANNER -> PLAN_FROZEN`

with:

`plan_revision = 1`

No architecture redesign and no production-source change.

### Phase H — H4 + final evidence

Executor evaluates the complete batch once on the unchanged H2 candidate that already passed release-critical G1–G6.

If PASS:

- record full outputs and adjudication;
- rerun only deterministic integrity checks needed to prove candidate/source unchanged;
- do not edit production source.

If FAIL:

- preserve failure;
- no new holdout batch;
- do not continue toward release PASS.

### Phase I — CI and independent Reviewer

After H4 PASS:

- write `RESULT.md`;
- bind `implementation_commit` to the exact H2 candidate that already passed release-critical G1–G6 and then H4;
- enter `WAITING_FOR_CI / ci_status=PENDING`;
- publish exact reviewed branch through normal authorized publisher;
- real GitHub CI must PASS;
- Scheduled GPT Reviewer reads:
  - frozen task-local Plan;
  - diff;
  - exact-H2 G1–G6 release-critical evidence plus G7/H4 and G8 closure evidence;
  - H4 batch/output;
  - rendered screenshots;
  - release/version/README/TODO state.

Reviewer PASS requires current implementation commit/candidate identity and cannot rely on stale review.

No paid Text/Visual Review is enabled by this task. If Reviewer cannot perform the required qualitative inspection from repository evidence, return a blocker requiring a separately authorized review route.

### Phase J — human acceptance and later integration

Reviewer PASS leads to human gate.

This execution package does not authorize:

- merge to `main`;
- moving `release`;
- deleting reviewed branch/worktree;
- consumer-repo bindings.

Those require later explicit authorization.

## 8. Candidate replay and evidence integrity

### 8.1 Same-session two-plugin proof

A cross-plugin release cannot claim success unless one runtime proves both candidate plugins were actually consumed.

Required receipt fields:

```text
CANDIDATE_COMMIT
WEB_DEVELOPMENT_PLUGIN_ID
WRITING_STYLE_PLUGIN_ID
WEB_DEVELOPMENT_INSTALLED_PATH
WRITING_STYLE_INSTALLED_PATH
WEB_DEVELOPMENT_CONSUMPTION_EVENT
WRITING_STYLE_CONSUMPTION_EVENT
INPUT_IDENTITY
OUTPUT_IDENTITY
PRODUCTION_INSTALLS_UNCHANGED
```

Do not infer cross-plugin consumption from output wording.

### 8.2 Real-project replay source

Freeze exact read-only source locators before final replay.

Do not copy more project source than needed.

Do not mutate target repos.

Any external/source transmission beyond the local execution boundary must be covered by the user's later approved Kickoff. Do not silently broaden to private unrelated data.

### 8.3 No maturity inflation

Lucerna/Mica/SeminarArc compatibility and one fresh holdout release do not justify maturity promotion.

Both affected plugins remain `unclassified`.

## 9. Independent qualitative review

Mechanical tests are necessary but insufficient.

The independent Reviewer must directly judge:

- naturalness;
- KEEP behavior;
- locale fit;
- protected-meaning fidelity;
- architecture vs wording escalation;
- product/legal/trust refusal/escalation;
- page rhythm;
- rendered hierarchy/wrap/CTA relationship;
- cross-surface trigger behavior;
- platform-owner preservation.

No detector score or banned-token scan can substitute.

## 10. Maintenance Board and tracking collisions

Architecture PASS confirmed the tracking plan.

This execution task must not reuse collided Issues:

- Frontend Product UI Copy currently points to unrelated #73;
- writing-style Product UI Copy naturalness currently points to unrelated #20.

Before final closure:

- create/bind a unique Frontend Product UI Copy tracking Issue;
- create/bind a unique writing-style Product UI Copy naturalness tracking Issue;
- preserve Issue #17;
- keep Issue #13 dependency-only;
- update canonical source `tracking: #N` values;
- Project status should be `DOING` during implementation and `ADAPTING` if consumer binding remains outstanding after central release;
- final `DONE` requires board policy closure, not only code PASS.

Any reader-facing Issue/Project mutation must use installed Clear Writing first.

If the current Executor surface cannot modify GitHub Project fields, write exact pending mutations for the Project-capable maintainer; do not ask the user to drag cards manually and do not claim sync.

## 11. Version contract

Planning decision is frozen:

```text
Repository bump decision: MINOR
Current baseline: 5.3.1
Expected release if unchanged: 5.4.0

Affected plugins:
- web-development: 0.3 -> 0.4
- writing-style: 0.3 -> 0.4
- all other central plugins: NO_BUMP

Maturity:
- web-development: unclassified
- writing-style: unclassified
```

Why MINOR:

After release, AI_Skills_Collection can complete a normal cross-plugin Product UI Copy workflow that 5.3.1 cannot complete:

`Frontend content architecture -> protected language handoff -> locale-aware Product UI Copy -> rendered Frontend acceptance`.

This matches the current version policy's explicit multi-plugin new-workflow case.

Do not bump during planning/bootstrap.

Do not bump early during implementation.

Do not bump twice after a repair.

The version bump/regeneration is part of the final candidate identity. Therefore:
- pre-version G1–G6 may only be development evidence;
- after the one version bump + regenerate, freeze H2;
- exact H2 must directly PASS release-critical G1–G6 before H3;
- if repaired, keep the same selected release versions, freeze a new H2 commit, and rerun release-critical G1–G6;
- never splice pre-H2 G1–G6 PASS with post-H2 H4/CI evidence.

## 12. Durable execution-ready Critic re-review

The next Critic re-review must write its actual result to:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md`

That artifact must bind:

- reviewed package version;
- Plan;
- Goal;
- Kickoff;
- package commit;
- task_key;
- exact branch;
- expected exact sibling worktree;
- Proposal v0.2 authority;
- architecture Critic PASS;
- execution-ready verdict;
- `READY_FOR_CODEX`.

Planner must not pre-fill a PASS.

## 13. Stop conditions

Return to Planner/Critic instead of expanding if implementation would require:

- a new cross-plugin dependency manager;
- a new workflow/state machine;
- changing Frontend coordinator topology;
- changing product/legal ownership;
- broad Clear Writing #13 work;
- consumer-repo mutation;
- paid review not yet authorized;
- a new fresh batch after H4 failure;
- a different branch/worktree than the frozen task identity;
- another formal release advancing main in a way that invalidates the version/workflow assumptions rather than merely requiring version arithmetic refresh;
- inability to prove both candidate plugins were actually consumed in one normal-entry runtime.

## 14. Completion claim

Before integration, maximum allowed claim is:

> The reviewed candidate implements the approved Product UI Copy cross-plugin workflow and passes the frozen release gates on the reviewed task branch.

Do not claim:

- repository 5.4.0 is released before integration;
- the six consumer repos are hard-bound;
- either plugin is baseline/alpha/stable;
- all future desktop/mobile/web products are proven;
- Product UI Copy can safely resolve unresolved product/legal semantics.

Overall repository/user-facing completion requires later human acceptance plus separately authorized integration/release closure.
