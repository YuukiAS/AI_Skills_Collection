# Artifact Manifest <task_key>

task: `prompts/tasks/<task_key>.md`
result: `results/<task_key>/result.md`
review: `results/<task_key>/review.md`
controller_report: `results/<task_key>/controller_report.md`  # controller tasks only

## Summary

Briefly state what this artifact directory contains and why it was produced.

## Artifacts

- `results/<task_key>/path/to/artifact`：用途、生成命令或来源、是否需要后续复盘。
- `results/<task_key>/subagents/executor_prompt.md`：controller task fallback executor prompt.
- `results/<task_key>/subagents/auditor_prompt.md`：controller task fallback auditor prompt.

## Reproduction

```bash
# command used to generate or verify the artifacts
```

## Notes

Record caveats, missing files, or follow-up checks.
