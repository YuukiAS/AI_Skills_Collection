# PASS integrity v0.5 Critic review — user-forwarded authority

Date: 2026-10-20  
Task key: `chatgpt-web--pass-integrity`  
Reviewed proposal: `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_5_2026-10-20.md@v0.5`  
Proposal commit: `afc19a46bf53d9f8841dee0cc9ec42fe17c41365`  
Reviewed package commit: `af68349e1283a8cb8c1f6928f6bc821236412d28`  
Critic prompt commit: `dc21711269aa9b1951f1eedb947f70c09b18e81d`  
Review stage: `DESIGN_AND_EXECUTION_PACKAGE_REVIEW_V0_5`  
Verdict: `REVISE`

## Stable findings

`PASSINT-V04-01=CLOSED`

The two-stage Clear Writing regression removes the v0.4 contradiction: the old package remains a permanent compatibility negative control, while the positive regression must use a new exact package and does not pre-assume PASS.

`PASSINT-V05-01=OPEN`

The package did not freeze the exact authority for the candidate Planner/Critic 1.8 contracts used by replay and the two-stage regression. It also prohibited main integration for the full task, leaving no normal path by which a successful 1.8 candidate becomes the actual main contract.

Minimum closure:
- freeze `GOVERNANCE_CANDIDATE_COMMIT`;
- all candidate-phase replay and Clear Writing regressions read 1.8 from that same exact commit;
- after all required regression and candidate acceptance, run integration preflight against current main, merge/push under AGENTS.md 8.5, then fresh-read main and confirm both role contracts are 1.8 and expected evidence matches the final candidate;
- no force; competing changes in the same contract area stop for Planner/Critic handling.

`PASSINT-V05-02=OPEN`

The package required both a separate independent implementation review and an implementation-after Critic safety gate, but did not bind a real task-scoped implementation Reviewer transport. This would reintroduce a hidden third manual role / user routing burden.

Preferred minimum closure:
- remove the separate implementation-review stage;
- Codex completes the approved implementation plus deterministic/local checks and compatibility replay;
- the existing implementation-after Critic safety gate directly reviews actual diff, final Planner/Critic 1.8 text, replay evidence, candidate identity, and the frozen two-stage regression inputs/criteria/stop conditions;
- verdict remains `PROCEED_TO_FINAL_EVALUATION / REVISE`;
- only after `PROCEED_TO_FINAL_EVALUATION` run the Clear Writing negative-control and positive execution-ready regressions.

## Scope retained

Do not reopen:
- Planner task-prompt compatibility preflight;
- Critic compatibility hard gate;
- atomic five-part PASS delivery;
- no post-hoc completion of an incomplete PASS;
- PASS follow-up classification as explanation / contradiction evidence / new requirement;
- contradictions may be discovered by the Critic;
- eight deterministic replay cases;
- two-stage Clear Writing regression;
- positive regression does not pre-assume PASS;
- Project setting and Capability Gate Policy remain unchanged;
- Clear Writing product architecture / G1-G6 remain unchanged;
- no new role, schema, state machine, database, service, watcher, daemon, or prompt compiler.

Tracking remains pending; Issue #13/#99 belong to other objects and must not be rebound.
