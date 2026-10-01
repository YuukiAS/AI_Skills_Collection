# Project Instructions Editor — Readability Design History

Date: 2026-10-01  
Status: PLANNING_ONLY  
Candidate future standalone Skill: `project-instructions-editor`

This document records the recent design evolution that led from a general ChatGPT readability problem to a candidate reusable Project-instruction editing capability. It is design evidence only.

**No production Skill, Plugin, profile, release, registry entry, README card, Marketplace package, or installation route is authorized or created by this document.**

## 1. Real problem

The user repeatedly observed that technically correct ChatGPT answers became difficult to read because Project-local instructions, engineering vocabulary, logs, status fields, and mathematical formatting leaked directly into the user-facing answer.

Two representative failures were preserved outside the public repository as private user evidence:

- an AI Research Stack answer with many ordinary English engineering phrases such as `source-of-truth`, `specialist routing`, `fallback`, `candidate consumption`, and design-document-style status language;
- a statistics explanation where ordinary statistical terms remained in English, simple parameter values and ratios were promoted to block equations, and the answer fragmented into many short lines.

The reusable problem is not “make everything Chinese.” It is:

> preserve exact machine identifiers and formal names when they matter, while transforming ordinary technical control language into a readable user-facing explanation.

## 2. v1 — stronger account-level readability rules

The first approach strengthened global personalization around four recurring failures:

1. unnecessary English in Chinese explanatory prose;
2. sentence-per-line and status-field fragmentation;
3. block-equation overuse for simple values and one-step relationships;
4. project/log/code language being copied directly into the explanation.

This was directionally correct but structurally incomplete. ChatGPT Project instructions can override global custom instructions, so account-level wording alone cannot guarantee Project-thread behavior.

## 3. v2 — two-layer architecture

The second design introduced two layers:

- account-level personalization as the complete user-reading contract;
- a short self-contained Project bridge for Projects that already have Project instructions.

The bridge repeated only the user-reading essentials:

- ordinary translatable technical terms should be Chinese;
- exact products, code, paths, fields, repository names, errors, and other machine identifiers may stay exact;
- prose should use natural paragraphs and only necessary structure;
- simple mathematics stays inline;
- machine-readable deliverables remain exact.

This version also removed mechanical rules such as English-word counts, fixed paragraph counts, and fixed block-equation counts.

## 4. v3 — machine-deliverable boundary and semantic English exception

Critic review exposed two remaining boundary problems.

First, readability rules must not rewrite required machine deliverables such as:

```text
RESULT=PASS
FINAL_HEAD=...
PUSHED=YES
```

v3 therefore separated:

- user-facing explanatory prose;
- exact machine deliverables required for copy, execution, parsing, or protocol compliance.

Second, “original terminology” was too broad an English exception. v3 narrowed the exception: an original term is retained only when the current answer genuinely needs exact source comparison, disambiguation, or retrieval/lookup. “The source is English” is not enough.

v3 also clarified that task recap dimensions such as background, goal, action, result, gap, and next step are logical dimensions, not mandatory headings or a fixed seven-part template.

Independent review returned PASS and recommended real Project regression rather than further global-rule design.

## 5. Real AI Research Stack regression

The AI Research Stack Project was used as the first real regression target.

A new Section 0 was added to its Project instructions as a user-reading bridge. The rest of the governance instructions were initially left semantically unchanged.

The next answer improved materially:

- the opening difference between `workflow-core 0.4` and planned `0.5` was explained in natural Chinese;
- many concepts became Chinese: core responsibility, specialist capability, environment judgment, alternate route, automatic downgrade, evidence strength, artifact identity, authorization boundary;
- simple prose became more continuous.

However, ordinary English leakage still remained, including:

- `source-of-truth`
- `specialist routing`
- `shell/PATH`
- `command not found`
- `fallback`
- “Bridge routing”

At the same time, retaining exact names such as `workflow-core 0.4/0.5`, Codex, Python, R, Node, XeLaTeX, Chromium, Bridge Kit, Reviewed Handoff, W1–W5, and `PATH` was reasonable.

This real regression showed that the bridge is effective but not sufficient by itself.

## 6. v4 — current Planner direction

The current Planner hypothesis is that the remaining leakage has a source-side cause:

- Section 0 requests a Chinese user-reading layer;
- Sections 1–18 still contain many ordinary English engineering concepts;
- those Project instructions are strong local context and continue to provide English lexical patterns.

The proposed architecture is therefore three-layered:

### A. User-reading layer

The Project's leading output section defines how the final explanatory answer should read.

Before sending the answer, explanatory prose should be rewritten into this layer rather than directly reusing wording from Project rules, logs, tables, or sources.

### B. Governance layer

The existing Project governance remains semantically unchanged, but ordinary English engineering/management/process vocabulary may be normalized into Chinese where exact English is not needed for lookup or execution.

This is a language-only refactor, not a governance redesign.

### C. Exact machine layer

Formal names and exact identifiers remain unchanged when precision matters, including repository/file names, paths, commands, fields, state values, fixed machine blocks, formal role/mechanism names, and versioned product/Skill names.

## 7. Important non-goals

The current work does **not** authorize:

- creating the `project-instructions-editor` Skill;
- adding a Skill directory;
- adding `agents/openai.yaml` or trigger evals;
- adding README standalone-Skill cards;
- changing repository or standalone-Skill versions;
- changing Marketplace topology;
- publishing or installing anything;
- introducing an English-word counter, paragraph counter, formula counter, linter service, daemon, state machine, or external checker.

The next step is independent Critic review of the current Planner architecture. A later user instruction will decide when the standalone Skill itself should be designed or implemented.

## 8. Related source

Maintenance inbox:

`docs/skill-todos/project-instructions-editor.md`

Current Planner proposal:

`docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_V4_PLANNER_PROPOSAL_2026-10-01.md`
