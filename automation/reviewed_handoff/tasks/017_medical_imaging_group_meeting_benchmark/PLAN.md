---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 017_medical_imaging_group_meeting_benchmark
decision: PLAN_FROZEN
---

# 017 Medical-Imaging Research Group Meeting Benchmark — Plan

## Objective and value

建立一个真正像成熟医学影像研究组会、而不是“医学影像主题模板”的 5 页 benchmark。核心故事固定为：**在多中心/多外观条件下，一个 segmentation predictor 的平均 overlap 指标可以看起来尚可，但小病灶或高 shift 条件下的 lesion-level failure 仍会被平均 Dice 掩盖；成熟汇报必须把图像、GT/prediction、定量 endpoint、失败机制与下一验证实验连成同一条证据链。**

本任务不是为了提出新的医学影像算法，而是检验 Presentation 系统能否把医学影像科研对象以成熟顶会 oral / 强 PI 组会水准表达出来。页面必须以真实生成的 synthetic image、mask、overlay、定量结果和实验设计为中心，不能退化成 cards/dashboard/wireframe。

## Frozen decisions

### Frozen benchmark story

使用完全 synthetic、固定随机种子的 short-axis cardiac-MR-like lesion-segmentation benchmark，不使用真实或私有 patient image，也不宣称临床验证。

Deterministic generator 至少产生：

- 3 个 synthetic center / acquisition-style condition；
- 每个 center 一组 cardiac-MR-like 2D slices，含 myocardium-like anatomy 与 lesion-like target；
- center-specific appearance shift，例如 contrast / noise / intensity-bias 的可解释组合；
- GT lesion mask；
- deterministic predicted mask，允许随 center shift 与 lesion size 出现不同程度的 miss / FP；
- 至少一个明确 small-lesion / high-shift failure regime。

比较重点不是虚构新算法优势，而是验证 endpoint semantics。主要 endpoint 至少包含：

- Dice 或等价 overlap metric；
- lesion-level recall / detection sensitivity；
- 一个与 lesion burden / false-positive burden 相关的可解释辅助 endpoint。

所有数值必须从同一批 synthetic image / GT / prediction 实际计算，不能手工填入结果图或 failure case。若实际 deterministic 结果不支持预设的“平均 Dice 掩盖 small-lesion failure”，则按真实结果重写 claim，不得强造负结果。

Synthetic 限定必须以自然学术语言出现，例如 `Synthetic cardiac-MR-like phantoms; not clinical validation`，不得写成 `evidence boundary`、`review contract` 等内部 QA 术语。

### Dependency boundary

为避免再次出现 CI/test dependency contract 漏项，本 benchmark 首轮实现优先只使用仓库 CI 已声明可用的 Python 依赖：stdlib、Pillow、python-pptx、matplotlib。若 Executor 认为必须引入新的第三方包，先路由 `NEEDS_GPT_PLANNER`，不得直接把新 import 留给干净 runner 再逐个补包。

## 五页页面合同

### Slide 1 — MEDICAL_IMAGE_COMPARISON / “What is the imaging task?”

页面只完成一个任务：让听众立即看清**图像是什么、目标结构/病灶是什么、预测对象是什么、评价单位是什么**。

必须可见：

- 一张足够大的 synthetic short-axis cardiac-MR-like slice；
- 直接 anatomy / lesion annotation；
- GT lesion mask 与 prediction / overlay 的清楚关系；
- modality / slice context 的自然说明；
- 当前任务的主要 endpoint 名称；
- natural synthetic-only qualifier。

图像必须是视觉中心。不要用三张定义卡解释 `image / GT / prediction`；annotation 应直接落在图像或紧邻区域。不得让装饰框、彩色背景或大段 prose 比图像更抢眼。

### Slide 2 — EXPERIMENT_DESIGN / “How is the multi-center stress test constructed?”

页面解释 synthetic center shift、预测、endpoint 计算之间的实验链。

必须可见：

- center / acquisition-style conditions；
- appearance-shift knobs；
- synthetic image + GT 生成；
- prediction 产生逻辑；
- endpoint evaluation；
- case-level 与 center-level aggregation 的关系。

