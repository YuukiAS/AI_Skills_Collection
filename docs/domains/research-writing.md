# research-writing

Active skills: 16

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain research-writing --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill writing/research/academic-paper-writer-pro --skill writing/research/citation-verification --skill writing/research/latex-paper-authoring --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `academic-paper-writer-pro` (`skills/writing/research/academic-paper-writer-pro`): 学术论文排版、OCR恢复、DOCX/Markdown整理和模板化交付工作流。用于扫描 PDF、DOC/DOCX、Markdown 到 Word/PDF 的结构修复、断点恢复、参考文献整理和最终文件验收；内容写作、审稿和事实保真应路由到 research-writing 与 writing-fidelity。
- `citation-verification` (`skills/writing/research/citation-verification`): Verify academic citations, references, BibTeX entries, DOI/PMID metadata, citation claims, and figure/table evidence before manuscript submission, review response, or report delivery. Use when citation existence or claim support matters more than citation formatting alone.
- `latex-paper-authoring` (`skills/writing/research/latex-paper-authoring`): Author, organize, repair, and prepare LaTeX research papers for arXiv, Overleaf, conference templates, or journal submission. Use when manuscript structure, LaTeX source hygiene, compilation, figures, bibliography, or template cleanup is central.
- `literature-review` (`skills/writing/research/literature-review`): Synthesize scholarly literature and create single-paper evidence cards. Use for systematic/scoping/narrative reviews, related work, paper精读, paper cards, claim-evidence extraction, method maps, thematic synthesis, and research-gap analysis. Route quick lookup, DOI/claim checks, BibTeX, and Zotero to citation skills.
- `nature-manuscript-workflow` (`skills/writing/research/nature-manuscript-workflow`): Plan, draft, revise, and audit broad-journal or high-impact manuscripts, including claim framing, figure logic, data availability, submission readiness, and reviewer response. Use for story-driven journal strategy, broad-audience manuscript framing, figure-to-claim alignment, and Nature-family targets when explicit.
- `ocr-kb` (`skills/writing/research/ocr-kb`): 长文档 OCR、扫描 PDF 恢复、公式/表格/图注提取、断点续跑和 DOCX/Markdown 交付工作流。用于把 PDF 页面安全转成可编辑文本并做质量核查；内部处理模式可记录为 OCR，但用户不需要说旧 pipeline 名。
- `paper-workflow-orchestrator` (`skills/writing/research/paper-workflow-orchestrator`): Orchestrate research paper workflows: manuscript plan, claim-evidence spine, result-to-claim gate, section contracts, figure/text sync, pre-submission acceptance checks, rebuttal planning, final artifact QA, and paper-structure rescue rather than paragraph polishing.
- `peer-review` (`skills/writing/research/peer-review`): Reviewer-style manuscript or grant critique and acceptance-risk assessment. Use for pre-submission self-review, paper验收, likely objections, rebuttal assessment, claim-evidence audit, methods/statistics critique, reporting standards, and concern ledgers. Route prose drafting to scientific-writing and scoring to scholar-evaluation.
- `research-grants` (`skills/writing/research/research-grants`): Write competitive research proposals for NSF, NIH, DOE, DARPA, and Taiwan NSTC. Agency-specific formatting, review criteria, budget preparation, broader impacts, significance statements, innovation narratives, and compliance with submission requirements.
- `research-notes` (`skills/writing/research/research-notes`): <!-- GPT-WRITES: RESEARCH_AUTHORING_DESIGN_V0_1.md 第 2.1～2.3、3.1 节；用户裁决 2 -->
- `research-reporting` (`skills/writing/research/research-reporting`): <!-- GPT-WRITES: RESEARCH_AUTHORING_DESIGN_V0_1.md 附录 D.1：兼容转接 -->
- `research-story` (`skills/writing/research/research-story`): <!-- GPT-WRITES: RESEARCH_AUTHORING_DESIGN_V0_1.md 第 2.1～2.3、3.1 节；用户裁决 2 -->
- `scholar-evaluation` (`skills/writing/research/scholar-evaluation`): Quantitatively evaluate scholarly work with a fixed rubric or ScholarEval-style dimensions. Use for rubric assessment, benchmarked quality scoring, numbered ratings, and dimension-by-dimension evaluation. Route ordinary reviewer-style critique to peer-review and prose revision to scientific-writing.
- `scientific-writing` (`skills/writing/research/scientific-writing`): Draft and revise scientific manuscript prose: abstracts, IMRaD sections, reviewer-response wording, claim-supported paragraphs, and reporting-guideline text. Route whole-paper planning, reviewer-risk critique, literature discovery, citation verification, BibTeX, figures, venue formatting, and LaTeX issues to neighboring skills.
- `student-materials` (`skills/writing/research/student-materials`): <!-- GPT-WRITES: RESEARCH_AUTHORING_DESIGN_V0_1.md 第 2.1～2.3、3.1 节；用户裁决 2 -->
- `venue-templates` (`skills/writing/research/venue-templates`): This skill should be used when preparing manuscripts for journal submission, conference papers, research posters, or grant proposals and need venue-specific formatting requirements and templates.

## Main References

- `skills/writing/research/research-notes/references/production-contract.md`
- `skills/writing/research/research-notes/references/research-notes.md`
- `skills/writing/research/research-reporting/references/group-meeting-advisor-reports.md`
- `skills/writing/research/research-story/references/group-meeting-advisor-reports.md`
- `skills/writing/research/research-story/references/production-contract.md`
- `skills/writing/research/research-story/references/research-story.md`
- `skills/writing/research/student-materials/references/production-contract.md`
- `skills/writing/research/student-materials/references/student-assessment-cumulative-acceptance-contract.md`
- `skills/writing/research/student-materials/references/student-assessment-delivery-closure-amendment-v1.md`
- `skills/writing/research/student-materials/references/student-assessment-end-to-end-pre-execution-runbook.md`
- `skills/writing/research/student-materials/references/student-assessment-hw1-nonrecurrence-amendment-v1.md`
