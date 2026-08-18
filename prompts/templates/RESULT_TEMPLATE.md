# Result 000 Short Task

status: EXECUTED_UNAUDITED
self_assessed_status: completed

## Execution Summary

Briefly state what was completed, what was not completed, and whether the task
goal appears satisfied from the executor perspective.

## Files Read

- `path/to/file.md`: purpose and key finding.

## Files Modified

- `path/to/file.py`: change summary.

If no files were modified, write `none`.

## Commands Run

```bash
command
```

- purpose:
- result:
- exit_status:

If no commands were run, write `none`.

## Test Results

- test_or_validation:
- result:
- evidence:

If no tests were run, explain why.

## Artifact Paths

- `results/000_short_task/MANIFEST.md`: artifact index linking task, result,
  review, and generated files.
- `results/000_short_task/path/to/artifact`: purpose and generation method.

If no additional file artifacts were generated, write `none`.

## Diff Summary

Summarize added, modified, and deleted files. If the target is not a git
repository, say so.

## Claims

Use one auditable claim per line:

- `claim.structure_checked`: The target directory structure was inspected.
- `claim.tests_passed`: The listed validation command exited 0.

Do not use domain-specific claim names unless the task defines them.

## Failure Information

Record failed commands, error messages, root cause if known, and incomplete
items. If no failure occurred, write `none`.

## Incomplete Items

- item:
- reason:
- required_next_state:

If none, write `none`.

## Human Approval Needed

List actions that require human approval before continuing. If none, write
`none`.

## Git Commit And Push

- auto_git_commit:
- commit_executed:
- commit_sha:
- auto_git_push:
- push_executed:
- remote:
- reason_if_not_executed:

Executors should not claim final audited promotion unless the task explicitly
authorizes them to commit/push without a separate audit.

## Self-Assessed Status

The executor may write one of:

- `completed`
- `partial`
- `blocked`
- `failed`

This is executor self-assessment only. It is not an audit decision and does not
replace `review.md` or `controller_report.md`.
