# Released AI Skills Maintainer G2 Smoke V2

Use the installed production plugin `ai-skills-core@yuukias-ai-skills`.

Normal user request:

```text
sync this machine
```

This is a read-only released normal-entry smoke.

Allowed reads:

- the provided input file;
- the installed production plugin manifest and skill snapshot for
  `ai-skills-core@yuukias-ai-skills`;
- `codex plugin list --marketplace yuukias-ai-skills --available --json`;
- `codex --version`.

Do not run generic help commands, feature-list commands, Git commands, network
commands, Marketplace mutation, plugin install/remove/update commands, Bridge
commands, Host commands, or project-consumer commands.

Report whether the released AI Skills Maintainer normal entry is loaded, which
internal skill owns `sync this machine`, the installed `ai-skills-core` version
and plugin path if visible, and the expected user-facing state for an already
updated current session.
