# PIE 0.1 Web Acceptance Handoff

Status: `PENDING_USER_WEB_ACTION`

## Wrapper Package

Archive:

```text
private/exports/project-instructions-editor--0.1-closure/project-instructions-editor-v0.1-wrapper-update.zip
```

SHA-256:

```text
b0f37935187a9f54dc0389598e3b6aa37d312ef4ab7a63120d6febd37614b8ea
```

Manifest:

```text
private/exports/project-instructions-editor--0.1-closure/project-instructions-editor-v0.1-wrapper-update.MANIFEST.json
```

Manifest SHA-256:

```text
edcad6c2aec6d61892f8a2532bea6977ebb36dd00041e5a6d8274d95f3f5b8e4
```

## Acceptance Scope

Run against the existing private/user `project-instructions-editor` ChatGPT Web
wrapper after updating it from the package above. Do not create a second wrapper.

Acceptance checks only PIE 0.1 editor semantics:

- semantic fidelity;
- source ownership and locator behavior;
- bounded edit / no-op eligibility;
- protected absence;
- authorization, privacy, safety and evidence strength;
- fail-closed degradation when input is missing;
- exact identifiers;
- budget/headroom.

Natural Chinese continuity, removal of all ordinary English, and mechanical line
wrapping across future ChatGPT turns are not PIE 0.1 blockers. C11 reader-layer
failure remains preserved and is not reclassified as PASS.

## Minimal Fresh-Thread Prompt

```text
帮我重新审一下这个 Project 现在的长期 instructions，看有没有还应该调整的地方。
只做确实有必要的长期修改，不要重做整个 Project。
如果需要改，给我完整可替换版本和简短理由；如果不需要改，就说明为什么。
不要实际修改账号、网络、服务或远程资源。
```

Record the first complete assistant response. Do not provide a translation list,
expected answer, or reader-layer hint.
