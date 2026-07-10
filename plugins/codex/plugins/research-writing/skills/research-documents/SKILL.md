---
name: research-documents
description: Work with research PDFs, Word documents, slides, Markdown conversion, figures, and schematics.
status: active
provenance: generated
trusted: false
requires_network: true
writes_files: true
executes_code: true
secrets_needed:
  - OPENROUTER_API_KEY
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/tools/documents-media/pdf
  - skills/tools/documents-media/docx
  - skills/tools/documents-media/pptx
  - skills/tools/documents-media/markitdown
  - skills/science/communication/scientific-slides
  - skills/science/communication/scientific-schematics
---

# research-documents

## Trigger Boundary

Work with research PDFs, Word documents, slides, Markdown conversion, figures, and schematics.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `pdf`: Use this skill whenever the user wants to do anything with PDF files. If the user mentions a .pdf file or asks to produce one, use this skill. Reference: `references/source-skills/tools-documents-media-pdf/source-skill.md`
- `docx`: Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Reference: `references/source-skills/tools-documents-media-docx/source-skill.md`
- `pptx`: Use this skill any time a .pptx file is involved in any way — as input, output, or both. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. Reference: `references/source-skills/tools-documents-media-pptx/source-skill.md`
- `markitdown`: Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs and more. Reference: `references/source-skills/tools-documents-media-markitdown/source-skill.md`
- `scientific-slides`: Build slide decks and presentations for research talks. Use this for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design templates, timing guidance, and visual validation. Works with PowerPoint and LaTeX Beamer. Reference: `references/source-skills/science-communication-scientific-slides/source-skill.md`
- `scientific-schematics`: Create publication-quality scientific diagrams using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.1 Pro Preview for quality review. Reference: `references/source-skills/science-communication-scientific-schematics/source-skill.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source-skill.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
