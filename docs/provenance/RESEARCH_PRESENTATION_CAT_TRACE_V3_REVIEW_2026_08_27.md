# CAT-TRACE v3 组会 PPT 批注记录 — 2026-08-27

本文记录用户对 CAT-TRACE group-meeting deck **v3**（29 页）的 Acrobat 批注。它先忠实保存本轮不满意点，再为下一轮逐页讨论提供依据；不在这里直接改 CAT-TRACE 科学内容。

## 1. 批注概况

- PDF：`CAT_TRACE_v3.pdf`
- 页数：29
- Highlight comments：51
- 黄色：27
- 橙色：21
- 深橙色：3
- 用户明确约定：**本轮所有橙色/深橙色批注都必须转化为可复用规则，并在后续科研 PPT 中持续应用。**
- 黄色主要记录当前页具体内容、解释、科学叙事或局部样式问题；其中部分也可能在第二轮确认后上升为通用规则。

## 2. 逐页批注整理

### P1

- 无批注。title page 当前没有新增问题。

### P2 — Expanding response space in biodiversity surveys

- [橙色/必须形成规则] 图中 `known catalogue taxa` 与 `catalogue-external` 仍然文字重叠。上一轮已经明确禁止 overlay，本轮仍发生。
- [黄色] `as new samples arrive` 表达生硬，用户更倾向自然科研口语，例如 `as we collect more samples`。
- [深橙/必须形成规则] 在 TRACE 尚未介绍时直接写 `CAT-TRACE separates ...`，叙事顺序错误。新方法不能早于其动机、基线或必要背景出现。
- [黄色] `Malagasy arthropod` 对统计学听众没有解释：arthropod 是什么，Malagasy/Madagascar 是哪里。
- [黄色] OTU 在下一页才定义，却在本页先使用，违反 first-use rule。
- [黄色] `182,402 OTUs occur in exactly one sample` 只报数字，没有说清这说明 extreme rare tail / singleton pressure 为什么重要。
- [黄色] `external catalogue` 也没有先解释 catalogue 在现实中是什么。

### P3 — From field sample to response column

- [黄色] OTU 与 species 的关系仍然不够直白。需要通过几个具体 case 解释：OTU 可对应已命名 species、只能到 genus/family、完全 anonymous、多个 OTU 可能对应同一 biological species 等实际情况，而不是一句抽象总结。

### P4 — Two types of future discovery

- [深橙/必须形成规则] 首行居中公式 `Delta` 在此前没有充分定义，也没有先说为什么我们关心这个 estimand。核心公式放在视觉中心前，必须先完成语义和动机铺垫。
- [黄色] `Example` 的视觉层级和 `Catalogue discovery` 几乎一样大；example 应明显低于所在小标题层级。

### P5

- 无批注。上一轮 TRACE challenge 结构本页没有新增问题。

### P6 — TRACE mechanism

- [黄色] `tau_p` 与 `mu_p` 属于同一 calibration 机制，应在结构上更靠近，不能隔很远让听众自行拼接。
- [黄色] 一个公式高亮但无 comment；结合上下文应继续检查公式间顺序与对齐。
- [橙色/必须形成规则] `as p grows` 被机械塞进 `lim` 两次，数学英语和 LaTeX 排版都不自然。极限条件应使用标准数学记法和统一位置，不允许把口语短语硬插入公式。

### P7 — HMSC

- [黄色] HMSC 首次引入时是否也应沿用统一 terminology style，需要统一决定。
- [黄色] phylogeny 对统计听众仍然没有解释：现实对象是什么、通常如何得到、HMSC 中有什么稳定例子、当前数据哪些能/不能得到可靠 phylogeny；最好配一个具体值/对象例子。
- [黄色] `Its response space is the observed species matrix.` 表达不自然、意思也不够直观。

### P8 — CORAL

- [黄色] CORAL 首次引入也应考虑统一 terminology style。
- [橙色/必须形成规则] `beta_r | Y_common ≈ N(m'_r,S'_r)` 只扔公式，不解释 `m'_r` / `S'_r` 是什么、从哪里来、如何用于 rare species。新公式中的核心新参数必须在同页解释。
- [黄色] `Boundary` 段的位置生硬；如果是结论，应放在方法解释之后形成自然收束，而不是像任务合同标签。

### P9 — CAT-TRACE: finite catalogue and open tail

- [橙色/必须形成规则] 两栏文字/公式整体太小，页面大量纵向空间闲置。科研 slide 不允许核心模型缩小而大面积留白。
- [橙色/必须形成规则] 下方 full-width residual / estimand 与上方两栏没有清楚的空间分隔。双栏 + full-width 布局必须有独立区域、足够 whitespace 和明确层级，不能挤在一起。

### P10 — CAT-TRACE architecture

