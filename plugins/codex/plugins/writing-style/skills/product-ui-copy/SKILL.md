---
name: product-ui-copy
description: Natural product-interface microcopy for labels, CTAs, states, help text, onboarding, settings, trust/privacy disclosures, landing-page interface copy, and locale-specific UI wording under frozen product meaning. Use for browser extension, web, desktop/WebView, mobile, and app surfaces after product semantics and UI role are known.
status: active
provenance: user-authored
trusted: false
requires_network: false
writes_files: true
executes_code: false
secrets_needed:
last_reviewed: 2026-09-29
profile_tags:
  - writing
  - frontend
recommended_scope: project
icon_small: assets/app-facing.svg
icon_large: assets/app-facing.svg
---
# Product UI Copy

Use this skill for short user-facing product-interface copy: labels, buttons,
calls to action, empty/loading/error/success states, settings text, onboarding,
help text, trust/privacy disclosure, permission prompts, landing-page interface
blocks, and other copy that appears inside a product surface.

This is not the long-form Chinese prose route. Reports, README files,
technical notes, scientific explanations, and ordinary Chinese document
polishing stay with `chinese-prose` or `scientific-rewrite` as appropriate.

## Ownership

Product/domain/legal authority owns product truth:

- availability and eligibility;
- current product state;
- user consequence and next action;
- payment, subscription, pricing, cancellation, deletion, retention, consent,
  privacy, safety, and trust facts;
- exact product, brand, feature, technical, and policy identities.

Frontend Design owns content architecture:

- whether text belongs on the surface;
- placement, amount, hierarchy, neighboring copy, duplicate payload, and
  progressive disclosure;
- final rendered page or screen rhythm.

Product UI Copy owns wording under frozen meaning:

- concise natural wording;
- locale/register;
- first-pass linguistic page rhythm;
- preserving or escalating protected meaning.

If product truth or legal/trust meaning is missing, do not invent it. Return a
clear escalation instead of a polished guess.

## Required Handoff

When receiving work from Frontend Design, expect this lightweight handoff:

```text
SURFACE:
UI_ROLE:
PRODUCT_STATE:
USER_JOB:
USER_CONSEQUENCE_OR_NEXT_ACTION:
NEIGHBORING_VISIBLE_COPY:
LOCALE:
PROTECTED_MEANING:
DISCLOSURE_LEVEL:
LENGTH_OR_VIEWPORT_CONSTRAINT:
DESIGN_AUTHORITY: optional
TERMINOLOGY_OR_BRAND_TOKENS: optional
```

Do not turn this handoff into a schema, database, ledger, or state machine.

## Decision Classes

Use these labels as reasoning structure when they help keep ownership clear:

- `KEEP`: the current copy is already clear and should not be rewritten just to
  show activity.
- `WORDING/NATURALNESS`: wording can be improved without changing meaning.
- `LOCALE/REGISTER`: the same protected meaning needs locale-specific wording.
- `CONTENT ARCHITECTURE`: Frontend should adjust placement, amount, hierarchy,
  disclosure, or neighboring text before wording is final.
- `PRODUCT SEMANTICS`: product truth, state, eligibility, consequence, or
  reversibility is missing or inconsistent.
- `LEGAL/TRUST/SAFETY`: consent, privacy, retention, deletion, safety, pricing,
  visibility to others/systems, or trust claims need product/domain/legal
  authority.

## Locale

`zh-Hans` and `zh-Hant-HK` are independent realizations from one protected
meaning. Character conversion alone is not localization.

For `zh-Hant-HK`, prefer Hong Kong user-facing wording and register where it is
meaningfully different. Preserve exact product names, feature names, technical
tokens, and policy terms that must match the product.

## Workflow

1. Confirm the handoff or prompt includes enough product truth to write safely.
2. Classify each requested line as `KEEP`, wording, locale, content
   architecture, product semantics, or legal/trust/safety.
3. Mark protected meaning before rewriting. Do not change user consequence,
   eligibility, privacy/safety/trust meaning, pricing, reversibility, or exact
   product identity.
4. Produce the smallest set of copy changes that improves the interface.
5. For locales, realize the same protected meaning independently for the
   target locale.
6. Return unresolved product/legal/trust questions explicitly.
7. Ask Frontend Design to validate final rendered rhythm when layout, viewport,
   density, or neighboring copy can change meaning or readability.

## Output Standard

- Short copy sounds like a product surface, not a report, audit log, or
  internal implementation note.
- Buttons use action verbs that match the real consequence.
- Help and trust text says what the product actually does and does not hide
  missing facts.
- Empty/error/loading/success states tell the user what happened and what they
  can do next.
- Already-good copy can remain unchanged.
- The copy does not over-explain just because there is available space.
- The result makes clear which owner must act next when wording is blocked by
  missing product truth or content architecture.

## Red Flags

- A UI request routes to long-form `chinese-prose` just because the text is
  Chinese.
- Wording hides unresolved privacy, legal, safety, payment, deletion, or
  visibility semantics.
- The copy changes an action consequence from reversible to final, public to
  private, optional to required, or diagnostic to user-facing.
- A locale version is only character conversion.
- All lines are rewritten even when some should be `KEEP`.
- Frontend layout or disclosure decisions are presented as Writing decisions.
- A backend/API/docs-only request activates this skill without a product
  interface surface.
