# Skills Directory

`skills/` is the callable workflow library. A directory should contain a
`SKILL.md` only when an agent can directly decide to use it for a concrete task.

## What Should Be A Skill

- A repeatable workflow with clear triggers and boundaries.
- A tool or library workflow users directly name, such as `scanpy`, `pydicom`,
  `PyMC`, `pptx`, or React/Tailwind implementation.
- A project-specific workflow with local conventions, such as CardiacNexus
  pipeline refactors.
- A system workflow used by the installer or skill maintenance profiles.

## What Should Not Be A Skill

- Provider notes for one database endpoint when an umbrella retrieval workflow
  can route to it.
- Static templates, schemas, palettes, prompt fragments, or long reference
  packs.
- Low-frequency documentation that is only read from another skill.
- Multiple copies of the same UI/UX, platform, or API reference content.

Move non-callable material to `shared/`, `palette/`, or a skill-local
`references/` directory. If a previous skill must be retained for migration,
mark it with `status: archived`; normal profiles and the default registry must
not include archived skills.

## Top-Level Buckets

- `reusable/`: cross-project workflows.
- `research/`: writing, discovery, ideation, and communication workflows.
- `domain/`: field-specific workflows.
- `project/`: repo-specific workflows.
- `system/`: installer, Codex, plugin, MCP, and skill authoring workflows.

Descriptions are discovery triggers, not tutorials. Keep frontmatter
`description` under 350 characters and put details in the body or references.
