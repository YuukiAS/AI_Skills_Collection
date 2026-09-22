# 056 交付工作流可靠性基线 — Final Integration / Release Plan v0.1

- Historical task key: `056_product_delivery_discipline`
- Human-readable name: 交付工作流可靠性基线
- Stage: `FINAL_INTEGRATION_AND_RELEASE_CLOSURE_PREPARATION`
- Status: `READY_FOR_INDEPENDENT_CRITIC_REVIEW`
- Planning source baseline:
  - AI_Skills main: `7a6d247e04b05d4371296a9415621b468ed492ce`
  - Bridge main: `9d2da9f485f26ca51842a1909a276cb44f73351a`
- Approved AI production candidate: `33c30bbe0dd528031a23d379905cd00d6b65bc1f`
- AI final evidence HEAD: `b6f675869449df8daa86a6abcf527fbb72c66e64`
- Approved Bridge candidate: `96a8ea1b58ebe6f9b7c5c46c43995666251911fe`
- Target releases:
  - AI_Skills repository 5.0.7
  - workflow-core 0.3
  - web-development 0.2
  - ai-skills-core 0.4
  - Bridge Kit 0.8.5

This is not a 056 redesign. G1-G8, Source Discovery, owner boundaries, version routes, least-privilege semantics and deferred follow-ups are frozen. All capability gates have already passed, including the final real-user HUMAN_ONLY reply -> same-Goal exact-once resume evidence. This stage only integrates the approved candidates into current main, closes release metadata/normal-entry parity, permanently upgrades the already-identified normal Bridge installation, permanently applies the approved 0.8.5 Host state, records closure evidence, and optionally removes only the exact reviewed branches after success.

## 1. What is already proven and must not be rerun mechanically

Already PASS:
- G1 real Host + real-user HUMAN_ONLY reply/resume;
- G2-G8;
- Source Discovery;
- agent-resolvable no-false-prompt;
- Plan-mode native input non-regression;
- Host backup/restore;
- `SOURCE_DEFECT_DISCOVERED=NO`.

AI evidence after the production candidate is evidence-only: compare `33c30bbe...` -> `b6f67586...` shows five commits and no changed path outside `results/056_product_delivery_discipline/**` plus `tests/test_056_product_delivery_discipline_gates.py`. Therefore evidence SHA movement did not alter the approved production candidate.

Do not rerun:
- Human Gate token smoke;
- Plan-mode smoke;
- G2-G8;
- Terra/paid review;
- the former full AI or Bridge suites merely because integration/evidence commits advance.

Only a conflict resolution that changes production semantics can reopen the corresponding minimal replay/regression.

## 2. Current drift audit

### 2.1 AI_Skills

Current main and reviewed branch diverge:

- main: `7a6d247e04b05d4371296a9415621b468ed492ce`
- reviewed: `b6f675869449df8daa86a6abcf527fbb72c66e64`
- merge base: `9f1c0d32abf49e674bcc7cab0e7287ed714a1199`
- reviewed ahead: 9 commits
- reviewed behind: 16 commits.

The main-only side after the merge base is docs/planning/TODO material. It does not consume the 5.0.7 / 0.3 / 0.2 / 0.4 release slots and does not touch 056 production source.

The exact changed-file intersection between current-main drift and the reviewed 056 branch is only:

`docs/plugin-todos/workflow-core.md`

No workflow-core production skill, Frontend Design production source, AI Skills Maintainer production source, Marketplace source/generated payload, VERSION, README or root CHANGELOG has current-main production overlap.

Resolution of the one TODO overlap is additive:
- preserve every newer current-main-only TODO entry and its wording;
- preserve the reviewed branch's implemented 056 production semantics and real Human Gate wording;
- mark the 056 “Review admission、Human Gate 与真实交付止损” batch as promoted/released in 5.0.7;
- mark least-privilege W2/G1 absorption as promoted/released in 5.0.7 rather than still “ABSORB_NOW”;
- keep ordinary bounded-kickoff renderer and task-local prohibition expiry deferred after 056;
- keep acceptance-artifact packaging as post-056 follow-up evidence; do not implement it here;
- do not create a successor task.

Any conflict outside that single TODO path is a stop condition and returns Planner/Critic.

### 2.2 Bridge

Current Bridge main:

`9d2da9f485f26ca51842a1909a276cb44f73351a`

is the direct ancestor of reviewed candidate:

`96a8ea1b58ebe6f9b7c5c46c43995666251911fe`

The reviewed branch is ahead by 3 commits and behind by 0. No main-side drift or conflict exists. Production integration is therefore a clean fast-forward candidate history, followed only by release-metadata cleanup.

## 3. Release meaning in this repository family

The repository contracts already treat an integrated, installable main identity with canonical VERSION/plugin version, changelog, README and generated parity as the release identity. Both repositories currently have zero GitHub Release objects. This task must not invent the first tag/GitHub Release/package-publication mechanism solely for 056.

