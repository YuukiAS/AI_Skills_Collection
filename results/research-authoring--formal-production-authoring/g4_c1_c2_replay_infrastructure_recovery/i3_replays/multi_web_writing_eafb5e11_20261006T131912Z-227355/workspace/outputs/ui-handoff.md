# Candidate Replay Review — UI Handoff

- **Target screen:** Candidate replay evidence review for plugin maintainers.
- **Primary user action:** Review the replay evidence to determine whether the candidate plugin was used, conflicting plugin paths were read, and cleanup restored the original plugin state.
- **Content layout:** Screen title followed by three evidence rows. Keep each label beside its finding and supporting evidence. Use English copy to match the product note.

| UI label | Meaning to preserve |
| --- | --- |
| Candidate plugin used | Whether the replay actually used the candidate plugin. |
| Conflicting plugin paths read | Whether the replay read conflicting plugin paths. |
| Original plugin state restored | Whether cleanup restored the original plugin state. |

**Empty state** — Show when no replay evidence is available, in place of the evidence rows:

> No replay evidence is available yet. Review it here when it becomes available.

**Handoff constraint:** Missing evidence must remain unknown; it must not imply success or failure. The note does not define a way to start a replay or load evidence, so no such control is specified. Validate text fit and row hierarchy when the screen is implemented.
