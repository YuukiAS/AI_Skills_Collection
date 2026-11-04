# Codex：Phase B 逐轮历史视觉审阅与可核验初筛

RUN_ID=asteria-phase-b-guided-history-review

这是 Asteria Blueprint / Atlas 恢复路线的 Phase B。目标不是重新设计，也不是让模型替用户决定历史资产，而是把 Phase A 已准备好的静态证据按历史对话逐轮展示给用户，让用户用最小精力确认哪些局部值得保留、修复、拒绝或暂不决定。

每次开始本任务、恢复会话或进入新一轮之前，先读取：

`YuukiAS/AI_Skills_Collection@design/frontend-feedback-continuity-20261104`

中的：

`docs/design/frontend-design/ASTERIA_RECOVERY_FRONTEND_VNEXT_MASTER_PLAN_20261104.md`

只需要定位当前阶段和已冻结规则，不要每轮向用户复述整份 Roadmap。

同时读取：

`docs/design/frontend-design/PHASE_A_EVIDENCE_PACK_AND_REVIEW_QUEUE_20261104.md`

本地静态证据根目录：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/`

如果路径不存在，停止并报告，不重新生成 Phase A。

本任务严禁调用 Claude，严禁重新设计产品，严禁修改 Blueprint / Atlas 产品代码，严禁启动 Obsidian、浏览器、Figma 或 Playwright。可以使用 macOS Preview / Quick Look / `open` 展示本地 PNG/JPG/GIF；这正是本任务的用户审阅界面。

## 一、先让用户看见 Phase A 到底是什么

第一次运行时，先打开：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/blueprint/contact-sheet.png`

以及：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/atlas/contact-sheet.png`

告诉用户一句话：这两张分别是 Blueprint 36 个历史版本和 Atlas 历史版本的静态总览，完整原图、关键 PDF 页和 manifest 都在同一证据目录。

同时给用户两个 GitHub 历史入口，方便随时自行回源：

Blueprint：
`https://github.com/YuukiAS/Asteria-Blueprint/blob/archive/asteria-blueprint-version-gallery-20261103/docs/design/version-gallery/VERSION_CATALOG.md`

Atlas：
`https://github.com/YuukiAS/Asteria-Atlas/blob/archive/atlas-visual-history/visual-history/README.md`

第一次只做 orientation，不要求用户马上给出任何设计结论。随后默认从 Blueprint 按时间顺序开始；用户明确要求切换项目时再切换。

## 二、初筛只能依据历史证据，不能依据当前模型审美

每一个版本先读取其归档 metadata / manifest，再只读原始历史 PDF 中该版本对应的用户反馈页。不得只根据 VERSION_CATALOG 的 verdict 或两轮 Pro 摘要决定级别。

Blueprint 原始历史 PDF：

仓库：
`YuukiAS/Asteria-Blueprint@archive/asteria-blueprint-version-gallery-20261103`

路径：
`docs/design/version-gallery/assets/sources/ChatGPT_Asteria-BluePrint-裁决_20261103-1638.pdf`

Atlas 原始历史 PDF：

仓库：
`YuukiAS/Asteria-Atlas@archive/atlas-visual-history`

路径：
`visual-history/source/ChatGPT_建立文献地图架构_20261103-1749.pdf`

优先使用 manifest / catalog 已记录的 `pdf_pages` 精确读取对应页及必要的前后 1–2 页。不要重新通读整本 PDF。

如果某个版本没有可核实的对话页，必须标记：

`HISTORICAL_FEEDBACK = NOT_VERIFIED`

不能凭当前总结补造用户态度。

## 二点五、先判断这轮属于“产品前史”还是“目标产品本体”

每一轮开始前，Codex必须先回答：这个版本当时是不是已经在做今天要恢复的目标产品。

### PREHISTORY_INHERITANCE

适用于原始 Asteria、Asteria 2.0、rc.19、Asteria Next 等作为 Asteria Blueprint 前史的版本，以及其它明显属于目标产品形成之前的探索。

这类轮次的目的不是重新验收旧 UI。Codex必须根据原始 PDF 和后续历史自己总结：

- 这个版本贡献了什么后来 Blueprint 仍可能需要的核心产品构想；
- 哪些只是当时旧宿主、旧侧栏、旧控件、旧布局的实现细节；
- 后来的 Blueprint / Next 有没有继承、改坏或丢失这些构想；
- 哪些具体画面最能证明这些继承资产。

