# Verification Matrix

Use this checklist for code, release, commit, PR, issue-fix, framework, generated artifact, or docs work.

## Required checks

- Run `git status --short --branch` before and after the task when inside a git repo.
- Identify dirty tree ownership: task-owned files, pre-existing user files, generated files, and unrelated files.
- Inspect the staged diff before any commit. Stage only task-owned changes.
- Run relevant tests. Prefer targeted tests first, then broader tests when risk warrants it.
- Run compile/static/format checks available in the repo.
- Run `git diff --check` before final report or commit.
- When the repo is meant to be generic, scan for forbidden project-specific strings in touched or staged content.
- Validate final artifacts directly: rendered PDF/HTML, schema output, metric file, production build, live status, or client-visible behavior.
- Do not push unless the user explicitly requested push and authentication is available.

## Reporting requirements

Report exact commands, exit status, important output, and any skipped checks.

If tests cannot run, state the exact reason, such as missing dependency, unavailable service, insufficient compute, network restriction, or user approval boundary. Include residual risk and the next strongest validation step.

## Completion boundary

Smoke, dryrun, preflight, compile success, file existence, job submission, and HTTP 200 responses are intermediate checks. They support progress but do not replace final acceptance unless the user explicitly asked only for that intermediate check.
