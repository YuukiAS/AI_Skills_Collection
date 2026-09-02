# Meaning Card And Fidelity Ledger

Use this reference when preparing a high-fidelity Chinese scientific rewrite.

## Document Map

The Document Map is compact context for the whole document. It may contain:

- audience
- document purpose
- section map
- terminology glossary
- cross-section definitions
- claim dependencies
- important caveats
- major conclusions
- literal-protected inventory

It is not a new fact source. The original document remains authoritative.

## Rewrite Unit

Choose a complete argument or discourse unit:

- one subsection; or
- 2-5 paragraphs that share a definition, condition, result, limitation, or
  conclusion.

Do not cut through formulas, tables, result interpretations, caveats, or
comparisons simply to fit a fixed token budget.

## Meaning Card Template

```text
Unit id:
Audience:
Purpose:
Claims:
Evidence/results:
Conditions/comparators:
Caveats/uncertainty/negative findings:
Literal-protected:
Terminology:
Relation to previous/next argument:
Reader takeaway:
Coverage check:
```

`Reader takeaway` helps expression only. It cannot add a fact, value judgment,
or conclusion not supported by the source.

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
