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

Checks performed:

- `pdfinfo`: 18 A4 pages.
- `pdffonts`: Chinese fonts are embedded and Unicode mapped.
- `pdftotext -layout`: no Markdown fences, HTML tags, raw LaTeX image commands,
  broken `newpage`, or workflow-state files were found in the rendered text.
- Visual preview: pages 3, 9, 10, 11, 13, 15, 16, 17, and 18 were inspected.
  Tables and screenshots are readable; the last page contains only user
  acceptance questions.
- Workflow state was not edited; `CURRENT.json` remains
  `AWAIT_HUMAN_DECISION`.
