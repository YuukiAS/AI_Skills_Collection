---
name: responsive-accessibility-review
description: Review and fix frontend responsiveness, accessibility, usability, keyboard behavior, text fitting, contrast, and visual regressions. Use before shipping UI or when asked to improve UX quality.
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
# Frontend Responsive and Accessibility Review

Use this skill as a quality gate for any user-facing UI.

## Responsive Checks

- Test desktop, tablet, mobile, and narrow mobile.
- Ensure text does not overflow controls or cards.
- Stack multi-column layouts when content becomes cramped.
- Replace horizontal dense UI with accordions, tabs, or single-column flows when needed.
- Keep fixed-format elements stable using explicit dimensions or aspect ratios.
- Ensure important content is not hidden below inaccessible scroll areas.

## Accessibility Checks

- Semantic landmarks: header, nav, main, section, aside, footer.
- Labels for inputs, buttons, icon buttons, and controls.
- Visible focus states.
- Keyboard navigation for menus, dialogs, tabs, accordions, and tables.
- Contrast that meets WCAG AA for normal text and controls.
- Error messages tied to fields.
- Reduced-motion fallback for large animations.

## UX Checks

- Standard actions use standard copy.
- Empty, loading, error, and success states exist where relevant.
- Buttons and links have clear affordance.
- Destructive actions require confirmation when the risk is meaningful.
- Dense dashboards support scanning and comparison.
- Product UI Copy is validated in the rendered surface: CTA/action text,
  neighboring explanatory copy, trust/help disclosure, empty/error/loading
  states, and locale-specific strings must fit the actual viewport without
  overlap, clipping, misleading hierarchy, or broken action relationships.

## Production Closure

- Participate in P1 closure when responsiveness, keyboard access, labels,
  contrast, focus management, hit targets, or text fit can block or risk the
  core flow.
- Participate in P3 closure for polish that should improve but does not block
  acceptance.
- Match the surface under review. Browser checks do not prove native-WebView
  behavior unless the claim is explicitly browser-equivalent.
- Report findings as concrete P1/P2/P3 issues tied to the exact screen, state,
  viewport, and evidence.
- When browser-rendered fixtures are used for Product UI Copy evaluation, bind
  the finding to the fixture, viewport, copy source, screenshot, and candidate
  commit. Do not claim native desktop/mobile runtime behavior from browser-only
  evidence.

## Review Output

Lead with concrete issues and file references when reviewing code. For fixes,
make the smallest change that resolves the usability or accessibility problem.

## References

- `references/shadcn-accessibility.md`: accessibility behavior for shadcn/Radix components.
- `references/tailwind-responsive.md`: responsive Tailwind patterns.
- `references/states-and-variants.md`: state and variant coverage.
