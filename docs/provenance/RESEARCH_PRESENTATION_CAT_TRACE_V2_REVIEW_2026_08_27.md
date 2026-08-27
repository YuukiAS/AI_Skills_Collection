# CAT-TRACE v2 组会 PPT 批注整理（2026-08-27）

本文件记录 CAT-TRACE 组会 PPT **v2** 的 Acrobat 批注。它首先保存项目事实：用户具体对哪些页面、哪些表达和哪些视觉结果不满意。可泛化的科研汇报规则另行提炼，不把 CAT-TRACE 特例直接当作通用规范。

## 1. 批注来源与颜色约定

- 审阅文件：`group_meeting-v2(1).pdf`，27 页。
- 共读取到 74 个高亮批注，覆盖 P2–P25 和 P27；P1、P26 没有本轮 Acrobat 批注。
- 颜色大致分布：黄色 43、紫色 14、橙色 10、蓝色 6、绿色 1。
- 用户的颜色约定是经验性的：蓝色通常表示 **style / 格式体系**；紫色通常表示 **不像人说话 / AI 味**；黄色和橙色混合记录具体内容、逻辑、格式与视觉问题；绿色用于术语呈现方式。

## 2. 逐页不满点

### P1

本轮无批注。标题页此前已经接受，后续返修默认受保护。

### P2 — expanding species space

- 图中 `known catalogue taxa` 与 `catalogue-external` 发生文字重叠，说明此前所谓 render QA 没有真正检查最终页面。
- OTU 首次出现没有一套稳定的术语样式；需要明确术语是和当前页一起解释还是单独用背景页解释。
- `arthropod` 对统计听众仍然偏领域化，最好配真实或直观视觉对象。
- `Example: ... 255,188 OTUs ... singletons ...` 像把多个事实塞成一条 column 文本；例子应有自己的视觉层级，而不是继续堆正文。

### P3 — future discovery

- `Victoria example` / `Malagasy example` 属于生硬的模板标签，不像自然科研汇报。
- COI 在这里直接出现，但此前没有解释；必须做全 deck 的 first-use 检查，不能只看当前页。

### P4 — TRACE sparsity

- `p is a computational truncation: ...` 的句子结构机械，不像现场会说的话；应直接先定义 `p`，再解释截断在实际模型中是什么意思。
- “固定 prior 会导致 richness 随 truncation 膨胀”既然是 challenge，就必须和解决方案、为什么能解决形成清楚逻辑，不可只作为孤立 bullet。
- `This page explains ... the next page ...` 属于纯元话语，以后任何 audience-facing slide 都不应再出现。

### P5 — TRACE richness calibration

- `Two sources are distinct` 后面却继续塞成一句话；既然是两个来源，应在视觉上分开。
- 四个公式只是纵向堆叠，没有推导顺序、没有文字桥接、相近式子也没有对齐；需要一套固定的数学排版规范，而不是“有公式就居中”。

### P6 — HMSC / CORAL

- CORAL 流程图仍然过于压缩。
- HMSC 不能只解释定义，还要说明为什么它是重要 reference / baseline：其已被广泛使用、能利用 traits / phylogeny / latent factors 等结构，以及 CAT-TRACE 为什么要在它基础上继续推进。
- `CORAL helps ... It does not ...` 这种正反对偶句式 AI 味明显，用户明确要求以后不要再出现同类句式。

### P7 — CAT-TRACE model

- 两栏 peer heading 字体不一致。
- 两栏下面突然悬着 residual dependence 和 discovery equations，却没有清楚的小标题，层级混乱。
- 两栏本身可以保留，但必须真正等高、对称；若下面还有 full-width 内容，必须预留足够空间，否则应拆页。

### P8 — architecture

- 箭头仍然太短、相互压叠/overlay，且有不清楚的连线路径；此前已经多轮返修仍未通过。
- `known-but-unseen catalogue taxa = ...` 又变成 diagram 外的一句公式/说明，破坏图的完整阅读路径。
- 以后 architecture diagram 必须先定拓扑、阅读方向、节点层级、edge routing，再做美化；diagram 本身应成为页面视觉中心。

