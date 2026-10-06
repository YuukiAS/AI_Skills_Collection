# presentations — Long-Term TODO

这是 `presentations` plugin 的长期问题清单。

以后在 TRACE、CARE 或其他真实项目里调用 `presentations` 时，如果问题本质上来自 plugin 的生成、返修、布局、检查或路由行为，直接把这次真实问题写到这里，状态先用 `NEW`。不要先在项目 repo 再维护一份 Presentation 插件问题副本。

Current capability status: `baseline`.

## Incoming real-use feedback

### CAT-TRACE v13/v14 follow-up feedback is consolidated into the canonical inbox
status: NEW
tracking: #29
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
tracking: #30
source: TRACE / CAT-TRACE 35-page group-meeting deck v11 review
evidence: `YuukiAS/TRACE` commit `06511e3d5444ae8be847ef42ea362c19f6d787f9`; the deck ends with three advisor-facing questions on stronger infinite-tail theory, identifiability constraints for catalogue borrowing, and computational scope. Independent review found that the questions are useful only because each unlocks a real project decision, but the current presentation workflow checks Question/Background styling more strongly than whether the question is worth asking, whether the intended advisor can reasonably answer it, and whether the presenter is prepared for the obvious follow-up questions. The user explicitly wants this judgment applied to future presentations, with likely advisor counterquestions and prepared responses kept in speaker notes or review evidence rather than cluttering the visible slide.
problem: Before an advisor/supervisor discussion question is accepted into a research deck, the presentation layer should record: (1) the concrete project decision the answer would change; (2) why that decision matters now; (3) whether this audience has the expertise/context to answer; (4) the presenter's current leaning rather than outsourcing all judgment to the advisor; (5) the most likely counterquestion/pushback; and (6) a concise prepared response. Questions that do not unlock a real decision, are not answerable by the audience, or exist only to make the Discussion section look interactive should be removed or rewritten. The visible slide usually needs only Question + minimal Background/options; counterquestion preparation belongs in speaker notes or an executor/reviewer artifact.
project-specific context: CAT-TRACE's exact three questions and the user's current preferred answers belong to TRACE. The generic issue is advisor-question quality, answerability and presenter preparation.

### Page-level language audits can pass while sentence and slide transitions remain mechanical
status: NEW
tracking: #31
source: TRACE / CAT-TRACE 34-page group-meeting deck v10 review
evidence: `YuukiAS/TRACE` commit `3d7bc06dd0f9a80bb87a863e8a74398bc0f866bf`. The v10 `full_deck_language_audit.md` marked every page P2–P34 `READY_FOR_REVIEW`, yet independent review still found that P2 and P3 read as individually correct sentences placed next to one another rather than one explanation, and that several slide boundaries still lacked a natural scientific handoff: metabarcoding -> OTU, the two discovery questions -> TRACE, TRACE -> HMSC, marked tails -> residual dependence, and priors -> full-model closure. The page-level audit described each page's intended meaning but did not actually test why sentence k leads to sentence k+1 or why slide k creates the need for slide k+1.
problem: Research-presentation language QA needs a **coherence/transition layer in addition to plain-language cleanup**. Within a slide, consecutive sentences should form an explicit causal, temporal, inferential or explanatory chain rather than a list of independently acceptable statements. Across slides, the reviewer should inspect the end of slide k together with the beginning of slide k+1 and ask what unresolved question, limitation or next object creates the transition. This must preserve the existing audience/page-job/first-use/plain-language rules rather than replace them. A useful evidence artifact is a short `transition_map` recording the scientific state at the end of each page and why the next page follows.
project-specific context: The exact CAT-TRACE sequence (survey -> catalogue -> metabarcoding -> OTU -> unseen discovery -> TRACE -> HMSC/CORAL -> CAT-TRACE) belongs to this deck. The generic problem is that sentence-level and page-level correctness do not guarantee narrative continuity.

### Accent colour and emphasis can drift without a semantic-role contract
status: NEW
tracking: #32
source: TRACE / CAT-TRACE 34-page group-meeting deck v10 review
evidence: `YuukiAS/TRACE` commit `3d7bc06dd0f9a80bb87a863e8a74398bc0f866bf`, especially P12 where a full ordinary sentence (`Both components can be coupled...`) is rendered in accent purple without a stable semantic reason, while `Example:`, `Question`, `Takeaway:` and `Limitation for our setting:` are also using accent treatments elsewhere.
problem: Presentation colour should encode stable semantic roles, not act as a generic importance marker. Ordinary explanatory prose should remain neutral by default. Accent colour may be reserved for a small set of reusable roles such as section/subheading labels, `Example:`, `Takeaway:`, `Question`, `Limitation`, and controlled semantic colouring inside equations/diagrams. The final deck-wide consistency pass should flag an entire prose sentence in accent colour when it does not belong to an approved role.
project-specific context: CUHK purple and the exact CAT-TRACE labels are project/template details. The generic issue is semantic emphasis consistency across a deck.

### Citation style, bibliography fidelity, and PDF text-layer integrity need one delivery contract
status: NEW
tracking: #33
source: TRACE / CAT-TRACE 34-page group-meeting deck v10 review
evidence: `YuukiAS/TRACE` commit `3d7bc06dd0f9a80bb87a863e8a74398bc0f866bf`. v10 uses role labels such as `Source:`, `Figure:` and `Data:`, but short-credit formatting still varies, the References slide contains several paraphrased/shorthand article titles rather than verified full bibliographic titles, and the compiled PDF text layer maps ordinary digits such as years/page numbers to incorrect Unicode characters when extracted/copied even though the rendered glyphs look correct.
problem: A research-deck delivery should distinguish three layers: (1) concise on-slide role-labelled citations; (2) a verified References bibliography generated from real metadata rather than author-written shorthand titles; and (3) PDF text-layer integrity. The plugin should encourage one house citation style per deck, prohibit invented/paraphrased bibliography titles, and require source metadata verification from BibTeX/Zotero/journal metadata or another authoritative source. Final PDF QA should run text extraction/copyability checks for ordinary ASCII digits, years, page numbers and citation text, so a visually correct PDF with broken ToUnicode/font mapping cannot pass delivery.
project-specific context: The specific TRACE papers, VicFlora and current XeLaTeX/theme font issue belong to this deck. The generic issue is citation-system consistency plus searchable/copyable PDF text integrity.

### Audience/page-job briefing before prose handoff materially improved a real research deck
status: NEW
tracking: #34
source: TRACE / CAT-TRACE 34-page group-meeting deck v9 review
evidence: `YuukiAS/TRACE` commit `c271e0f546ce7f38f35f70165f2c2ee7b6580b36`; v9 preflight confirms the active runtime was still `presentations 0.3` + `writing-style 0.1` and that the AI_Skills pull changed only TODO docs, not runtime files. The large language improvement came from the task/workflow instead: before drafting/revising prose it explicitly fixed the target audience, each slide's scientific job, why unfamiliar terms appear there, what the audience should remember, and then ran a full-deck first-use registry plus page-by-page language audit over P2–P34. The final human review judged v9's language markedly better than v8 even though the prose runtime itself had not changed.
problem: This is strong positive evidence that `presentations` should own a **pre-writing audience/page-job brief** rather than merely hand already-written slide text to `scientific-prose`. For each content slide, presentation orchestration should establish: audience assumptions, the one scientific point of the page, prerequisite context, why each unfamiliar term is needed now, and the intended plain-language takeaway. That brief should then be handed to `writing-style`/`scientific-prose` to produce or revise the English. `presentations` should not duplicate prose-style rules; its responsibility is to provide the semantic/audience brief, require the writing handoff after scientific freeze, and then reread the final rendered deck for reader effort. The v9 `first_use_registry.md` and `full_deck_language_audit.md` are useful evidence patterns for this boundary.
project-specific context: CAT-TRACE, VicFlora, COI, OTU, MGP and specific slide wording belong to TRACE. The generic lesson is orchestration: audience -> page job -> prerequisite/context -> term role -> takeaway -> writing-style -> rendered reader-effort review.

