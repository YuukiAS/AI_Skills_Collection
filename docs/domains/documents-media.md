# documents-media

Active skills: 9

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain documents-media --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill tool/documents-media/docx --skill tool/documents-media/get-available-resources --skill tool/documents-media/markitdown --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `docx` (`skills/tools/documents-media/docx`): Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill.
- `get-available-resources` (`skills/tools/documents-media/get-available-resources`): This skill should be used at the start of any computationally intensive scientific task to detect and report available system resources (CPU cores, GPUs, memory, disk space).
- `markitdown` (`skills/tools/documents-media/markitdown`): Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs and more.
- `open-notebook` (`skills/tools/documents-media/open-notebook`): Self-hosted, open-source alternative to Google NotebookLM for AI-powered research and document analysis. Supports 16+ AI providers including OpenAI, Anthropic, Google, Ollama, Groq, and Mistral with complete data privacy through self-hosting.
- `parallel-web` (`skills/tools/documents-media/parallel-web`): Search the web, extract URL content, and run deep research using the Parallel Chat API and Extract API. Use for ALL web searches, research queries, and general information gathering. Provides synthesized summaries with citations.
- `pdf` (`skills/tools/documents-media/pdf`): Use this skill whenever the user wants to do anything with PDF files. If the user mentions a .pdf file or asks to produce one, use this skill.
- `perplexity-search` (`skills/tools/documents-media/perplexity-search`): Perform AI-powered web searches with real-time information using Perplexity models via LiteLLM and OpenRouter.
- `pptx` (`skills/tools/documents-media/pptx`): Use this skill any time a .pptx file is involved in any way — as input, output, or both. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward.
- `xlsx` (`skills/tools/documents-media/xlsx`): Use this skill any time a spreadsheet file is the primary input or output. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
