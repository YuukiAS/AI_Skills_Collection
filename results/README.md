# Results Directory

`results/` stores file artifacts produced by Codex tasks, scripts, audits, or experiments.

Use the same task key as `prompts/tasks/<task_key>.md`:

```text
prompts/tasks/<task_key>.md
results/<task_key>/result.md
results/<task_key>/review.md
results/<task_key>/controller_report.md   # controller tasks
results/<task_key>/MANIFEST.md
```

`task_key` should be `<id>_<short_slug>`, with `short_slug` limited to 1-3 words joined by underscores.

`results/<task_key>/result.md` is the execution report and evidence index. Keep large logs, CSV/JSON files, figures, archives, long reports, and intermediate outputs under `results/<task_key>/`, then list them in `results/<task_key>/MANIFEST.md` and the result report.

For controller tasks, `results/<task_key>/controller_report.md` is the
execution-controller summary. It must list executor/auditor prompt, result, and
review paths; session/command/log evidence; audited decision; promotion
decision; automatic commit/push status; incomplete items; and whether GPT
planner is needed.

Do not mix artifacts from different tasks in the same `results/<task_key>/` directory.
