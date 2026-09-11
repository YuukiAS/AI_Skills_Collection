# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### Promote `writing-style` into the generic content-preserving language layer
status: READY_FOR_PROMOTION_AFTER_050
source: 050 Deep Research rewrite failures + Distributed Imaging report v2 + CAT-TRACE presentation reviews + cross-plugin boundary audit, 2026-09-05
evidence: `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`; task 050 smoke/replay evidence; `docs/plugin-todos/research-writing.md`; `docs/plugin-todos/presentations.md`
target layer: routing/language/fidelity
problem: the old `Writing Style` display name undersold the product and was easy to confuse with `research-writing`. The current display-name decision is now settled as `Clear Writing`, while the canonical plugin slug remains `writing-style` and no slug migration is planned in this cleanup. The remaining capability TODO is broader and still unresolved: make this plugin the reusable content-preserving reader-facing language layer that can be called by research reports, presentations, statistical analysis, scientific visualization, medical imaging, bioinformatics and other domain plugins for captions, conclusions, table/figure wording, slide copy, technical explanations and long source-faithful rewrites. It must improve clarity without taking ownership of domain semantics.
candidate action:
- Treat the plugin as the canonical source for generic reader-facing language behavior: Chinese-first wording, exact-name vs ordinary-reasoning English decisions, sentence/paragraph connective logic, first-use explanation, formula/caption/conclusion wording, local readability review and source-fidelity-preserving repair.
- Support multiple task sizes from the same canonical source: microcopy/caption/label/conclusion; paragraph/subsection; long existing-document rewrite; slide copy from a presentation-owned page brief; result explanation from a domain-owned claim/evidence brief.
- Keep domain semantics outside this plugin. `statistical-modeling` owns models, assumptions, inferential targets and conclusions; `scientific-visualization` owns visual encoding; `research-writing` owns document plan/evidence selection/tables/citations; `presentations` owns slide sequence/page jobs/rendered QA. The language layer may clarify their already-frozen content but must not change it.
- Do not maintain a separate “说人话” rule set inside every domain plugin. Reuse the canonical `skills/writing/core/...` source through the production-compatible packaging/companion route rather than forking behavior.
- Keep the fidelity contract strong: facts, numbers, formulas, citations, uncertainty, attribution, comparators, evidence authority and conclusion strength cannot drift for readability.
- For long existing-text structural rewrite, allow reader-facing regrouping/order changes while preserving every source proposition/evidence boundary; for short captions/microcopy do not force the heavy rewrite runtime.
- Current naming decision: displayName is `Clear Writing`; slug remains `writing-style`; do not perform slug migration, directory migration, compatibility aliasing, profile migration or production identity changes as part of this TODO.
- Any future slug migration would need a separate bounded migration with source config, generated plugin, profiles/docs/tests, real installed replay and compatibility retirement evidence. This item should not assume such a migration.
promotion gate: do not treat the display-name cleanup as resolving this capability item. Promote the remaining language-layer work only after 050 identity/acceptance is closed and replay verifies at least one long rewrite, one advisor report, one presentation handoff, one statistical result/caption, and one scientific-visualization caption/annotation without domain-semantic drift.

