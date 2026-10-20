# PASS integrity v0.4 Critic review — user-forwarded authority

Date: 2026-10-20  
Task key: `chatgpt-web--pass-integrity`  
Reviewed proposal: `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_4_2026-10-20.md@v0.4`  
Reviewed proposal commit: `756f99d77e878f99c440a409bf7620e6d038e4a4`  
Reviewed package commit: `0f06d156c55705895b8e9e6331d90c6a5a37ef4e`  
Review stage: `DESIGN_PROPOSAL_REVIEW_V0_4`  
Verdict: `REVISE`

## Stable blocker

`PASSINT-V04-01`

Proposal v0.4 contained a self-contradictory regression contract:

- compatibility hard gate correctly required the old Clear Writing 0.6 task-specific Critic prompt to cause `REVISE` because it conflicts with the central execution-ready contract;
- the positive regression section then proposed using the same exact conflicting package to obtain a valid execution-ready `PASS`.

Those cannot both be true.

## Required closure

The regression must be split into two phases:

1. negative compatibility control: keep exact old package `d7b810d194ead881303aaca9c2e4f1d59a97c1f1`; the new 1.8 compatibility gate must reject it;
2. positive execution-ready regression: minimally repair only the Clear Writing task-specific Critic prompt / locators necessary for compatibility, create a new exact package commit, then run a full execution-ready review under the new central contract.

The positive regression must not force a PASS. If the full review finds a real Clear Writing product blocker, the correct result remains `REVISE` in the same Clear Writing task.

The prior v0.4 design principles remain accepted for revision:
- task-prompt compatibility check;
- atomic PASS delivery;
- PASS follow-up classification as explanation / contradiction evidence / new requirement;
- no Project-setting or Capability Gate Policy change;
- no new role, schema, state machine, service, watcher, database, or prompt compiler.
