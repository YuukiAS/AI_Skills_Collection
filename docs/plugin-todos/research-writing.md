# research-writing — Long-Term TODO

Canonical maintenance inbox for the `research-writing` plugin.

## Open candidates


### Formal research reports can be scientifically correct yet still lack a coherent academic document identity
status: PARTIALLY_PROMOTED_IN_5.2.1
tracking: #20
source: real supervisor / group-meeting research-report rendering, 2026-09-19
evidence: private user-provided pair of rendered PDFs from the same report (not copied into this public repository); first render 17 pages/A4, second render 24 pages/US Letter; user feedback after the math was repaired: the report was readable and not obviously “wrong”, but still did not feel like a formal research document. Cross-reference: `docs/skill-todos/render-chinese-math-pdf.md` records the lower-level renderer/math/font failures from the same real use.
problem:
- Fixing equation rendering did not close the user-facing artifact-quality problem. The second PDF still looked like a generic/default document export rather than a deliberately designed supervisor-facing technical note.
- The visible issue was not one isolated CSS value. Several choices interacted: loose page density, large/uneven whitespace, a switch from A4 to US Letter without an explicit user request, mixed font texture, generic table/title treatment, and long-document rhythm that expanded the same material from 17 to 24 pages.
- Section hierarchy also exposed an authoring/render handoff problem. The source already contained human section numbers while the export added automatic numbering, producing forms such as `2.1 1. ...` and `8 9. ...`. The document title/TOC/title flow also repeated hierarchy instead of reading like a finished note.
- This is distinct from prose quality. The scientific content could be understandable and the formulas could be corrected, while the final artifact still failed the user’s expectation of “formal research report” presentation.
- Current `research-reporting` correctly says it should not implement low-level PDF/DOCX/LaTeX mechanics, and the existing TODO already keeps typography/pagination/render mechanics outside Research Authoring. This real case shows a remaining boundary gap: the document purpose still has to result in a coherent artifact-level identity (for example a formal advisor/group-meeting note rather than a generic article export) before/while the low-level renderer executes it. This NEW record intentionally does not decide whether that contract belongs in Research Authoring, the rendering layer, or a shared artifact layer.
project-specific context: the report’s scientific topic, methods, datasets, results and exact wording are project-local/private and must not become generic Research Authoring rules. The reusable evidence is only the document-purpose/style mismatch, duplicated hierarchy, page-geometry drift and final “readable but not formal” user experience.

2026-09-25 update: repository `5.2.1` keeps document semantics in Research Authoring and delegates explicitly requested formal PDF artifact mechanics to the standalone renderer companion installed by `research-main`. Standalone Marketplace Research Authoring fails closed when that companion is missing. This closes the bounded handoff/profile part of the issue; the broader academic document-identity question remains a future Research Authoring/artifact-quality refinement rather than a claim that all report design problems are solved.


### Keep research authoring separate from the generic language layer
status: READY_FOR_PROMOTION
tracking: #21
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
tracking: #22
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
tracking: #23
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
tracking: #24
source: Distributed_Imaging_Inference group-meeting report revision
evidence: `docs/provenance/RESEARCH_GROUP_MEETING_WRITING_REVIEW_2026_08_29.md`, `skills/writing/research/research-reporting/SKILL.md`, `references/group-meeting-advisor-reports.md`
target layer: writing/qa
problem: process-log language, invented time-boxed scripts, repeated result narration and implementation chronology were real user-facing failures; the active skill now contains fixes, but evidence is primarily one real report family.
candidate_action: replay these rules on the next independent advisor/group-meeting report and only add further rules when a new failure appears.
promotion_gate: at least one additional independent real report; protect current source-fidelity and claim-evidence behavior.

### Distinguish research-document semantics from comparison/render packaging
status: CANDIDATE_GENERIC
tracking: #25
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
tracking: #26
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
tracking: #27
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

