---
name: frontend-app-builder
description: Plan and build polished frontend apps from UX intent through visual direction and implementation.
status: active
provenance: generated-codex-marketplace
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
profile_tags:
recommended_scope: project
---

# frontend-app-builder

## Trigger Boundary

Plan and build polished frontend apps from UX intent through visual direction and implementation.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `product-ux-planning`: Plan frontend products before implementation: purpose, audience, information architecture, navigation, user flows, states, content discipline, and feature scope. Use when starting a new app/page, redesigning UX, or reviewing whether a frontend experience is coherent. Reference: `references/source-skills/tools-frontend-product-ux-planning/source-skill.md`
- `visual-direction`: Choose and execute a deliberate frontend visual direction across typography, palette, structure, texture, imagery, and composition. Use when designing or restyling frontend UI and avoiding generic AI-looking output. Reference: `references/source-skills/tools-frontend-visual-direction/source-skill.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source-skill.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
