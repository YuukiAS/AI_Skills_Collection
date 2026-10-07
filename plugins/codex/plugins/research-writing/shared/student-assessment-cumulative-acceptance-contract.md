# Student Assessment Research Authoring Cumulative Acceptance Contract

Status: **CANONICAL CANDIDATE / COMPANION TO `student-assessment-end-to-end-pre-execution-runbook.md`**  
Applies to: non-trivial student-facing Homework, Project, milestone/proposal, policy, template, submission and oral-brief artifacts

This contract defines the cumulative acceptance gates for student-facing assessment documents.

A later gate cannot override an earlier failure. Executor self-review cannot grant acceptance. Every accepted revision inherits all unretired prior gates and human guards.

---

# 1. Required artifact identity

Before any acceptance work:

```text
REPOSITORY =
BRANCH =
TASK_CLASSIFICATION =
ARTIFACT_FAMILY =
EXACT_BASELINE_COMMIT =
EXACT_BASELINE_ARTIFACT_HASH =
APPROVED_BODY_PATH =
APPROVED_BODY_HASH =
AUDIENCE_CONTRACT_PATH =
SOURCE_MANIFEST_PATH =
FEEDBACK_REGISTRY_PATH =
PRESERVATION_MAP_PATH =
ROUND_ALLOWLIST_PATH =
VALIDATOR_VERSION =
REVIEWER_RUBRIC_VERSION =
```

Missing or ambiguous identity blocks production.

---

# 2. Gate A — source, history and authority coverage

Required:

```text
SOURCE_SET_COMPLETE = YES
CANONICAL_COURSE_AUTHORITY_READ = YES
CURRENT_ARTIFACT_READ = YES
VERSION_LINEAGE_COMPLETE = YES | N/A
RAW_HIGHLIGHTS_AND_ANNOTATIONS_CONSUMED = YES | N/A
DIRECT_USER_DECISIONS_CONSUMED = YES
POSITIVE_BASELINES_BOUND = YES | N/A
REJECTED_BASELINES_BOUND = YES | N/A
SOURCE_GAPS = NONE | <details>
```

For major/recovery tasks, the cumulative feedback registry must report counts by lifecycle state.

```text
FEEDBACK_ACTIVE = <n>
FEEDBACK_PARTIAL = <n>
FEEDBACK_RENDER_PENDING = <n>
FEEDBACK_RESOLVED_IN_SPEC = <n>
FEEDBACK_RESOLVED_IN_RENDER = <n>
FEEDBACK_SUPERSEDED = <n>
FEEDBACK_RETIRED_BY_STRUCTURE_CHANGE = <n>
FEEDBACK_SOURCE_GAP = <n>
```

Any unresolved source/history gap prevents a global PASS.

---

# 3. Gate B — assessment validity and workload

Required for Homework/Project artifacts:

```text
ASSESSMENT_PURPOSE_EXPLICIT = YES
LEARNING_OUTCOME_ALIGNMENT = PASS
REQUIRED_STUDENT_EVIDENCE_EXPLICIT = YES
HIDDEN_DELIVERABLES = NONE
STUDENT_WORKLOAD = ACCEPTABLE | FAIL
TA_INSTRUCTOR_WORKLOAD = ACCEPTABLE | FAIL
ASSESSMENT_COMPONENT_OVERLAP = ACCEPTABLE | FAIL
REPORT_ORAL_BOUNDARY = CLEAR | N/A | FAIL
DATA_METHOD_CONSTRAINTS = REALISTIC | N/A | FAIL
REPRODUCIBILITY_BURDEN = PROPORTIONATE | FAIL
AI_POLICY_CONSISTENCY = PASS | N/A
```

A visually good document cannot compensate for invalid or excessive assessment design.

---

# 4. Gate C — audience and layer separation

Required:

```text
AUDIENCE = <specific student group>
READER_TASK = <action/understanding>
STUDENT_INCLUDE_SET = FROZEN
STUDENT_EXCLUDE_SET = FROZEN
INSTRUCTOR_MATERIAL_LEAKAGE = NONE
IMPLEMENTATION_QA_LEAKAGE = NONE
INTERNAL_MACHINE_LANGUAGE = NONE
PUBLIC_RUBRIC_GRANULARITY = APPROVED
STUDENT_RELEASE_SET = SEPARATE
INSTRUCTOR_RELEASE_SET = SEPARATE
QA_EVIDENCE_SET = SEPARATE
```

