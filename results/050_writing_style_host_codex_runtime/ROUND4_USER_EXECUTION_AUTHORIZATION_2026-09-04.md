# 050 round-4 user execution authorization

This file records explicit user authorization for the bounded round-4 clean-replay work in task `050_writing_style_host_codex_runtime`.

The purpose is to prevent repeated interactive approval prompts for operations that are already necessary to execute the frozen clean-replay contract. This authorization does not expand product scope and does not modify `PLAN.md`.

## Pre-authorized operations

For this task only, the Executor may proceed without asking the user again for each occurrence of the following operations:

1. Start fresh Codex children through the existing Bridge Kit command `ai-bridge plugin-replay`.
   - The child Codex CLI transport may use the normal Codex service transport required by `codex exec`.
   - This is execution substrate, not authorization for `scientific-rewrite`, helper code, a plugin, or a workflow to call OpenAI `/v1/responses` directly.
   - Memories remain disabled and the replay remains bounded by Bridge Kit isolation.

2. Refresh/update the **current** `CODEX_HOME` managed `yuukias-ai-skills` marketplace / `writing-style` installation through the repository's canonical managed install/update mechanism when needed to make the installed plugin match the intended generated plugin snapshot.
   - Do not hand-edit the installed plugin.
   - Do not modify another `CODEX_HOME`.
   - Do not modify unrelated plugins except what the canonical marketplace refresh necessarily updates as part of the same managed source.

3. For the baseline-A diagnostic only, temporarily switch the current managed `yuukias-ai-skills` marketplace/plugin source to a task-local generated snapshot corresponding to the frozen round-3 implementation `bac6bf37ee22b52a2894c90a385dd6ab0e8f0292`, run the clean baseline replay, and then restore the current task/repository marketplace/plugin state.
   - The switch must be reversible.
   - Record before/temporary/after installed identities or hashes.
   - Restoration is mandatory before proceeding to the final repaired A/B/C.
   - If the switch cannot be performed safely and reversibly through the managed plugin mechanism, do not improvise a direct-copy fallback; report the concrete blocker.

4. Copy the already-authorized exact private smoke plaintext into the machine-local Bridge Kit trusted replay inbox using neutral filenames, verify its SHA-256, and use it only as an explicit replay input.
   - Never commit the plaintext.
   - Do not stage diagnosis files, old candidates, role labels, or expected answers into the generation child.

5. Run the required clean replay sequence and local deterministic validation/test/build commands described by the round-4 contract, including three separate fresh A/B/C replay children after the implementation is frozen.

6. Write task-local temporary replay workspaces, local private stage artifacts, and privacy-safe public evidence required by the existing contract.

## Do not ask again for these operations

The Executor should not repeatedly call `request_user_input` for the six categories above. The user's authorization is already recorded here.

A new user question is appropriate only if the next operation is materially outside this authorization, such as:

- destructive Git operations (`reset --hard`, force push, branch deletion, rewriting unrelated history);
- changing another Codex identity / another `CODEX_HOME`;
- exposing private plaintext outside the local authorized replay path;
- direct application/plugin/workflow OpenAI or Terra API generation/review not already authorized by the frozen paid-review contract;
- changing the scientific/product semantics of 050;
- modifying unrelated plugins/projects;
- an irreversible environment mutation for which the canonical managed mechanism cannot provide safe restore.

## Explicit transport boundary

Allowed:

`outer Codex -> ai-bridge plugin-replay -> fresh codex exec child -> installed writing-style`

Not authorized by this file:

`scientific-rewrite/plugin/helper/workflow -> explicit OpenAI API key -> POST /v1/responses`

The former is the intended production replay mechanism. The latter remains forbidden for normal 050 generation.

## Completion boundary

After clean isolated A/B/C are generated from one frozen implementation, stop at the human style gate. Tests, receipts, validators, and the host's own reader-pass decision cannot override the user's `STYLE_ACCEPT` / `STYLE_REJECT` decision.
