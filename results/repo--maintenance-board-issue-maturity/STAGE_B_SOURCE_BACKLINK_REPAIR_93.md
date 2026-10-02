# Stage B Source Backlink Repair for Issue #93

Task: `repo--maintenance-board-issue-maturity`
Main repair commit: `56707e06117e91a5b55e7b080f7d186b0695ab1b`

## Source truth

Live Issue #93 identifies its tracking source as:

```text
docs/skill-todos/project-instructions-editor.md
```

Latest main already had a file-level locator:

```text
tracking: #93
```

The deterministic metadata audit consumes entry-level locators under `###`
canonical TODO entries. The four active entries in this file all belong to the
same standalone-Skill design maturity work tracked by Issue #93.

## Locator-only repair

The repair added `tracking: #93` under exactly these four active entries:

- `Shared Project instructions can become scope-imbalanced and bloated after a local addition request`
- `Follow-up review: Project instructions need semantic prioritization, not equal-detail accumulation`
- `Unnecessary English and copied workflow-contract detail waste the Project-instruction character budget`
- `Live Project editing must use the actual setting, Project history, and canonical repo together`

No status, source, evidence, problem, project-specific context, candidate action,
maturity, design conclusion, Issue title/body/state, or taxonomy label was
changed by this locator repair.

## Project sync

Issue #93 had already left a pending Project sync note in its body. The current
Project-capable maintenance action mechanically applied it:

```text
Project = AI Skills Maintenance
Status = DOING
Area = standalone-skill
```

Live audit readback after the repair confirms:

```text
METADATA_AUDIT.ok = true
METADATA_AUDIT.violation_count = 0
#93 Project Status = DOING
#93 Project Area = standalone-skill
#93 tracking_sources = 4 entry-level locators
```
