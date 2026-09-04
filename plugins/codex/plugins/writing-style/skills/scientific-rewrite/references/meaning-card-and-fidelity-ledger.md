# Meaning Card And Fidelity Ledger

Use this reference when preparing a high-fidelity Chinese scientific rewrite.

## Document Map

The Document Map is compact context for the whole document. It may contain:

- audience
- document purpose
- reader questions
- section map
- terminology glossary
- cross-section definitions
- claim dependencies
- evidence classes
- important caveats
- major conclusions
- literal-protected inventory

It is not a new fact source. The original document remains authoritative.

## Rewrite Unit

Choose a complete argument or discourse unit:

- one subsection; or
- 2-5 paragraphs that share a definition, condition, result, limitation, or
  conclusion.
- non-contiguous bounded spans when they answer the same scientific question
  and the argument plan records source-span ownership.

Do not cut through formulas, tables, result interpretations, caveats, or
comparisons simply to fit a fixed token budget.

For structural scientific rewrite, unit order may follow reader logic rather
than source order. The invariant is complete source-span coverage without
unmarked duplication, not adjacency.

## Meaning Card Template

```text
Unit id:
Audience:
Purpose:
Claims:
Evidence/results:
Conditions/comparators:
Caveats/uncertainty/negative findings:
Evidence class:
Literal-protected:
Terminology:
Relation to previous/next argument:
Reader takeaway:
Coverage check:
```

`Reader takeaway` helps expression only. It cannot add a fact, value judgment,
or conclusion not supported by the source.

Meaning Cards are host-Codex semantic artifacts. They must not be produced by
copying source excerpts into `normalized_meaning`, claims, evidence, or reader
takeaway. If a card is missing or malformed, fail and repair the card rather
than synthesizing a source-copy fallback.

## Literal Preservation

Preserve exactly when exact wording or token identity matters:

- numbers, dates, ranges, units, percentages
- formulas, notation, variables
- citations, DOI, exact quotations
- code, commands, paths, config keys, identifiers
- formal algorithm, dataset, benchmark, package, product, and metric names
- user-explicit no-touch spans

Ordinary reader-facing headings, internal workflow labels, and section wording
are not literal-protected by default.

### Literal Location Roles

Every literal item must also receive a location role:

- `inline-critical`: exact material belongs in the reader-facing scientific
  argument, either at the original location or at a nearby natural location.
  Typical examples include numbers, formulas, metrics, dataset/method formal
  names, comparison-defining identifiers, and citations that support a nearby
  scientific claim.
- `relocatable-trace`: exact material must remain in the complete deliverable,
  but may move to a clearly labeled technical/evidence appendix when it is
  evidence for a judgment rather than part of the main explanation. Typical
  examples include checkpoint paths, repository paths, exhaustive file
  identities, implementation locators, and low-level audit trails.

Relocation is not deletion. Limitations, negative findings, uncertainty,
contradicting evidence and decision conditions remain part of the reader-facing
argument even when implementation trace moves to an appendix.

An `inline-critical` item found only in a technical appendix, token inventory,
receipt, or trace list is still missing. A `relocatable-trace` item may move to
an appendix only when the appendix gives meaningful context, not a raw literal
bag.

## Semantic Preservation

Semantic items may be rewritten completely, but meaning cannot change:

- claim and polarity
- uncertainty and evidence strength
- condition, scope, exception
- comparator and comparison direction
- chronology and causality
- attribution
- caveat and negative result
- conclusion strength

## Claim/Relation Status

After rewriting, classify each claim or relation as:

- `preserved`
- `narrowed`
- `broadened`
- `reversed`
- `invented`
- `omitted`
- `reattributed`

For every non-`preserved` status, cite source evidence and candidate evidence.
