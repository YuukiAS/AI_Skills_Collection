# Project Skill Installation

This page is kept for compatibility. The current installer is:

```bash
ai-skills install --target repo --project /path/to/project --profile codex-research-writing --mode symlink --write-agents-md
```

Repo-specific skills are installed to:

```text
<project>/.agents/skills/
```

The older `scripts/install_project_skills.py` remains as a wrapper, but new automation should call `ai-skills` directly. Use `ai-skills` only as a fallback when the editable command is not installed.

See:

- `docs/INSTALLATION.md`
- `docs/MIGRATION.md`
- `docs/SKILL_AUTHORING.md`
