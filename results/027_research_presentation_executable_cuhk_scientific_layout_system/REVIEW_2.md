---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 027_research_presentation_executable_cuhk_scientific_layout_system
review_round: 2
decision: REVISE
implementation_commit: 7dadb5e027013253c23025a847bae5d3e3039bd7
---

# 027 Executable CUHK Scientific Layout System — Review 2

## Decision

`REVISE`

第二轮返修已经关闭了 REVIEW_1 的一部分真实问题，但 027 仍未达到冻结的 Stage 3 visual maturity gate，因此不能 PASS。

我独立核对了真实 CI 与 fresh visual evidence。`Codex Marketplace` run `32820700167` 对 handoff commit `44ddd5b627f3325ae756603ffcef1fbca6d4cc70` 已 `completed / success`。028 随后通过真实 `workflow_dispatch` run `32923111244` 对返修后六张 PNG 运行了新的 `gpt-5.6-terra` item/page-level review；review identity `326dcf0971a8aba0a32ae9bf671167667f1ec5cd52c379fb7e9dea2e57bbff8d` 与当前 027 manifest、PDF 和六张 PNG identity 一致，不是旧证据复用。

本轮明确改善：

- `slide_2_statistical_model` 继续 `PASS`，native LaTeX 数学页保持稳定；
- `slide_5_negative_result` 从第一轮 `REVISE` 变为 `PASS`，原先确定性的文字重叠已经关闭，失败证据图与解释现在可读。

但另外四页仍有 item-level blocking findings，直接违反 027 Acceptance Gates 5 和 9。

## Blocking finding 1 — quantitative result 仍不具备投影尺度可读性

### Plan basis

冻结 Plan 要求结果/不确定性页面以主结果图为视觉中心，legend、tick、annotation、caption 在投影尺度下直接可读。

### Observed evidence

新的 `slide_3_real_data_application` 仍被 Terra 判 `REVISE`。三面板 coverage plot 虽然比上一轮获得更大区域，但轴文字、点标注、`nominal 0.95` 注释仍很小；页面上只出现一个不完整的 `G=50` key，而 red/teal 方法映射主要依赖底部 caption。

这说明第一轮“扩大容器 + 增加 native legend binding”的修复没有真正解决 figure 内部的 presentation-scale typography 与完整方法键值问题。

### Minimal next mechanism

后续 recovery 不应继续只扩大外层 bbox。应建立一个真正的 presentation-native result-figure path：对该类结果图重新生成/重排 axes、facet labels、method legend、reference line 与 callout，使图内文字尺寸直接受 Stage 3 投影尺度合同约束；若既有 raster 不能安全重排，应走可解释的 native/vector redraw 或 `SPLIT_REQUIRED`，不得继续把不可读 raster 塞入大容器。

## Blocking finding 2 — experiment design 仍然是 generic workflow fixture

### Plan basis

冻结 Plan 明确禁止 generic box-arrow；实验设计必须把真实设计因素、层级、procedures 与 endpoints 组织成科学关系图。

### Observed evidence

新的 `slide_4_experiment_design` 虽加入了 `G=8,20,50`、ICC、cluster balance、interval procedures、coverage/width/bias 等具体术语，但 fresh Terra 仍判 `REVISE`：中央对象仍是四个浅色矩形卡片加箭头，且内部存在 source-like `centers -> subjects` 表达。

问题已从“内容太泛”缩小为“可执行 primitive 仍然把具体实验语义装进通用卡片流水线”。因此继续给四个框增加文字不会满足 Stage 3 成熟度门槛。

### Minimal next mechanism

后续 recovery 应替换这类通用 relation-card primitive，使用 job-specific experimental-design primitive：例如中心/受试者层级、DGP 因素、procedure branches、evaluation endpoints 分层组织，并让连线方向由 typed scientific relations 决定。必须让听众从图形结构本身读出实验设计，而不是从卡片文字中推断。

## Blocking finding 3 — medical comparison 缺少真实可检查的 error zoom

### Plan basis

冻结 Plan 要求同病例 input / GT / prediction / error / crop/zoom 在投影尺度下可检查，医学影像本身必须是页面主体。

### Observed evidence

新的 `slide_6_medical_image_comparison` 已扩大四个 same-case panels，但 Terra 仍判 `REVISE`。真正关键的 lesion/error 仍只占很小区域，页面标为 `Error zoom` 的部分实际上是文字说明框，而不是放大的影像 crop；因此 TP/FP/FN 差异仍无法从真实 rendered page 上检查。

### Minimal next mechanism

后续 recovery 必须把 zoom/crop 从“描述字段”变成真实 image primitive：从同一病例与同一坐标系裁剪 error ROI，生成可见放大图，与原 panel 用 callout 连接，并提供邻近、可读的 TP/FP/FN legend。若病灶尺度无法满足最低 inspectable area，应触发 medical-specific split/zoom layout，而不是继续放大整组 panel。

## Blocking finding 4 — next experiment 仍是卡片化 future-work workflow

### Plan basis

冻结 Plan 要求 discussion / next-experiment 通过正常 selector 消费 Stage 2 discussion-compatible gold，并把“已有证据/限制 -> 下一验证动作 -> 判定标准”转化为具体研究推理视觉；禁止 generic cards/box-arrow。

### Observed evidence

新的 `slide_7_next_experiment` 已包含 G=8、ICC=.5、imbalance、batch strategies、CR2 / wild bootstrap、coverage/width criterion 等具体研究内容，但 fresh Terra 仍判 `REVISE`：页面依然由三个相似矩形卡片和箭头构成，研究推理没有变成 evidence-linked decision experiment。

这说明 `GSC-018` 已被正常选中并消费，但当前 Stage 3 primitive 仍没有把 gold 的 next-experiment composition lesson落实为成熟页面结构。

### Minimal next mechanism

后续 recovery 应采用专门的 evidence-to-decision layout：明确显示当前失败证据、待操纵因素/选择策略、并列 comparator arms、预期诊断量和最终 decision criterion；这些对象之间的关系必须由 typed relations / quantitative endpoints 驱动，而不是继续复用通用卡片箭头组件。

## Accepted evidence that must be preserved

以下能力已通过，不应在后续 recovery 中重做或降低：

- exact CUHK canonical Beamer identity 与真实 compile/render；
- normal Stage 2 selector -> gold recipe -> CUHK resolver -> emitted TeX 链路；
- source-derived geometry mutation 会改变 resolved/emitted geometry；
- capacity mismatch 的 `SPLIT_REQUIRED` 合同，无 generic fallback；
- `slide_2_statistical_model` native LaTeX 页面；
- `slide_5_negative_result` 当前通过的 negative-evidence layout；
- audience-facing output 无 RRL/gold/QA/provenance 元语言；
- required tests、validation 与真实 CI 已通过。

## Review-limit conclusion

027 已使用两轮独立 review，不能开启第三轮。当前 blocker 已被 fresh rendered-pixel evidence 明确定位，而且存在唯一、质量保持、范围清楚的新实现机制：保留已通过的 Stage 3 基础能力，只为 result figure、experiment design、medical error zoom、next-experiment 四类未成熟 job 建立更专用的 executable primitives，并用新的真实像素验证。

因此 027 本身应保留 `REVIEW_LIMIT / REVISE` 历史；按照 Program Goal 的 Quality-Preserving Continuation Policy，Planner 应另建一个 bounded Stage 3 recovery task，而不是降低 mature bar、伪造 REVIEW_3 或要求用户在“继续保持质量”和“降低质量”之间重复选择。
