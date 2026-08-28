# Final Report

## What this task solved

034 解决了 033 留下的 evidence-identity 根问题：科研汇报在真实渲染和无系统级 PNG 渲染能力的 CI 环境中，现在都能区分“实际送去渲染的生产输入”与“真实产生的像素证据”。因此一次 bounded repair 如果真的改变了 `main.tex` / scientific render inputs，即使 CI 没有像素，也能被稳定审计；有真实像素时，逐页 PNG、contact sheet 与 PDF 仍保持严格绑定。

本 task 还在第一轮视觉审核后关闭了两个真实 presentation blocker：标题页工程元语言泄漏已移除并加入通用 metadata 防泄漏检查；模型页已经从“公式+单句”的明显欠填充状态提升为有公式主对象、模型角色与解释层的完整页面。当前 engineering deck 的 fresh Terra 六个内容页和整套 contact sheet 均为 item-level PASS。

034 最终没有被标记为 PASS，因为第二轮独立代码审核发现模型页 supporting copy 中仍残留当前 clustered-calibration fixture 的硬编码科学语义。这个问题不会通过降低质量门槛解决，而是由后续新的 bounded recovery 单独关闭。

## What changed

共享 research-presentation production path 增加并保留了双层 identity：render-input identity 直接绑定本次实际生成的 `main.tex`、`scientific_layouts.tex`、canonical CUHK support files 与直接影响像素的 scientific assets；rendered-pixel identity 则只在真实 render 存在时绑定 per-page PNG、contact sheet 和 PDF。

no-render validation 现在允许 pixel fields 明确为 unavailable，但不能跳过 render-input identity。deterministic repair 前后如果实际生产表示变化，render-input identity 必须同步变化。原有一次 automatic repair 上限、unknown/unsafe finding fail-closed/no-winner、deck contact sheet 和 deck-level reviewer contract 均未放宽。

第一轮 repair 还把 title/subtitle 纳入 audience-facing anti-meta policy，并把已有 `key_message` / `scientific_objects` 传入模型页 normal production spec，使 source-supported explanation 能进入真实渲染页面。shared skill source 与 Codex marketplace mirror 保持同步。

## New capabilities / behavior

系统现在可以在没有完整 TeX/PNG 渲染栈的干净 CI 环境里诚实表示“像素证据不可用”，同时仍然证明本次生产输入是什么、一次 repair 是否真实改变了将要渲染的 deck。这避免了过去用缺失 PNG identity 推断 production change 的语义漏洞。

在真实渲染环境里，当前 Stage 4 engineering bundle 已重新生成 exact CUHK PDF、六个内容页 PNG 与整套 contact sheet，并取得与当前 implementation/pixel identity 一致的 fresh visual review。标题页不再显示工程回归/来源包语言，模型页也不再呈现明显未完成的大面积空白。

## Deliberately not adopted / unchanged

没有通过伪造 PNG SHA、给 `None` 填假 hash、删除关键 assertion 或放宽 Terra/mature-quality bar 来让 CI 变绿。Stage 2 gold composition、Stage 3 executable layout、032 storyline、多 workstream 语义、CUHK identity、medical same-case TP/FP/FN、deck-level rhythm rubric 和一次 repair budget均保持不变。

没有运行 Stage 5 真实双-paper holdout，也没有把当前 synthetic engineering bundle 的通过当作长期 program PASS。

第二轮发现的 model-support hardcode 也没有在 034 内伪造第三轮 review。034 保留 review-limit 历史，后续只针对该唯一剩余 blocker 建立新的有限 recovery。

## Example usage

普通用户仍只需正常请求“根据这篇研究材料生成 CUHK 组会汇报”。内部生产路径可以先生成 source-faithful TeX/PDF，再对真实页面和整套 deck 做视觉审核；若一次安全修复改变了汇报，即使某个 CI runner 无法真正渲染 PNG，系统仍能证明修复改变了实际 render input，而不会把“没有像素”误报成“像素已通过”。

对于真实可渲染环境，系统继续要求最终页面 PNG/contact sheet 与本次 PDF、manifest 和 implementation 一致，不能拿旧截图替代当前结果。

## Regression and remaining limitations

真实 GitHub `Codex Marketplace` CI 已通过；fresh task-local Terra 对 `slide_2_statistical_model`、结果页、实验设计页、负结果页、下一实验页、医学影像页和 `deck_contact_sheet` 全部给出 PASS，并确认当前 deck 的跨页节奏、CUHK 身份、独立 workstream transition 和医学影像语义无回归。

剩余唯一 blocker 是共享 equation renderer 的 supporting copy 仍含当前 clustered-calibration fixture 专用文本：`Calibration link`、`Center variation and individual variation define the ICC before the interval comparison.`，以及缺 supporting fields 时的 `Source-grounded terms remain attached to the equation.` fallback。当前样例恰好语义匹配，因此像素审核无法暴露这一通用性问题；对未见模型它可能产生错误或制作型 audience-facing 文案。这个问题需要新的 bounded recovery 用 unrelated-model regression 关闭。

因此 034 以第二轮 `REVISE` 达到 review limit，不等于 Stage 4 PASS；Stage 4 继续保持 active。

## Technical appendix

- task: `034_research_presentation_render_identity_ci_recovery`
- implementation commit: `fc0b8908b865de464c0d1ddf4475a9e57c11bbd5`
- real CI locator/control commit: `29ed740042a4c08f41aac3a81993b26b9fa59a93`
- GitHub `Codex Marketplace` run: `33200314231`, all four jobs success
- GitHub task-local visual-review run: `33200314241`, success with evidence written back
- fresh visual evidence: `results/034_research_presentation_render_identity_ci_recovery/visual_review/VISUAL_REVIEW.json`
- current visual manifest: `results/034_research_presentation_render_identity_ci_recovery/visual_review/visual_inputs.json`
- generated deck artifacts: `results/034_research_presentation_render_identity_ci_recovery/generated/`
- current PDF SHA-256: `f55c396428cd1e11657717b0a8b64ddc73e6637c860bb5745a2327905e49470b`
- render-input identity: `a960ec005fc46f12fccb396bda639535e911273f7592dfa91f4494af5d8b5118`
- rendered-pixel identity: `d9048ee78d41e307821d1bb52a9430c05c212fea8c653f4d621a145e5eafd2c1`
- contact-sheet SHA-256: `5ba36bbd97f465e5bd05729113dc5f570243f5ec371e705758f98f747d55065a`
