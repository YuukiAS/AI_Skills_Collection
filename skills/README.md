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

- `domains/`: complete field collections that can be installed whole, such as
  `bayesian`, `bioinformatics`, `medical-imaging`, and `medicine-clinical`.
- `tools/`: cross-project tool families such as data science, frontend,
  document/media processing, visualization, and AI/ML libraries.
- `writing/`: first-class writing workflows. `writing/core/` is suitable for
  global guardrails; `writing/research/` is heavier and usually project-scoped.
- `science/`: research discovery, ideation, communication, and presentation
  workflows that are not themselves writing-style guardrails.
- `projects/`: repo- or product-specific workflows, such as CardiacNexus/CMR.
- `core/`: skill library maintenance, installer support, and Codex system
  compatibility workflows.
- `archive/`: retained material that should not appear in the default active
  registry, including external integration snapshots and misfit experiments.

Descriptions are discovery triggers, not tutorials. Keep frontmatter
`description` under 350 characters and put details in the body or references.

## Local-Only Folders

Ignore dot-prefixed local folders such as `.system/` when browsing the library.
They are not part of the installable taxonomy and should not be added to
profiles, bundles, or the generated registry.
