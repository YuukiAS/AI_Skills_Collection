# Verification Matrix

Use this checklist for complex code, data, document, release, generated artifact, or repository maintenance work.

## Required Checks

- Inspect `git status --short --branch` before and after repository work.
- Identify task-owned files, pre-existing user files, generated files, and unrelated changes.
- Inspect staged diffs before any commit. Stage only task-owned changes.
- Run relevant tests or validators. Prefer targeted checks first, then broader checks when blast radius warrants it.
- Validate final artifacts directly through the specialist-defined gate: schema, render, metric, build, live state, or client-visible behavior.
- Scan touched or staged content for forbidden project-specific strings when producing generic repository assets.
- Do not push, publish, delete user work, or perform expensive/destructive actions unless the user allowed it.

## Reporting Requirements

Report exact commands, exit status, important output, skipped checks, and residual risk. If a check cannot run, state the missing dependency, unavailable service, permission boundary, or required user decision.

## Completion Boundary

Intermediate checks support progress but do not replace acceptance criteria. Completion requires the final gate named by the user, repo, specialist skill, schema, or task plan.
