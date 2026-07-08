# AI Skills Collection

Central library for personal Codex/agent skills. The repository keeps the full skill collection; installation is explicit and can target a repo, the user-level skills directory, or an advanced legacy codex-home directory.

Default paths:

- Repo-specific: `<project>/.agents/skills/`
- User-level global: `$HOME/.agents/skills/`
- Explicit legacy compatibility: `${CODEX_HOME:-$HOME/.codex}/skills/`

If `--target` is omitted, `ai-skills install` defaults to `--target repo` and
installs into the detected current repo's `.agents/skills/`. New installs do
not write `.codex/skills/` unless `--target codex-home` is explicitly selected.

Deployment installs are source-read-only: `ai-skills install ...` reads this
collection and writes only the selected target. It should not modify
`AI_Skills_Collection` itself unless you deliberately target this repository.
Commands that intentionally edit the collection are authoring/maintenance
commands such as `ai-skills new`, `ai-skills registry --write`, and
`ai-skills catalog --write`.

Use the generated catalog first, then install a profile, a complete domain, or precise single skills.

## One-Time CLI Setup

On a new server, clone this repository once and install the short command from
that checkout:

```bash
git clone <repo-url> AI_Skills_Collection
python3 -m pip install --no-build-isolation -e AI_Skills_Collection
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

This is intentionally an editable install from a local checkout, not a PyPI
package. Keep the checkout available. `--mode symlink` installs point back to
this central library; use `--mode copy` when the target repo must keep a
self-contained snapshot.

## Codex App Marketplace Install

For ordinary Codex App use, add this repository as a Git plugin marketplace:

- Source: `https://github.com/YuukiAS/AI_Skills_Collection.git`
- Git reference: `main`
- Sparse path: `plugins/codex`

The sparse path is a generated, self-contained marketplace root. Codex App can
install the profile-backed plugins from there without running `ai-skills` after
installation.

Developers can still use the `ai-skills` CLI for repo, user, and explicit
codex-home local installs. The marketplace publication layer and the CLI install
path coexist: `skills/` and `profiles/` remain the source layer, while
`plugins/codex/` is the generated Codex App distribution layer.

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
ai-skills install --target user --profile codex-workflow-core --mode symlink
ai-skills install --target user --profile codex-writing-style --mode symlink
```

`codex-writing-style` also installs `render-chinese-math-pdf`, because Chinese/math PDF rendering is a global writing/document workflow rather than a project-local domain skill.

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
ai-skills install --target user --profile codex-workflow-core --mode symlink --dry-run
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
- `docs/CODEX_MARKETPLACE.md`: Codex App marketplace publication layer and release workflow.
- `docs/MIGRATION.md`: migrate old `.codex/skills` manifests to `.agents/skills`.
- `docs/SKILL_AUTHORING.md`: create skills, domains, references, descriptions, profiles, and trigger evals.
- `profiles/README.md`: profile vs domain vs single-skill selection.
