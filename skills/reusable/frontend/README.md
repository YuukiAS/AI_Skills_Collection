# Frontend Skills

This directory is organized as a direct skill registry for Cursor, Codex, and
other coding agents. Each top-level folder is a standalone skill.

Original upstream repositories and prompt fragments have been integrated into
the relevant skill folders as `references/`, `scripts/`, or `templates/`.

## Curated Skill Architecture

- `product-ux-planning/`: product intent, information architecture, flows, states, content discipline.
- `visual-direction/`: aesthetic direction, typography, palette, layout language, anti-generic design.
- `design-system-tokens/`: brand tokens, CSS variables, Tailwind themes, component specs.
- `implementation-react-tailwind/`: React, TypeScript, Tailwind, shadcn/ui, responsive implementation.
- `responsive-accessibility-review/`: mobile behavior, WCAG, keyboard states, usability review.
- `motion-interaction/`: animation systems, page-load choreography, micro-interactions, reduced motion.
- `figma-design-to-code/`: Figma MCP workflows, design inspection, handoff, sync, and code generation.
- `brand-creative-assets/`: brand identity, banners, slides, social assets, icons, and marketing visuals.
- `webapp-testing/`: browser automation, console inspection, static HTML automation, and local server testing helpers.

## Integration Notes

- Duplicate and overlapping source skills were not kept as separate triggerable
  skills. Their useful guidance was integrated into the topical skills.
- Long source references from UI/UX Pro Max, design-system, ui-styling, brand,
  banner, slides, and Figma MCP were preserved under the closest matching skill.
- Figma MCP remains a separate skill because it is a tool workflow, not a
  general visual design rule set.

## Recommended Consumption

Register this `frontend/` directory directly. The root contains only curated
skill folders plus this README.
