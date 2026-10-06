---
name: frontend-visual-systems
description: Frontend visual direction, product-interface content architecture, Product UI Copy handoff, rendered acceptance, design tokens, typography, palette, icon, layout, density, and motion brief.
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
  - skills/tools/frontend/product-ux-planning
  - skills/tools/frontend/visual-direction
  - skills/tools/frontend/design-system-tokens
  - skills/tools/frontend/figma-design-to-code
  - skills/tools/frontend/motion-interaction
  - skills/tools/frontend/responsive-accessibility-review
  - skills/tools/frontend/webapp-testing
  - skills/tools/frontend/research-product-frontend
icon_small: "assets/codex/app-skill-icons/aggregate.svg"
icon_large: "assets/codex/app-skill-icons/aggregate.svg"
routing_mode: "coordinator-first"
coordinator_artifact_id: "system"
default_prompt:
---

# frontend-visual-systems

## Trigger Boundary

Frontend visual direction, product-interface content architecture, Product UI Copy handoff, rendered acceptance, design tokens, typography, palette, icon, layout, density, and motion brief.

Use this aggregate Codex App skill by entering the coordinator source first.

## Source Workflows

- `frontend-visual-systems` (coordinator): Convert frontend references and product intent into design tokens, visual direction, palette, typography, icon, layout, density, and motion rules for implementation by a frontend builder. Reference: `_src/system/source.md`
- `product-ux-planning` (delegate): Plan frontend products before implementation: purpose, audience, information architecture, navigation, user flows, states, content discipline, and feature scope. Use when starting a new app/page, redesigning UX, or reviewing whether a frontend experience is coherent. Reference: `_src/ux/source.md`
- `visual-direction` (delegate): Choose and execute a deliberate frontend visual direction across typography, palette, structure, texture, imagery, and composition. Use when designing or restyling frontend UI and avoiding generic AI-looking output. Reference: `_src/direction/source.md`
- `design-system-tokens` (delegate): Create or refine frontend design systems: primitive, semantic, and component tokens; CSS variables; Tailwind theme config; typography scales; spacing; component states; brand consistency. Use when making reusable UI systems or aligning multiple screens. Reference: `_src/tokens/source.md`
- `figma-design-to-code` (delegate): Plan Figma-to-code handoff: identify frames, tokens, assets, accessibility risks, and implementation notes that complement official Figma tooling. Reference: `_src/figma/source.md`
- `motion-interaction` (delegate): Design and implement frontend motion: page-load choreography, transitions, hover states, scroll effects, feedback animation, and reduced-motion behavior. Use when adding or reviewing animation and interaction polish. Reference: `_src/motion/source.md`
- `responsive-accessibility-review` (delegate): Review and fix frontend responsiveness, accessibility, usability, keyboard behavior, text fitting, contrast, and visual regressions. Use before shipping UI or when asked to improve UX quality. Reference: `_src/responsive/source.md`
- `webapp-testing` (delegate): Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs. Reference: `_src/webapp-testing/source.md`
- `research-product-frontend` (delegate): Plan high-density research product frontends such as medical imaging viewers, phenotype explorers, model comparison dashboards, provenance tools, and experiment history interfaces. Reference: `_src/research/source.md`

## Workflow

1. Read the coordinator source `_src/system/source.md` first.
2. Let the coordinator classify the task, authority, surface, risk, and required delegates.
3. Load delegate sources only after the coordinator selects them.
4. Return delegate findings to the coordinator for convergence, admission, and final handoff.
5. Follow stricter current-project instructions when they apply.