### Advisor reports drafted before experiment completion should freeze the scientific story and leave only bounded result slots
status: NEW
tracking: UNASSIGNED
source: Distributed_Imaging_Inference / reusable-risk advisor report, 2026-10-02
evidence: DII `deliverables/group_meeting_2026-10-03/group_meeting_report_v1.md` at commit `259c9fcc1821a63533401e402b9b4a6016c58916`; frozen feasibility design and execution goal in `docs/research/2026-10-02_risk_transmission/05_FIRST_REUSABLE_RISK_FEASIBILITY_PROTOCOL.md` and `jobs/GOAL_MMS_FIRST_REUSABLE_RISK_FEASIBILITY_2026-10-02.md`
target layer: research-reporting planning / evidence-boundary / late-result update
problem: Advisor-facing reports are often prepared before a bounded experiment finishes. A common failure mode is to make the document look “complete” by filling it with runtime status, execution chronology or speculative interpretation; the opposite failure is to leave the whole report structurally unfinished and then rewrite the narrative after seeing the result. In this real case, the scientific question, loss definitions, experimental role and decision logic were already stable before the GPU result, while only a small set of decision-relevant empirical fields was genuinely unknown.
candidate_action:
- When the scientific question and experiment contract are already frozen, author the advisor-facing document around the stable story first: motivation, mathematical object, estimand/loss definition, why the experiment is informative, and the exact interpretation boundary.
- Represent unfinished evidence with a **bounded result slot**, not a generic “results coming later” section. Predeclare only the small set of quantities or decisions that the finished experiment is allowed to fill.
- Do not use queue state, runtime progress, job IDs, partial logs or executor chronology to fill missing scientific content. A concise sentence such as “formal result pending QA” is enough unless execution feasibility itself changes the science.
- Do not invent placeholder numbers, provisional claims, empty decorative figures or anticipated conclusions.
- After the audited result arrives, patch the bounded result slot and the directly dependent interpretation only. Do not silently rewrite the earlier motivation or method story to make the observed result look inevitable.
- If the result genuinely invalidates the frozen scientific framing, treat that as a research-design revision and explicitly rebuild the report rather than disguising it as a routine result insertion.
- Preserve the distinction between **document completeness** and **evidence completeness**: an advisor report can be structurally complete before every number exists, provided the unknown evidence is clearly bounded and the claim strength remains pending.
promotion_gate: replay on one additional advisor/group-meeting report prepared before a formal experiment completes; verify that late evidence can be inserted without execution-log filler, fabricated provisional claims, or post-hoc restructuring of the scientific story.

### Bilingual advisor reports should be two audience-calibrated versions, not interleaved translation
status: NEW
tracking: #28
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



