# PIE 0.1 ChatGPT Web wrapper update

Date: 2026-10-07

Final standalone Skill source commit:

```text
b296fe64437f6a0f15a9d91c3881d2cb54db0ec0
```

ChatGPT personal Plugin:

```text
plugin_id=plugins_6ac24c3637188191937fe99610ace3f2
wrapper_version_before=0.2.3
wrapper_version_after=0.2.4
release_id=pluginrel_6ac5e77752cc8191af28a4174fe2b4b4
scope=USER
discoverability=PRIVATE
```

The live wrapper was updated to the exact PIE 0.1 source for the two changed
runtime files:

```text
skills/project-instructions-editor/SKILL.md
skills/project-instructions-editor/references/editor-contract.md
```

Before upload, Git blob identity of the reconstructed wrapper payload was checked
against exact source commit `b296fe64437f6a0f15a9d91c3881d2cb54db0ec0`:

```text
SKILL.md blob = 76d30206b0a7890a9f5ceb8b4345e845cf903141
editor-contract.md blob = 69862356340bd147051b552ce5b63d6f48d0cb25
```

Post-update readback confirmed:

```text
wrapper_version=0.2.4
Skill version=0.1
semantic spine present
scope dominance present
dynamic-set abstraction present
internal edit-mode labels hidden in ordinary output
```

The wrapper remains PRIVATE / USER scope and adds no MCP finalizer, external
model provider, sibling-Skill chain, hosted service, or API key.

Historical comparison used for repository-side acceptance:

- C6 `6ddab9029bbd96a21d7e5bf0317f7674c66cd909` remains the useful structural
  development reference: false no-op avoided, volatile inventory moved behind
  a source bridge, broad production authorization preserved, compact setting.
- C7-C11 remain failure evidence for the reader-layer implementation path and
  are not reclassified.
- Current `b296fe64...` restores the C6 structural strengths generically while
  retaining later protected-absence, no-op, exact-identity, and user-output
  fixes.

Remaining release blocker: one fresh normal-entry Server+VPS Project acceptance
using this live wrapper.

C11 reader-layer failure preserved; not reclassified as PASS.
