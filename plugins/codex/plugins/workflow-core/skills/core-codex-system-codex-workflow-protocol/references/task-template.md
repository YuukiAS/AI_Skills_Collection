# Reusable Codex Task Template

Copy this template for complex research code, training pipelines, data processing, LaTeX/PDF, HPC debugging, GitHub issue fixes, documentation sites, and release work.

```markdown
---
task_key: <id>_<short_slug>
mode: explore_implement_verify_report
scope:
  repo_or_workspace: <absolute path>
  include:
    - <paths/files to include>
  exclude:
    - <paths/files to exclude>
allowed_actions:
  - read
  - edit:<paths or modules>
  - run_light_tests
  - run_slurm_under_budget:<optional>
  - commit:<yes/no>
forbidden_actions:
  - destructive delete without approval
  - expensive training without approval
  - upload/push without explicit approval
  - touching unrelated dirty files
final_artifact:
  path: <required output/report/result path>
  format: <md/pdf/csv/json/zip/code/commit/etc.>
acceptance_criteria:
  - <machine-checkable condition>
  - <metric/gate/status condition>
  - <artifact existence and QA condition>
escalation_policy:
  if_simple_method_fails: <stronger valid method to try>
  if_baseline_is_weak: <stronger method, larger validation, or blocked_target_not_met>
  if_target_unreachable: report blocked_target_not_met with evidence
---

# Task

<Describe the objective. State whether this requires exploration, implementation, verification, reporting, or all four.>

## Phase 1: Source-of-truth discovery

Codex must first locate and read:

- repo-level `AGENTS.md` or equivalent rules;
- user-specified prompt/task/plan/TODO files;
- current `git status --short --branch` if the target is a git repo;
- source-of-truth gate/status files such as `validation_summary.json`, metrics, logs, Slurm status, CI output, issue comments, or rendered artifact paths;
- relevant code, tests, configs, scripts, docs, and previous result files.

Codex must report contradictions before editing, especially conflicts between user prompt, `AGENTS.md`, TODO, plan registry, gate status, or dirty-tree state.

## Phase 2: Exploration

Codex must inspect the existing implementation, interfaces, commands, and prior artifacts before choosing an approach. It must distinguish discoverable repo truth from user preferences.

## Phase 3: Implementation or execution

Codex must keep changes scoped to the task and avoid unrelated dirty files. If the task is long or compute-heavy, use budgeted tmux/Slurm/sub-agent delegation only with owner, log path, stop condition, and polling plan.

Smoke test, dryrun, preflight, compile success, file existence, job submission, page 200, or child-agent launch is only an intermediate checkpoint. It is not final completion.

If the baseline/simple method fails or gives weak results, Codex must continue with the stronger method named in `escalation_policy`, unless that violates forbidden actions or needs approval.

## Phase 4: Verification

After every modification, Codex must provide concrete verification:

- exact commands run;
- exact status/metric/gate values;
- test result, build result, render result, or live-state evidence;
- final `git status` if applicable;
- artifact paths and whether they are final or intermediate.

If verification cannot run, Codex must say why and give the residual risk.

## Phase 5: Report

Codex must write the requested final artifact or final response. It must include:

- what was done;
- what evidence proves it;
- what was not completed;
- why it was not completed;
- next stronger step or required human decision;
- no unsupported claim of completion.

Use explicit final status:

- `complete`: all acceptance criteria met;
- `partial_complete`: useful work exists but some criteria are not met;
- `qa_failed`: artifact exists but fails QA;
- `blocked`: external input/state is required;
- `blocked_target_not_met`: target cannot be met under current constraints.
```
