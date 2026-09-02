# 048 ai-skills-core Production Maintenance Replay

You are running a public-safe production replay for AI_Skills_Collection task `048_writing_style_product_cutover_and_readable_report`.

Use the installed production plugin named `ai-skills-core`. Do not edit files, do not access private plaintext, and do not print secrets.

Inputs:

- `replay_identity.json`

Task:

1. Read the input identity file.
2. Use the `ai-skills-core` repository maintainer / maintenance companion behavior to inspect whether the identity describes a valid AI_Skills_Collection plugin refinement handoff.
3. Check that the task remains inside the `writing-style` plugin boundary and that `presentations` is not part of the requested implementation scope.
4. Return a concise public-safe JSON object with:
   - `status`;
   - `plugin_selector`;
   - `maintenance_skill_observed`;
   - `task_key`;
   - `writing_style_identity_observed`;
   - `presentations_scope_allowed`;
   - `private_plaintext_requested`;
   - `findings`.

Expected result: this is a preflight/replay evidence run only. It must not claim final Product PASS or user ACCEPT.