Student materials must not expose internal approval state, marker codes, atomic grading ledgers, implementation history or QA vocabulary unless explicitly approved for student action.

---

# 5. Gate D — exact student-visible copy and source fidelity

Required:

```text
APPROVED_BODY_PARITY = PASS
EXECUTOR_AUTHORED_VISIBLE_COPY = NONE
DATES_WEIGHTS_POINTS_PARITY = PASS
POINT_TOTAL = CORRECT
FILENAMES_COMMANDS_PARITY = PASS
FORMULAS_PARITY = PASS
TABLE_CELL_PARITY = PASS
QUESTION_CROSS_REFERENCES = CONSISTENT
OFFICIAL_SOURCE_LABELS = VERBATIM_WHERE_REQUIRED
CHAPTER_SECTION_TITLES = SOURCE_FAITHFUL | N/A
POLICY_QUOTE_TEXT_PARITY = PASS | N/A
POLICY_ATTRIBUTION_PARITY = PASS | N/A
LINK_LABELS_TARGETS_PARITY = PASS | N/A
LIFECYCLE_WORDING = APPROPRIATE
```

Any semantic change returns to human content approval.

---

# 6. Gate E — information architecture and scoring transparency

Required:

```text
STABLE_BLOCK_IDS = PASS
SEMANTIC_ZONE_MAP = PASS
BLOCK_ORDER = APPROVED
RULES_ASSESSED_POLICY_SEPARATION = PASS
SCORED_COMPONENTS_SUM_TO_TOTAL = YES | N/A
PENALTIES_DISTINCT_FROM_BASE_SCORE = CLEAR | N/A
PUBLIC_SCORING_LEVEL = APPROVED
TASK_DUE_WEIGHT_DELIVERABLES_DISCOVERABLE = PASS
SOURCE_FILE_ORDER_NOT_USED_AS_DOCUMENT_ORDER = PASS
```

For Homework:

- questions/tasks dominate;
- every scored component appears in the assessed sequence;
- administrative rules do not obscure the task.

For Project:

- task/components precede administrative detail;
- method/data rules do not become a pre-solved answer key;
- broad public mark allocation is clear without leaking atomic marker machinery.

---

# 7. Gate F — document-family and visual-semantics authority

Before implementation:

```text
DOCUMENT_FAMILY_CONTRACT = FROZEN
PAGE_COUNT_MODE = HARD | PREFERRED | FREE
PAGE_COUNT_TARGET =
FLOW_ZONES = FROZEN
LEGAL_BREAKPOINTS = FROZEN
FORBIDDEN_BREAKPOINTS = FROZEN
KEEP_TOGETHER_BLOCKS = FROZEN
TYPOGRAPHY_TOKENS = FROZEN
TABLE_FORM_QUOTE_ROLES = FROZEN
ALLOWED_LAYOUT_FALLBACKS = FROZEN
FORBIDDEN_LAYOUT_FALLBACKS = FROZEN
```

Renderer may not invent new layout strategy after production begins.

---

# 8. Gate G — component and representative proofs

Required for major/high-risk/new document families:

```text
COMPONENT_PROOF_REQUIRED = YES | NO
COMPONENT_PROOF_PASS = YES | N/A
REPRESENTATIVE_PROOF_REQUIRED = YES | NO
REPRESENTATIVE_PROOF_PASS = YES | N/A
COMPONENT_LOCKS_CREATED = YES | N/A
GOLDEN_BLOCK_PAGE_LOCKS_CREATED = YES | N/A
```

Proof set should cover all relevant high-risk structures: metadata, questions, scoring/penalty tables, policy quotation, form fields, dense/sparse pages and template routes.

A full artifact must not be the first visual prototype when the risk/history warrants proof stages.

---

# 9. Gate H — Prebuild Critic

Required when task is `NEW_MAJOR`, `MAJOR_REVISION` or `FAILED_VERSION_RECOVERY`.

