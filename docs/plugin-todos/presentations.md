# presentations — Long-Term TODO

这是 `presentations` plugin 的长期问题清单。

以后在 TRACE、CARE 或其他真实项目里调用 `presentations` 时，如果问题本质上来自 plugin 的生成、返修、布局、检查或路由行为，直接把这次真实问题写到这里，状态先用 `NEW`。不要先在项目 repo 再维护一份 Presentation 插件问题副本。

Current capability status: `baseline`.

## Incoming real-use feedback

### CAT-TRACE v13/v14 follow-up feedback is consolidated into the canonical inbox
status: NEW
source: TRACE / CAT-TRACE v13 and v14 human reviews on 2026-09-03
evidence: former packets `docs/plugin-todos/presentations-v13-regression-followup.md` and `docs/plugin-todos/presentations-v14-content-language-second-gate.md`; TRACE v13 commit `33b616866a47231b9e74bbc3486aba3b73a5d020`; v14 human review after the major v13 narrative/diagram repair.
problem: These reviews add one consolidated real-use feedback packet to the canonical `presentations` inbox. The unique failures to preserve are:

- First-use must be an ordering invariant, not only a definition checklist. v13 used `CAT-TRACE` in audience-facing P2, P8 and P12 before the method was formally introduced on P14. Future QA needs a method/concept registry with a first allowed anchor or prerequisite set, and the final deck scan must include rewritten bridge text that can reintroduce early terms.
- A scoped visual review must not certify the whole deck. v13 independent review focused on P21/P36/P42, then returned a global PASS while later human review found major unreviewed regressions on P2, P6, P12, P21, P25, P35 and elsewhere. Review artifacts need `review_scope`, `reviewed_requirements` and `unreviewed_requirements`; global PASS is impossible while mandatory global requirements remain unreviewed.
- New or substantially rewritten slides need the v9-style pre-writing semantic brief again. Accepted old-slide quality does not transfer to new slides drafted from planning notes; each new or heavily rewritten content slide needs audience assumption, one page job, prerequisites, one concrete object/example when useful, and one sentence the audience should remember before visible prose is written.
- Planner language and internal version labels need an audience-copy firewall. v13/v14 exposed labels such as `V1`, `V2`, `current construction`, `Theory result 1` and `Theory target` as if the audience needed project-management bookkeeping. Visible slides should explain the current method, future extension or theory status in scientific language, without implying unproved targets are established.
- Diagram QA needs a utility/quality floor in addition to semantic correctness and collision checks. A diagram should survive only if it helps the audience understand the relationship faster than a short explanation or equation; final render QA must still check whitespace, hierarchy, connector length, node text readability, and whether prose has been stuffed into tiny boxes.
- Examples and takeaways need an explanatory bridge when the conclusion is not self-evident. v13 P6 jumped from Malagasy OTU counts to the named-species conclusion without explaining why the example supports that inference.
- Natural slide language requires spoken scientific prose, not only grammatical cleanup. v13/v14 retained formulaic titles, repeated `What...` / `Where...` / `How...` stems, narrator labels such as `What it says`, and memo-like sentences. A second content-language gate should reread the final slide as spoken explanation after structural repair.
- Simplifying a slide must not delete why the scientific object is in the talk. v14 dataset pages became cleaner but over-compressed the narrative explaining each dataset's distinct role.
- First-use/context QA must include every visible text layer: figure legends, axis labels, tick labels, panel titles, table cells, diagram nodes, annotations, captions and baseline display names. v14 exposed `bigMVP`, `bigMVP-h`, `TRACE-h` and `TRACE no covariates` inside a figure before the audience had useful explanations.
- A result figure should be redrawn around the claim the audience needs to see. v14 kept analysis-style log-MSE boxplots even though the main communication need was over/underprediction and model-specification sensitivity.
- Diagram geometry rules are cumulative. A new semantic/utility rule does not replace older accepted arrow/node constraints such as boundary clipping, visible shaft length, peer-edge consistency, spacing and label clearance.
- Mathematical symbols need cross-slide first-use and conditioning-level checks. v14 used `D_W` and `lambda_{g,m|n}` without sufficient introduction or level distinction.
- Oracle/generative checks and fitted simulations need visibly different jobs. Simulation 1A is an oracle DGP/theory check and must not be presented as estimator quality; Simulation 1B is fitted recovery.
- A second-gate review should compare final deck language against the best accepted readability baseline, not only the immediate bad predecessor. CAT-TRACE v9 remains important evidence for the readability floor even when v14 improves over v13.

