---
name: frontend-product-ux-planning
description: "Plan frontend products before implementation: purpose, audience, information architecture, navigation, user flows, states, content discipline, and feature scope. Use when starting a new app/page, redesigning UX, or reviewing whether a frontend experience is coherent."
---

# Frontend Product UX Planning

Use this skill before visual styling or implementation when the task involves a
page, app, dashboard, workflow, landing page, or product surface.

## Workflow

1. Define the product job in one sentence.
2. Identify the audience, domain, frequency of use, and content density.
3. Map the primary workflow and the secondary workflows.
4. Choose the first screen by user intent, not by marketing convention.
5. List required states: empty, loading, error, success, permission, offline, long-content, and small-screen.
6. Decide what information must be real, user-provided, or clearly sample.
7. Remove filler copy, decorative labels, fake telemetry, and themed wording for standard actions.

## Output Standard

- Navigation is predictable and supports moving in and out of major views.
- Standard actions use standard labels.
- Screens show meaningful content, not ornamental status text.
- Dashboards and operational tools prioritize scanning, comparison, and repeated action.
- Marketing pages make the product, object, place, or offer visible in the first viewport.

## Handoff

After planning, route to:

- `frontend-visual-direction` for the visual system.
- `frontend-design-system-tokens` for reusable tokens.
- `frontend-implementation-react-tailwind` for production code.
