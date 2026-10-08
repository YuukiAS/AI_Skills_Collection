---
name: project-instructions-editor
description: Use when the user explicitly asks to create, update, compress, sync, restructure, or reset long-lived ChatGPT Project instructions, even if the live setting is missing; do not use for ordinary prose, writing fidelity, scientific rewrite, AI_Skills maintenance, workflow/control, generic agent/system prompts, or global Custom Instructions.
status: active
version: "0.1"
provenance: user-authored
trusted: false
requires_network: false
writes_files: false
executes_code: false
secrets_needed: []
last_reviewed: 2026-10-02
profile_tags: []
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
metadata:
  skill-author: AI Skills Collection maintainers
---
# Project Instructions Editor

Use this skill when the user wants to create, edit, compress, synchronize, or reset long-lived ChatGPT Project instructions or Project settings. The work is semantic placement and preservation for a Project-level instruction surface, not generic wording cleanup.

Do not use this skill for ordinary Chinese prose polishing, general writing fidelity, scientific or technical document restructuring, AI_Skills_Collection repository maintenance, complex workflow control, generic system or agent prompt optimization, or global Custom Instructions editing.

## Edit Mode

Classify the request before drafting:

- `preservation-sensitive`: an existing Project setting is in force and the user has not explicitly discarded unrelated existing semantics. Use the live Project setting as the baseline for any full replacement, deletion, compression, or global reorganization. If the live setting is missing or incomplete, do not claim a safe full replacement.
- `greenfield`: the Project instructions are confirmed empty or absent. You may draft a complete initial setting, but do not claim to preserve old Project-setting semantics.
- `explicit reset`: the current user clearly authorizes discarding the old Project setting and rebuilding from zero. This removes only the Project-setting preservation obligation; system, workspace, repository, safety, privacy, and current user requirements still apply.

If the mode changes what can be safely preserved and the available context does not decide it, ask the smallest useful clarification.

## Inputs

Always anchor the edit in the current user request. It defines the requested addition, deletion, correction, compression, synchronization, reset, and authorized scope.

Use the live Project setting when preservation-sensitive editing could rewrite, delete, compress, or rebalance existing instructions. A stale repo candidate, old reference, or summary is evidence only; it is not the live baseline.

Retrieve only relevant Project history: explicit acceptance, deletion, rejection, repeated correction, durable authority decisions, and requirements marked temporary. Missing history does not justify exhaustive audit or invented certainty.

Read canonical sources when the requested edit depends on repository-owned policy, workflow, version, task state, locator, or other current facts. If a source is unavailable, degrade only the affected claim and say what cannot be verified.

Respect the actual instruction budget when known. Track current length, candidate length, delta, hard limit or planning budget, and requested headroom when available. Unknown hard limits may support density improvements, but not a claim that the candidate fits an unverified limit.

## Reasoning Sequence

1. Identify the requested Project-instruction change and authorized scope.
2. Classify the edit mode.
3. Compare live setting, relevant history, canonical sources, and budget only as far as needed for the current edit.
4. For each affected durable rule, decide semantic ownership and effective enforcement placement separately.
5. Prefer bounded edit when it closes the request without weakening unrelated semantics.
6. Use full rewrite only when explicitly authorized or when bounded edits cannot resolve a real cross-scope contradiction, pervasive copied detail, material scope imbalance, budget impossibility, or systematic source/locator drift.
7. Preserve semantic invariants: mandatory versus optional force, trigger conditions, authority, permission, safety, privacy, distribution, evidence strength, role ownership, uncertainty, current-versus-future status, exact identifiers, and explicit user corrections or deletions.
8. Before returning no-op, run the no-op eligibility check against the live Project setting itself.
9. For any complete replacement, draft directly in the ordinary ChatGPT Web / Project chat runtime and run the mandatory final replacement pass on the actual replacement text before delivery.
10. If required live baseline, authority, budget, or source evidence is missing, degrade honestly with bounded advice, a clause, or a request for the missing input; do not invent an external finalizer, service, or independent verifier.
11. Deliver only what the current chat can support: a complete replacement when the Skill can preserve the relevant semantics, or an explicit partial/degraded result when it cannot.

Read [references/editor-contract.md](references/editor-contract.md) when the edit involves compression, full replacement, locator substitution, partial history, multiple Project scopes, missing live settings, or evidence for a release/review gate.

## Placement Rules

Semantic ownership asks where the detailed and maintainable truth belongs: Project setting, global preference, canonical repository file, institution/workspace policy, current thread/task, or another stable source.

Effective enforcement asks where the rule must appear so the current Project actually follows it: a direct Project-resident rule, a short Project-resident bridge plus locator, canonical-source only, task/thread only, another verified layer, or no change.

