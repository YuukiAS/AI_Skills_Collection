---
name: codex-workflow-protocol
description: Use for complex Codex tasks that require source-of-truth discovery, phased execution, gate-driven completion, verification, failure escalation, commit/release checks, live-state supervision, or honest final status reporting.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-03
profile_tags:
  - global
  - workflow
  - codex
recommended_scope: global
---
# Codex Workflow Protocol

## Trigger Boundary

Use this skill for complex Codex tasks, including research code, training pipelines, data processing, LaTeX/PDF artifacts, HPC/Slurm/tmux debugging, GitHub issue fixes, release/commit preparation, long-running jobs, sub-agent delegation, or any task where correctness depends on evidence beyond a single command.

Do not use this skill for trivial single-command answers, simple wording changes, casual explanations, or one-off facts unless the user explicitly asks for workflow-level execution.

## Non-Negotiable Rule

Do not claim completion without concrete evidence from the relevant source-of-truth, gate, test, metric, rendered artifact, live state, or final output.

Smoke tests, dryruns, preflights, successful compilation, file existence, job submission, HTTP 200, or a child-agent launch are intermediate evidence only. They are not final completion unless the user explicitly asked only for that intermediate check.

## Skill Hierarchy

This is a global workflow skill. It defines process only.

Domain-specific skills add domain knowledge and domain validation requirements, for example Bayesian priors and convergence diagnostics, medical imaging registration baselines, or CMR phenotype QC.

Project-specific skills add repo-local paths, scripts, output contracts, field IDs, docs architecture, and local validation commands.

Domain/project skills may add stricter gates, but must not weaken this global workflow protocol.

## Workflow

1. Source-of-truth discovery.
2. Exploration.
3. Implementation or execution.
4. Verification.
5. Report.

## Source-of-truth discovery

Before editing or executing a complex task, identify the source-of-truth files and states:

- repo `AGENTS.md`;
- installed `.agents/skills/**/SKILL.md` matching the task;
- user-specified prompt/task/TODO/plan;
- current `git status --short --branch`;
- gate/status/metric files such as `validation_summary.json`, Slurm logs, CI output, rendered artifact paths, production build output, or issue comments;
- relevant code, tests, configs, scripts, docs, and previous result files.

If source-of-truth files conflict, report the contradiction before implementation. Do not silently choose one.

## Gate-driven completion

A task is complete only when its acceptance criteria are met. If a workflow has a gate file, validation summary, metric target, rendered artifact, hosted page, live daemon state, or schema contract, that is the completion criterion.

## Failure escalation

If a simple method fails or gives weak results, escalate to the next stronger method unless that violates user constraints or requires approval. Do not stop at baseline failure, smoke failure, or poor metric without either trying the stronger method or reporting a precise blocked state.

## Verification and commit/release boundary

For code, release, commit, issue-fix, or framework work, report exact commands, test results, static checks, staged changes, dirty tree ownership, and final git state. Do not commit or push unless the user explicitly allows it.

## Live-state and delegation supervision

For tmux, Slurm, watchdog, tunnels, long-running jobs, frontend previews, daemon processes, and sub-agents, starting the process is not completion. Verify live process/job/log/status/client-visible behavior and distinguish stale artifacts from current state.

## Final status vocabulary

Use explicit final status:

- `complete`: all acceptance criteria met and verified.
- `partial_complete`: useful work exists, but some acceptance criteria remain unmet.
- `qa_failed`: an artifact exists but fails quality, validation, rendering, metric, or fidelity checks.
- `blocked`: external state, permission, dependency, or user decision is required.
- `blocked_target_not_met`: the target cannot be met under current constraints without unacceptable compromise.

## References

- Read `references/task-template.md` when the user asks for a reusable Codex task prompt or when starting a large complex task.
- Read `references/verification-matrix.md` for code, release, commit, PR, issue, or artifact verification.
- Read `references/live-state-delegation.md` for tmux, Slurm, watchdog, tunnel, daemon, or sub-agent tasks.
- Read `references/escalation-rules.md` when a simple method fails or a baseline gives weak results.
