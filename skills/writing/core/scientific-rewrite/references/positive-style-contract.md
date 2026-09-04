# Positive Style Contract

This contract defines the desired Chinese scientific prose direction. It is
positive guidance, not a blacklist.

## Target

The rewritten text should let a first-time scientific or technical reader know:

- what the subject is;
- what changed, failed, succeeded, or remains uncertain;
- why a method, dataset, package, or term appears here;
- which comparison or condition matters;
- what the reader should carry into the next paragraph.

## Preferred Transformations

- Replace internal workflow labels with the real subject, action, and relation.
- Explain first-use terms with local context, not only acronym expansion.
- Convert log narration into reader-facing scientific facts.
- Move caveats close to the claim they limit.
- Keep formal names unchanged when they are actual names.
- Use ordinary Chinese sentences when no technical compression is needed.
- Preserve uncertainty instead of smoothing it into a stronger conclusion.
- Use headings to name the scientific role of a section, not the maintenance
  process that produced it.
- Regroup scattered evidence under one reader question when the same scientific
  decision depends on facts from several source locations.
- Introduce formulas with the question or intuition they answer, then preserve
  the exact formula, explain important symbols, and state the implication.
- Turn flat method catalogs into decision-centered groups while retaining every
  method, condition, caveat, and comparison field.
- State the bounded conclusion before nearby qualifications when the source
  supports that order.
- Preserve evidence class distinctions in natural prose so project facts,
  literature facts, interpretation, candidate methods, and unverified items do
  not collapse into one authority level.
- Lower reader inference burden rather than character count. Add a short bridge,
  split a dense paragraph, or use a compact list/table when that lets the
  reader see the comparison without reconstructing it mentally.
- Classify English spans by function: preserve exact names, optionally keep an
  English identifier at first use when it helps recognition, and translate
  ordinary reasoning or organization language into natural Chinese.

## Anti-Patterns

- Adding a phrase to a permanent blacklist whenever a single document sounds
  awkward.
- Treating English density, scanner counts, or detector scores as language
  quality.
- Replacing one English abstraction with a literal Chinese calque while keeping
  the same machine sentence structure.
- Summarizing away conditions or caveats to make prose shorter.
- Rewriting already readable technical prose just because a heavy route exists.
- Appending exact items as a raw token list instead of repairing them in their
  scientific context.
- Treating source order as more important than the reader's scientific decision
  path in an explicit structural rewrite.
- Treating a shorter candidate as better when it has removed the explanation,
  transition, symbol meaning, or information shape that made the result easy to
  read.
