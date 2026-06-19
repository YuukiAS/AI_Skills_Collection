# writing

Active skills: 3

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain writing --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill natural-chinese-final-pass --skill reusable-writing-scientific-evidence-prose --skill reusable-writing-source-faithful-writing-final-pass --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `natural-chinese-final-pass` (`skills/reusable/writing/natural-chinese-final-pass`): 中文报告、README、技术文档和科研说明的最终审校。用于降低 AI 味、翻译腔、模板腔和宣传腔，同时保护事实、数字、术语、命令、引用、实验结果和中文读者的阅读习惯。
- `scientific-evidence-prose` (`skills/reusable/writing/scientific-evidence-prose`): English scientific report writing and revision pass. Use for research reports, progress reports, figure-heavy PDFs, manuscripts, technical summaries, and slide text that must keep evidence, uncertainty, captions, and conclusions scientifically defensible without AI-sounding prose.
- `source-faithful-writing-final-pass` (`skills/reusable/writing/source-faithful-writing-final-pass`): Prevent deletion, over-rewriting, mistranslation, formatting breakage, and false completion in user-facing writing. Use when editing, polishing, summarizing, translating, OCR-cleaning, rendering, compressing, or final-checking Markdown, LaTeX, PDF, reports, notes, exam review material, technical documents, or source-derived writing.

## Main References

- `skills/reusable/writing/natural-chinese-final-pass/references/chinese-final-pass-checklist.md`
- `skills/reusable/writing/natural-chinese-final-pass/references/group-meeting-chinese-report-prompt.md`
- `skills/reusable/writing/natural-chinese-final-pass/references/source-notes.md`
- `skills/reusable/writing/scientific-evidence-prose/references/scientific-report-checklist.md`
- `skills/reusable/writing/scientific-evidence-prose/references/source-notes.md`
- `skills/reusable/writing/source-faithful-writing-final-pass/references/failure-summary.md`
