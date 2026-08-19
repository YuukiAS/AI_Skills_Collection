# Research Presentations TODO

本文件记录真实科研汇报返修中反复暴露出的通用问题。目标不是保存某一个项目的经验，而是把这些问题转化为 `research-presentations` skill / presentation plugin 的**通用生成规则、可验证约束和 rendered-slide QA**，避免每次做组会、seminar、proposal 或 methods talk 时重新人工发现同一类问题。

## 1. Audience-first：先管理听众已经知道什么

- [ ] 新符号第一次出现时，必须在同一页、同一视觉邻域说明：**它是什么、来自哪里、在模型里做什么**。不能只给公式让听众自行补定义。
- [ ] 复合对象尤其需要现实语境。例如一个“证据对象”应说明可能由 sequence、measurement、classifier output、metadata 等组成，而不是只给抽象下标。
- [ ] 内部数据编号、实验 run ID、repo 路径、文件名、实现字段不得进入 audience-facing slide。内部标识只留在 notes、source manifest 或代码注释。
- [ ] 所有矩阵尺寸、样本量、维度必须带单位，例如 `30,000 locations × 1,100 species`，不能只写裸尺寸。
- [ ] acronym 第一次出现必须展开；如果该术语不值得解释，就不应进入主线。
- [ ] 先问“听众此时已经知道什么”，再决定当前页能出现哪些术语。禁止使用下一页才定义的概念。
- [ ] 对可选模型组件必须写出适用条件，例如 `If trait information is available...`，不能让公式看起来像所有项永远同时存在。

## 2. One slide, one intellectual job

- [ ] 每页在生成前必须先回答一个内部问题：**After this slide, what should the audience understand that they did not understand before?**
- [ ] 如果答案包含两个相互独立的教学任务，优先拆页或删除次要任务。
- [ ] 标题中出现 `and` 时应触发检查：两部分是否真的共享同一个核心公式、图或结论？如果不是，应拆分。
- [ ] 一页不能同时承担“定义符号 + 介绍已有方法 + 宣布 novelty + 给 simulation 设计”等多个任务。
- [ ] 科研汇报的页数不是首要优化目标。宁可多一页、每页讲 30–60 秒，也不要为了压页数把内容塞进三栏小字。

## 3. Scientific object first，不能用卡片代替内容

- [ ] 每页必须有真实 scientific object：数据、公式、图、实验设计、病例、模型结构、定理、结果或明确的问题。
- [ ] 纯粹的 `title + 3 cards + summary strip` 不构成科研内容。
- [ ] Prior / method / theorem 页如果核心是数学结构，应展示代表性公式；不能只剩抽象 prose cards。
- [ ] 用公式时解释参数功能；用 prose 时必须能明确对应到一个 model object。
- [ ] 不要把“视觉化”理解为“凡是有流程就画图”。很多统计内容用一条公式加两三句自然语言更清楚。

## 4. Existing-method comparison：像统计学家一样介绍模型

- [ ] 核心 comparator / closest prior work 不能只给一句功能标签。第一次听说该方法的观众至少要知道：输入是什么、核心模型/机制是什么、输出是什么、它解决了什么。
- [ ] 若方法 B 建立在方法 A 上，叙事顺序必须体现依赖关系，而不是并列三张卡片。
- [ ] 优先采用 `what it solves -> what remains unresolved`，而不是 marketing-style `ours is better`。
- [ ] 不要把已有工作的共同能力或共同 caveat 写成自己的 novelty。
- [ ] 已有方法页优先使用“最小模型式 + 2–3 句解释”；流程图仅在它明显比文字更快表达机制时使用。

## 5. Derivation / prior / scaling 必须交代来源

- [ ] 对关键但非显然的 prior、normalization、scaling、threshold 或 asymptotic form，至少用一行说明为什么是这个形式。
- [ ] 区分：
  - exact identity / algebraic calibration；
  - modeling choice；
  - asymptotic scaling；
  - regularization convention；
  - empirical heuristic。
- [ ] 不能把“通过恒等式反解得到”和“为了极值/收敛性质选择的 scale”混在一起讲。
- [ ] 同一机制的解释应放在首次引入处；后续 extension 页只讲新增部分，不重复基础机制。

## 6. Diagram gate：不是所有关系都应该画图

- [ ] 每次准备画 diagram 前必须先回答：**这个图是否比普通文字/公式更快传达一个真实结构关系？**
- [ ] 如果只是把三句话装进三个 box 再连箭头，默认不画。
- [ ] Arrow 表示的是方向性语义：数据流、条件依赖、转换、控制流或时间顺序。若关系只是“属于”“并列”“组成”“同一集合中的两个部分”，不应机械使用箭头。
- [ ] Containment 应优先使用 enclosure、brace、group label 或共同背景，而不是箭头。
- [ ] 如果一个大框只是“工作集合/系统边界”，不要让多个斜箭头射进框的不同角落；这会同时产生视觉噪音和错误的流程暗示。

