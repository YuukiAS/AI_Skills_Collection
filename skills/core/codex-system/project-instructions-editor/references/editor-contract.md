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

## No-Op Eligibility

Before returning no-op, review the live Project setting itself within the current user's requested scope. Treat it as the candidate and check whether it already satisfies active contracts for reading layer, language, placement, semantic ownership, durability, safety, privacy, authorization, evidence strength, fail-closed behavior, and mandatory/optional force.

No-op is valid when the setting already satisfies those contracts, when the remaining difference is only cosmetic preference, or when changing it would duplicate, weaken, misplace, overfit, or add semantic risk.

No-op is not eligible when the editor identifies a material live-setting defect in scope and a bounded edit or bounded consolidation can fix it without weakening unrelated semantics. Material defects include an active reading-layer or language-contract violation, a clear wrong owner or placement, volatile implementation or inventory detail that has a stable canonical source owner, duplicate detail that creates long-term maintenance burden, or another issue the current user explicitly asked the editor to check.

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

Exact identifiers include paths, commands, branch names, repository names, versions, state values, fields, model identifiers, and other tokens that need exact matching. Ordinary prose does not become exact merely because its source is in English.

## Mandatory Final Replacement Pass

Every path that emits a complete replacement must run the same mandatory final replacement pass on the actual replacement text. This includes bounded edit replacements, bounded consolidation, no-op rejected into bounded repair, full replacement, greenfield or explicit reset complete settings, reading/language repair, and protected-absence repair.

No complete replacement may be delivered before this pass. Check the actual final setting, in order:

1. protected absence and history residue;
2. the target Project's active reading-layer and language contract;
3. every remaining Latin-script token or mixed phrase for exact/formal necessity;
4. semantic invariants.

This pass is over the durable replacement itself, not only over analysis notes, source notes, or self-check prose.

Before delivery, also review each newly introduced or materially changed durable rule for current semantic support. Valid support can come from the current user request, the live Project setting, a current canonical source within the requested synchronization scope, or another current authority already valid under the ownership and effective-enforcement contract. Targeted deletion or rejection history is current-edit control evidence; by itself, it must not create a new durable Project rule.

If a candidate rule's only support is targeted deletion or rejection history, remove that newly generated durable rule from the final long-lived setting, keep the underlying deleted/rejected rule absent, and keep the deletion/rejection history out of the final setting. A durable prohibition or history marker is allowed only when the current user explicitly asks to store that marker as long-lived Project state.

If that Project requires ordinary explanation in natural Chinese, the final long-lived setting must itself use natural Chinese for ordinary explanatory prose. Descriptive English labels from old settings, repository text, logs, history, or workflow notes are not automatically exact identifiers.

Keep formal identities and machine strings exact when future work needs exact matching: repository names, paths, commands, file names, fields, state values, process names, versions, protocol or product names, and similarly precise tokens. Naturalize ordinary technical, engineering, workflow, management, and explanatory concepts under the Project's language contract.

The pass also applies to language introduced by the editor's own draft. If the target Project calls for natural prose, do not leave editor analysis labels, source labels, workflow shorthand, or policy jargon in the final setting unless they are exact identifiers.

The final setting is durable instructions, not a review note about old settings, sources, logs, or history. Do not preserve ordinary English examples from the input in the replacement as examples of what to avoid; explain that reasoning outside the replacement and make the replacement itself natural.

When the input classifies a group of English phrases as ordinary descriptive terms, budget waste, copied workflow detail, or non-exact prose, treat that group as non-exact for the replacement. If the user supplies an exact-preserve list, keep those exact strings and genuinely formal names; naturalize remaining ordinary English instead of repeating it as examples.

For a Project with an explicit Chinese reading-layer contract, review each remaining Latin-script token in the replacement. Keep the token only when it is exact or formal; otherwise rewrite it naturally in Chinese. This is a semantic token-by-token review aid, not an English-percentage score or banned-word check.

