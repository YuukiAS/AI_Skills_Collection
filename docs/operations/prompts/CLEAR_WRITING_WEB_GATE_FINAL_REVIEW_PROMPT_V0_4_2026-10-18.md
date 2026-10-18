# Clear Writing Web Gate v0.4 — final independent review prompt

你现在担任 Clear Writing Web Gate v0.4 的最终独立 Reviewer。

这不是 W2 初始盲评。W2 初始 preference verdict 必须已经在隔离的 blind-review context 中完成并冻结；你现在可以读取 reveal map、process/identity evidence 和全部 Web Gate evidence，形成最终因果与产品结论。

## Review identity

- repository: `YuukiAS/AI_Skills_Collection`
- task: `clear-writing--every-response-invocation-policy`
- evidence branch:
  `reviewed/clear-writing--scientific-explanation-readability-repair`
- frozen production candidate:
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- approved invocation-policy proposal:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md`
- manual execution Plan:
  `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_EXECUTION_PLAN_V0_4_2026-10-18.md`
- Goal:
  `docs/goals/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_WEB_GATE_GOAL_V0_4_2026-10-18.md`
- Task Bank:
  `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_4_2026-10-18.md`
- evidence root:
  `results/clear-writing--every-response-invocation-policy/web-gate-v0.4/`

## Must read

Read the frozen v0.4 execution package and the actual evidence, including:

- W2 matched-environment preflight v0.4;
- watcher inactivity evidence;
- candidate deterministic archive/file manifest;
- Plugin Creator post-create release parity evidence;
- W0 full raw outputs and exact comparisons;
- W1 full turn-by-turn outputs;
- W2 raw Treatment/Control execution evidence;
- blind-review context manifest;
- sanitized blind packet;
- frozen blind verdicts + hash;
- W2 reveal map;
- reveal record + causal summary;
- W3 evidence if reachable;
- attempt/retry log;
- `RESULT.md`;
- `FINAL_REVIEW_INPUT_MANIFEST.md`.

Do not judge from executor summaries alone.

## Required checks

### 1. Process / identity

Confirm:

- Web candidate is proven source-equivalent to `fd7a1578...`;
- no unapproved account/Project/plugin mutation occurred;
- one-answer / infrastructure-only retry rule was respected;
- frozen contract was not modified after outputs were seen;
- W2 strict matching and memory isolation remained valid;
- if W2 became INCONCLUSIVE, no W3 was run.

### 2. W0

Give:

`W0_PRODUCT_SAFETY=PASS|FAIL`

Check natural/mixed safety, exact machine protection, sibling ownership, long-answer preservation and explicit-plugin exact-only non-contamination.

Do not upgrade plugin-level exact stress into loaded-Skill bypass without direct evidence.

### 3. W1

Give:

`W1_PROJECT_POLICY_BEHAVIOR_RELIABILITY=PASS|FAIL`

W1 does not prove plugin causality.

### 4. W2 blind-review integrity

Before using the blind verdicts, confirm:

- blind Reviewer context was new/empty and project-only or equivalently isolated;
- no AI Research Stack Project history/repo/tool/connector source was accessible;
- blind packet contained only allowed fields;
- P01-P08 verdict + reasons were frozen and hashed before reveal;
- no rescoring happened after reveal.

If blindness was not valid, W2 cannot PASS.

### 5. W2 causal result

Using the frozen blind verdicts + reveal map + process identity, give exactly one:

- `W2_PLUGIN_INCREMENT=PASS`
- `W2_PLUGIN_INCREMENT=FAIL`
- `W2_PLUGIN_INCREMENT=INCONCLUSIVE`

Apply the frozen rule only:

- Treatment preferred on at least 4/7 P01-P07;
- Control preferred on at most 1/7;
- Treatment zero hard failures;
- exact/mixed protection does not regress;
- P08 is hard control only.

Do not change rubric or threshold.

### 6. W3

If W3 was reachable, report its discoverability/fallback finding as diagnostic only.

If W2 was INCONCLUSIVE, confirm W3 was not run.

### 7. Claim boundary

A full Web Gate PASS requires W0 PASS, W1 PASS and W2 PASS with valid process/identity evidence.

Even then, the maximum next state is:

`READY_FOR_G7_FREEZE`

Do not claim:

- fresh G7 PASS;
- real Project rollout;
- production release;
- user acceptance;
- PIE/Mica/Research Authoring/Presentations completion.

## Output

Return:

```text
PROCESS_IDENTITY=PASS|FAIL
CANDIDATE_PARITY=PASS|FAIL
W0_PRODUCT_SAFETY=PASS|FAIL
W1_PROJECT_POLICY_BEHAVIOR_RELIABILITY=PASS|FAIL
W2_PLUGIN_INCREMENT=PASS|FAIL|INCONCLUSIVE
W3_DIAGNOSTIC=<summary|NOT_RUN>
FINAL_WEB_GATE_DECISION=PASS|FAIL|INCONCLUSIVE
NEXT_HANDOFF=PLANNER
```

If FINAL_WEB_GATE_DECISION=PASS, explicitly state:
`READY_FOR_G7_FREEZE`.

Do not execute G7, production rollout or release.
