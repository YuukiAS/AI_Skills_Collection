---
name: clinical-guideline-checking
description: Check clinical guideline claims against current authoritative sources, jurisdictions, population boundaries, recommendation strength, and update dates before using them in medical documents.
status: active
provenance: user-authored
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-06-19
profile_tags:
recommended_scope: project
---
# Clinical Guideline Checking

## Workflow

1. Identify the guideline body, jurisdiction, version/update date, population, and recommendation topic.
2. Verify the current guideline or label from an authoritative source.
3. Extract recommendation strength, evidence certainty, exceptions, contraindications, and implementation notes.
4. Compare the user draft against the source and flag mismatches, outdated wording, or overgeneralization.
5. Report exact boundaries: who the recommendation applies to, who it excludes, and what remains uncertain.

## References

- Read `references/guideline-checklist.md` before finalizing a guideline-based claim.
