---
name: frontend-visual-direction
description: Choose and execute a deliberate frontend visual direction across typography, palette, structure, texture, imagery, and composition. Use when designing or restyling frontend UI and avoiding generic AI-looking output.
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
# Frontend Visual Direction

Commit to one coherent direction before coding. Do not blend incompatible styles
unless the user explicitly asks for an exploratory moodboard.

## Decision Pass

1. Purpose: what the interface does.
2. Audience: who uses it and how often.
3. Context: product category, content density, brand constraints, platform.
4. Direction: choose one recognizable aesthetic territory.
5. Differentiator: define one visible memorable move.

## Direction Families

- Swiss: white or neutral surfaces, sans typography, grid rules, strong alignment.
- Industrial: black surfaces, monospace typography, flat borders, tabular numerics.
- Brutalist: raw defaults, primary colors, hard shadows, visible browser controls.
- Editorial: expressive type hierarchy, magazine grid, strong image and text rhythm.
- Organic: earth tones, humanist type, rounded forms, subtle texture.
- Retro-futuristic: dark surfaces, neon accents, scanlines or glow, period typography.
- Luxury: restrained palette, premium typography, careful spacing, subtle motion.
- Maximalist: deliberate density, pattern, color collision, oversized typography.

## Rules

- Use CSS variables for palette, type, spacing, radius, shadow, and motion.
- Avoid default-looking stacks unless the chosen style requires them.
- Avoid purple-blue gradient defaults unless the brief truly calls for them.
- Do not use decorative text to imply functionality.
- Use real visual assets for websites and landing pages when assets matter.
- Keep palette, typography, surface, and layout mutually consistent.

## Verification

Before shipping, inspect whether:

- The chosen direction is visible without explanation.
- The differentiator exists in the rendered UI.
- Tokens do not drift into another style.
- Text fits on mobile and desktop.
- UI controls remain familiar and usable.

## References

Load files from `references/` only when needed:

- `frontend-design-eight-anchors.md`: strict visual anchor system.
- `frontend-design-anthropic-like.md`: broad anti-generic frontend guidance.
- `distinctive-frontend-design.md`: typography, color, motion, and background patterns.
- `frontend-design-ultimate.md`: React/Tailwind static-site workflow and mobile patterns.
- `../../../../shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/`:
  shared style, palette, product, and stack data.
