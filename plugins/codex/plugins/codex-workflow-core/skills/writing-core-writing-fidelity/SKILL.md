---
name: writing-fidelity
description: Prevent deletion, over-rewriting, mistranslation, formatting breakage, and false completion in user-facing writing. Use when editing, polishing, summarizing, translating, OCR-cleaning, rendering, compressing, or final-checking Markdown, LaTeX, PDF, reports, notes, exam review material, technical documents, or source-derived writing.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-06-19
profile_tags:
  - writing
  - global
recommended_scope: global
---
# Writing Fidelity

Use this skill as a guardrail before editing or finalizing user-facing writing.
Its purpose is to stop Codex from creating a cleaner-looking substitute that
violates the user's source, constraints, correction history, or requested
artifact.

## Non-Negotiable Rule

Preserve first. Improve second.

Do not delete, rewrite, translate, reorder, rename, compress, or normalize
protected content unless the user explicitly asked for that exact operation.

If the user's constraints conflict, report a blocked or partial status. Do not
silently satisfy one constraint by violating another.

## Workflow

1. Classify the task: `polish`, `edit`, `rewrite`, `summarize`, `translate`,
   `layout`, `render`, or `source-faithful reconstruction`.
2. Extract the user's latest corrections as hard constraints. Pay special
   attention to complaints about deletion, automatic rewriting, language
   changes, title changes, unreadable output, collisions, missing glyphs, OCR
   errors, formula spacing, or prior failed attempts.
3. Mark protected spans before editing: titles, headings, section order, labels,
   numbers, dates, units, formulas, variables, notation, code, paths, citations,
   Chinese/English language spans, user comments, caveats, examples, and quoted
   source text.
4. Apply only the requested operation. For polishing, preserve substantive
   content. For layout, do not change wording. For OCR cleanup, fix corruption
   without canonicalizing valid source notation.
5. When the deliverable is rendered or formatted, verify the artifact itself:
   page count/size, readable font, glyphs, formulas, collisions, clipping,
   whitespace, and absence of stray QA notes.
6. Finish with precise status and final artifact path. Do not treat reports,
   previews, audits, or side-by-side candidates as substitutes for the requested
   final artifact.

## Red Flags

- The user asked for polishing, but content was removed.
- Chinese was converted to English or mixed-language text was normalized.
- Titles, labels, equations, notation, citations, or ordering changed.
- A visual/style change touched wording or structure.
- A generated PDF/slide/document was not rendered and inspected.
- The user repeated a correction and the workflow did not change.

## References

- Read `references/failure-summary.md` when the user has complained about prior
  writing failures, source fidelity, deletion, layout collisions, unreadable
  output, OCR/math corruption, or false completion.

## Completion Standard

Use precise status:

- `complete`: requested artifact exists and checks pass.
- `partial_complete`: useful output exists, but some criteria are not met.
- `qa_failed`: output exists but fails fidelity, readability, rendering, or
  content checks.
- `blocked`: cannot proceed without user input or external state.
- `blocked_target_not_met`: a page/space target cannot be met without
  unapproved deletion or unreadable output.
