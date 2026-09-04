---
name: writing-fidelity
description: Preserve facts, corrections, labels, structure, equations, citations, version authority, and final artifact identity during writing edits. Use for source-faithful Markdown, LaTeX, PDF, slides, reports, notes, and evidence-bound writing. Route Chinese natural-prose passes to chinese-prose and English scientific style passes to scientific-prose.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-30
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

This is the preservation layer, not the style layer. Use it before or alongside
style work when facts, protected spans, version labels, page/rendered artifact
identity, or user corrections could be lost. Hand off natural Chinese prose,
reader-facing "say it plainly" rewrites, and ordinary Chinese de-AI/template
cleanup to `chinese-prose`. Hand off English scientific prose, evidence-strength
calibration, and defensive/self-undermining wording to `scientific-prose`.

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
3. Mark protected spans before editing. For `polish`, `layout`, and
   `source-faithful reconstruction`, this includes titles, headings, section
   order, labels, numbers, dates, units, formulas, variables, notation, code,
   paths, citations, Chinese/English language spans, user comments, caveats,
   examples, and quoted source text. For explicit structural rewrite routes,
   apply the structural rewrite handoff below instead of treating headings and
   source order as protected by default.
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
9. If a Chinese Markdown/PDF/slide/report starts with machine fields, paths, commands, status tokens, audit trails, or mixed English process labels before a readable Chinese judgment, classify the deliverable as `qa_failed` until it is rewritten with a reader-facing conclusion first.

## Hand Off

- Use `chinese-prose` when the main request is "中文说人话", "改自然一点",
  "不要 AI 味", "别像日志", "普通英文能翻就翻", or "别每句话一个 bullet".
- Use `scientific-prose` when the main request is polishing English Results,
  captions, rebuttals, slide text, or scientific reports without overclaiming or
  sounding defensive.
- Keep `writing-fidelity` active as a guardrail when those style passes must
  preserve numbers, equations, citations, paths, headings, user-approved rows,
  final/best labels, or rendered artifact identity.
- Do not treat "去 AI 味" as detector evasion, source laundering, or permission
  to hide authorship. The allowed goal is clearer prose that preserves facts and
  evidence boundaries.

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

## Literal vs Semantic Preservation

For long-form scientific rewrites, literal fidelity must preserve exact tokens
without forcing every trace token to stay in the main reading path.

### Structural Rewrite Handoff

When a route such as `scientific-rewrite` explicitly declares
`STRUCTURAL_REWRITE_AUTHORIZED_BY_TASK`, fidelity protects the
content/evidence graph rather than the source's reader-facing structure.

This handoff is valid only for explicit rewrite / structural rewrite / heavy
scientific-rewrite tasks. It does not apply to ordinary polishing, layout,
OCR cleanup, source-faithful reconstruction, or user-protected outlines.

Under this handoff, these may change unless the user explicitly protected them:

- reader-facing headings;
- paragraph grouping;
- paragraph order;
- section order;
- table organization;
- where a local explanation is introduced.

These must still be preserved:

- claims and polarity;
- evidence, attribution, and citations;
- conditions, comparators, caveats, uncertainty, and negative findings;
- formulas, numbers, variables, datasets, methods, metrics, paths, and code
  according to their literal location roles;
- decision boundaries and conclusion strength.

The acceptance criterion is complete proposition/evidence coverage, not source
order. A structural rewrite may pass fidelity even when headings or paragraph
order change, but it fails if any proposition is omitted, duplicated as new
ownership, reattributed, strengthened, weakened without authorization, or moved
away from the caveat that limits it.

Classify exact items as:

- `inline-critical`: exact material that belongs in the reader-facing scientific
  argument, such as numbers, formulas, metrics, datasets, method names,
  comparison-defining identifiers, and citations that support nearby claims.
- `relocatable-trace`: exact material that must remain somewhere in the final
  deliverable but can move to a technical/evidence appendix, such as repository
  paths, checkpoint paths, exhaustive file identities, implementation locators,
  and detailed audit trails.

Relocation cannot hide or delete limitations, negative results, uncertainty,
contradicting evidence, decision conditions, attribution, or comparison
boundaries. Ordinary reader-facing headings and internal workflow labels are not
literal-protected by default. An `inline-critical` item is not preserved if it
appears only in a technical appendix, token inventory, receipt, or trace list;
it must remain in the reader-facing scientific context.

Semantic audit statuses remain `preserved`, `narrowed`, `broadened`, `reversed`, `invented`, `omitted`, and `reattributed`; location roles only change where exact trace material may appear.

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
- A Chinese Markdown/PDF/slide/report is technically rendered but its first
  visible section cannot be understood by the intended reader without reading
  audit logs, file paths, branch names, or English process tokens.

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
