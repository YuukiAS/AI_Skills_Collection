# Product UI Copy Cross-Plugin — Independent Critic Prompt v0.1

你是 `YuukiAS/AI_Skills_Collection` 的独立 Critic。

当前只审 Product UI Copy cross-plugin architecture Proposal，不实现，不创建 Executor Goal，不启动 Reviewed Handoff，不修改 production Skill，不修改 CUHK Date / Lucerna / Mica / Asteria / Bobbio / SeminarArc。

Frontend Design 0.3 已正式发布；本轮不是重新审它的 coordinator-first architecture。

---

## 1. Review object

Repository:

`YuukiAS/AI_Skills_Collection`

Proposal:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_1_2026-09-28.md`

Exact Proposal commit:

`d1b3a13435cb51e9503f9fe6cbfd1b4b064aadd1`

Planning source baseline:

`2eb66c4543b62214c47eca51832972cb7c50eb0c`

Current production baseline at planning time:

```text
repository = 5.3.1
web-development / Frontend Design = 0.3
writing-style / Clear Writing = 0.3
web-development maturity = unclassified
writing-style maturity = unclassified
```

Review stage:

`ARCHITECTURE / CROSS-PLUGIN OWNERSHIP`

Your verdict applies only to this Proposal. PASS does not authorize production implementation.

---

## 2. Required source reads

First read latest `main`:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

Then read the exact Proposal at commit `d1b3a13435cb51e9503f9fe6cbfd1b4b064aadd1`.

Read current relevant production/source evidence at least:

### Frontend Design

- `results/web-development--frontend-design-production-consolidation/FINAL_REPORT.md`
- `docs/plugin-changelogs/web-development.md`
- `docs/plugin-todos/web-development.md`
- `skills/tools/frontend/frontend-visual-systems/SKILL.md`
- `skills/tools/frontend/product-ux-planning/SKILL.md`
- `skills/tools/frontend/responsive-accessibility-review/SKILL.md`
- `scripts/codex_marketplace_config.json`

### Clear Writing

- `docs/plugin-todos/writing-style.md`
- `docs/plugin-changelogs/writing-style.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `skills/writing/core/chinese-prose/SKILL.md`
- `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`

### Product UI Copy evidence

- `docs/design/product-ui-copy/evidence/CUHK_DATE_PRODUCT_COPY_NATURALNESS_AUDIT_2026-09-26.md`

For tracking collision reality, independently inspect GitHub Issues #13, #17, #20 and #73.

For the proposed independent browser-extension replay, inspect current `YuukiAS/Mica-for-ChatGPT` main:

- `AGENTS.md`
- `extension/popup/index.html`
- `extension/popup/popup.ts`

For mobile surface-generalization, inspect current `YuukiAS/SeminarArc/AGENTS.md`.

Do not modify those consumer repositories.

---

## 3. External reality check

Do one targeted external verification of the Proposal's UI-writing/localization assumptions using current primary/official sources.

Suitable primary sources include:

- Apple Human Interface Guidelines / interface writing / localization
- GOV.UK Design System
- Microsoft Writing Style Guide / globalization guidance

The goal is to test the architecture assumptions, not copy a vendor brand voice.

Record briefly what you verified and whether it supports or contradicts the Proposal.

---

## 4. Architecture boundary under review

The Proposal freezes this three-owner model:

```text
Product/domain/legal authority
  owns product truth / policy / user consequence

Frontend Design
  owns content architecture:
  whether / where / role / amount / hierarchy / duplication /
  progressive disclosure / rendered acceptance

Clear Writing / Product UI Copy
  owns natural-language realization under frozen meaning:
  wording / locale / register / short-copy naturalness /
  first-pass linguistic page rhythm / fidelity escalation
```

Critic must test both directions:

1. Is any responsibility missing?
2. Is any responsibility duplicated so badly that two owners can issue contradictory final decisions?

Do not collapse the three owners merely for simplicity.

---

## 5. Dedicated Product UI Copy Skill decision

The Proposal compares:

### Option 1
Extend `chinese-prose`.

### Option 2
Add sibling:
`skills/writing/core/product-ui-copy/`

### Option 3
No new Skill; only a handoff mode using existing writing skills.

Planner recommends Option 2.

Review whether this recommendation is justified by **real capability boundaries**, especially:

- UI role/state/context is a different reasoning unit from long-form prose;
- trigger clarity;
- overlap risk;
- context budget;
- regression risk to `chinese-prose`;
- future English/other locale support;
- testability;
- cross-plugin routing.

Do not block merely because “fewer Skills is always simpler”.

