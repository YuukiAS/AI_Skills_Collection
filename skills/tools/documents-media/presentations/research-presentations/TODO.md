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
  3. **comparators / ablations**（仅在 comparator 本身是本轮实验问题时；不要为了模板完整性强塞）；
  4. **primary estimand or prediction type**；
  5. **evaluation metrics**；
  6. **planned plot(s)**，说明最终准备画什么即可，不要求机械拆成 Panel A/B/C。
- [ ] Simulation metric 必须匹配 scientific estimand，而不是机械复用 AUC。对 JSDM / binary community prediction，应区分 marginal prediction、joint prediction、species-richness/discovery prediction，并选择相应的 Brier/log score、PR-AUC/AUC、community dissimilarity、richness error、joint likelihood/log score、coverage 等指标。
- [ ] 极端不平衡 rare-species 场景不得只报告 AUC；至少考虑 PR-AUC、Brier/log score 或其他对 rare positives / probability calibration 更敏感的指标。
- [ ] 若 simulation 有已知真值，可将 coefficient/correlation recovery 作为 mechanism check；但不能让 parameter MSE 取代真正关心的 predictive/discovery target。
- [ ] Metric 不能只列名字。至少用半句说明统计含义，例如 Brier score 衡量概率预测平方误差、PR-AUC 强调稀有正类排序、coverage 检查 posterior uncertainty 是否达到名义覆盖率。
- [ ] Planned figure 默认用一两句自然语言说明，不要为了“设计感”预先固定 `Panel A / Panel B / Panel C`。真正产生结果后再按数据决定 figure layout。

### 7. Data slides are scientific arguments, not dataset inventory cards

- [ ] Dataset slide 应优先回答：数据是什么、已有工作用它回答了什么、当前方法新增回答什么。避免重复模板标题 `What was sampled / What previous work did / Role in the deck`。
- [ ] 正式英文优先使用自然标题，如 `Data and sampling design`, `Existing analysis`, `CAT-TRACE question`，并允许不同数据页使用不同结构。
- [ ] 图片必须足够大，图和正文之间保留明确留白。一个 slide 不应同时塞入过多小图、rare-tail panel、三组 caption 和大段文字。
- [ ] Composite image 中每个 panel 有独立 caption 时，应优先真正裁成独立 panel，而不是依赖整张 PNG 的内部白边与外部 tabular caption 对齐。
- [ ] Render QA 必须检查“scientific content 实际占据的像素区域”，而不是只检查图片 bounding box。PNG canvas 很大但内容很小仍应判为失败。
- [ ] 当图太小时，第一反应应是**减少图的数量**，而不是继续压缩正文或把所有图同时放大。一个 dataset 页默认只保留 1 个主图，必要时再加 1 个辅助图。
- [ ] 主图应真正成为页面视觉中心。若主图只占页面约四分之一，却同时存在大量正文/小图，应判为 layout failure。

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
- [ ] `Interpretation note`, `Prediction target`, `Main takeaway`, `Key message` 等标签默认视为可疑；若删掉标签后正文完全成立，就应直接删掉标签。
- [ ] Speaker notes 也要去生成过程语言。`This slide...`, `Use this page...`, `reference point for the deck` 等应改成真实讲稿提示，而不是把制作说明伪装成 speaker cue。

### 12. Rendered-slide QA must be semantic, not only mechanical

- [ ] `no overflow / no compilation warning` 不是视觉通过标准。
- [ ] 独立 reviewer 必须逐页判断：第一次看到这一页的人，是否能在 5-10 秒内知道变量是什么、图表示什么、比较对象是什么、单位是什么。
- [ ] 对 figure-heavy slides 检查字体和 scientific panel 的实际尺寸；对 equation-heavy slides 检查符号是否在首次出现时解释；对 discussion slides 检查阅读路径是否自然。
- [ ] Contact sheet 只能做全局密度筛查，关键 slide 必须单页放大检查。
- [ ] 对投影场景建立字号软门槛：如果核心内容依赖 `scriptsize` 才能装下，默认判为 scope/layout failure，应拆页或删内容；不能把缩小字号当成完成任务。

### 13. Visual restraint: not every scientific idea needs a diagram