### Formula display and notation should follow scientific role, not a blanket inline/block rule
status: NEW
tracking: UNASSIGNED
source: Distributed_Imaging_Inference / advisor-report PDF review, 2026-10-02
evidence: DII \`deliverables/group_meeting_2026-10-03/group_meeting_report_v1.pdf\` rendered from commit \`259c9fcc1821a63533401e402b9b4a6016c58916\`; user feedback that key formulas were visually buried while difficult calligraphic notation reduced readability; revised source in DII commit \`53c910c060782ecb1e925f35cf232462654adfd4\`
target layer: research-reporting document semantics / mathematical presentation / QA
problem:
- A previous anti-overuse correction pushed too many formulas into running prose. This made scientifically decisive definitions such as the centre empirical risk, cross-entropy, Dice and global Dice visually indistinguishable from ordinary notation.
- The opposite extreme is also wrong: turning every mathematical fragment into a display equation creates unnecessary vertical breaks and destroys reading flow.
- Decorative or difficult-to-distinguish mathematical symbols can further reduce readability in advisor-facing documents. Calligraphic symbols such as \(\mathcal V\) are inappropriate when a plain symbol such as \(V\) carries the same meaning.
candidate_action:
- Decide inline versus display from the **scientific role of the formula**, not from formula length alone and not from a global “prefer inline” or “prefer display” rule.
- Use a display equation when the formula defines a central estimand, objective, model map, theorem-level relation, or other mathematical object that the reader must notice and return to.
- Keep short definitions, parameter values, simple equalities, and one-step relations inline when they are subordinate to the prose.
- **Never isolate a single symbol or trivial fragment such as \(x\), \(\theta\), \(n\), \(p\), \(t=0\), or \(r=5\) as a display equation.** A display equation must carry a complete mathematical statement or definition with independent reading value.
- Avoid ornamental, calligraphic, script or otherwise hard-to-recognize notation in advisor-facing research artifacts when an ordinary Latin or Greek symbol is sufficient. Prefer \(V\) to \(\mathcal V\), and short named quantities such as \(D_{\mathrm{fg}}\) to visually dense constructions such as long textual subscripts.
- Preserve established notation when it has genuine mathematical meaning or is required by a cited theorem/method; do not simplify notation in a way that changes semantics.
- Research Authoring should decide **which formulas deserve emphasis and which notation is reader-appropriate**. The low-level renderer owns font embedding, spacing and actual equation layout after that semantic decision is fixed.
promotion_gate: replay on one additional advisor-facing mathematical report and one manuscript-like artifact; confirm that important formulas are easy to locate, routine symbols stay inline, and notation simplification does not alter meaning.

### Advisor-facing reports should separate reader-facing sources from internal authoring provenance
status: NEW
tracking: UNASSIGNED
source: Distributed_Imaging_Inference / advisor-report PDF review, 2026-10-02
evidence: the first rendered DII advisor PDF placed repository paths, internal source notes and authoring reminders on its final page together with real references; after review, public-facing references were kept in the report while internal paths were moved to \`deliverables/group_meeting_2026-10-03/group_meeting_report_v1_sources.md\`
target layer: research-reporting inclusion/exclusion planning / provenance boundary
problem:
- Internal source tracking is useful for authorship and reproducibility, but it is not automatically useful to an advisor reading the scientific argument.
- Repository paths, canonical filenames, rendering instructions, update reminders and “fill this after QA” notes can make a finished research report look like an internal export rather than a deliberate advisor-facing document.
- Genuine literature references and evidence sources needed to evaluate the scientific claims must remain visible; the problem is mixing those reader-facing sources with author-only tracking material.
candidate_action:
- In an advisor-facing report, keep only sources that the reader may reasonably need to understand, verify or follow the scientific argument: papers, datasets, externally meaningful reports, and concise evidence references.
- Move author-only material such as repository paths, internal filenames, canonical-source locators, rendering instructions, future-edit reminders and update rules into a companion provenance/source file or machine-readable metadata.
- Do not expose internal research-management traces merely because they are available in the source Markdown.
- Do not remove attribution that changes claim authority. If an internal artifact itself is the scientific evidence the advisor needs to inspect, reference it in a reader-facing form rather than hiding it.
- The final artifact should not contain author instructions such as “insert results after QA” unless the user explicitly wants that workflow state visible.
promotion_gate: replay on one additional advisor report and one formal manuscript/supplement workflow; verify that internal provenance remains recoverable without appearing as reader-facing scientific content.

### Final research artifacts must be surfaced as actual user-openable/downloadable deliverables
status: NEW
tracking: #29
source: STAT5060 Tutorial 1 Rich Edition final handoff, 2026-10-01
evidence: `YuukiAS/STAT5060-TA` commit `511fddfda9721f00c1d8bdb3774d9a17f37c3e95` successfully produced the canonical Rich Edition PDF and full provenance/QA evidence, but the executor-facing completion report exposed repository paths/status rather than an immediate user-openable/downloadable artifact surface; the user then had to ask whether the PDF had actually been produced and how to get it.
target layer: research-reporting -> artifact/workflow handoff -> user delivery
problem: A canonical repository path, checksum and PASS receipt prove provenance but do not complete user delivery. When Research Authoring produces or delegates a PDF/DOCX/LaTeX artifact, the final handoff should surface the actual finished file through the host's supported attachment/file-card/download/open mechanism whenever available, while still reporting the canonical repo path/hash separately. Research Authoring should not reimplement transport or renderer mechanics, but its delivery contract must not treat a path-only response as equivalent to handing the document to the user.
candidate_action:
- Add a user-delivery requirement to the Research Authoring artifact handoff: `canonical identity + real artifact surface + concise open/save instruction only when needed`.
- Prefer the host's native attachment/file reference or equivalent clickable artifact surface. Do not merely print a filesystem/repository path when a real file has been created and can be surfaced.
- Keep provenance separate: canonical repo path, commit and SHA remain useful evidence, but they supplement rather than replace the user-facing deliverable.
- If the current execution environment genuinely cannot expose the file directly, say so explicitly and use the nearest supported materialization/handoff mechanism; do not report a path-only artifact as fully delivered.
- Keep low-level delivery implementation in workflow/artifact infrastructure. Research Authoring owns the requirement that a requested finished research document reaches the user as an actual artifact.
promotion_gate: replay on one formal research-report PDF and one editable/office-style research deliverable; verify that the user can open/save the finished artifact directly without needing a second message asking where the file is.


### Student-facing assessment documents need a minimum-sufficient information budget
status: NEW
tracking: UNASSIGNED
source: STAT5060 Project Guide annotated-PDF revision, 2026-10-07
evidence: user annotated the two-page Project Guide candidate with 14 Highlights and 6 StrikeOuts after prior Research Authoring review; repeated feedback removed duplicated deadline language, extra page-policy detail, package-engineering explanation, universal model-selection explanation, redundant AI-policy prose, and unrelated privacy/policy detail while preserving the actual statistical task.
target layer: student-assessment planning / source-to-reader filtering / annotation handling / QA
problem:
- Student-facing assessment artifacts repeatedly accumulate true but unnecessary information because authoring optimizes for completeness of the source bundle instead of minimum information needed for correct student action.
- The same rule is often repeated in metadata, a date table, and later prose (for example a hard deadline), increasing cognitive load without changing student action.
- When a user marks text with StrikeOut, later authoring can mistakenly “repair” or paraphrase it instead of treating the deletion itself as a binding reader-facing decision.
- Detailed implementation/package instructions, grading rationale, edge cases, and internal reasoning can leak into a student Guide merely because they are useful to instructors or QA.
candidate_action:
- Add an explicit **minimum-sufficient student information budget** to student-assessment authoring: include a fact only when it changes what the student must do, submit, understand, or avoid.
- For each student-visible sentence, ask: **If this sentence is removed, can the intended student still complete the assessment correctly?** If yes, default to omission unless the sentence materially improves ambiguity, fairness, or safety.
- Give each administrative rule one canonical visible home. Do not repeat the same due date, hard-deadline consequence, page limit, file requirement, or policy in metadata, tables, and prose unless the second occurrence serves a genuinely different action.
- Treat raw PDF annotations as authoritative revision input. **StrikeOut means delete, not paraphrase.** Highlight comments constrain the selected region. A deleted sentence cannot return elsewhere under new wording without an explicit new human decision.
- Distinguish **statistical task completeness** from **administrative completeness**. Preserve source-emphasized research question, model formulation, statistical inference, analysis, findings, conclusions, references, and required deliverables; aggressively compress implementation and process detail.
- Do not make student-facing documents explain internal rubric logic, QA mechanics, package engineering, or every exception merely because these are needed by graders or executors.
- Add a deterministic duplication check for high-salience rules such as due date, hard deadline, page limit, file count, and named required statements. The intended occurrence count should be frozen by the Planner rather than inferred by the renderer.
- In annotated-document revisions, require a compact annotation ledger with counts by annotation type and an explicit disposition for every Highlight and StrikeOut before rendering.
- **Cumulative annotation replay must cross rounds, not only the latest PDF.** Before authoring a new annotated revision, reread every still-active Highlight/StrikeOut from prior rounds, mark supersession explicitly, and verify that a locally correct new edit does not resurrect an older rejected phrase or erase an earlier accepted sentence. A latest-round annotation ledger is insufficient without the cumulative lifecycle view.
- When the user says a previous version had better wording, recover that exact accepted wording/history before drafting a replacement; do not reconstruct it from memory or let an executor improvise.
promotion_gate: replay on one additional annotated Homework/Project revision and one new student-facing assessment artifact; verify that student action remains complete while duplicate/irrelevant administrative prose decreases and no StrikeOut content recurs.


### Student-assessment typography should allow a bounded rendered size range and preserve successful positive samples
status: SUCCESS_SAMPLE_ACCEPTED
tracking: UNASSIGNED
source: STAT5060 Project Guide V6 12pt user acceptance, 2026-10-07
evidence: private user-provided `Project-V6-12pt.pdf`, SHA256 `07978fe3cff3565663646e4d4c062df448d715c7ede44d3171e9a2f62cb70296` (2-page A4; not copied into the public repository), plus `YuukiAS/STAT5060-TA/docs/review/STAT5060_PROJECT_GUIDE_USER_ACCEPTANCE_V12.md`. The user explicitly accepted this version as the successful Project Guide baseline after cumulative annotation replay. At 12pt body text, the first page remains dense but readable and the second page has intentional rather than accidental whitespace; the larger body text improves reading comfort without forcing a third page.
target layer: student-assessment visual planning / positive-baseline registry / rendered review
problem:
- A single globally hard-coded body font size is too rigid for short student-facing assessment documents. The visually best size depends on content length, page count, document family, title hierarchy and the amount of natural whitespace.
- Earlier recovery work showed the opposite failure as well: font-size changes can invalidate pagination controls, so an executor must not freely shrink or enlarge text after seeing the render.
- A successful artifact can be lost if it is treated only as the latest candidate rather than registered as a positive sample with the characteristics that made it work.
candidate_action:
- Allow the Planner to freeze a **bounded typography candidate set** rather than one exact body size when typography is still genuinely open. For a restrained A4 assessment handout, a task may for example permit `11pt / 11.5pt / 12pt`; the exact range is document-family specific, not a universal constant.
- Hold copy, margins, typeface family, title hierarchy and information architecture fixed while comparing the permitted body sizes. Do not use font-size reduction as a hidden page-count repair.
- Run deterministic checks first, then let fresh rendered review choose among already-valid size candidates based on legibility, hierarchy, paragraph rhythm, page balance and reading effort. Occupancy/density remains diagnostic rather than a universal hard gate.
- Any body-size/leading change automatically reopens dependent pagination controls such as `Needspace`, keep-together rules and manual break hints, consistent with the existing non-recurrence amendment.
- Positive-baseline metadata should record the accepted artifact plus the relevant typography envelope: page size, margins, body size/leading, title sizes, page count and any intentionally accepted whitespace pattern.
- Treat the STAT5060 Project Guide V6 12pt PDF as a **successful positive sample** for concise postgraduate student-facing assessment guides: short two-page A4 artifact, restrained academic styling, clear title/due-date hierarchy, minimum-sufficient administrative detail, and statistical-task language dominant over policy/process language.
- Do not generalize its information architecture to Homework or other artifact families; reuse the principles and visual calibration, not the exact layout.
promotion_gate: replay the bounded-size selection on one additional student-facing assessment document and verify that the chosen size is selected by independent rendered review without changing approved copy, margins or page-count semantics.


### Human-facing assessment PDFs must pass a rendered-output hygiene gate, not only source-copy review
status: NEW
tracking: UNASSIGNED
source: STAT5060 Project final-consolidation Clear Writing review, 2026-10-08
evidence: the six human-facing Project PDFs passed source-level Clear Writing and semantic audits, but Chromium rendering inserted a current timestamp, candidate filename/title header, and a local `file:///users/a/e/aereinh/...` source path on every page. The English Question Bank also rendered its title twice because document metadata and an H1 both became visible. The Chinese Written Marking Guide still exposed machine-schema fields and malformed mixed-language text despite a source-level language PASS.
target layer: student-assessment / instructor-assessment rendering / Clear Writing QA / release-readiness
problem:
- Source Markdown can be reader-facing while the rendered PDF leaks browser-generated headers/footers, local filesystem paths, timestamps, candidate filenames, URLs, or duplicated metadata.
- A source-level Clear Writing PASS can miss renderer-added text because that text did not exist in the source.
- Text-search gates that look only for a small fixed blacklist can PASS while other machine-facing strings remain visible, such as schema field names, enum values, local-path syntax, seeds, or malformed bilingual fragments.
- Human-facing instructor documents can accidentally include machine grading schema blocks simply because the source bundle contains them.
candidate_action:
- Add a **rendered-output hygiene gate** after PDF generation and before rendered-review PASS. Extract text from the final PDF and fail on local/environment leakage such as `file://`, `/users/`, `/overflow/`, `localhost`, temporary build paths, source filenames, candidate filenames, or unintended current date/time headers.
- For Chromium/browser PDF routes, explicitly disable print headers and footers (for example `displayHeaderFooter=false` or the renderer-equivalent). Never rely on browser defaults.
- Add a title-occurrence check so YAML/HTML metadata plus visible H1 cannot silently create duplicated document titles.
- Inspect the top and bottom page margins visually on every page; browser-generated date/title/path/page-number furniture is a P1 release blocker even when body content is correct.
- Run Clear Writing / reader-facing review on the **rendered text layer as well as the source layer**. Source-copy PASS must not override a rendered artifact containing machine or environment traces.
- Separate human-facing rubric prose from machine schema. Raw field names, enum dumps, seed strings, local storage paths, repository instructions, and machine-only selection/log structures stay in supporting files unless the human marker genuinely needs them.
- For bilingual outputs, add a post-render scan for malformed mixed-language artifacts and token-splicing (for example accidental fragments like `状态ment`, `目标ed check`, or untranslated field-name suffixes) rather than checking only a predefined blacklist.
- Require the final rendered Reviewer to read representative full sentences from each page family, not merely confirm page count, clipping, and a handful of forbidden tokens.
promotion_gate: replay on one additional student-facing PDF and one instructor-facing rubric/examiner PDF rendered through HTML/Chromium; verify zero local-path/timestamp/header leakage, no duplicate title, and no machine-schema text in the normal human reading flow.