Conversely, if current production source already supports this reliably without a new Skill, give direct evidence and explain why Option 2 would duplicate an existing owner.

---

## 6. Handoff contract

The Proposal recommends a lightweight conceptual structured block, not a new schema:

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

Optional:

```text
DESIGN_AUTHORITY
TERMINOLOGY_OR_BRAND_TOKENS
```

Review:

- Is every field materially useful?
- Is any important field missing?
- Is this light enough to remain a prompt/handoff convention rather than a new protocol?
- Can it distinguish rewrite vs shorten vs keep vs merge/delete recommendation vs escalation?
- Does it preserve S1 scale-down?

Do not demand a JSON schema unless there is a direct production reason.

---

## 7. Defect taxonomy

Review the six-class reasoning taxonomy:

- KEEP
- WORDING / NATURALNESS
- LOCALE / REGISTER
- CONTENT ARCHITECTURE
- PRODUCT SEMANTICS
- LEGAL / TRUST / SAFETY

Check:

- whether Writing can avoid rewriting semantic/legal problems;
- whether Frontend can avoid “fixing” every language problem by deleting text;
- whether KEEP is strong enough to stop gratuitous rewriting;
- whether the taxonomy overlaps improperly with P1/P2/P3 severity;
- whether any class needs a separate owner.

This taxonomy is intended as reasoning structure, not a machine enum/state system.

---

## 8. writing-fidelity boundary

Review whether the Proposal protects all product truths that must not drift, including:

- product state / availability
- eligibility
- verification meaning
- consent
- privacy/data collection/use/retention/deletion
- safety claims
- pricing/payment/subscription
- action consequence
- destructive/reversible status
- what other people/systems can see
- required legal/trust disclosure
- exact brand/product/technical tokens

Check the proposed deletion/move rule:

A protected proposition can disappear from one visible block only if Frontend confirms it is duplicated elsewhere or deliberately moved to an accepted disclosure path, and required product/legal authority permits that placement.

Does this prevent “naturalness” from hiding a product/legal defect without making every string immutable?

---

## 9. Page-level rhythm ownership

The Proposal deliberately uses two owners:

### Writing
First-pass **linguistic page rhythm**:
- repeated rhetoric
- repeated pronouns
- repeated reassurance
- repeated internal nouns
- sloganization
- role-inappropriate wording
- locale awkwardness

### Frontend
Final **rendered page/screen rhythm**:
- duplicate state across badge/heading/body/CTA
- viewport density
- wrap
- prominence
- CTA relationship
- layout/disclosure hierarchy
- final whole-product taste

Review whether this split is clear enough to avoid:

- two independent “final” owners;
- sentence-local polish without page context;
- Frontend duplicating locale/style rules;
- Writing making layout decisions it cannot see.

---

## 10. Chinese naturalness mechanism

The Proposal explicitly rejects phrase bans and AI detectors.

Review whether the mechanisms are sufficiently general:

- state/action/consequence-first where the UI role calls for it;
- restrained but not banned second person;
- accumulated rhetorical symmetry rather than phrase matching;
- ordinary state vs sloganization;
- internal noun → user-perceivable consequence when semantically safe;
- progressive disclosure for reassurance;
- fragment vs full sentence by UI role;
- standard action labels before decorative phrasing.

Use the CUHK Date evidence as known regression only. Do not turn exact CUHK Date phrases into universal banned tokens.

---

## 11. Locale contract

Review whether:

```text
one protected meaning
→ independent zh-Hans realization
→ independent zh-Hant-HK realization
```

is the correct production contract.

Check:

- neither locale is master wording for the other;
- no character-conversion acceptance;
- Mainland and Hong Kong product register can differ;
- protected meaning and legal/trust strength stay equivalent;
- rendered acceptance checks wrapping and CTA/layout consequences;
- exact product/technical tokens remain stable where needed.

A blocker requires a real semantic/localization gap, not a preference for one vocabulary table.

---

## 12. Frontend Design integration

Frontend Design 0.3 coordinator-first architecture is already accepted and released.

Review only whether Product UI Copy integrates cleanly:

```text
frontend-visual-systems coordinator
→ P0/P1 content architecture + UI role
→ conditional Clear Writing / product-ui-copy handoff
→ P2 implementation
→ P3 rendered copy acceptance
→ F-D admission
→ P4 whole-product taste
```

Do not reopen:

- coordinator-first
- S1/S2/S3 architecture
- F-A/F-B/F-C/F-D
- Figma/no-Figma
- browser/native evidence
- handoff-action reachability

Block only if the Product UI Copy integration contradicts those accepted semantics.

---

## 13. Surface-agnostic Frontend Design auto-trigger

