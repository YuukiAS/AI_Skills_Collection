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
last_reviewed: 2026-10-07
profile_tags: []
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
metadata:
  skill-author: AI Skills Collection maintainers
---
# Project Instructions Editor

Use this skill when the user wants to create, edit, compress, synchronize, restructure, or reset long-lived ChatGPT Project instructions or Project settings. The work is semantic placement and preservation for a Project-level instruction surface, not generic wording cleanup.

Do not use this skill for ordinary Chinese prose polishing, general writing fidelity, scientific or technical document restructuring, AI_Skills_Collection repository maintenance, complex workflow control, generic system or agent prompt optimization, or global Custom Instructions editing.

PIE v0.1 is an editor for the durable Project setting. It may draft natural, concise instructions for the current edit, but it does not guarantee that all future ChatGPT turns in that Project will keep a cross-turn final reader layer such as always-natural Chinese, no unnecessary English, or no mechanical line breaks. That future cross-turn reading-layer work belongs to Clear Writing, not to PIE v0.1.

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
4. Build a durable semantic map before drafting. Collapse live rules, current request, relevant history, and canonical-source facts by long-lived meaning rather than by source wording, log labels, or repeated surface phrases.
5. For each affected durable meaning, decide semantic ownership and effective enforcement placement separately: direct Project rule, short locator bridge, source-only, task-only, another verified layer, or omit.
6. Merge rules with the same semantic effect. Keep the stronger or clearer enforceable wording, preserve mandatory/optional force and trigger conditions, and avoid repeating the same long-lived rule under several source labels.
7. Prefer bounded edit when it closes the request without weakening unrelated semantics.
8. Use full rewrite only when explicitly authorized or when bounded edits cannot resolve a real cross-scope contradiction, pervasive copied detail, material scope imbalance, budget impossibility, or systematic source/locator drift.
9. Apply candidate expansion discipline: every newly introduced or materially changed Project-resident rule must have current semantic support from the live setting, current request, current canonical authority, explicit current re-adoption, or a necessary lookup-before-action bridge. If a rule's only support is stale history, rejected/deleted history, source wrapper wording, or task-local commentary, omit it from the final Project setting.
10. Preserve semantic invariants: mandatory versus optional force, trigger conditions, authority, permission, safety, privacy, distribution, evidence strength, role ownership, uncertainty, current-versus-future status, exact identifiers, and explicit user corrections or deletions.
11. Before returning no-op, check whether a material in-scope Project-setting defect has a safe bounded repair.
12. If required live baseline, authority, budget, or source evidence is missing, degrade honestly with bounded advice, a clause, or a request for the missing input.
13. Before delivery, run a semantic coverage and redundancy review over the actual candidate: required meanings are still covered, unsupported durable rules are absent, repeated meanings have been consolidated, locator bridges still trigger lookup before action, protected absence remains protected, and the known budget/headroom still holds.
14. Deliver only what the current chat can support: a complete replacement when the Skill can preserve the relevant semantics, or an explicit partial/degraded result when it cannot.

Read [references/editor-contract.md](references/editor-contract.md) when the edit involves compression, full replacement, locator substitution, partial history, multiple Project scopes, missing live settings, or evidence for a release/review gate.

## Placement Rules

Semantic ownership asks where the detailed and maintainable truth belongs: Project setting, global preference, canonical repository file, institution/workspace policy, current thread/task, or another stable source.

Effective enforcement asks where the rule must appear so the current Project actually follows it: a direct Project-resident rule, a short Project-resident bridge plus locator, canonical-source only, task/thread only, another verified layer, or no change.

Do not move a rule out of Project instructions merely because another source owns the detailed truth. For routing, authority, permission, safety, privacy, evidence, completion, output contract, and lookup-before-action rules, keep a direct subset or bridge when Project-local enforcement is needed before lookup.

Only replace detail with a locator when the locator is stable, the relevant future task will look it up before acting, the removed detail is not needed before lookup, and the Project setting keeps enough trigger/bridge text to preserve authority, safety, evidence strength, uncertainty, and mandatory/optional force.

## No-Op Eligibility

No-op remains valid when changing the Project setting would duplicate, weaken, misplace, overfit, or add risk, or when the remaining difference is only cosmetic preference.

Before returning no-op, treat the current live Project setting itself as the candidate to review within the current user's requested scope. Check whether it already satisfies active contracts for placement, semantic ownership, durability, safety, privacy, authorization, evidence strength, fail-closed behavior, and mandatory/optional force.

No-op is not eligible when you identify a material live-setting defect in scope and a bounded edit or bounded consolidation can fix it without weakening unrelated semantics. Material defects include a clear wrong owner or placement, volatile implementation or inventory detail that has a stable canonical source owner, duplicate detail that creates long-term maintenance burden, or another issue the current user explicitly asked you to check.

When the material defect is volatile implementation, inventory, status, or client/detail copied from a stable canonical source, the bounded repair should keep a short trigger and locator bridge and omit the copied volatile list or detail unless a specific item is truly needed before lookup for routing, authorization, safety, or exact identity.

