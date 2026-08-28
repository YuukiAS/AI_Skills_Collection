---
name: research-reporting
description: Create repo-grounded research reports, milestone summaries, experiment reviews, technical notes, advisor/group-meeting reports, and result retrospectives from project evidence. Use for Markdown reports and internal scientific documentation, not for full journal manuscript workflows.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-08-29
profile_tags:
  - research-writing
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Research Reporting

Use this skill when the output is a project-grounded research report rather than a formal manuscript.

The report should help a researcher or advisor make a scientific decision. It is not a prettier execution log.

## Boundary

- Use for repo reports, milestone summaries, experiment retrospectives, technical notes, evidence-backed Markdown documents, advisor reports, and group-meeting research notes.
- Do not use for full manuscript planning, rebuttals, supplements, or grants; route those to the appropriate paper/grant workflow.
- Do not implement low-level PDF, DOCX, PPTX, or LaTeX file mechanics here.
- Keep `writing-fidelity` active when facts, equations, labels, citations, versions, or evidence authority must be preserved.
- For Chinese output, run `chinese-prose` after the evidence structure is stable.

## Source discipline

1. Identify the source of truth: code, results, logs, figures, tables, notes, prior reports, user corrections, and open questions.
2. Separate observed results, user-confirmed judgments, interpretation, hypothesis, limitation, and future plan.
3. Build a claim-evidence map before polishing prose.
4. Do not promote a run status, audit token, or implementation note into a scientific conclusion.
5. When the final analysis definition differs from an earlier attempt, report the final scientific definition unless the earlier error materially changes how old evidence must be interpreted.

## Default report structure

Use enough structure for review, but do not force every report into the same template.

A scientific report usually needs:

- the scientific question;
- why the current method/paper/idea is relevant;
- the final experiment or analysis design;
- the comparison/baseline;
- the main evidence, preferably a compact table or figure when comparison matters;
- interpretation and evidence boundary;
- the next decision or falsifiable question.

Do not add sections merely because a template has them.

## Advisor / group-meeting mode

If the audience is a PI, advisor, group meeting, lab meeting, or project decision meeting, read `references/group-meeting-advisor-reports.md` and apply it as a hard style/structure reference.

Core rules:

- Organize by scientific question and decision, not by Codex thread, run order, debug history, or iteration number.
- Main-body content should remain understandable if all repo paths, job IDs, audit tokens, and commit hashes are removed.
- `audit: PASS`, preflight status, push status, allocation state, validator tokens, and similar internal QA belong in the evidence appendix unless they are essential to scientific validity.
- Minor corrections, reruns, and debugging should not become standalone scientific sections. If a correction changes the valid comparison, fold the corrected rule into the final method description.
- Do not automatically generate `30-second version`, `3-minute version`, `elevator pitch`, `if you only have X minutes`, `you can say it like this`, or a verbatim speaking script. Only do this when the user explicitly requests a time-boxed or oral script.
- When one file serves both advisor and author, put advisor-facing science first and self-only material later: stop criteria, candidate mechanisms, implementation risks, evidence paths, commits, and reproducibility metadata.
- End with advisor questions only when a real scientific decision remains. Do not manufacture a discussion section.

## Results and tables

- Use a table when the reader must compare conditions across methods, datasets, budgets, metrics, or subgroups.
- Let the table carry exact values. The prose should interpret the comparisons that matter rather than repeat every cell.
- Do not repeat the same conclusion in a heading, table, body paragraph, and final summary unless each repetition serves a different purpose.
- State metric direction when it is not obvious.
- Keep strong baselines comparable: same data, split, endpoint, budget, and evaluation rule where the scientific question requires it.
- If the evidence is conditional on one fold, one dataset, a short budget, or a few seeds, keep that condition visible in the interpretation.

## Prose and structure QA

Reject or revise the report if it shows these patterns:

- process chronology dominates the scientific logic;
- main sections are named after internal lifecycle stages such as `correction`, `stability`, `audit`, `finalizer`, or `closeout`;
- one or two sentences are repeatedly promoted into their own headings;
- headings are mechanically `Result 1/2/3/4` or `Step 1/2/3` without a scientific reason;
- the report repeatedly uses `not X but Y`, `the real/core/most important thing`, `most valuable`, or similar rhetorical machinery instead of stating the observation;
- exact numbers are copied from the table into multiple paragraphs without additional interpretation;
- limited evidence is dramatized as `proof`, `overturning a hypothesis`, or general success/failure;
- ordinary workflow English is left in otherwise Chinese prose when a natural Chinese expression is clearer;
- report meta-text explains how the report is written rather than advancing the science.

## Workflow

1. Recover the user's original research question and current decision point.
2. Read the current repo/source evidence rather than relying on old chat state.
3. Identify the strongest result and the biggest unresolved uncertainty.
4. Decide the audience: advisor-facing, author-internal, mixed, or technical archive.
5. Build a claim-evidence map.
6. Draft the scientific narrative before adding paths and reproducibility metadata.
7. Add tables/figures where they reduce comparison burden.
8. Move internal QA/process details to the back unless scientifically necessary.
9. Run a de-duplication pass: remove repeated conclusions and unnecessary recap sections.
10. Run an audience-relevance pass: if deleting a paragraph would not change the advisor's understanding of the scientific problem, evidence, or next decision, move it to the internal appendix or remove it.
11. Run `chinese-prose` or the appropriate language/style pass.
12. Verify important claims against evidence anchors one more time.

## Acceptance

- Every important claim has an evidence anchor.
- Missing or weak evidence is named directly.
- Facts, interpretation, hypotheses, and plans are not blended together.
- The report does not invent results, citations, benchmarks, reviewer feedback, time constraints, or advisor questions.
- Advisor-facing prose is scientific rather than operational.
- The final experiment is described as the final experiment, not as a diary of corrections that produced it.
- Exact results are easy to compare.
- The next action is tied to a current uncertainty and is falsifiable where possible.
- If the document mixes advisor-facing and self-facing material, the boundary is explicit and the main scientific narrative comes first.
