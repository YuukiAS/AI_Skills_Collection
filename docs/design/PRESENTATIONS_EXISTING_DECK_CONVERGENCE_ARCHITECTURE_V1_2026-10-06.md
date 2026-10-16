# Presentations — Existing-Deck Convergence Architecture V1

Date: 2026-10-06  
Status: **P0 DESIGN INPUT / NOT YET RUNTIME**  
Primary real-use evidence: repeated STAT5060 Tutorial 01 revisions and earlier research-deck regressions

## 1. Problem statement

The previous revision model treated each prompt as a fresh slide-generation task. It could fix one visible defect while rewriting unrelated pages, shared chrome, language or scientific content. Historical feedback existed in prose and review packets but did not block an implementation that reintroduced the same failure.

A mature presentations workflow must behave like controlled product revision, not repeated document regeneration.

Target outcome:

- most decks converge in two to four human review rounds;
- open defects decrease monotonically;
- accepted pages/components become immutable;
- executor-authored audience copy is prohibited;
- deterministic failures are rejected before aesthetic review;
- the user sees only bounded deltas and makes final subtle decisions.

## 2. Separate production modes

### Mode A — New deck

Required sequence:

1. source/evidence reading;
2. audience and purpose freeze;
3. narrative/page-job map;
4. exact visible copy;
5. approved layout archetypes;
6. implementation;
7. deterministic QA;
8. independent visual/pedagogical review;
9. human acceptance and locks.

### Mode B — Existing deck revision

Adds mandatory history controls:

1. artifact-family identification;
2. complete version lineage;
3. cumulative human-feedback registry;
4. stable semantic PageIDs;
5. page/component ancestry;
6. explicit modify/freeze scope;
7. accepted-page/component locks;
8. candidate regression matrix against all active history.

Mode B is not allowed to fall back to “read the latest PDF and improve it.”

## 3. Canonical artifact graph

Every deck family needs:

```text
ArtifactFamily
  ├── VersionLineage
  ├── PageRegistry
  │     ├── StablePageID
  │     ├── semantic job
  │     ├── visible-copy version
  │     ├── layout archetype
  │     ├── ancestors
  │     └── locks
  ├── SharedComponentRegistry
  ├── HumanFeedbackRegistry
  ├── AcceptanceStandard
  └── CandidateEvidence
```

A physical page number is presentation order, not identity.

## 4. Three independent locks

### Semantic lock

Freezes page purpose, scientific claims, equations, values, evidence and required/forbidden content.

### Copy lock

Freezes every audience-visible string, including captions, labels, table cells and figure annotations.

### Visual lock

Freezes body composition and shared-component binding after explicit human PASS.

A later round may unlock one dimension without unlocking the others. For example, a footer repair does not authorize body copy or layout changes.

## 5. Human-feedback memory

The plugin must ingest every available human annotation and direct rejection for the artifact family.

Each item retains:

- immutable raw comment;
- source artifact/page/coordinates/type/colour;
- normalized intent;
- stable page/component target;
- lifecycle state;
- supersession relation;
- verification method;
- current-candidate verdict.

Lifecycle:

```text
ACTIVE
SUPERSEDED
RETIRED
INSTRUCTOR_ONLY
RESOLVED_BUT_GUARDED
CURRENT_ROUND_OPEN
```

A new version, page renumbering or automated PASS never closes an item by itself.

## 6. No executor authorship

The presentation executor may:

- escape and typeset approved copy;
- bind approved objects to approved layouts;
- wrap lines;
- resize within frozen role constraints;
- substitute approved asset paths;
- run builds and tests.

It may not:

- add/delete/paraphrase visible prose;
- invent a title, caption, transition, example, warning, prerequisite or takeaway;
- create a new page job;
- merge/delete page jobs;
- choose a new layout archetype;
- fill whitespace with copy;
- move instructor/developer material into the audience artifact.

If approved content does not fit, return a structured layout conflict. Do not solve it by writing.

## 7. Layout grammar

Default composition is one clear vertical reading path.

Allowed multi-region archetypes are explicit components, for example:

- `PEER_50_50`
- `FIGURE_EXPLANATION_60_36`
- `FIGURE_EXPLANATION_56_40`
- `CODE_PEER_50_50`
- `TOP_CONTEXT_BAND_PLUS_FULL_WIDTH_MODEL`
- `QUESTION_TABLE_ANSWER_VERTICAL`
- `CENTRED_ADMIN_TABLE`
- `PLAIN_TITLE`
- `DEDICATED_CLOSE`

Every archetype defines:

- width ratio;
- gutter;
- top/bottom anchors;
- object roles;
- equal-height regions where applicable;
- fallback when content does not fit;
- forbidden reading paths.

