# Product UI Copy Cross-Plugin — Independent Critic Re-review Prompt v0.2

你继续担任 `YuukiAS/AI_Skills_Collection` 的独立 Critic。

当前不是重新设计 Product UI Copy，也不是重新审 Frontend Design 0.3。

上一轮审查对象：

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_1_2026-09-28.md`

上一轮 Proposal commit：

`d1b3a13435cb51e9503f9fe6cbfd1b4b064aadd1`

上一轮 Critic review archive：

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_REVIEW_V0_1_2026-09-28.md`

archive commit：

`386856ddbb60a6cc5d7bc4492554d001425b29f1`

上一轮结果：

```text
RESULT = REVISE
IMPLEMENTATION_AUTHORIZED = NO
```

仅有三个 blocker：

- `PUC-C01 Clear Writing trigger metadata still conflicts with the new sibling`
- `PUC-C02 Fresh holdout frozen before implementation is not fresh`
- `PUC-C03 Mobile/Compose auto-trigger lacks a real normal-entry replay`

本轮只复核这三个 blocker，以及 v0.2 amendment 直接引入的回归。

不要重新打开已经 PASS 的 ownership matrix、handoff contract、writing-fidelity boundary、page rhythm ownership、locale contract、project-binding separation、tracking-collision plan、版本方向或 Frontend Design 0.3 architecture，除非 v0.2 引入新的直接证据使它们不成立。

---

## 1. Review object

Repository:

`YuukiAS/AI_Skills_Collection`

Current Proposal:

`docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md`

Exact Proposal commit:

`a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67`

Planning only.

Do not:

- implement production code;
- modify production Skill;
- modify CUHK Date;
- modify Mica / Lucerna / SeminarArc / Asteria / Bobbio;
- create Executor Goal;
- start Reviewed Handoff;
- bump version;
- close TODO;
- modify Bridge Kit.

---

## 2. Required source reads

Read latest `AI_Skills_Collection/main`:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- v0.1 Proposal
- v0.1 Critic review archive
- v0.2 Proposal

For PUC-C01 read current:

- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `scripts/codex_marketplace_config.json`
- `docs/SKILL_AUTHORING.md`

For PUC-C03 read current:

- `YuukiAS/SeminarArc/AGENTS.md`
- `YuukiAS/SeminarArc/.agents/skills/android-lead/SKILL.md`
- `YuukiAS/SeminarArc/.agents/skills/compose-expert/SKILL.md`

Do not modify SeminarArc.

---

## 3. Minimal external verification

Independently verify the execution-critical OpenAI Skills assumption using current official OpenAI developer documentation.

At minimum verify:

- the model first sees Skill metadata/name/description for discovery;
- description should state what the Skill does and when to use it;
- focused Skills are preferred when triggers/inputs/success criteria differ;
- representative activation tests should include direct, indirect, incomplete/edge and should-not-activate cases.

Current Planner sources:

- https://developers.openai.com/plugins/concepts/skills
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/connect-chatgpt

Do not use this external check to reopen already-passed Product UI Copy ownership.

---

## 4. PUC-C01 closure — trigger metadata competition

The blocker required v0.2 to make normal routing reliable, not just add a new Skill file.

Review whether v0.2 now freezes all of the following:

### New Product UI Copy frontmatter

The new `product-ui-copy` description must positively cover UI/product-interface language such as:

- label / CTA;
- status;
- help;
- empty/loading/error;
- onboarding;
- settings;
- trust/privacy;
- landing microcopy;
- locale-specific UI wording.

It must make clear:

- this is user-visible product-interface language;
- product meaning/context is already frozen;
- it is not the route for reports, README, technical docs, manuscripts or ordinary paragraph rewriting.

### Existing chinese-prose frontmatter

The current broad `chinese-prose` metadata must be narrowed at **frontmatter description level**, not only in the body.

It must:

- continue owning reports/README/technical docs/ordinary Chinese prose;
- exclude Product UI microcopy;
- preserve its current long-form mechanisms;
- continue handing heavy scientific/technical structural rewrite to `scientific-rewrite`.

### Plugin-level discovery

Under the current source baseline, the Proposal requires later implementation to update:

- `writing-style` plugin description;
- at least one Product UI Copy default prompt;
- packaged Skill list.