### Full-deck audience-context and responsive-layout review still regresses after repeated real revisions
status: NEW
tracking: #35
source: TRACE / CAT-TRACE 33-page group-meeting deck v8 review; STAT5060 Tutorial 1 annotated teaching deck review, 2026-09-29
evidence: STAT5060 adds unrelated real-use evidence: pages 8–10, 12–14, 18, 20 and 22 were called out for weak composition despite no simple overflow failure - content stranded at page bottoms, awkward side-by-side figure/table pairings, over-centred captions, a cramped posterior-summary/PPC page, and a visibly inconsistent type scale on page 22. Existing TRACE evidence: `YuukiAS/TRACE` commit `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. v8 successfully fixed several long-running issues by adding spacing tokens and regenerating presentation-specific figures, but human/GPT review still found: inconsistent same-role label scale/gutters on P2; a cognitively repetitive catalogue explanation on P3; first-use terms on P4/P19 that were expanded without enough local purpose/context; repeated/non-unified Example treatment across P3/P5/P15; diagram transition text on P10 colliding with arrows or wrapping formulas awkwardly; sequential CORAL content still arranged as three columns despite large unused vertical space; short table row labels wrapping unnecessarily on P16; a newly introduced duplicate `diag(Sigma_W)=1` step on P18; a contextless MGP acronym and defensive source-note-like threshold sentence on P19; cramped oracle-side text on P24; inconsistent Question line spacing/hyphenation across P27-P29; and P29/P30 body compositions whose figure/data regions remain visually unbalanced. The v8 English-final-pass record also states that it only reviewed visible wording touched in v8.
problem: The production path now has many local rules, but it still lacks a sufficiently strong full-artifact reader-effort gate. A final presentation review should not ask only whether each requested object changed. It must inspect every final page for: (1) unfamiliar term introduced with both expansion and immediate purpose/context; (2) one clear reading path with minimal semantic repetition; (3) columns used only for genuinely peer-level comparison, not sequential stages; (4) same-role typography, gutters, question leading and intra-node text/formula spacing; (5) short labels kept on one line when space permits; (6) no new duplicate math, awkward hyphenation, defensive/meta prose or source-note language introduced by a repair; and (7) responsive fallback when a region becomes cramped. Full-deck language/readability QA must cover the final rendered artifact, not only source lines edited in the current round.
project-specific context: VicFlora, COI, metabarcoding, MGP, CAT-TRACE equations and specific page numbers belong to TRACE. The generic issue is full-deck audience-context, cognitive-load, responsive layout and no-new-regression review, not a CAT-TRACE-specific template.

### Review coverage can self-certify unresolved reviewer feedback
status: NEW
tracking: #36
source: TRACE / CAT-TRACE 33-page group-meeting deck v6 and v7 reviews
evidence: `YuukiAS/TRACE` commits `ef08bc25673fb33b639e523504676c0f333d93f4` and `e5bce0c0b8d24b33aa6930a2ea8f9a8a9c86e252`; v6 `v5_review_coverage.md` marked all 21 prior review points `PASS` despite unresolved issues. v7 correctly downgraded executor labels to `READY_FOR_REVIEW`, but the subsequent human/GPT review still found repeated failures in P2 annotation spacing, P10/P13 arrow geometry, P11/P18 vertical-space use, P24 figure readability and the dataset Question/readability treatment even though all corresponding rows were reported ready for review
problem: 当前 coverage matrix 仍然容易把“做过一次针对性改动 + 生成了 render”当作“已经足够值得 reviewer 接受”。把最终 `PASS` 留给 reviewer 是必要的，但还不够；executor-side readiness 也需要 requirement-level acceptance evidence，而不是 source diff 或 checklist presence。对重复问题应要求可观察、可比较的最终条件，例如同类 annotation gap 是否统一、arrow 是否真正接到 node boundary 且长度足够、主内容是否使用了可用纵向空间、图内文字是否达到最终展示字号下限。后续 Planner 应考虑把 `READY_FOR_REVIEW` 的门槛从“我改了”提升为“我能展示 reviewer 原始问题在 final render 中已被具体处理”。
project-specific context: CAT-TRACE 的具体页码、Malaise 图片、CORAL 文案和公式属于项目；通用问题是 reviewer feedback 必须按原始语义和最终 render 逐条验收，不能把“做过修改”弱化成“已经解决/已经 ready”。

### Presentations 0.2 completion evidence can still miss obvious rendered regressions
status: NEW
tracking: #37
source: TRACE / CAT-TRACE 32-page group-meeting deck v5 review
evidence: `YuukiAS/TRACE` commit `1de90f2f26b3f787073ecedd7a4df41a985712eb`; executor produced the presentations 0.2 revision packet, rendered QA and English-final-pass artifacts, but human review still found a sample-axis/arrow collision, text/formula overlap inside an architecture node, awkward formula wrapping/spacing, and dense Question blocks on real-data slides
problem: 0.2 已把 existing-deck revision gate 接入 production，但 v5 证明“packet 字段齐全”仍不等于 rendered artifact 真的通过。尤其 text–formula/text–edge collision、窄框内数学断行、Question block 与邻接内容重叠等明显视觉错误，仍可能在 executor-side QA 里被标成可交付。需要后续 Planner 判断是 reviewer evidence 粒度不足、视觉 reviewer 没真正消费高分辨率页，还是 gate 还缺具体可见碰撞检查。
project-specific context: CAT-TRACE 的具体页码、公式和图形属于项目；通用问题是 production completion evidence 必须来自真实 render 的可见几何判断，而不是文件存在或自报 checklist。

### Deck-wide formula, text and emphasis scale still lacks a stable hierarchy
status: NEW
tracking: #38
source: TRACE / CAT-TRACE group-meeting deck v5 and v7 reviews; STAT5060 Tutorial 1 annotated teaching deck review, 2026-09-29
evidence: STAT5060 independently exposed the same hierarchy drift: page 22 mixed visibly different text scales in one dense frame, page 18 made the formula/plot/table hierarchy feel unbalanced, and several sparse pages left key explanatory objects smaller than the available space justified. Existing TRACE evidence: v5 shows an oversized residual formula, an oversized connective word and a too-small model-closure formula; v7 P18 still leaves a key three-step mathematical chain comparatively small in a large empty body area
problem: 当前 plugin 有“按科学重要性分配空间”的原则，但缺少足够稳定的 deck-level typography/math scale contract。核心公式、supporting formula、diagram/table 内数学、正文、caption/source、强调粗体之间会逐页漂移；`resizebox` 还可能把普通连接词和数学对象一起放大。需要一种模板相对、角色驱动的尺度层级，并把“页面有大量空白但 supporting/core math 仍然偏小”也纳入最终层级检查，而不是只防止公式过大。
project-specific context: 用户把 CAT-TRACE v5 P14 的核心 borrowing equation 视为当前 deck 可接受的最大公式视觉尺度，这是本 deck 的局部标尺；通用规则不应硬编码该页或某个绝对字号。

### Diagram planning needs a semantic-purpose gate before geometry
status: NEW
tracking: #39
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
tracking: #40
source: TRACE / CAT-TRACE group-meeting deck v4, v5 and v7 reviews; STAT5060 Tutorial 1 annotated teaching deck review, 2026-09-29
evidence: STAT5060 adds teaching-mode evidence: the user explicitly asked whether page 12 should use bullets or prose, requested interpretation next to tables rather than a table alone, disliked a figure and table forced side-by-side on page 18, and found multiple pages to have facts placed in visually arbitrary bottom paragraphs. Existing TRACE evidence: v4 P11–P13, P21–P26；v5 metabarcoding definition block and tables; v7 P3 still reads heavily because one concept is split across a definition paragraph, three boxed statements, a separate sample matrix and a bottom example paragraph
problem: paragraph/list/table 的选择规则还不足以覆盖整页 composition。连续论证适合短 paragraph；多个并列、可独立理解的定义/事实适合 bullets；重复比较相同属性或数值对齐才适合 table。除此以外，还应限制同一页同时出现的 container/primitive 类型：不要为了“结构化”把一个简单关系拆成多组卡片 + diagram + prose。相同意思的事实应该合并，而不是分别占一个 box。
project-specific context: P3 的 VicFlora/catalogue 页面是新的真实证据；通用问题是 paragraph/bullet/table 选择与 information-slide composition grammar。

### Complex multi-slide models can finish without a model-closure page
status: NEW
tracking: #41
source: TRACE / CAT-TRACE group-meeting deck v4 review
evidence: v4 Model section P9–P16；用户看完各组件后仍无法快速重建“完整模型到底由哪些部分组成”
problem: one-slide-one-job 规则能避免单页过载，但复杂模型被拆成多页后，plugin 没有检查 section 结束时听众能否重新拼回完整 generative/model structure。需要一种 model-closure / reassembly 页面模式，而不是再画一张重复的自由流程图。
project-specific context: finite catalogue、open tail、matching、residual dependence 等具体组件属于 CAT-TRACE；通用问题适用于任何被拆成多页讲解的复杂统计/机器学习模型。

### Question/background callout lacks a stable research-deck primitive
status: NEW
tracking: #42
source: TRACE / CAT-TRACE group-meeting deck v4–v7 reviews
evidence: v5 introduced a purple-line Question treatment; v6 improved geometry and v7 added purple question text, but on v7 P28–P30 the Question is still forced into a narrow right column with small type and heavy wrapping, so the primitive remains visually weak even though its color treatment is more coherent.
problem: simulation question 与 advisor discussion 都需要一种轻量、成熟、非卡片化的 emphasis primitive。Question primitive 需要明确 vertical centering、line height、padding、color hierarchy 和**minimum readable size**；当窄栏不能容纳正常字号时，Question 应改成 full-width block 或页面底部横向区，而不是继续缩字/多行挤压。Background 仍只恢复回答问题所需的 1–2 条事实。
project-specific context: CAT-TRACE dataset 右栏和具体颜色属于项目；通用问题是 Question/Background 的信息、视觉合同和 responsive layout fallback。

### Slide source/figure citation style is inconsistent and underspecified
status: NEW
tracking: #43
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


### Course-standard teaching template needs structural navigation, not only colours and bands
status: PROMOTE_NOW
tracking: #49
planner disposition: promoted only into Presentations Stage 1 two-template adapter foundation; implementation remains pending execution-ready Critic PASS
source: STAT5060 Tutorial 1 annotated Beamer review, 2026-09-29
evidence: `YuukiAS/STAT5060-TA` work branch `work/stat5060--tutorial-01-v2`, content commit `4366e33bb58594ead5156002eba0aae30a2595dd`; 27-page Beamer candidate reviewed by the user with 56 highlight annotations in a local annotated PDF (not committed to this public repo). The first real course-standard use was judged too bare even though the blue-title/white-body visual direction was acceptable.
problem: The current `course-standard` contract captures a 4:3 reference look, frame-title colour, bullets and page number, but real teaching use needs a fuller structural shell: a deliberately sparse opening slide, section-aware navigation, PDF outline/bookmarks, top/bottom navigation/action affordances where the Beamer runtime supports them, stable footline/page-number behaviour, and an intentional concluding frame. Template identity should separate this structural/navigation grammar from a rigid aspect ratio: exact Chapter1 reproduction may default to 4:3, but a user-requested 16:9 teaching deck should be able to preserve the same course-standard identity instead of falling back to an unrelated template.
project-specific context: STAT5060 exact section names, page count and tomorrow's tutorial content remain course-local. The generic issue is that a teaching template is more than colours/fonts; it also owns opening/closing structure, section state, navigation/bookmarks and ratio-aware identity.
candidate_action: Treat this as a narrow Stage-1 course-standard template-contract amendment before the two-template foundation is implemented. Do not pull later composition/storyline intelligence into Stage 1.

### Teaching decks need a presenter-learning companion distinct from student-visible slides
status: NEW
tracking: #50
source: STAT5060 Tutorial 1 annotated Beamer review, 2026-09-29
evidence: user marked technically acceptable content in blue where the presenter still needed to learn how to explain it, especially the Poisson Pearson-residual plot and model-misspecification interpretation; yellow questions also asked what NB2 means, what adding a random intercept changes, why the simulation uses a chosen kappa, what the true slope 0.5 represents, and how to interpret posterior diagnostics.
problem: A teaching deck can be visually correct and student-readable while still leaving the presenter unable to teach the method confidently. Teaching mode needs an optional instructor-learning artifact separate from speaker-facing slide copy: for each nontrivial diagnostic/model object, record why it appears, what the displayed object means, how to read a good/poor pattern, what a common misconception is, one likely student question, and a source anchor for deeper review. This material must not inflate student slides or turn ordinary speaker notes into an internal QA dump.
project-specific context: Poisson residuals, NB2, Ohio GLMM, the specific simulation and PyMC/brms details belong to STAT5060. The generic gap is presenter preparation for technical teaching content.
candidate_action: Keep out of Stage 1 template implementation. Promote later only as a bounded teaching-mode notes/companion capability, ideally consuming source-grounded domain explanations rather than inventing pedagogy from layout rules.

### Teaching presentations need optional lecture/source cross-references without duplicating the lecture
status: NEW
tracking: #51
source: STAT5060 Tutorial 1 annotated Beamer review, 2026-09-29
evidence: on the multinomial/alligator section the user asked for an explicit pointer to the relevant Lecture Note page so students can connect Tutorial material back to the course source, while also warning not to repeat too much of the Lecture or conflict with it.
problem: Current source-fidelity machinery is mostly internal. Teaching presentations sometimes need a small audience-facing cross-reference such as “Lecture 2, pp. 42–46” or an equivalent source cue so students know where the model was introduced. The cue should be optional, compact and source-verified; it must not become citation clutter, reproduce the lecture, or let a tutorial silently contradict the canonical course source.
project-specific context: the exact Chapter 2/3 pages and course file locations belong to STAT5060. The generic issue is a teaching-source anchor that connects derived tutorial material to canonical lecture material without duplicating it.
candidate_action: Record now; implement after the base course-standard adapter unless the existing source/citation layer already supports a trivial teaching-source role.

### Assessment-introduction slides need answer-leakage and provisional-administration guardrails
status: NEW
tracking: #52
source: STAT5060 Tutorial 1 annotated Beamer review, 2026-09-29
evidence: the user rejected a detailed “Tutorial topic -> Application in HW1” matrix because it felt like a solution scaffold rather than a student-facing tutorial slide; the course-assessment/project pages also need to tolerate still-unknown dates and evolving oral-defense details without sounding like internal engineering status.
problem: Teaching decks that introduce homework/projects need a distinct audience contract. They should explain what the assessment is for, broad deliverables, what skills students are expected to demonstrate, and what information is confirmed vs forthcoming. They should not expose internal alignment matrices, rubric logic, model-by-model answer hints, or unstable administrative placeholders. Provisional details should use normal course language (“details will be announced on Blackboard / stay tuned”) rather than “unconfirmed/release blocker” language. Project rationale may explain why the assessment format changed (for example, to emphasize analysis and explanation in an AI-assisted environment) without leaking grading internals.
project-specific context: STAT5060's exact HW1 questions, deadlines, weights, oral-defense duration and AI policy are course-local and remain in the course repo. The generic issue is student-facing assessment introduction versus instructor/internal assessment design.
candidate_action: Keep out of Stage 1 template work. Use the current tutorial as real evidence for a later teaching-mode semantic/composition guardrail.

### Closing frames need a teaching-purpose contract, not a generic Questions/Thanks default
status: NEW
tracking: #53
source: STAT5060 Tutorial 1 annotated Beamer review, 2026-09-29
evidence: the user explicitly questioned whether the final frame should be a question, a takeaway, a Thanks frame, or another conclusion form, and whether the current “What evidence would make you reconsider a fitted model?” actually aligns with Tutorial 1, HW1 and Lectures 2–3.
problem: The presentation layer should choose the closing job from the talk's purpose. For a teaching deck, an integrative question can be useful when it rehearses the central reasoning students need next; a recap is better when the session introduced several methods that need consolidation; a bare “Thanks” is only a terminal social frame and should not replace pedagogical closure. Template structure should provide a closing frame slot, while semantic planning chooses recap/question/Q&A/thanks based on audience and next action. The closing prompt itself must be checked against the actual lecture/tutorial/assessment goals rather than generated as generic reflective prose.
project-specific context: the current STAT5060 closing question belongs to this tutorial. The generic issue is structural closing support plus a purpose-driven choice of closing content.
candidate_action: Split ownership: Stage 1 template may add a canonical closing-frame primitive; semantic choice should remain a later composition/storyline responsibility.



### Final presentation reviewer must be extracted from the human-accepted STAT5060 reviewer, not reconstructed from memory
status: NEW
tracking: #54
source: STAT5060 Tutorial 1 V4–V7 repeated false-positive review cycle, 2026-09-29
evidence: `YuukiAS/STAT5060-TA` work branch `work/stat5060--tutorial-01-v2`; V4/V5/V6 all produced executor/reviewer PASS artifacts that were immediately rejected by the user after inspecting the rendered PDF. The review protocol is still being hardened in the course repo and is not yet frozen.
problem: Presentations currently has reviewer logic, but repeated real use shows that a reviewer can still self-certify a visibly poor deck by over-weighting mechanical evidence such as successful build, no clipping, page count, outline existence, or executor-written closure narratives. The final generic reviewer must not be reinvented later from these intermediate TODO notes. Once the STAT5060 reviewer reaches a human-accepted frozen version, Presentations should extract that exact reviewed contract, genericize only course-specific names/thresholds, preserve the acceptance semantics, and regression-test it against the known V4/V5/V6 rejected artifacts.
candidate_action: Do not promote an intermediate STAT5060 reviewer into production. Add an explicit extraction task after the Tutorial reaches human acceptance: record exact source commit/path, copy the final reviewer contract into Presentations, remove course-specific details, and verify that historical rejected decks still deterministically fail.
promotion_gate: human acceptance of a final STAT5060 Tutorial reviewer package + successful replay on at least V4, V5 and V6 rejected artifacts + one unrelated deck.
project-specific context: STAT5060 page numbers, lecture references, assessment wording and exact course slides stay in `STAT5060-TA`. The generic asset to extract is the reviewer architecture and gate semantics.

### Reviewer calibration must be blind, artifact-bound and proven before candidate review
status: NEW
tracking: #55
source: STAT5060 Tutorial 1 V6/V7 reviewer hardening
evidence: the initial calibration proposal exposed the expected V6 failure list to the reviewer before calibration, making it possible to pass by paraphrasing the answer sheet rather than detecting defects from pixels.
problem: A reviewer-quality check is meaningless if the reviewer sees the expected failures in advance. Presentation review needs a blind pre-gate: a fresh isolated calibration run receives only a rejected artifact, rendered evidence, role and broad categories; an external aggregator holds the expected minimum-hit set. Candidate review starts only after calibration proves that the reviewer independently detected the required defects with page/evidence/concrete observation. Calibration run identity and output hash should travel with the candidate-review artifact.
candidate_action: Add reviewer calibration as a reusable QA primitive after #54 is extracted. Keep expected failure sets outside the reviewer context; never pass human-rejection answer keys into the calibration run.
promotion_gate: replay where a weak/answer-fed reviewer fails calibration while a genuinely pixel-reading reviewer passes, without requiring project-specific page names.

### Human rejection must invalidate prior reviewer PASS and create persistent regression guards
status: NEW
tracking: #56
source: STAT5060 Tutorial 1 V4–V7; repeated recurrence of already-rejected patterns
evidence: after prior PASS claims, later candidates reintroduced previously rejected behaviour including answer-mapping assessment slides, first-use violations, AI-like source wording, oversized diagram elements, cramped code stacks and weak closing frames.
problem: Current revision workflows can treat the latest candidate as a fresh deck and forget that a human already rejected specific visible patterns. A human rejection must be higher authority than any earlier executor/reviewer PASS. Every rejection should produce a persistent regression-guard ledger that later candidates must check explicitly; a candidate cannot pass merely because the original page changed enough that the old finding no longer matches by line number.
candidate_action: Store semantic regression guards such as “no answer scaffold”, “no first-use before introduction”, “no low-contrast header”, “no internal QA language”, rather than page-number-only fixes. On every later round, report ABSENT/PRESENT against the full final render.
promotion_gate: at least one replay where the guard ledger catches a regression that ordinary changed-page review misses.

### Independent presentation review needs role separation, verdict isolation and role-scoped closure
status: NEW
tracking: #57
source: STAT5060 Tutorial 1 V6/V7 reviewer redesign
evidence: repeated false PASS showed that one generic reviewer can shallowly repeat executor claims. The hardened course review separates visual/template QA from teaching/language QA and isolates their verdicts.
problem: One reviewer asked to judge template fidelity, figure readability, natural scientific language, pedagogy, first-use order and assessment boundaries tends to perform each shallowly. The generic reviewer system should support at least two independent roles: visual/presentation and teaching/language (or domain/audience for non-teaching decks). Both inspect the full deck, but each owns explicit gates. Neither sees executor PASS narratives or the other reviewer verdict before freezing its own decision. Round-2 closure is role-scoped; only an aggregator checks the union after both verdicts freeze and it cannot override reviewer findings.
candidate_action: Promote only after the final STAT5060 reviewer is frozen; preserve distinct run IDs, isolated contexts, role-owned finding IDs, full-deck re-review after repair and aggregator non-override semantics.
promotion_gate: successful two-role replay on a rejected deck where each role catches distinct failures and neither can hide the other's failure behind a top-level PASS.

### Rendered-pixel review must use whole-slide projection scale before zoomed diagnostics
status: NEW
tracking: #58
source: STAT5060 Tutorial 1 V4–V7 + CAT-TRACE figure-readability failures
evidence: reviewers repeatedly called small plots/readability acceptable when high-resolution evidence could be zoomed, even though the same axes, legends and labels were poor in the whole projected slide.
problem: High-resolution screenshots can make an unreadable slide appear acceptable. Presentation QA should judge every page first at a fixed whole-slide projection representation (for example 1920×1080 fit-to-screen, no zoom), then use high-resolution pages/crops only to diagnose failures. Figure-internal text, code, tables, header/footer controls and captions must be judged at the final rendered scale.
candidate_action: Add a mandatory whole-slide evidence tier and make high-res diagnostic-only. A page that fails whole-slide readability cannot be rescued by a zoomed crop.
promotion_gate: historical replay where at least one figure passes zoomed inspection but correctly fails whole-slide review.

### Template QA must test semantic behaviour and optical geometry, not element presence
status: NEW
tracking: #59
source: STAT5060 Tutorial 1 V5–V7 course-standard template iterations
evidence: a candidate contained section labels, dots, navigation symbols and page numbers yet remained visibly poor: inactive labels/dots had weak contrast, current-state emphasis was unclear, footer controls and page number were not optically aligned, and ordinary navigation leaked onto title/closing frames.
problem: “Section dots exist” and “footer exists” are not enough. Template review needs semantic and geometric invariants: section/bookmark order, dot count/order/current state, readable active/inactive contrast, title/closing special behaviour, stable source safe-zone, and optical alignment of navigation controls with page number. Renderer/source implementation details such as independent raisebox hacks should not be accepted when the final pixels remain misaligned.
candidate_action: Add template-specific rendered crops/evidence and behaviour checks to course-standard and CUHK-research adapters. Keep thresholds template-relative, with contrast and pixel-alignment checks used as evidence rather than universal design constants.
promotion_gate: replay on at least one failed teaching template and one research template.

### First-use dependency checks must inspect legends, plot titles, captions, annotations and footers
status: NEW
tracking: #60
source: STAT5060 Tutorial 1 V6 first-use regression
evidence: the crab-data slide displayed an NB2 curve/legend before NB2 had been introduced, while body-text-oriented review still reported the sequence as acceptable.
problem: Current first-use checks can miss scientific concepts introduced visually. A term/model shown in a legend, figure title, caption, annotation, table label or footer counts as audience-visible use. Narrative-order QA must build first-use from the final rendered artifact, not only body copy or source headings.
candidate_action: Extend first-use/dependency scan to every visible text surface and figure semantics. When a concept is intentionally previewed, the planner must explicitly justify the preview rather than letting it happen accidentally.
promotion_gate: replay where a visual legend/caption first-use violation is caught although body text alone would pass.

### Figure-caption policy must be semantic: explain the scientific object, never narrate the slide
status: NEW
tracking: #61
source: STAT5060 Tutorial 1 V7 emergency repair
evidence: a mechanical “every image needs a caption” interpretation generated audience-noise such as “Data plot: ...” and “Crab image: context only.” The user rejected these immediately even though they technically satisfied a caption checklist.
problem: Caption existence is not the goal. Scientific figures need enough explanation to identify the statistic/comparison/reference line/panel when the visual is not self-explanatory. Obvious contextual images do not need meta captions that merely say what the image is. Captions should be concise, audience-facing, normally left-aligned, and should not duplicate the frame title or narrate slide construction.
candidate_action: Replace boolean caption-presence QA with a semantic caption-role check: REQUIRED / OPTIONAL / REMOVE. Require captions for ambiguous scientific plots; permit no caption when axes/legend + nearby prose already fully explain an obvious object; always retain source attribution separately when needed.
promotion_gate: replay where a technically present but useless meta-caption is rejected and a meaningful statistical caption passes.

### Teaching/course-standard route should freeze a reusable standard Beamer separate from CUHK research and commercial PPT
status: NEW
tracking: #62
source: STAT5060 Tutorial 1 V7 course-standard hardening
evidence: repeated tutorial work showed that the research CUHK Beamer, a generic teaching Beamer and commercial/business PPT have different structural needs. The user now requires a cleaned reusable standard Beamer to be extracted from the human-accepted Tutorial design.
problem: Presentations currently discusses two built-in templates but real product routing needs a clearer modality boundary. CUHK research decks can keep the research template and research-specific rhythm; tutorial/course teaching needs a restrained standard Beamer with readable section navigation, stable footer, title/closing primitives, figure-caption discipline and audience-safe typography; commercial PPT should remain a separate workflow rather than being forced into either academic route.
candidate_action: After final STAT5060 human acceptance, import the exact standard-Beamer theme/usage note as the canonical course-standard reference implementation. Do not accept the earlier failed theme or a renamed copy. Preserve aspect-ratio flexibility and template identity across 4:3/16:9 where supported.
promotion_gate: accepted STAT5060 standard Beamer + one additional tutorial/course deck + one regression check that CUHK research routing remains unchanged.

### Teaching closing frames may combine pedagogical recap with durable contact information
status: NEW
tracking: #63
source: STAT5060 Tutorial 1 V7 closing-frame redesign
evidence: generic Questions/Thanks/reflective-question endings repeatedly felt unfinished. The teaching use case benefits from leaving a concise summary plus TA/instructor contact information visible during Q&A.
problem: A teaching closing frame often has two legitimate jobs: consolidate the session and provide a stable contact path. A bare “Thanks” wastes the final visible screen; a generic reflective question can feel generated; a pure contact card loses pedagogical closure.
candidate_action: Add a course-standard closing primitive supporting 2–4 recap bullets plus a compact contact block (name/email/optional phone/office when explicitly supplied). Contact fields are user/course data, not inferred. Closing frames normally suppress ordinary navigation/header clutter.
promotion_gate: accepted real teaching deck where recap+contact is judged better than generic Questions/Thanks.

### Student-facing slide language needs a rendered full-deck anti-meta/anti-AI gate
status: NEW
tracking: #64
source: STAT5060 Tutorial 1 V4–V7 language failures
evidence: repeated candidates reintroduced phrases such as “Course anchor”, validation/parity wording, internal release language, assessment-design explanation, generic “under a ... lens” titles and meta narration even after source-level writing passes.
problem: Clear Writing/source prose checks alone are insufficient if the final slide language is not independently re-read in context. The presentation reviewer needs a full-deck rendered-language gate focused on audience function: every visible sentence should teach, label, interpret, source, or instruct the audience. Sentences whose main function is to explain internal workflow, validation status, assessment design, slide construction or generic AI-style framing should fail.
candidate_action: Couple Presentations with Clear Writing at the final rendered-artifact stage, but keep presentation-specific anti-meta checks in the reviewer. Ordinary academic titles should be preferred over slogan-like generated headings.
promotion_gate: replay across teaching and research decks where the gate catches functionally similar AI/meta prose without relying only on a phrase blacklist.



### Reviewer runtime contract must include agent type, model, reasoning and image capability
status: NEW
tracking: #65
source: STAT5060 Tutorial 1 V7 blind-calibration failure, 2026-09-29
evidence: the executor spawned multiple blind-calibration reviewers as built-in `explorer` agents. They could identify text-visible defects such as NB2 first-use and closing/contact issues but repeatedly missed pixel-dependent failures such as header contrast, footer optical alignment, P13 geometry, P20 crowding and P22 wasted space.
problem: A reviewer prompt is not enough. Presentation acceptance quality depends on the runtime contract that executes it. If a generic code-exploration agent, low-reasoning model or image-incapable context runs the same prompt, the output can still be a false PASS. The final reviewer extracted from STAT5060 must freeze reviewer agent class/capabilities, model/reasoning floor, read-only execution posture and direct image-consumption capability in addition to textual rubric.
candidate_action: Once the STAT5060 reviewer is human-accepted, capture the exact reviewer runtime contract alongside the prompt. Presentations should refuse visual PASS when reviewer runtime identity/capabilities do not satisfy the frozen contract.
promotion_gate: one replay showing the same rubric fails under an unsuitable explorer/text-only runtime and succeeds under the intended reviewer runtime.

### Presentation visual review must prove actual pixel consumption, not merely receive an archive
status: NEW
tracking: #66
source: STAT5060 Tutorial 1 V7 calibration bundles
evidence: blind reviewers were given a tar.gz containing PDF/renders/contact sheet, but repeated misses on visual defects created no proof that the reviewer had actually opened and inspected the rendered pages.
problem: Supplying image files is not equivalent to consuming them. Visual acceptance needs evidence that the reviewer actually viewed final page pixels. A bundle/archive can degrade into text-only or filename-level review if the agent never invokes image viewing. Presentations should record image evidence consumption or use a review entry that directly attaches/opens whole-slide renders.
candidate_action: Add a reviewer-evidence requirement such as viewed-image manifest/tool trace/direct image attachment. If visual evidence was not actually consumed, return BLOCKED_VISUAL_REVIEW_NOT_PERFORMED rather than PASS.
promotion_gate: replay where a reviewer receiving but not viewing images is correctly blocked.

### Blind calibration must be frozen, sentinel-based and must not become prompt tuning on the holdout
status: NEW
tracking: #67
source: STAT5060 Tutorial 1 V7 calibration A–F cycle
evidence: after A/B failed blind calibration, successive C/D/E/F prompts were made progressively more exhaustive while using the same rejected V6 holdout. This improves hit rate but starts tuning the calibration prompt to the holdout, weakening its meaning as an independent reviewer-quality test.
problem: Reviewer calibration can itself overfit. A blind holdout cannot remain a meaningful capability test if the prompt is repeatedly edited after each miss. Calibration should use a frozen prompt and a small objective sentinel set rather than require reproduction of every human complaint. Failure should trigger runtime/capability repair or a new calibration fixture, not repeated wording changes against the same expected answers.
candidate_action: Freeze role-specific calibration prompts before the first run. Use a sentinel policy: require a small set of objective visual/teaching defects plus additional independently discovered findings. Record prompt hash. After a calibration failure, do not edit the prompt against the same holdout.
promotion_gate: successful fixed-prompt calibration across at least two reviewer runtimes and one fresh rejected deck.

### Artifact review must not depend on the unfinished Presentations production plugin
status: NEW
tracking: #68
source: STAT5060 Tutorial 1 V7 reviewer dispatch failure
evidence: the executor initially attempted `ai-bridge plugin-replay --plugin presentations`; the current Codex identity did not have the Presentations production plugin installed/enabled and review stalled even though the deck artifacts themselves were reviewable.
problem: This creates a circular dependency: a deck is being used to improve Presentations, but its independent reviewer requires the unfinished Presentations plugin to run. Generic artifact review must be able to operate as a plain fresh reviewer context/process over explicit PDF/render evidence. Production plugin replay is for validating installed plugins, not a mandatory transport for presentation artifact acceptance.
candidate_action: Separate `presentation artifact reviewer` from `Presentations plugin production replay`. The former must have a plugin-independent review entry; the latter remains a later product-validation path.
promotion_gate: independent artifact review of a deck succeeds on a machine without Presentations installed.

### Review transport should distinguish plugin replay from fresh reviewer execution
status: NEW
tracking: #69
source: STAT5060 Tutorial 1 V7 + Bridge Kit 0.9.x usage confusion
evidence: the executor treated the need for a fresh independent child as a reason to reach for `plugin-replay`, despite the task being artifact review rather than installed-plugin replay.
problem: “fresh child” and “plugin replay” are different capabilities. Presentation review needs a fresh isolated read-only reviewer context with explicit artifacts; it should not inherit plugin-replay requirements such as installed production plugin identity. Conflating them causes avoidable blocking and fallback pressure.
candidate_action: Document a canonical reviewer dispatch matrix: artifact review -> native fresh reviewer/subagent or isolated fresh Codex process; plugin regression -> plugin replay; human/ChatGPT review -> explicit external handoff. Fail closed if no qualifying reviewer transport exists.
promotion_gate: routing tests for all three cases without cross-route fallback.

### Review standards must not Goodhart into renderer hacks
status: NEW
tracking: #70
source: STAT5060 Tutorial 1 V7 footer alignment repair
evidence: a synthetic “<=2 px centre difference” footer metric caused the executor to replace ordinary Beamer navigation with custom TikZ-drawn chrome purely to satisfy the measured threshold. The result optimized the metric rather than the intended mature Beamer behaviour.
problem: Quantitative diagnostics are useful evidence, but turning them into implementation targets can create worse designs. Reviewer rules should state the perceptual invariant (“controls and page number are optically aligned”) while numeric measurements remain diagnostic, not a renderer contract. Similar risk applies to whitespace percentages, font-size thresholds and pixel gaps.
candidate_action: Distinguish hard semantic constraints from diagnostic heuristics. Reviewers may cite measurements to support REVISE, but generators must not be instructed to optimize arbitrary pixel numbers unless the template itself truly requires them.
promotion_gate: replay where the generic reviewer rejects a visually misaligned footer without requiring custom chrome or a universal pixel constant.

### Native template chrome must remain native; diagrams and scientific graphics use separate rendering ownership
status: NEW
tracking: #71
source: STAT5060 Tutorial 1 V7 footer regression
evidence: while repairing footer alignment, the executor temporarily introduced custom TikZ navigation/footer controls. The user explicitly rejected this because ordinary Beamer already owns navigation chrome.
problem: Rendering ownership should be explicit. Template chrome (headline/miniframes/footline/navigation/page numbers) belongs to the template/runtime, not diagram drawing. TikZ may be appropriate for conceptual scientific diagrams; R/Python for data-driven plots; native Beamer for Beamer UI. Crossing these ownership boundaries makes themes brittle and visually inconsistent.
candidate_action: Add renderer-ownership QA: native Beamer template chrome, R/Python data figures, TikZ only for conceptual diagrams unless a frozen template explicitly says otherwise.
promotion_gate: accepted standard-Beamer reference and regression test preventing custom-drawn navigation chrome.

### Final candidate review should bind to a frozen artifact identity before independent acceptance
status: NEW
tracking: #72
source: STAT5060 Tutorial 1 V7 finalization
evidence: repeated emergency fixes changed PDF, render evidence and template after earlier checks. Reviewer status became ambiguous unless every review named the exact candidate hash.
problem: Presentation review is meaningless if evidence and verdict can refer to different renders. Before independent acceptance, freeze PDF/slide source/render-manifest identities. Reviewer artifacts must state the exact PDF hash and render-set identity they inspected; any subsequent mutation invalidates the verdict and requires fresh review.
candidate_action: Make artifact identity binding mandatory at candidate freeze. Reuse the same principle for PPTX and other export formats.
promotion_gate: a mutation-after-review test correctly invalidates previous PASS.



### Final presentation artifacts must be surfaced as actual openable/downloadable deliverables
status: NEW
tracking: #73
source: STAT5060 Tutorial 1 Rich Edition final handoff, 2026-10-01
evidence: `YuukiAS/STAT5060-TA` commit `511fddfda9721f00c1d8bdb3774d9a17f37c3e95` produced `STAT5060_TUTORIAL_01_RICH_EDITION_BEAMER.pdf` plus complete build/render evidence, but the executor completion message primarily exposed repository paths and status fields. The user had to ask separately whether the PDF existed and requested a result they could click to open/save locally.
problem: A deck can pass build/render/QA and still fail the user-facing handoff if the finished PDF/PPTX is not surfaced as an actual artifact. Repository paths, commits and hashes are provenance; they are not a substitute for handing the user the file. A presentation run should not claim final human handoff merely because an artifact exists somewhere in the repo.
candidate_action:
- Add a final delivery gate: when a finished PDF/PPTX/source bundle exists and the host supports attachment/file-card/download/open surfaces, the final response must expose the real artifact through that surface.
- Report canonical repo path, commit and SHA separately for provenance, but never make them the only delivery mechanism when a direct artifact surface is available.
- Prefer at least the primary audience artifact (PDF or PPTX) and, when useful, the editable source as separate user-accessible artifacts.
- If the runtime genuinely cannot surface a file, state that limitation explicitly and use the nearest supported materialization/handoff mechanism. Path-only output must not be treated as `READY_FOR_HUMAN_ACCEPTANCE=YES`.
promotion_gate: one real Beamer/PDF delivery and one real editable PPTX delivery where the user can directly open/save the produced artifact from the completion message.

### Beamer navigation QA must reject duplicate section declarations and duplicate visible section labels
status: NEW
tracking: #74
source: STAT5060 Tutorial 1 Rich Edition human acceptance, 2026-10-01
evidence: `YuukiAS/STAT5060-TA` commit `511fddfda9721f00c1d8bdb3774d9a17f37c3e95`; the generated Rich Edition TeX contained pairs such as `\\section{GLMs}` followed by `\\section[GLMs]{GLMs}`, likewise for GLMMs/Simulation/Bayesian/Assessment/Summary. The compiled PDF therefore exposed duplicated top-navigation labels such as `GLMs GLMs`, `GLMMs GLMMs`, `Simulation Sim`, while the automated `navigation_check.json` still reported PASS because frame counts, page denominator and destination coverage were correct.
problem: Current navigation checks can verify page count and miniframe coverage yet miss a visibly broken section model. In Beamer, section identity is structural template chrome: duplicate section declarations must not survive merely because all frame destinations exist. This is also direct evidence for TODO #49: a course-standard template needs one canonical section declaration per logical section and a reviewer that inspects the rendered section labels, not only frame counts.
candidate_action:
- For generated Beamer, maintain a canonical logical-section manifest and assert exactly one `\\section...` declaration per logical section unless an explicit frozen template requires otherwise.
- Compare the declared section sequence with rendered headline/miniframe labels; reject duplicated adjacent labels and long-title/short-title pairs that accidentally become two sections.
- Navigation QA should check both structure and rendered text: logical section count, declaration count, visible label sequence, frame membership, destination coverage and page denominator.
- Keep native Beamer ownership. Do not repair duplicate labels by drawing custom navigation chrome or hiding them with overlays.
- Add a regression fixture from this Rich Edition failure so a 37-page deck with correct frame counts but duplicated section labels deterministically fails.
promotion_gate: course-standard template implementation plus one unrelated Beamer deck both pass the structural/rendered-label gate, while the Rich Edition pre-repair artifact fails.

### Beamer font identity must be fixed and renderer-owned, not host-selected
status: NEW
tracking: #98
source: STAT5060 Tutorial 1 Rich v2 font-blocker recovery, 2026-10-04
evidence: Rich v2 implementation stopped because a temporary handoff required Times New Roman; host `fc-match` resolved Liberation Serif instead. Review of `render-chinese-math-pdf` showed the established reliable pattern is fixed bundle-local font files, not host font substitution. Canonical Presentations font policy was then written to `shared/font-policy.md`.
problem: Presentation templates must not choose a body/math font per machine, and an unavailable proprietary font must not force ordinary deck work into repeated blocked states. CUHK and course-standard also cannot drift onto different scientific font stacks merely because their legacy sources differ.
candidate_action:
- Treat the font set as a shared Beamer-core contract, not a skin choice.
- Reuse the render-owner resource resolver and load exact bundled files: TeX Gyre Termes for Latin text, TeX Gyre Termes Math for math, New Computer Modern Math only for cal/bfcal, Noto Serif/Sans SC for CJK, and Latin Modern Mono for code.
- Remove legacy Times New Roman from the migrated CUHK shared-core implementation; do not replace it with Liberation/DejaVu/fontconfig fallbacks.
- Add preflight + `pdffonts` allowlist QA and record font-file hashes in render receipts.
- Keep missing canonical bundle files as a typed installation/resource error, while explicitly preventing “Times New Roman missing” from being a deck-level blocker.
promotion_gate: both `cuhk-research` and `course-standard` render the same typography fixture from two supported resource-root configurations; exact allowed font identities are embedded, injected host-font fallback is rejected, and neither adapter contains its own font discovery logic.

### Final release review must be requirement-led, not self-attested or render-only
status: NEW
tracking: #35
source: STAT5060 Tutorial 1 Rich v2 independent release review, 2026-10-04
evidence: candidate `f4c3572e97a94886c61a17ccb1f827bec36a117f` produced 37 renders and a passing executor QA summary, but independent review found missing footer navigation, multiple unimplemented frozen page repairs, invalid whitespace metrics, and generic `39/39 CLOSED_VISIBLE` evidence. A second independent audit additionally found frozen-spec drift on P01, P03/P20, P06 and P34 that the first reviewer missed.
problem: Presentation acceptance can still falsely PASS when evidence files are self-attested, when whole-slide review is described but not demonstrated page-by-page, or when the reviewer judges only visual plausibility instead of checking every frozen requirement against both source and render.
candidate_action:
- Require a three-way release ledger: `frozen requirement -> exact source evidence -> final render evidence`. Every bounded repair item must have one row and one explicit PASS/REVISE result.
- Reject repeated boilerplate page-review rows such as “top navigation, content balance...” without a page-specific observation naming the primary object, bottom edge, and any intentional whitespace reason.
- Annotation closure must map annotation ID -> page -> original issue -> exact repair -> source anchor -> after-render/crop. Generic identical `CLOSED_VISIBLE` lines are invalid evidence.
- Whitespace metrics must exclude fixed chrome (headline, footer, page number, source credit) and operate on the usable body. Automated metrics are triggers only; final composition status requires whole-slide inspection.
- Add source-level assertions for deterministic frozen facts before visual review: protected frame options, required macros, exact footer primitives, code font role, column widths, caption role, table width, exact frozen strings, and forbidden legacy strings/layout primitives.
- Final independent reviewer must separately answer “looks acceptable?” and “matches the frozen repair contract?”. Either failure blocks release.
- A claimed `ALL_PAGES_VIEWED=YES` must be backed by unique page-level notes; executor self-review is not independent acceptance.
promotion_gate: replay the Rich v2 failed candidate so the strengthened gate rejects it for both source-contract drift and visual composition; then pass the bounded repair candidate plus one unrelated deck without requiring project-specific page logic.

### Beamer header miniframe markers need native-size projection QA
status: NEW
tracking: #98
source: STAT5060 Tutorial 1 Rich v2 human screenshot review, 2026-10-04
evidence: Rich v2 course-standard theme overrode Beamer miniframe markers with custom `\scalebox{0.55}` bullet/open-circle glyphs. At normal slide scale, the section labels were readable but the per-frame markers collapsed into tiny pinpricks. Both executor QA and independent release review missed the defect because they checked names/link destinations, not marker visibility.
problem: A navigation header can be structurally correct and clickable while still failing as presentation chrome because the miniframe markers are too small to read as progress/state indicators at whole-slide scale.
candidate_action:
- Shared Beamer core should use the same native miniframe template/size for `cuhk-research` and `course-standard`; do not downscale native markers with arbitrary `scalebox` values.
- Treat section text and miniframe row as one visual unit. Marker outer size, inter-marker spacing, and vertical separation from the section label must remain legible at 1920x1080 whole-slide view.
- Add a header crop/fixture with short and long sections (including 10+ frames) and reject markers that visually collapse to punctuation.
- QA must check marker visibility/state contrast in addition to full section labels, destination coverage, and clickability.
- Prefer native Beamer ownership; do not repair by drawing a custom navigation overlay.
promotion_gate: the failed STAT5060 header deterministically fails the new projection-size gate; repaired course-standard and CUHK fixtures use the same marker template/metrics and pass at normal whole-slide scale.

### Code typography is a deliberate compact role, not body-text typography
status: NEW
tracking: #98
source: STAT5060 Tutorial 1 Rich v2 human screenshot review, 2026-10-04
evidence: a release audit incorrectly treated `\scriptsize` teaching code as a defect because body text uses a larger role. The actual 1920x1080 slide showed the code legible, and the user explicitly prefers code to remain compact because code blocks routinely contain more characters and lines than prose.
problem: Same-role typography parity must not be misread as “all slide content uses body size.” Code is a distinct semantic role with different density constraints.
candidate_action:
- Freeze formal Beamer code/listing typography to monospaced `\scriptsize` by default for both CUHK and course-standard.
- Do not flag code merely for being smaller than body text.
- Code QA should instead check whole-slide legibility, line wrapping, clipping, balanced paired boxes, syntax fidelity, and whether a denser slide should reduce code content rather than silently shrink below the code token.
- `\tiny` remains forbidden for normal code; body/table/caption roles keep their own independent size tokens.
promotion_gate: paired R/Python and a dense research-code fixture both remain readable at 1920x1080 with fixed scriptsize code, while injected tiny/clipped code fails.

### Whitespace QA must use archetype-aware hard gates and cannot be waived by free-text reasons
status: NEW
tracking: #35
source: STAT5060 Tutorial 1 Rich v2 final rereview, 2026-10-05
evidence: reviewed candidate `bda8d2c68d86041da746026b32bf6e0217977f92`, PDF SHA256 `b267917df179aa5a50ff341a7a71343a13bbb15525f4754bb298f02678890c78`. Executor evidence used `usable_body_bbox=[80,135,1840,990]`, which still included the frame-title region, and then cleared >25% bottom-gap pages P14/P16/P22/P30/P31/P36 using free-text `intentional_whitespace_reason`. Independent rereview using a post-title body region found seven ordinary content pages over the frozen 25% hard threshold: P14/P16/P22/P28/P30/P31/P36.
problem: A whitespace metric can look quantitative while still being semantically wrong if its body region includes fixed chrome or if ordinary content pages can self-exempt with arbitrary prose. Requirement ledgers can also falsely PASS if they summarize composition requirements rather than enumerate every frozen page-level repair.
candidate_action:
- Derive the usable body from template chrome boundaries: below the rendered frame-title region and above the footer rule/source/navigation area. Do not use a single hard-coded top coordinate that includes the frame title.
- Separate page archetype from free-text rationale. Hard-threshold exemptions must come from a frozen archetype allowlist (e.g. title, section-divider, closing); an executor-written `intentional_whitespace_reason` must never waive an ordinary-content hard gate.
- Ordinary content pages over the hard gap threshold fail automatically. Pages over the soft threshold require primary-object scale + visual-balance review; the executor cannot clear the trigger by narrative alone.
- Store both metric geometry and the detected chrome geometry in evidence so independent review can reproduce the denominator.
- Requirement ledger completeness must be machine-checkable against the frozen requirement IDs: no grouped summary row may silently omit page-level composition repairs.
- Cross-gate consistency: if whitespace metrics, requirement ledger, annotation closure, and page review disagree, overall release QA must be REVISE.
promotion_gate: replay the STAT5060 candidate so P14/P16/P22/P28/P30/P31/P36 fail automatically and title/closing pages remain valid exceptions; then pass a repaired candidate plus an unrelated deck using the same archetype-aware rule.

### Teaching code/reference slides need runnable-context and PDF-copyability QA
status: NEW
tracking: #35
source: STAT5060 Tutorial 1 student-deck V05 human review, 2026-10-05
evidence: V04 showed package names and partial snippets but omitted imports, data-object creation, complete model calls, posterior extraction/predictive calls, and honest backend disclosure. The final PDF text layer also converted straight code quotes into typographic quotes on several code pages, so visually plausible code could not be copied and executed.
problem: A teaching presentation can look technically sophisticated while failing its practical teaching job if code is shown as fragments rather than a runnable workflow. Source-level syntax correctness is not enough; the final rendered PDF must preserve copyable code text.
candidate_action:
- Treat code/reference slides as a distinct teaching artifact role: prerequisites -> complete call -> relevant output/extraction -> interpretation.
- Require imports/data objects before use; do not show an object that has not been created.
- Require the package call actually used for the claimed statistical task, including package-specific parameterisation differences and any shared backend.
- Require final-PDF code extraction QA: ASCII quotes/operators/underscores preserved, zero curly quotes in code, syntax parse/smoke checks, and visible result/meaning on the page.
- A software-name matrix or API-name list does not satisfy software teaching when the page job is “how to fit/check this model”.
promotion_gate: replay STAT5060 V04 so the fragmentary brms/PyMC/code pages and curly-quote PDF fail; pass V05-style complete syntax pages plus one unrelated teaching deck.

### Column layout is for peer comparison; sequential reasoning must use a vertical reading path
status: NEW
tracking: #35
source: STAT5060 Tutorial 1 V04 annotations plus CAT-TRACE v8/v9 layout evidence, 2026-10-05
evidence: V04 repeatedly forced sequential explanations into side-by-side regions: relative-logit weights vs normalization, condition/marginal diagrams, blocked-Gibbs -> MH-within-Gibbs, and HMC/NUTS stages. CAT-TRACE had already shown that learn -> prior -> update became clearer after changing from columns to a vertical sequence, while genuinely peer objects remained successful in columns.
problem: “There is horizontal space” is not a valid reason to use columns. Columns imply simultaneous peer status and invite wide meaningless gutters when the content is actually causal, temporal, inferential or prerequisite-ordered.
candidate_action:
- Before composing a multi-column slide, record the semantic relation: PEER_COMPARE or SEQUENTIAL_DEPENDENCY.
- Allow columns only for peer objects with comparable roles and matching anchors (e.g. R vs Python, ordinary model vs GLMM).
- Use vertical/stacked flow when object B depends on A, one denominator/formula governs the next step, or the explanation has a natural prerequisite order.
- QA must inspect actual nearest-object gutter, top/formula/code alignment and lower-edge balance; declared column widths alone are insufficient.
- If one column becomes mostly a label while the other carries the explanation, collapse to a single vertical reading path.
promotion_gate: same fixture set must reject sequential content placed in columns and retain peer-comparison columns without false positives.

### Semantic proximity must be a release gate, not sacrificed to whitespace metrics
status: NEW
tracking: #35
source: STAT5060 Tutorial 1 V04/V05 human review, 2026-10-05
evidence: prior repairs reduced bottom whitespace by pushing conclusions toward the lower page, which separated interpretation from the table/figure/formula it explained. Pages could satisfy a bottom-gap threshold while becoming harder to read. STAT5060 Tutorial 1 Student Deck V06 reproduced the failure on P18 and P35: both satisfied the lower-body whitespace gate, while whole-slide review still showed a large internal gap splitting one semantic group. The generated `semantic_proximity.json` only measured whole-body centre distance from the slide-body centre and therefore returned PASS without measuring evidence-to-interpretation or block-to-follow-up distance.
problem: Whitespace occupancy and semantic grouping are different constraints. A page can be “full” and still be badly composed if evidence and its interpretation are visually far apart.
candidate_action:
- Define semantic groups before layout: evidence object + interpretation/conclusion.
- Measure or review evidence-to-interpretation proximity in addition to bottom gap.
- Ordinary figure/table interpretation should normally stay near the object; do not use vfill to separate items that belong to one semantic group.
- Permit stretch glue only between independently meaningful groups.
- Release QA must fail pages where a conclusion is moved away from its evidence merely to satisfy whitespace thresholds.
promotion_gate: replay known STAT5060 pages where bottom-gap passed but evidence/interpretation proximity failed, then pass repaired layouts and an unrelated sparse slide.

### Connector geometry needs a minimum visible shaft and boundary-to-boundary contract
status: NEW
tracking: #39
source: STAT5060 Tutorial 1 V04 arrows plus CAT-TRACE v7-v9 diagram fixes, 2026-10-05
evidence: STAT5060 V04 simulation/HMC/GLMM diagrams contained arrows that were too short, detached-looking or visually crowded. CAT-TRACE independently established the same failure mode and converged on boundary-clipped edges with about 8–10 mm visible shaft where space permits.
problem: A connector can be syntactically present and collision-free yet still fail visually if it is too short to read as a relationship, starts/ends inside a node, or is compressed until arrowheads/labels collide.
candidate_action:
- Default connector rule: node-boundary to node-boundary; no overlap with text/formula/border/other connectors.
- At 1920x1080, target at least about 36 px / 8 mm visible shaft; peer-row arrows should use comparable visible lengths.
- Relation labels require stable clearance from the shaft.
- Do not use arbitrary shorten values that create detached arrows.
- If the available width cannot support readable connectors, switch to a numbered vertical sequence instead of keeping miniature arrows.
- Add rendered connector-length/collision evidence to final QA; source styles alone do not prove acceptability.
promotion_gate: failed short-arrow fixtures must be rejected; repaired peer-flow and vertical-fallback fixtures pass across CUHK and course-standard skins.

### Footer alignment must be regression-tested after every theme/font/page-count change
status: NEW
tracking: #98
source: STAT5060 Tutorial 1 V04 human review, 2026-10-05
evidence: footer alignment regressed after earlier accepted rounds even though the footer structure, navigation groups and page count had previously passed review. The user again observed native action buttons visually misaligned relative to source credit/page number.
problem: Footer acceptance is being treated as a one-time template fact, but font, theme, total-page count and nearby layout changes can move optical alignment. Structural presence of the right controls does not guarantee a mature footer.
candidate_action:
- Treat footer as shared-core chrome consumed by CUHK/course-standard skins rather than duplicate project-local implementations.
- After any theme/font/page-count change, rerun footer crops on title, code, figure, dense-model, assessment and closing pages.
- Check source/page-number baseline, native action-group optical centre, action-to-page-number horizontal gap, exact approved action set and collisions.
- Prior footer PASS must be invalidated when a dependency affecting geometry changes.
promotion_gate: an injected vertical/button offset must fail the shared fixture; both adapters pass the same footer-core geometry with skin-only differences.

### Question vertical-rule geometry must follow the rendered text box
status: NEW
tracking: #32
source: STAT5060 Tutorial 1 V04 annotation A004, 2026-10-05
evidence: the Question macro was present and stylistically consistent, yet the accent rule extended above the first question line and read as a misplaced decoration.
problem: Macro presence and colour-role consistency do not guarantee correct rendered geometry.
candidate_action:
- Bind rule top/bottom to the actual rendered label+question text box.
- At release scale, allow at most about 1 px optical overshoot.
- Rule must not extend into title, previous object, or following object.
- Multi-line Question blocks and full-width Questions require dedicated regression fixtures.
promotion_gate: the V04-style overshooting rule fails; one-line and multi-line Question fixtures pass in both skins.

### QA evidence artifacts must be self-validating, page-index aligned, and hash-bound
status: NEW
tracking: #36
source: STAT5060 Tutorial 1 Student Deck V05 independent review, 2026-10-06
evidence: V05 had a 46-page PDF, but `page_review.md` contained only 45 rows, labeled the actual title page as “Tutorial overview”, shifted every later title by one page, and omitted P46. `requirement_ledger.md` was only a summary paragraph. Six supposed representative footer crops were the exact same 637-byte Git blob. Column/semantic/connector evidence files contained prose or page names rather than frozen metrics. The artifact manifest named an evidence directory but did not bind its Git tree. V06 then showed that a nominal evidence-integrity checker can still self-certify bad evidence: the requirement ledger hard-coded its own integrity requirement as PASS; RGB `Image.getbbox()` would accept an all-white crop as nonblank; no malformed fixture proved fail-closed behaviour; and the recorded evidence payload/tree identities disagreed with the committed evidence root. V07 attempted to repair these checks but exposed a second-order regression: the eight “negative fixtures” were small fixture-specific dictionaries evaluated by a separate `rejects()` switch instead of being passed through production validators; `V07-32-evidence-integrity` remained hard-coded `True`; the production blank-crop check still used RGB `Image.getbbox()`; the connector audit false-passed P34/P36, which have no diagram connectors, by treating dark-blue text pixels as connector evidence; and final tree/payload identities were still placeholders or internally contradictory.
problem: Presentation QA evidence can currently look complete by filename while being internally inconsistent, off-by-one, blank/duplicated, or unrelated to the reviewed artifact.
candidate_action:
- Add an evidence-integrity preflight that validates page-review row count == PDF page count and matches every row title to text extracted from the same final PDF.
- Require requirement IDs and one row per frozen requirement; prose-only ledgers are invalid.
- Bind each crop to source page/render hash; reject blank crops, wrong dimensions, and duplicate crop hashes where distinct pages are expected.
- Require numeric/schema fields for column alignment, semantic proximity, connector shaft/collision, footer baseline/optical/gap checks.
- Record PDF/source/theme hashes plus evidence-root Git tree SHA in the artifact manifest.
- Cross-evidence contradictions automatically force REVISE.
promotion_gate: replay STAT5060 V05 so the 45/46 page-review mismatch, six duplicate footer crops, prose-only ledger, and metric-free audits all fail before independent review.

### Reviewer capability limits need NOT_VERIFIED semantics, not false artifact failures
status: NEW
tracking: #36
source: STAT5060 Tutorial 1 Student Deck V05 GPT Work review and independent binary recheck, 2026-10-06
evidence: GPT Work returned `CODE_COPYABILITY = FAIL` only because its connector could not materialize the final PDF bytes. A second reviewer received the exact uploaded binary, independently ran `pdftotext -layout`, reproduced the expected PDF SHA256, found zero curly quotation marks and zero replacement characters, and confirmed ASCII quoted code across all code pages.
problem: Review tooling limitations are currently conflated with defects in the artifact. This produces false FAIL findings and makes it impossible to distinguish “bad PDF” from “reviewer could not independently verify the PDF”.
candidate_action:
- Review status vocabulary must distinguish PASS / REVISE(artifact defect) / NOT_INDEPENDENTLY_VERIFIED(capability or evidence access missing).
- A mandatory gate that is NOT_INDEPENDENTLY_VERIFIED still blocks release, but must not be reported as a demonstrated content/layout defect.
- Binary-only gates should record the exact artifact hash and extraction capability used by each reviewer.
promotion_gate: a fixture with inaccessible bytes produces NOT_INDEPENDENTLY_VERIFIED; the same artifact supplied as bytes is independently extracted and can PASS without changing the artifact.

### Template/core references must pin exact provenance instead of saying “current CUHK”
status: NEW
tracking: #98
source: STAT5060 Tutorial footer regressions during course-standard/CUHK parity work, 2026-10-06
evidence: project specifications referred to the “accepted/current CUHK footer core” while the central CUHK template continued to evolve. A later repository state can therefore point at different footer primitives than the ones used when the project contract was frozen.
problem: Cross-template parity is not reproducible if a project says “match current template” without commit/blob identity. Later maintenance can silently change the reference under an already-frozen deck.
candidate_action:
- Every template-derived frozen contract must record template repo, commit, source path and source blob/hash.
- Runtime/executor should verify the pinned identity before copying or comparing a shared primitive.
- Newer template revisions require an explicit migration decision, not silent substitution during a bounded deck repair.
promotion_gate: a deck frozen against template identity A rejects silent use of later identity B; an explicit migration updates the recorded provenance and reruns affected chrome regression tests.

### Short Question/label blocks need a no-awkward-hyphenation render gate
status: NEW
tracking: #32
source: STAT5060 Tutorial 1 Student Deck V05 P30, 2026-10-06
evidence: the short Question “Do the priors put substantial mass...” rendered `substan-` / `tial` despite ample room for a cleaner line break. Source text and semantic macro were correct, so source-level QA missed the visible language defect.
problem: Automatic TeX hyphenation inside short questions, labels and takeaways can make otherwise correct slide language look mechanical and harder to read.
candidate_action:
- Question/Answer/Takeaway/Example semantic primitives should strongly discourage automatic word hyphenation.
- Final render QA flags discretionary hyphens in short audience-facing semantic blocks and prefers clean phrase-level line breaks.
- Do not globally disable scientific hyphenation in long prose; scope the rule to short semantic blocks or explicitly authored labels.
promotion_gate: the V05 P30 fixture fails; a clean non-hyphenated reflow passes without changing the sentence.

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
tracking: #44
source: repeated TRACE visual feedback
evidence: presentation maintenance archive + CAT-TRACE real deck revisions
target layer: rendering/qa
problem: diagram 的语义规则已经有了，但实际箭头、节点、对齐、连接路径和层级几何仍然可能做坏。
candidate_action: 只有新的真实 deck 再次暴露问题时，才补 renderer-level primitive 和 QA，不为了历史 TODO 预先造一整套几何系统。
promotion_gate: 新的真实 CAT-TRACE 或 unrelated deck 用实际 render 重现问题，并能证明修改真的改善输出且不会过度限制其他 diagram。

### Deck-wide style system and terminology hierarchy
status: CANDIDATE_GENERIC
tracking: #45
source: repeated real research deck revisions
evidence: presentation maintenance archive
target layer: reasoning/rendering/qa
problem: 一整套 deck 里，标题大小写、术语首次解释、dataset/simulation 编号、小标题、metric label、caption 和 references 容易逐页漂移。
candidate_action: 只有真实返修再次证明这是当前问题时，才增加最小 deck-wide consistency contract，不把所有页面强行做成同一种布局。
promotion_gate: independent rendered deck 证明 consistency check 能抓到真实问题且不会压平不同科研页面。

### Math and theory slide hierarchy
status: CANDIDATE_GENERIC
tracking: #46
source: repeated statistics and theory deck feedback
evidence: presentation maintenance archive + CAT-TRACE review docs
target layer: reasoning/rendering/qa
problem: definition、design setting、estimand、theorem、derivation 容易都被做成同一种“居中大公式”，科学角色没有层次。
candidate_action: 在新的 math-heavy real deck 再次出现时，才进一步加强公式层级、首次语义解释和 theory-page QA。
promotion_gate: theorem/statistical-method real deck replay + unrelated math-heavy deck regression。

### Simulation, metric and structured-fact presentation
status: CANDIDATE_GENERIC
tracking: #47
source: repeated real statistics deck feedback; STAT5060 Tutorial 1 annotated teaching deck review, 2026-09-29
evidence: presentation maintenance archive + STAT5060 pages 16–18. The tutorial exposed exactly the unresolved reader questions this candidate targets: why run the simulation at all, what the true slope 0.5 represents, why NB2 uses kappa=1.5, and how Bias/RMSE relate to the displayed figure rather than appearing as detached formulas.
target layer: reasoning/rendering/qa
problem: DGP、estimand、baseline、metric direction、dataset facts、seed/reproducibility 信息容易混成段落或弱表格，读起来很累。
candidate_action: 新的 simulation-heavy / real-data deck 再次出现时，再提炼更稳定的 table/list patterns 和 QA。
promotion_gate: 至少一个 simulation-heavy 和一个 real-data deck 的真实 render 都证明改善了可读性。

### Natural scientific slide language
status: CANDIDATE_GENERIC
tracking: #48
source: repeated presentation and writing-style feedback; STAT5060 Tutorial 1 annotated teaching deck review, 2026-09-29
evidence: presentation maintenance archive + `docs/plugin-todos/writing-style.md` + nine pink annotations in the STAT5060 27-page tutorial candidate. The teaching deck still contained formulaic/AI-like prose even after a dedicated content rewrite, including generic caveat sentences, mechanical “same displayed probabilities”/“these are specified parameters” phrasing, and engineering-flavoured audience copy.
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
