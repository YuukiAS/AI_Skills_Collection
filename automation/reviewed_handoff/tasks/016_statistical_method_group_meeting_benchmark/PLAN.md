---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 016_statistical_method_group_meeting_benchmark
decision: PLAN_FROZEN
---

# 016 Statistical / Biostatistical Method Group Meeting Benchmark — Revised Plan

## Revision context

这是本任务唯一一次 scheduled re-plan。第一轮实现已经证明科学故事、确定性 simulation、真实 PPTX 渲染、CI 和基础 visual-review transport 可以工作，但用户对真实 rendered slides 的检查暴露出更根本的质量问题：当前页面虽然“对象齐全”，仍明显像自动生成的 benchmark fixture / wireframe，而不像成熟统计方法组会成品。

因此，本次 revision **不改变科学问题、DGP、simulation 数值或方法比较**，但明确撤销 REVIEW_1 中对 slide 2–5 的“视觉 accepted-element lock”。旧 Terra 对 slide 2–5 的 PASS 只能证明当时 rubric 下的局部语义完整，不能证明页面达到成熟学术汇报质量。本轮允许在保持科学内容与证据不变的前提下重构全部 5 页的 audience-facing 实现。

本任务的完成标准不是“测试 fixture 通过”，而是：**五页均达到可以直接投影给统计/生统导师、PI 或顶会研究听众的成熟组会水平，视觉完成度至少不低于成熟 oral / invited research talk，同时保留组会需要的技术深度。**

## Frozen decisions

### Frozen scientific story — unchanged

使用完全 synthetic、固定随机种子的多中心连续结局模拟。科学故事保持不变：中心内相关可能让点估计看起来稳定，但把个体当作独立观测会使区间覆盖率失真；center-cluster-robust inference 修复大部分问题，但 small-G / high-ICC / imbalance 条件仍出现覆盖不足。

DGP 保持：

\[
Y_{ij}=\beta_0+\beta_1T_{ij}+u_j+\varepsilon_{ij},
\qquad
u_j\sim N(0,\tau^2),
\qquad
\varepsilon_{ij}\sim N(0,\sigma^2),
\]

\[
\rho=\frac{\tau^2}{\tau^2+\sigma^2}.
\]

目标 estimand 仍为 treatment effect \(\beta_1\)。比较至少：

- naive iid OLS interval；
- center-cluster-robust interval。

Simulation grid 保持现有真实 deterministic output：seed `20260822`、每个 cell `400` replicates、`G=[8,20,50]`、`rho=[0,0.1,0.3,0.5]`、balanced / imbalanced cluster-size stress。主要 endpoint 仍为 95% interval coverage，辅助 endpoint 为 bias 与 interval width。不得为了视觉效果改写已有数值或制造新的结果。

## External quality baseline

本 revision 将以下公开专业规范作为**视觉成熟度基线**，不是要求机械套模板：

1. MIT EECS / NSE Communication Lab：每页只承担一个 message；标题应帮助听众抓住 takeaway；只保留支持该 message 的内容；visuals 优先于大段文字；简化 figure、提高 signal-to-noise、用 annotation 引导视线、保证后排可读。
   - `https://mitcommlab.mit.edu/eecs/commkit/slideshow/`
   - `https://mitcommlab.mit.edu/nse/commkit/slide-design/`
   - `https://mitcommlab.mit.edu/eecs/commkit/figure-design/`
2. NeurIPS talk accessibility guidance：minimal text、large fonts、high contrast，不依赖装饰性文本效果；短报告强调 simple / visual / accessible。这里只借其视觉可读性标准，不削弱统计组会的技术深度。
   - `https://neurips.cc/Conferences/2026/MainTrackHandbook`
3. CVPR 的公开展示建议强调 little text、few large expressive figures。这里只作为“主视觉对象必须足够大”的下限参考，不把 statistical group meeting 做成 poster。
4. MICCAI oral guidance 的 16:9、真实会场投影和约 1 slide/minute 节奏将继续作为后续 medical-imaging benchmark 的会场尺度参考；016 仍保持 16:9。

## Inspected-reference design contract

