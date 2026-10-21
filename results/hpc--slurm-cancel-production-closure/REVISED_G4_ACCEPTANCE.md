# Current-user revised G4 acceptance — 2026-10-21

Frozen runtime candidate: `3e81802ab0251d3bf31ec2d808d4e3273505b2f6`.

The current user expressly replaces the live held-Job retain gate with real native retain UI mapping plus the same candidate's deterministic retain integration coverage. No further Job creation, scheduler access, Job operations or real cancellation is authorized. Historical `KEEP_TEST=NOT_RUN` remains unchanged; it is not relabeled PASS.

## Actual harmless native retain response

The first harmless form timed out without a response; it did not prove either mapping outcome. On the user's renewed request, exactly one fresh harmless form was issued through the unchanged installed product's `ui_probe` mode. The required schema was the same two-choice schema used by the real confirmation paths, with `确认取消 -> confirm` and `保留 Job -> retain`.

Audit identity: `33480a9f07065eaf4426bbb1be969aea7ff5dcdcf7f382340195dfbfbef65bbd`.
Root metadata thread and session: `01a1572b-d446-7fa3-94cf-95f978b0efde`.

Actual immutable answer:

```json
{"action":"accept","content":{"decision":"retain"}}
```

The pending record was `operation=ui_probe`, `job_ids=[]`, and closed after the response. It was not a cancellation reservation. No scheduler was accessed or queried, no Job was created, and no cancellation executable was invoked. SHA256 snapshots of all existing cancellation reservations and invocation-intent records were identical before and after the probe (the same four files). Thus the probe added no Slurm mutation or cancellation reservation. Frozen product source, installed runtime and native trust were not changed.

The durable private request/answer/pending snapshot and receipt are in the canonical checkout at `private/exports/hpc--slurm-cancel-production-closure/retain-ui-mapping-pass-20261021/`.

## Evidence combined under the revised user contract

- Deterministic retain integration: same frozen candidate, focused 54-test bank and full 69-test Slurm bank PASS; explicit retain test verifies zero reservation and zero invocation.
- Original live confirm: Job 5693449, one invocation, terminal cancellation, zero runtime/allocation, no other Job mutation; see `LIVE_CONFIRMATION_EVIDENCE.md`.
- Replacement live confirm: Job 6028303, one invocation, terminal cancellation, zero runtime/allocation, no other Job mutation; see `REPLACEMENT_G4_EVIDENCE.md`.
- Same-candidate full repository: 401 PASS. Candidate CI run 39434396011 PASS. These checks are retained, not repeated as a prerequisite for the harmless probe.

```text
KEEP_TEST=NOT_RUN
LIVE_JOB_RETAIN_TEST=WAIVED_BY_CURRENT_USER
LIVE_RETAIN_UI_MAPPING=PASS
DETERMINISTIC_RETAIN_PATH=PASS
LIVE_CONFIRM_PATH=PASS
ORIGINAL_CONFIRM_JOB_ID=5693449
REPLACEMENT_CONFIRM_JOB_ID=6028303
SLURM_MUTATION_COUNT=0
CANCELLATION_RESERVATION_CREATED=NO
OTHER_JOB_MUTATION=NO
G4_REVISED_ACCEPTANCE=PASS
```

G5, independent final review, final release CI, release publication and formal install verification remain separate gates. No previous release or final-review PASS is claimed here. The next action is independent review and the authorized release closure, preserving runtime bytes and current main's unrelated changes.
