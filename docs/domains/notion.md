# notion

Active skills: 14

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain notion --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill create-database-row --skill create-page --skill create-task --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `create-database-row` (`skills/reusable/notion/notion-workspace-skills-codex/create-database-row`): Insert a new row into a specified Notion database using natural-language property values. Handles property name matching and validation.
- `create-page` (`skills/reusable/notion/notion-workspace-skills-codex/create-page`): Create a new Notion page, optionally under a specific parent. Automatically structures content based on page type (meeting notes, project pages, etc.).
- `create-task` (`skills/reusable/notion/notion-workspace-skills-codex/create-task`): Create a new task in the user's Notion tasks database with sensible defaults for due date, status, owner, and project.
- `database-query` (`skills/reusable/notion/notion-workspace-skills-codex/database-query`): Query a Notion database by name or ID and return structured, readable results with optional filters and sorting.
- `find` (`skills/reusable/notion/notion-workspace-skills-codex/find`): Quickly find pages or databases in Notion by title keywords. Returns precise matches rather than comprehensive results.
- `knowledge-capture` (`skills/reusable/notion/notion-workspace-skills-codex/knowledge-capture`): Transform conversations and discussions into structured documentation pages in Notion. Captures insights, decisions, and knowledge from chat context with proper organization and linking.
- `meeting-intelligence` (`skills/reusable/notion/notion-workspace-skills-codex/meeting-intelligence`): Prepare meeting materials by gathering context from Notion, enriching with research, and creating both an internal pre-read and external agenda saved to Notion.
- `research-documentation` (`skills/reusable/notion/notion-workspace-skills-codex/research-documentation`): Search across your Notion workspace, synthesize findings from multiple pages, and create comprehensive research documentation with proper citations and actionable insights.
- `search` (`skills/reusable/notion/notion-workspace-skills-codex/search`): Search the user's Notion workspace using the Notion MCP server. Use for finding pages, databases, and content by keywords or natural-language queries.
- `spec-to-implementation` (`skills/reusable/notion/notion-workspace-skills-codex/spec-to-implementation`): Turn product or tech specs into concrete Notion tasks. Breaks down spec pages into detailed implementation plans with clear tasks, acceptance criteria, and progress tracking.
- `tasks-build` (`skills/reusable/notion/notion-workspace-skills-codex/tasks-build`): Build a task from a Notion page URL. Fetches task details, marks it in progress, implements the work, and updates status in Notion.
- `tasks-explain-diff` (`skills/reusable/notion/notion-workspace-skills-codex/tasks-explain-diff`): Generate a rich Notion document explaining code changes. Creates comprehensive documentation with background, intuition, code walkthrough, and verification steps.
- `tasks-plan` (`skills/reusable/notion/notion-workspace-skills-codex/tasks-plan`): Create an implementation plan from a Notion task or specification. Breaks down requirements into actionable steps with estimates and dependencies.
- `tasks-setup` (`skills/reusable/notion/notion-workspace-skills-codex/tasks-setup`): Set up a Notion task board for tracking tasks. Guides users through using a template or connecting an existing board.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