若使用 diagram：

- 单一 left-to-right 或 top-to-bottom 阅读方向；
- connector 必须表示真实数据流或计算关系；
- 可见 arrowhead；
- 不允许 edge crossing；
- 不得写 `Diagram contract`、`Reading target` 等制作语言；
- 不得把每个节点做成默认 pastel card。

如果一条 compact schematic + 一个示例 slice 比多个 box 更清楚，优先前者。

### Slide 3 — RESULT_FIGURE / “Where does the aggregate metric hide the failure?”

这是主定量结果页。必须由 deterministic benchmark 的真实 summary 生成图，而不是手工绘制示意值。

必须同时让听众看懂：

- center / shift condition；
- Dice 或 overlap；
- lesion-level recall；
- 辅助 burden endpoint；
- uncertainty 或跨-case variation；
- 哪个 condition 产生 endpoint disagreement。

主图必须占页面主导面积。优先使用能直接比较 endpoint disagreement 的成熟 figure grammar，例如 aligned dot/interval plots、small multiples 或紧凑的 paired panels；不要默认三张 pastel metric cards。

标题/annotation 必须由真实结果驱动。若 average Dice 尚可但 lesion recall 明显恶化，直接在图上标出，而不是另做“Key takeaway”卡片。

### Slide 4 — FAILURE_CASE / “What does the failure actually look like?”

使用同一个真实 synthetic case 的 aligned panels，至少包含：

- input image；
- GT；
- prediction；
- error overlay。

Overlay 必须有直接、可读的颜色语义 legend，例如 TP / FP / FN；颜色不要求固定，但必须可解释且在投影尺度清楚。

必须同时显示该 case 的关键定量 metric，并与图像中的实际错误相互对应。若 failure 是 missed small lesion，应在图像上直接 annotation；不要只写一句“small lesion missed”。

所有 panel 必须来自同一 case / 同一 slice geometry；不得为了排版拼接不同病例。图像 crop 应足够大，避免主体只是小 inset。

### Slide 5 — NEGATIVE_RESULT / VALIDATION_DECISION / “What should we validate next?”

只聚焦一个由本 benchmark 实际数据支持的负结果，例如：

- small lesion size strata 下 lesion recall 明显下降；或
- high-shift center 的 Dice 与 lesion-level endpoint 分歧；或
- FP burden 在某 center 变差。

页面必须由真实 quantitative evidence 主导，并明确：

- failure regime；
- 当前证据支持的最小机制解释；
- 为什么单一平均 Dice 不够；
- 下一步真正有区分力的 validation experiment，例如 lesion-size stratification、center-held-out stress、threshold / calibration sensitivity。

下一实验必须标记为 planned / proposed，不得伪装成 completed evidence。不要把页面做成“失败机制 / next step / takeaway”三张卡。

## Reference retrieval contract

当前 inspected corpus 对医学影像 benchmark 已足够，首轮不扩 source corpus、不做 Source Scout。

优先使用现有真实 inspected medical-imaging research pages，包括但不限于：

- `RRL-013`：representative lesion samples，先让 image unit 成为视觉中心；
- `RRL-014`：metric formula 与实际 masks 并置；
- `RRL-015`：uncertainty 与 observed distribution 同页；
- `RRL-016` / `RRL-017`：clinical/subgroup question 与 quantitative result 对齐；
- `RRL-018`：保留 scientifically useful failing baseline / negative comparator；
- `RRL-019`：先连接 imaging task、data 和 downstream application；
- `RRL-020`：loss / model object 与组件关系清楚；
- `RRL-021`：result endpoint / subgroup structure 明确；
- `RRL-022`：same-case input / GT / prediction / reconstruction aligned panels。

每页仍必须根据 page function + medical-imaging domain + evidence type 语义检索 2–5 个 inspected pages，并保存 query、candidate IDs、selected IDs、ranking/relevance reason 与 source tier；上面的 RRL 只是当前已检查的高相关 anchor，不得在 generator 中硬编码成固定答案。

