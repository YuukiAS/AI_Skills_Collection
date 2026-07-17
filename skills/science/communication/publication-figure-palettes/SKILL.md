---
name: publication-figure-palettes
description: Choose publication figure palettes, contextual Notion-derived style candidates, presets, and snippets with provenance and experimental gates.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: false
executes_code: true
secrets_needed:
last_reviewed: 2026-07-17
profile_tags:
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Publication Figure Palettes

Use this skill when a user asks which palette to use for a paper figure,
conference-style plot, journal-inspired figure, heatmap, UMAP, schematic,
histogram, bar chart, or multi-panel scientific figure.

## Source Of Truth

- In the source repo, use `palette/scientific-figure-palettes.json`,
  `palette/notion-palette-candidates.json`,
  `palette/figure-example-registry.json`, and
  `palette/publication-figure-presets.json`.
- Inside the Codex App plugin, first read the same files under
  `../../shared/palette/`.
- Use `python scripts/palette.py` in the source repo or
  `../../shared/scripts/palette.py` inside the plugin for read-only lookup,
  recommendations, contextual discovery, snippets, presets, and examples.

## Routing Rules

- Default publication figures use `tier=core_publication` for actual plotting.
- Journal-inspired palettes are non-official style references. Do not describe
  them as publisher branding.
- Notion-derived candidates never enter canonical core. They may appear by
  default in contextual discovery when the user provides a venue, figure type,
  or domain context such as AAAI, CVPR, Nature, ICML, UMAP, histogram,
  schematic, benchmark, or Gaussian splatting. Do not require the user to know
  or name Notion.
- Contextual discovery is not application: keep safe canonical palettes,
  experimental candidates, and guidance-only examples in separate lanes.
- Unreviewed Notion transcriptions require `--allow-experimental` for snippets.
- Picker-derived, figure-sampled, or composite Notion candidates are
  inspiration-only and snippet-blocked until a future manual review changes
  their status.
- cols4all entries are GPL-3 external data; keep license/provenance visible.

## Commands

```bash
python scripts/palette.py list --tier core_publication
python scripts/palette.py recommend --figure-type heatmap --style-source core --explain
python scripts/palette.py discover --figure-type schematic --paper-venue AAAI --explain
python scripts/palette.py notion search --venue CVPR
python scripts/palette.py explain notion_aaai_1
python scripts/palette.py guidance notion_icml_clean_1 --target matplotlib
python scripts/palette.py preset get nature_biomedical_multi_panel_nonofficial
python scripts/palette.py example --figure-type histogram --style-source notion --page python_bar_distribution
python scripts/palette.py snippet notion_aaai_1 --target matplotlib --allow-experimental
```

Always report the lane, tier, review status, license or disclaimer, and the
canonical fallback when showing an experimental or guidance-only candidate.