### English scientific slide microcopy and full-deck prose remain cognitively heavy after a nominal final pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4–v8 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb`, `ef08bc25673fb33b639e523504676c0f333d93f4` and `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. Earlier rounds exposed `Failure prevented`, mechanical `Example.` language, `What it measures`, `Focal method`, `Backbone` and `Rare fit`. The 33-page v8 deck still contains first-use domain terms that are expanded but not placed in enough context for a statistics audience (`COI`, `Metabarcoding`, `VicFlora`, `MGP`), source-note-like wording such as `That threshold is an implementation choice, not a CAT-TRACE theoretical constant.`, and dense table/slide language that is grammatically valid but unnecessarily hard to parse. The v8 English-final-pass record explicitly says that it only reviewed visible wording touched in v8, so untouched but still difficult language could survive.
problem: `scientific-prose` / presentation handoff needs to distinguish grammatical correctness from reader effort. A research slide should let a first-time expert reader understand what an unfamiliar term is, why it appears here, and what the sentence is asking them to retain. Expanding an acronym alone is insufficient when the term remains contextless. Final slide prose review also cannot be limited only to source lines modified in the current round: layout changes alter wrapping and old wording may still be cognitively heavy. The desired behavior is a full-deck audience-facing pass after scientific freeze: direct sentences, explicit local context for unfamiliar terms, natural action labels, short explanatory bridges where needed, and removal of internal/defensive/meta wording. This is not detector evasion and must not weaken scientific precision.
project-specific context: CAT-TRACE, TRACE, CORAL, VicFlora, COI, OTU, GBIF, MGP, catalogue/open-tail and the specific slide sentences belong to this project. Do not create a CAT-TRACE-specific banned-word list, and do not let writing-style alter equations, scientific claims, dataset values, theorem status, citations or slide layout.

### Versioned Chinese technical documents can regress into English-keyword scaffolding during content-preserving revision
status: NEW
source: TRACE / CAT-TRACE canonical architecture and code implementation plan, 2026-09-09
evidence: compare `YuukiAS/TRACE/docs/model/catalog_aware/CAT_TRACE_CANONICAL_NOTATION_AND_ARCHITECTURE_20260908.md` with `...20260909.md`, and `CAT_TRACE_CODE_IMPLEMENTATION_MASTER_PLAN_20260908.md` with `...20260909.md`; user review of the rendered 20260909 PDFs found the newer technical content substantially stronger but the reader-facing Chinese markedly worse. Examples include prose such as `TRACE continuity + 按组标记的开放尾部 + residual structure`, `极端 rare-tail / scale stress test`, `production inference`, `composite 后验 interval`, `independent-residual`, `working set`, `source script`, `taxonomy-proxy variant`, `structured dependence`, `large-p engine`, and many sentences built from English noun chains joined by `/` or `+`. The 20260908 versions were easier to read despite containing older scientific decisions.
problem: content-preserving revision of an existing Chinese technical document needs a version-aware prose contract: the newest version is authoritative for scientific content, notation, numbers and decisions, while an earlier accepted version may be the style/readability baseline. A revision pass must compare the full document, not only newly changed lines, and must prevent ordinary reasoning words from drifting back into English merely because the executor is editing technical content. Exact code identifiers, library names, method names and necessary acronyms should remain unchanged, but ordinary connective logic, section prose, role descriptions, implementation explanations and phase descriptions should be natural Chinese. This is a readability/fidelity problem, not a request to ban English globally or to alter domain semantics.
project-specific context: CAT-TRACE notation, zero-slot logic, `C^{tax}`/`C^{phy}`, rd001–rd003 roles, R/C++ API names and implementation phases belong to TRACE. Do not promote those details into generic wording rules. The general reusable lesson is to support `current content authority + prior accepted prose baseline + full-document readability diff`, while preserving formulas, code fields, filenames, method/library names, citations and scientific claim strength.

## Open candidates

### Audit `academic-humanizer` only for genuinely missing academic-writing capabilities
status: CANDIDATE_GENERIC
source: external resource discovery, 2026-09-02
evidence: `AIScientists-Dev/academic-humanizer` at commit `94b88b23703bed7df507acae7d6d5876209a0cdf` (`SKILL.md` v0.3.3), MIT. The inspected public skill focuses on English academic editing: AI-assisted paper/thesis/rebuttal/proposal cleanup, claim-evidence calibration, author-voice matching, and paper-vs-NSF/NIH proposal register. It has useful before/after academic examples, but much of its claim-strength and anti-template guidance overlaps the current `scientific-prose`; it also contains team-specific stylistic preferences such as broad AI-tell lists and a blanket em-dash removal rule.
target layer: writing
problem: this source may contain a few capabilities that are genuinely missing from the current `writing-style` / `research-writing` stack, especially author-reference voice matching and paper-vs-grant register separation. It should not be added to the active 047 scientific-rewrite architecture merely because it is popular, and its AI-tell catalog must not become another phrase wall. The current 047 frozen Plan intentionally uses only `shuorenhua` and `human-writing-skills` as selectively ported architecture sources.
candidate_action: keep `academic-humanizer` as `REFERENCE_ONLY` during 047. After 047 closes, run a bounded source-vs-current-capability audit against `scientific-prose`, `writing-fidelity`, and relevant `research-writing` skills. Selectively port only a concrete capability that is absent, non-duplicative, license-compatible, and supported by a real task. Do not wholesale vendor the repo, create a new top-level humanizer plugin, copy broad banned-word/AI-tell lists, import author-specific house-style rules as universal rules, or duplicate claim-evidence behavior already implemented.
promotion_gate: promote only if the later audit identifies a specific missing production capability and a real replay shows that current skills fail without it. Otherwise record `REVIEWED_NOT_ADOPTED` / `REFERENCE_ONLY` and leave production behavior unchanged.

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate_action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion_gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

