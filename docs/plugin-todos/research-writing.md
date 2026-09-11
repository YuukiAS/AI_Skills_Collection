# research-writing — Long-Term TODO

Canonical maintenance inbox for the `research-writing` plugin.

## Open candidates

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

### Distinguish report content quality from PDF/DOCX rendering quality
status: BLOCKED_NEEDS_EVIDENCE
source: ongoing real research-report use
evidence: `research-reporting` correctly delegates low-level artifact mechanics
target layer: routing/qa
problem: future user feedback may mix narrative/report failures with PDF/DOCX layout failures owned by official document capabilities.
candidate_action: keep ownership explicit and only promote cross-layer handoff rules if a real artifact demonstrates the gap.
promotion_gate: real rendered report evidence.

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