This is an explicit user requirement and is part of the Proposal review.

The desired central trigger is **product-interface work**, not “web page work”.

Positive surfaces include:

- browser extension — Mica for ChatGPT
- browser/web — CUHK Date, Asteria
- desktop/Tauri/WebView — Bobbio, Lucerna
- mobile/Android/Compose — SeminarArc

Negative/non-trigger examples include:

- Mica content-script hot-path work with no UI change
- Lucerna runtime/provider diagnostics with no UI change
- SeminarArc Room/WorkManager/data-layer work with no UI change
- Asteria API/math-only work
- docs-only README edits

Review:

1. Can central plugin description/default prompts/Skill trigger boundaries/evals reasonably make this automatic without requiring the user to say “use Frontend Design”?
2. Is the trigger broad enough for desktop/mobile but narrow enough not to steal backend/runtime/domain work?
3. Does SeminarArc correctly retain `android-lead` / `compose-expert` platform ownership?
4. Is the Proposal correct that central discovery improvement is **not** the same as a hard per-repository binding?

Do not claim the named repos are already hard-bound.

---

## 14. Project-local binding distinction

The Proposal recommends a later minimal project binding for:

- Mica for ChatGPT
- CUHK Date
- Asteria
- Bobbio
- Lucerna
- SeminarArc

Concept:

> user-facing UI/Figma/visual/copy/interaction tasks use installed Frontend Design (`web-development`) as generic product-interface coordinator, while project-local platform/product skills and canonical sources remain higher authority.

Review whether this is the correct long-term strategy for “don't make the user remind the model every time”.

This Proposal does not authorize those repo changes now.

If Critic believes project-local binding is unnecessary, explain how current plugin discovery alone gives sufficiently reliable cross-surface routing and what evidence supports that claim.

---

## 15. Clear Writing routing / long-form protection

Review that Product UI Copy positive triggers include product interface:

- labels
- CTA
- status
- help
- empty/loading/error
- onboarding
- landing microcopy
- settings/support/privacy/trust surfaces
- “UI 中文不自然 / 都能读但有 AI 味”

And that it does not steal:

- Chinese research reports
- README long-form prose
- technical docs
- manuscripts
- advisor reports
- ordinary paragraph rewrite
- source-faithful scientific rewrite
- scientific/presentation-owned caption/slide prose

Existing routes should remain:

- `chinese-prose`
- `scientific-rewrite`
- `scientific-prose`
- `writing-fidelity`

Check whether the proposed negative-route boundary is enough to prevent regression.

---

## 16. #13 dependency decision

The Proposal says:

- writing-style #13 is reviewed as dependency only;
- current `writing-fidelity` / Clear Writing semantics already provide enough protected-language ownership;
- Product UI Copy does not require reopening the entire #13 generic language-layer promotion.

Review this specifically.

REVISE only if Product UI Copy cannot be implemented coherently without a concrete missing #13 capability. If so, name the exact missing seam and why it blocks Product UI Copy.

Do not broaden into #12/#14/#15/#16/#18/#19 without direct dependency evidence.

---

## 17. Evaluation design

Review all evidence classes separately.

### Known regression
CUHK Date 150-line audit:
- taxonomy calibration
- known replay
- KEEP/B/C/D behavior
- never fresh holdout
- no CUHK Date mutation

### Independent real-project replays
- Lucerna #17
- Mica browser-extension popup

Check whether Mica is a legitimate independent real-project replay and whether it adds independent value rather than duplicating CUHK Date.

### Fresh holdout
Must be frozen before implementation and include:

- zh-Hans
- zh-Hant-HK
- CTA
- state
- help
- empty/error
- privacy/trust
- landing
- repeated page rhythm
- already-natural KEEP controls
- content-architecture escalation
- product-semantics escalation
- legal/trust/safety escalation

The final batch cannot be adaptively replaced after failure.

### Independent review
Must include:

- routing/contract tests
- known regression
- unrelated Clear Writing regressions
- unrelated Frontend regressions
- independent real-project replay
- fresh holdout
- independent text/naturalness review
- rendered Frontend acceptance

Check that mechanical tests cannot stand in for naturalness or rendered UI quality.

---

## 18. Tracking collisions

Independently verify:

- Frontend Product UI Copy source currently says `tracking: #73`, but GitHub Issue #73 belongs to Statistical Modeling.
- writing-style Product UI Copy naturalness source currently says `tracking: #20`, but GitHub Issue #20 belongs to Research Authoring.
- writing-style #17 correctly maps to Issue #17.
- writing-style #13 correctly maps to Issue #13.

Review whether Proposal's plan is correct:

