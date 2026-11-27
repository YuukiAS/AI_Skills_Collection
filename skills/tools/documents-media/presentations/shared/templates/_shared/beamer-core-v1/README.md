# Shared Beamer core v1

The research_standard and RESEARCH_STANDARD templates load this 16:9 core. Both reserve an 8 mm body rail and use the same fixed fonts, page chrome and components. A skin supplies colours, the default credit and optional artwork in the shared brand slots.

| File | Owns |
|---|---|
| `core.tex` | Packages, font binding and imports |
| `typography.tex` | File-bound fonts, size, leading and weight by role |
| `geometry.tex` | 160 × 90 mm slide, 8 mm rail, title and frame title |
| `semantic-components.tex` | Lists, spacing, Q&A, captions, tables, code, columns, diagrams and closing |
| `navigation.tex` | Section labels and clickable frame markers, footer, brand slots |
| `layout-contract.yaml` | Byte copy of the frozen Planner contract |

Build through `shared/scripts/build_beamer_template.py`. The builder stages a source-editable copy with the shared core and asks the companion PDF renderer for exact font paths. It writes `beamer-font-root.tex` to the build directory. XeLaTeX runs twice to resolve the frame count, links and outlines. Build from the staged directory when editing locally so TeX can find the assets and relative imports.

Call the spacing command for the relation between adjacent objects, such as `\CoreParagraphToTable` or `\CoreCaptionToBody`. These commands supply TeX glue. Check the actual gap between rendered objects since glyph height and object depth affect it. Break a dense frame into slides before considering a layout change.

Use `\CoreEqualColumns` for peers, `\CoreEvidenceLeft` or `\CoreEvidenceRight` for evidence plus explanation, and `\CoreCaptioned{object}{caption}` to align a caption to its object. Put `\CoreTableLayout` before the tabular environment and wrap terms that must remain intact with `\CoreAtom`. Mark verbatim code frames `[fragile]` and use `lstlisting`. Connect process nodes by their boundaries with the shared TikZ styles. Set the local credit with `\slidefoot` inside its frame.

Use `\section[Short label]{Full section name}` when the navigation label needs more room. With the frame counts resolved, each label gets a warning at 90% of its budget and an error when it exceeds the cap. Use `\CoreClosing{Headline}{Takeaways}` for a recap and centred Questions cue. The canonical adapter uses 16:9. A separate geometry adapter would be needed for a validated 4:3 deck.
