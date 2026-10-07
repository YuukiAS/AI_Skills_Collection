---
task_key: presentations_historical_blackbox_validator_bootstrap_v1
status: READY
controller_mode: true
task_type: cross_repo_validator_bootstrap
primary_repository: YuukiAS/AI_Skills_Collection
primary_branch: work/presentation-historical-blackbox-validator-v1
fixture_repository: YuukiAS/STAT5060-TA
fixture_branch: work/stat5060--tutorial-01-v2
critic_oracle_required_before_build: false
final_validator_acceptance_allowed: false
slide_production_allowed: false
user_routine_qa_allowed: false
---

# Historical Presentation Validator Bootstrap Goal V1

## 1. 本轮唯一目标

先搭出一个**能用的历史逐页验收器**，不要等待逐页 Critic oracle。

它必须对 STAT5060 Tutorial 01 的全部主要历史失败/未接受版本执行逐页验收，并为每一页输出：

```text
PASS | REVISE
issue_classes[]
substantive_observation
evidence
applicable_historical_guards[]
```

本轮结果是可运行的 bootstrap validator 和 provisional observed verdict，不是最终 ground truth，也不授权 V14。

Critic 后续给出逐页判断后，再用它校准 false PASS / false REVISE。

## 2. 必须先读

完整读取以下 presentation workflow：

1. `plugins/codex/plugins/presentations/shared/presentation-end-to-end-pre-execution-runbook.md`
2. `plugins/codex/plugins/presentations/shared/pre-execution-cumulative-acceptance-contract.md`
3. `plugins/codex/plugins/presentations/shared/rendered-artifact-positive-ancestry-acceptance-contract.md`
4. `plugins/codex/plugins/presentations/shared/authoring-production-workflow.md`
5. `plugins/codex/plugins/presentations/shared/chatgpt-web-authoring-contract.md`
6. `plugins/codex/plugins/presentations/shared/anti-shortcut-production-contract.md`
7. `plugins/codex/plugins/presentations/shared/independent-review-contract.md`

然后读取 STAT5060 当前 authority、历史批注审计、page map、V14 page freeze、V13 rejection 和历史 corpus inventory。

开始实现前生成 read manifest。

## 3. 当前已消费的历史反馈规模

bootstrap 必须确认并使用以下 corpus：

```text
ANNOTATION_OBJECTS = 193
HIGHLIGHT_ANNOTATIONS = 187
TEXT_ANNOTATIONS = 6
DIRECT_HUMAN_DECISIONS = 20
```

其中两条历史 highlight 只有计数、缺少完整原文，必须保留为 `SOURCE_GAP_UNVERIFIABLE`，不得猜测。

主要历史 candidate corpus：

```text
MAIN_HISTORICAL_ARTIFACTS = 18
MAIN_HISTORICAL_PAGES = 629
COMPLETE_PAGE_RENDERS = 18/18
```

另有 taught baseline、component proof、golden proof，可作为补充 fixture，但不改变 629 页主分母。

## 4. 八个验收方面

只实现 Tutorial 当前真正需要的八类验收，不扩张成完整通用平台。

### A. 历史 artifact 与页面完整性

- exact PDF/render identity；
- page count、page hash、artifact map；
- 18 个主要历史 artifact、629 页全部执行；
- 缺页或无法读取必须 `REVISE/BLOCKED_EVIDENCE`，不得跳过。

### B. 课程 shell 与共享组件

- title/header/miniframe/footer/page number/navigation；
- Question/Answer rule；
- table/code/caption/closing 的共享几何；
- shared component 改坏 consumer page 时必须发现。

### C. 文字、公式、表格与代码可读性

- typography floor；
- code/table/formula 是否投影可读；
- clipping、overflow、broken glyph、curly quote、不可复制代码；
- P18 类小字密集页必须能被发现。

### D. 布局、空白、双栏和主体对象尺度

- primary object 是否过小；
- 小对象与大空白同时出现；
- sequential logic 被错误塞入双栏；
- peer columns 是否对齐、是否一边过短造成大空洞；
- title/closing/普通页面是否明显未完成。

双栏、空白、字号、对象尺度属于 validator/Codex 的普通责任，不能留给 GPT Work 或用户首次发现。