- [橙色/必须形成规则] diagram 仍有箭头/节点 overlay、箭头太小、整体拥挤。该问题已多轮重复，今后必须作为直接 QA fail，而不是审美建议。
- [黄色] `K \ {matched taxa in first n}` 放在 block 内仍显拥挤，应检查是否需要更清楚的 node 结构或 annotation。

### P11 — Matching observed features to catalogue

- [黄色] table header 是否首字母大写需要全 deck 固定规则；table 也缺一个自然的 `Example`/context 引导，听众不清楚为什么突然看到三数据集表。
- [橙色/必须形成规则] GBIF 作为一个次要术语解释，不能突兀地占据整页底部形成视觉主项。次要 glossary/definition 应放在首次出现的局部邻域、脚注/注释或更轻的 supporting text 中，不能破坏主层级。
- [黄色] `use` 作为表头不自然，需要更明确地说是 matching interpretation / role / evidence use。

### P12 — Identity-aware catalogue borrowing

- [黄色] table header capitalization 继续需要统一。
- [黄色] `Catalogue intercepts ...` 作为极小 footer/脚注位置莫名其妙；重要科学信息不能降成几乎不可见 footer。
- [黄色] traits/taxonomy table 当前像字段清单，缺乏“这是什么、为什么影响 response borrowing”的自然解释。
- [黄色] 最后一段 remark 是否需要统一 remark/callout style，需要决定。

### P13

- 无批注。

### P14

- 无批注。

### P15 — Residual dependence

- [黄色] `diag(Sigma_W)=1` 是否值得单独占据正中间一整行，应按公式重要性重新判断。
- [橙色/必须形成规则] `Residual factor-copula specification in the CAT-TRACE manuscript draft.` 这种内部稿件/项目状态脚注再次出现。Audience-facing slide 禁止出现 manuscript draft、validation audit、repo path、internal note 等编辑/工程语言。

### P16 — Priors

- [黄色] `Residual-factor shrinkage` 没有直接说 MGP 名字，失去方法定位；可考虑引用/重绘原论文图或增加更直观 visual，但不能仅为填空加图。

### P17 — Theorem

- [橙色/必须形成规则] theorem 页第一行直接从 `N_ig^U = sum...` 开始。核心数学对象不能毫无引导地成为页面首项；先用一行自然语言说明“我们控制的是每个 group 在一个 sample 中的 expected number of present open-tail species”，再给定义/定理。
- [橙色/必须形成规则] `as p_U,g grows` 是上一页同类数学英语问题，不再重复：极限条件必须使用标准记法。
- [橙色/必须形成规则] Theory 主结果应有编号体系（Theorem 1 / Corollary 1 / Proposition 1，或与 manuscript 一致的正式编号），并检查理论覆盖是否足以体现方法价值；不能只因为页面形式需要而随意叫 theorem/corollary/proposition。

### P18 — Corollary

- [橙色/必须形成规则] 首行直接定义 `N_i^U=sum_g...`，与 P17 同一问题：数学对象需要先解释其科学含义，再进入公式。
- [橙色/必须形成规则] `as all p_U,g grow` 再次违反标准极限排版；属于重复 regression。

### P19

- 无批注。

### P20 — Oracle simulation

- [橙色/必须形成规则] 图仍然太小；caption 冗长且像论文底注，实际验收没有把图的可读性作为硬门槛。Figure-heavy page 主图必须占据足够视觉面积，caption 只能保留理解编码所需的信息。
- [深橙/必须形成规则] `analysis/simulation_oracle/.../summary_note.md` 这种 repo path 仍进入 audience-facing slide，明确禁止。
- [黄色] truncation grid `50 to 5,000` 没有说明具体 step/grid，应给实际取值或明确 sampling rule。
- [黄色] `target ... is` wording 不准确，应区分 theoretical target / expected target / observed estimate。
- [橙色/必须形成规则] seed 被放在主 slide 的 Design 区。Random seed 属于 reproducibility metadata，除非它本身影响科学解释，否则不应占 audience-facing 主页面空间。

### P21 — Simulation 1B

- [橙色/必须形成规则] `Question` 需要更稳定、明显但不过度的统一 visual treatment，可考虑 callout / quotation-style / accent rule，而不是纯小标题。
- [橙色/必须形成规则] metric direction 不应写 `lower / higher / near target` 这种弱 table prose；应采用紧凑、学术论文常见的 `RMSE ↓`, `PR-AUC ↑`, `Coverage -> 95%` 等方向标记，并解释 metric 检查什么。
- [黄色] `Comparison` 行把 CAT-TRACE 自己与 baseline 混在一个分号串里，语义和排版都不自然；comparison 应明确 focal method 与 baselines 的关系，避免 semicolon dump。

### P22

- 无批注。

### P23

- 无批注。

### P24 — Finland dataset

- [橙色/必须形成规则] `samples / fungal OTUs / nonzero entries / zero fraction / singleton...` 裸竖排数字难看且难扫读。3 个以上结构化 facts 应使用 compact table、definition list 或清楚分组，不允许看似表格却无表格结构的数字堆。

