# research-writing — Long-Term TODO

Canonical maintenance inbox for the `research-writing` plugin.

## Open candidates

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

### Meaning-first rewriting should be a reusable transformation pattern
status: READY_FOR_PROMOTION
source: successful manual Deep Research rewrite + TRACE v8→v9 language review
evidence: `共享预训练医学分割模型_极低通信联邦适应_说人话重写版.md`; TRACE v9 revision evidence
 target layer: planning/prose
problem: phrase-level cleanup is insufficient when the source prose is built from compressed noun stacks, slash-separated abstractions, audit labels or source-note language.
candidate action:
- Build a claim/terminology map first, then rewrite complete argument units from meaning rather than editing sentence-by-sentence.
- Preserve literal content only for objects that truly require literal fidelity: numbers, formulas, code identifiers, formal method names, citations. Reader-facing headings, labels and explanatory sentences usually require semantic preservation, not literal preservation.
- Use the pattern repeatedly validated in the manual rewrite: **plain-language conclusion -> intuition / concrete example -> exact technical detail / formula -> evidence boundary**.
- When a process is sequential, write it as a sequence. When several alternatives are parallel, use a short list/table. Do not compress everything into one long sentence merely to save space.
- Remove repeated restatements once the role is clear. TRACE v9 repeatedly improved readability by replacing source-note repetition with one direct explanation and a short takeaway.
promotion gate: replay on one additional long-form scientific report and one advisor-facing report.

### Cross-project replay of advisor-facing report rules
status: CANDIDATE_GENERIC
source: Distributed_Imaging_Inference group-meeting report revision
evidence: `docs/provenance/RESEARCH_GROUP_MEETING_WRITING_REVIEW_2026_08_29.md`, `skills/writing/research/research-reporting/SKILL.md`, `references/group-meeting-advisor-reports.md`
target layer: writing/qa
problem: process-log language, invented time-boxed scripts, repeated result narration and implementation chronology were real user-facing failures; the active skill now contains fixes, but evidence is primarily one real report family.
candidate action: replay these rules on the next independent advisor/group-meeting report and only add further rules when a new failure appears.
promotion gate: at least one additional independent real report; protect current source-fidelity and claim-evidence behavior.

### Distinguish report content quality from PDF/DOCX rendering quality
status: BLOCKED_NEEDS_EVIDENCE
source: ongoing real research-report use
evidence: `research-reporting` correctly delegates low-level artifact mechanics
target layer: routing/qa
problem: future user feedback may mix narrative/report failures with PDF/DOCX layout failures owned by official document capabilities.
candidate action: keep ownership explicit and only promote cross-layer handoff rules if a real artifact demonstrates the gap.
promotion gate: real rendered report evidence.

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
