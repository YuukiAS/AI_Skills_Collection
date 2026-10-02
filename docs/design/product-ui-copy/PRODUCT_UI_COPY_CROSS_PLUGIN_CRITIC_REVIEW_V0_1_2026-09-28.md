# Product UI Copy Cross-Plugin — Independent Critic Review v0.1

Date: 2026-09-28  
Review object: `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_1_2026-09-28.md`  
Reviewed commit: `d1b3a13435cb51e9503f9fe6cbfd1b4b064aadd1`  
Source note: **This file archives the independent Critic result supplied to the Planner by the user. The Planner did not originate or alter the verdict.**

```text
RESULT = REVISE
FRONTEND_DESIGN_BASELINE = web-development 0.3
FRONTEND_DESIGN_ARCHITECTURE_REOPENED = NO
IMPLEMENTATION_AUTHORIZED = NO
```

## Overall assessment

The Critic accepted the core direction and did not require reopening Frontend Design 0.3.

Accepted architecture included:

- the three-owner boundary:
  - product/domain/legal authority owns truth and user consequence;
  - Frontend Design owns whether/where/how much to say, hierarchy and rendered acceptance;
  - Clear Writing owns natural-language realization under frozen meaning;
- a dedicated `product-ui-copy` sibling Skill as a justified design direction;
- the lightweight Frontend → Writing handoff;
- the `writing-fidelity` protected-meaning boundary;
- Writing first-pass linguistic page rhythm + Frontend final rendered rhythm;
- independent zh-Hans / zh-Hant-HK realization;
- project-local binding separation;
- tracking-collision repair direction;
- planned versions:
  - `web-development 0.3 -> 0.4`
  - `writing-style 0.3 -> 0.4`
  - repository `5.3.1 -> 5.4.0`
  - maturity unchanged.

Three blockers remained.

---

## PUC-C01 — Clear Writing trigger metadata still conflicts with the new sibling

**Requirement**

After adding `product-ui-copy`, ordinary Product UI Copy requests must reliably route to it, while reports/README/scientific Chinese remain on `chinese-prose`.

**Direct evidence**

Current `chinese-prose` frontmatter description says that essentially any Chinese reader/user-facing content should automatically trigger that Skill. That description can capture Product UI Copy before the model ever loads the body-level negative-route note.

OpenAI's current Skills documentation says the model first sees Skill metadata, including name and description, and uses that metadata to decide whether to consider/load the Skill.

**Causal risk**

A new sibling can exist in source but remain unreliable in normal routing because the older broad `chinese-prose` description still overlaps UI copy.

**Minimal closure condition**

Proposal v0.2 must explicitly freeze:

- positive `product-ui-copy` frontmatter trigger metadata for UI label/CTA/status/help/error/onboarding/settings/trust/localization;
- a narrowed `chinese-prose` **frontmatter description** that excludes Product UI microcopy while preserving long-form behavior;
- no rewrite of the working `chinese-prose` long-form mechanism;
- direct / indirect / near-miss / negative activation evals covering competition between the two Skills;
- execution planning must check/update `writing-style` plugin-level description/default prompts for Product UI Copy discovery.

Owner: Planner.

---

## PUC-C02 — Fresh holdout frozen before implementation is not fresh

**Requirement**

Fresh holdout evidence must not be visible to the candidate during development/tuning.

**Direct evidence**

Proposal v0.1 said:

> Freeze before implementation a compact scenario batch.

The same exact batch was then intended to support final fresh-holdout evidence.

**Causal risk**

If Executor can see exact holdout scenarios before or during implementation, it can tune triggers/taxonomy/wording to them. A later PASS then proves known regression, not fresh generalization.

**Minimal closure condition**

Use either:

1. pre-implementation freeze only of holdout task families/coverage/rubric; exact final batch is frozen only after final candidate + review criteria are frozen; or
2. exact batch is frozen by an independent owner but remains unavailable to Executor until final candidate freeze.

Preserve:

- one complete final batch;
- no replacement/chasing after failure;
- once the candidate is changed based on the batch, that batch is no longer fresh.

Owner: Planner.

---

## PUC-C03 — Mobile/Compose auto-trigger lacks a real normal-entry replay

**Requirement**

The explicit user requirement is cross-surface normal triggering: browser extension, web, desktop and mobile. Mobile cannot be claimed from metadata/fixtures alone.

**Direct evidence**

Proposal v0.1 explicitly included:

- mobile / Android / Compose — SeminarArc

but the independent real-project replay set only included Lucerna and Mica.

Current SeminarArc authority includes project-local:

- `android-lead`
- `compose-expert`

So the real question is not only whether “mobile” keywords trigger Frontend Design; it is whether:

```text
natural mobile UI task
→ Frontend Design generic product-interface coordinator
→ android-lead / compose-expert keep Android/Compose implementation authority
```

and, conversely:

```text
Room / WorkManager / data-layer task
→ does not activate Frontend Design
```

**Causal risk**

A release could prove desktop + extension compatibility while still failing the explicit mobile requirement or stealing platform/data-layer ownership.

**Minimal closure condition**

Add a read-only SeminarArc final-candidate normal-entry replay:

- one natural Compose/UI task proving automatic Frontend Design entry;
- preserve `android-lead` / `compose-expert` platform semantics;
- one Room/WorkManager/data-only negative control proving no false trigger;
- do not modify SeminarArc;
- do not count this as maturity promotion evidence.

Owner: Planner.

---

## Accepted review matrix

```text
OWNERSHIP_MATRIX = PASS
DEDICATED_PRODUCT_UI_COPY_SKILL = REVISE
HANDOFF_CONTRACT = PASS
WRITING_FIDELITY_BOUNDARY = PASS
PAGE_RHYTHM_OWNERSHIP = PASS
LOCALE_CONTRACT = PASS
SURFACE_AGNOSTIC_FRONTEND_TRIGGER = REVISE
PROJECT_BINDING_SEPARATION = PASS
EVALUATION_PLAN = REVISE
TRACKING_COLLISION_PLAN = PASS

PLANNED_PLUGIN_VERSIONS =
- web-development: 0.3 -> 0.4
- writing-style: 0.3 -> 0.4

PLANNED_REPOSITORY_BUMP = 5.3.1 -> 5.4.0
MATURITY_CHANGE = NONE
```

## Maintenance Board note from Critic

The Critic did not claim Project fields were synchronized.

Pending mutation remains:

- Issue #17: `TODO -> DOING` if still TODO; anchor = current Product UI Copy Proposal; next = Planner v0.2 then Critic re-review.
- Issue #13: dependency-only / TODO.
- Frontend Product UI Copy heading: create a unique Issue and replace collided `#73`; Project = DOING.
- writing-style Product UI Copy naturalness heading: create a unique Issue and replace collided `#20`; Project = DOING.
- Do not ask the user to maintain the Project manually.
