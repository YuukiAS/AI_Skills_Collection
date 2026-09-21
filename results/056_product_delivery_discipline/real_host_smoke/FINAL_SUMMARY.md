# 056 Real Host Smoke Evidence Summary

Status: `FAIL`

The temporary Bridge 0.8.5 host install and candidate `host validate` passed, and the candidate Host policy was removed after smoke. The overall gate is not PASS because Plan-mode fresh-session evidence is unavailable from the current tool surface and exact pre-smoke Host state was not fully restored: `config.toml` marketplace metadata changed during smoke and was preserved to avoid overwriting unrelated live config drift.

## Gate Results

- `CANDIDATE_HOST_VALIDATE=PASS`
- `DEFAULT_HUMAN_ONLY_PLAIN_TEXT=PASS`
- `DEFAULT_WAIT_NO_CONTINUATION=PASS`
- `SAME_GOAL_EXACT_ONCE_RESUME=PASS`
- `POST_ACTION_CLOSURE=PASS`
- `AGENT_RESOLVABLE_NO_FALSE_PROMPT=PASS`
- `PLAN_MODE_NATIVE_INPUT_NONREGRESSION=FAIL`
- `HOST_PRESTATE_RESTORED=NO`
- `UNEXPECTED_HOST_MUTATION=YES`

## Key Locators

- Backup: `/overflow/htzhu/mingcheng_new/.codex/ai-bridge-kit/backups/20260921T222437Z`
- Default HUMAN_ONLY successful thread: `01a0c617-73f9-7f63-a473-299f7f94542b`
- Sentinel: `results/056_product_delivery_discipline/real_host_smoke/default_resume_sentinel.txt`

`NEXT_HANDOFF=CRITIC`
