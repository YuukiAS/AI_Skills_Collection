# research-writing

Active skills: 9

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain research-writing --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill writing/research/academic-paper-writer-pro --skill writing/research/content-generation --skill writing/research/literature-review --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `academic-paper-writer-pro` (`skills/writing/research/academic-paper-writer-pro`): 基于规范目录结构的学术论文排版助手。支持 PDF / .doc / .docx / .md 多种输入格式，自动选择 OCR 管道、重排版管道或 MD 直转管道。包含环境清理确认、断点恢复、智能配图裁剪、逐单元增量生成 DOCX、双单元质量核查、中间状态保存和 BibTeX 参考文献管理。所有中间文件放 resources/，最终产物放 outputs/。
- `content-generation` (`skills/writing/research/content-generation`): 基于代码仓库、笔记、实验数据或论文要求，全自动智能撰写学术论文初稿的主线管线。强制分章逐批检索代码、分步输出，内置规避上下文超限机制和人工审核卡点，无缝衔接格式化引擎。内置严格的学术 Prompt 准则与多模态图表检索能力。
- `literature-review` (`skills/writing/research/literature-review`): Conduct comprehensive, systematic literature reviews using multiple academic databases (PubMed, arXiv, bioRxiv, Semantic Scholar, etc.).
- `ocr-kb` (`skills/writing/research/ocr-kb`): 使用多模态大模型逐页读取长文档图片，精确提取文本、LaTeX公式和独立科研配图。支持环境清理、断点恢复、全局编号管理、失败页标记与部分重跑。逐页生成DOCX并每两页核查质量。本 Skill 专用于 Pipeline A（OCR 管道），处理 PDF 输入。中间产物全部放在 resources/，最终交付物放在 outputs/。Pipeline B / C 定义在主 SKILL.md 中。
- `peer-review` (`skills/writing/research/peer-review`): Structured manuscript/grant review with checklist-based evaluation. Use when writing formal peer reviews with specific criteria methodology assessment, statistical validity, reporting standards compliance (CONSORT/STROBE), and constructive feedback.
- `research-grants` (`skills/writing/research/research-grants`): Write competitive research proposals for NSF, NIH, DOE, DARPA, and Taiwan NSTC. Agency-specific formatting, review criteria, budget preparation, broader impacts, significance statements, innovation narratives, and compliance with submission requirements.
- `scholar-evaluation` (`skills/writing/research/scholar-evaluation`): Systematically evaluate scholarly work using the ScholarEval framework, providing structured assessment across research quality dimensions including problem formulation, methodology, analysis, and writing with quantitative scoring and actionable feedback.
- `scientific-writing` (`skills/writing/research/scientific-writing`): Core skill for the deep research and writing tool. Write scientific manuscripts in full paragraphs (never bullet points).
- `venue-templates` (`skills/writing/research/venue-templates`): This skill should be used when preparing manuscripts for journal submission, conference papers, research posters, or grant proposals and need venue-specific formatting requirements and templates.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
