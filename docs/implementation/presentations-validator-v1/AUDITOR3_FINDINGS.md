# Presentations Validator V1 - Auditor 3 Finding Packet

Candidate commit: `8fd001330a224bb021a14e1a367426b4c3287950`

Verdict:

```text
VALIDATOR_ACCEPTED=NO
NEEDS_GPT_PLANNER=YES
P0=0
P1=3
P2=0
```

## Planner Authority Conflict

The Controller Goal requires `STAT5060_READ_ONLY_REPLAY=PASS`, but the frozen V4
locator is absent at the specified evidence commit:

```text
a255e716cf7a846208a62edc82132c3752a16417:docs/reviews/2026-27/STAT5060_TUTORIAL_01_RECOVERY_GOVERNANCE_V4_PLANNER_REVIEW_V1.md
```

Auditor evidence:

- `git cat-file -e <commit>:<V4 review path>` exited `128`;
- `git ls-tree <commit>:docs/reviews/2026-27` showed only V1/V2/V3 governance review files;
- adapter output reported `review_locator_status=configured_exact_path_absent`;
- adapter output reported `stat5060_replay_status=NOT_INDEPENDENTLY_VERIFIED`;
- validation output reported deterministic `FAIL` with `missing_source_manifest`.

This is not an ordinary implementation PASS. Without a Planner-authorized exact
replacement locator or revised replay authority, final controller acceptance
cannot claim `STAT5060_READ_ONLY_REPLAY=PASS`.

## AUD3-P1-001

SEVERITY: P1

INVARIANT: Mandatory source identities must bind exact path, role, commit, and
blob identity.

OBSERVED: If authority requires `git_blob_sha` but candidate omits it,
validation returns `failure_count=0`.

COUNTEREXAMPLE: Public bundle with authority
`mandatory_source_identities[0].git_blob_sha=<actual blob>` and candidate
`source_identity_manifest[0]` with `git_blob_sha` removed.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`

REQUIRED_BEHAVIOR: Missing mandatory blob identity must fail, then independently
resolve `<commit>:<path>`.

ROOT_MECHANISM: Candidate blob field is optional in the detector.

REGRESSION_CLASS: Source identity binding / candidate evidence omission.

## AUD3-P1-002

SEVERITY: P1

INVARIANT: Human-locked objects must have unchanged-lock proof independently
verified.

OBSERVED: Removing all `lock_evidence` from the patch manifest returns
`failure_count=0`.

COUNTEREXAMPLE: Public bundle with `patch_manifest.lock_evidence=[]`.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`

REQUIRED_BEHAVIOR: Missing required lock evidence must fail.

ROOT_MECHANISM: Absence of proof is accepted as no drift.

REGRESSION_CLASS: Lock/scope enforcement false PASS.

## AUD3-P1-003

SEVERITY: P1

INVARIANT: Candidate/evidence must bind baseline commit, candidate commit, and
candidate tree.

OBSERVED: Removing `baseline_commit`, `candidate_commit`, and `candidate_tree`
from `candidate_manifest.json` returns `failure_count=0`.

COUNTEREXAMPLE: Public bundle with those three manifest fields deleted.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`

REQUIRED_BEHAVIOR: Missing required Git identity fields must fail before
comparison.

ROOT_MECHANISM: Required Git binding fields are treated as optional.

REGRESSION_CLASS: Candidate/evidence mismatch / Git identity binding.