project-specific context: CAT-TRACE, TRACE, HMSC, CORAL, exact page numbers, exact method labels, dataset roles, simulation numbering, and mathematical notation belong to TRACE. The generic issues are ordering, scope integrity, pre-writing orchestration, audience-copy firewall, diagram utility/geometry, spoken scientific language, all-visible-text first-use, claim-first figures, symbol registry, and quality-reference baselines.

### Advisor discussion questions need a decision-value and answerability gate
status: NEW
source: TRACE / CAT-TRACE 35-page group-meeting deck v11 review
evidence: `YuukiAS/TRACE` commit `06511e3d5444ae8be847ef42ea362c19f6d787f9`; the deck ends with three advisor-facing questions on stronger infinite-tail theory, identifiability constraints for catalogue borrowing, and computational scope. Independent review found that the questions are useful only because each unlocks a real project decision, but the current presentation workflow checks Question/Background styling more strongly than whether the question is worth asking, whether the intended advisor can reasonably answer it, and whether the presenter is prepared for the obvious follow-up questions. The user explicitly wants this judgment applied to future presentations, with likely advisor counterquestions and prepared responses kept in speaker notes or review evidence rather than cluttering the visible slide.
problem: Before an advisor/supervisor discussion question is accepted into a research deck, the presentation layer should record: (1) the concrete project decision the answer would change; (2) why that decision matters now; (3) whether this audience has the expertise/context to answer; (4) the presenter's current leaning rather than outsourcing all judgment to the advisor; (5) the most likely counterquestion/pushback; and (6) a concise prepared response. Questions that do not unlock a real decision, are not answerable by the audience, or exist only to make the Discussion section look interactive should be removed or rewritten. The visible slide usually needs only Question + minimal Background/options; counterquestion preparation belongs in speaker notes or an executor/reviewer artifact.
project-specific context: CAT-TRACE's exact three questions and the user's current preferred answers belong to TRACE. The generic issue is advisor-question quality, answerability and presenter preparation.

### Page-level language audits can pass while sentence and slide transitions remain mechanical
status: NEW
source: TRACE / CAT-TRACE 34-page group-meeting deck v10 review
evidence: `YuukiAS/TRACE` commit `3d7bc06dd0f9a80bb87a863e8a74398bc0f866bf`. The v10 `full_deck_language_audit.md` marked every page P2–P34 `READY_FOR_REVIEW`, yet independent review still found that P2 and P3 read as individually correct sentences placed next to one another rather than one explanation, and that several slide boundaries still lacked a natural scientific handoff: metabarcoding -> OTU, the two discovery questions -> TRACE, TRACE -> HMSC, marked tails -> residual dependence, and priors -> full-model closure. The page-level audit described each page's intended meaning but did not actually test why sentence k leads to sentence k+1 or why slide k creates the need for slide k+1.
problem: Research-presentation language QA needs a **coherence/transition layer in addition to plain-language cleanup**. Within a slide, consecutive sentences should form an explicit causal, temporal, inferential or explanatory chain rather than a list of independently acceptable statements. Across slides, the reviewer should inspect the end of slide k together with the beginning of slide k+1 and ask what unresolved question, limitation or next object creates the transition. This must preserve the existing audience/page-job/first-use/plain-language rules rather than replace them. A useful evidence artifact is a short `transition_map` recording the scientific state at the end of each page and why the next page follows.
project-specific context: The exact CAT-TRACE sequence (survey -> catalogue -> metabarcoding -> OTU -> unseen discovery -> TRACE -> HMSC/CORAL -> CAT-TRACE) belongs to this deck. The generic problem is that sentence-level and page-level correctness do not guarantee narrative continuity.

