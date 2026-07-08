# Codex App Marketplace

This repository has two layers:

- `skills/` and `profiles/` are the source layer. Edit these when changing skill behavior or profile membership.
- `plugins/codex/` is the generated Codex App publication layer. It is self-contained for sparse checkout installation and does not depend on files outside that directory.
- `scripts/codex_marketplace_config.json` is the Codex App publication config. It deliberately publishes fewer app-facing plugins and skills than the local CLI profiles.

## Install In Codex App

Add a Git plugin marketplace with:

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Git reference: main
Sparse path: plugins/codex
```

The generated marketplace currently publishes six curated plugins:

- `ai-skills-core`
- `workflow-writing`
- `web-development`
- `research-writing`
- `statistical-modeling`
- `bio-medical-imaging`

Each plugin carries active skills under its own `skills/` directory. Some active
skills are aggregate skills: they expose one Codex trigger boundary while copying
their detailed source workflows under `references/source-skills/`. The
publication layer uses copied snapshots, not symlinks.

## Local Build

After changing `skills/`, `profiles/`, or `scripts/codex_marketplace_config.json`,
regenerate and validate the marketplace:

```bash
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
```

Before opening a pull request, also run:

```bash
python3 scripts/build_codex_marketplace.py --check
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
```

If a PR check fails after marketplace generation, the usual cause is that
`plugins/codex/` was not regenerated and committed.

## Release Workflow

The `.github/workflows/codex-marketplace.yml` workflow runs on pull requests,
pushes to `main`, and manual `workflow_dispatch`.

Pull requests only check the generated layer and fail if `plugins/codex/` is out
of date. Pushes to `main` and manual runs regenerate and validate the layer; if
`plugins/codex/` changes, the workflow commits the generated files back with:

```text
chore: publish codex marketplace [skip codex-marketplace]
```

The skip marker prevents the follow-up workflow run from creating another
publish commit.
