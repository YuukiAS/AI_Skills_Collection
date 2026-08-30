# Real-world presentation guardrails

Use this reference for real research deck revisions after reading `SKILL.md`.
It keeps mature cross-project rules in runtime context without carrying
project-specific TODO history into installed plugins.

## Rule Inheritance

For any deck revision based on user, advisor, reviewer, or visual-review
feedback:

- read the current active skill and this reference before changing slides;
- identify accepted slides/components from the version that was actually
reviewed;
- record the revision constraints in working notes or the deck plan;
- verify each inherited constraint against the final render, not only against
source text or generator output.

If the same failure has already been pointed out in prior rounds, treat a repeat
as `REVISE` or `BLOCKED`, not as a fresh style preference.

## Audience And Evidence

- Introduce new notation, acronyms, datasets, methods, estimands, and domain
  terms before using them as central slide objects.
- When current audited data include a real example for a new concept, prefer one
  short real example over placeholders such as `group 1` or toy categories.
- State the availability boundary for optional evidence. Do not imply that a
  field, classifier score, trait, phylogeny, or source figure exists unless the
  source audit verifies it.
- Keep internal paths, run status, audit labels, seeds, hashes, and draft
  workflow notes out of audience-facing slide text unless they are the
  scientific subject.

## Layout And Math

- Use one intellectual job per slide. If a slide teaches unrelated concepts,
  split or remove the weaker job.
- Allocate space by scientific importance, not by symmetry. A main figure,
  formula, medical panel, table, or diagram should be readable at presentation
  distance.
- Use two columns only for true peer-level comparison. If a full-width shared
  object remains below two columns, reserve a distinct region with whitespace
  and a clear role.
- A first-line centered display formula must be the page's central scientific
  object and must already have semantic context.
- Choose math environments intentionally: `align` for connected derivations,
  `cases` for mutually exclusive branches under one left-hand object, and
  inline or left-aligned definitions for short notation.

## Diagrams

Draw a diagram only when it communicates a scientific relationship, mechanism,
computation, experiment path, dependency, or transformation faster than text or
formula alone.

Construction order:

1. semantic graph;
2. explicit layout constraints;
3. reading direction;
4. node levels or columns;
5. legal edge paths;
6. ports and anchors;
7. box sizes;
8. arrow style;
9. color and polish.

Connectors must encode real structure. Arrows are not containment, decoration,
or prose punctuation. If a user requires vertical, downward, aligned, equal-size,
or two-column geometry, satisfy that geometry in the layout before styling.

## Rendered QA

Before delivery, inspect a real render:

- full deck or contact sheet for rhythm, density, repetition, and transitions;
- high-resolution single-page renders for diagram, figure-heavy, theory,
  discussion, references, and known-problem slides;
- visible text from source and rendered artifact for internal-language leakage;
- accepted-element regression against the reviewed prior version.

Compilation success, absence of LaTeX overfull warnings, object editability, or
generator self-reporting is not enough to declare a research deck complete.
