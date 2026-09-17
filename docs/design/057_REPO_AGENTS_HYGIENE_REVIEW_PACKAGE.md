# 057 Repo AGENTS Hygiene — Review Package

Status: `AWAITING_CRITIC_REVIEW`

## Task identity

- Task key: `057_repo_agents_hygiene`
- Current Planner proposal: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Superseded proposal: `docs/design/057_REPO_AGENTS_HYGIENE_PROPOSAL_2026-09-17.md`
- Current Critic prompt: `docs/design/057_REPO_AGENTS_HYGIENE_V2_CRITIC_PROMPT_2026-09-17.md`
- Stage: design review only

## Purpose

057 now has two tightly related goals before Task 056 implementation:

1. semantics-preserving cleanup of each target repository's **own** instruction surface — within-repo duplication, contradiction, stale authority, discoverability and structure;
2. add a reusable **project-owned root `AGENTS.md` scaffold** to Bridge Kit so future fresh repositories do not begin with only a handoff block and then accumulate rules incident-by-incident.

The scaffold standardizes structure/ownership, not project content. `prompts/AGENT_RULES.md` remains the Lite/execution-rule owner; the root template must not duplicate it.

## Target first-wave repos

- Bobbio `develop`
- Lucerna `main`
- Mica-for-ChatGPT `main`
- Asteria `main`
- SeminarArc `main`
- CUHK Date `main` prototype instruction surface — inspect only; do not create root AGENTS merely for symmetry

## Bridge Kit design scope

The v2 proposal asks Critic to review a reusable source template, proposed as:

`templates/repo/AGENTS_TEMPLATE.md`

Expected behavior if later approved/implemented:

- fresh repo without root `AGENTS.md`: real `ai-bridge init` consumes the scaffold and inserts exactly one managed Bridge block;
- existing root `AGENTS.md`: keep current fail-safe behavior, preserve project-owned prose, only append/update the managed Bridge block;
- `--force` must not reset user/project-owned AGENTS content;
- no automatic migration of existing repos;
- no duplicated Lite L1-L6 / `prompts/AGENT_RULES.md` authority.

## Relationship to 056

The already execution-ready-PASS 056 package is **not being redesigned here** and must not start while the user wants 057 completed first.

Proposed sequence:

```text
057 review / implementation / audit / integration
-> return to 056
-> bounded source-drift revalidation
-> mechanical package amendment if needed
-> no v6 redesign unless 057 actually changes a frozen 056 assumption
```

Because 057 may change Bridge Kit production source/version and may already complete the Bobbio Figma locator, the later 056 revalidation must remove duplicate work and refresh exact refs/version targets rather than executing stale assumptions twice.

## Hard boundary

No product repo file has been modified by the Planner. No Bridge Kit production source has been modified. No branch/worktree has been created. No Executor is authorized. No 056 implementation has started.

`NEXT_HANDOFF = CRITIC`
