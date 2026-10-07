# PIE 0.1 ChatGPT Web wrapper update

Date: 2026-10-07

Final standalone Skill source commit:

```text
162199ccfa69509033422411b24e58520effd331
```

ChatGPT personal Plugin:

```text
plugin_id=plugins_6ac24c3637188191937fe99610ace3f2
wrapper_version_before=0.2.5
wrapper_version_after=0.2.6
release_id=pluginrel_6ac62ecb0034819182b814bb1652ff05
scope=USER
discoverability=PRIVATE
```

The Codex run could not create its wrapper candidate because the sandbox denied
the exact worktree export write. The ChatGPT-side wrapper update therefore used
an independently reconstructed delta archive built from the current live wrapper
manifest shape plus the exact final source files at
`162199ccfa69509033422411b24e58520effd331`.

Exact source identity was checked before upload:

```text
skills/project-instructions-editor/SKILL.md
git_blob=3d9c53633ae77c1c3ee917f168015ada947aa784
size=11182 bytes

skills/project-instructions-editor/references/editor-contract.md
git_blob=d391040431c3ac8e5e8f4f345b75cb697866cc4c
size=15952 bytes
```

Locally reconstructed delta archive:

```text
project-instructions-editor-v0.1-wrapper-0.2.6-live.zip
sha256=0a9f3ed150453cf5d5bebce19015d0bf8c9a2f91888893214fe9f31af9feb56b
```

Post-update readback confirmed:

```text
wrapper_version=0.2.6
Skill version=0.1
Simple Editing Core=present
K1-K7 Runtime Kernel=absent
Known-Good Candidate Construction=present
Protected Absence=present
C11 unsupported reader-layer boundary=present
```

The wrapper remains PRIVATE / USER scope. No MCP finalizer, sibling-Skill chain,
external model provider, hosted service, or API key was introduced.

Remaining release blocker: one fresh normal-entry Server+VPS ChatGPT Web
acceptance using this restored live wrapper. Compare the first complete response
against the user-confirmed earlier good structural baseline and the two recent
source-shaped failures.

C11 reader-layer failure preserved; not reclassified as PASS.