Appropriate Project-resident repetition may still be kept when it improves effective enforcement before lookup. That does not justify ignoring a separate acknowledged defect that is safely repairable.

## Protected Absence

When history is missing or partial, keep absent any durable rule that is not in the live baseline and appears only in an old candidate, reference, summary, or historical generated setting. Reintroduce it only when the current user explicitly re-adopts it or the current task explicitly synchronizes a named canonical source whose current content and authority support the rule.

When a rule was deleted or rejected and is absent from the live Project setting, use that evidence only to protect the current edit. The final long-lived Project setting should omit both the deleted rule and its deletion history; do not emit `do not restore X`, `X was deleted`, or equivalent Project-resident tombstones unless the current user explicitly asks to keep that prohibition or history marker as a durable rule.

Protected absence is a current-edit safety principle, not a tombstone registry or permanent ban.

## Surface Consolidation

Complex source, history, and live-setting packets must be reduced to a long-lived semantic map before writing the final Project setting. Do not copy every source heading, current-task note, audit label, client inventory, workflow step, or old candidate sentence into Project instructions merely because it appeared in an input.

Use these dispositions:

- `direct Project rule`: the Project must enforce the rule before doing future work.
- `short locator bridge`: the Project needs a trigger plus stable locator, while details stay in the canonical source.
- `source-only`: the source owns the detail and the Project does not need a pre-lookup rule.
- `task-only`: the fact matters only to the current task/thread.
- `omit`: the fact is stale, unsupported, deleted/rejected, duplicative, or outside the authorized scope.

The final candidate should expand only for real semantic reasons: adding a missing required rule, repairing a wrong owner or locator, preserving a stronger live requirement, restoring necessary evidence/safety/authorization force, or replacing volatile copied detail with a durable bridge. Do not expand the setting just because the input packet is long, because a source uses many labels, or because history contains several near-duplicate formulations.

After drafting, compare the candidate against the semantic map rather than against source surface order. If two candidate clauses have the same long-lived effect, consolidate them. If a clause has no current semantic support, remove it. If a source-owned detail is volatile, keep only the lookup trigger and locator needed for future enforcement.

For a Project whose current setting or user request calls for natural Chinese, the current replacement should digest ordinary source labels and descriptive English into natural Chinese when that does not change meaning. Keep exact machine/formal identifiers unchanged. This is current-artifact readability inside the edit, not a promise that PIE v0.1 will enforce future cross-turn reader-layer behavior.

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

Exact identifiers include paths, commands, branch names, repository names, versions, state values, fields, model identifiers, and other tokens that need exact matching.

## Runtime Boundary

FINAL_ROUTE=`SIMPLE_FORMAL_CORE`.

The formal Project Instructions Editor runtime is ordinary ChatGPT Web / Project chat with this Skill loaded. It must be directly usable without an MCP finalizer, `OPENAI_API_KEY`, hosting, separate API billing, an external model provider, a sibling Skill chain, or a separately deployed model service for normal use.

Complete replacements are drafted and checked by the Skill itself in the current chat, using the edit-mode, ownership, protected-absence, no-op eligibility, exact-identity, authorization, privacy, safety, evidence, and budget rules above.

If the current chat lacks enough live baseline, canonical-source evidence, budget facts, or authority to safely emit a complete replacement, degrade explicitly with bounded advice, a clause, or a request for the missing input. Do not claim that an independent finalizer, external Chinese realization, raw-source verifier, or cross-turn reading-layer guarantee has run.

ADVANCED_INDEPENDENT_MULTI_CALL_FINALIZATION=`UNSUPPORTED`.
CROSS_TURN_FINAL_READER_LAYER_GUARANTEE=`UNSUPPORTED_IN_PIE_0_1`.

## Output Contract

Deliver proportionally:

- For a small bounded edit, give the concise decision, exact additions/deletions/replacements, short reasons, key unchanged semantics, length/delta when available, and a clean full setting only when safe.
- For a medium edit, also explain scope impact, locator/bridge substitutions, effective enforcement, balance, and budget margin when relevant.
- For a full replacement, state the edit mode, why bounded edit is insufficient or why greenfield/reset applies, major placement changes, direct rules/bridges, preserved invariants, budget change, and the complete clean replacement.
- For missing inputs, provide only safe bounded advice or clauses, name the single missing input that truly blocks a full replacement, and avoid offloading repo/source lookup that you can do yourself.
- For no-op, say that the Project setting should not change, identify the correct owner, locator, already-covered rule, or semantic risk, and explain why no material in-scope defect is safely repairable.

By default, normal user-facing output should not expose internal labels such as preservation-sensitive, durable semantic map, disposition table, invariant checklist, or coverage/redundancy review. Use a short conclusion, the replacement or bounded edit when safe, and only the few key changes a user needs to trust the edit. Expose audit detail only when the user asks for review evidence or the task is explicitly an audit packet.

Never present mechanical surface scoring as the quality decision.
