# Student Assessment Research Authoring — HW1 / Final Project Postmortem and Non-Recurrence Plan V1

Date: 2026-10-07  
Status: **PROMOTE_NOW / BINDING DESIGN INPUT FOR THE SHARED RUNBOOK**  
Primary evidence: repeated STAT5060 HW1 student-PDF revisions and the rejected STAT5060 Final Project student Guide

## 1. Why this postmortem exists

The STAT5060 HW1 and Final Project work repeatedly produced technically valid artifacts that were not acceptable to the instructor/user. The failures were not caused by one weak sentence or one difficult TeX page. They came from a production system that repeatedly made the user perform routine audience, visual and regression QA.

The core failure was:

> The workflow protected files, tests and local change scope more reliably than it protected reader purpose, accepted style, relational consistency and actual visual quality.

A student-facing artifact can be statistically correct, searchable, unclipped, reproducible and heavily tested while still being wrong because it is written for the wrong audience, contains the wrong layer of information, breaks accepted document-family style, or reaches the user before independent reader review.

This postmortem records what actually failed, the root cause behind each class, and the mandatory workflow changes for HW2, the Final Project and future student-facing assessment material.

---

## 2. Failure inventory

### 2.1 Source and authority failures

Observed failures:

- a provisional HW1 due date was rendered after a course-wide frozen timetable already existed;
- the Final Project Guide introduced a contingency oral date that had not been approved;
- the Guide introduced consultation routes and method-specific guidance that were not part of the approved student-facing design;
- later revisions sometimes read the previous generated artifact more carefully than the underlying course authority;
- complete raw highlights and direct user decisions were not always reread before the next revision.

Root cause:

- the authority bundle was incomplete or stale;
- source priority was not explicit;
- a generated candidate was treated as a design source rather than an implementation to re-judge;
- there was no mandatory conflict matrix proving that timetable, assessment authority, approved body and current artifact agreed before implementation.

Non-recurrence requirement:

- bind exact canonical source files and hashes before planning;
- create an authority-priority table;
- fail before drafting when two authorities disagree;
- never use a prior generated student artifact as sole semantic authority.

### 2.2 Audience and information-layer failures

Observed failures:

- the Final Project Guide read like an internal policy, method-reference and marking manual;
- atomic rubric items, internal codes, rejected implementation alternatives and QA-era language leaked into student material;
- the Guide explained method eligibility in a way that partially solved the course-selection judgment for postgraduate students;
- student, instructor and QA materials were mixed in review/release bundles;
- excessive true information was included because it existed in the source bundle, not because students needed it.

Root cause:

- the process asked “what is in the sources?” rather than “what does this reader need to act correctly?”;
- no formal student include/exclude set existed before drafting;
- completeness was mistaken for maximal disclosure.

Non-recurrence requirement:

- freeze audience, reader task, include set and exclude set before content drafting;
- require a source-to-reader disposition map;
- separate student, instructor, implementation and QA deliverables before production begins.

### 2.3 Assessment-semantic and information-architecture failures

Observed failures:

- a scored 5-point component was visually embedded among ungraded HW1 rules;
- the stated total was 100 while Questions 1–4 visibly totalled 95;
- after Question 5 was introduced, the report-format rule still referred to “Questions 1–4”;
- the first pages of Homework were dominated by submission/admin rules instead of a clear student workflow;
- Final Project scoring transparency was confused with publication of the full internal atomic rubric;
- student instructions followed repository/frozen-file order instead of student action order.

Root cause:

- semantic classes were not frozen before layout;
- exact-copy preservation was applied without relational consistency checks;
- the workflow lacked a dependency graph for totals, ranges, section references and filenames;
- scored content and rules were not treated as distinct zones.

Non-recurrence requirement:

- assign stable BlockIDs and semantic classes before rendering;
- freeze a relational-invariant ledger, including totals, question ranges, section references and file counts;
- deterministic QA must check both exact-copy locks and relational consistency;
- all scored components must appear in the assessed sequence unless the instructor explicitly approves another presentation.

### 2.4 Course-family and positive-baseline failures

Observed failures:

- early HW1 redesigns drifted toward card/dashboard/corporate styling rather than the original restrained academic assignment family;
- title, metadata, due-date and weight layout were repeatedly reinvented;
- line spacing, paragraph spacing and list spacing varied between versions;
- later local fixes sometimes changed global macros or page rhythm outside the target.

Root cause:

