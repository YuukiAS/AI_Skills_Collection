# presentations — Long-Term TODO

这是 `presentations` plugin 的长期问题清单。

以后在 TRACE、CARE 或其他真实项目里调用 `presentations` 时，如果问题本质上来自 plugin 的生成、返修、布局、检查或路由行为，直接把这次真实问题写到这里，状态先用 `NEW`。不要先在项目 repo 再维护一份 Presentation 插件问题副本。

Current capability status: `baseline`.

## Incoming real-use feedback

### Presentations 0.2 completion evidence can still miss obvious rendered regressions
status: NEW
source: TRACE / CAT-TRACE 32-page group-meeting deck v5 review
evidence: `YuukiAS/TRACE` commit `1de90f2f26b3f787073ecedd7a4df41a985712eb`; executor produced the presentations 0.2 revision packet, rendered QA and English-final-pass artifacts, but human review still found a sample-axis/arrow collision, text/formula overlap inside an architecture node, awkward formula wrapping/spacing, and dense Question blocks on real-data slides
problem: 0.2 已把 existing-deck revision gate 接入 production，但 v5 证明“packet 字段齐全”仍不等于 rendered artifact 真的通过。尤其 text–formula/text–edge collision、窄框内数学断行、Question block 与邻接内容重叠等明显视觉错误，仍可能在 executor-side QA 里被标成可交付。需要后续 Planner 判断是 reviewer evidence 粒度不足、视觉 reviewer 没真正消费高分辨率页，还是 gate 还缺具体可见碰撞检查。
project-specific context: CAT-TRACE 的具体页码、公式和图形属于项目；通用问题是 production completion evidence 必须来自真实 render 的可见几何判断，而不是文件存在或自报 checklist。

### Deck-wide formula, text and emphasis scale still lacks a stable hierarchy
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v5 review
evidence: 32-page v5 shows one model page with an oversized residual formula, another marked-tail transformation with an oversized connective word, a model-closure page with formulas/text too small, and theory formulas at inconsistent scales
problem: 当前 plugin 有“按科学重要性分配空间”的原则，但缺少足够稳定的 deck-level typography/math scale contract。核心公式、supporting formula、diagram/table 内数学、正文、caption/source、强调粗体之间会逐页漂移；`resizebox` 还可能把普通连接词和数学对象一起放大。需要一种模板相对、角色驱动的尺度层级，而不是每页凭感觉调大调小。
project-specific context: 用户把 CAT-TRACE v5 P14 的核心 borrowing equation 视为当前 deck 可接受的最大公式视觉尺度，这是本 deck 的局部标尺；通用规则不应硬编码该页或某个绝对字号。

### Diagram planning needs a semantic-purpose gate before geometry
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v5 review
evidence: v5 phylogeny-borrowing slide produced a technically simple tree-like sketch, but the user could not see a clear visual explanation of why related species borrow more strongly; geometry cleanup alone would not fix the conceptual weakness
problem: 现有 Diagram Gate 已要求 semantic graph，但真实 production 仍可能先画对象、后补意义。对于科研 diagram，应在进入 TikZ/PPT composition 前明确一条 audience-facing purpose statement、必须出现的 scientific objects、必须编码的关系以及 reading direction；如果不能说明“这张图让听众更快看懂什么关系”，就不应开始画。
project-specific context: A/B/C species tree、具体相关矩阵和 CAT-TRACE phylogeny prior 属于当前项目；通用问题是 diagram 的 pre-layout semantic sketch/plan，而不是固定某种树图模板。

