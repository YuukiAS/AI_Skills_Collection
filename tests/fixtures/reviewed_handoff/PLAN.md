---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: <TASK_KEY>
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Explain what problem this task will solve and why the change is useful.

## Frozen decisions

State the semantic/product/architecture decisions that Codex must not reinvent.

## Positive completion

State the real user, product, scientific, or repository observable outcome that
would make this task complete. Tests, CI, file existence, package validation, or
absence of forbidden tokens cannot alone define positive completion unless the
task target is exactly that mechanism. Also state the maximum claim scope that
the required evidence may support.

## Non-substitutable semantics

Record the few core semantics that decide whether this remains the same task.
Codex must not silently weaken required data, method, scale, execution entry,
artifact, renderer, model/source, budget, or quality bar. If an equivalent
fallback is allowed, say why it is equivalent and what evidence must prove that
equivalence.

## Implementation scope

List the intended modules/files/capabilities and how conflicts or overlaps are resolved.

## Acceptance and regression gates

Define observable completion criteria and behaviors that must not degrade.

## Natural-language usage / routing expectations

Give realistic examples of how a user would invoke or benefit from the capability when relevant.

## Out of scope

List tempting adjacent improvements that Reviewer must not turn into blocking scope.