Therefore:

- **AI_Skills formal release 5.0.7** = verified 5.0.7 candidate integrated to main with README/changelog/version/generated parity and normal main identity.
- **Bridge formal release 0.8.5** = verified 0.8.5 candidate integrated to main with README/changelog/version parity and normal installation upgraded from that integrated main.
- Git tags, GitHub Releases, package-registry publish and deploy remain `NOT_REQUIRED / NOT_AUTHORIZED`.

External check:
- GitHub documents merge commits as preserving every branch commit plus an explicit merge point, which matches the need to preserve the reviewed AI history.
- GitHub Releases are a separate tag-based packaging surface. Since neither repo currently uses them and the repo-local release contract does not require them, 056 does not add that new publication mechanism.

## 4. Exact integration worktrees and Git strategy

No successor branch is created.

After the approved Kickoff, exact temporary integration worktrees:

AI:
`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-056-final-integration`

Bridge:
`/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit-056-final-integration`

They are based on the exact kickoff-time `origin/main`. Planning/review docs-only main advances are absorbed without reopening gates. If kickoff-time main has any new production/version/release overlap with 056, STOP and return Planner/Critic before merging.

AI integration:
- merge exact reviewed branch history with a real merge commit;
- no rebase, squash, cherry-pick or history rewrite;
- resolve only the one pre-audited workflow-core TODO overlap;
- then create any necessary release/closure docs-only commit(s).

Bridge integration:
- fast-forward the integration worktree from current main through exact candidate `96a8ea1b...`;
- then make only release-metadata changes described below;
- no production source edit.

Before pushing either main, re-fetch both origins and require the observed remote main tips to still match the integration bases. No force push.

## 5. AI_Skills release closure

The reviewed branch already carries:
- `VERSION=5.0.7`;
- Marketplace source versions: workflow-core 0.3, web-development 0.2, ai-skills-core 0.4;
- generated plugin payload versions;
- README 5.0.7/plugin versions;
- affected plugin changelogs.

Required integration-only corrections:

1. `CHANGELOG.md`
   - change 5.0.7 from “release candidate” to formal compatible release;
   - use release date 2026-09-22;
   - remove the stale statement that real Host/live Host smoke is still pending;
   - state that final real-user G1 evidence passed and permanent normal Bridge/Host installation is completed only after that later closure stage actually succeeds.

2. Affected plugin changelogs
   - keep the already reviewed before/after semantics;
   - align 0.3 / 0.2 / 0.4 formal release date to 2026-09-22 if needed.

3. `README.md`
   - expected content is already correct for 5.0.7 / 0.3 / 0.2 / 0.4;
   - preserve current human-facing main structure;
   - modify only if parity audit finds a factual mismatch.
   - Closure must record: `README checked`.

4. `docs/plugin-todos/workflow-core.md`
   - resolve the one audited main/reviewed overlap additively as Section 2 specifies.

5. `results/056_product_delivery_discipline/RESULT.md` and `evidence_manifest.json`
   - before main push, update stale “real Host pending” language to reflect G1-G8 + Source Discovery PASS and indicate that only final integration/permanent normal installation remains;
   - preserve all historical R1/R2 evidence and failed-attempt provenance rather than rewriting history.

No production source/generated payload/version source change is allowed during conflict resolution.

## 6. Pre-push AI verification without rerunning gates

First prove integration did not alter the approved production candidate.

The final AI integration tree must be byte-equivalent to `33c30bbe...` for:
- `skills/`
- `scripts/codex_marketplace_config.json`
- `plugins/codex/plugins/`
- `.agents/plugins/marketplace.json`
- `registry.json`
- `docs/SKILL_CATALOG.md`
- `VERSION`
- `setup.py`

Expected diff on these paths: none.

Then run only release/parity checks:

```bash
python scripts/build_codex_marketplace.py --validate --check --path-report
python scripts/skills.py validate
python scripts/skills.py audit --all
python -m unittest tests.test_codex_marketplace
```

Do not run generator `--write` merely to make integration pass. If `--check` says the generated publication would change, STOP: that would mean the integrated production identity is not the approved final candidate.

Required parity:
- VERSION/setup/registry/README repository identity = 5.0.7;
- Marketplace = workflow-core 0.3, web-development 0.2, ai-skills-core 0.4;
- generated manifests match source config;
- affected plugin changelogs match released versions;
- README matches those source versions.

No full-suite/Gate replay unless a production semantic diff is discovered.

## 7. Bridge release closure

After fast-forwarding exact candidate history, make a docs-only release metadata commit:

- README: replace “0.8.5 candidate / not main merge” wording with current integrated version 0.8.5;
- CHANGELOG: mark 0.8.5 as released on 2026-09-22;
- preserve pyproject 0.8.5 and `ai_bridge_kit.__version__=0.8.5`;
- production Host/Human Gate code and templates remain byte-identical to `96a8ea1b...`.