除非某个旧 UI 细节后来直接演化成 Blueprint 的关键能力，否则不得问用户“旧侧栏好不好读”“追踪开关打开后是否清楚”“旧按钮位置是否合适”之类问题。

用户不负责总结产品血统，也不需要对 Codex 的抽象继承总结逐条再次确认。Codex应把继承总结记为自己的 `CANDIDATE` 判断；用户只需要看图并自然表达喜欢、不喜欢、觉得有价值或拿不准的地方。只有出现真正会改变未来产品方向、且历史与用户当前反馈都无法回答的冲突时，才允许额外问一个具体问题。

### TARGET_PRODUCT_REVIEW

适用于已经明确属于 Asteria Blueprint 本体、Asteria Atlas 本体或直接决定当前目标产品结构的版本。

这时才可以细看具体工作面、机制表达、graph / detail职责、实现绑定、证据、返回行为、信息密度和视觉层级。

即使进入 TARGET_PRODUCT_REVIEW，也不能把用户变成旧版 QA。只讨论会影响未来目标产品的局部，不讨论已经没有继承价值的旧实现细节。

每轮 ledger 新增：

`REVIEW_MODE = PREHISTORY_INHERITANCE | TARGET_PRODUCT_REVIEW`

并新增：

- `INHERITABLE_PRODUCT_IDEAS`：Codex根据原始历史提出的候选继承构想；
- `OBSOLETE_UI_DETAILS`：明确不需要用户重新验收的旧实现细节；
- `LATER_INHERITANCE_OR_LOSS`：后续如何继承、改坏或丢失；
- `USER_SCOPE`：本轮真正需要用户判断的最多 1–3 个候选继承点。

用户永远不需要替 Codex总结“这版是什么、为什么重要、后来发生了什么”。

## 三、初筛只有三档，而且只是“审阅优先级”

### DEEP_REVIEW

出现以下任一条件就必须仔细看：

- 当时用户明确表达过局部正面评价，同时又否定其它部分；
- 后续版本丢失了此前得到正面反馈的能力；
- 这是当前候选 / 历史 baseline / 当前比较基线；
- 两轮 GPT Pro 对它的价值判断存在实质分歧；
- 它改变了核心产品工作方式，而不仅是样式；
- 它属于关键错误返修链，必须同时看改前与改后才能理解失败。

DEEP_REVIEW 一轮可以放 1 个版本，或最多 2–4 个必须直接比较的同一历史族版本。

### QUICK_SCAN

适用于：

- 是一个真正不同的方向，但历史反馈基本为负面；
- 没有发现明确需要保护的局部正面资产；
- 主要价值是帮助用户确认“不要再走这条路”。

每轮只展示 1 张代表图或一个小型对照拼图，配极短历史说明。用户随时可以说“这个我要细看”，立即升级为 DEEP_REVIEW。

### ARCHIVE_ONLY

只有以下情况才允许：

- 明确属于未授权生成、当时立即作废；
- 没有独立可恢复视觉；
- 没有发现任何局部正面反馈、独立产品能力或后续继承价值；
- 纯重复失败，且已经有另一个版本完整代表相同方向。

ARCHIVE_ONLY 不能从历史清单删除。只是不主动占用用户审阅轮次；最终必须给用户一个“本次未细看版本”清单，用户可以随时点名恢复。

## 四、基于已核实对话 PDF 的初始优先级种子

以下只是初始审阅优先级，不是产品结论。Codex 必须在每轮回读原始 PDF 后才能最终确认该轮级别。

Blueprint 首批 DEEP_REVIEW 候选：

- R2 / 后续收敛中恢复真实拓扑、关系探索和返回上下文的版本；
- Asteria Next / Blueprint 盲审中出现对象稳定性、状态、时序、计算、消费者链和真实实现追踪的版本；
- PDF 约 172–176 页附近的视觉方向，尤其历史记录中用户曾指出“第三张”有视觉潜力的方向；
- PDF 约 196–206 页的 Workbench R1，必须同时保留“整屏过载”与“实现台局部不错”两条反馈，不得只保留其中一条；多实现 binding、切换和行号按需必须作为局部资产单独审；
- 当前第 36 版 Total Redesign，作为当前最完整比较基线，但不得预设接受。

