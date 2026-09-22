# research-writing — Long-Term TODO

Canonical maintenance inbox for the `research-writing` plugin.

## Open candidates


### Formal research reports can be scientifically correct yet still lack a coherent academic document identity
status: PARTIALLY_PROMOTED_IN_5.0.7
source: real supervisor / group-meeting research-report rendering, 2026-09-19
evidence: private user-provided pair of rendered PDFs from the same report (not copied into this public repository); first render 17 pages/A4, second render 24 pages/US Letter; user feedback after the math was repaired: the report was readable and not obviously “wrong”, but still did not feel like a formal research document. Cross-reference: `docs/skill-todos/render-chinese-math-pdf.md` records the lower-level renderer/math/font failures from the same real use.
problem:
- Fixing equation rendering did not close the user-facing artifact-quality problem. The second PDF still looked like a generic/default document export rather than a deliberately designed supervisor-facing technical note.
- The visible issue was not one isolated CSS value. Several choices interacted: loose page density, large/uneven whitespace, a switch from A4 to US Letter without an explicit user request, mixed font texture, generic table/title treatment, and long-document rhythm that expanded the same material from 17 to 24 pages.
- Section hierarchy also exposed an authoring/render handoff problem. The source already contained human section numbers while the export added automatic numbering, producing forms such as `2.1 1. ...` and `8 9. ...`. The document title/TOC/title flow also repeated hierarchy instead of reading like a finished note.
- This is distinct from prose quality. The scientific content could be understandable and the formulas could be corrected, while the final artifact still failed the user’s expectation of “formal research report” presentation.
- Current `research-reporting` correctly says it should not implement low-level PDF/DOCX/LaTeX mechanics, and the existing TODO already keeps typography/pagination/render mechanics outside Research Authoring. This real case shows a remaining boundary gap: the document purpose still has to result in a coherent artifact-level identity (for example a formal advisor/group-meeting note rather than a generic article export) before/while the low-level renderer executes it. This NEW record intentionally does not decide whether that contract belongs in Research Authoring, the rendering layer, or a shared artifact layer.
project-specific context: the report’s scientific topic, methods, datasets, results and exact wording are project-local/private and must not become generic Research Authoring rules. The reusable evidence is only the document-purpose/style mismatch, duplicated hierarchy, page-geometry drift and final “readable but not formal” user experience.

2026-09-22 update: `research-reporting` now keeps document semantics in Research Authoring and delegates explicitly requested formal PDF artifact mechanics to the standalone renderer companion installed by `research-main`. Standalone Marketplace Research Authoring fails closed when that companion is missing. This closes the bounded handoff/profile part of the issue; the broader academic document-identity question remains a future Research Authoring/artifact-quality refinement rather than a claim that all report design problems are solved.


### Keep research authoring separate from the generic language layer
status: READY_FOR_PROMOTION
source: cross-plugin boundary audit after 050 + Distributed Imaging advisor-report revision, 2026-09-05
evidence: `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md`; Distributed Imaging report v2; existing `research-reporting` and paper/literature aggregates
target layer: routing/planning/qa
problem: the old `Research Writing` / `Writing Style` display-name pair made two different production jobs look overlapping. The current product display names separate them as `Research Authoring` and `Clear Writing`; the canonical slug remains `research-writing`. The remaining responsibility-boundary TODO is still active: research authoring owns scholarly/research artifact authoring, including what claims/evidence belong in a report or manuscript, how sections/tables/figures/citations are organized, and what the advisor/reviewer needs to see. The generic language layer should own content-preserving reader-facing wording after those decisions are stable.
candidate action:
- Keep the `research-writing` slug. The current user-facing displayName is `Research Authoring`, which describes the real domain: research reports, manuscripts, paper workflows, literature/citations, review/rebuttal/supplement coordination and claim-evidence organization.
- Treat reader-facing document planning as a first-class `research-writing` responsibility: audience, document purpose, decisive evidence, section jobs, main-text vs appendix split, table/figure roles and citation/evidence authority.
- Make table semantics an explicit research-writing responsibility: scientific comparison rows/columns, units, metric direction, precision/rounding, missing-value notation, comparability, captions/notes and prose/table division of labor.
- Delegate generic wording, de-translation, local formula explanation and say-it-plain final prose to the canonical generic language layer instead of duplicating a second Chinese/English style rule set.
- Do not let the language layer choose which experiment is decisive, silently delete a secondary experiment from a newly authored report, alter manuscript contribution scope or change literature/citation authority.
- Use the logical handoff `audience + document purpose + section job + claim/evidence boundary + table/figure role + allowed structural freedom -> generic language layer -> document-level QA`; do not invent a new schema unless a real production failure later requires one.
promotion gate: do not treat the display-name separation as resolving this responsibility-boundary item. Promote after replay on one advisor report plus one manuscript/paper workflow; verify that `research-writing` still owns document semantics while `Clear Writing` only changes expression.