### Accent colour and emphasis can drift without a semantic-role contract
status: NEW
source: TRACE / CAT-TRACE 34-page group-meeting deck v10 review
evidence: `YuukiAS/TRACE` commit `3d7bc06dd0f9a80bb87a863e8a74398bc0f866bf`, especially P12 where a full ordinary sentence (`Both components can be coupled...`) is rendered in accent purple without a stable semantic reason, while `Example:`, `Question`, `Takeaway:` and `Limitation for our setting:` are also using accent treatments elsewhere.
problem: Presentation colour should encode stable semantic roles, not act as a generic importance marker. Ordinary explanatory prose should remain neutral by default. Accent colour may be reserved for a small set of reusable roles such as section/subheading labels, `Example:`, `Takeaway:`, `Question`, `Limitation`, and controlled semantic colouring inside equations/diagrams. The final deck-wide consistency pass should flag an entire prose sentence in accent colour when it does not belong to an approved role.
project-specific context: CUHK purple and the exact CAT-TRACE labels are project/template details. The generic issue is semantic emphasis consistency across a deck.

### Citation style, bibliography fidelity, and PDF text-layer integrity need one delivery contract
status: NEW
source: TRACE / CAT-TRACE 34-page group-meeting deck v10 review
evidence: `YuukiAS/TRACE` commit `3d7bc06dd0f9a80bb87a863e8a74398bc0f866bf`. v10 uses role labels such as `Source:`, `Figure:` and `Data:`, but short-credit formatting still varies, the References slide contains several paraphrased/shorthand article titles rather than verified full bibliographic titles, and the compiled PDF text layer maps ordinary digits such as years/page numbers to incorrect Unicode characters when extracted/copied even though the rendered glyphs look correct.
problem: A research-deck delivery should distinguish three layers: (1) concise on-slide role-labelled citations; (2) a verified References bibliography generated from real metadata rather than author-written shorthand titles; and (3) PDF text-layer integrity. The plugin should encourage one house citation style per deck, prohibit invented/paraphrased bibliography titles, and require source metadata verification from BibTeX/Zotero/journal metadata or another authoritative source. Final PDF QA should run text extraction/copyability checks for ordinary ASCII digits, years, page numbers and citation text, so a visually correct PDF with broken ToUnicode/font mapping cannot pass delivery.
project-specific context: The specific TRACE papers, VicFlora and current XeLaTeX/theme font issue belong to this deck. The generic issue is citation-system consistency plus searchable/copyable PDF text integrity.

### Audience/page-job briefing before prose handoff materially improved a real research deck
status: NEW
source: TRACE / CAT-TRACE 34-page group-meeting deck v9 review
evidence: `YuukiAS/TRACE` commit `c271e0f546ce7f38f35f70165f2c2ee7b6580b36`; v9 preflight confirms the active runtime was still `presentations 0.3` + `writing-style 0.1` and that the AI_Skills pull changed only TODO docs, not runtime files. The large language improvement came from the task/workflow instead: before drafting/revising prose it explicitly fixed the target audience, each slide's scientific job, why unfamiliar terms appear there, what the audience should remember, and then ran a full-deck first-use registry plus page-by-page language audit over P2–P34. The final human review judged v9's language markedly better than v8 even though the prose runtime itself had not changed.
problem: This is strong positive evidence that `presentations` should own a **pre-writing audience/page-job brief** rather than merely hand already-written slide text to `scientific-prose`. For each content slide, presentation orchestration should establish: audience assumptions, the one scientific point of the page, prerequisite context, why each unfamiliar term is needed now, and the intended plain-language takeaway. That brief should then be handed to `writing-style`/`scientific-prose` to produce or revise the English. `presentations` should not duplicate prose-style rules; its responsibility is to provide the semantic/audience brief, require the writing handoff after scientific freeze, and then reread the final rendered deck for reader effort. The v9 `first_use_registry.md` and `full_deck_language_audit.md` are useful evidence patterns for this boundary.
project-specific context: CAT-TRACE, VicFlora, COI, OTU, MGP and specific slide wording belong to TRACE. The generic lesson is orchestration: audience -> page job -> prerequisite/context -> term role -> takeaway -> writing-style -> rendered reader-effort review.

