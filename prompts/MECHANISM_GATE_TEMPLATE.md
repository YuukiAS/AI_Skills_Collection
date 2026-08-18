# Mechanism Gate Template

Use this file as a generic evidence-gate pattern. Project-specific repositories
should define their own domain gates in `AGENTS.md`, project rules, or skills,
then reference those gates from task frontmatter.

## Gate Name

`<gate-name>`

## Mechanism Class

`<bugfix | feature | refactor | documentation | release | audit | experiment | other>`

## Completion Definition

- What user-visible or repository-visible behavior must change?
- What files, commands, tests, or artifacts prove the change?
- What must remain unchanged?

## Forbidden Substitutes

- Workarounds that look similar but do not satisfy the goal.
- Cosmetic edits that do not affect the required behavior.
- Evidence from unrelated files, stale logs, or unreviewed self-assessment.

## Required Evidence

- File or diff evidence:
- Command evidence with exit status:
- Test or validation evidence:
- Artifact or manifest evidence:
- Audit/review evidence:

## Promotion Gate

Promotion is allowed only when all required claims are supported by evidence and
the auditor decision is `AUDITED_GO` or the task explicitly waives review.

## Failure Escalation Policy

- What can the execution controller try within this task?
- What must stop and return `NEEDS_GPT_PLANNER`?
- What requires human approval?
