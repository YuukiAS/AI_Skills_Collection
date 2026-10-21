# Release candidate identity

Frozen behavioral implementation:
`3e81802ab0251d3bf31ec2d808d4e3273505b2f6`.
Merged latest main base:
`c7f98f201c746d357344091f89cce7a3541154d9`.
Normal merge commit:
`6a1ece94609809bfe8289a04fa2f5d224e0d6fa9`.

The latest main merged without conflict. Its unrelated Clear Writing, PIE,
AGENTS, README, CHANGELOG, registry and other changes are preserved.

Repository bump decision: PATCH
Reason: compatible safety improvement to an existing standalone Slurm workflow;
no collection-level installation or central-plugin topology change.
Affected standalone skills:
- slurm-workflows: 0.4 -> 0.5, exactly once in this task.
Affected plugins:
- all central Marketplace plugins: NO_BUMP.
Bridge Kit, DII, CARE and other tasks: NO CHANGE.

Release metadata: Repository 5.5.1 -> 5.5.2, based on the freshly read formal
main. setup.py reads VERSION; registry/catalog are regenerated from source.
The only Slurm SKILL.md delta from the frozen candidate is its version field.
The release-baseline test changes only its two expected release values.

Runtime SHA256 (unchanged from the frozen candidate):

| File | SHA256 |
| --- | --- |
| setup_protected_cancel.py | 0fa4c9a601645470cf778038ea17f1c062c794fd31b2bc7bde3c0cb931327d03 |
| slurm_cancel_hook.py | 1b5d2cc5cdbd390865fb14862e7c84a803f6a75b60141c8e629cb433dadeea65 |
| slurm_protected_cancel_mcp.py | e1582e92bbe6d9f0f2086761d3ef092c08d3481df10fbc5830c7f170244e34e9 |

Revised G4 and independent frozen implementation review passed. Live Job
retain remains NOT_RUN and is expressly waived by the current user. The real
harmless native retain response and deterministic retain integration are
separate evidence. No scheduler access, Job operation or cancellation occurs
during this release closure.

Existing same-runtime focused 54, full Slurm 69, full repository 401 and CI
39434396011 remain valid. Final release CI is a separate required run on the
merged release candidate; it is PENDING at this checkpoint. G5 and formal
installation are not yet claimed. Maintenance tracking: #109.
