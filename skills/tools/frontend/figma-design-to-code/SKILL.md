---
name: figma-design-to-code
description: "Plan Figma-to-code handoff: identify frames, tokens, assets, accessibility risks, and implementation notes that complement official Figma tooling."
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
# Frontend Figma Handoff

Use this skill when a frontend task depends on Figma files, frames, components,
tokens, or design handoff.

Actual Figma file inspection, node edits, asset export, Code Connect, or design generation should use the official Figma capability and its required skill flow. This repository skill only defines the handoff checklist and implementation boundary.

## Workflow

1. Confirm the exact Figma file, page, frame, node IDs, and target implementation stack.
2. Use the official Figma capability to inspect frames, components, styles, variables, and assets.
3. Extract or request design tokens before writing code.
4. Identify reusable project components and variants.
5. Check accessibility concerns such as contrast, text size, hit targets, and hierarchy.
6. Produce implementation notes that preserve design intent while using the project stack and components.
7. Verify the rendered app against the Figma frame.

## Rules

- Do not rely on implicit page context when multiple agents or sessions may be active.
- Use explicit frame/node identifiers when asking the official Figma tooling to inspect or modify Figma.
- Keep Figma tooling separate from general visual-design skills.
- Prefer existing project components over pixel-copying everything.
- Preserve meaningful design intent, not accidental spacing noise.

## Useful Tasks

- Create implementation notes for React/Vue components from selected frames.
- Extract color and typography tokens.
- Audit contrast and hierarchy.
- Prepare safe requests for bulk style updates or asset export through official Figma tooling.
- Create implementation notes for developers.

## References And Utilities

- `references/figma-mcp-readme.md`: workflow overview.
- `references/figma-mcp-commands.md`: available MCP commands.
- `references/figma-mcp-installation.md`: setup details for Cursor, Claude, and other tools.
- `references/figma-mcp-troubleshooting.md`: failure modes and fixes.
- `scripts/`: upstream setup, launcher, and integration test utilities.
