# Research Authoring C2 Promotion Freeze

Task: `research-authoring--formal-production-authoring`  
Branch: `work/research-authoring--formal-production-authoring`  
Date: 2026-10-06

## Admission authority

Critic admission:

`docs/design/059_RESEARCH_AUTHORING_C2_PROMOTION_ADMISSION_CRITIC_REVIEW_V0_1_2026-10-06.md`

Critic commit:

`a0bf3b3e6ccdc827a39923920c13baa452d4bd26`

The admission review established:

```text
DEVELOPMENT_BLOCKER_CLOSED=YES
C2_PROMOTION_ADMISSIBLE=YES
REPAIRED_PRODUCT_COMMIT=ac501d988f00cb6672fec105ae5fd51a0679cae0
REPLAY_INFRASTRUCTURE_COMMIT=eafb5e11ec65e54259b99fea44fe169096b9dcb9
EVIDENCE_PACKET_HEAD=7d780ca50b67785877a87af0ada967f8389254c2
059_DEVELOPMENT_REPLAY=PASS
FINAL_GATES_NOT_STARTED=YES
```

## Promotion decision

Planner now mechanically promotes the unchanged Research Authoring product tree:

```text
C2_FINAL_CANDIDATE_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0
```

No Research Authoring production source is changed by this promotion.

Shared replay infrastructure is separately bound as:

```text
REPLAY_INFRASTRUCTURE_COMMIT=
eafb5e11ec65e54259b99fea44fe169096b9dcb9

DEVELOPMENT_EVIDENCE_PACKET_HEAD=
7d780ca50b67785877a87af0ada967f8389254c2
```

These infrastructure/evidence commits are not part of the Research Authoring product candidate identity.

## Evidence policy

All final G1-G4 evidence for release closure must bind directly to C2.

Historical final evidence on the failed predecessor candidate becomes regression/should-not-change evidence only:

- old G1 -> regression;
- old DII G2 -> regression;
- old MoSAIC G3 -> regression/should-not-change;
- first G4 ChatGPT package -> immutable FAIL regression.

No historical PASS may be stitched into C2 release PASS.

## Authority boundary

This freeze authorizes no final Gate execution, no live Plugin update, no paid API, no PDF production, no main merge, and no release.
