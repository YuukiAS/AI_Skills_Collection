# 057 Repo AGENTS Hygiene — Review Package

Status: `AWAITING_CRITIC_REVIEW`

## Task identity

- Task key: `057_repo_agents_hygiene`
- Planner proposal: `docs/design/057_REPO_AGENTS_HYGIENE_PROPOSAL_2026-09-17.md`
- Critic prompt: `docs/design/057_REPO_AGENTS_HYGIENE_CRITIC_PROMPT_2026-09-17.md`
- Stage: design review only

## Purpose

Perform a semantics-preserving cleanup of each target repository's own instruction surface before starting Task 056 implementation. The focus is **within-repo** duplication, contradiction, stale authority and navigation quality, not making all repositories carry identical rules.

Target first-wave repos:

- Bobbio `develop`
- Lucerna `main`
- Mica-for-ChatGPT `main`
- Asteria `main`
- SeminarArc `main`
- CUHK Date `main` prototype instruction surface (inspect; do not create root AGENTS merely for symmetry)

## Hard boundary

No product repo file has been modified by the Planner. No branch/worktree has been created. No Executor is authorized. No 056 production implementation has started.

The already-approved 056 execution package remains unchanged. The user should not send its approved Kickoff if they want 057 completed first. After 057 closes, 056 receives a short source-drift revalidation rather than an automatic architecture redesign.

`NEXT_HANDOFF = CRITIC`
