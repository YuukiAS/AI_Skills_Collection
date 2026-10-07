# Presentations Historical Black-Box Validator — Independent Mechanism Critic Prompt V1

Role: **fresh read-only mechanism Critic**

This is not presentation production and not validator implementation. Do not edit
code, tests, fixtures, authority, slides, PDFs or renders.

## 1. Inputs

Review the exact candidate commits supplied by the Parent Controller for:

- `YuukiAS/AI_Skills_Collection` generic validator candidate;
- `YuukiAS/STAT5060-TA` Tutorial adapter/evidence candidate.

Read:

- the Presentation end-to-end runbook;
- cumulative acceptance contract;
- rendered-artifact/positive-ancestry contract;
- historical black-box validator specification;
- STAT5060 V1–V13 black-box validation specification;
- STAT5060 validator oracle-governance/reuse freeze;
- the exact Critic-frozen historical expected-outcome oracle and its prebuild
  Critic report;
- STAT5060 V14 page-by-page visual repair freeze;
- generic and adapter source/tests;
- static anti-fitting report;
- corpus manifest and every required result artifact;
- fresh Auditor report;
- hidden-pack hash/metadata and summarized outcomes;
- unrelated-deck results.

## 2. Core question

Does the mechanism demonstrate, without answer fitting, that:

1. compliant scoped controls pass;
2. known historical failures fail;
3. failures are identified on the correct artifact/page with the correct class;
4. all materialised V1–V13 and historical-lineage artifacts were actually run;
5. generic reusable logic is separated from STAT5060-specific mapping;
6. the user will not again become the first effective visual reviewer?

## 3. Oracle isolation audit

Verify independently that:

- the oracle was authored/frozen before validator implementation;
- its prebuild Critic gate passed with complete coverage and zero ambiguity;
- neither Generic Producer nor Adapter Producer had access to expected verdict
  fields;
- no source, generated fixture, cache or import graph in either Producer
  candidate mirrors oracle verdict rows;
- Parent/Auditor loaded the exact frozen oracle only after candidate freeze;
- any historical classification change is an explicit evidence-backed rebuttal,
  not a silent Planner/Producer reinterpretation.

Any Producer oracle access is P0.

## 4. Mandatory architecture audit

Verify:

- Generic Producer was isolated from STAT5060 and hidden oracle data.
- Adapter Producer could not edit generic detectors.
- Hidden pack was created only after candidate freeze.
- Fresh Auditor had read-only candidate access.
- The hidden pack used a fresh seed and included coordinated mutations.
- Generic core detector functions were identical across real validation, public
  controls and hidden tests.
- The generic core does not receive version/PageID/feedback-ID values as detector
  control inputs.
- Course adapter maps findings but cannot suppress or reclassify them.

Any failure is P0.

## 5. Anti-fitting audit

Independently inspect the generic source and static report for:

- project names;
- version IDs;
- PageIDs;
- feedback IDs;
- historical filenames/hashes;
- expected verdict labels;
- fixture/test/mutation-ID branches;
- hidden-oracle imports;
- version-based result lookup;
- candidate-provided expected/allowed fields expanding authority;
- magic thresholds without calibration evidence.

Do not accept a self-reported zero. Inspect representative code paths and rerun
static analysis.

## 6. Corpus completeness

Independently reconcile the discovered corpus with:

- version manifest;
- release directories;
- historical artifact page map;
- historical results directories.

Require execution of all materialised artifacts from V1 through V13, plus the
named early, Rich, later-student and proof/golden lineages.

A missing or skipped artifact cannot be hidden by changing the denominator.

## 7. Good-pass / bad-fail audit

### Positive behavior

Confirm at least the frozen scoped historical positives and synthetic compliant
fixtures pass their named gates. A detector that rejects all pages fails.

### Negative behavior

Confirm historical human-rejected artifacts and hidden mutations fail with:

- correct artifact;
- correct physical page and mapped PageID where applicable;
- correct issue class;
- concrete evidence;
- appropriate severity.

Generic “visual issue” findings are insufficient.

### False positives / false negatives

Independently derive counts. Require:

