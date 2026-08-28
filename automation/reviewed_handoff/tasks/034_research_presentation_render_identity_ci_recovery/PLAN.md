---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 034_research_presentation_render_identity_ci_recovery
decision: PLAN_FROZEN
---

# 034 Research Presentation Render Identity CI Recovery — Plan

## Frozen decisions

### Objective and value

只关闭 033 Review 2 已明确定位的两个 clean-CI identity blocker，使同一 normal production path 在“真实像素可渲染”和“CI 环境缺少系统级渲染能力”两种情况下都拥有一致、可审计的 evidence semantics。

本 recovery 不重新设计 deck quality loop，也不降低 033 冻结的 mature-quality / Terra / source-fidelity bar。完成后应能回到 033 尚未真正进行的 deck/contact-sheet 视觉质量审核，而不是把 CI compatibility 本身当成 Stage 4 PASS。

### Preserved decisions

以下 033 已有能力全部冻结保护：

- normal `research-presentations` one-call production entry；
- source-fidelity map、032 通用 workstream storyline、normal gold selector/recipe 与 Stage 3 executable layouts；
- exact canonical CUHK `.tex + PDF + PNG` production route；
- deck contact sheet、deck sequence summary、deck-level Visual Review rubric；
- shared reviewer-evidence consumer；
- automatic repair cycle 上限 1；
- unknown / unsafe finding 的 `QUALITY_LOOP_FAIL_NO_WINNER`；
- medical same-case TP/FP/FN semantics 与 anti-meta leakage；
- task-local Visual Review manifest/evidence contract。

不得修改 Stage 2/3 mature bar，不得增加第二次 automatic repair，不得运行 Stage 5 holdout。

## Implementation scope

### Recovery mechanism — dual evidence identity, not validator relaxation

033 Review 1 已尝试只放宽 no-render validator 条件，但第二轮 CI 证明这种逐项补条件会遗漏 identity semantics。本 recovery 必须改用一个新的、有限机制：明确区分 **render-input identity** 与 **rendered-pixel identity**。

### 1. Render-input identity must always exist

每次 production render attempt 在调用真实编译/PNG render 之前或同时，必须从本次实际送入渲染链的确定性输入生成一个 64-char SHA identity。

优先绑定实际生成文件，而不是重新发明语义摘要。至少应覆盖：

- 当前 `main.tex`；
- 当前 `scientific_layouts.tex`；
- 若页面引用会直接改变输出像素的 copied scientific assets，也应使用已有 asset SHA / deterministic asset manifest 纳入同一 render-input identity。

实现可以采用一个 canonical manifest + stable SHA，或对上述实际 render inputs 的 path/SHA 组合做 stable SHA。不得只对 reviewer finding、repair directive 或 quality-loop state 本身哈希，因为 Acceptance Gate 7 要证明**生产表示/渲染输入真实变化**。

该 identity 必须在 compile/render unavailable 时仍存在。

### 2. Pixel identity remains strict and nullable when pixels do not exist

真实 PNG render 成功时：

- per-page `rendered_page_sha256` 必须继续为真实 64-char SHA；
- contact-sheet path/SHA 必须继续与本次 page pixels 一致；
- visual manifest 的 page/contact-sheet binding 继续严格核对；
- deck evidence 可以保留/扩展现有 `deck_identity_sha256`，但必须同时包含或可追溯到 render-input identity 与真实 pixel evidence。

render unavailable 时：

- 不得生成假 PNG SHA、空字符串冒充 SHA 或 synthetic pixel identity；
- `rendered_page_sha256` / contact-sheet pixel fields 可明确为 `null` / unavailable；
- sequence summary 必须有 machine-readable 状态说明 pixel evidence unavailable；
- `--allow-missing-render` 只允许跳过**不存在的像素证据**，不能跳过 render-input identity、storyline、gold/layout、quality-loop contract。

### 3. Repair identity must change when actual render input changes

033 deterministic repair fixture 已经证明 `ADJUST_TRANSITION_CUE` 会让 production `deck_plan` 和实际 `main.tex` 变化。本 recovery 必须把这件事纳入 identity contract：

- initial render attempt 保存 initial render-input identity；
- apply repair 后重新生成真正的 production render input；
- repaired render-input identity 必须与 initial 不同；
- quality-loop state 中的 initial/repaired identity 字段必须语义清楚，不得把“像素 identity”和“render-input identity”混为同一字段后依赖运行环境猜测。

如果保留旧 `initial_render_identity` / `repaired_render_identity` 字段，应明确它们到底指向哪种 identity，并新增必要的 pixel-specific 字段；也可以进行最小 schema-compatible 扩展，例如新增 `initial_render_input_identity` / `repaired_render_input_identity`，同时保留现有字段供下游兼容。不要新造另一套状态机。

