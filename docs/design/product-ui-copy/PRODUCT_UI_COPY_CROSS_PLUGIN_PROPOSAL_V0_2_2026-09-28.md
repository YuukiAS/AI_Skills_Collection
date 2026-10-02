# Product UI Copy Cross-Plugin Proposal v0.2

Date: 2026-09-28  
Status: `DRAFT_FOR_INDEPENDENT_CRITIC_RE_REVIEW`  
Repository: `YuukiAS/AI_Skills_Collection`  
Planning source baseline: `82b53a3468d483f4cba0fefbd99cd50e726c8683`  
Prior Proposal: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_1_2026-09-28.md` @ `d1b3a13435cb51e9503f9fe6cbfd1b4b064aadd1`  
Independent Critic review archive: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_REVIEW_V0_1_2026-09-28.md` @ `386856ddbb60a6cc5d7bc4492554d001425b29f1`  
Scope: `web-development / Frontend Design 0.3` + `writing-style / Clear Writing 0.3`  
Planning only: **no production Skill change, no CUHK Date mutation, no Executor Goal, no version bump**

---

## 0. v0.1 Critic disposition

The independent Critic returned `REVISE` with exactly three blockers. This v0.2 accepts all three.

| Finding | Planner disposition | v0.2 closure |
|---|---|---|
| `PUC-C01 Clear Writing trigger metadata conflict` | **ACCEPT** | Freeze frontmatter trigger changes for both `product-ui-copy` and `chinese-prose`; add activation competition evals; require plugin-level Clear Writing discovery metadata review/update. |
| `PUC-C02 Fresh holdout visible before candidate freeze` | **ACCEPT** | Pre-implementation freezes only task families/coverage/rubric. Exact final holdout becomes visible only after final candidate + review criteria freeze, then runs once without adaptive replacement. |
| `PUC-C03 Mobile/Compose lacks real normal-entry replay` | **ACCEPT** | Add read-only SeminarArc final-candidate normal-entry replay with one natural Compose/UI positive and one Room/WorkManager/data-only negative control; preserve `android-lead` / `compose-expert` authority. |

The Critic already passed ownership, handoff weight, fidelity boundary, page-rhythm ownership, locale contract, project-binding separation, tracking-collision plan and version direction. v0.2 does not reopen those decisions.

## 1. Current reality

Frontend Design 0.3 is already a real coordinator-first production entry. It owns S1/S2/S3 scale, design-authority selection, browser/native evidence boundaries, producer self-QA, handoff action reachability, and whole-product rendered acceptance. It is not being reopened.

Clear Writing 0.3 already has a strong content-preserving language layer:

- `writing-fidelity` protects facts, labels, claims, equations, citations, versions and artifact identity;
- `chinese-prose` handles natural Chinese for reports, README, technical documents and reader-facing long/paragraph prose;
- `scientific-rewrite` handles source-faithful structural scientific/technical rewrites;
- `scientific-prose` handles English scientific prose.

The missing capability is a different unit of work: **UI copy is not just a sentence; it is language inside a specific rendered product state, role, hierarchy and neighboring-copy context**.

Current production versions at the planning baseline:

```text
AI_Skills_Collection = 5.3.1
web-development / Frontend Design = 0.3
writing-style / Clear Writing = 0.3
web-development maturity = unclassified
writing-style maturity = unclassified
```

The CUHK Date audit is strong known-regression evidence, but it is not an unseen holdout. The exact 150-line audit found:

```text
A / natural = 53
B / readable-but-modelish = 72
C / clearly unnatural = 15
D / product-semantic/trust problem = 10
```

The dominant failure is not grammar. It is ownership failure across content architecture, product semantics, locale realization and page-level rhythm.

---

## 2. Exact scoped TODOs and durable locators

### Frontend Design

Canonical locator:

`docs/plugin-todos/web-development.md`

Heading:

`Product UI copy needs an explicit Frontend Design content-architecture contract`

The current source line `tracking: #73` is **not a valid durable identity**. GitHub Issue #73 belongs to Statistical Modeling: `Delegate reader-facing wording without giving away statistical semantics`.

Until AI Skills Maintainer creates/rebinds a unique tracking issue, use **file path + exact heading** as the canonical identity.

### Clear Writing #17

Canonical source:

`docs/plugin-todos/writing-style.md`

Heading:

`Product UI microcopy should state user consequence, not internal implementation reassurance`

GitHub Issue #17 is valid and matches this TODO.

### Clear Writing #20

Canonical source:

`docs/plugin-todos/writing-style.md`

Heading:

`Product UI copy naturalness needs a dedicated microcopy capability, not more long-form prose rules`

Important new reality check: the current source says `tracking: #20`, but GitHub Issue #20 is a **Research Authoring** issue about academic document identity. Therefore #20 is also a tracking collision. Do not use GitHub Issue #20 as this Product UI Copy item's identity. Use file path + heading until a unique issue is created/rebound.

### Clear Writing #13 — dependency only

Canonical source:

`docs/plugin-todos/writing-style.md`

Heading:

`Promote writing-style into the generic content-preserving language layer`

GitHub Issue #13 is valid.

Disposition in this task:

`REVIEWED_AS_DEPENDENCY_ONLY`

The existing language/fidelity ownership is sufficient for Product UI Copy. This task does **not** need to reopen the entire #13 promotion. It needs only a narrow routing seam from `writing-fidelity` / Clear Writing into the Product UI Copy capability.

---

## 3. Evidence summary

### Known regression: CUHK Date

Use:

`docs/design/product-ui-copy/evidence/CUHK_DATE_PRODUCT_COPY_NATURALNESS_AUDIT_2026-09-26.md`

This evidence establishes recurring generic failure modes:

- product self-definition before current user state/action;
- unnecessary repeated explicit second person;
- accumulated balanced rhetoric such as `不是 X，而是 Y`, `只有 X，才 Y`, `先 X，再 Y`;
- ordinary state sloganization;
- internal product/engineering/legal nouns leaking into consumer UI;
- over-complete reassurance;
- mechanical zh-Hans / zh-Hant-HK realization;
- individually readable strings producing modelish whole-page rhythm;
- product/legal/trust problems that cannot be fixed by wording polish.

It is a known replay and taxonomy calibration source only. This AI_Skills task must not modify CUHK Date production.

### Independent real-project evidence: Lucerna

Use Clear Writing #17 / Lucerna 01050 as an independent real-project regression:

- normal UI exposed implementation reassurance and maintenance detail;
- the user-facing question was simpler: current state, consequence and next action;
- Frontend Design owns disclosure/placement/hierarchy;
- the language layer should not narrate internal policy merely because it is technically correct.

### Additional independent real-project replay: Mica for ChatGPT

Mica is a suitable second independent read-only replay because it is a real **browser extension**, not another web landing page or desktop tray app.

Current popup source at `YuukiAS/Mica-for-ChatGPT` main includes real strings such as:

- `Long-thread optimization`
- `Stale clear recovery`
- `Connector continuity`
- `Send residual recovery`
- `Recent turns kept native`
- diagnostic/action labels and status messages.

These are useful to test whether Product UI Copy can distinguish:

- legitimate advanced/diagnostic language;
- implementation nouns that should remain behind diagnostic surfaces;
- user-facing feature labels that may need consequence-first wording;
- copy that is already acceptable and should stay unchanged.

Mica remains read-only evidence. This proposal does not authorize any Mica modification.

### Surface-generalization requirement

The user has made a durable product requirement explicit:

> Frontend Design must not be treated as “web pages only”. User-facing UI work in browser extensions, web products, desktop apps and mobile apps should be able to enter Frontend Design without the user repeatedly reminding the model.

This Proposal treats that as a **normal-trigger requirement**, not a project-specific style preference.

---

## 4. External reality check

The v0.1 UI-writing/localization checks remain valid. v0.2 adds one execution-critical check against current OpenAI Skills guidance because `PUC-C01` is specifically about activation metadata.

### OpenAI Skills activation and focused boundaries

Current OpenAI Developers documentation states that the model first sees a Skill's metadata, including `name` and `description`, and only loads the full instructions when the request matches. The current Build Skills guidance also says to keep each Skill focused on a recognizable user goal, split workflows when triggers/inputs/success criteria differ, and test direct, indirect, incomplete, should-not-activate and edge cases.

Sources:

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/connect-chatgpt

Implication for this Proposal:

- a body-only negative-route note in `chinese-prose` is insufficient;
- the `chinese-prose` **frontmatter description must be narrowed**;
- `product-ui-copy` needs a precise positive description;
- activation tests must cover competition between the two Skills, not only output quality after the right Skill is already loaded.

### Apple

Apple interface-writing guidance treats language as part of interface design, not post-hoc prose cleanup. HIG labels guidance says labels help people understand current context and what they can do next, and recommends small amounts of text appropriate to the UI role.

Sources:

- https://developer.apple.com/videos/play/wwdc2022/10037/
- https://developer.apple.com/design/human-interface-guidelines/labels

Adopt:

- language is part of interface design;
- UI role/action/context matter;
- concise interface text is a product-design concern.

Do not adopt Apple brand voice as generic style.

### GOV.UK Design System

GOV.UK button guidance says button text should describe the action it performs; error guidance emphasizes clear, specific language bound to the actual user problem.

Sources:

- https://design-system.service.gov.uk/components/button/
- https://design-system.service.gov.uk/components/text-input/
- https://design-system.service.gov.uk/components/error-summary/

Adopt:

- standard action labels should describe the real action;
- UI role and user consequence matter;
- error copy must be specific to the state.

Do not import GOV.UK service tone as a global product voice.

### Microsoft

Microsoft current style guidance recommends simple, precise wording and consistent terminology for the same concept. Its globalization guidance distinguishes localization from mere translation: localization adapts content to a specific locale's expectations.

Sources:

- https://learn.microsoft.com/en-us/style-guide/word-choice/
- https://learn.microsoft.com/en-us/style-guide/global-communications/
- https://learn.microsoft.com/en-us/globalization/reference/microsoft-language-resources

Adopt:

- the same concept should not acquire multiple decorative synonyms;
- short/simple is useful when the role permits it;
- locale is a language + market/register decision, not character conversion.

Do not copy Microsoft-specific terminology as generic product vocabulary.

### Apple localization

Apple supports region-specific localizations and treats localization as language/region-aware product adaptation; it recommends testing localization in the actual interface.

Sources:

- https://developer.apple.com/documentation/xcode/choosing-localization-regions-and-scripts
- https://developer.apple.com/documentation/xcode/localization

Adopt:

- zh-Hans and zh-Hant-HK are separate realizations from the same protected meaning;
- rendered layout must be checked after localization.

## 5. Ownership matrix## 5. Ownership matrix

| Decision / responsibility | Frontend Design | Clear Writing / Product UI Copy | Product/domain owner |
|---|---|---|---|
| Whether this surface needs text | **Owner** | May suggest deletion/merge, not decide | Supplies product truth |
| Where text appears | **Owner** | No | Supplies constraints |
| UI role | **Owner** | Consumes | No |
| Hierarchy / visual prominence | **Owner** | No | No |
| Progressive disclosure | **Owner** | May flag over-complete reassurance | Legal/product owner may constrain |
| Duplicate semantic payload across neighboring blocks | **Owner** | May flag rhetorical/lexical duplication | No |
| Product state / eligibility / capability semantics | Consumes / escalates | Protected, cannot change | **Owner** |
| User consequence / next action semantics | Freezes | Realizes naturally | Product owner supplies truth |
| Short-copy naturalness | Reviews rendered fit | **Owner** | No |
| Locale/register realization | Provides target locale/context | **Owner** | May provide terminology/brand constraints |
| Protected-meaning fidelity | Provides source/constraints | **Owner guardrail via writing-fidelity** | **Authority source** |
| Page-level linguistic rhythm | Final rendered owner | **First-pass language owner** | No |
| Line wrap / CTA relationship / viewport prominence | **Owner** | Consumes constraints | No |
| Product-semantic defect | **Owner to escalate** | Must not cosmetically rewrite | **Decision owner** |
| Legal/trust/safety truth | Layout/disclosure owner only | May improve wording only under frozen facts | **Decision/approval owner** |
| Final rendered page/screen acceptance | **Owner** | Supplies wording candidate / linguistic review | May approve product/legal facts |

Core boundary:

> **Frontend Design owns content architecture. Clear Writing owns natural-language realization under frozen meaning. Product/domain authority owns the truth being communicated.**

---

## 6. Page-level rhythm owner

Single-line naturalness and whole-page naturalness are different problems.

Freeze a two-stage ownership model:

### Writing first-pass rhythm

Product UI Copy receives the visible copy set, not only one bare string, and reviews:

- accumulated parallel rhetoric;
- repeated explicit second person;
- repeated reassurance;
- repeated internal nouns;
- repeated state phrased several different ways;
- sloganization;
- role-inappropriate sentence/fragment choices;
- locale-specific rhetorical awkwardness.