- the original accepted style was not bound as a positive baseline before modernization;
- component style was inferred from the latest candidate rather than proved from the course family;
- semantic, copy, component and visual locks were not separated early enough.

Non-recurrence requirement:

- recover and freeze a positive document-family baseline before implementation;
- prove title/metadata, question, subpart, table, quote, footer and typography components before full production;
- any deviation from the family requires an explicit reader-need decision, not executor taste.

### 2.5 Page-count and composition-authority failures

Observed failures:

- one-page and two-page targets were frozen before feasibility was established;
- an explicit hard break was introduced after Report format despite a prior user decision that rules should flow continuously through AI assistance;
- a large `Needspace` later recreated an effective hard break while nominally satisfying “no hard break”;
- the Page-limit paragraph was separated from its table and consequence sentence;
- the AI policy oscillated between cramped one page and sparse two pages;
- candidate searches changed small spacing values while the actual unresolved issue was the semantic page-break/archetype decision.

Root cause:

- hard page-count targets were treated as Planner preferences rather than constraints requiring feasibility proof;
- legal breakpoints and keep-together units were not proved before full rendering;
- the workflow searched micro-spacing before resolving the composition archetype;
- implementation controls such as `Needspace` were not tested for semantic equivalence to forbidden hard breaks.

Non-recurrence requirement:

- before hard-freezing page count, produce a measurement render under the frozen copy and family typography;
- prove that at least one legal composition exists;
- choose semantic page archetypes before micro-spacing search;
- treat effective-break controls as equivalent to explicit hard breaks for acceptance purposes;
- if one-page versus two-page remains ambiguous, compare only already valid alternatives.

### 2.6 Revision and preservation failures

Observed failures:

- fixing one page reopened accepted spacing or content elsewhere;
- each round tended to focus on the latest user comment and could forget earlier accepted decisions;
- “preserve exact copy” retained a stale cross-reference after the assessed structure changed;
- local layout repairs were sometimes implemented by regenerating broad source sections;
- user-rejected routes were not always encoded as persistent recurrence guards before the next implementation.

Root cause:

- preservation maps were incomplete;
- dependencies between a changed block and related copy were not declared;
- feedback memory remained partly conversational rather than machine-readable;
- bounded revision existed as prose but was not always enforced by source/render allowlists.

Non-recurrence requirement:

- maintain cumulative feedback and lock registries keyed by stable BlockID/component;
- distinguish exact-copy locks from relational invariants;
- require a proof-carrying patch manifest;
- changes outside the explicit allowlist fail before visual review;
- all guarded historical items must be revalidated on every candidate.

### 2.7 Validator and acceptance-design failures

Observed failures:

- arbitrary page occupancy and bottom-blank thresholds were encoded as deterministic hard gates;
- all otherwise relevant candidates could be eliminated by uncalibrated aesthetic thresholds;
- zero survivors were initially interpreted as a document/layout impossibility rather than a validator-ownership defect;
- metrics could trigger while the same report still declared visual PASS;
- validators were developed during the same evolving task, creating risk that they encoded the current preferred answer rather than stable acceptance meaning.

Root cause:

- objective correctness and aesthetic quality were not separated;
- thresholds were not calibrated against accepted positive controls;
- validator validity was not independently established before candidate production;
- acceptance standards changed too late in the production cycle.

Non-recurrence requirement:

- deterministic validators own objective conformance only;
- rendered reviewers own whitespace, rhythm, balance and reader effort;
- aesthetic metrics are diagnostics unless calibrated to accepted family baselines or objective usability failures;
- acceptance standard and validator version freeze before candidate generation;
- every validator must reject known-bad controls and accept at least one known-good or synthetic-valid control before it governs a real candidate;
- zero survivors from one failure family trigger gate-ownership review before any wider search.

### 2.8 Review-independence and user-workload failures

Observed failures:

- Codex produced artifacts and then reported its own visual PASS;
- obvious visual defects reached the user repeatedly;
- the user became the first real reader and spacing debugger;
- intermediate candidates and large QA packages were exposed when only a student artifact decision was needed;
- GPT Work and truly independent reader review were introduced too late.

Root cause:

- Producer evidence was mistaken for independent acceptance;
- user-review budget was not treated as a protected resource;
- review-package scope was not filtered to the user’s actual decision.

Non-recurrence requirement:

- fresh read-only deterministic and rendered review after Producer stops;
- GPT Work for major/recovery final reader-effort review;
- user receives only independently accepted artifacts or two already acceptable alternatives;
- intermediate candidates stay internal;
- default bounded-revision human-review budget is one final acceptance review.

