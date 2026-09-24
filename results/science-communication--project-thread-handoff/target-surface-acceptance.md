# Project Thread Handoff V1 — Target Surface Acceptance

Status: `CHATGPT_PLUGIN_WRAPPER_REGULAR_CHAT_PASS`

Final candidate branch: `reviewed/science-communication--project-thread-handoff`

Upload package:

`private/exports/project-thread-handoff-v1.zip`

Package SHA-256:

`0784e81f7141c99a0b79b5a6a48b2226ebe34f2e54bed1759662ffde167b28e1`

## Direct Standalone Skill Route

Observed:

- Skill ZIP upload succeeded.
- ChatGPT Skills page recognized the standalone Skill.
- Work can load the standalone Skill.
- Current user Pro regular Chat runtime did not truly load the standalone Skill.
- Work -> Chat UI workaround can make the entry temporarily visible, but the actual runtime Skill registry remains missing.

Conclusion:

- Direct standalone regular-Chat G1/G2: `NOT_PASS`.
- Do not rewrite the original standalone runtime failure as PASS.
- Do not claim all accounts or surfaces can invoke a bare standalone Personal Skill directly from regular Chat.

## Skills-Only Personal Plugin Wrapper Route

Observed:

- User used Plugin Creator to wrap exact canonical Skill candidate
  `038265a40fae7952a16370c2248e3033fdebbfc9`.
- Wrapper type: PRIVATE, USER-scope, skills-only personal Plugin.
- `MCP_ADDED = NO`.
- ChatGPT regular Chat successfully invoked the bundled Project Thread Handoff Skill.

Conclusion:

- `CHATGPT_PLUGIN_WRAPPER_REGULAR_CHAT = PASS`.
- The wrapper is a distribution package only; it is not a second handoff source.
- Future Skill behavior changes remain owned by
  `skills/science/communication/project-thread-handoff/`.

## Current Gate State

- Direct standalone regular Chat route: `NOT_PASS`.
- Skills-only personal Plugin wrapper regular Chat route: `PASS`.
- G3 development representative regression: PASS.
- Private evidence boundary: no DII thread transcript, no complete private handoff output, and no private Plugin URL or ID committed.
