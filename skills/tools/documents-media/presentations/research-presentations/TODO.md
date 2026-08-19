# Research Presentations TODO

本文件记录真实组会返修中暴露出的 presentation 规划与质检问题。后续升级 `research-presentations` skill / presentation plugin 时，应优先把这些经验转成可执行规则、deck-plan 校验项和 rendered-slide QA，而不是继续依赖人工发现。

## 2026-08-19：CAT-TRACE 组会返修经验

### 1. Audience-first symbol introduction

- [ ] 禁止在符号第一次出现时只给公式、不解释对象。任何新符号都应在同一页、同一视觉邻域内说明“它是什么、从哪里来、用于什么”。
- [ ] 对复合证据对象尤其如此。例如 `s_f` 不能只写在 `q_{fk}=P(c(f)=k\mid s_f)` 中；必须说明它是 feature `f` 的身份识别证据，可包含 sequence、alignment/similarity score、classifier output、morphology 或其他 matching evidence，并给一个真实数据语境中的例子。
- [ ] Dataset-specific abbreviations、内部 ID、路径名不得直接进入 audience-facing slide。`rd001/rd002/rd003` 这类仓库内部编号只能出现在 notes / source manifest，不应要求听众记忆。
- [ ] 所有矩阵尺寸必须带单位，例如 `30,955 sites × 1,116 plant species`、`2,874 samples × 255,188 OTUs`，不得只写裸尺寸。

### 2. Cognitive-load gate before layout

- [ ] 先问“听众此时已经知道什么”，再决定这一页能出现哪些术语和公式。不能在 catalogue 尚未定义前使用 `catalogue-external`，不能在 HMSC/CORAL 尚未解释前直接用其缩写承担论证。
- [ ] 每页新增概念数量必须受控；如果一句 bullet 依赖一个尚未解释的前提，应在该 bullet 中显式加入 `if / when` 条件，而不是让听众自行推断适用条件。
- [ ] 对可选层级项使用条件化表达，例如：`If trait information is available...`; `If a reliable phylogenetic position is available...`; `Otherwise remove that term.`
- [ ] 一张 slide 的视觉结构不得迫使观众在三个以上并列栏之间来回跳读。三列布局不是默认解；讨论问题、复杂模拟和层级模型优先使用自上而下或逐步展开的顺序。

### 3. Existing-method comparison must teach the model, not only name it

- [ ] 当一个已有方法是核心 comparator / closest prior work 时，不能只给一句功能标签。必须给足够的数学或流程结构，让第一次听说它的观众知道“它做了什么、输入输出是什么、与当前方法差在哪里”。
- [ ] 若方法 B 建立在方法 A 上，叙事顺序必须体现依赖关系。例如 CORAL 应在 HMSC 之后解释：先对 common species 拟合 HMSC backbone，再将 common-species posterior / latent factors 转成 rare-species 的 informative conditional prior，最后逐个拟合 rare species。
- [ ] 不要把已有工作的共同能力误写成自己的增量。诸如“residual association is not causal”属于解释边界，不是相对 HMSC/CORAL 的 novelty。

### 4. Derivations and hyperparameter forms need provenance

- [ ] 对报告中关键但非显然的 prior / scaling 形式，至少用一行说明其来源或设计逻辑。不能只展示 `\mu_p, \tau_p` 的最终形式。
- [ ] 区分“由某个恒等式精确校准得到”与“为了某种渐近性质选择的 scale”。例如 TRACE 中 `\mu_p` 可由 Gaussian-probit identity 解出，以控制单列 occurrence probability；`\tau_p=\sqrt{2\log p}` 则是与 Gaussian extreme-value scale 对齐的建模选择，不能伪装成同一个恒等式推导出来。
- [ ] 同一机制的解释图与公式应放在首次引入它的位置，不要在后续 extension slide 再重复基础机制。例如 TRACE calibration intuition 应靠近 TRACE slide，而 group-marked extension slide 只讲“如何从单组 TRACE 扩展到多个 marked groups”。

### 5. Scientific slide must contain scientific objects

- [ ] Prior slide 不能只剩抽象 prose cards。若 prior 本身是方法设计的一部分，应展示代表性的数学形式，例如 catalogue hierarchy、group intensity prior、MGP loading shrinkage。
- [ ] 用公式时必须解释参数的功能；用 prose 时必须能对应到一个明确的 model object。禁止“Catalogue side / Open-tail side / Residual dependence”这种只有概括词、没有模型结构的空页。
- [ ] 相邻视觉 block 若承担同层级概念，必须统一真实高度、基线和文字密度；仅设置 `minimum height` 不足以保证视觉等高，应检查实际 render 并必要时使用固定 `text height/text depth` 或统一内容行数。

### 6. Simulation slides require a minimum evidence specification

- [ ] 不允许把多个尚未解释的 simulation 压成一页三列“标题 + 一句话 + metrics”。若 audience 看不到 DGP，就无法判断实验是否真正检验 claim。
- [ ] 每个 simulation 主 slide 至少包含：
  1. **DGP / generative equations**；
  2. **one manipulated axis / stress factor**；
  3. **comparators / ablations**；
  4. **primary estimand or prediction type**；
  5. **evaluation metrics**；
  6. **planned plot(s)**，明确 x/y axis 或 panel 含义。
