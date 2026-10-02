# Product UI Copy Human Acceptance PDF Render Check

Artifact:

- `PRODUCT_UI_COPY_HUMAN_ACCEPTANCE.pdf`
- `PRODUCT_UI_COPY_HUMAN_ACCEPTANCE.md`
- `assets/*.png`

Render command:

```bash
RENDER_WORKDIR=results/product-ui-copy--cross-plugin-production-integration/human_acceptance \
RENDER_MARGIN=13mm \
/home/yuukias/render_resources/chinese_math_pdf/scripts/render_markdown_pdf.sh \
  results/product-ui-copy--cross-plugin-production-integration/human_acceptance/PRODUCT_UI_COPY_HUMAN_ACCEPTANCE.md \
  results/product-ui-copy--cross-plugin-production-integration/human_acceptance/PRODUCT_UI_COPY_HUMAN_ACCEPTANCE.pdf
```

Checks performed:

- `pdfinfo`: 12 A4 pages.
- `pdffonts`: Chinese fonts are embedded and Unicode mapped.
- `pdftotext -layout`: no Markdown fences, HTML tags, or raw LaTeX commands were found in the rendered body.
- Visual page preview: pages are in the requested order; body text and screenshots are readable; no obvious truncation, overflow, or orphan Chinese character was observed.
- Workflow state was not edited; `CURRENT.json` remains `AWAIT_HUMAN_DECISION`.
