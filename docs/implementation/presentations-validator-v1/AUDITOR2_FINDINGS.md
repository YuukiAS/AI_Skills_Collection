# Presentations Validator V1 - Auditor 2 Finding Packet

Candidate commit: `518b28946ac290ab24e6429de85d04eeec3d7daa`

Verdict:

```text
VALIDATOR_ACCEPTED=NO
P0=0
P1=4
P2=0
```

This is the second independent Auditor rejection. The STAT5060 replay locator
class overlaps the Auditor 1 replay/identity class, so the next Producer must
repair the root replay/evidence-locator mechanism rather than patching the
named example.

## AUD2-P1-001

SEVERITY: P1

INVARIANT: Candidate derivative feedback rows must preserve all authority-bound
record fields, not only ID/target.

OBSERVED: `feedback_authority_coverage` checks only ID set and `authority_id`;
`row_target_ancestry` uses authority row fields for allowed targets but does not
compare candidate feedback provenance fields.

COUNTEREXAMPLE: In the public valid bundle, Auditor changed candidate
`derived_feedback_registry.jsonl` row `fb-1` to `artifact_id="deck-b"`,
`historical_page=99`, and added executor provenance text while keeping ID and
target valid. Validator returned `failure_count=0`.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`
- `docs/frozen/PRESENTATIONS_VALIDATOR_V1_FROZEN_SPEC_2026-10-06.md`

REQUIRED_BEHAVIOR: Feedback/direct-decision/source-gap candidate rows must be
compared against immutable authority for every authority-bound field, with only
explicit allowed derived/candidate-only fields ignored.

ROOT_MECHANISM: ID/target-specific detector coverage substitutes for complete
derivative fidelity.

REGRESSION_CLASS: Complete derivative field drift / authority meaning drift.

## AUD2-P1-002

SEVERITY: P1

INVARIANT: Component records must preserve all authority fields, while also
verifying consumer inverse.

OBSERVED: `component_consumer_inverse` checks ID set and consumers/inverse only.
Non-consumer component fields such as `type` or style contract can drift without
findings.

COUNTEREXAMPLE: In the public valid bundle, Auditor changed component `header`
from `type="shared"` to `type="local_rebuilt_header"` and added
`style_contract="changed"` while keeping consumers unchanged. Validator returned
`failure_count=0`.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`
- `docs/frozen/PRESENTATIONS_VALIDATOR_V1_FROZEN_SPEC_2026-10-06.md`

REQUIRED_BEHAVIOR: Component candidate records must be full-record compared to
authority, with consumer inverse as an additional check.

ROOT_MECHANISM: Component detector narrowed fidelity to consumers only.

REGRESSION_CLASS: Component derivative field drift / shared-component authority
drift.

## AUD2-P1-003

SEVERITY: P1

INVARIANT: Review scope/global PASS must bind exact artifact identity/hashes,
not accept artifact ID aliases as artifact hashes.

OBSERVED: `review_scope_integrity` treats `artifact_hashes` as interchangeable
with `reviewed_artifacts` and compares those strings to artifact lineage IDs.

COUNTEREXAMPLE: Auditor set review scope to global `PASS` with all
pages/components/requirements reviewed, but used `artifact_hashes=["deck-a"]`
where `deck-a` is the artifact ID, not a hash. Validator returned
`failure_count=0`.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/detectors.py`
- `plugins/codex/plugins/presentations/shared/independent-review-contract.md`

REQUIRED_BEHAVIOR: Artifact review coverage must validate artifact hash
format/value against authority or rendered artifact identity, and must not let
IDs satisfy hash-bound review evidence.

ROOT_MECHANISM: Artifact identity namespace confusion between IDs and hashes.

REGRESSION_CLASS: Review-scope false global PASS / artifact identity aliasing.

## AUD2-P1-004

SEVERITY: P1

INVARIANT: STAT5060 replay must use the exact frozen V4 review locator or fail
truthfully; it must not silently substitute a stale review path.

OBSERVED: The adapter hardcodes the V4 path, but if absent it searches all
planner reviews and chooses the sorted last replacement. On the audited
repo/commit it substituted the V3 review and still produced a passing ingestion
validation.

COUNTEREXAMPLE: `git cat-file -e
a255e716...:docs/reviews/...V4...md` exited 128; adapter summary reported
`configured_path_absent_discovered_replacement`,
`review_path=...V3_PLANNER_REVIEW_V1.md`, `failure_count=0`.

EVIDENCE:

- `plugins/codex/plugins/presentations/shared/validator_v1/presentations_validator_v1/stat5060_adapter.py`
- `docs/execution/PRESENTATIONS_VALIDATOR_V1_CODEX_IMPLEMENTATION_GOAL_2026-10-06.md`

REQUIRED_BEHAVIOR: Missing exact frozen replay evidence must be a replay failure
or explicit `NOT_INDEPENDENTLY_VERIFIED`, not automatic substitution to another
review generation.

ROOT_MECHANISM: Exact authority locator relaxed into heuristic path discovery.

REGRESSION_CLASS: Stale/source path substitution / STAT5060 replay evidence
substitution.
