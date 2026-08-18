# 011 Round Handoff — Planner Review

reviewed_commit: `2c54c52f287be94c5919bc5886fb52804f94fc49`
current_main_control_commit: `ee6719ba397cb060b47b01a9308bfeb06061f48d`
review_round: 2
decision: BLOCKED

## 结论

上一轮两个可由 Executor 修复的完整性问题已经基本关闭：Inspected Page Library 不再包含已知的 `RRL-020` 错页记录，并补齐了 inspection date / means；四页 regression 也已经从 literal `RRL-*` 列表改成基于 inspected index 的可审计检索，并为每页留下 query、candidate、selected ids、source tier、相关性理由和未复制整页的边界。

当前 round 仍不能 `PASS`，但这次原因不再是 corpus implementation。唯一剩余硬门槛是 **external academic visual review 仍无法在当前 Planner 运行环境中真正看到四张 rendered PNG**。长期合同明确禁止只凭 PNG 数量、manifest、expected object contract 或机械 QA 判学术视觉通过；因此本轮必须 `BLOCKED`，不能用 `MECHANICAL_PASS` 替代。

## 上一轮 Blocker 1 closure — Inspected Page Library

### 实现证据

当前 `research_slide_reference_index.csv` 的 inspected rows 已包含：真实 source URL、实际页码、scientific object、页面特异观察、rights note、source/rendered-page SHA256、`inspection_date` 和 `inspection_means`。已知错误记录 `RRL-020 / SRC-006` 已从错误的第 8 页修正为第 17 页 `Overall objective function`，scientific object 也改为 PET-Disentangler overall objective function。

### Planner 独立抽查

本轮没有只采用 Executor 自报结果，而是重新核公开原 deck：

- `RRL-020 / SRC-006 / actual_page_number=17`：SFU 公开 ISBI 2025 PDF 对应页明确写出 critic 单独优化、critic loss，以及 encoder / segmentation decoder / image decoder 的 overall objective，和当前 record 对应。
- `RRL-003 / SRC-001 / actual_page_number=13`：MIT AeroAstro 公开 committee PDF 实际页面以 training-step reward curve 为主对象，并显示 global/local information baselines 与 InforMARL，和当前 `RESULT_FIGURE` 记录对应。
- `RRL-028 / SRC-054 / actual_page_number=14`：Gelman CDC talk 对应页面是 `The poststratification identity`，核心对象为单独呈现的 estimator/identity 公式，和当前 record 对应。

这三个跨 source 抽样没有再发现上一轮那种“页码存在但页面对象完全不对应”的错误。当前显式 `INSPECTED_PAGE_SPECS` 也没有恢复 metadata rotation、模板轮转或自动猜 `page_function/page_number` 的旧实现。

因此上一轮 Blocker 1 关闭。这里的结论只代表当前抽样未发现新的完整性阻断，不代表 48 条记录被逐条重新人工复审。

## 上一轮 Blocker 2 closure — Reference retrieval 已进入生成链

当前 regression generator 已存在独立 `REFERENCE_QUERIES` 和 `retrieve_references()`：

- 只从 `verification_status=inspected` 且具有 source/rendered hash、inspection date/means 的 rows 中检索；
- 按 page function、evidence type、domain/subdomain、token overlap 与 source tier 评分；
- 每个 archetype 从候选中选择 2–5 条 inspected references；
- 每页 manifest 记录 query、candidate ids、selected ids、source tiers、ranking/relevance reason、organization lesson 与 `what_was_not_copied`；
- 测试明确禁止退化回上一轮 literal RRL 列表，并检查 selected ids 与 retrieval trace 一致。

这已经达到当前 round 要求的“简单、可审计、真正使用 inspected corpus”的最低门槛。它不需要在本轮升级成向量检索或更复杂的推荐系统。

因此上一轮 Blocker 2 关闭。

## Mechanical reviewer boundary — 通过

当前 `review_research_group_meeting_regression.py` 的职责已经正确收窄：

- 只检查真实 PPTX render 链、PNG 数量/尺寸、非空、基本对比度、对象合同等机械信号；
- 输出类型为 `MECHANICAL_VISUAL_REVIEW`；
- `academic_visual_decision` 固定为 `NOT_ASSESSED`；
- 不生成 `SCIENTIFIC_VISUAL_REVIEW.json`；
- 不再把 manifest 中存在 expected scientific objects 直接扩写成十项 academic PASS。

这一边界符合长期合同。

## Blocking Gate — 当前 Planner 无法实际查看四张 rendered PNG

当前仓库确实提交了四张 golden PNG：

- `tests/fixtures/presentations/research_group_meeting/expected_render/slide-1.png`
- `slide-2.png`
- `slide-3.png`
- `slide-4.png`

GitHub connector 能定位这些 binary blobs，也能以 base64 形式返回文件内容；但本次 Planner 运行环境没有可将 connector 返回的 binary/base64 无损落到本地图像文件并交给视觉查看器的可用通道。公开 GitHub raw URL 在当前网页读取链路中也返回 cache miss，因此本轮没有真正看到四张 regression PNG。

这意味着我无法诚实完成以下学术视觉验收：

- scientific object 是否真的可读；
- object relationship 是否正确；
- 是否退化为 card / table / dashboard；
- 主图、公式、标签是否具有组会可读性；
- evidence boundary 是否在实际页面上清楚；
- 四页是否存在结构重复、空洞装饰或视觉失衡。

按照 Program 合同，**未实际查看 rendered PNG 就不得写 academic visual PASS**。因此当前 round 状态必须是 `BLOCKED`。

### 最小解阻条件

下一次外部 Planner review 必须获得一个真正可由当前工具链下载并打开的视觉 review packet，且必须绑定 implementation commit `2c54c52f287be94c5919bc5886fb52804f94fc49` 或其后续只改变 review transport 的等价提交。推荐最小方案是让 Codex/仓库提供一个 connector 可下载的 GitHub Actions artifact（ZIP 内含四张 rendered PNG、对应 PDF/PPTX locator、`EVIDENCE_MANIFEST.json` 和 render status），或其他能在 Planner 环境中落成实际 PNG/PDF 文件的等价通道。

这只是 evidence transport，不得由脚本代替学术判断。即使 packet 完整，最终 decision 仍必须由外部 Planner 实际看图后逐页写页面特异观察。

## Source Scout

本轮不新增 Source Scout。当前 round 的 statistics/biostatistics candidate backlog 已被当前合同判定为足够，且上一轮至今没有形成新的 acquisition gap；继续搜索新来源不会解除当前视觉 review blocker。

如果视觉 gate 后续通过，下一轮最高价值 benchmark 仍是 `statistical-method group meeting`，优先 3–6 张关键页，覆盖 estimator/formula、simulation/uncertainty、model checking 或 failure analysis，再根据实际失败决定 theorem-heavy / biostatistics validation-study / PhD proposal 的顺序。

## Program maturity

当前远未满足 `PROGRAM_MATURE`：现阶段仍只有有限 corpus round 与四页 regression，且外部 academic visual gate 尚未完成。版本、测试数量、source 数量或 mechanical QA 均不能替代多类真实 benchmark 的连续稳定证据。

## 下一动作

当前 task 不再要求扩大 corpus，也不要求重新设计 retrieval。先解决 external Planner 对 rendered visual evidence 的可访问性；在真正看完四张 PNG 之前，本 round 保持 `BLOCKED`，不得发布 academic visual PASS 或宣称 program mature。