### 4. Close the two exact CI regressions

必须修正 033 Review 2 中的两个失败：

- `test_research_presentation_one_call_production_entry` 在 no-render path 不得再对 `None` pixel SHA 无条件执行长度 64 的断言；测试必须同时确认 render-input identity 始终存在，并确认真实 render 时 pixel SHA 仍严格存在。
- `test_research_presentation_deck_quality_loop_consumes_review_and_fails_closed` 必须确认 transition repair 前后 render-input identity 不同。若 CI 没有像素，不再要求不存在的 pixel identity 证明变化；若本地/真实 render 有像素，可额外确认最终 pixel/contact-sheet binding。

禁止仅删除断言让测试通过。每个被放宽的 pixel-only assertion 都必须由对应的 unavailable-state + always-present render-input identity assertion替代。

### Production / plugin parity

如果 shared presentation scripts 同步镜像到 `plugins/codex/plugins/presentations/...`，相关 generator / validator / quality-loop changes 必须保持 parity，现有 parity regression 继续通过。不得只修 skill source 而留下 marketplace copy 漂移。

### Fresh evidence requirements

Executor 完成后必须重新生成当前 Stage 4 engineering bundle 的 normal production artifacts，并记录：

- render-input identity；
- 若本地真实 render 成功，则 page PNG SHA、contact-sheet SHA、PDF SHA；
- deck sequence summary；
- quality-loop state；
- task-local visual manifest，绑定本次新的 implementation/pixel identity。

不得复用 033 当前缺失的 Terra evidence。真实 GitHub CI 通过后，按现有 task-local Visual Review contract等待 fresh `VISUAL_REVIEW.json`；缺 evidence 时不消耗 review round。

## Acceptance and regression gates

Planner 只有在以下全部成立时才可 PASS 034：

1. normal production render attempt 始终产生 64-char render-input identity，且直接绑定实际生成的 render inputs；
2. no-render CI path 明确把 pixel evidence 标为 unavailable，不伪造 page/contact-sheet SHA；
3. real-render path 仍严格要求并核对真实 page PNG SHA、contact-sheet SHA 和当前 manifest binding；
4. deterministic `ADJUST_TRANSITION_CUE` repair 前后 render-input identity 必须不同，并且实际 `main.tex` / production representation 的变化仍由 regression 直接检查；
5. automatic repair count 仍最多 1；unknown finding 仍 fail closed/no-winner；
6. 033 Review 2 的两个失败测试通过，full unittest 全部通过；
7. skills validation、marketplace validate/check/path-report、shared/plugin parity、Reviewed Handoff validation通过；
8. 真实 GitHub `Codex Marketplace` CI 通过；
9. fresh task-local Visual Review evidence 与当前 implementation/render/contact-sheet identity 一致，并对 deck/contact-sheet 给出 item-level judgement；top-level workflow success 不能替代 evidence；
10. source fidelity、032 storyline、gold/layout、CUHK identity、medical semantics 无 regression。

## Out of scope

034 不得：

- 重新设计 deck quality loop；
- 降低 mature-quality、Terra 或 source-fidelity bar；
- 增加第二次 automatic repair；
- 扩展 Stage 2 或 Stage 3 mature layout scope；
- 运行 Stage 5 holdout；
- 把 CI compatibility 本身当成 Stage 4 PASS；
- 伪造 pixel identity、PNG SHA 或 contact-sheet SHA；
- 新造 Reviewed Handoff 状态机、role、receipt 或 hash graph。

## Stop condition

只要上述 identity contract、真实 CI 与 fresh deck-level evidence闭合即停止。034 不扩展新的 deck-quality feature，也不运行 Stage 5 holdout。

如果真实 fresh Terra 暴露的是新的视觉质量 blocker，Planner 按正常最多两轮 review处理；不要把它塞回 identity recovery scope。若 034 再到 review limit且出现唯一、范围清楚、质量保持的新 recovery，继续按 Program Goal 保留终态历史并另建 bounded task；禁止重复“再放宽一个测试条件”的同类无限链。

## Natural-language behavior

用户不会看到新的额外步骤。正常请求生成科研组会汇报时，系统仍走一次生产入口。内部如果第一次 deck review要求一次安全修复，系统应能证明修复真正改变了将要渲染的 deck；即使某个 CI 环境没有安装完整 TeX/PNG 渲染栈，也只能说“像素证据暂不可用”，不能把未渲染当成已渲染，也不能因为缺像素而失去对 render input 变化的可审计性。
