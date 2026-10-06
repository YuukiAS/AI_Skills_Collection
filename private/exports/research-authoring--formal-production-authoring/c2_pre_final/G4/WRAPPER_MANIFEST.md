# C2 G4 Offline Wrapper Manifest

```text
C2_FINAL_CANDIDATE_COMMIT=
ac501d988f00cb6672fec105ae5fd51a0679cae0

WRAPPER_LIVE_MUTATION_AUTHORIZED=
NO

G4_FINAL_EXECUTION_STARTED=
NO
```

## Canonical input identity

Research Authoring generated payload:

`plugins/codex/plugins/research-writing/** @ ac501d988f00cb6672fec105ae5fd51a0679cae0`

Clear Writing support roots:

```text
skills/writing/core/writing-fidelity/**
skills/writing/core/chinese-prose/**
skills/writing/core/scientific-prose/**
```

all from the same C2 commit.

Representative Git blobs are recorded in:

`results/research-authoring--formal-production-authoring/C2_SOURCE_GENERATED_IDENTITY.md`

## Frozen G4 rubric authority

Existing rubric remains unchanged:

`private/exports/research-authoring--formal-production-authoring/final_tasks/G4/CHAT_CODEX_HANDOFF_RUBRIC.md`

Git blob SHA:

`a7bf0b765bd9bf6d5b5a6acdf31c3a5b6bf6c5ad`

The rubric is reused semantically; C2 binding is supplied by this manifest and the new G2 baseline.

## Future live update

Before any live mutation:

1. rebuild the complete skills-only archive from C2;
2. compute archive/file manifest hashes;
3. re-read the current live Plugin/release identity;
4. obtain a new bounded user authorization;
5. guarded-update only the existing PRIVATE USER-scope wrapper.

No live mutation occurs during pre-final packet preparation.
