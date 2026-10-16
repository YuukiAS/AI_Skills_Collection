# Presentations Core TODO — History, Locks, and Bounded Convergence

Status: PROMOTE_NOW  
Source: repeated STAT5060 Tutorial 01 revisions through V09 and three failed governance materializations, plus earlier research-deck regressions  
Detailed specifications:

- `docs/design/PRESENTATIONS_HISTORY_PREFLIGHT_PAGE_LOCK_AND_MATH_FIGURE_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_EXISTING_DECK_CONVERGENCE_ARCHITECTURE_V1_2026-10-06.md`
- `docs/design/PRESENTATIONS_CONTROL_PLANE_SEMANTIC_FIDELITY_AND_REAL_DETECTOR_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_ANTI_SELF_CERTIFICATION_AND_CONVERGENCE_GOVERNANCE_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_PRODUCTION_DETECTOR_AUTHENTICITY_AND_EVIDENCE_BINDING_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_INDEPENDENT_EXECUTION_AND_REVIEW_ARCHITECTURE_2026-10-06.md`
- runtime contracts: `plugins/codex/plugins/presentations/shared/anti-shortcut-production-contract.md` and `independent-review-contract.md`

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
28. separate materializer and validator paths so generated truth is not validated by regenerating it through the same code;
29. production-hook identity: accepted controls, negative mutations and persisted validation call the same detector function;
30. fixture-name branches are forbidden inside detector logic;
31. row ancestry validates exact allowed stable/component target sets, not merely global ID validity or page-map existence;
32. persisted Git object identities are real 40-hex blobs resolved from commit plus path, never echoed path strings;
33. non-self-referential implementation/evidence binding, preferably an implementation commit followed by an evidence commit whose runtime validator checks the actual remote head;
34. detector-catalog coverage with honest phase states such as `EXECUTED_PASS` and `SPEC_READY_NOT_EXECUTED`, rather than reporting future copy/render detectors as already passing;
35. trust-domain separation: the executor that edits a candidate cannot authoritatively validate or accept that same candidate;
36. the authoritative deterministic validator runs only after executor stop in a fresh process/CI or strictly isolated read-only subagent;
37. validator/reviewer runtime is version-pinned and immutable during an ordinary deck revision task;
38. executor completion state is at most `READY_FOR_INDEPENDENT_VALIDATION`, never final PASS;
39. blind rendered-artifact review is isolated from executor narrative and expected human-rejection answer keys;
40. repeated new P0 self-certification defects trigger a generic validator rebuild rather than indefinite project-local V5/V6/V7 patches;
41. a frozen authority bundle and explicit round allowlist exist before candidate editing begins;
42. every candidate carries a proof-carrying patch manifest that maps modified PageIDs/components to feedback IDs and proves unrelated locks unchanged;
43. required scientific/teaching objects cannot disappear unless an explicit Planner-approved relocation record names the destination;
44. local layout/build pressure cannot authorize semantic deletion, unapproved copy, page merging, or archetype replacement;
45. full-deck regeneration requires explicit Planner approval and is forbidden by default once most pages are locked;
46. shared-component changes automatically place every consumer page in deterministic regression scope without reopening semantic/copy locks;
47. review scope is explicit, and a scoped review cannot issue a global PASS while mandatory global requirements remain unreviewed;
48. historical rejected artifacts include hidden holdouts unavailable to the executor, preventing prompt tuning against the full answer key;
49. recurrence of a closed guard triggers root-cause repair of the shared primitive/authority/detector rather than another page-local patch;
50. if open issues fail to decrease or accepted items reopen, the next action is root-cause analysis, not another broad candidate.

## Why this is core

The visible-deck failure recurred across multiple real versions even after ledgers and review standards existed. The missing capability is not another checklist. It is enforcement and controlled revision: history must be counted and consumed, accepted pages/components must be immutable, executors must not author copy, and a local repair must not rewrite unrelated parts of the deck.

The first governance failure showed that a control plane can report the correct row/page/gate counts while losing semantic meaning, mapping feedback to the wrong page, truncating source fields or testing only pre-declared violation flags.

The second governance failure showed that even structured inputs and 24/24 rejected fixtures can self-certify an incomplete system: annotation totals can be wrong, ancestry can remain unenforced row by row, source evidence can be stale, component fixtures can be made unique but irrelevant, and detectors can be tuned to one chosen bad value while still returning `PASS`.

The third governance failure showed that separate materializer/validator files and corrected headline counts are still insufficient when mutation tests branch on fixture names, positive controls only assert constants, persisted blob fields contain paths rather than Git objects, and final/remote arguments are accepted by syntax rather than verified against repository state.

The broader presentation history shows where the executor repeatedly chooses proxies: delete difficult content to solve layout, regenerate unrelated pages during local repair, shrink objects rather than redesign composition, treat source presence as rendered quality, and treat the latest feedback round as if earlier human rejections no longer exist.

Counts, schema presence, unique fixture tuples, fixture totals, file separation, and longer prompts are necessary but never sufficient.

## Promotion gate

- omission of one historical item blocks editing;
- wrong batch-level annotation-type totals block editing;
- a generic/non-actionable normalized feedback guard blocks editing;
- an unknown or wrong historical-page mapping blocks editing even when the target PageID is otherwise valid;
- a row whose targets are globally valid but not allowed for its exact historical artifact/page blocks editing;
- unresolved feedback conflict blocks editing;
- Markdown/code-span pipe corruption blocks source materialization;
- an executor mutation of Planner authority blocks acceptance unless separately ratified, and still remains a scope finding;
- stale or unvalidated persisted preflight evidence blocks review;
- a persisted `git_blob_sha` that is not a real 40-hex object blocks review;
- final/remote commit arguments must match actual local and remote repository state, not merely a SHA-shaped string;
- page deletion without approved semantic relocation blocks editing;
- incomplete page/component binding blocks implementation;
- touching a round-frozen page blocks commit;
- touching a human-PASS body region blocks commit;
- executor-added visible copy blocks commit;
- an unauthorised layout archetype blocks commit;
- a candidate without a complete proof-carrying patch manifest blocks independent validation;
- modified PageIDs/components outside the explicit round allowlist block the candidate;
- disappearance of a required object without an approved relocation blocks the candidate;
- an acceptance standard that omits an unretired predecessor gate blocks review;
- authorised header/footer change preserves locked body pixels and revalidates all consumers;
- Question/Answer one-line and multi-line fixtures align within calibrated whole-slide tolerance;
- a figure labelled with literal `eta` fails, while a `$\eta$` render passes;
- malformed fixtures mutate real inputs and are caught by general production detectors without fixture-ID branches or magic predicates;
- positive controls pass through those same production detector functions;
- component fixtures are demonstrably relevant to the component they claim to test;
- a committed forbidden audience-path change is detected even after the worktree is clean;
- detector coverage names every required detector and distinguishes executed proof from future specification readiness;
- the candidate executor cannot modify the authoritative validator/reviewer runtime in the same task;
- authoritative validation is launched outside the executor context and is artifact/commit-bound;
- a subagent counts as independent only when it has fresh context, read-only candidate/authority, no answer key and no permission to edit tests or gates;
- executor self-tests are debugging evidence only and cannot become release acceptance;
- a scoped reviewer cannot emit global PASS for unreviewed mandatory requirements;
- a previously closed guard recurrence rejects the candidate and adds a root-cause regression guard;
- one real existing deck converges within two to four review rounds under the new workflow.
