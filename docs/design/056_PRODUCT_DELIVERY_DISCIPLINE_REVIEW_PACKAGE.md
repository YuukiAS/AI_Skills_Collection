# 056 Product Delivery Discipline — Review Package

状态：`AWAITING_INDEPENDENT_CRITIC_R2`

## Task identity

- Task key: `056_product_delivery_discipline`
- Review stage: Planner response to first Critic `REVISE`; pre-implementation architecture/workflow review
- Planner revision base: `main@efd6896a97977158e4641c662e5830c0088ed2b8`
- Current proposal: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Current Critic prompt: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CRITIC_PROMPT_2026-09-16.md`
- Host capability probe draft: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_DRAFT.md`
- Superseded review object: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`
- Primary maintenance inbox: `docs/plugin-todos/workflow-core.md`

## Why 056 exists

This is a major workflow-design round after task 055. The identifier binds the Planner/Critic review object and, only after independent approval and any required capability probe, a possible later implementation package.

Assigning the number does **not** authorize an execution Goal, kickoff, reviewed branch/worktree, production plugin change, Bridge Kit change, repo-specific AGENTS change, or host capability probe. The current Planner/Critic contracts still require an independent Critic decision on the explicit proposal/probe version and a separate user action to authorize any probe or implementation prompt.

## First Critic decision

First review object:

`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`

Decision:

`RESULT = REVISE`

Stable blockers:

- `C056-B1-PERSISTENT-PROMPT-CAPABILITY`
- `C056-B2-REVIEW-ADMISSION-SCOPE`
- `C056-B3-ACTIVE-RULE-CONSUMPTION`
- `C056-B4-LAYER-DUPLICATION`

Planner has produced v6 responses, but **none of these blockers is self-declared closed**. Only the independent Critic may close them.

## Planner response status for R2

| Finding | Planner response in v6 | Status before Critic R2 |
|---|---|---|
| `C056-B1-PERSISTENT-PROMPT-CAPABILITY` | Native persistent transport changed to `PROBE_REQUIRED`; separate bounded probe draft added; Default-mode native/fallback/gap semantics separated | `RESPONDED_PENDING_CRITIC / PROBE_REQUIRED` |
| `C056-B2-REVIEW-ADMISSION-SCOPE` | Hard Review Admission limited to acceptance/release/user-ready review; advisory/diagnostic/design/architecture review remains available before completion; completion scoped to frozen review object | `RESPONDED_PENDING_CRITIC` |
| `C056-B3-ACTIVE-RULE-CONSUMPTION` | Added Lucerna/Bobbio/Mica/Asteria/SeminarArc consumption matrix and default rule: active rule failure triggers consumer/fidelity diagnosis before new policy | `RESPONDED_PENDING_CRITIC` |
| `C056-B4-LAYER-DUPLICATION` | Architecture reduced to 6 Lite + 5 workflow + 3 Frontend + 1 maintainer capability; Bridge Kit transport only; repo AGENTS invariant/locator only | `RESPONDED_PENDING_CRITIC` |

## New real-world evidence since v5

Lucerna Goal `01035_longleaf_extensions_daily_surface` strengthens the design problem beyond prompt persistence. Its task explicitly authorized broad non-human work and instructed the Executor to finish all independent work before asking the user, yet the result still aggregated several different dependency classes into a Human Boundary, including local/canonical source friction, an unsupported editor interface, optional integrations and conditional/scaffold capability states.

v6 therefore requires **Human-Gate Eligibility / Dependency Triage** before user input:

```text
HUMAN_ONLY
AGENT_RESOLVABLE
UNSUPPORTED_WITH_EVIDENCE
OPTIONAL_NOT_REQUIRED_FOR_CURRENT_CLOSURE
SAFETY_OR_AUTHORITY_BLOCKER
```

Only `HUMAN_ONLY` may become an ordinary Human Decision Gate. This is integrated into W2 rather than added as another top-level capability.

v6 also adds **Vertical Capability Closure** inside W1/W3 so UI shells, setup cards, handlers, placeholders, conditional `IMPLEMENTED_WHEN_*` states and broad test suites cannot individually masquerade as a completed end-to-end feature.

For high-risk/multi-deliverable goals only, v6 permits a small task-local closure table before Human Gate / Acceptance Admission. It is evidence for the gate, not a repository ledger, schema or new state machine.

## Current review question

Determine whether v6 is now the **minimum sufficient architecture** for preventing repeated user-costly development loops while keeping ordinary small work lightweight.

The second Critic review must attack both directions:

- **too simple**: still allows half-finished candidates, Human-Gate laundering, scaffold-as-capability, proxy evidence, repeated human QA, Figma drift, unfaithful fixtures, or a falsely claimed persistent prompt;
- **too complex**: duplicates rules across Lite/workflow/domain/repo layers, forces acceptance gates on advisory reviews or small tasks, turns the closure table into a new ledger, adds unnecessary schema/state, or creates visual requirements for non-visual work.

The requested output is not a courtesy review. The Critic must re-evaluate the original four blockers against v6, review the bounded host probe as a separate executable object, and decide whether the design should proceed to the probe phase or be revised again.

## Expected next-step boundary

If architecture and probe draft both pass:

```text
NEXT_HANDOFF = USER_AUTHORIZED_CAPABILITY_PROBE
```

not implementation.

The real probe result returns to Planner/Critic before any implementation Plan/Goal/Kickoff that depends on prompt transport is frozen.
