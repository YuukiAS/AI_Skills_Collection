# frontend

Active skills: 9

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain frontend --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill tool/frontend/brand-creative-assets --skill tool/frontend/design-system-tokens --skill tool/frontend/figma-design-to-code --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `brand-creative-assets` (`skills/tools/frontend/brand-creative-assets`): Create and review brand-related frontend assets: brand identity, visual guidelines, banners, hero visuals, slides, social images, icons, and marketing creative. Use for branded campaigns and visual asset systems.
- `design-system-tokens` (`skills/tools/frontend/design-system-tokens`): Create or refine frontend design systems: primitive, semantic, and component tokens; CSS variables; Tailwind theme config; typography scales; spacing; component states; brand consistency. Use when making reusable UI systems or aligning multiple screens.
- `figma-design-to-code` (`skills/tools/frontend/figma-design-to-code`): Work with Figma design files and MCP workflows: inspect designs, extract tokens/assets, audit accessibility, sync styles, and generate frontend code from Figma context. Use when Figma, design handoff, or design-to-code is involved.
- `implementation-react-tailwind` (`skills/tools/frontend/implementation-react-tailwind`): Implement production-ready frontend code with React, TypeScript, Tailwind CSS, and shadcn/ui. Use for components, pages, dashboards, forms, tables, navigation, themes, and responsive UI implementation.
- `motion-interaction` (`skills/tools/frontend/motion-interaction`): Design and implement frontend motion: page-load choreography, transitions, hover states, scroll effects, feedback animation, and reduced-motion behavior. Use when adding or reviewing animation and interaction polish.
- `product-ux-planning` (`skills/tools/frontend/product-ux-planning`): Plan frontend products before implementation: purpose, audience, information architecture, navigation, user flows, states, content discipline, and feature scope. Use when starting a new app/page, redesigning UX, or reviewing whether a frontend experience is coherent.
- `responsive-accessibility-review` (`skills/tools/frontend/responsive-accessibility-review`): Review and fix frontend responsiveness, accessibility, usability, keyboard behavior, text fitting, contrast, and visual regressions. Use before shipping UI or when asked to improve UX quality.
- `visual-direction` (`skills/tools/frontend/visual-direction`): Choose and execute a deliberate frontend visual direction across typography, palette, structure, texture, imagery, and composition. Use when designing or restyling frontend UI and avoiding generic AI-looking output.
- `webapp-testing` (`skills/tools/frontend/webapp-testing`): Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

## Main References

- `skills/tools/frontend/brand-creative-assets/references/approval-checklist.md`
- `skills/tools/frontend/brand-creative-assets/references/asset-organization.md`
- `skills/tools/frontend/brand-creative-assets/references/banner-sizes-and-styles.md`
- `skills/tools/frontend/brand-creative-assets/references/brand-guideline-template.md`
- `skills/tools/frontend/brand-creative-assets/references/cip-deliverable-guide.md`
- `skills/tools/frontend/design-system-tokens/references/component-specs.md`
- `skills/tools/frontend/design-system-tokens/references/component-tokens.md`
- `skills/tools/frontend/design-system-tokens/references/primitive-tokens.md`
- `skills/tools/frontend/design-system-tokens/references/semantic-tokens.md`
- `skills/tools/frontend/design-system-tokens/references/states-and-variants.md`
- `skills/tools/frontend/figma-design-to-code/references/figma-mcp-commands.md`
- `skills/tools/frontend/figma-design-to-code/references/figma-mcp-installation.md`
- `skills/tools/frontend/figma-design-to-code/references/figma-mcp-readme.md`
- `skills/tools/frontend/figma-design-to-code/references/figma-mcp-testing.md`
- `skills/tools/frontend/figma-design-to-code/references/figma-mcp-troubleshooting.md`
- `skills/tools/frontend/implementation-react-tailwind/references/canvas-design-system.md`
- `skills/tools/frontend/implementation-react-tailwind/references/shadcn-accessibility.md`
- `skills/tools/frontend/implementation-react-tailwind/references/shadcn-components.md`
- `skills/tools/frontend/implementation-react-tailwind/references/shadcn-theming.md`
- `skills/tools/frontend/implementation-react-tailwind/references/tailwind-customization.md`
- `skills/tools/frontend/product-ux-planning/references/ui-ux-pro-max-source-skill.md`
- `skills/tools/frontend/responsive-accessibility-review/references/shadcn-accessibility.md`
- `skills/tools/frontend/responsive-accessibility-review/references/states-and-variants.md`
- `skills/tools/frontend/responsive-accessibility-review/references/tailwind-responsive.md`
- `skills/tools/frontend/visual-direction/references/distinctive-frontend-design.md`
- `skills/tools/frontend/visual-direction/references/frontend-design-anthropic-like.md`
- `skills/tools/frontend/visual-direction/references/frontend-design-eight-anchors-duplicate.md`
- `skills/tools/frontend/visual-direction/references/frontend-design-eight-anchors.md`
- `skills/tools/frontend/visual-direction/references/frontend-design-ultimate.md`
