# Protected cancellation — formal release closure

Task: `hpc--slurm-cancel-production-closure`.
Date: 2026-10-21.

## Exact identities

- Frozen behavioral implementation: `3e81802ab0251d3bf31ec2d808d4e3273505b2f6`.
- Merged latest main base: `c7f98f201c746d357344091f89cce7a3541154d9`.
- Normal merge: `6a1ece94609809bfe8289a04fa2f5d224e0d6fa9`.
- Final tested, independently reviewed, published release:
  `f4517798a73adf29d3484306d60845488739f1fc`.
- Both remote main and formal release were read back at that exact release
  commit after normal fast-forward publication. Subsequent task closure
  documentation does not change that exact formal product release identity.

Repository bump decision: PATCH
Reason: compatible safety improvement within the existing standalone Slurm
workflow and collection contract.
Affected standalone skills:
- slurm-workflows: 0.4 -> 0.5, exactly once.
Affected plugins:
- all central Marketplace plugins: NO_BUMP.
Bridge Kit, DII, CARE, other task-owned source and central-plugin versions:
NO CHANGE relative to the merged main base.

Latest-main changes were preserved through a conflict-free normal merge.
Only Slurm SKILL version metadata changes from the frozen behavioral candidate;
all runtime, rules and declaration/installation generation bytes are identical.

## Revised G4, without rewriting history

The actual harmless native form returned
`{"action":"accept","content":{"decision":"retain"}}`.
Its empty UI-only pending record closed with no scheduler access, Slurm
mutation or cancellation reservation. Deterministic retain integration checks
zero invocation and reservation. Historical Jobs 5693449 and 6028303 each have
one actual confirm invocation and independent terminal-cancellation evidence,
zero runtime/allocation and no other-Job mutation.

The current user explicitly waived live held-Job retain. Historical
`KEEP_TEST=NOT_RUN` remains unchanged. No third Job was created, neither
historical Job was queried or operated on in this closure, and no real
cancellation was executed. See `REVISED_G4_ACCEPTANCE.md` and the independent
review; harmless UI evidence is not presented as live Job retain.

## Final validation and independent review

Final CI: [39639471530](https://github.com/YuukiAS/AI_Skills_Collection/actions/runs/39639471530),
exact head `f4517798a73adf29d3484306d60845488739f1fc`, all four jobs success:

- complete repository regression: 406 tests, OK;
- Marketplace generation, validation, freshness, Windows path/sparse checks;
- skill validation and audit: 156 active skills, 18 profiles;
- editable CLI install/smoke on Ubuntu and Windows;
- generated files committed and clean.

Same-runtime focused 54, full Slurm 69 and historical full repository 401 PASS
remain preserved. They are not mislabeled as the new merged-candidate run.
First release CI 39639003443 failed one stale repository-version expectation;
that single metadata expectation was corrected and the final exact candidate
passed. No frozen runtime or plugin behavior was changed for that correction.

An independent implementation reviewer checked the frozen source, actual
private audit receipts, exact release candidate deltas and final formal
source/install/CI identities. Its original report and staged follow-up
conclusions are preserved in `INDEPENDENT_FINAL_REVIEW.md` / `REVIEW_1.md`.

README SHA256
`ee6190e52390a40e35abfd09f64ef0616f8e4e28f031448eadb56005c8925483`
passed actual installed Clear Writing replay. Initial and conditional completed
maintenance Issue copy were also actually reviewed before publication.

## Formal publication and installation

The existing `release` branch is the formal channel. Existing selected main
and release worktrees were clean and fast-forwarded; bounded
`ai-bridge host publish-current-branch` published both refs without force.
No new GitHub Release mechanism, branch, wrapper or confirmation architecture
was introduced.

The existing product renderer and atomic installer ran from the exact formal
release checkout. All seven installed manifest files equal both the formal
release rendering and the original frozen-candidate installation receipt.
The configuration is byte-identical before/after; all other Hook/MCP settings
and all native trust entries are unchanged. All existing durable state records
were preserved, including the same two cancellation reservations and two
invocation intents. No new cancellation reservation or invocation was created.

The formal CLI reports 5.5.2. Its precise standalone-skill copy install reports
the formal commit; installed SKILL version 0.5 and three scripts match source.
This isolated copy-install smoke does not claim a new global Skill install.

Normal `config/batchWrite`, empty edits, `reloadUserConfig=true` succeeded.
Backend `hooks/list` then showed exactly the task's three handlers enabled,
trusted, with unchanged hashes and no load errors:

| Handler | Current/trusted hash |
| --- | --- |
| PreToolUse command | sha256:b72dc9a527334c043cb867d7feb8c282784e603b3a4a387124f74af1aeb3d0ee |
| PreToolUse MCP | sha256:0a564649173eeca987e856fa5b844999bf9ee86753d8df9d93d6b754d65436f2 |
| PermissionRequest command | sha256:067c6b65d84ea46759609935704fea931b4f81efeef70764ec777b29b3b335a3 |

Actual normal-entry `git status --short` exited 0 with empty output after
installation. Actual normal-entry `scancel --help` was blocked by PreToolUse
with `SLURM_CANCEL_DENIED reason=unsupported_scancel_target_or_option` before
process launch. It made no scheduler query or Job mutation. No extra form was
requested after the successful harmless retain mapping.

Durable private evidence in the canonical checkout:

- `private/exports/hpc--slurm-cancel-production-closure/formal-install-20261021/`;
- `final-release-ci-39639471530.json` and `.log` in that task's private root;
- `release-clear-writing-20261021/`;
- the unchanged original/replacement/retain UI audit bundles.

Formal install receipt SHA256:
`10bbdbe741338c0572212b6d57bcba62152550f8c3c678732555e03a18305e45`.

A repository-wide Reviewed Handoff metadata validation also reported historical
errors in unrelated tasks (legacy task names and old missing metadata). It
reported no error for this task; its existing transition/review records
validated. Those unrelated workflows were left unchanged and are not a release
CI failure.

The only required current consumer is Longleaf Codex USERS identity,
`CODEX_HOME=/users/a/e/aereinh/.codex`; it passed. No additional machines,
Bridge, DII or CARE adaptation is claimed or required. Tracking Issue: #109.

```text
LIVE_JOB_RETAIN_TEST=WAIVED_BY_CURRENT_USER
KEEP_TEST=NOT_RUN
LIVE_RETAIN_UI_MAPPING=PASS
DETERMINISTIC_RETAIN_PATH=PASS
LIVE_CONFIRM_PATH=PASS
ORIGINAL_CONFIRM_JOB_ID=5693449
REPLACEMENT_CONFIRM_JOB_ID=6028303
OTHER_JOB_MUTATION=NO
G4_REVISED_ACCEPTANCE=PASS
INDEPENDENT_REVIEW=PASS
G5=PASS
FINAL_RELEASE_CI=PASS
REPOSITORY_VERSION=5.5.2
SLURM_WORKFLOWS_VERSION=0.5
PUBLISHED=YES
FORMAL_INSTALL_VERIFIED=YES
COMPLETE=YES
```
