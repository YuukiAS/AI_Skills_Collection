# Historical Black-Box Render Validator Specification

Status: **IMPLEMENTATION SPEC / MUST PASS INDEPENDENT REVIEW BEFORE PROMOTION**

This specification defines a reusable presentation validation runtime that learns
nothing from artifact names or expected verdict labels. It validates exact
rendered candidates, historical regressions, positive visual ancestry, and review
evidence through generic invariants plus a separate project adapter.

## 1. Separation of responsibilities

The runtime has two layers.

### Generic reusable core

Lives in `AI_Skills_Collection` and contains no project/version/PageID literals.

It validates:

- exact artifact/render identity;
- page inventory and hashes;
- typography and projection readability;
- primary-object scale;
- whitespace versus underused content;
- reading path and peer/sequential layout semantics;
- shared-component consistency;
- Question/Answer geometry;
- table/code/figure readability;
- code-output and evidence-interpretation proximity;
- positive visual ancestry object preservation;
- no-deletion-as-repair;
- whole-slide and contact-sheet rhythm;
- numerical figure/source/summary consistency framework;
- exact-candidate closure of render-dependent guards;
- release-state routing;
- lock/allowlist/diff protection;
- evidence completeness and reviewer scope;
- black-box holdout and mutation execution.

### Project adapter

Lives with the project and supplies implementation-time project constraints, but
does **not** own historical expected verdicts.

It supplies:

- artifact inventory and lineage;
- PageIDs and page jobs;
- copy/content/layout authority;
- active historical guards;
- positive visual ancestry;
- domain-specific numbers, variables, labels and source anchors;
- project-specific mappings/guards needed to interpret generic findings;
- current release-state rules.

The adapter cannot weaken or suppress generic findings.

### Critic-owned evaluation oracle

The exact expected historical artifact/page outcomes are frozen by an independent
project Critic before implementation. They are evaluation data, not detector
configuration.

The oracle supplies, for evaluation only:

- artifact/page expected status;
- expected failure classes;
- known positive scoped controls;
- severity/evidence bindings;
- explicit rebuttals of prior classifications.

Neither Generic Producer nor Adapter Producer may receive the oracle or a mirror
of its expected verdict fields. The Parent Controller and fresh Auditor may load
it only after Producer candidate commits freeze.

If the oracle is incomplete or ambiguous, implementation is blocked.

## 2. Detector API boundary

The generic core receives normalized objects only:

```text
artifact_identity
page_image_and_hash
page_object_map
text_role_map
layout_role_map
authority_constraints
positive_ancestry_constraints
numerical_claim_contracts
review_evidence
```

It must not receive artifact version names, project PageIDs, feedback IDs or
expected verdict labels as detector control flow inputs.

The adapter maps generic findings back to project identities after detection.
Expected verdict comparison occurs outside both production layers in the
Parent/Auditor evaluation plane.

## 3. Required generic detector families

```text
D-ARTIFACT-IDENTITY
D-PAGE-INVENTORY
D-REVIEW-EVIDENCE-COMPLETENESS
D-TYPOGRAPHY-FLOOR
D-PRIMARY-OBJECT-SCALE
D-WHITESPACE-SCALE-INTERACTION
D-READING-PATH
D-PEER-ALIGNMENT
D-QA-GEOMETRY
D-SHARED-COMPONENT-CONSISTENCY
D-TABLE-READABILITY
D-CODE-READABILITY
D-CODE-OUTPUT-PROXIMITY
D-FIGURE-READABILITY
D-EVIDENCE-INTERPRETATION-PROXIMITY
D-POSITIVE-ANCESTRY-PRESERVATION
D-NO-DELETION-AS-REPAIR
D-CONTACT-SHEET-RHYTHM
D-NUMERICAL-FIGURE-CONSISTENCY
D-RENDER-PENDING-CLOSURE
D-LOCK-ALLOWLIST-DIFF
D-RELEASE-STATE-ROUTING
```

Every detector must expose:

```text
detector_id
version
input_schema
finding_schema
production_function
positive_controls
negative_controls
hidden_holdout_hook
phase_state
```

## 4. Black-box execution topology

```text
Parent Controller
├─ fresh Producer: implements validator candidate
├─ public tests only
├─ candidate commit freezes
├─ Parent loads Critic-frozen oracle and creates hidden holdout/mutation pack outside Producer context
├─ fresh read-only Auditor: runs hidden pack and historical corpus
├─ fresh Mechanism Critic: inspects architecture, evidence and false pass/fail risk
└─ repair loop with new Producer/Auditor/Critic contexts
```

The Producer cannot see:

- hidden expected findings;
- Critic-frozen oracle rows or any derivative verdict table;
- hidden holdout artifact/page selection;
- hidden mutation seeds;
- exact hidden threshold-boundary cases;
- Auditor scratchpad or prior hidden results.

