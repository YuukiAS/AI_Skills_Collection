# Research Authoring — Student-Audience Contract and Pre-Render Approval TODO

status: NEW
source: `YuukiAS/STAT5060-TA` / STAT5060 2026–27 Final Project student-guide failure and annotated instructor review
evidence:
- rejected student artifact: `YuukiAS/STAT5060-TA/materials/2026-27/final-project/student/release/STAT5060_Project_Guide_2026-27.pdf`
- candidate implementation commit: `145c7bc265265e4bc266824af8c770d9e3e55014`
- instructor annotations and thread corrections, 2026-10-06
- related course-specific TODO: `docs/skill-todos/course-assessment-authoring.md`

target layer: research-document planning / audience contract / approval gating / QA boundary

## Problem

A technically correct, fully rendered and heavily validated document can still be wrong because it was authored for the wrong audience.

The failed STAT5060 Guide was nominally student-facing, but much of its content was selected from instructor, marker, implementation and QA needs. It exposed or over-explained material that may be valid internally but was not needed by postgraduate students to complete the assessment. Examples included:

- internal publication and approval state;
- machine-style decision labels and grading codes;
- instructor-side atomic rubric detail;
- method-selection scaffolding that effectively pre-solved the task of consulting the lecture notes;
- unrequested consultation requirements;
- an unrequested contingency oral date;
- internal score-cap exception logic;
- removed implementation alternatives and QA history.

The central failure was not factual inaccuracy. It was an audience-selection failure: the author asked “what information exists?” instead of “what does this reader need to act correctly?”

## Cross-domain lesson for Research Authoring

Research Authoring already distinguishes advisor-facing, reviewer-facing and manuscript-facing documents. The same general contract should be made explicit for any reader-facing artifact:

1. Declare the intended reader before drafting.
2. Declare the decisions or actions that reader must be able to make.
3. Declare what belongs to other audiences and must be excluded.
4. Select content because it serves the reader’s task, not because it is available in the source bundle.
5. Do not assume that material useful to an author, supervisor, marker, implementer or QA reviewer belongs in the reader-facing artifact.

A reusable preflight should require:

```text
AUDIENCE = <specific reader>
READER_TASK = <what this reader must understand or do>
INCLUDE = <information required for that task>
EXCLUDE = <author/instructor/marker/implementation/QA-only information>
```

## Student-facing specialization

For student assessment materials, the audience contract should normally be:

```text
AUDIENCE = students completing the assessment
READER_TASK = understand the required work, deadlines, deliverables, broad assessment priorities and permitted tools
NOT_FOR = instructor, marker, rubric calibrator, implementation agent or QA reviewer
```

The student artifact should normally include:

- the task;
- required components;
- quantities and limits the student must satisfy;
- deadlines;
- submission format;
- broad mark allocation when publication is pedagogically useful;
- consequences the student must know;
- allowed and prohibited assistance.

It should not automatically include:

- instructor reasoning for why a rule exists;
- atomic grading ledgers;
- machine identifiers;
- internal exceptions or cap logic;
- contingency plans not approved for publication;
- method-selection aids that remove work the instructor expects students to do from lecture materials;
- implementation history;
- QA evidence.

Not every true statement belongs in every artifact.

## Mandatory content-approval gate before rendering

A substantial reader-facing artifact must not move directly from internal sources to Codex rendering.

Required sequence:

```text
source and policy review
-> audience contract
-> complete reader-facing body draft
-> human content approval
-> frozen approved content
-> Codex layout/render/build
-> visual and semantic QA
```

For student-facing Homework, Project, Milestone and oral materials:

- the complete body text must be shown to the instructor before Codex compilation or rendering;
- the instructor must explicitly approve the content;
- rendering approval is not implied by approval of the assessment design;
- Codex must fail closed when the content-approval record is absent;
- a later revision must return to content approval when it changes meaning, information scope or audience-facing structure.

## Revision preflight

Every revision must begin by restating:

```text
WHO THIS IS FOR
WHAT THIS READER NEEDS TO DO
WHAT THIS DOCUMENT MUST NOT CONTAIN
```

It must then re-read:

- current canonical sources;
- the currently approved body;
- all active user annotations;
- the audience contract;
- the previous rejection guards.

A previous successful render or validation report is not sufficient context.

## Boundary with Course Assessment Authoring

This TODO records the generic Research Authoring lesson: audience determines document semantics and content selection, and substantial reader-facing content requires human approval before rendering.

The proposed `course-assessment-authoring` skill should own the course-specific specialization for Homework, Project, Milestone, rubric publication, student/instructor separation and assessment release packaging.

STAT5060-specific weights, dates, methods, penalties, filenames and oral rules must remain in `YuukiAS/STAT5060-TA` and must not be generalized into Research Authoring.

## Promotion evidence needed

Before promotion, replay the audience-contract and pre-render approval sequence on at least:

- one student Homework brief;
- one student Project brief;
- one advisor-facing research report;
- one reviewer-facing manuscript or rebuttal artifact.

Verify that the same audience contract improves content selection without collapsing distinct domain workflows into one template.
