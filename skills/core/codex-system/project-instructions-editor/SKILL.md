---
name: project-instructions-editor
description: Edit long-lived ChatGPT Project instructions using live settings, targeted history, canonical sources, and budget constraints; do not use for ordinary prose polishing, generic system/agent prompts, global Custom Instructions, or AI_Skills repository maintenance.
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

Read [references/editor-contract.md](references/editor-contract.md) when the edit involves compression, full replacement, locator substitution, partial history, multiple Project scopes, missing live settings, or evidence for a release/review gate.

## Placement Rules

Semantic ownership asks where the detailed and maintainable truth belongs: Project setting, global preference, canonical repository file, institution/workspace policy, current thread/task, or another stable source.

Effective enforcement asks where the rule must appear so the current Project actually follows it: a direct Project-resident rule, a short Project-resident bridge plus locator, canonical-source only, task/thread only, another verified layer, or no change.

Do not move a rule out of Project instructions merely because another source owns the detailed truth. For routing, authority, permission, safety, privacy, evidence, completion, user-output contract, and lookup-before-action rules, keep a direct subset or bridge when Project-local enforcement is needed before lookup.

Only replace detail with a locator when the locator is stable, the relevant future task will look it up before acting, the removed detail is not needed before lookup, and the Project setting keeps enough trigger/bridge text to preserve authority, safety, evidence strength, uncertainty, and mandatory/optional force.

## Protected Absence

When history is missing or partial, keep absent any durable rule that is not in the live baseline and appears only in an old candidate, reference, summary, or historical generated setting. Reintroduce it only when the current user explicitly re-adopts it or the current task explicitly synchronizes a named canonical source whose current content and authority support the rule.

Protected absence is a current-edit safety principle, not a tombstone registry or permanent ban.

## Output Contract

Deliver proportionally:

- For a small bounded edit, give the concise decision, exact additions/deletions/replacements, short reasons, key unchanged semantics, length/delta when available, and a clean full setting only when safe.
- For a medium edit, also explain scope impact, locator/bridge substitutions, effective enforcement, balance, and budget margin when relevant.
- For a full replacement, state the edit mode, why bounded edit is insufficient or why greenfield/reset applies, major placement changes, direct rules/bridges, preserved invariants, budget change, and the complete clean replacement.
- For missing inputs, provide only safe bounded advice or clauses, name the single missing input that truly blocks a full replacement, and avoid offloading repo/source lookup that you can do yourself.
- For no-op, say that the Project setting should not change and identify the correct owner, locator, or already-covered rule.

Never present a blacklist, English ratio, fixed character percentage, paragraph count, heading count, formula count, or keyword score as the quality decision.
