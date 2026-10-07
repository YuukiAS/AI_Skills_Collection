# AGENTS.md

<!-- AI_SKILLS_COLLECTION_START -->
# AI Skills Collection

Installed: `2026-10-07T07:07:46+00:00`
Target: `repo`
Install mode: `profile:research-main`
Project skills: `.agents/skills/`
Central collection: `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

When a task matches an installed skill, read that skill's `SKILL.md` before acting. Keep progressive disclosure: load `references/` only when the skill says they are relevant.

## Profile Routing Notes

- For advisor-facing, group-meeting, milestone, experiment-review, or repo-grounded report requests that also ask for a formal/readable PDF, use Research Authoring first: read `research-authoring-core`, then `research-reporting`, produce stable source plus an explicit downstream production handoff, then use `render-chinese-math-pdf` only for admitted PDF route/profile/font/layout mechanics, and finally return to Research Authoring for scientific QA. Do not satisfy such requests by using only PDF/rendering skills.
- For manuscript, supplement, thesis-chapter, reviewer-response, or submission-package requests that also ask for PDF, use `research-authoring-core` and `paper-workflow-orchestrator` first, delegate source/package details to `latex-paper-authoring` when needed, hand off to `render-chinese-math-pdf` only after the source/package is stable, then run final Research Authoring scientific QA.
- For finalized Markdown or LaTeX where the user asks only to render or QA the existing source, route directly to `render-chinese-math-pdf`; do not run full Research Authoring planning.
- For generic existing-PDF extraction, merging, inspection, or manipulation, use the generic `pdf` helper when appropriate; it is not the creator-owner for new formal research reports or manuscripts.

## Skill Routing

### core
- `codex-workflow-protocol`: Use for complex or risky Codex tasks that require source-of-truth discovery, phased planning, specialist routing, gate-driven verification, live-state supervision, integration ownership, or honest final status reporting. Path: `.agents/skills/core-codex-system-codex-workflow-protocol/SKILL.md`

### documents-media
- `docx`: Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file,... Path: `.agents/skills/tools-documents-media-docx/SKILL.md`
- `markitdown`: Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs and more. Path: `.agents/skills/tools-documents-media-markitdown/SKILL.md`
- `pdf`: Use this skill whenever the user wants to do anything with PDF files. If the user mentions a .pdf file or asks to produce one, use this skill. Path: `.agents/skills/tools-documents-media-pdf/SKILL.md`
- `render-chinese-math-pdf`: Render and validate finalized Chinese or mixed Chinese/English mathematical Markdown/LaTeX as PDF, or run PDF QA after document-owner handoff. Use for render-only source and admitted renderer stages. Do not become fir... Path: `.agents/skills/tools-documents-media-render-chinese-math-pdf/SKILL.md`

### research-discovery
- `citation-management`: Manage bibliography, BibTeX, citation metadata, and reference-library hygiene. Use for DOI/PMID/arXiv-to-BibTeX conversion, metadata extraction, duplicate repair, and style formatting. Route claim support to citation-... Path: `.agents/skills/science-discovery-citation-management/SKILL.md`
- `research-lookup`: Find current research information and recent papers quickly. Use for latest papers, targeted evidence gathering, methods/protocol checks, and source-backed facts. Route systematic or related-work synthesis to literatu... Path: `.agents/skills/science-discovery-research-lookup/SKILL.md`

### research-writing
- `citation-verification`: Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or cl... Path: `.agents/skills/writing-research-citation-verification/SKILL.md`
- `latex-paper-authoring`: Author, organize, repair, and prepare LaTeX research paper source/packages for arXiv, Overleaf, templates, or submission. Use directly for existing-LaTeX compile/debug/source hygiene; for new/substantial manuscripts,... Path: `.agents/skills/writing-research-latex-paper-authoring/SKILL.md`
- `literature-review`: Synthesize scholarly literature and create single-paper evidence cards. Use for systematic/scoping/narrative reviews, related work, paper精读, paper cards, claim-evidence extraction, method maps, thematic synthesis, and... Path: `.agents/skills/writing-research-literature-review/SKILL.md`
- `nature-manuscript-workflow`: Plan, draft, revise, and audit broad-journal or high-impact manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use for story-driven journal strategy, br... Path: `.agents/skills/writing-research-nature-manuscript-workflow/SKILL.md`
- `paper-workflow-orchestrator`: Orchestrate research paper workflows: manuscript plan, claim-evidence spine, result-to-claim gate, section contracts, figure/text sync, pre-submission checks, rebuttal planning, source/package handoff, and post-render... Path: `.agents/skills/writing-research-paper-workflow-orchestrator/SKILL.md`
- `research-authoring-core`: Canonical document-level coordinator for Research Authoring. Use before producing or substantially revising reports, manuscripts, related work, research updates, responses, or supplements, including formal-PDF intent.... Path: `.agents/skills/writing-research-research-authoring-core/SKILL.md`
- `research-reporting`: Create repo-grounded research reports, milestone summaries, experiment reviews, technical notes, advisor/group-meeting reports, and result retrospectives from project evidence. Use for report semantics even when the f... Path: `.agents/skills/writing-research-research-reporting/SKILL.md`
- `scientific-writing`: Draft and revise scientific manuscript prose: abstracts, IMRaD sections, reviewer-response wording, claim-supported paragraphs, and reporting-guideline text. Route whole-paper planning, reviewer-risk critique, literat... Path: `.agents/skills/writing-research-scientific-writing/SKILL.md`

### visualization
- `matplotlib`: Low-level plotting library for full customization. Use when you need fine-grained control over every plot element, creating novel plot types, or integrating with specific scientific workflows. Path: `.agents/skills/tools-visualization-matplotlib/SKILL.md`
- `plotly`: Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static publication figures use matplotlib or scie... Path: `.agents/skills/tools-visualization-plotly/SKILL.md`

### writing
- `chinese-prose`: 中文报告、README、Markdown/PDF 成稿、技术文档、科研说明、组会材料和长文“说人话”终审。任何中文 Markdown/PDF/报告/README/面向读者的文档型中文内容都应自动触发本 skill，用于普通中文润色、中文为主、降低 AI 味/翻译腔/模板腔/宣传腔，并保护事实、数字、术语、命令、引用、实验结果和证据边界。产品界面标签、按钮、状态、帮助、信任/隐私披露和 locale-specific UI micr... Path: `.agents/skills/writing-core-chinese-prose/SKILL.md`
- `scientific-prose`: English scientific report writing and revision pass. Use for research reports, progress reports, figure-heavy PDFs, manuscripts, rebuttals, technical summaries, and slide text that must keep evidence, uncertainty, cap... Path: `.agents/skills/writing-core-scientific-prose/SKILL.md`
- `writing-fidelity`: Preserve facts, corrections, labels, structure, equations, citations, version authority, and final artifact identity during writing edits. Route Chinese natural-prose passes to chinese-prose, source-faithful structura... Path: `.agents/skills/writing-core-writing-fidelity/SKILL.md`

## Skill Maintenance

- Update command: `python3 /overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring/scripts/skills.py install --target repo --mode copy --profile research-main --write-agents-md`
- Managed manifest: `.agents/skills/.ai-skills-collection-manifest.json`
- The installer only manages paths recorded in that manifest.
- User-created skills outside the manifest are never pruned.
<!-- AI_SKILLS_COLLECTION_END -->
