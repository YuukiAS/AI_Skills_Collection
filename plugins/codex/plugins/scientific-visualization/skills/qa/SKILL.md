---
name: scientific-figure-qa
description: Audit scientific figures for publication readiness, accessibility, grayscale readability, export quality, and venue visual constraints.
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
# Scientific Figure QA

Use this skill when a user asks whether a figure is ready for a manuscript,
conference paper, journal submission, poster, rebuttal, or camera-ready
package.

## Checks

- Color accessibility: color vision deficiency, grayscale distinguishability,
  contrast on white backgrounds, and redundant marker/line encodings.
- Palette provenance: confirm canonical, journal-inspired non-official,
  external GPL, or Notion-derived experimental status.
- Typography and layout: final-size font legibility, axis labels with units,
  legend placement, panel labels, consistent spacing, and annotation clarity.
- Statistical visual integrity: uncertainty/error bars, significance markers,
  colorbar labels, centered diverging maps only for data with a real midpoint.
- Export readiness: vector output for line art, 300+ dpi raster output,
  transparent-background risks, and journal/venue file-format constraints.

## Palette QA

For palette-specific checks, use the palette CLI rather than inventing color
metadata:

```bash
python scripts/palette.py get okabe_ito --format json
python scripts/palette.py recommend --figure-type umap --paper-venue Nature --style-source all --explain
```

Do not promote Notion-derived candidates to reviewed status during QA unless a
separate manual review explicitly records the review evidence.
