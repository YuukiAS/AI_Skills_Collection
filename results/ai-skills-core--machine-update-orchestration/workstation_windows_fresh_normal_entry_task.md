# Windows Workstation Fresh Normal Entry

Use the installed production plugin `ai-skills-core@yuukias-ai-skills`.

Normal user request:

```text
使用 AI Skills Maintainer，同步这台机器。
```

This is a read-only fresh-process acceptance check after the authorized machine
refresh. Do not mutate Marketplace sources, plugin installation, Git refs,
Bridge refs, Bridge runtime/source, Host Policy, project consumers, or unrelated
repositories. Do not call paid APIs.

Read the provided public machine-state input and the installed production plugin
snapshot. Verify and report:

- whether installed `ai-skills-core@yuukias-ai-skills` was actually loaded;
- whether the normal request routes to `machine-update-orchestrator`;
- the installed `ai-skills-core` version and production plugin path if visible;
- whether the supplied Marketplace revision matches the supplied formal release;
- whether every supplied installed AI_Skills plugin is at its formal version;
- whether supplied optional plugins remain uninstalled;
- whether Bridge is aligned with its formal release runtime content;
- whether Host Policy is configured;
- the final user-facing state for this already refreshed machine.

Do not substitute a source-tree `SKILL.md` read for production plugin loading.