This must be a required production change, not an optional “consider whether”.

### Competition evals

Verify the evaluation explicitly covers:

- direct Product UI Copy;
- indirect Product UI Copy;
- near-miss long-form Chinese that must use `chinese-prose`;
- heavy structural rewrite that must use `scientific-rewrite`;
- negative backend/runtime/data work;
- selected Skill identity, not only final prose quality.

If these are all frozen clearly, close PUC-C01.

Do not ask Planner to redesign `chinese-prose` beyond the narrow route seam.

---

## 5. PUC-C02 closure — fresh holdout chronology

The blocker was that v0.1 exposed the exact “fresh” batch before implementation.

v0.2 now proposes:

```text
H0 pre-implementation:
  freeze task families / coverage / rubric / batch size / criteria only
  exact final prompts remain unavailable to Executor

H1 development:
  use deterministic tests + known regressions + real-project compatibility

H2:
  freeze exact final candidate + reviewer criteria

H3:
  only after H2, freeze exact final holdout batch

H4:
  one-shot full-batch evaluation on the same final candidate
```

Review whether this satisfies current Capability Gate policy.

Required properties:

- exact holdout is not visible during implementation/tuning;
- complete batch, not cherry-picked samples;
- no replacement/chasing after failure;
- no adding easy cases to dilute failure;
- if candidate changes using holdout results, same batch is no longer fresh;
- any later fresh round must be separately authorized after a new candidate freeze rather than improvised inside the failed run;
- no new hidden service/database/role is created merely to implement freshness.

If so, close PUC-C02.

Do not require a secret external evaluation platform unless current policy actually demands one.

---

## 6. PUC-C03 closure — real mobile/Compose normal-entry evidence

The explicit product requirement remains:

> Frontend Design should automatically handle user-facing product-interface tasks across browser extension, web, desktop and mobile without the user repeatedly saying “use Frontend Design”.

v0.2 adds a read-only SeminarArc final-candidate replay.

Current planning source:

`YuukiAS/SeminarArc main @ 74caaa4ecec16f1bc90987979458d1a4e93f52be`

Current project-local authority includes:

- `android-lead`
- `compose-expert`

Review the proposed paired normal-entry replay.

### Positive mobile UI task

Natural prompt shape:

> The seminar list/detail flow in SeminarArc is visually flat and the current hierarchy makes the primary action hard to scan. Plan the UI repair for the existing Compose app without changing product scope.

The prompt must **not** name Frontend Design or expected routing.

Required evidence:

```text
normal task
→ Frontend Design generic product-interface coordinator activates
→ generic hierarchy/design/evidence work is routed correctly
→ android-lead / compose-expert retain Android/Compose implementation semantics
```

### Negative data/background task

Natural prompt shape:

> Move an existing background cleanup job to WorkManager while preserving Room state and retry semantics. No UI behavior changes.

Required evidence:

```text
Frontend Design does not activate
→ Android/data/background owner handles task
```

The replay must:

- use the same final candidate;
- be read-only against SeminarArc;
- not modify consumer source;
- not count toward maturity promotion;
- prove compatibility/discovery only.

If this closes the previously missing real mobile evidence, close PUC-C03.

Do not demand consumer-repo hard binding in this AI_Skills release; v0.1 Critic already passed the separation between central discovery and later project-local binding.

---

## 7. Amendment regression check

Check only regressions directly caused by v0.2.

At minimum ensure:

- three-owner Product UI Copy ownership is unchanged;
- dedicated `product-ui-copy` sibling remains inside Clear Writing, not a new top-level plugin;
- handoff remains lightweight conceptual structure, not schema/state machine;
- `writing-fidelity` protected product/legal semantics remain unchanged;
- Writing remains linguistic first-pass rhythm owner;
- Frontend remains final rendered rhythm owner;
- zh-Hans / zh-Hant-HK remain independent realizations;
- CUHK Date remains known replay and read-only;
- Lucerna/Mica remain read-only independent replay sources;
- SeminarArc is added only for surface/discovery compatibility;
- no fourth project is added for maturity chasing;
- Project binding remains later consumer adaptation;
- Product UI Copy does not steal long-form Clear Writing;
- Frontend Design 0.3 coordinator-first is not reopened.

