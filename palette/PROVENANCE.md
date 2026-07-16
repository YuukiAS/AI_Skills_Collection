# Palette Provenance

Access date for this refactor: 2026-07-16.

External repositories were cloned or downloaded into
`$env:TEMP\ai-skills-palette-sources` for source verification. These upstream
repositories are not vendored into this repo.

## Sources

| Source | Upstream | Local source status | Commit / access date | Usage |
| --- | --- | --- | --- | --- |
| ColorBrewer | https://github.com/axismaps/colorbrewer | cloned | `7d135fc4e19eda73f2eb1bf55fcdf4a04fe4881f` | Copied target GPL palette RGB values |
| Matplotlib | https://github.com/matplotlib/matplotlib | cloned | `63bd095608a65ff6f33112009797b66cadab7f06` | Sampled target colormaps from cloned source files |
| Material Color Utilities | https://github.com/material-foundation/material-color-utilities | cloned | `6fd88eb3e95ba1d457842e2a2bf847d06b3a018a` | Referenced for product/UI dynamic color boundary; no scientific palette copied |
| ggsci | https://github.com/nanxstats/ggsci | cloned | `16660ea17f8d9b306828b8411580ea1ac1fa9109` | Copied journal-inspired palette constants |
| Color Universal Design (CUD) | https://jfly.uni-koeln.de/color/ | downloaded page | 2026-07-16 | Referenced Okabe-Ito/CUD guidance |

## Copied Or Sampled Palette Ids

### ColorBrewer

- `Dark2`, `Set2`, `Paired`
- `Blues`, `YlGnBu`, `OrRd`
- `RdBu`, `BrBG`, `PuOr`

Copied from `export/gpl/*_N.gpl` files in the cloned ColorBrewer repository.
License note: see upstream `LICENCE.txt`.

### Matplotlib

- `viridis`, `plasma`, `inferno`, `magma`, `cividis`, `twilight`
- `coolwarm`

The listed colormaps were sampled from `lib/matplotlib/_cm_listed.py`.
`coolwarm` was sampled by interpolating the segmented colormap data in
`lib/matplotlib/_cm.py`. License note: see upstream Matplotlib license files;
upstream keeps additional notes for individual colormap provenance.

### Okabe-Ito / CUD

- `okabe_ito`

The palette is included as the standard Okabe-Ito color set used with Color
Universal Design guidance. The downloaded CUD page is the verified guidance
source for intended use. Use redundant encodings and test final figures in
grayscale and color vision deficiency simulations.

### Journal-Inspired Palettes

- `nature_npg`, `science_aaas`, `nejm`, `lancet`, `jama`, `bmj`, `jco`

Copied from `ggsci` `R/palettes.R`. These entries are journal-inspired helper
palettes, not official publisher branding, publisher style guides, or legal
brand specifications.

## Compatibility And Archive

- `palette/scientific-figure-palettes.json` is the canonical palette library.
- `palette/palettes.json` remains as a compatibility layer and preserves legacy
  ids.
- `palette/archive/unverified-or-deprecated.json` contains legacy non-core
  palettes that need stronger provenance before being promoted.
