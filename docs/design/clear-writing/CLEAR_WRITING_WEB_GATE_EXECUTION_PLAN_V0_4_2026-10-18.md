# Clear Writing Web Gate manual execution Plan v0.4

Date: 2026-10-18  
Status: FROZEN_FOR_EXECUTION_READY_REREVIEW  
Task identity: `clear-writing--every-response-invocation-policy`

## Authority

- Repository: `YuukiAS/AI_Skills_Collection`
- Source/evidence branch:
  `reviewed/clear-writing--scientific-explanation-readability-repair`
- Approved invocation-policy proposal:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md@1f905d294c3c2e5b0951c9d5e818c285d236cef7`
- Proposal Critic PASS:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_2_2026-10-18.md@50e09a2dc68a097ef21e0cf245f7951eb9d06f89`
- Execution-ready v0.3 review:
  `docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_EXECUTION_READY_CRITIC_REVIEW_V0_3_2026-10-18.md@e33b42169aeade563ebb360e16d6380729a8b902`
- Frozen production candidate:
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`
- Tracking: Issue #13

This v0.4 Plan changes only the execution transport and blind-review isolation
needed to close `CW-WEB-ER-01` and `CW-WEB-ER-05`.

`CW-WEB-ER-02`, `CW-WEB-ER-03` and `CW-WEB-ER-04` remain closed and their
v0.3 contracts are reused without redesign.

## 1. Objective

Run the approved Clear Writing Web Gate as a **manual, user-authorized Web
evaluation**, decoupled from the exhausted Reviewed Handoff machine state.

The Web evaluation still tests the approved invocation-policy v0.2:

- W0: natural/mixed safety and exact-only non-contamination;
- W1: `PROJECT_POLICY_BEHAVIOR_RELIABILITY` only;
- W2: strict matched plugin incremental value;
- W3: non-release-critical diagnostic;
- G7: forbidden in this package.

Production and the six-skill architecture remain unchanged.

## 2. CW-WEB-ER-01 — decouple manual Web execution from exhausted machine state

### 2.1 Existing machine state is intentionally inert

The existing Reviewed Handoff task exhausted its one allowed Plan revision at:

```text
plan_revision=1
max_plan_revisions=1
```

v0.4 therefore closes the machine transport through the current Bridge Kit's
existing legal Planner-decision terminal path:

```text
NEEDS_GPT_PLANNER -> AWAIT_HUMAN_DECISION
human_gate_reason=PLANNER_DECISION
```

The required task-local `FINAL_REPORT.md` is present. This terminalizes only
the exhausted Reviewed Handoff transport; it does not close Issue #13 or the
manual Web evaluation.

`AWAIT_HUMAN_DECISION` is not watcher-eligible. The machine task is now
deliberately inert and is never re-armed by this package.

Specifically, v0.4 forbids:

- `NEEDS_GPT_PLANNER -> PLAN_FROZEN` re-arm;
- raw `CURRENT.json` edit;
- resetting `plan_revision`;
- increasing `max_plan_revisions`;
- adding a state/schema;
- modifying Bridge Kit;
- starting watcher/Codex to execute the Web Gate;
- pretending the manual Web evaluation is a Reviewed Handoff Executor event.

After the legal terminalization above, the existing `CURRENT.json` remains
unchanged throughout Web execution.

### 2.2 Manual canonical Web handoff is the execution transport

After execution-ready Critic PASS and after the user sends the approved v0.4
Kickoff, the Web Gate proceeds as a manual canonical prompt handoff governed by
this immutable v0.4 package.

The machine Reviewed Handoff task remains an inert historical/control-plane
record. It is **not** the runtime transport for W0/W1/W2/W3.

This is not a state-graph bypass because no Reviewed Handoff transition is
claimed or performed for the manual Web run.

### 2.3 Watcher remains fail closed

Before any live ChatGPT mutation:

1. resolve the actual authorized AI_Skills checkout for the exact evidence
   branch;
2. run current Bridge Kit `watcher status` for that exact target + branch;
3. if active, run current Bridge Kit `watcher stop`;
4. run `watcher status` again;
5. require proof of no active watcher and no active Executor event.

If watcher inactivity cannot be proven, stop before all live mutation.

The exact branch watcher must remain stopped for the entire manual Web Gate.

### 2.4 Legal start condition

The manual Web Gate may start only when all are true:

1. the machine task remains
   `AWAIT_HUMAN_DECISION / PLANNER_DECISION`;
2. independent execution-ready Critic PASS exists for this exact v0.4 package;
3. user explicitly sends the exact approved v0.4 Kickoff;
4. exact target+branch watcher inactivity is proven;
5. read-only W2 matched-environment preflight v0.4 returns PASS.

No further `CURRENT` transition is part of this start condition.

### 2.5 Legal reviewer handoff after Web evidence

Web evidence is handed to an independent final Critic by the frozen manual
prompt:

`docs/operations/prompts/CLEAR_WRITING_WEB_GATE_FINAL_REVIEW_PROMPT_V0_4_2026-10-18.md`

The final Critic reads the frozen package and actual result evidence directly.

This manual review does **not** create `REVIEW_1.md`, does not alter
`CURRENT.review_round`, and does not pretend to be a machine Reviewed Handoff
review transaction.

The terminalized `CURRENT` stays unchanged.

The final Critic's review artifact is stored as ordinary task evidence under:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/final-review/`

