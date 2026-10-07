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

`canonical source` is needed when the requested edit depends on current repository, document, workflow, policy, version, task, inventory, or locator facts. If the source is unavailable, block only the claim that depends on it unless that claim governs the whole replacement.

`budget` includes current length, candidate length, delta, hard product limit when known, planning budget, remaining margin, and requested headroom. Do not turn a historical planning budget such as 8000 characters into a universal product rule.

## Ownership and Enforcement

For every affected durable rule, decide both:

- semantic ownership: where the detailed, current, maintainable truth belongs;
- effective enforcement placement: where the rule must appear so this Project actually follows it before acting.

Allowed dispositions for the current edit are:

1. direct Project-resident rule;
2. short locator bridge or trigger plus canonical source locator;
3. canonical-source only;
4. task/thread only;
5. another verified effective layer;
6. omit or no change.

Semantic ownership alone is not enough to remove a rule from Project settings. Rules about routing, authority, authorization, safety, privacy, distribution, evidence, completion, output contract, and lookup-before-action often need a direct Project subset or bridge even when their details live elsewhere.

## Known-Good Candidate Construction

The known-good editing behavior is intentionally simple:

```text
live setting + current request + necessary current source facts
-> identify durable user-facing rule groups
-> consolidate duplicates
-> move volatile detail behind stable source bridges
-> preserve current semantic force
-> emit clean replacement
```

Use the live setting as semantic evidence, not as a paragraph-by-paragraph scaffold. Source headings, source labels, old section names, source order, duplicated rationale, and document grouping are not protected by default. They may be merged, renamed, reordered, or omitted when the durable meanings remain covered.

Group rules by governed actor or surface, trigger or phase, owner or authority, intended behavior or prohibition, and user consequence. Merge clauses with the same normal trigger and user consequence into one primary durable home. Keep a distinct family only when the trigger, governed surface, owner, or consequence is materially different.

Project instructions should grow only when growth corresponds to a real long-lived semantic change or repair. A new or materially changed Project-resident rule, exception, concrete example, enumeration, or current-member list needs current semantic support from at least one of:

- the live Project setting;
- the current request;
- a current canonical authority in the requested synchronization scope;
- explicit current re-adoption by the user;
- a necessary lookup-before-action bridge.

Do not create durable rules whose only support is stale history, old generated candidates, rejected/deleted history, prior incidents, model best practice, source wrapper wording, task-local commentary, review labels, or incidental source examples. Keep the underlying deleted/rejected rule absent and keep its deletion history out of the final setting unless the current user explicitly asks to preserve that history or prohibition as durable Project state.

Concrete examples are semantic content. Adding an example list can narrow, broaden, or fossilize a rule, so each example needs the same current support as a durable rule.

## Locator Substitution And Volatile Detail

Move detail out of Project instructions only when all are true:

- the locator is stable and resolvable;
- the relevant future task will look it up before acting;
- the removed detail is not required before lookup;
- the Project setting keeps the trigger or bridge that causes lookup;
- mandatory/optional force, authority, permission, safety, evidence strength, uncertainty, and exact identity are not weakened;
- the external source is genuinely the current semantic owner.

The point is maintainable recovery, not pushing all text out of Project instructions.

When a client, platform, device, route, inventory, supported-target, or other set has mutable membership and a stable canonical source owns the current list, Project instructions should preserve coverage and lookup, not current members. Use a short bridge such as "all currently supported items defined by the canonical source" plus the locator and lookup-before-action trigger.

Apply this globally. If one section says to use the canonical source for the current supported set, another section may not preserve the same set's current members as durable Project state. The abstraction is semantic, not literal platform-name matching.

## Scope, Bounded Edit, And Full Rewrite

Bounded edit is the default. It limits the semantic change, not necessarily the surface reconstruction. If the old structure is duplicated, source-shaped, or overloaded, a complete replacement may globally regroup, rename, reorder, and redraft while keeping unrelated valid semantics intact.

Use full rewrite or restructure only when at least one real condition holds:

- the user explicitly requests and authorizes it;
- local edits cannot resolve a cross-cutting contradiction;
- copied workflow detail has polluted the setting broadly;
- multiple scopes are materially imbalanced;
- required durable semantics cannot fit the budget through local deduplication and locator substitution;
- source ownership or locator use has systematically drifted or conflicted.

"It would be cleaner" or "the recent topic is important" is not enough. Preservation-sensitive full rewrite also requires a live baseline and enough current facts to preserve affected semantics.

