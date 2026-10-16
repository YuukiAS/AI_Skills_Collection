# course-assessment-authoring — Student-Audience and Approval-Gate Evidence

status: NEW
source: `YuukiAS/STAT5060-TA` / STAT5060 2026–27 Final Project student-guide revision
evidence:
- rejected student Guide at candidate `145c7bc265265e4bc266824af8c770d9e3e55014`;
- instructor PDF annotations and subsequent thread corrections, 2026-10-06;
- primary candidate TODO: `docs/skill-todos/course-assessment-authoring.md`;
- cross-domain Research Authoring note: `docs/plugin-todos/research-writing-student-audience-and-pre-render-approval.md`.

target layer: student-facing assessment authoring / content selection / human approval gate / revision protocol

## Additional failure evidence

The initial TODO correctly identified internal-specification leakage, but later revision attempts revealed a stricter problem: even after removing obvious machine language, the author continued adding material that had not been requested for students.

Concrete failures included:

- adding a contingency oral date that the instructor had not asked to publish;
- adding consultation requirements without instructor approval;
- publishing a method-eligibility and required-analysis map that did work students were expected to do by consulting lecture notes;
- publishing internal score-cap exception logic and its rationale;
- treating every defensible instructor-side rule as student-facing information;
- moving toward rendering before the instructor had approved the complete student-facing body.

These are not merely wording defects. They show that a student-facing artifact needs an explicit inclusion boundary.

## Audience contract for student assessment materials

Before drafting or revising, state:

```text
AUDIENCE = postgraduate students enrolled in the course
PURPOSE = tell them exactly what they must do, submit and be prepared to explain
NOT_FOR = instructor, marker, course designer, rubric calibrator, implementation agent or QA reviewer
```

The artifact should include only information students need to:

- understand the task;
- identify required components;
- plan workload;
- comply with deadlines and submission rules;
- understand broad assessment priorities;
- use permitted tools appropriately;
- prepare for any student-facing oral component.

The artifact should not automatically include:

- instructor-side method-selection aids;
- a solved mapping from data structures to course methods when students are expected to consult lecture notes;
- internal rubric atoms or cap exceptions;
- consultation requirements that were not explicitly approved;
- contingency dates not explicitly approved;
- marker codes;
- implementation and QA details;
- reasons for rejected alternatives;
- policy nuance that does not alter student action.

A useful rule is:

> Publish what the student must know to act correctly, not everything the course team knows.

## Mandatory human content approval before Codex rendering

Student-facing Homework, Project, Milestone and oral instructions must use two separate stages.

### Stage A — content only

- Re-read canonical course sources and all active annotations.
- Restate the audience contract.
- Produce the complete student-facing body in plain text or Markdown.
- Do not build PDF/DOCX/templates.
- Do not invoke rendering or layout tools.
- Present the complete body to the instructor.
- Record explicit approval or requested changes.

### Stage B — implementation only

Stage B may begin only after an approval record exists for the exact content version.

Codex may then:

- materialize templates;
- render PDF/DOCX;
- apply the approved visual system;
- run consistency and leakage checks;
- package student materials.

Codex may not add new content, examples, dates, consultation rules, rubric detail or explanatory policy during rendering.

## Mandatory revision preamble

Every later revision must begin by repeating:

```text
This is written for: <student audience>
Students need this document to: <reader task>
This document is not for: <instructor/marker/QA/implementation audiences>
```

Then re-read:

- the full approved content;
- the audience contract;
- all active annotations;
- all previous rejected-route guards;
- the current rendered artifact if layout is in scope.

The agent must not revise from memory or only from the most recent complaint.

## Approval record and invalidation

The approval record should identify:

- exact content file;
- exact content SHA or commit;
- approving user/instructor decision;
- scope of approval;
- whether rendering is authorized.

Any semantic change to student-facing content invalidates the previous render authorization and returns the task to Stage A.

Purely mechanical fixes that preserve approved content may remain in Stage B, but the agent must show that content hashes or semantic-diff checks are unchanged.

## QA additions

Student-facing semantic QA should verify:

- no unapproved date or contingency appears;
- no unapproved consultation requirement appears;
- no instructor-only scoring nuance appears;
- no method-selection scaffolding exceeds the instructor-approved scope;
- the first page states the required work and quantities;
- student and instructor artifacts are clearly separated;
- every sentence changes or supports student action;
- the rendered artifact matches the approved body without additions.

## Project-specific exclusions

Do not generalize the following STAT5060 details:

- written/oral weights;
- Chapter range and titles;
- milestone dates;
- page limits;
- filenames;
- late deductions;
- data size limits;
- AI statement wording;
- oral timing and question structure.

These remain canonical only in `YuukiAS/STAT5060-TA`.
