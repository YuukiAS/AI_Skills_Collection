# Project Instructions Editor Contract

This reference is the stable contract for editing long-lived ChatGPT Project instructions. Load it when the request involves preservation-sensitive edits, finite budgets, locator substitution, multi-scope balancing, full replacement, partial history, or review evidence.

## Product Boundary

The skill owns semantic placement for ChatGPT Project instructions:

- what belongs directly in the Project setting;
- what should remain behind a canonical source locator;
- what should stay in the current task or thread;
- what must be protected because it is already accepted, corrected, deleted, uncertain, safety-sensitive, or outside the authorized scope.

It does not own ordinary prose polishing, generic system prompts, global Custom Instructions, AI_Skills repository maintenance, workflow state management, Project history storage, database/ledger construction, watcher behavior, live ChatGPT account mutation, external finalization services, or cross-turn final reader-layer guarantees.

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

## Durable Semantic Map

For complex edits, compression, synchronization, or full replacement, first form
a durable semantic map. The map is internal reasoning, not normal user-facing
output. It groups live setting clauses, current-request changes, targeted
history, and canonical-source facts by long-lived meaning.

The map prevents two common failures:

- copying source/history surface labels directly into the Project setting;
- letting several near-duplicate clauses survive because they came from
  different sources.

Each meaning receives one current disposition:

1. direct Project-resident rule;
2. short locator bridge or trigger plus canonical source locator;
3. source-only;
4. task/thread only;
5. another verified effective layer;
6. omit or no change.

Disposition is semantic, not phrase matching. It depends on current support,
effective enforcement, durability, lookup-before-action needs, budget, and
should-not-change semantics.

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

If a deleted or rejected rule is already absent from the live Project setting, the final long-lived setting should normally omit both the deleted rule and its deletion history. Use the deletion evidence internally to avoid reintroducing the rule, but do not emit `do not restore X`, `X was deleted`, or any equivalent Project-resident tombstone unless the current user explicitly asks to preserve that prohibition or history marker as durable Project state.

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

## Expansion, Coverage, and Redundancy

Project instructions should grow only when the growth corresponds to a real
long-lived semantic change or repair. A new or materially changed
Project-resident rule needs current semantic support from at least one of:

- the live Project setting;
- the current request;
- a current canonical authority in the requested synchronization scope;
- explicit current re-adoption by the user;
- a necessary lookup-before-action bridge.

Do not create durable rules whose only support is stale history, old generated
candidates, rejected/deleted history, source wrapper wording, task-local
commentary, or review/audit labels. Keep the underlying deleted/rejected rule
absent and keep its deletion history out of the final setting unless the current
user explicitly asks to preserve that history or prohibition as durable Project
state.

Before delivering a complete candidate, run a final semantic coverage and redundancy review against the actual candidate text:

- required live/current/canonical meanings remain covered;
- protected absence remains absent;
- unsupported durable rules are absent;
- repeated clauses with the same semantic effect are consolidated;
- source-owned volatile detail has either a valid locator bridge or is omitted;
- authorization, safety, privacy, evidence strength, uncertainty, completion
  claims, exact identifiers, and mandatory/optional force remain unchanged;
- known hard budget and headroom are still satisfied.

This review is not an English-token scan, blacklist, translation table,
percentage score, or fixed-section template.

## No-Op Eligibility

Before returning no-op, review the live Project setting itself within the current user's requested scope. Treat it as the candidate and check whether it already satisfies active contracts for placement, semantic ownership, durability, safety, privacy, authorization, evidence strength, fail-closed behavior, and mandatory/optional force.

No-op is valid when the setting already satisfies those contracts, when the remaining difference is only cosmetic preference, or when changing it would duplicate, weaken, misplace, overfit, or add semantic risk.

No-op is not eligible when the editor identifies a material live-setting defect in scope and a bounded edit or bounded consolidation can fix it without weakening unrelated semantics. Material defects include a clear wrong owner or placement, volatile implementation or inventory detail that has a stable canonical source owner, duplicate detail that creates long-term maintenance burden, or another issue the current user explicitly asked the editor to check.

When the material defect is volatile implementation, inventory, status, or client/detail copied from a stable canonical source, the bounded repair should keep a short trigger and locator bridge and omit the copied volatile list or detail unless a specific item is truly needed before lookup for routing, authorization, safety, or exact identity.

Appropriate Project-resident repetition may still be kept when it improves effective enforcement before lookup. That does not justify ignoring a separate acknowledged defect that is safely repairable.

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

Exact identifiers include paths, commands, branch names, repository names, versions, state values, fields, model identifiers, and other tokens that need exact matching. Ordinary prose can be edited for the current Project setting, but exact identifiers must remain exact when future work depends on exact spelling.

## Runtime Boundary

PIE v0.1 uses `FINAL_ROUTE=SIMPLE_FORMAL_CORE`.

It runs as an ordinary ChatGPT Web / Project chat Skill. It does not require and must not claim an MCP finalizer, `OPENAI_API_KEY`, external model provider, sibling Skill chain, hosted service, or extra paid API call for normal operation.

PIE v0.1 may produce a clear, concise Project setting for the current edit, including natural Chinese when the current user or Project calls for it. It must not claim to guarantee cross-turn final reader-layer behavior for future chats. C11 evidence remains a preserved failure boundary: advanced multi-call or cross-turn reading-layer finalization is unsupported in PIE v0.1 and belongs to future Clear Writing work.

When the active Project setting or current request calls for Chinese-facing
Project instructions, the current replacement should express ordinary source
labels and descriptive prose naturally in Chinese while preserving exact
machine/formal identifiers. This narrow current-artifact language responsibility
does not make PIE v0.1 the owner of future cross-turn reader-layer enforcement.

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
- no-op eligibility when a material in-scope defect has a safe bounded repair;
- should-not-change checks for authorization, safety, evidence strength, exact identifiers, and explicit user deletion/correction.

Do not convert regression examples into mechanical surface-form scoring or fixed layout quotas.

## User Delivery

Keep the response proportional to edit risk.

Small bounded edits should be concise: decision, concrete edit, short reason, key preserved semantics, and length/delta when available.

Medium edits may add scope impact, locator/bridge reasoning, enforcement placement, balance, and budget margin.

Full replacements must include mode, reason bounded edit is insufficient or reset/greenfield applies, major placement changes, direct rules/bridges, preserved invariants, budget change, and a clean complete replacement.

Missing-input outputs must avoid false-safe full settings. Name only the input that truly blocks safe completion and provide safe partial work.

No-op is valid only when the setting already satisfies the active contract, the remaining difference is cosmetic, or changing Project settings would duplicate, weaken, misplace, overfit, or add semantic risk.

Normal user-facing answers should be concise and should not expose internal
preservation-sensitive labels, semantic maps, disposition tables, invariant
checklists, or coverage/redundancy reviews unless the user asks for audit
evidence. The default delivery is a short conclusion, the bounded edit or clean
replacement when safe, and a few key reasons.
