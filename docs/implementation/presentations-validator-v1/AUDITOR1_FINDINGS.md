# Presentations Validator V1 - Auditor 1 Finding Packet

Candidate commit: `528464f1d9d49d08c1ae1c8860a859fa7a692aad`

Verdict:

```text
VALIDATOR_ACCEPTED=NO
P0=0
P1=5
P2=0
```

## AUD1-P1-001

SEVERITY: P1

INVARIANT: Exact/duplicate authority IDs must be detected, including duplicate IDs hidden by dictionary materialization.

OBSERVED: JSON object duplicate keys are loaded through plain `json.loads()`, so earlier duplicate keys disappear before `records_by_id()` can see them.

COUNTEREXAMPLE: Auditor case `duplicate_json_keys_hidden_by_materialization` returned `failure_count=0`; relevant detectors passed.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/io.py`
- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/schemas.py`

REQUIRED_BEHAVIOR: Load JSON with duplicate-key detection or forbid dict-materialized record maps when uniqueness matters.

ROOT_MECHANISM: Parser-level duplicate loss before validator-level ID checks.

REGRESSION_CLASS: Duplicate IDs hidden by dictionary materialization.

## AUD1-P1-002

SEVERITY: P1

INVARIANT: Mandatory source identities must bind exact path, role, blob and commit, and independently prove immutable source state at the candidate commit.

OBSERVED: Source identity validation only compares ID, role and immutable flag. Git blob validation trusts candidate-provided `commit` and `path`, instead of comparing mandatory source path/blob at the bound candidate commit.

COUNTEREXAMPLES:

- `stale_source_identity_uses_baseline_blob_after_candidate_source_change`
- `mandatory_source_path_substitution_same_id_role`

Both returned `failure_count=0`.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`

REQUIRED_BEHAVIOR: Mandatory source `path`, role, immutability and blob must be compared against authority and resolved at the bound candidate/evidence commit unless authority explicitly permits another commit.

ROOT_MECHANISM: Candidate-provided identity tuple is self-consistent but not authority-bound.

REGRESSION_CLASS: Source-role/path substitution; candidate/evidence commit mismatch; two-field evidence consistency attack.

## AUD1-P1-003

SEVERITY: P1

INVARIANT: Required-object deletion/relocation requires explicit authority, not candidate self-assertion.

OBSERVED: `required_object_relocations` passes if the candidate supplies any non-empty `authority_record_id`; the detector does not verify that such authority exists or authorizes the destination.

COUNTEREXAMPLE: `required_object_fake_relocation_authority_id` returned `failure_count=0`.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`

REQUIRED_BEHAVIOR: Relocation records must resolve to an authority record with matching object ID, allowed destination and relocation semantics.

ROOT_MECHANISM: Detector accepts candidate payload as relocation authority.

REGRESSION_CLASS: Required-object relocation/deletion claims.

## AUD1-P1-004

SEVERITY: P1

INVARIANT: Scoped review cannot issue global PASS while page/component/artifact requirements remain unreviewed.

OBSERVED: `review_scope_integrity` only checks `unreviewed_requirements` and mandatory requirement labels; it ignores partial `reviewed_pages`/components/artifact coverage even when `verdict=PASS`.

COUNTEREXAMPLE: `global_pass_partial_reviewed_pages` returned `failure_count=0`; `review_scope_integrity` status passed.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`

REQUIRED_BEHAVIOR: Global PASS must prove all mandatory pages/components/artifacts/requirements are reviewed or explicitly block as unverified.

ROOT_MECHANISM: Review coverage model is requirement-label-only.

REGRESSION_CLASS: Review-scope partial coverage falsely issuing global PASS.

## AUD1-P1-005

SEVERITY: P1

INVARIANT: STAT5060 replay adapter must support read-only replay of frozen START/A/B identities through the same generic validator and valid evidence locators.

OBSERVED: Adapter materialization reports the configured V4 review path is absent at `EVIDENCE_B`, and validating the materialized bundle against the read-only STAT5060 repo fails with `candidate_commit_mismatch` because current HEAD is not `IMPLEMENTATION_A`.

COUNTEREXAMPLE: `materialize_stat5060_bundle()` wrote a bundle, then `validate_bundles()` returned `candidate_commit_mismatch`; `git cat-file -e a255...:docs/reviews/...V4...` exited 128.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/stat5060_adapter.py`
- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`

REQUIRED_BEHAVIOR: Historical replay must validate exact frozen commits without mutating STAT5060, for example via commit-aware Git resolution/worktree-free object lookup or a read-only detached/materialized checkout, and must use real review paths.

ROOT_MECHANISM: Generic Git binding is current-HEAD-bound; adapter is only an ingestion smoke and uses a stale review locator.

REGRESSION_CLASS: STAT5060 replay gate / candidate-evidence identity mismatch.
