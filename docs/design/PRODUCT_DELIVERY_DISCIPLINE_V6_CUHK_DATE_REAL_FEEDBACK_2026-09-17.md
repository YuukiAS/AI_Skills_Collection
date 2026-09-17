# Product Delivery Discipline v6 — CUHK Date Real-Project Feedback

Date: 2026-09-17
Status: `REAL_PROJECT_FEEDBACK_FOR_V6_REVIEW`
Source project: `YuukiAS/CUHK_Date`

This is factual feedback from a real product-delivery failure after Questionnaire V4 was reported as ready for founder/GPT Work review. It is intended for the ongoing v6 Planner/Critic refinement. It does not modify production skills/plugins.

## 1. Bottom line

The current v6 direction is substantially relevant to this failure, especially:

- W1 Acceptance Review Admission / Vertical Closure;
- W3 Exact Failure / Verification / Evidence Fidelity;
- F-B Design-System Coherence;
- F-C Actual-Surface Convergence;
- producer self-QA before external/human review.

If those mechanisms were consumed strongly, several CUHK Date failures should not have reached the founder.

However, the current v6 proposal is still **underspecified for data-backed consumer forms and localized web products**. It can still allow a producer to present a candidate as acceptance-ready while all broad tests pass but:

- a raw internal enum token leaks as English into Chinese UI;
- a “complete” city catalog is actually a hand-written 40-city demo;
- an external search feature passes mocked unit tests while hosted provider search is unavailable/weak;
- a number input passes final-value validation but corrupts ordinary keystroke sequences;
- one product branch (e.g. undergraduate) works while sibling branches (TPG/RPG/PhD) were never exercised;
- a fallback/recovery path is counted as proof that the primary feature is implemented;
- a real backend capability exists (YuNet moderation) but the hosted candidate is configured onto a deferred/manual path, so the user-visible lifecycle is not actually closed.

The proposal does not need another top-level capability. The missing protections can fit inside W1/W3/F-C and Frontend Design.

## 2. Concrete CUHK Date evidence

Candidate history:

```text
CUHK_Date main candidate reported READY_FOR_FOUNDER_QUESTIONNAIRE_REVIEW_ROUND2
-> founder found ~40 product/UX defects
-> V4 rebuilt and later appearance pass reported ready for GPT Work audit
-> founder spot-check stopped GPT Work before launch because obvious defects still remained
```

Relevant current CUHK Date evidence at diagnosis start:

```text
main = e85dcacfa8bc5808006e2db4f5348b45bece8dc4
Questionnaire = 4.0.0-candidate
```

Canonical defect record:

```text
docs/operations/QUESTIONNAIRE_V4_PRE_REVIEW_BLOCKERS_2026-09-17.md
```

### 2.1 Localization / raw-token leakage

The V4 localization helper fell back to the internal key when a translation was absent. This allowed values such as `undecided` or other enum-like English/internal strings to appear in a Simplified/Traditional Chinese consumer UI.

Broad typecheck/build/unit suites did not fail because the values were technically valid.

This is not merely “copy polish”; it is a production acceptance defect that should be deterministically gateable.

### 2.2 Catalog breadth was asserted by implementation shape, not product coverage

The future-city selector was described as a GeoNames-derived local registry, but the shipped candidate contained only a small hand-written list of a few dozen cities. Ordinary cities such as Ningbo and Shijiazhuang were missing.

The implementation had:

```text
canonical IDs
search function
aliases
UI combobox
```

but did not have a product-level coverage contract or minimum representative corpus. Presence of the architecture was mistaken for capability completion.

### 2.3 External media search tests proved adapters, not the hosted feature

Book/movie/series provider tests mocked `fetch` and verified request language / response parsing. These are valid unit tests but do not prove:

- staging provider credential exists;
- actual provider is reachable;
- representative Chinese/English titles return results;
- the normal authenticated product UI can use the provider.

