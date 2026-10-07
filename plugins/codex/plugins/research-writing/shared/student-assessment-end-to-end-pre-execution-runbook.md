# Student Assessment Research Authoring End-to-End Pre-Execution Runbook

Status: **CANONICAL CANDIDATE / MUST READ IN FULL BEFORE EVERY NON-TRIVIAL STUDENT-FACING HOMEWORK OR PROJECT TASK**  
Applies to: Homework briefs, Project Guides, milestone/proposal forms, student policy sheets, submission instructions, report templates, student oral-defense briefs, and later revisions of those artifacts  
Companion acceptance contract: `student-assessment-cumulative-acceptance-contract.md`

This runbook is the complete operating procedure for student-facing assessment authoring under Research Authoring.

It exists because repeated STAT5060 HW1 and Final Project failures showed that isolated correctness rules are not enough. A document can be statistically correct, searchable, unclipped, reproducible, hash-stable and heavily tested, yet still fail because:

- it was written for the instructor or marker rather than the student;
- internal policy, rubric, QA or implementation language leaked into the student artifact;
- the document exposed too much true but irrelevant information;
- source-file order became student-document order;
- scoring information was visually mixed with ordinary rules;
- Codex improvised copy, page breaks, spacing or document-family style;
- a local revision regenerated accepted regions;
- the latest round forgot earlier highlights and direct user decisions;
- the Producer validated its own work;
- obvious visual failures reached the user first.

The rule from now on is:

> **Before any non-trivial student-facing Homework or Project task begins, read this runbook in full, then read the cumulative acceptance contract. Only then may planning, Critic review, implementation, revision, user review or release work start.**

No task-local prompt, course-specific skill or later workflow may weaken this runbook. Course-specific authority may add requirements.

---

# 1. Core objective

The workflow must optimize four things simultaneously:

1. **assessment quality** — the task measures the intended statistical, mathematical, scientific or professional capability;
2. **student usability** — the intended student can identify what to do, what to submit, what counts, when it is due and what evidence is required without decoding internal process;
3. **document quality** — information architecture, hierarchy, typography, spacing, tables, forms, page flow and course-family identity are deliberate;
4. **revision efficiency** — accepted content and visual regions remain accepted, obvious defects are solved internally, and the user is not routine QA.

Infrastructure exists to support a good student artifact. Once enough authority is frozen, production must move to visible proofs and a real candidate. Do not spend open-ended time extending governance while no useful artifact appears.

---

# 2. Mandatory first-step output

Before substantive work, the Planner/Controller must determine and be able to report:

```text
RUNBOOK_READ = YES
CUMULATIVE_ACCEPTANCE_CONTRACT_READ = YES
TASK_CLASSIFICATION =
ARTIFACT_FAMILY =
COURSE / PROJECT =
DELIVERABLE_FORMAT =
AUDIENCE =
READER_TASK =
ASSESSMENT_PURPOSE =
EXACT_BASELINE =
SOURCE_SET =
HISTORY_SCOPE =
CURRENT_FREEZE_LEVEL =
ACTIVE_GLOBAL_GUARDS =
LOCKED_BLOCK_IDS =
LOCKED_COMPONENTS =
IN_SCOPE_BLOCK_IDS =
ROUND_ALLOWLIST =
PREBUILD_CRITIC_REQUIRED =
GPT_WORK_REQUIRED =
USER_IS_FIRST_QA = NO
HUMAN_REVIEW_BUDGET =
```

If these fields cannot be determined, the next action is source/history recovery or Planner clarification, not document production.

---

# 3. Task classification

Classify before authoring.

## 3.1 `NEW_SMALL`

Use only when all are true:

- the artifact is short and low-risk;
- assessment meaning is already frozen;
- source, audience and deliverables are clear;
- no complex annotation/revision history exists;
- an accepted course document family already exists;
- no high-stakes policy, scoring or workload decision is being introduced.

A separate prebuild Critic is optional.

## 3.2 `NEW_MAJOR`

Use when a new artifact is:

- a substantial Homework or Project Guide;
- assessment-defining;
- method/data/policy heavy;
- template-defining;
- likely to require non-trivial workload, page-count, scoring-transparency or audience-boundary decisions.

A fresh prebuild Critic is required before broad implementation.

## 3.3 `MINOR_REVISION`

Minor only when **all** are true:

- assessment meaning unchanged;
- student-visible section order unchanged;
- no new requirement, score, penalty, date, exception or status;
- no document-family redesign;
- no page-count target change;
- no section split/merge;
- visible-copy changes are local, source-supported and normally confined to a few blocks;
- no closed historical guard has recurred;
- no shared generator/style root cause is suspected.

Minor work may skip the prebuild Critic, but still requires history refresh, a bounded change contract, deterministic QA, rendered review and full regression of locked regions.

## 3.4 `MAJOR_REVISION`

Major when any of the following holds:

- task or assessment structure changes;
- score/weight/rubric-publication/penalty meaning changes;
- section order or information architecture changes;
- page count or page-budget mode changes;
- student/instructor content boundary changes;
- broad copy changes span multiple sections;
- title/header/footer/table/form/template system changes;
- new document component or layout archetype is introduced;
- a fillable form is redesigned;
- repeated regression suggests the current Planner authority is wrong;
- the user asks to rethink, rebuild, reread history or stop recurring failures.