## 7. Diagram geometry：先定阅读方向，再放节点

- [ ] 一个 diagram 只能有一个主要阅读方向：**top-to-bottom** 或 **left-to-right**。不要一部分向下、一部分横向、再用斜箭头折回来。
- [ ] 同一层级的节点必须对齐：相同 y 或相同 x；peer nodes 的 baseline、中心线和间距应一致。
- [ ] 输入、转换、输出/结果应形成清楚层级。优先用 grid / level-based layout，不用“哪里有空塞哪里”。
- [ ] 多路输入汇合时，优先：
  1. 对称进入同一个目标节点；或
  2. 先进入一个 merge/junction，再由一条主箭头继续。
- [ ] 多路输出分叉时同理。避免两根斜线以不同角度随机飞向两个 box。
- [ ] 若 layout 中出现 edge crossing，默认判为失败；应重新排节点，而不是用更细的线掩盖。
- [ ] 箭头不得穿过 box、文字、公式、caption 或其他箭头。
- [ ] 节点之间必须留足 edge clearance。若箭头一出框就立即碰到另一个框，说明 vertical/horizontal spacing 不足。

## 8. Arrow style：建立统一默认，不准每页临时发挥

- [ ] Presentation plugin 应提供统一的 canonical arrow style，禁止每个 deck / 每张 slide 自己临时定义默认箭头。
- [ ] 推荐的 Beamer/TikZ 起点（可随模板比例微调）：
  ```tex
  \tikzset{
    diagram edge/.style={
      -{Stealth[length=2.8mm,width=2.0mm]},
      draw=black!70,
      line width=0.9pt,
      shorten <=2pt,
      shorten >=2pt
    }
  }
  ```
- [ ] 不要只写 `>=Stealth` 后依赖库默认 arrowhead；默认箭头头部经常过小，投影时几乎看不见。
- [ ] 同一张图所有主箭头必须使用一致的：arrowhead family、长度、宽度、line width、颜色。
- [ ] 若存在 secondary / optional edge，可通过更浅灰、dashed 或 thinner 区分，但整张图最多 2 类 edge style；超过 2 类必须有明确语义和 legend。
- [ ] 箭头应从 box **边界的语义 anchor** 出发并落到目标 box 边界，例如 `.south -> .north`、`.east -> .west`。不要从 box 内部文字中心出发，也不要随机命中角点。
- [ ] 默认避免斜箭头进入矩形角落。层级图优先使用中心到中心的垂直/水平边；需要转弯时使用 orthogonal routing（如 `|-`, `-|`）而不是任意 diagonal。
- [ ] Arrowhead 与 box 边框之间必须留出呼吸空间，避免箭头头部压在边框上；`shorten >=` 应纳入 canonical style。
- [ ] 对汇合/分叉的边，几何角度应尽可能对称。左右 peer branches 不应一根陡、一根缓。
- [ ] 不允许不同页面出现明显不同大小的箭头头部。Arrow style 属于 deck-level theme，而不是 page-level choice。

## 9. Box style：语义层级决定样式，不是“有内容就画框”

- [ ] Box 只用于真正需要界定边界的对象：model component、state、input/output、set/container、decision point。普通解释文字不需要 box。
- [ ] 同一 semantic level 的 peer boxes 必须一致：
  - border style；
  - fill；
  - corner radius；
  - text size；
  - internal padding；
  - 实际高度（不仅是 `minimum height`）。
- [ ] 推荐统一基础 node style（可随模板微调）：
  ```tex
  \tikzset{
    diagram node/.style={
      draw=black!55,
      line width=0.7pt,
      rounded corners=1.5pt,
      fill=black!2,
      align=center,
      inner xsep=7pt,
      inner ysep=5pt,
      font=\small
    }
  }
  ```
- [ ] Peer node 高度不一致时，不能只靠 `minimum height`。应使用统一 `text width`、控制内容行数，必要时固定 `text height/text depth`。
- [ ] 长公式不应被硬塞进窄 box。公式若是主要 scientific object，应脱离卡片，使用正常 display math。
- [ ] Container box 与 process box 必须视觉区分。Container 应更轻、更淡，避免让 enclosure 看起来像流程节点。
- [ ] 嵌套 box 只有在真实 containment 语义下才允许。不要用“大框包小框”制造层级感。
- [ ] 避免 box 边框与箭头、公式、其他 box 边界视觉相切。

