# course-assessment-authoring — Long-Term TODO

Maintenance inbox for a proposed standalone `course-assessment-authoring` skill.

This candidate is intentionally separate from `research-writing`. Its target is the transformation of frozen course-assessment decisions into student-facing Homework, Project, Milestone, submission, template and oral-assessment materials, while keeping instructor grading materials and QA evidence separate.

The file records real project failures first. It does not yet authorize creating, publishing or releasing a new skill.

## Open candidates

### Student-facing assessment material was generated from internal specifications instead of reader needs
status: NEW
source: `YuukiAS/STAT5060-TA` / STAT5060 2026–27 Final Project student-guide production and instructor review
evidence:
- repository candidate: `YuukiAS/STAT5060-TA@145c7bc265265e4bc266824af8c770d9e3e55014`
- failed student artifact: `materials/2026-27/final-project/student/release/STAT5060_Project_Guide_2026-27.pdf`
- frozen course authority: `docs/frozen/2026-27/STAT5060_FINAL_PROJECT_*.md`
- instructor annotation closure specification: `docs/execution/STAT5060_FINAL_PROJECT_STUDENT_GUIDE_REWRITE_V3_ANNOTATION_LOCKED.md`
- current project thread: instructor annotated the first three Guide pages and rejected the resulting student-facing information architecture despite successful build, visual and automated validation

target layer: standalone skill candidate / student-facing assessment authoring / review protocol / QA

problem:
- A 10-page student Guide was assembled largely from frozen policy files, method-reference material, atomic grading criteria and submission rules.
- The artifact was technically valid and passed extensive automated checks, but it read like an internal policy and grading manual rather than a postgraduate Project handout.
- Internal publication state, machine-style decision labels, grading codes, rejected implementation alternatives and QA-era vocabulary leaked into student-facing material.
- The main task, required statistical components and mark allocation were not surfaced with the required priority.
- Course-source labels were paraphrased or merged with derived eligibility descriptions instead of being preserved in distinct fields.
- A 25-row instructor grading ledger was treated as if it automatically belonged in the student Guide.
- Dense tables passed clipping/overflow tests while remaining difficult to scan because adjacent logical rows were visually indistinct.
- Later revisions failed because the agent did not re-read and close every instructor annotation; it carried forward partial memory from the previous version.

project-specific context:
- The following remain STAT5060-only and must not become generic skill rules: 25% written / 15% oral, Chapter 4–9 eligibility, exact 2026 dates, 10+2 pages, 100 MB, exact filenames, late deductions, specific AI wording, specific oral format, A1–G2 and P01–P09.
- `YuukiAS/STAT5060-TA` remains canonical for the actual assessment design and student materials.
- This TODO concerns the authoring and review method, not the course-specific content.

## Candidate capability boundary to evaluate

A future skill should operate only after assessment meaning is frozen. It should not decide what to teach, assess, score or penalize. Its role would be to turn canonical course decisions into usable reader-facing artifacts and review revisions against the full source and annotation history.

The candidate should distinguish at least four audiences:

1. students;
2. instructors / markers;
3. implementation agents;
4. QA / release reviewers.

It should support distinct artifact families rather than one generic template:

- Homework brief;
- Project brief / Guide;
- Milestone or proposal form;
- oral-defense student brief;
- student submission checklist;
- instructor rubric and grading sheet;
- instructor solution / calibration material;
- release and QA evidence.

## Lessons to preserve for later skill design

### 1. Audience boundaries

- Student-facing artifacts state the effective course rule, not the internal representation of that rule.
- Internal publication state, approval status, branch/commit information, implementation history, machine enums and QA vocabulary do not belong in student materials.
- Student release, instructor release and QA evidence must be separate deliverable sets.
- A student Guide must not double as a marker manual.

### 2. Assessment information architecture

- First-page priority should be the task, weighting, required components, key quantities, deadline and final deliverables.
- Project materials should surface required evidence before administrative detail.
- The source-file order must not determine the student-document order.
- A future workflow should freeze student-facing content structure before Codex or another implementation agent begins layout and rendering.

### 3. Appropriate postgraduate level

- State required components and evidence without adding remedial teaching that was not requested.
- Do not automatically add “what a good project looks like”, toy case studies, weak-versus-strong examples or elementary research-method explanations for postgraduate students.
- Examples should appear only when the instructor explicitly decides that they are pedagogically necessary.

### 4. Scoring transparency versus internal grading machinery

- Student-facing scoring should normally expose assessment dimensions, weights, caps and essential conditions at the level needed to plan work.
- An atomic instructor rubric exists for scoring reliability and does not automatically belong in student materials.
- The workflow must explicitly decide which rubric layer is public rather than assuming all rubric detail should be published.
- Internal penalty identifiers should be translated into plain-language student consequences.