```text
PREBUILD_CRITIC_REQUIRED = YES | NO
CRITIC_CONTEXT_FRESH = YES | N/A
CRITIC_READ_ONLY = YES | N/A
CRITIC_SOURCE_HISTORY_COVERAGE = PASS | N/A
CRITIC_ASSESSMENT_VALIDITY = PASS | N/A
CRITIC_STUDENT_WORKLOAD = PASS | N/A
CRITIC_TA_INSTRUCTOR_WORKLOAD = PASS | N/A
CRITIC_STUDENT_EXECUTABILITY = PASS | N/A
CRITIC_AUDIENCE_BOUNDARY = PASS | N/A
CRITIC_SCORING_PENALTY = PASS | N/A
CRITIC_VISUAL_AUTHORITY = PASS | N/A
CRITIC_CONTROLLER_PLAN = PASS | N/A
CRITIC_P0_COUNT = 0 | N/A
CRITIC_P1_COUNT = 0 | N/A
```

Any major Planner amendment after PASS requires a new fresh Critic pass.

---

# 10. Gate I — proof-carrying bounded implementation

Every candidate must include:

```text
CANDIDATE_ID =
PARENT_CANDIDATE_ID =
BASELINE_COMMIT =
MODIFIED_BLOCK_IDS = []
MODIFIED_COMPONENT_IDS = []
ADDRESSED_FEEDBACK_IDS = []
UNCHANGED_LOCKED_BLOCK_IDS = []
VISIBLE_COPY_CHANGES = []
AUTHORIZED_DEPENDENCY_INVALIDATIONS = []
OPEN_ITEMS_BEFORE = []
OPEN_ITEMS_AFTER = []
```

Required:

```text
MODIFIED_IDS_SUBSET_OF_ALLOWLIST = YES
UNRELATED_SOURCE_CHANGES = 0
UNRELATED_RENDER_CHANGES = 0
CLOSED_GUARD_RECURRENCES = 0
LOCKED_CONTENT_PRESERVED = YES
LOCKED_COMPONENTS_PRESERVED = YES
```

---

# 11. Gate J — deterministic implementation QA

Fresh read-only Auditor required.

```text
DETERMINISTIC_AUDITOR_FRESH = YES
DETERMINISTIC_AUDITOR_READ_ONLY = YES
AUTHORITY_HASHES_MATCH = YES
APPROVED_COPY_PARITY = PASS
BLOCK_ORDER_COUNT_PARITY = PASS
DATES_WEIGHTS_POINTS_PARITY = PASS
FORMULA_GLYPH_PARITY = PASS
LINK_CITATION_PARITY = PASS | N/A
PACKAGE_STRUCTURE = PASS | N/A
STUDENT_INSTRUCTOR_LEAKAGE = ZERO
LOCKED_ASSET_HASHES = PASS
PDF_DOCX_STRUCTURE = PASS
SEARCHABLE_TEXT = PASS
KNOWN_BAD_BASELINES_REJECTED = YES | N/A
VALIDATOR_EDITED_DURING_CANDIDATE = NO
DETERMINISTIC_VERDICT = PASS
```

A same-context Producer self-test is not authoritative deterministic acceptance.

---

# 12. Gate K — rendered-artifact review

Fresh read-only Reviewer inspects actual renders.

Required review dimensions:

```text
ALL_IN_SCOPE_PAGES_REVIEWED = YES
WHOLE_DOCUMENT_SEQUENCE_REVIEWED = YES
FIRST_TIME_STUDENT_READING_PATH = PASS
HIERARCHY_SCANABILITY = PASS
BODY_LEADING_CONSISTENCY = PASS
PARAGRAPH_LIST_TABLE_RHYTHM = PASS
SEMANTIC_PROXIMITY = PASS
PAGE_FLOW_AND_DENSITY = PASS
NO_ARTIFICIAL_WHITESPACE = PASS
NO_PAGE_COUNT_DRIVEN_COMPRESSION = PASS
FORMS_ACTUALLY_USABLE = PASS | N/A
TABLES_ACTUALLY_READABLE = PASS
QUOTATION_ATTRIBUTION_VISUALLY_DISTINCT = PASS | N/A
COURSE_DOCUMENT_FAMILY = PASS
NO_OBVIOUS_USER_DEBUGGING_REQUIRED = PASS
RENDERED_REVIEW_VERDICT = PASS
```

No-clipping/no-overflow is necessary but insufficient.