## 10. Color：diagram 默认一个 accent + 中性色

- [ ] 默认只使用一个主 accent color + neutral gray / black。
- [ ] 不要用五六种相近紫、红、粉去区分没有必要的节点；这会让结构更难读，而不是更清楚。
- [ ] 同一 semantic level 默认同色；只有真正不同的类别/状态才改变 fill 或 stroke。
- [ ] 箭头默认中性深灰。只有 arrow 本身携带类别语义时才着色。
- [ ] Container fill 应比 process node 更淡，避免抢视觉主导。
- [ ] 色彩必须服从整个 deck template，不单独在 diagram 中创造新的 palette。

## 11. Diagram text：尽量短，不在框里写段落

- [ ] 一个 box 里优先：短名词/短动词 + 必要公式。不要放 3–5 行 prose。
- [ ] 若一个 node 需要完整句子解释，应把解释放在图外，并缩短 node label。
- [ ] Box 内的公式必须在投影上可读；如果缩成 `scriptsize` 才能放下，应重构 diagram。
- [ ] Diagram 中的符号依旧服从首次定义规则；不能因为“这是图”就省略定义。

## 12. Diagram-specific rendered QA

- [ ] 每个 diagram 页必须单独放大检查，contact sheet 不足以验收。
- [ ] Reviewer 必须逐项确认：
  - reading direction 是否一眼可见；
  - peer nodes 是否对齐；
  - peer boxes 是否等高等距；
  - arrowhead 是否足够大；
  - arrow line width 是否一致；
  - edge 是否从正确 anchor 出发；
  - 是否存在随机 diagonal；
  - 是否存在 edge crossing；
  - 箭头是否碰 box 边框/文字；
  - box 是否只在有语义边界时出现；
  - color 是否超出一个 accent + neutrals；
  - 图在 5 秒内是否能读出主要关系。
- [ ] 若 diagram 需要作者口头解释“这根箭头其实不是这个意思”，图即判失败。

## 13. Layout should follow scientific hierarchy, not symmetry

- [ ] 左右 50/50、三栏 1/3-1/3-1/3 不得作为默认布局。版面面积按 scientific importance 分配。
- [ ] 主图、主公式、主结论应获得最多空间；辅助 context 可以不对称地放在边缘或直接删除。
- [ ] 当用户指出“图片太小”时，不允许继续在同一页保留所有原图后做微调；必须重新决定信息优先级，删掉低价值对象。
- [ ] 同页多图时，每张图都必须达到会议室投影可读；否则删图或拆页。
- [ ] 核心内容若依赖 `scriptsize` 才能装下，默认判为 scope/layout failure，应拆页或删内容。

## 14. Simulation slides：最低信息标准

- [ ] 不允许多个 simulation 压成一页三列“标题 + 一句话 + metrics”。若看不到 generative model，观众无法判断实验是否真正检验 claim。
- [ ] 每个 simulation 主 slide 至少包含：
  1. generative equations / DGP；
  2. main manipulated axis / stress factor；
  3. primary estimand / prediction target；
  4. evaluation metrics；
  5. 一句 planned figure description。
- [ ] Comparator / ablation 仅在它本身是 scientific question 时加入，不作为模板必填项。
- [ ] Metric 必须匹配 estimand，不能机械复用 AUC。
- [ ] 极端不平衡问题不能只报告 ROC-AUC；需要考虑 PR-AUC、Brier/log score 或其他概率校准指标。
- [ ] Metric 不能只列名称，应说明统计含义。
- [ ] Planned figure 用一两句自然语言说明即可，不预先强制 Panel A/B/C。真正有结果后再决定 panel layout。
- [ ] Parameter recovery 可作为 mechanism check，但不能取代真正关心的 prediction/discovery target。

## 15. Data / figure slides：主图必须真正大

- [ ] Dataset / experiment slide 是 scientific argument，不是 inventory card。
- [ ] 一个 slide 默认 1 个主图，必要时再加 1 个辅助图。
- [ ] 图片太小时，第一反应是减少图的数量，而不是缩正文或继续拼图。
- [ ] Render QA 必须检查 scientific content 的实际像素 bbox，而不是图片 object bbox。
- [ ] Composite image 有独立 caption 时，应真正裁成独立 panel；不要依赖大 PNG 内部白边。
- [ ] 图和文字之间要有明确 whitespace；caption 必须紧贴对应图。
- [ ] 主图如果只占页面约四分之一，而页面同时有大量正文/小图，应判为 layout failure。