Do not move a rule out of Project instructions merely because another source owns the detailed truth. For routing, authority, permission, safety, privacy, evidence, completion, user-output contract, and lookup-before-action rules, keep a direct subset or bridge when Project-local enforcement is needed before lookup.

Only replace detail with a locator when the locator is stable, the relevant future task will look it up before acting, the removed detail is not needed before lookup, and the Project setting keeps enough trigger/bridge text to preserve authority, safety, evidence strength, uncertainty, and mandatory/optional force.

## No-Op Eligibility

No-op remains valid when changing the Project setting would duplicate, weaken, misplace, overfit, or add risk, or when the remaining difference is only cosmetic preference.

Before returning no-op, treat the current live Project setting itself as the candidate to review within the current user's requested scope. Check whether it already satisfies active contracts for reading layer, language, placement, semantic ownership, durability, safety, privacy, authorization, evidence strength, fail-closed behavior, and mandatory/optional force.

No-op is not eligible when you identify a material live-setting defect in scope and a bounded edit or bounded consolidation can fix it without weakening unrelated semantics. Material defects include an active reading-layer or language-contract violation, a clear wrong owner or placement, volatile implementation or inventory detail that has a stable canonical source owner, duplicate detail that creates long-term maintenance burden, or another issue the current user explicitly asked you to check.

When the material defect is volatile implementation, inventory, status, or client/detail copied from a stable canonical source, the bounded repair should keep a short trigger and locator bridge and omit the copied volatile list or detail unless a specific item is truly needed before lookup for routing, authorization, safety, or exact identity.

Appropriate Project-resident repetition may still be kept when it improves effective enforcement before lookup. That does not justify ignoring a separate acknowledged defect that is safely repairable.

## Protected Absence

When history is missing or partial, keep absent any durable rule that is not in the live baseline and appears only in an old candidate, reference, summary, or historical generated setting. Reintroduce it only when the current user explicitly re-adopts it or the current task explicitly synchronizes a named canonical source whose current content and authority support the rule.

When a rule was deleted or rejected and is absent from the live Project setting, use that evidence only to protect the current edit. The final long-lived Project setting should omit both the deleted rule and its deletion history; do not emit `do not restore X`, `X was deleted`, or equivalent Project-resident tombstones unless the current user explicitly asks to keep that prohibition or history marker as a durable rule.

Protected absence is a current-edit safety principle, not a tombstone registry or permanent ban.

## Final Candidate Consistency

Every path that emits a complete replacement must run the same mandatory final replacement pass immediately before delivery. This includes bounded edit replacements, bounded consolidation, no-op rejected into bounded repair, full replacement, greenfield or explicit reset complete settings, reading/language repair, and protected-absence repair.

Run this pass on the actual replacement text, not only on analysis notes or the surrounding self-check. No complete replacement may be delivered until the pass has checked, in order: protected absence and history residue; the target Project's active reading-layer and language contract; every remaining Latin-script token or mixed phrase for exact/formal necessity; and semantic invariants.

Also review every newly introduced or materially changed durable rule for current semantic support. A durable rule may be supported by the current user request, live Project setting, current canonical source within the requested synchronization scope, or another current authority already valid under the ownership and enforcement contract. Targeted deletion or rejection history is current-edit control evidence; by itself, it must not create a new durable Project rule.

If a candidate rule's only support is targeted deletion or rejection history, remove that newly generated rule from the final long-lived setting, keep the underlying deleted/rejected rule absent, and keep the deletion/rejection history out of the final setting. Preserve a durable prohibition or history marker only when the current user explicitly asks to store that marker as long-lived Project state.

If the target Project clearly requires ordinary explanation in natural Chinese, the final Project setting must satisfy that contract itself. Descriptive English labels from old settings, repositories, logs, or history are not automatically exact identifiers; they remain exact only when they are formal identities or machine strings that future work must match exactly.

Preserve exact repository names, paths, commands, file names, fields, state values, process names, versions, protocol/product names, and other tokens that require exact matching. Translate or naturally restate ordinary technical, engineering, workflow, management, or explanatory concepts according to the Project's reading-layer contract instead of copying them merely because the source was English.

Apply the same check to language introduced by your own draft. Do not leave editor analysis labels, source labels, workflow shorthand, or policy jargon in the final Project setting when the target Project calls for natural prose and those labels are not exact identifiers.

Write the final Project setting as durable instructions, not as commentary about the old setting, source, logs, or history. Do not preserve ordinary English examples from the input merely to explain that they should be avoided; put that reasoning in the surrounding review text, and make the replacement itself natural.