---

# 13. Gate L — GPT Work

For major/new/recovery candidates:

```text
GPT_WORK_REQUIRED = YES
GPT_WORK_CONTEXT_INDEPENDENT = YES
GPT_WORK_SCOPE = ALL_STUDENT_PAGES + RELEVANT_FORMS_TEMPLATES
GPT_WORK_FIRST_TIME_STUDENT_TEST = PASS
GPT_WORK_READER_EFFORT = PASS
GPT_WORK_INFORMATION_ARCHITECTURE = PASS
GPT_WORK_VISUAL_RHYTHM = PASS
GPT_WORK_WORKLOAD_CLARITY = PASS
GPT_WORK_AUDIENCE_BOUNDARY = PASS
GPT_WORK_CUMULATIVE_GUARDS = PASS
GPT_WORK_VERDICT = PASS
```

For minor bounded revisions, a scoped GPT Work review is allowed only when global copy/structure/components remain locked and full-document sequence is still reviewed at contact-sheet level.

GPT Work cannot override deterministic or Critic failures.

---

# 14. Gate M — user review

Only internally accepted candidates reach the user.

```text
USER_IS_FIRST_QA = NO
USER_REVIEW_PACKAGE_STAGE_SPECIFIC = YES
INTERNAL_LOGS_EXCLUDED = YES
GENUINE_USER_DECISIONS_ONLY = YES
HUMAN_REVIEW_BUDGET_RESPECTED = YES
READY_FOR_USER_REVIEW = YES
```

For A/B review, both options must already pass all preceding applicable gates.

User verdict:

```text
USER_ACCEPTED = YES | NO
USER_SELECTED_OPTION = <id or N/A>
NEW_HUMAN_LOCKS_CREATED = YES | NO
```

---

# 15. Gate N — revision monotonicity

For every accepted revision:

```text
OPEN_FEEDBACK_NEXT_STRICT_SUBSET = YES
LOCKED_BLOCKS_NEXT_SUPERSET = YES
LOCKED_COMPONENTS_NEXT_SUPERSET = YES
MODIFIED_IDS_SUBSET_OF_ALLOWLIST = YES
UNRELATED_SOURCE_CHANGES = 0
UNRELATED_RENDER_CHANGES = 0
CLOSED_GUARD_RECURRENCES = 0
```

If not satisfied, reject the round and perform root-cause review before another candidate.

A repeated closed-guard recurrence stops project-local patching and routes repair to the shared Research Authoring generator/validator/reviewer layer.

---

# 16. Gate O — final full-artifact regression

Before release, rerun on the exact delivery artifact:

```text
FINAL_SOURCE_COMMIT_BOUND = YES
FINAL_ARTIFACT_HASHES_BOUND = YES
ALL_STUDENT_PAGES_REVIEWED = YES
ALL_ACTIVE_FEEDBACK_CLOSED_OR_EXPLICITLY_DEFERRED = YES
ALL_HUMAN_LOCKS_PRESERVED = YES
FINAL_COPY_PARITY = PASS
FINAL_FORMULA_TABLE_LINK_PARITY = PASS
FINAL_VISUAL_REGRESSION = PASS
FINAL_PACKAGE_LEAKAGE = ZERO
FINAL_TEMPLATE_ROUTE_CHECKS = PASS | N/A
NATIVE_WORD_OFFICE_CHECK = PASS | N/A
FINAL_REPRODUCIBILITY_CHECK = PASS
FINAL_GPT_WORK_REGRESSION = PASS | N/A
```

Delta review never replaces final whole-document regression.

---

# 17. Gate P — release closure

Student, instructor and QA packages remain separate.

```text
STUDENT_RELEASE_CONTENTS = APPROVED
INSTRUCTOR_RELEASE_CONTENTS = APPROVED | N/A
QA_EVIDENCE_EXCLUDED_FROM_STUDENT_PACKAGE = YES
FILENAMES = PASS
PACKAGE_ROOT_STRUCTURE = PASS | N/A
LINKS_FORMS = PASS
BLACKBOARD_OR_PUBLICATION_AUTHORIZED = YES
READY_FOR_RELEASE = YES
RELEASED = YES | NO
```

No artifact is released merely because it is user-accepted.

---

# 18. Completion state machine