### Fixed presentation-question banks need applicability-aware selection and question-specific examiner keys
status: NEW
tracking: UNASSIGNED
source: STAT5060 Project public question bank + examiner key review, 2026-10-08
evidence: a public fixed bank correctly grouped questions by model family, but several questions only applied to a subtype or analysis state (for example a GLMM-only link/distribution question, a random-slope-only question, an offset/standardization question, a mixed-HMM/HMLVM extension question, or questions requiring fitted results). The mechanical rotation operated at model-family level only. The internal examiner key also contained templated cross-question and cross-family prose, including at least one mixed-membership answer key that incorrectly described exposure/mediator structure from the mediation chapter.
target layer: student-assessment / oral-presentation question-bank authoring / examiner-key QA
problem:
- A fixed/public bank is not fair merely because selection is mechanical. A mechanically selected question can still be inapplicable to the student's actual submodel, included components, or work-in-progress state.
- Model-family classification is often too coarse to define the eligible question pool.
- Template-generated examiner keys can look structurally complete while the expected answer does not actually answer the corresponding public question, or contains copied concepts from another method family.
candidate_action:
- Give every question a machine/internal **applicability predicate** before mechanical selection, for example required model subtype, required component, required fitted-result availability, or `ALWAYS_APPLICABLE`.
- Apply the rule in the order: `identify model family -> filter to applicable questions -> mechanically select within the applicable Q1/Q2 pools`. Never draw first and then improvise a replacement because the question does not fit.
- The public bank should explain any material applicability condition in reader-facing language when students need it; internal predicates may remain machine-readable.
- Work-in-progress presentations must always have a predeclared result-independent Q2 fallback pool so lack of final numerical results never creates ad hoc examiner discretion.
- Require a deterministic cross-check that each examiner-key entry has the same Question ID/text and that its `what this tests` / expected-core content is semantically specific to that exact question.
- Add a cross-family contamination scan: examiner-key text for one model family must not contain concepts unique to another family unless the public question itself requires that comparison.
- During independent review, sample every question-key pair, not only the public question wording or source map. A source-fidelity PASS for the public bank does not validate the examiner key.
promotion_gate: replay on one additional fixed oral/presentation bank with subtype-conditional questions; verify that all selected questions are applicable by construction and that no examiner-key entry contains copied content from another question or model family.


