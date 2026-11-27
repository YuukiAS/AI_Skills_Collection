---
name: design-system-tokens
description: "Create or refine frontend design systems: primitive, semantic, and component tokens; CSS variables; Tailwind theme config; typography scales; spacing; component states; brand consistency. Use when making reusable UI systems or aligning multiple screens."
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
# Frontend Design System Tokens

Use this skill when design choices need to scale across components, pages, or
applications.

## Token Architecture

Use three layers:

1. Primitive tokens: raw values such as color ramps, spacing steps, font sizes.
2. Semantic tokens: purpose aliases such as background, foreground, primary, muted.
3. Component tokens: button, card, input, table, nav, chart, and dialog values.

For product or UI color, use semantic tokens rather than direct academic
palette ids. Scientific palettes from `palette/` may be referenced only after
mapping them into chart/data-visualization tokens with clear roles.

## Required Token Groups

- Color: background, foreground, muted, border, primary, secondary, accent, danger, success, warning.
- Typography: display, body, mono, weights, line heights, tracking.
- Spacing: page, section, stack, inline, control, grid gap.
- Radius: control, card, modal, media.
- Shadow/elevation: use sparingly and consistently.
- Motion: duration, easing, stagger, reduced-motion alternative.
- State: hover, focus, active, disabled, selected, loading, invalid.

## Tailwind Guidance

- Prefer CSS variables as source of truth.
- Map Tailwind utilities to semantic tokens.
- Avoid hardcoded hex values inside components unless prototyping.
- Keep dark mode semantic, not a duplicate pile of component overrides.

## Component Specs

For shared components, define:

- Anatomy and slots.
- Props and variants.
- Interaction states.
- Accessibility requirements.
- Responsive behavior.
- Token dependencies.

## Ownership

- Own semantic typography, color, surface, border, status, spacing, state, and
  component grammar once the coordinator has accepted the product/design route.
- For icons, preserve source authority: prefer canonical platform/component
  sources, separate brand marks from generic UI icons, keep a central registry
  or component path when the project has one, normalize optical size/stroke, and
  record third-party source, license, and provenance when external assets are
  used.
- Component and icon repairs must preserve accessibility, theme behavior,
  hover/focus/disabled states, and reduced-motion expectations.
- Do not treat a token update as authority to change product meaning, Figma
  intent, or actual-surface evidence requirements; return those gaps to the
  coordinator.

## Output

Provide code-ready tokens plus short usage guidance. If an existing design system
is present, extend it instead of replacing it.

## References And Utilities

- `references/token-architecture.md`: three-layer token model.
- `references/primitive-tokens.md`, `semantic-tokens.md`, `component-tokens.md`:
  detailed token specs.
- `references/tailwind-integration.md`: Tailwind mapping.
- `scripts/generate-tokens.cjs`, `validate-tokens.cjs`, `embed-tokens.cjs`:
  upstream token utilities.
- `templates/design-tokens-starter.json`: starter token file.
