# Migration

Older versions installed project skills under `<project>/.codex/skills/`. The recommended repo-specific path is now `<project>/.agents/skills/`.

## Inspect State

```bash
python3 scripts/skills.py doctor --project /path/to/repo
```

Doctor reports repo root, repo skills root, user skills root, detected codex home, codex-home skills root, legacy `.codex/skills` state, manifest state, and recommended commands.

## Dry Run Migration

```bash
python3 scripts/skills.py migrate-legacy --project /path/to/repo --dry-run
```

The migration reads `<project>/.codex/skills/.ai-skills-collection-manifest.json`, reinstalls managed skills into `<project>/.agents/skills/`, and updates the managed AGENTS.md block.

## Real Migration

```bash
python3 scripts/skills.py migrate-legacy --project /path/to/repo --mode symlink --yes
```

The old `.codex/skills` directory is not deleted. Keep it until the project works with `.agents/skills`.

## Safety Rules

- If `<project>/.codex` or `<project>/.codex/skills` resolves to `${CODEX_HOME:-$HOME/.codex}/skills`, migration refuses to modify it.
- Codex-home installs and migration are never default behavior.
- Existing codex-home skills are not pruned unless `--target codex-home --prune-managed` is explicit and the manifest proves this tool manages the paths.
