# Public Input: Central Plugin Maintenance Closure

The current maintenance task changes two central plugins: `workflow-core` and `ai-skills-core`. It also regenerates the corresponding Codex plugin payloads and updates the repository version and plugin changelogs.

The user-facing behavior change is workflow control-plane behavior: semantic task keys, human-label separation, regression-bank-first capability gates, narrow-gate eligibility, broad/full fallback triggers, and final-candidate evidence binding.

The task should bump `workflow-core` from `0.1` to `0.2`, bump `ai-skills-core` from `0.2` to `0.3`, and bump the repository from `5.0.5` to `5.0.6`. Other plugins should remain unchanged.

Replay evidence proves candidate plugin loading and normal skill consumption. It does not replace source/generated parity checks, deterministic tests, release version/changelog consistency, or independent implementation review.