It can return:

- wording candidates;
- `KEEP`;
- a recommendation to merge/delete/move copy;
- an escalation.

It does **not** decide page hierarchy or physically remove/move elements.

### Frontend final rendered rhythm

Frontend Design owns the final rendered acceptance after implementation:

- is the same state repeated in badge + heading + body + CTA?
- does mobile first viewport over-explain before the primary action?
- did localization create awkward wrapping or CTA displacement?
- are several individually natural lines collectively too promotional or repetitive?
- is trust/legal text visually over-promoted or under-disclosed?
- does the relationship between copy and control make the action clear?

Thus Writing owns **linguistic page rhythm analysis**; Frontend owns **rendered page rhythm acceptance**.

---

## 7. Decision: add a dedicated sibling Skill

### Option 1 — extend `chinese-prose`

Rejected as the main route.

Advantages:

- no new Skill;
- current Chinese naturalness behavior is strong;
- low packaging cost.

Problems:

- `chinese-prose` is intentionally broad and document/paragraph oriented;
- UI role, neighboring copy, product state, viewport and rendered interaction are not its native unit;
- adding many UI-specific mechanisms risks regressing reports/README/technical prose;
- its **current frontmatter description is too broad** and explicitly overlaps Product UI Copy;
- future English/other-locale UI copy would be awkwardly owned by a Chinese-named Skill.

### Option 2 — new sibling `product-ui-copy`

**Recommended and retained.**

Proposed source:

`skills/writing/core/product-ui-copy/`

The unit of work is distinct and stable: interface language inside a frozen product role/state/context.

The new Skill does not create a new top-level plugin.

### Option 3 — no Skill; handoff mode only

Rejected as the primary production route.

A prompt-only mode would still leave normal activation dependent on ambiguous existing Skill metadata, which is exactly the failure exposed by `PUC-C01`.

### 7.1 Frozen frontmatter trigger contract

The execution package must treat Skill metadata as production routing, not documentation polish.

#### `product-ui-copy` positive description

The exact final wording can receive ordinary copy editing, but it must preserve this trigger meaning and stay within repository metadata limits:

> Product UI microcopy for labels, CTAs, status, help, empty/loading/error states, onboarding, settings, trust/privacy, landing copy, and locale-specific UI wording. Use for user-visible product interfaces with frozen product meaning/context; do not use for reports, README, technical docs, manuscripts, or ordinary paragraph rewrites.

Required properties:

- explicitly says **product UI / interface**;
- names representative UI roles;
- mentions frozen product meaning/context;
- is not Chinese-only;
- excludes long-form/document tasks.

#### `chinese-prose` narrowed description

The current description's broad clause covering “任何……面向用户或读者的中文内容” must be replaced.

The final description must preserve this boundary:

> 中文报告、README、Markdown/PDF、技术文档、科研说明和普通段落的自然中文终审；用于说人话、减少翻译腔/模板腔并保护事实与证据。产品 UI label/CTA/status/help/error/onboarding/settings 等 microcopy 不走本 Skill，交给 `product-ui-copy`；结构性科研/技术重写交给 `scientific-rewrite`。

Do **not** rewrite the existing `chinese-prose` long-form mechanism beyond the narrow routing seam needed to prevent Product UI Copy capture.

### 7.2 Clear Writing plugin-level discovery

Current `writing-style 0.3` plugin metadata does not advertise Product UI Copy.

If this Proposal is implemented, the execution package must update the Clear Writing plugin discovery surface so the new Skill is reachable from ordinary plugin use:

- `writing-style` plugin description;
- at least one Product UI Copy default prompt;
- packaged Skill list including `product-ui-copy`.

This is mandatory under the current source baseline, not merely a “check if needed”.

### 7.3 Activation competition evals

The final candidate must test both activation and non-activation.

Minimum categories:

**Direct Product UI Copy**
- “把这个按钮/CTA 文案改自然一点。”
- “这几个错误状态文案帮我改得像正式产品。”

**Indirect Product UI Copy**
- “这个设置页中文都能看懂，但很像 AI 连续润色出来的。”
- “这个浏览器插件 popup 的状态说明太像内部工程术语。”

**Near-miss that must stay on `chinese-prose`**
- “帮我把 README 这段中文写自然一点。”
- “这份中文技术说明别像运行日志。”

**Heavy rewrite that must stay on `scientific-rewrite`**
- “把这份中文科研报告重新组织，但保留公式、引用、数字和结论强度。”

**Negative / no Clear Writing UI route**
- backend/data/runtime work with no user-visible copy change.

The activation eval must record which Skill was selected. A good final string from the wrong route is not a routing PASS.

## 8. Frontend → Writing handoff contract## 8. Frontend → Writing handoff contract

The handoff is a **conceptual contract expressed as a lightweight structured block**, not a new machine schema/state machine/ledger.

Recommended minimum:

```text
SURFACE:
UI_ROLE:
PRODUCT_STATE:
USER_JOB:
USER_CONSEQUENCE_OR_NEXT_ACTION:
NEIGHBORING_VISIBLE_COPY:
LOCALE:
PROTECTED_MEANING:
DISCLOSURE_LEVEL:
LENGTH_OR_VIEWPORT_CONSTRAINT:
```

Optional when relevant:

```text
DESIGN_AUTHORITY:
TERMINOLOGY_OR_BRAND_TOKENS:
```

Interpretation:

- `SURFACE`: landing, onboarding, settings, tray panel, dialog, extension popup, mobile screen, etc.
- `UI_ROLE`: label, CTA, status, help, empty/loading/error, trust/legal, marketing/brand, field help, confirmation, etc.
- `PRODUCT_STATE`: actual state being communicated.
- `USER_JOB`: what the user is trying to do on this surface.
- `USER_CONSEQUENCE_OR_NEXT_ACTION`: what matters after reading.
- `NEIGHBORING_VISIBLE_COPY`: enough local/page copy to detect duplication/rhythm.
- `LOCALE`: at least `zh-Hans`, `zh-Hant-HK`, or another explicit locale.
- `PROTECTED_MEANING`: propositions that cannot drift.
- `DISCLOSURE_LEVEL`: primary inline / secondary help / details / legal/trust.
- `LENGTH_OR_VIEWPORT_CONSTRAINT`: line count, control width, mobile first viewport, etc.

Do not require JSON. Markdown/YAML-like structured text is enough.

### Writing response contract

