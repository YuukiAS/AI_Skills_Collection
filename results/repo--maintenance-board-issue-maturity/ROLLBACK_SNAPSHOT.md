# Rollback Snapshot

Task: `repo--maintenance-board-issue-maturity`
Stage: Stage A pre-migration snapshot. No v7 taxonomy labels have been created or applied by this task yet.

## Rollback Boundary

- `maintenance-track` is protected and must never be modified, deleted, or redefined by v7.
- Existing Issue rollback may remove only v7 taxonomy labels applied by this task: `triage:*`, `kind:*`, `scope:*`, `area:*`, and `integration:bridge-kit` as applicable.
- Rollback must not reopen/close existing maintenance Issues, change Project Status/Area, edit canonical TODO files, or change `tracking:#N`.
- Pre-v7 repository-level label definitions are not frozen in Stage A because G7 label cutover is forbidden before independent Reviewer PASS. They must be appended from `PRE_CUTOVER_LABEL_DEFINITIONS.json` immediately before any G7 label mutation.

## Pre-Migration Issue Label Memberships

| Issue | State | Project Status | Project Area | Pre-migration labels | Planned v7 labels |
|---:|---|---|---|---|---|
| #4 | OPEN | ADAPTING | repo | `maintenance-track` | `kind:governance, scope:repo-workflow, area:repo` |
| #5 | OPEN | TODO | workflow-core | `maintenance-track` | `kind:governance, scope:cross-repo, area:workflow-core, integration:bridge-kit` |
| #6 | OPEN | TODO | workflow-core | `maintenance-track` | `kind:governance, scope:plugin, area:workflow-core` |
| #7 | OPEN | TODO | workflow-core | `maintenance-track` | `kind:governance, scope:plugin, area:workflow-core` |
| #8 | OPEN | TODO | workflow-core | `maintenance-track` | `kind:enhancement, scope:plugin, area:workflow-core` |
| #9 | OPEN | TODO | workflow-core | `maintenance-track` | `kind:governance, scope:plugin, area:workflow-core` |
| #10 | OPEN | TODO | workflow-core | `maintenance-track` | `kind:governance, scope:plugin, area:workflow-core` |
| #11 | OPEN | TODO | workflow-core | `maintenance-track` | `kind:governance, scope:plugin, area:workflow-core` |
| #12 | OPEN | TODO | writing-style | `maintenance-track` | `kind:enhancement, scope:plugin, area:writing-style` |
| #13 | OPEN | TODO | writing-style | `maintenance-track` | `kind:new-capability, scope:plugin, area:writing-style` |
| #14 | OPEN | TODO | writing-style | `maintenance-track` | `kind:regression, scope:plugin, area:writing-style` |
| #15 | OPEN | TODO | writing-style | `maintenance-track` | `kind:regression, scope:plugin, area:writing-style` |
| #16 | OPEN | TODO | writing-style | `maintenance-track` | `kind:regression, scope:plugin, area:writing-style` |
| #17 | OPEN | TODO | writing-style | `maintenance-track` | `kind:enhancement, scope:plugin, area:writing-style` |
| #18 | OPEN | TODO | writing-style | `maintenance-track` | `kind:enhancement, scope:plugin, area:writing-style` |
| #19 | OPEN | TODO | writing-style | `maintenance-track` | `kind:governance, scope:plugin, area:writing-style` |
| #20 | OPEN | TODO | research-writing | `maintenance-track` | `kind:enhancement, scope:plugin, area:research-writing` |
| #21 | OPEN | TODO | research-writing | `maintenance-track` | `kind:governance, scope:plugin, area:research-writing` |
| #22 | OPEN | TODO | research-writing | `maintenance-track` | `kind:enhancement, scope:plugin, area:research-writing` |
| #23 | OPEN | TODO | research-writing | `maintenance-track` | `kind:enhancement, scope:plugin, area:research-writing` |
| #24 | OPEN | TODO | research-writing | `maintenance-track` | `kind:enhancement, scope:plugin, area:research-writing` |
| #25 | OPEN | TODO | research-writing | `maintenance-track` | `kind:governance, scope:plugin, area:research-writing` |
| #26 | OPEN | TODO | research-writing | `maintenance-track` | `kind:enhancement, scope:plugin, area:research-writing` |
| #27 | OPEN | TODO | research-writing | `maintenance-track` | `kind:enhancement, scope:plugin, area:research-writing` |
| #28 | OPEN | TODO | research-writing | `maintenance-track` | `kind:enhancement, scope:plugin, area:research-writing` |
| #29 | OPEN | TODO | presentations | `maintenance-track` | `kind:governance, scope:plugin, area:presentations` |
| #30 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #31 | OPEN | TODO | presentations | `maintenance-track` | `kind:regression, scope:plugin, area:presentations` |
| #32 | OPEN | TODO | presentations | `maintenance-track` | `kind:regression, scope:plugin, area:presentations` |
| #33 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #34 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #35 | OPEN | TODO | presentations | `maintenance-track` | `kind:regression, scope:plugin, area:presentations` |
| #36 | OPEN | TODO | presentations | `maintenance-track` | `kind:regression, scope:plugin, area:presentations` |
| #37 | OPEN | TODO | presentations | `maintenance-track` | `kind:regression, scope:plugin, area:presentations` |
| #38 | OPEN | TODO | presentations | `maintenance-track` | `kind:regression, scope:plugin, area:presentations` |
| #39 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #40 | OPEN | TODO | presentations | `maintenance-track` | `kind:regression, scope:plugin, area:presentations` |
| #41 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #42 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #43 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #44 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #45 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #46 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #47 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #48 | OPEN | TODO | presentations | `maintenance-track` | `kind:enhancement, scope:plugin, area:presentations` |
| #49 | OPEN | TODO | scientific-visualization | `maintenance-track` | `kind:enhancement, scope:plugin, area:scientific-visualization` |
| #50 | OPEN | TODO | scientific-visualization | `maintenance-track` | `kind:regression, scope:plugin, area:scientific-visualization` |
| #51 | OPEN | TODO | scientific-visualization | `maintenance-track` | `kind:enhancement, scope:plugin, area:scientific-visualization` |
| #52 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #53 | CLOSED | DONE | web-development | `maintenance-track` | `kind:regression, scope:plugin, area:web-development` |
| #54 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #55 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #56 | CLOSED | DONE | web-development | `maintenance-track` | `kind:regression, scope:plugin, area:web-development` |
| #57 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #58 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #59 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #60 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #61 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #62 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #63 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #64 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #65 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #66 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #67 | CLOSED | DONE | web-development | `maintenance-track` | `kind:regression, scope:plugin, area:web-development` |
| #68 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #69 | CLOSED | DONE | web-development | `maintenance-track` | `kind:regression, scope:plugin, area:web-development` |
| #70 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #71 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #72 | CLOSED | DONE | web-development | `maintenance-track` | `kind:enhancement, scope:plugin, area:web-development` |
| #73 | OPEN | TODO | statistical-modeling | `maintenance-track` | `kind:enhancement, scope:plugin, area:statistical-modeling` |
| #74 | OPEN | TODO | statistical-modeling | `maintenance-track` | `kind:enhancement, scope:plugin, area:statistical-modeling` |
| #75 | OPEN | TODO | statistical-modeling | `maintenance-track` | `kind:enhancement, scope:plugin, area:statistical-modeling` |
| #76 | OPEN | TODO | statistical-modeling | `maintenance-track` | `kind:enhancement, scope:plugin, area:statistical-modeling` |
| #77 | OPEN | TODO | statistical-modeling | `maintenance-track` | `kind:enhancement, scope:plugin, area:statistical-modeling` |
| #78 | OPEN | TODO | statistical-modeling | `maintenance-track` | `kind:enhancement, scope:plugin, area:statistical-modeling` |
| #79 | OPEN | TODO | medical-imaging | `maintenance-track` | `kind:enhancement, scope:plugin, area:medical-imaging` |
| #80 | CLOSED | DONE | standalone-skill | `maintenance-track` | `kind:regression, scope:standalone-skill, area:standalone-skill` |
| #81 | CLOSED | DONE | standalone-skill | `maintenance-track` | `kind:regression, scope:standalone-skill, area:standalone-skill` |
| #82 | CLOSED | DONE | standalone-skill | `maintenance-track` | `kind:regression, scope:standalone-skill, area:standalone-skill` |
| #83 | OPEN | TODO | standalone-skill | `maintenance-track` | `kind:enhancement, scope:standalone-skill, area:standalone-skill` |
| #84 | OPEN | TODO | bioinformatics | `maintenance-track` | `kind:enhancement, scope:plugin, area:bioinformatics` |
| #85 | OPEN | TODO | medical-imaging | `maintenance-track` | `kind:enhancement, scope:plugin, area:medical-imaging` |
| #86 | CLOSED | DONE | ai-skills-core | `maintenance-track` | `kind:new-capability, scope:plugin, area:ai-skills-core` |
| #89 | OPEN | DOING | web-development | `maintenance-track` | `kind:new-capability, scope:plugin, area:web-development` |
| #90 | OPEN | DOING | writing-style | `maintenance-track` | `kind:new-capability, scope:plugin, area:writing-style` |
| #92 | OPEN | DOING | repo | `maintenance-track` | `kind:governance, scope:repo-workflow, area:repo` |

## Pre-v7 Repository-Level Label Definitions

Pending G7. Exact live repository-level definitions for every v7 label, plus protected `maintenance-track`, must be captured in `PRE_CUTOVER_LABEL_DEFINITIONS.json` after independent implementation Reviewer PASS and latest-main drift check, before any label mutation. `ROLLBACK_SNAPSHOT.md` must be refreshed at that time to reference those definitions.

## Clear Writing / Tracking Issue Evidence

- v7 tracking Issue: #92
- Clear Writing replay receipt: `results/repo--maintenance-board-issue-maturity/clear_writing/CLEAR_WRITING_RECEIPT.md`
- Revised Issue body: `results/repo--maintenance-board-issue-maturity/clear_writing/revised_tracking_issue_body.md`
