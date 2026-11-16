# Presentations Validator V2 — Frozen Specification

Date: 2026-11-14
Status: **FROZEN PLANNER AUTHORITY**
Implementation repository: `YuukiAS/AI_Skills_Collection`

## 1. Why V2 exists

Validator V1 is not an accepted production validator. Three independent Auditor rounds rejected it for authority-binding, lock-proof, source-identity, review-scope and historical-replay failures.

STAT5060 Tutorial V19 exposed a separate class of failures: mechanically valid slides with poor rendered composition, local crowding, bad spacing, tiny objects, weak columns, invalid captions, short arrows and whitespace imbalance.

V2 must solve both classes without conflating them.

The design rule is:

> deterministic checks prove objective contracts; anything that still needs visual or pedagogical judgment returns REVIEW. Absence of a deterministic failure is never sufficient evidence for aesthetic PASS.

## 2. Package

Canonical target:

```text
plugins/codex/plugins/presentations/shared/validator_v2/
  presentations_validator_v2/
    cli.py
    schemas.py
    io.py
    integrity/
    layout/
    render/
    review/
    adapters/
  tests/
  README.md
```

V2 may reuse repaired generic code from V1, but must not inherit V1 acceptance status or its unsafe optional-field semantics.

Production code must not import STAT5060 project-local scripts.

## 3. Three-layer result model

### Layer A — authority / integrity

Checks:

- exact authority vs candidate separation;
- repository identity;
- baseline commit;
- candidate commit/tree;
- exact source path/role/blob/commit;
- artifact hash identity;
- round scope;
- human/page/component locks;
- required-object preservation;
- full derivative-record fidelity;
- component inverse/fidelity;
- review coverage;
- visible-copy authority;
- no candidate-authored authority expansion.

### Layer B — deterministic rendered layout

Checks:

- typography roles;
- body rail;
- local font/leading/compression overrides;
- semantic spacing;
- teaching-list spacing;
- columns/peer anchors/gutters;
- caption/table-note geometry;
- Question/Answer geometry;
- footer geometry and links;
- section-label budget;
- table-cell wrapping;
- diagram/arrow/node geometry;
- closing geometry;
- overflow/collision;
- protection/pixel regression when a baseline exists;
- whitespace/density objective contradictions.

### Layer C — rendered semantic review routing

The deterministic engine may emit REVIEW for:

- whitespace balance without an objective contradiction;
- page density without hard violation;
- custom columns/archetypes;
- semantic caption necessity;
- content sufficiency;
- narrative hierarchy;
- information load;
- subtle alignment/optical quality not reliably measurable.

REVIEW is a first-class state. It must never be auto-converted to PASS.

## 4. Final deterministic states

Per check:

- `PASS`
- `FAIL`
- `REVIEW`
- `NOT_VERIFIED`

Artifact-level deterministic result:

- any mandatory FAIL => `DETERMINISTIC_FAIL`
- no FAIL but mandatory NOT_VERIFIED => `DETERMINISTIC_INCOMPLETE`
- no FAIL/NOT_VERIFIED but REVIEW exists => `DETERMINISTIC_NO_FAIL_REVIEW_REQUIRED`
- no FAIL/NOT_VERIFIED/REVIEW => `DETERMINISTIC_PASS`

None of these states is equivalent to final rendered/pedagogical release acceptance.

## 5. Authority-binding repairs required from V1

V2 must permanently regress the three Auditor packets.

### Required JSON/parser behavior

- duplicate JSON object keys must be detected before materialization;
- record collections requiring unique IDs must reject duplicates;
- no duplicate can disappear through dictionary overwrite.

### Mandatory source identity

Authority-bound source identity includes:

- source ID;
- exact role;
- exact path;
- exact required commit/evidence binding;
- Git blob SHA when required;
- immutability policy.

Missing mandatory path/blob/commit fields fail.

Candidate self-consistency is insufficient. V2 resolves `<commit>:<path>` independently.

### Required-object relocation

A candidate relocation/deletion claim must resolve to a real authority record whose:

- authority ID exists;
- object ID matches;
- destination is allowed;
- relocation semantics match.

A non-empty candidate string is not authority.

### Derivative feedback fidelity

Candidate/derived feedback rows must preserve all authority-bound fields, not only IDs/targets.

### Component fidelity

Component records are full-record compared to authority. Consumer inverse is an additional invariant, not a substitute.

### Review scope

Global PASS claims require exact reviewed coverage of mandatory:

- pages;
- components;
- artifact hashes;
- requirements.

Artifact IDs cannot satisfy hash fields.

Partial coverage cannot issue global PASS.

### Locks

If human/authority locks require evidence, missing `lock_evidence` fails.

### Candidate identity

Missing baseline commit, candidate commit or candidate tree fails before further validation.

### Historical replay

Historical replay uses exact commit-aware Git object lookup. A missing configured evidence locator is FAIL or NOT_VERIFIED; it may never silently substitute another generation/path.

## 6. Layout contract interface

The validator reads a generic layout contract derived from Shared Beamer Core V1.

It must not contain course page numbers, specific visible phrases, fixture IDs or exact bad hashes in production logic.

Suggested input:

```text
layout-contract.yaml
candidate.pdf
candidate-source-manifest.json
semantic-object-map.json
baseline.pdf                  # optional for revision
baseline-source-manifest.json # optional
review-scope.json
```

