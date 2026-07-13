---
name: chinese-prose
description: Chinese technical and scientific prose polishing with CJK/math rendering support.
status: active
provenance: generated
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/writing/core/chinese-prose
  - skills/tools/documents-media/render-chinese-math-pdf
default_prompt:
---

# chinese-prose

## Trigger Boundary

Chinese technical and scientific prose polishing with CJK/math rendering support.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `chinese-prose`: 中文报告、README、技术文档和科研说明的最终审校。用于降低 AI 味、翻译腔、模板腔、宣传腔和不必要英文，同时保护事实、数字、术语、命令、引用、实验结果、机器精确字段和中文读者的阅读习惯。 Reference: `_src/prose/source.md`
- `render-chinese-math-pdf`: Render and validate Chinese or mixed Chinese/English mathematical Markdown/LaTeX as PDF. Use for CJK text, Unicode math, equations, tables, Pandoc/XeLaTeX/LuaLaTeX, TeX font/cache failures, citation cleanup, or readable PDF QA. Reference: `_src/pdf/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