### P25 — Malagasy dataset

- [黄色] prevalence 图太小且没有 caption；图像可读性检查未落实。
- [橙色/必须形成规则] `TRACE validation audit.` 再次出现内部记录语言，属于重复 hard fail。

### P26

- 无批注。

### P27 — Questions for discussion

- [橙色/必须形成规则] 页面大量纵向空间浪费，三组 question 过度压缩在上半页。Discussion 也必须充分利用可用空间、保证投影字号；不能因为信息已经齐全就缩成小字。
- [橙色/必须形成规则] `Background:` 是有效设计：帮助第一次听 topic 的教授快速恢复必要上下文。后续 supervisor/advisor question 应默认考虑一行 compact background，前提是确实降低理解成本。

### P28

- 无批注。

### P29 — References

- [橙色/必须形成规则] Reference 页仍然字号过小、纵向空间没有充分利用。Reference 不是“塞进去就行”；在引用数量允许时必须优先放大字号、行距并利用页面高度。

## 3. 按失败类型归类

### A. 重复出现、必须升级为 hard QA 的视觉问题

页：P2, P9, P10, P20, P24, P25, P27, P29。

核心问题：

- overlay / edge overlap 仍发生；
- diagram 箭头仍太小；
- 主图仍太小；
- 纵向空间大量浪费；
- structured facts 没有使用合适容器；
- reference/discussion 页人为压缩字号。

这些不是新的审美意见，而是 v2 已经提出、v3 再次违反的 regression。

### B. 数学对象层级与引导不足

页：P4, P6, P8, P15, P17, P18。

核心问题：

- 公式先于动机/定义；
- 新参数不解释；
- `as p grows` 等非标准数学英语直接进入公式；
- 非核心公式被放在视觉中心；
- theorem / corollary / proposition 编号与理论覆盖没有统一体系。

### C. Audience-first 仍执行不稳定

页：P2, P3, P7, P11, P12。

核心问题：

- OTU、catalogue、arthropod、Malagasy、phylogeny 等仍然先用后解释或只做形式定义；
- framework/term style 没有完全统一；
- 定义没有通过真实 case 建立直觉。

### D. 内部项目/工程语言继续泄漏

页：P15, P20, P25；相关局部还有 P12。

出现：

- manuscript draft；
- validation audit；
- repo path / summary note path；
- 不重要的 reproducibility metadata（seed）占据主页面。

这是多轮明确禁止后仍出现的严重 regression。

### E. Table / list / callout 选择仍不稳定

页：P11, P12, P21, P24, P27。

核心问题：

- table 缺 context；
- header capitalization / wording 不统一；
- facts 没有形成 table/list；
- question 没有稳定 visual treatment；
- comparison 继续用分号串；
- background 的好做法没有上升成 reusable pattern。

### F. 科学叙事顺序仍有跳跃

页：P2, P4, P7, P8, P17, P18。

核心问题：

- CAT-TRACE 名称早于 TRACE/模型动机；
- estimand 早于“为什么关心”；
- HMSC/CORAL 仍有一句公式/边界代替完整机制；
- theorem 直接从符号开始，没有先说研究问题。

## 4. 对 v2 规则执行情况的复盘

v3 并不是完全没有使用 v2 新规则。`002_cat_trace_group_meeting_v3` 明确吸收了：sentence case、first-use term style、mini-header、two-column rule、核心公式居中门槛、metrics table、main visual size、diagram contract、anti-AI scan、reference 放大等要求；源文件也新增了 `newterm`, `minihead`, `standalonehead`, `semanticlabel`, `metricrow` 等宏。

但结果说明当前流程存在一个关键缺口：**规则被写进 prompt ≠ 规则被可靠执行与验收。**

本轮重复失败包括：

- v2 已禁止 overlay，P2/P10 仍出现；
- v2 已要求利用纵向空间，P9/P27/P29 仍失败；
- v2 已要求 diagram 箭头足够大、无 overlay，P10 仍失败；
- v2 已禁止内部工程语言，P15/P20/P25 仍出现 manuscript/audit/path；
- v2 已规定首行居中公式必须是核心对象，P17/P18 仍从未解释的定义开场；
- v2 已要求主图足够大，P20/P25 仍然过小。

因此下一轮不能只把规则继续复制进 prompt；必须增加“继承 + 逐条验收 + regression evidence”机制。

## 5. 下一轮讨论边界

当前先保存全部 v3 批注并建立问题地图。下一步由 GPT 按 P1 -> P29 做第一轮审阅和修改方向讨论；用户确认后，再形成 v4 execution task。

所有橙色/深橙色项必须在 v4 task 前被映射到可复用规则，并标记是否：

1. 已有规则但 v3 执行失败 -> 升级为 hard regression gate；
2. 已有规则但太模糊 -> 补充可执行阈值/示例；
3. 真正新规则 -> 加入 presentation TODO candidates；
4. CAT-TRACE 特例 -> 不进入通用规则。
