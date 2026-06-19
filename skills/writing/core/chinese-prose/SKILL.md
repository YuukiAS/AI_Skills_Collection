---
name: chinese-prose
description: 中文报告、README、技术文档和科研说明的最终审校。用于降低 AI 味、翻译腔、模板腔和宣传腔，同时保护事实、数字、术语、命令、引用、实验结果和中文读者的阅读习惯。
status: active
provenance: local
trusted: true
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-06-01
profile_tags:
recommended_scope: project
license: MIT-compatible synthesis plus public-domain style guidance
---
# Natural Chinese Final Pass

Use this skill as the final pass for Chinese reports, READMEs, technical docs, research progress notes, and public-facing Chinese explanations. The goal is not to make text casual. The goal is to make it clear, factual, natural for Chinese readers, and not obviously model-generated.

## Use When

- The user asks for Chinese text to be more natural, less AI-like, less translated, less slogan-like, or easier for Chinese readers.
- Revising Chinese reports, README files, project docs, research updates, grant/project summaries, or technical explanations.
- Checking whether a Chinese draft preserves facts while removing boilerplate.
- Converting mixed English/Chinese technical text into stable Chinese documentation style.

Do not use this skill to fact-check claims, translate literally, imitate a brand voice, or rewrite code/logs/commands.

## Core Rule

先保真，再自然。

Never change these unless the user explicitly asks:

- Numbers, dates, versions, ranges, units, percentages.
- Experiment conditions, metrics, baselines, table/figure labels, p-values, sample sizes.
- Commands, code, paths, parameters, environment variables, errors, logs, API names.
- Product names, module names, project names, people, institutions, citations, quoted text.
- Responsibility and attribution: who did what, who observed what, what is still uncertain.

If a sentence can only become smoother by weakening these facts, keep the facts and accept a little stiffness.

## Workflow

1. Identify the scene: `report`, `README`, `docs`, `status`, or `public-writing`.
2. Mark protected spans before editing.
3. Decide edit scope:
   - `minimal`: remove obvious template phrases and punctuation/style issues.
   - `standard`: rewrite sentences for Chinese rhythm while preserving structure.
   - `structural`: reorder sections only when the document is confusing or the user asks for a rewrite.
4. Remove AI-like patterns.
5. Apply Chinese documentation conventions.
6. Reread for fact preservation.
7. Return one clean version. Add notes only when there were overclaims, missing sources, or protected facts that constrained the rewrite.

## Scene Rules

### Report

Use for Chinese科研报告、组会材料、进展总结、实验说明。

- Keep question, evidence, interpretation, uncertainty, and next step visible.
- Do not turn "观察到" into "证明了".
- Avoid "具有重要意义", "为后续研究奠定基础", "展现出巨大潜力" unless the text names the evidence and boundary.
- Prefer concrete next steps: "下一步先做分层复现" instead of "后续继续优化".

### README

Use for project introduction and user-facing docs.

- First screen should answer: what this is, who it is for, what problem it solves, and how to start.
- Avoid promotional slogans.
- Keep commands, package names, config keys, and file paths unchanged.
- Prefer short sections with clear titles.

### Docs

Use for technical documentation and how-to material.

- Keep terminology stable. Do not alternate between Chinese name, English name, and abbreviation without reason.
- Keep step order and conditions explicit.
- Use direct instructions. Avoid chatty filler.
- Use punctuation and spacing consistent with Chinese technical documentation.

### Status

Use for progress updates and team communication.

- Keep time, action, result, risk, blocker, and owner.
- Do not soften risk or uncertainty to sound polished.
- Remove ceremonial summaries.

## AI-Like Patterns To Fix

Replace these with specific facts or delete them:

- 开场套话: "值得注意的是", "需要指出的是", "在当今快速发展的时代".
- 空总结: "综上所述", "总的来说", "归根结底".
- 价值拔高: "具有重要意义", "展现巨大潜力", "提供坚实基础".
- 无源权威: "研究表明", "业内普遍认为", "专家指出" without a source.
- 二元排比: "不仅是 X，更是 Y" when Y is vague.
- 三件套: forced "准确性、效率和鲁棒性" when the text only measured one property.
- 翻译腔: long chains of "基于...通过...实现...", overuse of passive voice, English word order in Chinese.
- 宣传腔: "赋能", "打造闭环", "全方位提升", "深度融合".
- 过度谄媚 or meta-commentary in README/docs: "这个问题非常关键", "下面我将".

## Chinese Documentation Conventions

- One paragraph should cover one topic.
- Prefer short, direct headings. Do not use ornate titles.
- Use Arabic numerals for measurements, versions, years, counts, and ranges.
- Keep spaces around inline English/code only when it improves readability; keep code spans exact.
- Define abbreviations on first use when readers may not know them.
- Avoid excessive exclamation marks, decorative punctuation, and em dashes.
- Keep list items parallel only when parallelism helps scanning; do not force every section into three bullets.

## Output

Default output is the revised text only.

If the user asks for review before rewrite, use:

```markdown
## 主要问题
- ...

## 建议改法
...
```

If facts were risky, add:

```markdown
## 保真说明
- ...
```

## References

Read `references/chinese-prose-checklist.md` for a full audit checklist. Read `references/source-notes.md` when provenance matters.