每页还必须生成内部 `reference_design_audit`：记录 selected reference pages 的主 scientific object、图文比例、annotation/legend 习惯、可借鉴 lesson、当前页实际采用的设计决策以及明确不复制的 source-specific styling。该 audit 只能存在 evidence/notes，不得进入 audience-facing slide。

只有当实际 semantic retrieval 证明某个冻结 page function 没有至少两个可用的 inspected reference pages，才允许路由 Planner 考虑 targeted quality scout；首轮 Executor 不得自行扩 corpus。

## Implementation scope

允许新增/修改：

- 新 benchmark fixture，例如 `tests/fixtures/presentations/medical_imaging_group_meeting/`；
- deterministic synthetic cardiac-MR-like image / mask / prediction generator；
- editable PPTX generator；
- PDF / PNG real-render evidence；
- `EVIDENCE_MANIFEST.json`、`RENDER_STATUS.json`、`MECHANICAL_VISUAL_REVIEW.json`、case/metric summary、`reference_design_audit.json`；
- 017 专用 AI Bridge visual-input adapter 与 `results/017_medical_imaging_group_meeting_benchmark/visual_review/visual_inputs.json`；
- 与本 benchmark 直接相关的 deterministic tests；
- `results/017_medical_imaging_group_meeting_benchmark/RESULT.md`；
- Bridge Kit 写回的 `VISUAL_REVIEW.json`。

不得在首轮实现里大规模重写 active Presentation skill / visual QA / archetype contract。若 017 独立审核暴露出真正缺失的通用规则，由 Planner 决定最小 re-plan 或后续 bounded task。

## Implementation requirements

1. 所有 synthetic image、GT、prediction、overlay 与 quantitative metric 必须由同一 deterministic pipeline 生成并可追溯。
2. 生成器必须输出真实 editable PPTX，不得另画 parallel PDF 冒充 render。
3. 真实链路固定为 editable PPTX -> presentation engine -> PDF -> PNG；真实 renderer 缺失时必须明确 BLOCKED。
4. Mechanical reviewer 只能做 render/clipping/object consistency 等机械结论，不得冒充 academic visual PASS。
5. 每页 one-slide-one-job；image / result figure / failure evidence / experiment diagram 按科学层级分配面积，不机械追求三栏对称。
6. audience-facing 页面不得出现 RRL ID、retrieval trace、repo path、run ID、`Reference retrieval`、`Diagram contract`、`style not copied`、`Reading target`、`Evidence boundary` 等内部元语言。
7. 英文 slide text 必须使用自然科研表达；避免 `Key takeaway`、`Observed in this synthetic run`、`Role in the deck` 等 AI/制作元标签。
8. 影像页必须有直接 annotation / legend；若显示 GT/prediction/overlay，听众无需猜颜色或 panel 语义。
9. result page 的 metric favorable direction / target semantics 必须清楚；不能暗示所有指标都是“越高越好”。
10. 不使用 clinical language 夸大 synthetic phantom；不得写成 patient validation、clinical deployment 或真实 multi-center study。
11. 当前 benchmark 新增 Python import 必须属于已声明 CI 依赖；若需要额外第三方依赖，先停止并请求 Planner。

## Deterministic tests

至少验证：

- 5 页 page function 与 frozen story 对应；
- synthetic case / mask / prediction / metrics 由同一固定 seed pipeline 产生；
- slide 1 存在足够大的 image scientific object、modality/slice context、GT/prediction/endpoint grounding；
- slide 2 diagram 若存在，connector/arrowhead metadata、单一方向与 peer alignment 合法；
- slide 3 的 plotted numbers 与 case/center metric summary 一致，并存在 uncertainty / variation encoding；
- slide 4 四个 panel 来自同一 case，overlay legend 明确，case metrics 从同一 GT/prediction 计算；
- slide 5 negative-result claim 与实际 stratified/center summary 一致，planned validation 没被写成 completed evidence；
- 每页有 2–5 个 inspected reference retrieval trace 和内部 reference-design audit；
- audience-facing slide text 不含内部 ID / QA / provenance 泄漏；
- 不出现明显 source-like math / code string 作为核心 audience object；
- source/generated/plugin 不因本 benchmark 发生无关漂移。

