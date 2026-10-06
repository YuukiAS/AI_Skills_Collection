# Candidate Replay Review — UI Handoff

**Target screen:** Candidate replay evidence review for plugin maintainers.

**Primary user action:** Review the evidence to check candidate plugin use, conflicting path reads, and restoration of the original plugin state after cleanup.

**Three UI labels** (evidence rows, in reading order):

1. Candidate plugin used
2. Conflicting plugin paths read
3. Original plugin state restored

**Empty state:** “No replay evidence yet. When evidence is available, review it here to check plugin use, conflicting paths, and cleanup.”

**Placement and meaning:** Show each label beside its supporting evidence. When no evidence is available, show the empty state in the evidence area. Missing evidence must not imply that a check passed. These labels describe checks, not confirmed outcomes.
