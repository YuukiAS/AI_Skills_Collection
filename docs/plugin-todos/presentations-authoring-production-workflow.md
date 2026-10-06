# Presentations Core TODO — Authoring, Production, Review, and Bounded Revision

Status: **PROMOTE_NOW / CANONICAL WORKFLOW ADOPTION**  
Canonical runtime contract:

`plugins/codex/plugins/presentations/shared/authoring-production-workflow.md`

Historical design inputs retained rather than replaced:

- `docs/design/PRESENTATIONS_EXISTING_DECK_CONVERGENCE_ARCHITECTURE_V1_2026-10-06.md`
- `docs/design/PRESENTATIONS_CUMULATIVE_HUMAN_FEEDBACK_AND_TEACHING_DECK_AUTHORING_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_HISTORY_PREFLIGHT_PAGE_LOCK_AND_MATH_FIGURE_TODO_2026-10-06.md`
- `plugins/codex/plugins/presentations/shared/anti-shortcut-production-contract.md`
- `plugins/codex/plugins/presentations/shared/independent-review-contract.md`

## 1. What must be preserved from the original convergence architecture

The new workflow must not lose:

1. separate new-deck and existing-deck/recovery modes;
2. stable semantic PageIDs and version/page ancestry;
3. cumulative feedback memory with lifecycle and supersession;
4. semantic, copy and visual locks;
5. no executor-authored audience copy;
6. explicit layout grammar rather than page-local improvisation;
7. shared-component registries and locks;
8. cumulative acceptance standards;
9. deterministic QA separated from visual/pedagogical review;
10. immediate human locking after acceptance;
11. two-to-four-round monotone convergence;
12. delta review plus final full-deck regression.

Any future simplification that drops one of these foundations is a workflow regression.

## 2. What the canonical workflow adds

### P0 — ChatGPT Web becomes a first-class Presentation Author

ChatGPT Web should be able to invoke the presentations capability for:

- source reading and reconciliation;
- audience/purpose definition;
- narrative and page-count decisions;
- page-job and required-object freeze;
- exact visible-copy authoring;
- teaching/student/instructor boundary;
- semantic layout and archetype selection;
- feedback ingestion, lifecycle and lock decisions;
- generation of autonomous Codex Controller Goals;
- high-level review of filtered proof/delta artifacts.

This role is analogous to `research-authoring`: ChatGPT owns human-level content and communication judgment; Codex owns file production and execution.

ChatGPT Web must not be reduced to writing an open-ended prompt such as “make this deck better.”

### P0 — Task proportionality

The plugin must distinguish:

- new deck;
- existing deck revision;
- failed-version recovery.

History reconstruction, incident ledgers and exhaustive annotation recovery are required only when the artifact history warrants them. A small new deck must not inherit the full STAT5060 recovery ceremony.

Conversely, a complex recovery must not fall back to latest-version-only revision.

### P0 — Component proof before full-deck production

A non-trivial deck should prove real-content shared components before a full candidate:

- title;
- header/navigation;
- footer/page number/source;
- typography;
- Question/Answer;
- table;
- code;
- caption;
- figure/diagram treatment;
- closing.

Human acceptance locks these components. Later page repair cannot reimplement or drift them.

### P0 — Golden-page proof pack before full-deck production

Select six to ten high-risk/representative pages covering all major archetypes and historical failure classes.

A complete deck must not be the first visual prototype.

Golden pages establish:

- density floor;
- composition grammar;
- actual template behavior;
- code/table/figure/formula/Q&A treatment;
- opening/closing quality;
- teaching/research communication standard.

### P0 — One autonomous Controller Goal per production/revision milestone

Normal topology:

```text
Parent Controller
├─ fresh Producer
├─ fresh read-only Auditor/Reviewer
├─ fresh Producer repair
├─ new fresh Auditor/Reviewer
└─ independently accepted candidate/delta
```

Ordinary build, test, layout, copy-fidelity, visual and reviewer findings are internal engineering work. The user must not relay completion blocks, launch reviewers or become first QA.

### P0 — Artifact-first progress rule

After page/copy/layout authority is ready, the next milestone must be visible proof pages.

Do not let generic validator, evidence or governance development indefinitely postpone:

```text
component proof sheet
-> golden-page pack
-> full candidate
```

Generic runtime hardening may proceed in parallel. It is not automatically a blocker for project-local authoring and bounded proof production.

### P0 — Proof-carrying bounded revision

Every revision candidate records:

- exact baseline;
- modified PageIDs/components;
- addressed feedback IDs;
- unchanged human locks;
- required-object relocations;
- visible-copy changes;
- dependency invalidations;
- open items before/after.

Pages/components outside the explicit allowlist are round-frozen.

### P0 — Dependency-aware layered locks

Locks distinguish:

- semantics;
- visible copy;
- layout archetype;
- page-body visual composition;
- shared component.

A footer change revalidates footer consumers without reopening page semantics or copy. A copy change does not unlock header/footer. A page-body repair cannot alter shared chrome.

### P0 — Root-cause stop rule

If a closed guard returns:

1. reject the candidate;
2. identify the shared primitive, authority or review-coverage root cause;
3. repair the root cause;
4. add a persistent regression guard.

If open issues fail to decrease or accepted pages reopen, do not produce another broad candidate.

### P0 — Separate delta review from final regression

During convergence, the user sees only changed pages/components and minimum context.

Before delivery, the complete deck is still reviewed for page order, narrative, shared chrome, locks, history, figures, code, fonts, PDF text and artifact identity.

## 3. Required production sequence

```text
mode/source intake
-> ChatGPT deck brief
-> semantic page authority
-> exact visible-copy authority
-> layout/archetype authority
-> shared-component proof sheet
-> golden-page proof pack
-> full candidate through autonomous Controller Goal
-> filtered user review and locks
-> bounded delta revisions
-> final full-deck regression and delivery
```

## 4. Teaching-deck requirements retained

- why the method is needed precedes or accompanies formalism;
- method first introductions must be pedagogically sufficient;
- count/rate/offset, conditional/marginal and Bayesian computation chains must not be compressed merely for layout convenience;
- instructor-learning feedback does not automatically inflate student slides;
- software/API plumbing defaults outside student-visible body unless it changes statistical meaning;
- whitespace is evaluated only after content sufficiency;
- every visible prose object has a semantic role;
- Question and Answer form a paired grammar;
- interpretation remains near its evidence.

## 5. Promotion tests

The workflow is not mature until it demonstrates:

- one new deck reaches a useful golden-page proof without unnecessary recovery machinery;
- one failed existing deck preserves complete history and accepted locks;
- a local repair changes only the allowlist;
- an executor-added sentence is rejected;
- difficult content cannot be deleted to fix layout;
- shared-component repair leaves page bodies unchanged;
- Producer/Reviewer/repair occurs inside one Goal without user relay;
- the user reviews only two to four shrinking deltas;
- final whole-deck regression catches a deliberately reintroduced historical defect;
- at least one teaching deck and one research deck pass the same general workflow.

## 6. Immediate adoption rule

Projects may and should apply this workflow before generic runtime automation is complete.

Do not wait for the presentations plugin roadmap to finish before using:

- ChatGPT page/copy/layout freeze;
- shared-component proofs;
- golden pages;
- one-Goal Producer/Reviewer repair loops;
- human locks;
- bounded revisions;
- delta review;
- final full-deck regression.

The current STAT5060 Tutorial 01 recovery is the first mandatory immediate adoption case.