Focused mechanical checks only:
- pyproject/runtime version parity = 0.8.5;
- README/changelog = 0.8.5;
- production source diff candidate -> release commit is empty outside README/CHANGELOG.

Do not rerun 372 tests or live G1 smoke for a docs-only release metadata commit.

## 8. Main push order and production identity

Prepare and freeze both exact release commits before any main push.

Push order:
1. Bridge main first.
2. Verify remote Bridge main is the exact frozen 0.8.5 release commit.
3. AI_Skills main second.
4. Verify remote AI main is the exact frozen 5.0.7 release commit.

If Bridge push fails or remote main raced, do not push AI.

If AI push later fails because main raced, do not force/rewrite. Preserve the already valid Bridge 0.8.5 release and return Planner/Critic for the new AI drift.

After each push, normal-main identity checks replace redundant semantic gate reruns:
- exact remote SHA;
- source/release version;
- production tree/hash equivalence to the already approved candidate;
- README/changelog/generated parity.

## 9. Permanent normal Bridge upgrade

Only after Bridge main is exact integrated 0.8.5.

Exact normal source root:
`/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit`

Current pre-release observed identity:
- HEAD `cb77b1cc5a1fce097a38066d2db452291e359852`
- version 0.8.2
- executable `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge`

Authorized final behavior after the user sends the approved Kickoff:
- require the canonical root to have no unrelated user-owned dirty changes;
- `git fetch origin main` and `git pull --ff-only origin main` to the exact released Bridge main;
- no stash/reset/restore/rebase;
- inspect the executable/shebang/Python environment and refresh the existing local editable installation from that canonical root using the same environment, e.g. the repo-supported `pip install -e <canonical-root>`; no alternate provider/source;
- verify `ai-bridge where` points to the canonical root and imported/runtime version is 0.8.5.

If the canonical root has unrelated dirty work that prevents the exact upgrade, STOP rather than silently installing from the temporary integration worktree.

## 10. Permanent real CODEX_HOME install

Exact target:
- host: `c0824.ll.unc.edu`
- user: `aereinh`
- CODEX_HOME: `/overflow/htzhu/mingcheng_new/.codex`

This is a new current-user-visible bounded authorization in the final Kickoff.

After normal Bridge 0.8.5 identity is verified:
- run the normal integrated `ai-bridge host install --codex-home /overflow/htzhu/mingcheng_new/.codex`;
- allow its existing timestamped backup/manifest;
- run normal `ai-bridge host validate`;
- expected permanent desired state includes `features.default_mode_request_user_input=false`, 0.8.5 managed AGENTS block and candidate rules, while unrelated config is preserved.

Unlike the pre-release smoke, successful final install is **not restored**; it is the permanent released Host state.

Because the exact production Host bytes already passed the real-user G1 final review, do not repeat Human Gate token/Plan/agent-resolvable smoke if integrated 0.8.5 production bytes are unchanged. Normal install identity + Host validate is the release closure check.

If permanent install/validate fails:
- preserve failure and backup locator;
- do not broaden Host policy or retry indefinitely;
- restore the immediate pre-install Host state if the existing backup can do so safely and no concurrent drift exists;
- source/semantic repair => return Planner/Critic.

## 11. Final closure evidence and task completion

After both main pushes and permanent normal Bridge/Host validation succeed, update AI main task evidence:

`results/056_product_delivery_discipline/FINAL_INTEGRATION_RELEASE_CLOSURE.md`
and a small machine-readable JSON companion.

Update `RESULT.md` / `evidence_manifest.json` so they truthfully record:
- exact AI release main commit;
- exact Bridge release main commit;
- candidate/tree equivalence;
- repository/plugin versions;
- README/changelog/generated parity;
- normal Bridge root/executable/version;
- permanent Host backup locator and validate PASS;
- G1-G8 + Source Discovery prior PASS locators;
- no repeated paid/Terra/full gate runs;
- `SOURCE_DEFECT_DISCOVERED=NO`;
- overall 056 achieved only at this point.

This final evidence-only commit may be pushed non-force to AI main. It does not invalidate the approved production candidate.

## 12. Exact reviewed-branch cleanup

The final Kickoff may authorize deletion of only:

- AI remote `reviewed/056_product_delivery_discipline`
- Bridge remote `reviewed/056_product_delivery_discipline`

and only after:
- the exact reviewed heads are ancestors of their corresponding main histories;
- both main release identities are verified;
- permanent Host validation passes;
- final closure evidence is pushed.

No other branch deletion. No force. Local historical worktrees are not automatically deleted by this package.

## 13. Explicitly not authorized / not required

- Git tag creation;
- GitHub Release creation;
- package-registry publish;
- deployment;
- paid API/Terra;
- product repo writes;
- new Gate/successor;
- production redesign;
- force push/remote remap/history rewrite;
- rerunning final gates just because release/evidence SHAs change.

`NEXT_HANDOFF=CRITIC`