016 继续使用现有 inspected-page library，不需要为本次 revision 扩 source corpus。当前 library 已包含足以约束 016 的高价值统计页面；本轮必须真正吸收其 page-level lesson，而不是把 reference IDs 打印到 slide 上。

Planner 本轮明确认可的代表性 lesson 包括：

- `RRL-028`（Gelman, MRP talk, estimator）：估计量公式本身可作为页面主对象；当一个公式定义后续叙事时，页面可以很稀疏，不需要再用三张卡片包围它。
- `RRL-030` / `RRL-033`（Gelman interval / applied uncertainty pages）：主图占据页面大部分面积，估计值与区间直接一起显示；不确定性是图的一部分，而不是正文解释。
- `RRL-023`（Gelman Bayesian Workflow）：区间图可同时表达排序与不确定性，图形本身承担结论。
- `RRL-025`（Gelman Bayesian Workflow negative result）：失败/修正可以作为正常科学结果，保持同一证据结构直接比较，而不是转成“failure card + takeaway card”。
- `RRL-026`（Gelman Bayesian Workflow simulation）：生成机制与实际模拟输出应一起出现；simulation 不是装饰性流程图。
- `RRL-009`（CMU proposal estimator）：只有当输入、限制、操作与输出本身构成真实方法机制时才使用 diagram。
- `RRL-044`（Gelman Bayesian inference）：公式、推断目标与检查对象应分清层级，不使用互相误导的方向箭头。

每页仍需按 page function + statistics/biostatistics domain + evidence type 语义检索 2–5 个 inspected reference pages。允许因本次 revision **在现有 inspected corpus 内重新排序/重新选择 IDs**，因为旧选择没有充分转化为设计质量；不允许硬编码固定 IDs 代替检索。

新增内部 `reference_design_audit`（可以是独立 JSON，也可以是 EVIDENCE_MANIFEST 的明确字段），每页至少记录：

- selected reference IDs；
- `visual_dominance`、`equation_usage`、figure/text ratio 等已检查的 page-level 特征；
- 2–4 条真正采用的 design lesson；
- 哪些 source-specific style 明确没有复制；
- 当前 slide 如何体现这些 lesson。

这些内容仅供 evidence / Planner / Terra 使用，**不得出现在 audience-facing slide**。

## Audience-facing hard gates

以下任一项存在时，016 不得进入最终 PASS：

1. 核心数学仍以源码式 ASCII 显示，例如 `beta_1`、`epsilon_ij`、`rho`、`sum_g`、`(X'X)^(-1)`、`X'X` 等，而不是正常的数学符号、上下标、希腊字母、转置和求和排版。
2. audience-facing slide 出现内部制作/QA/provenance 语言，例如：`RRL-`、`Reference retrieval`、`EVIDENCE_MANIFEST`、repo/path/run ID、`Diagram contract`、`style not copied`、`Reading target`、`Observed in this synthetic run`、`evidence boundary` 作为 QA 标签、implementation/review 字段等。
3. 页面退化为明显 AI / consulting 模板：title + pastel cards / boxes + slogan / summary strip；大量圆角框代替公式、图、实验对象；元语言解释“这一页该怎么看”。
4. 主 scientific object 太小、被框架和空白吞掉，或页面大片空白但公式/图仍缩在局部。
5. 视觉仍像 wireframe / placeholder：矩形和箭头只是“能表达”，但字体、对齐、线宽、颜色、层级、caption、annotation 明显不到可直接组会使用的完成度。
6. 文案出现机械的 AI 元标签或抽象套话，而不是自然的学术标题、方法说明、figure annotation 与结论。
7. result figure / formula / table 在投影尺度不可读，或图没有直接支撑标题中的主要 scientific claim。

必要的 synthetic 限定仍必须保留，但应自然写成 subtitle、caption 或 footnote，例如 `Synthetic multi-center simulation` / `Simulation study`，不能写成内部 QA 术语 `evidence boundary`。

## Mathematical typesetting contract

