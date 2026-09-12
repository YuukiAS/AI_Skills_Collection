# Reviewed Handoff Request — 053_clear_writing_release_quality_hardening

## Objective

Complete the release-quality hardening for the existing `writing-style` production plugin, displayed to users as `Clear Writing`.

The highest completion contract is:

```text
docs/goals/053_CLEAR_WRITING_RELEASE_QUALITY_HARDENING_GOAL.md
```

This bootstrap step only initializes the Reviewed Handoff task and hands planning to the Scheduled GPT Planner. It is not an implementation pass, product PASS, release PASS, or user artifact acceptance.

The product target is a compatible `Clear Writing` release that preserves the useful 051 long-form Chinese rewrite quality and the 0.2 structure/boundary improvements, while closing the current observed failures: raw wiki/HTML/template leakage, fenced `text` formula degradation, operator/subscript/exponent loss, table/render regressions, non-requested Traditional Chinese output, ordinary-English scaffolding, and reader-visible workflow/provenance/audit voice.

## User-provided inputs

- Canonical Goal:
  `docs/goals/053_CLEAR_WRITING_RELEASE_QUALITY_HARDENING_GOAL.md`
- Exact task key:
  `053_clear_writing_release_quality_hardening`
- Exact branch:
  `reviewed/053_clear_writing_release_quality_hardening`
- Exact task-owned worktree:
  `/tmp/ai-skills-053-clear-writing-release-quality`
- Current startup source of truth:
  `origin/main` fetched on 2026-09-12; `origin/main` and the remote 053 branch both pointed to `2c731faf9571398f09b2554bd37d3c8836dd6154` when this task was initialized.
- Current formal plugin identity:
  slug `writing-style`, displayName `Clear Writing`, version `0.2`.
- Expected repo-local private diagnostic locators from the Goal:
  `private/exports/clear-writing-0.2-deep-research-diagnostic/`
  and
  `private/exports/051_writing_style_rebuild/gate4-full-report/`.

## User constraints

- Default user-facing narrative is Simplified Chinese.
- The Goal file is the highest completion contract. No bootstrap, Plan, commit, test, handoff, CI run, review, smoke, or partial gate may override it.
- First enter a Planner-owned state and let the existing `053 Clear Writing Planner Reviewer Watch` freeze the bounded Plan before Executor changes production behavior.
- Planner must read and apply the Goal's Gate 0 requirements, including current `main/AGENTS.md`, `TODO.md`, `docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md`, `docs/plugin-todos/writing-style.md`, current `scientific-rewrite` / `chinese-prose` / `writing-fidelity` source and focused tests, 051 Gate 4 historical evidence, 052 Plan/result/review/Text Review/regression evidence, and repo-private 0.2 diagnostics/comparison evidence when available.
- Planner must freeze each observed failure's owner layer, known-regression gate, exactly 2 public-safe fresh holdouts, final artifact acceptance path, paid-review boundary, release/version decision, production smoke, GPT Reviewer handoff, and latest-main integration semantics.
- Required maintenance routing for any production behavior change:
  `workflow-core` for process,
  `ai-skills-core` as maintenance companion,
  `writing-style` / `Clear Writing` as domain owner.
- Keep 051 as historical `STOPPED / NOT_RELEASED`; do not rewrite 051 history or consume 051 budget/state.
- Keep 052 as completed history; do not use 052 PASS to dismiss the newly observed artifact failures.
- Do not create a new top-level skill, plugin, schema, state, role, ledger, renderer, provider path, or broad source-markup postprocessor unless the frozen Plan explicitly proves it is necessary and within the Goal.
- The user has upfront-authorized the exact 053 scope listed in the Goal: exact branch/worktree, canonical candidate replay, bounded use of the same Deep Research private artifact, exactly 2 public-safe fresh holdouts, exactly 1 final `gpt-5.6-terra` Text Review with `store=false`, automatic paid retry `0`, worst-case `<= USD 0.25`, required zero-paid CI, deterministic render QA, bounded live `writing-style@yuukias-ai-skills` production install/upgrade smoke with restoration, and final user `ACCEPT` followed by conflict-free latest-main integration and non-force push.
- Do not ask the user again for routine branch/worktree, same-provider/private-scope, CI, production smoke, push, merge, candidate cache, or same-scope replay questions.
- Ask again only for genuinely new private data, provider/credential scope, paid-call count or cost, live-global target, destructive Git/remote mutation, or final artifact `ACCEPT / REJECT`.
- If the current run must stop before all Goal gates are complete, report `PARTIAL_PROGRESS`, commit and push exact task branch if there are task-owned tracked changes, verify the remote task branch, and leave `CURRENT.next_action` truthful.
