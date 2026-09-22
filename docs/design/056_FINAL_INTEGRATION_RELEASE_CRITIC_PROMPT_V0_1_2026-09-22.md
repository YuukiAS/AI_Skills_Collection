# 056 Final Integration / Release — Critic Prompt v0.1

你是 AI Research Stack 的长期独立 Critic thread。

继续 historical task：

`056_product_delivery_discipline`

人类可读名称：

交付工作流可靠性基线

当前只审：

`FINAL_INTEGRATION_AND_RELEASE_EXECUTION_READY_PACKAGE_V0_1`

Reviewed package commit：

`a90b92bc4931b3f1d8cca62fa9d67ba084ee1a66`

这不是重新设计 056。

## 1. 必须读取

实际读取 AI_Skills 最新 main：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`

然后以 exact package commit `a90b92bc4931b3f1d8cca62fa9d67ba084ee1a66` 读取：

- `docs/design/056_FINAL_INTEGRATION_RELEASE_PLAN_V0_1_2026-09-22.md`
- `docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_1.md`
- `docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_1.md`
- `docs/design/056_FINAL_INTEGRATION_RELEASE_REVIEW_PACKAGE_V0_1_2026-09-22.md`

同时实际读取两个 repo 当前 main / exact reviewed branch，独立复核 drift。

## 2. Frozen implementation identity

AI_Skills:
- repo: `YuukiAS/AI_Skills_Collection`
- reviewed branch: `reviewed/056_product_delivery_discipline`
- approved production candidate:
  `33c30bbe0dd528031a23d379905cd00d6b65bc1f`
- final evidence HEAD:
  `b6f675869449df8daa86a6abcf527fbb72c66e64`
- target release:
  - repository 5.0.7
  - workflow-core 0.3
  - web-development 0.2
  - ai-skills-core 0.4

Bridge:
- repo: `YuukiAS/GPT_Codex_AI_Bridge_Kit`
- reviewed branch: `reviewed/056_product_delivery_discipline`
- candidate:
  `96a8ea1b58ebe6f9b7c5c46c43995666251911fe`
- target release: 0.8.5

Latest planning baselines before package:
- AI main `7a6d247e04b05d4371296a9415621b468ed492ce`
- Bridge main `9d2da9f485f26ca51842a1909a276cb44f73351a`

The package commit itself is a docs-only AI main advance and must not create a self-triggering review loop.

## 3. Already PASS — do not reopen without new direct semantic evidence

Latest independent final review says:

- G1 PASS
- G2-G8 PASS
- Source Discovery PASS
- real-user HUMAN_ONLY reply -> same Goal exact-once resume PASS
- post-action closure PASS
- Plan-mode native request_user_input non-regression PASS
- agent-resolvable no-false-prompt PASS
- Host restore PASS
- SOURCE_DEFECT_DISCOVERED=NO
- Terra NOT REQUIRED

Do not request another Human Gate token smoke, Plan smoke, G2-G8 replay, Terra, paid review or full suite solely because integration/release/evidence SHAs advance.

## 4. Planner drift findings to independently verify

### AI

At planning time:

- main and reviewed histories diverged;
- merge base:
  `9f1c0d32abf49e674bcc7cab0e7287ed714a1199`;
- reviewed ahead 9 / behind 16;
- the exact changed-file intersection between main-side drift and reviewed-side changes was only:
  `docs/plugin-todos/workflow-core.md`;
- main-side drift was docs/planning/TODO only and did not touch 056 production/version/release slots.

Planner's proposed conflict rule:
- merge reviewed history into latest main with a real merge commit;
- no rebase/squash/cherry-pick/history rewrite;
- only the pre-audited workflow-core TODO conflict may be resolved;
- preserve every newer main-only TODO item;
- preserve reviewed 056 promoted semantics;
- mark the 056 delivery/Human-Gate and least-priv absorption as released in 5.0.7;
- keep explicitly deferred post-056 items deferred;
- any other conflict => STOP Planner/Critic.

Also verify:
`33c30bbe...` -> `b6f67586...` contains only task evidence plus `tests/test_056_product_delivery_discipline_gates.py`, no production source change.

### Bridge

At planning time:
- main `9d2da9f...` is direct ancestor of candidate `96a8ea1b...`;
- reviewed ahead 3 / behind 0;
- no conflict;
- candidate production source already passed real Host/user gates.

Planner proposes fast-forward candidate history, then only README/CHANGELOG release metadata.

## 5. Critic focus A — candidate equivalence and gate reuse

Planner proposes no repeated semantic gates if final integrated production bytes remain exactly equivalent to the approved candidates.

For AI, integration must prove no diff vs `33c30bbe...` on:
- `skills/`
- `scripts/codex_marketplace_config.json`
- `plugins/codex/plugins/`
- `.agents/plugins/marketplace.json`
- `registry.json`
- `docs/SKILL_CATALOG.md`
- `VERSION`
- `setup.py`

Then only:
- Marketplace validate/check/path-report;
- skills validate/audit;
- focused `tests.test_codex_marketplace`;
- release/version/README/changelog parity.

For Bridge, post-candidate release commit may change only README/CHANGELOG; production source must remain byte-identical.

Independently judge whether this is enough and whether any proposed check is too weak or unnecessarily repeats already frozen gates.

If integration conflict resolution changes workflow-core, Frontend Design, ai-skills-core, Bridge Host/Human Gate behavior or normal routing, the shortcut is invalid. Require only the affected minimal replay after returning Planner/Critic.

## 6. Critic focus B — formal release semantics

Planner found both GitHub repositories currently expose zero GitHub Release objects.

Current AI repo version policy treats repository releases through canonical VERSION/plugin versions, root/plugin changelogs, README and installable/generated main identity. Bridge similarly uses version/changelog/main.

Planner therefore defines this 056 formal release as:
- main integration + verified release metadata and normal installation identity;
- NOT a new GitHub tag/GitHub Release/package-registry publication mechanism.

Kickoff keeps forbidden:
- tag creation;
- GitHub Release creation;
- package-registry publish;
- deploy.

Do an independent targeted official GitHub check. GitHub documents Releases as a separate tag-based packaging surface and merge commits as preserving full branch history.

Judge whether 056 should preserve the repositories' actual existing release practice rather than inventing the first GitHub Release/tag mechanism.

## 7. Critic focus C — release metadata truth

AI reviewed branch currently already has:
- VERSION 5.0.7;
- README 5.0.7;
- workflow-core 0.3;
- web-development 0.2;
- ai-skills-core 0.4;
- plugin changelogs.

But root CHANGELOG still says “release candidate” and contains stale text saying real Host/live Host smoke remains pending.

Plan requires:
- formal release date 2026-09-22;
- remove candidate wording;
- replace stale Host-pending note with actual G1 final closure;
- preserve evidence history;
- update RESULT/evidence manifest truthfully.

Bridge reviewed README still says 0.8.5 candidate/not merged; CHANGELOG 0.8.5 has no release date. Plan formalizes those after fast-forward without production source changes.

Check this closure for completeness against README/changelog/version policy.

## 8. Critic focus D — exact current-user authorization

If approved, user sending the exact Kickoff would authorize:

- exact two temporary integration worktrees:
  - `/overflow/htzhu/mingcheng_new/AI_Skills_Collection-056-final-integration`
  - `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit-056-final-integration`
- exact reviewed-history integration;
- ordinary non-force pushes to both mains;
- no force/remap/rewrite;
- normal Bridge canonical-root ff-only upgrade;
- refresh of the existing editable local Bridge install in its current Python environment when needed;
- permanent Host install/validate only for:
  - host `c0824.ll.unc.edu`
  - user `aereinh`
  - CODEX_HOME `/overflow/htzhu/mingcheng_new/.codex`;
- final AI main evidence-only closure commit;
- deletion only of the two exact remote `reviewed/056_product_delivery_discipline` branches, only after ancestry/main/Host/final-evidence closure.

Check that the Kickoff does not accidentally authorize arbitrary branches, arbitrary main writes, other CODEX_HOME, other provider/account/credential changes, product repo writes, tag/release asset publication, or destructive Git.

## 9. Critic focus E — normal Bridge 0.8.5 upgrade

Current pre-release normal identity:

- canonical root:
  `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit`
- previously observed HEAD:
  `cb77b1cc5a1fce097a38066d2db452291e359852`
- version 0.8.2
- executable:
  `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge`

Plan:
1. only after Bridge main is integrated 0.8.5;
2. require canonical root free of unrelated dirty user work;
3. ff-only pull exact main;
4. inspect existing executable/shebang/Python environment;
5. refresh existing editable install from the canonical released root in that same environment when needed;
6. verify normal `ai-bridge where` + runtime/package version 0.8.5;
7. never install permanently from reviewed/temp worktree.

Judge whether this is the minimal safe normal-install closure.

## 10. Critic focus F — permanent real Host install

Pre-release candidate already passed the exact real-user G1 gate and then restored Host prestate.

Final package now authorizes, only after integrated normal Bridge 0.8.5:
- normal `ai-bridge host install --codex-home /overflow/htzhu/mingcheng_new/.codex`;
- its existing timestamped backup;
- normal `host validate`;
- on success leave released 0.8.5 Host state permanently installed.

No repeated token/Plan/agent-resolvable smoke if production bytes are candidate-equivalent.

Failure:
- preserve evidence and backup;
- bounded safe restore to immediate pre-install state when possible/no concurrent drift;
- no silent source repair or policy expansion.

Judge whether permanent installation is correctly separated from the already passed pre-release live gate.

## 11. Push ordering / recovery

Planner freezes both release commits first.

Proposed push order:
1. Bridge main;
2. verify exact remote Bridge SHA;
3. AI main;
4. verify exact remote AI SHA.

If Bridge push fails => do not push AI.
If AI push fails/races after Bridge success => keep valid Bridge 0.8.5 main; do not force/rewrite; return Planner/Critic.

Judge whether this bounded partial-integration recovery is preferable to dangerous rollback/history rewrite.

## 12. Branch cleanup

Only after:
- both mains exact;
- permanent Host validate PASS;
- final AI closure evidence pushed;
- exact reviewed heads are ancestors of corresponding main.

Then delete only:
- AI remote `reviewed/056_product_delivery_discipline`;
- Bridge remote `reviewed/056_product_delivery_discipline`.

Local historical worktrees are not automatically deleted.

Review whether this ordering is safe and whether branch deletion belongs in the same bounded final Kickoff.

## 13. Output

If REVISE:

Only block on a direct final-integration/release/authorization/recovery risk.

Each blocker must contain:
- STABLE_ID
- REQUIREMENT
- DIRECT_EVIDENCE
- CAUSAL_RISK
- MINIMUM_CLOSURE
- OWNER

Do not reopen already passed 056 architecture/Gates without new evidence.

Then automatically output:

`NEXT_HANDOFF=PLANNER`

and a complete `COPY TO PLANNER` prompt with this package commit and stable finding IDs.

If PASS:

Because this 056 major round previously had REVISEs, first give the user a concise human-readable closure explanation covering:
- why earlier blockers are now closed;
- actual AI and Bridge integration shape;
- why gates are not repeated after byte-equivalent integration;
- what “formal release” means here;
- exactly what permanent normal Bridge/Host effects the user will authorize;
- what remains forbidden.

Then output:

```text
APPROVED_PACKAGE_COMMIT=a90b92bc4931b3f1d8cca62fa9d67ba084ee1a66
APPROVED_PLAN_PATH=docs/design/056_FINAL_INTEGRATION_RELEASE_PLAN_V0_1_2026-09-22.md
APPROVED_GOAL_PATH=docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_1.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_1.md
APPROVED_REVIEW_PACKAGE_PATH=docs/design/056_FINAL_INTEGRATION_RELEASE_REVIEW_PACKAGE_V0_1_2026-09-22.md
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

Finally reproduce the approved Kickoff from package commit `a90b92bc4931b3f1d8cca62fa9d67ba084ee1a66` verbatim. Do not rewrite it after PASS.
