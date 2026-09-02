---
schema: AI_SKILLS_PRIVATE_SOURCE_LOCATOR_V1
task_key: 048_writing_style_product_cutover_and_readable_report
implementation_commit: afa39916ff4355ad5a064c09a2f6382553f6e8a1
---

# Private Source Locator

The full private Deep Research source was located from prior local production replay state, without printing or committing plaintext.

Canonical local source used for encryption:

```text
plugin-replay/inbox/writing_style_044_source_extracted_layout.txt
```

Identity:

```text
sha256=f447de7acaae76486e42e6281f9280b482c770303a67c0861256ddba67316213
size_bytes=75936
encoding=UTF-8
```

Cross-checks:

```text
plugin-replay/20260901T074833Z-007561df1d05/inputs/02_input_writing_style_044_source_extracted_layout.txt
sha256=f447de7acaae76486e42e6281f9280b482c770303a67c0861256ddba67316213

plugin-replay/20260901T075933Z-2e88b3e0ba16/inputs/02_input_writing_style_044_source_extracted_layout.txt
sha256=f447de7acaae76486e42e6281f9280b482c770303a67c0861256ddba67316213
```

The encrypted transform manifest records the same plaintext SHA-256 and size. The temporary local `.md` copy used for MIME-compatible encryption was deleted after `input.age` and `text_transform_inputs.json` were generated.
