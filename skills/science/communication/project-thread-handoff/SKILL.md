---
name: project-thread-handoff
description: Use only after explicit Skill selection in an existing long project thread to produce one continuation prompt for a new thread; do not use for ordinary summaries, status checks, brainstorming, or general project continuation.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: false
executes_code: false
secrets_needed: []
last_reviewed: 2026-09-21
profile_tags: []
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
metadata:
  skill-author: AI Skills Collection maintainers
---
# Project Thread Handoff

Use this skill only after the user explicitly invokes the installed Project Thread Handoff Skill from the current product surface. Do not trigger it for an ordinary request to summarize, continue, explain what happened, or define handoff.

## Goal

Produce exactly one initialization prompt that the user can paste as the first message of a new thread. The prompt should carry only the minimum information needed for the next agent to continue the current long-running project without asking the user to re-explain the thread.

## Workflow

1. Read the current thread context already available in the conversation. Do not ask the user to paste the full history again.
2. Identify the current project, the user's latest continuation goal, and the latest explicit user or frozen decisions.
3. Separate authority types:
   - User decisions and frozen task requirements determine intent, scope, naming, route choices, and next action.
   - Repositories, artifacts, reports, and generated outputs remain the authority for code, experiments, numeric results, and runtime facts.
   - Later assistant brainstorming does not override an earlier explicit user decision unless the user accepted it.
4. Preserve thread-only deltas only when they change decision semantics, such as an updated research direction, naming choice, next step, or unresolved question that has not yet been written into canonical sources.
5. Reduce stale or superseded exploration. Keep a rejected route only as a short recurrence guard when it is likely to be accidentally revived.
6. Prefer locators over copied detail for facts that the next thread can recover from canonical sources. Include exact paths, refs, commits, branches, or artifacts only when they are known from the thread; never invent unknown paths or SHAs.
7. Resolve entity roles from the current thread. For example, if a project uses one named item as data or a data source, do not restate it as the active method unless the latest user decision says so.
8. Output one self-contained prompt and stop. Do not ask for confirmation, offer multiple drafts, write files, create a new thread, or modify a repository.

## Output Shape

The output must be a single prompt addressed to the next thread. Use natural language and adapt the structure to the project, but include:

- current project and continuation objective;
- latest effective decisions, including thread-only deltas;
- immediate next action;
- canonical source recovery guidance and locators;
- entity-role clarifications needed to prevent known confusion;
- active hypotheses, open questions, or recurrence guards only when they affect the next step.

Keep the prompt concise. A typical Chinese research handoff is about 800-1800 Chinese characters, with about 2500 characters as a soft ceiling unless exact unresolved constraints, formulas, or prompts are necessary.

## Boundaries

- Explicit-only: do not run from implicit routing or ordinary project-summary phrasing.
- ChatGPT normal entry is the formal Skill selection, mention, or invocation entry exposed by the user's current product surface; do not require a specific `$`, `@`, or `/` syntax.
- No repository writes, no state database, no history store, no browser automation, no MCP dependency, and no Bridge Kit dependency.
- Do not turn project locators into claims that the current thread has verified the latest code or experiment state.
