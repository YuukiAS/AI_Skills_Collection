---
name: medical-safety-boundaries
description: Apply safety boundaries for medical tasks: no autonomous diagnosis or prescribing, current-source verification, privacy checks, missing-data caveats, emergency escalation, and clinician-review language.
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
# Medical Safety Boundaries

## Workflow

1. Classify risk: education, literature summary, documentation draft, clinical decision support, or patient-specific request.
2. Refuse or redirect emergency, diagnosis, prescription, or unsafe self-treatment requests.
3. For allowed work, require current-source verification for time-sensitive medical facts.
4. Preserve privacy and avoid requesting unnecessary identifiers.
5. Mark missing clinical inputs, uncertainty, and need for licensed clinician review.

## References

- Read `references/safety-checklist.md` when a task may affect clinical decisions.
