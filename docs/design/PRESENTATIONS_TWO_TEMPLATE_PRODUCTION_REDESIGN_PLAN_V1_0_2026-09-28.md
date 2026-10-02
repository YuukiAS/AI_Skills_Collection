# Presentations 双模板生产架构重设计 Plan

**Plan version:** 1.0  
**Status:** READY FOR CRITIC REVIEW / NOT EXECUTION AUTHORIZATION  
**Date:** 2026-09-28  
**Repository:** `YuukiAS/AI_Skills_Collection`  
**Target plugin:** `presentations`  
**Design topic / task key:** `presentations--two-template-production-redesign`  
**Repository baseline reviewed:** `952f92f6b59d4cc3b6294b8eb3a31ec3b5b342d5`

本 Plan 是一次完整重做，不是对 `PRESENTATIONS_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md` 的小修补。若本 Plan 获得 Critic PASS，它将成为后续 implementation proposal / Goal / Kickoff 的设计依据；旧 V0.1/V0.2 继续保留为历史证据，045 继续保留为已完成的局部回归加固记录，但二者都不能替代本轮批准。

本 Plan 只冻结产品方向、架构、TODO 归属、Capability Gates、迁移与恢复边界。它不修改 production source，不创建 implementation branch/worktree，不启动 Codex Executor，不运行付费评审，也不授权发布。

---

## 0. 本轮冻结的用户决策

1. **以后任何演示文稿任务都必须先进入 `presentations` plugin。** 包括新建 deck、重构 storyline、现有 deck 返修、局部编辑、Tutorial、组会、seminar、oral/defense、paper talk、PPTX/Slides 编辑。`presentations` 是统一前门，可以按任务复杂度走轻量或完整路径，但不能被绕过。
2. **仓库只维护两个内置模板：**
   - `cuhk-research`：现有 exact CUHK Beamer，主要用于组会、导师讨论、科研进展、seminar、paper talk、QE/oral/defense 等正式科研场景；
   - `course-standard`：根据用户提供的老师课程 PDF 重新复现的标准 Beamer，主要用于 Tutorial、lecture、课程讲解、公式推导和通用教学 deck。
3. 用户或 venue 明确提供的锁定模板可以作为 **external locked input** 原样保留，但不进入内置模板库，也不形成第三个默认模板。
4. 当前 `docs/plugin-todos/presentations.md` 的全部有效 TODO（tracking `#29`–`#48`，以及 `#29` 内的独立失败项）都必须在本 Plan 中获得明确机制、Gate、阶段或 evidence disposition；“覆盖”不等于无证据地全部立刻实现。
5. 新架构不再以 schema、packet 字段、gold-layout 命中或测试数量作为产品中心。普通用户最终消费的是完整 deck、真实 render、可复制文本、可验证引用和可继续编辑的 source。

---

## 1. 为什么必须重做，而不是继续补规则

当前 `presentations 0.3` 已经有真实能力：来源保真、research-group-meeting 规划、exact CUHK、真实 render、contact sheet、existing-deck revision gate、accepted-element preservation、first-use 检查、scientific-prose handoff 和独立视觉 review。

但 CAT-TRACE v4–v14 的连续真实返修证明了一个更深的问题：**规则越来越多，production path 仍然可以产出“形式合规但讲不清、看不清、review 范围不诚实”的 deck。** 典型表现包括：

- 每页都能解释自己在做什么，但页与页之间没有必然关系；
- 术语“定义过”却仍在听众真正理解前被使用；
- 图、公式、diagram 都存在，但没有围绕观众需要读出的 claim 组织；
- Executor 生成了 packet、render 和 coverage matrix，却仍漏过明显碰撞、短箭头、细小图中文字和窄栏强行缩字；
- 局部 reviewer 看了少数页，却给整套 deck 全局 PASS；
- 新增局部规则后，旧的 geometry、spacing、citation、language 要求反而被遗忘；
- 教学 deck 仍没有独立模式，只能借用 research/business 路径。

因此本轮不再继续向现有 `deck-plan.yaml`、guardrail 或 TODO 堆同义字段，而是重建正常生产链：

```text
统一前门与任务模式
  -> 来源/证据边界
  -> 语义故事板：听众为什么现在需要这一页
  -> 页面构图：这一含义怎样占据页面
  -> 领域、写作、可视化协作
  -> 两个模板适配器之一
  -> 真实编译、逐页 render、整套 contact sheet
  -> scope-honest 独立 review
  -> 有界返修与最终交付
```

---

## 2. 已核实的事实来源

### 2.1 仓库事实

