# Bobbio / Lucerna / Asteria Replay Preflight

Task key: `web-development--frontend-design-production-consolidation`

This is read-only preflight evidence. No target project was modified.

## Bobbio

- Repository path: `/home/yuukias/code/Bobbio`
- Current branch/status: `main...origin/main`
- Current HEAD: `445d31e5d5408b2a39948ad1d98613f6eb31e742`
- Dirty state observed: none in `git status --short --branch`

Located authority/evidence files:

- `docs/design/FIGMA_HANDOFF.md`
- `design-qa.md`
- `docs/design/Bobbio_Product_Design_Review.pdf`
- `docs/design/prototype/qa/browser-qa.json`
- `docs/design/prototype/qa/*.png`

Read-only source notes:

- `docs/design/FIGMA_HANDOFF.md` names the Figma file as the canonical visual design source for subsequent implementation.
- `design-qa.md` records no remaining P0/P1/P2 issues and contains browser QA evidence, interaction checks, and source visual truth.

Replay classification expectation:

- Much of Bobbio's canonical Figma and P1/P2/browser QA behavior is repo-local compatibility evidence.
- Plugin capability can only be counted if the candidate coordinator independently makes a generic decision not directly supplied by Bobbio authority.

## Lucerna

- Repository path: `/home/yuukias/code/Lucerna`
- Current branch/status: `main...origin/main`
- Current HEAD: `3b7b349d6bc0460acccf98a4b607fddc40336eda`
- Dirty state observed: untracked `.gitignore`, `index.html`, `package.json`, `prompts/tasks/`, `src-tauri/`, `src/`, `tsconfig.json`

v0.3 plan-required files:

- `AGENTS.md`: present
- `docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`: missing at current HEAD/worktree
- `docs/design/lucerna/LUCERNA_UI_PRODUCT_SYSTEM_V1.md`: missing at current HEAD/worktree
- `docs/design/lucerna/LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1.md`: missing at current HEAD/worktree
- Additional read-only recovery: after `git fetch origin main`, `origin/main` resolves to `b626c2ce998882941dba0f30a00ecf627cc740b5` and contains the three missing v0.3 paths.

Nearby located files:

- `docs/AUTH.md`
- `docs/design/VISUAL_DIRECTION.md`
- `origin/main:docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md`
- `origin/main:docs/design/lucerna/LUCERNA_UI_PRODUCT_SYSTEM_V1.md`
- `origin/main:docs/design/lucerna/LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1.md`

Read-only source notes:

- `AGENTS.md` records the local handoff protocol.
- `docs/AUTH.md` defines credential and device-auth boundaries.
- `docs/design/VISUAL_DIRECTION.md` defines Lucerna's lamp/lighting brand direction, platform IA split, and state color semantics.

Replay preflight gap:

- Strict G6 can use the exact v0.3 Lucerna source set from frozen ref `origin/main` / `b626c2ce998882941dba0f30a00ecf627cc740b5`.
- The current Lucerna worktree remains dirty and behind; do not mutate, pull over dirty state, clean, reset, or checkout it for replay.

## Asteria

- Repository path: `/home/yuukias/code/Asteria`
- Current branch/status: `main...origin/main [behind 4]`
- Current HEAD: `f2fbbc3cd2edb3f005ae939f8d30637966256098`
- Dirty state observed: none in `git status --short --branch`

Located authority/evidence files:

- `docs/design/accepted-concepts/README.md`
- `docs/design/accepted-concepts/*.png`
- `results/asteria_v2_rc15_visual_system_result.md`
- `docs/design/LINEAGE_EVIDENCE_VISUAL_GRAMMAR_SPEC.md`
- `docs/design/SCIENTIFIC_GRAPH_VISUAL_SYSTEM.md`

Read-only source notes:

- Accepted concepts define visual/interaction language but are not mathematical, citation, simulation-status, real-data-status, or authorship truth.
- `results/asteria_v2_rc15_visual_system_result.md` records developer visual self-QA and browser/public evidence for the active visual system.

Replay classification expectation:

- Asteria is best suited to browser/no-Figma should-not-overreach compatibility.
- Repo-local visual self-QA and accepted-concept boundaries should not be relabeled as plugin maturity evidence unless the coordinator makes an independent generic decision beyond those sources.

## Current G6 Status

`G6` is not complete.

Reasons:

1. Candidate plugin replay now PASSed through `scripts/candidate_plugin_replay.py`; see `replay/candidate_plugin_replay_status.md`.
2. Bobbio/Lucerna/Asteria real-project replay is frozen in `replay/real_project_replays/`, but running it requires explicit authorization to transmit those project documents to the child Codex/model provider for analysis.
