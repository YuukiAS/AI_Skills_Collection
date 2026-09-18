# 056 Product Delivery Discipline — Post-057 Execution Package Critic Review

你是 AI Research Stack 的长期独立 Critic thread。

继续：

TASK_KEY = `056_product_delivery_discipline`

当前阶段：

`057 fully integrated -> bounded 056 source-drift revalidation / execution-package amendment v0.3 review`

本轮不是重新设计 v6。不要修改 repo，不创建 branch/worktree，不启动 Executor，不 merge/release/deploy，不安装 Host Policy，不开始 paid API/Terra。

## Review package

Exact package-content commit:

`4f998975f4ca32d817a0d0e59c02d81413455c04`

Review objects:

- `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_POST_057_SOURCE_DRIFT_REVALIDATION_2026-09-18.md`
- `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` v0.3
- `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` v0.3
- `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` v0.3
- `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_REVIEW_PACKAGE.md`

## Mandatory current reads

Read latest AI_Skills main first, then:

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

056 authority:

- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`

057 authority/evidence needed for drift review:

- `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md`
- `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- `results/057_repo_agents_hygiene/MANIFEST.md`
- `results/057_repo_agents_hygiene/RESULT.md`
- current 057 review/integration-recovery evidence only as needed to verify canonical integration state.

Independently check current canonical refs and the relevant source in:

- GPT_Codex_AI_Bridge_Kit main;
- Bobbio develop;
- Lucerna main;
- Mica-for-ChatGPT main;
- Asteria main;
- SeminarArc main;
- CUHK Date main.

Recheck current official `openai/codex` source for the Default-vs-Plan request-user-input assumption rather than relying only on the old probe.

## Frozen decisions — do not reopen without a direct contradiction

Keep closed:

- Lite = 6;
- workflow-core = W1-W5;
- Frontend Design = F-A/F-B/F-C;
- AI Skills Maintainer = one consumption-diagnosis capability;
- no W6/W7;
- no G9/G10;
- Source Discovery remains existing capability;
- Default HUMAN_ONLY transport = durable plain-text transcript wait/resume;
- candidate desired Default native flag = disabled;
- Plan-mode native blocking semantics must remain valid;
- CUHK-like failures map to W1/W3/W5 + Frontend;
- no second state machine/review engine;
- no paid API/Terra.

Do not reopen 057 H1-H9, I1-I6, AGENTS hygiene or integration.

## Narrow review questions

### 1. Post-057 drift attribution

Check whether Planner correctly distinguished:

- already completed by 057;
- unrelated canonical advancement;
- still-valid 056 implementation work;
- genuine architecture contradiction.

In particular verify that no current source requires a v7 redesign.

### 2. 057-completed work removed from 056

Confirm:

- Bobbio old locator write is already present on current `develop`;
- Bobbio is now ZERO WRITE / read-only G6 reference;
- Lucerna/Mica/Asteria/SeminarArc remain ZERO WRITE;
- CUHK Date current root AGENTS exists, but `NO_GENERIC_056_AGENTS_COPY` still follows from current source;
- Bridge 057 scaffold/raw-byte/Lite-versioning behavior is preserved as should-not-change instead of reimplemented.

Reject if v0.3 still allows Executor to “do a little product-repo cleanup”.

### 3. Bridge next version slot

Independently read current Bridge:

- `AGENTS.md`
- `templates/repo/AGENTS_TEMPLATE.md`
- `templates/prompts/AGENT_RULES.md`
- `templates/host/GLOBAL_AGENTS_SNIPPET.md`
- `templates/host/CODEX_CONFIG_PROFILE.md`
- `ai_bridge_kit/host.py`
- `tests/test_host_policy.py`
- `README.md`
- `CHANGELOG.md`
- `pyproject.toml`
- `ai_bridge_kit/__init__.py`

Confirm:

- current canonical version identity is 0.8.3 from 057;
- 056 still changes user-consumable Host/Lite behavior;
- current version contract forbids reusing one formal version for a different candidate;
- `0.8.4` is therefore the correct next compatible candidate slot;
- current package does not authorize release/tag/publish/deploy.

If a different slot is required, cite the current repo-local contract directly.

### 4. Exact current refs

Verify current canonical refs or a later equivalent state:

- AI_Skills `main@f68e800fb604850c20a29cb3c7572e4f1a119236` at revalidation source, with M3 in ancestry;
- Bridge `main@e1d6b781ad7e56d567bed419001069baf439d0a5`;
- Bobbio `develop@ab5dccb6b8b87c49671aa097233ce1bcc38be004`;
- Lucerna `main@687752861b4859f7f24799b9e17d985afc992ad2`, 057 candidate in ancestry;
- Mica `main@e49416f874f633aedc7521734ee5b0f441aae970`;
- Asteria `main@0ce1d4daca1e410ce551570578dd563d4ef67e90`;
- SeminarArc `main@74caaa4ecec16f1bc90987979458d1a4e93f52be`;
- CUHK Date `main@e4fdba4d6e38f300d5aeb9861f7c944f07c61e3d`.