When the input explicitly classifies a group of English phrases as ordinary descriptive terms, budget waste, copied workflow detail, or non-exact prose, treat that group as non-exact for the replacement. If the user supplies an exact-preserve list, keep those exact strings and genuinely formal names; naturalize the remaining ordinary English rather than repeating it as examples.

For a Project with an explicit Chinese reading-layer contract, use remaining Latin-script tokens in the replacement as review cues. Keep each token only when it is exact or formal; otherwise rewrite it naturally in Chinese. This is a semantic token-by-token review aid, not an English-percentage score or banned-word check.

For every remaining Latin-script token or phrase in a Chinese final setting, the preservation reason must satisfy at least one concrete exactness condition: future lookup, execution, or matching depends on exact spelling; the token is a formal repository, product, protocol, path, command, file, field, state, process, version, or other machine identity; or translation would create material ambiguity that natural Chinese cannot remove. Preserve only the exact/formal part of a mixed phrase and naturalize generic labels around it.

Do not treat a token as exact only because it is technical, common in the field, useful for reviewer context, appears in a source, appeared in an earlier setting, or has product/context value. If your self-check keeps an ordinary token, give the concrete exact/formal reason; otherwise naturalize it.

When a Latin-script phrase mixes a formal identity with a generic descriptive label, preserve only the formal identity. A product, protocol, repository, or scope name does not make neighboring labels exact; translate the label unless the whole phrase is itself a formal UI string, field, command, state value, or lookup key.

Do not copy the editor's own English meta-labels into a Chinese replacement. If an English phrase is only naming the instruction surface, current baseline, output mode, review category, or safety concept, express that label in natural Chinese unless the exact English phrase is itself a formal UI string, field, command, state value, or lookup key.

Generic category labels are not exact merely because they are technical. In a Chinese final setting, write ordinary labels in Chinese rather than as Latin-script tokens unless the user marks the exact spelling as required. The following are examples to translate, not examples to preserve: setting, repo, log, history, identifier, secret, token, endpoint, service, driver, watchdog, artifact, candidate, validation, routing, rollback, and fail closed.

If your user-visible self-check says ordinary English was naturalized, first inspect the final replacement itself. The self-check must match the replacement and cannot excuse ordinary non-exact English that remains in the durable Project setting.

Do not impose Chinese when the target Project has no Chinese or natural-language contract. Language normalization must not weaken or change ownership, authorization, privacy, safety, fail-closed behavior, evidence strength, uncertainty, or mandatory/optional force.

This is a semantic self-consistency review of the complete candidate, not a banned-word list, translation dictionary, English ratio, keyword count, or scoring rule.

## Formal Runtime Route

FINAL_ROUTE=`SIMPLE_FORMAL_CORE`.

The formal Project Instructions Editor runtime is the ordinary ChatGPT Web / Project chat Skill contract. It must be directly usable without an MCP finalizer, `OPENAI_API_KEY`, hosting, separate API billing, an external model provider, or a separately deployed model service for normal use.

The old C10 helper-composition route and the C11 external finalizer route are not adopted as production runtime dependencies. They must not be executed as fallback routes, presented as required routes, or used as independent PASS gates for the formal Skill.

Complete replacements are drafted and checked by the Skill itself in the current chat, using the edit-mode, ownership, protected-absence, no-op eligibility, exact-identity, authorization, privacy, safety, evidence, budget, and final-candidate consistency rules above. The final replacement pass is mandatory, but it is an in-skill semantic consistency review, not a call to a registered app or sibling Skill.

If the current chat lacks enough live baseline, canonical-source evidence, budget facts, or authority to safely emit a complete replacement, degrade explicitly with bounded advice, a clause, or a request for the missing input. Do not claim that an independent multi-call finalization or raw-source verifier has run.

ADVANCED_INDEPENDENT_MULTI_CALL_FINALIZATION=`UNSUPPORTED`.

## Output Contract

Deliver proportionally:

- For a small bounded edit, give the concise decision, exact additions/deletions/replacements, short reasons, key unchanged semantics, length/delta when available, and a clean full setting only when safe.
- For a medium edit, also explain scope impact, locator/bridge substitutions, effective enforcement, balance, and budget margin when relevant.
- For a full replacement, state the edit mode, why bounded edit is insufficient or why greenfield/reset applies, major placement changes, direct rules/bridges, preserved invariants, budget change, and the complete clean replacement.
- For missing inputs, provide only safe bounded advice or clauses, name the single missing input that truly blocks a full replacement, and avoid offloading repo/source lookup that you can do yourself.
- For no-op, say that the Project setting should not change, identify the correct owner, locator, already-covered rule, or semantic risk, and explain why no material in-scope defect is safely repairable.

Never present a blacklist, English ratio, fixed character percentage, paragraph count, heading count, formula count, or keyword score as the quality decision.
