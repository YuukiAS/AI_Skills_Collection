---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 038_research_presentation_two_real_paper_holdouts
review_round: 2
decision: REVISE
implementation_commit: be001f2d29a308a4cadeb9b841fcc9cfe239ea3b
---

# GPT Review

## Decision

REVISE。

038 的第二轮没有关闭第一轮真实 holdout blocker，因此本 task 到达两轮 review 上限。这里不需要也不允许第三轮：Executor 按冻结 Plan 只把 Round-1 item-level Terra finding 交给已经 shipped 的 bounded quality loop；真实 quality-loop state 对 statistics 与 medical 两套 deck 都记录 `repair_cycle_count=0`、`selected_repair_directives=[]`、`repair_allowed=false`，并以 `unsupported repair intent: <missing>` fail closed。也就是说没有任何 repair 被实际选择或应用，最终 `main.tex`、render-input identity、rendered-pixel identity 与 Round-1 Terra 所审像素保持不变。

当前真实 GitHub CI 已通过：包含 `CURRENT.state=WAITING_FOR_CI` 的 main control commit `ab9c12c74274ddb8f2e976937bdffd22179179e5` 上，`Codex Marketplace` run `33245235906` conclusion 为 `success`。CI green 只证明工程检查通过，不能覆盖仍与最终像素 identity 精确匹配的 Terra blocker。

由于没有产生新像素，不应为了形式再请求一份内容相同的 fresh Terra。Round-1 保存的 task-local Terra evidence 仍精确绑定 statistics rendered-pixel identity `43b45471...`、medical rendered-pixel identity `21e4c10f...` 与两个未变化 contact sheet；其中两个 contact sheet 的 item-level decision 均为 `BLOCKED`，且分别明确判断未达到 mature doctoral group-meeting / strong paper-talk bar。故第二轮只能维持 REVISE。

## Blocking findings

### 1. 现有 bounded quality loop 无法消费真实 Terra blocker，且未产生任何输出变化

**Plan / regression boundary**

038 只允许 Stage 4 已 shipped 的一次 bounded automatic repair；不能手工 patch、改 frozen source bundle、改 production code 或在同一 holdout 上新增规则。若 mapping 无法安全处理 finding，Plan 明确要求 fail closed 并保留该 holdout 失败历史。

**Observed evidence**

- `statistics/generated/quality_loop_state.json`：`deck_level_decision=UNSAFE_REPAIR_MAPPING`、`repair_cycle_count=0`、`selected_repair_directives=[]`、`final_decision=QUALITY_LOOP_FAIL_NO_WINNER`，原因是 `unsupported repair intent: <missing>`。
- `medical/generated/quality_loop_state.json` 同样为 `UNSAFE_REPAIR_MAPPING / QUALITY_LOOP_FAIL_NO_WINNER`，repair count 为 0。
- 独立读取 shared `deck_quality_loop.py` 确认 `map_finding_to_directive()` 当前只接受 finding 自带的 `repair_intent` / `intent`；Terra 的真实 blocking findings 提供 requirement、summary、evidence、recommendation，但没有该字段，因此 consumer 会机械 fail closed。
- 独立代码搜索还确认 `primary_object_scale_hint` 与 `legend_repair_hint` 当前只在 quality-loop consumer 内写入，仓库没有其他生产消费者；因此即使未来只补 intent 字段，也必须证明 repair directive 实际改变 layout/render，而不能只让 state 从 fail-closed 变成“已选择”。

**Minimal quality-preserving recovery**

不得在 038 内继续修。后续新的 bounded recovery 应只修正常 production quality loop 的通用 consumer/execution gap：在现有 task-local Visual Review contract 内，把 item-level requirement/finding 安全归一到有限 repair family，并让这些 repair directives 对实际 audience pixels 产生可验证影响；未知/歧义 finding 继续 fail closed。必须使用与 brms/MedSAM 无关的非-holdout regression，不得把 038 两篇论文或其像素变成调优 fixture。

**Required closure evidence for the recovery**

- unrelated non-holdout fixtures 覆盖：内部 audience-copy 泄漏、figure/caption overlap、undersized table/primary object、next-step/process diagram collision、medical legend/image obstruction；
- 每类 finding 在允许范围内映射到明确 repair intent，且 repair 前后 render-input / pixel identity 发生与预期一致的变化；
- source claims、真实 medical pixels、CUHK identity 与一轮 repair budget保持；unknown/unsafe finding 仍 no-winner；
- fresh task-local Terra 对 non-holdout recovery pages/contact sheet 达到既有 mature bar；
- shared skill 与 marketplace mirror parity + real CI PASS。

### 2. 两个 Stage-5 holdout 的最终像素仍保持 Round-1 的七个 blocking findings

**Observed evidence**

Statistics：

- 最终 `main.tex` 仍真实包含 audience-facing `rather than importing the Stage 4 clustered-calibration fixture.`；
- Terra BF-02/BF-03/BF-04 对 workflow footer overlap、package comparison table 不可读、closing decision diagram 多处碰撞均未发生任何 repair；
- statistics contact sheet item-level `BLOCKED`，明确未达到成熟博士组会 paper-talk bar。

Medical：

- 最终 `main.tex` 仍把 architecture citation 与 takeaway 放在同一底部坐标；
- limitations/decision layout 仍使用造成碰撞的 comparator/diamond/text arrangement；
- same-case CT comparison 仍把 `Overlay legend` 放入 lower MedSAM crop 区域，且 connector 穿过该区域；
- medical contact sheet item-level `BLOCKED`，明确未达到成熟博士组会 paper-talk bar。

**Disposition**

两篇论文已经完成一次真实 unseen evaluation 并暴露 blocker，因此从现在起都永久失去 Stage-5 “未见 holdout”资格。038 不能在这些论文上继续修改后再宣称 unseen PASS。后续 generic recovery 完成后，statistics/methodology 与 medical-imaging 两个 domain 都必须选择新的、预生成前未参与 exemplar/rule/tuning 的真实公开 paper 重新做 one-shot。

## Non-blocking notes

- 038 仍提供了有价值的正向证据：两篇论文都完成公开 source/license audit、source bundle freeze-before-render、正常 production entry、exact-CUHK 编译和真实图像/表格使用；MedSAM deck 确实使用论文许可覆盖的真实 medical-image pixels。
- 当前失败不是“CI 没跑”或“Terra package 不可评估”，而是成熟度 blocker 与 quality-loop consumer/execution gap。继续使用同一 holdout 做修复会污染最终泛化测试，因此必须隔离到新的非-holdout recovery。
- 本 task 的 `AWAIT_HUMAN_DECISION / REVIEW_LIMIT` 只用于保留 Reviewed Handoff 两轮上限历史；Program Goal 的 Quality-Preserving Continuation Policy 已给出唯一机械恢复路线，因此不构成需要用户产品选择的真实人工门。
