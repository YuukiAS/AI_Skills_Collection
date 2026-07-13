---
name: research-product-frontend
description: Plan high-density research product frontends such as medical imaging viewers, phenotype explorers, model comparison dashboards, provenance tools, and experiment history interfaces.
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
# Research Product Frontend

Use this skill for frontend surfaces where scientific evidence, models, images, or experiment state are central.

## Boundary

- Define domain-specific UI constraints for medical imaging, CMR, phenotype, model, provenance, and statistical evidence interfaces.
- Keep project facts in the project repository; this skill supplies reusable interface patterns.
- Do not build the frontend directly; hand off to `build-web-apps` or project implementation tools.

## Workflow

1. Identify the research object: patient/sample, model, image, phenotype, experiment, paper, or dataset.
2. Define required provenance, uncertainty, units, version, and evidence fields.
3. Choose comparison surfaces: tables, viewers, charts, timelines, panels, or linked detail views.
4. Specify safe defaults for dense scanning, auditability, and repeated expert use.
5. Produce a design brief with data contracts and QA criteria for the implementation step.