#### 2026-09-11：导师文稿需要摆脱内部策划口吻，而不只是减少英文
feedback_status: NEW
source: Distributed_Imaging_Inference / 将研究记录改写为上次会议纪要和下次会议报告。
evidence: DII内部记录 `docs/research/DII_FEW_SHOT_ADAPTATION_LITERATURE_POSITIONING_2026-09-11.md`（`59e45ed0d2abbccf4e5090ad960e24c0e1388db4`）；两份新草稿位于DII `deliverables/group_meeting_2026-09-05/meeting_minutes_2026-09-05.md` 与 `deliverables/group_meeting_2026-09-12/group_meeting_report_v1.md`（`6d295317cdcbc0d02958d5f0bf6ca9b90c77defd`）。
problem: 用户明确指出，“如果DGST后gap仍存在”“最终论文需要怎样的benchmark结构”“明日组会的完整叙事”不是面向老师的表达。即使把gap和benchmark逐词译成中文，句子仍在指导写作者如何准备材料，而不是直接向读者解释研究对象、证据和问题。
observed handling: 在研究文体、章节职责和证据范围先确定后，改写为“相关文献把问题推进到了哪里”“DGST：本次直接比较的方法”“下一阶段拟研究的问题”等直接讨论内容的句子。用完整中文解释参考病例、模型更新和测量修正之间的关系；保留正式方法名、指标及单位，不用内部状态代替结论。正文先说明实际含义，再在表注或附录交代可比性限制；删除的是面向执行者的措辞，不是尚未验证的事实边界。
project-specific context: 本例与Research Authoring的文体、时间线和来源工作分开记录，不重复接管证据选择、数据解释或会议归因。原文是有意保留的内部记录，不能因目标读者后来变化而追认其为原任务失败。当前没有正式Clear Writing插件调用或生产回放证据，新草稿也尚未获得用户认可；此处仅补充现有候选的真实需求和人工改写案例，等待后续回放，不修改正式插件规则。