### E. 证据、结果与解释的邻接关系

- figure/table/equation 与 interpretation 是否相邻；
- code 与其 output 是否相邻；
- Question → evidence → Answer 是否完整连续；
- caption 是否偷承担正文解释；
- 页面是否完成自己的 teaching job。

### F. 正向视觉祖先与受保护对象

- diagram/plot/table/code-output composition 是否保留；
- diagram 被删后只剩 prose 必须 `REVISE`；
- generic boxes 不能冒充 mechanism diagram；
- explicit Planner retirement 才允许删除。

重点 replay：shared-`u_i`、RWM/HMC/NUTS method diagram、closing shell、Q/A composition。

### G. STAT5060 专属内容与边界

- 38 个 PageID/page job；
- count/rate/offset、GLMM、Bayesian sequence；
- 具体反馈 guard 与禁止项；
- HW1/oral-defense 可见范围；
- API/package inventory、prerequisite、内部工程语言、隐藏 rubric 等越界内容。

### H. 数值图形与验收证据完整性

- chart/trace 的 source variable、unit、scale、warmup/filter 与附近 summary；
- P26 可先输出 `REVISE_NUMERICAL_BLOCK`，不得因图片干净而 PASS；
- 只有 hash/PASS flag、没有实质观察的 page review 必须失败；
- `READY_FOR_GPT_WORK` 不得被当成 `READY_FOR_USER_REVIEW`。

## 5. 实现方式：确定性提取 + 独立 rendered review

不要试图只靠一个几何阈值解决全部问题，也不要把全部问题扔给 GPT Work。

### 5.1 确定性 page feature extractor

优先使用 PDF 自带 text/vector layer，避免 OCR：

- PyMuPDF / PDF text spans / bounding boxes；
- `pdftotext -bbox-layout`；
- page PNG occupancy、connected regions、largest object/body usage；
- repeated header/footer geometry；
- font-size distribution；
- text/table/code/figure region map；
- page image and artifact hashes。

输出统一 `page_features.jsonl`。

### 5.2 规则引擎

规则引擎接受 normalized features + applicable guards，不接受版本名作为 verdict lookup。

允许 course adapter 提供：

- artifact/page → PageID mapping；
- applicable feedback/guard IDs；
- required/protected objects；
- course-specific numeric/content contracts。

禁止：

- `if artifact == V13 and page == 18 then REVISE`；
- fixture-ID branch；
- hard-coded expected verdict；
- 所有页面统一 FAIL；
- 为通过而放宽阈值或缩小分母。

### 5.3 fresh rendered reviewer

对每一页实际 PNG 做 whole-slide review。输入仅包括：

- exact page image/hash；
- normalized page features；
- PageID/page job；
- applicable guards/mandatory objects；
- 不提供预设 PASS/REVISE 答案。

输出严格 JSON。必须有实质观察，不能只写 `PASS=true`。

### 5.4 verdict 聚合

```text
存在任何未关闭 P0/P1/P2 -> REVISE
证据缺失或 numerical block -> REVISE
全部适用检查通过且 observation 完整 -> PASS
```

每页只给一个最终 `PASS|REVISE`，同时保留 issue classes 和 scoped positive properties。

## 6. Codex / subagent 拓扑

使用一个 Parent Controller，不让用户转发中间结果。

```text
Parent Controller
├─ Producer：实现 extractor、rules、adapter、runner
├─ fresh deterministic Auditor：检查 18 artifacts / 629 pages、hash、schema、coverage、anti-hardcode
├─ fresh rendered Reviewer workers：按 artifact 分批看全部 page PNG，合并成 629/629 page rows
├─ fresh Repair Producer：修复 Auditor/Reviewer 发现的 root mechanism
└─ fresh rerun，直到 bootstrap gate 通过
```

Rendered Reviewer 可以按 artifact 分给多个 fresh read-only subagents，但：

- 每页只能有一个 canonical row；
- 所有 worker 使用同一 rubric/schema；
- aggregator 必须验证 629/629，无重复、无遗漏；
- Reviewer 不能编辑 detector、threshold 或 candidate。

## 7. Workflow 角色边界

### Codex

本轮承担：实现、render/page extraction、普通视觉规则、全 corpus 执行、自动修复、fresh audit。

