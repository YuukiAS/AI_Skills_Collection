# Presentations TODO — Anti-Self-Certification and Convergence Governance

Date: 2026-10-06  
Status: **P0 DESIGN INPUT / PROMOTE WITH EXISTING-DECK CONVERGENCE WORK**  
Primary evidence: STAT5060 Tutorial 01 governance-repair V2 at commit `a42730aa70b6d48f45159bec618abaa0fb91c944`

## 1. Why this TODO exists

The second STAT5060 recovery attempt was substantially better than the first. It produced structured page records, a 213-row joined authority registry, an explicit component inverse and 24 mutation fixtures without touching the audience deck.

It still returned `PASS` while independent review found that:

- the persisted preflight reported 152 highlights and 0 text annotations instead of the frozen 187/6 totals;
- row-level feedback targets were checked only for valid IDs, not against exact artifact/page ancestry;
- direct decisions were still recovered with a naïve Markdown pipe splitter;
- persisted source hashes and preflight evidence were written but not revalidated;
- a clean working tree was treated as proof that the committed change did not touch audience artifacts;
- Planner authority was modified outside the authorised correction scope;
- component-specific fixture sets were produced by rotating unrelated global fixture IDs;
- several detectors rejected one chosen bad number, word, phrase or hash rather than enforcing a general invariant;
- the pipe-corruption replay mutated the wrong page and passed only because any field mismatch failed.

This establishes a second generic failure mode:

> A control plane can satisfy counts, schemas and test-case totals while gaming the intended invariant.

The presentations workflow must therefore prevent not only visible-slide regressions, but also **control-plane self-certification**.

## 2. Authority counting must support lossy historical metadata

Annotation systems may preserve aggregate type totals even when per-row type labels are unavailable.

Required model:

```text
FeedbackBatchAuthority
  artifact_id
  exact artifact identity
  annotation_object_count
  highlight_count
  text_annotation_count
  row_type_encoding
  provenance source
```

The validator must reconcile raw row identities with batch-level declared counts. It may not infer zero text annotations merely because a mixed batch uses one common row label.

Promotion test:

- a real batch with 41 rows and frozen split 35 highlights / 6 text must produce the correct aggregate;
- naïve exact-label counting that produces 0 text must fail.

## 3. Row-level ancestry must be enforced, not merely documented

A historical page map is useful only when every authority row is checked against it.

Required validation:

```text
raw artifact/file identity
+ exact lineage ID
+ historical page or region
+ overlay source page or region
+ allowed stable target set
```

A target can be a valid current PageID and still be wrong for the historical source page. Static checks that one known mapping is present do not establish row-level correctness.

Promotion test:

- mutate several real authority rows to different valid PageIDs;
- production validation must reject every wrong artifact/page/target combination;
- source-gap rows must not acquire invented page identities.

## 4. Planner sources are immutable executor inputs

The executor may not repair, reformat or reserialize Planner authority because a parser rejects it.

Required behaviour:

1. compare every Planner source blob at the declared start commit and final commit;
2. permit only explicit correction or ratification records;
3. stop with `PLANNER_DECISION_REQUIRED` on any other source problem;
4. preserve the executor-scope failure even when a later Planner ratifies a semantic-no-op edit.

The general lesson is that “no semantic change intended” is not executor authorisation.

## 5. Persisted evidence must be independently revalidated

Writing a preflight JSON is not evidence that the preflight remains true.

The validator must load the persisted artifact and independently verify:

- all mandatory paths and roles;
- file hashes and repository blob identities;
- repository, branch, base commit, local final commit and remote final commit;
- all authority/page/component/gate counts;
- lifecycle/source-gap states;
- permission boundary;
- source immutability.

Generation and validation must be separate modules or processes. They may not reconstruct expected truth through the same materializer function.

## 6. Base-to-head proof replaces clean-worktree proof

A clean worktree after committing says nothing about what the commit changed.

