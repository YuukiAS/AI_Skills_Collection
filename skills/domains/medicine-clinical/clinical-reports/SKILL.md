---
name: clinical-reports
description: Draft clinical case reports, diagnostic summaries, trial reports, SOAP/H&P/discharge-style documentation, and de-identified medical report templates with privacy, source, and guideline checks.
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
# Clinical Report Writing

## Safety Boundary

Use this skill for drafting and structuring medical documentation. Do not assert diagnosis, causality, guideline compliance, or regulatory status without current source verification and user-provided facts.

## Workflow

1. Classify report type: case report, diagnostic report, clinical trial/SAE/CSR document, SOAP note, H&P, discharge summary, or consultation note.
2. Confirm privacy constraints and remove identifiers before analysis or drafting.
3. Read the relevant checklist for report type, then verify any clinical guideline, CARE/CONSORT/STROBE/ICH statement, or disease fact against current sources.
4. Draft with clear separation between user-provided data, interpretation, missing data, and literature-backed context.
5. Keep required sections only; avoid copying long generic checklists into the output.
6. Validate de-identification, consent language, source dates, and limits of interpretation.

## References

- Read `references/source-notes.md` before citing guidelines, regulatory standards, or clinical facts.
- Read `references/clinical-report-checklist.md` for report-type routing and de-identification checks.
- Read `references/legacy-full-skill.md` only for detailed legacy templates, CARE checklist text, and LaTeX formatting patterns.

## Validation

- All patient facts are either supplied by the user or explicitly marked missing.
- All current clinical claims are dated and sourced.
- The report includes review/sign-off language when used for clinical or regulatory contexts.