- path + exact heading remain canonical until repaired;
- unique issues should later be created/bound;
- no tracking collision should be silently reused;
- no TODO/Issue mutation occurs in this planning task.

Do not block solely because Project status could not be changed by the Planner surface; require exact pending mutation rather than false synchronization.

---

## 19. Version implications

Planning task itself must not bump anything.

Proposal recommends, if implemented and released under the current baseline:

```text
web-development: 0.3 -> 0.4
writing-style: 0.3 -> 0.4
all other central plugins: NO_BUMP
maturity: unchanged / unclassified
```

Review those plugin-version decisions under `PLUGIN_VERSIONING_AND_CHANGELOGS.md`.

Proposal also recommends:

```text
repository: 5.3.1 -> 5.4.0
Repository bump decision: MINOR
```

Reason given:

A new repository-level cross-plugin normal workflow would exist:

```text
Frontend content architecture
→ protected Product UI Copy handoff
→ locale-aware Clear Writing realization
→ rendered Frontend acceptance
```

Critic must independently decide whether this truly satisfies the policy's “previously absent repository-level user capability / multi-plugin workflow” test.

Do not choose PATCH merely because only two existing plugins change; do not choose MINOR merely because the change feels large. Apply the actual policy.

If you disagree, return the correct bump class and direct policy reasoning. Treat version classification as architecture-review scope because it determines later release closure, but do not mutate versions now.

---

## 20. Blocker standard

A blocker must identify a real execution/product risk such as:

- ownership gap/duplication that can produce contradictory outputs;
- new Skill duplicates existing production capability;
- handoff lacks information needed to preserve meaning;
- writing can still silently rewrite product/legal truth;
- page rhythm has no final owner;
- locale contract allows mechanical conversion or semantic drift;
- central trigger still excludes desktop/mobile/browser extension in normal use;
- project binding strategy would incorrectly override platform/domain authority;
- evaluation can PASS by rewriting every line or overfitting CUHK Date;
- fresh holdout is not actually fresh/frozen;
- release version class contradicts policy.

Non-blocking notes include:

- alternative field names;
- preference for JSON instead of lightweight structured text without a demonstrated need;
- adding more examples “for safety”;
- vendor-specific tone preference;
- unrelated TODO cleanup.

For every blocker give:

```text
FINDING_ID
Requirement
Direct evidence
Causal risk
Minimal closure condition
Owner
```

Do not move the goalposts across revisions. If you return REVISE, a later re-review should first check these exact blockers.

---

## 21. Required final output

Start with a concise Chinese assessment of:

1. ownership;
2. dedicated Skill choice;
3. handoff weight;
4. fidelity/product/legal boundary;
5. page rhythm;
6. locale;
7. cross-surface Frontend auto-trigger;
8. Clear Writing regression risk;
9. evaluation integrity;
10. version implications.

Then return exactly:

```text
RESULT = PASS | REVISE

REVIEWED_OBJECT = docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_1_2026-09-28.md
REVIEWED_COMMIT = d1b3a13435cb51e9503f9fe6cbfd1b4b064aadd1

FRONTEND_DESIGN_BASELINE = web-development 0.3
FRONTEND_DESIGN_ARCHITECTURE_REOPENED = NO

OWNERSHIP_MATRIX = PASS | REVISE
DEDICATED_PRODUCT_UI_COPY_SKILL = PASS | REVISE
HANDOFF_CONTRACT = PASS | REVISE
WRITING_FIDELITY_BOUNDARY = PASS | REVISE
PAGE_RHYTHM_OWNERSHIP = PASS | REVISE
LOCALE_CONTRACT = PASS | REVISE
SURFACE_AGNOSTIC_FRONTEND_TRIGGER = PASS | REVISE
PROJECT_BINDING_SEPARATION = PASS | REVISE
EVALUATION_PLAN = PASS | REVISE
TRACKING_COLLISION_PLAN = PASS | REVISE

PLANNED_PLUGIN_VERSIONS =
- web-development: 0.3 -> 0.4 | REVISE
- writing-style: 0.3 -> 0.4 | REVISE

PLANNED_REPOSITORY_BUMP = 5.3.1 -> 5.4.0 | PATCH_INSTEAD | REVISE
MATURITY_CHANGE = NONE

IMPLEMENTATION_AUTHORIZED = NO
NEXT_STEP = Planner execution-package design after Critic PASS
```

If REVISE, list only blockers supported by the blocker standard above.

If PASS, make explicit that this is architecture Proposal approval only. It does not authorize production edits, CUHK Date edits, consumer-repo binding edits, TODO closure, version bump, or Executor launch.
