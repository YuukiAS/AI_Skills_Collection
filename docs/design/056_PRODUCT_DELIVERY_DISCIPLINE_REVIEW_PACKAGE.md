# 056 Product Delivery Discipline — Review Package

状态：`AWAITING_POST_PROBE_CRITIC_REVIEW`

## Task identity

- Task key: `056_product_delivery_discipline`
- Review stage: v6 architecture passed; bounded host probe completed; Planner post-probe implementation direction awaiting short Critic review
- Current architecture authority: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`
- Current post-probe review object: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md`
- Probe draft: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_DRAFT.md`
- Probe result: `docs/design/056_PERSISTENT_PROMPT_CAPABILITY_PROBE_RESULT_2026-09-17.md`
- New CUHK Date real-project feedback: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md`
- Current Critic prompt: `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_CRITIC_PROMPT_2026-09-17.md`
- Primary maintenance inbox: `docs/plugin-todos/workflow-core.md`

No implementation Plan, Goal, Kickoff, reviewed branch/worktree, production plugin change, Bridge Kit production change, or repo-specific AGENTS change is authorized by this package.

## Review history

### Round 1 — v5

Review object:

`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md`

Decision:

`RESULT = REVISE`

Stable blockers:

- `C056-B1-PERSISTENT-PROMPT-CAPABILITY`
- `C056-B2-REVIEW-ADMISSION-SCOPE`
- `C056-B3-ACTIVE-RULE-CONSUMPTION`
- `C056-B4-LAYER-DUPLICATION`

### Round 2 — v6

Review object:

`docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_PROPOSAL_2026-09-16.md`

User relayed the independent Critic conclusion:

- v6 architecture: `PASS`;
- previous four blockers were considered substantively closed by the v6 responsibility split;
- persistent prompt was correctly isolated as a pre-implementation capability probe rather than assumed available;
- the probe draft was acceptable to execute;
- implementation Plan could not yet be frozen because the real probe result would determine W2 transport.

This package does not reinterpret that as production authorization.

## Probe result

The bounded Default-mode probe was executed and returned:

```text
RESULT = PARTIAL
CODEX_CLI_VERSION = codex-cli 0.142.0
COLLABORATION_MODE = DEFAULT
DEFAULT_MODE_REQUEST_USER_INPUT_FEATURE = ENABLED
NATIVE_TOOL_AVAILABLE = YES
ELAPSED_SECONDS = 114
NATIVE_AUTO_RESOLVED = YES
EMPTY_OR_DEFAULT_ANSWER_RETURNED = YES
NATIVE_150S_PENDING = FAIL
FALLBACK_TYPE = DURABLE_TRANSCRIPT_WAIT_RESUME
FALLBACK_RESUME = PASS
HOST_CAPABILITY_GAP = YES
NATIVE_DEFAULT_PERSISTENT_PROMPT = FAIL
```

Therefore native Default-mode `request_user_input` is not an admissible implementation of the user requirement on the tested installation. The transcript fallback demonstrated same-thread bounded resume once.

Current upstream source research also indicates no supported `config.toml` timeout/always-wait control for Default-mode native `request_user_input`; blocking is mode-derived (`Plan` blocking, Default non-blocking). This is why the post-probe addendum proposes `DURABLE_TRANSCRIPT_WAIT_RESUME` and asks Critic to review whether Bridge Kit should fail-closed by disabling `features.default_mode_request_user_input` in Default mode.

## New real-project evidence after v6 review

### Existing repo/source resolution

A Bridge Kit implementation attempt abandoned an existing local repo because of unrelated dirty state, created extra `/tmp` clones, then attempted remote remapping that required separate authorization. Planner treats this as an enforcement gap in existing Verified Workflow Source Discovery / dirty-tree protection, not a new W6 or Bridge Kit product capability.

### CUHK Date Questionnaire V4

Current main now records a real project feedback package showing that broad green tests can still leave acceptance-critical gaps in localized/data-backed consumer flows: demo catalog breadth, untranslated enum fallback, mock-only provider evidence, final-value-only input validation, untested material branches, fallback counted as primary capability, hosted config not consuming an implemented backend capability, and a rewrite regressing a previously strong structured interaction.

Planner maps these into existing v6 owners:

```text
representative breadth / material branches / state lifecycle / fallback != primary -> W1
real hosted provider / interaction sequence -> W3
protect accepted interaction -> W5
localization completeness / actual surface -> Frontend F-B/F-C
```

No new Lite rule or workflow capability is proposed.

## Current review question

The architecture count remains:

```text
Lite baseline             6
workflow-core             5 new/strengthened capabilities
Frontend Design           3 production gates
AI Skills Maintainer      1 consumption-diagnosis capability
Bridge Kit                transport/wait/recovery only
repo AGENTS               project-specific invariant/locator only
```

The post-probe Critic only needs to decide whether:

1. `DURABLE_TRANSCRIPT_WAIT_RESUME` is the correct W2 transport for current Default-mode production use;
2. disabling `default_mode_request_user_input` in Bridge Kit's managed Default-mode config is the smallest fail-closed enforcement or an unnecessary side effect;
3. local existing-repo/worktree reuse belongs inside existing source discovery rather than a new capability;
4. CUHK Date evidence is correctly absorbed into W1/W3/W5/Frontend without making simple tasks heavy.

## Expected next-step boundary

If the post-probe addendum receives Critic PASS:

```text
NEXT_HANDOFF = PLANNER_IMPLEMENTATION_PLAN_DRAFT
```

This still does **not** mean Executor may run. Under the current Critic contract, the later Proposal/Plan + canonical Goal + Kickoff execution package must be reviewed together before `READY_FOR_CODEX=YES`, and the user must then actually send the approved kickoff to authorize execution.
