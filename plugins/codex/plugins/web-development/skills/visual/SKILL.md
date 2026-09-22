---
name: frontend-visual-systems
description: Frontend visual direction, design tokens, typography, palette, icon, layout, density, and motion brief.
status: active
provenance: generated
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/tools/frontend/frontend-visual-systems
  - skills/tools/frontend/visual-direction
  - skills/tools/frontend/design-system-tokens
  - skills/tools/frontend/figma-design-to-code
  - skills/tools/frontend/motion-interaction
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
default_prompt:
---

# frontend-visual-systems

## Trigger Boundary

Frontend visual direction, design tokens, typography, palette, icon, layout, density, and motion brief.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `frontend-visual-systems`: Convert frontend references and product intent into design tokens, visual direction, palette, typography, icon, layout, density, and motion rules for implementation by a frontend builder. Reference: `_src/system/source.md`
- `visual-direction`: Choose and execute a deliberate frontend visual direction across typography, palette, structure, texture, imagery, and composition. Use when designing or restyling frontend UI and avoiding generic AI-looking output. Reference: `_src/direction/source.md`
- `design-system-tokens`: Create or refine frontend design systems: primitive, semantic, and component tokens; CSS variables; Tailwind theme config; typography scales; spacing; component states; brand consistency. Use when making reusable UI systems or aligning multiple screens. Reference: `_src/tokens/source.md`
- `figma-design-to-code`: Plan Figma-to-code handoff: identify frames, tokens, assets, accessibility risks, and implementation notes that complement official Figma tooling. Reference: `_src/figma/source.md`
- `motion-interaction`: Design and implement frontend motion: page-load choreography, transitions, hover states, scroll effects, feedback animation, and reduced-motion behavior. Use when adding or reviewing animation and interaction polish. Reference: `_src/motion/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