The UI had a custom-text fallback, which made the route technically recoverable but let the primary canonical-search feature remain unproven.

### 2.4 Input validation did not test user interaction sequence

Height final values such as 100/170/230 could validate, while the controlled number input clamped every intermediate keystroke. A normal sequence such as typing `178` could therefore produce a corrupted result.

Value-domain tests were green; event-sequence behavior was broken.

### 2.5 Variant coverage was not an acceptance matrix

The Programme Registry actually contained undergraduate and graduate entries, and the API supported career filtering. The founder still observed an undergraduate-only experience. Source-count and type-level evidence did not prove hosted behavior across:

```text
undergraduate
TPG
RPG/MPhil
PhD
```

A single happy-path acceptance smoke is insufficient when the product has explicit material branches.

### 2.6 Backend capability existed but hosted lifecycle did not use it

A real OpenCV YuNet face detector existed and could reject no-face/multiple-face/unusable photos. Staging/production config nevertheless used `local_operator_batch`, meaning upload followed a deferred/manual review path rather than exercising the real automatic detector inline.

Code existence + unit tests therefore overstated the user-visible hosted capability.

## 3. What v6 already gets right

### W1 Vertical Closure

The proposed chain:

```text
authoritative source / contract
-> backend/runtime
-> persistence/state
-> normal product entry
-> real target behavior
-> failure/recovery semantics
-> targeted regression
-> actual-surface confirmation
```

is the correct architecture for the CUHK Date failure.

The key refinement is that “real target behavior” must sometimes include **coverage breadth / representative variants**, not only one successful example.

### W3 Evidence Fidelity

W3 correctly says synthetic/helper/unit evidence proves only that surface. This directly applies to mocked media-provider tests and deterministic photo fixtures.

The missing specificity is how to detect when the goal's primary claim inherently requires hosted/provider/interaction evidence.

### F-C Actual-Surface Convergence

F-C would help with obvious raw-token leakage, inconsistent controls and visibly poor interaction. But “look at whole product” alone is too subjective to reliably catch localization completeness or hidden branch gaps. Some defects need deterministic pre-review gates.

## 4. Proposed v6 refinements — no new top-level capability

### R-CU1 — Representative Capability Coverage inside W1

For a user-facing capability backed by a catalog, provider, or material product variants, Vertical Closure should include a lightweight **representative coverage contract** when breadth is part of the promise.

Examples:

```text
catalog/search -> minimum corpus + representative known items
multi-branch flow -> representative branches/personas
locale support -> every reachable enum/control in every supported locale
provider integration -> actual configured hosted provider
```

Do not require this for every tiny task. Trigger when the frozen objective contains breadth claims such as “all programmes”, “city search”, “supports Chinese/English”, “all major states”, “multiple providers/variants”.

A schema, handler, generated file, or sample list is not sufficient evidence of breadth.

### R-CU2 — Recovery/fallback must not satisfy the primary capability claim

Add to W1/L6:

> A fallback can prove recoverability, but it cannot prove the primary requested capability is complete unless the Goal explicitly accepts the fallback as an equivalent product outcome.

Examples:

- `使用我输入的名称` proves graceful media-search recovery; it does not prove canonical media search works.
- `needs_review` manual photo queue proves safe degradation; it does not prove automatic face moderation is active.
- generic/raw text entry does not prove a canonical city/programme registry is complete.

### R-CU3 — Hosted/external-provider claim requires real-provider evidence inside W3

When a feature claim depends on an external provider/service, acceptance evidence should include a bounded probe of the **real configured target environment** when safe and feasible.

Mock/provider-unit tests remain required but cannot alone support a hosted capability claim.

A useful pattern:

```text
provider adapter unit test
+ configured-capability check
+ representative target-environment query
+ normal product-entry confirmation
```

Do not require paid calls when not necessary; use bounded representative probes.

### R-CU4 — Interaction controls need sequence-level verification when intermediate states matter

W3 should distinguish:

```text
final value validity
vs
normal user input sequence validity
```

