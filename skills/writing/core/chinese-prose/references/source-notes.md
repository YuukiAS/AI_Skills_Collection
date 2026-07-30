# Source Notes

This skill is a local synthesis. It does not vendor upstream repositories directly.

Sources inspected locally:

- `MrGeDiao/shuorenhua`, commit `1cd6145`, MIT license. Used for protected spans, scene-based rewrite scope, residual AI-taste audit, and Chinese-first naturalization rules.
- `op7418/Humanizer-zh`, commit `91f3d39`, MIT license. Used for common AI writing traces such as vague significance claims, promotional language, fuzzy attribution, forced triads, filler phrases, and generic positive conclusions.
- `ruanyf/document-style-guide`, commit `5719517`, public domain. Used for Chinese technical documentation conventions around titles, paragraphs, numbers, punctuation, document structure, and references.
- `vale-cli/vale`, commit `5242b459`, MIT license. Used only as a conceptual reference for programmable prose linting; this skill has no Vale runtime dependency.
- `chen3feng/cn-doc-style-guide`, commit `6da4697b964ac8d45d99b230e5400ab74087c7bd`, CC0-1.0. Used for README first-screen expectations, document status, ownership/contact, and minimum useful documentation checks.
- `LifelongLazyLearner/qu-ai-wei`, commit `1600d3fcb5ec9f4db8835f48681b50e3e7f56fff`, MIT license. Used for style-register first routing, over-correction protection, and simplified Chinese AI-taste cleanup concepts; local rules are rewritten for technical/research outputs.
- `zLanqing/codex-claude-academic-skills`, commit `7ed6377f0efb6a38951b48ef03b19d996e454b1f`, MIT license. Used for Chinese research-writing evidence boundaries, protected English technical objects, and measured-claim discipline.
- `zhlint-project/zhlint`, commit `c8678fe71ce3bcafe38ac168d11e9a0c6a2cfa0d`, MIT license; `huacnlee/autocorrect`, commit `e1a75da3faa9b1f005db97b77f47eb67abe1395e`, MIT license; `lint-md/lint-md`, commit `148a9a5de09725954ca00175a5e1b9e7f6ecc524`, MIT license; `Jackychen-12/zh-quality`, commit `8e7332fc621e7bfd2385cd095499559327450156`, MIT license. Used as reference sources for Markdown/PDF final-pass lint categories, CJK/English spacing, punctuation, protected-token exceptions, and machine-text artifact checks; no runtime dependency is vendored.

If upstream guidance conflicts with fact preservation, fact preservation wins.
