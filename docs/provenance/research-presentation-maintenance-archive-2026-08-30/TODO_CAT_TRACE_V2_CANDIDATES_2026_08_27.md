# Research presentation TODO candidates — CAT-TRACE v2 review, 2026-08-27

本文件只记录 **可泛化到其他科研 PPT** 的候选规则，不记录 CAT-TRACE 项目本身的科学决定。它是 `research-presentations/TODO.md` 的补充候选，后续通过正常 reviewed-handoff / consolidation 再决定哪些进入 active skill、shared QA、template primitives 或 regression tests。

## 1. 统一的文字层级与 sentence case

- [KEEP_BACKLOG] Research slide title、section subheading、table header、dataset / simulation title、question header 默认使用 **sentence case**；专有名词按正式写法保留。
- [KEEP_BACKLOG] Dataset / Simulation 编号必须有统一模板，例如 `Dataset 1: ...`, `Simulation 1A: ...`；数字与字母必须使用同一字号和基线，不允许 `1B` 视觉大小不一致。
- [KEEP_BACKLOG] 同一 deck 中 `Example`, `Question`, `Design`, `Metrics`, `Comparison`, `Data` 等功能标签只能各有一套样式，禁止 `Victoria example`, `Victoria plant examples`, `Main question`, `Core question` 等随机变体。
- [KEEP_BACKLOG] Inline label 只在“短标签 + 同行内容最多一行”时使用，如 `Example.` 后接一句短句；若内容超过一行、含公式、表格、选项或 bullet，则 label 必须升级为独立 subheading 并换行。

## 2. 新术语 first-use style

- [KEEP_BACKLOG] 领域术语第一次出现时，不仅要展开 acronym，还要使用固定视觉样式。CUHK Beamer 候选：**term 本体使用 `maincolor` + bold，正式英文全称使用中性深灰 italic，定义使用普通正文**。
- [KEEP_BACKLOG] 推荐模式：`\textbf{\textcolor{maincolor}{OTU}} \textit{(operational taxonomic unit)}: ...`。不要把整个定义涂成 accent color，也不要为每个术语画 card。
- [KEEP_BACKLOG] First-use 术语同时回答三个问题：它是什么现实对象、怎么得到、是否等同于附近使用的日常概念。
- [KEEP_BACKLOG] 如果一个术语需要超过约两句才能让目标听众理解，或它是理解后续 3+ 页的前置概念，应考虑独立 background slide，而不是把 glossary 句子硬塞进已有页面。

## 3. 布局选择：单栏、双栏、full-width 的使用条件

- [KEEP_BACKLOG] 两栏只用于**真正 peer-level、可并行比较**的两个对象。对象若是因果/推导/流程关系，优先纵向单栏；不能因为“正好有两个主题”就自动两栏。
- [KEEP_BACKLOG] 双栏 peer objects 必须 top-aligned，render 后实际高度差建议不超过约 3%；heading、font、padding、公式 baseline 必须一致。
- [KEEP_BACKLOG] 若双栏下还有 full-width 内容，必须在源布局中预留独立区域。候选软约束：上方双栏不超过可用内容高度约 55–60%，下方 full-width 至少保留约 22–25%，中间保留明确 whitespace；无法满足就拆页。
- [KEEP_BACKLOG] 不允许在双栏下方悬一条无标题公式或解释句。Full-width 区必须有自己的 scientific role（例如 residual model / shared prediction target）和清楚标题。

## 4. 数学层级：什么可以首行居中

- [KEEP_BACKLOG] **首行独立居中的 display formula 必须是当前页核心 scientific object**：主模型、estimand、theorem statement、关键 identity 或核心 derivation step。Design grid、sample-size list、参数范围、普通 definition 不得因为“是数学”就居中。
- [KEEP_BACKLOG] 普通 design settings 应进入 `Design` table / aligned list，例如 `n`, `m`, `p`, rank, working-set size。
- [KEEP_BACKLOG] `align` 用于连续等式、同一推导链或需要对齐等号的多行数学；`cases` 只用于同一左侧对象下互斥的分支定义；短定义优先 inline / left-aligned definition list；`underbrace` 只在需要把公式项直接映射到语义标签时使用。
- [KEEP_BACKLOG] 禁止连续堆多个彼此无视觉关系的 display equations。若逻辑是 `identity -> target probability -> solve parameter -> limit`，应通过 `align`、短文字桥接或分步结构显式表现顺序。
- [KEEP_BACKLOG] 核心公式的字体与占地必须明显高于普通 notation；如果公式是本页主要内容却只能以小字号放在上方或角落，判为 layout failure。

## 5. Formula-term semantic coloring

