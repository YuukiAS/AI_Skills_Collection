---
name: frontend-visual-systems
description: Convert frontend references and product intent into design tokens, visual direction, palette, typography, icon, layout, density, and motion rules for implementation by a frontend builder.
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
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Frontend Visual Systems

Use this skill to turn research and product intent into an executable visual system.

## Boundary

- Define tokens, density, typography, color, icon strategy, layout rhythm, and interaction tone.
- Do not implement the app; route implementation to the official `build-web-apps` capability or project code workflow.
- Do not rely on decorative blobs, generic purple gradients, or unexplained hero copy.
- Do not use academic or journal-inspired palettes from `palette/` as direct UI colors. Product surfaces need semantic tokens; scientific palettes may map only to chart roles.

## Workflow

1. Summarize the product job, audience, and information density.
2. Choose a coherent visual direction and one differentiating move.
3. Translate taste references into concrete constraints: image/reference first, clear hierarchy, disciplined typography, spacing rhythm, contextual brand cues, and purposeful motion.
4. Define tokens for color, type, spacing, radius, borders, charts, and motion.
5. State responsive and accessibility constraints.
6. Produce a handoff brief that a frontend implementation tool can execute.

## Production Frontend Design Gates

Apply these gates before a frontend candidate is described as production-ready,
user-ready, release-ready, or ready for external acceptance.

### F-A Design Authority And State Coverage

Do not force every project into Figma. When a canonical Figma file, design
handoff, product design brief, or other current design source exists, treat it
as production visual authority rather than inspiration. Read the current design
source before coding or reviewing. Material states, variants, responsive
breakpoints, interaction states, and important transitions that will ship need a
design target; if they are missing, close the design-source gap instead of
inventing the state directly in code.

### F-B Design-System Coherence

Use shared component families and tokens for layout, typography, spacing,
radius, surfaces, icon style, and motion. Icons should belong to a coherent
family; motion should clarify state or hierarchy and must respect reduced
motion. Brand/product assets and generic UI chrome must remain visually
consistent. When the frozen product claim includes multiple locales or finite
reachable enums, all user-visible tokens for those locales must be covered;
internal identifiers are not an acceptable production fallback except for
narrowly approved proper names or acronyms.

### F-C Actual-Surface Convergence

Verify the real target surface, not only component snippets or screenshots.
When a canonical design exists, compare complete native screens against the
design source at normal working sizes and record intentional deviations.
Screenshots alone do not prove click, native, provider, persistence, or live
behavior. Producer self-QA should catch obvious hierarchy, spacing, overflow,
translation-token, interaction, and motion defects before external acceptance.

## Quality Bar

- Avoid generic "AI page" tells: undifferentiated purple gradients, oversized cards, weak contrast, random icon mixes, decorative motion, and unsupported hero copy.
- Prefer one strong visual idea over a pile of effects.
- Use screenshot comparison and browser QA to verify hierarchy, density, text fit, responsive behavior, and motion restraint.
