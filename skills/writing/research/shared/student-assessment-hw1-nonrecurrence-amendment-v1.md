# Student Assessment Research Authoring — HW1 Non-Recurrence Amendment V1

Status: **CANONICAL COMPANION / MUST READ AFTER THE RUNBOOK AND ACCEPTANCE CONTRACT**  
Date: 2026-10-07  
Applies to: all non-trivial student-facing Homework, Project, milestone, policy, template and oral-brief work

This amendment is binding because the first STAT5060 HW1 replay exposed gaps that were not sufficiently explicit in the original runbook. It does not replace the runbook or cumulative acceptance contract. It adds mandatory preflight, proof, calibration and escalation rules.

Primary incident record:

`docs/design/research-authoring/STUDENT_ASSESSMENT_HW1_FINAL_PROJECT_POSTMORTEM_AND_NONRECURRENCE_V1_2026-10-07.md`

---

## 1. Additional mandatory preflight fields

Before planning, Critic review or implementation, report:

```text
POSITIVE_STYLE_BASELINE =
REJECTED_BASELINES =
AUTHORITY_COHERENCE_MATRIX = READY | NOT_READY
RELATIONAL_INVARIANT_LEDGER = READY | NOT_READY
PAGE_COUNT_FEASIBILITY_STATUS = PROVED | UNPROVED | N/A
COMPOSITION_ARCHETYPE_STATUS = PROVED | UNPROVED | N/A
VALIDATOR_VERSION_FROZEN = YES | NO
VALIDATOR_KNOWN_BAD_CONTROL = PASS | NOT_RUN
VALIDATOR_KNOWN_GOOD_CONTROL = PASS | NOT_RUN | N/A
OBJECTIVE_AESTHETIC_GATE_OWNERSHIP = PASS | FAIL
GOVERNANCE_BUDGET = PROPORTIONATE | EXCEEDED
NEXT_VISIBLE_PROOF_MILESTONE =
```

Production cannot begin when any required field is unresolved.

---

## 2. Positive-baseline requirement

Before redesign, modernization or major revision, bind an accepted positive baseline for the document family.

The positive baseline may include separate artifacts for:

- title / metadata;
- typography / mathematics;
- question / subpart / point treatment;
- tables;
- quotations and links;
- forms;
- footer / page number;
- overall tone and density.

A latest candidate that the user rejected cannot silently become the style authority.

Required record:

```text
POSITIVE_BASELINE_ARTIFACT
POSITIVE_BASELINE_HASH
POSITIVE_COMPONENTS_INHERITED[]
EXPLICIT_DEVIATIONS[]
DEVIATION_REASON[]
```

---

## 3. Authority-coherence matrix

Before the Prebuild Critic, reconcile all fields that can drift across syllabus, timetable, frozen assessment authority, approved body and current artifact.

Minimum fields:

```text
course title
affected academic year / term
due date / time / timezone
weight / points / total
question or section range
required file count / filenames
page-count mode
public scoring granularity
AI-policy rule
student / instructor / QA release boundary
```

For every field record:

```text
FIELD
CANONICAL_OWNER
CURRENT_VALUE
OTHER_OBSERVED_VALUES
CONFLICT_STATUS
RESOLUTION
```

Any unresolved conflict blocks drafting and rendering.

---

## 4. Relational-invariant ledger

Exact-copy locks are insufficient when one approved change alters related references.

Freeze and validate relations such as:

```text
question_range = first_question .. last_question
sum(question_points) = stated_total
listed_file_count = stated_file_count
listed_template_routes = supported_template_routes
page_limit_table = page_limit_prose
penalty_consequence = penalty_authority
milestone/final wording = artifact lifecycle stage
section/table/figure references resolve
report/oral responsibilities do not overlap improperly
```

A candidate fails when exact text is preserved but a relation becomes false.

---

## 5. Constraint-satisfiability proof before hard freeze

Do not hard-freeze page count, break positions or dense visual constraints before proving that the frozen copy and document-family typography admit at least one legal composition.

Required proof:

```text
FROZEN_COPY_RENDERED = YES
FROZEN_FAMILY_TYPOGRAPHY_APPLIED = YES
LEGAL_COMPOSITION_COUNT >= 1
HARD_CONSTRAINTS_MUTUALLY_COMPATIBLE = YES
```

