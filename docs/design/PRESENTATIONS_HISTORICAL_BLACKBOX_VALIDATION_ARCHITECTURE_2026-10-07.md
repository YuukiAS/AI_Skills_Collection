# Presentations — Historical Black-Box Validation Architecture

Date: 2026-10-07  
Status: **P0 DESIGN / IMPLEMENTATION ON VALIDATION BRANCH**

## 1. Problem

A presentation workflow can preserve source, page count, copy, hashes and
review manifests while still returning a visibly poor artifact. It can also
self-certify if the same executor writes the detector, fixtures, expected results
and PASS report.

A mature Presentation plugin therefore needs a historical black-box validator,
not only per-candidate checks.

## 2. Required architecture

```text
Generic validator core
+ project adapter
+ historical corpus
+ scoped positive controls
+ hidden holdout/mutations
+ fresh read-only Auditor
+ fresh mechanism Critic
```

The generic core cannot branch on project/version/PageID/feedback identities.
The adapter maps generic findings to project authority but cannot suppress them.

## 3. Generic reusable capabilities

Promote to the Presentation plugin:

- exact artifact/render identity;
- page inventory and review-evidence completeness;
- typography floor;
- primary-object scale;
- whitespace/scale interaction;
- reading-path and peer/sequential layout checks;
- Question/Answer geometry;
- shared-component consistency;
- table/code/figure readability;
- code-output and evidence-interpretation proximity;
- positive visual ancestry preservation;
- no-deletion-as-repair;
- contact-sheet rhythm;
- numerical figure/source/summary consistency framework;
- exact-render closure of historical visual guards;
- release-state routing;
- lock/allowlist/diff checks;
- hidden holdout and randomized mutation runner;
- finding/evidence schemas;
- generic/project-specific ownership matrix.

## 4. Project-specific responsibilities

Projects retain:

- artifact/version inventory;
- stable PageIDs and page jobs;
- feedback and direct decisions;
- content and layout authority;
- positive visual ancestors;
- exact numbers/variables/units/source anchors;
- course/product policy boundaries;
- historical expected issue labels.

Course content and exact feedback must not enter the generic plugin.

## 5. Black-box requirement

The generic Producer works in an isolated workspace without project fixtures or
hidden answers. The project adapter is implemented separately and cannot edit
generic detectors.

After candidates freeze, the Parent Controller generates a hidden pack with:

- held-out historical pages;
- scoped positives;
- randomized visual/numerical/evidence mutations;
- coordinated multi-field mutations;
- an unrelated deck.

A fresh read-only Auditor runs the pack. A fresh Critic reviews architecture,
false-pass/false-fail risk and evidence quality.

## 6. Promotion gate

The validator is not promotable until a real historical deck corpus demonstrates:

```text
all_artifacts_executed = YES
project_specific_branches_in_generic_core = 0
fixture_name_branches = 0
hidden_oracle_imports = 0
positive_false_failures = 0
negative_misses = 0
historical_P0_P1_false_negatives = 0
release_false_passes = 0
finding_precision = PASS
unrelated_deck_generalisation = PASS
fresh_Auditor = PASS
mechanism_Critic = PASS
```

## 7. Current implementation route

Implementation and acceptance work occurs on:

`YuukiAS/AI_Skills_Collection@work/presentation-historical-blackbox-validator-v1`

The STAT5060 Tutorial 01 V1–V13 lineage is the first real corpus. It is a fixture
and proving ground, not generic plugin content.