The Writing side returns, as applicable:

- classification;
- `KEEP` or candidate wording;
- protected-meaning check;
- locale note;
- page-rhythm note;
- architecture recommendation if wording alone cannot solve the problem;
- explicit escalation when semantics/trust/legal facts are unsafe or incomplete.

Writing may recommend `DELETE` / `MERGE` / `MOVE`, but Frontend decides whether that architecture change is accepted.

---

## 9. Defect taxonomy

Use this as a reasoning taxonomy, not a runtime enum schema.

### KEEP

The copy is role-appropriate, natural, locale-appropriate and semantically safe. Do not rewrite merely to demonstrate capability.

### WORDING / NATURALNESS

Meaning and placement are sound, but the realization is awkward, modelish, over-complete, overly rhetorical, internally framed, or poorly matched to the UI role.

Owner: Product UI Copy.

### LOCALE / REGISTER

Meaning and architecture are sound, but the wording is not native to the target locale/register.

Examples:

- Mainland product Chinese vs Hong Kong product Chinese;
- inappropriate `电邮/郵箱`, `资料/資料`, support/service terminology;
- mechanically converted phrasing.

Owner: Product UI Copy under protected meaning.

### CONTENT ARCHITECTURE

The problem is whether/where/how much text exists, duplication, progressive disclosure, hierarchy or role.

Owner: Frontend Design.

Writing may flag it but cannot solve it by inventing multiple polished phrasings.

### PRODUCT SEMANTICS

The text exposes an internally inconsistent, incomplete or unsafe product rule/state.

Owner: product/domain authority, routed through Frontend Design.

Writing must not make it sound plausible.

### LEGAL / TRUST / SAFETY

The truth, consent, privacy, legal responsibility, safety promise or user consequence is uncertain, unfinished or approval-sensitive.

Owner: appropriate product/legal/trust authority.

Writing may improve language only after facts/required disclosure are frozen.

Severity P1/P2/P3 remains a separate Frontend/workflow concept; do not encode severity into this taxonomy.

---

## 10. writing-fidelity boundary

For Product UI Copy, protected meaning includes at least:

- product state and availability;
- eligibility;
- verification meaning;
- consent and opt-in/opt-out effect;
- privacy/data collection/use/retention/deletion facts;
- safety limitations/promises;
- pricing/payment/subscription facts;
- what action will occur;
- whether an action is reversible/destructive;
- what another person/system can see;
- legal/trust disclaimers that are actually required;
- exact brand/product/technical tokens whose identity matters.

Product UI Copy may:

- shorten;
- change sentence structure;
- convert a sentence to a role-appropriate fragment;
- remove unnecessary rhetorical scaffolding;
- realize each locale differently;
- recommend merge/delete/move when content architecture is wrong.

It may **not** silently delete a protected proposition.

A proposition may disappear from one visible block only when Frontend explicitly confirms that:

- it is duplicated elsewhere on the same accepted surface/disclosure path; or
- it is marked non-primary and intentionally moved behind details/help; and
- the product/legal owner does not require it in the original position.

If that cannot be established, return escalation.

---

## 11. Chinese naturalness mechanism

Do not build a banned-word list.

### Product self-definition vs action/state first

Transactional/status surfaces should normally lead with current state, user consequence or next action.

Brand/marketing surfaces may define the product when that is genuinely the page job.

Do not convert this into “never say 这是/這是一個”.

### Explicit second person

Use `你/你的` when directly addressing a choice, consequence, consent, personal data, error or action improves clarity.

Avoid repeating it where Chinese naturally permits a neutral task/state phrase.

Do not ban `你`.

### Balanced rhetoric

`不是 X，而是 Y`, `只有 X，才 Y`, `先 X，再 Y` are legitimate forms.

The defect is **accumulated rhetorical symmetry** across a page or flow, not the phrase itself.

### Ordinary state sloganization

Registration-open, matching-closed, ready, offline, syncing, etc. should normally be expressed as state/action rather than automatically promoted to a brand slogan.

### Internal implementation nouns

Translate to user-perceivable state/consequence when safe.

If no faithful user-facing mapping exists because the product rule itself is unclear, escalate rather than inventing.

### Over-complete reassurance

Reassurance is useful when the user has a real risk/question. It should not narrate every internal guarantee by default.

Use progressive disclosure for low-frequency implementation detail.

### Fragment vs sentence

- CTA / tab / field label / status chip: prefer conventional short labels.
- status/help/error/empty state: use the shortest complete form that communicates consequence/action.
- trust/legal: complete, precise sentences are often appropriate.
- landing/brand: sentence length follows hierarchy, not a universal brevity rule.

### Standard action labels

Prefer standard action verbs when they describe the actual action. Do not replace `登录/登入`, `保存`, `继续`, `删除`, etc. with decorative brand language merely to sound distinctive.

---

## 12. Locale contract

Freeze one protected meaning source and create **independent locale realizations**.

For `zh-Hans` and `zh-Hant-HK`:

- neither locale is the master wording for the other;
- no character-conversion acceptance;
- both may choose different sentence structure, pronouns and standard UI vocabulary;
- exact brand/product/technical tokens remain consistent unless locale policy explicitly localizes them;
- semantic propositions, consequence and legal/trust strength must remain equivalent;
- both must be rendered in the real/representative UI and checked for wrap, prominence and CTA relationship.

Evaluation must prove independent realization by including cases where an acceptable Hong Kong phrase is not the preferred Mainland phrase and vice versa.

---

## 13. Line-level workflow

For each copy unit:

1. Frontend freezes UI role, product state, user job, consequence/action, protected meaning and neighboring context.
2. Product UI Copy classifies the defect.
3. If `KEEP`, return unchanged.
4. If `WORDING` or `LOCALE`, realize the target locale while preserving meaning.
5. If `CONTENT ARCHITECTURE`, return an architecture recommendation to Frontend; do not cosmetically rewrite as if placement were correct.
6. If `PRODUCT SEMANTICS` or `LEGAL/TRUST/SAFETY`, escalate and preserve the unresolved fact boundary.
7. Frontend integrates accepted wording and proceeds to rendered acceptance.

---

## 14. Page-level rhythm workflow

For S2/S3 surfaces or any copy-heavy page:

1. Frontend inventories visible roles and removes/merges obvious semantic duplication before wording polish.
2. Writing receives the visible copy set and performs first-pass linguistic rhythm review.
3. Writing returns line candidates plus page-level rhythm flags.
4. Frontend implements the candidate copy.
5. Frontend inspects the actual rendered page/screen across relevant viewport/locale states.
6. If a rhythm problem is caused by layout/role/duplication, Frontend fixes architecture.
7. If caused by realization/register, hand the frozen context back to Product UI Copy.
8. P4 whole-product taste includes the final copy rhythm.

Do not run this heavy page pass for an isolated S1 label change unless neighboring copy creates a real ambiguity.

---

## 15. Product / legal / trust escalation

Product UI Copy is not a policy engine.

Escalate when:

- a public surface exposes “pending legal approval” or internal product-contract language and there is no frozen public disclosure decision;
- privacy/consent meaning is incomplete;
- the proposed rewrite would weaken or strengthen a guarantee;
- a user consequence is unknown;
- a trust reassurance conflicts with real behavior;
- eligibility/verification language overstates authority;
- deleting text would remove a required notice.

Allowed output is a diagnosis + the missing decision needed, not a polished invented answer.

---

## 16. S1 / S2 / S3 scale-down

### S1 — isolated local copy repair

Examples: one CTA, label, short help line, typo-like naturalness defect.

Use:

`Frontend role/meaning freeze → Product UI Copy line realization → local rendered check`

No full page-rhythm review or independent review unless the change touches trust/legal/product semantics.

### S2 — bounded UI/copy change

Examples: empty/error state, settings section, status cluster, onboarding step.

Use:

- local content-architecture check;
- structured handoff;
- line realization;
- neighboring-copy rhythm;
- rendered cluster/state acceptance.

### S3 — page/flow redesign or copy-heavy landing/onboarding

Use:

- full content-architecture inventory;
- product-semantic escalation before wording;
- locale-paired realization;
- page-level rhythm;
- rendered multi-viewport acceptance;
- independent final review according to Frontend 0.3 admission rules.

---

## 17. Figma / no-Figma copy authority

### Canonical Figma exists

Figma may be the visual/copy placement authority when the approved frame contains intentional copy.

It does not become product/legal truth authority.

If copy changes materially alter line count, hierarchy, grouping or CTA layout, the accepted design should round-trip through the canonical design source when the project contract requires Figma convergence.

### No Figma

Durable copy/content authority may come from:

- product/design brief;
- screen/state specification;
- string catalog with semantic comments;
- accepted current product grammar for bounded S1/S2 changes;
- task-local copy brief produced by the Frontend coordinator.

No-Figma is a normal path.

---

## 18. Clear Writing routing

### Positive Product UI Copy triggers

Route to `product-ui-copy` for user-visible product-interface language such as:

- labels;
- CTA/buttons;
- status;
- field help;
- empty/loading/error;
- onboarding;
- landing/product microcopy;
- settings/support/privacy/trust surface copy;
- “这个产品页面中文不自然”;
- “UI 都能读，但有 AI 味”;
- locale-specific UI realization.

### Near-miss / negative triggers

Do not let Product UI Copy steal:

- Chinese research reports;
- README long-form prose;
- technical docs;
- manuscripts;
- advisor reports;
- ordinary paragraph rewrite;
- source-faithful scientific structural rewrite;
- captions/slide prose whose owner is scientific/presentation workflow rather than product UI.

Routes remain:

- long/ordinary Chinese reader-facing prose → `chinese-prose`;
- heavy source-faithful Chinese scientific/technical rewrite → `scientific-rewrite`;
- English scientific prose → `scientific-prose`;
- fidelity-sensitive guardrail → `writing-fidelity`;
- product UI language → `product-ui-copy` + `writing-fidelity`.

### Metadata priority

This separation must be visible in **frontmatter metadata**, not only in the Skill body.

Implementation must update:

- new `product-ui-copy.description`;
- narrowed `chinese-prose.description`;
- Clear Writing plugin description/default prompts;
- positive/indirect/near-miss/negative trigger evals.

The long-form body rules of `chinese-prose` remain otherwise intact.

## 19. Frontend Design integration## 19. Frontend Design integration

Do not alter the 0.3 coordinator-first topology.

Integrate Product UI Copy into the existing flow:

```text
frontend-visual-systems coordinator
  → P0/P1: product state + content architecture + UI role
  → if wording/localization needed:
       lightweight handoff to Clear Writing / product-ui-copy
  → candidate copy returns
  → P2 implementation
  → P3 actual rendered copy acceptance
  → F-D admission
  → P4 whole-product taste
```

The cross-plugin handoff is conditional. Frontend Design remains useful without Clear Writing for layout/visual/product structure, but it cannot claim Product UI Copy naturalness/locale closure when the language capability required by acceptance is unavailable.

Do **not** vendor/copy Product UI Copy rules into `web-development`.

---

## 20. Surface-agnostic Frontend Design trigger contract

This remains an explicit user requirement.

Frontend Design is a **product-interface design capability**, despite the compatibility slug `web-development`.

Positive normal triggers must include user-facing UI/design/copy/layout/interaction work for:

- browser extension — Mica for ChatGPT;
- browser/web product — CUHK Date, Asteria;
- desktop app / Tauri / Electron / native-WebView — Bobbio, Lucerna;
- mobile / Android / Compose — SeminarArc.

Frontend Design must not depend on the user saying “use Frontend Design”.

Negative examples:

- Mica content-script hot-path performance with no UI design change;
- Lucerna runtime/provider/Longleaf diagnostics with no product-surface work;
- SeminarArc Room/WorkManager/data-layer work with no UI change;
- Asteria API/math-only work;
- docs-only README editing.

### Central discovery changes required for implementation

Future implementation must update the production discovery surface so “Frontend” is not read as “web page only”:

- `web-development` plugin description;
- representative default prompts;
- `frontend-visual-systems` frontmatter description/trigger boundary;
- `product-ux-planning` trigger boundary where needed;
- trigger evals covering browser extension, web, desktop/WebView and mobile/Compose positives plus backend/docs negatives.

Do not rename the compatibility slug.

### Project-local binding for known long-lived products

Central trigger expansion improves discovery but is not equivalent to a hard project binding.

The desired steady state for:

- Mica for ChatGPT;
- CUHK Date;
- Asteria;
- Bobbio;
- Lucerna;
- SeminarArc

is a minimal project-local binding:

> User-facing UI / Figma / visual / copy / interaction work should use installed Frontend Design (`web-development`) as the generic product-interface coordinator; project-local platform/product skills and canonical design/product sources remain higher authority for platform-specific and domain semantics.

Consumer adaptation is a later authorized task. This Proposal does not modify any consumer repo.

