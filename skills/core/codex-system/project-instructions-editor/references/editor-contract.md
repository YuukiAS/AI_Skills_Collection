# Project Instructions Editor Contract

This reference is the stable contract for editing long-lived ChatGPT Project instructions. Load it when the request involves preservation-sensitive edits, finite budgets, locator substitution, multi-scope balancing, full replacement, partial history, or review evidence.

## Product Boundary

The skill owns semantic placement for ChatGPT Project instructions:

- what belongs directly in the Project setting;
- what should remain behind a canonical source locator;
- what should stay in the current task or thread;
- what must be protected because it is already accepted, corrected, deleted, uncertain, safety-sensitive, or outside the authorized scope.

It does not own ordinary prose polishing, generic system prompts, global Custom Instructions, AI_Skills repository maintenance, workflow state management, Project history storage, database/ledger construction, watcher behavior, or live ChatGPT account mutation.

## Modes

### Preservation-Sensitive

Use when an existing Project setting is in force and the user has not explicitly discarded unrelated semantics. A full replacement, deletion pass, compression, or global reorganization requires a sufficiently complete live baseline. Without that baseline, the safe output is bounded advice, a clause, a placement recommendation, or a request for the live setting.

### Greenfield

Use only when Project instructions are confirmed empty or absent. A complete initial setting may be drafted, but it must still respect current user scope, canonical sources, safety, privacy, and known budget.

### Explicit Reset

Use only when the current user clearly authorizes discarding the old Project setting and rebuilding from zero. Reset does not override higher-priority instructions, workspace policy, repository authority, privacy, safety, or the current request's limits.

## Inputs and Degradation

`current request` is always required. It defines the edit scope and current authorization.

`live setting` is required for preservation-sensitive full replacement, deletion, compression, and global reorganization. A stale candidate, reference snapshot, summary, or repository draft is not a replacement for the live setting.

`targeted history` means reading only decision history relevant to the current edit: acceptance, rejection, explicit deletion, repeated correction, durable authority, or temporary status. Missing history should produce honest uncertainty, not broader search by default.

`canonical source` is needed when the requested edit depends on current repository, document, workflow, policy, version, task, or locator facts. If the source is unavailable, block only the claim that depends on it unless that claim governs the whole replacement.

`budget` includes current length, candidate length, delta, hard product limit when known, planning budget, remaining margin, and requested headroom. Do not turn a historical planning budget such as 8000 characters into a universal product rule.

## Ownership and Enforcement

For every affected durable rule, decide both:

- semantic ownership: where the detailed, current, maintainable truth belongs;
- effective enforcement placement: where the rule must appear so this Project actually follows it before acting.

Allowed dispositions for the current edit are:

1. direct Project-resident rule;
2. short Project-resident bridge or trigger plus canonical source locator;
3. canonical-source only;
4. task/thread only;
5. another verified effective layer;
6. omit or no change.

Semantic ownership alone is not enough to remove a rule from Project settings. Rules about routing, authority, authorization, safety, privacy, distribution, evidence, completion, output contract, and lookup-before-action often need a direct Project subset or bridge even when their details live elsewhere.

## Locator Substitution

Move detail out of Project instructions only when all are true:

- the locator is stable and resolvable;
- the relevant future task will look it up before acting;
- the removed detail is not required before lookup;
- the Project setting keeps the trigger or bridge that causes lookup;
- mandatory/optional force, authority, permission, safety, evidence strength, uncertainty, and exact identity are not weakened;
- the external source is genuinely the current semantic owner.

The point is maintainable recovery, not pushing all text out of Project instructions.

## Protected Absence

When history is partial or unavailable, a durable rule absent from the live baseline and present only in an old candidate, reference, summary, or generated historical setting remains absent by default.

Reintroduce it only when:

- the current user explicitly adds or re-adopts it; or
- the current task explicitly synchronizes a named canonical source, and that source currently supports the rule within the requested synchronization scope.

Protected absence does not create a permanent tombstone registry. It is a conservative rule for the current edit.

## Bounded Edit and Full Rewrite

Bounded edit is the default. Keep unrelated valid semantics intact and make the smallest change that closes the current request.

Use full rewrite or restructure only when at least one real condition holds:

- the user explicitly requests and authorizes it;
- local edits cannot resolve a cross-cutting contradiction;
- copied workflow detail has polluted the setting broadly;
- multiple scopes are materially imbalanced;
- required durable semantics cannot fit the budget through local deduplication and locator substitution;
- source ownership or locator use has systematically drifted or conflicted.

"It would be cleaner" or "the recent topic is important" is not enough. Preservation-sensitive full rewrite also requires a live baseline and enough current facts to preserve affected semantics.

## Semantic Invariants

Never silently weaken or alter:

- mandatory versus optional force;
- trigger or escalation conditions;
- authority, permission, and authorization boundaries;
- safety, privacy, and distribution boundaries;
- evidence strength and completion claims;
- role ownership and adjacent skill ownership;
- uncertainty, negative findings, and current-versus-future status;
- exact machine or formal identifiers;
- current user explicit corrections, deletions, rejections, or acceptances;
- unrelated live scopes.

Exact identifiers include paths, commands, branch names, repository names, versions, state values, fields, model identifiers, and other tokens that need exact matching. Ordinary prose does not become exact merely because its source is in English.

## Regression Families

Use these families as review coverage, not as a fixed gate count:

- normal unnamed Project-instruction editing and near-miss routing;
- stale candidate versus live setting;
- multi-scope Project under finite budget;
- source-drift controlled synchronization;
- preservation-sensitive replacement with missing live baseline;
- greenfield and explicit reset;
- locator substitution with lookup-before-action requirements;
- protected absence under partial history;
- no-op when the correct owner is a canonical source or already-covered rule;
- should-not-change checks for authorization, safety, evidence strength, exact identifiers, and explicit user deletion/correction.

Do not convert regression examples into banned-word tables, English ratios, keyword scorers, fixed paragraph counts, fixed heading counts, fixed formula counts, or fixed character-per-section quotas.

## User Delivery

Keep the response proportional to edit risk.

Small bounded edits should be concise: decision, concrete edit, short reason, key preserved semantics, and length/delta when available.

Medium edits may add scope impact, locator/bridge reasoning, enforcement placement, balance, and budget margin.

Full replacements must include mode, reason bounded edit is insufficient or reset/greenfield applies, major placement changes, direct rules/bridges, preserved invariants, budget change, and a clean complete replacement.

Missing-input outputs must avoid false-safe full settings. Name only the input that truly blocks safe completion and provide safe partial work.

No-op is valid when changing Project settings would duplicate, weaken, or misplace the rule.