### 5. Lifecycle-aware wording

- Proposal or milestone artifacts use `proposed`, `planned` and future-oriented language.
- Final-submission artifacts use `fitted`, `completed`, `reported` and submitted-evidence language.
- Student-visible statuses must state the next action in plain language.
- Internal machine enums may remain in implementation records but should not dominate reader-facing text.

### 6. Course-source fidelity

- Canonical course code, full course name, academic year, term, due-date convention and document-family header should be recovered from actual course artifacts rather than invented per document.
- Official Chapter numbers and titles should be preserved verbatim from lecture sources.
- Derived eligibility, explanation or modernization belongs in separate fields and must not silently replace source labels.
- Date and time formatting should be consistent across the course family.

### 7. Positive specification

- Tell students what they must include and submit.
- Do not expose rejected design alternatives or lists of requirements that were deliberately removed.
- Avoid expanding uncommon exceptions in the main Guide when consultation can handle them.
- Explain the purpose of a requirement only when the explanation changes student action.

### 8. Forms and tables

- A reading table and a fillable planning form require different layout contracts.
- Long instructional tables should normally avoid vertical rules, use restrained horizontal rules and use whitespace/grouping to separate logical rows.
- Form QA must inspect actual writable space, checkbox clarity, student/instructor section separation and one-page usability, not only text-token presence.
- Table readability is part of information architecture, not a cosmetic afterthought.

### 9. Revision protocol

- Every revision must re-read canonical source, current artifact and all active user annotations; a previous generated version is not sufficient context.
- User annotations should be tracked as a closure ledger: annotation ID, exact target, intent, implementation, validation and status.
- A new version must not inherit assumptions merely because the previous version passed technical QA.
- Any user-rejected route should be retained as a recurrence guard until the replacement is accepted.

### 10. Semantic QA beyond build QA

A release check must go beyond existence, searchability, page size and clipping. It should ask:

- Can the intended reader identify the task and required quantities immediately?
- Is internal workflow language absent?
- Is the wording appropriate to the assessment lifecycle stage?
- Are official source labels faithful?
- Are student and instructor materials separated?
- Are tables and forms actually readable and usable?
- Does the artifact communicate the instructor-approved information hierarchy?

### 11. Codex / implementation boundary

- Codex may materialize, render, test and package a frozen content specification.
- Codex should not independently choose what students need to know, how much rubric detail to reveal, or how course-source terminology should be reorganized.
- Substantial student-facing artifacts require a frozen reader-facing content specification before implementation.



### 12. Course document-family identity

Homework, Project, Milestone and related student documents should inherit a course-level family contract rather than inventing metadata layout independently.

The reusable specialization should support a family schema covering:

- full course title;
- artifact title;
- academic year / term;
- due-date label and placement;
- course-weight / total-points metadata when applicable;
- compact metadata spacing;
- page geometry and type family;
- heading hierarchy;
- page number/footer conventions;
- hyperlink style;
- direct-quotation style.

The contract controls presentation and labels. Exact dates, weights and points remain course-specific canonical data.

A later artifact may deviate only when the instructor explicitly approves a different reader need. “Use a different template because it looks nicer” is not sufficient.

### 13. Direct quotations and source-backed policy text

For student-facing policy or institutional guidance:

- quote only source text that has been explicitly selected and verified;
- render substantive quotations in an unmistakable quotation style, preferably a block quote with a left rule or equivalent restrained academic treatment;
- keep exact attribution adjacent to the quote;
- distinguish direct quotation from course-authored paraphrase;
- preserve approved link labels and link destinations;
- do not let Codex invent policy prose, citation text, quotation wording or source interpretation during rendering.

The student-facing approved body must freeze both the exact quotation and the exact course-authored connective prose before implementation.


## Candidate workflow to evaluate later

A later Planner should evaluate a workflow such as:

```text
course sources and frozen assessment decisions
-> audience and artifact classification
-> student-facing content specification
-> instructor-facing grading specification
-> explicit source/derived-field map
-> implementation handoff
-> technical QA
-> semantic reader review
-> annotation closure review
-> bounded revision
```

This is only a candidate workflow. It must be tested against more than one real Homework/Project case before promotion.

## Promotion evidence needed

Before creating or releasing a skill, obtain evidence from multiple course artifacts, preferably including:

- one Homework brief;
- one open-ended Project brief;
- one milestone/proposal form;
- one instructor grading package;
- at least one revision driven by annotated PDF feedback.

The promotion review should confirm that the skill improves reader usability without taking over assessment design or leaking course-specific policy into the reusable layer.

## Recently promoted