Columns are for peers or stable figure/explanation pairs, not sequential reasoning.

## 8. Shared component library

At minimum:

- title;
- header/section navigation;
- footer/source/navigation/page number;
- Question/Answer;
- typography tokens;
- tables;
- code;
- captions;
- scientific figures;
- closing.

Each component has:

- semantic role;
- renderer implementation;
- synthetic fixtures;
- real-deck consumers;
- objective geometry tests;
- whole-slide review evidence;
- human lock state;
- versioned change history.

A component accepted for a deck may not drift during unrelated page repair.

## 9. Cumulative acceptance model

A successor acceptance standard must import all unretired predecessor gates through a machine-readable carry-forward matrix.

Required gate order:

1. artifact identity;
2. complete historical-feedback consumption;
3. page ancestry;
4. modify/freeze/lock scope;
5. exact-copy compliance;
6. scientific/source correctness;
7. pedagogical sufficiency;
8. audience boundary;
9. shared template;
10. layout grammar;
11. whitespace and object scale;
12. typography/code/math glyphs;
13. figure provenance;
14. full-deck narrative/language;
15. PDF/build integrity;
16. independent review and human lock.

Audience-facing failure blocks evidence/release closure. Evidence integrity cannot upgrade a bad deck.

## 10. Division of review labour

### Executor/Codex

Runs nearly all deterministic checks:

- exact counts and IDs;
- text/source/asset diffs;
- lock/freeze enforcement;
- geometry and component tests;
- font/glyph/text extraction;
- code copyability;
- PDF structure;
- reproducibility;
- known-failure fixtures.

### Independent visual/pedagogical reviewer

Judges:

- hierarchy;
- reading path;
- scientific-object scale;
- whitespace use;
- visual rhythm;
- natural audience language;
- whether the page actually teaches its job.

### User

Sees only candidates that passed earlier gates and receives a delta bundle. User PASS immediately locks the page/component.

## 11. Two-to-four-round convergence protocol

### Round 0 — Freeze and component proof

Freeze history, page map, copy and layouts. Prove shared components and lock them.

### Round 1 — High-risk proof

Render only pages with new structures, repeated historical failures or shared-component consumers. Lock accepted pages.

### Round 2 — Full candidate

Assemble the full deck from locked pieces and frozen specifications. Run all deterministic and independent review gates before presenting it.

### Round 3 — Bounded repair

Modify only rejected PageIDs/components. All others are frozen. Lock newly accepted pages.

### Round 4 — Optional subtle polish

Only explicitly named minor issues. No broad cleanup or structural rewrite.

Convergence invariants:

```text
open_pages_next <= open_pages_current
locked_pages_next >= locked_pages_current
unrelated_regressions = 0
unauthorised_changed_pages = 0
```

A fifth broad repair round triggers incident review rather than routine continuation.

## 12. User-facing delta bundle

Every review round should present:

- pages/components changed;
- before/after whole-slide comparison;
- human-feedback IDs addressed;
- objective gates passed/failed;
- dependency pages rerendered;
- unrelated pages proven unchanged;
- remaining open pages.

The user should not have to re-annotate the entire deck because a few pages changed.

## 13. Success metrics

The workflow is not production-ready until real replay demonstrates:

- a historical feedback pattern returning on a different page is caught;
- a missing feedback row blocks editing;
- a page deletion without semantic relocation fails;
- an executor-added sentence fails exact-copy checks;
- a locked page/body change fails;
- a shared footer repair leaves locked body pixels unchanged;
- an unauthorised column layout fails;
- a later acceptance standard omitting an older gate fails;
- a known bad deck does not receive a shallow global PASS;
- one real deck converges within two to four review rounds.

## 14. Implementation stages

### P0.1 — Registries and schemas

Implement version lineage, feedback registry, stable PageIDs, page/component locks and carry-forward acceptance schema.

### P0.2 — Exact-copy and change-scope enforcement

Implement visible-copy comparison, source/asset/body-render locks and round-frozen checks.

### P0.3 — Layout grammar and shared-component fixtures

Implement approved archetypes, template components and geometry tests.

### P0.4 — Review orchestration

Implement deterministic executor gate → isolated independent review → human delta review → lock update.

### P0.5 — Real replay

Replay at least one teaching deck and one research deck with historical regressions before promoting runtime behaviour.

## 15. Project-specific boundary

Do not encode course page numbers, model examples, exact feedback counts, equations, assessment policies or course-specific wording in the generic plugin.

The reusable capability is controlled revision, cumulative feedback, exact-copy authority, layout grammar, deterministic rejection, independent aesthetic review and monotone convergence.
