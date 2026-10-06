# Presentations Core TODO — History Preflight and Accepted-Page Locks

Status: PROMOTE_NOW  
Source: repeated STAT5060 Tutorial 01 revisions through V08  
Detailed specification:
`docs/design/PRESENTATIONS_HISTORY_PREFLIGHT_PAGE_LOCK_AND_MATH_FIGURE_TODO_2026-10-06.md`

## Core requirements

The presentations workflow must add first-class support for:

1. exact historical-feedback count preflight before any source edit;
2. feedback lifecycle and supersession;
3. explicit modify / human-locked / round-frozen scopes for every revision;
4. immutable human-PASS page locks with body-region hash/pixel protection;
5. shared-component locks for header, footer, Question/Answer geometry, caption, code, and table styles;
6. retained and aligned Question/Answer accent rules;
7. page PASS rows that name relevant historical guard IDs and current rendered evidence;
8. stable semantic page IDs across page-number/version changes;
9. real mathematical glyphs inside scientific figures (`$\eta$`, `$\beta$`, `$\kappa$`, `$\mu$`) rather than English transliterations;
10. completion reports proving zero locked-page, frozen-page, and shared-component violations.

## Why this is core

The failure recurred across multiple real versions even after ledgers and review standards existed. The missing capability is enforcement: history must be counted and consumed, accepted pages must be immutable, and shared geometry must be protected like production UI components.

## Promotion gate

- omission of one historical item blocks editing;
- unresolved feedback conflict blocks editing;
- touching a round-frozen page blocks commit;
- touching a human-PASS body region blocks commit;
- authorised header/footer change preserves locked body pixels;
- Question/Answer one-line and multi-line fixtures align within calibrated whole-slide tolerance;
- a figure labelled with literal `eta` fails, while a `$\eta$` render passes.
