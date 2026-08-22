---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 015_presentation_terra_blocker_repair
decision: PLAN_FROZEN
---

# 015 Presentation Terra Blocker Repair — Plan

## Objective and value

在 Phase A 已关闭的前提下，只修当前 canonical `gpt-5.6-terra` 对四页 research-group-meeting regression 给出的三个具体 blocker，并把“定向返修不得破坏已接受内容”的规则真正落实到 generator、真实 render 和回归证据中。目标不是重做四页或继续扩规则，而是证明现有 active contract 能约束生成器把已知视觉问题关闭。

## Frozen decisions

1. 当前 canonical visual evidence 固定读取 `results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json`。当前 identity 下：slide 1、2、3 为 `REVISE`，slide 4 为 `PASS`；该 evidence 在新 PNG identity 产生后自动成为历史证据，不得直接改写其旧结论。
2. 本任务只修三个 blocker：
   - **slide 1 / RESULT_FIGURE**：`burden error` 是 error endpoint，必须明确 favorable direction 为“越低越好”；保留当前 synthetic 数值，不为了让某一方法继续“赢”而篡改数据。解释文字必须改为与实际 bar ordering 一致：`Calibrated` 可继续按真实数据描述 recall 表现，但 burden-error winner 必须由现有数值的最小值决定；图上应直接标明 `lower is better` 或等价向下方向语义。
   - **slide 2 / FAILURE_CASE**：保持同一 synthetic case、GT、prediction、FP/FN overlay 和现有 metrics/counts 不变，只重分配页面面积，使 image / GT / prediction / overlay 成为真正可投影检查的视觉中心。不得通过放大外框、缩小文字或更换病例来规避问题。
   - **slide 3 / EXPERIMENT_DESIGN**：沿用现有“local-only comparator”科学语义，把它从 footer/prose 提升为真实 diagram branch；global estimator 与 local-only comparator 两个比较输出都必须通过结构连接线进入同一个 endpoint-evaluation / success gate。不得发明新的 comparator、endpoint 或额外实验阶段。
3. **slide 4 是 accepted element**：不得修改其科学内容、布局、公式、evidence-boundary 文案或视觉对象。若现有生成链允许，应保持 slide 4 rendered PNG byte-identical；如果仅因 deck-level metadata/render nondeterminism 无法字节一致，Executor 必须证明 slide 4 的 PPTX object/text/geometry 未被本任务修改，并在 RESULT 中解释差异来源。
4. 除上述三个直接修复及其必要局部依赖外，不允许全局重排 deck、改标题风格、改主题/配色、换参考来源、改 slide 4、删除已接受元素或重新设计其它页面。
5. Phase A 已经把 metric favorable direction、medical evidence area、complete comparator path、revision scope、diagram semantics 等通用规则放入 active contract。本任务不得再新增第二套同义规则；只允许补充能防止这三个 generator regression 复发的最小 deterministic test。
6. reference retrieval、2–5 inspected pages、selected reference IDs/reasons、source tiers、evidence boundary、synthetic/public-safe 标记必须继续保留。不得扩 Source Registry、Inspected Page Library、Synthesized Knowledge 或下载新 deck。
7. Terra Visual Review 必须使用 Bridge Kit 当前默认 `gpt-5.6-terra`。每个新的 visual identity 只允许一次正常 live review；不得为了追求 PASS 对同一 identity 重跑。

## Implementation scope

允许修改：

- `tests/fixtures/presentations/research_group_meeting/generate_research_group_meeting_regression.py` 中与 slide 1–3 直接相关的生成逻辑；
- 与该 fixture 直接相关、为真实 render/mechanical review/visual packet 更新所必需的现有脚本；
- `tests/test_presentations.py` 中最小、语义明确的 regression assertions；
- 由现有真实生成链重新产生的 regression artifacts，例如 PPTX、PDF、rendered PNG、expected render、evidence/render/mechanical manifests 与 visual-review packet source；
- `results/012_presentation_visual_adapter/visual_review/visual_inputs.json`，但只能由现有 adapter 基于新真实 PNG identity 重新生成，不得手工伪造 SHA；
- 本任务的 `results/015_presentation_terra_blocker_repair/RESULT.md`；
- 若 existing generated/plugin mirror 因本任务真实 source change 必须同步，可使用现有生成器更新，但本任务原则上不改 active skill 文本。

Executor 执行顺序：

1. 同步最新 main，读取本 PLAN、当前 `VISUAL_REVIEW.json`、`visual_inputs.json`、mechanical evidence、generator、reviewer、packet builder 与相关 tests。
2. 建立 accepted-element ledger：slide 4 全部接受；slide 1 只允许 metric-direction / interpretation 局部修复；slide 2 只允许 case visual area/layout 修复；slide 3 只允许 comparator branch / endpoint connectivity 局部修复。
3. 实现三个最小 generator repair，不改 synthetic scientific data 和 source retrieval。
4. 增加最小 deterministic regression：至少验证 slide 1 生成文本明确 lower-is-better 且 claim 不再声称错误的 burden winner；slide 3 生成内容存在显式 local-only comparator 与 endpoint-evaluation 语义。不要用脆弱的整页像素阈值代替最终视觉判断。slide 2 的“是否足够大”主要由真实 render + Terra 判断，可在不制造任意阈值的前提下检查图片对象没有退回旧的小 inset 几何。
5. 运行真实生成与渲染链：editable PPTX -> real presentation engine -> PDF/PNG；更新 expected render / visual-review packet source 和 mechanical evidence。不得另画 parallel PDF。
6. 重新运行现有 AI Bridge visual-input adapter，使 `visual_inputs.json` 的四个 PNG SHA、PPTX/PDF/render/mechanical bindings 与新 artifacts 一致。
7. 运行本地验证，至少包括：
   - `python -m unittest tests.test_presentations`
   - `python -m unittest discover -s tests`
   - `python scripts/skills.py validate`
   - `python scripts/build_codex_marketplace.py --validate --check --path-report`
   - `python -m ai_bridge_kit.bridge_cli reviewed-handoff validate --target /home/yuukias/AI_Skills_Collection`（使用当前可用 Bridge Kit 环境）
   - `git diff --check`