### P9 — matching

- 正文中随意使用 `+` 连接普通语言，不自然。
- `currently hard/partial only` 像内部项目状态，不像给统计老师看的科研表达。

### P10 — catalogue borrowing

- 公式下面五个解释框的文字实际溢出框外，最终 render 没有被验收。
- `Poll_Abiotic`、`Disp_Wind`、`Glycophyte` 等内部字段/编码不应直接出现在 audience-facing slide；应写真实含义。
- `Victoria plant examples` 与此前 `Victoria example` 又是另一套标签，说明 example style 没有统一。
- 五个公式项需要有清楚区分度；不能全部同色。可以让“公式项 + 对应标签”共享同色，同时采用一套和 CUHK 模板兼容的受控 palette。

### P11 — information before discovery

- 表格首行、首列是否 sentence case 没有规范。
- `may be available / generally unavailable / only coarse mark if modeled / not defensible...` 等短语像数据库状态字段，句式生硬，需要改成真正给人读的表格语言。

### P12 — marked groups

- `Malagasy order-level examples` 不像明确的 example 视觉对象；应统一成规范的 example / callout style。
- `not only how many ...` 等反向补充式句子 AI 味明显，核心结论应正面直接说。
- 本页主变换式太小；既然它是核心科学对象，就应该更大，并用受控颜色突出真正新增的 group index / parameters。

### P13 — residual dependence

- 当前 HMSC vs CAT-TRACE 的自由两栏排版差，阅读路径不清楚；用户明确反感为了“两件事”就机械两栏。
- `This is not just ...`、`..., not evidence of ...` 等句式 AI 味明显。
- 更适合用纵向逻辑：HMSC mean structure → CAT-TRACE mean/residual split → normalized correlation → marginal probability。

### P14 — priors

- `Part 1 / Part 2` 没有必要，应该用真正说明内容的小标题。
- MGP 公式本身可以，但以后必须明确什么时候用 `align`、什么时候 `cases`、什么时候普通 display / inline definitions。
- 末尾两句解释更适合 bullet；同时要建立“什么时候用 bullet”的统一规则。

### P15 — theorem

- 只出现一个 theorem，无法体现 CAT-TRACE 相比现有模型到底多解决了哪些正式问题；用户要求至少形成三个清楚的 theorem / proposition / corollary 层级结果。
- `Why this matters` 是典型 AI / 模板标签，禁止继续使用。
- `the theorem says ...` 等解释口吻不自然。
- `preserves TRACE calibration` 需要守住 claim boundary，避免没有证明到的绝对表述。

### P16 — proof

- 当前 `Proof idea and relation to TRACE` 删除。真正证明尚未整理完之前，不在主 deck 放 proof idea；以后证明完成后再补正式 proof slide。

### P17 — discovery / marginal preservation

- `Under hard matching` / `Under soft matching` 不应碎片化塞进连续 prose；如果要对比，就用统一的 list / subheading 结构。
- `is an estimand partition: ...` 放在公式后面不好看；若需要解释两项，可在公式前解释，或用 `underbrace` 直接标注。
- `This decomposition is scientifically important, but ...` 这种对 PPT 没有实际信息增量的自我评论应删除。
- `Open theory question:` 触发通用 style 问题：什么时候允许“粗体 label + 同行正文”，什么时候必须独立小标题换行，需要统一规则。

### P18 — oracle simulation

- 主图仍然偏小；不能每次靠人工提醒，要建立 main-visual size contract。
- bullet 首字母大小写不统一。
- `theoretical total target: 10.822` 没有说明三组 target 如何组成 10.822；需要表格或结构化解释。
- `this is an oracle ... not a fitted ...` 是用户明确不接受的 AI 对偶句式。事实可以保留，但应直接正面说明实验性质。

### P19 — fitted discovery simulation