For SeminarArc, Frontend Design complements rather than replaces `android-lead` and `compose-expert`.

### Real mobile compatibility proof

Metadata and synthetic activation tests are insufficient for the explicit mobile claim.

The final candidate must run the read-only SeminarArc normal-entry replay defined in §22.3, proving both:

```text
natural Compose/UI task
→ Frontend Design generic coordinator
→ Android/Compose platform authority retained
```

and:

```text
Room / WorkManager / data-only task
→ Frontend Design does not activate
```

This replay is compatibility/discovery evidence only and cannot promote maturity.

## 21. Packaging / topology## 21. Packaging / topology

Recommended Clear Writing production topology after implementation:

```text
writing-style / Clear Writing
├── writing-fidelity
├── product-ui-copy          NEW
├── chinese-prose
├── scientific-prose
└── scientific-rewrite
```

No new top-level plugin.

Recommended profile changes:

- add `product-ui-copy` + `writing-fidelity` to relevant frontend-oriented profiles where Clear Writing companion behavior is expected;
- do not duplicate Product UI Copy source into the Frontend plugin;
- protect current research/long-form profiles from unnecessary UI trigger noise.

Likely profile surfaces to review:

- `profiles/codex-webdev.json`
- `profiles/frontend-research-product.json`

The exact installation mechanism must be validated against current profile/plugin tooling during execution planning; do not invent a new dependency manager.

---

## 22. Evaluation and replay plan

### 22.1 Deterministic routing / contract tests

Cover:

- Product UI Copy direct positives;
- Product UI Copy indirect positives;
- `chinese-prose` near-miss positives / Product UI Copy negatives;
- `scientific-rewrite` negatives;
- Frontend non-web surface positives;
- backend/runtime/docs negatives;
- handoff field completeness;
- protected-meaning escalation;
- no direct rewriting of PRODUCT_SEMANTICS / LEGAL_TRUST_SAFETY cases.

These tests prove routing/mechanical contract only, not naturalness.

### 22.2 Known regression replay

CUHK Date 150-line audit remains known replay:

- taxonomy/ownership calibration;
- B/C naturalness handling;
- D escalation;
- good A lines often return `KEEP`;
- no CUHK Date production mutation;
- never describe it as unseen/fresh.

### 22.3 Independent real-project replay

Use three read-only real projects on the same final candidate.

#### Lucerna — desktop/native-WebView microcopy regression

Purpose:

- #17 consequence-first vs implementation-reassurance behavior;
- disclosure/placement remains Frontend-owned;
- project source remains read-only.

#### Mica for ChatGPT — browser-extension UI

Purpose:

- product-interface auto-trigger outside ordinary web-page framing;
- normal feature labels vs diagnostic-only language;
- internal implementation vocabulary vs user consequence;
- `KEEP` on already-good standard action labels.

Current planning evidence includes popup labels such as `Long-thread optimization`, `Stale clear recovery`, `Connector continuity`, `Send residual recovery`, and diagnostic actions. Exact replay ref must be frozen in the execution package/final-candidate evidence.

#### SeminarArc — mobile/Compose normal-entry compatibility

Current planning source:

`YuukiAS/SeminarArc main @ 74caaa4ecec16f1bc90987979458d1a4e93f52be`

Current project authority includes:

- `.agents/skills/android-lead/SKILL.md`
- `.agents/skills/compose-expert/SKILL.md`

Freeze two neutral replay prompts that do **not** mention Frontend Design or expected routing.

**Positive natural UI prompt shape**

A real Compose/UI change, for example:

> The seminar list/detail flow in SeminarArc is visually flat and the current hierarchy makes the primary action hard to scan. Plan the UI repair for the existing Compose app without changing product scope.

Required behavior:

- normal Frontend Design entry activates;
- generic product-interface coordinator handles product hierarchy/design authority/evidence;
- Android/Compose implementation semantics remain owned by SeminarArc's `android-lead` / `compose-expert`;
- no claim that Frontend Design replaces project-local platform authority.

**Negative data/background prompt shape**

For example:

> Move an existing background cleanup job to WorkManager while preserving Room state and retry semantics. No UI behavior changes.

Required behavior:

- Frontend Design does not activate;
- SeminarArc's Android/data/background owner handles the task.

This replay is **surface/discovery compatibility only**, not maturity evidence.

### 22.4 Fresh repo-safe holdout — corrected freeze chronology

The exact holdout batch must **not** be visible to the Executor during normal implementation/tuning.

#### H0 — pre-implementation freeze

Before implementation, freeze only:

- task families;
- coverage matrix;
- scoring/rubric;
- batch size;
- locale balance;
- required KEEP / rewrite / architecture / product-semantic / legal-trust outcomes;
- reviewer criteria;
- rule that the full batch is evaluated once.

Do **not** freeze or expose the exact final scenario texts to the Executor.

Required coverage families remain:

- zh-Hans;
- zh-Hant-HK;
- CTA;
- state;
- help;
- empty/error;
- privacy/trust;
- landing;
- repeated page rhythm;
- already-natural copy that must remain unchanged;
- CONTENT ARCHITECTURE escalation;
- PRODUCT SEMANTICS escalation;
- LEGAL/TRUST/SAFETY escalation.

#### H1 — development evidence

During implementation, use:

- deterministic routing tests;
- CUHK Date known regression;
- Lucerna/Mica/SeminarArc known real-project compatibility replay;
- unrelated Frontend/Clear Writing regressions.

These are tuneable development/known evidence and must not be relabeled fresh.

#### H2 — final candidate + review criteria freeze

After implementation stabilizes:

1. freeze exact candidate;
2. freeze reviewer criteria/rubric;
3. prohibit further production tuning before fresh evaluation.

#### H3 — exact final holdout freeze

Only now may an independent existing owner (Planner/Critic/Reviewer as defined by the execution package) freeze the exact repo-safe final holdout batch.

The exact batch becomes visible only after H2.

No new role, service, private database or hidden evaluation system is required.

#### H4 — one-shot evaluation

Run the complete exact batch once against the same final candidate.

Rules:

- no cherry-picking;
- no partial batch PASS;
- no replacing failed prompts;
- no appending easier cases to dilute failures;
- no candidate modification followed by calling the same batch fresh.

If the candidate is changed using holdout results, that batch becomes **known regression evidence**. The release gate has failed for that final candidate. Any later fresh evaluation requires a newly authorized evaluation round after another candidate freeze; it cannot be improvised inside the failed run.

## 23. Independent review plan

