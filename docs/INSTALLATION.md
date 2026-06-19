# Installation

Use `scripts/skills.py` as the single entry point.

## Repo-Specific Install

From inside any git repo:

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py install --target repo --domain bayesian --mode symlink --write-agents-md
```

If `--project` is omitted, the CLI detects the current git root. If the current directory is not a git repo, it uses the current directory and prints a warning.

Explicit project:

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py install --target repo --project /path/to/repo --profile codex-research-writing --mode symlink --write-agents-md
```

Repo installs write:

- `<project>/.agents/skills/<flat-skill-name>/`
- `<project>/.agents/skills/.ai-skills-collection-manifest.json`
- a managed block in `<project>/AGENTS.md` when `--write-agents-md` is set

## User Target

User-level global installs go to `$HOME/.agents/skills/`.

```bash
python3 scripts/skills.py install --target user --profile codex-core-global --mode symlink
python3 scripts/skills.py install --target user --domain reusable --mode symlink --dry-run
```

Keep user-level installs small unless you intentionally want broad cross-project skills.

## Codex-Home Target

Codex-home is explicit legacy/advanced compatibility:

```bash
python3 scripts/skills.py install --target codex-home --profile codex-core-global --mode symlink --dry-run
```

The path is `${CODEX_HOME:-$HOME/.codex}/skills`. The CLI prints detected `CODEX_HOME`, resolved codex home, target skills root, whether `config.toml` exists, writability, and a legacy target warning.

## Domain, Profile, And Single Skills

Complete domain:

```bash
python3 scripts/skills.py install --target repo --domain bayesian --mode symlink --write-agents-md
```

Precise skills:

```bash
python3 scripts/skills.py install --target repo --skill domain/bayesian/pymc --skill domain/bayesian/bayesian-ppl-diagnostics --mode symlink --write-agents-md
```

Profile:

```bash
python3 scripts/skills.py install --target repo --profile codex-bayesian-jsdm --mode symlink --write-agents-md
```

## Interactive Selection

```bash
python3 scripts/skills.py select
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
