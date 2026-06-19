# Shared Assets

`shared/` is for repository-level material reused by multiple skills or by the
installer. It is not an install target by itself.

- `templates/AGENTS.md.template`: source template for the managed AGENTS.md
  routing block. `ai-skills validate` checks that it exists, uses `.agents/skills`,
  and contains the managed block markers.
- `reference-packs/frontend-ui-ux/`: shared frontend planning and visual design
  reference data. `skills/tools/frontend/visual-direction` and
  `skills/tools/frontend/product-ux-planning` link here instead of each carrying
  duplicate copies.

Put content here only when at least two skills or one CLI/template path use it.
Otherwise keep references inside the owning skill's `references/` directory.