本轮实际读取了最新 `main` 的：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/AI_SKILLS_MAINTENANCE_BOARD.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- `docs/plugin-todos/presentations.md`
- `docs/plugin-changelogs/presentations.md`
- `docs/design/PRESENTATIONS_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md`
- `automation/reviewed_handoff/tasks/045_presentations_real_use_regression_hardening/PLAN.md`
- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/template-routing.md`
- `skills/tools/documents-media/presentations/shared/ppt-skill-routing.md`
- `profiles/presentation-desktop.json`
- `skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source/**`

当前事实：plugin version 为 `0.3`，capability status 为 `baseline`；`Unreleased` 没有待发布变化；exact CUHK 仍是 desktop research 默认路线。

### 2.2 用户提供模板来源

- `CUHK Template.pdf`，SHA-256：`a62a4bb5ec2296b875ffe9ff8c1d850b88797e27a74aac7d64f576abb91daa7e`
- `CUHK Template.zip`，SHA-256：`5cbe4a545d8abbab007f5f0aceec405138f8035b9dcb09c617e1e7cf7b525ee9`
- `Chapter1.pdf`，SHA-256：`ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7`

`Chapter1.pdf` 是 50 页、默认 Beamer 4:3 页面（约 `128 mm × 96 mm`），由旧版 Beamer/pdfTeX 生成。可见风格是黑色顶部带、蓝色 frame-title 带、白色正文、蓝色圆点、右下角页码、Nimbus Sans 正文与 Computer Modern 数学。PDF 中黄色、橙色、绿色、青色标记属于后加的 PDF Highlight annotations；它们不是模板元素，不能复现进 `course-standard`。

### 2.3 外部核查与采用决定

- 当前 Beamer 正式版本为 `3.78`（2026-08-20）。Beamer 官方说明其外观由 template system 控制，适合用两个受控 adapter，而不是复制整套 class。
- LaTeX 的 tagged PDF / PDF/UA-2 能力在 2025–2026 明显推进，但现有 Beamer 路线不能据此直接宣称已获得完整 PDF/UA-2。首轮 release 只承诺真实文本层、复制/搜索、普通数字与引用提取正确；完整 tagged PDF/accessibility 作为后续独立能力研究，不冒充当前完成。
- 不采用 `ltx-talk` 替换 Beamer：它对 tagged presentation 很有潜力，但 2026 年仍有与 Beamer 行为兼容相关的活跃问题；本轮以稳定复现现有两个模板为优先。

采用状态：

```text
Beamer 3.78 template system: RUNTIME_DEPENDENCY / ADOPTED
LaTeX tagged PDF guidance: REFERENCE_ONLY for future accessibility work
ltx-talk: REVIEWED_NOT_ADOPTED in this round
第三方 Beamer theme packs: REJECTED; 用户已冻结两个模板
```

---

## 3. 产品边界与正常入口

### 3.1 统一前门

所有含 slide/deck/PPT/Beamer/Slides 语义的任务先进入 `presentations`。前门只负责识别模式、模板、交付格式、来源与风险，不要求所有任务都走同样重的流程。

四个生产模式：

| 模式 | 典型请求 | 必经步骤 |
|---|---|---|
| `new-deck` | 从论文、报告、课程材料、代码结果新做一套 slides | 完整语义故事板 → 构图 → 模板 → render → review |
| `existing-deck-revision` | 按导师/用户批注继续返修已有 deck | reviewer-seen baseline → accepted-element ledger → 定向修改 → 全套回归 |
| `local-edit` | 改一个标题、颜色、对齐、页码或局部对象 | 保留模板与内容，只做局部 edit + affected-page render；仍由 plugin 判断不可越界 |
| `plan-only` | 只要 storyline、页级结构或 speaker notes | 完成语义故事板即可，不伪装成已完成 deck |

普通用户不需要知道 `generate_research_presentation_production_entry.py`、validator 名称、schema 或内部 mode token。

### 3.2 新 deck 默认交付

没有显式要求 editable PPTX/Slides 时，新的内置模板 deck 默认交付：

```text
source-editable .tex
compiled PDF
per-page PNG render
contact sheet
speaker notes / backup source when task requires
source/citation manifest
review summary
```

显式要求 editable PPTX/Slides 时，`presentations` 仍负责内容与 QA，再委托官方 Presentation/Slides adapter；本轮不增加第三套内置 PPTX 模板，也不把整页图片伪装成可编辑 PPTX。

---

## 4. 双模板合同

### 4.1 内置模板只有两个

#### A. `cuhk-research`

用途：

- 组会与 supervisor discussion；
- research update、seminar、paper talk、journal club；
- QE、oral、defense；
- 其他具有 CUHK 研究身份且没有 venue-locked 模板的正式学术演示。

冻结特征：

- exact source authority：`shared/templates/cuhk/beamer/source/`；
- 约 16:9，CUHK 紫 `#72256D`，Times New Roman；
- title slide、顶部 section navigation、底部导航/页码、logo 与 safe zone 保持 exact template contract；
- template 只提供视觉和布局 primitives，不强迫 `Introduction / Methods / Results / Discussion` storyline；
- ordinary explanatory prose 默认中性色，紫色只用于冻结的 semantic roles；
- 允许按内容需要使用全宽、左右栏、图主导、公式主导、model closure、Question/Background 等 composition，但不能破坏模板身份。

#### B. `course-standard`

用途：

- Tutorial、lecture、课程讲解；
- 定义—例子—推导—练习式数学/统计教学；
- 无需 CUHK branding 的通用标准 Beamer。

冻结目标：基于 `Chapter1.pdf` 重新实现**视觉系统**，不复制课程正文。

冻结特征：

- 4:3 默认 Beamer 页面，约 `128 mm × 96 mm`；
- 黑色顶部带 + 蓝色 frame-title 带 + 白色正文；
- 蓝色一级 bullet、简洁嵌套层级、右下页码；
- Nimbus Sans/等价开源 sans 字体与 Computer Modern/兼容数学字体；
- 支持章节目录页、定义页、公式推导页、例子页、算法步骤页、表格页、references 页；
- 不包含 CUHK logo、顶部 section mini-frame、紫色 accent 或复杂品牌装饰；
- 不复现 PDF 的黄色/橙色/绿色/青色 highlight annotations；教学强调由内容层显式请求，不能成为全局模板默认。

### 4.2 模板选择

| 场景 | 默认模板 |
|---|---|
| 组会、科研进展、导师讨论、seminar、paper talk、journal club | `cuhk-research` |
| QE、oral、defense | `cuhk-research` |
| Tutorial、lecture、课程讲解、公式推导 | `course-standard` |
| 泛用非品牌 Beamer | `course-standard` |
| 用户/会议/课程明确给出模板 | external locked input，优先于两个默认模板，但不加入内置模板库 |
| 返修已有 deck | 保留现有模板；不因本轮只有两个内置模板而擅自换皮 |

用户明确指定模板时直接服从。只有模板选择会实质改变交付且无法从场景判断时，才询问一次；不能每次都把两种模板再抛给用户。

### 4.3 模板不拥有内容逻辑

两个模板都不得决定：

- deck 顺序；
- 哪一页必须出现；
- theorem/figure/table 的数量；
- 是否使用 diagram；
- 结论强度；
- 数据、公式、引用或科学解释。

模板只实现经过批准的 composition contract。

---

## 5. 目标架构

### 5.1 一套共享核心，不新增第三个 presentation plugin

保留 `presentations` 作为唯一用户入口。`research-presentations` 与 `business-presentations` 暂时保留触发兼容性，但 production logic 下沉到 shared core；后者不再分别维护一套故事板、模板或 QA 规则。

Teaching 不是新的顶级 plugin/skill，而是 shared core 的 mode policy。若后续真实业务 deck 证明两个模板不足，必须重新进入 Planner–Critic；本 Plan 不预建第三套模板。

### 5.2 七层正常生产链

#### Layer 1 — Request / mode / deliverable router

冻结：任务类型、目标听众、时长、语言、交付格式、模板、是否 existing deck、是否要求 speaker notes/backup、是否存在 external locked template。

该层解决“所有 PPT 必须调用 presentations”，但不把小编辑升级成完整重做。

#### Layer 2 — Source and evidence boundary

建立 source anchors：论文页码、报告章节、代码输出、图表、数据、已有 slides、导师批注、课程材料。Domain owner 决定科学正确性；`presentations` 不能因为故事需要而改 estimand、公式、图像含义或引用支持关系。

真实证据不足时，只允许：标为未知、转为 next step、放进 speaker notes/backup，或删除。禁止用装饰图、合成数据或 generic cards 假装证据存在。

#### Layer 3 — Semantic storyboard

只回答“听众为什么现在需要这一页”，不回答两栏还是三栏。

Deck-level：

- audience current state；
- talk objective / decision update；
- duration and attention budget；
- start state → end state；
- section dependency map；
- key uncertainties / decisions；
- template and deliverable contract。

Page-level 最小 contract：

- `page_job`：这一页唯一主要工作；
- `audience_before` / `audience_after`；
- `required_evidence` 与 source anchors；
- prerequisites / first-use dependencies；
- intended takeaway；
- visible content obligation；
- notes/backup obligation；
- incoming transition / outgoing unresolved question；
- revision preservation constraints（仅 revision mode）。

这里不得出现 `two-column`、`RESULT_FIGURE`、`density=medium`、字号、坐标或 renderer primitive。

#### Layer 4 — Page composition

把 semantic brief 转成页面形态：

- 选择 text / equation / table / plot / image / diagram / mixed composition；
- 主对象、辅助对象、阅读顺序、空间比例；
- split / merge / full-width / side-by-side / sequential staging；
- 角色驱动的字号、公式尺度、色彩、caption/source 区；
- responsive fallback：放不下时优先重排、拆页、换形态，不默认缩字。

组成选择必须说明为什么比更简单的替代更好。Diagram 先过 utility gate，再进入 geometry；table 只有在同属性反复比较或数值对齐时使用；连续论证优先短 paragraph；可独立并列事实才用 bullets。

#### Layer 5 — Domain / language / visualization handoffs

- `statistical-modeling`、`medical-imaging`、`bioinformatics` 等负责专业语义；
- `scientific-visualization` 负责图型选择、坐标、误差/不确定性、可视编码和 presentation-specific redraw；
- Clear Writing / `writing-style` 在结构、公式、claim、citation 冻结后负责可见文案与 notes 的自然表达；
- `presentations` 在 handoff 返回后重新检查 page job、first-use、长度、口头可讲性和 rendered fit。

写作插件不能接管 layout；presentation 不能静默改变领域结论。

#### Layer 6 — Template adapter and renderer

`cuhk-research` 与 `course-standard` 消费同一 composition contract。Adapter 只负责 template primitives、fonts、safe zones、标题/页脚、章节导航、source/citation 区、编译和资产放置。

禁止：

- 没有合适 gold composition 就阻止生成；
- 用 whole-slide image 冒充可编辑 source；
- 为了模板一致把所有页面做成同一布局；
- silent fallback 到 generic cards。

#### Layer 7 — Rendered review and bounded repair

必须同时看：

- 每页高分辨率 render；
- 整套 contact sheet；
- source/citation/text extraction；
- review scope；
- existing-deck baseline diff（revision mode）。

开发期可以迭代修复，但只有每轮有可观察进展时继续。若同类 blocker 连续出现而没有实质改善，返回 Planner/实现层查根因；不靠无限 reviewer 循环。

---

## 6. 核心机制

### 6.1 First-use、符号与所有可见文字

最终 deck scan 必须覆盖：标题、正文、figure legend、axis/tick、panel title、table cell、diagram node、annotation、caption、source line 和 baseline display name。

为每个方法、缩写、数据集、符号、条件层级记录其：

- audience-facing first allowed anchor；
- prerequisites；
- first visible use；
- first explanatory use；
- later reintroduction requirement。

该 registry 是从最终可见内容与 storyboard 派生的 review artifact，不是新的长期数据库。

### 6.2 Transition map

每一页记录：

```text
这一页结束时听众知道什么？
还不知道什么？
下一页为什么必须出现？
```

句内、页内、页间至少存在一种明确关系：因果、时间、推理、比较、限制、问题—答案或机制展开。不能把独立正确的句子简单并排。

### 6.3 Audience-copy firewall

以下内容默认不能进入可见 slides：

- `V1/V2`、internal build state、workflow/status token；
- `current construction`、`route promotion`、`Theory target` 等项目管理措辞；
- 为 reviewer 或 Executor 写的 checklist 语言；
- 未证明目标写成已成立结论。

允许在 notes / internal evidence 中保留，并翻译成观众需要的科学状态、限制或下一步。

### 6.4 Scientific-object primitives

本 Plan 不固定每类页面唯一布局，但冻结以下行为合同：

- **Result figure：** 围绕 claim 重画；图内字体、axis、legend、panel label 可读；caption 说明观众要看什么；
- **Diagram：** 关系本身必须值得画；node 是真实科学对象/操作；edge 有结构含义；边界、长度、间距、箭头头部和文字 clearance 一致；
- **Math/theory：** 区分 definition、setting、estimand、assumption、theorem、derivation、guarantee；不能都做成居中大公式；
- **Simulation：** 明确 DGP、oracle/generative check、fitted recovery、estimand、baseline、metric direction、sample size/seed/reproducibility；
- **Model closure：** 多页组件讲解结束后，必须让听众重新拼回完整模型/流程；不是再画一张无信息量流程图；
- **Question/Background：** Question 必须对应真实决策；窄栏放不下正常字号时改成全宽或底部横区，不继续缩字；Background 只保留回答所需事实；
- **Table/list/paragraph：** 按信息关系选择，不把一个简单关系拆成 cards + diagram + prose。

### 6.5 角色驱动的视觉系统

每个模板分别定义角色，而不是逐页自由配色：

- deck title / frame title；
- section label；
- ordinary body；
- definition / example / takeaway / question / limitation；
- core formula / supporting formula / inline math；
- figure caption / source / footnote；
- warning / negative result；
- reference entry。

普通说明文字默认中性。整句 accent 色只有命中批准角色时才合法。

### 6.6 Citation、bibliography 与文本层

每套 research deck 必须统一：

- on-slide role labels：`Source:` / `Figure:` / `Data:` / 简短 author-year；
- References 页面来自真实 BibTeX、Zotero、journal metadata 或其他权威元数据；
- 禁止作者手写或模型改写论文标题；
- final PDF 运行文本提取/copyability 检查：普通数字、年份、页码、引用、英文/中文和主要数学符号不能被错误 Unicode 映射；
- 可读 citation 仍须验证支持关系；支持正确但不可读也不能 PASS。

首轮不宣称 PDF/UA-2 完成，只承诺上述真实交付行为。

### 6.7 Advisor questions

导师/答辩讨论问题进入 visible slide 前，内部 brief 必须回答：

1. 答案会改变哪个真实项目决定；
2. 为什么现在要决定；
3. 当前听众是否有能力回答；
4. presenter 当前倾向；
5. 最可能追问/反驳；
6. 准备好的简洁回答。

可见页面通常只保留 Question + 必要 Background/options；追问准备放 notes/review artifact。

### 6.8 Review scope 与完成权

每次 review 必须声明：

- review object / candidate identity；
- reviewed pages；
- reviewed requirements；
- unreviewed pages/requirements；
- source/render identity；
- item-level observations。

只有 mandatory global requirements 和所有目标页都被实际检查时，才能给 global PASS。局部 review 只能给局部结论。

Executor 的 `READY_FOR_REVIEW` 需要展示原 finding 在 final render 中怎样被处理；“改过 source + 生成文件”不够。最终 PASS 由独立 reviewer 给出，不能由 generator/Executor 自签。

### 6.9 Existing-deck revision

必须保留：

- reviewer-seen baseline；
- accepted-element ledger；
- targeted feedback；
- allow-to-change / must-preserve 边界；
- revised source 与 full rerender；
- affected page high-resolution review；
- deck-wide should-not-change regression。

局部修改不得变成全局 redesign；新版本必须与 reviewer 真正看过的版本比较。

---

## 7. 当前 TODO 全覆盖矩阵

### 7.1 Tracking #29 内部失败项

| #29 子项 | 本 Plan 的机制 | 主要 Gate |
|---|---|---|
| first-use 是顺序约束 | semantic dependency + first-use registry + final visible-text scan | G2 |
| scoped review 不能全局 PASS | review scope contract + unreviewed requirements | G9 |
| 新/重写页需 pre-writing brief | page semantic contract | G2 |
| Planner/version 语言泄漏 | audience-copy firewall | G2 / G8 |
| diagram 要有 utility floor | diagram utility gate，再做 geometry | G4 |
| example 到 takeaway 缺解释桥 | transition/inference bridge | G2 |
| 英文仍不自然 | scientific freeze 后 Clear Writing handoff + spoken review | G8 |
| 简化删掉 dataset/object 的作用 | `required_evidence` + `why_now` + page job | G2 |
| visible text 层未全覆盖 | final visible-text inventory | G2 / G6 |
| result figure 没围绕 claim | claim-first figure contract + scientific-visualization handoff | G4 |
| 新 diagram 规则覆盖旧 geometry | cumulative geometry invariants regression bank | G4 |
| 符号与 conditioning 层级不清 | symbol/level registry | G2 / G4 |
| oracle 与 fitted simulation 混淆 | simulation-role contract | G4 |
| 只和差的上一版比较 | best accepted baseline + accepted-element ledger | G7 / G9 |

### 7.2 Tracking #30–#48

| Tracking | 当前问题 | Plan disposition |
|---|---|---|
| #30 | advisor question 的决策价值与可回答性 | 纳入 advisor-question brief、speaker notes 与 G2/G8 |
| #31 | 句间与页间过渡机械 | transition map，纳入 semantic storyboard 与 G2 |
| #32 | accent colour 漂移 | template role token contract 与 G3/G5 |
| #33 | citation、bibliography、PDF text layer | delivery contract 与 G6 |
| #34 | audience/page-job brief 有效但未产品化 | 成为 Layer 3 正常入口，G2 |
| #35 | full-deck audience-context / responsive layout 回归 | contact-sheet deck review、responsive fallback、G3/G8 |
| #36 | coverage matrix 自证 READY | finding-level render evidence + independent review，G9 |
| #37 | packet 齐全仍漏明显碰撞 | high-resolution rendered-object QA，G3/G4/G9 |
| #38 | 公式/正文/强调尺度漂移 | role-driven type/math scale，G3/G5 |
| #39 | diagram semantic purpose 与 geometry | two-stage diagram gate，G4 |
| #40 | table/list/paragraph primitives 漂移 | composition grammar，G3 |
| #41 | complex model 无 closure page | model-closure primitive，G2/G4 |
| #42 | Question/Background primitive 不稳定 | responsive Question primitive，G3/G5 |
| #43 | slide source/figure citation 不统一 | 合并进入 #33 delivery contract，保留 source locator，G6 |
| #44 | canonical edge/node renderer 仍缺证据 | 不预建新 geometry engine；现有 invariants 进入 regression，新的 renderer-level扩展须真实复现后再开 bounded amendment |
| #45 | deck-wide style / terminology hierarchy | consistency pass + template roles + first-use，G2/G3/G5 |
| #46 | math/theory hierarchy | math/theory role contract，G4 |
| #47 | simulation/metric/structured facts | simulation page contract，G4 |
| #48 | natural scientific slide language | Clear Writing/scientific-prose handoff + rendered reader-effort review，G8 |

已由 045 推广的 footer safe zone、first-use、diagram geometry、space use、figure readability、English final pass 全部进入 regression bank；本轮不把它们当“已经永远解决”。

---

## 8. Capability Gate Matrix

所有正式 release gate 必须由**同一个 final candidate、同一个 production identity**直接通过。机械 tests 只是前置证据，不能替代完整 deck 判断。

| Gate | Capability / claim | Why distinct | Normal entry | 必须看到的证据 | 明确失败 | Regression boundary | Final candidate |
|---|---|---|---|---|---|---|---|
| G1 统一发现、路由与模板选择 | 任何 PPT/deck 请求都进入 `presentations`，并正确选择模式/模板/交付 | 证明用户能自然触发，不是 helper 可用 | 新 deck、返修、local edit、Tutorial、组会 | installed plugin identity；自然请求 routing trace；两模板选择；小编辑走轻量路径 | 绕过 plugin、研究/教学模板选错、反复询问已可推断选择 | business/existing PPTX route 不被误改；显式用户模板优先 | 是 |
| G2 语义故事板、first-use 与连续叙事 | deck 顺序、page job、prerequisite、符号、transition、advisor decision 均成立 | 与视觉好看不同，证明“讲得通” | research + teaching 完整 deck | source-grounded storyboard；transition map；first-use/symbol report；完整 speaker flow review | 页面孤立、术语提前、结论无桥、问题无决策价值 | 不改变 domain truth、公式、结论强度 | 是 |
| G3 页面构图、视觉层级与响应式布局 | 页面空间真正服务主对象，primitive 与 typography 稳定 | 与语义正确不同，证明“页面可读” | 两模板的图/公式/表/Question/长短内容页 | 高分辨率 render；type scale；safe zone；contact sheet；split/merge fallback | 局部拥挤+大空白、缩字、accent 无语义、碰撞、同页 container 过多 | intentional sparse transition / take-home 页不能被误杀 | 是 |
| G4 科学对象与专门页面 | diagram、figure、math/theory、simulation、model closure 科学角色正确且可见 | 这些对象有领域和几何双重风险 | math-heavy、figure-heavy、simulation-heavy、复杂模型 deck | domain owner evidence；claim-first redraw；diagram utility+geometry；oracle/fitted distinction；closure page | fake evidence、图内字不可读、diagram 无价值、公式层次错、simulation job 混淆 | figure-free theory 页、compact legitimate diagram 保持正常 | 是 |
| G5 两模板真实消费与复现 | production path 只使用两个 canonical built-in templates，且 visual identity 精确 | 证明不是“写了模板说明但实际没加载” | new research deck + new tutorial deck | source hash/manifest；compiled render；template-specific page skeleton；font/page-size/header/footer checks；人工视觉比较 | 使用 derived scaffold 冒充 exact、混用模板 token、course template 带入 highlight annotation | external locked template pass-through 不被计作第三模板 | 是 |
| G6 引用、bibliography 与 PDF 文本交付 | 引用可定位、bibliography 真实、PDF 可搜索复制 | 视觉 PASS 不能证明交付文本正确 | research deck with citations + references | metadata verification；house style；`pdftotext`/copy tests；年份/数字/页码/引用抽查 | 伪造/改写标题、role label 漂移、ToUnicode 错、视觉可见但复制乱码 | 无 citation 的内部 tutorial 不被强制制造 references | 是 |
| G7 Existing-deck revision preservation | 定向修复不破坏已接受内容，不从头重做 | 新建能力不能证明返修可靠 | 真实 reviewer-seen deck + targeted feedback | baseline、accepted ledger、source/render diff、affected-page review、whole-deck should-not-change | unrelated redesign、accepted element 回归、和错误 baseline 比较 | 合法的全局重构需用户明确授权 | 是 |
| G8 自然语言与整套读者负担 | final deck 能口头讲、标题/句子/过渡自然，教学/科研语体匹配 | 机械 grammar 或单页检查不能证明全场可讲 | English research + Chinese/English tutorial | Clear Writing handoff evidence；scientific freeze；rerender；spoken-read review；deck sequence review | memo/AI 式语言、模板标题、内部状态、dataset 作用被删、final prose 导致 layout 回归 | 写作层不得改公式、数值、citation、layout ownership | 是 |
| G9 Review scope、独立判断与完成权 | reviewer 看到了其声称审核的完整对象，global PASS 不越权 | 证明 completion 可信，不只是 artifact 存在 | 任何 pre-final / final review | review scope；item-level observations；unreviewed list；candidate identity；原 finding closure | 局部 review 给 global PASS、自签 PASS、只有 top-level score | reviewer 错判可追加裁定，但不涂改原记录 | 是 |
| G10 跨模式真实使用与发布一致性 | 同一 final candidate 在 CUHK research、course tutorial、revision 三类正常任务均可靠 | 防止只针对 CAT-TRACE 或单模板调参 | frozen final batch | known regression bank + unrelated tasks + fresh research + fresh teaching；安装/Marketplace/profile identity；README/changelog/version closure | 拼接不同 commit 的 PASS、fresh 样本被调参、正常入口未消费新机制 | 不要求每次新失败都新建 gate；归入现有 gate | 是 |

### 8.1 Final batch 建议

开发期：

- CAT-TRACE 已知失败回放；
- 当前已有 presentation fixtures；
- 两模板 skeleton/render probes；
- deterministic text/citation/geometry checks。

最终候选冻结后：

1. 一个新的 CUHK research deck 完整任务；
2. 一个新的 `course-standard` Tutorial/lecture 完整任务；
3. 一个 existing-deck targeted revision；
4. 一个 should-not-change compact/sparse/math-only 反例集合。

最终样本数量可由 Critic 根据 blast radius 调整，但不能在看到结果后换题或拼赢家。

---

## 9. 实施分期

本 Plan 通过不等于一次 Codex 任务把全部代码同时改完。建议用同一架构下的三个 bounded implementation packages；每个 package 都有明确新增能力，不能只增加 schema/metadata。

### Package A — 统一前门与双模板基础

新增能力：任何 deck 请求都能正确进入 plugin；`course-standard` 有可编译 canonical source；两个模板有明确 routing、manifest、render probe 和 visual tokens。

范围：

- universal front-door routing；
- new/revision/local-edit/plan-only mode；
- `cuhk-research` authority 清理；
- `course-standard` reconstruction；
- template tests、font/resource probe；
- compatibility routing for existing research/business skills；
- G1、G5 的开发证据。

不做：完整 semantic/storyboard migration，不假装 TODO 已全部关闭。

### Package B — 语义故事板与页面构图核心

新增能力：先决定听众理解顺序，再决定页面形态；first-use、transition、advisor question、math/simulation/model closure 成为 normal path。

范围：

- semantic storyboard 与 composition contract；
- `deck-plan.yaml` compatibility reader/export；
- first-use/symbol/transition derived reports；
- primitive grammar；
- diagram/figure/math/simulation/model-closure/Question contracts；
- color/type/caption/source roles；
- G2、G3、G4 的开发证据。

### Package C — 交付、revision、review 与 release closure

新增能力：完整 deck 的引用、文本层、语言、scope-honest review 和 existing-deck preservation 能成为真实 completion gate。

范围：

- source/citation/bibliography/text-layer contract；
- Clear Writing handoff + rerender；
- full-deck contact-sheet review；
- review scope/authority；
- existing-deck runtime，而不只是 validator；
- known/unrelated/fresh final batch；
- version/changelog/README/Marketplace/profile closure；
- G6–G10。

若 Package A/B 的实现证明架构关键假设不成立，必须回 Planner–Critic，不允许 C 用更多 validator 掩盖。

---

## 10. 迁移与兼容

1. `research-presentations` / `business-presentations` 保留现有 trigger 名称至少一个正式 release，内部统一调用 shared core；不做破坏性 slug migration。
2. 现有 `deck-plan.yaml` 暂时保留 compatibility reader/export；新的 normal entry 不继续向旧 schema 添加顶级职责。
3. 当前 exact CUHK source 保留；derived `design-tokens.json`、reference PPTX 或旧 helper 不能冒充 exact source。
4. 现有 gold/reference library 只作为候选启发；没有命中不能阻塞 production，命中也不能覆盖 semantic/composition 决策。
5. generated `plugins/codex/plugins/**` 只能由 generator 重建，禁止手工 patch。
6. current existing-deck validator 可以暂时作为 evidence checker，但 normal revision entry 必须真正执行 diagnose → edit → render → compare。
7. 外部模板/已有 PPTX 走 pass-through/preserve，不加入内置模板 registry。

---

## 11. 测试与证据诚信

### 11.1 机械检查只能证明机械事实

允许的 deterministic checks：

- template files / hashes / package availability；
- schema/plan structural validation；
- first-use/order rules；
- source/generated parity；
- PDF page size、font presence、text extraction；
- object bounding boxes、overflow、known collision probes；
- accepted-element diff scope。

这些不能单独证明 storyline、视觉成熟度、语言自然或科学正确。

### 11.2 Render 是用户消费对象

每个最终 deck 必须真实编译并 render。不能用独立重建 PDF 代表 PPTX，也不能用 source screenshot 代替 renderer output。Reviewer 必须能访问全文或完整 render；只看摘要不能给全文 PASS。

### 11.3 私有材料

- CAT-TRACE 私有全文/render 不提交进普通 plugin payload；只提交 public-safe regression evidence；
- `Chapter1.pdf` 只作为用户提供的 style reference，implementation 提交重建 source、设计规格和 synthetic fixture，不复制课程正文；
- 必须记录模板来源、hash、检查内容、采用范围和不采用内容；
- 不把老师 slide 的 annotation/highlight、课程内容或具体例题当 plugin 默认资产。

---

## 12. 风险、停止条件与恢复

| 风险 | 最小防线 | 何时停止并回 Planner |
|---|---|---|
| 又造一个更大的 schema/packet 系统 | 三类 task-local artifact；schema 只验证结构，不证明质量 | 新增字段不能对应真实失败或正常入口不消费 |
| 两模板把所有 deck 压成同一种脸 | semantic/composition 先于 adapter；页面形态由内容决定 | 为通过 template test 开始硬编码固定 storyline/layout |
| `course-standard` 复现成旧 PDF 的截图/抄本 | 只复现视觉系统，用 synthetic content 验证 | 无法在不复制课程正文的情况下复现 |
| Clear Writing 改坏科学含义 | scientific freeze + fidelity diff + rerender | 公式、数值、claim/citation 被改 |
| reviewer 越权或循环不收敛 | scope contract + finding-level evidence + stagnation stop | 同类 blocker 两轮无可见进展或需要改变架构 |
| 图/diagram rules 误杀合法简洁页面 | should-not-change compact/sparse/math-only regressions | 规则只能靠大量例外维持 |
| PDF 文本层与 visual render 冲突 | compile/render/text extraction 双证据 | renderer 无法同时满足主要字体、公式和复制需求 |
| implementation 太大 | A/B/C 分包；每包新增可观察能力 | 一个 package 扩展到跨 repo workflow 或新状态机 |

恢复原则：保留当前 `presentations 0.3` 可安装版本；所有新 normal entry 在 final gates 前留在 task branch。任一 package 失败时可回退到原版本，不破坏 CUHK 现有生产路径。

---

## 13. 版本、maturity 与 README 决策

当前设计文档阶段：

```text
Repository bump decision: NONE
Affected plugins:
- presentations: NO_BUMP
  Reason: 本轮只新增 architecture Plan，没有修改 production behavior。
```

若 A/B/C 全部实现、原失败 replay、unrelated regression、fresh final batch、独立 review 和 release closure 均通过：

```text
Repository bump decision: PATCH（仅在形成正式可安装 repository release 时）
Affected plugins:
- presentations: 0.3 -> 0.4
  Reason: universal invocation、双模板 production、semantic/composition pipeline、delivery/review/revision contract 构成一个完整用户可见 improvement batch。
```

`baseline` 不因一次 gate matrix 自动提升。是否进入 `alpha` 需要 CUHK research、course tutorial、existing-deck revision 等多个独立真实任务稳定运行后再由用户/Planner决定。

README closure 是 implementation Package C 的显式检查项：

- 若用户入口、模板选择、安装/profile 或版本变化，同步 README；
- 若没有 README-facing 变化，记录 `README checked: no update required`；
- README 不写内部 task/CI 流水账。

---

## 14. 明确不做

- 不新增第三个内置模板；
- 不新增顶级 presentation plugin；
- 不为了本 Plan 修改 Bridge Kit；
- 不将 `course-standard` 做成课程内容仓库；
- 不把 highlight annotations 复制进模板；
- 不因所有 TODO 被“Plan 覆盖”就立即把 #29–#48 标成 PROMOTED/DONE；
- 不用 synthetic PASS 宣称 production-ready；
- 不在 Critic PASS 前生成 Executor Goal/Kickoff；
- 不承诺本轮完成 PDF/UA-2；
- 不删除现有兼容入口，直到 migration gates 真实通过。

---

## 15. Critic 必须重点攻击的问题

1. “所有 PPT 先调用 presentations”是否通过轻重模式避免了小编辑过重？
2. 两个内置模板的边界是否清楚，external locked input 是否被错误地变成第三模板？
3. semantic storyboard 与 page composition 是否仍有隐藏职责重叠？
4. `course-standard` 的复现合同是否足以忠实，又避免复制课程内容和 annotations？
5. 是否遗漏任何 `docs/plugin-todos/presentations.md` 当前有效条目或把 TODO 机械塞进无效字段？
6. G1–G10 是否证明不同用户能力，是否有重复 gate 或遗漏 normal entry / full artifact / should-not-change？
7. A/B/C 三包是否仍然过大，是否应调整依赖顺序或验收边界？
8. existing-deck revision、scope-honest review、final candidate identity 是否能阻止当前假 PASS？
9. 保留 research/business trigger、共享 core、teaching mode 的迁移是否足够简单？
10. 版本、maturity、README、生成层和私有材料边界是否符合 repo policy？

Critic 只有在本 Plan 的架构、TODO coverage、Capability Gate Matrix、迁移、风险和恢复路线均可执行且不过重时才应 PASS。PASS 只批准设计，不授权 implementation、付费 review 或发布。
