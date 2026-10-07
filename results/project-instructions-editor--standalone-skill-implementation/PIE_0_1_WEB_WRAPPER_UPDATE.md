# PIE 0.1 ChatGPT Web wrapper update

Date: 2026-10-07

## Current live wrapper

The personal ChatGPT Plugin has been updated to the exact historical runtime
source that previously backed live wrapper 0.2.1.

```text
plugin_id=plugins_6ac24c3637188191937fe99610ace3f2
wrapper_version_before=0.2.6
wrapper_version_after=0.2.7
release_id=pluginrel_6ac643171b788191a0f3f44fc5c6827d
scope=USER
discoverability=PRIVATE
```

Historical runtime source:

```text
6c098ce07d9a01e2d2e353841443d2f13a943dc6
historical_live_wrapper_version=0.2.1
```

Restoration branch source:

```text
01423430eb61529518cc7e3fa5993bc17e617947
packaging_head=142d1c52df197dbda5034fbe06ebc3b64fc0650b
```

The Codex-produced source payload candidate was verified before the live update:

```text
candidate_sha256=5f0c9e36484e856f3c8d04f168e1b52be3589db4cb0b0acf550eca4f9ce1ce90
runtime_subtree_exact=YES
later_fixes_ported=NO
```

The live wrapper update archive changed only the wrapper manifests to version
0.2.7 and overlaid the exact historical runtime files.

Post-update readback was compared byte-for-byte against GitHub commit
`6c098ce07d9a01e2d2e353841443d2f13a943dc6`.

```text
SKILL.md=EXACT
blob=5cd97e087c0e3747a514cd82f0b00ffebd2b5b0a

agents/openai.yaml=EXACT
blob=d84c958a7be2092c06d944007ceb14c09ca1d180

assets/app-facing.svg=EXACT
blob=3f9db7f1d98308d53d45fe249c324da23d02de21

evals/trigger_queries.json=EXACT
blob=f79d719756e57bd53b5e962f4f565c318568e174

references/editor-contract.md=EXACT
blob=2a4932ff0b01e2d3021959d9a97b2923550ae0dd
```

Both wrapper manifests read back as version 0.2.7.

This update intentionally does not port later PIE repairs. It exists to test one
question cleanly: whether the exact historical runtime that backed the known
good 0.2.1 period reproduces the desired Server+VPS Project-instruction behavior
in ordinary ChatGPT Web today.

No MCP finalizer, sibling-Skill chain, external provider, hosted service, or API
key was added.

Remaining step: one fresh Server+VPS normal-entry Web test using the same natural
Project-instructions review prompt. Judge the first complete answer only.

C11 reader-layer failure remains preserved; not reclassified as PASS.