双栏、空白、字号、主体尺度、表格/代码可读性、Q/A 几何、output proximity、protected object deletion 等普通问题必须在 Codex/Auditor 层关闭。

### GPT Work

本轮不作为 bootstrap validator 的日常检测器，也不承担 629 页逐页初筛。

以后仅在真正 V14 immutable candidate 通过 deterministic + rendered audit 后，承担最终 aesthetic / reader-effort / pedagogy / deck-rhythm gate。

### 用户

用户不是 routine QA，不审 629 页，不负责指出明显双栏、空白、字号和对象丢失问题。

用户以后只看：

- validator 与 Critic ground truth 的差异摘要；
- genuine semantic conflict；
- 最终已内部通过的候选。

## 8. 通用与 Tutorial 专属：本轮只做标记

不要在本轮重构完整 Presentation 插件。

对每个 detector/guard 只标记：

```text
REUSABLE_CANDIDATE
STAT5060_SPECIFIC
```

明显可复用候选包括：typography、primary-object scale、whitespace interaction、peer alignment、reading path、Q/A geometry、evidence proximity、protected-object deletion、review-evidence completeness。

PageID、feedback ID、课程数值、P26 exact contract、HW1/oral-defense 边界保持 `STAT5060_SPECIFIC`。

是否正式晋升通用插件、跨 deck calibration 和更完整 hidden mutation 留到后续工作，不阻塞本轮。

## 9. 允许路径

AI Skills：

```text
plugins/codex/plugins/presentations/shared/validator_v1/
plugins/codex/plugins/presentations/shared/validator_v1/tests_public/
docs/reviews/PRESENTATIONS_HISTORICAL_VALIDATOR_BOOTSTRAP_AUDIT_V1.md
```

STAT5060：

```text
scripts/presentation_validation/tutorial01_validator_adapter_v1/
tests/presentation_validation/tutorial01_public/
results/tutorial-01-validator-v1/bootstrap/
docs/reviews/2026-27/STAT5060_TUTORIAL_01_VALIDATOR_BOOTSTRAP_REPORT_V1.md
```

禁止修改任何 Tutorial slide/theme/figure/PDF/render、V14 authority 或历史 fixture bytes。

## 10. 必须输出

```text
corpus_manifest.json
page_features.jsonl
page_results.jsonl
artifact_summary.json
historical_guard_results.json
positive_object_results.json
numerical_results.json
review_evidence_results.json
detector_ownership.json
coverage_report.json
fresh_deterministic_audit.md
fresh_rendered_review.md
bootstrap_acceptance_report.md
```

`page_results.jsonl` 必须正好覆盖 629 个主要历史页面，每行至少包含：

```text
artifact_id
artifact_sha256
physical_page
page_png_sha256
page_id_or_unmapped
page_job
applicable_guards
observed_features
issue_classes
positive_scoped_properties
substantive_observation
verdict = PASS | REVISE
reviewer_id
```

## 11. Bootstrap 完成门槛

```text
RESULT = BOOTSTRAP_VALIDATOR_READY_FOR_CRITIC_CALIBRATION
MAIN_HISTORICAL_ARTIFACTS_EXECUTED = 18/18
MAIN_HISTORICAL_PAGES_REVIEWED = 629/629
MISSING_PAGE_ROWS = 0
DUPLICATE_PAGE_ROWS = 0
PAGE_ROWS_WITHOUT_SUBSTANTIVE_OBSERVATION = 0
OBVIOUS_V13_FAILURE_REPLAY = PASS
KNOWN_POSITIVE_OBJECT_REPLAY = PASS
GENERIC_CORE_VERSION_LOOKUP_BRANCHES = 0
USER_ROUTINE_QA_USED = NO
GPT_WORK_USED_AS_ROUTINE_QA = NO
REUSE_CLASSIFICATION_COMPLETE = YES
FINAL_CRITIC_CALIBRATION = PENDING
VALIDATOR_ACCEPTED = NO
V14_PRODUCTION_ALLOWED = NO
NEXT_ACTION = COMPARE_WITH_FRESH_CRITIC_AND_CALIBRATE
```

不允许停在“代码已写完但没有跑完整 corpus”。不允许只跑抽样页面。不允许要求用户手动检查页面。
