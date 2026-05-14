---
name: frontend-motion-interaction
description: "Design and implement frontend motion: page-load choreography, transitions, hover states, scroll effects, feedback animation, and reduced-motion behavior. Use when adding or reviewing animation and interaction polish."
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
# Frontend Motion and Interaction

Motion should clarify structure, provide feedback, or create one memorable moment.
Avoid scattered animation that competes with the interface.

## Motion Strategy

1. Choose the role: orientation, feedback, delight, continuity, or emphasis.
2. Define one primary moment: page load, hero interaction, panel transition, or data reveal.
3. Keep secondary motion quiet.
4. Respect reduced-motion preferences.

## Patterns

- Page load: staggered entrance with short delays and consistent easing.
- Hover: small transform, color, elevation, or reveal tied to affordance.
- Press: immediate tactile feedback.
- Layout transition: preserve spatial continuity.
- Data reveal: animate changes only when it improves comprehension.
- Scroll effects: use sparingly and avoid blocking content access.

## Timing

- Micro-interactions: 120-220ms.
- UI transitions: 180-350ms.
- Large hero moments: 400-800ms when appropriate.
- Use one easing family per interface.

## Implementation

- Prefer CSS transitions for simple effects.
- Use Framer Motion when coordinating React state, route transitions, or complex sequencing.
- Avoid animation that changes layout unexpectedly.
- Provide `prefers-reduced-motion` fallbacks.

## Verification

Confirm animations do not cause jank, obscure text, trap focus, or delay primary tasks.
