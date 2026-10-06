---
name: machine-update-orchestrator
description: Normal AI Skills Maintainer entry for current-machine update requests such as update presentations, update workflow-core, update AI Skills, update Bridge Kit, and sync this machine. Discovers formal release state, selects the bounded route, delegates to the owning maintainer, and verifies reload/session boundaries.
status: active
provenance: user-authored
trusted: false
requires_network: true
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-09-23
profile_tags:
  - ai-skills-maintainer
recommended_scope: global
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
allow_implicit_invocation: false
---
# Machine Update Orchestrator

Use this skill only inside the `ai-skills-core` plugin, displayed as `AI Skills Maintainer`, when the user asks for a short current-machine update such as:

- `update presentations`
- `update workflow-core`
- `update research-writing`
- `update AI Skills`
- `update Bridge Kit`
- `sync this machine`

The user should not need to supply versions, commits, checkout paths, `CODEX_HOME`, Bridge roots, local repo inventories, adaptation templates, or component dependency lists.

## Boundary

This skill is a thin orchestrator. It discovers current state, resolves the formal release target, selects the minimum safe route, classifies Human Gates, delegates mutations to the owning capability, verifies the normal entry and reload boundary, and reports a concise result.

It does not create a daemon, watcher, database, machine registry, ledger, second authorization system, state machine, package manager, Bridge runtime implementation, or all-repo AGENTS rewriter.

## Required References

Read the relevant reference before acting:

- `references/formal-release-and-update-impact.md` for stable release identity and scope expansion.
- `references/ai-skills-plugin-profile-update.md` for Route A, isolated AI_Skills plugin/profile update.
- `references/cross-layer-stack-workflow-composition.md` for Route B, formal cross-layer composition.
- `references/bridge-kit-distribution-runtime-update.md` for Route C, Bridge Kit distribution/runtime update.
- `references/failure-recovery-human-gate.md` for failure, recovery, Human Gate and result vocabulary.

## Route Selection

There are exactly three mutation routes:

1. Route A: isolated AI_Skills plugin/profile update.
2. Route B: formal cross-layer stack/workflow composition declared by release metadata.
3. Route C: Bridge Kit distribution/runtime update through `bridge-kit-maintainer`.

`sync this machine` composes the same three routes for the currently participating installed stack. It is not a fourth route.

Do not infer cross-layer work from arbitrary Git diffs, commit messages, TODO prose, README prose or model intuition. Scope expansion comes only from the formal `release` ref and the matching root `CHANGELOG.md` `### Update impact` section.

## Discovery

Always discover only the bounded facts needed for the requested route:

- platform, host, current user, HOME and `CODEX_HOME`;
- Codex executable/version;
- configured Marketplace source/ref/owning layer;
- installed and available plugin identities/versions;
- formal release ref and matching release metadata;
- dirty/source state for canonical checkouts that will be mutated.

Discover AI_Skills source only when source, CLI, profile or managed-consumer adaptation requires it. Discover Bridge only when Bridge is requested or release metadata declares Bridge impact. Discover project consumers only from managed manifests, Bridge-known target paths, explicit workspace roots or already identified Git worktrees.

Do not recursively inventory `/`, all of HOME, network mounts, or every disk.

## Delegation

- AI_Skills repository/plugin release production: `ai-skills-repository-maintainer`.
- AI_Skills manifest/profile/managed-block install and refresh: `project-skill-installer`.
- Bridge Kit source/version/distribution/release channel: `bridge-kit-maintainer`.
- Skill overlap or library structure choices: `skill-library-analysis`.

Target domain judgment remains with the target domain plugin. Workflow delivery semantics remain with `workflow-core`. Bridge runtime and Host behavior remain with Bridge Kit and canonical `ai-bridge` commands.

## Session Truth

After installing or updating a plugin, do not claim the current session hot-reloaded. Return `UPDATED_RELOAD_REQUIRED` when a fresh Codex process/session is required, and verify release acceptance from a genuinely fresh normal entry when claiming release readiness.

