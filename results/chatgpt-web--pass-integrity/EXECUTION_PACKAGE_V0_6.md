# PASS integrity v0.6 execution package manifest

Task key: `chatgpt-web--pass-integrity`  
Stage: FINAL_EXECUTION_READY_CRITIC_PENDING  
Design branch: `design/chatgpt-web--pass-integrity-v0-4`  
Current formal main baseline at package formation: `272f5cd1b3599acb0c5b95ef57ce00a0cf1b0ac3`

## Review history

- v0.4 Critic:
  `results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_4_CRITIC_REVIEW_2026-10-20.md`
- v0.5 Critic:
  `results/chatgpt-web--pass-integrity/PASS_ATOMIC_DELIVERY_V0_5_CRITIC_REVIEW_2026-10-20.md`

Stable findings:

```text
PASSINT-V04-01=CLOSED
PASSINT-V05-01=CLOSED_IN_V0_6_DESIGN
PASSINT-V05-02=CLOSED_IN_V0_6_DESIGN
```

## v0.6 package files

- Proposal:
  `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_PROPOSAL_V0_6_2026-10-20.md`
- Execution Plan:
  `docs/workflows/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_EXECUTION_PLAN_V0_6_2026-10-20.md`
- Canonical Goal:
  `docs/goals/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_GOAL_V0_6.md`
- Kickoff Draft:
  `docs/operations/prompts/CHATGPT_WEB_PASS_ATOMIC_DELIVERY_KICKOFF_DRAFT_V0_6_2026-10-20.md`

The final Critic invocation must supply one exact `PACKAGE_COMMIT` containing all package files plus the v0.6 Critic prompt. The Critic must read every package file from that same exact commit.

## Intended implementation identity if and only if final Critic PASS occurs

```text
task_key=chatgpt-web--pass-integrity
execution_branch=reviewed/chatgpt-web--pass-integrity
execution_worktree=/tmp/ai-skills-chatgpt-web-pass-integrity
```

## Candidate authority contract

Implementation later freezes:

`GOVERNANCE_CANDIDATE_COMMIT=<exact implementation candidate commit>`

All candidate-phase deterministic replay, post-implementation Critic safety gate, Clear Writing negative control, Clear Writing positive execution-ready regression, and PASS-follow-up regression must explicitly read Planner/Critic 1.8 from this exact candidate commit.

Current `main` remains 1.7 until final integration succeeds.

## No implementation authority yet

Before the final execution-ready Critic produces the unique `PASS + READY_FOR_CODEX=YES` and the user actually sends the short `COPY TO CODEX`:

- no execution branch/worktree creation;
- no 1.8 implementation;
- no Clear Writing branch mutation;
- no G1-G6;
- no main integration;
- no Personal Plugin mutation;
- no paid calls.
