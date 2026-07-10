---
name: frontend-testing-debugging
description: Test and debug rendered frontend apps with browser automation, responsive checks, and accessibility review.
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
  - skills/tools/frontend/webapp-testing
  - skills/tools/frontend/responsive-accessibility-review
---

# frontend-testing-debugging

## Trigger Boundary

Test and debug rendered frontend apps with browser automation, responsive checks, and accessibility review.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `webapp-testing`: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs. Reference: `references/source-skills/tools-frontend-webapp-testing/source-skill.md`
- `responsive-accessibility-review`: Review and fix frontend responsiveness, accessibility, usability, keyboard behavior, text fitting, contrast, and visual regressions. Use before shipping UI or when asked to improve UX quality. Reference: `references/source-skills/tools-frontend-responsive-accessibility-review/source-skill.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source-skill.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