- `n in {...}, m=...` 莫名其妙单独居中在首行。首行居中的公式必须是当前 slide 的核心 scientific object；普通 design parameters 应进入 Design 区域。
- metrics 只是术语堆砌，没有方向（高/低好）、没有解释各 metric 衡量什么、为什么需要多个 metric。
- real-data scale 的解释意思可以，但 `for advisor feedback rather than claimed...` AI 味明显。
- simulation 标题大小写需要统一。
- `1B` 中数字与字母视觉大小不一致，属于格式 QA 失败。

### P20 — borrowing simulation

- ablation 用 `|` 生硬隔开不可接受；应使用表格、对齐列表或真正的比较结构。
- metrics 同 P19：不能只列名词，必须说明评价目标和好坏方向。

### P21 — residual-dependence simulation

- `Low-rank truth uses rank 3 or 5` 没解释“哪个矩阵的 rank”，统计老师也不能靠猜。
- `n`、`|W|` 又被作为孤立居中内容，违反信息层级。
- `Core question` 应有 deck-level question style；标题/问句 sentence case 也要统一。
- `rather than forcing all 255k OTUs...` 句子可表达同样事实，但需要去掉模板化对照口吻。

### P22 — Finland dataset

- 主视觉偏小。
- 右侧整块文字可读性差，连续出现 `This ... This ...`；事实、数据规模、问题应拆成明确层级。
- dataset slide 要让第一次看到的统计老师迅速知道采了什么、数据长什么样、这个数据用于回答什么问题。

### P23 — Madagascar dataset

- question 需要统一 style。
- 正文不应把多个普通步骤用 `→` 串起来；如果流程值得画，就画真正 diagram，否则写正常 prose。
- 多个 context image 太小，且两/三个不同图共用一个模糊 caption，caption 失去解释作用。

### P24 — Victoria dataset

- `30,955 × 1,116 → 25,955 × 622` 单独甩数字和箭头，听众不知道过滤了什么；必须说明 raw → filtered 的规则/含义。
- covariates / traits 用大量分号串成一句，不适合 slide；需要明确的变量呈现规范。
- `This is not the main ... It checks ...` 属于已被反复指出的 AI 句式。
- dataset title、主图、辅助图、caption 层级混乱；标题也没有统一成 `Dataset 3: ...`。

### P25 — discussion

- 同一页三个问题出现三套格式：第一题 ABC 居中，第二题没有 ABC，第三题 ABC 全挤在一行。
- 选项是否 sentence case 没统一。
- `Current theorem solves ...` 信息价值不清楚。
- `first-paper` 假定存在后续论文，不适合组会 audience-facing 文案。
- Discussion question 必须由我们根据科研问题和听众决定，不交给 Codex 自己想；统计教授不一定熟悉具体 topic，因此问题必须给足必要背景且能基于统计判断作答。

### P26

本轮无批注。后续只做 regression check，除非上下文重构迫使局部调整。

### P27 — references

- 字体仍太小，页面下半部大量空白。
- Reference slide 必须主动利用纵向空间；条目少时提高字号/行距，而不是固定小字号后留下大片空白。

## 3. 跨页问题分类

### A. 缺少统一的 presentation style system

集中页：P2、P5、P7、P10–P14、P17–P25、P27。

需要统一：sentence case、术语 first-use、example、question、mini-header、inline label、bullet、table header、two-column、formula hierarchy、metrics、caption、reference、dataset/simulation numbering。

### B. 最终 render 没有真正验收

集中页：P2、P7、P8、P10、P12、P13、P18、P19、P22–P24、P27。

反复出现：文字重叠、box overflow、箭头 overlay / 过短、主图过小、caption 失效、两栏不等高、字号不统一、大片未利用空白。以后编译成功不能视为交付成功。

### C. AI 味 / 模板化句式

集中页：P3、P4、P6、P9、P11–P13、P15、P17–P19、P21、P22、P24、P25。

用户反复不接受的模式包括：

