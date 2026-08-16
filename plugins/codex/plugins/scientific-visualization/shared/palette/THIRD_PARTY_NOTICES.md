# Third-Party Notices for Scientific Figure Palettes

This directory contains palette data and derived metadata from several sources.
Keep these boundaries visible when recommending or generating figure code.

## cols4all

- Upstream: https://github.com/cols4all/cols4all-R
- Source commit: `6c0ca5a6026109d2fb476d2011538c65aa5f0794`
- Package version used for export: `0.10`
- License: GPL-3
- Use in this repository: `palette/external/cols4all-palettes.json` stores
  redistributed palette colors from the runtime export. Curated entries copied
  into `palette/scientific-figure-palettes.json` remain non-core and must keep
  GPL-3 provenance visible.

## ggsci Journal-Inspired Palettes

- Upstream: https://github.com/nanxstats/ggsci
- Source commit: `16660ea17f8d9b306828b8411580ea1ac1fa9109`
- Use in this repository: copied journal-inspired categorical constants.
- Boundary: these palettes are not official publisher or journal branding.
  Treat them as contextual style references and run accessibility checks before
  submission.

## Notion-Derived Palette Metadata

- Source: user-curated Notion `Skills Collection` records with `Type=Palette`.
- Source images: not redistributed in this repository.
- Stored data: derived HEX/color metadata, candidate routing, figure-example
  metadata, and review queue state.
- Boundary: Notion-derived candidates are not official CVPR, ICML, AAAI,
  Nature, journal, or publisher style guidance. All candidates remain
  unreviewed until a future manual review records otherwise.
