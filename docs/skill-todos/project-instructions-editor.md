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


### Follow-up review: Project instructions need semantic prioritization, not equal-detail accumulation
status: NEW
source: user review of the same shared-course Project settings, 2026-09-28
evidence: detailed user comparison of what the Project should preserve versus what should move to course repositories/workflows; same two private Project-instruction drafts above.
problem:
- A multi-scope Project needs a global balance check. Shared durable principles should be stated once at Project level, while scope-specific detail should remain proportionate to each scope's long-term importance. The most recently discussed scope must not receive most of the instruction budget merely because it triggered the edit.
- Project instructions should hold stable ownership, routing, authority, safety/distribution boundaries and durable design philosophy. They should not absorb task SOPs such as per-document reconstruction steps, LaTeX build procedures, figure-redrawing instructions, detailed review checklists or exhaustive tool task lists.
- When two scopes share the same durable rule, the editor should lift it into one shared rule rather than duplicate a full workflow under one scope. In the real case, both courses can share a source -> clarification -> polished artifact -> review principle while keeping different end goals.
- Stable high-level product/course philosophy deserves more instruction budget than implementation detail. In the real case, the long-lived STAT5060 analysis/assessment philosophy was more central than low-level STAT5050 note-production mechanics, yet the revision allocated space in the opposite direction.
- Source and derived-artifact identity should be expressed as one reusable provenance rule: instructor/course sources remain sources; reconstructed notes, tutorials, solutions and study notes are derived artifacts and must not silently impersonate the original source.
- Stable copyright/distribution boundaries belong at Project level when they govern all downstream work. Transforming restricted instructor material into a cleaner format does not by itself make that material public or redistributable.
- Time-varying policy should normally be represented by a durable lookup gate rather than copied as a permanent fact. For example, student-side AI use should defer to the current institutional/instructor policy instead of freezing one term's rule into long-lived Project instructions.
- Tool division should be stated at capability level, not as duplicated task inventories: judgment/specification, substantial multi-source transformation, and implementation/build/testing are durable distinctions; exhaustive per-tool bullet lists are not.
- A course/project repository can be a validation ground for later reusable knowledge. The Project-level rule should distinguish local course artifacts from validated downstream extraction into AI_Skills or another general knowledge layer, instead of only saying “do not copy course content.”
- The instruction editor needs an explicit knowledge-layer check so that instructor/source material, project reconstruction, modern supplementation and reusable general knowledge do not collapse into one undifferentiated instruction surface.
- A bounded local request should default to a bounded edit. In this real case, the prior Project settings were already mostly correct, so the desired change was roughly a 10–20% semantic increment, not a wholesale rewrite. A large rewrite should require an actual cross-cutting inconsistency, not merely a newly discussed subtopic.
project-specific context: the concrete courses, assessment design and note workflows are local examples. The reusable requirement is semantic prioritization under a finite instruction budget: decide what belongs at Project level, preserve balance and existing valid authority, lift shared rules, keep volatile/detail-heavy procedures behind locators, and make the smallest edit that closes the real gap.
