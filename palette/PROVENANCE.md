# Palette Provenance

Access date for this refactor: 2026-07-16 and 2026-07-17.

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
| cols4all | https://github.com/cols4all/cols4all-R | cloned + CRAN package installed into temp R library | `6c0ca5a6026109d2fb476d2011538c65aa5f0794` / 2026-07-17 | Exported 689 GPL-3 palettes, curated non-core scientific candidates, and computed `c4a_scores` for canonical palettes |
| Notion Skills Collection palette pages | Notion `Skills Collection` database, `Type=Palette` rows | local latest images in `C:\Users\yuukias\Downloads` | 2026-07-17 | Extracted reviewable image-derived palette candidates and figure-example routing; not promoted to core |

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

### cols4all

- Complete exported library: `palette/external/cols4all-palettes.json`
- Schema: `palette/external/cols4all-palettes.schema.json`
- Canonical non-core curated ids:
  - `cols4all_area7`, `cols4all_area8`, `cols4all_area9`
  - `cols4all_line7`, `cols4all_line8`, `cols4all_line9`
  - `cols4all_friendly5`, `cols4all_friendly7`, `cols4all_friendly9`, `cols4all_friendly11`, `cols4all_friendly13`
  - `tol_bright`, `carto_safe`, `scico_batlow`, `hcl_purple_green`

License note: these color values were exported from the GPL-3 `cols4all`
package. They are deliberately marked as external/non-core and must keep GPL-3
license and provenance metadata visible in redistributed plugin payloads.

### Notion Image-Derived Palettes And Figure Examples

- `CVPR25优质绘图学配色`: 1 latest image, visible bottom HEX labels; experimental palette plus 3D point cloud / Gaussian splatting example.
- `AAAI跟着顶会学配色`: 3 latest images, visible RGB/HEX labels; parse labels where possible and keep picker output for verification; use for AI schematics, codec pipelines, benchmark panels, histogram/box/scatter examples.
- `攒了九组顶刊审稿人都挑不出毛病的配色`: 9 latest images, visible HEX cards; experimental journal-aesthetic palettes for small multiples, line and bar examples.
- `ICML的清爽绘图风格！学了就能Accept‼️`: 3 latest images, no reliable visible HEX; treat primarily as figure examples for clean schematic, line chart, attention heatmap, and model comparison.
- `Nature顶刊配色灵感🌷`: 8 latest images, mixed visible HEX and figure colors; use for UMAP/single-cell, line/scatter and biomedical multi-panel examples after manual review.
- `顶刊配色直接抄！Nature同款色板也太绝了`: 8 latest images, visible palette cards; non-official Nature-inspired experimental palettes for UMAP, activation heatmap, ridge plot and histogram examples.
- `Python绘制高颜值柱状图展示数据分布`: 18 latest images, no visible HEX; use mainly as bar/histogram/distribution figure examples with picker-derived four-level palette candidates.
- `Palettes and Typical Figures (Old)`: no latest local image import; only `cols4all` is fused from this old-page direction, and typical figures are recorded as example routing rather than palette core data.

## Compatibility And Archive

- `palette/scientific-figure-palettes.json` is the canonical palette library.
- `palette/palettes.json` remains as a compatibility layer and preserves legacy
  ids.
- `palette/archive/unverified-or-deprecated.json` contains legacy non-core
  palettes that need stronger provenance before being promoted.
