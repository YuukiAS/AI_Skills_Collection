---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 031_research_presentation_one_call_production_entry
review_round: 2
decision: REVISE
implementation_commit: 11509b5e2bf7959433f1616c1d4ad77f77f4000e
---

# 031 One-Call Production Entry — Review 2

## Decision

`REVISE`

第二轮确认第一轮两个 blocker 已经真实关闭，但 fresh production render 暴露出一个仍属于冻结 Plan 的 deck-coherence blocker，因此 031 不能 PASS。

真实 CI 对 repair handoff `47c8330a0893dcb4b4886a0ee227ab57ebf646ca` 的 `Codex Marketplace` run `33124952035` 已完成且 `conclusion=success`。当前 task-local Visual Review 绑定 implementation `11509b5e2bf7959433f1616c1d4ad77f77f4000e` 与六张当前 PNG identity，不是旧 evidence。

## 第一轮两个 blocker 已关闭

### 1. canonical CUHK identity 已在真实像素中恢复

第一轮要求 source-side canonical provenance 与最终 rendered pixels 一致。当前共享 CUHK theme 的 headline 使用 canonical `assets/logo_RGB`，不是 031 专用文字贴片；fresh Terra 对六个主要内容页均明确观察到 CUHK crest / purple navigation identity 可见。

因此 `R-CUHK-IDENTITY` blocker 关闭。当前 exact-CUHK title/navigation/frame/footline/content geometry 没有发现相关回归。

### 2. 医学影像 GT / Prediction / Error 语义已经可检查

repair 使用同一病例、同一 ROI 和已有 error asset 派生 shared semantic display overlays：GT view 显示 overlap / missed-GT，Prediction view 显示 overlap / prediction-only，Error view 同时显示 TP/FP/FN；full panels 和 ROI zoom 使用同一 coordinate space。

fresh Terra 对医学页明确确认 Input / GT / Prediction / Error、ROI zoom、TP/FP/FN legend 与 matching error-region callout 在页内语义一致，因此第一轮的 image-semantic-inspectability blocker 关闭。

## Blocking finding — production storyline 把两个独立 workstream 串成一条没有桥接的故事

### Plan basis

冻结 Plan 要求：

- one-call path 必须 derive coherent research storyline and explicit page jobs；
- task-local Visual Review 必须判断 generated deck 是否像 one coherent research update，而不是 disconnected benchmark pages；
- 031 Acceptance Gate 3 要求 storyline/page jobs 由 production path 生成，而不是机械照搬固定顺序。

### Observed evidence

当前 source bundle 本身包含两个 engineering workstream：

1. clustered interval calibration：model、coverage result、simulation design、negative evidence、next experiment；
2. synthetic segmentation robustness：same-case medical image comparison。

source 并没有声明 segmentation error 是 clustered interval coverage failure 的因果组成部分，因此 Planner 不能为了“连起来”而虚构科学关系。

当前 `deck_plan.json` 和生成 `main.tex` 的实际顺序却是：

`Model -> Results -> Experiment Design -> Negative Result -> Medical Image -> Next Experiment`

也就是在 small-G coverage failure 后突然插入 segmentation page，然后又回到 coverage 的 next experiment。生成 TeX 也真实使用 `\section{Medical Image}` 后立刻回到 `\section{Next}`，没有 agenda、workstream label、transition frame 或 audience-facing bridge。

fresh Terra 因此只对 `slide_6_medical_image_comparison` 给出 `REVISE`：该页内部医学语义已经通过，但放在整套 deck 中看起来像无关 benchmark page；Slides 2–5 和 7 都围绕 clustered interval coverage，Slide 6 没有可见解释其在研究更新中的角色。

这不是单纯采样波动。独立检查 source、deck plan 和实际 TeX 后，Planner 同意这个 deck-level blocker。

### Why blocking

031 的目标不是证明“六类页面都能分别渲染”，Stage 3 已经证明过这一点；031 要证明普通 production entry 会把输入材料组织成一套连贯 research update。如果 normal one-call route 把两个独立 workstream 机械按 source section 次序串接，产品仍可能稳定地产生“每页都不错、整套却像 benchmark 拼盘”的 deck，直接违反 Stage 4 production contract。

### Minimal quality-preserving repair

031 已达到两轮 review 上限，因此不得创建 `REVIEW_3`。后续应由新的 bounded recovery task 只修 production storyline / workstream grouping：

- 从 source/deck-plan evidence 派生 workstream grouping，不 hardcode 本 fixture 的页号或标题；
- 对彼此没有 source-supported scientific relation 的 workstream，不虚构因果桥；
- 将同一 workstream 的 page jobs 保持连续，并通过 canonical CUHK section/transition cue 明确切换到第二 workstream；
- 对当前 fixture，clustered-coverage sequence 应保持 `Model -> Results -> Experiment Design -> Negative Result -> Next Experiment` 连续，segmentation page 作为明确标识的第二 workstream，而不是插在 failure 与 next experiment 中间；
- 保留当前已通过的 CUHK identity、六类 page layout、medical overlay semantics、gold selection、source-fidelity map 与 runtime trace；
- fresh deck-level/page-level visual evidence 必须确认医学页不再像无关 benchmark 插页。

这个 recovery 不应顺便实现完整 Stage 4 bounded automatic repair loop；完整 deck-rhythm / bounded repair loop 仍是后续独立 Stage 4 task。

## Accepted evidence preserved

以下能力第二轮继续接受：

- normal file/path one-call production surface；
- source-fidelity/evidence map；
- normal compatibility-driven gold selector / recipe / Stage 3 consumption；
- no force-id / score override / benchmark-helper orchestration；
- canonical exact-CUHK source copy/compile/render；
- six content pages 的 page-level scientific-object quality（医学页内部语义也已通过）；
- audience-facing anti-meta leakage；
- engineering fixture 明确排除 Stage 5 holdout；
- 031 没有声称 Stage 4 或 program 完成。

031 因第二轮仍存在冻结 Plan blocker，必须按 review limit 保留 terminal history；依据 Program Goal 的 Quality-Preserving Continuation Policy，应自动创建一个新的、范围严格限定的 storyline-coherence recovery，而不是降低 deck coherence bar 或要求用户做本不需要的产品选择。