- [KEEP_BACKLOG] 当一个核心公式包含 3–5 个可解释组成项时，可使用“公式项 + 对应标签同色”的语义着色，而不是五个同色 box。
- [KEEP_BACKLOG] 同一项内部颜色一致，不同项采用模板兼容的受控 palette；残差/基准项可用中性灰，避免强行五种高饱和色。
- [KEEP_BACKLOG] CUHK 当前模板候选 palette 基于已有 theme colors：主紫 `#72256D`、深紫/酒红 `#780050`、金色 `#D4AF37`、深绿 `#004628`、muted mauve `#AA7CA7`、中性深灰。实际使用时优先 3–4 个 accent + 1 neutral，而非 rainbow。
- [KEEP_BACKLOG] 颜色只承担 category mapping / term mapping，不用来装饰普通 prose；同一语义在全 deck 必须保持同色。

## 6. Diagram 必须是页面中心对象，并通过严格几何验收

- [KEEP_BACKLOG] Architecture / mechanism diagram 应成为页面主要视觉对象。候选软约束：diagram bbox 至少约占 usable width 的 65–70%，usable height 的 50–55%；若达不到，应减少节点或拆页。
- [KEEP_BACKLOG] Diagram 的定义、set difference、shared relation 等若是理解图本身所必需，应整合进 node / brace / caption / in-diagram annotation，不允许在图下面再悬一条“其实这个节点等于……”的孤立公式。
- [KEEP_BACKLOG] 主箭头不得 overlay 节点、文字、其他箭头；不得 edge crossing；不得随机射入 box 角落；edge 必须从语义 anchor 到语义 anchor。
- [KEEP_BACKLOG] 箭头不能短到几乎只剩 arrowhead。Beamer/TikZ 候选：主 edge 可见直线段优先不少于约 10–12 mm；arrowhead 使用显式尺寸（如约 2.8 mm × 2.0 mm），box 边缘保留约 2–3 mm clearance。需要 renderer benchmark 后再固化成 hard threshold。
- [KEEP_BACKLOG] 一个 diagram 只允许一个主要阅读方向。若用户要求 top-to-bottom，则节点布局必须为垂直 edge 让路，不能画完 node 后用 diagonal 修补。
- [KEEP_BACKLOG] 每个 diagram 页都要单页高分辨率 render 检查；contact sheet 不足以验收。任何箭头 overlay / node overflow / dangling formula / reading-order ambiguity 直接 REVISE。

## 7. Main visual size contract

- [KEEP_BACKLOG] “图明显应该放大”必须变成可执行规则。对于 figure-heavy / dataset slide，主视觉块（主图或主图+直接相关辅助图）候选应至少占 usable slide area 的约 40–45%。
- [KEEP_BACKLOG] Side-by-side figure + prose 布局中，主图宽度一般不应低于 usable width 的约 42–45%，高度不应低于 usable height 的约 32–35%；如果仍看不清地图点、legend、axis 或照片对象，应删辅助图或拆页。
- [KEEP_BACKLOG] 两个以上独立视觉对象不能共用一个模糊 caption。若 panel 语义不同，必须提供对应 subcaption；只有真正组成一个整体图时才使用单一 composite caption。
- [KEEP_BACKLOG] Dataset slide 若 rare-tail / prevalence 是核心动机，应优先保留一张 quantitative panel；context visuals 需要裁剪到真正理解采样所需的最小数量，避免三四个 thumbnail。
- [KEEP_BACKLOG] QA 需要检查 **实际 scientific content bbox**，不是图片外框 bbox；大白边 PNG 不能冒充“大图”。

## 8. Metrics 的展示方式

- [KEEP_BACKLOG] Metrics 不得只写成逗号分隔术语串，也不推荐 `Metric — explanation` 的长横线列表。优先使用 compact table；指标很少时可用 `Metric ↑/↓ (meaning)` 的括号结构。
- [KEEP_BACKLOG] 指标方向直接写在 metric label 中，参考 CVPR 等论文常见表格形式，例如 `PSNR ↑`, `SSIM ↑`, `MAE ↓`, `RMSE ↓`。这比额外写“higher is better”更紧凑。
- [KEEP_BACKLOG] 对 coverage 这类不是单调越高越好的指标，用 target notation，例如 `Coverage -> 95%` / `Coverage ≈ nominal`，不要误写 `↑`。
- [KEEP_BACKLOG] 多个同类指标不机械重复方向。例如 `Discovery RMSE ↓` 可在同一行/同一 group 下列 `total / catalogue / open-tail` 三个对象。
- [KEEP_BACKLOG] 推荐 table columns：`Metric | What it checks`。说明必须回答“这个指标对应什么统计性质”，例如 point-prediction error、probability quality、rare-positive ranking、uncertainty calibration，而不是把定义扩写成教科书段落。
- [KEEP_BACKLOG] 多指标必须各有必要性。若两个 metric 都回答同一问题且不会改变方法判断，应删掉一个。

### 外部样例依据