### 2.9 Task-proportionality and governance failures

Observed failures:

- a simple HW1 front matter accumulated many local version prompts and increasingly large governance files;
- control-plane work expanded while the visible artifact remained unresolved;
- repeated micro-revisions were attempted after the root cause had moved to authority/validator design;
- the process sometimes became more complex than the document.

Root cause:

- failure recovery was added incrementally instead of restarting from a clean classified workflow;
- there was no governance-budget or artifact-first stop rule;
- each new failure created another local patch rather than triggering incident consolidation.

Non-recurrence requirement:

- classify the task once and choose the smallest adequate process;
- after a closed guard recurs or two broad rounds fail to reduce open issues, stop local versioning and perform root-cause incident review;
- one consolidated authority supersedes old prompts;
- governance work must lead directly to a visible proof milestone;
- do not create another project-local version unless the previous authority has been explicitly retired and the new root cause is stated.

---

## 3. Root-cause summary

The repeated failures can be reduced to seven shared root causes:

1. **wrong authority timing** — source, audience, copy, composition and acceptance were not frozen in the correct order;
2. **wrong semantic unit** — files and pages were treated as primary when stable reader-facing blocks and relationships should have been primary;
3. **missing positive baseline** — the accepted original course style was not protected before redesign;
4. **premature hard constraints** — page count and visual thresholds were frozen before feasibility/calibration;
5. **trust-boundary failure** — Producer self-review and uncalibrated validators were allowed to approximate acceptance;
6. **incomplete regression model** — exact-copy checks existed without relational and cumulative-feedback checks;
7. **user-as-QA** — internal convergence and filtered review happened too late.

---

## 4. Mandatory runbook amendments

The shared student-assessment runbook must include and enforce the following additions.

### 4.1 Positive-baseline freeze

Before visual redesign or modernization:

```text
POSITIVE_STYLE_BASELINE = exact accepted artifact(s)
POSITIVE_COMPONENTS = title / metadata / typography / questions / tables / footer / quote / form
ALLOWED_DEVIATIONS = explicit list
```

A rejected latest candidate cannot silently replace the positive baseline.

### 4.2 Authority coherence matrix

Before Critic or implementation:

| Field | Canonical owner | Current value | Conflicts | Resolution |
|---|---|---|---|---|
| due date | timetable | ... | ... | ... |
| weight/points | assessment authority | ... | ... | ... |
| student body | approved copy | ... | ... | ... |
| page-count mode | composition authority | ... | ... | ... |
| public rubric granularity | assessment authority | ... | ... | ... |

Any unresolved conflict blocks implementation.

### 4.3 Relational-invariant ledger

Freeze and validate relationships, not only strings:

```text
question_range = Q1-Q5
total_points = sum(component_points) = 100
required_file_count = stated count = listed count
page-limit consequence references correct subtotal
section/table/figure references resolve
milestone/final lifecycle wording matches artifact stage
```

### 4.4 Constraint-satisfiability proof

Before hard-freezing page count or layout constraints:

```text
FROZEN_COPY_RENDERED = YES
FROZEN_FAMILY_TYPOGRAPHY_APPLIED = YES
AT_LEAST_ONE_LEGAL_COMPOSITION_EXISTS = YES
HARD_CONSTRAINTS_MUTUALLY_COMPATIBLE = YES
```

If not, Planner decides among page count, information architecture or explicitly authorised typography changes before production.

### 4.5 Composition-archetype proof before micro-spacing search

First compare meaningful structures, for example:

- one-page versus two-page rules;
- semantic break after Block A versus Block B;
- top-aligned versus deliberately distributed short page;
- table inline versus dedicated compact block.

Only after selecting/proving an archetype may the Producer search small spacing values.

### 4.6 Validator calibration and ownership

Before candidate production:

```text
VALIDATOR_VERSION_FROZEN = YES
KNOWN_BAD_CONTROLS_REJECTED = YES
KNOWN_GOOD_OR_SYNTHETIC_VALID_CONTROLS_ACCEPTED = YES
OBJECTIVE_GATES_ONLY = YES
AESTHETIC_METRICS_ARE_DIAGNOSTIC = YES
```

A zero-survivor result concentrated in one aesthetic failure class invalidates the gate design until reviewed.

### 4.7 Mandatory independent review ladder

