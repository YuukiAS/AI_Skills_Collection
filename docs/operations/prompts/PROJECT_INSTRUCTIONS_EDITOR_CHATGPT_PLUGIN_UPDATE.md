# Project Instructions Editor ChatGPT Plugin Wrapper

The existing PRIVATE / USER-scope `skills-only` ChatGPT personal Plugin is a
distribution shell for the standalone Project Instructions Editor Skill. The
standalone Skill remains the only capability source.

## Current identity

- Accepted Skill candidate: `f0e41f49b46be1a3b9f3c499cb580066f694b031`
- Main integration commit: `55b8d93d8f9a0f120ac7100b2af75caf9a2182a0`
- Standalone Skill version: `0.2`
- PRIVATE / USER wrapper version: `0.2.8`
- Wrapper status: updated and verified through real ChatGPT Web acceptance

The wrapper payload contains exactly:

```text
SKILL.md
agents/openai.yaml
assets/app-facing.svg
evals/trigger_queries.json
references/editor-contract.md
```

Canonical source:

```text
skills/core/codex-system/project-instructions-editor/
```

Runtime file identities:

```text
SKILL.md: caa3c99ef6e09742cd04f247cdff20af23970391
agents/openai.yaml: 1473d6ad6db11eb7619be7608abd524015912e69
assets/app-facing.svg: 3f9db7f1d98308d53d45fe249c324da23d02de21
evals/trigger_queries.json: 5cb66e82b062e4f679360e7b7017d55ef3e69f7d
references/editor-contract.md: 49af7c39f13d929d9ba2f4bedf2d59460a30a91f
```

## Boundary

Normal use works in ordinary ChatGPT Web / Project chat. The wrapper adds no
MCP finalizer, `OPENAI_API_KEY`, hosted service, sibling-Skill chain, external
model provider, or paid API call. Project Instructions Editor v0.2 does not
claim automatic implicit invocation or a cross-turn final reader-layer
guarantee.

The C11 reader-layer failure remains historical failure evidence and is not
reclassified as PASS.
