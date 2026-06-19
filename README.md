# AI Skills Collection

Central library for personal Codex/agent skills. The repository keeps the full skill collection; installation is explicit and can target a repo, the user-level skills directory, or an advanced legacy codex-home directory.

Default paths:

- Repo-specific: `<project>/.agents/skills/`
- User-level global: `$HOME/.agents/skills/`
- Explicit legacy compatibility: `${CODEX_HOME:-$HOME/.codex}/skills/`

Use the generated catalog first, then install a profile, a complete domain, or precise single skills.

## One-Time CLI Setup

Install the short command from this checkout:

```bash
python3 -m pip install --no-build-isolation -e /path/to/AI_Skills_Collection
```

Then use `ai-skills` from any repo:

```bash
ai-skills --help
ai-skills doctor
ai-skills select
ai-skills list --domain bayesian
```

The long-form fallback remains available when the editable command is not installed:

```bash
python3 /path/to/AI_Skills_Collection/scripts/skills.py --help
```

## Main Commands

Use this as the command cheat sheet.

Help and diagnostics:

```bash
ai-skills --help
ai-skills install --help
ai-skills doctor
```

Browse:

```bash
ai-skills list --domain bayesian
ai-skills list --domain bioinformatics
ai-skills list --scope writing
ai-skills catalog --write
```

Interactive install:

```bash
ai-skills select
```

Install into the current repo:

```bash
ai-skills install --target repo --domain bayesian --mode symlink --write-agents-md
```

Install a complete domain:

```bash
ai-skills install --target repo --domain bioinformatics --mode symlink --write-agents-md
```

Install one precise skill:

```bash
ai-skills install --target repo --skill domain/bayesian/pymc --mode symlink --write-agents-md
```

Install multiple precise skills:

```bash
ai-skills install --target repo \
  --skill domain/bayesian/pymc \
  --skill domain/bayesian/bayesian-ppl-diagnostics \
  --mode symlink --write-agents-md
```

Bootstrap user-level core skills:

```bash
ai-skills install --target user --profile codex-core-global --mode symlink
ai-skills install --target user --profile codex-writing-style --mode symlink
```

Explicit legacy codex-home install:

```bash
ai-skills install --target codex-home --profile codex-core-global --mode symlink --dry-run
```

Validate before committing:

```bash
ai-skills registry --write
ai-skills validate
ai-skills audit --all
ai-skills catalog --write
```

## Installation Models

Profiles are curated combinations for a project or global bootstrap. Domains are complete field collections. Single-skill selectors are exact installs.

Complete domain installs are supported. If `audit` warns about total description length or active skill count, treat that as a context-budget warning, not an installation error.

Examples:

```bash
ai-skills install --target repo --profile codex-bayesian-jsdm --mode symlink --write-agents-md
ai-skills install --target repo --domain bayesian --mode symlink --write-agents-md
ai-skills install --target user --profile codex-writing-style --mode symlink --dry-run
ai-skills install --target codex-home --profile codex-core-global --mode symlink --dry-run
```

`--target codex-home` is explicit, legacy, and advanced. The CLI prints detected `CODEX_HOME`, resolved codex home, target skills root, `config.toml` status, and writability before installing.

## Layout

Root folders:

- `skills/`: the central skill library. This is the main source of installable skills.
- `profiles/`: curated skill sets for common global or project setups.
- `bundles/`: legacy bundle definitions kept for compatibility with `scripts/install_bundle.py`; prefer profiles/domains for new installs.
- `docs/`: necessary user-facing and generated documentation: installation, migration, authoring, generated skill catalog, and generated domain pages.
- `scripts/`: necessary CLI implementation and compatibility wrappers. `scripts/skills.py` is the source CLI; `ai-skills` is the short installed entrypoint.
- `shared/`: necessary shared material used in more than one place. It currently holds the AGENTS.md managed-block template validated by the CLI and a frontend UI/UX reference pack linked by multiple frontend skills.
- `palette/`: shared visual palette data used by design/visualization skills. Keep separate from `shared/` because it is a concrete machine-readable palette asset.
- `registry.json`: generated machine-readable registry.
- `setup.py` and `ai_skills_cli/`: editable-install wrapper that provides the `ai-skills` command.

Skill folders:

- `skills/domains/`: complete domain-installable areas such as `bayesian`, `bioinformatics`, and medical domains.
- `skills/tools/`: cross-project tool capabilities such as data science, frontend, documents, and visualization.
- `skills/writing/`: first-class writing skills, split into globally useful `core` guardrails and `research` writing workflows.
- `skills/science/`: research discovery, communication, and ideation workflows.
- `skills/projects/`: project-specific skills.
- `skills/core/`: skill-library maintenance, installer, and system skills.
- `skills/archive/`: inactive, external, or misfit skills kept under version control for reference/migration. It is not gitignored; instead the registry excludes it by default unless `--include-archive` is used.
- `skills/**/references/`: longer domain knowledge, dated source notes, checklists, formulas, and legacy long-form material.

## Validation

Run before committing:

```bash
ai-skills registry --write
ai-skills validate
ai-skills audit --all
ai-skills catalog --write
```

## Documentation

- `docs/INSTALLATION.md`: CLI install patterns, SSH/HPC notes, symlink/copy, Windows/WSL, user vs codex-home.
- `docs/MIGRATION.md`: migrate old `.codex/skills` manifests to `.agents/skills`.
- `docs/SKILL_AUTHORING.md`: create skills, domains, references, descriptions, profiles, and trigger evals.
- `profiles/README.md`: profile vs domain vs single-skill selection.
