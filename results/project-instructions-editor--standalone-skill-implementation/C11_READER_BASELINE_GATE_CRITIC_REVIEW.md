# C11 Reader-Baseline Gate Critic Review

Date: 2026-10-06

Review stage: independent exact-final-candidate complete-artifact review

## Identity

```text
FINAL_CANDIDATE_COMMIT=187212887bc8f7a339cd43097384df35c1e71baf
EVIDENCE_COMMIT=9824d0501dea233442d3f0aca85e319f757bbe27
CANDIDATE_OWNED_SOURCE_CHANGED_AFTER_FINAL_CANDIDATE=NO
C11_IS_LAST_IMPLEMENTATION_CYCLE=YES
DO_NOT_CREATE_C12=YES
```

Direct comparison confirms that all changes after the candidate are under
`results/project-instructions-editor--standalone-skill-implementation/**`.

## Decision

```text
CRITIC_RESULT=REVISE
IMPLEMENTATION_OVERALL=STOP
READY_FOR_PLUGIN_UPDATE=NO
READY_FOR_WEB_USER_ACCEPTANCE=NO
READY_FOR_INTEGRATION=NO
READY_FOR_RELEASE=NO
NEXT_HANDOFF=FINAL_STOP
```

The source implementation is structurally aligned with the approved
`SIMPLE_FORMAL_CORE` plan, but the exact-candidate complete artifacts reproduce
the core reader-facing failure that this final refinement was meant to close.

## Blocking finding

### C11-RB-GATE1 — exact-candidate complete artifacts violate the new reader-facing baseline

Requirement:

- For a default-Chinese Project, ordinary technical/workflow prose must be
  naturalized when Chinese can express it accurately.
- Source English is not itself a preservation reason.
- The final setting must itself comply with the baseline.
- Rewriting must preserve semantic invariants and must not invent unsupported
  durable rules.
- A self-check may not claim compliance when the actual replacement contradicts
  it.

Direct evidence:

1. G2 Case A is a Chinese complete replacement but keeps ordinary English
   `private data`. It also introduces two durable rules not supported by the
   supplied live setting/current request: a licensing/source-confirmation rule
   and a new no-stale-completion rule.
2. G3's complete replacement keeps ordinary source-derived English such as
   `private datasets`, `secret value`, `readiness`, `stale evidence`, and
   `publish`. Its self-check nevertheless says ordinary descriptive English was
   naturalized.
3. G4's complete replacement keeps a much larger set of ordinary descriptive
   English copied from source/history, including `notebooks`,
   `package API authority`, `breaking change`, `public API`, `policy`,
   `public`, `explicitly redistributable examples`, `private`,
   `institution-only`, `unclear-license datasets`, `overview/setup`,
   `build/test/workflow`, `release history`, `stale summary`,
   `implementation`, `readiness`, `current evidence`, and
   `publish/tag/release`. Most are not machine identifiers, fields, commands,
   paths, product names, or strings whose exact spelling is needed for
   copy/execution/search/unique lookup.

Causal risk:

The final source contains the intended rule, but the normal generation path can
still copy ordinary English from source/history into the durable Project
setting and then self-report compliance. That is the same user-visible failure
family previously observed in C8/C9 and means the new Project-resident baseline
is not reliably consumed by the `SIMPLE_FORMAL_CORE` output path.

Minimum closure:

The frozen stop rule does not permit another same-mechanism repair, helper,
service, fresh-case substitution, or C12. Therefore this blocker is not assigned
to another implementation round. The truthful closure is to stop this release
candidate and record that the advanced cross-Project reader-baseline guarantee
is unsupported reliably enough for formal release on the current simple-core
route.

## Gate adjudication

```text
G1=DEVELOPMENT_EVIDENCE_ONLY
G2=FAIL
G3=FAIL
G4_COMPLETE_ARTIFACT=FAIL
G4_REAL_SERVER_VPS_ACCEPTANCE=NOT_RUN
```

G1 is not promoted to final PASS here because the approved matrix ultimately
requires the exact private Plugin identity and normal Web activation/readback;
that stage was intentionally downstream of this independent artifact review.
This is not the blocking reason, because G2/G3/G4 already fail on the exact
candidate artifacts.

C5-C10 remain known/development regressions only and are not relabeled fresh.

## Stop contract

```text
READER_BASELINE_SIMPLE_CORE_UNSUPPORTED=YES
IMPLEMENTATION_STOPPED=YES
DO_NOT_CREATE_C12=YES
PLUGIN_CREATOR_UPDATE=DO_NOT_RUN
SERVER_VPS_FINAL_ACCEPTANCE=DO_NOT_RUN
ISSUE_93_STATUS=DOING
```

Issue #93 should remain open/DOING. No README/CHANGELOG/VERSION/main/release
closure is authorized by this review.
