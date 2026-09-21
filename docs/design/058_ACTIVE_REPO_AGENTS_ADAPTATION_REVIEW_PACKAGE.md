# 058 Active Repo AGENTS Adaptation — Review Package

Status: `AWAITING_DESIGN_CRITIC_REVIEW`

## Task

- Task key: `058_active_repo_agents_adaptation`
- Proposal: `docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_PROPOSAL_2026-09-18.md`
- Critic prompt: `docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_CRITIC_PROMPT_2026-09-18.md`
- Planner proposal commit: `4b2bc83c47bbcf6e4fd42cef42d1384d111147d4`
- Current source when drafted: AI_Skills `main@f4da398aa749769b52f884d264fa43b64128d20e`

## Problem

The current repository estate has uneven instruction surfaces:

- some repos were already hygiened under 057;
- some have older Lite/Handoff copies;
- some have only project-local AGENTS;
- some have broken locators or no AGENTS;
- DII has a real user-observed prompt-consumption failure despite a root rule saying the prompt should be displayed;
- CARE's root AGENTS exceeds the default Codex project-doc budget before nested instructions.

The user wants a one-time active-repo adaptation after 056, without repeating a heavy workflow per repo.

## Proposed design

One cross-repo Critic review, then after 056 is fully integrated:

- bind the final canonical Bridge/Lite source;
- generate independent per-repo docs-only prompts;
- edit each repo directly on its canonical branch;
- no task branches/worktrees by default;
- no per-repo Planner/Critic cycle;
- no cross-repo atomic integration;
- no product/runtime/scientific changes;
- one repo failure does not block another.

## Hard dependency

058 mass execution must wait until 056 canonical Bridge/Lite integration is complete, because final HUMAN_ONLY prompt visibility/blocked-resume behavior belongs to 056. Do not propagate a pre-056 Lite snapshot across repositories.

## Current next step

Independent Critic reviews the design only.

`NEXT_HANDOFF = CRITIC`
