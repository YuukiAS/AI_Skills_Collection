---
name: clinical-decision-support
description: Produce group-level clinical decision support, cohort evidence summaries, biomarker-stratified analyses, and guideline-style recommendation documents. Use for research, pharmaceutical, or policy documents, not bedside individual care.
status: active
provenance: unknown
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-06-19
profile_tags:
recommended_scope: project
license: MIT License
metadata:
  skill-author: K-Dense Inc.
allowed-tools: Read Write Edit Bash
---
# Clinical Decision Support

## Safety Boundary

Do not present recommendations as current medical fact without checking authoritative, current sources. Use this skill for research and documentation support, not for direct diagnosis, prescribing, or emergency decisions. For individual care plans, use `treatment-plans` and keep clinician review explicit.

## Workflow

1. Define document purpose: cohort analysis, evidence summary, treatment algorithm, biomarker strategy, or regulatory/research support.
2. Identify population, intervention/exposure, comparator, outcomes, time horizon, and required jurisdiction or guideline body.
3. Search or verify current authoritative sources before clinical claims: guidelines, regulator labels, trial publications, systematic reviews, and institutional policy.
4. Grade evidence and uncertainty. Separate observed data, model-derived estimates, expert consensus, and assumptions.
5. Build only the required document sections: executive summary, evidence table, statistical methods, recommendation rationale, limitations, and review/sign-off.
6. Validate privacy, de-identification, citation completeness, and whether all recommendations are traceable to dated sources.

## References

- Read `references/source-notes.md` before citing guidelines, labels, or standards.
- Read `references/evidence-checklist.md` when grading evidence, writing recommendation strength, or auditing safety language.
- Read `references/legacy-full-skill.md` only when you need the older LaTeX layout patterns, figure suggestions, or report-structure examples.

## Validation

- Every clinical recommendation has a source, date, population boundary, and uncertainty statement.
- Patient-level identifiers are absent unless the user explicitly provides de-identified material.
- Budget warnings about this domain are context warnings only; they do not block installing the complete medical domain.
