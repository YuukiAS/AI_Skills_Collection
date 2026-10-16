# Presentations Core TODO — Authoring, Production, Review, and Bounded Revision

Status: **PROMOTE_NOW / CANONICAL WORKFLOW ADOPTION**

Canonical runtime contracts:

- `plugins/codex/plugins/presentations/shared/presentation-end-to-end-pre-execution-runbook.md` **(mandatory first read; complete workflow)**
- `plugins/codex/plugins/presentations/shared/pre-execution-cumulative-acceptance-contract.md` **(mandatory second read; cumulative acceptance + failure ownership)**
- `plugins/codex/plugins/presentations/shared/authoring-production-workflow.md`
- `plugins/codex/plugins/presentations/shared/chatgpt-web-authoring-contract.md`
- `plugins/codex/plugins/presentations/shared/anti-shortcut-production-contract.md`
- `plugins/codex/plugins/presentations/shared/independent-review-contract.md`

Historical design inputs remain evidence and must not be discarded:

- `docs/design/PRESENTATIONS_EXISTING_DECK_CONVERGENCE_ARCHITECTURE_V1_2026-10-06.md`
- `docs/design/PRESENTATIONS_CUMULATIVE_HUMAN_FEEDBACK_AND_TEACHING_DECK_AUTHORING_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_HISTORY_PREFLIGHT_PAGE_LOCK_AND_MATH_FIGURE_TODO_2026-10-06.md`
- later anti-self-certification and independent-review design documents.

## 0. P0 — Mandatory read-before-work gate

Every non-trivial presentation task must begin by reading `presentation-end-to-end-pre-execution-runbook.md` in full and then `pre-execution-cumulative-acceptance-contract.md` and emitting/deriving the task classification, Critic requirement, history scope, freeze state, locks, and round allowlist before execution.

The failure-class ownership table in that contract is cumulative. Future revisions may append new failure classes or strengthen ownership, but may not silently drop an existing class because one candidate fixed it.

## 1. Foundations that must be preserved

Any implementation or simplification must retain:

1. new-deck, minor-revision, major-revision, and failed-recovery modes;
2. stable PageIDs, version lineage, and page/component ancestry;
3. cumulative raw human feedback with lifecycle and supersession;
4. semantic, copy, layout, page-body, and shared-component locks;
5. no executor-authored audience copy;
6. explicit layout grammar rather than page-local improvisation;
7. cumulative acceptance requirements;
8. deterministic QA separated from rendered review;
9. immediate human locking after acceptance;
10. two-to-four-round monotone convergence;
11. delta review plus final whole-deck regression;
12. user is not first or routine QA.

## 2. ChatGPT Web must become a first-class Presentation Author

ChatGPT Web should be able to invoke presentations for:

- source reading and reconciliation;
- audience/purpose/format definition;
- task classification and Critic routing;
- narrative, page count, section order, and page jobs;
- required/forbidden object freeze;
- exact visible-copy authoring;
- audience/speaker/instructor/internal boundaries;
- semantic layout and archetype selection;
- feedback intake, lifecycle, supersession, and locks;
- prebuild Critic requests;
- autonomous Codex Controller Goals;
- rendered-artifact comparison and filtered user deltas.

This role is analogous to Research Authoring: ChatGPT owns human-level meaning and communication judgment; Codex owns implementation and execution.

ChatGPT must not be reduced to an open-ended prompt such as “make this deck better.”

## 3. Major/minor classification and Critic gate

### P0 — Minor revision route

A separate prebuild Critic may be skipped only when:

- page count and section order are unchanged;
- no page job, claim, shell, or archetype changes;
- no page split/merge;
- copy changes are local and source-supported;
- scope is normally at most three pages and one already-defined component;
- no closed guard has recurred.

The Planner still freezes the exact allowlist, locks, and active guard bundle.

### P0 — Major revision/recovery route

A fresh prebuild Critic is mandatory for:

- page-count, section-order, narrative, or page-job changes;
- broad copy/content changes;
- shell/template/header/footer/navigation changes;
- new archetypes, page splits/merges, or major figure systems;
- scientific/statistical/pedagogical meaning changes;
- repeated regressions or human-rejected lineages;
- user requests to rethink, rebuild, overhaul, or reread all history.

The Critic must report evidence-consumption counts, independently judge page count/sequence, review every planned page, and audit the Controller workflow. Any major Planner amendment after Critic review requires another Critic pass.

## 4. Freeze ladder

The generic runtime should encode:

```text
F0 source/baseline/history
F1 narrative/page count/page jobs
F2 exact visible copy
F3 layout semantics/archetypes/component bindings
F4 accepted shared components
F5 accepted golden-page composition/density
F6 exact full candidate
F7 human page/component locks
```

A later stage cannot silently reopen an earlier freeze.

## 5. Historical-feedback consumption policy

### Major/recovery

ChatGPT Planner and Critic reread the complete raw history and actual rendered lineage. They report exact counts, direct decisions, source gaps, unresolved conflicts, and positive/negative baselines.

### Every Codex round

Codex receives a read-only compiled bundle with:

- all active global guards;
- guards for modified PageIDs/components;
- current locks and round-frozen scope;
- current-round feedback;
- ancestry and consumer dependencies.

The independent Auditor verifies cumulative coverage. Codex does not resolve human-feedback conflicts.

### Minor revision

ChatGPT reads current feedback, exact baseline, active global guards, and complete history for affected pages/components. A recurrence or shared-root change escalates to major.

Raw human feedback remains above derived registries.

## 6. Layout grammar and double-column decision

The plugin must decide composition from semantic relationship.

Columns are appropriate for:

- true peers;
- R/Python code;
- before/after;
- model A/model B;
- written/oral roles;
- figure plus interpretation;
- independent image/evidence pairs.

Columns are inappropriate for:

- derivations;
- algorithms;
- mechanism or cause chains;
- Question -> evidence -> Answer;
- ordered model interpretation;
- prose split merely to occupy horizontal space.

Default test:

> If the right region depends on finishing the left region, the page is sequential and should normally be vertical.

Codex may adjust spacing/widths inside the frozen archetype, but cannot invent a new archetype or delete copy to make columns fit.

## 7. Whitespace and density

Whitespace is judged after content sufficiency.

Accept intentional whitespace when the page job is complete, the primary object is already readable and properly scaled, and the reading path is deliberate.

Reject large unused regions when they coexist with:

- undersized primary objects;
- interpretation far from evidence;
- result pushed to the bottom;
- tiny text;
- column-created lower voids;
- missing explanation or deleted content;
- an unfinished composition.

Do not fill space with slogans, cards, decorative arrows, repeated labels, or generic takeaways. Review whitespace at whole-slide scale and on the contact sheet.

## 8. Shared-component and golden-page proof

Before a non-trivial full candidate, prove real-content:

- title;
- header/navigation;
- footer/source/buttons/page number;
- typography;
- Question/Answer;
- table;
- code;
- caption;
- figure/diagram treatment;
- closing.

Then prove six to ten high-risk/representative pages covering all major archetypes and historical failure classes.

Human acceptance locks components and composition standards.

A major Critic may authorize direct full production in an urgent recovery only when it explicitly confirms that shell, copy, layouts, history guards, and full review route are sufficiently frozen. This is an exception.

## 9. Codex autonomous production

Every non-trivial milestone should run as one Controller Goal:

```text
Parent Controller
├─ fresh Producer
├─ deterministic QA
├─ fresh read-only Auditor/Reviewer
├─ fresh Producer repair
├─ new immutable candidate when bytes change
├─ fresh complete re-review
└─ independently accepted candidate/delta
```

Ordinary build, layout, copy-fidelity, whitespace, visual, and reviewer findings are internal engineering work. The user must not relay completion blocks, launch routine reviewers, or become first QA.

## 10. GPT Work role

GPT Work is the final aesthetic, reader-effort, and pedagogical/communication gate.

- Major/new/recovery: all pages plus full contact sheet on the exact immutable candidate.
- Minor revision: changed pages, affected component consumers, minimum context, and full contact sheet when global structure remains locked.
- Final release: complete whole-deck regression.

GPT Work does not implement fixes or override deterministic/statistical failures.

## 11. Proof-carrying bounded revision

Every revision candidate records:

- exact baseline;
- modified PageIDs/components;
- addressed feedback IDs;
- unchanged locks;
- required-object relocations;
- visible-copy changes;
- dependency invalidations;
- open items before/after.

Pages/components outside the allowlist are round-frozen.

## 12. Root-cause stop rule

If a closed guard returns:

1. reject the candidate;
2. find the shared primitive, authority, or review-coverage root cause;
3. repair the root cause;
4. add a persistent regression guard.

If open issues fail to decrease or accepted pages reopen, do not create another broad candidate.

## 13. Required production sequence

```text
mode/severity/source intake
-> ChatGPT deck brief
-> F1 page authority
-> F2 visible-copy authority
-> F3 layout authority
-> prebuild Critic when major
-> component proof
-> golden pages
-> full candidate through autonomous Controller
-> GPT Work gate
-> filtered user review and locks
-> bounded delta revisions
-> final whole-deck regression and delivery
```

## 14. Promotion tests

The workflow is not mature until it demonstrates:

- one new deck reaches useful visible proof without unnecessary recovery machinery;
- one minor revision skips the heavy Critic but preserves all locks and history;
- one major revision is blocked by the Critic until all page specifications pass;
- one failed deck preserves complete raw history and negative baselines;
- a local repair changes only the allowlist;
- executor-added copy is rejected;
- difficult content cannot be deleted to solve layout;
- a sequential page cannot be converted to arbitrary columns;
- shared-component repair leaves page bodies unchanged;
- Producer/Reviewer/repair occurs inside one Goal without user relay;
- the user reviews only two to four shrinking deltas;
- final whole-deck regression catches a reintroduced historical defect;
- at least one teaching deck and one research/decision deck pass the same general workflow.

## 15. Immediate adoption

Projects should apply this workflow before generic automation is complete. Plugin work must not indefinitely postpone real visible artifacts once authority is ready.