统计/理论页的核心公式必须真正 typeset/render。Generator 中保留 LaTeX/source formula 作为可审计来源；PPTX 中应使用当前环境可靠的高质量数学渲染路径：优先矢量 math asset / native equation；若当前 PPTX 工具链无法可靠插入矢量公式，可使用高分辨率透明 math render，但必须在真实 `PPTX -> presentation engine -> PDF -> PNG` 链路中保持清晰、无锯齿感、基线和字号与正文协调。

不允许逐字符手工拼“伪公式”，也不允许把 LaTeX / Python / ASCII source 直接当 slide text。公式 asset 的 source expression、输出文件和 slide 使用关系必须可追溯。

## Five-slide revised page contracts

### Slide 1 — STATISTICAL_MODEL

任务：让听众在一页内理解 estimand、组内相关来源，以及“点估计没有明显偏差”为什么不等于区间推断正确。

必须：

- 真正 typeset 的 DGP 主公式成为页面核心对象；
- \(\beta_1\)、\(u_j\)、\(\varepsilon_{ij}\)、\(\rho\) 在公式邻域自然 grounding；
- 明确 center 是相关性/推断单元；
- `u_j` 与 `epsilon_ij` 不得使用串行生成箭头；它们是不同层级的 additive components；
- synthetic context 用自然 subtitle/caption 表达；
- 视觉组织以公式 + 少量直接 annotation 为主，禁止三张定义卡替代模型。

标题应是自然的统计学 message 或问题，不得包含内部 page-function / contract 语言。

### Slide 2 — ESTIMATOR / DERIVATION

任务：让听众直接看到 naive iid variance 与 cluster-robust sandwich covariance 的差别在哪里。

核心公式必须真正排版，例如：

\[
\widehat V_{\mathrm{CR}}
=
(X^\top X)^{-1}
\left(
\sum_g X_g^\top \hat u_g\hat u_g^\top X_g
\right)
(X^\top X)^{-1}.
\]

设计约束：

- 公式是绝对主 scientific object，优先参考 `RRL-028` 的 formula-dominant lesson；
- 对 middle “meat” term 做直接 annotation / brace / concise label，解释为何按 center 聚合；
- naive variance comparator 只作为紧凑 secondary element；
- 不再使用三块 pastel card 作为默认布局；
- 不出现 `Reference retrieval` footer、源码式公式或 QA 说明。

### Slide 3 — SIMULATION_DESIGN

任务：用约 5 秒可以读懂的实验结构说明 DGP knobs、replicates、interval methods 与 endpoints 如何连接。

必须可见：`G`、`rho`、cluster-size imbalance、400 replicates、两种 interval、coverage / bias / width。

若 diagram 仍是最佳表达：

- 单一 left-to-right 阅读方向；
- 只保留真实 scientific nodes / operations；
- connectors 有可见 arrowhead、无 crossing、peer alignment 清楚；
- 不出现 `Diagram contract` 或“如何阅读本图”的 QA 元文字；
- box 数量和颜色压到最低，不得像 UI / workflow dashboard。

若一个简洁 design matrix + 两个 method columns + endpoint block 比 flow diagram 更成熟，允许改用该结构；不要为了“必须画图”保留低质量框图。

### Slide 4 — RESULT_FIGURE

任务：主结果图直接回答 coverage 在哪里失败，以及 cluster-robust interval 修复了多少。

必须：

- 沿用当前 deterministic simulation 真值；
- coverage plot 成为页面绝对视觉中心，参考 `RRL-030` / `RRL-033` 的 plot-dominant lesson；
- nominal 0.95 reference 一眼可见；
- Monte Carlo uncertainty 直接编码在图中；
- 方法 legend 尽量直接靠近数据；
- 用 1–2 个直接 annotation 标出关键 stress regime；
- 删除 `Reading target`、`Observed in this synthetic run` 等元标签；
- synthetic simulation 限定自然地落在 subtitle/caption/footnote。

标题必须由实际数据支持，不能写成泛化定理。

### Slide 5 — NEGATIVE_RESULT + NEXT_EXPERIMENT

任务：把 small-G / high-ICC / imbalance 下仍存在的 undercoverage 作为真正的科学负结果，并定义下一项有区分力的实验。

必须：

