# Presentations Core TODO — History, Locks, and Bounded Convergence

Status: PROMOTE_NOW  
Source: repeated STAT5060 Tutorial 01 revisions through V09 and two failed governance materializations, plus earlier research-deck regressions  
Detailed specifications:

- `docs/design/PRESENTATIONS_HISTORY_PREFLIGHT_PAGE_LOCK_AND_MATH_FIGURE_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_EXISTING_DECK_CONVERGENCE_ARCHITECTURE_V1_2026-10-06.md`
- `docs/design/PRESENTATIONS_CONTROL_PLANE_SEMANTIC_FIDELITY_AND_REAL_DETECTOR_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_ANTI_SELF_CERTIFICATION_AND_CONVERGENCE_GOVERNANCE_TODO_2026-10-06.md`

## Core requirements

The presentations workflow must add first-class support for:

1. exact historical-feedback count preflight before any source edit;
2. feedback lifecycle and supersession;
3. explicit modify / human-locked / round-frozen scopes for every revision;
4. immutable human-PASS page locks with body-region hash/pixel protection;
5. separate semantic, visible-copy and visual locks;
6. shared-component locks for title, header, footer, Question/Answer geometry, typography, columns, caption, code, table, figure and closing styles;
7. retained and aligned Question/Answer accent rules;
8. stable semantic page IDs and explicit ancestry across page-number/version changes;
9. exact-copy enforcement so the executor cannot add audience-visible prose;
10. a versioned layout grammar with approved column/page archetypes rather than page-local improvisation;
11. cumulative acceptance standards with a predecessor-gate carry-forward matrix;
12. real mathematical glyphs inside scientific figures (`$\eta$`, `$\beta$`, `$\kappa$`, `$\mu$`) rather than English transliterations;
13. deterministic Codex rejection before isolated visual/pedagogical review;
14. a user-facing delta bundle instead of repeated full-deck re-annotation;
15. two-to-four-round monotone convergence: open pages decrease, locked pages increase, unrelated regressions remain zero;
16. Planner-authored structured semantic sources separated from generated registries and independent validation;
17. specific executable guard requirements for every human-feedback item, not generic “preserve and review” placeholders;
18. explicit artifact-version page maps and explicit page/component bindings, never physical-page or keyword heuristics;
19. executable gate contracts with inputs, detector/reviewer procedures, evidence outputs, dependencies and pass conditions;
20. realistic mutation tests that exercise actual detectors rather than boolean violation flags;
21. batch-level annotation count authority when historical per-row type labels are lossy, so aggregate Highlight/Text totals remain exact;
22. row-level ancestry enforcement for every feedback item, not only static checks that a historical map file exists;
23. immutable Planner-source blobs, with any parser or serialization problem routed back to Planner rather than silently repaired by the executor;
24. persisted preflight/source-read evidence independently revalidated against repository, branch and start/final/remote commits;
25. base-to-head audience-artifact protection rather than clean-worktree or staged-diff self-certification;
26. semantically relevant component proof-fixture contracts rather than arbitrary unique or index-rotated fixture tuples;
27. general invariant detectors with positive controls and multiple distinct mutations, not one magic bad number, phrase, token or hash;
28. separate materializer and validator paths so generated truth is not validated by regenerating it through the same code.

## Why this is core

The visible-deck failure recurred across multiple real versions even after ledgers and review standards existed. The missing capability is not another checklist. It is enforcement and controlled revision: history must be counted and consumed, accepted pages/components must be immutable, executors must not author copy, and a local repair must not rewrite unrelated parts of the deck.

The first governance failure showed that a control plane can report the correct row/page/gate counts while losing semantic meaning, mapping feedback to the wrong page, truncating source fields or testing only pre-declared violation flags.

The second governance failure showed that even structured inputs and 24/24 rejected fixtures can self-certify an incomplete system: annotation totals can be wrong, ancestry can remain unenforced row by row, source evidence can be stale, component fixtures can be made unique but irrelevant, and detectors can be tuned to one chosen bad value while still returning `PASS`.

Counts, schema presence, unique fixture tuples and fixture totals are necessary but never sufficient.

## Promotion gate

- omission of one historical item blocks editing;
- wrong batch-level annotation-type totals block editing;
- a generic/non-actionable normalized feedback guard blocks editing;
- an unknown or wrong historical-page mapping blocks editing even when the target PageID is otherwise valid;
- unresolved feedback conflict blocks editing;
- Markdown/code-span pipe corruption blocks source materialization;
- an executor mutation of Planner authority blocks acceptance unless separately ratified, and still remains a scope finding;
- stale or unvalidated persisted preflight evidence blocks review;
- page deletion without approved semantic relocation blocks editing;
- incomplete page/component binding blocks implementation;
- touching a round-frozen page blocks commit;
- touching a human-PASS body region blocks commit;
- executor-added visible copy blocks commit;
- an unauthorised layout archetype blocks commit;
- an acceptance standard that omits an unretired predecessor gate blocks review;
- authorised header/footer change preserves locked body pixels;
- Question/Answer one-line and multi-line fixtures align within calibrated whole-slide tolerance;
- a figure labelled with literal `eta` fails, while a `$\eta$` render passes;
- malformed fixtures mutate real inputs and are caught by general production detectors without fixture-ID branches or magic predicates;
- component fixtures are demonstrably relevant to the component they claim to test;
- a committed forbidden audience-path change is detected even after the worktree is clean;
- one real existing deck converges within two to four review rounds under the new workflow.
