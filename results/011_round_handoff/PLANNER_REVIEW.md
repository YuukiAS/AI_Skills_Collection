# 011 Round Handoff — Planner Review

reviewed_commit: `4fda5c0d28fa054ee7a99187ea03bfc7d6787ea3`
current_main_control_commit: `d1ef8e90f1e2e4bad86a823974664af2d9784186`
review_round: 2
decision: BLOCKED

## 结论

当前 corpus implementation 本身没有重新打开上一轮已经关闭的两个 blocker：Inspected Page Library 的已知错页修复、inspection evidence 补全，以及基于 inspected records 的 2–5 条语义检索与 retrieval trace，仍可视为本轮已达到最低完整性门槛。机械视觉 reviewer 也继续正确停在 `NOT_ASSESSED`，没有冒充 academic visual PASS。

最新 `4fda5c0d...` 只调整视觉 packet 对 renderer/font 像素漂移的处理：默认记录 regenerated PNG 与 committed golden PNG 的 SHA 比较，而不因为 byte-level drift 自动把 CI 视为学术 PASS/FAIL。这一改动比“必须逐字节一致”更合理，也没有改变机械 QA 与学术视觉 QA 的职责边界。

但本轮仍不能 `PASS`。`c23a0586...` 起新增 `.github/workflows/research-presentation-visual-packet.yml`，后续 `f6c3b4bc...` / `4fda5c0d...` 持续完善 packet builder。该路线在技术上把“生成真实 PNG/PDF/PPTX packet”与“学术视觉判断”分开，方向本身合理，但它修改了 GitHub Actions workflow。当前 Planner 合同明确规定：在用户没有明确授权 workflow/Actions/权限类变更时，外部视觉 transport blocker 不能被路由成普通 Executor implementation。此前 Planner 把 GitHub Actions artifact 写成推荐最小方案，属于过度具体化 transport；该建议不能覆盖当前更高优先级的授权边界。

因此现在的正确结论仍是：**BLOCKED_EXTERNAL_VISUAL_ACCESS（映射到本 round 的合法 decision `BLOCKED`）**。核心实现无需继续返修；下一步需要先取得视觉 transport 授权，或提供不涉及 `.github/workflows` / Actions 权限变更、但当前 Planner 工具链确实能打开的等价 packet。

## 已关闭的实现问题保持关闭

### Inspected Page Library

上一轮已经确认 `RRL-020 / SRC-006` 从错误的第 8 页修正为实际第 17 页 `Overall objective function`，并补齐 `inspection_date` / `inspection_means`；跨 source 抽查没有发现新的同类错页阻断。当前 transport 提交没有恢复 metadata rotation、模板轮转或自动猜 page-level metadata。

### Reference retrieval

当前 regression generator 仍按 page function、evidence type、domain/subdomain、token overlap 与 source tier 从合格 inspected rows 中检索，每页选择 2–5 条 references，并在 evidence manifest 中保留 query、candidate ids、selected ids、source tiers、排序/相关性理由、组织学习点与未复制整页边界。新 transport 提交没有把链路退化回 literal `RRL-*` 硬编码。

### Mechanical / academic visual boundary

`review_research_group_meeting_regression.py` 仍只做机械 QA，输出 `MECHANICAL_VISUAL_REVIEW`，并保持 `academic_visual_decision=NOT_ASSESSED`。`build_visual_review_packet.py` 也明确只组装 transport packet，不写 academic PASS。最新 render-drift 处理只是记录 byte-level comparison，不把像素差异升级成 academic decision。这一职责边界是正确的。

## 新 transport 实现的独立审查

### Packet 设计

当前 packet 设计包含四张 regenerated rendered PNG、四张 committed golden PNG、PDF、PPTX、Evidence Manifest、Render Status、Mechanical Visual Review、packet manifest 与 SHA256；同时绑定 core implementation commit 和 transport commit，并显式写 `academic_visual_decision=NOT_ASSESSED`。

`4fda5c0d...` 将 golden comparison 改成可记录的 `golden_render_comparison`，默认不因不同 LibreOffice/font 环境导致的 byte-level drift 直接失败，只有显式 `--strict-golden-pngs` 才要求逐字节一致。这个调整避免把 renderer 差异错误升级为学术结论，技术上可以接受。

### 仍未关闭的两项证据缺口

1. 用户没有在当前合同中明确授权新增或修改 `.github/workflows/*` 来解除该 transport blocker；
2. 当前 Planner 仍没有实际取得一个可下载并打开的 Actions artifact / PNG / PDF。本轮能确认的是 workflow、packet builder、本地 packet 组装与 SHA comparison 逻辑存在；这不等于当前 Planner 已实际看到四张 rendered visual。

因此 transport implementation 不能单独关闭视觉 gate。

## Blocking Gate — 需要真实视觉访问，而不是更多 manifest

本轮仍无法诚实完成以下学术视觉验收：

- scientific object 是否在实际页面上可读；
- 对象之间的关系是否正确；
- 是否退化为 card / table / dashboard；
- 主图、公式、标签是否具有真实组会可读性；
- evidence boundary 是否清楚；
- 四页是否出现重复结构、视觉失衡或空洞装饰。

仓库中的 golden PNG 通过 GitHub connector 目前仍只能作为 binary/base64 内容取得，当前 Planner 工具链没有得到可直接交给视觉查看器的本地图像文件。仅有 PNG 数量、SHA、manifest、mechanical PASS、packet builder success 或 golden comparison 都不能替代实际看图。

## 解阻路径

当前不再给 Executor 新的普通 REVISE 任务，也不继续修改 GitHub workflow/权限配置。只有以下任一路径成立后才重新做 academic visual review：

1. 用户明确授权保留/使用 GitHub Actions artifact 作为视觉 transport，并且当前 Planner 能实际下载 artifact、打开其中 PNG/PDF；或
2. 提供不需要修改 `.github/workflows/*`、Actions/Pages 设置、OAuth/PAT scopes、Secrets、branch protection 的等价传输，例如用户直接上传 packet、或其他当前工具能真正打开的文件通道。

无论采用哪条 transport，最终 `PASS` 都必须由 Planner 实际查看四张 rendered visual，并逐页写页面特异观察后产生。若用户不授权 Actions 路线，不得要求 Codex 继续用普通 manifest、checksum、golden comparison 或更多脚本假装解除视觉不可见问题。

## Source Scout

本轮不做新的 Source Scout。当前 statistics/biostatistics candidate backlog 仍足以支撑本 round，且当前唯一未关闭门槛是视觉 transport；新增来源不会改变 decision。

视觉 gate 通过后，下一轮最高价值 coverage gap 仍是 `statistical-method group meeting`：优先做 3–6 张真正包含 estimator/formula、simulation/uncertainty、model checking 或 failure analysis 的关键页，再根据真实失败模式决定 theorem-heavy / biostatistics validation-study / PhD proposal 的优先级。

## Program maturity

当前远未达到 `PROGRAM_MATURE`。现阶段只有有限 corpus round 与四页 regression，且外部 academic visual gate 尚未通过；版本、source 数量、测试数量、packet 完整性或 mechanical QA 都不能替代至少 5–8 类真实科研任务的多轮独立 benchmark。

## 下一动作

保持本 round 的 Planner decision 为 `BLOCKED`，不要继续扩大 corpus、重做 retrieval、增加新的 workflow/权限改动，亦不要宣称 academic visual PASS。等待用户对视觉 transport 路线给出授权，或出现当前 Planner 可以真实打开的等价视觉 packet；届时只重新执行外部 academic visual review，不重复已经关闭的 core implementation 工作。
