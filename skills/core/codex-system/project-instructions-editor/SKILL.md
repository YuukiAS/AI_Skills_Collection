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

## Modes And Inputs

Classify the request before drafting:

- `preservation-sensitive`: an existing Project setting is in force and the user has not explicitly discarded unrelated semantics. Use the live Project setting as the baseline for any full replacement, deletion, compression, or global reorganization. If that baseline is missing or incomplete, do not claim a safe full replacement.
- `greenfield`: Project instructions are confirmed empty or absent. Draft an initial setting without claiming to preserve old Project-setting semantics.
- `explicit reset`: the current user clearly authorizes discarding the old Project setting and rebuilding from zero. Reset does not override higher-priority instructions, workspace policy, repository authority, privacy, safety, or current request limits.

If the mode changes what can be safely preserved and the available context does not decide it, ask the smallest useful clarification.

Anchor every edit in the current request, live setting, relevant Project history, current canonical sources, and actual budget when those inputs matter. A stale candidate, old reference, generated setting, or summary is evidence only; it is not the live baseline. Missing history, source, baseline, authority, or budget creates bounded degradation, not invented certainty.

Read [references/editor-contract.md](references/editor-contract.md) when the edit involves compression, full replacement, locator substitution, partial history, multiple Project scopes, missing live settings, or evidence for a release/review gate.

## Simple Editing Core

For complex edits and complete replacements, use this simple editor core:

```text
live setting + current request + necessary current source facts
-> identify durable user-facing rule groups
-> consolidate duplicate rules
-> move volatile detail behind stable source bridges
-> preserve semantic force and exact identities
-> emit a compact replacement
```

Draft from durable user-facing responsibilities, not from source headings, old section order, source labels, incident logs, or repository document layout. Heading names, section count, order, and old grouping are normally surface, not preserved semantics.

Bounded edit limits which long-lived meanings may change. It does not require preserving old paragraphs, titles, or source-shaped scaffolding. If a full replacement is safe and authorized, regenerate the surface from the current durable meanings instead of patching the old setting section by section.

Cluster rules by practical trigger, governed surface, owner, and user consequence. Merge overlapping clauses that tell the assistant to do the same thing for the same trigger. Keep a distinct rule only when the trigger, surface, owner, or consequence is materially different.

Do not add a durable rule, exception, concrete example, or current member list merely because it appears in history, memory, an old candidate, a prior incident, a source example, or model best practice. New durable content needs current support from the live setting, current request, in-scope canonical source, explicit current re-adoption, or a necessary lookup-before-action bridge.

When a mutable inventory, supported-target list, client/platform set, route table, status list, or similar fact has a stable canonical owner, keep a short Project-resident bridge and locator instead of freezing current members. Apply this globally: the same source-owned set should not be abstracted in one section while its current members survive elsewhere as durable Project truth.

Preserve broad authorization, privacy, safety, evidence, completion, and fail-closed boundaries. A narrower special-case rule may add useful detail, but it must not swallow a broader live boundary. A historical-only broad rule that is absent from the live setting stays absent unless the current user or current authorized source synchronization re-adopts it.

For Chinese-facing Project settings, write ordinary concepts naturally in Chinese during drafting and keep only formal names or machine strings that need exact matching. Do not use mechanical language scoring, banned terms, translation tables, fixed heading counts, or fixed templates as the quality decision.

## Placement, Bridges, And No-Op

Semantic ownership asks where the detailed and maintainable truth belongs. Effective enforcement asks where the rule must appear so this Project follows it before acting. Do not move a rule out of Project instructions merely because another source owns detail; for routing, authority, authorization, safety, privacy, evidence, completion, user-output, and lookup-before-action rules, keep a direct subset or bridge when Project-local enforcement is needed.

Only replace detail with a locator when the locator is stable, future work will look it up before acting, removed detail is not needed before lookup, and the Project bridge preserves authority, safety, evidence strength, uncertainty, and mandatory/optional force.

No-op remains valid when changing the Project setting would duplicate, weaken, misplace, overfit, or add risk, or when the remaining difference is only cosmetic preference.

Before returning no-op, treat the live Project setting itself as the candidate under the current request. No-op is not eligible when a material in-scope defect has a safe bounded repair: wrong owner or placement, volatile detail with a canonical owner, costly duplication, or another issue the user asked you to check.

If required live baseline, authority, budget, or source evidence is missing, degrade honestly with bounded advice, a safe clause, or a request for the single missing input that truly blocks a full replacement. Do not claim a safe complete replacement when the necessary baseline or authority is absent.

## Protected Absence And Invariants

When history is missing or partial, keep absent any durable rule that is not in the live baseline and appears only in an old candidate, reference, summary, or historical generated setting. Reintroduce it only when the current user explicitly re-adopts it or the current task synchronizes a named canonical source whose current content and authority support the rule.

When a rule was deleted or rejected and is absent from the live Project setting, use that evidence only to protect the current edit. The final long-lived Project setting should omit both the deleted rule and its deletion history; do not emit `do not restore X`, `X was deleted`, or equivalent Project-resident tombstones unless the current user explicitly asks to keep that prohibition or history marker as a durable rule.

Never silently weaken or alter mandatory versus optional force, trigger conditions, authority, permission, authorization, safety, privacy, distribution, evidence strength, completion claims, role ownership, uncertainty, negative findings, current/future status, exact identifiers, explicit user corrections/deletions/rejections/acceptances, or unrelated live scopes. Exact identifiers include paths, commands, branch names, repository names, versions, state values, fields, model identifiers, protocol/product names, and other tokens that need exact matching.

## Runtime Boundary

FINAL_ROUTE=`SIMPLE_FORMAL_CORE`.

The formal runtime is ordinary ChatGPT Web / Project chat with this Skill loaded. It must be directly usable without an MCP finalizer, `OPENAI_API_KEY`, hosting, separate API billing, external model provider, sibling Skill chain, or separately deployed model service.

Complete replacements are drafted and checked by the Skill itself in the current chat. If the chat lacks enough live baseline, canonical-source evidence, budget facts, or authority to safely emit one, degrade explicitly with bounded advice, a clause, or a request for the missing input. Do not claim an independent finalizer, external Chinese realization, raw-source verifier, or cross-turn reading-layer guarantee has run.

ADVANCED_INDEPENDENT_MULTI_CALL_FINALIZATION=`UNSUPPORTED`.
CROSS_TURN_FINAL_READER_LAYER_GUARANTEE=`UNSUPPORTED_IN_PIE_0_1`.

## Output Contract

Deliver proportionally. For a bounded edit, give the decision, exact edit, short reason, preserved semantics, and length/delta when available. For a full replacement, explain the user-relevant basis only when it affects understanding or safety: that the candidate is based on the existing setting, starts from an empty setting, or follows an explicit reset. Do not print internal mode labels such as `preservation-sensitive`, `greenfield`, or `explicit reset` in ordinary user output.

For missing inputs, provide safe bounded advice or clauses, name the single input that truly blocks a full replacement, and avoid offloading repo/source lookup that you can do yourself. For no-op, say the Project setting should not change, identify the owner, locator, covered rule, or semantic risk, and explain why no material in-scope defect is safely repairable.

By default, normal user-facing output should not expose internal labels such as preservation-sensitive, greenfield, explicit reset, semantic map, disposition table, invariant checklist, or coverage/redundancy review. Use a short conclusion, the replacement or bounded edit when safe, and only the few key changes a user needs to trust the edit. Expose audit detail and internal labels only when the user asks for formal audit or review evidence.

Never present mechanical surface scoring as the quality decision.
