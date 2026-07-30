---
name: writing-fidelity
description: Prevent deletion, over-rewriting, mistranslation, formatting breakage, false completion, wrong version labels, and report/audit substitutes. Use for source-faithful Markdown, LaTeX, PDF, slides, reports, notes, best/final labels, month/date labels, author-approved rows, headings, and evidence-bound writing.
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
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
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
6. Before finalizing Markdown, LaTeX, PDF, slides, or reports, check artifact
   authority: title, method name, version label, selected row, final/best
   designation, and visible headline must match the latest user decision and
   evidence ledger. Do not invent lifecycle labels such as `start <project>` or
   `final <project>` unless the source explicitly defines them.
7. Finish with precise status and final artifact path. Do not treat reports,
   previews, audits, or side-by-side candidates as substitutes for the requested
   final artifact.
8. For Chinese, Markdown, PDF, slide, or report acceptance, verify readability authority before status: the first visible conclusion must be human-readable, and machine fields, paths, commands, status tokens, and audit trails must support rather than replace the conclusion.

## Version and Label Fidelity

When a document contains dates, months, leaderboard rows, draft labels, model
nicknames, or result variants, preserve the user's intended authority rather
than normalizing names into a cleaner but false story.

- Do not use month, season, stage, or old-draft labels as a substitute for
  the actual selected version. If the best or author-approved row is known,
  name that row by metric, absolute date, and evidence path.
- Do not call a result `final`, `complete`, `official`, `best`, or the project
  method unless the evidence supports that exact status. Use bounded labels such
  as `partial audit`, `leaderboard row by author rule`, `draft-only`, or
  `not verifiable` when that is the real state.
- Do not restore stale numbers, stale headings, inactive blocks, or old draft
  labels just because they are polished or familiar. Prefer the latest explicit
  user decision and the best-supported evidence.
- When two rows are both permissible, distinguish the best row from an alternate
  historical row; do not hide that distinction behind month shorthand.
- A report, audit note, preview, candidate output, old draft, or side-by-side comparison is not the final deliverable unless the user explicitly selected it as final. Name the selected artifact and the authority for that selection.
- Treat `audit result`, `leaderboard row`, `best row`, `author decision`, `old draft`, and month/date labels as different authority classes. Do not promote one class into another for cleaner prose.
- If the user's correction names a phrase as wrong or unnatural, treat that
  phrase as protected-negative text: avoid reintroducing it in headings, PDF
  titles, captions, status summaries, or final answers.

## Red Flags

- The user asked for polishing, but content was removed.
- Chinese was converted to English or mixed-language text was normalized.
- Titles, labels, equations, notation, citations, or ordering changed.
- A visual/style change touched wording or structure.
- A generated PDF/slide/document was not rendered and inspected.
- The user repeated a correction and the workflow did not change.
- The final artifact uses month shorthand, stage shorthand, or invented
  `start/final` project labels instead of the best-supported version.
- Machine fields, paths, status tokens, or checklist fragments appear before
  the human-readable conclusion in a user-facing report.

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
