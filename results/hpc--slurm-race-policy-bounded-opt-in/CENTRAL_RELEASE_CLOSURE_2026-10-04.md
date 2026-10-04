# Central Release Closure — hpc--slurm-race-policy-bounded-opt-in

RESULT = CENTRAL_RELEASE_COMPLETE

## Identity

- Repository: `YuukiAS/AI_Skills_Collection`
- Task: `hpc--slurm-race-policy-bounded-opt-in`
- Reviewed branch: `reviewed/hpc--slurm-race-policy-bounded-opt-in`
- Product candidate: `5a3dc447da2ea429ba2d229b0301c378be9e8018`
- Locator repair tip: `520fd159737c63b2aabdddb43a8e491219fff897`
- Final Critic PASS: `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`
- GitHub CI: run `37187784359`, `head_sha = 5a3dc447da2ea429ba2d229b0301c378be9e8018`, PASS

REAL_SLURM_MUTATION = NO

## Versions

- Formal release baseline: `03b0281b1f7fbd29621faa6298cd1db2578a0ffc`
- Baseline repository version: `5.4.3`
- Baseline `slurm-workflows`: `0.3`
- Released repository version: `5.4.4`
- Released `slurm-workflows`: `0.4`
- Central Plugins: `NO_BUMP`
- Bridge Kit: `NO_CHANGE`

## Release Commits

- Main integration commit: `f2fbf49ac2203a377106891fd36ddfc901b98ed3`
- Formal release commit: `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`
- `origin/release` after publication: `06d135d8a6ee62cd41abb40fc5771fcef7f8db25`
- `origin/main` after main integration publication: `f2fbf49ac2203a377106891fd36ddfc901b98ed3`

## Release Isolation Proof

The formal `5.4.4` release target is the Final Critic PASS reviewed line,
not the current `main` tree.

Preflight evidence:

- `origin/release` was `03b0281b1f7fbd29621faa6298cd1db2578a0ffc` with
  repository `5.4.3`.
- `origin/release` was an ancestor of
  `origin/reviewed/hpc--slurm-race-policy-bounded-opt-in`.
- The release target contained no changes under:
  - `skills/tools/documents-media/presentations`
  - `plugins/codex/plugins/presentations`
- Central Marketplace plugin versions matched the `5.4.3` baseline.
- Slurm release-critical bytes at the release target matched product candidate
  `5a3dc447da2ea429ba2d229b0301c378be9e8018`.

Current `main` contains unrelated Presentations production development:

- `skills/tools/documents-media/presentations/shared/font-policy.md`
- `skills/tools/documents-media/presentations/shared/template-routing.md`
- corresponding generated plugin payload paths.

Those changes were preserved on `main` but were not included in the formal
`5.4.4` release target.

After publication:

- `origin/release = 06d135d8a6ee62cd41abb40fc5771fcef7f8db25`
- `origin/release` is an ancestor of `origin/main`
- `VERSION = 5.4.4` on `origin/release`
- `slurm-workflows = 0.4` on `origin/release`

## Scope Closed

The released Slurm Workflows behavior keeps duplicate race off by default and
requires all of the following before a race may be authorized:

- no explicit site prohibition;
- explicit user/local opt-in;
- exactly two distinct candidate routes;
- full workload/scientific contract identity;
- matching `workload_scope_digest` when present;
- hard GPU, memory, CPU, walltime, and explicit resource compatibility;
- closed winner/loser cancellation semantics.

The release does not authorize real `sbatch`, `salloc`, `scancel`, duplicate
GPU race execution, weekly GPU enrollment, Bridge Kit changes, DII mutation, or
central plugin version bumps.

## Tracking

- Issue: `#96`
- Issue lifecycle after central release: OPEN
- Project Status after central release: ADAPTING
- Resolution commit: EMPTY
- DII adaptation: PENDING
- Clear Writing replay for central release Issue update:
  `20261004T124653Z-38ef2f750575`
- Issue #96 central release update comment:
  `https://github.com/YuukiAS/AI_Skills_Collection/issues/96#issuecomment-5980097091`
- Project verification: Issue #96 remains OPEN and Project item status is
  `ADAPTING` with option id `7527fc31`.

The central standalone skill release is complete. The remaining work is a
separate DII consumer adaptation: install/load the formal `slurm-workflows 0.4`
release in DII and run read-only/synthetic verification without real Slurm
mutation.
