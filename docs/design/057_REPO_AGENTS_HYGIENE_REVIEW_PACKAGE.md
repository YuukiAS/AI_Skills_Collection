# 057 Repo AGENTS Hygiene — Review Package

Status: `AWAITING_INTEGRATION_RECOVERY_CRITIC_R2`

## Task identity

- Task key: `057_repo_agents_hygiene`
- Approved design proposal: `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- Approved bounded versioning amendment: `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- Implementation Plan/Goal v0.2: executed and independently reviewed
- Final reviewed implementation evidence: `E3 = 745281b70322b8508e43e59a5bdef70529749ea5`
- Final reviewed implementation manifest: `M3 = 24051588d13f07e7f71e0edf5a723aca36754ed5`
- Prior Integration Plan/Goal/Kickoff: v0.2, execution attempted then blocked by local canonical-checkout preflight
- Current recovery proposal: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md` v1.1
- Current narrow R2 Critic prompt: `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_R2_CRITIC_PROMPT_2026-09-17.md`
- Stage: lighter per-repo integration recovery R2

## Implementation review closure

Independent Critic accepted the repaired final implementation tuple and closed:

- C057-I1 Bridge H8 raw-byte preservation
- C057-I2 Bridge version/Lite closure
- C057-I3 Mica testing consolidation
- C057-I4 Asteria map conversion
- C057-I5 SeminarArc map conversion
- Bobbio consolidation
- C057-I6 historical M SHA mismatch
- H1–H9 final implementation review

The reviewed implementation tuple remains frozen and is not being reopened.

## Exact reviewed tuple

- AI_Skills E3: `745281b70322b8508e43e59a5bdef70529749ea5`
- AI_Skills M3: `24051588d13f07e7f71e0edf5a723aca36754ed5`
- Bridge: `e1d6b781ad7e56d567bed419001069baf439d0a5`
- Bobbio: `ab5dccb6b8b87c49671aa097233ce1bcc38be004`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica: `e49416f874f633aedc7521734ee5b0f441aae970`
- Asteria: `0ce1d4daca1e410ce551570578dd563d4ef67e90`
- SeminarArc: `74caaa4ecec16f1bc90987979458d1a4e93f52be`
- CUHK Date inspected only: `711fab75f044b7ad31e5ff8610c076f902ccc949`

## Integration recovery history

The globally coupled clean-canonical-checkout integration path was abandoned after repeated real execution blocks on unrelated local state:

- AI_Skills ordinary local `main` contains stale/diverged old 044 work and must not be reset/rebased/cleaned for 057;
- Bridge ordinary local `main` has a pre-existing `.gitignore` change and must not be stashed/reset/cleaned/committed for 057.

No canonical integration push was performed by the blocked run.

Recovery v1 proposed repo-by-repo execution:

- Bridge/Bobbio/Mica/Asteria/SeminarArc: explicit exact-SHA non-force push after ancestry verification;
- Lucerna/AI_Skills: existing reviewed worktree, detached current `origin/main`, no-manual-edit mechanical merge, non-force push, switch back;
- one repo failure does not block unrelated repo prompts;
- successful partial integration remains truthful and is not rewritten.

Independent Critic accepted that recovery direction but returned `REVISE` on exactly two stable blockers:

- `C057-R1-CANONICAL-PUSH-DESTINATION-IDENTITY`
- `C057-R2-PARTIAL-INTEGRATION-056-HANDOFF`

## v1.1 response

### R1 — ACCEPT

All seven exact repo prompts now perform a **read-only remote identity gate before any fetch/push/merge**:

- verify local repo identity;
- inspect effective `origin` fetch URL;
- inspect all effective `origin` push URLs, including pushurl;
- normalize equivalent GitHub SSH/HTTPS forms to exact `github.com/YuukiAS/<repo>` identity;
- require every effective push destination to resolve only to the declared canonical repo;
- extra destination, mismatch or ambiguity stops only that repo;
- no `git remote set-url`, pushurl/config rewrite, remote remap or equivalent mutation is allowed.

This proves destination identity separately from exact source commit identity.

### R2 — ACCEPT

Repo-by-repo execution may still produce truthful partial integration, but partial integration is explicitly **not** 057 integration completion.

The recovery proposal now requires successful integration evidence for all seven mutable canonical targets before any handoff to 056:

- Bridge
- Bobbio
- Mica-for-ChatGPT
- Asteria
- SeminarArc
- Lucerna
- AI_Skills_Collection

Prompt G no longer advances unconditionally after AI_Skills succeeds. If any target is `BLOCKED`, `FAILED`, or `NOT_RUN`, it must report the exact partial state, preserve successful published integrations, keep 056 untouched, and hand back to Planner for 057 integration status/recovery.

## Accepted recovery direction remains frozen

No other recovery semantics changed:

- exact reviewed tuple/M3 unchanged;
- canonical target branches unchanged;
- five fast-forward repos remain exact-SHA non-force pushes;
- AI_Skills/Lucerna remain detached reviewed-worktree clean mechanical merges;
- current path-overlap/conflict stop conditions remain;
- no manual reconciliation;
- no new branch/worktree;
- no force/rebase/squash/cherry-pick/history rewrite;
- no user-work stash/reset/clean;
- CUHK Date remains inspect-only;
- Bridge remains `0.8.3` source-only, no tag/release/package publish/deploy/Host install/`0.8.4`;
- no Bridge 363-test/H1–H9 rerun merely for integration;
- no paid API;
- no 056 work until all seven 057 canonical integrations are complete.

## External Git basis for R1

Official Git documentation confirms:

- `git remote get-url [--push] [--all]` exposes effective remote URLs and expands URL rewrite configuration;
- push URLs can differ from fetch URLs;
- a configured remote can have multiple push URLs and pushes go to all configured push destinations.

Therefore exact source SHA alone is not enough; the v1.1 remote-identity gate is a necessary narrow correction.

## Hard boundary

The seven per-repo recovery prompts remain **unapproved** until independent Critic returns:

```text
RESULT = PASS
READY_FOR_PER_REPO_INTEGRATION = YES
```

for recovery proposal v1.1.

If PASS, the user may send the seven approved repo prompts independently. No additional integration package should be created unless a repo's actual remote preconditions materially change.

`NEXT_HANDOFF = CRITIC`
