# Presentations Validator V2 — Longleaf Codex Implementation Goal

Repository: `YuukiAS/AI_Skills_Collection`
Parent branch: `work/presentations-v19-core-validator-template-promotion-20261114`
Recommended child branch: `implementation/presentations-validator-v2-v19-20261114`

## Objective

Implement Validator V2 as a generic plugin component. This task is implementation only. Do not change the frozen Planner specifications and do not claim final acceptance.

Read first:

1. `docs/frozen/PRESENTATIONS_VALIDATOR_V2_FROZEN_SPEC_2026-11-14.md`
2. `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_FROZEN_SPEC_2026-11-14.md`
3. `docs/frozen/PRESENTATIONS_SHARED_BEAMER_CORE_V1_LAYOUT_CONTRACT_2026-11-14.yaml`
4. old V1 frozen spec and all three Auditor finding packets
5. current `plugins/codex/plugins/presentations/shared/validator_v1/` if present
6. current independent-review and anti-self-certification contracts

## Implementation boundary

Create a new package under:

`plugins/codex/plugins/presentations/shared/validator_v2/`

Do not modify V1 production code to make tests pass. V1 remains historical evidence.

V2 must have separate modules for:

- authority/integrity;
- layout/rendered geometry;
- review-state routing;
- adapters/fixtures.

Production modules may not import STAT5060 project-local code.

## Required CLI

Provide a generic CLI capable of:

- validating authority + candidate bundles;
- validating a layout contract against a rendered PDF/source/object map;
- emitting structured PASS / FAIL / REVIEW / NOT_VERIFIED rows;
- producing an artifact-level deterministic state.

The exact command surface may be compact, but must be documented and stable.

## Mandatory V1 root repairs

Implement regression tests and production fixes for every P1 class in:

- Auditor 1;
- Auditor 2;
- Auditor 3.

At minimum:

- duplicate JSON key detection before materialization;
- exact mandatory source path/role/commit/blob binding;
- fake relocation authority rejection;
- full feedback derivative fidelity;
- full component fidelity;
- artifact hash namespace correctness;
- global PASS requiring complete review coverage;
- required lock evidence;
- baseline/candidate/tree fields mandatory;
- exact historical replay locator handling with no heuristic substitution.

## Layout detectors

Implement the generic detectors required by the V2 spec and frozen layout contract:

- TYPE
- RAIL
- SPACE
- COLUMN
- CAPTION
- QA
- FOOTER
- SECTION_NAV
- TABLE
- DIAGRAM
- CLOSING
- DENSITY/WHITESPACE
- PROTECTION

No production branch may depend on a known STAT5060 page number, version name, human complaint phrase, fixture name, mutation ID or expected verdict.

## Public tests

Build public tests for:

- authority-integrity root mechanisms;
- font/spacing boundaries;
- body rail;
- caption left alignment;
- Q/A;
- footer;
- section-label budget;
- table wrap;
- arrow thresholds;
- closing geometry;
- whitespace/crowding REVIEW vs FAIL semantics;
- protection masks.

Include property/mutation tests where appropriate.

## Public real-use fixtures

The implementation branch may receive/use public controls, but it must not see the GPT Work held-out pack.

Public controls should include:

- one exact or deidentified STAT5060 positive slice;
- several deidentified historical negative classes;
- one unrelated teaching fixture;
- one unrelated research fixture;
- synthetic boundary fixtures.

## STAT5060 adapter

Provide a generic adapter that can bind exact frozen Git objects/paths from an external repo and run replay without importing course code.

If an exact historical locator is absent, emit NOT_VERIFIED/FAIL according to policy. Never substitute a nearby review file.

## Evidence

Produce:

- implementation report;
- public test report;
- coverage/introspection report;
- mutation report;
- changed-file manifest;
- exact candidate commit.

Do not create or modify the hidden acceptance pack.

## Completion

Allowed final state only:

```text
VALIDATOR_V2_CANDIDATE_READY = YES
READY_FOR_INDEPENDENT_ACCEPTANCE = YES
CANDIDATE_COMMIT = <sha>
```

Do not claim `VALIDATOR_V2_ACCEPTED`.
