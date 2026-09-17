# 057 Repo AGENTS Hygiene — Review Package

Status: `AWAITING_EXECUTION_PACKAGE_CRITIC_REVIEW`

## Task identity

- Task key: `057_repo_agents_hygiene`
- Approved design proposal: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Superseded proposal: `docs/design/057_REPO_AGENTS_HYGIENE_PROPOSAL_2026-09-17.md`
- Design Critic prompt: `docs/design/057_REPO_AGENTS_HYGIENE_V2_CRITIC_PROMPT_2026-09-17.md`
- Implementation Plan: `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.1
- Canonical Goal: `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.1
- Kickoff Draft: `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.1
- Execution-package Critic prompt: `docs/design/057_REPO_AGENTS_HYGIENE_EXECUTION_CRITIC_PROMPT_2026-09-17.md`
- Stage: execution-ready package review

## Design review decision

The user relayed the independent Critic decision for v2:

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md
READY_FOR_EXECUTION_PLAN = YES
NEXT_HANDOFF = PLANNER
```

This PASS approves the v2 design direction only. It does not authorize execution.

## Purpose

057 has two approved design goals before Task 056 implementation:

1. semantics-preserving cleanup of each target repository's **own** instruction surface — within-repo duplication, contradiction, stale authority, discoverability and structure;
2. add a reusable **project-owned root `AGENTS.md` scaffold** to Bridge Kit so future fresh repositories do not begin with only a handoff block and then accumulate rules incident-by-incident.

The scaffold standardizes structure/ownership, not project content. `prompts/AGENT_RULES.md` remains the Lite/execution-rule owner; the root template must not duplicate it.

## Execution package v0.1

The exact execution-review bundle is:

1. `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.1
2. `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.1
3. `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` v0.1

The package proposes task isolation branches `reviewed/057_repo_agents_hygiene` for AI_Skills evidence, Bridge Kit, Bobbio, Lucerna, Mica, Asteria and SeminarArc. CUHK Date remains inspect-only.

Bridge Kit candidate behavior:

- new `templates/repo/AGENTS_TEMPLATE.md`;
- fresh `ai-bridge init` consumes scaffold + exactly one managed Bridge block;
- existing repo and `--force` preserve project-owned root text;
- no automatic migration of existing repos;
- no Lite duplication;
- conditional patch candidate `0.8.2 -> 0.8.3` only after H7–H9 and regression gates pass.

Existing-repo implementation is bounded:

- Bobbio: substantial reorganization + Figma canonical locator/authority clarification, no product/Figma/runtime change;
- Lucerna: light root normalization only;
- Mica: testing-section consolidation only;
- Asteria: root map conversion + `docs/operations/development/RUNTIME_OPERATIONS.md` for moved volatile operations;
- SeminarArc: root map conversion + `docs/DEVICE_TESTING.md` as detailed device/environment owner;
- CUHK Date: inspect only, no root creation.

## H1–H9

The execution package freezes these gates:

- H1 semantic preservation
- H2 no internal contradiction
- H3 discoverability
- H4 managed-block integrity
- H5 context quality
- H6 repo-specific regression
- H7 fresh Bridge scaffold normal entry
- H8 existing-repo should-not-change
- H9 no Lite duplication

Success is not measured by line-count reduction alone.

## Relationship to 056

The already execution-ready-PASS 056 package is not redesigned by 057 and must remain unexecuted while the user wants 057 completed first.

Required sequence:

```text
057 execution-package Critic review
-> user sends exact approved 057 Kickoff
-> 057 implementation on isolated task branches
-> independent implementation review
-> separately approved integration
-> return to 056
-> bounded source-drift revalidation/package amendment
-> no v6 redesign unless 057 actually invalidates a frozen 056 assumption
```

The later 056 revalidation must remove duplicate work already completed by 057, refresh exact refs, and choose the then-valid Bridge patch version if 057 consumed `0.8.3`.

## Hard boundary

No product repo file has been modified by the Planner. No Bridge Kit production source has been modified. No branch/worktree has been created. No Executor is authorized. No 056 implementation has started.

Only if independent Critic returns both:

```text
RESULT = PASS
READY_FOR_CODEX = YES
```

for this exact v0.1 Plan + Goal + Kickoff may the user send the approved Kickoff and thereby authorize execution.

`NEXT_HANDOFF = CRITIC`
