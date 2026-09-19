# render-chinese-math-pdf — Long-Term TODO

Maintenance inbox for the standalone `render-chinese-math-pdf` skill.

This skill is not one of the central Marketplace plugins, so its real-use failures should not be forced into an unrelated plugin TODO. This file stays under `docs/` so maintenance history is not shipped as ordinary skill runtime payload. For new real-project feedback, follow the same evidence-first `status: NEW` discipline described in `docs/plugin-todos/README.md`: record the failure and current evidence first; do not pre-decide the implementation architecture or release.

## Open candidates

### Nominal skill invocation can still bypass the declared Pandoc + XeLaTeX production route
status: NEW
source: real mixed Chinese/English mathematical group-meeting report render, 2026-09-19
evidence: private user-provided first and second PDF renders from the same Markdown report (not copied into this public repository); `pdfinfo` identifies both artifacts as HeadlessChrome / Skia PDFs. Current source contract: `skills/tools/documents-media/render-chinese-math-pdf/SKILL.md`.
problem:
- The user explicitly had Codex invoke `render-chinese-math-pdf`, but the delivered artifacts were still produced by HeadlessChrome/Skia rather than the skill’s declared default `Markdown -> Pandoc -> XeLaTeX -> PDF` route.
- The first delivered PDF materially corrupted mathematical notation: equations degraded into incomplete bracket/plain-text fragments and lost operators/symbol structure. Correct mathematical rendering appeared only after the user manually called out the problem and requested another render.
- This is therefore not primarily a missing “remember to use LaTeX” instruction. The active skill already says the default renderer is strictly Pandoc + XeLaTeX, says not to silently switch to Chromium, and says the task is incomplete if formulas fail. The real failure is that nominal invocation did not guarantee actual production-path consumption or contract enforcement.
- A successful PDF file/command is not sufficient evidence that the skill ran correctly. The final artifact identity must match the declared route when that route is required.
project-specific context: the underlying biomedical/statistical formulas and report topic are project-local/private. The reusable failure is route identity + mathematical fidelity, not the scientific content.

### Current PDF validator can miss mathematical corruption and non-canonical font output
status: NEW
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
status: NEW
source: same real report, first vs second render
evidence: first PDF is A4 and 17 pages; second PDF is US Letter and 24 pages, despite representing the same report family. Both identify HeadlessChrome/Skia as producer.
problem:
- Retry/repair of math changed page geometry and pagination at the same time. The user did not ask to change the paper format.
- This makes it hard to distinguish “formula repair” from unrelated visual/layout drift and contributes to the perception that the final report is not a controlled formal artifact.
- The exact higher-level visual profile belongs to later ownership triage with Research Authoring/artifact rendering; this skill-level record is limited to preserving a stable render identity and not silently changing basic page geometry during a repair.
project-specific context: whether a future formal report profile should use A4, Letter, particular margins or particular type sizes is not decided here.