This supplies a legal human/Planner-Critic review path without falsifying the
Bridge state graph.

## 3. Gate-zero preflight remains before all live mutation

Use:

`docs/design/clear-writing/CLEAR_WRITING_W2_MATCHED_ENVIRONMENT_PREFLIGHT_V0_4_2026-10-18.md`

It runs before:

- test candidate creation;
- test Project creation/edit;
- Project bridge writes;
- first model prompt.

It must prove:

- same account/workspace boundary;
- same surface/model/effort;
- exact same bridge bytes;
- candidate availability/consumption can be the only W2 arm difference;
- no account/subscription/workspace/role/permission mutation;
- no repeated global install/uninstall;
- project-only or explicitly equivalent cross-arm memory isolation;
- feasibility of the separate W2 blind-review isolation context.

If any required condition cannot be proven:

`W2=INCONCLUSIVE`

and the entire live batch stops before candidate/Project creation and before
W0/W1/W2/W3.

W3 cannot rescue W2.

## 4. Candidate materialization remains frozen

Reuse unchanged:

`docs/design/clear-writing/CLEAR_WRITING_WEB_TEST_CANDIDATE_MATERIALIZATION_V0_3_2026-10-18.md`

The sole source authority remains:

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

After preflight PASS only:

- deterministically build the exact archive;
- record per-file/archive hashes;
- create at most one PRIVATE Clear Writing test candidate;
- record real plugin/release/version/scope/discoverability identity;
- re-read Plugin Creator metadata/files/full archive;
- prove actual Web release parity before W0.

Any failure after candidate creation leaves it unchanged + PRIVATE. No
uninstall/delete/update/publish/replacement is authorized.

## 5. W0/W1/W2/W3 semantics remain unchanged

Task inputs and gate semantics are frozen in:

`docs/design/clear-writing/CLEAR_WRITING_WEB_GATE_TASK_BANK_V0_4_2026-10-18.md`

Accepted rules remain:

- W0 release-critical safety first;
- W1 only proves `PROJECT_POLICY_BEHAVIOR_RELIABILITY`;
- W2 is strict matched causal evidence;
- W2 scoring is unchanged:
  - Treatment preferred at least 4/7;
  - Control preferred at most 1/7;
  - Treatment zero hard failure;
  - exact/mixed controls do not regress;
- W2 INCONCLUSIVE stops and W3 is not run;
- determinate W2 PASS/FAIL may be followed by W3 diagnostic;
- W3 never rescues W2;
- G7 is forbidden.

One model answer per frozen task/turn/arm remains the default.
Infrastructure-only retry rules remain unchanged.

## 6. CW-WEB-ER-05 — real blind-review isolation

### 6.1 Isolated blind review context

The initial W2 preference review must use:

`docs/design/clear-writing/CLEAR_WRITING_W2_BLIND_REVIEW_CONTEXT_V0_4_2026-10-18.md`

Preferred Web transport:

- a **new empty Project** named `CW-W2-BLIND-v04`;
- project-only memory;
- zero prior task chats;
- zero Project files/knowledge/repository source;
- no current AI Research Stack Project membership/context;
- no GitHub/Files/Plugin/web/connected-source access;
- one new blind-review chat.

A fresh thread inside the current AI Research Stack Project is explicitly
invalid.

### 6.2 Blind-review context pre-record

Before the first blind-review model response, record:

- sanitized blind-review context identity;
- surface/model/effort;
- project-only/equivalent isolation mode;
- zero related file/knowledge count;
- zero prior task-chat count;
- blind packet hash;
- blind prompt hash.

If the isolation cannot be proven, W2 cannot receive PASS.

### 6.3 Blind Reviewer input

Use the frozen prompt:

`docs/operations/prompts/CLEAR_WRITING_W2_BLIND_REVIEW_PROMPT_V0_4_2026-10-18.md`

The Reviewer receives only:

- exact task id;
- exact prompt;
- two opaque output labels and raw outputs;
- frozen preference/hard-failure rubric.

Before verdict freeze it must not access:

- AI Research Stack Project;
- `YuukiAS/AI_Skills_Collection`;
- GitHub;
- Files/Project files;
- Plugin Creator/Plugin Management;
- web;
- connected apps;
- execution package;
- reveal map;
- Treatment/Control identity;
- execution order/timestamps/load evidence/account/workspace locators.

Any such access invalidates the blind review. Do not rerun to obtain a favorable
result.

### 6.4 Opaque mapping remains pre-frozen

Reuse unchanged:

`docs/design/clear-writing/CLEAR_WRITING_W2_REVEAL_MAP_V0_3_2026-10-18.json`

The execution-ready Critic sees this reveal map and is therefore ineligible to
serve as the later blind preference Reviewer.

The blind Reviewer must be a different independent thread inside the isolated
context above.

### 6.5 Verdict freeze before reveal

For P01-P08 the blind Reviewer must freeze verdict + reason in:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/W2/blind/BLIND_VERDICTS_FROZEN.md`

Record its hash before reveal.

Only after all verdicts/reasons are frozen may the execution operator read/use
the reveal map and produce the causal W2 summary.

The blind Reviewer itself never needs reveal access.

## 7. Frozen contracts are read-only after execution-ready PASS

Read-only:

- proposal v0.2 + proposal Critic review;
- this v0.4 Plan;
- Goal v0.4;
- Kickoff v0.4;
- Task Bank v0.4;
- Project bridge bytes;
- W2 preflight v0.4;
- candidate materialization v0.3;
- reveal map v0.3;
- blind-review context v0.4;
- blind-review prompt v0.4;
- final-review prompt v0.4;
- task/pair order;
- attempt budget;
- rubric/scoring threshold;
- stop/recovery rules.

Execution may write only:

- `results/clear-writing--every-response-invocation-policy/**`;
- Issue #13 necessary tracking copy.

The exhausted Reviewed Handoff `CURRENT.json` remains read-only and unchanged
during manual execution.

If a frozen contract needs changing:

**stop -> Planner -> independent Critic**.

## 8. Evidence root and privacy

All live evidence:

`results/clear-writing--every-response-invocation-policy/web-gate-v0.4/`

Required evidence includes:

- preflight;
- watcher status/stop proof;
- freeze manifest + exact bridge hash;
- candidate archive/file manifest and Web release parity;
- W0 raw outputs;
- W1 full turns;
- W2 raw arm evidence;
- blind-review context manifest;
- sanitized blind packet;
- frozen blind verdicts + hash;
- reveal record + causal summary;
- W3 when reachable;
- attempt/retry record;
- `RESULT.md`;
- `FINAL_REVIEW_INPUT_MANIFEST.md`;
- final independent review artifact.

Do not publish account IDs, credentials, private URLs or unrelated Project
content. Private UI screenshots remain under `private/exports/`.

## 9. Stop / recovery

Stop immediately if:

- watcher inactivity cannot be proven;
- W2 preflight is INCONCLUSIVE;
- candidate parity fails;
- W0 fails;
- W1 fails;
- W2 matching fails or becomes contaminated;
- blind-review isolation cannot be proven;
- blind Reviewer accesses a forbidden source/tool/context;
- surface/model/candidate identity changes;
- a frozen rule would need modification.

No adaptive successor or cleanup is created automatically.

## 10. Completion and claim boundary

Successful v0.4 Web Gate execution requires:

- preflight PASS;
- exact candidate parity PASS;
- W0 PASS;
- W1 behavior reliability PASS;
- W2 strict matched incremental-value PASS;
- valid isolated blind review;
- W3 diagnostic recorded;
- independent final review PASS.

This only permits a later separately frozen G7 package.

It does not authorize:

- real Project-setting rollout;
- production changes;
- release/version bump;
- G7;
- PIE;
- Mica;
- Research Authoring;
- Presentations.
