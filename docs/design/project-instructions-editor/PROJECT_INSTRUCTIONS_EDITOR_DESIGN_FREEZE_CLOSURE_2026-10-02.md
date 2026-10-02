# Project Instructions Editor — Design Freeze Closure

Date: 2026-10-02  
Status: DESIGN_FROZEN  
Repository: `YuukiAS/AI_Skills_Collection`  
Source branch: `main`  
Tracking: #93  
Design topic: `project-instructions-editor--standalone-skill-design`

Approved architecture:

`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_PLANNER_PROPOSAL_2026-10-02.md`

Architecture Critic PASS:

`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_STANDALONE_SKILL_DESIGN_V2_CRITIC_REVIEW_2026-10-02.md`

Approved final design freeze:

`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_PLANNER_PROPOSAL_2026-10-02.md`

Design-freeze Critic PASS:

`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md`

Design-freeze review commit:

`bf9add585924e93ab8844bb59a366f1cd4f837d6`

```text
DESIGN_FREEZE=PASS
READY_FOR_FUTURE_SKILL_DESIGN=YES
READY_FOR_SKILL_IMPLEMENTATION=NO
```

## 1. Closure decision

The pre-implementation product and architecture design is frozen.

No new product fact was found that reopens the approved architecture. The independent Critic concluded that future implementation no longer needs to decide what this Skill is, what it owns, when it should trigger, how the edit modes differ, how missing inputs degrade, how Project-local enforcement differs from semantic ownership, or what real user capabilities must eventually be demonstrated.

This closure is planning-only. It does not authorize implementation planning, Skill creation, Codex execution, trigger evals, packaging, installation, release, or publication.

## 2. Frozen product contract

The following are frozen and must not be re-decided by a future implementation unless new direct evidence forces a Planner–Critic design revision.

### Product responsibility

`project-instructions-editor` owns long-lived ChatGPT Project instruction placement/editing across the actual live setting, relevant history, canonical sources, effective Project enforcement, and finite instruction budget.

It does not own generic prompt optimization, global Custom Instructions, ordinary prose polishing, scientific document structural rewrite, AI_Skills repository maintenance, or complex workflow execution/control.

### Trigger boundary

Natural user requests to create, modify, compress, synchronize, or restructure long-lived ChatGPT Project instructions belong to this Skill even when the user does not name it.

Near-miss ownership remains with:

- `chinese-prose` for ordinary Chinese prose;
- `writing-fidelity` for ordinary writing-fidelity tasks;
- `scientific-rewrite` for scientific/technical structural rewriting;
- `workflow-core` for complex process/control;
- `ai-skills-core` for AI_Skills_Collection repository maintenance.

A wording-only pass over already-selected Project text does not automatically require the full Project-editor reasoning path.

### Three edit modes

Frozen modes:

1. preservation-sensitive;
2. greenfield;
3. explicit reset.

Preservation-sensitive replacement requires a sufficiently complete live baseline before claiming preservation of unmodified semantics.

Greenfield or explicit reset may produce a full setting without an old baseline, but cannot claim preservation of unknown old Project-setting rules.

### Inputs and degradation

Frozen inputs:

- current edit request;
- live Project setting when preservation requires it;
- relevant targeted Project history;
- canonical project sources;
- actual/user-provided instruction budget when known.

Missing inputs degrade only the affected claim or edit scope. The Skill must not fabricate a safe full replacement, exhaustive history, current canonical rule, or unknown hard-limit compliance.

### Semantic ownership and effective enforcement

Every affected durable rule must distinguish:

- where its current detailed truth is maintained;
- where enough of that rule must actually appear for the current Project to be constrained.

A canonical external source may own the detail while the Project still needs a direct semantic subset or bridge/trigger.

### Locator boundary

Detail may move behind a locator only when lookup happens early enough, the locator is usable, the Project retains any required trigger, and mandatory/optional meaning, authority, safety, evidence strength, and uncertainty remain unchanged.

### Protected absence

When relevant history is partial or unavailable, an old-only durable rule absent from the live baseline remains absent by default.

It may be reintroduced only by current explicit user re-adoption or an explicitly authorized synchronization from the rule's current canonical owner.

This is a current-edit protection rule, not a persistent tombstone registry.

### Mutation radius

Bounded edit is the default.