---

## 8. Version and maturity — do not reopen without direct contradiction

Previous Critic passed:

```text
web-development: 0.3 -> 0.4
writing-style: 0.3 -> 0.4
repository: 5.3.1 -> 5.4.0
maturity change: NONE
```

The rationale remains:

```text
Frontend content architecture
→ protected Product UI Copy handoff
→ locale-aware Clear Writing realization
→ rendered Frontend acceptance
```

is a new repository-level multi-plugin normal workflow, not merely two unrelated plugin fixes.

Do not reopen version classification unless v0.2 changes that architecture or current version policy directly contradicts the earlier PASS.

Planning itself performs no bump.

---

## 9. Maintenance Board

The Planner did not claim Project synchronization.

Current exact pending mutations are:

- Issue #17:
  - TODO → DOING if still TODO;
  - anchor = v0.2 Proposal;
  - next = independent Critic re-review.
- Issue #13:
  - remain dependency-only / TODO.
- Frontend Product UI Copy heading:
  - create unique Issue after required Clear Writing copy check;
  - replace collided #73;
  - Project = DOING;
  - anchor = v0.2.
- writing-style Product UI Copy naturalness:
  - create unique Issue after required Clear Writing copy check;
  - replace collided #20;
  - Project = DOING;
  - anchor = v0.2.

Do not block solely because this surface cannot mutate Project fields. Do not ask the user to update the board manually.

---

## 10. Blocker standard

REVISE only if:

- PUC-C01 remains unclosed;
- PUC-C02 remains unclosed;
- PUC-C03 remains unclosed;
- the v0.2 amendment creates a new direct risk in already-passed architecture.

Do not create new blockers from:

- preference for different metadata wording when trigger boundaries are equivalent;
- wanting more replay projects;
- wanting a JSON schema;
- wanting a hidden holdout service;
- reopening Frontend Design 0.3;
- unrelated Clear Writing TODOs;
- aesthetic preference about project-binding wording.

Every new blocker must contain:

```text
FINDING_ID
Requirement
Direct evidence
Causal risk
Minimal closure condition
Owner
```

First explicitly report:

```text
PUC-C01 = CLOSED | OPEN
PUC-C02 = CLOSED | OPEN
PUC-C03 = CLOSED | OPEN
```

Do not move the goalposts after a blocker has enough evidence to close.

---

## 11. Required final output

Return:

```text
RESULT = PASS | REVISE

REVIEWED_OBJECT = docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md
REVIEWED_COMMIT = a0ac70226c7b1ddd7d6e33c9d4c00aebbf473f67

PUC-C01 = CLOSED | OPEN
PUC-C02 = CLOSED | OPEN
PUC-C03 = CLOSED | OPEN

FRONTEND_DESIGN_BASELINE = web-development 0.3
FRONTEND_DESIGN_ARCHITECTURE_REOPENED = NO

OWNERSHIP_MATRIX = PASS
DEDICATED_PRODUCT_UI_COPY_SKILL = PASS | REVISE
HANDOFF_CONTRACT = PASS
WRITING_FIDELITY_BOUNDARY = PASS
PAGE_RHYTHM_OWNERSHIP = PASS
LOCALE_CONTRACT = PASS
SURFACE_AGNOSTIC_FRONTEND_TRIGGER = PASS | REVISE
PROJECT_BINDING_SEPARATION = PASS
EVALUATION_PLAN = PASS | REVISE
TRACKING_COLLISION_PLAN = PASS

PLANNED_PLUGIN_VERSIONS =
- web-development: 0.3 -> 0.4
- writing-style: 0.3 -> 0.4

PLANNED_REPOSITORY_BUMP = 5.3.1 -> 5.4.0
MATURITY_CHANGE = NONE

IMPLEMENTATION_AUTHORIZED = NO
NEXT_STEP = Planner execution-package design after Critic PASS
```

If PASS, state clearly:

- Proposal architecture only is approved;
- implementation is still unauthorized;
- no production Skill changes;
- no CUHK Date or consumer-repo mutations;
- no TODO closure;
- no version bump yet;
- no Executor Goal yet.

If REVISE, list only still-open old blockers or direct amendment regressions.
