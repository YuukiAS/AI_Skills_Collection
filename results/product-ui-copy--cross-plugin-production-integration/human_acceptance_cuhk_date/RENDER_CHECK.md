# CUHK Date Product UI Copy Acceptance PDF Render Check

Artifact:

- `CUHK_DATE_PRODUCT_UI_COPY_ACCEPTANCE.pdf`
- `CUHK_DATE_PRODUCT_UI_COPY_ACCEPTANCE.md`

Render command:

```bash
RENDER_WORKDIR=results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date \
RENDER_MARGIN=12mm \
/home/yuukias/render_resources/chinese_math_pdf/scripts/render_markdown_pdf.sh \
  results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/CUHK_DATE_PRODUCT_UI_COPY_ACCEPTANCE.md \
  results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/CUHK_DATE_PRODUCT_UI_COPY_ACCEPTANCE.pdf
```

Checks performed after adding the historical-audit comparison:

- `pdfinfo`: 18 A4 pages.
- `pdffonts`: Chinese fonts are embedded and Unicode mapped.
- `pdftotext -layout`: no Markdown fences, HTML tags, raw LaTeX image commands,
  broken `newpage`, `CURRENT.json`, `H3`, or `H4` strings were found in the
  rendered text.
- Rendered comparison page 17 contains the expected second-stage figures:
  `118 条仍可见`, `64 / 78`, `10 / 10`, and zero obvious wrong rewrites or
  material misses.
- Visual preview: pages 12, 17, and 18 were inspected after re-render. The
  screenshot page remains readable, the historical comparison table does not
  overflow, and the last page contains only user acceptance questions.
- Workflow state was not edited; `CURRENT.json` remains
  `AWAIT_HUMAN_DECISION`.