If uncertain, classify as major.

## 3.5 `FAILED_VERSION_RECOVERY`

Always major.

Required additions:

- authoritative version map;
- exact user/reviewer-seen historical artifacts;
- raw PDF highlights/annotations and direct decisions;
- feedback lifecycle and supersession;
- positive baselines;
- rejected/negative baselines;
- exact recovery scope;
- prebuild Critic;
- known-bad regression corpus;
- independent internal convergence before user review.

A failed-version recovery may not fall back to “read the latest PDF and improve it.”

---

# 4. Role separation

## 4.1 ChatGPT Web / Planner / Assessment Author

ChatGPT owns human-level assessment and communication judgment.

Responsible for:

- reading and reconciling lecture notes, syllabus, old assignments/projects, frozen decisions and current materials;
- identifying instructor-original content, later clarification and derived reorganization;
- defining intended student, assumed level and reader task;
- defining assessment purpose and capability being measured;
- checking workload, validity, fairness and student executability;
- deciding what belongs in student, instructor, implementation and QA layers;
- selecting public scoring granularity;
- freezing artifact family and information architecture;
- stable BlockIDs and semantic zones;
- exact student-visible copy;
- lifecycle-aware wording (`proposed`, `planned`, `submitted`, `completed`);
- source-faithful titles, dates, labels and terminology;
- document-family style, page-budget mode, flow zones, visual-rhythm tokens and legal page breaks;
- annotation/highlight interpretation, lifecycle and supersession;
- locks, unlocks and rejected-route guards;
- Prebuild Critic prompt;
- autonomous Codex Parent Controller Goal;
- deciding whether a finding is an assessment/specification defect or implementation defect.

ChatGPT must not be reduced to “tell Codex to make it better.”

ChatGPT does **not** own:

- TeX/Quarto/DOCX implementation;
- compilation and export;
- low-level package/build mechanics;
- deterministic validator execution;
- final pixel rendering.

## 4.2 Fresh Prebuild Critic

Fresh, read-only and independent.

Required for `NEW_MAJOR`, `MAJOR_REVISION`, `FAILED_VERSION_RECOVERY`, and any task changing assessment meaning, student workload or public scoring.

The Critic must actively try to overturn the Planner specification. It checks:

- source/history consumption;
- assessment validity;
- alignment between learning objective, task and evidence;
- actual student workload and hidden deliverables;
- TA/instructor workload;
- whether a student can understand and independently execute all requirements;
- scoring transparency versus internal grading machinery;
- penalties and duplicate deductions;
- method/data constraints;
- reproducibility burden;
- report/oral overlap;
- AI/policy consistency;
- source fidelity and stale-rule conflicts;
- student/instructor/QA separation;
- exact visible-copy completeness;
- information architecture and visual-composition authority;
- historical-regression coverage;
- Codex Controller review/repair plan.

Critic verdict:

```text
PASS
REVISE
BLOCKED_SOURCE_OR_HISTORY_NOT_CONSUMED
```

For `REVISE`, return a bounded Planner-amendment list with exact file/section, risk, minimum repair and acceptance test.

The Critic does not implement files.

A major Planner amendment after Critic review requires a new fresh Critic pass.

## 4.3 Codex Parent Controller

Owns autonomous production and internal review.

Normal topology:

```text
fresh Producer
-> Producer self-QA
-> fresh read-only deterministic Auditor
-> fresh rendered-artifact Reviewer
-> fresh Producer repair
-> new immutable candidate
-> new fresh Auditor
-> new fresh Reviewer
-> repeat until independently accepted
```

The Controller:

- binds exact authority, baseline, candidate and round scope;
- maintains stable BlockIDs and patch manifest;
- routes ordinary findings internally;
- never asks the user to relay intermediate completion blocks;
- does not make new assessment or copy decisions;
- stops only for a real Planner decision, human-only external action or proven reviewer-runtime failure.

## 4.4 Codex Producer

Owns implementation only.

Allowed:

- typeset approved copy;
- implement approved document-family components;
- choose line wrapping, widths and alignment inside frozen constraints;
- apply approved spacing tokens and legal fallbacks;
- build/render/export PDF/DOCX/HTML/Quarto/LaTeX;
- create approved forms/tables/templates from frozen specifications;
- run code and deterministic smoke tests;
- prepare a proof-carrying patch manifest;
- repair Auditor/Reviewer findings within the frozen allowlist.

Forbidden:

- decide what students need to know;
- add/delete/paraphrase student-visible prose;
- add an example, explanation, exception, date, status, penalty or consultation rule;
- reveal internal rubric/QA/process information;
- choose public rubric granularity;
- change page count or information architecture without authority;
- delete difficult content to fix layout;
- change shared components without explicit unlock;
- edit acceptance rules/validators to make the candidate pass;
- declare final acceptance.

If approved content does not fit, return a structured layout conflict. Do not solve it by writing.

