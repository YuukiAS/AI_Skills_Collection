# 056 Real Host Integration Authorization Review Package — r1

Review object: pre-release real-host G1 authorization package  
Base 056 package: v0.5  
Stage: `REAL_HOST_INTEGRATION_AUTHORIZATION_REVIEW`

## Already closed — do not reopen without new direct evidence

- 056 V6 bounded architecture
- G1-G8 taxonomy
- least-privilege W2/G1 semantics
- version routes / defer dispositions
- C056-E1 / C056-E2 / C056-E3
- C056-I1
- G2-G8 + Source Discovery implementation evidence

## New authorization object

Exact Host:
- `c0824.ll.unc.edu`
- user `aereinh`
- CODEX_HOME `/overflow/htzhu/mingcheng_new/.codex`

Exact Bridge candidate:
`96a8ea1b58ebe6f9b7c5c46c43995666251911fe` / 0.8.5

Exact AI production candidate:
`33c30bbe0dd528031a23d379905cd00d6b65bc1f`

Exact reviewed AI evidence:
`b4adf85bafe29b20de2c2fbeb95668150642f5ae`

Current normal Bridge is 0.8.2:
- executable `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge`
- root `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit`
- HEAD `cb77b1cc5a1fce097a38066d2db452291e359852`

## Key Planner decision to review

Do not permanently bind the user's normal runtime to an unreleased reviewed worktree.

Instead:
1. run exact 0.8.5 candidate directly;
2. temporarily apply candidate Host state to the exact real CODEX_HOME;
3. validate;
4. execute real fresh-session Default/agent-resolvable/Plan G1 smoke;
5. save evidence;
6. restore exact pre-smoke Host state from the existing candidate backup manifest.

Critic must explicitly decide whether temporary apply + real smoke + restoration is faithful final-candidate real-host evidence.

## Mutation envelope

Current preflight means config mutation should only need:
`features.default_mode_request_user_input: true -> false`

Host AGENTS managed block is missing, so official candidate install adds the full 0.8.5 managed block while preserving outside text.

Rules are drifted. Source comparison shows the tracked rules template did not change between active 0.8.2 `cb77b1cc...` and candidate 0.8.5 `96a8ea1b...`. The package forbids broader allowlist and stops before install if live drift would overwrite obvious user-added/non-Bridge policy.

## Recovery object

0.8.5 already provides backup-on-change:
`<CODEX_HOME>/ai-bridge-kit/backups/<UTC timestamp>/manifest.json`

No new restore product mechanism is proposed. Restoration is task-local execution recovery:
- manifest-listed paths only;
- concurrent drift fail-closed;
- verify exact pre/post hashes.

## Live smoke object

Default genuine HUMAN_ONLY:
- fresh real session;
- unknown user-only token;
- plain-text question;
- no native Default card;
- no dependent sentinel write before reply;
- no infer/poll/repeat/timeout-continuation;
- reply `W2_RESUME_056_FINAL`;
- same Goal exact-once resume;
- post-action closure.

Agent-resolvable:
- fresh Default session;
- equivalent reversible internal choice;
- no false user interruption.

Plan:
- fresh Plan session;
- genuine user-owned A/B decision;
- native blocking request_user_input still works.

No Terra, paid API, product-repo writes, or full-suite reruns are required.

## Expected Critic output

REVISE only for a direct risk in this Host authorization/recovery/smoke object. Give stable finding ID, requirement, direct evidence, causal risk and minimum closure, then a complete Planner prompt.

PASS should explain the exact Host mutations, backup/restoration, why normal Bridge 0.8.2 is not permanently upgraded, the Default/Plan user experience, and remaining forbidden boundaries; then approve the exact Goal/Kickoff and emit the Kickoff verbatim with `READY_FOR_CODEX=YES`.

PASS does not authorize release/main/paid/product write.
