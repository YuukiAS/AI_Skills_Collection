# Project Skill Installation

This page is kept for compatibility. The current installer is:

```bash
python3 scripts/skills.py install --target repo --project /path/to/project --profile codex-research-writing --mode symlink --write-agents-md
```

Repo-specific skills are installed to:

```text
<project>/.agents/skills/
```

The older `scripts/install_project_skills.py` remains as a wrapper, but new automation should call `scripts/skills.py` directly.

See:

- `docs/INSTALLATION.md`
- `docs/MIGRATION.md`
- `docs/SKILL_AUTHORING.md`
