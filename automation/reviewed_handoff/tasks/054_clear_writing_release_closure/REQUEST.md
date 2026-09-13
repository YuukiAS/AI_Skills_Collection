# Reviewed Handoff Request - 054_clear_writing_release_closure

## Objective

Complete the release closure for the existing `writing-style` production plugin, displayed to users as `Clear Writing`.

The highest completion contract is:

```text
docs/goals/054_CLEAR_WRITING_RELEASE_CLOSURE_GOAL.md
```

This bootstrap step only initializes the Reviewed Handoff task and hands planning to the Scheduled GPT Planner. It is not an implementation pass, product PASS, release PASS, Text Review PASS, production smoke PASS, or user artifact acceptance.

054 must close Clear Writing from the current evidence-bearing but unreleased state into a production-validated release for real Chinese or Chinese-dominant scientific and technical rewriting. The new product issue to plan around is semantic reader relevance / information selection: source facts are not automatically reader-facing facts, and irrelevant source packaging, webpage metadata, maintenance labels, duplicate links, and non-useful attached foreign aliases should not be promoted into independent Chinese prose. This rule must preserve necessary formal identities, names, citations, formulas, datasets, methods, APIs, authorship, source fidelity, and reproducibility details.

## User-provided inputs

- Canonical Goal:
  `docs/goals/054_CLEAR_WRITING_RELEASE_CLOSURE_GOAL.md`
- Exact task key:
  `054_clear_writing_release_closure`
- Exact branch:
  `reviewed/054_clear_writing_release_closure`
- Exact task-owned worktree:
  `/tmp/ai-skills-054-clear-writing-release-closure`
- Current startup source of truth:
  `origin` fetched on 2026-09-13 before this task initialization.
- Current 054 bootstrap commit:
  `5003eb8251f496b38b45bf620700b1e6b83ef674`
- Then-current `origin/main` at initialization:
  `8da77f419c3166f81ea97469a6f73ae77d89334e`
- Required inherited 053 production candidate:
  `d4570c764326cd10b63eae5e605cc8ff885bd7f2`
- Historical evidence families to read, not rewrite:
  `results/051*`, `results/052_writing_style_reader_facing_generalization_closure/`,
  `results/053_clear_writing_release_quality_hardening/`, and the matching
  `automation/reviewed_handoff/tasks/051*`, `052*`, and `053*` task state when present.

## User constraints

- Default user-facing narrative is Simplified Chinese.
- The Goal file is the highest completion contract. No bootstrap, Plan, commit, test, handoff, CI run, review, smoke, or partial gate may override it.
- First enter a Planner-owned state and let the existing `054 Clear Writing Planner Reviewer Watch` freeze the bounded Plan before Executor changes production behavior.
- Keep 053 as `NOT_RELEASED / evidence-bearing / fresh batch FAIL`. Do not rewrite 053 as PASS, do not rescore 053 H1/H2 as 054 fresh holdouts, and do not claim the failed 053 batch can be repaired into unseen PASS.
- Inherit 053 frozen production candidate `d4570c764326cd10b63eae5e605cc8ff885bd7f2`, but rerun required known regressions on the 054 final candidate. Predecessor evidence is baseline evidence only.
- Do not redo the 051/052/053 heavy rewrite architecture. Keep the route shape:
  `writing-style -> scientific-rewrite -> Meaning Map -> Reader Plan -> chinese-prose REALIZE_MEANING -> assembly -> writing-fidelity / semantic audit -> bounded repair`.
- Do not modify Bridge Kit for this task. Bridge Kit remains responsible for general capability; repo-specific plugin refinement, evaluation, QA, release, and closure stay in AI_Skills_Collection.
- Candidate replay must use the already selected OpenAI official local marketplace / cachebuster / reinstall / fresh-session route. Do not reopen undocumented hot-load research.
- Required maintenance routing for any production behavior change:
  `workflow-core` for process,
  `ai-skills-core` as maintenance companion,
  `writing-style` / `Clear Writing` as domain owner.
- The user has upfront-authorized the exact 054 scope listed in the Goal: exact branch/worktree ordinary commit/fetch/non-force push; reading and using 051/052/053 evidence; the same private Deep Research source through the current existing Codex/OpenAI provider, same account/CODEX_HOME, same writing-validation purpose, at most 2 candidate replays; exactly 3 public-safe fresh holdouts; exactly 1 final `gpt-5.6-terra` Text Review with `store=false`, automatic retry `0`, worst-case `<= USD 0.25`; required local tests, render QA, zero-paid CI; bounded production `writing-style@yuukias-ai-skills` install/upgrade smoke with snapshot and restore; and final user `ACCEPT` followed by conflict-free latest-main integration and non-force push.
- Do not ask the user again for routine branch/worktree, same-provider/private-scope, candidate replay, CI, production smoke, push, or same-scope workflow questions.
- Ask again only for genuinely new private data, provider/credential scope, paid-call count or cost, live-global target, destructive Git/remote mutation, or final artifact `ACCEPT / REJECT`.
- Before any fresh holdout, the complete known/stress matrix in the Goal must PASS on the 054 final implementation candidate.
- The fresh batch must be exactly 3 public-safe holdouts frozen once as a complete batch. All three must PASS; no adaptive replacement, H4, cherry-picking, or retry-until-PASS.
- The complete private Deep Research artifact must be regenerated directly by the 054 final candidate and QA'd end to end as Markdown and PDF. Do not show the user half-finished artifacts with known blockers.
- Do not let new reader-relevance fixes regress formulas, markup cleanup, mathematical symbols, tables, Simplified Chinese, source fidelity, Deep Research long-form quality, compatibility routes, or normal production routing.
- Only after known/stress matrix, complete Deep Research, 3 fresh holdouts, real Markdown/PDF QA, Terra, full CI, production smoke, and GPT Reviewer all PASS may the task generate the final dossier / Deep Research PDF and ask the user for `ACCEPT` or `REJECT`.
- Only after the user explicitly `ACCEPT`s may the task integrate latest `main`, push, and verify released identity.
- If the current run must stop before all Goal gates are complete, report partial progress truthfully, commit and push only task-owned tracked initialization or implementation changes within the authorized branch, verify the remote task branch when pushed, and leave `CURRENT.next_action` truthful.
