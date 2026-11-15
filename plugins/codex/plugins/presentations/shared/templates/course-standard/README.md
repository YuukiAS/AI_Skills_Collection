# Course-standard Beamer

Use this template for teaching in Beamer or when your project selects course-standard. Start with [main.tex](beamer/source/main.tex), an editable example with a title slide, a teaching slide and a recap. The [reference PDF](reference.pdf) shows the full set of common components. Both decks use the [shared 16:9 core](../_shared/beamer-core-v1/README.md).

From the Presentations plugin directory, build the example:

```sh
python shared/scripts/build_beamer_template.py --skin course-standard --out-dir course-deck
```

Open `course-deck/main.pdf` and edit `course-deck/main.tex` for your own content. The output directory contains the same skin and core plus a receipt listing the resolved font files and embedded PDF fonts. To build an edited copy into a fresh directory, use `--source-dir` with the editable source directory. Keep images and other inputs alongside that source.

The blue palette and default credit are in [skin.tex](beamer/source/skin.tex). Keep geometry and typography in the core. See the [font policy](../../font-policy.md) for the required XeLaTeX resources.
