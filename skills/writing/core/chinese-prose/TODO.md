# TODO: make Chinese progress reports actually usable for oral presentations

Created: 2026-06-01  
Skill: `writing/core/chinese-prose`

## Why this TODO exists

The current skill correctly says "先保真，再自然", but it is not strict enough for group-meeting materials. In the CARE progress-report rewrite, the output stayed too much like a repo audit or technical archive:

- It preserved internal terms such as `guardrail`, `component gate`, `hosted metric`, `dry-run`, `remote FP`, `proxy`, `OOF`, and `submission-level`.
- It produced long prose and evidence dumps before giving the speaker a usable first slide.
- It mixed three different artifacts: audit record, written report, and oral meeting script.
- It treated "natural Chinese" as sentence polishing, not as choosing what a human can actually say in a meeting.
- It put file paths and implementation lineage too close to the main story instead of keeping them in backup.

The skill needs explicit rules for **presentation-facing Chinese**.

## Missing capability

Add a scene under `Scene Rules`:

### Group Meeting / Presentation Outline

Use this when the user asks for:

- 组会汇报
- 汇报用
- 可以讲的版本
- slide outline
- "讲一个故事"
- "人读的"
- "不要 AI 味"
- "方便我讲"

Rules:

1. Start with the speaker's first page, not a background essay.
2. The first section must answer:
   - 现在到底有没有新结果？
   - 哪个指标最重要？
   - 相比上次多做了什么？
   - 哪些方法有用？
   - 哪些方法失败？
   - 下一步做什么？
3. Use bullets and small tables before prose.
4. Write speaker-ready sentences under headings like `可以这样讲`.
5. Move paths, commit IDs, command details, branch names, and audit trails to a final backup section.
6. Translate internal English terms into meeting Chinese unless the term is the actual challenge metric or model name.
7. Keep evidence boundaries visible: "本地信号", "还不是官网结果", "需要更多折复现", "不建议直接提交".
8. Do not make the user read a repository report aloud.

## Required jargon cleanup

Before finalizing a Chinese presentation document, scan and replace internal jargon:

| Avoid in main text | Prefer in presentation Chinese |
| --- | --- |
| guardrail | 保护指标 / 不能被误伤的指标 |
| component gate | 可疑区域筛选 / 过滤不可靠的小块 |
| hosted metric | 官网指标 / 官网评分 |
| leaderboard | 排行榜 |
| submission-ready | 可以直接提交 |
| dry-run | 本地预演 |
| cache-isolated | 单独输出目录 / 不复用旧结果 |
| external repo | 外部代码库 |
| remote FP | 远端假阳性 / 远离主体区域的假阳性 |
| proxy | 本地观察指标 / 间接指标 |
| topology cleanup | 形态修正 / 连通性修正 |
| sanity metric | 辅助检查指标 |
| label mapping | 标签转换 |
| case manifest | 病例清单 |
| zip layout | 压缩包结构 |
| backbone | 主干网络 |
| pipeline | 流程 |

Allowed exceptions:

- Keep official metric names such as `myops_scar`, `myops_edema`, `myocardium_cinemyops`.
- Keep model names such as nnU-Net, MedNeXt, CAA-Seg, SegVol.
- Keep file paths exact in backup/evidence sections.

## Acceptance checklist

Before returning a rewritten Chinese meeting document, verify:

- The first page can be read aloud in under 60 seconds.
- The first section contains concrete bullets, not only paragraphs.
- A non-author can answer "what changed since last time?" after reading the first page.
- Each metric has one sentence saying the current biggest problem.
- Each attempted method has a result and a decision: continue, pause, backup only, or needs calibration.
- Failed routes are not hidden; each failure says whether it still has value.
- External code usage is summarized as: used and has metrics / only audited / not yet used.
- Internal jargon is either translated or moved to backup.
- Evidence paths are not in the main speaking flow.
- The output sounds like meeting notes for a person, not a generated repo report.

## Prompt to add as a reference

See `references/group-meeting-chinese-report-prompt.md`.