## 16. Discussion slide：优化导师决策，不做 dashboard

- [ ] Discussion questions 默认自上而下排列，不使用三列卡片。
- [ ] 每个问题应满足：一般领域教授无需熟悉内部软件/实现即可回答；答案会实际改变理论、模型、推断或实验边界。
- [ ] 已能内部决定的问题不要浪费导师讨论时间。
- [ ] 一个主问题一行，必要背景一行；不要堆 4–5 个子问。

## 17. Anti-AI-language audit

- [ ] 搜索并人工审阅 `What ...`, `Role in the deck`, `Why it matters`, `Current plan`, `This slide...`, `Interpretation note`, `Prediction target`, `Main takeaway`, `Key message` 等元话语。
- [ ] Slide 应直接陈述 scientific object / claim，不解释“这一页在 deck 中扮演什么角色”。
- [ ] 如果删掉标签后正文完全成立，就删掉标签。
- [ ] Speaker notes 也要去生成过程语言；应写真实讲稿 cue，而不是 deck 制作说明。
- [ ] 允许非对称结构，不要为了“整齐”强制三栏、三卡、三 bullet。

## 18. Backup / appendix 默认克制

- [ ] Research group meeting 默认不自动生成大量 backup slides。
- [ ] 相对次要但理解主线必须的内容，应在主线快速讲；真正不影响主线的内容直接省略或放 speaker notes/source document。
- [ ] 只有用户明确需要 appendix，或存在高概率追问且 notes 无法支撑的关键技术细节时，才加少量 backup。
- [ ] `backup_count / main_count` 应设软警告；接近主 deck 一半时必须重新审视 scope。

## 19. Rendered-slide QA：semantic > mechanical

- [ ] `no overflow / no compilation warning` 不是视觉通过标准。
- [ ] 每页必须判断：第一次看到这一页的人，5–10 秒内是否知道变量是什么、图是什么、比较什么、单位是什么。
- [ ] Figure-heavy slide 检查主图实际尺寸；equation-heavy slide 检查符号是否首次定义；diagram slide 检查 arrow/box geometry；discussion slide 检查阅读路径。
- [ ] Contact sheet 只能做全局密度筛查，关键页必须单页放大检查。
- [ ] Core content 若依赖 `scriptsize`，默认 REVISE。

## 20. Plugin / tooling implementation TODO

- [ ] 将 audience-first、units、DGP、planned-figure、internal-ID、backup 等规则加入 `deck-plan.schema` 或 `validate_deck_plan.py`。
- [ ] 新增 semantic QA 字段：
  - `symbol_defined_on_first_use`
  - `units_present`
  - `one_intellectual_job_per_slide`
  - `main_visual_large_enough`
  - `scriptsize_core_content_absent`
  - `editorial_labels_absent`
  - `backup_justified`
- [ ] 新增 diagram QA 字段：
  - `diagram_needed`
  - `reading_direction_single`
  - `peer_nodes_aligned`
  - `peer_boxes_equal_size`
  - `canonical_arrow_style_used`
  - `arrowheads_projection_readable`
  - `edge_anchors_semantic`
  - `random_diagonals_absent`
  - `edge_crossings_absent`
  - `edge_box_clearance_ok`
  - `diagram_palette_restrained`
  - `container_vs_process_style_distinct`
- [ ] 在 shared presentation styles 中提供 canonical `diagram node`, `diagram container`, `diagram edge`, `diagram optional edge`，让 generator 复用，而不是每个任务重新 invent TikZ style。
- [ ] `validate_deck_plan.py` 对 diagram 页增加软警告：超过 7 个节点、超过 8 条边、超过 2 类 edge style、存在多阅读方向时要求 justification。
- [ ] 增加 rendered-diagram regression：检测 node bbox 对齐、peer node size variance、edge crossing、edge-to-node overlap、arrowhead 最小像素尺寸。
- [ ] 对箭头做投影可读性检查：150–200 dpi render 后 arrowhead 若低于最小 pixel footprint，判为 soft fail。
- [ ] 在 `RESEARCH_PRESENTATION_ANTIPATTERNS.md` 中加入通用失败案例：
  - 三列 discussion；
  - prose-only prior slide；
  - DGP-free simulation summary；
  - tiny multi-panel data slide；
  - dangling formula under diagram；
  - three-box process flow that prose could replace；
  - random diagonal arrows into container corners；
  - peer boxes unequal size；
  - tiny default arrowheads；
  - rainbow node palette；
  - editorial labels masquerading as scientific content。
- [ ] 将这些规则同步到 Codex plugin mirror，并加入 regression eval，避免每个真实项目再次人工返修同类问题。
