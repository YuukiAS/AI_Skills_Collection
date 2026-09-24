# Canonical ai-bridge Delegation

Use the installed Bridge CLI as the implementation owner for Bridge runtime surfaces.

Allowed discovery and verification:

- resolve `ai-bridge` on PATH;
- run `ai-bridge --version` or the current version surface;
- run `ai-bridge where` when available;
- inspect the returned source/runtime root;
- verify package/runtime path and version after refresh.

Delegate behavior to canonical `ai-bridge` commands for:

- `ai-bridge host install/status/validate`;
- Host Policy generation and validation;
- Lite init/validate;
- Review, Control, Persistent Run and other Bridge consumer install/validate;
- plugin replay runtime;
- managed Bridge consumer/template refresh.

Do not implement alternate Host Policy generation, Human Gate transport, plugin replay runtime, Bridge validator logic, daemon/watchers, or a second Bridge state machine in AI_Skills.

When release impact declares Host or consumer work, call the canonical Bridge command and record command, target, version/path and validation result. When no Bridge update impact is declared, leave Host and optional consumers unchanged.
