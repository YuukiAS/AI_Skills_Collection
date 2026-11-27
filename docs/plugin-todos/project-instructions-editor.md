# project-instructions-editor — Long-Term TODO

This inbox keeps unresolved, reusable failures for the standalone Project Instructions Editor skill. Historical design snapshots belong in Blueprint, not in this public repository.

## Open candidates

### Shared instructions can become scope-imbalanced after a local addition
status: NEW
tracking: #93
problem: A narrow addition can grow into repeated workflow prose, flatten priorities, and consume the instruction budget. The editor should preserve the requested local change while checking the whole instruction set for duplicated detail and lost emphasis.

### Live editing must compare the actual setting, its history, and canonical repository guidance
status: NEW
tracking: #93
problem: Editing only one source can overwrite newer decisions or preserve stale instructions. The normal route should inspect the complete current setting, relevant history, and current canonical repository guidance before producing a replacement.

### Repository instructions can drift from their owning policy
status: NEW
tracking: #108
problem: A repository-level projection can silently diverge from its canonical owner. Maintenance should identify the owner, compare the projection, and update only the bounded projection rather than inventing a second policy source.

### Private wrappers may expose an optional user-owned locator
status: NEW
problem: A private wrapper may need a user-controlled locator for instruction configuration, but the public skill must not embed private paths, credentials, or account-specific defaults.