- quantitative negative evidence 是视觉中心，优先复用与主结果一致的数据/图形语法；
- 关键失败点直接 annotation；
- failure mechanism 用极短自然语言解释；
- planned CR2 / wild-cluster-bootstrap comparison 作为 secondary next-experiment 区域，清楚标为计划而非完成证据；
- 不做“negative result card + failure mechanism card + next experiment card”的三卡布局；
- 参考 `RRL-025`：失败页应让 evidence 本身说明问题，而不是用漂亮 summary 掩盖失败。

## Language contract

English audience-facing slide text 必须通过现有 `scientific-prose` handoff / 等价 writing-fidelity 流程做最终措辞。Generator 不得临时生成大段 academic-sounding meta prose。

重点清除：

- `target / contract / observed / key change / reading target` 等制作元词反复出现；
- “This slide ... / Role in the deck ... / Reference retrieval ...” 等内部说明；
- slogan / consulting-style takeaway；
- 机械重复同一 sentence pattern。

标题可使用自然的 claim title、直接 scientific question 或 concise technical title；不要求所有页机械写成完整句，但标题必须帮助听众理解这一页真正的学术动作。

## Deterministic QA revision

在调用 Terra 之前，016 必须新增或强化可维护的 deterministic gate。优先做 **016-specific / Presentation benchmark helper**，不要因为本任务直接大改 active shared skill。

### Audience-facing internal leak gate

对 audience-facing slide text，至少以下高置信模式出现即 FAIL：

- `RRL-`
- `Reference retrieval`
- `EVIDENCE_MANIFEST`
- `Diagram contract`
- `style not copied`
- `Reading target`
- `Observed in this synthetic run`
- 明显 repo / result / run / implementation provenance

只检查 audience-facing objects，不误伤 notes、EVIDENCE_MANIFEST、retrieval trace、source code。

### Math-source leak gate

对 slide 1 / 2 的公式区域，必须验证最终 PPTX/render 所依据的 audience-facing content 不再使用明显 source-like string 充当公式。至少覆盖当前已出现的高风险模式：`beta_`、`epsilon_`、`sum_`、`^(-1)`、`X'X`、ASCII-only `rho = ...`。

不要机械禁止所有下划线；检查应限定在 mathematical page / formula region 或预期核心公式对象。QA 必须同时确认存在对应的 rendered math object / asset，而不只是删除字符串。

### Regression scope

至少新增测试保证：

- 五页无上述 audience-facing internal leakage；
- slide 1 / 2 核心公式使用真实 math render source，不是 ASCII formula box；
- slide 1 不存在 `u_j -> epsilon_ij` 串行 edge；
- slide 3 不出现 QA/meta labels；
- slide 4/5 的结果数据仍与原 simulation summary 一致；
- reference IDs 仍完整存在于 internal evidence，但不进入 rendered slide text。

## Terra rubric revision

本次新 visual identity 的 `gpt-5.6-terra` consumer-specific rubric 必须比首轮更严格。修改 `tests/fixtures/presentations/statistical_method_group_meeting/build_ai_bridge_visual_inputs.py` 或等价 016 adapter；**不要修改 Bridge Kit 通用 core**。

Terra 至少逐页检查：

1. scientific correctness：公式、DGP、interval method、结果解释、uncertainty、planned work 是否正确；
2. mathematical typesetting：是否仍有 ASCII/source-like math；核心公式是否投影可读并且视觉上像真正数学；
3. audience-facing language：是否泄漏 RRL/QA/provenance/制作元语言；是否有明显 AI 套话；
4. scientific hierarchy：公式、结果图、simulation evidence、negative evidence 是否真正成为视觉中心；
5. visual maturity：是否仍像 pastel cards、dashboard、wireframe、自动生成草图；字体、对齐、颜色、留白、caption、annotation 是否达到 mature research talk 水平；
6. reference-informed quality：rubric 中不仅提供 reference IDs，还提供本轮 `reference_design_audit` 的 page-specific lessons，并要求判断当前页是否真正体现这些 lesson；
7. projection readability：主内容能否在真实组会/会议投影尺度快速读懂。

Rubric 必须显式要求回答：

> Would this slide look professionally finished if projected in a strong PI's research group meeting or a top-conference oral talk?

