---
name: project-thread-handoff
description: Use only after explicit Skill selection to hand off the current project thread or recover a same-Project old thread; do not use for ordinary summaries, status checks, brainstorming, or general continuation.
status: active
version: "0.2"
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

Support two explicit modes:

- Mode A: in the current long project thread, produce exactly one initialization prompt that the user can paste as the first message of a new thread. The prompt should carry only the minimum information needed for the next agent to continue without asking the user to re-explain the thread.
- Mode B: in a new thread within the same ChatGPT Project, recover semantic continuation state from an identifiable old conversation in that same Project, hydrate the current thread, and continue the user's bounded request when the invocation asks to recover and continue.

## Workflow

### Mode A — Current-Thread Handoff

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

### Mode B — Same-Project Old-Thread Recovery

1. Use this mode only when the user explicitly asks to recover a previous or old thread from the same ChatGPT Project. The old thread may be full or unavailable for new messages.
2. Treat title, topic, approximate date, distinctive phrases, project/task clues, and distinctive corrections only as past-chat retrieval or candidate-identification clues. Do not describe them as deterministic conversation database keys, and do not invent any conversation database API.
3. Recover strongly only from identifiable target past-chat provenance exposed by the product surface, such as a target old chat in Sources or Memory Sources, an identifiable source card, a target conversation title/link/locator, or equivalent formal past-chat source metadata.
4. Generic Saved Memory, profile summaries, unsourced semantic recall, remembered context that cannot be attributed to the target conversation, and model prior knowledge are not target-thread authority.
5. Require target-chat backing for route-changing recovered claims: latest user decisions or corrections, frozen or rejected route status, entity roles, thread-only deltas, current open questions, immediate next steps, and user-accepted assistant proposals.
6. If all key continuation decisions have target past-chat backing, output a compact recovered continuation state and continue the user's bounded request in the current new thread. Do not generate a prompt that must be pasted back into the same thread.
7. If recovery is only unsourced or attribution-unverified, label it as limited recovery. Do not turn it into an authoritative decision, thread-only delta, direct quote, exact prompt, formula, or frozen contract. If a missing key decision would change the route, fail closed on that decision after bounded source identification and ask at most one minimal clarification only when needed to continue.
8. Keep the cross-Project boundary strict: Mode B only accepts target same-Project conversation evidence as recovery authority. Project membership alone is not provenance, and Project-external or unattributed context must not be used as recovery authority.
9. Keep canonical facts anchored in current repositories, artifacts, reports, results, and other canonical sources. A conversation plan to do something is not evidence that it was completed.

## Output Shape

For Mode A, output a single prompt addressed to the next thread. Use natural language and adapt the structure to the project, but include:

- current project and continuation objective;
- latest effective decisions, including thread-only deltas;
- immediate next action;
- canonical source recovery guidance and locators;
- entity-role clarifications needed to prevent known confusion;
- active hypotheses, open questions, or recurrence guards only when they affect the next step.

Keep the prompt concise. A typical Chinese research handoff is about 800-1800 Chinese characters, with about 2500 characters as a soft ceiling unless exact unresolved constraints, formulas, or prompts are necessary.

For Mode B with strong recovery, hydrate the current thread with a compact recovered continuation state. Include:

- target old conversation identity at the minimum useful level, such as a title, topic, date, or redacted source locator;
- current objective;
- latest effective decisions and their target-chat-backed status;
- thread-only deltas, entity-role guards, open questions, and immediate next step;
- canonical source recovery guidance for code, experiments, numbers, runtime facts, and reports.

For Mode B with limited recovery, explicitly separate target-chat-backed facts from unsourced recall and state which route-changing decision cannot be verified.

## Legacy Mode A Prompt Shape

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
- No repository writes, no state database, no history store, no transcript exporter, no browser automation or browser extension, no MCP dependency, no external API, and no Bridge Kit dependency.
- No second Recovery Skill, no CURRENT file, no Project-wide full transcript scan, no periodic checkpoint requirement, and no automatic new thread.
- Do not turn project locators into claims that the current thread has verified the latest code or experiment state.
