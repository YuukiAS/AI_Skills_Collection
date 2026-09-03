# Codex App Marketplace

This repository has two layers:

- `skills/` and `profiles/` are the source layer. Edit these when changing skill behavior or profile membership.
- `.agents/plugins/marketplace.json` is the generated Codex App repo marketplace manifest.
- `plugins/codex/plugins/` is the generated plugin payload layer. It is self-contained and does not depend on source files outside the generated plugin directories.
- `scripts/codex_marketplace_config.json` is the Codex App publication config. It deliberately publishes fewer app-facing plugins and skills than the local CLI profiles.

## Install In Codex App

Add a Git plugin marketplace with:

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Git reference: main
Sparse paths:
.agents/plugins
plugins/codex/plugins
```

Enter the sparse paths as two separate lines. `.agents/plugins` provides the
repo marketplace manifest. `plugins/codex/plugins` provides the plugin payloads.
Sparse checkout does not redefine the repository root, so the manifest must
remain at `.agents/plugins/marketplace.json` relative to the real checkout root.

The generated marketplace currently publishes ten curated plugins. This is the repository's current app-facing publication budget, not a general Codex plugin limit:

- `workflow-core`
- `ai-skills-core`
- `writing-style`
- `research-writing`
- `presentations`
- `scientific-visualization`
- `web-development`
- `statistical-modeling`
- `bioinformatics`
- `medical-imaging`

Each plugin carries active skills under its own `skills/` directory. Some active
skills are aggregate skills: they expose one Codex trigger boundary while copying
their detailed source workflows under a compact `_src/<source-id>/` directory
inside the active skill. The publication layer uses copied snapshots, not
symlinks.

The physical directory names in `plugins/codex/plugins/` are short artifact ids from
`scripts/codex_marketplace_config.json`. They do not change plugin names,
frontmatter `name`, or provenance. Source provenance continues to use canonical
`skills/...` paths in `source_skills`.

## Windows Path Budget

The marketplace is designed to install through the same Codex App Git sparse
checkout on Windows:

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Git reference: main
Sparse paths:
.agents/plugins
plugins/codex/plugins
```

The builder enforces a repository-relative path budget of 140 characters for
the root manifest and every generated file and directory under
`plugins/codex/plugins/`. This includes the sparse paths themselves and is
checked on Linux as well as Windows.

`Filename too long` was historically caused by aggregate source snapshots using
full flattened source paths such as `references/source-skills/<full-source>/`.
The fix is the compact generated layout, not asking ordinary users to enable
`core.longpaths` or move Codex App to a shorter directory.

`marketplace root does not contain a supported manifest` means the sparse
checkout did not include `.agents/plugins/marketplace.json` at the real
repository root. Use both sparse paths shown above; do not use `plugins/codex`
as a single marketplace root.

## Local Build

After changing `skills/`, `profiles/`, or `scripts/codex_marketplace_config.json`,
regenerate and validate the marketplace:

```bash
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --path-report
```

Before opening a pull request, also run:

```bash
python3 -m unittest discover -s tests
python3 scripts/build_codex_marketplace.py --check
python3 scripts/build_codex_marketplace.py --path-report
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
```

If a PR check fails after marketplace generation, the usual cause is that
`.agents/plugins/marketplace.json` or `plugins/codex/plugins/` was not
regenerated and committed.

## Integration / Release Gate

The `.github/workflows/codex-marketplace.yml` workflow is a heavyweight
integration/release gate. It runs on pull requests and explicit
`workflow_dispatch`. Ordinary pushes to `main` or `reviewed/**` do not launch
the full matrix.

The workflow is read-only. It regenerates and validates the generated layer in
the runner, then fails if `.agents/plugins/marketplace.json` or
`plugins/codex/plugins/` would change. Canonical generated files must be
produced by the Executor before commit:

```bash
python3 scripts/build_codex_marketplace.py --write
git diff
git add .agents/plugins/marketplace.json plugins/codex/plugins
git commit
```

CI must not push a generated commit back to the repository. This prevents a
push -> generated commit -> second CI loop and keeps generated parity as a
verification gate, not an automation side effect.

## Metadata Rules

Marketplace builds fail when active skill names collide across plugins, source
skills contain `[TODO:` placeholders, source snapshots include symlinks, or a
published source skill references secret environment variables not declared in
frontmatter. Builds also fail when generated paths exceed the Windows path
budget. Aggregate skills use `provenance: generated` and keep their source skill
paths in `source_skills`.
