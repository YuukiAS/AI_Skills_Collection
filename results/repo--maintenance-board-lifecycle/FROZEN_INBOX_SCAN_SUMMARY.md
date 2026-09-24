# Frozen Inbox Scan Summary

Task: `repo--maintenance-board-lifecycle`

This is a pre-backfill scan of the frozen canonical inbox allowlist. It is not
`TODO_COVERAGE.md` and does not replace source `tracking: #N` locators.

Project / Issue backfill is waiting for GitHub `project` scope. No tracking
Issues or source locators have been created yet.

TOTAL_ENTRIES = 101

STATUS_COUNTS =

| Status | Count |
|---|---:|
| `BLOCKED_NEEDS_EVIDENCE` | 6 |
| `CANDIDATE_GENERIC` | 8 |
| `DEFER_AFTER_056_WORKFLOW_CORE` | 2 |
| `DEFER_UNTIL_056_COMPLETE` | 1 |
| `MANUAL_BASELINE_CAPTURED` | 1 |
| `NEW` | 56 |
| `NEW / POST_056_REFINEMENT` | 1 |
| `PROMOTED` | 10 |
| `PROMOTED / RELEASED_IN_5.0.7` | 2 |
| `PROMOTED_BY_045` | 6 |
| `PROMOTE_NOW` | 2 |
| `READY_FOR_PROMOTION` | 3 |
| `READY_FOR_PROMOTION_AFTER_050` | 1 |
| `READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER` | 2 |

BY_FILE =

| Inbox | Entries | Status summary |
|---|---:|---|
| `docs/plugin-todos/workflow-core.md` | 9 | `DEFER_AFTER_056_WORKFLOW_CORE`: 2; `DEFER_UNTIL_056_COMPLETE`: 1; `NEW`: 1; `NEW / POST_056_REFINEMENT`: 1; `PROMOTED / RELEASED_IN_5.0.7`: 2; `PROMOTE_NOW`: 2 |
| `docs/plugin-todos/ai-skills-core.md` | 9 | `PROMOTED`: 9 |
| `docs/plugin-todos/writing-style.md` | 9 | `CANDIDATE_GENERIC`: 2; `MANUAL_BASELINE_CAPTURED`: 1; `NEW`: 5; `READY_FOR_PROMOTION_AFTER_050`: 1 |
| `docs/plugin-todos/research-writing.md` | 9 | `CANDIDATE_GENERIC`: 2; `NEW`: 4; `READY_FOR_PROMOTION`: 3 |
| `docs/plugin-todos/presentations.md` | 27 | `BLOCKED_NEEDS_EVIDENCE`: 1; `CANDIDATE_GENERIC`: 4; `NEW`: 16; `PROMOTED_BY_045`: 6 |
| `docs/plugin-todos/scientific-visualization.md` | 3 | `BLOCKED_NEEDS_EVIDENCE`: 1; `NEW`: 1; `READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER`: 1 |
| `docs/plugin-todos/web-development.md` | 22 | `NEW`: 21; `PROMOTED`: 1 |
| `docs/plugin-todos/statistical-modeling.md` | 6 | `BLOCKED_NEEDS_EVIDENCE`: 1; `NEW`: 4; `READY_FOR_PROMOTION_AFTER_LANGUAGE_LAYER`: 1 |
| `docs/plugin-todos/bioinformatics.md` | 1 | `BLOCKED_NEEDS_EVIDENCE`: 1 |
| `docs/plugin-todos/medical-imaging.md` | 2 | `BLOCKED_NEEDS_EVIDENCE`: 2 |
| `docs/skill-todos/render-chinese-math-pdf.md` | 4 | `NEW`: 4 |
