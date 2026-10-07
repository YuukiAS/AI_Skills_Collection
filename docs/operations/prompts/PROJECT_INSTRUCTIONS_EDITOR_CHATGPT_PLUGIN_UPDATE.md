# Project Instructions Editor ChatGPT Plugin Update Handoff

Purpose: update the existing `skills-only` ChatGPT personal Plugin wrapper for
Project Instructions Editor. The wrapper is a distribution shell only; the
standalone Skill remains the capability source.

Source commit: `47f3a2d9caec295955040d90cfb19c0f4d3bf7a8`

Skill source:

```text
skills/core/codex-system/project-instructions-editor/
```

Files to copy into the wrapper Skill payload:

```text
SKILL.md
agents/openai.yaml
assets/app-facing.svg
evals/trigger_queries.json
references/editor-contract.md
```

Identity:

```text
Skill version: 0.1
Skill tree Git SHA: 48ea5f53132a10a38b966e0ee5ade73dd2db57f3
SKILL.md blob: b9aa8c3468294ed8196208588c7a2f52e2171171
Icon blob: 3f9db7f1d98308d53d45fe249c324da23d02de21
SKILL.md SHA-256: 2289dd487604699a123b362853754964b360d8af62e8f72b7751a4349a10706f
Icon SHA-256: 8b75cb827af0f02eb05e7cf1d133c5f0d0fb0c09950a4ae1f28a54111f1b10aa
```

Wrapper version:

- Change only if the existing wrapper release process requires a package
  version bump for replacing its embedded Skill payload.
- Do not change the standalone Skill version; it remains `0.1`.

Runtime boundary:

- Normal use must work in ordinary ChatGPT Web / Project chat.
- No MCP finalizer, `OPENAI_API_KEY`, hosted service, sibling-Skill chain,
  external model provider, or paid API call is part of PIE v0.1.
- PIE v0.1 edits long-lived ChatGPT Project instructions. It does not guarantee
  cross-turn final reader-layer behavior for all future answers.

C11 reader-layer failure preserved; not reclassified as PASS.