## 4.5 Fresh deterministic Auditor

Fresh, read-only and independent from Producer.

Checks objective conformance:

- authority and exact baseline identity;
- exact student-visible copy;
- BlockID/order/section count;
- dates, weights, points, penalties, filenames and totals;
- formulas and mathematical glyphs;
- source-faithful official labels/titles;
- active annotation and recurrence-guard coverage;
- round allowlist and locked paths;
- student/instructor/QA release boundaries;
- template/data/starter/helper hashes;
- package/file structure;
- links, citations and quotation parity;
- PDF/DOCX structure, searchability and accessibility basics;
- page-count and semantic-block gates;
- known-bad regression fixtures.

A deterministic failure cannot be overridden by visual review.

## 4.6 Fresh rendered-artifact Reviewer

Reviews actual renders after Producer stops.

Checks:

- first-time-student reading path;
- hierarchy and scanability;
- whether task/due/weight/deliverables are quickly identifiable;
- rule versus assessed-content separation;
- semantic proximity of headings, paragraphs, tables and consequences;
- typography, line spacing, paragraph rhythm and page density;
- tables/forms at realistic print/read scale;
- fillable space and checkbox usability;
- quotations versus course-authored prose;
- cross-page flow and page-turn cost;
- document-family consistency;
- obvious audience-language problems;
- whether the artifact is genuinely ready for user acceptance rather than another debugging round.

This is internal Codex-controlled QA. It must remove routine visible defects before GPT Work or the user.

## 4.7 GPT Work

GPT Work is the final independent reader-effort, communication and assessment-usability gate for major/new/recovery candidates.

It should receive:

- exact final candidate render;
- audience contract;
- approved body and source anchors;
- cumulative annotation/guard registry;
- relevant artifact-family acceptance rubric;
- no Producer scratch narrative or expected-answer key.

For student-facing Homework/Project materials, GPT Work reviews all pages and, where relevant, all templates/forms. It judges:

- whether a first-time student can identify what to do;
- whether the document exposes only student-relevant information;
- whether hidden deliverables or workload remain;
- whether score/penalty information is understandable and internally consistent;
- whether rules, assessed content and policy are visually distinguishable;
- whether tables/forms are actually usable;
- whether visual rhythm and page flow are natural;
- whether source labels and institutional quotations are handled correctly;
- whether the artifact communicates at the intended postgraduate level;
- whether student and instructor artifacts remain separate.

For a truly minor bounded revision, GPT Work may review changed blocks, affected component consumers, minimum context pages and a full-document contact sheet only when global structure and copy are locked.

GPT Work does not:

- implement fixes;
- invent copy;
- decide assessment meaning;
- override deterministic failures;
- convert an incomplete scope into a global PASS.

## 4.8 User / Instructor

The user owns:

- genuine assessment decisions not determined by source;
- subjective choice between already acceptable options;
- explicit content/visual locks;
- final acceptance and publication authorization.

The user is not routine QA, spacing debugger or the first reader to discover obvious contradictions.

---

# 5. Freeze ladder

Later stages cannot silently reopen earlier freezes.

## F0 — source / course / baseline / history freeze

Freeze:

- syllabus, lecture sources, old Homework/Project, official policy and frozen decisions;
- canonical repository and branch;
- exact reader-seen baseline artifacts;
- version lineage;
- raw annotations/highlights;
- positive and rejected baselines;
- current accepted locks;
- source/derived-artifact boundary.

## F1 — audience / artifact-family freeze

Freeze:

- intended student and assumed level;
- reader task;
- artifact family;
- what the artifact includes and excludes;
- student/instructor/implementation/QA separation;
- assessment lifecycle stage.

## F2 — assessment-meaning freeze

Freeze:

- assessment purpose and capability measured;
- required work and evidence;
- weight/points/marks;
- workload boundary;
- data/method constraints;
- public scoring granularity;
- penalties and submission rules;
- oral/written boundary;
- AI/policy meaning.

## F3 — exact student-visible copy freeze

Freeze every student-visible string:

- course/artifact title;
- due date / weight / points;
- instructions and questions;
- formulas, labels and table cells;
- filenames and commands;
- scoring summaries;
- penalties;
- policy text;
- quotations and attribution;
- form fields/status/action labels;
- link labels.

No Codex implementation begins before complete student-visible copy is approved.

## F4 — information architecture and visual-semantics freeze

Freeze:

- stable BlockIDs;
- semantic zones (`IDENTITY`, `RULES`, `ASSESSED`, `POLICY`, `SOURCE_QUOTE`, `REFERENCE`);
- block order and reader action;
- continuous-flow zones;
- page-count mode (`HARD`, `PREFERRED`, `FREE`);
- legal/forbidden page breaks;
- keep-together units;
- title/metadata family;
- typography and spacing tokens;
- table/form/quotation roles;
- allowed layout fallback;
- forbidden fallback.

## F5 — shared-component proof freeze

For a new/major document family, prove real-content components before the full candidate:

- course title / artifact title / year / due / weight block;
- rule paragraph and numbered list;
- major question/subpart/point style;
- scoring table and penalty table;
- institutional quotation and attribution;
- form field and checkbox layout;
- page number/footer;
- template sample page;
- link style.