```text
Prebuild Critic
-> Producer
-> deterministic Auditor
-> rendered Reviewer
-> GPT Work when major/recovery
-> user final acceptance
```

A major Planner amendment requires a fresh Critic.

### 4.8 Human-review budget

Before production:

```text
HUMAN_REVIEW_BUDGET = one final acceptance review
USER_IS_FIRST_QA = NO
```

A candidate with obvious copy, spacing, hierarchy, block-split or consistency defects is not user-reviewable.

### 4.9 Incident escalation

Trigger a consolidated incident/recovery restart when any:

- a closed guard recurs;
- open issues do not decrease;
- two broad rounds fail;
- validator/reviewer ownership is disputed;
- user-review budget is being consumed by routine defects;
- governance versions proliferate without a visible accepted proof.

Do not continue ordinary local revision after escalation.

### 4.10 Artifact-first checkpoint

Every substantial workflow must declare the next visible proof milestone and deadline/order:

```text
approved body
-> component proof
-> representative proof
-> full candidate
```

Governance work that does not unblock the next visible proof is deferred.

---

## 5. Mandatory startup plan for STAT5060 HW2

HW2 should begin as `NEW_MAJOR`, not as a copy/edit of HW1.

Before Codex:

1. read syllabus, lecture coverage, old HW2, timetable and current course policy;
2. freeze assessment purpose, workload and required student evidence;
3. recover the positive course-family style from the finally accepted HW1;
4. create source-to-reader and student/instructor/QA separation maps;
5. draft the complete student-visible body;
6. run Prebuild Critic on validity, workload and executability;
7. obtain user approval of the complete body;
8. prove title/metadata, question, table and rule components using real HW2 content;
9. render representative dense/sparse/question pages;
10. use one Controller Goal for production, deterministic audit, rendered review and repair;
11. run GPT Work before user final acceptance;
12. lock the accepted HW2 before solution/rubric/release work can change it.

HW2 must not inherit rejected HW1 layout history. It inherits only the accepted course-family components and generic regression guards.

---

## 6. Mandatory restart plan for the STAT5060 Final Project

The Final Project is `FAILED_VERSION_RECOVERY` because the student Guide was repeatedly rejected and has substantial historical decisions.

Before resuming:

1. bind the approved student-visible body and all frozen assessment decisions;
2. recover every highlight/direct decision and map it to stable BlockIDs;
3. explicitly retire internal/student-guide content that must not return;
4. bind the accepted Homework/course-family visual components without forcing Homework information architecture onto a Project Guide;
5. run a fresh Prebuild Critic covering assessment validity, student/TA workload, public rubric granularity, penalty consistency, template fairness, package burden, report/oral boundary and AI policy;
6. prove high-risk components: first-page summary, dates, public marks, method/data boundary, penalty table, AI/oral block, milestone form and three template routes;
7. obtain user approval of the complete student-visible body before render;
8. produce representative pages/forms/templates before a full Guide/package;
9. run one Controller Goal with fresh Auditor/Reviewer cycles;
10. run GPT Work over all student-facing artifacts;
11. give the user only the independently accepted student review set;
12. after user acceptance, lock student artifacts before reviewing instructor rubric and grading assistance.

---

## 7. Promotion and replay tests

The workflow is not mature until it demonstrates:

- accepted HW1 style/content survives final local repair;
- HW2 reaches a usable first candidate without the HW1 revision pattern;
- Final Project excludes internal material and closes all historical highlights;
- a stale cross-reference mutation is caught;
- an arbitrary aesthetic threshold cannot eliminate all valid candidates unnoticed;
- a Producer-added sentence is rejected;
- a local repair leaves unrelated blocks and components unchanged;
- GPT Work catches a seeded reader-effort defect after deterministic PASS;
- user receives no obvious routine QA defect;
- student/instructor/QA packages remain separate through release.

---

## 8. Final non-recurrence principles

1. Bind the correct source and positive style baseline before designing.
2. Freeze assessment meaning and complete student-visible copy before rendering.
3. Protect relationships and totals, not only exact strings.
4. Prove page-count feasibility before making it a hard constraint.
5. Choose composition archetypes before micro-spacing.
6. Keep objective validation and aesthetic review in separate trust layers.
7. Treat historical highlights as cumulative guarded requirements.
8. Preserve accepted regions through layered locks and explicit dependency invalidation.
9. Stop ordinary revision when open issues do not decrease.
10. The user chooses among acceptable outcomes; the user does not debug routine failures.