Blueprint 首批 QUICK_SCAN 候选：

- 已明确退化为叙事/步骤/宣传式说明的早期 R1；
- 已明确被否决但仍代表独立视觉方向的 Figma / system-direction / visual-direction；
- Workbench R1B 的模板 IDE 回归；
- Cartography 学术海报式路线。

Blueprint 首批 ARCHIVE_ONLY 候选：

- 未授权生成且当时明确作废的 IDE 图；
- 原图已经不可恢复、无法形成独立视觉判断的版本。

Atlas 首批 DEEP_REVIEW 候选：

- V05 Visual v1 GPT-6：空间社区、轻论文、稀疏语义关系有历史保留价值，但真实 Obsidian 可读性失败，必须把“方向价值”和“像素/宿主缺陷”分开审；
- V06 → V07 必须作为一个连续审阅轮次：原始反馈是去掉匿名桥梁和无意义关系，但保留真正有意义的科研关系；V07 后来删除全部总览边并形成七分类入口，是关键错误返修案例；
- V08 Astra Visual v2：信息架构、语义缩放和规模约束可能有参考价值，但视觉本身被明确否决，必须分开判断；
- V10 Final Visual Refinement：当前设计候选，必须比较它究竟继承了 V05 什么、修了什么、仍缺什么。

Atlas QUICK_SCAN 候选：

- V01 / V02 MVP；
- V03 Visual Redesign；
- V04 GPT-5.6 Visual v1；
- V09 taxonomy-first Figma；
- V12 一次性领域概念稿。

Atlas ARCHIVE_ONLY 候选：

- V11 当前没有新的视觉交付物，只记录“尚未完成真实移植”的状态，不占用视觉审阅轮次。

任何版本如果原始 PDF 证据与以上种子分类冲突，以原始 PDF 为准，并在 ledger 里写 `TRIAGE_CHANGED_BECAUSE = <具体页码和证据>`。

## 五、每一轮 Codex 必须怎么带用户看

一次只进行一个 review round。不要在同一条回复里塞接下来五轮。

