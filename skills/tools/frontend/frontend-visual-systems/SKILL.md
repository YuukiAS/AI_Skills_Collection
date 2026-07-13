---
name: frontend-visual-systems
description: Convert frontend references and product intent into design tokens, visual direction, palette, typography, icon, layout, density, and motion rules for implementation by a frontend builder.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-07-13
profile_tags:
  - web-development
recommended_scope: project
---
# Frontend Visual Systems

Use this skill to turn research and product intent into an executable visual system.

## Boundary

- Define tokens, density, typography, color, icon strategy, layout rhythm, and interaction tone.
- Do not implement the app; route implementation to the official `build-web-apps` capability or project code workflow.
- Do not rely on decorative blobs, generic purple gradients, or unexplained hero copy.

## Workflow

1. Summarize the product job, audience, and information density.
2. Choose a coherent visual direction and one differentiating move.
3. Define tokens for color, type, spacing, radius, borders, charts, and motion.
4. State responsive and accessibility constraints.
5. Produce a handoff brief that a frontend implementation tool can execute.
