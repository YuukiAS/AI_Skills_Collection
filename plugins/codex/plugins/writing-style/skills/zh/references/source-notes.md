# Source Notes

This skill is a local synthesis. It does not vendor upstream repositories directly.

Sources inspected locally:

- `MrGeDiao/shuorenhua`, commit `1cd6145`, MIT license. Used for protected spans, scene-based rewrite scope, residual AI-taste audit, and Chinese-first naturalization rules.
- `op7418/Humanizer-zh`, commit `91f3d39`, MIT license. Used for common AI writing traces such as vague significance claims, promotional language, fuzzy attribution, forced triads, filler phrases, and generic positive conclusions.
- `ruanyf/document-style-guide`, commit `5719517`, public domain. Used for Chinese technical documentation conventions around titles, paragraphs, numbers, punctuation, document structure, and references.
- `vale-cli/vale`, commit `5242b459`, MIT license. Used only as a conceptual reference for programmable prose linting; this skill has no Vale runtime dependency.

If upstream guidance conflicts with fact preservation, fact preservation wins.