测试不得用单一像素阈值替代最终视觉判断，但可以机械检查 panel count、同-case identity、caption/legend text、shape/connector metadata、render status 与 evidence hashes。

## Local validation and CI

Executor 至少运行：

- `python -m unittest tests.test_presentations`
- `python -m unittest discover -s tests`
- `python scripts/skills.py validate`
- `python scripts/build_codex_marketplace.py --validate --check --path-report`
- Reviewed Handoff repository-wide validation
- `git diff --check`

实现完成后写 RESULT 并发布 handoff，进入 `WAITING_FOR_CI`。本地 CI bridge 必须对 current branch tip 发布 `reviewed-handoff/ci-summary`。

## Terra visual review

Conventional CI 与真实 render 准备完成后，为 017 自己的 visual-input manifest 正常 dispatch 一次 Bridge Kit visual review：

```text
manifest=results/017_medical_imaging_group_meeting_benchmark/visual_review/visual_inputs.json
output=results/017_medical_imaging_group_meeting_benchmark/visual_review/VISUAL_REVIEW.json
```

默认模型为 `gpt-5.6-terra`，不创建 repo-level model override。

017 consumer-specific rubric 必须逐页检查：

- actual image pixels，而不是 metadata / object count；
- image / GT / prediction / overlay 是否足够大且同-case 对齐；
- modality / anatomy / lesion / endpoint 是否自然 grounding；
- overlay legend / direct annotation 是否投影可读；
- result figure 是否真正由定量 evidence 主导，uncertainty / endpoint semantics 是否清楚；
- failure case 是否能从像素直接看出失败机制；
- planned validation 与 completed evidence 是否区分；
- 是否出现 internal QA/provenance/meta language；
- 是否退化成 pastel cards、dashboard、wireframe 或装饰性医疗 UI；
- reference-informed design 是否真正吸收 mature medical-imaging slide 的组织经验；
- 最终明确回答：`Would this slide look professionally finished if projected in a strong medical-imaging PI's group meeting or a MICCAI/RSNA-style research talk?`

Terra 是视觉证据，不是最终 Reviewer。即使 Terra PASS，Planner 仍需独立核对 frozen Plan、真实 render、reference design audit 与 scientific evidence。

## Acceptance and regression gates

本 task 只有以下全部成立才可 PASS：

1. 真实 GitHub CI PASS；
2. synthetic image / mask / prediction / metrics 均来自 deterministic pipeline，claim 可追溯；
3. 五页形成一条连贯 medical-imaging research story，不是五种模板拼盘；
4. image / GT / prediction / overlay 在投影尺度可 inspect，panel 语义和 legend 清楚；
5. experiment design 在约 5 秒内读出 center shift -> prediction -> endpoint 的主路径，若画 diagram 则无 crossing 且方向明确；
6. 主 result figure 是页面视觉中心，endpoint disagreement、uncertainty 与 synthetic scope 清楚；
7. failure-case 页能直接从图像像素看出错误区域，并与 case metric 对应；
8. negative-result / validation-decision 页由真实 evidence 主导，planned experiment 不冒充完成结果；
9. 每页有 2–5 个真实 inspected reference retrieval trace 和内部 reference-design audit，且 reference IDs 不进入 audience slide；
10. real editable PPTX render + mechanical QA 合法；
11. 新 identity 只进行正常的一次 `gpt-5.6-terra` review，Planner 独立判断成熟科研汇报质量；
12. 不扩 source corpus、不做 Source Scout、不发布新 plugin 版本、不使用私有 patient image。

若第一轮审核发现冻结范围内可局部修复的 blocker，只给最小 REVISE；第二轮仍不能关闭则进入 human gate，不得第三轮自动返修。

## Out of scope

- 真实 patient / hospital / private clinical data；
- 新医学影像算法研究结论；
- source corpus expansion / Source Scout；
- active Presentation rule 大规模重写；
- 发布新 Presentation plugin 版本；
- 将 synthetic cardiac-MR-like benchmark 表述为真实 clinical validation；
- 长期 `PROGRAM_MATURE` 宣告。