### Reader-first advisor report rewriting must change the document plan, not just the wording
status: READY_FOR_PROMOTION
source: Distributed_Imaging_Inference group-meeting report v1 failure; earlier Deep Research Chinese rewrite; TRACE v8→v9 reviewer feedback
evidence: `Distributed_Imaging_Inference/deliverables/group_meeting_2026-09-05/group_meeting_report_v1.md`; human-approved rewrite `共享预训练医学分割模型_极低通信联邦适应_说人话重写版.md`; `TRACE/presentations/group_meetings/2026-07-29/REVISION_CONSTRAINTS.md`
target layer: planning/prose/qa
problem: a scientifically correct report can still fail badly when the writer preserves the source experiment chronology, internal labels, audit vocabulary and English abstraction stack. The v1 advisor report reproduced nearly every experiment in order and kept terms such as `local drift`, `phenotype-validity gate`, `measurement validity`, `Pattern H`, `P-SIMPLE`, `S-DICE`, `Level 2/3`, `falsification`, `transportability`, etc. The result read like a Deep Research / project log rather than something an advisor would naturally read.
candidate action:
- Before drafting, rebuild a **reader-facing document plan** from the scientific meaning. Protect facts, numbers, formulas, citations and claim strength, but do **not** protect the source section order, headings, experiment tokens or workflow labels.
- Main narrative should normally answer, in this order: **what is the scientific question -> what did the decisive evidence change -> what can we now say -> why it matters -> what simpler explanations still need to be ruled out -> what decision/input is needed from the advisor**.
- Do not narrate every experiment just because it exists. Keep only the experiments needed to establish the main claim in the body; move the rest to an appendix or a compact `question / comparison / result / implication` table.
- Internal experiment labels (`GATE_P_PASS`, `Pattern H`, `P-SIMPLE`, `S-DICE`, job names, audit status, seed IDs) are indexing aids, not audience-facing prose. Translate them into ordinary scientific language in the main text; preserve the exact token only in appendix/cross-reference when genuinely useful.
- Ordinary English abstractions must not carry the Chinese sentence skeleton. Keep formal method/dataset/software names, but rewrite common ideas in Chinese: explain what “local drift”, “measurement validity”, “personalization”, “transportability”, etc. mean in the specific scientific context instead of stacking labels.
- At first use, an unfamiliar term needs **role and purpose**, not just an expansion. TRACE v8→v9 showed that one extra clear sentence is better than an acronym expansion or compressed source-note wording.
- Prefer direct positive statements over defensive/meta phrasing (`not X but Y`, `gate`, `threat`, `closure`, `kill the paper`, `current status`). Explain the scientific reason directly.
- Tables carry exact values and experiment contracts; prose should interpret. If detailed split counts, seeds, hyperparameters or robustness variants are necessary, put them in a later methods/appendix section rather than interrupting the main argument.
- Advisor-facing names must match the advisor’s vocabulary. Internal project nicknames unknown to the advisor (for example a private pipeline codename) should be replaced by the broader scientific object, e.g. `UKB CMR pipeline`.
- Final QA should explicitly ask: **Could a reader who did not watch the experiments run understand the report without knowing our internal tokens? Could the first 2–3 pages stand alone? Does each paragraph earn its place in the decision story?**
promotion gate: incorporate into `research-reporting` and replay on the next advisor-facing report; preserve exact source fidelity while allowing large-scale structural rewriting.

