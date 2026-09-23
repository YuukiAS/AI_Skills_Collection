# G4/G5 Fixture Evidence

Task key: `ai-skills-core--machine-update-orchestration`
Fixture root: `/home/yuukias/AI_Skills_Collection-ai-skills-core-machine-update-orchestration/private/exports/ai-skills-core--machine-update-orchestration/fixtures`

| Case | Status | Before hash | After hash | Diagnostics |
|---|---|---|---|---|
| `stale_managed_consumer` | `UPDATED_RELOAD_REQUIRED` | `f4eaa8d367e72c4d76fc9075bde06ca9f64479e48b151f732f3af9890c704bde` | `a8271e199733c180f109ea44c1cd0a908953b757a5be65cea39e5c624904dde1` | managed block updated from ai-skills-core 0.4 to 0.5<br>project-owned preface/suffix preserved<br>README.md unchanged=True |
| `unaffected_repo` | `ALREADY_CURRENT` | `a937a64909c05c4612b5a706eb40d9956c1d139c60b027045cdc9383ab48e49f` | `a937a64909c05c4612b5a706eb40d9956c1d139c60b027045cdc9383ab48e49f` | no managed locator discovered<br>byte-for-byte unchanged |
| `unmanaged_conflict` | `REPO_OWNED_CONFLICT` | `4205ddf977e33c7dfb732b99e114d57276402cd31fa6b3eaeb1cf8ed121a418e` | `4205ddf977e33c7dfb732b99e114d57276402cd31fa6b3eaeb1cf8ed121a418e` | AGENTS.md unchanged=True<br>no automatic edit to repo-owned text |
| `unrelated_dirty_non_overlap` | `UPDATED_RELOAD_REQUIRED` | `fe9aa5c2aae6594b6f521e7ff39229712bc519f83dfb762893e10bbe987def06` | `ef4ca373f0979bb5be2305e2658640b50c6e370872f425749bb961a7ba1563a1` | non-overlapping dirty notes.txt preserved<br>notes.txt hash preserved after managed update=True<br>git status entries=['M AGENTS.md', ' M notes.txt'] |
| `overlapping_dirty_human_gate` | `HUMAN_ONLY` | `02f9b5ac0f23c541eaac902bca4c9a685f21f6af19596bf8412f686fe195eedb` | `02f9b5ac0f23c541eaac902bca4c9a685f21f6af19596bf8412f686fe195eedb` | AGENTS.md unchanged=True<br>exactly one bounded dirty-overlap Human Gate required |
| `failure_restoration_and_rerun` | `PARTIAL_UPDATE` | `cda584689289732d046182c0b7599d5a774941df1e53979d560d50106b8557b0` | `ceb16b3897456a37f82d590e5462f352434a07eb223e8138fbe5bfada4ecce50` | safe managed update retained after later marketplace swap failure<br>legacy marketplace source restored exactly after simulated add-release failure<br>rerun converged without second mutation=True<br>README.md unchanged=True |

All fixture repositories are task-owned local repositories under `private/exports/`.
The tracked evidence records only paths, hashes and result states; unrelated real projects were not used.