The semantic object map binds stable semantic roles, not physical page-number exceptions.

## 7. Generic layout detectors

At minimum:

### TYPE
- role font identity/size;
- local font override scan;
- scale/resize scan;
- normal body leading.

### RAIL
- body-left/right rail;
- protected body bounds;
- closing rail.

### SPACE
- list item spacing;
- paragraph→list/table/figure/math;
- math→table/body;
- table→interpretation;
- caption→body;
- Question→next;
- within/between group;
- title→Question when declared.

### COLUMN
- approved preset or REVIEW;
- peer top/baseline anchor;
- visible gutter;
- bottom imbalance routing.

### CAPTION
- owned-object relation;
- below-object;
- left anchor;
- multiline left anchor;
- source vs caption role distinction.

### QA
- Question rule/label/body relation;
- Answer label outside rule;
- Answer rule endpoints.

### FOOTER
- divider/band;
- left credit/source optical centre;
- native navigation link presence;
- page-number geometry;
- source/identity branch.

### SECTION_NAV
- fixed font token;
- single-line label;
- frame-count width budget;
- adjacent gap;
- no shrink/wrap hack.

### TABLE
- semantic atom wrapping;
- header intentional-wrap metadata;
- row/column region binding;
- table font token.

### DIAGRAM
- node style;
- node padding;
- connector boundary;
- collision;
- peer connector geometry;
- visible shaft thresholds.

### CLOSING
- body rail;
- approved closing archetype;
- Questions token/centre;
- region relationship.

### DENSITY / WHITESPACE
- rendered content distribution;
- lower/internal contiguous void;
- primary-object size;
- local crowding;
- compression;
- semantic-block count.

Important: DENSITY/WHITESPACE can auto-FAIL only when an objective contradiction is present. Otherwise it returns REVIEW.

### PROTECTION
- region/component pixel regression;
- expected chrome/brand masks;
- exact allowed change regions.

## 8. No self-certification shortcuts

Production detectors must not branch on:

- fixture name;
- version name;
- mutation ID;
- known bad page number;
- known hash;
- human complaint text;
- expected verdict field.

Public and hidden controls call the same production functions.

## 9. Benchmark corpus

### 9.1 STAT5060 positive

Exact V19 frozen style:
- production commit `62678cd22409906797474752ae4f304f867d96cc`
- PDF SHA-256 `88eae6b2073715729abd9c2b004d1d0f31541c4314c2b64cd49194346b35d6e1`

Expected:
- objective frozen rules: no FAIL;
- explicitly accepted near-boundary values may remain REVIEW;
- validator must never produce an aesthetic global PASS without rendered review.

### 9.2 STAT5060 negatives

Build exact rejected controls from direct human feedback and archived renders. Required classes include:

- large dead whitespace + undersized/crowded content;
- top-heavy layout;
- tiny code/table/body type;
- local negative spacing/compression;
- Question→table crowding;
- caption→body crowding;
- invalid/missing caption role;
- centered caption regression;
- invalid columns / heterogeneous 3-column layout;
- column→full-width orphan prose;
- bad table wrapping;
- Answer rule mismatch;
- footer/source geometry regression;
- short/overlapping arrows;
- section label over-budget;
- closing body-rail regression.

For a human-explicit rejection:
- expected validator/reviewer route is FAIL or REVIEW;
- unqualified PASS is a benchmark failure.

### 9.3 Unrelated fixtures

At least:
- one unrelated teaching/lecture Beamer deck;
- one research/CUHK deck;
- one synthetic minimal deck focused on token boundaries.

## 10. Held-out acceptance

The implementer/Longleaf Codex receives:

- frozen spec;
- public fixtures;
- public mutation/property tests.

GPT Work retains a held-out acceptance pack that is not exposed before implementation stops.

Held-out pack must include:

- coordinated multi-field authority mutations;
- source/path/blob/commit substitutions;
- missing lock evidence;
- partial review/global PASS attack;
- duplicate JSON keys;
- layout boundary mutations near spacing/font/rail thresholds;
- whitespace/crowding combinations;
- unrelated decks;
- standard/CUHK parity candidates.

After each implementation change, acceptance is rerun from a fresh read-only context.

## 11. Acceptance metrics

No single accuracy percentage is sufficient.

Required gates:

1. **Zero false PASS on explicit human-rejected benchmark cases.**
2. V19 has zero objective FAIL.
3. All three historical Validator V1 Auditor P1 classes are covered and pass regression.
4. Hidden authority-integrity mutations are caught.
5. Hidden layout mutations are caught or routed REVIEW as specified.
6. No fixture/mutation-name branching.
7. At least two unrelated deck families run successfully.
8. Review state is preserved; unresolved REVIEW cannot be upgraded by executor claim.

## 12. Promotion boundary

V2 becomes the plugin validator only after fresh independent acceptance.

Until then:
- V1 remains historical candidate;
- project-local V19 validator remains frozen replay evidence;
- deck producers may not modify V2 during the same production task that consumes it.

## 13. Completion state

Implementation executor may only claim:

```text
VALIDATOR_V2_CANDIDATE_READY = YES
READY_FOR_INDEPENDENT_ACCEPTANCE = YES
```

Only GPT Work's independent acceptance may write:

```text
VALIDATOR_V2_ACCEPTED = YES
```
