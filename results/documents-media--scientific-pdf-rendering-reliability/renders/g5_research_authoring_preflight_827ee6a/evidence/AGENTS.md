# AGENTS.md

<!-- AI_SKILLS_COLLECTION_START -->
# AI Skills Collection

Installed: `2026-09-24T12:54:01+00:00`
Target: `repo`
Install mode: `profile:research-main`
Project skills: `.agents/skills/`
Central collection: `/tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability`

When a task matches an installed skill, read that skill's `SKILL.md` before acting. Keep progressive disclosure: load `references/` only when the skill says they are relevant.

## Profile Routing Notes

- For advisor-facing, group-meeting, milestone, experiment-review, or repo-grounded research-report requests that also ask for a formal/readable PDF, first read and apply `research-reporting` for the scientific report semantics, then use `render-chinese-math-pdf` only for PDF route/profile/font/layout mechanics. Do not satisfy such requests by using only PDF/rendering skills.

## Skill Routing

### core
- `codex-workflow-protocol`: Use for complex or risky Codex tasks that require source-of-truth discovery, phased planning, specialist routing, gate-driven verification, live-state supervision, integration ownership, or honest final status reporting. Path: `.agents/skills/core-codex-system-codex-workflow-protocol/SKILL.md`

### documents-media
- `docx`: Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file,... Path: `.agents/skills/tools-documents-media-docx/SKILL.md`
- `markitdown`: Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs and more. Path: `.agents/skills/tools-documents-media-markitdown/SKILL.md`
- `pdf`: Use this skill whenever the user wants to do anything with PDF files. If the user mentions a .pdf file or asks to produce one, use this skill. Path: `.agents/skills/tools-documents-media-pdf/SKILL.md`
- `render-chinese-math-pdf`: Render and validate Chinese or mixed Chinese/English mathematical Markdown/LaTeX as PDF. Use for CJK text, Unicode math, equations, tables, Pandoc/XeLaTeX, TeX font/cache failures, citation cleanup, or readable PDF QA. Path: `.agents/skills/tools-documents-media-render-chinese-math-pdf/SKILL.md`

### research-discovery
- `citation-management`: Manage bibliography, BibTeX, citation metadata, and reference-library hygiene. Use for DOI/PMID/arXiv-to-BibTeX conversion, metadata extraction, duplicate repair, and style formatting. Route claim support to citation-... Path: `.agents/skills/science-discovery-citation-management/SKILL.md`
- `research-lookup`: Find current research information and recent papers quickly. Use for latest papers, targeted evidence gathering, methods/protocol checks, and source-backed facts. Route systematic or related-work synthesis to literatu... Path: `.agents/skills/science-discovery-research-lookup/SKILL.md`

### research-writing
- `citation-verification`: Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or cl... Path: `.agents/skills/writing-research-citation-verification/SKILL.md`
- `latex-paper-authoring`: Author, organize, repair, and prepare LaTeX research papers for arXiv, Overleaf, conference templates, or journal submission. Use when manuscript structure, LaTeX source hygiene, compilation, figures, bibliography, or... Path: `.agents/skills/writing-research-latex-paper-authoring/SKILL.md`
- `literature-review`: Synthesize scholarly literature and create single-paper evidence cards. Use for systematic/scoping/narrative reviews, related work, paper精读, paper cards, claim-evidence extraction, method maps, thematic synthesis, and... Path: `.agents/skills/writing-research-literature-review/SKILL.md`
- `nature-manuscript-workflow`: Plan, draft, revise, and audit broad-journal or high-impact manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use for story-driven journal strategy, br... Path: `.agents/skills/writing-research-nature-manuscript-workflow/SKILL.md`
- `paper-workflow-orchestrator`: Orchestrate research paper workflows: manuscript plan, claim-evidence spine, result-to-claim gate, section contracts, figure/text sync, pre-submission acceptance checks, rebuttal planning, final artifact QA, and paper... Path: `.agents/skills/writing-research-paper-workflow-orchestrator/SKILL.md`
- `research-reporting`: Create repo-grounded research reports, milestone summaries, experiment reviews, technical notes, advisor/group-meeting reports, and result retrospectives from project evidence. Use for report semantics even when the f... Path: `.agents/skills/writing-research-research-reporting/SKILL.md`
- `scientific-writing`: Draft and revise scientific manuscript prose: abstracts, IMRaD sections, reviewer-response wording, claim-supported paragraphs, and reporting-guideline text. Route whole-paper planning, reviewer-risk critique, literat... Path: `.agents/skills/writing-research-scientific-writing/SKILL.md`

### visualization
- `matplotlib`: Low-level plotting library for full customization. Use when you need fine-grained control over every plot element, creating novel plot types, or integrating with specific scientific workflows. Path: `.agents/skills/tools-visualization-matplotlib/SKILL.md`
- `plotly`: Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static publication figures use matplotlib or scie... Path: `.agents/skills/tools-visualization-plotly/SKILL.md`

### writing
- `chinese-prose`: 中文报告、README、Markdown/PDF 成稿、技术文档、科研说明、组会材料和“说人话”终审。任何中文 Markdown/PDF/报告/README/面向用户或读者的中文内容都应自动触发本 skill，用于普通中文润色、中文为主、降低 AI 味/翻译腔/模板腔/宣传腔，并保护事实、数字、术语、命令、引用、实验结果和证据边界。 Path: `.agents/skills/writing-core-chinese-prose/SKILL.md`
- `scientific-prose`: English scientific report writing and revision pass. Use for research reports, progress reports, figure-heavy PDFs, manuscripts, rebuttals, technical summaries, and slide text that must keep evidence, uncertainty, cap... Path: `.agents/skills/writing-core-scientific-prose/SKILL.md`
- `writing-fidelity`: Preserve facts, corrections, labels, structure, equations, citations, version authority, and final artifact identity during writing edits. Route Chinese natural-prose passes to chinese-prose, source-faithful structura... Path: `.agents/skills/writing-core-writing-fidelity/SKILL.md`

## Skill Maintenance

- Update command: `python3 /tmp/ai-skills-documents-media-scientific-pdf-rendering-reliability/scripts/skills.py install --target repo --mode copy --profile research-main --write-agents-md`
- Managed manifest: `.agents/skills/.ai-skills-collection-manifest.json`
- The installer only manages paths recorded in that manifest.
- User-created skills outside the manifest are never pruned.
<!-- AI_SKILLS_COLLECTION_END -->
