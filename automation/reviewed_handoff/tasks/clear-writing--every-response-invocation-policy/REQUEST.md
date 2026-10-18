# Reviewed Handoff Request

Task: `clear-writing--every-response-invocation-policy`

## Objective

Freeze and later execute the Critic-approved Clear Writing Web Gate policy v0.2
without changing the already-PASS production candidate.

Authority:
- approved proposal:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md`
- proposal commit:
  `1f905d294c3c2e5b0951c9d5e818c285d236cef7`
- independent Critic PASS:
  `docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_2_2026-10-18.md`
- Critic review commit:
  `50e09a2dc68a097ef21e0cf245f7951eb9d06f89`
- frozen production candidate:
  `fd7a1578a5042a46a55c5b638f6d550655b1096b`

This task is a Web product-evaluation workflow, not a production implementation
task. It must preserve the six-skill Clear Writing architecture and the prior
repo/Codex PRODUCT / ARTIFACT PASS.

## Required gate order

1. W0 — natural/mixed invocation safety plus explicit-plugin exact-only stress.
2. W1 — Project-setting policy multi-turn behavior reliability.
3. W2 — strict matched plugin-vs-setting-only incremental-value comparison.
4. W3 — no-bridge automatic-selection diagnostic only.
5. Fresh G7 is not executable under this task until W0/W1/W2 satisfy their
   release-critical conditions and a later G7 freeze is independently reviewed.

## Hard boundaries

- Do not modify `fd7a157...` production source.
- Do not modify the user's real/production Project setting.
- Do not mutate ChatGPT account/plugin state before execution-ready Critic PASS
  and a later explicit execution kickoff from the user.
- Do not implement PIE or Mica.
- Do not modify Research Authoring or Presentations.
- Do not add a seventh skill, router, state machine or finalizer.
- Do not release or bump versions.
- Issue #13 remains the only tracking Issue.
