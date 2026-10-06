# Candidate replay review — UI handoff

**Target screen:** Candidate replay evidence, for plugin maintainers. Show three evidence rows together; replace them with the empty state when no evidence is available. UI copy is in English, matching the product note.

**Primary user action:** Review the evidence to check whether the candidate plugin was used, conflicting plugin paths were read, and cleanup restored the original plugin state.

**Three UI labels** (evidence-row headings):

1. Candidate plugin used
2. Conflicting plugin paths read
3. Original plugin state restored

**Empty state:** No replay evidence is available to review yet. When evidence is available, check it here.

**Display rule:** Keep each result tied to its evidence. Missing evidence means “Unknown”; it does not prove success or failure.
