---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 031_research_presentation_one_call_production_entry
review_round: 1
decision: REVISE
implementation_commit: 93c99427012d771098f4116b81cb7e86e406fbbc
---

# 031 One-Call Production Entry — Review 1

## Decision

`REVISE`

031 已经证明了本任务最核心的生产集成链路：普通 `research-presentations` 路径能够从文件路径读取输入 bundle，建立 source-fidelity map 和 page jobs，经正常 Stage 2 selector / recipe 选择 gold，调用 Stage 3 shared layouts，复制 canonical CUHK Beamer source，生成 `.tex + PDF + rendered PNGs`，并产出 task-local Visual Review manifest。当前 runtime trace 也明确显示没有 benchmark helper 作为 orchestration surface、没有 `force_gold_id` 或 score override；engineering fixture 明确排除在 Stage 5 holdout 之外。真实 CI 已由当前 handoff 状态结算为 PASS。

当前不能 PASS 的原因仅来自 fresh task-local rendered-pixel review 中两个与冻结 Plan 直接相关的阻断项。其余页面的 source specificity、主科学对象可读性、内部元语言防泄漏、页面形态多样性和 deck coherence 已有正向证据。

## Blocking finding 1 — exact CUHK source 与当前可见 identity 不一致

### Plan basis

冻结 Plan 要求：exact CUHK title/navigation/frame/footline identity 必须来自 canonical template source；Visual Review rubric 同时要求当前 rendered deck 中 exact CUHK identity 可见。

### Observed evidence

生产实现确实执行了 `shutil.copytree(CANONICAL_CUHK, build_dir)`，生成的 `main.tex` 使用 `\usetheme{sintef}` 与 canonical assets；生成 build 中的 `beamerthemesintef.sty` 也保留了 canonical headline 定义，明确声明每页顶部使用 `assets/logo_RGB`。因此 source-side exact-CUHK provenance 本身成立。

但是当前 fresh `VISUAL_REVIEW.json` 绑定 implementation `93c99427...` 与六张当前 rendered PNG，并逐页观察到：内容页可见的是一致的顶部导航/页码风格，却没有能够识别为 CUHK 的名称、crest/logo 或其他明确 identity；六页因此全部在 `R-CUHK-IDENTITY` 上被 BLOCKED。

这里不能简单把 Terra 的要求解释成“每页必须额外添加一套新 logo”。真正的 blocker 是 source contract 与 rendered pixels 不一致：canonical source 声称 headline/logo 应出现，但当前 review pixels 没有建立该 identity。Planner 不能只凭 source 文件存在就覆盖真实像素证据。

### Minimal repair

只诊断并修复 canonical CUHK identity 为什么没有在当前 content-page render 中可见。优先保持 canonical template 原样生效；如果是生成入口、headline/导航覆盖、asset copy/load 或 content-space interaction 导致 identity 消失，修对应 shared production/Stage-3 integration 原因。

不得重新设计 CUHK template，不得为 031 单独画一个伪造 logo，也不得用 audience-facing `CUHK` 文本贴片绕过 canonical source。

修复后需要看到：新的 content-page rendered pixels 中，canonical CUHK identity 按模板设计真实可见，且 title/navigation/frame/footline/content geometry 不回归。

## Blocking finding 2 — medical comparison 的误差颜色与 prediction view 无法从像素上对应

### Plan basis

冻结 Plan 要求 math/plot/image semantic correctness；Stage 3 已接受的 medical comparison 能力要求 same-case full panels + ROI crop/zoom + adjacent TP/FP/FN legend，031 不能在接入 production path 时降低这一语义正确性。

### Observed evidence

source-fidelity map 正确把该页绑定到 same-case `failure_input / failure_gt / failure_pred / failure_error` 资产，runtime trace 也正常选择 `GSC-008` 并走 `same_case_medical_roi_zoom` shared layout。

但 fresh pixel review 对 `slide_6_medical_image_comparison` 观察到：Error panel / Error crop 同时出现红色和橙色误差，而 Prediction panel / crop 没有让对应 prediction mask 在该病灶区域清楚可辨；结合页面 legend 的“红=FP、橙=FN”，观众无法直接从当前像素验证 prediction 与 error classification 的关系。

代码侧也确认当前 shared `emit_image_panel` 只是并排显示 source Input / GT / Prediction / Error 图片并绘制 legend，本身没有保证 GT 与 prediction mask 在 prediction view 中以足够清楚、可互相区分的方式呈现。因此这不是单纯文案问题，而是当前 page-level semantic inspectability 不足。

### Minimal repair

保持 same-case asset、ROI coordinate 和既有 gold/layout geometry；只增强 shared medical comparison 的可检查语义，使 GT、Prediction 和 Error 三者在 full panel 与 ROI zoom 中可直接对应。可以采用清楚的 prediction overlay / mask treatment、直接标注或等价的最小 shared fix，但必须保证 TP/FP/FN 颜色与 GT / prediction 的实际关系一致且投影尺度可读。

不得换病例、伪造误差、改变 source evidence，也不得只改 legend 文字掩盖像素对应关系。

修复后需要新的 task-local rendered identity 和 fresh item-level review，明确确认 error colors 可以与 GT / prediction views 无歧义对应。

## Accepted evidence preserved for round 2

以下能力本轮没有发现 blocker，第二轮只需确认没有回归：

- normal one-call file/path production surface 已建立，默认 fixture 只是回归输入，CLI 仍接受 `--input-bundle`；
- source-fidelity map 对六个 page job 都有真实 evidence anchor；
- normal compatible gold selection / recipe / Stage 3 consumption 有 runtime trace；
- 无 force-id、score override、benchmark helper orchestration；
- canonical CUHK source 被真实复制并用于 compile；
- real PDF/PNG render 与 mechanical QA 成立；
- audience-facing 页面没有 RRL/GSC/SRC、QA、provenance、workflow/repo/run-id 等内部制作元语言；
- equation、result plot、experiment design、negative result、next experiment 的当前像素除 CUHK identity 共性 blocker 外均得到正向 item-level observation；
- 031 没有声称 Stage 4 或长期 program 完成。

## Round-2 scope

只修上面两个 blocker，并重新生成 `.tex + PDF + PNG`、task-local visual manifest、真实 CI 和 fresh Visual Review evidence。不要提前实现 deck-rhythm review / bounded repair loop，也不要开始 Stage 5 holdout。
