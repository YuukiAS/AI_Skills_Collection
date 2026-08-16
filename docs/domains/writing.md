# writing

Active skills: 16

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain writing --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill writing/research/academic-paper-writer-pro --skill writing/core/chinese-prose --skill writing/research/citation-verification --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `academic-paper-writer-pro` (`skills/writing/research/academic-paper-writer-pro`): 学术论文排版、OCR恢复、DOCX/Markdown整理和模板化交付工作流。用于扫描 PDF、DOC/DOCX、Markdown 到 Word/PDF 的结构修复、断点恢复、参考文献整理和最终文件验收；内容写作、审稿和事实保真应路由到 research-writing 与 writing-fidelity。
- `chinese-prose` (`skills/writing/core/chinese-prose`): 中文报告、README、Markdown/PDF 成稿、技术文档、科研说明、组会材料和“说人话”终审。任何中文 Markdown/PDF/报告/README/面向用户或读者的中文内容都应自动触发本 skill，用于中文为主、降低 AI 味/翻译腔/模板腔/宣传腔、移除非必要英文、修正版本/阶段名误用和机器字段先行，同时保护事实、数字、术语、命令、引用、实验结果、证据边界和中文读者习惯。
- `citation-verification` (`skills/writing/research/citation-verification`): Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or claim support matters more than citation formatting alone.
- `latex-paper-authoring` (`skills/writing/research/latex-paper-authoring`): Author, organize, repair, and prepare LaTeX research papers for arXiv, Overleaf, conference templates, or journal submission. Use when manuscript structure, LaTeX source hygiene, compilation, figures, bibliography, or template cleanup is central.
- `literature-review` (`skills/writing/research/literature-review`): Synthesize scholarly literature and create single-paper evidence cards. Use for systematic/scoping/narrative reviews, related work, paper精读, paper cards, claim-evidence extraction, method maps, thematic synthesis, and research-gap analysis. Route quick lookup, DOI/claim checks, BibTeX, and Zotero to citation skills.
- `nature-manuscript-workflow` (`skills/writing/research/nature-manuscript-workflow`): Plan, draft, revise, and audit broad-journal or high-impact manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use for story-driven journal strategy, broad-audience manuscript framing, figure-to-claim alignment, and Nature-family targets when explicit.
- `ocr-kb` (`skills/writing/research/ocr-kb`): 长文档 OCR、扫描 PDF 恢复、公式/表格/图注提取、断点续跑和 DOCX/Markdown 交付工作流。用于把 PDF 页面安全转成可编辑文本并做质量核查；内部处理模式可记录为 OCR，但用户不需要说旧 pipeline 名。
- `paper-workflow-orchestrator` (`skills/writing/research/paper-workflow-orchestrator`): Orchestrate research paper workflows: manuscript plan, claim-evidence spine, result-to-claim gate, section contracts, figure/text sync, pre-submission acceptance checks, rebuttal planning, final artifact QA, and paper-structure rescue rather than paragraph polishing.
- `peer-review` (`skills/writing/research/peer-review`): Reviewer-style manuscript or grant critique and acceptance-risk assessment. Use for pre-submission self-review, paper验收, likely objections, rebuttal assessment, claim-evidence audit, methods/statistics critique, reporting standards, and concern ledgers. Route prose drafting to scientific-writing and scoring to scholar-evaluation.
- `research-grants` (`skills/writing/research/research-grants`): Write competitive research proposals for NSF, NIH, DOE, DARPA, and Taiwan NSTC. Agency-specific formatting, review criteria, budget preparation, broader impacts, significance statements, innovation narratives, and compliance with submission requirements.
- `research-reporting` (`skills/writing/research/research-reporting`): Create repo-grounded research reports, milestone summaries, experiment reviews, technical notes, and result retrospectives from project evidence. Use for Markdown reports and internal scientific documentation, not for full journal manuscript workflows.
- `scholar-evaluation` (`skills/writing/research/scholar-evaluation`): Quantitatively evaluate scholarly work with a fixed rubric or ScholarEval-style dimensions. Use for rubric assessment, benchmarked quality scoring, numbered ratings, and dimension-by-dimension evaluation. Route ordinary reviewer-style critique to peer-review and prose revision to scientific-writing.
- `scientific-prose` (`skills/writing/core/scientific-prose`): English scientific report writing and revision pass. Use for research reports, progress reports, figure-heavy PDFs, manuscripts, rebuttals, technical summaries, and slide text that must keep evidence, uncertainty, captions, and conclusions scientifically defensible without AI-sounding or defensive/self-undermining prose.
- `scientific-writing` (`skills/writing/research/scientific-writing`): Draft and revise scientific manuscript prose: abstracts, IMRaD sections, reviewer-response wording, claim-supported paragraphs, and reporting-guideline text. Route whole-paper planning, reviewer-risk critique, literature discovery, citation verification, BibTeX, figures, venue formatting, and LaTeX issues to neighboring skills.
- `venue-templates` (`skills/writing/research/venue-templates`): This skill should be used when preparing manuscripts for journal submission, conference papers, research posters, or grant proposals and need venue-specific formatting requirements and templates.
- `writing-fidelity` (`skills/writing/core/writing-fidelity`): Preserve facts, corrections, labels, structure, equations, citations, version authority, and final artifact identity during writing edits. Use for source-faithful Markdown, LaTeX, PDF, slides, reports, notes, and evidence-bound writing. Route Chinese natural-prose passes to chinese-prose and English scientific style passes to scientific-prose.

## Main References

- `skills/writing/core/chinese-prose/references/chinese-prose-checklist.md`
- `skills/writing/core/chinese-prose/references/group-meeting-chinese-report-prompt.md`
- `skills/writing/core/chinese-prose/references/source-notes.md`
- `skills/writing/core/scientific-prose/references/scientific-report-checklist.md`
- `skills/writing/core/scientific-prose/references/source-notes.md`
- `skills/writing/core/writing-fidelity/references/failure-summary.md`
