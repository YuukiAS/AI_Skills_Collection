# Project Scope Authorization Required

Task: `repo--maintenance-board-lifecycle`

Current state:

- GitHub identity: `YuukiAS`
- Repository identity readback: `YuukiAS/AI_Skills_Collection`
- Existing repository labels readback: PASS
- Existing `maintenance-track` label: MISSING
- Existing `maintenance-track` issues: none returned by `gh issue list`
- GitHub Project readback: BLOCKED

Observed command:

```text
gh project list --owner YuukiAS --format json --limit 100
```

Observed result:

```text
error: your authentication token is missing required scopes [read:project]
To request it, run:  gh auth refresh -s read:project
```

An attempted bounded refresh for `project` scope was rejected by Auto-review because it would persistently expand the current GitHub credential scope. No workaround was attempted.

Required user authorization before Project/Issue backfill:

```text
gh auth refresh -h github.com -s project
```

Purpose:

- read whether the private Project `AI Skills Maintenance` already exists;
- create or reconcile that exact Project if needed;
- configure approved fields, views, workflows, and repository link;
- perform issue-only backfill with `maintenance-track`;
- write source `tracking: #N` locators only inside the frozen canonical inbox allowlist.

No Project mutation, Issue backfill, or source locator write has been performed yet.