AI_Skills main will naturally be later than the revalidation SHA because this v0.3 package itself was committed. Treat package-only advancement as mechanical; relevant production drift is what matters.

### 5. C056-E1 remains complete

Do not auto-close it merely because 057 finished.

Check that v0.3 still has:

- one plain-text required HUMAN_ONLY question;
- no dependent execution before reply;
- explicit deadline/current run-end authority;
- no-reply -> Goal blocked/achieved=no/complete=no/user-ready=no;
- existing legal human-required/recovery machine state, no new BLOCKED enum;
- later same-Goal exact-once recovery;
- human action != completion;
- External GPT normal waiting unaffected;
- G1 reply and no-reply branches;
- current upstream Default-vs-Plan behavior still supports this route.

Also check the Plan correctly notices the stale workflow TODO wording and limits its repair to consistency with E1, rather than creating a new capability.

### 6. C056-E2 remains complete

Check current Critic contract v1.3 still supplies the generic post-REVISE final-PASS closure explanation and v0.3 does not create a second reporting source/state/gate.

### 7. No accidental v6/gate drift

Compare v0.3 with v0.2/v6.

There must be no new:

- W capability;
- Frontend gate;
- G gate;
- state/schema/ledger/controller/watcher;
- product repo write;
- provider/credential/paid API;
- architecture redesign.

Later workflow TODO evidence marked NEW / DEFER must not be pulled into 056.

### 8. Current narrower authorization is truthful

The user explicitly requires this amended execution package to keep outside the current implementation stage:

- main/develop merge;
- release/tag/package publish/deploy;
- real user Host Policy install/update;
- paid API;
- unrelated product work.

Check that v0.3 Plan/Goal/Kickoff all agree:

- AI_Skills + Bridge task-branch implementation is authorized only after PASS + user-sent Kickoff;
- product repos are ZERO WRITE;
- Bridge source/tests may exercise isolated temporary test fixtures;
- the user's real `$CODEX_HOME` is not modified;
- no final live `W2_RESUME_056_FINAL` smoke is requested under this Kickoff;
- isolated evidence cannot be misreported as final real-host G1 PASS;
- overall 056 cannot be called achieved while a required real-host integration boundary remains pending.

This is an execution-stage authorization tightening, not a v7 architecture change.

## PASS explanation requirement

056 has already had formal REVISE rounds. If this review ends in PASS, follow `CRITIC_ROLE_CONTRACT.md` v1.3 and **first** explain in normal Chinese, before machine fields/Kickoff:

1. Lite L1-L6 final role;
2. Bridge Host/Lite changes, 057 behavior preserved, 0.8.4 slot, and current no-real-Host-install boundary;
3. workflow-core W1-W5 + existing Source Discovery;
4. Frontend F-A/F-B/F-C and Figma/motion production wiring;
5. AI Skills Maintainer consumption diagnosis;
6. repo-specific disposition: Bobbio/Lucerna/Mica/Asteria/SeminarArc/CUHK Date all ZERO WRITE and why;
7. G1-G8 and what each proves;
8. Source Discovery regression and why it is not G9;
9. affected candidate versions / no-release boundary;
10. what the user will do less of and what Codex must do more of;
11. what this PASS proves and does not prove.

Do not turn this explanation into a log dump.

## Output

If there is a blocker:

```text
RESULT = REVISE
TASK_KEY = 056_product_delivery_discipline
REVIEW_PACKAGE_VERSION = v0.3
PACKAGE_CONTENT_COMMIT = 4f998975f4ca32d817a0d0e59c02d81413455c04
PLAN = docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md
GOAL = docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md
KICKOFF = docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md
READY_FOR_CODEX = NO
NEXT_HANDOFF = PLANNER
```

Give stable blocker IDs and a complete Planner revision prompt. Keep the review bounded to the current amendment unless a direct source contradiction is found.

If ready:

First provide the required plain-language closure explanation.

Then:

```text
RESULT = PASS
TASK_KEY = 056_product_delivery_discipline
REVIEW_PACKAGE_VERSION = v0.3
PACKAGE_CONTENT_COMMIT = 4f998975f4ca32d817a0d0e59c02d81413455c04
PLAN = docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md
GOAL = docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md
KICKOFF = docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md
C056-E1-HUMAN-GATE-BLOCKED-NOT-ACHIEVED = CLOSED
C056-E2-POST-REVISE-PASS-HUMAN-EXPLANATION = CLOSED
READY_FOR_CODEX = YES
NEXT_HANDOFF = USER_SENDS_APPROVED_KICKOFF
```

Finally return the exact reviewed v0.3 `## Kickoff` body verbatim:

```text
=== APPROVED 056 KICKOFF BEGIN ===
<verbatim reviewed v0.3 kickoff body>
=== APPROVED 056 KICKOFF END ===
```

Do not write a newer “improved” Kickoff after PASS.
