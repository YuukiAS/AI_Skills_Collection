# PIE 0.1 ChatGPT Web wrapper update

Date: 2026-10-07

Standalone Skill source commit:

```text
47f3a2d9caec295955040d90cfb19c0f4d3bf7a8
```

Closure branch observed before wrapper update:

```text
work/project-instructions-editor--0.1-closure
b4a93960acb5f42334cb42649bd87aef61aa4b4f
```

ChatGPT personal Plugin:

```text
plugin_id=plugins_6ac24c3637188191937fe99610ace3f2
wrapper_version_before=0.2.1
wrapper_version_after=0.2.2
release_id=pluginrel_6ac5c9e43f1c8191806259956695dea8
scope=USER
discoverability=PRIVATE
```

The wrapper payload was updated to the PIE 0.1 source files from commit
`47f3a2d9caec295955040d90cfb19c0f4d3bf7a8`:

```text
SKILL.md
agents/openai.yaml
assets/app-facing.svg
evals/trigger_queries.json
references/editor-contract.md
```

The standalone Skill version remains `0.1`. The wrapper package version is
independent and was advanced to `0.2.2` because Plugin Creator requires a new
wrapper version for an update.

Post-update readback confirmed the current personal Plugin release contains the
PIE 0.1 runtime boundary, including:

```text
ADVANCED_INDEPENDENT_MULTI_CALL_FINALIZATION=UNSUPPORTED
CROSS_TURN_FINAL_READER_LAYER_GUARANTEE=UNSUPPORTED_IN_PIE_0_1
```

No MCP finalizer, external model provider, sibling-Skill chain, hosted service,
or API key was added.

Remaining release blocker: one fresh normal-entry Server+VPS Project acceptance
using the updated wrapper. Reader-layer language quality is out of scope for PIE
0.1 and remains tracked under Clear Writing #13.

C11 reader-layer failure preserved; not reclassified as PASS.