#### 2026-09-11：同一研究材料拆成会议纪要与下一次会议报告
feedback_status: NEW
source: Distributed_Imaging_Inference / 用户要求将带批注的上次组会PDF、会后转述及近期研究记录，分别整理为两份面向老师的Markdown。
evidence: 内部记录 `YuukiAS/Distributed_Imaging_Inference/docs/research/DII_FEW_SHOT_ADAPTATION_LITERATURE_POSITIONING_2026-09-11.md`，提交 `59e45ed0d2abbccf4e5090ad960e24c0e1388db4`；用户附件 `Meeting_2026_09_05.pdf`；本次草稿 `deliverables/group_meeting_2026-09-05/meeting_minutes_2026-09-05.md` 与 `deliverables/group_meeting_2026-09-12/group_meeting_report_v1.md`，在DII提交 `6d295317cdcbc0d02958d5f0bf6ca9b90c77defd` 可定位。
problem: 用户明确指出，内部记录中的“如果DGST后gap仍存在”“最终论文需要怎样的benchmark结构”“明日组会的完整叙事”不能直接变成给老师看的报告。同一资料还包含不同时间的数据划分、已完成实验、老师口头反馈和未完成的新实验。只换标题或翻译英文，会保留错误的文体，也可能把会后结果写进上次会议、把研究者建议写成老师决定。
observed handling: 本次将上次纪要与未来报告分开；纪要以所供PDF为历史事实来源，老师转述与会后拟定安排另列，不补造参会者、共识或投稿期限。未来报告按科学问题、设计、有限结论、相关方法和待验证问题组织，保留必要数字及比较对象，不搬运执行日志。新结果即使在写作期间入库，也不自动纳入未经复核的科学叙述；预留结果更新位置而不生成假结果或空白图表。原PDF个别图表数字不一致时，在来源说明中保留差异，不替用户暗自统一。
project-specific context: CARE/M&Ms、91/59与91/30/29、DGST、FedFisher、pFLFE及MICCAI安排是DII内容，不能成为通用写作模板。原文件原本就是内部记录，并非错误地交付的导师报告；本例记录的是文体转换需求和误用风险，未证实调用过当前正式插件，不标记为生产回归。两份草稿尚待用户审阅；本条补充已有候选的真实证据，不改变其推广状态，也不修改插件版本或运行规则。中文措辞层的配套记录见 `writing-style.md` 的“Keep style cleanup downstream of scientific structure”。

### Meaning-first rewriting should be a reusable transformation pattern
status: READY_FOR_PROMOTION
source: successful manual Deep Research rewrite + TRACE v8→v9 language review
evidence: `共享预训练医学分割模型_极低通信联邦适应_说人话重写版.md`; TRACE v9 revision evidence
 target layer: planning/prose
problem: phrase-level cleanup is insufficient when the source prose is built from compressed noun stacks, slash-separated abstractions, audit labels or source-note language.
candidate_action:
- Build a claim/terminology map first, then rewrite complete argument units from meaning rather than editing sentence-by-sentence.
- Preserve literal content only for objects that truly require literal fidelity: numbers, formulas, code identifiers, formal method names, citations. Reader-facing headings, labels and explanatory sentences usually require semantic preservation, not literal preservation.
- Use the pattern repeatedly validated in the manual rewrite: **plain-language conclusion -> intuition / concrete example -> exact technical detail / formula -> evidence boundary**.
- When a process is sequential, write it as a sequence. When several alternatives are parallel, use a short list/table. Do not compress everything into one long sentence merely to save space.
- Remove repeated restatements once the role is clear. TRACE v9 repeatedly improved readability by replacing source-note repetition with one direct explanation and a short takeaway.
promotion_gate: replay on one additional long-form scientific report and one advisor-facing report.

### Cross-project replay of advisor-facing report rules
status: CANDIDATE_GENERIC
source: Distributed_Imaging_Inference group-meeting report revision
evidence: `docs/provenance/RESEARCH_GROUP_MEETING_WRITING_REVIEW_2026_08_29.md`, `skills/writing/research/research-reporting/SKILL.md`, `references/group-meeting-advisor-reports.md`
target layer: writing/qa
problem: process-log language, invented time-boxed scripts, repeated result narration and implementation chronology were real user-facing failures; the active skill now contains fixes, but evidence is primarily one real report family.
candidate_action: replay these rules on the next independent advisor/group-meeting report and only add further rules when a new failure appears.
promotion_gate: at least one additional independent real report; protect current source-fidelity and claim-evidence behavior.

