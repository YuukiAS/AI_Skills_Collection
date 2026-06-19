# Installation

Use `ai-skills` as the normal entry point after one editable install. On a new
server:

```bash
git clone <repo-url> AI_Skills_Collection
python3 -m pip install --no-build-isolation -e AI_Skills_Collection
ai-skills --help
```

This repository is installed from a local checkout. Keep the checkout available:
`--mode symlink` deployments point back to it, while `--mode copy` creates a
self-contained copy in the target.

Default target behavior:

- Omitted `--target` means `--target repo`.
- Repo installs write to `<project>/.agents/skills/`.
- User/global installs write to `$HOME/.agents/skills/`.
- `.codex/skills/` is not used by default. It is only used through explicit
  `--target codex-home` legacy compatibility.

If the short command is not installed yet, the exact fallback is:

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py --help
```

## Repo-Specific Install

From inside any git repo:

```bash
ai-skills install --target repo --domain bayesian --mode symlink --write-agents-md
```

If `--project` is omitted, the CLI detects the current git root. If the current directory is not a git repo, it uses the current directory and prints a warning.

Explicit project:

```bash
ai-skills install --target repo --project /path/to/repo --profile codex-research-writing --mode symlink --write-agents-md
```

Repo installs write:

- `<project>/.agents/skills/<flat-skill-name>/`
- `<project>/.agents/skills/.ai-skills-collection-manifest.json`
- a managed block in `<project>/AGENTS.md` when `--write-agents-md` is set

## User Target

User-level global installs go to `$HOME/.agents/skills/`.

```bash
ai-skills install --target user --profile codex-core-global --mode symlink
ai-skills install --target user --profile codex-writing-style --mode symlink --dry-run
```

Keep user-level installs small unless you intentionally want broad cross-project skills.

## Codex-Home Target

Codex-home is explicit legacy/advanced compatibility:

```bash
ai-skills install --target codex-home --profile codex-core-global --mode symlink --dry-run
```

The path is `${CODEX_HOME:-$HOME/.codex}/skills`. The CLI prints detected `CODEX_HOME`, resolved codex home, target skills root, whether `config.toml` exists, writability, and a legacy target warning.

## Domain, Profile, And Single Skills

Complete domain:

```bash
ai-skills install --target repo --domain bayesian --mode symlink --write-agents-md
```

Precise skills:

```bash
ai-skills install --target repo --skill domain/bayesian/pymc --skill domain/bayesian/bayesian-ppl-diagnostics --mode symlink --write-agents-md
```

Profile:

```bash
ai-skills install --target repo --profile codex-bayesian-jsdm --mode symlink --write-agents-md
```

## Interactive Selection

```bash
ai-skills select
```

The selector chooses target, project path, strategy, profile/domain/single skills, mode, AGENTS.md write, and prune policy. It uses InquirerPy when available:

```bash
python3 -m pip install InquirerPy
```

Without InquirerPy it prints equivalent non-interactive commands.

## Symlink Vs Copy

Use `--mode symlink` for central-library development and easy updates. Use `--mode copy` when symlinks are unreliable, especially on Windows-mounted drives.

## HPC, SSH, And tmux

Use non-interactive commands in SSH/tmux or scheduled jobs. Prefer `--dry-run` first when targeting user or codex-home. Avoid interactive selection on terminals that do not pass arrow/space keys reliably.

## Windows And WSL

Prefer WSL Linux filesystem paths for symlinks. For `/mnt/c/...` projects, use `--mode copy` if symlink permissions fail.

## Pruning

Default installs only add or update selected managed skills. `--prune-managed` removes only entries recorded in this tool's manifest that are absent from the new selection. It never removes user-created skills outside the manifest.
