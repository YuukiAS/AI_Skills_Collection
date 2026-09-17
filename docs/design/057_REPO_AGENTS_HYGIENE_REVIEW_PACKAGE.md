# 057 Repo AGENTS Hygiene — Review Package

Status: `AWAITING_EXECUTION_PACKAGE_CRITIC_REVIEW`

## Task identity

- Task key: `057_repo_agents_hygiene`
- Approved design proposal: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Bounded user amendment for current review: `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- Implementation Plan: `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.2
- Canonical Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.2
- Kickoff Draft: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.2
- Current execution Critic prompt: `docs/design/057_REPO_AGENTS_HYGIENE_V0_2_EXECUTION_CRITIC_PROMPT_2026-09-17.md`
- Stage: execution-ready package R2 review

## Review history

### Design review

Independent Critic approved v2 design direction:

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md
READY_FOR_EXECUTION_PLAN = YES
NEXT_HANDOFF = PLANNER
```

### Execution package v0.1

Reviewed commit:

`57f58821deecf56ee69a6504f85145ce3bdfb11e`

Decision:

```text
RESULT = REVISE
READY_FOR_CODEX = NO
```

Stable blockers:

- `C057-E1-BOBBIO-AUTHORITY-OWNER-SCOPE`
- `C057-E2-SEMINARARC-AUTHORITY-INVERSION`
- `C057-E3-SELF-REFERENTIAL-FINAL-CANDIDATE`

## v0.2 response

### E1 — ACCEPT

Bobbio scope now includes `docs/PRODUCT_DESIGN_BRIEF.md` only for source-of-truth / visual-authority wording. H2 must directly compare final:

- `AGENTS.md`
- `docs/design/FIGMA_HANDOFF.md`
- `docs/PRODUCT_DESIGN_BRIEF.md`

Final authority:

- Figma = current canonical visual design/components/screen composition;
- Product Design Brief = durable product/interaction constraints;
- old `Bobbio_Design_*.png` = historical/supporting references.

### E2 — ACCEPT

SeminarArc final ownership is explicit:

- root AGENTS = prominent non-negotiable physical-device safety summary + locator;
- `docs/DEVICE_TESTING.md` = detailed device/environment/test mechanics, command restrictions, volatile inventory and historical incident evidence.

The stale `DEVICE_TESTING -> AGENTS owns complete physical rules` wording must be repaired. Root retains Emulator-first, protected-device not generic connected-test target, no automatic transport reset/recovery, explicit verified serial + pre/postflight for authorized physical writes, independent WSL/headless/Emulator continuation, and PIN/secret non-disclosure.

### E3 — ACCEPT

Final candidate identity is now two-stage:

- Stage A evidence/result commit `E`: finalized RESULT/preservation/size/H1-H9 evidence; no self-SHA field.
- Stage B manifest commit `M`: MANIFEST records `E`, all candidate commits/Bridge version/CUHK inspected ref/H1-H9 locators; no self-SHA field for `M`.
- Executor handoff reports `AI_SKILLS_MANIFEST_COMMIT=M` externally.
- Independent implementation review targets the tuple bound by `M`.

## New bounded user amendment requiring this Critic's approval

The user additionally requires a generic version-number standard to be part of Lite Handoff so future repositories do not invent arbitrary conventions.

Authority:

`docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`

If approved, 057 additionally updates Bridge canonical `templates/prompts/AGENT_RULES.md` with a concise fallback policy:

- explicit current repo-local version policy wins;
- otherwise default `MAJOR.MINOR.PATCH`;
- PATCH compatible repair; MINOR compatible user-visible capability; MAJOR incompatible contract/migration and explicit Planner/user approval;
- `0.y.z` allowed for initial development; `1.0.0` requires explicit stability/default-use decision;
- `alpha` / `beta` / `rc` / preview/date/arbitrary prerelease suffixes are opt-in only under approved repo lifecycle or explicit current task/user authorization;
- same formal version cannot identify different user-consumable runtime candidates;
- build/commit labels do not replace the formal version;
- release-ready version/source/changelog parity must be truthful.

No H10 is added. H7 proves fresh Lite normal-entry consumption; H9 proves root does not duplicate the rule.

This amendment does not normalize existing repository version histories during 057. After 057 and 056 are integrated, the user wants a separate reviewed all-active-repo adaptation round.

## Current source refs refreshed for drafting

- Bridge main `cb77b1cc5a1fce097a38066d2db452291e359852`, `0.8.2`
- Bobbio develop `0811116ac7197590f0af773f3c6296d4ca41db80`
- Lucerna main `760931ae8a1f0edffefe41c83c1667c7190c3014`
- Mica main `aa4ce52581fff2e207d1f93600becbb3018b0efc`
- Asteria main `166791c27752c70255043f026dcbda4deb693c04`
- SeminarArc main `71c59d39f4d7e9cd3a3d813ad55d5cf6a38a4b11`
- CUHK Date main `711fab75f044b7ad31e5ff8610c076f902ccc949`

Lucerna/CUHK Date ref advancement is not an architecture redesign. Kickoff-time source authority is still rechecked.

## H1–H9

The same nine gates remain frozen:

- H1 semantic preservation
- H2 no internal contradiction, explicitly including Bobbio three-way + SeminarArc owner closure
- H3 discoverability
- H4 managed-block integrity
- H5 context quality
- H6 repo-specific regression
- H7 fresh Bridge scaffold/Lite normal entry
- H8 existing-repo should-not-change
- H9 no Lite/versioning duplication in root

No H10.

## Relationship to 056

057 remains first. After independent implementation review and separately approved integration:

```text
057 integrated
-> Planner bounded 056 source-drift revalidation
-> remove work already completed by 057
-> refresh Bridge/current refs/version slot
-> narrow Critic amendment review
-> execute 056 only after amended package approval
```

Do not redesign v6 unless 057 actually invalidates a frozen 056 architecture assumption.

## Hard boundary

This package is still a review object. No target product repo/AGENTS or Bridge production source has been modified by Planner; no 057 Executor is authorized; no 056 execution is authorized.

Only if independent Critic returns:

```text
RESULT = PASS
READY_FOR_CODEX = YES
```

for this exact v0.2 Plan + Goal + Kickoff + versioning amendment may the user send the approved Kickoff.

`NEXT_HANDOFF = CRITIC`
