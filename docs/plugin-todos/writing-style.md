# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### English scientific slide microcopy and full-deck prose remain cognitively heavy after a nominal final pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4–v8 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb`, `ef08bc25673fb33b639e523504676c0f333d93f4` and `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. Earlier rounds exposed `Failure prevented`, mechanical `Example.` language, `What it measures`, `Focal method`, `Backbone` and `Rare fit`. The 33-page v8 deck still contains first-use domain terms that are expanded but not placed in enough context for a statistics audience (`COI`, `Metabarcoding`, `VicFlora`, `MGP`), source-note-like wording such as `That threshold is an implementation choice, not a CAT-TRACE theoretical constant.`, and dense table/slide language that is grammatically valid but unnecessarily hard to parse. The v8 English-final-pass record explicitly says that it only reviewed visible wording touched in v8, so untouched but still difficult language could survive.
problem: `scientific-prose` / presentation handoff needs to distinguish grammatical correctness from reader effort. A research slide should let a first-time expert reader understand what an unfamiliar term is, why it appears here, and what the sentence is asking them to retain. Expanding an acronym alone is insufficient when the term remains contextless. Final slide prose review also cannot be limited only to source lines modified in the current round: layout changes alter wrapping and old wording may still be cognitively heavy. The desired behavior is a full-deck audience-facing pass after scientific freeze: direct sentences, explicit local context for unfamiliar terms, natural action labels, short explanatory bridges where needed, and removal of internal/defensive/meta wording. This is not detector evasion and must not weaken scientific precision.
project-specific context: CAT-TRACE, TRACE, CORAL, VicFlora, COI, OTU, GBIF, MGP, catalogue/open-tail and the specific slide sentences belong to this project. Do not create a CAT-TRACE-specific banned-word list, and do not let writing-style alter equations, scientific claims, dataset values, theorem status, citations or slide layout.

## Active refinement

### Deep Research long-form rewrite: host Codex must own generation; external Terra is bounded final QA only
status: PROMOTE_NOW
active_task: `050_writing_style_host_codex_runtime`
source: 044/047/048/049 Deep Research rewrite series. 048 showed a one-shot production failure despite automated PASS; 049 then showed that making every semantic stage a paid Terra/OpenAI call was both the wrong plugin architecture and an unacceptable cost regression.
evidence: 048 implementation `928de2325d781ca630883d03e0f381092675b269`; 049 historical branch tip `19d7ba6f1a2a8752adfa4e7c11d3ebe9ed318070`; user rejected the first 049 A/B/C outputs as showing no perceptible improvement, and 049's paid per-stage pipeline later exhausted the API credit balance. 049 also produced useful engineering work around argument units, Meaning Cards, literal roles, reader-core/technical-trace separation, isolated replay and dataflow evidence, but that work is not Product PASS.
target layer: writing
problem: the remaining issue is architectural, not a missing vocabulary rule. `writing-style` is a Codex plugin and should guide the current host Codex model to perform document understanding, argument segmentation, Meaning Cards, rewriting, semantic self-audit, targeted repair and assembly in the normal task/session. Local deterministic helpers may verify exact literals and stage/evidence contracts, but must not fabricate semantic understanding or source-copy missing meaning. External Terra should not be a hidden generation dependency and should not be called for intermediate stages.
candidate_action: task 050 inherits useful 049 work but replaces the production owner model. Use isolated installed `writing-style` + current host Codex for generation/intermediate semantic work; use local deterministic exact/privacy/dataflow checks; keep the same fixed private A/B/C regression inputs; optionally run at most one combined candidate-only Terra reader QA for A/B/C and one final candidate-only Terra QA after style acceptance. Normal released plugin use keeps Terra/API off by default. Paid QA must be manual-only, hard-budgeted, and never triggered by ordinary push.
promotion_gate: 050 final cutover requires real installed host-Codex production behavior, fixed A/B/C user `STYLE_ACCEPT`, full private report user `ACCEPT`, and release/integration closure. Automated QA cannot override human rejection.

## Open candidates

### Audit `academic-humanizer` only for genuinely missing academic-writing capabilities
status: CANDIDATE_GENERIC
source: external resource discovery, 2026-09-02
evidence: `AIScientists-Dev/academic-humanizer` at commit `94b88b23703bed7df507acae7d6d5876209a0cdf` (`SKILL.md` v0.3.3), MIT. The inspected public skill focuses on English academic editing: AI-assisted paper/thesis/rebuttal/proposal cleanup, claim-evidence calibration, author-voice matching, and paper-vs-NSF/NIH proposal register. It has useful before/after academic examples, but much of its claim-strength and anti-template guidance overlaps the current `scientific-prose`; it also contains team-specific stylistic preferences such as broad AI-tell lists and a blanket em-dash removal rule.
target layer: writing
problem: this source may contain a few capabilities that are genuinely missing from the current `writing-style` / `research-writing` stack, especially author-reference voice matching and paper-vs-grant register separation. It should not be added to the active scientific-rewrite architecture merely because it is popular, and its AI-tell catalog must not become another phrase wall.
candidate_action: keep `academic-humanizer` as `REFERENCE_ONLY` during 050. Later run a bounded source-vs-current-capability audit against `scientific-prose`, `writing-fidelity`, and relevant `research-writing` skills. Selectively port only a concrete capability that is absent, non-duplicative, license-compatible, and supported by a real task.
promotion_gate: promote only if a later audit identifies a specific missing production capability and a real replay shows that current skills fail without it. Otherwise leave production behavior unchanged.

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate_action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion_gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

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
- Do not treat a documented multistage workflow as implemented unless the normal production path actually executes it.
- Do not use automated readability PASS to override explicit human rejection of the real artifact.
- Do not make normal `writing-style` use depend on an external paid model when the current host Codex can perform the semantic/writing work itself.
- Do not let ordinary Git pushes trigger paid model QA.