When two currently supported rules overlap, a broad authorization, safety, privacy, evidence, completion, or fail-closed boundary cannot be removed merely because a narrower special-case rule survives. Retain the broad boundary once at the broadest correct home. Retain a narrower rule only when it adds action-specific detail that the broad rule does not provide.

This broad-rule preservation applies to current live or currently authorized meanings. A historical-only broad rule that is absent from the live setting remains absent unless the current user re-adopts it or current authorized source synchronization brings it into scope.

## Protected Absence

When history is partial or unavailable, a durable rule absent from the live baseline and present only in an old candidate, reference, summary, or generated historical setting remains absent by default.

Reintroduce it only when:

- the current user explicitly adds or re-adopts it; or
- the current task explicitly synchronizes a named canonical source, and that source currently supports the rule within the requested synchronization scope.

Protected absence does not create a permanent tombstone registry. It is a conservative rule for the current edit.

If a deleted or rejected rule is already absent from the live Project setting, the final long-lived setting should normally omit both the deleted rule and its deletion history. Use the deletion evidence internally to avoid reintroducing the rule, but do not emit `do not restore X`, `X was deleted`, or any equivalent Project-resident tombstone unless the current user explicitly asks to preserve that prohibition or history marker as durable Project state.

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

Exact identifiers include paths, commands, branch names, repository names, versions, state values, fields, model identifiers, protocol/product names, and other tokens that need exact matching. Ordinary prose can be edited for the current Project setting, but exact identifiers must remain exact when future work depends on exact spelling.

For Chinese-facing Project settings, express ordinary source labels and descriptive prose naturally in Chinese while preserving exact machine/formal identifiers. This is not mechanical language scoring, a banned-term table, a translation table, a percentage metric, or a fixed-section template. If the target Project has no Chinese or natural-language requirement, do not impose one.

## Runtime Boundary

PIE v0.1 uses `FINAL_ROUTE=SIMPLE_FORMAL_CORE`.

It runs as an ordinary ChatGPT Web / Project chat Skill. It does not require and must not claim an MCP finalizer, `OPENAI_API_KEY`, external model provider, sibling Skill chain, hosted service, or extra paid API call for normal operation.

PIE v0.1 may produce a clear, concise Project setting for the current edit, including natural Chinese when the current user or Project calls for it. It must not claim to guarantee cross-turn final reader-layer behavior for future chats. C11 evidence remains a preserved failure boundary: advanced multi-call or cross-turn reading-layer finalization is unsupported in PIE v0.1 and belongs to future Clear Writing work.

## Regression Families

Use these families as review coverage, not as a fixed gate count:

- normal unnamed Project-instruction editing and near-miss routing;
- stale candidate versus live setting;
- multi-scope Project under finite budget;
- source-drift controlled synchronization;
- preservation-sensitive replacement with missing live baseline;
- greenfield and explicit reset;
- locator substitution with lookup-before-action requirements;
- volatile source-owned inventory moved behind a bridge;
- protected absence under partial history;
- no-op when the correct owner is a canonical source or already-covered rule;
- no-op eligibility when a material in-scope defect has a safe bounded repair;
- should-not-change checks for authorization, safety, evidence strength, exact identifiers, and explicit user deletion/correction.

Do not convert regression examples into banned-word tables, language-percentage metrics, keyword scorers, fixed paragraph counts, fixed heading counts, fixed formula counts, or fixed character-per-section quotas.

## User Delivery

Keep the response proportional to edit risk.

Small bounded edits should be concise: decision, concrete edit, short reason, key preserved semantics, and length/delta when available.

Medium edits may add scope impact, locator/bridge reasoning, enforcement placement, balance, and budget margin.

Full replacements should explain the user-relevant basis only when it affects understanding or safety: that the candidate is based on the existing setting, starts from an empty setting, or follows an explicit reset. Ordinary user output must not print internal mode labels such as `preservation-sensitive`, `greenfield`, or `explicit reset`.

Missing-input outputs must avoid false-safe full settings. Name only the input that truly blocks safe completion and provide safe partial work.

No-op is valid only when the setting already satisfies the active contract, the remaining difference is cosmetic, or changing Project settings would duplicate, weaken, misplace, overfit, or add semantic risk.

Normal user-facing answers should be concise and should not expose internal mode labels, semantic maps, disposition tables, invariant checklists, or coverage/redundancy reviews unless the user asks for formal audit evidence. The default delivery is a short conclusion, the bounded edit or clean replacement when safe, and a few key reasons.
