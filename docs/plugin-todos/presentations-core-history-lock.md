# Presentations Core TODO — History, Locks, and Bounded Convergence

Status: PROMOTE_NOW  
Source: repeated STAT5060 Tutorial 01 revisions through V09 plus earlier research-deck regressions  
Detailed specifications:

- `docs/design/PRESENTATIONS_HISTORY_PREFLIGHT_PAGE_LOCK_AND_MATH_FIGURE_TODO_2026-10-06.md`
- `docs/design/PRESENTATIONS_EXISTING_DECK_CONVERGENCE_ARCHITECTURE_V1_2026-10-06.md`

## Core requirements

The presentations workflow must add first-class support for:

1. exact historical-feedback count preflight before any source edit;
2. feedback lifecycle and supersession;
3. explicit modify / human-locked / round-frozen scopes for every revision;
4. immutable human-PASS page locks with body-region hash/pixel protection;
5. separate semantic, visible-copy and visual locks;
6. shared-component locks for title, header, footer, Question/Answer geometry, typography, columns, caption, code, table, figure and closing styles;
7. retained and aligned Question/Answer accent rules;
8. stable semantic page IDs and explicit ancestry across page-number/version changes;
9. exact-copy enforcement so the executor cannot add audience-visible prose;
10. a versioned layout grammar with approved column/page archetypes rather than page-local improvisation;
11. cumulative acceptance standards with a predecessor-gate carry-forward matrix;
12. real mathematical glyphs inside scientific figures (`$\eta$`, `$\beta$`, `$\kappa$`, `$\mu$`) rather than English transliterations;
13. deterministic Codex rejection before isolated visual/pedagogical review;
14. a user-facing delta bundle instead of repeated full-deck re-annotation;
15. two-to-four-round monotone convergence: open pages decrease, locked pages increase, unrelated regressions remain zero.

## Why this is core

The failure recurred across multiple real versions even after ledgers and review standards existed. The missing capability is not another checklist. It is enforcement and controlled revision: history must be counted and consumed, accepted pages/components must be immutable, executors must not author copy, and a local repair must not rewrite unrelated parts of the deck.

## Promotion gate

- omission of one historical item blocks editing;
- unresolved feedback conflict blocks editing;
- page deletion without approved semantic relocation blocks editing;
- touching a round-frozen page blocks commit;
- touching a human-PASS body region blocks commit;
- executor-added visible copy blocks commit;
- an unauthorised layout archetype blocks commit;
- an acceptance standard that omits an unretired predecessor gate blocks review;
- authorised header/footer change preserves locked body pixels;
- Question/Answer one-line and multi-line fixtures align within calibrated whole-slide tolerance;
- a figure labelled with literal `eta` fails, while a `$\eta$` render passes;
- one real existing deck converges within two to four review rounds under the new workflow.
