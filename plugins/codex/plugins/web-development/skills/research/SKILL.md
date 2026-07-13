---
name: research-product-frontend
description: High-density research product frontend planning for imaging, phenotype, model comparison, provenance, and experiment interfaces.
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
  - skills/tools/frontend/research-product-frontend
  - skills/tools/frontend/product-ux-planning
default_prompt:
---

# research-product-frontend

## Trigger Boundary

High-density research product frontend planning for imaging, phenotype, model comparison, provenance, and experiment interfaces.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `research-product-frontend`: Plan high-density research product frontends such as medical imaging viewers, phenotype explorers, model comparison dashboards, provenance tools, and experiment history interfaces. Reference: `_src/product/source.md`
- `product-ux-planning`: Plan frontend products before implementation: purpose, audience, information architecture, navigation, user flows, states, content discipline, and feature scope. Use when starting a new app/page, redesigning UX, or reviewing whether a frontend experience is coherent. Reference: `_src/ux/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
