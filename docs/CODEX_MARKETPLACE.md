# Codex App Marketplace

This repository has two layers:

- `skills/` and `profiles/` are the source layer. Edit these when changing skill behavior or profile membership.
- `plugins/codex/` is the generated Codex App publication layer. It is self-contained for sparse checkout installation and does not depend on files outside that directory.

## Install In Codex App

Add a Git plugin marketplace with:

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Git reference: main
Sparse path: plugins/codex
```

Each active `profiles/*.json` file becomes one Codex plugin. The generated
plugin copies the profile's primary `skills` list into its own `skills/`
directory. The publication layer uses copied snapshots, not symlinks.

## Local Build

After changing `skills/` or `profiles/`, regenerate and validate the marketplace:

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
