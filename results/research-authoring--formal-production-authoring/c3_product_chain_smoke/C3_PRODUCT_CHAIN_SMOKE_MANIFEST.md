# C3 product-chain development smoke manifest

Date: 2026-10-07
Task: `research-authoring--formal-production-authoring`

```text
C3_PROVISIONAL_PRODUCT_COMMIT=9e88d7eda1749c09bac0ed97562909a90810ccdb
FINAL_GATES_STARTED=NO
RAW_CODEX_AUTHORING_OWNER_COMPETITION=NOT_RUN
```

## A. Codex production handoff consumer

Input was already-stabilized Research Authoring source plus complete Codex production handoff:

- `codex_handoff_consumer/project/stable_source.md`
- `codex_handoff_consumer/project/production_handoff.md`
- `codex_handoff_consumer/project/smoke_prompt.md`

Evidence:

- Profile install: `codex_handoff_consumer/install.json`
- Child trace: `codex_handoff_consumer/codex_handoff_trace.jsonl`
- Final child response: `codex_handoff_consumer/codex_handoff_last.txt`
- Produced source: `codex_handoff_consumer/project/outputs/advisor_update.md`
- Produced PDF: `codex_handoff_consumer/project/outputs/advisor_update.pdf`
- Post-render scientific QA: `codex_handoff_consumer/project/outputs/post_render_scientific_qa.md`

Result:

```text
CODEX_HANDOFF_CONSUMER_SMOKE=PASS
SOURCE_HANDOFF_READ=YES
PDF_PRODUCED_FROM_HANDOFF=YES
POST_RENDER_SCIENTIFIC_QA=PASS
SCIENTIFIC_MEANING_PRESERVED=YES
```

## B. finalized Markdown render-only

Evidence:

- Source: `render_only_markdown/finalized_note.md`
- PDF: `render_only_markdown/outputs/finalized_note.pdf`
- QA: `render_only_markdown/outputs/pdfinfo.txt`, `render_only_markdown/outputs/text.txt`
- Hashes: `render_only_markdown/outputs/sha256.txt`

Result:

```text
FINALIZED_MARKDOWN_RENDER_ONLY=PASS
```

## C. existing LaTeX compile/debug

Evidence:

- Source: `existing_latex_compile_debug/existing_note.tex`
- PDF: `existing_latex_compile_debug/outputs/existing_note.pdf`
- Compile log and QA: `existing_latex_compile_debug/outputs/pdflatex.log`, `pdfinfo.txt`, `text.txt`
- Hashes: `existing_latex_compile_debug/outputs/sha256.txt`

Result:

```text
EXISTING_LATEX_COMPILE_DEBUG=PASS
```

## D. existing PDF operations

Evidence:

- Input PDF: `existing_pdf_operations/existing_advisor_update.pdf`
- Operations: `pdfinfo`, `pdftotext`, text assertions
- QA files: `existing_pdf_operations/outputs/pdfinfo.txt`, `text.txt`, `text_assertions.txt`
- Hashes: `existing_pdf_operations/outputs/sha256.txt`

Result:

```text
EXISTING_PDF_OPERATIONS=PASS
```

## Summary

```text
PRODUCTION_HELPER_REGRESSION=PASS
FINAL_GATES_NOT_STARTED=YES
```