### Footer/source safe zone is not enforced
status: PROMOTED_BY_045
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: `YuukiAS/TRACE` commit `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, 29-page v4 PDF, especially the first motivation/data slides
problem: 正文、Example/callout、source credit 和 Beamer 底部导航之间没有稳定安全区；有的正文已经靠近 source/footer，source 本身又接近底部紫线。当前 plugin 能检查 overflow，却没有把 body-to-source、source-to-footer 的最小视觉间距作为真实 render 验收项。
project-specific context: CAT-TRACE 使用当前 CUHK 16:9 Beamer 模板和紫色底线；具体毫米阈值属于模板/renderer 校准，不应直接写成所有模板的固定数字。

### First-use and narrative-order guardrails still regress in production
status: PROMOTED_BY_045
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: v4 P2–P11；v4 execution task已经要求读取 presentation guardrails 与 scientific-prose
problem: 新方法名在动机/基线讲清楚前仍提前出现，部分缩写和领域术语在听众尚未获得现实解释时进入 slide；说明“先介绍再使用”的 active guardrail 被读取后仍没有形成可靠的整 deck narrative-order check。
project-specific context: CAT-TRACE、TRACE、CORAL、COI、OTU、GBIF 的具体顺序属于本 deck；通用问题是 first-use 与 dependency order 没有被最终交付检查挡住。

### Diagram QA still passes rigid narrow nodes and inconsistent connector endpoints
status: PROMOTED_BY_045
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: v4 P3, P8–P10；多轮真实 render 返修后仍出现短箭头、节点过窄导致多行断字、箭头与 block 间距不一致
problem: 现有 diagram semantic/geometry guidance 已存在，但 production 仍能输出固定窄 box、过多换行、箭头有的停在 block 前、有的压到 block/文字、主图没有充分占据页面中心等问题。单纯“有 connector / 无 crossing”不足以保证成熟的科研 diagram。
project-specific context: CAT-TRACE matching / catalogue split 的具体节点与拓扑属于项目；通用问题是 node width 应由内容和画布反推，edge endpoint/clearance 与 arrowhead 可读性需要最终 render 证据。

### Scientific hierarchy QA misses simultaneous crowding and unused space
status: PROMOTED_BY_045
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: v4 P9, P20–P27；页面一侧拥挤或核心文字/图很小，同时另一部分仍有明显可用空间
problem: active guardrail 已要求按科学重要性分配空间，但最终 render 仍会出现“右侧挤、左图小”“核心公式/标题相互贴近”“discussion/table 字小而页面仍有空白”。现有 QA 需要判断 usable area 是否真正转化为可读字号、图尺寸和层级间距，而不是只检查 overflow。
project-specific context: 具体 P9/P20 等页码只用于定位真实证据；不应形成 CAT-TRACE 专属 layout selector。

### Figure readability and caption pairing are not checked at the rendered-content level
status: PROMOTED_BY_045
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: v4 P20, P24–P26；prevalence 图、图内 axis/legend/caption 仍偏小，辅助图的 caption/label 不完整或层级不统一
problem: plugin 已经要求主图可读，但实际检查仍偏向 image object 是否存在/是否够大，没有稳定检查图内文字、轴、legend、panel title 在最终投影尺寸是否可读，也没有强制每个独立 figure/panel 与自己的 caption/label 配对。
project-specific context: Finland/Madagascar/Victoria 的具体图和数据属于 TRACE；通用问题是 figure-content bbox、内部字体和 caption pairing 的 rendered QA。

### Table, list and paragraph primitives still drift across one deck
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4 and v5 reviews
evidence: v4 P11–P13, P21–P26；v5 continues the issue in the metabarcoding definition block, information-before-discovery table, simulation metric tables and dense real-data right columns
problem: 当前 deck-wide style candidate 没有转化为足够稳定的 production primitive。相同层级的短表头有时全小写，结构化事实有时做表、有时裸排；并列事实和连续解释也会随机在 paragraph/list 之间切换，增加阅读负担。还需要明确：连续论证适合短 paragraph；多个并列、可独立理解的定义/事实更适合 bullets；重复比较相同属性或数值对齐时才优先 table。
project-specific context: 具体 trait、dataset 字段、COI/metabarcoding 定义属于 CAT-TRACE；通用问题是 table header/row-label typography，以及 paragraph、bullet、table 的选择门槛。

### Complex multi-slide models can finish without a model-closure page
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: v4 Model section P9–P16；用户看完各组件后仍无法快速重建“完整模型到底由哪些部分组成”
problem: one-slide-one-job 规则能避免单页过载，但复杂模型被拆成多页后，plugin 没有检查 section 结束时听众能否重新拼回完整 generative/model structure。需要一种 model-closure / reassembly 页面模式，而不是再画一张重复的自由流程图。
project-specific context: finite catalogue、open tail、matching、residual dependence 等具体组件属于 CAT-TRACE；通用问题适用于任何被拆成多页讲解的复杂统计/机器学习模型。

### Question/background callout lacks a stable research-deck primitive
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4 and v5 reviews
evidence: v4 P21–P27；v5 introduced a purple-line Question treatment, but on dense simulation/real-data/discussion pages the label, question text and neighboring content are not vertically balanced and can visibly crowd or overlap
problem: simulation question 与 advisor discussion 都需要一种轻量、成熟、非卡片化的 emphasis primitive；Background 应只恢复回答问题所需的 1–2 条事实，必要时允许公式或受控的前页引用，而不是重复整段项目状态。Question primitive 本身也需要明确 vertical centering、line height、padding 和与邻接 table/text 的 safe area。
project-specific context: CAT-TRACE 三个 discussion 问题和具体公式属于项目；通用问题是 Question/Background 的信息和视觉合同，以及跨页引用时的返回路径。

### Slide source/figure citation style is inconsistent and underspecified
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4 and v5 reviews
evidence: v4 P24–P26；v5 still mixes bare author-year citations with `Source:`, `Figure:` and `Data:` labels across motivation/model/data slides
problem: plugin 没有稳定区分“论文/理论来源”“图片来源”“数据来源”“普通参考文献”，导致 source footer 格式逐页漂移。真实科研 slide 需要一致、足以定位原始 paper/figure 的 source line，同时不能把完整 bibliography 挤成不可读的小字。一个可验证的 house style 应明确不同 source role 使用什么 label，以及同一 deck 不能混用裸 citation 和带 role label 的 citation。
project-specific context: Stolf & Dunson、Abrego、Hardwick、Tikhonov 等具体文献属于 TRACE；通用问题是 slide-level source citation 的统一模板和与 References 页的分工。

### English scientific prose handoff is optional rather than a completion gate
status: PROMOTED_BY_045
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: v4 task要求读取 `scientific-prose`，但最终仍反复出现 `Failure prevented`, 机械 `Example.` 标签、noun-stack/table microcopy 和不自然开场；presentation skill 当前只规定英文 slide text “can use” scientific-prose
problem: presentation 结构和科学事实稳定后，没有一个明确的 reader-facing English final-pass handoff/acceptance gate。仅“读取 writing skill”或让 Codex顺手润色不足以阻止模板化、机器式科研英语进入最终 PDF。
project-specific context: 具体 CAT-TRACE 术语和句子属于当前 deck；通用问题是 presentations 与 writing-style 的 routing/QA 边界，不能把 presentation layout 责任交给 writing-style。

真实项目 thread 新增时只需要最小格式：

```text
### <简短的问题标题>
status: NEW
source: <真实项目 / 当前任务>
evidence: <实际 PDF / render / commit / task 路径>
problem: <用户实际看到的问题>
project-specific context: <哪些细节只属于当前项目>
```

此时先记事实，不要直接发明通用规则。后续由 AI_Skills Planner / maintainer 去重、整理并决定是否变成下面的长期候选。

## Open candidates

### Diagram geometry and canonical edge/node treatment
status: BLOCKED_NEEDS_EVIDENCE
source: repeated TRACE visual feedback
evidence: presentation maintenance archive + CAT-TRACE real deck revisions
target layer: rendering/qa
problem: diagram 的语义规则已经有了，但实际箭头、节点、对齐、连接路径和层级几何仍然可能做坏。
candidate action: 只有新的真实 deck 再次暴露问题时，才补 renderer-level primitive 和 QA，不为了历史 TODO 预先造一整套几何系统。
promotion gate: 新的真实 CAT-TRACE 或 unrelated deck 用实际 render 重现问题，并能证明修改真的改善输出且不会过度限制其他 diagram。

### Deck-wide style system and terminology hierarchy
status: CANDIDATE_GENERIC
source: repeated real research deck revisions
evidence: presentation maintenance archive
target layer: reasoning/rendering/qa
problem: 一整套 deck 里，标题大小写、术语首次解释、dataset/simulation 编号、小标题、metric label、caption 和 references 容易逐页漂移。
candidate action: 只有真实返修再次证明这是当前问题时，才增加最小 deck-wide consistency contract，不把所有页面强行做成同一种布局。
promotion gate: independent rendered deck 证明 consistency check 能抓到真实问题且不会压平不同科研页面。

### Math and theory slide hierarchy
status: CANDIDATE_GENERIC
source: repeated statistics and theory deck feedback
evidence: presentation maintenance archive + CAT-TRACE review docs
target layer: reasoning/rendering/qa
problem: definition、design setting、estimand、theorem、derivation 容易都被做成同一种“居中大公式”，科学角色没有层次。
candidate action: 在新的 math-heavy real deck 再次出现时，才进一步加强公式层级、首次语义解释和 theory-page QA。
promotion gate: theorem/statistical-method real deck replay + unrelated math-heavy deck regression。

### Simulation, metric and structured-fact presentation
status: CANDIDATE_GENERIC
source: repeated real statistics deck feedback
evidence: presentation maintenance archive
target layer: reasoning/rendering/qa
problem: DGP、estimand、baseline、metric direction、dataset facts、seed/reproducibility 信息容易混成段落或弱表格，读起来很累。
candidate action: 新的 simulation-heavy / real-data deck 再次出现时，再提炼更稳定的 table/list patterns 和 QA。
promotion gate: 至少一个 simulation-heavy 和一个 real-data deck 的真实 render 都证明改善了可读性。

### Natural scientific slide language
status: CANDIDATE_GENERIC
source: repeated presentation and writing-style feedback
evidence: presentation maintenance archive + `docs/plugin-todos/writing-style.md`
target layer: writing/qa
problem: slides 仍可能出现内部流程词、模板化对比句、面向作者而不是面向听众的说法。
candidate action: 真实失败出现后再决定应该改 `research-presentations`、`scientific-prose`，还是两者的交接；不要重复造一套写作规则。
promotion gate: 多个独立英文科研 slide 的真实证据。

## Current real-use focus

现在不继续做 synthetic challenge chain。

下一步就是用已安装的 `presentations` plugin 继续返修**现有 CAT-TRACE deck**。新的 plugin 问题直接作为 `NEW` 写到本文件，再由中央 Planner 整理。

这不是一个需要单独“完成”的 TODO，也不需要为了证明 workflow PASS 重启 043。

## Recently promoted / established

- `0.1` 已修掉 normal-production validator 对 Stage-4 固定六类页面和固定 storyline 的硬编码。
- `0.1` 已加固 existing-deck revision：用户要求继续返修已有 deck 时，不应重新生成一套；已接受页面/元素要作为约束保留，并和用户真正看过的上一版 render 对比。
- `045` 已将 existing-deck revision 接入可执行 production gate：`validate_existing_deck_revision_entry.py` 会消费 reviewer-seen baseline、accepted-element ledger、targeted feedback、rerender、高分辨率问题页、first-use dependency order、rendered scientific-object QA、English final pass 和 independent visual review；CAT-TRACE v4 known-failure replay 必须返回 `REVISE`/`BLOCKED`，不能自检后误报 final PASS。
- Presentation maintenance 历史已从普通 runtime 中移出；普通安装只保留已经确认有用的规则。
- Evidence-first research-group-meeting routing 和 scientific-object page archetypes 已建立。
- Exact CUHK Beamer/PDF 仍是默认 desktop research route。
- Source fidelity、scientific layout、真实 render/contact-sheet review 和 bounded repair contract 已建立。
- Theory 页面按“解决了什么问题 / 提供什么保证”组织，而不是按 theorem 数量炫技。

## Do not do

- 不要为了 workflow PASS 重启已经暂停的 043 synthetic challenge。
- 不要把已经用来调过系统的 holdout 再说成 unseen。
- 不要把 CAT-TRACE 页码、论文名、theorem 名称写成 selector/layout 特例。
- 不要每出现一个视觉问题就新建 skill；优先修已有 reasoning/rendering/QA 层。
- 用户说“继续完善现有 CAT-TRACE PPT”时，不要从头重新生成。