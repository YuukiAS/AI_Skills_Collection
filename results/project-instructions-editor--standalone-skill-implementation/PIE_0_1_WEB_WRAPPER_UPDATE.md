# PIE 0.1 ChatGPT Web wrapper update

Date: 2026-10-07

Final standalone Skill source commit:

```text
8eebd7fb988b4415704d1555dd0adab48e204465
```

ChatGPT personal Plugin:

```text
plugin_id=plugins_6ac24c3637188191937fe99610ace3f2
wrapper_version_before=0.2.4
wrapper_version_after=0.2.5
release_id=pluginrel_6ac60cfbe30c819191bff2296bfc8b9d
scope=USER
discoverability=PRIVATE
```

The live wrapper was updated after repository-side validation. The two changed
runtime files were reconstructed from the exact `8eebd7fb...` source and
verified by Git blob identity before upload:

```text
skills/project-instructions-editor/SKILL.md
blob=e7c404825d45afed25c71fe894d45b1c6f1ffc99
size=14637 bytes

skills/project-instructions-editor/references/editor-contract.md
blob=2af1d2b9aad1839d22df90e6a4e5292f4ca07f38
size=22522 bytes
```

Post-update readback confirmed:

```text
wrapper_version=0.2.5
Skill version=0.1
Runtime Kernel=present
Allowed Durable Meaning Set=present
bidirectional reconciliation=present
semantic-vs-surface radius separation=present
scope dominance + protected absence=present
global dynamic-set abstraction=present
```

The wrapper remains PRIVATE / USER scope. No MCP finalizer, sibling-Skill chain,
external model provider, hosted service, or API key was introduced.

Remaining release blocker: exactly one fresh normal-entry Server+VPS ChatGPT Web
acceptance using this live wrapper. Per the frozen stop rule, if that first
complete response still materially copies the old section scaffold, leaks a
mutable source-owned set elsewhere, narrows a currently-live broad boundary,
adds unsupported history/best-practice-derived durable content, or fails
bidirectional semantic traceability, no further simple-core prompt repair should
be opened. The PIE 0.1 release scope must instead be narrowed.

C11 reader-layer failure preserved; not reclassified as PASS.