- CVPR 2020 Zero-DCE supplemental 的 quantitative table 使用 `PSNR↑ | SSIM↑ | MAE↓`。
- CVPR 2025 VolFormer supplemental 的 table 使用 `SAM↓ | CC↑ | ERGAS↓ | RMSE↓ | MPSNR↑ | MSSIM↑`。
- 这类顶会表格说明：**方向箭头应该直接绑定 metric 名称；解释 metric 作用则由 caption / nearby text / slide table 第二列承担。**

## 9. Variables / traits / covariates 的呈现

- [KEEP_BACKLOG] 一页要讲 3+ 个 covariates / traits 时，不用分号串成长句。优先使用 2-column compact table、短 bullet list 或 `name (plain meaning)` 结构。
- [KEEP_BACKLOG] Audience-facing slide 不显示内部 field code / encoding，除非代码本身是讨论对象。优先写 `Wind dispersal`，而不是 `Disp_Wind`。
- [KEEP_BACKLOG] 若变量很多但不重要，不全列；只展示理解当前 claim 必需的代表性变量。

## 10. Theory coverage 从“独特问题”出发

- [KEEP_BACKLOG] 选择 theorem / proposition 的第一问题不是“手稿里有哪些结果”，而是：**proposed model 解决了 closest existing methods 不能同时解决的哪些 formal problems？**
- [KEEP_BACKLOG] Main theory coverage map 至少列：problem、formal statement、closest baseline、what is genuinely new、proof status、是否进入主 deck。
- [KEEP_BACKLOG] 一个统计方法组会若理论是主贡献，主 deck 不应只展示一个孤立 theorem；应覆盖支撑主要 novelty 的 2–4 个 formal guarantees，但简单定义/partition identity 不得包装成 theorem。
- [KEEP_BACKLOG] 如果 proof 尚未完成，不用 `Proof idea` 填充空间。可以先准确展示 theorem/proposition statement 和 logical relationship，proof 完成后再加入真正可讲的 proof slide。
- [KEEP_BACKLOG] Theory slide title 可以直接写 formal claim，例如 `Each marked tail has a finite richness limit`，而不是 `Why this matters` / `Theory result 1`。

## 11. Discussion question 的生成责任

- [KEEP_BACKLOG] Discussion / supervisor-decision questions 必须由高层研究推理阶段决定，不交给 layout executor / Codex 临场发明。
- [KEEP_BACKLOG] Target audience rule：假设教授熟悉其本学科基础理论，但不熟悉当前具体 topic、内部 notation、数据工程和项目历史。
- [KEEP_BACKLOG] 每个 question 必须能在不读 repo 的情况下回答；背景最多一两行，随后给 2–3 个真正可选方案及 tradeoff。
- [KEEP_BACKLOG] 同一 discussion slide 的所有问题和 A/B/C options 使用完全相同的左对齐模板；不允许一个居中、一个 prose、一个挤成单行。
- [KEEP_BACKLOG] 内部已经可以直接决定的问题不要拿去问教授；问题的答案必须会改变理论强度、模型约束、计算目标、实验范围或论文主张。

## 12. Reference slide 纵向空间利用

- [KEEP_BACKLOG] References 不是固定小字号模板。条目少时必须增大字号和行距，主动使用纵向空间。
- [KEEP_BACKLOG] 候选规则：reference text block 应占 usable height 约 65–85%，两栏条目数差不超过 1；如果下半页仍有约 30%+ 空白，优先增大字号/行距，而不是保持 7–8 pt。
- [KEEP_BACKLOG] Research group meeting references 正文字号建议不低于约 8.5 pt；如果条目多到做不到，缩短题名或拆页，而不是把所有内容压成小字。

## 13. Anti-AI scientific slide language：多道关口，不是一轮润色

### 13.1 当前 active skill 的缺口

- `scientific-prose` 已经会检查 `This highlights`, `underscores`, 空泛 importance、模板化三点式和 generic future-work，但目前没有覆盖足够多的 **presentation-specific sentence architecture**。
- `research-presentations` 当前把 English slide text 交给 `scientific-prose` 仍偏“可用”，后续应考虑升级为科研英文 slide 的默认 mandatory final pass。
- 单纯要求 Codex “polish the wording” 不足以稳定消除 AI 味，尤其当 layout executor 同时在重新生成 audience-facing prose 时。

### 13.2 推荐生产链

