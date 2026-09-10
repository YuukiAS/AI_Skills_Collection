# Reviewed Handoff Request — 052_writing_style_reader_facing_generalization_closure

## Objective

Complete the final reader-facing generalization closure for the existing
`writing-style` heavy Chinese scientific/technical rewrite path.

052 has exactly two residual production targets:

- standalone reader-facing rewrites must not leak source-process framing such
  as "原文指出", "原文同时提到", "根据给定材料", "源文", or "这里保留原文",
  unless the user explicitly asks for source comparison, editing commentary,
  peer review, provenance, or audit;
- Text Review plaintext packets must contain only real candidate text. Workflow
  wrapper labels such as Gate, known regression, holdout, recovery, candidate,
  Planner, Reviewer, Executor, task id, commit/hash, or run id belong only in
  manifest/metadata. If a reviewer only hits wrapper text that is absent from
  candidate bytes, classify it as `REVIEW_PACKET_CONSTRUCTION_FAILURE`, not a
  writing-style product failure.

051 history must remain unchanged:

```text
STOPPED / NOT_RELEASED / FINAL_TEXT_REVIEW_REVISE
```

Do not rewrite 051 into PASS, and do not consume 051 holdout/review budget.

## User-provided inputs

- Goal objective file:
  `/overflow/htzhu/mingcheng_new/.codex-homes/Longleaf_Connection_Bridge/attachments/640f4025-178d-4525-80e3-f8b9d5b0f3ac/goal-objective.md`
- Authorized task branch:
  `reviewed/052_writing_style_reader_facing_generalization_closure`
- Authorized task-owned temporary worktree:
  `/tmp/ai-skills-052-20260910`
- Implementation starting point to selectively port:
  `2690de2cbc3d4ffb0741ecb80297a569647051f2`

## User constraints

- Start from latest `origin/main`; fetch latest main and 051 branch.
- Current main already owns candidate replay governance, authorization dedup,
  state-refresh rules, holdout completeness preflight, paid-review recovery
  policy, and Bridge Kit 0.7.4 consumer pin; do not re-create those mechanisms.
- Selectively port only 051 production changes that still satisfy 052.
- Do not copy 051 `CURRENT`, `RESULT`, `FINAL_REPORT`, private artifacts, or
  paid-review state.
- Do not create new replay/runtime/Bridge/Host Policy mechanisms.
- Freeze exactly 2 fresh public-safe holdouts before first holdout generation,
  after production candidate freeze.
- Paid Text Review budget for 052: at most 1 call, worst-case at most USD 0.25,
  automatic retry 0, only after local/holdout gates pass.
- Normal completion requires all gates from the objective, including full CI,
  production install/upgrade smoke, GPT Reviewer, final user ACCEPT, and
  integration to latest `main`.