If not satisfied, Planner must decide which authority changes:

- page-count mode;
- information architecture;
- explicit semantic breakpoint;
- approved typography/geometry;
- or content scope through renewed content approval.

Codex must not be asked to discover a contradiction by brute force.

---

## 6. Composition archetype before micro-spacing

When layout is unresolved, first compare meaningful composition structures, not dozens of near-identical spacing combinations.

Examples:

- one rules page versus two rules pages;
- semantic break after Block A versus after Block B;
- top-aligned short page versus deliberately distributed short page;
- compact table inline versus dedicated compact table block;
- one-column versus approved peer-column structure.

Only after an archetype passes objective feasibility and rendered proof may the Producer search a small spacing range.

Micro-spacing cannot repair a wrong information architecture.

---

## 7. Deterministic versus aesthetic gate ownership

### Deterministic Validator owns

- exact copy, values, formulas, dates, points and filenames;
- relational invariants;
- BlockID/order/page placement when frozen;
- semantic-block split/no-split rules;
- clipping, overflow, missing glyph and missing artifact;
- protected paths, hashes and allowlists;
- student/instructor/QA leakage;
- known-bad regression classes.

### Rendered Reviewer owns

- whether whitespace is intentional;
- whether a short page feels calm or residual;
- whether adjacent pages feel balanced enough;
- whether spacing is cramped or loose;
- whether a composition fits the course family;
- reader effort, rhythm, scanability and page-turn cost.

Occupancy, density and bottom-blank metrics are diagnostics unless:

1. calibrated against an accepted positive baseline for the same family; or
2. protecting an objective usability failure.

If all candidates fail the same aesthetic metric, stop and repair gate ownership before expanding the search.

---

## 8. Validator calibration

Before a validator governs a real candidate:

```text
VALIDATOR_VERSION_FROZEN = YES
KNOWN_BAD_CONTROLS_REJECTED = YES
KNOWN_GOOD_OR_SYNTHETIC_VALID_CONTROL_ACCEPTED = YES | JUSTIFIED_NA
VALIDATOR_EDITABLE_BY_PRODUCER = NO
THRESHOLDS_EDITABLE_DURING_CANDIDATE_RUN = NO
```

A validator that only proves rejection is not sufficient when it is intended to admit valid candidates.

If no positive control exists, create a synthetic-valid fixture for objective gate calibration before production.

---

## 9. Prebuild Critic additions

For major/recovery work, the Critic must explicitly answer:

```text
POSITIVE_BASELINE_BOUND = YES | NO
AUTHORITY_CONFLICTS = NONE | <details>
RELATIONAL_INVARIANTS_COMPLETE = YES | NO
PAGE_COUNT_FEASIBILITY_PROVED = YES | NO | N/A
COMPOSITION_ARCHETYPE_PROVED = YES | NO | N/A
VALIDATOR_GATE_OWNERSHIP = PASS | FAIL
VALIDATOR_CALIBRATION = PASS | FAIL | N/A
TASK_PROPORTIONALITY = PASS | FAIL
USER_REVIEW_BUDGET_PROTECTED = YES | NO
```

A major Planner amendment after Critic PASS requires a new fresh Critic.

---

## 10. Task proportionality and governance budget

Every task declares the smallest adequate process.

For a simple new Homework using an accepted family:

- recover sources;
- freeze body and components;
- prove a small representative set;
- produce one internally reviewed candidate.

Do not automatically import failed-version recovery machinery.

For a genuine recovery:

- consolidate authority once;
- supersede old local prompts;
- stop creating new project-local versions after root-cause escalation;
- ensure every governance change directly unlocks the next visible proof.

Required:

```text
GOVERNANCE_FILES_ADDED_THIS_ROUND = <n>
NEXT_VISIBLE_PROOF_MILESTONE = <artifact>
OPEN_ISSUES_BEFORE = <n>
OPEN_ISSUES_AFTER = <n>
```

If governance grows while visible proof and open-issue reduction do not advance, stop and simplify.

---

## 11. Incident escalation and round budget

Trigger incident/root-cause mode when any occurs:

- a closed guard recurs;
- a user-accepted component reopens;
- two broad rounds fail to reduce open issues;
- the same visible defect reaches the user twice;
- zero candidates survive one common failure class;
- validator/reviewer ownership is disputed;
- the user is asked to debug routine visual or consistency defects.

