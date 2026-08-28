---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 033_research_presentation_deck_rhythm_quality_loop
review_round: 2
decision: REVISE
implementation_commit: 3130e3db9b5a724ac05f0c3ba9da5886b5920260
---

# 033 Deck Rhythm + Bounded Quality Loop — Review 2

## Decision

`REVISE`

033 不能 PASS。Review 1 的 contact-sheet validator blocker 已被局部关闭，但真实 GitHub CI 再次在全库测试中失败，而且新的失败仍位于冻结 Plan 要求的 clean-run / deterministic repair regression contract。由于本 task 已用满两轮 review，本文件只记录第二轮结论；不得创建 `REVIEW_3`。后续若继续，必须按 Program Goal 另建质量保持的 bounded recovery task。

## Blocking finding 1 — no-render CI 路径仍把 pixel SHA 当成必有字段

### Plan / regression basis

冻结 Plan 要求完整 deck sequence summary 保存 per-page rendered SHA，同时要求真实 CI 全部通过。CI runner 允许缺失系统级 TeX/render 依赖，因此测试会使用 `--allow-missing-render` 验证 non-render path；这种环境不能伪造 PNG SHA，也不能因为没有像素而让 machine-readable deck evidence 自相矛盾。

### Observed evidence

真实 `Codex Marketplace` run `33161765248` 在 `python3 -m unittest discover -s tests` 失败。`test_research_presentation_one_call_production_entry` 在 `tests/test_presentations.py:869` 对 `page["rendered_page_sha256"]` 直接执行 `len(...)`，但 clean GitHub runner 的 render unavailable path 合法返回 `None`，触发：

```text
TypeError: object of type 'NoneType' has no len()
```

Review 1 repair 已把 contact-sheet path/SHA 的 validator 与若干测试改成只在 `render_status == ok` 时强制，但没有把相同的 rendered-page identity contract 一并处理完整。因此 CI 仍无法通过 clean no-render path。

### Minimal recovery direction

新的 recovery 必须显式区分“始终存在的 render-input / production representation identity”和“只有真实像素存在时才有的 rendered-pixel SHA”。不得给缺失像素伪造 SHA，也不得通过删除真实 rendered evidence requirement 来让 CI 变绿。

## Blocking finding 2 — repair regression 的 identity 没有绑定实际 render input

### Plan / regression basis

冻结 Plan Acceptance Gate 7 要求 deterministic repair regression 证明 repair directive 会改变相应 production representation/render input，而不是只写一份状态报告；同时 quality-loop state 需要记录 initial 与 repaired render identity。

### Observed evidence

同一真实 CI run 中，`test_research_presentation_deck_quality_loop_consumes_review_and_fails_closed` 在 `tests/test_presentations.py:960` 失败：

```text
AssertionError: 'c9ff68840f290e847a2e28a36d90f45b99ca0479ca592edc609ed030aa00b886'
==
'c9ff68840f290e847a2e28a36d90f45b99ca0479ca592edc609ed030aa00b886'
```

测试已经确认 repair 后 `deck_plan` 的 transition cue 变为 `compact`，生成的 `main.tex` 也出现对应更紧凑的 panel geometry，因此 repair 确实改变了 production render input。但当前 `deck_identity_sha256` 只由 page order、rendered-page SHA、workstream/title sequence 和 contact-sheet SHA 组成；在 GitHub runner 没有像素 render 时，rendered SHA 与 contact-sheet SHA 都为 `None`，transition repair 没有进入 identity payload，于是 initial / repaired identity 保持相同。

这不是视觉成熟度问题，而是 evidence identity 的语义缺口：当前 identity 不能在 render unavailable 的合法运行环境中证明“一次 repair 确实改变了将要送去渲染的输入”。

### Minimal recovery direction

新的 recovery 应采用与 blocker 对应的新机制：为每次 render attempt 生成 deterministic render-input identity，例如直接绑定实际生成的 `main.tex` / scientific layout input（及必要的已有科学资产 identity），并把它纳入 deck evidence / quality-loop identity。真实 PNG 存在时仍继续保存 page-level pixel SHA 与 contact-sheet SHA；没有像素时只允许 pixel fields 为缺失状态，不能假装已有视觉证据。

## Evidence required in recovery

后续 bounded recovery 至少必须看到：

1. clean no-render runner 中，sequence summary 明确表示 pixel evidence unavailable，同时始终有可验证的 render-input identity；
2. 同一 deterministic transition repair 前后，实际 render input identity 必须变化；
3. 若真实 render 可用，per-page rendered SHA、contact-sheet SHA 与现有 task-local Visual Review binding 继续严格成立；
4. 上述两个当前失败测试与 full unittest 全部通过；
5. 真实 GitHub CI 通过后，再生成 fresh task-local Terra deck/contact-sheet evidence；不得使用 033 当前没有产生的 `VISUAL_REVIEW.json` 冒充视觉通过。

## Preserved evidence / scope

本轮不推翻 033 已建立的 deck contact sheet、deck sequence summary、bounded evidence consumer、单次 repair budget、unknown finding fail-closed/no-winner、032 storyline、normal gold/layout、exact CUHK identity 或 medical semantics。当前 task-local engineering artifact 本身具有真实 7-slide contact sheet 和 current-pixel manifest；但 CI 未通过且当前不存在 fresh `VISUAL_REVIEW.json`，因此这些证据不能形成 033 PASS。