Full rewrite/restructure requires a real cross-cutting reason such as an explicit user request, unresolved cross-scope contradiction, pervasive copied workflow detail, material multi-scope imbalance, budget impossibility under local repair, or systemic source/locator drift.

Recency and cosmetic cleanliness are not sufficient reasons.

### No-op

“No Project-setting change” is a valid product result when the requested behavior is already covered or belongs to another canonical/task owner.

### User delivery contract

Delivery remains proportional to edit risk:

- bounded edits show the substantive change, reason, protected semantics, and length/delta when available;
- medium edits add scope/locator/enforcement/budget impact only when relevant;
- full replacements state the edit mode, major placement changes, protected invariants, budget effect, and complete clean replacement;
- missing-input cases return only what is safely supportable;
- no-op identifies why no Project-setting mutation is needed.

## 3. Frozen future capability families

Future implementation and release planning must preserve four distinct capability families rather than mechanically converting the A–L regression bank into twelve Gates.

### Gate family 1 — Normal entry / routing boundary

Proves ordinary users can reach the Skill from natural Project-instruction editing requests and that near-miss tasks remain with their correct owners.

### Gate family 2 — Core Project editing semantics

Proves the three edit modes, input degradation, ownership/enforcement reasoning, locator decisions, protected absence, bounded/full edit, no-op, and budget behavior.

### Gate family 3 — Fidelity / authority / should-not-change

Proves the requested edit does not silently weaken mandatory/optional meaning, authorization, safety, permission, evidence strength, uncertainty, exact identifiers, user corrections/deletions, unrelated live scope, or adjacent owner behavior.

### Gate family 4 — Representative complete task + qualitative final artifact

Proves the same final candidate works on representative complete long/multi-scope Project tasks from normal entry through final setting/no-op/advice, with complete-input and full-output qualitative review.

This family also carries final-candidate identity, fixed-source/ref discipline, and risk-matched fresh generalization.

A–L remain regression/task-family evidence that can be assigned to these Gate families. Gate splitting requires a genuinely different capability, evidence type, failure semantics, normal entry, or owner/risk boundary.

## 4. What remains implementation-time detail

The frozen design intentionally leaves these for a later explicitly authorized implementation phase:

- exact Skill directory/file layout;
- final `SKILL.md` prose;
- exact description wording;
- whether a deterministic character-count/diff helper is useful;
- concrete trigger eval queries;
- regression fixture selection;
- test commands;
- install/validation mechanics;
- version/release/package details.

These decisions must implement the frozen contract rather than revise it.

If implementation evidence shows the frozen contract cannot work, the task returns to Planner–Critic instead of narrowing the product silently.

## 5. Maintenance state

Canonical tracking remains:

```text
tracking: #93
```

Issue #93 remains open with:

```text
maintenance-track
kind:new-capability
scope:standalone-skill
area:standalone-skill
```

The target Project lifecycle remains:

```text
Project = AI Skills Maintenance
Issue = #93
Status = DOING
Area = standalone-skill
current design anchor =
docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_PRE_IMPLEMENTATION_DESIGN_FREEZE_V1_CRITIC_REVIEW_2026-10-02.md
```

The current runtime exposes no GitHub Project field mutation surface, so this is an exact pending mutation, not a claim that the Project has been synchronized.

Issue #93 reader-facing copy is still stale. `AI_SKILLS_MAINTENANCE_BOARD.md` requires a real current Clear Writing invocation before substantive Issue-copy changes. No verifiable Clear Writing invocation surface is available in this runtime:

```text
CLEAR_WRITING_UNAVAILABLE
```

Therefore Issue #93 is not substantively rewritten in this closure.

The next reader-facing Issue update, when Clear Writing is actually available, should state that the final design freeze passed and that the item is waiting for an explicit future user decision on implementation planning/implementation.

## 6. Stop condition

This design phase is closed.

Do not automatically:

- create `skills/.../project-instructions-editor/`;
- create `SKILL.md` or `agents/openai.yaml`;
- create trigger evals;
- create an implementation Goal or Kickoff;
- create a Plugin;
- change README, VERSION, registry, catalog, Marketplace, profile, or release metadata;
- start Codex implementation.

Wait for an explicit future user instruction before entering implementation planning or implementation.

```text
DESIGN_FREEZE=PASS
READY_FOR_SKILL_IMPLEMENTATION=NO
```
