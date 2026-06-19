---
name: treatment-plans
description: Draft concise, clinician-reviewed treatment plan documents with goals, interventions, monitoring, and follow-up. Use only as documentation support with current-source verification, not as autonomous medical advice.
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
license: MIT license
metadata:
  skill-author: K-Dense Inc.
allowed-tools: Read Write Edit Bash
---
# Treatment Plan Writing

## Safety Boundary

This skill drafts documentation for clinician review. Do not diagnose, prescribe, alter medication, or imply that the plan is safe/current without checking authoritative sources and the user's local clinical context.

## Workflow

1. Confirm the intended use: one-page quick plan, 3-4 page standard plan, rehabilitation pathway, perioperative plan, chronic disease plan, or patient-education draft.
2. Gather constraints: de-identified patient context, diagnosis, goals, allergies/contraindications if provided, setting, jurisdiction, and required format.
3. Verify current sources for disease-specific interventions, dosing, safety monitoring, and follow-up intervals. Prefer guidelines, regulator labels, institutional protocols, and current reviews.
4. Draft only clinically necessary sections: goals, interventions, monitoring, escalation criteria, follow-up, patient preferences, and review status.
5. Mark uncertain or missing inputs plainly. Do not invent patient-specific facts.
6. Validate privacy, source dates, contraindication caveats, and clinician sign-off language.

## References

- Read `references/source-notes.md` for source hierarchy and date requirements.
- Read `references/treatment-plan-checklist.md` before finalizing a plan.
- Read `references/legacy-full-skill.md` only for older LaTeX templates and formatting examples.

## Validation

- The plan says it requires licensed clinician review.
- All medical facts that could change over time are sourced or flagged for verification.
- The document is concise by default; expand only when the user asks for a more detailed protocol.
