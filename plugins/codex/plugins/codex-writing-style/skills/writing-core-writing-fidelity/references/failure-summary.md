# Source-Faithful Writing Failure Summary

This note summarizes recurring writing failures found in previous Qualify_Exam
conversations. Use it as evidence when a user asks for faithful editing,
polishing, OCR cleanup, layout repair, rendered-document QA, or final checks.

## High-Priority User Signals

Prioritize explicit user criticism such as:

- "不要乱删除"
- "还是有问题"
- "还是改了表里的内容"
- "莫名其妙"
- "听不懂"
- "我交代的事情要我重复几遍"
- "之前的修复仍然失败了"
- "不要自动改写"
- "不要把中文改成英文"
- "标题不要改"
- "字号放大一点"
- "这里撞到了"
- "还是有空白"
- "公式里还是莫名其妙有空格"
- "方框"

These identify failure modes the skill must prevent.

## Core Pattern

The repeated failure was not just bad LaTeX, bad PDF layout, or one bad review
sheet workflow. The deeper pattern was:

1. Codex changed content that should have been protected.
2. Codex polished by deleting or compressing information.
3. Codex optimized surface appearance while damaging readability or fidelity.
4. Codex treated a generated draft/report as completion.
5. Codex ignored user corrections that narrowed the task.

## Failure Modes To Prevent

### Deleting Under The Name Of Polishing

Polishing means improving readability while preserving content. Do not delete
facts, examples, equations, terms, caveats, comments, section titles, or source
structure unless the user explicitly asks to shorten or cut. If space is
limited, first reduce whitespace, improve layout, or use tighter phrasing.

### Rewriting Instead Of Editing

For edit/reconstruction tasks, preserve original wording and notation unless a
change is needed to fix a typo, rendering error, or obvious OCR corruption. Do
not canonicalize, translate, formalize, or normalize unless the user asks.

### Changing The Requested Language

Preserve the language of each source span. Chinese stays Chinese. English stays
English. Mixed Chinese/English stays mixed unless the user requests translation.

### Breaking Titles, Labels, And Local Structure

Titles, section names, table labels, theorem labels, source IDs, and ordering
are protected spans. A style pass must not rename titles. A layout pass must not
reorder content unless the user explicitly asks for reorganization.

### Ignoring Readability While Satisfying A Format

A document is not complete if it is technically generated but hard to read.
Check font size, line spacing, formula spacing, collisions, clipping, and
excessive whitespace. Use available space before shrinking text.

### Leaving Visual Or Formatting Errors

Visual QA is part of writing QA for PDF, slides, Markdown rendered to PDF, and
formatted documents. Render and inspect output. Do not call a document final if
there are visible collisions, unreadable regions, unexplained blank areas, or
awkward placement that contradicts the user's layout request.

### Font And Glyph Failures

For Chinese/math PDF output, verify rendered glyphs. Use Unicode-capable
engines and known fonts. Scan logs for missing glyphs and fatal LaTeX errors.
Build success is not the same as readable PDF success.

### OCR, Typo, And Formula Corruption

Treat OCR as draft, not final text. Run a typo/formula sanity pass before
finalizing. Protect formulas, code, variables, labels, citations, and numerical
values. Do not "fix" notation by preference; only fix actual corruption.

### Confusing Style With Content

Style-only edits must be style-only. Do not touch wording, titles, order, or
content during color/font/background changes. When the user specifies a color
or style, obey exactly or explain why it cannot be done.

### Treating Drafts, Reports, Or Side Files As Final

The requested artifact must exist, have the requested type, and be validated.
Reports and audits are supporting evidence, not replacements. Always state the
exact final file path and identify the real final candidate if several exist.

### Failing To Internalize User Corrections

Treat user corrections as updated hard constraints. Before each new edit,
restate internally what cannot be changed, what must remain, and what failure
triggered the correction. Do not continue a previous workflow unchanged after
the user says it failed.