### Deep Research 中文报告作为 `writing-style` 的真实压力测试输入
status: MANUAL_BASELINE_CAPTURED
source: ChatGPT Deep Research 中文科研报告，2026-08-31；2026-09-03 完成一次人工“说人话”重写作为可读性 baseline。该 PDF 由 Deep Research 直接生成，**没有经过 `writing-style` plugin**。
evidence: 用户提供的 22 页 PDF《共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策》；正文反复出现 `anchor`、`provenance`、`estimand`、`scientific gap`、`method gap`、`residual gap`、`resource contract`、`strict one-shot contract`、`testbed`、`axis`、`comparator`、`correction/stability run` 等表达，并存在“法律意义上证明”“forensic-level exact provenance proof”一类不必要的法律/取证腔。2026-09-03 的人工重写在不重新检索文献、不改变实验数值、公式、算法名、数据集名、结论强度和未验证事项的前提下，把全文重新组织为读者先能回答“现在到底知道什么、为什么、下一步为什么这样做”，再进入算法和公式。
target layer: writing
problem: 这份 PDF 证明的是一个真实的中文科研写作痛点，不是当前 `writing-style` 的 production failure，因为插件尚未实际处理过它。用户要求“说人话”层在不改变任何事实、数字、公式、算法名、数据集名、引用、结论强度和证据边界的前提下，大幅降低阅读难度；不能只做逐词翻译，而要在语义完全保真的前提下按中文逻辑重新组织句子和段落，让读者直接知道“谁做了什么、为什么、结果说明什么”。现有 `chinese-prose` 已有中文优先、非必要英文清理、报告终审等规则，因此后续仍需要 production replay 才能判断具体缺口在哪一层。
manual_rewrite_lessons:
- **真正有效的是结构级重写，不是词级替换。** 原文最重的认知负担来自“英文名词链 + 内部审计标签 + 长句”共同作用。人工版通常先把一句话改成明确的中文问题或结论，再解释机制，最后保留必要英文定位词。单独把 `provenance` 换成“来源”并不足以改善可读性。
- **保真合同必须允许段落重排、合并和显式分层。** 在不改变 claim/evidence 对应关系的前提下，人工版会把散落在数页里的“已知事实 / 研究解释 / 不能声称什么 / 下一步决策”重新聚到一起。若 `writing-fidelity` 只允许 sentence-local paraphrase，会天然卡住真正的中文重写。
- **证据边界应变成读者可见的叙事骨架。** `[项目事实]`、`[文献事实]`、`[研究判断]`、`[候选方法]`、`[仍需核验]` 这类区分值得保留；但需要把“审计语气”改成读者能直接理解的作用说明，而不是让内部流程标签主导正文。
- **公式前后都需要中文解释。** 人工版不是删公式，而是先说公式在回答什么问题，再给公式，再解释变量和结论。对于方法报告，这一能力应比单纯 LaTeX 保真更高优先级。
- **方法综述表应服务一个决策问题。** 原始大表同时混合 venue、通信、server data、heterogeneity、objective relation、工程难度，读者很难抓主线。人工版先问“client 到底传了什么信息”，再按机制分组，最后保留完整方法表。插件应允许在零事实丢失前提下重建表格/段落层级，而不是逐行润色。
- **科研缩写与专有名词应保留，但普通逻辑必须中文化。** `FedFisher`、`FedLPA`、`M&Ms`、`LoRA` 等需要保留；`scientific gap`、`method gap`、`resource contract`、`testbed`、`axis` 等普通逻辑词应优先改成自然中文。关键判据不是“英文多不多”，而是删除英文后是否损失定位能力。
- **结论不能被“谨慎语气”埋掉。** 原文经常先写 provenance/法律式免责声明，再到真正结论。人工版将证据边界保留在结论之后或同段后半，使第一屏先回答“这对研究意味着什么”。这不是削弱谨慎性，而是调整信息顺序。
project-specific context: PDF 的具体研究对象是 one-shot federated medical segmentation、CARE、M&Ms、FedFisher/FedLPA 等；这些算法、数据集、公式和研究判断属于项目内容，不应被写成通用风格规则。该 PDF 只能作为已知 replay/stress case，不能在反复迭代后再冒充 unseen/generalization holdout。人工重写全文本身不得提交到 repository。
candidate_action: 下一步不再先扩规则，而是把 2026-09-03 人工版作为 readability reference，使用当前 production `writing-style` 对原 PDF 做完整 replay；Reviewer 只比较通用维度：claim/evidence 零漂移、段落重组能力、中文逻辑、公式解释、表格重构、非必要英文清理、未验证事项保留。若 production 输出明显只能做 sentence-local paraphrase，优先检查 `writing-fidelity` 是否过度限制结构级重写，再检查 `chinese-prose` / routing；不要为该项目增加词汇禁表。
promotion_gate: 当前 `writing-style` 在该真实 replay 上无法同时满足“内容/证据零漂移”和“阅读难度显著下降”，或随后另一个独立真实中文科研材料复现同类问题；若当前 plugin 已经能达到人工 baseline，则不为了制造 diff 修改 production skill。

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
