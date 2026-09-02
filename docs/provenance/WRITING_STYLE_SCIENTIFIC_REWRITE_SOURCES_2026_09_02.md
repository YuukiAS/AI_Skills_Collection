# Writing Style Scientific Rewrite Sources - 2026-09-02

This note records the stable source-adoption evidence for the 048
`writing-style` scientific-rewrite cutover. It is a provenance record, not a
runtime instruction file.

## MrGeDiao/shuorenhua

- source: `https://github.com/MrGeDiao/shuorenhua.git`
- exact commit: `6de1fcfeca5fff6fd15b28c619c11b6d41d1f657`
- license: MIT
- license SHA-256: `d26eebf6104e9770ca097771022767da18fc07ca73a542469d2748b2e3186878`
- decision: `SELECTIVELY_PORTED`

Adopted ideas: positive Chinese style direction, scene/scope thinking,
literal-vs-semantic protection boundaries, and should-fix / should-not-fix
evaluation philosophy.

Not adopted: broad phrase lists, fiction/social-media modules, wholesale
vendoring, runtime dependencies, detector evasion, or project-specific
blacklists.

## whh110112/human-writing-skills

- source: `https://github.com/whh110112/human-writing-skills.git`
- exact commit: `2b02ae77bd1ea009ea2d7a1cc6d2dcdce1437a00`
- license: MIT
- license SHA-256: `4683c8e7b19375dad28c8589e7b31bb67eadcc6799ce14ab9feb64f1d21e3c1a`
- decision: `SELECTIVELY_PORTED`

Adopted ideas: original/reference/source authority separation, claim-ledger
fidelity, bounded long-form context, deterministic exact checks, and explicit
coverage thinking before rewriting.

Not adopted: fiction/webnovel modules, style imitation machinery, package
vendoring, runtime dependency, or reference text as a factual authority.

## AIScientists-Dev/academic-humanizer

- source: `https://github.com/AIScientists-Dev/academic-humanizer`
- exact commit: `94b88b23703bed7df507acae7d6d5876209a0cdf`
- decision: `REFERENCE_ONLY`

This source remains out of the 048 active cutover. It may be audited later for
non-duplicative English academic-writing capabilities, but 048 does not adopt
its AI-tell catalogue, blanket punctuation house style, or grant-writing rules.

## Cross-Source Synthesis

Both selectively ported sources support the same narrow production direction:

- define positive rewrite operations instead of only collecting bad phrases;
- separate literal preservation from semantic preservation;
- keep examples as transformation evidence only, never as fact sources;
- split long documents by argument/discourse units rather than fixed tokens;
- run deterministic exact checks before judging style quality;
- audit claim/relation drift separately from naturalness.