进入一轮后，Codex先准备 1–4 张最能代表问题的现有静态图。优先直接使用 Phase A `priority/` 和 archive 原图；如果需要比较多张，允许在：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/review-rounds/tmp/`

生成一个临时 montage PNG，左上角清楚标 version id，不改变原图。然后用 macOS `open` 打开图片或 montage，让用户实际看到。不要启动浏览器。

图片打开后，Codex 的用户可见文字最多两段短自然段。第一段只说这一轮在历史里的位置、当时用户明确的好/坏，以及后来继承、改坏或丢失了什么；第二段只在必要时给一个简短建议，格式接近“我的建议：保留 X 这个思路，Y 只作为旧实现，不继承”。不得输出大段历史讲解、编号列表或新的设计方案。

历史反馈必须给 PDF 页码。可以短引用户原话，但不能用后来的 Pro 总结冒充当时反馈。

Codex 可以把自己的候选判断用一句自然语言展示给用户，帮助用户不用仔细研究每一张图；但最多一句，不拆成多条，不要求逐条确认。用户可以赞同、反对、补充、只评论其中一部分，或者完全忽略建议只说视觉感觉。Codex再结合历史证据与用户反馈记录到 ledger。不得要求用户总结版本意义。

如果用户已经在上一条消息给出了清楚反馈，Codex必须直接记录并继续下一轮，不能把相同内容重新包装成抽象结论让用户再回答。只有当这一轮出现会改变未来产品方向的真实冲突，才允许停下来问一个具体问题。

## 六、用户不需要填写任何表

用户可以完全按自然语言回答，例如：

“这个实现台可以，整屏不要；多 binding 要；行号默认别显示；第二张配色无所谓。”

或者：

“这几张我都不喜欢，只有空间关系这个思路可以留。”

Codex负责把自然语言转换成记录。不要要求用户回复固定代码、JSON、表格或完整 `KEEP/REPAIR/REJECT` 模板。

只有用户表达真的有歧义时，最多问一个具体问题。能从原话准确判断就直接记录，不要重复确认。

## 七、每一轮必须记录什么

在本地维护唯一 ledger：

`/Users/yuukias/Code/Asteria-Phase-A-Evidence/PHASE_B_REVIEW_LEDGER.md`

每轮追加，而不是重写历史。

每轮记录：

- `ROUND_ID`
- `PROJECT`
- `VERSION_IDS`
- `TRIAGE = DEEP_REVIEW | QUICK_SCAN | ARCHIVE_ONLY`
- `IMAGES_SHOWN`：实际打开给用户看的文件
- `SOURCE_PDF_PAGES`
- `HISTORICAL_GOAL`：当时想解决什么
- `HISTORICAL_USER_POSITIVE`：当时明确认可什么；没有就写 NONE_VERIFIED
- `HISTORICAL_USER_NEGATIVE`：当时明确否定什么；没有就写 NONE_VERIFIED
- `WHAT_CHANGED_NEXT`：后续版本继承、丢失或误改了什么
- `CODEX_CANDIDATE_JUDGMENT`：只允许局部 CANDIDATE_KEEP / REPAIR / REJECT / UNCERTAIN
- `USER_RAW_RESPONSE`：用户本轮原话，尽量逐字保存；不得丢弃上一轮已经给出的视觉反馈
- `USER_INTERPRETED_DECISION`：把原话解释成具体局部的 KEEP / REPAIR / REJECT / UNSURE；若用户只是给视觉偏好而未做产品裁决，按视觉偏好记录，不强行升级成产品决定
- `CARRY_FORWARD`：后续 design brief 必须继承的具体局部
- `FORBID_REVIVAL`：已经明确不要再次复活的具体东西
- `OPEN`：仍然没决定什么
- `CHANGE_REASON`：若后来修改本轮解释，必须写新增证据或用户新决定；没有则 NONE

绝对禁止把“用户喜欢一个局部”解释成“用户接受整个版本”。

## 八、每轮结束如何推进

如果用户对当前轮次已经说清楚，Codex直接把原话和解释写入 ledger，然后立即准备下一轮。默认不要再向用户回放记录，也不要询问“是否继续”。用户没有明确否决某个 Codex 建议，不得视为默认接受；未被用户触及的建议保持 CANDIDATE。只有解释存在歧义或出现高影响产品冲突时，才用一句话说明并问一个具体问题。

如果用户说“不确定”，就记 UNSURE 并继续，不逼用户当场选择。

DEEP_REVIEW 历史线审完后，Codex可以根据已经记录的用户决定生成一个局部压缩结论，但必须保留每个原 version id 和来源页，不能用新总结替换 ledger。

## 九、压缩什么时候才允许发生

只有一个历史族的相关版本都按以上方式处理完，才允许生成压缩结果。

两个版本只有同时满足以下条件才可以被归为同一设计族：

- 解决的是同一个用户任务；
- 核心交互模式没有改变；
- 信息架构和主工作面没有实质改变；
- graph / detail / implementation / evidence 的职责没有改变；
- 上下文保持与返回方式没有实质改变；
- 差异主要是样式、密度、局部布局或同一方向的返修。

只要以上任一项改变，就必须保持为独立历史节点。

压缩结果必须注明包含哪些版本、继承哪些用户当前决定、还有哪些 UNSURE，并链接回 ledger。压缩不是新的产品裁决。

## 十、第一轮怎么开始

第一次 orientation 完成后，默认从 Blueprint 的产品血统开始，但原始 Asteria / Asteria 2.0 / rc.19 等前史必须作为 PREHISTORY_INHERITANCE 审阅，不得逐项做旧 UI QA。必要时可把连续前史版本合并成一个“继承构想”轮次，只要所有 version id、对应 PDF 页和原图都保留可追源。进入真正的 Asteria Next / Blueprint 产品设计后，再提高到 TARGET_PRODUCT_REVIEW 的审阅粒度。

当进入第一个真正 DEEP_REVIEW 的历史族时，务必提示用户：

“从这里开始值得仔细看，因为这条历史线出现了后来可能需要继承的正面资产。”

不要一次把后面的路线都讲完。

## 十一、停止条件

每一轮用户回复后都停止当前分析，先记录 ledger，再进入下一轮。用户随时可以说“今天到这里”，此时保存 ledger 和 CURRENT_POSITION，不做总结大报告。

不得在用户尚未完成历史审阅前启动 Claude、生成最终 design brief、决定最终产品方向或修改产品仓库。
