---
name: experiment-execution
description: Plan, run, monitor, interpret, and reproduce computational or scientific experiments, including run setup, metric tracking, statistical interpretation, failure triage, and reproducibility checks.
status: active
provenance: external-adapted
source_repo_url: https://github.com/Imbad0202/experiment-agent
source_path: .
source_ref: e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651
source_imported_at: 2026-07-09
source_license: MIT
source_note: Distilled from experiment-agent and existing codex-workflow-protocol verification gates.
trusted: false
requires_network: false
writes_files: true
executes_code: true
secrets_needed:
last_reviewed: 2026-07-09
profile_tags:
  - workflow
  - research
recommended_scope: project
metadata:
  skill-author: AI Skills Collection maintainers with recorded upstream sources
---
# Experiment Execution

Use this when a task moves from paper planning into executable experiments, metrics, or reproducibility checks.

## Workflow

1. Define hypothesis, baseline, treatment, dataset, metric, resource budget, and success criteria.
2. Record exact run configuration before execution: code revision, command, environment, seeds, data split, and output directory.
3. Prefer dry runs or small smoke tests before full runs.
4. Monitor logs and intermediate artifacts. Starting a run is not completion.
5. Interpret results with uncertainty:
   - compare against baseline;
   - check variance or confidence intervals;
   - inspect failure cases;
   - avoid overclaiming from a single run.
6. Package reproducibility evidence: command, config, artifact path, metric table, and known caveats.

## Failure Handling

- If a run fails, preserve the error, config, and last valid artifact.
- If results are weak, report whether the issue is implementation, data, metric mismatch, or hypothesis weakness.
- If a method requires expensive compute, state the smallest meaningful validation first.

## Hand Off

- Use `statistical-analysis` or `bayesian-ppl-diagnostics` for model-level statistical reasoning.
- Use `scientific-visualization` for paper-ready result figures.
- Use `paper-workflow-orchestrator` when results change the manuscript claim.
