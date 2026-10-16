# Project Instructions Editor C5 real user acceptance review

Date: 2026-10-05
Result: `REVISE`

Active review context:

```text
target_repo=YuukiAS/AI_Skills_Collection
target_plugin_or_domain=standalone Skill / project-instructions-editor
design_topic_or_task_key=project-instructions-editor--standalone-skill-implementation
source_branch_or_ref=work/project-instructions-editor--standalone-skill-implementation
review_stage=real Server+VPS Project acceptance after C5 wrapper update
FINAL_CANDIDATE_COMMIT=C5=2d0aab2d995c89326a80eae29e0f0925f2c7e00f
EVIDENCE_HEAD=E5=b45d90a172997f773cdf84d0f90038e2a5cbaa8f
```

## New real evidence

The user invoked the exact C5 private wrapper in a fresh Server+VPS Project thread using the general-purpose Project-instructions review request rather than a Server+VPS-specific translation checklist.

The first response concluded `no-op`.

However, the response itself acknowledged at least two live-setting defects inside the authorized edit scope:

1. ordinary explanatory English still remains in the durable Project setting;
2. the `Clash_Profile` section still keeps a concrete device list even though the Project already has a canonical repository/inventory owner for volatile client coverage.

The response then declined to fix either issue because it judged the semantic-drift risk of editing higher than the benefit.

That is not consistent with the user's request to improve the current Project instructions or with PIE's own placement/reading-layer contract.

## R6 — no-op eligibility bypasses final-candidate consistency

Status: `BLOCKING`

### Requirement

PIE may return no-op only when changing the Project setting would duplicate, weaken, or misplace the rule and there is no material bounded defect in the requested scope that can be fixed safely.

The existing C5 final-candidate consistency mechanism correctly reviews a drafted bounded edit/consolidation/full replacement, but it runs too late: a no-op decision can bypass it entirely.

### Direct evidence

The real C5 response said both:

- ordinary terms still use English;
- a concrete client/device list remains in the Project setting;

while still concluding:

`no-op. 当前 Server+VPS Project instructions 不需要修改。`

The C5 source says:

> After drafting a bounded edit, consolidation, or full replacement, re-read the complete candidate...

Therefore the consistency pass is conditioned on already having drafted a candidate. A premature no-op can escape the check.

The public-safe C5 regression also over-constrained the task relative to the real normal entry: it explicitly instructed the runtime to naturalize ordinary explanation under the Chinese reading-layer contract and explicitly supplied the machine-string preservation distinction. The real user prompt only asked the editor to inspect and improve the Project setting generally and expected PIE to infer the active language/source-placement contract from the live setting itself.

### Causal risk

PIE can become systematically over-conservative:

live setting contains a real, low-risk, bounded defect
-> editor notices the defect
-> editor prefers no-op to avoid semantic drift
-> no candidate is drafted
-> final-candidate consistency never runs
-> the defect survives indefinitely.

This makes `no-op` an escape hatch from the very quality contract C5 was intended to enforce.

### Minimum closure

Do not redesign the product and do not remove no-op.

Add a generic **no-op eligibility check** before committing to no-op:

- treat the current live setting itself as the object to review against the active Project reading-layer, placement/ownership, durability, and budget contract;
- if the editor identifies a real defect inside the user's requested scope that violates an active Project contract or duplicates volatile detail owned by a canonical source, and a bounded edit/consolidation can fix it without weakening protected semantics, no-op is not eligible;
- cosmetic preference alone still does not require editing;
- no-op remains valid when the setting already satisfies the active contract or when the only possible change would duplicate, weaken, misplace, or overfit.

Add an uncoached public-safe regression derived from this exact failure:

- generic request to inspect/improve current Project instructions;
- current setting itself contains the Chinese reading-layer contract;
- current setting contains ordinary descriptive English and one volatile concrete inventory/list already owned by a canonical source;
- prompt does **not** tell the editor which English phrases to translate and does **not** explicitly instruct it to preserve a supplied exact-string list;
- expected decision is bounded edit/consolidation, not no-op;
- quality is judged on the complete replacement and semantic preservation, not keyword counts.

Freeze a new same-final-candidate C6 and rerun affected G1–G4 evidence from exact C6. The prior real C4 and C5 Server+VPS acceptance attempts remain FAIL and must not be rewritten as PASS.

## Decision

```text
CRITIC_RESULT=REVISE
BLOCKER=R6

C5_INTERNAL_G1=PASS
C5_INTERNAL_G2=PASS
C5_INTERNAL_G3=PASS
C5_INTERNAL_G4=PASS

C5_REAL_SERVER_VPS_USER_ACCEPTANCE=FAIL
C5_RELEASE_ACCEPTANCE=FAIL

READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO

NEXT_HANDOFF=CODEX_BOUNDED_C6_REPAIR
```

This new evidence supersedes the earlier C5 implementation-readiness conclusion for release purposes. It does not reopen the frozen architecture, wrapper architecture, FD1 release-cleanliness design, or unrelated repository mechanisms.
