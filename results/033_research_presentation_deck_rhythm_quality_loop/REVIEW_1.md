---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 033_research_presentation_deck_rhythm_quality_loop
review_round: 1
decision: REVISE
implementation_commit: d89161077b13c80b0ce7b20e50eddb608f57e8b4
---

# 033 Deck Rhythm + Bounded Quality Loop — Review 1

## Decision

`REVISE`

033 当前不能进入视觉质量审核，因为真实 GitHub CI 在全库测试阶段失败。失败属于冻结 Plan 明确要求的 clean-run regression gate，不是视觉成熟度判断，也不是用户产品选择。

## Blocking finding — clean runner 生成的 visual manifest 缺少 contact-sheet identity binding

### Plan / regression basis

冻结 Plan 要求 normal production render 后生成真实 deck contact sheet，并要求 task-local visual manifest 将 `deck_contact_sheet`、contact-sheet identity 与当前 production/build/storyline identity 一起绑定。Acceptance Gate 10 同时要求 full tests 与真实 GitHub CI 全部通过。

### Observed evidence

真实 `Codex Marketplace` workflow run `33158181950` 的 `codex-marketplace` job 在 `python3 -m unittest discover -s tests` 失败；其余 Windows sparse checkout 与 Linux/Windows editable-install smoke 均通过。

两个失败测试分别是：

- `test_research_presentation_one_call_production_entry`
- `test_research_presentation_deck_quality_loop_consumes_review_and_fails_closed`

二者都在 clean temporary output 上调用 production validator 时失败，错误完全一致：

```text
visual_inputs.json: identity binding missing deck_contact_sheet
visual_inputs.json: identity binding missing deck_contact_sheet_sha256
```

这说明当前 tracked 033 artifact 虽然已经包含这两个 binding，但共享 normal production generator 在干净 runner / 临时输出目录中并不能稳定生成同样完整的 manifest。也就是说，当前实现存在“任务目录里的预生成证据是完整的，但正常 production 重新生成时 contract 不完整”的可复现差异。

同时，当前 push 触发的 `AI Bridge Visual Review` run `33158181985` 虽然 workflow conclusion 为 success，但 `Run visual review` 与 evidence commit 两步均被跳过；因此没有 fresh Terra evidence 可以绕过本次 CI failure，也不应消耗视觉审核轮次。

### Minimal repair

只修 shared normal production generation / manifest-writing path，使任何 clean output directory 在 contact sheet 已生成后，都确定性写入：

- `identity_bindings.deck_contact_sheet`
- `identity_bindings.deck_contact_sheet_sha256`
- 与该 contact sheet 对应的 `deck_contact_sheet` visual input item

并保证这些字段来自本次真实生成的 contact-sheet artifact，而不是仅在 `--write-result-visual-inputs` 或 task-local post-processing 路径中补写。

不得借机修改：

- deck-level quality rubric 或成熟度门槛；
- repair budget / no-winner 语义；
- 032 storyline、gold selector/recipe、Stage 3 layouts、CUHK identity 或 medical semantics；
- Stage 5 holdout scope。

### Evidence required after repair

至少需要看到：

1. 上述两个失败测试在 clean temporary directory 中通过；
2. `python -m unittest discover -s tests` 通过；
3. normal production validator 在 clean-generated output 上通过，并能核对 contact-sheet path 与 SHA；
4. 真实 GitHub CI 通过；
5. CI 通过后再由 task-local Visual Review 对当前 render/contact-sheet identity 生成 fresh evidence，之后才进入真正的 deck-level视觉审核。

## Non-blocking evidence retained

当前任务目录中的 033 manifest 已包含 deck contact sheet、contact-sheet SHA、deck sequence summary、quality-loop state 与 7 个 visual inputs，因此这轮不否定 contact-sheet 设计本身；问题仅是共享 normal production path 的 clean-run 可重复性。现有 RESULT 中记录的 bounded quality-loop 设计、一次 repair 上限与 fail-closed/no-winner 方向也不因本次 CI failure 被推翻。
