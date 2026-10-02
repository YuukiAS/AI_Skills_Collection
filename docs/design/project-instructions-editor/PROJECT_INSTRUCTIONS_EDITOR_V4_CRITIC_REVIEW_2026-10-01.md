# Project Instructions Editor — v4 Critic Review

Date: 2026-10-01  
Source: user-forwarded independent Critic review  
Reviewed proposal: `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_V4_PLANNER_PROPOSAL_2026-10-01.md`  
Reviewed main: `231f21b970c6159e76c571bad30ca2d9af8a8aaa`

```text
CRITIC_RESULT=REVISE

CURRENT_MAIN=231f21b970c6159e76c571bad30ca2d9af8a8aaa

PLANNING_ONLY_STATE_VERIFIED=YES

PRODUCTION_SKILL_EXISTS=NO

README_RELEASE_SURFACE_CHANGED=NO

VERSION_CHANGED_FOR_THIS_WORK=NO

MARKETPLACE_CHANGED_FOR_THIS_WORK=NO
```

## Overall decision

The v4 three-layer direction is accepted and close to freeze. No standalone Skill implementation is authorized.

Two architecture blockers remain.

## Blocker 1 — governance semantic-preservation acceptance is missing

The proposal already says Sections 1–18 may receive language normalization only and that governance semantics must not change. The regression plan, however, does not explicitly verify that semantic preservation after the rewrite.

The risk is real: a readability rewrite could accidentally weaken “must” into “usually,” merge independent trigger conditions, drop exceptions, widen Planner/Critic authority, or soften evidence requirements.

Minimum closure:

- explicitly state that Sections 1–18 may receive only local natural-language normalization;
- do not reorder, merge, delete, summarize, or redesign governance rules as part of this readability edit;
- before real Project regression, compare current and candidate instructions and verify that roles, triggers, permissions, authorization, safety, evidence, Bridge, Capability Gate, release, resource, and research-integrity semantics are unchanged;
- exact identifiers must remain exact.

Root-cause wording must also remain bounded: Project governance language is a credible contributing factor to residual English leakage, not a proven unique cause. Old threads, Project files, and model expression inertia may also contribute.

## Blocker 2 — final user-reading rewrite needs a semantic invariant

The final user-reading rewrite principle is approved in direction, but v4 protects exact identifiers more explicitly than it protects the strength of natural-language conclusions.

Minimum closure:

> The final user-reading rewrite may change expression and information organization only. It must not change factual conclusions, conditional relationships, mandatory/optional meaning, authorization or safety state, evidence strength, uncertainty, or conclusion boundaries.

A regression case must contain at least:

- one mandatory condition;
- one authorization state;
- one uncertain conclusion;
- one PASS/REVISE result.

The rewritten answer should be easier to read while preserving all four semantic strengths.

## Maintenance tracking

The Critic also observed that `docs/skill-todos/project-instructions-editor.md` did not yet have a tracking locator even though substantive design had begun.

Required maintenance action at the next writable Planner step:

- create or bind a tracking Issue;
- move the maintenance item to DOING in the AI Skills Maintenance Project when a Project-mutation surface is available;
- write `tracking: #N` into the canonical TODO;
- set the current design anchor to the revised proposal.

This tracking gap is a repository workflow item, not a reason to redesign the v4 architecture.

## Future Skill state

```text
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

Future implementation remains blocked until the user explicitly opens that phase.