- [ ] Simulation metric 必须匹配 scientific estimand，而不是机械复用 AUC。对 JSDM / binary community prediction，应区分 marginal prediction、joint prediction、species-richness/discovery prediction，并选择相应的 Brier/log score、PR-AUC/AUC、community dissimilarity、richness error、joint likelihood/log score、coverage 等指标。
- [ ] 极端不平衡 rare-species 场景不得只报告 AUC；至少考虑 PR-AUC、Brier/log score 或其他对 rare positives / probability calibration 更敏感的指标。
- [ ] 若 simulation 有已知真值，可将 coefficient/correlation recovery 作为 mechanism check；但不能让 parameter MSE 取代真正关心的 predictive/discovery target。

### 7. Data slides are scientific arguments, not dataset inventory cards

- [ ] Dataset slide 应优先回答：数据是什么、已有工作用它回答了什么、当前方法新增回答什么。避免重复模板标题 `What was sampled / What previous work did / Role in the deck`。
- [ ] 正式英文优先使用自然标题，如 `Data and sampling design`, `Existing analysis`, `CAT-TRACE question`，并允许不同数据页使用不同结构。
- [ ] 图片必须足够大，图和正文之间保留明确留白。一个 slide 不应同时塞入过多小图、rare-tail panel、三组 caption 和大段文字。
- [ ] Composite image 中每个 panel 有独立 caption 时，应优先真正裁成独立 panel，而不是依赖整张 PNG 的内部白边与外部 tabular caption 对齐。
- [ ] Render QA 必须检查“scientific content 实际占据的像素区域”，而不是只检查图片 bounding box。PNG canvas 很大但内容很小仍应判为失败。

### 8. Diagram semantics must match the probabilistic story

- [ ] 流程图中的箭头必须表示真实的数据/条件依赖。若 catalogue 是外部已知对象，就不能画成 `observed features -> matching -> catalogue`，暗示 catalogue 由样本产生；应将 external catalogue 与 observed raw features 作为 matching 的两个输入。
- [ ] 定义某集合的公式应放在代表该集合的 block 内或紧邻其标题，不要把核心定义悬空放在图外形成视觉“尾巴”。
- [ ] 对 normalization 公式要定义所有中间量，例如 `D=diag(\Omega)`；不得假定 audience 会自行补齐。

### 9. Discussion slide should optimize for advisor decisions

- [ ] Discussion questions 默认自上而下排版，不使用三列卡片。
- [ ] 每个问题必须满足：一般统计/Bayesian 教授无需熟悉项目软件即可回答；答案会实际改变 theorem、model identifiability、inference 或 experimental scope。
- [ ] 已经由项目内部可以决定的问题不要浪费导师讨论时间，例如内部 dataset 数量、具体文件命名、是否复用某段代码。
- [ ] 问题文本不应同时堆 4-5 个子问题；主问题一行，必要背景一行即可。

### 10. Do not default to backup-slide accumulation

- [ ] Research group meeting 默认**不自动生成大量 backup slides**。相对次要但理解主线所需的内容，应在主线快速解释；真正不影响主线的内容应直接省略或放 speaker notes / source document。
- [ ] 只有用户明确需要 appendix / backup，或存在高概率被追问且无法用 notes 支撑的关键技术细节时，才增加少量 backup。
- [ ] QA 应对 `backup_count / main_count` 设置软警告；若 backup 接近或超过主 deck 的一半，应要求重新审视 scope。

### 11. Anti-AI-language audit

- [ ] 搜索并人工审阅重复模板短语，特别是连续页面使用 `What ...`, `Role in the deck`, `Why it matters`, `Current plan`, `This slide...` 等元话语。
- [ ] Slide 应直接陈述 scientific object / claim，不解释“这一页在 deck 中扮演什么角色”。
- [ ] 允许非对称结构。不要为了视觉整齐把每页强行压成同样的三栏、三卡、三 bullet。

### 12. Rendered-slide QA must be semantic, not only mechanical

- [ ] `no overflow / no compilation warning` 不是视觉通过标准。
- [ ] 独立 reviewer 必须逐页判断：第一次看到这一页的人，是否能在 5-10 秒内知道变量是什么、图表示什么、比较对象是什么、单位是什么。
- [ ] 对 figure-heavy slides 检查字体和 scientific panel 的实际尺寸；对 equation-heavy slides 检查符号是否在首次出现时解释；对 discussion slides 检查阅读路径是否自然。
- [ ] Contact sheet 只能做全局密度筛查，关键 slide 必须单页放大检查。

## 后续实现建议

- [ ] 将上述 audience-first、simulation-minimum-spec、dataset-unit、no-internal-ID、no-default-backup 规则加入 `deck-plan.schema` 或 `validate_deck_plan.py` 可验证字段。
- [ ] 为 research group meeting 新增 semantic QA checklist：`symbol_defined_on_first_use`, `units_present`, `dgp_present`, `planned_plot_present`, `comparator_explained`, `internal_ids_hidden`, `backup_justified`。
- [ ] 在 `RESEARCH_PRESENTATION_ANTIPATTERNS.md` 中加入真实失败案例：三列 discussion、prose-only prior slide、DGP-free simulation summary、tiny multi-panel dataset slide、dangling definition under diagram。
- [ ] 在后续 presentation plugin 版本中把这些规则同步到 Codex plugin mirror，并补 regression eval。
