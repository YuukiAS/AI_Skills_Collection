# README Clear Writing final check

Use the installed Clear Writing plugin to review the supplied `README.md`.

Scope:

- the repository release line;
- the Clear Writing row in the central plugin table;
- enough surrounding reader-facing context to detect a local language mismatch.

Requirements:

- keep repository version `5.5.1` and Clear Writing version `0.5` exact;
- preserve product names, plugin slugs, paths, commands, and technical meaning;
- do not add release-process, Gate, review, commit, or test history;
- prefer natural Simplified Chinese for ordinary reader-facing explanation;
- do not change unrelated README sections.

Return `PASS_AS_WRITTEN` if no language edit is needed. Otherwise return only a
minimal replacement for the affected reader-facing line and a short reason.
