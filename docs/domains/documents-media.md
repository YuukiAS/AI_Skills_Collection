# documents-media

Active skills: 11

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain documents-media --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill tool/documents-media/business-presentations --skill tool/documents-media/docx --skill tool/documents-media/get-available-resources --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `business-presentations` (`skills/tools/documents-media/presentations/business-presentations`): Plan business, executive, product, operations, market, client, strategy, pitch, and decision decks. Use when the audience is non-technical or the deck asks for a decision, resource, proposal, or business update.
- `docx` (`skills/tools/documents-media/docx`): Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill.
- `get-available-resources` (`skills/tools/documents-media/get-available-resources`): This skill should be used at the start of any computationally intensive scientific task to detect and report available system resources (CPU cores, GPUs, memory, disk space).
- `markitdown` (`skills/tools/documents-media/markitdown`): Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs and more.
- `open-notebook` (`skills/tools/documents-media/open-notebook`): Self-hosted, open-source alternative to Google NotebookLM for AI-powered research and document analysis. Supports 16+ AI providers including OpenAI, Anthropic, Google, Ollama, Groq, and Mistral with complete data privacy through self-hosting.
- `parallel-web` (`skills/tools/documents-media/parallel-web`): Search the web, extract URL content, and run deep research using the Parallel Chat API and Extract API. Use for ALL web searches, research queries, and general information gathering. Provides synthesized summaries with citations.
- `pdf` (`skills/tools/documents-media/pdf`): Use this skill whenever the user wants to do anything with PDF files. If the user mentions a .pdf file or asks to produce one, use this skill.
- `perplexity-search` (`skills/tools/documents-media/perplexity-search`): Perform AI-powered web searches with real-time information using Perplexity models via LiteLLM and OpenRouter.
- `render-chinese-math-pdf` (`skills/tools/documents-media/render-chinese-math-pdf`): Render and validate Chinese or mixed Chinese/English mathematical Markdown/LaTeX as PDF. Use for CJK text, Unicode math, equations, tables, Pandoc/XeLaTeX/LuaLaTeX, TeX font/cache failures, citation cleanup, or readable PDF QA.
- `research-presentations` (`skills/tools/documents-media/presentations/research-presentations`): Plan research and technical presentations from papers, repo evidence, Markdown reports, Asteria or TRACE exports, code results, figures, and existing decks. Use for group meetings, seminars, conferences, journal clubs, defenses, and scientific project updates.
- `xlsx` (`skills/tools/documents-media/xlsx`): Use this skill any time a spreadsheet file is the primary input or output. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it.

## Main References

- `skills\tools\documents-media\render-chinese-math-pdf\references\checklists.md`
- `skills\tools\documents-media\render-chinese-math-pdf\references\citation-cleanup.md`
- `skills\tools\documents-media\render-chinese-math-pdf\references\portable-rendering.md`
- `skills\tools\documents-media\render-chinese-math-pdf\references\source-notes.md`
