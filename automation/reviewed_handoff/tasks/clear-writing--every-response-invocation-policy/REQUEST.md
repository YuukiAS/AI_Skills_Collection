# Reviewed Handoff Request

Task: `clear-writing--every-response-invocation-policy`

## Objective

Freeze and later execute the Critic-approved Clear Writing invocation-policy
v0.2 on real ChatGPT Web without changing the already-PASS production candidate.

Invocation-policy authority:
- proposal:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md`
- proposal commit:
  `1f905d294c3c2e5b0951c9d5e818c285d236cef7`
- independent proposal Critic PASS:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_2_2026-10-18.md@50e09a2dc68a097ef21e0cf245f7951eb9d06f89`
- frozen production candidate:
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`

The first execution package at `35c28d5ee695d20bcfcc37ee919d60545cae34bb`
was execution-ready REVISE. Web Gate package v0.3 closes only the five transferred
blocking findings:

- `CW-WEB-ER-01`: watcher/CURRENT fail-closed before user Kickoff;
- `CW-WEB-ER-02`: exact PRIVATE Web candidate materialization/parity contract;
- `CW-WEB-ER-03`: W2 matched-environment preflight before all live mutation;
- `CW-WEB-ER-04`: frozen execution contracts become read-only;
- `CW-WEB-ER-05`: opaque W2 arm labels and genuinely blind first-pass review.

This task is Web product evaluation, not production implementation.

## Required order

0. Execution-ready Critic PASS + user sends approved Kickoff.
1. Prove exact branch watcher inactive and keep watcher disabled for this manual Web transport.
2. Run read-only `W2_MATCHED_ENVIRONMENT_PREFLIGHT`.
3. Only after preflight PASS, deterministically materialize and create at most
   one PRIVATE test candidate from `fd7a1578...`, then verify actual Web release
   parity.
4. W0.
5. W1.
6. W2 strict matched comparison with frozen blind packet.
7. W3 diagnostic only after determinate W2 PASS/FAIL.
8. Stop before G7.

If preflight or later W2 is `INCONCLUSIVE`, release-critical execution stops;
W3 is not run.

## Hard boundaries

- Do not modify `fd7a157...` production source.
- Do not modify the user's real AI Research Stack Project setting.
- Do not modify global custom instructions.
- Do not create/update/delete/uninstall unrelated plugins.
- Do not create a replacement Clear Writing candidate.
- Do not change plugin permissions, account/workspace/subscription/model plan.
- Do not implement PIE or Mica.
- Do not modify Research Authoring or Presentations.
- Do not add a seventh Skill/router/state machine/finalizer.
- Do not release or bump versions.
- Issue #13 remains the only tracking Issue.
