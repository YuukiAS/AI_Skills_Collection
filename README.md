# AI Skills Collection

Central library for personal Codex/agent skills. The repository keeps the full skill collection; installation is explicit and can target a repo, the user-level skills directory, or an advanced legacy codex-home directory.

Default paths:

- Repo-specific: `<project>/.agents/skills/`
- User-level global: `$HOME/.agents/skills/`
- Explicit legacy compatibility: `${CODEX_HOME:-$HOME/.codex}/skills/`

Use the generated catalog first, then install a profile, a complete domain, or precise single skills.

## Main Commands

Browse:

```bash
python3 scripts/skills.py list --domain bayesian
python3 scripts/skills.py catalog --write
```

Interactive install:

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py select
```

Install into the current repo:

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py install --target repo --domain bayesian --mode symlink --write-agents-md
```

Install one precise skill:

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py install --target repo --skill domain/bayesian/pymc --mode symlink --write-agents-md
```

Install multiple precise skills:

```bash
python3 scripts/skills.py install --target repo \
  --skill domain/bayesian/pymc \
  --skill domain/bayesian/bayesian-ppl-diagnostics \
  --mode symlink --write-agents-md
```

Bootstrap user-level core skills:

```bash
python3 scripts/skills.py install --target user --profile codex-core-global --mode symlink
```

Doctor:

```bash
python3 scripts/skills.py doctor
```

## Installation Models

Profiles are curated combinations for a project or global bootstrap. Domains are complete field collections. Single-skill selectors are exact installs.

Complete domain installs are supported. If `audit` warns about total description length or active skill count, treat that as a context-budget warning, not an installation error.

Examples:

```bash
python3 scripts/skills.py install --target repo --profile codex-bayesian-jsdm --mode symlink --write-agents-md
python3 scripts/skills.py install --target repo --domain bayesian --mode symlink --write-agents-md
python3 scripts/skills.py install --target user --profile codex-writing-style --mode symlink --dry-run
python3 scripts/skills.py install --target codex-home --profile codex-core-global --mode symlink --dry-run
```

`--target codex-home` is explicit, legacy, and advanced. The CLI prints detected `CODEX_HOME`, resolved codex home, target skills root, `config.toml` status, and writability before installing.

## Layout

- `skills/domains/`: complete domain-installable areas such as `bayesian`, `bioinformatics`, and medical domains.
- `skills/tools/`: cross-project tool capabilities such as data science, frontend, documents, and visualization.
- `skills/writing/`: first-class writing skills, split into globally useful `core` guardrails and `research` writing workflows.
- `skills/science/`: research discovery, communication, and ideation workflows.
- `skills/projects/`: project-specific skills.
- `skills/core/`: skill-library maintenance, installer, and system skills.
- `skills/archive/`: inactive or external plugin skills kept for reference.
- `skills/**/references/`: longer domain knowledge, dated source notes, checklists, formulas, and legacy long-form material.
- `profiles/`: curated skill sets.
- `scripts/skills.py`: unified CLI for list/catalog/install/select/new/validate/audit/registry/doctor/migrate-legacy.
- `registry.json`: generated machine-readable registry.
- `docs/SKILL_CATALOG.md`: generated catalog.
- `docs/domains/`: generated domain pages.
- `shared/templates/AGENTS.md.template`: managed routing block template.

## Validation

Run before committing:

```bash
python3 scripts/skills.py registry --write
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
python3 scripts/skills.py catalog --write
```

## Documentation

- `docs/INSTALLATION.md`: CLI install patterns, SSH/HPC notes, symlink/copy, Windows/WSL, user vs codex-home.
- `docs/MIGRATION.md`: migrate old `.codex/skills` manifests to `.agents/skills`.
- `docs/SKILL_AUTHORING.md`: create skills, domains, references, descriptions, profiles, and trigger evals.
- `profiles/README.md`: profile vs domain vs single-skill selection.