Final implementation cannot rely on Executor self-review.

Required evidence layers:

1. deterministic routing/contract tests, including `product-ui-copy` vs `chinese-prose` metadata competition;
2. CUHK Date known regression replay;
3. unrelated Clear Writing regression:
   - Chinese report/README route;
   - scientific-rewrite route;
   - English scientific-prose route;
4. unrelated Frontend Design regression:
   - coordinator-first;
   - S1/S3 scale;
   - Figma/no-Figma;
   - browser/native evidence;
5. independent read-only real-project replay:
   - Lucerna;
   - Mica for ChatGPT;
   - SeminarArc positive Compose/UI + negative Room/WorkManager/data-only normal-entry pair;
6. H0/H2/H3/H4 fresh-holdout chronology from §22.4;
7. independent text/naturalness review;
8. actual rendered Frontend acceptance for representative page/screen contexts.

Independent review asks:

- Was protected meaning preserved?
- Is the copy appropriate for the actual UI role?
- Is the locale native rather than mechanically converted?
- Did the system correctly escalate architecture/product/legal defects instead of polishing them?
- Did it avoid changing already-good copy?
- Does the whole rendered page/screen read naturally?
- Did Frontend trigger on browser extension/web/desktop/mobile UI while staying out of backend/runtime/data-only work?
- Did platform-specific owners remain authoritative?
- Is claim scope no broader than evidence?
- Was the fresh batch truly unavailable until after candidate/rubric freeze?

No AI detector, banned-phrase score, trigger-only fixture, CI, or schema check may substitute for qualitative naturalness/rendered acceptance.

## 24. Future implementation surface

If v0.2 receives Critic PASS and a later execution package is approved, likely production surfaces include:

### Frontend Design

- `skills/tools/frontend/frontend-visual-systems/SKILL.md`
  - surface-agnostic product-interface trigger metadata;
  - Product UI Copy handoff point;
- `skills/tools/frontend/product-ux-planning/SKILL.md`
  - content-architecture ownership;
- `skills/tools/frontend/responsive-accessibility-review/SKILL.md`
  - rendered copy/wrap/viewport acceptance where applicable;
- Frontend trigger evals:
  - browser extension;
  - web;
  - desktop/WebView;
  - mobile/Compose;
  - backend/runtime/data/docs negatives;
- `scripts/codex_marketplace_config.json`
  - `web-development` description/default prompts updated so discovery is not web-page-only.

### Clear Writing

- **new** `skills/writing/core/product-ui-copy/SKILL.md`
  - focused UI trigger description;
  - UI-role/context workflow;
- **new** `skills/writing/core/product-ui-copy/evals/trigger_queries.json`
  - direct/indirect/near-miss/negative activation;
- `skills/writing/core/writing-fidelity/SKILL.md`
  - narrow Product UI Copy semantic-fidelity handoff;
- `skills/writing/core/chinese-prose/SKILL.md`
  - **frontmatter description narrowed** to exclude Product UI microcopy;
  - body only receives the minimal route-boundary note needed for consistency;
  - long-form mechanism otherwise protected;
- Clear Writing routing tests for `product-ui-copy` vs `chinese-prose` vs `scientific-rewrite`;
- `scripts/codex_marketplace_config.json`
  - package new sibling under `writing-style`;
  - update Clear Writing plugin description/default prompts to expose Product UI Copy.

### Profiles / packaging

Review:

- `profiles/codex-webdev.json`;
- `profiles/frontend-research-product.json`;
- generated Marketplace layer through the existing generator only;
- existing parity/version tests.

The execution Planner must validate the existing installation/profile mechanism rather than inventing a new dependency manager.

### Evaluation artifacts

Future execution must create repo-owned evidence for:

- routing competition;
- known replay;
- Lucerna/Mica/SeminarArc read-only replay;
- H0 coverage/rubric freeze;
- H2 final candidate freeze;
- H3 exact final holdout batch;
- H4 one-shot evaluation;
- independent text review;
- rendered Frontend acceptance.

### Consumer adaptation

Mica / CUHK Date / Asteria / Bobbio / Lucerna / SeminarArc project-local bindings remain **separate later consumer tasks**. This AI_Skills implementation must not mutate those repositories.

### Maintenance / release

- `docs/plugin-todos/web-development.md`
- `docs/plugin-todos/writing-style.md`
- `docs/plugin-changelogs/web-development.md`
- `docs/plugin-changelogs/writing-style.md`
- root `CHANGELOG.md`
- `README.md`
- `VERSION`
- release/version tests

No production file is changed by this planning task.

## 25. Regression risks

### Risk 1 — chinese-prose regression

UI-specific mechanisms inside `chinese-prose` could make reports/README/technical prose unnaturally terse or UI-like.

Mitigation: dedicated sibling Skill; only narrow `chinese-prose` metadata/route exclusion; long-form behavior protected.

### Risk 2 — metadata collision still routes UI to chinese-prose

A correct body-level `product-ui-copy` implementation can remain undiscoverable if the old broad `chinese-prose` description wins activation.

Mitigation: frontmatter description changes are a hard production requirement; activation competition evals gate release.

### Risk 3 — Frontend becomes writing owner

If Frontend rewrites language itself, rules duplicate and locale logic drifts.

Mitigation: Frontend owns architecture/context; Writing owns realization.

### Risk 4 — Writing silently fixes product/legal problems

A polished sentence can hide an unresolved product/legal defect.

Mitigation: protected meaning + explicit escalation taxonomy.

### Risk 5 — every line gets rewritten

The model may “show work” by changing already-natural strings.

Mitigation: `KEEP` is first-class and final holdout includes good controls.

### Risk 6 — page rhythm becomes another phrase scanner

Mechanical detection of `你`, `先`, or contrast structures would overfit CUHK Date.

Mitigation: judge accumulation + UI role + neighboring copy, never word bans.

### Risk 7 — localization becomes character conversion

Mitigation: independent locale realization and rendered acceptance.

### Risk 8 — web-only trigger

Compatibility slug/category can bias discovery toward web pages.

Mitigation: surface-agnostic plugin/Skill metadata + real Mica/Lucerna/SeminarArc final-candidate normal-entry replay + later project bindings.

### Risk 9 — Frontend steals Android/Compose platform ownership

Mitigation: SeminarArc positive replay must preserve `android-lead` / `compose-expert`; data/background negative control must not trigger Frontend.

### Risk 10 — holdout leakage

Exact “fresh” prompts exposed before candidate freeze allow tuning and invalidate generalization evidence.

