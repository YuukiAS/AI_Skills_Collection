# render-chinese-math-pdf — Long-Term TODO

Maintenance inbox for the standalone `render-chinese-math-pdf` skill.

This skill is not one of the central Marketplace plugins, so its real-use failures should not be forced into an unrelated plugin TODO. This file stays under `docs/` so maintenance history is not shipped as ordinary skill runtime payload. For new real-project feedback, follow the same evidence-first `status: NEW` discipline described in `docs/plugin-todos/README.md`: record the failure and current evidence first; do not pre-decide the implementation architecture or release.

## Open candidates

### 2026-09-22 release closure note
status: PROMOTED_IN_5.2.1
source: `documents-media--scientific-pdf-rendering-reliability`
evidence: `skills/tools/documents-media/render-chinese-math-pdf/scripts/render_scientific_pdf.py`; `profiles/canonical_formal_note.json`; `tests/test_render_chinese_math_pdf.py`; release evidence under `results/documents-media--scientific-pdf-rendering-reliability/`
problem closed: the first three route/math/font/profile-stability failures below are promoted into the canonical renderer orchestration and QA contract. Chromium remains diagnostic-only, canonical Markdown uses Pandoc AST -> LaTeX -> XeLaTeX, ordered Math payload signatures and generated-TeX anchors are checked, canonical font fallback is rejected for the formal-note route, and resolved profile identity is recorded.
remaining boundary: complete artifact typography still requires actual page/montage review on each final candidate; project/venue templates keep their own typography and are not forced into the canonical formal-note font allowlist.

### Nominal skill invocation can still bypass the declared Pandoc + XeLaTeX production route
status: PROMOTED_IN_5.2.1
tracking: #80
source: real mixed Chinese/English mathematical group-meeting report render, 2026-09-19
evidence: private user-provided first and second PDF renders from the same Markdown report (not copied into this public repository); `pdfinfo` identifies both artifacts as HeadlessChrome / Skia PDFs. Current source contract: `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`.
problem:
- The user explicitly had Codex invoke `render-chinese-math-pdf`, but the delivered artifacts were still produced by HeadlessChrome/Skia rather than the skill’s declared default `Markdown -> Pandoc -> XeLaTeX -> PDF` route.
- The first delivered PDF materially corrupted mathematical notation: equations degraded into incomplete bracket/plain-text fragments and lost operators/symbol structure. Correct mathematical rendering appeared only after the user manually called out the problem and requested another render.
- This is therefore not primarily a missing “remember to use LaTeX” instruction. The active skill already says the default renderer is strictly Pandoc + XeLaTeX, says not to silently switch to Chromium, and says the task is incomplete if formulas fail. The real failure is that nominal invocation did not guarantee actual production-path consumption or contract enforcement.
- A successful PDF file/command is not sufficient evidence that the skill ran correctly. The final artifact identity must match the declared route when that route is required.
project-specific context: the underlying biomedical/statistical formulas and report topic are project-local/private. The reusable failure is route identity + mathematical fidelity, not the scientific content.

### Current PDF validator can miss mathematical corruption and non-canonical font output
status: PROMOTED_IN_5.2.1
tracking: #81
source: same 2026-09-19 real render; current `validate_pdf_layout.py` and `SKILL.md`
evidence: first render visibly lost equation structure; second render became readable only after explicit user intervention. `pdffonts` on the supplied artifacts reports Liberation Serif, Droid Sans Japanese/Fallback and, in the second render, FreeSerif and DejaVu Sans. Current source inspection shows `validate_pdf_layout.py` checks page count, embedded fonts, CJK extraction/fragmentation, table survival and a first-page preview, but does not compare source math against rendered math.
problem:
- The declared font policy requires bundle-local TeX Gyre Termes / TeX Gyre Termes Math plus Noto Serif/Sans SC and explicitly says Liberation/DejaVu/Fandol should not be default sources. The real artifact nevertheless used non-canonical fonts without being blocked before delivery.
- The validator currently treats names such as `DroidSansFallback` as recognizable CJK fonts and mainly checks ToUnicode compatibility; it does not enforce the declared canonical font family.
- Source-to-PDF mathematical fidelity is not directly validated. `pdftotext -layout` can prove that some text exists while still missing whether hats, subscripts, superscripts, sums, gradients, Greek letters, delimiters or operators survived with the intended mathematical structure.
- The automated preview is currently first-page oriented. A long report can therefore have equation-heavy failures on later pages while the first page looks acceptable.
- This is an existing-contract regression/gap rather than evidence that more prose rules should simply be added to `SKILL.md`.
project-specific context: exact equations, page text and unpublished research content are intentionally omitted. The generic evidence is the mismatch between declared render/font/QA policy and the real output.

