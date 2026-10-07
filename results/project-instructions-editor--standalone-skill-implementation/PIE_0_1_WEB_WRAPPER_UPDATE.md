# PIE 0.1 ChatGPT Web wrapper update

Date: 2026-10-07

Final standalone Skill source commit:

```text
9cdbe8ed712caf3a3a90592cd09c61ac146d9b02
```

ChatGPT personal Plugin:

```text
plugin_id=plugins_6ac24c3637188191937fe99610ace3f2
wrapper_version_before=0.2.2
wrapper_version_after=0.2.3
release_id=pluginrel_6ac5d8c91bb88191821b02a96cdba816
scope=USER
discoverability=PRIVATE
```

The live wrapper was updated with the exact final PIE 0.1 source for:

```text
skills/project-instructions-editor/SKILL.md
skills/project-instructions-editor/references/editor-contract.md
```

Post-update readback confirmed wrapper version `0.2.3`, Skill version `0.1`,
and current embedded file sizes matching the final source payload:

```text
SKILL.md=16028 bytes
references/editor-contract.md=14705 bytes
```

The final source keeps the surface-consolidation repair and the tightened
user-output contract: normal user replies do not print internal edit-mode labels,
semantic maps, disposition tables, or invariant checklists unless formal audit
evidence is requested.

No MCP finalizer, external model provider, sibling-Skill chain, hosted service,
or API key was added.

Remaining release blocker: one fresh normal-entry Server+VPS Project acceptance
using this live wrapper. Reader-layer behavior beyond the current edited Project
setting remains out of PIE 0.1 scope and stays with Clear Writing #13.

C11 reader-layer failure preserved; not reclassified as PASS.