For controlled inputs, range controls, typeahead, multi-step selection, drag/rank controls, or debounced autosave, representative interaction sequences should be tested when the implementation can transform intermediate input.

Example regression:

```text
type 1 -> 17 -> 178
paste 178
backspace/replace
blur/commit
```

A final-value schema test does not cover this.

### R-CU5 — Localization integrity is a Frontend acceptance invariant

Add under Frontend Design F-B/F-C:

- user-visible enum/token localization must be complete for supported locales;
- internal enum identifiers must never be a production fallback;
- supported-locale UI should have deterministic completeness tests where values are finite/enumerated;
- actual-surface review should scan for untranslated/internal tokens and unnecessary implementation English;
- proper nouns/acronyms may be allowlisted narrowly.

This would have caught `undecided` and similar leakage before user review.

### R-CU6 — Material branch matrix inside W1/F-C

When a product control explicitly has material branches, acceptance should list representative branches rather than test only the default branch.

CUHK Date example:

```text
UG -> undergraduate programmes / College visible
TPG -> TPG programmes / College hidden
MPhil/RPG -> RPG programmes
PhD -> RPG programmes
```

The matrix remains task-local and small; it is not a repo-wide state machine.

### R-CU7 — User-visible state lifecycle must close across navigation/re-entry

For uploaded/saved/persisted user state, actual-surface acceptance should include the relevant lifecycle, not only immediate mutation success:

```text
action
-> visible result
-> navigation
-> refresh/re-entry
-> same authoritative state
```

This is particularly important for upload status, autosave, setup/configured status and consent/state machines.

### R-CU8 — Existing accepted structured interaction should be protected during rewrites

W5 adjacent-behavior protection should explicitly cover a proven user interaction pattern when a rewrite replaces the component. A “new schema” should not silently regress a previously working structured selector into a lower-quality free-text fallback unless that simplification was an explicit product decision.

CUHK Date example: curated per-interest detail tags were replaced with a generic text-list interaction during V4 rewrite.

## 5. Suggested replay gate for v6

Add one real/synthetic workflow regression using the CUHK Date pattern:

```text
Goal claims:
- two Chinese locales
- searchable external/provider-backed content
- generated catalog breadth
- several product branches
- controlled numeric input

Candidate intentionally contains:
- one untranslated enum fallback
- catalog with only demo entries
- mocked provider tests but provider unavailable in staging
- one branch untested/broken
- number input that corrupts a normal keystroke sequence
- fallback that keeps flow completable
```

Expected discipline behavior:

```text
Acceptance Review Admission = DENIED
READY_FOR_USER_REVIEW = NO
```

The producer should identify the concrete incomplete rows before GPT Work/user review, despite broad build/unit suites being green.

Negative control: a small docs/server-only task should not inherit this entire UI/catalog/provider matrix.

## 6. Recommended disposition for Planner/Critic

Do not add a new W6 or another global checklist layer.

Recommended mapping:

```text
R-CU1 / R-CU2 / R-CU6 / R-CU7 -> W1 Vertical Closure / Acceptance Admission
R-CU3 / R-CU4                  -> W3 Verification / Evidence Fidelity
R-CU5                           -> Frontend F-B / F-C
R-CU8                           -> W5 adjacent behavior + Frontend implementation
```

This preserves v6's smaller architecture while making its admission criteria harder to satisfy with proxy PASS, demo catalogs, fallback-only capability, mock-only provider evidence, or default-branch-only smoke tests.

## 7. Project-specific context that should NOT become generic rules

Do not encode the following CUHK Date specifics into the generic discipline:

- CUHK Programme names or degree taxonomy;
- Ningbo/Shijiazhuang as universal city fixtures;
- Questionnaire V4 fields;
- YuNet specifically;
- TMDB/OpenLibrary specifically;
- Meet at CU visual styling;
- Dating hard-filter policy.

Only the delivery failure patterns above are candidates for generic promotion.