# Fresh Longleaf AI Skills Maintainer Normal Entry Replay

Use the installed production plugin `ai-skills-core@yuukias-ai-skills`.

User request to consume through the normal entry:

```text
使用 AI Skills Maintainer，同步这台机器。
```

This is the Longleaf_Codex current-consumer closure check for
`ai-skills-core--machine-update-orchestration`.

Read the input state file and verify the installed AI Skills Maintainer can
route this request through the machine-update orchestrator. Do not install
optional plugins that are not already installed. Do not advance Bridge release.
Do not follow Bridge `origin/main`. Do not modify Bridge source logic.

Return a concise status that states whether the current machine is aligned:

- AI_Skills Marketplace release state;
- installed/enabled AI_Skills plugin versions;
- Bridge runtime/package/source version;
- Bridge checkout identity;
- Host Policy validate state;
- whether any reload/fresh-session boundary remains.
