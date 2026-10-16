# Project Instructions Editor — C10 Implementation Critic Review

Date: 2026-10-06
Result: `REVISE`

## Review identity

```text
FINAL_CANDIDATE_COMMIT=C10=b93913e2d27cca2f1d5be1cd8626bc0aa38b6ea9
FRESH_G4_FREEZE_COMMIT=F10=d255abe094da1be5d63f4c09929375f4ec90d8bb
EVIDENCE_PAYLOAD_COMMIT=E10=2818f8245bc9e63affe13ca3fd69498daa251f41
EVIDENCE_SEAL_COMMIT=S10=d2f382d6b7ac1aba3a1e3a39408a229405b3de86
```

Reviewed directly:

- latest main governance;
- exact C10 PIE source/reference;
- F10 freeze packet and frozen qualitative rubric;
- G1/G2/G3 evidence;
- G4 complete-task packet;
- raw replay final outputs and event logs for the C9 known replay, C9 F9 development replay, C10 fresh case, helper-consumption case, no-op case and helper-fidelity case;
- C10 -> F10 / E10 / S10 diffs;
- current formal release identity and pinned chinese-prose runtime snapshot.

## Evidence-chain integrity

The campaign mechanics are correct.

```text
C10..F10 = results-only
C10..E10 = results-only
C10..S10 = results-only
C10_CANDIDATE_IMMUTABLE=YES
C10_WRAPPER_SUPPORT_SNAPSHOT=PASS
```

The current formal release is still:

```text
06d135d8a6ee62cd41abb40fc5771fcef7f8db25
VERSION=5.4.4
writing-style=0.4
```

The vendored chinese-prose runtime tree remains the exact pinned formal runtime tree.

Raw event evidence also shows that the C10 mixed routes actually read both:

- `project-instructions-editor/SKILL.md`;
- vendored `chinese-prose/SKILL.md`.

Thus the failure below is not an evidence-identity or “helper merely packaged but not consumed” problem.

## G1-G3

G1, G2 and G3 are acceptable as C10 diagnostic evidence.

Observed:

- PIE remains the primary Project-semantic owner;
- the vendored chinese-prose helper is actually consumed on mixed Chinese complete-replacement routes;
- routing near-misses remain separated;
- R5 protected absence remains closed;
- R6 no-op eligibility remains closed;
- helper snapshot identity and post-helper fidelity are preserved in the reviewed cases.

These do not override the failed final G4 holdout.

## G4 known/development regressions

### C9 Server/VPS known replay

PASS for the historical R7 failure class.

The old `tunnel` leakage is naturalized to Chinese in the durable replacement, while exact machine/product/repository strings are preserved.

### C9 F9 development replay

PASS as development regression.

Protected absence remains closed, volatile lists are replaced by current-source bridges, and ordinary descriptive English is substantially naturalized.

Neither case is fresh evidence.

## C10-B3 — final fresh holdout still violates the frozen R7 rubric

Status: `BLOCKING`

### Requirement

The F10 qualitative rubric explicitly requires ordinary descriptive/meta English to be naturalized in the final durable setting.

Its explicit FAIL examples include retaining:

```text
Project setting
```

as ordinary English merely because it is technical, common, present in source, or convenient.

The same rubric requires the self-check to match the actual final replacement.

### Direct evidence

The first and only C10 F10 fresh output contains this durable sentence:

```text
路线、工具包、联系人、发布细节和季节性例外会变，以当前文件为准，不在 Project setting 里固化清单。
```

But the same output then claims:

```text
普通英文已中文化
```

and justifies remaining Latin material by listing `Project` among exact/formal tokens.

This does not satisfy the frozen rubric. `Project setting` was named in advance as a FAIL example for this exact class, and the generic label `setting` has a natural Chinese realization.

The same failure family previously appeared in C8.

### Causal risk

C10 was specifically intended to stop repeated R7 self-check leakage by consuming the mature chinese-prose helper.

The fresh holdout shows:

```text
PIE consumed
+ chinese-prose consumed
+ final output still leaks ordinary "Project setting"
+ self-check still claims ordinary English was naturalized
```

Therefore the current composition does not yet establish stable R7 behavior outside the tuned known/development cases.

Passing G4 would convert a frozen explicit FAIL condition into PASS after observing the output, which would violate the Gate contract.

### Minimum closure

Do not modify C10.

Do not rerun or replace F10.

C10 final campaign is failed.

The exact F10 case has now been observed and permanently becomes development regression evidence for any successor.

Per the already-approved C10 stop rule, do not open a successor as another synonymous PIE prompt-strengthening round.

Return to Planner/Critic for implementation-class attribution among the already-defined possibilities:

1. `chinese-prose` itself does not reliably naturalize this class when used as a sibling support Skill;
2. the current same-model sibling-Skill consumption mechanism does not create a sufficiently distinct realization pass even though both Skills are read;
3. a different bounded implementation class is required.

Any successor mechanism must be materially different from adding another example, blacklist, translation table, English-ratio rule, or stronger self-check wording.

## Freshness consequence

```text
F10_FRESH_STATUS=CONSUMED_AND_FAILED
F10_SUCCESSOR_ROLE=DEVELOPMENT_REGRESSION_ONLY
```

A successor candidate must use a different final fresh case if and when a new implementation mechanism is independently approved.

## Final decision

```text
CRITIC_RESULT=REVISE

C10-B3=FRESH_G4_R7_PROJECT_SETTING_LEAKAGE

R5=CLOSED
R6=CLOSED
R7=OPEN

G1=PASS_FOR_C10_DIAGNOSTIC
G2=PASS_FOR_C10_DIAGNOSTIC
G3=PASS_FOR_C10_DIAGNOSTIC
G4=FAIL

CHINESE_PROSE_HELPER_ACTUALLY_CONSUMED=YES
C10_WRAPPER_SUPPORT_SNAPSHOT=PASS
C10_CANDIDATE_IMMUTABLE=YES

F10_FRESH_STATUS=CONSUMED_AND_FAILED
F10_SUCCESSOR_ROLE=DEVELOPMENT_REGRESSION_ONLY

IMPLEMENTATION_OVERALL=REVISE

C10_SERVER_VPS_RETEST=DO_NOT_RUN
PLUGIN_CREATOR_MUTATION_AUTHORIZED=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO

NEXT_HANDOFF=PLANNER
```

This review does not reopen PIE product responsibilities, R5/R6, edit modes, routing, four-Gate taxonomy, wrapper ownership topology, Bridge Kit, Host Policy, final-delivery design or FD1. It reopens only the implementation mechanism needed to make R7 stable after actual helper consumption.