### Rendering defaults can drift across retries even when the document purpose did not change
status: PROMOTED_IN_5.2.1
tracking: #82
source: same real report, first vs second render
evidence: first PDF is A4 and 17 pages; second PDF is US Letter and 24 pages, despite representing the same report family. Both identify HeadlessChrome/Skia as producer.
problem:
- Retry/repair of math changed page geometry and pagination at the same time. The user did not ask to change the paper format.
- This makes it hard to distinguish “formula repair” from unrelated visual/layout drift and contributes to the perception that the final report is not a controlled formal artifact.
- The exact higher-level visual profile belongs to later ownership triage with Research Authoring/artifact rendering; this skill-level record is limited to preserving a stable render identity and not silently changing basic page geometry during a repair.
project-specific context: whether a future formal report profile should use A4, Letter, particular margins or particular type sizes is not decided here.

### Technically correct XeLaTeX output can still be visually inconsistent because the template invents typography by block class
status: PARTIALLY_PROMOTED_IN_5.2.1
tracking: #83
source: Clear Writing 055 / real Original-only acceptance PDF render, 2026-09-20
evidence: private user-provided Clear Writing 055 Case 1 PDF and the producing Codex thread (private material not copied into this public repository). Direct artifact inspection confirms an 8-page A4 PDF produced by XeTeX/xdvipdfmx with embedded TeX Gyre Termes, Noto Serif SC and TeX Gyre Termes Math. The producing thread reports a custom template that assigns `\\LARGE\\bfseries` to the title, `\\small` to explanatory lines, default 10pt to ordinary paragraphs, `\\footnotesize` to blocks classified as `tableline`, and `\\section*` to subheadings.
problem:
- This is a different failure from the earlier Chromium-route/math-corruption case. Here the declared XeLaTeX route and canonical font families were actually used and the mathematical content rendered, yet the final document still looked visibly inconsistent.
- The renderer/template introduced multiple font sizes and hierarchy treatments that were not requested by the user. In particular, text classified as `tableline` was automatically reduced to `\\footnotesize`, so source extraction/line-shape heuristics directly changed reader-facing typography.
- Some source blocks were only semi-tabular or line-wrapped text from an earlier comparison/extraction artifact. Misclassifying them as table-like content avoided overflow but silently shrank large amounts of prose. This traded clipping risk for a new visual-consistency failure instead of preserving the document's semantic role.
- Cross-script font pairing is technically expected to use separate Latin, CJK and math fonts, so “one literal font file for everything” is not the requirement. The missing capability is visual coherence across those families: comparable apparent size, weight, baseline/rhythm and paragraph texture in mixed Chinese/English/math prose.
- Current validation is biased toward technical survival (embedded fonts, extractable text, glyphs, tables and preview existence). It does not establish that body text remains visually uniform, that a heuristic block classifier did not arbitrarily shrink prose, or that the final artifact has a coherent typographic scale.
- A rendering skill should not treat “no overflow” as sufficient if the repair is achieved by silently switching ordinary content into smaller typography. When source structure is ambiguous, preservation of readable body-text identity matters more than aggressive auto-classification.
- The real failure therefore sits at the boundary between source-structure interpretation and renderer-level typography QA: a technically successful PDF can still be unacceptable because the renderer invents presentation semantics that were never present in the source.
project-specific context: the underlying Clear Writing case content and scientific subject matter are private/project-local. The reusable evidence is the unintended size hierarchy, block misclassification, cross-script visual mismatch and the gap between technical render success and coherent typography. This record does not prescribe the future implementation or a single mandatory font/size scheme; those decisions belong to the upcoming Planner/Critic refinement round.

2026-09-25 update: repository `5.2.1` removes the line-shape/tableline typography route from the canonical renderer path by using Pandoc semantic nodes and a declarative formal-note profile with no ordinary-prose downscaling. The broader qualitative typography responsibility remains active through G3-style complete-artifact review, not a one-time mechanical font check.
