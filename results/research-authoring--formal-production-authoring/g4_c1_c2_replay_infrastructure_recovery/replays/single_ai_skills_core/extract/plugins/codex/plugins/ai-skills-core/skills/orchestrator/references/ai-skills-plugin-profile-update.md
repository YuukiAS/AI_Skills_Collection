# Route A: Isolated AI_Skills Plugin Or Profile Update

Use Route A for central plugin or profile updates such as `update presentations`, `update workflow-core`, `update research-writing`, `update AI Skills`, or a named managed profile when release metadata does not declare cross-layer impact.

## Default Scope

- Formal AI_Skills Marketplace source at `release`.
- The requested plugin or profile.
- Relevant AI_Skills managed consumer only when a manifest or managed block proves ownership.

Default non-scope:

- Bridge Kit;
- Host Policy;
- unrelated plugins;
- arbitrary project repos;
- unowned project `AGENTS.md` text.

## Legacy Marketplace Bootstrap

For a pre-capability AI_Skills install, support one explicit migration from an expected user-owned AI_Skills Marketplace source pinned to `main`.

Before mutation, discover and record:

- Marketplace name;
- Git source URL;
- ref;
- sparse paths;
- owning config layer;
- installed/enabled AI_Skills plugin state;
- exact legacy metadata needed for restoration.

Proceed only when the source is the expected AI_Skills repository, ref is `main`, sparse paths match the generated Marketplace/payload paths, the source is user-owned/mutable, and remote `release` is verified.

Use official Codex Marketplace and plugin commands only. Do not hand-edit Codex config.

If replacing the source fails after removal, restore the exact captured `main` source, verify restoration, report `PARTIAL_UPDATE`, and stop. If another config layer owns the source, fail closed with the exact layer.

After successful bootstrap, reinstall `ai-skills-core` and the requested target, then require a fresh session. Do not claim ai-skills-core 0.4 already implements this path.

## Delegation

Delegate managed project/profile refresh to `project-skill-installer`. Delegate AI_Skills release production to `ai-skills-repository-maintainer`. Do not upgrade unrelated installed plugins opportunistically.

