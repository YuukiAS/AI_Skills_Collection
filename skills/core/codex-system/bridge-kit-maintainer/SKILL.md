---
name: bridge-kit-maintainer
description: Internal AI Skills Maintainer capability for Bridge Kit source, version, distribution, formal release-channel maintenance, editable package refresh, runtime identity checks, and delegation to canonical ai-bridge commands.
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
# Bridge Kit Maintainer

Use this skill only inside `ai-skills-core` / `AI Skills Maintainer` for Bridge Kit distribution, version, source identity, formal release-channel maintenance and current-machine runtime refresh.

## Boundary

This skill owns Bridge maintenance/distribution concerns:

- discover the resolved `ai-bridge` executable;
- identify `ai-bridge where` runtime/source root;
- verify package/runtime version and path;
- resolve the formal Bridge `release` ref;
- discover current Bridge `main` and the canonical version source without
  treating either as sufficient release evidence by itself;
- read the Bridge `AGENTS.md` owner locator before claiming formal
  distribution ownership;
- identify the newest Bridge release commit/version that is provably formally
  closed from version, changelog and closure evidence;
- classify the relationship among `main`, `release`, and the latest provable
  formal release as `ALIGNED`, `LAGGING`, `AHEAD/INCONSISTENT`, or
  `FORMAL_RELEASE_NOT_PROVABLE`;
- safely update a canonical Bridge checkout when ancestry and dirty ownership permit;
- refresh the existing editable package/entry point from the formal source;
- during formal Bridge release closure, verify closure/version/changelog evidence and advance the Bridge `release` ref;
- delegate Host/project-consumer mutation back to canonical `ai-bridge` commands.

It does not own Bridge runtime semantics and must not copy Bridge runtime logic into AI_Skills.

Bridge Kit remains owner of:

- Host Policy implementation;
- Lite, Review, Control and Persistent Run behavior;
- Human Gate and plugin replay runtime;
- Bridge runtime source changes;
- Bridge project-consumer implementation.

If Bridge production runtime/source behavior must change, stop and return to Planner/Critic.

## Required References

Read the relevant reference before acting:

- `references/bridge-release-channel.md` for Bridge `release` producer/consumer behavior.
- `references/canonical-ai-bridge-delegation.md` for what must remain delegated to Bridge CLI.

## Bridge AGENTS Locator

Formal Bridge release discoverability requires exactly one minimal owner locator in `YuukiAS/GPT_Codex_AI_Bridge_Kit/AGENTS.md`:

- Bridge runtime / Host / Lite / Review / Control / Persistent Run implementation authority remains in Bridge Kit.
- Formal Bridge distribution/version closure, including the moving `release` ref, is owned by AI Skills Maintainer (`ai-skills-core` -> `bridge-kit-maintainer`).
- A Bridge formal release must hand off to that owner before distribution completion.
- The canonical producer contract remains in AI_Skills_Collection and is not duplicated into Bridge.

Do not duplicate that locator into Bridge README, QUICKSTART, CHANGELOG or runtime source.

## Release State Discovery

For `update Bridge Kit`, do dynamic discovery from the real Bridge source. Do
not hard-code a Bridge version or SHA into AI_Skills behavior.

Minimum discovery:

1. verify the Bridge repo origin is `YuukiAS/GPT_Codex_AI_Bridge_Kit`;
2. discover current `main`;
3. discover current `refs/heads/release`;
4. read `pyproject.toml` and `ai_bridge_kit/__init__.py` as canonical version
   sources;
5. read Bridge `AGENTS.md` and confirm the formal-distribution owner locator;
6. inspect root `CHANGELOG.md` and existing formal closure evidence;
7. identify the newest release commit/version that is actually provable as
   formally closed.

Do not infer the latest formal release from newest `main` SHA, a high-looking
version string alone, a changelog heading alone, arbitrary docs/TODO prose or
model intuition.

Classify the release relation:

- `ALIGNED`: `refs/heads/release` equals the latest provable formal release.
- `LAGGING`: `refs/heads/release` is an ancestor of the latest provable formal
  release. Report formal distribution as pending/incomplete; never call the old
  ref the latest release.
- `AHEAD/INCONSISTENT`: `refs/heads/release` is ahead of, unrelated to, or
  otherwise inconsistent with the latest provable formal release, or the
  intended target cannot fast-forward. Fail closed.
- `FORMAL_RELEASE_NOT_PROVABLE`: current source lacks sufficient version,
  changelog or closure evidence. Fail closed for release advancement and do not
  treat newer `main` as formal.

Daily `update Bridge Kit` may consume this classification but remains read-only
with respect to `refs/heads/release`. Only formal producer closure may advance
that ref.
