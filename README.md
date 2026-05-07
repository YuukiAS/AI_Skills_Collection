# AI Skills Collection

This repository is a central skill registry for multiple servers. It keeps
callable skills, shared palette resources, deployment bundles, and helper
scripts in one place so each machine can pull the same repo and install only
the parts it needs.

## Top-Level Layout

- `palette/`: Shared color palettes and palette metadata.
- `skills/`: Callable skills organized by reuse scope.
- `bundles/`: Named deployable subsets for different servers or workflows.
- `scripts/`: Registry, validation, and bundle installation helpers.
- `registry.json`: Generated index of every `SKILL.md`.

## Skill Scopes

- `skills/reusable/`: Cross-project skills for common work.
- `skills/research/`: High-value research workflow skills.
- `skills/domain/`: Field-specific reusable skills.
- `skills/project/`: Repo-specific skills.
- `skills/system/`: Agent and skill-management skills.

## Architecture Principles

- Organize callable skills by reuse scope, not upstream provenance.
- Keep `palette/` independent because it is a shared resource, not a skill.
- Use `bundles/` as the deployment contract for each server.
- Keep `registry.json` generated from the filesystem so paths stay accurate.

## Server Workflow

1. Pull this repository on a server.
2. Pick a bundle from `bundles/`.
3. Install that bundle into the target agent skill directory.
4. Validate the repo after local changes.
5. Regenerate `registry.json` after adding or moving skills.

Flat install is recommended for Codex/Cursor because each skill lands directly
under the target directory:

```bash
git clone https://github.com/YuukiAS/AI_Skills_Collection.git
cd AI_Skills_Collection
python3 scripts/install_bundle.py bundles/frontend.json --target ~/.codex/skills --mode flat
python scripts/validate_skills.py
python scripts/generate_registry.py
```

Tree install preserves repository-relative paths and is useful for mirroring:

```bash
python3 scripts/install_bundle.py bundles/base.json --target /opt/AI_Skills_bundle --mode tree
```

## Maintenance

Run these before committing:

```bash
python3 scripts/generate_registry.py
python3 scripts/validate_skills.py
find skills -type f -name '*.pyc' -delete
```