## 5. Anti-fitting rules

The generic core fails static review if it contains or branches on:

- project names;
- artifact version names;
- project PageIDs;
- feedback IDs;
- artifact hashes or filenames;
- expected verdict labels;
- fixture/test/mutation IDs;
- one hard-coded bad phrase/value/coordinate without a general authority rule.

Required checks:

- AST scan;
- import graph scan;
- string/literal scan;
- test-only path scan;
- production-hook identity check;
- canonical mutation payload uniqueness;
- no candidate-provided expected/allowed fields expanding authority.

## 6. Positive and negative evidence

A validator cannot pass by rejecting everything.

It must pass:

- compliant synthetic pages/components;
- scoped positive properties from historical artifacts;
- an unrelated deck under the same core.

It must reject:

- known historical regressions;
- hidden randomized mutations;
- coordinated multi-field attempts to fake compliance;
- stale or incomplete review evidence;
- pre-final candidates routed to users.

## 7. Mutation framework

Hidden mutations are applied after candidate freeze and include randomized:

- object shrinking plus unused body space;
- evidence/interpretation separation;
- peer-column imbalance;
- protected-object deletion;
- diagram-to-prose substitution;
- table/code typography reduction;
- code-output detachment;
- Q/A rule deletion or block leakage;
- shell element removal/abbreviation;
- mathematical glyph corruption;
- variable/unit/filter/scale chart corruption;
- stale evidence and partial-review false global PASS;
- release-state promotion before final gate.

The same production detector functions must catch public and hidden mutations.

## 8. Numerical figure contract

A project adapter provides:

```text
figure_id
source_data_or_draws
variable
transformation
filtering_or_warmup_rule
unit_and_scale
axis_and_legend_contract
nearby_summary_contract
allowed_tolerance
```

The generic core validates that the rendered figure and source evidence agree.
A clean image is not evidence of numerical correctness.

## 9. Oracle isolation

The accepted mechanism must emit `oracle_isolation_report.json` showing:

- exact oracle file/hash used by Parent/Auditor;
- Generic Producer workspace did not contain oracle bytes;
- Adapter Producer workspace did not contain oracle expected verdict fields;
- generic and adapter import graphs contain no oracle module/path;
- generated public tests contain no historical expected verdict mirror;
- oracle comparison occurs only in Parent/Auditor evaluation code after
  candidate freeze.

Any Producer access to oracle expected outcomes is an anti-fitting failure.

## 10. Reuse extraction

The accepted mechanism must emit `reusability_extraction_report.md` with three
classes:

```text
GENERIC_REUSABLE_NOW
GENERIC_CANDIDATE_NEEDS_MORE_CROSS_DECK_EVIDENCE
STAT5060_SPECIFIC
```

Reusable detector/runtime/schema logic belongs in the shared presentations
plugin. Project lineage, PageIDs, human feedback, historical verdicts, exact
course numerical contracts and release rules stay in the project repository.

Promotion to `GENERIC_REUSABLE_NOW` requires unrelated-deck evidence; passing
only the Tutorial corpus is insufficient.

## 11. Required evidence outputs

```text
corpus_manifest.json
artifact_results.json
page_results.json
detector_coverage.json
detector_ownership_matrix.json
positive_control_results.json
negative_control_results.json
hidden_holdout_results.json
hidden_mutation_results.json
numerical_figure_results.json
render_pending_closure_results.json
static_anti_fitting_report.json
unrelated_deck_results.json
fresh_auditor_report.md
mechanism_critic_report.md
oracle_isolation_report.json
reusability_extraction_report.md
final_acceptance_report.md
```

Every page-level PASS must include substantive observations, not only flags and
hashes.

## 12. Acceptance

```text
GENERIC_CORE_PROJECT_SPECIFIC_BRANCHES = 0
FIXTURE_NAME_BRANCHES = 0
HIDDEN_ORACLE_IMPORTS = 0
PUBLIC_POSITIVE_FALSE_FAILURES = 0
PUBLIC_NEGATIVE_MISSES = 0
HIDDEN_POSITIVE_FALSE_FAILURES = 0
HIDDEN_NEGATIVE_MISSES = 0
HISTORICAL_P0_P1_FALSE_NEGATIVES = 0
RELEASE_FALSE_PASSES = 0
UNRELATED_DECK_GENERALISATION = PASS
FINDING_PRECISION = PASS
FRESH_AUDITOR = PASS
MECHANISM_CRITIC = PASS
CRITIC_ORACLE_COVERAGE = PASS
PRODUCER_ORACLE_ACCESS = NO
ORACLE_ISOLATION_REPORT = PASS
REUSABILITY_EXTRACTION = PASS
```

The runtime is not promotable until these conditions are demonstrated on a real
historical corpus and an unrelated deck.