- `This page / This slide ...`
- `This is not X; it is Y` / `this is X, not Y`
- `X does ..., it does not ...` 的机械正反对偶
- `Why this matters`
- `the theorem says ...`
- `not only ...` 作为模板化补充
- `rather than ...` 仅为制造对比语气
- `currently ... only` 等内部状态语言
- `for advisor feedback rather than claimed ...`
- `first-paper ...`
- `Victoria example / Malagasy example / Role / regime / anchor` 等项目标签式语言

### D. Audience grounding 不足

集中页：P2–P4、P6、P9–P12、P18–P24。

目标听众是统计学教授：可以假设懂 Bayesian / regression / asymptotics / latent factors，但不能假设懂 OTU、COI、metabarcoding、GBIF、arthropod taxonomy、具体 plant trait encoding、CAT-TRACE 内部 notation。

### E. 数学与信息层级没有规范

集中页：P4、P5、P7、P10、P12–P21、P24。

问题包括：核心公式和普通参数同样居中；不相关公式堆叠；`align` / `cases` / inline definition / `underbrace` 没有选择标准；公式与解释脱节。

### F. Theory 没有围绕“模型真正新增什么”组织

集中页：P15–P17、P25。

Theory 的出发点不是“手稿里有什么 theorem 就放什么”，而是：**CAT-TRACE 解决了哪些 TRACE、HMSC、fixed-list JSDM 单独解决不了的问题？** 主 deck 至少需要三个正式结果层级，并清楚说明它们之间的逻辑关系。当前 proof idea 暂时删除。

### G. Simulation / metrics 没有让统计老师快速判断实验

集中页：P18–P21。

需要分清 Design、DGP、estimand、metrics、comparison；metric 既要说明方向，也要说明它检查哪种统计性质。普通 design grid 不允许作为首行居中公式。

### H. Dataset 页缺少统一交付标准

集中页：P22–P24。

需要统一 dataset 标题与层级，但不强制三页同一布局。主图必须足够大；不同图片需要对应 caption/subcaption；真正重要的 rarity 需要定量 visual；字段/变量需要正常人能扫读的结构。

## 4. 第二轮已经确认的方向

用户在本记录之后确认：

1. 全 deck 使用 sentence case。
2. 新增一页简短背景，集中讲清 metabarcoding / OTU / COI 与 species 的关系。
3. HMSC 与 CORAL 拆成两页。
4. CAT-TRACE finite catalogue vs open tail 保留两栏，但必须等高、对称；底部 full-width 内容只能在有足够空间时保留。
5. residual dependence 改成纵向逻辑，不再机械两栏。
6. Theory 以至少三个正式结果体现 CAT-TRACE 相比现有模型新增解决的问题；当前 proof idea 删除，完整 proof 等真正完成后再补。
7. Dataset 1–3 统一标题与文字层级，但不强迫同一种图片布局。
8. 新术语需要统一 first-use style（粗体/颜色/斜体组合应服从模板）。
9. Metrics 推荐 table 或括号结构，并使用 `↑/↓`（或 target，如 coverage → nominal level）表达评价方向，同时解释 metric 作用；多个同类 RMSE 不机械重复箭头。
10. 首行居中的公式只允许核心 scientific object；`n={...}` 等 design settings 不得孤立居中。
11. Diagram QA 进一步收紧：箭头不得 overlay、不得过短，关系必须完整收进图中，diagram 应成为页面视觉中心。
12. 需要建立模板兼容的受控 palette；公式项与对应标签可同色，但不同项需要足够区分度。
13. 图片大小、reference 纵向空间利用、question style、数学环境选择都必须变成可复用标准，而不是每次人工判断。
14. AI 味是当前最大问题，需要多道写作与验收关口；不能只要求 Codex “最后润色一遍”。

## 5. 下一步

- CAT-TRACE v2 → v3 的具体执行说明写入 TRACE repo，由 Codex 读取后实现。
- 本轮可泛化经验单独整理为 research-presentation TODO candidates，并记录 AI-like scientific slide prose 的外部研究依据。
- active presentation skill / `scientific-prose` 的正式升级仍应走 AI_Skills_Collection 自己的审阅与合并流程，避免一次项目返修直接改坏全局规则。