Allowed forward states:

```text
SOURCE_HISTORY_FROZEN
AUDIENCE_ASSESSMENT_FROZEN
CONTENT_DRAFTED
CONTENT_USER_APPROVED
PREBUILD_CRITIC_PASS
COMPONENT_PROOF_PASS
REPRESENTATIVE_PROOF_PASS
CANDIDATE_MATERIALIZED
DETERMINISTIC_QA_PASS
RENDERED_REVIEW_PASS
GPT_WORK_PASS
READY_FOR_USER_REVIEW
USER_ACCEPTED
FINAL_REGRESSION_PASS
RELEASE_READY
RELEASED
```

A regression returns the artifact to the earliest affected state.

---

# 19. Mandatory stop conditions

Stop and return to Planner when:

- source/history is incomplete;
- assessment meaning is ambiguous;
- student/instructor boundary is unresolved;
- approved copy does not fit under frozen constraints;
- no candidate passes the approved internal search space;
- independent validation cannot be guaranteed;
- a closed guard recurs;
- open feedback fails to decrease;
- a validator/reviewer defect is discovered;
- user review budget would be exceeded by another speculative candidate.

Required stop result:

```text
STOP_PLANNER_DECISION_REQUIRED = YES
READY_FOR_USER_REVIEW = NO
READY_FOR_RELEASE = NO
```


---

# 20. Gate Q — deterministic / rendered-review ownership integrity

Before accepting a validator/reviewer stack, confirm:

```text
OBJECTIVE_GATES_IN_DETERMINISTIC_VALIDATOR = YES
SUBJECTIVE_COMPOSITION_GATES_IN_RENDER_REVIEW = YES
ARBITRARY_DENSITY_THRESHOLDS_AS_HARD_GATES = NO
KNOWN_BAD_OBJECTIVE_FAILURES_REJECTED = YES
ZERO_SURVIVOR_ROOT_CAUSE_REVIEW = PASS | N/A
```

Page occupancy, bottom blank area and adjacent-page density may be logged as diagnostics. They may become hard gates only when explicitly calibrated to an accepted family baseline or when they protect an objective usability failure.

If a bounded candidate search returns zero survivors because every candidate fails the same aesthetic-density threshold, acceptance stops and the Planner must repair the gate ownership before more production. Do not expand the parameter grid until this review is complete.

A rendered Reviewer may still reject a deterministic PASS candidate for poor whitespace, rhythm, scanability or reader effort.


# 21. Gate R — annotation and editorial-fidelity acceptance

For annotated-PDF revisions and lecture-source-grounded assessment copy, require:

```text
ANNOTATION_OBJECTS_EXTRACTED = YES | N/A
STRIKEOUTS_APPLIED_OR_EXPLICITLY_SUPERSEDED = YES | N/A
HIGHLIGHTS_MAPPED_TO_CURRENT_BLOCKS = YES | N/A
ANNOTATION_COMMENTS_CONSUMED = YES | N/A
DIRECT_USER_SUPERSESSIONS_RECORDED = YES | N/A
STUDENT_TERMINOLOGY_FIDELITY = PASS
UNAPPROVED_SOFTWARE_SHORTHAND = NONE
REDUNDANT_STUDENT_PROSE = NONE
GRATUITOUS_DISPLAY_MATH = ZERO
TITLE_HIERARCHY = PASS
QUESTION_HEADING_BODY_GAP_CONSISTENCY = PASS
```

A visually polished render fails this gate if it reintroduces struck-out prose, invents course terminology not used by the canonical source, or uses unnecessary display mathematics that degrades reading flow.


# 22. Gate S — unmarked-copy preservation

For a revision driven by an annotated baseline:

```text
ANNOTATED_BASELINE_BOUND = YES
UNMARKED_COPY_PRESERVATION = PASS
UNMARKED_COPY_LOSS_COUNT = 0
STRIKEOUT_DISPOSITIONS = CLOSED
HIGHLIGHT_COMMENT_DISPOSITIONS = CLOSED
DIRECT_SUPERSESSIONS_RECORDED = YES
```

Any unmarked reader-visible baseline copy that disappears must have an explicit source/user/Planner authority. A general instruction to simplify the document or a `MAJOR_REVISION` classification is not sufficient authority for silent deletion.