After escalation:

1. freeze current candidate and authority;
2. write one root-cause statement;
3. consolidate/supersede old prompts;
4. repair the shared authority, component, generator, validator or reviewer layer;
5. add a regression guard;
6. rerun from the frozen candidate;
7. do not expose another candidate until independent convergence.

---

## 12. User-review budget and delivery gate

Default bounded-revision budget:

```text
HUMAN_REVIEW_BUDGET = one final acceptance review
USER_IS_FIRST_QA = NO
```

Before user delivery:

```text
PREBUILD_CRITIC = PASS | N/A
DETERMINISTIC_VALIDATION = PASS
RENDERED_ARTIFACT_REVIEW = PASS
GPT_WORK = PASS | N/A
RELATIONAL_INVARIANTS = PASS
ACTIVE_FEEDBACK_OPEN = 0
LOCKED_REGIONS_PRESERVED = PASS
OBVIOUS_ROUTINE_DEFECTS = NONE
READY_FOR_USER_REVIEW = YES
```

The user may receive two alternatives only when both already pass every non-subjective gate and are independently judged acceptable.

---

## 13. Mandatory HW2 startup rule

STAT5060 HW2 should begin as `NEW_MAJOR` with:

1. actual source/timetable/policy intake;
2. positive family baseline from accepted HW1;
3. authority-coherence matrix;
4. assessment-purpose/workload freeze;
5. student/instructor/QA source-to-reader map;
6. complete student-visible body approval;
7. relational-invariant ledger;
8. Prebuild Critic;
9. component proof and representative pages;
10. one Controller Goal with fresh Auditor/Reviewer;
11. GPT Work before user acceptance;
12. immediate locking of accepted student artifacts.

HW2 inherits accepted family components and generic guards, not rejected HW1 page layouts or recovery ceremony.

---

## 14. Mandatory Final Project restart rule

STAT5060 Final Project remains `FAILED_VERSION_RECOVERY`.

Before resuming:

1. bind approved body and all assessment decisions;
2. recover all raw highlights/direct decisions into the cumulative registry;
3. bind positive visual-family components without copying Homework information architecture;
4. complete authority-coherence and relational-invariant ledgers;
5. run fresh Prebuild Critic on validity, workload, scoring transparency, penalties, templates, package burden, report/oral boundary and AI policy;
6. prove first-page summary, date/mark block, method/data boundary, penalty table, AI/oral block, milestone form and three template routes;
7. obtain content approval before render;
8. produce representative pages/forms/templates before full package;
9. use one Controller Goal with independent Auditor/Reviewer cycles;
10. run GPT Work over the complete student release set;
11. user sees only independently accepted student artifacts;
12. lock student materials before reviewing instructor rubric/grading assistance.

---

## 15. Completion criterion

This amendment is considered successfully adopted only when:

- HW1 closes without another user-discovered routine defect;
- HW2 reaches a useful first candidate without repeated broad layout repair;
- Final Project closes all historical highlights without internal-material leakage;
- a seeded relational inconsistency is caught;
- a seeded aesthetic-threshold ownership defect is caught;
- a local repair preserves all unrelated accepted regions.


---

## 17. Typography changes invalidate pagination guards

A font-size, body-leading, geometry, or comparable global typography change invalidates page-protection controls that were tuned under the previous typography.

Controls such as:

- `Needspace`;
- keep-with-next / keep-together thresholds;
- widow/orphan protections;
- manual break hints;
- minimum-space guards before headings, questions, tables, equations, or list items

must be treated as **dependent layout state**, not as immutable content.

Before declaring a typography alternative visually infeasible:

1. inspect the actual generated source around every unexpected blank/residual page;
2. inventory all explicit and effective pagination controls affecting that region;
3. distinguish natural text reflow from a stale guard inherited from the old typography;
4. repair only the stale pagination guard while keeping copy, semantics, margins, and the requested typography change fixed;
5. rerender and independently review the repaired alternative.

A candidate must not be rejected as “font size does not work” when the visible failure is actually caused by a stale `Needspace` / keep-together / break control from the previous font scale.

For bounded typography comparisons, pagination guards are automatically reopened for review even when visible copy remains locked.