- [ ] Presentation generator 不得把“可视化”理解为“凡是有流程就画 TikZ”。很多统计内容用一条公式加两三句自然语言比流程图更清楚。
- [ ] 对每个拟议 diagram 先问：**图是否比文字更快地传达一个真实的结构关系？** 如果只是把三句话装进三个方框再用箭头连接，应删除图，恢复为 prose/equation。
- [ ] TRACE calibration、CORAL 两阶段机制、matching 逻辑等内容只有在图真正降低理解成本时才绘制；否则优先使用普通数学叙述。
- [ ] 禁止“卡片化就是设计”的默认审美。真实科研汇报可以是一页正常标题、一个公式、一段解释和一张大图。
- [ ] 对图形化 architecture，组件数量越多越应克制颜色。默认使用一个主色 + 中性灰，不用五六种语义相近的紫/红/粉来区分概念。

### 14. One slide, one intellectual job

- [ ] 一页不能同时承担两个独立教学任务。例如 matching 页不应同时解释 discovery decomposition；已有工作页不应同时承担 novelty enumeration；dataset 页不应同时塞采样设计、rare-tail 图、已有模型历史和新方法问题。
- [ ] 若一页标题中出现 `and`，应检查是否实际上是两个可拆开的认知任务；只有它们共享同一个核心公式或结论时才允许合并。
- [ ] 每页先写出一句内部问题：`After this slide, what should the audience now understand that they did not understand before?`。如果答案包含两个以上互相独立的概念，优先拆分或删除次要内容。

### 15. Layout should follow scientific hierarchy, not symmetry

- [ ] 左右 50/50、三栏 1/3-1/3-1/3 不得作为默认布局。版面面积应按科学重要性分配，而不是追求几何对称。
- [ ] 主图、主公式、主结论应获得最多空间；辅助 context 可以不对称地放在边缘或删除。
- [ ] 当用户反复指出“图片太小”，禁止继续在同一页保留所有原图后做微调。必须重新决定信息优先级，删掉低价值对象。
- [ ] 同页同时出现多张图片时，应检查每张是否仍达到会议室投影可读性；若任何一张只能靠靠近屏幕才能辨认，应删图或拆页。

### 16. Existing-method slides should sound like a statistician explaining a model

- [ ] HMSC/CORAL/TRACE 等已有方法页优先使用“模型式 + 两三句解释”，不使用 marketing-style boxes 或 process cards。
- [ ] 对 CORAL 这类 transfer-learning 方法，首次介绍至少回答：先拟合什么、从中得到什么、如何传给 rare species、rare species 是否已经 observed。
- [ ] closest prior work 的边界必须说清楚，但不要堆优劣评价。成熟组会叙事优先是 `what it solves -> what remains unresolved`，而不是 `ours is better`。

### 17. Scientific labels must be content, not editorial metadata

- [ ] Slide 上出现的加粗标签应当是科学对象，例如 `Catalogue discovery`, `Open-tail discovery`, `Marginal calibration`，而不是编辑/叙事标签，例如 `Interpretation note`, `Prediction target`, `Role in the deck`。
- [ ] 如果一行标签只是在告诉作者“这一段起什么作用”，而不是告诉 audience 一个科学概念，就应移到 source comment / speaker notes。

## 后续实现建议

- [ ] 将上述 audience-first、simulation-minimum-spec、dataset-unit、no-internal-ID、no-default-backup 规则加入 `deck-plan.schema` 或 `validate_deck_plan.py` 可验证字段。
- [ ] 为 research group meeting 新增 semantic QA checklist：`symbol_defined_on_first_use`, `units_present`, `dgp_present`, `planned_plot_present`, `comparator_explained`, `internal_ids_hidden`, `backup_justified`。
- [ ] 扩展 semantic QA checklist：`main_visual_large_enough`, `scriptsize_core_content_absent`, `diagram_adds_information`, `one_intellectual_job_per_slide`, `editorial_labels_absent`, `planned_figure_not_overpanelized`。
- [ ] 在 `RESEARCH_PRESENTATION_ANTIPATTERNS.md` 中加入真实失败案例：三列 discussion、prose-only prior slide、DGP-free simulation summary、tiny multi-panel dataset slide、dangling definition under diagram、three-box CORAL flow、five-box TRACE calibration flow、editorial `Interpretation note`、主图被多个辅助图挤小。
- [ ] 为 dataset-heavy 组会建立 visual dominance regression：主图实际 scientific-content bbox 占 slide 面积过低时给 soft fail，而不是只检查图片 object bbox。
- [ ] 为 simulation plan 建立结构化字段，但 `comparators` 设为 optional；`planned_figures` 应允许一句自然语言计划，不强制 panel 数量。
- [ ] 在后续 presentation plugin 版本中把这些规则同步到 Codex plugin mirror，并补 regression eval。
