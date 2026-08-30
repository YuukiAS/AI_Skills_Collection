# research-writing — Long-Term TODO

Canonical maintenance inbox for the `research-writing` plugin.

## Open candidates

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
