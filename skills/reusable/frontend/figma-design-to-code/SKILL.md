---
name: frontend-figma-design-to-code
description: "Work with Figma design files and MCP workflows: inspect designs, extract tokens/assets, audit accessibility, sync styles, and generate frontend code from Figma context. Use when Figma, design handoff, or design-to-code is involved."
---

# Frontend Figma Design To Code

Use this skill when a frontend task depends on Figma files, frames, components,
tokens, or design handoff.

## Workflow

1. Connect to the Figma MCP/tooling specified by the environment.
2. Inspect the relevant frame, selection, components, styles, and variables.
3. Extract design tokens before writing code.
4. Identify reusable components and variants.
5. Check accessibility concerns such as contrast, text size, hit targets, and hierarchy.
6. Generate code that matches the design while using the project stack and components.
7. Verify the rendered app against the Figma frame.

## Rules

- Do not rely on implicit page context when multiple agents or sessions may be active.
- Use explicit frame/node identifiers when modifying Figma.
- Keep Figma tooling separate from general visual-design skills.
- Prefer existing project components over pixel-copying everything.
- Preserve meaningful design intent, not accidental spacing noise.

## Useful Tasks

- Generate React/Vue components from selected frames.
- Extract color and typography tokens.
- Audit contrast and hierarchy.
- Bulk update styles or colors.
- Export assets.
- Create implementation notes for developers.

## References And Utilities

- `references/figma-mcp-readme.md`: workflow overview.
- `references/figma-mcp-commands.md`: available MCP commands.
- `references/figma-mcp-installation.md`: setup details for Cursor, Claude, and other tools.
- `references/figma-mcp-troubleshooting.md`: failure modes and fixes.
- `scripts/`: upstream setup, launcher, and integration test utilities.
