# CUHK Beamer

[beamer/source](beamer/source/) is the canonical CUHK Beamer template and is used only when the user or repository explicitly requests CUHK. It uses the [shared 16:9 core](../_shared/beamer-core-v1/README.md) for fonts, role sizes, leading, margins, layout grid, caption alignment, list spacing and formula sizing. [skin.tex](beamer/source/skin.tex) keeps the original CUHK purple palette, title bar, school logo and school footer credit. The four original PNG assets remain in [assets](beamer/source/assets/), including both negative variants.

From the Presentations plugin directory:

```sh
python shared/scripts/build_beamer_template.py --skin cuhk --out-dir cuhk-deck
```

The build directory contains editable `main.tex`, the assets, the shared core, `main.pdf`, and the build receipt. For a research bundle, use `shared/scripts/generate_research_presentation_production_entry.py`. Both commands use the [fixed font policy](../../font-policy.md) and record the fonts embedded in the PDF.

Existing decks that use `\usetheme{sintef}` and keep the CUHK source tree can still use that import. The historical [beamer/main.tex](beamer/main.tex) forwards to the canonical source. The old `\titlebackground` and `\titlebackground*` calls select the image for the shared title slot. Use `\slidefoot` for a source credit or `\CoreClosing` for a substantive recap. The legacy `\backmatter`, author metadata and color block names remain available. Older full-slide background layouts need to be laid out with the shared components.

The editable PPTX reference and its design-token JSON are separate scaffolds. They are based on the supplied CUHK template subset and do not control Beamer geometry. See [the template freeze](../FREEZE.md) for the versioned appearance and style-alignment boundary.
