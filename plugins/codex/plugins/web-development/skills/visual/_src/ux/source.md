---
name: product-ux-planning
description: "Plan frontend products before implementation: purpose, audience, information architecture, navigation, user flows, states, content discipline, and feature scope. Use when starting a new app/page, redesigning UX, or reviewing whether a frontend experience is coherent."
status: active
provenance: unknown
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-05-14
profile_tags:
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Frontend Product UX Planning

Use this skill before visual styling or implementation when the task involves a
page, app, dashboard, workflow, landing page, or product surface.

## Workflow

1. Define the product job in one sentence.
2. Identify the audience, domain, frequency of use, and content density.
3. Map the primary workflow, secondary workflows, and handoff actions.
4. Choose the first screen by user intent, not by marketing convention.
5. List required states: empty, loading, error, success, permission, offline, long-content, and small-screen.
6. Define actionability and lifecycle rules: what is visible, enabled, disabled, pending, destructive, or user-only.
7. Decide what information must be real, user-provided, or clearly sample.
8. Remove filler copy, decorative labels, fake telemetry, and themed wording for standard actions.

## Ownership

- Own the P0 product/state contract before visual styling or implementation.
- Distinguish normal user flows from diagnostics, admin-only tools, and developer-only recovery surfaces.
- For visible metrics, rankings, model scores, provenance, and status values, require a durable semantic source; do not let UI styling invent unsupported numbers or priority claims.
- When a UI action will be handed to the user, define the expected next state or the safe user-only boundary so the coordinator can verify reachability.

## Output Standard

- Navigation is predictable and supports moving in and out of major views.
- Standard actions use standard labels.
- Screens show meaningful content, not ornamental status text.
- Dashboards and operational tools prioritize scanning, comparison, and repeated action.
- Marketing pages make the product, object, place, or offer visible in the first viewport.

## Handoff

After planning, route to:

- the Frontend Design coordinator for delegate selection and admission;
- `visual-direction` for whole-screen direction;
- `design-system-tokens` for reusable tokens;
- the implementation builder only after the coordinator has accepted the product/design contract.
