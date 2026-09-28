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
- Act as the normal Frontend Design coordinator for production UI work. Classify the task before choosing delegates.
- Do not implement the app; route implementation to the official `build-web-apps` capability or project code workflow.
- Do not rely on decorative blobs, generic purple gradients, or unexplained hero copy.
- Do not use academic or journal-inspired palettes from `palette/` as direct UI colors. Product surfaces need semantic tokens; scientific palettes may map only to chart roles.

## Workflow

1. P0 product/state contract: summarize the product job, primary states, user actions, and target surface.
2. P1 design authority and direction: identify canonical Figma, another durable authority, or current production grammar for a narrow fix; choose the visual direction and delegate only where needed.
3. P2 implementation handoff: translate the accepted direction into concrete tokens, components, states, assets, motion, and implementation notes.
4. P3 actual-surface convergence: verify the rendered browser or native-WebView surface that the claim is about; record P1/P2/P3 findings against the exact candidate.
5. P4 whole-product taste: ask observable taste questions and require independent confirmation for substantive redesign, release gates, major canonical-design convergence, major native user-flow milestones, or whole-product hierarchy/interaction-model changes.

Scale the work before delegating:

- S1 targeted/local fix: use existing production grammar; do not force Figma, full redesign, or independent review unless the fix exposes a larger product/design gap.
- S2 bounded UI change: extend only the affected states, components, and authority source.
- S3 product/redesign: run the full P0-P4 loop.

Design authority and surface are modifiers, not size classes. Figma is conditional authority, not mandatory. Browser evidence proves browser behavior; native-WebView claims need native evidence or a clearly bounded user-only stop.

Delegate ownership:

- `product-ux-planning`: product job, primary states, actionability, lifecycle, normal-vs-diagnostic boundary, visible metric/ranking semantics.
- `visual-direction`: whole-screen direction, composition, differentiator, and observable taste questions.
- `design-system-tokens`: component craft, icon source/registry/provenance, semantic typography, color, status, state, and token grammar.
- `figma-design-to-code`: canonical Figma authority, completeness, round-trip, and final design/render convergence.
- `motion-interaction`: motion intent and the boundary between design motion and runtime latency or jank.
- `responsive-accessibility-review`: applicable P1 accessibility/responsive constraints and P3 closure.
- `webapp-testing`: browser evidence companion for F-C; not a native or design authority.
- `research-product-frontend`: research-specific UI constraints after this coordinator has classified the generic product/design route.

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

### F-D Producer Admission And Handoff Reachability

Producer self-QA is admission to independent review or user handoff, not an
independent quality proof. Bind `P1=0/P2=0` to the exact candidate, surface,
state, and evidence. If the final report asks the user to click, select, expand,
save, or authorize a UI control and the producer can safely exercise it, verify
that the control is visible, enabled, triggered by real interaction, reaches the
expected next state or user-only boundary, and has no obvious P2 defect.

Classify defects before repair:

- Design defect: return to P0/P1 and the relevant authority/delegate.
- Implementation drift: repair the implementation without changing the design source.
- Product semantic defect: return to product UX/state semantics.
- Runtime-only repair: fix runtime behavior while preserving accepted design intent.

Interaction causality belongs to F-C. Ordinary browser locator/actionability
plus a postcondition is enough unless there is a competing route or control-path
claim; then prove the specific route.

## Quality Bar

- Avoid generic "AI page" tells: undifferentiated purple gradients, oversized cards, weak contrast, random icon mixes, decorative motion, and unsupported hero copy.
- Prefer one strong visual idea over a pile of effects.
- Use screenshot comparison and browser QA to verify hierarchy, density, text fit, responsive behavior, and motion restraint.
- Whole-product taste is observable judgment: ask whether hierarchy, density,
  motion, iconography, affordances, copy placement, and state transitions feel
  coherent in the actual screen, not whether a checklist keyword appears.
