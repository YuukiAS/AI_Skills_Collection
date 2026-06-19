---
name: implementation-react-tailwind
description: Implement production-ready frontend code with React, TypeScript, Tailwind CSS, and shadcn/ui. Use for components, pages, dashboards, forms, tables, navigation, themes, and responsive UI implementation.
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
---
# Frontend Implementation: React and Tailwind

Use existing project conventions first. Add dependencies only when the project
already uses them or the task clearly needs them.

## Stack Defaults

- React + TypeScript for application UI.
- Tailwind CSS for utility styling when present.
- shadcn/ui and Radix primitives for accessible common components when present.
- lucide-react for icons when available.
- Framer Motion only for meaningful animation systems.

## Implementation Rules

- Build the actual usable screen, not a landing page placeholder.
- Keep components scoped and composable.
- Use semantic HTML and accessible labels.
- Use stable layout dimensions for boards, grids, tiles, toolbars, and counters.
- Avoid nested cards and decorative card-heavy layouts for operational tools.
- Use familiar controls: icons for toolbar actions, segmented controls for modes,
  checkboxes/toggles for binary options, sliders/inputs for numeric values.
- Use real data passed by the user or clearly marked sample data.

## Tailwind Patterns

- Keep class composition readable.
- Extract repeated complex patterns into components or helpers.
- Put theme values in CSS variables or Tailwind theme tokens.
- Use responsive constraints such as `minmax`, `aspect-ratio`, `clamp` for layout
  dimensions, and container-aware sizing.

## shadcn/ui Patterns

- Install only the components needed.
- Preserve accessibility behavior from Radix primitives.
- Customize via tokens and variants instead of one-off overrides.
- Confirm dialogs, dropdowns, forms, tables, and command palettes have keyboard states.

## Verification

Run the project formatter/tests when available. For visual work, inspect desktop
and mobile rendering before finalizing.

## References And Utilities

- `references/shadcn-components.md`: component selection and usage notes.
- `references/shadcn-theming.md`: theme customization.
- `references/tailwind-utilities.md`, `tailwind-customization.md`,
  `tailwind-responsive.md`: Tailwind implementation details.
- `scripts/shadcn_add.py`: upstream helper for shadcn component installation.
- `scripts/tailwind_config_gen.py`: upstream helper for Tailwind config generation.
- `references/ui-ux-pro-max-templates/`: upstream implementation templates.