### Full-deck audience-context and responsive-layout review still regresses after repeated real revisions
status: NEW
source: TRACE / CAT-TRACE 33-page group-meeting deck v8 review
evidence: `YuukiAS/TRACE` commit `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. v8 successfully fixed several long-running issues by adding spacing tokens and regenerating presentation-specific figures, but human/GPT review still found: inconsistent same-role label scale/gutters on P2; a cognitively repetitive catalogue explanation on P3; first-use terms on P4/P19 that were expanded without enough local purpose/context; repeated/non-unified Example treatment across P3/P5/P15; diagram transition text on P10 colliding with arrows or wrapping formulas awkwardly; sequential CORAL content still arranged as three columns despite large unused vertical space; short table row labels wrapping unnecessarily on P16; a newly introduced duplicate `diag(Sigma_W)=1` step on P18; a contextless MGP acronym and defensive source-note-like threshold sentence on P19; cramped oracle-side text on P24; inconsistent Question line spacing/hyphenation across P27-P29; and P29/P30 body compositions whose figure/data regions remain visually unbalanced. The v8 English-final-pass record also states that it only reviewed visible wording touched in v8.
problem: The production path now has many local rules, but it still lacks a sufficiently strong full-artifact reader-effort gate. A final presentation review should not ask only whether each requested object changed. It must inspect every final page for: (1) unfamiliar term introduced with both expansion and immediate purpose/context; (2) one clear reading path with minimal semantic repetition; (3) columns used only for genuinely peer-level comparison, not sequential stages; (4) same-role typography, gutters, question leading and intra-node text/formula spacing; (5) short labels kept on one line when space permits; (6) no new duplicate math, awkward hyphenation, defensive/meta prose or source-note language introduced by a repair; and (7) responsive fallback when a region becomes cramped. Full-deck language/readability QA must cover the final rendered artifact, not only source lines edited in the current round.
project-specific context: VicFlora, COI, metabarcoding, MGP, CAT-TRACE equations and specific page numbers belong to TRACE. The generic issue is full-deck audience-context, cognitive-load, responsive layout and no-new-regression review, not a CAT-TRACE-specific template.

### Review coverage can self-certify unresolved reviewer feedback
status: NEW
source: TRACE / CAT-TRACE 33-page group-meeting deck v6 and v7 reviews
evidence: `YuukiAS/TRACE` commits `ef08bc25673fb33b639e523504676c0f333d93f4` and `e5bce0c0b8d24b33aa6930a2ea8f9a8a9c86e252`; v6 `v5_review_coverage.md` marked all 21 prior review points `PASS` despite unresolved issues. v7 correctly downgraded executor labels to `READY_FOR_REVIEW`, but the subsequent human/GPT review still found repeated failures in P2 annotation spacing, P10/P13 arrow geometry, P11/P18 vertical-space use, P24 figure readability and the dataset Question/readability treatment even though all corresponding rows were reported ready for review
problem: 当前 coverage matrix 仍然容易把“做过一次针对性改动 + 生成了 render”当作“已经足够值得 reviewer 接受”。把最终 `PASS` 留给 reviewer 是必要的，但还不够；executor-side readiness 也需要 requirement-level acceptance evidence，而不是 source diff 或 checklist presence。对重复问题应要求可观察、可比较的最终条件，例如同类 annotation gap 是否统一、arrow 是否真正接到 node boundary 且长度足够、主内容是否使用了可用纵向空间、图内文字是否达到最终展示字号下限。后续 Planner 应考虑把 `READY_FOR_REVIEW` 的门槛从“我改了”提升为“我能展示 reviewer 原始问题在 final render 中已被具体处理”。
project-specific context: CAT-TRACE 的具体页码、Malaise 图片、CORAL 文案和公式属于项目；通用问题是 reviewer feedback 必须按原始语义和最终 render 逐条验收，不能把“做过修改”弱化成“已经解决/已经 ready”。

### Presentations 0.2 completion evidence can still miss obvious rendered regressions
status: NEW
source: TRACE / CAT-TRACE 32-page group-meeting deck v5 review
evidence: `YuukiAS/TRACE` commit `1de90f2f26b3f787073ecedd7a4df41a985712eb`; executor produced the presentations 0.2 revision packet, rendered QA and English-final-pass artifacts, but human review still found a sample-axis/arrow collision, text/formula overlap inside an architecture node, awkward formula wrapping/spacing, and dense Question blocks on real-data slides
problem: 0.2 已把 existing-deck revision gate 接入 production，但 v5 证明“packet 字段齐全”仍不等于 rendered artifact 真的通过。尤其 text–formula/text–edge collision、窄框内数学断行、Question block 与邻接内容重叠等明显视觉错误，仍可能在 executor-side QA 里被标成可交付。需要后续 Planner 判断是 reviewer evidence 粒度不足、视觉 reviewer 没真正消费高分辨率页，还是 gate 还缺具体可见碰撞检查。
project-specific context: CAT-TRACE 的具体页码、公式和图形属于项目；通用问题是 production completion evidence 必须来自真实 render 的可见几何判断，而不是文件存在或自报 checklist。

### Deck-wide formula, text and emphasis scale still lacks a stable hierarchy
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v5 and v7 reviews
evidence: v5 shows an oversized residual formula, an oversized connective word and a too-small model-closure formula; v7 P18 still leaves a key three-step mathematical chain comparatively small in a large empty body area
problem: 当前 plugin 有“按科学重要性分配空间”的原则，但缺少足够稳定的 deck-level typography/math scale contract。核心公式、supporting formula、diagram/table 内数学、正文、caption/source、强调粗体之间会逐页漂移；`resizebox` 还可能把普通连接词和数学对象一起放大。需要一种模板相对、角色驱动的尺度层级，并把“页面有大量空白但 supporting/core math 仍然偏小”也纳入最终层级检查，而不是只防止公式过大。
project-specific context: 用户把 CAT-TRACE v5 P14 的核心 borrowing equation 视为当前 deck 可接受的最大公式视觉尺度，这是本 deck 的局部标尺；通用规则不应硬编码该页或某个绝对字号。

### Diagram planning needs a semantic-purpose gate before geometry
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v5 and v7 reviews
evidence: v5 phylogeny-borrowing slide produced a technically simple tree-like sketch without a clear visual explanation; v7 improved the semantics but still produced a chain with short detached-looking arrows and cramped node text such as a line containing only `only`, showing that semantic planning alone does not guarantee mature geometry
problem: 现有 Diagram Gate 已要求 semantic graph，但真实 production 仍可能先满足“节点和关系都在”，却没有形成自然、成熟的视觉解释。科研 diagram 在进入 TikZ/PPT composition 前应明确 audience-facing purpose、scientific objects、relationships、reading direction；进入 geometry 后还需要最小可见 edge length、node-to-node boundary clipping、peer gap consistency、line-break quality 等约束。不能因为语义图正确就接受难看的短箭头和机械换行。
project-specific context: A/B/C species tree、具体相关矩阵和 CAT-TRACE phylogeny prior 属于当前项目；通用问题是 diagram 的 semantic preflight 加 geometry invariants，而不是固定某种树图模板。

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
source: TRACE / CAT-TRACE group-meeting deck v4 and v7 reviews
evidence: v4 P3, P8–P10；v7 P10 still uses shortened arrows that visibly stop before node boundaries, while P13 packs successive node rows so tightly that arrows become tiny black segments despite large unused space below
problem: 现有 diagram semantic/geometry guidance 已存在，但实际 production 仍可能做出边界间距不一致、箭头过短、节点/文字过挤或需要图外补一句关系的 diagram。node-to-node connectors should normally clip naturally at node boundaries; arbitrary `shorten` should not create detached arrows. When arrows are too short, increase node/row spacing rather than compressing the edge. Peer edges should have comparable visible length and endpoint treatment.
project-specific context: CAT-TRACE matching / catalogue split 的具体节点与拓扑属于项目；通用问题是 node width、row/column gap、edge endpoint/clearance、minimum visible connector length 与 arrowhead 可读性需要最终 render 证据。

### Scientific hierarchy QA misses simultaneous crowding and unused space
status: PROMOTED_BY_045
source: TRACE / CAT-TRACE group-meeting deck v4 and v7 reviews
evidence: v4 P9, P20–P27；v7 P3, P11, P13, P18, P24 and P28–P30 again show the same pattern: too many small reading zones or cramped right columns while large parts of the body remain unused, so the primary object stays small even though the slide has available space
problem: active guardrail 已要求按科学重要性分配空间，但最终 render 仍会出现“局部拥挤 + 整页空”“核心公式/图/Question 很小但 body 仍有大量空白”。除了 overflow 检查，需要更具体的 information-slide composition grammar：一页通常只有一个主阅读路径，尽量限制到 2–3 个视觉区；优先采用“一句定义/问题 + 一个主视觉关系 + 一个必要例子/解释”，而不是同时堆多组卡片、diagram、table 和 prose。信息页若仍有约四分之一以上无意义空白而主对象偏小，应先重排/放大/拆页，而不是称为 clean。
project-specific context: P3 的 catalogue 解释、P11 CORAL、P24 oracle 和 dataset 右栏是当前证据；通用问题是 composition grammar 与 usable-area 转化为可读性的 QA。

### Figure readability and caption pairing are not checked at the rendered-content level
status: PROMOTED_BY_045
source: TRACE / CAT-TRACE group-meeting deck v4 and v7 reviews
evidence: v4 P20, P24–P26；v7 P24 enlarged the outer oracle image but the 2x2 plot's internal axes, legend and panel text remain too small; v7 P28–P30 also show prevalence/secondary figures whose internal text is not comfortably readable at projected slide size
problem: plugin 已经要求主图可读，但实际检查仍偏向 image object 是否存在/是否够大。若原始 manuscript/report figure 的内部字体不适合投影，单纯放大 `includegraphics` 不应算修复；应允许/要求生成 presentation-specific figure，减少内部白边、扩大 axis/tick/legend/panel text、简化 legend/caption。最终 QA 需要有图内文字的最小视觉字号/可读性门槛。
project-specific context: Finland/Madagascar/Victoria prevalence 图和 grouped-richness oracle 属于 TRACE；通用问题是 figure-content bbox、内部字体、caption pairing 和 presentation-specific regeneration。

### Table, list and paragraph primitives still drift across one deck
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4, v5 and v7 reviews
evidence: v4 P11–P13, P21–P26；v5 metabarcoding definition block and tables; v7 P3 still reads heavily because one concept is split across a definition paragraph, three boxed statements, a separate sample matrix and a bottom example paragraph
problem: paragraph/list/table 的选择规则还不足以覆盖整页 composition。连续论证适合短 paragraph；多个并列、可独立理解的定义/事实适合 bullets；重复比较相同属性或数值对齐才适合 table。除此以外，还应限制同一页同时出现的 container/primitive 类型：不要为了“结构化”把一个简单关系拆成多组卡片 + diagram + prose。相同意思的事实应该合并，而不是分别占一个 box。
project-specific context: P3 的 VicFlora/catalogue 页面是新的真实证据；通用问题是 paragraph/bullet/table 选择与 information-slide composition grammar。

### Complex multi-slide models can finish without a model-closure page
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: v4 Model section P9–P16；用户看完各组件后仍无法快速重建“完整模型到底由哪些部分组成”
problem: one-slide-one-job 规则能避免单页过载，但复杂模型被拆成多页后，plugin 没有检查 section 结束时听众能否重新拼回完整 generative/model structure。需要一种 model-closure / reassembly 页面模式，而不是再画一张重复的自由流程图。
project-specific context: finite catalogue、open tail、matching、residual dependence 等具体组件属于 CAT-TRACE；通用问题适用于任何被拆成多页讲解的复杂统计/机器学习模型。

### Question/background callout lacks a stable research-deck primitive
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4–v7 reviews
evidence: v5 introduced a purple-line Question treatment; v6 improved geometry and v7 added purple question text, but on v7 P28–P30 the Question is still forced into a narrow right column with small type and heavy wrapping, so the primitive remains visually weak even though its color treatment is more coherent.
problem: simulation question 与 advisor discussion 都需要一种轻量、成熟、非卡片化的 emphasis primitive。Question primitive 需要明确 vertical centering、line height、padding、color hierarchy 和**minimum readable size**；当窄栏不能容纳正常字号时，Question 应改成 full-width block 或页面底部横向区，而不是继续缩字/多行挤压。Background 仍只恢复回答问题所需的 1–2 条事实。
project-specific context: CAT-TRACE dataset 右栏和具体颜色属于项目；通用问题是 Question/Background 的信息、视觉合同和 responsive layout fallback。

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
candidate_action: 只有新的真实 deck 再次暴露问题时，才补 renderer-level primitive 和 QA，不为了历史 TODO 预先造一整套几何系统。
promotion_gate: 新的真实 CAT-TRACE 或 unrelated deck 用实际 render 重现问题，并能证明修改真的改善输出且不会过度限制其他 diagram。

### Deck-wide style system and terminology hierarchy
status: CANDIDATE_GENERIC
source: repeated real research deck revisions
evidence: presentation maintenance archive
target layer: reasoning/rendering/qa
problem: 一整套 deck 里，标题大小写、术语首次解释、dataset/simulation 编号、小标题、metric label、caption 和 references 容易逐页漂移。
candidate_action: 只有真实返修再次证明这是当前问题时，才增加最小 deck-wide consistency contract，不把所有页面强行做成同一种布局。
promotion_gate: independent rendered deck 证明 consistency check 能抓到真实问题且不会压平不同科研页面。

### Math and theory slide hierarchy
status: CANDIDATE_GENERIC
source: repeated statistics and theory deck feedback
evidence: presentation maintenance archive + CAT-TRACE review docs
target layer: reasoning/rendering/qa
problem: definition、design setting、estimand、theorem、derivation 容易都被做成同一种“居中大公式”，科学角色没有层次。
candidate_action: 在新的 math-heavy real deck 再次出现时，才进一步加强公式层级、首次语义解释和 theory-page QA。
promotion_gate: theorem/statistical-method real deck replay + unrelated math-heavy deck regression。

### Simulation, metric and structured-fact presentation
status: CANDIDATE_GENERIC
source: repeated real statistics deck feedback
evidence: presentation maintenance archive
target layer: reasoning/rendering/qa
problem: DGP、estimand、baseline、metric direction、dataset facts、seed/reproducibility 信息容易混成段落或弱表格，读起来很累。
candidate_action: 新的 simulation-heavy / real-data deck 再次出现时，再提炼更稳定的 table/list patterns 和 QA。
promotion_gate: 至少一个 simulation-heavy 和一个 real-data deck 的真实 render 都证明改善了可读性。

### Natural scientific slide language
status: CANDIDATE_GENERIC
source: repeated presentation and writing-style feedback
evidence: presentation maintenance archive + `docs/plugin-todos/writing-style.md`
target layer: writing/qa
problem: slides 仍可能出现内部流程词、模板化对比句、面向作者而不是面向听众的说法。
candidate_action: 真实失败出现后再决定应该改 `research-presentations`、`scientific-prose`，还是两者的交接；不要重复造一套写作规则。
promotion_gate: 多个独立英文科研 slide 的真实证据。

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