Human or independent acceptance locks these components. Later local repair cannot reimplement them.

## F6 — representative/golden-page freeze

Select representative/high-risk pages or artifacts covering:

- densest rule page;
- first assessed page;
- equation/table/code page;
- final assessment page;
- form page;
- policy/quotation page;
- Word/Quarto/LaTeX template samples where applicable.

A full document must not be the first visual prototype for a high-risk major task.

## F7 — full-candidate freeze

Freeze exact:

- source;
- commit;
- PDF/DOCX/ZIP;
- per-page renders;
- hashes;
- BlockID/page map;
- student release set;
- review bundle.

## F8 — human locks and release freeze

Explicit user acceptance creates locks over approved content/components/pages. Release authorization remains separate and binds exact files/hashes.

---

# 6. Artifact-family information architecture

A single generic outline is forbidden.

## 6.1 Homework brief

Default priority:

1. course/assignment identity;
2. due date, weight/points and essential submission information;
3. minimum data/software context needed before starting;
4. assessed questions/tasks and requested outputs;
5. concise page/reproducibility/AI rules.

Questions should dominate. Administrative instructions must not become half the assignment unless genuinely necessary.

All scored components belong in the assessed sequence and should sum transparently to the stated total.

## 6.2 Project Guide

Default priority:

1. project task and required analytical components;
2. key dates and milestone/proposal requirements;
3. data/method boundary without pre-solving course judgment;
4. required report contents;
5. broad public mark allocation;
6. templates, page limits and final submission;
7. necessary format/late/AI/oral rules.

Do not turn the Guide into a marker manual, method answer key, policy archive or QA history.

## 6.3 Milestone/proposal form

Use `proposed` / `planned` wording. Keep it concise and genuinely fillable. It should prevent late discovery of major feasibility problems without becoming a mini-report.

Review actual writable space, checkbox clarity and student/instructor section separation.

## 6.4 Student policy sheet

State the effective student rule and required action. Distinguish institutional quotation from course-authored interpretation. Do not expose internal classification deliberation.

## 6.5 Student report/template package

Clarify route choice, locked geometry, report source, executable code, final filenames and package skeleton. Do not expose QA manifests or internal production artifacts.

## 6.6 Oral-defense student brief

State duration, structure, permitted tools, preparation expectations and what is assessed. Keep student briefing separate from examiner question banks and scoring anchors.

## 6.7 Instructor artifacts

Solutions, atomic rubrics, tolerances, follow-through rules, grading calibration, expected-failure examples and GPT-assisted marking prompts are separate artifacts and separate reviews. They never enter the student release merely because they exist.

---

# 7. Source-to-reader map

Before drafting, classify every source item:

| Field | Meaning |
|---|---|
| Source locator | canonical file/section/page/table |
| Source role | fact / rule / evidence / rationale / implementation / QA |
| Intended audience | student / instructor / implementer / QA |
| Reader need | required action or interpretation |
| Disposition | INCLUDE / SUMMARIZE / MOVE_INTERNAL / EXCLUDE / USER_DECISION |
| Fidelity | verbatim label / exact number / semantic preservation / optional reorganization |
| Lifecycle stage | proposed / planned / completed / submitted / graded |
| Semantic class | identity / rule / assessed / penalty / policy / quote / context |
| Visual role | title / metadata / paragraph / list / table / form / quote / note |

A source item does not belong merely because it is true, available or internally important.

Student-facing artifacts use **minimum sufficient completeness for correct action**, not maximum disclosure.

---

# 8. Historical highlights, annotations and direct decisions

Historical acceptance is cumulative.

## 8.1 Raw annotation recovery

For major/recovery tasks, recover every available:

- PDF highlight/comment;
- screenshot annotation;
- direct user message;
- explicit rejection;
- explicit acceptance;
- course/source correction.

Preserve raw wording, selected text, page, coordinates/region and highlight colour/type where available. Colour is metadata; never infer a universal meaning unless the user/course has defined one.

## 8.2 Stable feedback registry

Every item receives:

```text
feedback_id
historical_artifact_id
historical_physical_page
selected_text_or_region
raw_feedback_text
highlight_colour_or_type
normalized_intent
semantic_target_block_id
component_target_if_any
lifecycle_state
supersedes / superseded_by
verification_method
current_evidence_locator
next_owner
```

Physical page number is history, not identity. Map old pages to stable current BlockIDs.

## 8.3 Lifecycle states

Allowed states:

```text
ACTIVE
PARTIAL
RESOLVED_IN_SPEC
RENDER_PENDING
RESOLVED_IN_RENDER
RESOLVED_BUT_GUARDED
SUPERSEDED
RETIRED_BY_STRUCTURE_CHANGE
ROUTED_INSTRUCTOR_ONLY
SOURCE_GAP_UNVERIFIABLE
```

Rules:

- `RENDER_PENDING` remains open;
- a new PDF or automated PASS never closes feedback automatically;
- page deletion/merge does not erase history;
- `RETIRED_BY_STRUCTURE_CHANGE` requires explicit authority and replacement BlockID;
- every later candidate revalidates all active and guarded items;
- the same cumulative ledger is updated; do not rebuild or drop rows.

## 8.4 Historical-feedback Critic requirement

For major/recovery work, the Prebuild Critic audits feedback item by item and reports counts by lifecycle state. A prose summary is insufficient.

---

# 9. Student-facing content approval before rendering

Required sequence:

```text
source/history review
-> audience contract
-> assessment-meaning freeze
-> source-to-reader map
-> semantic block map
-> complete student-visible body
-> user/instructor content approval
-> frozen approved body
-> implementation
```

Before Codex renders a substantial student artifact, the user must see and approve the complete student-visible body in Markdown/plain text.

Any later semantic change — requirement, date, score, example, exception, status, penalty, explanation, rubric detail or policy interpretation — returns to content approval.

Layout-only changes may remain in implementation only when semantic diff proves no visible-copy change.

---

# 10. Visual composition and page-flow authority

## 10.1 Course document-family contract

Recover and freeze:

- full course title;
- artifact title;
- academic year/term;
- due-date/weight/points placement;
- type and math family;
- page geometry;
- heading hierarchy;
- footer/page number;
- hyperlink and quotation style.

A new artifact inherits the course family unless the instructor explicitly approves a different reader need.

## 10.2 Semantic zones

At minimum:

```text
IDENTITY
RULES
ASSESSED_OR_DECISION_CONTENT
POLICY
SOURCE_QUOTE
REFERENCE
INTERNAL_ONLY
```

Different student actions require distinguishable visual roles. A scored component may not be buried as ordinary rules prose.

## 10.3 Continuous-flow zones

If blocks should follow continuously, freeze:

```text
FLOW_ZONE = A -> B -> C -> ...
INTERNAL_HARD_BREAKS = FORBIDDEN
HARD_BREAK_AFTER = approved boundary or NONE
```

Use natural flow, then bounded keep-together controls, then only explicitly approved hard breaks.

## 10.4 Page-budget mode

Every artifact declares:

```text
PAGE_COUNT_MODE = HARD | PREFERRED | FREE
PAGE_COUNT_TARGET =
CONTENT_MUTABLE = YES | NO
FONT_MUTABLE = YES | NO
MARGINS_MUTABLE = YES | NO
RHYTHM_MINIMUMS =
```

Do not compress font, margins, line spacing or content merely to reduce page count.

When one-page versus two-page quality is genuinely ambiguous, produce bounded A/B proofs under identical content/font/geometry locks and let the user choose between already acceptable options.

## 10.5 Visual-rhythm tokens

Freeze at least:

```text
BODY_SIZE
BODY_LEADING
PARAGRAPH_GAP
TITLE_GAP_AFTER
HEADING_GAP_BEFORE
HEADING_GAP_AFTER
LIST_GAP_BEFORE_AFTER
LIST_ITEM_GAP
NESTED_LIST_ITEM_GAP
QUOTE_GAP_BEFORE
QUOTE_GAP_AFTER
ATTRIBUTION_GAP_AFTER
TABLE_GAP_BEFORE_AFTER
TABLE_ROW_PADDING
FOOTER_RESERVE
```

Codex may search only an approved finite parameter space. It may not invent spacing values after seeing the result.

## 10.6 Tables and forms

- instructional tables use restrained hierarchy and whitespace, not vertical-rule grids by default;
- compact tables remain associated with their explanatory paragraph/consequence;
- fillable forms are reviewed for writable space, checkbox clarity and section separation;
- no-clipping is necessary but not sufficient.

---

# 11. Prebuild Critic workflow

Required for all major/new/recovery tasks.

The Planner supplies:

- source/history manifest;
- audience contract;
- assessment-purpose and workload statement;
- source-to-reader map;
- exact student-visible body;
- BlockID/semantic-zone map;
- public/private rubric decision;
- document-family and visual contract;
- annotation ledger;
- proposed Controller Goal and acceptance plan.

The Critic must attempt to disprove:

1. assessment validity;
2. workload reasonableness;
3. student executability;
4. TA/instructor workload;
5. scoring/penalty clarity;
6. source/policy consistency;
7. student/instructor boundary;
8. artifact-family structure;
9. visual/page-flow sufficiency;
10. regression and review coverage.

Only `P0 = 0` and `P1 = 0` permits major implementation.

---

# 12. Component proofs and representative proofs

A high-risk major artifact should not first appear as a complete PDF.

## 12.1 Component proof sheet

Use real content to prove:

- title/metadata;
- rule paragraph/list;
- question/subpart/point style;
- scoring/penalty table;
- quotation/attribution;
- form fields;
- footer/page number;
- template sample.

## 12.2 Golden/representative proof pack

Select a small set covering all high-risk structures and historical failures.

User acceptance locks components/proof pages. Later revisions cannot reimplement them.

Task proportionality applies: a two-page simple Homework need not inherit a large proof ceremony unless history or risk warrants it.

---

# 13. Codex Controller production loop

One autonomous Controller Goal should normally perform:

```text
Parent Controller
├─ fresh Producer
├─ fresh deterministic Auditor
├─ fresh rendered Reviewer
├─ fresh Producer repair
├─ new fresh Auditor
├─ new fresh Reviewer
└─ independently accepted candidate/delta
```

## 13.1 Authority bundle

Before production, freeze a read-only bundle containing:

- task classification;
- exact baseline and source hashes;
- BlockIDs and semantic zones;
- approved visible copy;
- document-family/style tokens;
- annotation registry;
- locks and unlocks;
- round allowlist;
- cumulative acceptance gates;
- validator/reviewer version.

## 13.2 Proof-carrying patch manifest

Every candidate records:

```text
candidate_id
parent_candidate_id
baseline_commit
modified_block_ids[]
modified_component_ids[]
addressed_feedback_ids[]
unchanged_locked_block_ids[]
visible_copy_changes[]
authorized_dependency_invalidations[]
open_items_before[]
open_items_after[]
```

Every source/render change must map to the allowlist.

## 13.3 Internal candidate convergence

For visual ambiguity, Codex should render a finite approved candidate set, reject invalid candidates deterministically, then send only survivors to independent rendered review.

Do not make one speculative spacing guess and send it to the user.

## 13.4 Stop rule

If no candidate passes within the approved internal cycle budget, return:

```text
STOP_PLANNER_DECISION_REQUIRED = YES
READY_FOR_USER_REVIEW = NO
```

Do not expose another speculative PDF.

---

# 14. GPT Work gate

GPT Work occurs only after deterministic and internal rendered review pass.

For major/new/recovery artifacts, GPT Work reviews:

- every student-facing page;
- full contact sheet/sequence;
- actual forms/templates where in scope;
- first-time-student reading effort;
- cumulative visual/audience guards;
- cross-page consistency and whole-document rhythm.

GPT Work verdict:

```text
PASS
REVISE
NOT_INDEPENDENTLY_VERIFIED
BLOCKED
```

`REVISE` findings name exact block/page/region and required outcome; they do not author new copy.

A GPT Work PASS cannot override deterministic failure or unresolved Critic finding.

---

# 15. Cumulative acceptance order

Apply the companion acceptance contract in this order:

1. artifact identity and task mode;
2. source/history coverage;
3. assessment correctness and workload;
4. audience and layer separation;
5. exact copy and source fidelity;
6. information architecture and scoring transparency;
7. document-family and visual semantics;
8. component/representative proof;
9. deterministic implementation QA;
10. rendered-artifact review;
11. GPT Work review;
12. user acceptance;
13. release/package closure.

A later gate cannot upgrade an earlier failure.

---

# 16. Revision and monotone convergence

Every revision declares:

- exact baseline;
- task classification;
- changed BlockIDs/components;
- locked scope;
- round-frozen scope;
- feedback IDs addressed;
- change budget;
- semantic/copy/visual unlocks;
- acceptance tests.

Layered locks:

```text
assessment-semantic lock
student-visible-copy lock
information-architecture lock
document-family/component lock
page/block visual lock
release-layer lock
```

Accepted round invariants:

```text
open_feedback_next is a strict subset of open_feedback_current
locked_blocks_next is a superset of locked_blocks_current
locked_components_next is a superset of locked_components_current
modified_ids is a subset of round_allowlist
unrelated_source_changes = 0
unrelated_render_changes = 0
closed_guard_recurrences = 0
```

If open issues do not decrease or accepted work reopens, do not produce another broad candidate. Diagnose the root authority, component, generator or review-coverage failure first.

A recurrence of the same closed guard requires:

1. reject candidate;
2. identify shared root cause;
3. repair root cause;
4. add persistent regression guard;
5. rerun historical negative baseline.

Repeated recurrence stops project-local patching and routes repair to the generic Research Authoring production system.

---

# 17. User review and human-review budget

The user should see only internally accepted artifacts or bounded deltas.

A review package states:

- what is being reviewed now;
- what is already locked;
- what remains deferred;
- changed blocks/pages;
- genuine decisions the user must make;
- proof that unrelated locks are unchanged.

Do not include internal JSON, validator logs, contact sheets, manifests or prompts unless requested.

Default for a bounded revision:

```text
HUMAN_REVIEW_BUDGET = one final acceptance review
```

For an A/B choice, both options must already be independently acceptable.

---

# 18. Release closure

Student release, instructor release and QA evidence are separate.

## 18.1 Student release

Contains only intended student artifacts: Guide/Homework, forms, templates, data/starter files and concise instructions.

## 18.2 Instructor release

Contains solutions, rubrics, grading sheets, calibration, question banks and marking prompts.

## 18.3 QA/release evidence

Contains hashes, manifests, renders, reports and validation evidence; it does not enter the student package.

Before release:

- bind exact final files/hashes;
- verify filenames and package structure;
- verify no instructor leakage;
- verify links and forms;
- perform native Word/Office checks when required;
- rerun final full-document regression;
- obtain explicit publication authorization.

`READY_FOR_USER_REVIEW`, `USER_ACCEPTED`, `RELEASE_READY` and `RELEASED` are distinct states.

