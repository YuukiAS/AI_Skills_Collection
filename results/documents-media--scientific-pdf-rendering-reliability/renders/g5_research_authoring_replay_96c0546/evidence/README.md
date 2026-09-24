# Render and validation evidence

The delivered report is `../advisor_report.pdf`, rendered directly from
`../advisor_report.md` with Pandoc and XeLaTeX. It has two A4 pages, 11 pt
body text, 25 mm margins and 1.15 line spacing, using the canonical formal-note
profile. TeX Gyre Termes and TeX Gyre Termes Math are embedded.

Reproduction command (run from the project root):

```sh
python .agents/skills/tools-documents-media-render-chinese-math-pdf/scripts/render_scientific_pdf.py outputs/advisor_report.md outputs/advisor_report.pdf --root . --work-dir outputs/evidence/build --preview-dir outputs/evidence/previews --preview-pages all --receipt outputs/evidence/render_receipt.json
```

No additional environment overrides were set. Resource resolution, tool versions,
exact commands, profile identity, font checks and generated-TeX math checks are
recorded in `render_receipt.json`. `validation.json` binds the final files to
SHA-256 hashes and records fidelity and visual checks. `extracted_text.txt`
retains the text layer; `previews/` contains the two inspected pages.

The scientific headings, all three display equations, table values, and the
original Interpretation paragraphs are preserved. The opening is adapted for
an advisor; added explanation describes the supplied objectives, delta sign,
and limits of the mean without adding experimental results. Formatting instructions
and pagination filler are preserved separately in `source_formatting_requirements.md`
rather than presented as scientific narrative.

The final build has non-fatal package hook and math-package compatibility
warnings, recorded in the receipt/log. Visual inspection found no affected
notation or layout. No missing glyph or overfull-box error was observed.
