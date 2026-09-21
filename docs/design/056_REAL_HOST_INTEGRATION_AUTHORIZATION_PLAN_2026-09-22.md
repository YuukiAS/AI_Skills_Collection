# 056 Real Host Integration Authorization Plan — r1

Historical task: `056_product_delivery_discipline`  
Human-readable name: 交付工作流可靠性基线  
Stage: `REAL_HOST_INTEGRATION_AUTHORIZATION_PREPARATION`

This package does not redesign 056. Existing architecture, G1-G8, version routes, owner boundaries, least-privilege semantics, and implementation-review conclusions remain frozen.

## Frozen implementation identities

AI_Skills:
- branch: `reviewed/056_product_delivery_discipline`
- production candidate: `33c30bbe0dd528031a23d379905cd00d6b65bc1f`
- reviewed evidence HEAD: `b4adf85bafe29b20de2c2fbeb95668150642f5ae`
- candidate versions: repo 5.0.7; workflow-core 0.3; web-development 0.2; ai-skills-core 0.4

Bridge:
- branch: `reviewed/056_product_delivery_discipline`
- candidate: `96a8ea1b58ebe6f9b7c5c46c43995666251911fe`
- version: 0.8.5
- candidate worktree: `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`

Implementation review state:
- C056-I1 CLOSED
- G2-G8 + Source Discovery PASS
- G1 source/unit/fixture/non-host evidence PASS
- final real-host G1 smoke PENDING
- Terra NOT REQUIRED

## Exact real Host identity

Read-only preflight froze:
- hostname: `c0824.ll.unc.edu`
- user: `aereinh`
- HOME: `/overflow/htzhu/mingcheng_new`
- CODEX_HOME env/resolved: `/overflow/htzhu/mingcheng_new/.codex`

Relevant Host state:
- approval_policy on-request: configured
- sandbox_mode workspace-write: configured
- approvals_reviewer auto_review: configured
- sandbox network access true: configured
- memories true: configured
- default_mode_request_user_input true: drifted relative to 0.8.5
- global Bridge Host AGENTS managed block: missing
- narrative managed state: missing
- Bridge global rules: drifted
- AI task project overrides: absent
- existing Bridge backup root: absent

## Current installed Bridge and why this stage is temporary

Current normal executable:
`/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge`

Current active source:
`/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit`

Current active identity:
- HEAD `cb77b1cc5a1fce097a38066d2db452291e359852`
- pyproject version 0.8.2
- runtime version 0.8.2

The normal installation is therefore stale relative to the reviewed 0.8.5 candidate. This pre-release gate MUST NOT permanently rebind the user's normal executable to an unmerged reviewed worktree.

Instead, the exact 0.8.5 candidate source is run directly from its reviewed worktree, temporarily applied to the exact real CODEX_HOME, validated and live-smoked, then the pre-smoke Host state is restored. Permanent normal-entry installation belongs after later main/release integration.

## Exact authorized candidate-managed Host delta

Only after Critic PASS and the user sends the approved Kickoff:

1. `/overflow/htzhu/mingcheng_new/.codex/config.toml`
   - managed key `features.default_mode_request_user_input`: `true -> false`
   - preserve all unrelated config

2. `/overflow/htzhu/mingcheng_new/.codex/AGENTS.md`
   - add/update the complete 0.8.5 Bridge-managed Host block
   - preserve all content outside Bridge markers
   - current managed block is missing, so the official installer will add the full block, not only the Human Gate subsection

3. `/overflow/htzhu/mingcheng_new/.codex/rules/ai-bridge-global.rules`
   - reconcile the Bridge-managed file to the 0.8.5 candidate desired text
   - source comparison shows this tracked rules template has no change between current active 0.8.2 commit `cb77b1cc...` and candidate `96a8ea1b...`; this stage must not broaden the execpolicy allowlist
   - if pre-mutation read-only comparison indicates user-added/non-Bridge policy would be overwritten, STOP before mutation

## Backup/restoration

Existing 0.8.5 `host install` creates, only when changes exist:

`/overflow/htzhu/mingcheng_new/.codex/ai-bridge-kit/backups/<UTC timestamp>/manifest.json`

The manifest records modified path, pre-existence, and backup path.

No new restore command/state machine is added.

After smoke, restore the exact pre-smoke Host state because 0.8.5 is not yet the user's released normal CLI:
- verify candidate-installed files have not changed concurrently;
- restore only paths listed in this run's manifest;
- existing paths restore from backup;
- newly created paths are removed only if still identical to the task-installed candidate file;
- do not touch any unlisted path;
- verify post-restore hashes/state equal pre-state;
- concurrent drift => fail closed, do not overwrite.

## Candidate validation

Use exact 0.8.5 candidate source directly, not stale normal 0.8.2 `ai-bridge`, for install/status/validate.

Before mutation recheck exact candidate HEAD/version, target Host/CODEX_HOME, expected Host pre-state, and absence of project overrides. Material drift => STOP.

After install:
- exact CODEX_HOME unchanged;
- default_mode_request_user_input=false configured;
- managed Host AGENTS configured;
- rules configured;
- other already-correct managed config unchanged;
- candidate host validate PASS.

## Final live G1 smoke

Evidence root:
`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-056-product-delivery-discipline/results/056_product_delivery_discipline/real_host_smoke/`

### Default genuine HUMAN_ONLY

Use a fresh Default-mode session on the exact Host/CODEX_HOME.

Sentinel:
`.../real_host_smoke/default_resume_sentinel.txt`

Give a harmless task whose completion requires one user-only token that has not yet been provided. The fresh session is NOT told what transport to use.

Required observations:
- one concise plain-text question;
- no native Default request_user_input card carries the required question;
- before answer, dependent sentinel write does not happen;
- no default inference, polling, repeated question, or timeout-continuation during bounded observation;
- exact user reply: `W2_RESUME_056_FINAL`;
- same Goal resumes once;
- sentinel contains exactly one line with that token;
- read-back/post-action closure occurs before completion.

### Agent-resolvable non-regression

Fresh Default session, harmless reversible internal choice with two equivalent implementation options. It must choose and proceed without asking the user.

### Plan-mode non-regression

Fresh Plan-mode session, harmless no-write planning scenario with one genuinely user-owned A/B decision. Native Plan-mode request_user_input must remain available and blocking.

Current upstream OpenAI Codex Default instructions still say explicit required input should be asked as one concise plain-text question rather than request_user_input; current Plan instructions continue to use request_user_input for material plan decisions. This is external support only; PASS must come from the live Host smoke.

## Evidence and handoff

Store only non-secret task-owned evidence under `results/056_product_delivery_discipline/real_host_smoke/`, including exact identities, pre-state hashes, backup locator, candidate status/validate output, smoke observations, sentinel hash/line count, restoration hashes, and unexpected-mutation check.

An evidence-only ordinary commit + non-force push to the exact AI reviewed branch is allowed after the approved Kickoff. No Bridge commit if Bridge files do not change.

If smoke reveals a source/runtime defect:
- preserve first failure evidence;
- restore pre-state when safe;
- `SOURCE_DEFECT_DISCOVERED=YES`;
- do not repair production source;
- return Planner/Critic.

## Forbidden

No main merge, tag/release/publish/deploy, permanent 0.8.5 normal-install rebind, paid API/Terra, product-repo write, arbitrary CODEX_HOME, remote remap/force push, Persistent Run work, new provider/account/credential purpose, unrelated Host edits, broader execpolicy allowlist, deletion of unrelated user config, new Gate/state/daemon/watcher, or production-source repair.

NEXT_HANDOFF=CRITIC
