# Project Skill Installation

This repository supports a tiny global loader plus project-local skills.

## When The User Only Says "Install Skills"

The global `project-skill-installer` skill handles prompts such as:

- "为这个项目安装 skills"
- "给这个 repo 配 skills"
- "setup skills for this project"
- "install project skills"

It should identify the current project root, locate the central
`AI_Skills_Collection` repository, and run:

```bash
python3 scripts/install_project_skills.py --project /path/to/project --profile auto --mode symlink --write-agents-md
```

When the user's sentence states the purpose, pass that text with `--intent`.
This lets an empty new folder still route correctly:

```bash
python3 scripts/install_project_skills.py --project /path/to/project --profile auto --intent "build a website" --mode symlink --write-agents-md
```

The installer auto-detects the project type from both intent and files, installs
a small profile into the project's `.codex/skills/`, writes a project manifest,
and creates or updates the managed routing block in `AGENTS.md`.

## Sync Rules

The project manifest is local to that project:

`<project>/.codex/skills/.ai-skills-collection-manifest.json`

Later syncs may update or remove only skill directories listed in that manifest.
They must not delete user-written project files, affect other projects, or clean
global `~/.codex/skills`.

## Global Bootstrap

Run occasionally, not per project:

```bash
python3 scripts/install_project_skills.py --global --profile codex-core-global --mode symlink
```

This installs only the tiny global management skills. It is not a profile
switcher.

## WSL And Windows

Use Linux filesystem paths for WSL projects when possible. If a project lives on
a Windows-mounted drive or symlink permissions fail, use `--mode copy`; the
installer also automatically falls back to copy mode and records the mode in the
manifest.
