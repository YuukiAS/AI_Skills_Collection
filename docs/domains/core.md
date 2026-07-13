# core

Active skills: 10

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain core --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill core/codex-system/ai-skills-repository-maintainer --skill core/codex-system/codex-workflow-protocol --skill core/codex-system/imagegen --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `ai-skills-repository-maintainer` (`skills/core/codex-system/ai-skills-repository-maintainer`): Maintain AI_Skills_Collection itself: registry, catalog, provenance, marketplace config, generated layer, icons, profiles, and validation gates. Use only when the user is working on this repository or explicitly asks to maintain the central skill collection.
- `codex-workflow-protocol` (`skills/core/codex-system/codex-workflow-protocol`): Use for complex or risky Codex tasks that require source-of-truth discovery, phased planning, specialist routing, gate-driven verification, live-state supervision, integration ownership, or honest final status reporting.
- `imagegen` (`skills/core/codex-system/system-skills/imagegen`): Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts.
- `mcp-builder` (`skills/core/codex-system/mcp-builder`): Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
- `openai-docs` (`skills/core/codex-system/system-skills/openai-docs`): Use for openai docs workflows when the task directly names this tool or domain. Prefer narrower project skills or umbrella retrieval skills when the task is only a lookup.
- `plugin-creator` (`skills/core/codex-system/system-skills/plugin-creator`): Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing.
- `project-skill-installer` (`skills/core/codex-system/project-skill-installer`): Use when the user asks to install, update, or set up skills for the current project. Finds AI_Skills_Collection, runs project-local installation, then reads AGENTS.md.
- `skill-creator` (`skills/core/codex-system/system-skills/skill-creator`): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.
- `skill-installer` (`skills/core/codex-system/system-skills/skill-installer`): Install external Codex skills from curated lists or GitHub repo paths. Use for third-party skill downloads; for AI_Skills_Collection installs prefer ai-skills repo/user targets and treat codex-home as explicit legacy compatibility.
- `skill-library-analysis` (`skills/core/codex-system/skill-library-analysis`): Analyze, deduplicate, cluster, and select skills from a large skill library or cloned upstream sources. Use when maintaining AI_Skills_Collection, comparing external skill repos, or deciding whether to merge, add, archive, or ignore skills.

## Main References

- `skills\core\codex-system\codex-workflow-protocol\references\escalation-rules.md`
- `skills\core\codex-system\codex-workflow-protocol\references\live-state-delegation.md`
- `skills\core\codex-system\codex-workflow-protocol\references\task-template.md`
- `skills\core\codex-system\codex-workflow-protocol\references\verification-matrix.md`
- `skills\core\codex-system\system-skills\imagegen\references\cli.md`
- `skills\core\codex-system\system-skills\imagegen\references\codex-network.md`
- `skills\core\codex-system\system-skills\imagegen\references\image-api.md`
- `skills\core\codex-system\system-skills\imagegen\references\prompting.md`
- `skills\core\codex-system\system-skills\imagegen\references\sample-prompts.md`
- `skills\core\codex-system\system-skills\openai-docs\references\latest-model.md`
- `skills\core\codex-system\system-skills\openai-docs\references\prompting-guide.md`
- `skills\core\codex-system\system-skills\openai-docs\references\upgrade-guide.md`
- `skills\core\codex-system\system-skills\plugin-creator\references\plugin-json-spec.md`
- `skills\core\codex-system\system-skills\skill-creator\references\openai_yaml.md`
