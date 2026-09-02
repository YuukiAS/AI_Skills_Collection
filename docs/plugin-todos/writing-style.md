# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Incoming real-use feedback

### English scientific slide microcopy and full-deck prose remain cognitively heavy after a nominal final pass
status: NEW
source: TRACE / CAT-TRACE group-meeting deck v4–v8 reviews
evidence: `YuukiAS/TRACE` commits `e36cb5d93fc882ce158d88ac9201fe494b98b69a`, `1de90f2f26b3f787073ecedd7a4df41a985712eb`, `ef08bc25673fb33b639e523504676c0f333d93f4` and `26fd2ad0f042f0a8d7c7dc2154392e3f9460760d`. Earlier rounds exposed `Failure prevented`, mechanical `Example.` language, `What it measures`, `Focal method`, `Backbone` and `Rare fit`. The 33-page v8 deck still contains first-use domain terms that are expanded but not placed in enough context for a statistics audience (`COI`, `Metabarcoding`, `VicFlora`, `MGP`), source-note-like wording such as `That threshold is an implementation choice, not a CAT-TRACE theoretical constant.`, and dense table/slide language that is grammatically valid but unnecessarily hard to parse. The v8 English-final-pass record explicitly says that it only reviewed visible wording touched in v8, so untouched but still difficult language could survive.
problem: `scientific-prose` / presentation handoff needs to distinguish grammatical correctness from reader effort. A research slide should let a first-time expert reader understand what an unfamiliar term is, why it appears here, and what the sentence is asking them to retain. Expanding an acronym alone is insufficient when the term remains contextless. Final slide prose review also cannot be limited only to source lines modified in the current round: layout changes alter wrapping and old wording may still be cognitively heavy. The desired behavior is a full-deck audience-facing pass after scientific freeze: direct sentences, explicit local context for unfamiliar terms, natural action labels, short explanatory bridges where needed, and removal of internal/defensive/meta wording. This is not detector evasion and must not weaken scientific precision.
project-specific context: CAT-TRACE, TRACE, CORAL, VicFlora, COI, OTU, GBIF, MGP, catalogue/open-tail and the specific slide sentences belong to this project. Do not create a CAT-TRACE-specific banned-word list, and do not let writing-style alter equations, scientific claims, dataset values, theorem status, citations or slide layout.

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

### Deep Research 中文报告作为 `writing-style` 的真实压力测试输入
status: BLOCKED_NEEDS_EVIDENCE
source: ChatGPT Deep Research 中文科研报告，2026-08-31；该 PDF 由 Deep Research 直接生成，**没有经过 `writing-style` plugin**。
evidence: 用户提供的 22 页 PDF《共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策》；正文反复出现 `anchor`、`provenance`、`estimand`、`scientific gap`、`method gap`、`residual gap`、`resource contract`、`strict one-shot contract`、`testbed`、`axis`、`comparator`、`correction/stability run` 等表达，并存在“法律意义上证明”“forensic-level exact provenance proof”一类不必要的法律/取证腔。
target layer: writing
problem: 这份 PDF 证明的是一个真实的中文科研写作痛点，不是当前 `writing-style` 的 production failure，因为插件尚未实际处理过它。用户要求“说人话”层在不改变任何事实、数字、公式、算法名、数据集名、引用、结论强度和证据边界的前提下，大幅降低阅读难度；不能只做逐词翻译，而要在语义完全保真的前提下按中文逻辑重新组织句子和段落，让读者直接知道“谁做了什么、为什么、结果说明什么”。现有 `chinese-prose` 已有中文优先、非必要英文清理、报告终审等规则，因此下一步应先用**当前 production plugin**完整 replay 这份材料，再判断是已有规则已经足够、只是以前没有调用，还是确实需要修改 skill / fidelity contract / routing。
project-specific context: PDF 的具体研究对象是 one-shot federated medical segmentation、CARE、M&Ms、FedFisher/FedLPA 等；这些算法、数据集、公式和研究判断属于项目内容，不应被写成通用风格规则。该 PDF 只能作为已知 replay/stress case，不能在反复迭代后再冒充 unseen/generalization holdout。
candidate_action: baseline-first：先用未修改的 `writing-style` 对同一材料做一次完整、保真、中文优先的重写；若真实输出仍存在抽象英文标签、英文科研语序、逐词翻译、过强 `writing-fidelity` 导致不敢整句重写，或可读性明显不足，再由 Reviewed Handoff Planner 冻结最小通用修改。禁止为了这一个 PDF 增加项目词汇禁表或专门规则。
promotion_gate: 当前 `writing-style` 在该真实 replay 上无法同时满足“内容/证据零漂移”和“阅读难度显著下降”，或随后另一个独立真实中文科研材料复现同类问题；若当前 plugin 已经能把该 PDF 改好，则不为了制造 diff 修改 production skill。

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