### Student-assessment PDF production must delegate to the canonical renderer and fail closed on browser fallback
status: NEW
tracking: UNASSIGNED
source: STAT5060 Project final-consolidation PDF regression, 2026-10-08
evidence: Research Authoring produced human-facing assessment PDFs through a Chromium/browser print route even though the repository already had the canonical `render-chinese-math-pdf` companion and Research Authoring's own reporting contract requires delegation to it. The resulting PDFs exposed browser timestamps, source filenames, and `file:///users/...` paths. This duplicated a previously known scientific-PDF failure mode where browser rendering bypassed the declared Pandoc/XeLaTeX production route.
target layer: student-assessment production / artifact handoff / renderer routing
problem:
- Research Authoring can stabilize content correctly yet hand PDF production to an ad hoc browser/HTML path, bypassing the installed renderer skill.
- Browser/Chromium output may leak environment paths and timestamps, use a different typography engine, and silently diverge from the accepted course/document family.
- A downstream rendered-review gate is too late if the production route itself violated the declared renderer authority.
candidate_action:
- For formal assessment PDFs, bind the production route before rendering: Research Authoring owns semantics; `render-chinese-math-pdf` owns PDF mechanics.
- Invoke the installed canonical renderer explicitly and record its route/identity receipt. Default production is Pandoc -> LaTeX -> XeLaTeX (or the renderer skill's current canonical route); native TeX follows the renderer's direct-TeX rule.
- Browser/Chromium rendering is diagnostic only. It must never satisfy the production gate or become an automatic fallback.
- If the renderer companion is unavailable or its required fonts/TeX dependencies are missing, fail closed with the exact dependency blocker. Do not substitute `wkhtmltopdf`, Chromium print-to-PDF, ad hoc HTML, or a local one-off template and report PASS.
- Preserve the accepted artifact's paper size, typography family, margins and pagination contract as resolved renderer profile inputs rather than recreating them in a second rendering stack.
- Add a deterministic producer/engine check to final assessment PDF QA so a browser-generated PDF cannot pass when the frozen route requires the canonical renderer.
promotion_gate: replay on one bilingual instructor rubric and one student-facing assessment handout; require canonical renderer receipts, non-browser producer identity, no local-path/timestamp leakage, and independent all-pages visual PASS.

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

### HW1 instructor-solution bounded revision broke an accepted seven-page baseline and reached release
status: NEW
source: `YuukiAS/STAT5060-TA` / STAT5060 2026–27 HW1 instructor-solution R/Python delivery, user feedback 2026-10-08
evidence:
- The user identified `STAT5060_HW1_Solution_R_Annotated.pdf` as the already acceptable seven-page R-route solution baseline and repeatedly instructed the executor not to damage correctly accepted content or presentation.
- In the executor's quoted incident acknowledgment, Codex stated that it regenerated the whole solution through the Markdown/render route, expanded the R solution from seven to nine pages, and put the unapproved result in `final-release/`. This is a user-supplied incident account and executor acknowledgment; the exact input/output PDF bytes, hashes, branch commit and actual renderer diff have not been independently verified for this TODO intake.
- The bounded requests concerned the solution header/meta text and student-style alignment, Q2(b) indentation and bullet formatting, and producing downloadable R and Python solution PDFs; several header/meta features had already been correct in the accepted annotated baseline.
problem:
- The failure occurred *after repeated explicit user instructions to preserve already-good material*. The executor treated a narrow repair as authority for full-document reflow, lost the accepted page-flow/visual baseline, and promoted an unaccepted candidate to the release directory. The user then had to discover regressions by inspecting the artifact.
- This failure class is **already explicitly covered** by the active Research Authoring student-assessment contracts: `student-assessment-delivery-closure-amendment-v1.md` §§4, 9–11 (positive baseline, bounded changes, user-review budget, incident mode, closure); `student-assessment-cumulative-acceptance-contract.md` Gates I, N, O, S (change allowlist, zero unrelated source/render changes, monotonic revision, full final-candidate regression, unmarked-content preservation); and `student-assessment-hw1-nonrecurrence-amendment-v1.md` §§11–12 (incident escalation and user-facing review protection).
- Therefore do not add another synonymous "do not change accepted content" policy and do not assume the mere existence of rules proves they were consumed. A central maintainer must establish which actual HW1 executor entry loaded the active contracts, what baseline identity and permitted edit scope reached the renderer, why unrelated pagination was not caught or escalated, and how an unaccepted artifact reached `final-release/`. Distinguish an intentionally necessary full-source compilation from an **unauthorized change to the full rendered artifact**.
project-specific context: the original seven-page layout, R/Python route names, Q2(b) list details, header wording and local `final-release/` structure belong to STAT5060 HW1. Seven pages is an accepted *case-specific baseline*, not a universal page-count rule for research/assessment PDFs. This raw feedback does not modify the ongoing 059 frozen implementation plan, approve a new plugin design, or claim a verified fix.