### Distinguish research-document semantics from comparison/render packaging
status: CANDIDATE_GENERIC
source: ongoing real research-report use; Clear Writing 055 final user-acceptance comparison failure, 2026-09-17
evidence: `research-reporting` already delegates low-level artifact mechanics; Clear Writing 055 then produced multiple unusable Original-vs-C6 acceptance artifacts because long-form scientific content was mechanically chunked into misaligned pages and citation/report/gate material was not separated by domain semantics. The generic packaging follow-up is recorded separately in `docs/plugin-todos/workflow-core.md`.
target layer: research-document planning/qa boundary with workflow-core and artifact/presentation rendering
problem: A research-document comparison is not only a rendering problem. When a rewrite legitimately reorganizes sections, condenses repeated evidence, converts prose into tables, or moves details between main text and appendix, a generic packager cannot infer correspondence by sentence count or page length. The domain owner must decide which source unit corresponds to which rewritten scientific unit, what evidence/citation material is in scope, and which formulas/tables/code/limitations/future-work blocks must stay coherent. Conversely, Research Authoring should not own slide typography, pagination, clipping, Office/PDF rendering, repo delivery paths, or retry/acceptance-state mechanics.
candidate_action:
- For an Original-vs-revised research report/manuscript acceptance surface, define a lightweight **semantic alignment plan** before layout: source section/paragraph group/claim-evidence unit/table/formula/code block/limitation/future-work item -> corresponding candidate unit. This is a planning responsibility, not a new persistent schema by default.
- Align by scientific meaning rather than character count, sentence count or equal page length. One source unit may map to several candidate units, and several source units may legitimately collapse into one candidate unit when the rewrite removes repetition or reorganizes the argument.
- Treat scientific tables, formulas, code/path snippets, limitation statements and future-work statements as coherent units. Do not split a table mid-row, a formula across unrelated comparison pages, or detach a limitation/future-work qualifier from the claim it constrains merely to make pages even.
- Citation/reference handling belongs to research-document semantics. If the user excludes bibliography/reference bulk from the acceptance comparison, omit that bulk from the main review surface, but do not silently strip attribution or citation-bearing context when it changes claim authority, provenance or scientific meaning. Main-text vs appendix/reference handling must follow the frozen user scope.
- The research comparison surface should contain the research content being judged, not workflow Gate history, paid-review receipts, render-proof pages or internal review packets. Those are workflow evidence unless the user explicitly asks to inspect them.
- Research Authoring QA should ask whether the revised document's structural transformation is scientifically legitimate: claims/evidence still correspond, decisive experiments are not lost, modality/limitations/future work remain correct, and tables/figures/formulas still play the intended document role. Visual legibility/render correctness remains the artifact/presentation capability's job.
- Handoff to the artifact layer should be `comparison scope + semantic alignment plan + inclusion/exclusion rules + atomic technical units + allowed structural freedom`; the artifact layer then decides slide/page composition without redefining scientific correspondence.
- Keep the generic workflow concerns in workflow-core: freezing the acceptance contract, canonical repo delivery, truthful artifact identity, real-open/render evidence, repeat-failure circuit breaker, cost discipline and user handoff.
promotion_gate: **do not modify the already-reviewed 056 architecture or implementation package for this item. Finish 056 first.** After 056 completes, map what its generic Acceptance Review / Evidence Fidelity / Actual-Surface rules already cover, then replay this domain boundary on one real advisor/report comparison and one manuscript/paper-like comparison. Promote only the residual research-specific semantics; do not duplicate workflow-core or presentation rendering rules.