Mitigation: H0 coverage/rubric only; H2 candidate freeze; H3 exact batch freeze; H4 one-shot evaluation; any later candidate modification makes the batch known regression.

### Risk 11 — cross-plugin dependency makes Frontend unusable alone

Mitigation: Frontend can still own content architecture and emit a handoff; only Product UI Copy naturalness/locale closure requires the writing companion.

## 26. Explicit non-goals## 26. Explicit non-goals

This Proposal does not:

- edit CUHK Date copy;
- edit Lucerna copy;
- edit Mica copy;
- edit Asteria/Bobbio/SeminarArc;
- adopt CUHK Date founder tone as a global house style;
- create AI-detector evasion;
- create banned phrase lists;
- create deliberate errors/slang/random variation;
- rewrite all of Clear Writing;
- reopen Frontend Design 0.3 architecture or #52–#72;
- promote writing-style #13 wholesale;
- solve product/legal semantics inside a writing Skill;
- create a cross-plugin state machine/schema/ledger;
- create an Executor Goal.

---

## 27. TODO disposition plan

Planning recommendation, pending independent Critic:

### Frontend Product UI Copy heading

`NEW -> PROMOTE_NOW` as the Frontend half of one bounded cross-plugin batch.

Tracking repair required before implementation lifecycle closure:

- remove/rebind wrong `tracking: #73`;
- create a unique Frontend Product UI Copy tracking Issue if none exists;
- preserve title + source path as authority until then.

### writing-style #17

`NEW -> PROMOTE_NOW` inside the same bounded Product UI Copy batch.

GitHub Issue #17 is a valid tracking locator.

### writing-style #20

`NEW -> PROMOTE_NOW` inside the same bounded Product UI Copy batch.

Tracking repair required:

- current source `tracking: #20` collides with unrelated Research Authoring Issue #20;
- create a unique Product UI Copy naturalness tracking Issue and rebind the source.

### writing-style #13

Keep current source maturity/status unchanged.

Use only as a conceptual dependency proving that Clear Writing is the content-preserving companion layer. Do not close or broadly implement #13 in this task.

No TODO is changed or closed during this planning round.

---

## 28. Maintenance Board pending mutation

This planning round remains inside AI Skills maintenance tracking scope. The current Planner surface still does not expose safe GitHub Project field mutation, and reader-facing Issue/Project mutation requires the repository's Clear Writing mutation rule.

Do not claim Project synchronization.

Exact pending mutations for a Project-capable AI Skills Maintainer:

1. writing-style Issue #17:
   - Project Status: `TODO -> DOING` if still TODO;
   - current anchor: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md`;
   - next step: independent Critic re-review of v0.2.
2. writing-style Issue #13:
   - remain dependency-only / `TODO`;
   - do not move merely because Product UI Copy is planned.
3. Frontend Product UI Copy heading:
   - create/bind a unique issue only after the required Clear Writing copy check;
   - replace collided `tracking: #73`;
   - Project Status = `DOING`;
   - current anchor = v0.2 Proposal;
   - next step = independent Critic re-review.
4. writing-style Product UI Copy naturalness heading:
   - create/bind a unique issue only after the required Clear Writing copy check;
   - replace collided `tracking: #20`;
   - Project Status = `DOING`;
   - current anchor = v0.2 Proposal;
   - next step = independent Critic re-review.

The v0.1 Critic review artifact is now archived at:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_REVIEW_V0_1_2026-09-28.md`

Do not ask the user to maintain the board manually.

## 29. Version and maturity implications

No version changes occur in this planning task.

If the approved architecture is later implemented and released as designed, this is a real production behavior change in **both** affected plugins.

### Plugin versions

Recommended:

```text
web-development: 0.3 -> 0.4
writing-style: 0.3 -> 0.4
all other central plugins: NO_BUMP
```

So: **yes, the next Frontend Design release for this Product UI Copy integration should be 0.4 under the current baseline.**

Clear Writing should also move to 0.4 because it gains a distinct production Product UI Copy capability and routing behavior.

### Repository version

Recommended planned decision:

```text
Repository bump decision: MINOR
Current baseline: 5.3.1
Expected release if unchanged: 5.4.0
```

Reason: this Proposal creates a previously absent **cross-plugin normal user workflow**:

```text
Frontend content architecture
→ protected Product UI Copy handoff
→ locale-aware Clear Writing realization
→ rendered Frontend acceptance
```

That is a repository-level user capability involving multiple plugins, matching the current version policy's explicit minor-release case for a new complete multi-plugin workflow.

If execution/review later narrows the implementation so it no longer forms that repository-level workflow, the final release Planner must re-evaluate under the version policy. It may not choose `NO_BUMP` if the two plugins' production behavior actually changed.

### Maturity

Do not promote maturity as part of this release.

```text
web-development maturity = unclassified
writing-style maturity = unclassified
```

Known replay, one release, or synthetic/fresh fixtures do not establish long-term maturity.

---

## 30. Stage value

If this design is implemented successfully, the new capability is not “more copy rules”.

The actual added capability is:

> A product UI task can decide whether text belongs on the surface, hand a protected semantic/UI-role context to a dedicated language capability, realize natural locale-specific microcopy without changing product truth, and then validate the result in the real rendered page/screen.

The companion trigger improvement also makes Frontend Design explicitly surface-agnostic across browser extension, web, desktop and mobile product UI instead of relying on the user to repeatedly say “use Frontend Design”.

---

## 31. Critic re-review target

The next independent Critic should review v0.2 only for:

1. closure of `PUC-C01`:
   - Product UI Copy frontmatter trigger;
   - narrowed `chinese-prose` frontmatter trigger;
   - Clear Writing plugin discovery metadata;
   - direct/indirect/near-miss/negative competition evals;
2. closure of `PUC-C02`:
   - H0 coverage/rubric freeze;
   - H2 candidate+criteria freeze;
   - H3 exact batch freeze;
   - H4 one-shot evaluation;
   - no adaptive replacement/chasing;
3. closure of `PUC-C03`:
   - read-only SeminarArc positive mobile UI normal-entry replay;
   - project-local `android-lead` / `compose-expert` authority retained;
   - Room/WorkManager/data-only negative control;
   - no maturity credit.

Also check only direct regressions introduced by these amendments.

Do not reopen already-passed ownership, handoff, fidelity, page-rhythm, locale, project-binding, tracking or version decisions unless v0.2 introduces new direct evidence that invalidates them.

No implementation is authorized by Proposal PASS.