```text
PUBLIC_POSITIVE_FALSE_FAILURES = 0
PUBLIC_NEGATIVE_MISSES = 0
HIDDEN_POSITIVE_FALSE_FAILURES = 0
HIDDEN_NEGATIVE_MISSES = 0
HISTORICAL_P0_P1_FALSE_NEGATIVES = 0
RELEASE_FALSE_PASSES = 0
```

## 8. Exact V13 failure replay

Confirm the validator detects, at minimum:

- widespread tiny-object plus large-empty-body failures;
- P18 unreadable dense page;
- P23 prior table/whitespace regression;
- P25 text/formula half-empty page;
- P28 half-empty peer layout;
- P30 protected method diagram deleted/replaced by prose;
- P33 small top cluster plus half-empty page;
- P34 undersized predictive panels and weak evidence proximity;
- P26 numerical figure inconsistency or BLOCKED numerical status;
- page review rows containing PASS flags/hashes without substantive observation;
- V13 release-state routing before GPT Work PASS.

If these are not surfaced precisely, Critic result is REVISE.

## 9. Positive visual ancestry audit

Verify the mechanism can distinguish:

- preserving a protected object while improving it;
- deleting the object but retaining prose;
- replacing it with unrelated generic boxes;
- retiring it through explicit Planner authority.

Run or inspect hidden tests for P16, P21, P23, P30 and P38-style ancestry cases.

## 10. Numerical figure audit

Verify the numerical framework binds:

- source draws/data;
- variable;
- transformation;
- filtering/warmup stage;
- axis/units;
- nearby summary;
- tolerance.

P26 must not PASS without resolving the plotted quantity/scale. A clean PNG or
matching hash is insufficient.

## 11. Generic versus project-specific ownership

Review `detector_ownership_matrix.json` and `reusability_extraction_report.md`.

Generic reusable checks must be implemented in `AI_Skills_Collection`.
STAT5060 content, PageIDs, feedback and exact numerical contracts must remain in
`STAT5060-TA`.

Fail if:

- course literals enter generic detectors;
- generic whitespace/readability/ancestry logic is duplicated only in the course
  adapter;
- the adapter can change generic thresholds or suppress findings;
- a Tutorial-only rule is promoted as generic without unrelated-deck evidence;
- a genuinely reusable detector is duplicated only inside the Tutorial adapter.

## 12. Evidence quality

A page-level PASS requires a substantive observation row including object scale,
typography, whitespace, reading path, ancestry, and applicable numerical checks.
Flags and hashes alone do not count.

Check exact candidate identity throughout. Stale reports or mismatched hashes are
P0.

## 13. Required output

Write an immutable Critic report with:

- reviewed commits;
- corpus counts and exact artifact list;
- architecture verdict;
- anti-fitting verdict;
- positive/negative control verdict;
- historical replay verdict;
- V13 replay verdict;
- numerical-figure verdict;
- generic/specific ownership verdict;
- evidence completeness verdict;
- P0/P1/P2 findings;
- bounded required repairs.

Return:

```text
CRITIC_RESULT = PASS | REVISE | BLOCKED
GENERIC_CORE_ANTI_FITTING = PASS | FAIL
CORPUS_COMPLETENESS = PASS | FAIL
GOOD_MUST_PASS = PASS | FAIL
BAD_MUST_FAIL_PRECISELY = PASS | FAIL
V01_V13_EXECUTION = PASS | FAIL
V13_FAILURE_REPLAY = PASS | FAIL
POSITIVE_VISUAL_ANCESTRY = PASS | FAIL
NUMERICAL_FIGURE_VALIDATION = PASS | FAIL
GENERIC_SPECIFIC_SEPARATION = PASS | FAIL
CRITIC_ORACLE_COVERAGE = PASS | FAIL
PRODUCER_ORACLE_ACCESS = NO | LEAKED
ORACLE_ISOLATION_REPORT = PASS | FAIL
REUSABILITY_EXTRACTION = PASS | FAIL
EVIDENCE_COMPLETENESS = PASS | FAIL
P0 = <n>
P1 = <n>
P2 = <n>
VALIDATOR_ACCEPTED = YES | NO
V14_PRODUCTION_ALLOWED = NO
NEXT_ACTION = FREEZE_VALIDATOR_ACCEPTANCE | VALIDATOR_REPAIR | RECOVER_MISSING_ARTIFACT
```

The Critic never authorizes V14 production directly. It only accepts or rejects
the validation mechanism.