### Advisor/group-meeting reports need method and dataset orientation before project-specific results
status: NEW
source: Distributed_Imaging_Inference / Supervisor Bridge MOSAiC group-meeting report revision, 2026-09-19
evidence: DII \`docs/results/SUPERVISOR_BRIDGE_GROUP_MEETING_PRELIMINARY_2026-09-19.md\`; user feedback that an advisor-facing report was not self-contained because it moved too quickly into project execution and omitted a clear explanation of MOSAiC and the two datasets.
target layer: research-reporting planning / audience model
problem: A group-meeting report can be scientifically correct yet still assume too much project context. The advisor should not have to infer what a newly introduced paper contributes, why its algorithmic machinery is used, what the datasets contain, or how the current experiment maps those objects into the research question. Starting from internal progress, current pipeline status or a project-specific adaptation before introducing the source method/data makes the report hard to follow and wastes meeting time.
candidate_action:
- For a report centered on a newly introduced method/paper, first give the minimum conceptual background required to understand the experiment: original problem, central idea, decisive properties/assumptions, why the main computational device is used, and the boundary of the original claim.
- For every primary dataset, include a compact reader-facing data card before presenting results: scientific task, modality, patient/case count, real site/centre structure, labels/endpoints, relevant heterogeneity, and the exact subset/client definition used in the current study.
- Clearly separate **official dataset background** from **the local artifact/current experiment subset** when counts or site coverage differ. Do not collapse “375 cases in the published dataset” and “345 subjects in the locally available artifact” into one number.
- Explain the translation from source method to the current domain explicitly (e.g. original local likelihood/risk -> frozen segmentation logits -> low-dimensional local imaging risk -> TT message). Do not require the advisor to reconstruct this mapping from implementation details.
- Keep the orientation section short enough to support the decision story; this is not a literature-review dump. Include only the paper properties and dataset facts needed to understand the experiment and its interpretation.
promotion_gate: replay on one additional advisor/group-meeting report involving a new method plus at least one unfamiliar dataset; verify that a reader outside the project can understand the experiment before seeing any result.

### Advisor-facing research reports should suppress execution/runtime details unless they change the scientific interpretation
status: NEW
source: Distributed_Imaging_Inference / Supervisor Bridge preliminary group-meeting report revision, 2026-09-19
evidence: user rejected a report section explaining why a Longleaf run took longer than estimated; the runtime explanation was useful for internal planning but irrelevant to the advisor-facing scientific discussion.
target layer: research-reporting inclusion/exclusion planning
problem: Internal engineering facts are easy to retrieve and often feel concrete, so report writers over-include them. Runtime estimates, queue/allocation state, cache/I/O bottlenecks, job IDs, implementation chronology, why an executor is slower than expected, and similar details do not belong in an advisor-facing group-meeting report unless they create a scientific feasibility result, invalidate evidence, or require an advisor decision.
candidate_action:
- Before including an execution detail, ask: **Does this change the scientific claim, feasibility boundary, evidence quality, or decision requested from the advisor?** If not, omit it from the main report.
- Keep operational diagnostics in internal notes / execution reports. Do not create a “why the run is slow” section merely because the run is ongoing.
- It is acceptable to state the scientific evidence boundary concisely (“formal comparison is still running”) without narrating compute progress.
- If computational scalability itself is the scientific question, report the measured complexity/runtime as a result; distinguish that from incidental engineering overhead.
- Group-meeting main text should prioritize method, data, estimand, comparison, evidence and next scientific decision over implementation status.
promotion_gate: replay on the next long-running computational research project and confirm that internal execution evidence remains available without contaminating the advisor-facing narrative.

### Bilingual advisor reports should be two audience-calibrated versions, not interleaved translation
status: NEW
source: Distributed_Imaging_Inference / recurring user preference for group-meeting reports, reinforced 2026-09-19
evidence: DII \`docs/results/SUPERVISOR_BRIDGE_GROUP_MEETING_PRELIMINARY_2026-09-19.md\`; user explicitly requested English in the first half for the advisor and Chinese in the second half for personal preparation.
target layer: research-reporting document architecture
problem: When one artifact must serve an English-speaking research audience and the user's own Chinese preparation, line-by-line bilingual text or interleaved translation creates visual clutter and weakens both versions. The English section needs to stand alone as the advisor-facing report; the Chinese section can be more explanatory and can clarify the user's own speaking logic without changing scientific claims.
candidate_action:
- When the user explicitly requests this audience split, default to **complete English version first, complete Chinese version second**.
- The two halves must share the same evidence boundary, numbers, formulas and claim strength, but they do not need sentence-level literal correspondence.
- English should be concise and presentation-ready for the advisor. Chinese may include additional intuition, speaking cues and “how to understand this result” explanations for the user, while avoiding unsupported new claims.
- Do not duplicate internal execution details in either half merely because the Chinese half is “for self”; personal preparation still benefits from a scientific decision narrative.
- Make the audience role explicit in headings so downstream presentation/rendering tools can safely use only the English half when appropriate.
promotion_gate: replay on two independent bilingual research reports and confirm semantic parity without literal translation artifacts.


## Recently promoted / established

- Advisor-facing reports organize around scientific question and decision, not run/debug chronology.
- Internal audit/PASS/commit/job state belongs outside the scientific main narrative.
- Minor corrections are folded into the final method when they define the valid analysis.
- No invented 30-second/3-minute/elevator scripts without explicit user request.
- Tables carry exact values; prose interprets rather than repeats every cell.
- Limited evidence uses conditional conclusions rather than dramatic claims.

## Do not do

- Do not create a second generic “humanizer” skill for these report rules.
- Do not move repo execution logs into advisor-facing prose just because they are easy to retrieve.
- Do not equate source fidelity with preserving source organization, headings or internal experiment vocabulary.
- Do not make an advisor learn project-internal tokens before they can understand the scientific argument.
