# Reusable Codex Task Template

Use this template for complex work that needs phased execution and evidence-driven completion.

```markdown
---
task_key: <id>_<short_slug>
mode: discover_plan_execute_verify_report
scope:
  repo_or_workspace: <absolute path>
  include:
    - <paths/files to include>
  exclude:
    - <paths/files to exclude>
allowed_actions:
  - read
  - edit:<paths or modules>
  - run_tests:<scope>
  - delegate:<optional>
  - commit:<yes/no>
forbidden_actions:
  - destructive action without approval
  - expensive or external execution without approval
  - upload/push/publish without explicit approval
  - touching unrelated dirty files
specialist_routing:
  - <domain or artifact type>: <skill or owner>
acceptance_criteria:
  - <machine-checkable condition>
  - <artifact or live-state condition>
  - <quality or fidelity condition>
escalation_policy:
  if_simple_method_fails: <stronger valid method or blocked condition>
  if_target_unreachable: report blocked_target_not_met with evidence
---

# Task

<Describe the objective and final deliverable.>

## Phase 1: Source-of-Truth Discovery

Read user instructions, repo rules, relevant skills, current git state, configs, tests, schemas, prior artifacts, and any live-state evidence.

## Phase 2: Execution Plan

Define task-owned files, specialist routes, acceptance gates, verification commands, and escalation boundaries.

## Phase 3: Implementation or Execution

Make scoped changes or run scoped work. Treat smoke checks, launch events, and intermediate artifacts as progress only.

## Phase 4: Verification

Run the specialist-defined final checks and record exact evidence.

## Phase 5: Report

State what changed, what evidence proves it, what remains incomplete, and which final status applies.
```