8. 写 `RESULT.md`，清楚记录三个 blocker 如何修、slide 4 如何保持、旧/新 PNG identity、local/mechanical validation，以及 Phase C 尚未开始。
9. push 实现和 handoff，进入 `WAITING_FOR_CI`。本地 CI bridge 必须把 required GitHub Actions 聚合为 current-tip `reviewed-handoff/ci-summary`。
10. 对新 visual identity，只在确认没有已经成功调用同一 identity 的 Terra run 后，手动 dispatch 一次 `.github/workflows/ai-bridge-visual-review.yml`，参数固定为：
   - manifest=`results/012_presentation_visual_adapter/visual_review/visual_inputs.json`
   - output=`results/012_presentation_visual_adapter/visual_review/VISUAL_REVIEW.json`
   等待 bot 写回新的 tracked evidence。不得第二次调用同一 identity。
11. CI bridge 的 success 只有在 Plan-required conventional CI 与本次 Terra run 都完成且没有 transport failure 后才能发布。Terra 的学术决定即使是 `REVISE`，也不等于 transport CI failure；学术 PASS/REVISE 由 Scheduled Planner读取新 `VISUAL_REVIEW.json` 后决定。

## Acceptance and regression gates

只有以下全部成立，本 task 才可 PASS：

1. 真实 GitHub conventional CI 全部通过；Presentation/Marketplace tests、generation/validation、skills validation/audit 实际执行。
2. 新 visual-input manifest 与当前真实 PPTX/PDF/PNG/mechanical evidence identity 完整匹配；四张 PNG SHA 均来自新的真实 render。
3. slide 1：图上明确 burden error 的 favorable direction，interpretation 与实际 synthetic bar ordering 一致，不再出现“error 最大却被称为 winner”的矛盾；不篡改原 synthetic 数值来迁就 claim。
4. slide 2：同一 case 的 image / GT / prediction / FP-FN overlay 在投影尺度上成为主要视觉对象，metrics 与错误区域可读；不得仍是 oversized panel 中的小 central inset。
5. slide 3：diagram 中显式存在 local-only comparator；global estimator 与 local-only comparator 都通过真实 structural connector 抵达 endpoint evaluation / success gate，形成完整比较路径。
6. slide 4：保持 accepted scientific content 与 layout，不因本 task 被重新设计；若 PNG 非 byte-identical，必须有可审计的非内容原因说明。
7. reference IDs/retrieval trace、synthetic evidence boundary、source tiers 与现有 page contracts 保持正确；无 source/corpus expansion。
8. 新 identity 的 `VISUAL_REVIEW.json` 必须由一次 `gpt-5.6-terra` live review 产生，image SHA 与 manifest 一致，Structured Output 合法。Planner 独立核对三个旧 blocker是否关闭，并检查没有因返修产生新的 blocking regression。
9. Terra 若仍对 slide 1–3 中任一旧 blocker给出有证据支持的 `REVISE`，本 task 不得 PASS；第一轮只给最小 repair。Terra 若提出完全超出冻结范围的新“偏好型”意见，Planner只能作 non-blocking note，不能借机扩大 task。
10. 不进入 Phase C，不新增 statistical/biostatistical 或 medical-imaging benchmark，不做 Source Scout，不修改长期 Program 架构。

## Natural-language usage / routing expectations

本任务不新增用户调用入口。它验证的是：当用户或独立视觉审阅明确指出“结果解释与图不一致”“医学图太小”“实验设计缺 comparator path”时，Presentation 系统能做局部、可回归的修复，而不会把整个 deck 重新设计或破坏已经通过的页面。

## Review behavior

Reviewer 必须独立读取 frozen PLAN、真实 implementation diff、conventional CI、机械 render evidence、新旧 manifest identity 与新的 Terra `VISUAL_REVIEW.json`。不得只相信 Executor 的 RESULT，也不得因为 Terra transport 成功就自动 PASS。

第一轮若仍有冻结 blocker，写最小 `REVISE` 并只允许对应局部 repair；第二轮仍不能关闭则进入 human gate。若出现需要改变 synthetic scientific data、page contract、隐私策略、source corpus 或 benchmark 方向的选择，不得自行扩大 PLAN。

## Out of scope

- 不扩 source corpus / inspected page library / synthesized knowledge；
- 不做 Source Scout；
- 不新增 active presentation rule 的同义副本；
- 不启动统计/生统或医学影像新 benchmark；
- 不重构 Presentation plugin / marketplace / profile 架构；
- 不改 Bridge Kit Visual Review 默认模型或 secret contract；
- 不将 slide 4 当作可自由重做页面；
- 不为了 Terra PASS 对同一 visual identity 重复调用 API。