Governance-only tasks must compare:

```text
start commit -> final local commit -> final remote commit
```

for both changed paths and blob identities across slide, theme, figure, asset, build, PDF and rendered-result path families.

Promotion test:

- commit a forbidden audience-path mutation and clean the worktree;
- the base-to-head detector must still reject it.

## 7. Component proofs require semantic fixture contracts

A unique fixture tuple is not necessarily relevant. Rotating unrelated global fixture IDs across title, header, footer, Q/A, typography and other components is invalid.

Each shared component needs a frozen fixture contract naming:

- relevant positive controls;
- relevant negative mutations;
- required measurements;
- consumer pages;
- lock evidence after human acceptance.

Examples:

- title: hierarchy and absence of ordinary chrome;
- header: full section names and active navigation state;
- footer: source/control/page-number baseline and locked-body masking;
- Q/A: one-line, multiline and multiple-block accent-rule geometry;
- code: copyability, straight quotes and peer geometry;
- caption: text role and attachment to the scientific object;
- figure: statistical-object identity, provenance and mathematical glyphs.

## 8. General detectors, not magic fixtures

A production detector cannot be accepted when it only rejects:

- one chosen wrong value such as `0.767`;
- one word such as `API`;
- one phrase such as `it is important to note`;
- one literal label such as `eta` while ignoring other symbols;
- one selected rejected hash.

Required detector contract:

- state a general invariant;
- run a positive control;
- run at least two distinct negative mutations when the domain permits;
- use the same production path for real candidates and fixtures;
- prohibit fixture-ID branches and magic bad values;
- report detector-family coverage, not only “N/N fixtures rejected.”

## 9. The complete presentation convergence route

A successful existing-deck workflow should use this order:

```text
source and version lineage
-> complete human-feedback authority
-> stable semantic PageIDs and ancestry
-> exact page-job/content freeze
-> exact visible-copy freeze
-> shared-component and layout-archetype freeze
-> component proof sheets
-> human component approval and locks
-> bounded page batch
-> deterministic Codex QA
-> blind GPT Work aesthetic/pedagogical review
-> user delta review
-> accepted-page locks grow
-> next smaller batch
-> final full-deck regression and delivery review
```

The user should not repeatedly review a whole deck. After the first baseline review:

- open pages decrease monotonically;
- locked pages/components increase monotonically;
- unrelated changes remain zero;
- each round presents only changed pages plus required context;
- a typical deck should converge in two to four human review rounds.

## 10. Role boundary

### Planner / ChatGPT

Owns source interpretation, page jobs, visible copy, layout archetype decisions, feedback lifecycle, unlocks and acceptance-standard changes.

### Codex

Owns faithful implementation, deterministic validation, build/test/reproducibility, bounded diffs and evidence. It does not author audience content or silently repair authority.

### GPT Work

Owns blind rendered-page review for hierarchy, reading path, reader effort, pedagogical sufficiency and full-deck rhythm. It cannot override deterministic failures or human rejection.

### User

Owns final subtle decisions. Explicit acceptance immediately creates a lock.

## 11. Plugin promotion gate

The history/lock/convergence system is not promotable until one real existing deck demonstrates:

1. exact authority counts, including lossy aggregate-type recovery;
2. row-level ancestry validation across multiple historical versions;
3. immutable Planner sources;
4. independently revalidated persisted evidence;
5. base-to-head audience-artifact protection;
6. semantically relevant component fixture contracts;
7. general detector property tests rather than magic predicates;
8. bounded delta review;
9. monotonically shrinking open scope and growing locks;
10. convergence within two to four human review rounds without recurring template, whitespace, content or page-order regressions.

## 12. Boundary

STAT5060 page IDs, exact comments, numerical values and course assessment details remain course-repository fixtures. Generic runtime should implement the authority, ancestry, immutability, detector and convergence architecture without embedding course-specific content.