For every remaining Latin-script token or phrase in a Chinese final setting, the preservation reason must satisfy at least one concrete exactness condition: future lookup, execution, or matching depends on exact spelling; the token is a formal repository, product, protocol, path, command, file, field, state, process, version, or other machine identity; or translation would create material ambiguity that natural Chinese cannot remove. Preserve only the exact/formal part of a mixed phrase and naturalize generic labels around it.

Do not treat a token as exact only because it is technical, common in the field, useful for reviewer context, appears in a source, appeared in an earlier setting, or has product/context value. If the editor's self-check keeps an ordinary token, it must give the concrete exact/formal reason; otherwise naturalize it.

When a Latin-script phrase mixes a formal identity with a generic descriptive label, preserve only the formal identity. A product, protocol, repository, or scope name does not make neighboring labels exact; translate the label unless the whole phrase is itself a formal UI string, field, command, state value, or lookup key.

Do not copy the editor's own English meta-labels into a Chinese replacement. If an English phrase is only naming the instruction surface, current baseline, output mode, review category, or safety concept, express that label in natural Chinese unless the exact English phrase is itself a formal UI string, field, command, state value, or lookup key.

Generic category labels are not exact merely because they are technical. In a Chinese final setting, write ordinary labels in Chinese rather than as Latin-script tokens unless the user marks the exact spelling as required. The following are examples to translate, not examples to preserve: setting, repo, log, history, identifier, secret, token, endpoint, service, driver, watchdog, artifact, candidate, validation, routing, rollback, and fail closed.

If the user-visible self-check says ordinary English was naturalized, inspect the final replacement itself before making that claim. The self-check must match the replacement and cannot excuse ordinary non-exact English that remains in the durable Project setting.

If the target Project has no Chinese or natural-language requirement, do not impose one. Language normalization must not weaken or change ownership, authorization, privacy, safety, fail-closed behavior, evidence strength, uncertainty, or mandatory/optional force.

This pass reviews semantic consistency of the whole candidate. It is not a banned-word list, translation dictionary, English ratio, keyword score, or surface-form scoring rule.

## Formal Runtime Route

FINAL_ROUTE=`SIMPLE_FORMAL_CORE`.

The formal runtime is ordinary ChatGPT Web / Project chat with this Skill loaded. The Skill must be directly usable without an MCP finalizer, `OPENAI_API_KEY`, hosting, separate API billing, an external model provider, or a deployed model service.

The historical C10 helper-composition route and the C11 external finalizer route are not adopted as production dependencies. They must not be executed as fallback routes, advertised as required normal routes, or used as independent PASS gates for complete Project-instruction replacements.

Complete replacements are drafted and checked by the Skill itself using the current edit-mode and semantic-preservation contract. The mandatory final replacement pass remains required for every complete replacement, but it is an in-skill semantic consistency review of the actual durable setting, not a call to a sibling Skill, service, MCP tool, or separate provider.

If a complete replacement cannot be supported from the current chat's live baseline, canonical sources, budget, or authority evidence, the safe result is bounded advice, a clause, or a request for the missing input. Do not claim independent multi-call finalization, external Chinese realization, or raw-source fidelity verification.

ADVANCED_INDEPENDENT_MULTI_CALL_FINALIZATION=`UNSUPPORTED`.

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
- final-candidate reading-layer consistency after bounded edits, consolidation, or full replacement.

Do not convert regression examples into banned-word tables, English ratios, keyword scorers, fixed paragraph counts, fixed heading counts, fixed formula counts, or fixed character-per-section quotas.

## User Delivery

Keep the response proportional to edit risk.

Small bounded edits should be concise: decision, concrete edit, short reason, key preserved semantics, and length/delta when available.

Medium edits may add scope impact, locator/bridge reasoning, enforcement placement, balance, and budget margin.

Full replacements must include mode, reason bounded edit is insufficient or reset/greenfield applies, major placement changes, direct rules/bridges, preserved invariants, budget change, and a clean complete replacement.

Missing-input outputs must avoid false-safe full settings. Name only the input that truly blocks safe completion and provide safe partial work.

No-op is valid only when the setting already satisfies the active contract, the remaining difference is cosmetic, or changing Project settings would duplicate, weaken, misplace, overfit, or add semantic risk.