- [KEEP_BACKLOG] **Content-author pass:** 高层 GPT / planner 先完成科学逻辑和 audience-facing 文案；英文科研 slide 默认调用 `scientific-prose`，而不是把措辞全部交给 Codex。
- [KEEP_BACKLOG] **Pattern lint pass:** 对 source text 扫描已知高风险模板句式；hard-fail 项直接改，warning 项进入人工/LLM 复读。
- [KEEP_BACKLOG] **Oral-read pass:** 把 slide body 按讲稿顺序导出成纯文本，逐句问“研究者现场会这样说吗？这句话有没有在评论 slide 自己，而不是陈述 scientific object？”
- [KEEP_BACKLOG] **Rendered text pass:** 编译后再从 PDF / rendered deck 抽取可见文本做第二次扫描，防止 layout 修改重新引入模板句。
- [KEEP_BACKLOG] **Independent QA:** 最终 reviewer 不能只看语法正确；要单独判定自然科研表达、meta-language leakage、repetitive contrast templates 和 internal project language。

### 13.3 Hard-fail / warning 候选

Hard-fail audience-facing patterns（除非引用原文）：

- `This page ...`, `This slide ...`
- `Why this matters`
- `Role in the deck`, `Current plan`, `for advisor feedback`
- `the theorem says ...`
- `This is not X; it is Y` / `this is X, not Y` 作为套路对偶
- `This is not the main ... It checks ...`
- `first-paper ...` / `first paper ...` 作为内部发表规划标签
- `anchor`, `schema calibration`, `regime`, `stress test` 等项目管理语言直接出现在 slide 主文案

Warning / manual-review patterns：

- 句首连续使用 `This ...` / `These ...` / `It is ...`
- `not only ...`、`rather than ...` 仅用于制造“高级对比”而没有必要逻辑
- `Moreover`, `Furthermore`, `Additionally`, `Overall`, `In summary`
- `highlights`, `underscores`, `demonstrates the importance of`
- `delve`, `intricate`, `nuanced` 等在 LLM 科学英语中被发现过度出现的词
- 连续使用分号、em dash、三段对称排比、perfectly balanced 3-item filler

这些 warning 不是“出现即证明 AI”；目标是触发自然性复读和具体化重写。

### 13.4 外部研究依据

- Juzek & Ward, COLING 2025, *Why Does ChatGPT “Delve” So Much?*：在科学英语中识别出 21 个与 LLM 使用相关的过度增长词，典型包括 `delve`, `intricate`, `underscore`。这支持 lexical warning list，但不支持单词级“AI 检测”。
- Wikipedia AI Cleanup 的公开经验总结指出 editorial commentary、`it's important to note`, `it is worth`, `overall / in conclusion` 等是常见机器写作信号；它更适合作为 pattern inventory，而非学术判定标准。
- `harshaneel/humanize` 等公开写作工具把 `This highlights the importance of`, `It is clear that`, `Furthermore/Moreover/Additionally` 等作为需要删除或直接改写的连接语；可作为工程规则参考，但 active skill 不应照搬其“AI detector”主张或任意硬阈值。

### 13.5 关键原则

- [KEEP_BACKLOG] 目标是**科研表达自然、具体、可讲、保真**，不是逃避 AI detector。
- [KEEP_BACKLOG] 优先删掉元话语和模板壳，直接陈述对象、机制、数字、关系和结论。
- [KEEP_BACKLOG] 一条 lexical blacklist 只能做 warning；真正 hard-fail 应优先针对用户已反复拒绝的 sentence templates 和 internal-language leakage。

## 14. 交付前统一格式验收

- [KEEP_BACKLOG] Final QA 增加 `style_consistency_matrix`：slide title、mini-header、inline label、question、example、dataset/simulation numbering、table header、metric direction、formula hierarchy、caption、references 逐项检查全 deck 是否只有一种合法样式。
- [KEEP_BACKLOG] 需要从 compiled PDF / rendered PNG 验收，而不是只检查 `.tex` 宏定义。宏统一但视觉不一致仍然算失败。
- [KEEP_BACKLOG] 对重复失败模式建立 regression list：text overlap、box overflow、tiny main figure、short/overlaid arrows、dangling formula、inconsistent question layout、caption ambiguity、unused reference whitespace、AI meta-sentence。

## 15. Tooling candidate fields

建议未来加入 deck plan / QA：

```yaml
style_contract:
  title_case: sentence
  terminology_first_use: accent_bold_plus_italic_expansion
  question_style: header_then_sentence
  example_style: single_canonical
  centered_display_requires_core_object: true
  metric_direction_in_label: true
  two_column_peer_only: true

language_qa:
  scientific_prose_pass_required: true
  hard_fail_patterns_scan: true
  warning_patterns_scan: true
  oral_read_pass: true
  post_render_text_scan: true

diagram_qa:
  central_visual_required: true
  dangling_relation_text_absent: true
  edge_crossing_absent: true
  edge_overlap_absent: true
  min_edge_length_checked: true
  enlarged_render_reviewed: true

visual_qa:
  main_visual_area_checked: true
  panel_caption_mapping_clear: true
  reference_vertical_space_used: true
```

这些字段当前只作为 TODO candidates，不应在没有 benchmark / reviewed handoff 的情况下直接成为全局 hard schema。