但不能把这句话当唯一标准；仍必须给出 page-specific evidence 和最小修复理由。

Terra 仍然只是独立视觉证据，不是最终 Reviewer。新 identity 正常调用一次，不为追求 PASS 重刷。

## Implementation scope

允许修改：

- `tests/fixtures/presentations/statistical_method_group_meeting/` 下 generator、016-specific reviewer/QA、visual-input adapter；
- 016 的 editable PPTX、PDF、rendered PNG、expected render、evidence manifest、render status、mechanical review、simulation evidence；
- `tests/test_presentations.py` 中与上述成熟度 gate 直接相关的 regression；
- `results/016_statistical_method_group_meeting_benchmark/RESULT.md` 与新的 visual-review artifacts；
- 内部 `reference_design_audit` artifact / manifest fields。

若为了真正 typeset math 需要一个**仅服务当前 presentation fixture、边界清楚的最小 math-render helper**，允许新增在该 fixture 或现有 shared presentation script 的低风险位置；不得借机重构整个 Presentation plugin。

## Required validation and handoff

Executor 完成后必须：

1. 重新生成整套真实 editable PPTX；
2. 通过真实 presentation engine 生成 PDF / PNG；
3. 运行 revised deterministic / mechanical QA；
4. 逐页人工/程序查看真实 PNG，确认不再是旧 wireframe；
5. 生成新的 `visual_inputs.json` 和新的 visual identity；
6. 对该新 identity 只运行一次 `gpt-5.6-terra` review；
7. 运行：
   - `python -m unittest tests.test_presentations`
   - `python -m unittest discover -s tests`
   - `python scripts/skills.py validate`
   - `python scripts/build_codex_marketplace.py --validate --check --path-report`
   - Reviewed Handoff repository-wide validation
   - `git diff --check`
8. 写 RESULT、push implementation/handoff，进入真实 CI；CI bridge 发布 current-tip `reviewed-handoff/ci-summary`。

## Acceptance and regression gates

第二轮 Reviewer 只有在以下全部成立时才可 PASS：

1. 真实 GitHub CI PASS；
2. scientific story、DGP、simulation、数值和 negative-result claim 与原 deterministic evidence 一致；
3. 五页均达到成熟 statistical/biostatistical group meeting 的专业完成度，不像测试 fixture / dashboard / wireframe；
4. slide 1 / 2 核心数学真正 typeset/render，投影尺度清楚，无 source-like ASCII math；
5. audience-facing 页面没有 RRL / reference retrieval / QA / provenance / repo 元语言；
6. 语言自然，内部制作标签和明显 AI 模板措辞已经清除；
7. 每页只有一个清楚的学术动作，scientific object 是视觉中心；
8. slide 3 若使用 diagram，方向清楚、无 crossing、没有 decorative/meta flow；
9. slide 4 result figure 是绝对主视觉，0.95 target、method comparison、Monte Carlo uncertainty 与关键 stress annotation 清楚；
10. slide 5 用真实 quantitative failure evidence 承担主要叙事，next experiment 明确为 planned；
11. 每页 2–5 个 inspected reference retrieval 仍可审计，并有 `reference_design_audit` 证明实际吸收 page-level lesson；
12. Terra rubric 已升级并对新 identity 正常运行一次；Terra PASS 不是充分条件，Planner 必须独立检查真实 rendered pixels 与 reference-informed design；
13. 不提前开始 medical-imaging benchmark，不扩与 016 无关的 source corpus，不借机大规模重构 active Presentation rules。

若第二轮仍明显低于成熟组会标准，即使 Terra 给 PASS，也必须 `REVISE` 并按两轮上限进入 human gate；不得为了避免 human gate 降低标准。

## Out of scope

- 改变现有 DGP、simulation grid、seed、方法比较或已验证数值，除非发现真实统计 correctness bug；
- medical-imaging Phase C benchmark；
- 与当前 page archetype 无关的大规模新 source acquisition；
- Bridge Kit 通用 core 修改；
- 发布新 Presentation plugin 版本；
- 真实临床数据或私有 patient image；
- 把本 synthetic benchmark 当作一般统计定理或真实临床结论。
