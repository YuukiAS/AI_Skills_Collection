# Phase 0 standalone-clone chat-confirmation probe

This directory records the harmless capability and authority probe required by
the approved v2.1 execution package and its standalone-clone recovery.

The probe never invokes Slurm. Its private binder accepts only the exact native
`request_user_input` question frozen for this test, an explicit `确认测试`
answer, matching session/turn/tool-use identifiers, and valid clone-private
runtime material. A valid event writes a harmless marker; empty, cancelled,
modified, replayed, or fabricated inputs fail closed.

## Initial Phase 0 result

`PHASE_0_CAPABILITY=FAIL`

The standalone clone itself is valid and an isolated trusted-identity
`hooks/list` readback discovered only the clone-local declarations below. It
did not discover a Hook from the canonical checkout.

| Event | Stable key | Current hash | Trust status |
| --- | --- | --- | --- |
| `PostToolUse` | `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1-standalone-clone/.codex/hooks.json:post_tool_use:0:0` | `sha256:93a4651d6b516e58cd5dff6e7acad7cba7ca56429ea245383f9eb5a03feadad8` | `untrusted` |
| `SessionStart` | `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1-standalone-clone/.codex/hooks.json:session_start:0:0` | `sha256:029721041a7b625109aaf425a9dd27319c5521a93ac8b2dd9500952c54386abb` | `untrusted` |

The current Codex identity is
`CODEX_HOME=/users/a/e/aereinh/.codex`. Its pre-trust `hooks.state` has no
entry for either key. The official app-server readback under that identity
failed closed before `hooks/list` because the exact standalone clone is not a
trusted project. Codex reported:

```text
Project-local config, hooks, and exec policies are disabled in the following
folders until the project is trusted, but skills still load.
1. /overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1-standalone-clone/.codex
```

The recovery authorization active at that point permitted only user action
through the official Hook trust UI for frozen Hook keys and hashes. It did not
permit adding project trust to user config. The clone-local Hook therefore
could not be loaded by the current Desktop identity and the live chat probe did
not start.

No DII or CARE candidate clone was created. No canonical checkout was changed.
No Slurm command was invoked. Phase 1, Gate A-D, publication, production render,
and production activation were not started.

## Project-trust recovery

`PROBE_READY_FOR_PROJECT_TRUST`

The user subsequently authorized one additional side effect: the user may use
the official Codex Desktop Project Trust UI to mark this exact standalone clone
as trusted. The executor has not written user config or invoked a config writer.

Pre-trust baseline:

```text
CODEX_HOME=/users/a/e/aereinh/.codex
TRUST_TARGET=/overflow/htzhu/mingcheng_new/AI_Skills_Collection-hpc--slurm-protected-partition-chat-confirmation-v2-1-standalone-clone
EXACT_PROJECT_TRUST=ABSENT
CONFIG_SHA256=cb5122666a7ed803aae07c7edc0ed46840c3b6047c75c6a08899119c907387c2
NON_TARGET_CONFIG_SHA256=90b86c9b5660d576c0549ec515eaef801c6897548587881ccd133ba2886dffb3
HOOK_STATE_COUNT=0
```

`NON_TARGET_CONFIG_SHA256` is the deterministic hash of the parsed user config
after removing only the exact target project entry. It must remain unchanged
after the official UI writes `trust_level = "trusted"` for this path.

## Superseding candidate-validation strategy

The user subsequently replaced the project-trust recovery requirement with a
narrower candidate strategy. The standalone clones remain code and offline
validation environments, but candidate project trust, candidate Hook live
loading, and the candidate `request_user_input` / `PostToolUse` Desktop probe
are no longer Phase 0 prerequisites. Those live checks move to canonical
production acceptance after independent review and a separate production
authorization.

This later instruction supersedes the earlier `PHASE_0_CAPABILITY=FAIL` as a
candidate blocker without changing the approved v2.1 product behavior. The
historical failure above is retained as evidence; it is not relabeled as a
successful live probe.

No project-trust or Hook-trust UI action occurred for the candidate clone. The
executor did not edit user-level Codex configuration, and no task-owned
`hooks.state` or `projects.<path>.trust_level` side effect was created. DII and
CARE standalone candidate clones were created only after this strategy change.
No canonical checkout was modified and no Slurm command was invoked.

## Frozen probe bytes

```text
config.toml sha256: 9ad97b103129e83e4930e37e1549b878d45a915c2f8daefed02ed03580578266
hooks.json sha256: 0c436e35c3c73a8fe8b2e28e9017a918cde2782d200dbc09cb7d497a788f7a3f
session_start_probe.py sha256: 04e4ad6ea866bf058391ba6f9c68d69a3e9340428340fbbfb991af56ad84a1c8
probe binder sha256: e7b8d8d722011cdb3f65591024df890d06719384a1da4eac9ffbec20fb8c1dd9
```
