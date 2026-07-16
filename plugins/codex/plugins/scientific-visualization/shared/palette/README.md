# Scientific Figure Palettes

`palette/` is the repo-local palette library for academic papers, scientific
plots, publication-ready figures, supplementary figures, and research posters.
It is not a presentation theme system and not a product UI token system.

## Canonical File

Use `palette/scientific-figure-palettes.json` for new scientific figure work.
It contains palette metadata, provenance, routing hints, accessibility notes,
and legacy aliases.

```text
Use the palette from palette/scientific-figure-palettes.json: okabe_ito
Use the palette from palette/scientific-figure-palettes.json: viridis
Use the palette from palette/scientific-figure-palettes.json: RdBu
```

`palette/palettes.json` is preserved as a compatibility layer for old prompts
and old ids. Do not add new canonical scientific palettes there first.

## External And Image-Derived Sources

- `palette/external/cols4all-palettes.json` contains a full runtime export of
  689 palettes from the GPL-3 R `cols4all` package. Use it as an external
  exploration library and keep GPL-3 provenance visible.
- Curated `cols4all` candidates such as `cols4all_line7`,
  `cols4all_area7`, `cols4all_friendly9`, `tol_bright`, `carto_safe`,
  `scico_batlow`, and `hcl_purple_green` are included in the canonical file as
  non-core `external_curated` palettes.
- `palette/cols4all-evaluation.json` records `cols4all` scoring for canonical
  palettes.
- `palette/notion-image-palettes.json` records the latest local Notion
  `Type=Palette` image pages, picker-derived colors, visible HEX/RGB status,
  and figure-example routing. These are experimental review candidates, not
  core palettes.

## Scope

- Use scientific palettes for plots, panels, heatmaps, line charts, maps, and
  publication figures.
- Use presentation themes for research and business decks.
- Use semantic design tokens for product/frontend UI.

See `palette/ROUTING.md` for the full boundary.

## Provenance

Every canonical palette includes `origins`, `provenance_status`, and
`stability`. See `palette/PROVENANCE.md` for upstream repositories, clone
commits, access dates, license notes, and copied palette ids.

Journal-inspired palettes such as `nature_npg`, `science_aaas`, `lancet`,
`jama`, `bmj`, `jco`, and `nejm` are not official journal or publisher brand
specifications. Treat them as visual inspiration only and verify accessibility
before manuscript submission.

## Validation

Run:

```bash
python -m json.tool palette/scientific-figure-palettes.json
python -m json.tool palette/external/cols4all-palettes.json
python -m json.tool palette/cols4all-evaluation.json
python -m json.tool palette/notion-image-palettes.json
python -m json.tool palette/publication-figure-presets.json
python -m json.tool palette/palettes.json
python scripts/validate_palette_library.py
```

The validator checks required metadata, core palette coverage, legacy alias
conflicts, source records, and non-official journal-inspired disclaimers.

## Tools

Use the read-only CLI for palette lookup and code snippets:

```bash
python scripts/palette.py list
python scripts/palette.py list --source cols4all
python scripts/palette.py list --source notion
python scripts/palette.py recommend --purpose heatmap
python scripts/palette.py recommend --figure-type heatmap --source all
python scripts/palette.py snippet okabe_ito --target matplotlib
python scripts/palette.py snippet cols4all_line7 --source all --target matplotlib
python scripts/palette.py snippet RdBu --target latex
```

Use `palette/publication-figure-presets.json` for common top-conference,
heatmap, centered diverging, clinical, and journal-inspired non-official figure
defaults.

Generate a local preview gallery with:

```bash
python scripts/generate_palette_gallery.py
```
