# Route B: Cross-Layer Stack Or Workflow Composition

Use Route B only when formal release metadata explicitly declares required companions or managed-consumer refreshes through `### Update impact`.

Possible owners may include:

- AI_Skills central plugins;
- Bridge Kit distribution;
- Bridge Host;
- Bridge managed consumers;
- AI_Skills managed consumers.

Route B composes existing owners; it does not create a cross-stack runtime.

## Execution Order

1. Resolve the exact AI_Skills and/or Bridge formal release identity.
2. Parse the matching root `CHANGELOG.md` release section.
3. Build the required companion list from `### Update impact` only.
4. Discover ownership-proven managed consumers.
5. Record the should-not-change set.
6. Execute owner operations in dependency order.
7. Verify each owner through its normal surface.
8. Report `UPDATED`, `UPDATED_RELOAD_REQUIRED`, `ALREADY_CURRENT`, `PARTIAL_UPDATE`, `RELEASE_METADATA_INCONSISTENT`, `REPO_OWNED_CONFLICT`, or `DEVELOPMENT_SOURCE_PRESENT` as appropriate.

## Managed Consumer Boundary

Automatic mutation is allowed only on:

- AI_Skills manifest-managed installs and exact managed blocks;
- Bridge canonical managed consumers/templates/blocks;
- exact migration targets named by release impact with an ownership locator.

Unmanaged repo-authored text is diagnosis-only. If an unowned rule blocks the update, report `REPO_OWNED_CONFLICT` with exact repo/path/reason and request a bounded repo-owned decision or separate authorized task.

