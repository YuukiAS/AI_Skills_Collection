# project-instructions-editor — Long-Term TODO

Maintenance inbox for a candidate standalone support skill for editing ChatGPT Project instructions.

No production skill or Plugin is created by this file. This inbox records real failures first; architecture, packaging, release route and acceptance gates remain for later Planner/Critic work.

## Open candidates

### Shared Project instructions can become scope-imbalanced and bloated after a local addition request
status: NEW
source: real ChatGPT Project settings revision, 2026-09-28
evidence: two private user-provided Project-instruction drafts, not copied into this public repository. One draft is about 9,375 characters / 480 lines; a later compressed draft is about 6,486 characters / 353 lines. Both describe one shared Project for two statistics courses.
problem:
- The Project is intentionally shared by two courses with different roles and repositories, but a request to add or strengthen one course caused that course's detailed learning workflow to dominate the Project-level instructions.
- The first draft exceeded the user's 8,000-character Project-instruction budget. The second fit under that ceiling but remained substantially over-specified, showing that merely shrinking text is not enough.
- The drafts copy large amounts of domain workflow into Project settings: theorem/algorithm explanation checklists, polished-note production stages, review checklists, tool-role breakdowns and repeated response-style rules. Much of this belongs in canonical course repositories, course documents, global user instructions, or task-specific prompts and should be retrieved when needed rather than permanently duplicated.
- The latest local request was treated too much like permission to rewrite the whole instruction surface around the newly discussed subproject. Existing valid scope and balance were not treated as constraints to preserve.
- There is no explicit semantic budget that distinguishes stable routing/ownership rules from recoverable detailed knowledge, no reserved headroom below the hard character limit, and no check that multiple subprojects remain proportionately represented after an edit.
- Success therefore drifted toward “include every useful detail” instead of “keep the smallest stable instruction surface that reliably routes future work to the right sources and constraints.”
project-specific context: STAT5050/STAT5060 names, course roles, repository names, note-production details and assessment specifics are local to the user's course Project. The reusable failure is Project-instruction editing under a hard character budget: preserve prior valid semantics, maintain balance across subscopes, prefer canonical locators over copied detail, separate stable rules from task-specific knowledge, and make bounded edits instead of allowing the latest request to dominate the whole Project.
