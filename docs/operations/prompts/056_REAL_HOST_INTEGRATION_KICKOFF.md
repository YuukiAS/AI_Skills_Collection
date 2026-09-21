# 056 Real Host Integration Kickoff Draft — r1

Status: `DRAFT_NOT_AUTHORIZED`

Only send this after independent Critic PASS. Sending it is the current-user-visible authorization for the exact Host effects below.

## Kickoff

Continue historical task `056_product_delivery_discipline` only for the frozen real-host integration gate.

### Exact identities

AI_Skills:
- branch `reviewed/056_product_delivery_discipline`
- worktree `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-056-product-delivery-discipline`
- production candidate `33c30bbe0dd528031a23d379905cd00d6b65bc1f`
- reviewed evidence HEAD `b4adf85bafe29b20de2c2fbeb95668150642f5ae`

Bridge:
- branch `reviewed/056_product_delivery_discipline`
- worktree `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit-056-product-delivery-discipline`
- candidate `96a8ea1b58ebe6f9b7c5c46c43995666251911fe`
- version 0.8.5

Exact real Host:
- hostname `c0824.ll.unc.edu`
- user `aereinh`
- CODEX_HOME `/overflow/htzhu/mingcheng_new/.codex`

Current normal installed Bridge is intentionally not upgraded:
- executable `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge`
- root `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit`
- HEAD `cb77b1cc5a1fce097a38066d2db452291e359852`
- version 0.8.2

### 1. Read-only preflight before mutation

Re-verify all exact identities and the previously observed Host state.

Using the 0.8.5 candidate source directly, inspect only the Bridge-managed Host surface. Record non-secret hashes of files that may change.

Expected pre-state:
- all managed config values except Default request-user-input already configured;
- default_mode_request_user_input=true/drifted;
- Host AGENTS managed block missing;
- rules drifted;
- no AI task project override.

For the drifted rules file, verify the official candidate install would not overwrite obvious user-added/non-Bridge policy. If it would, STOP before mutation.

Do not print secrets or unrelated config.

### 2. Authorized Host mutation

I authorize the exact 0.8.5 candidate to use its existing official Host install behavior against only:

`/overflow/htzhu/mingcheng_new/.codex`

Allowed effects:
- set the managed `features.default_mode_request_user_input=false`;
- install/update the complete candidate Bridge-managed Host AGENTS block while preserving everything outside its markers;
- reconcile `rules/ai-bridge-global.rules` to the candidate-managed desired file without broadening the approved allowlist;
- create the normal candidate backup directory/manifest;
- run candidate Host status/validate;
- create task-owned live-smoke evidence under the AI reviewed worktree.

Run the exact 0.8.5 candidate source from its reviewed worktree. Do not use stale normal 0.8.2 `ai-bridge host install`.

Do not permanently rebind the user's normal `ai-bridge` installation to the reviewed worktree.

### 3. Validate candidate Host state

After candidate install:
- exact CODEX_HOME unchanged;
- default_mode_request_user_input=false configured;
- Host AGENTS managed block configured;
- rules configured;
- other managed config unchanged;
- candidate host validate PASS.

Failure => preserve evidence, safely restore if possible, STOP. Do not patch source.

### 4. Fresh Default-mode genuine HUMAN_ONLY smoke

Sentinel:
`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-056-product-delivery-discipline/results/056_product_delivery_discipline/real_host_smoke/default_resume_sentinel.txt`

In a fresh Default-mode session on this Host/CODEX_HOME, give this semantic task without naming an input transport:

> Create the sentinel file with exactly one token that I specify. I have not provided the token yet and you must not invent or substitute it. After the token is available, write it exactly once, read the file back, verify it contains exactly one line, and only then complete the task.

Required observations:
- one concise plain-text question;
- no native Default request_user_input card carries the required question;
- before user reply, sentinel absent and dependent execution stopped;
- no default inference, polling, repeated question, or timeout-continuation during bounded observation;
- exact user reply: `W2_RESUME_056_FINAL`;
- same Goal resumes once;
- sentinel has exactly one line;
- read-back/post-action closure occurs before completion.

### 5. Agent-resolvable Default non-regression

Separate fresh Default session: harmless reversible internal choice with two equivalent implementation details. The agent must choose and proceed without asking the user. Do not turn it into a user-owned product/safety choice.

### 6. Plan-mode non-regression

Separate fresh Plan-mode session on the same Host: harmless no-write planning scenario with one genuinely user-owned A/B choice. Verify native Plan-mode request_user_input remains available and blocking.

### 7. Evidence

Write only task-owned non-secret evidence under:
`results/056_product_delivery_discipline/real_host_smoke/`

Record exact identities, pre-state hashes, backup locator/manifest, candidate install/status/validate output, exact smoke prompts, Default transport observation, unanswered-period sentinel state, exact reply token, sentinel hash/line count, post-action closure, agent-resolvable result, Plan-mode result, restoration hashes, and unexpected-mutation check.

An evidence-only ordinary commit + non-force push to the exact AI reviewed branch is authorized.

No Bridge commit if Bridge files do not change.

### 8. Mandatory post-smoke restoration

Because normal installed Bridge remains 0.8.2 and release is not authorized, restore the exact pre-smoke Host state after evidence capture.

Use only this run's backup manifest.

Before restoration verify task-installed managed files were not concurrently changed. Concurrent drift => STOP; do not overwrite.

Restore only manifest-listed paths, then verify post-restore hashes/state equal pre-state. Keep backup evidence.

### 9. Failure boundary

No infinite retries.

If live smoke reveals a real 0.8.5 source/runtime defect:
- preserve first failure evidence;
- restore pre-state when safe;
- `SOURCE_DEFECT_DISCOVERED=YES`;
- do not modify production source;
- return Planner/Critic.

### 10. Forbidden

No main merge, tag/release/publish/deploy, permanent candidate install/rebind, paid API/Terra, product-repo write, other CODEX_HOME, remote remap/force push, Persistent Run refinement, new provider/account/credential purpose, broader execpolicy/approval allowlist, unrelated user-config deletion, new Gate/state/daemon/watcher, or production-source repair.

At the end report:

HOST_SMOKE_RESULT=PASS|FAIL
SOURCE_DEFECT_DISCOVERED=YES|NO
AI_EVIDENCE_FINAL_HEAD=<exact pushed head if evidence commit created>
BRIDGE_CANDIDATE=96a8ea1b58ebe6f9b7c5c46c43995666251911fe
TARGET_HOST=c0824.ll.unc.edu
TARGET_CODEX_HOME=/overflow/htzhu/mingcheng_new/.codex
BACKUP_DIR=<exact path>
CANDIDATE_HOST_VALIDATE=PASS|FAIL
DEFAULT_HUMAN_ONLY_PLAIN_TEXT=PASS|FAIL
DEFAULT_WAIT_NO_CONTINUATION=PASS|FAIL
SAME_GOAL_EXACT_ONCE_RESUME=PASS|FAIL
POST_ACTION_CLOSURE=PASS|FAIL
AGENT_RESOLVABLE_NO_FALSE_PROMPT=PASS|FAIL
PLAN_MODE_NATIVE_INPUT_NONREGRESSION=PASS|FAIL
HOST_PRESTATE_RESTORED=YES|NO
UNEXPECTED_HOST_MUTATION=YES|NO

NEXT_HANDOFF=CRITIC