---

# 19. Required completion states

```text
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
RELEASE_READY
RELEASED
```

Do not collapse these into a single `PASS`.

---

# 20. Immediate adoption and promotion tests

This workflow should be used immediately before generic runtime automation is complete.

Promotion evidence must include at least:

- one Homework brief;
- one open-ended Project Guide;
- one milestone/proposal form;
- one instructor solution/rubric package;
- one annotated-PDF revision;
- one failed-version recovery;
- one local repair proving unrelated accepted regions unchanged;
- one executor-added sentence rejected;
- one known-bad artifact rejected by a frozen validator;
- one A/B visual choice where both options are already acceptable;
- one final release with student/instructor/QA separation.

STAT5060 HW1 is the first mandatory full replay. STAT5060 Final Project must use this workflow when resumed.

---

# 21. Final principles

1. **Decide who the document is for before deciding what it contains.**
2. **Student-facing completeness means enough to act correctly, not everything the course team knows.**
3. **Assessment meaning and exact visible copy are frozen before Codex implementation.**
4. **Codex implements; it does not decide pedagogy, policy, scoring transparency or student information needs.**
5. **A Critic tries to break the specification before production.**
6. **Deterministic QA, rendered review and GPT Work are separate trust layers.**
7. **Historical highlights remain cumulative until explicitly superseded, retired or verified in render.**
8. **Accepted content, copy, components and visual regions are layered locks.**
9. **A local repair cannot become a whole-document regeneration.**
10. **The user is the final decision-maker, never routine QA.**


---

# 22. Deterministic versus aesthetic gate ownership

A recurring failure mode is to encode subjective composition goals as rigid deterministic thresholds and then treat the absence of survivors as evidence that the document itself is impossible.

Research Authoring must separate:

## 22.1 Deterministic gates

Use deterministic validation for facts that have one objectively correct result, for example:

- exact visible copy;
- dates, weights, points and filenames;
- formulas and links;
- page count when explicitly hard;
- block presence/order;
- semantic-block split/no-split when frozen;
- protected path and hash checks;
- clipping/overflow/missing glyph;
- known-bad regression guards;
- student/instructor leakage;
- exact locked-region pixel parity where appropriate.

These may fail closed.

## 22.2 Render-review heuristics

Use rendered review for visual judgments that do not have a universal numeric optimum, including:

- whether whitespace looks intentional;
- whether a short second page feels calm or wasteful;
- whether adjacent pages feel balanced enough;
- whether block spacing feels cramped or too loose;
- whether one page or two pages reads better when both are structurally valid;
- whether visual rhythm fits the document family.

Metrics such as occupied-page fraction, bottom-blank fraction or adjacent-page density delta may be recorded as **diagnostics** and review triggers, but must not be hard acceptance gates unless one of the following holds:

1. the threshold is calibrated against an explicitly accepted baseline for the same document family; or
2. the threshold protects an objective failure state such as clipping, hidden content or unusable form space.

Do not invent an arbitrary density target and then allow it to eliminate every otherwise valid candidate.

## 22.3 Planner response when the search space has zero survivors

If all candidates fail the same visual-density or whitespace threshold:

1. stop;
2. inspect whether the threshold belongs to deterministic validation or rendered review;
3. inspect whether the structural archetype, rather than micro-spacing, is the real decision variable;
4. repair the **authority / validator / reviewer ownership boundary** before expanding the candidate space;
5. do not continue brute-force spacing search under a contradictory gate.

The next search should operate over meaningful composition alternatives (for example, semantic breakpoint, top-aligned versus deliberately distributed rule blocks, compact versus airy but family-consistent spacing), not arbitrary micro-spacing alone.

## 22.4 Visual proof selection

For a small bounded document repair, prefer:

```text
frozen content
-> small set of semantically valid composition archetypes
-> deterministic rejection of objectively invalid candidates
-> fresh rendered reviewer selection
-> optional GPT Work comparison
-> user sees only already acceptable finalists
```

This is the document analogue of presentation layout-archetype and golden-page proof. The renderer does not decide the semantic structure, while the deterministic validator does not substitute itself for aesthetic review.


# 23. Annotation fidelity, source terminology, and mathematical typography

## 23.1 Annotated-PDF revision is annotation-first

When the user/instructor provides a marked PDF, do not infer the revision only from rendered appearance or prior chat summaries.

Before drafting:

1. extract the annotation object inventory;
2. render the annotated pages;
3. map each Highlight / StrikeOut / Underline / comment to the selected text or region;
4. preserve raw annotation text/comments;
5. map every substantive annotation to a stable feedback ID and lifecycle state;
6. apply later direct user decisions as explicit supersession, never as silent replacement.

Required fields:

```text
ANNOTATION_OBJECT_COUNT =
SUBSTANTIVE_ANNOTATION_COUNT =
STRIKEOUTS_MAPPED = YES
HIGHLIGHTS_MAPPED = YES
ANNOTATION_COMMENTS_MAPPED = YES
DIRECT_USER_SUPERSESSIONS_MAPPED = YES
```

A StrikeOut normally means remove the marked student-visible content. A Highlight does not have a universal meaning: use its comment, surrounding context, and direct instructor/user decision. Do not guess from colour alone.

## 23.2 Source terminology outranks convenient shorthand

Student-facing method names and parameterization language should follow the instructor's lecture notes / canonical course source unless the instructor explicitly approves a modernization or alternate notation.

Do not introduce a shorthand label merely because it is common in software or another textbook.

Examples:

- if the lecture uses “negative binomial distribution” / “negative binomial loglinear model”, do not silently relabel it “NB2”;
- if the lecture defines dispersion through (k) and/or (D), use that notation or explicitly define any conversion;
- package-specific names belong in implementation/help text, not automatically in the assessment question.

Required:

```text
COURSE_TERMINOLOGY_SOURCE =
STUDENT_TERMINOLOGY_FIDELITY = PASS
UNAPPROVED_SOFTWARE_SHORTHAND = NONE
```

## 23.3 Minimum sufficient student prose

Every student-visible sentence must do at least one of:

- define the task;
- identify required input/output;
- state a condition/constraint;
- state a consequence;
- provide essential context for interpretation.

If removing the sentence does not change what the student must do or understand, remove it.

Do not retain process prose merely because it existed in a previous version.

## 23.4 Mathematical display restraint

Use inline mathematics for short expressions that read naturally inside a sentence.

Use display mathematics only when at least one is true:

- the equation is central to the task and must be read as an object;
- multiple related expressions must be compared together;
- the formula is long/multiline;
- students must use the formula directly and visual separation materially improves comprehension.

Do not create separate display blocks for single short expressions such as a mean function or one distribution statement when they can be written inline. Consolidate related generating-model statements into one sentence or one compact aligned block.

Required visual check:

```text
GRATUITOUS_DISPLAY_MATH = ZERO
RELATED_FORMULAS_GROUPED = PASS
MATH_FLOW_READS_NATURALLY = PASS
```

## 23.5 Title and heading-to-body rhythm

The visual hierarchy must reflect reader importance, not default LaTeX size steps.

For a course handout:

- course identity should be prominent but must not dwarf the assignment title;
- the assignment title must be visually substantial;
- if both are centered, the course title should normally be only modestly larger than the assignment title;
- academic-year metadata is subordinate.

Every repeated major-question heading must use one shared heading-to-first-body spacing token. The first paragraph/subpart must not sit noticeably tighter than elsewhere.

Likewise, repeated front-matter labels such as Data / Submission / Report format should use a coherent block rhythm.

Required:

```text
TITLE_HIERARCHY = PASS
QUESTION_HEADING_BODY_GAP_TOKEN = FROZEN
QUESTION_HEADING_BODY_GAP_CONSISTENCY = PASS
FRONT_MATTER_BLOCK_RHYTHM = PASS
```

Do not repair one heading locally with an ad hoc vertical skip; fix the shared component/token.


# 24. Opening-page information-value and composition rule

The first page of a student assessment has a distinct reader job. It should normally let the student identify:

- what artifact this is;
- when it is due and the visible total/weight information that has been approved;
- what data/context they need before starting;
- what they must submit;
- where the assessed work begins.

A sparse first page is **not** permission to add filler.

When the opening page becomes visually underfilled after legitimate simplification, use this order:

1. recover concise, source-backed context that materially helps interpretation or action;
2. improve the scan structure of existing required information, for example a short data map or a numbered submission list;
3. allow the first assessed block to flow naturally upward/downward under the semantic-pagination rules;
4. accept purposeful whitespace if no additional information passes the reader-value test.

Any newly proposed contextual sentence must pass at least one of:

```text
INTERPRETATION_VALUE = helps the student interpret the data/task correctly
NAVIGATION_VALUE = helps locate/reuse a relevant course example/source
ACTION_VALUE = changes or clarifies what the student must do/submit
ERROR_PREVENTION_VALUE = prevents a likely substantive misunderstanding
```

If none apply, exclude the sentence.

For a short Homework brief, contextual enrichment should normally be no more than one or two compact sentences before the data/deliverable structure.

Good candidates include:

- whether a shared dataset is synthetic/observational when that affects interpretation;
- whether treatment/group assignment was not randomized when causal interpretation matters;
- that several questions deliberately reuse one dataset/context;
- that a later question revisits a named lecture example when this helps students locate relevant course material.

Do not add:

- motivational filler;
- generic course summaries;
- “what a good answer looks like” teaching unless explicitly approved;
- privacy/provenance disclaimers that do not change student action;
- internal design rationale;
- text whose only purpose is to occupy vertical space.

For multiple required submission files, prefer a short numbered or bulleted deliverable list when it is more scannable than a dense paragraph. Put consequences immediately after the relevant requirement, in plain student language.

Required review fields:

```text
FIRST_PAGE_READER_JOB = PASS
FIRST_PAGE_CONTEXT_VALUE = PASS | N/A
FILLER_COPY_ADDED = NO
SUBMISSION_SCANNABILITY = PASS
FIRST_ASSESSED_BLOCK_VISIBLE = YES
OPENING_PAGE_RHYTHM = PASS
```
