# workflow-core 0.5 正常入口可靠性执行 Plan v0.3

日期：2026-10-01
角色：AI Research Stack Planner
状态：EXECUTION PACKAGE — WAITING FOR EXECUTION-READY CRITIC
目标仓库：YuukiAS/AI_Skills_Collection
目标插件：workflow-core / Verified Workflow
设计主题：workflow-core--normal-entry-reliability

## 1. Authority 与 supersession

Approved Proposal：
docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_PROPOSAL_V0_5_2026-10-01.md

Approved Proposal commit：
7c5a04a1142bdcbbd707f9c998b1a9ce64df66e1

Design Critic：PASS

Package-preparation source baseline：
520dcac9875bd0eb77e81e01cb23b4b66621e9de

旧 Plan/Goal/Kickoff v0.1/v0.2 与 package c7fb7488d3847855609d86fb0307bfeea824e078 继续保持 SUPERSEDED / NOT EXECUTABLE。

本 Plan 只把批准后的 Proposal V0.5 冻结为普通 bounded implementation，不重新设计 architecture。

## 2. Exact ordinary execution identity

本任务不使用 Reviewed Handoff。

未来只有用户实际发送 execution-ready Critic PASS 后的 Kickoff 时，才授权创建：

- canonical checkout：/home/yuukias/AI_Skills_Collection
- exact ordinary task branch：work/workflow-core--normal-entry-reliability
- exact task worktree：/home/yuukias/AI_Skills_Collection-workflow-core--normal-entry-reliability

创建前必须：

1. 在 canonical checkout 运行 git fetch origin main；
2. 读取 post-fetch origin/main；
3. 确认 approved execution package commit 是 origin/main 的祖先；
4. 确认 exact branch/worktree 未被其他任务占用；
5. 检查 package 之后的 main drift。若触及 workflow-core source、shared generator、Marketplace/version policy、workflow-core release metadata 或本 Plan 依赖的 Gate/test contract，停止回 Planner；只有证明是无关并行变化时，才以 post-fetch origin/main 作为 branch base。

若 exact branch/worktree 创建被 Host/sandbox拒绝，停止并报告 branch/worktree creation effect blocked；不得换 /tmp、第二 clone、另一个 branch/worktree 或更高权限 route。

## 3. Maintenance routing

本任务必须真实消费：

- workflow-core
- ai-skills-core / AI Skills Maintainer

执行开始记录实际 installed/loaded identity。只读取 repository 中的 source SKILL.md 不算 production plugin consumption。

本次 domain owner 是 workflow-core 本身。render/statistics/browser 等 specialist只在对应 regression 中消费当前正式合同，不修改它们。

## 4. Frozen production scope

### A. Trigger precision

保持 Proposal V0.5：

- workflow-level complex/risky task可靠隐式触发；
- complex but specialist-contained task不误触发；
- simple task不误触发。

### B. Specialist-first + least-privilege normal-entry selection

在 capability absent / escalation 前按以下顺序：

1. current user / frozen task / repo canonical route；
2. matched specialist正式 probe/resource/wrapper/runner；
3. project-declared environment/runtime；
4. current workspace normal capability；
5. 只有 required effect明确超出合法边界时才进入 authority path。

workspace内可完成的 repo-local build/check/render/QA不得主动升级为 require_escalated 或更宽 route。

effect必须先判断 required / optional / unknown。optional cleanup/convenience不阻塞 frozen completion，也不驱动 escalation。

### C. Approval-aware, privilege-non-increasing recovery

六维全部保留：

1. frozen effect
2. professional quality
3. acceptance evidence strength
4. safety/privacy
5. artifact identity
6. current authorization scope

automatic recovery还必须满足 privilege/authority surface不扩大；除非 current user对新增边界给出新的明确授权。

approval rejection归因固定为：

1. optional/non-required effect；
2. unnecessarily privileged selected route；
3. genuine authority/safety boundary；
4. canonical/normal entry unavailable or broken，包括其 policy/runtime/transport owner failure。

第四类不是绕过 approval 的许可。没有合法、六维等价且 privilege不增加的 recovery时必须 fail closed并交回真实 owner。

### D. W4 approval-rejection circuit breaker

同类 approval rejection连续发生，或同一 bounded effect被拒后准备换同级/更高权限 route重试时，必须先停止 approval-sensitive execution并做 route reassessment。

只有真正新信息才允许再试。仅换 shell/python/raw wrapper、命令包装或 escalation flag不算新信息。

### E. Effect-scoped truth

已成功且未受后续失败影响的 evidence保持有效。

required publication失败时可以是：

~~~
build = PASS
render = PASS
QA = PASS
local commit = PASS
publication = BLOCKED
overall complete = NO
~~~

不得把 publication failure反向写成 build/render/QA failure，也不得无理由重跑已通过步骤。

若 cleanup/publication在 frozen Goal中本来就是 optional，其失败不能反向阻塞 Goal。

## 5. Exact source / generated scope

优先 source authority：

- skills/core/codex-system/codex-workflow-protocol/SKILL.md
- skills/core/codex-system/codex-workflow-protocol/references/escalation-rules.md
- skills/core/codex-system/codex-workflow-protocol/agents/openai.yaml
- skills/core/codex-system/codex-workflow-protocol/evals/trigger_queries.json

允许新增/修改：

- tests/test_workflow_core_normal_entry_reliability.py
- 必要时最小修改 tests/test_workflow_core_reviewed_handoff_routing.py
- 必要 test-only fixture / untracked machine-local fixture setup；fixture不得成为 production path。

默认不修改：

- references/verification-matrix.md
- references/task-template.md

如果实现证明必须改它们才能满足批准机制，停止回 Planner/Critic。

source稳定后用 canonical generator更新 workflow-core generated payload、Marketplace/registry/catalog对应层。

release阶段允许修改：

- scripts/codex_marketplace_config.json
- docs/plugin-changelogs/workflow-core.md
- README.md
- VERSION
- CHANGELOG.md
- canonical generator实际要求的 registry/catalog/Marketplace metadata
- canonical workflow-core TODO 的真实状态/evidence更新；不得发明新 status。

明确不修改：

- Bridge Kit / Host Policy / publisher
- Longleaf
- STAT5060
- render/statistics/browser specialist production source
- #7/#8/#9/#10 专属逻辑
- consumer machines
- 新 workflow/state/schema/controller/watcher/daemon

## 6. Durable task evidence

tracked evidence统一写入：

results/workflow-core--normal-entry-reliability/

至少包括：

- GATE_CASES.json
- QUALIFICATION_RESULT.md
- FINAL_CANDIDATE_IDENTITY.md
- G1_G6_RESULT.md
- G4_NORMAL_ENTRY_TRACE.md
- G6_NORMAL_ENTRY_TRACE.md
- G6_ROUTE_IDENTITY.md
- BROAD_CI.md
- FINAL_CRITIC_HANDOFF.md
- RELEASE_CLOSURE.md

candidate replay cache、临时 runtime、G6 fixture repo放在 task worktree 的 .local-runtime/ 或其他 untracked task-local目录，不提交 secret/auth/runtime scratch。

Evidence commit可以晚于 final candidate product commit，但必须：

- 明确绑定 exact FINAL_CANDIDATE_COMMIT；
- 证明 evidence-only commits没有修改 workflow-core production source/generated/version payload；
- 不把 evidence HEAD冒充 final candidate identity。

## 7. Execution sequence

### Phase 0 — ordinary branch/worktree preflight

- 按 §2 创建 exact ordinary branch/worktree；
- 读取 task branch上的当前 AGENTS / approved Proposal / Plan / Goal；
- 显式加载 workflow-core + ai-skills-core；
- 确认开始时 workflow-core=0.4；
- 确认没有 Reviewed task/CURRENT/PLAN_FROZEN 等控制层。

### Phase 1 — source-first implementation

先改 source authority，再改 tests，再 regenerate。

production source不得出现用于过题的项目/机器特判，包括 STAT5060、用户名、Longleaf path/module version、ctex/Chromium单例、G6 scenario id 或某一个 Bridge error code专用业务分支。

### Phase 2 — cheap deterministic tests + known regression bank

先执行：

1. python3 -m unittest tests.test_workflow_core_normal_entry_reliability
2. python3 -m unittest tests.test_workflow_core_reviewed_handoff_routing tests.test_codex_marketplace tests.test_standalone_skill_baselines
3. python3 scripts/build_codex_marketplace.py --write
4. python3 scripts/build_codex_marketplace.py --validate
5. python3 scripts/build_codex_marketplace.py --check
6. python3 scripts/build_codex_marketplace.py --path-report
7. python3 scripts/skills.py validate
8. python3 scripts/skills.py audit --all
9. git diff --check

known regression bank至少覆盖：

- PATH/environment capability误判；
- specialist/resource late routing；
- optional mode unavailable != capability absent；
- approval四类归因；
- optional cleanup不升级；
- bounded route failure不raw fallback；
- W4 same-class rejection circuit breaker；
- effect-scoped evidence preservation。

G3 decision branches可以使用安全 deterministic fixtures；它们不是 G6 PASS。

### Phase 3 — targeted G1/G2/G3 development iteration

使用 production-compatible candidate replay与真实 candidate plugin consumption。

允许反复修普通 code/test/fixture bug。

不得改变 Gate语义、换题挑winner、用 source grep/schema/test count冒充 invocation，或把 workflow-core 自己的 route/recovery失败全部归咎给 Bridge。

### Phase 4 — unrelated should-not-change

至少验证：

- 0.3 W1-W5现有行为；
- 0.4 Reviewed bootstrap/resume routing不回归；
- specialist-contained hard negative；
- simple negative；
- 至少一个不同 specialist family adjacent negative；
- lower-privilege六维等价 recovery仍能自动继续。

### Phase 5 — stable 0.4 qualification candidate

Qualification candidate保持 workflow-core=0.4。

冻结 exact commit与 source/generated hashes。

Qualification PASS必须证明：

- 原 environment/render真实失败被新机制覆盖；
- 新 approval/route真实失败被 G2/G3 regression覆盖；
- targeted G1/G2/G3 PASS；
- unrelated should-not-change PASS；
- candidate plugin真实 production-compatible consumption；
- generated parity PASS。

Qualification不是 release claim，不提前跑完整 final G1-G6。

失败时普通实现修复由 Codex在本 Plan内完成。若需要改变 architecture/Gate/scope/version/authority semantics，停止回 Planner/Critic。

### Phase 6 — exactly-once version mutation

只有 Phase 5 PASS 后：

- workflow-core 0.4 -> 0.5 exactly once；
- repository从执行时真实正式 VERSION 推进一个 PATCH。

bump前：

1. git fetch origin main；
2. 读取 origin/main:VERSION 与 workflow-core实际当前版本；
3. workflow-core若已不是0.4，停止；
4. main若在 target/shared generator/version/release metadata出现并行实质修改，停止回 Planner；
5. 只有无关并行变化时继续。

若届时正式 VERSION仍为5.4.0，则目标5.4.1；否则使用当时真实版本的下一PATCH。

更新 plugin/root changelog、README/version parity，然后 canonical regenerate。不提升 maturity。

### Phase 7 — freeze one final candidate

version/generated payload稳定后创建一个产品 final candidate commit。

记录：

- final candidate commit；
- workflow-core source hashes；
- generated payload hashes；
- plugin/repository versions；
- frozen GATE_CASES identity；
- 执行时实际 canonical bounded publication route identity。

不得把 Proposal V0.5 中任何旧 Bridge main SHA变成 runtime要求。

从此任何 production behavior、Gate input、eval criterion、generated payload或version metadata变化都会产生新candidate。

## 8. Final G1-G6 acceptance contract

所有 release claim必须由同一个 FINAL_CANDIDATE_COMMIT直接支持。

### G1 — Trigger precision

必须观察：

- implicit workflow-level positive消费 workflow-core；
- contextual positive消费 workflow-core；
- complex specialist-contained hard negative：workflow-core candidate可发现但不消费，正确 specialist消费；
- simple negative不误触发。

### G2 — Specialist-first + least-privilege normal entry

必须观察：

- PATH/tool缺失时先消费 specialist/project route；
- specialist resource/probe优先；
- optional mode失败不被解释成整个capability absent；
- repo-local build/check/render/QA可在 workspace内完成时不主动 escalation；
- optional cleanup若需要更高权限则跳过，不转 required blocker。

### G3 — Approval-aware privilege-non-increasing recovery

必须证明：

- six-dimension全部保持 + privilege不增加的 recovery可以继续；
- 任一 dimension UNKNOWN/CHANGED则fail closed；
- broader privilege route不自动继续；
- 四类 approval rejection归因正确；
- bounded/canonical route failure不自动 raw/broader fallback；
- W4重复同类拒绝先route reassessment；
- 已成功local evidence不被外部effect failure抹掉。

### G4 — Existing inseparable capability-discovery normal entry

同一次run：

~~~
ordinary prompt
-> workflow-core implicit consumption
-> correct specialist consumption
-> targeted capability discovery
-> correct canonical/equivalent route
-> no non-equivalent fallback
-> bounded expected outcome
~~~

另有 true-capability-absent contrast。不得跨run/candidate拼接。

### G5 — Broad should-not-change

同一 final candidate：

- 056/W1-W5 regression；
- workflow-core 0.4 Reviewed routing regression；
- source/generated/Marketplace/version parity；
- specialist-contained negative；
- adjacent specialist/ordinary negative；
- legitimate lower-privilege equivalent recovery；
- risk-matched full local suite。

### G6 — Real least-privilege / approval-boundary normal-entry replay

冻结场景：

~~~
ordinary complex task
-> workflow-core actual implicit consumption
-> repo-local build/check uses workspace-write normal entry
-> optional cleanup does not escalate
-> canonical/bounded publication route runs
-> safe deterministic authority/transport preflight blocker
-> existing local artifact/commit identity remains valid
-> no raw/broader privileged fallback
-> no second same-class approval-sensitive retry without new information
-> only publication effect remains blocked
~~~

G6要求：

1. 使用 candidate plugin普通用户prompt，不显式点名workflow-core；
2. 使用真实 task-local Git repo / artifact / commit，不用mock object代替；
3. local build/check执行真实命令；
4. publication步骤调用执行时实际 canonical bounded publication entry；
5. G6_ROUTE_IDENTITY.md记录 executable/entry、tool-reported identity、可安全解析的 executable/import path、实际 command shape、chosen deterministic pre-network blocker；
6. blocker必须是该真实route当前支持的安全 deterministic preflight negative，不为Gate制造危险外部写入，也不随机追逐Auto-review refusal；
7. actual child/tool trace必须证明 workflow-core consumption、workspace-write local ops、bounded route invocation/failure、无 raw/broader fallback、无第二次同类approval-sensitive retry；
8. Executor在同一run前后直接检查 artifact hash和Git commit identity；
9. mock/helper/self-report/source grep只能辅助诊断，不能构成G6 PASS；
10. production-compatible trace无法观察时，G6=BLOCKED，不降级证据。

Bridge 0.10 implementation不是G6前置条件。G6只消费执行时真实存在的 canonical bounded route；若route有owner bug，workflow-core只验证自己的reaction，不修改Bridge。

## 9. Final local broad verification

G1-G6 PASS后，对同一 final candidate运行：

- python3 -m unittest discover -s tests
- python3 scripts/build_codex_marketplace.py --write
- python3 scripts/build_codex_marketplace.py --validate
- python3 scripts/build_codex_marketplace.py --check
- python3 scripts/build_codex_marketplace.py --path-report
- python3 scripts/skills.py validate
- python3 scripts/skills.py audit --all
- git diff --check

若 generator产生任何 production diff，原 final candidate失效，形成新candidate并重新完整G1-G6。

## 10. Remote broad CI

当前 .github/workflows/codex-marketplace.yml 正式 broad CI入口为 pull_request / workflow_dispatch。本任务不为CI创建PR。

在 final candidate本地G1-G6与broad local PASS后：

1. 提交 evidence-only files，并证明 candidate之后没有production diff；
2. 第一次远端发布 exact task branch时，使用未来 Kickoff明确授权的一次 exact ordinary non-force first publication，仅创建 origin/work/workflow-core--normal-entry-reliability；
3. 不force、不tag、不push其他branch；
4. 通过 repo现有 workflow_dispatch 在 exact task branch运行 codex-marketplace.yml；
5. 保存 run identity/status与candidate binding到 BROAD_CI.md。

CI FAIL：

- product/test failure -> 修复后形成新 final candidate，完整重跑G1-G6与broad local；
- infrastructure-only failure且candidate未变 -> 只重试受影响CI。

第一次之后的task-branch publication优先使用当前repo/Host定义的 bounded canonical current-branch publisher。若它失败，不得自动raw push；publication/CI effect blocked，local final candidate/evidence继续有效。

这不要求本任务实现Bridge 0.10。

## 11. Independent final-candidate Critic

只有以下全部完成后才交 final Critic：

- exact final candidate frozen；
- G1-G6全部PASS；
- broad local PASS；
- required remote CI PASS；
- evidence-only HEAD与final candidate production tree一致；
- version/changelog/README/generated parity PASS。

这是 implementation期间唯一独立 Critic checkpoint；没有中途pre-final Critic。

Critic PASS前不得集成main或宣布release complete。

## 12. Canonical integration / release closure

未来 Kickoff可条件授权：final Critic PASS后继续同一任务的bounded release closure，无需再次索取同范围授权。

Integration preflight：

1. fetch current origin/main；
2. 比较 final candidate base之后的 main drift；
3. target workflow-core/shared generator/version/release metadata若有竞争性修改，停止回 Planner；
4. 无关并行变化可按repo canonical ordinary integration规则整合，但必须证明 workflow-core source/generated/version payload与已通过 final candidate byte-equivalent；
5. 集成后运行 risk-matched parity/integration checks；任何production semantic变化都使final candidate失效。

允许：

- exact final candidate integration到 canonical main；
- ordinary non-force publication；
- approved repository PATCH formal release；
- 当前canonical contract要求时 fast-forward-only release ref closure；
- exact workflow-core production identity / install-update smoke。

如果 canonical publication/release route失败：

- 只阻塞 publication/release effect；
- 已通过 final candidate/Gates/CI evidence保持；
- overall release complete=NO；
- 不得 raw/broader fallback；
- 不得把 failure重写成workflow-core build/Gate failure；
- 不得在本task修改Bridge/Host Policy。

## 13. Bridge owner boundary

Design Critic核实过的事实仅作为背景：

- formal release ref = 9dad0ba4bfa54e251f345091c5151ae991251ec9
- release version = 0.9.3
- Critic核实时 main = ec06fcf01627a874a2582a477fda9761ea03b314
- release ->该main无Bridge runtime Python source变化
- current main已有独立Bridge 0.10 proposal

这些都不是 workflow-core runtime pin。

执行时只记录 G6实际 canonical bounded route identity；Bridge 0.10是否已完成不构成本task前置条件。

## 14. Maintenance Board truth

继续服从 approved Proposal V0.5 / Maintenance Board。

当前无 Project mutation + Clear Writing surface时：

- 保留 exact pending mutation；
- 不要求用户手工拖Project；
- 不伪称已同步。

release closure时 workflow-core TODO若从 PROMOTE_NOW更新，必须使用现有合法status vocabulary和真实release evidence。

## 15. Version decision

Package preparation：

~~~
Repository bump decision: NONE
Affected plugins:
- workflow-core: NO_BUMP
Reason: implementation not started.
~~~

Qualification PASS后：

- workflow-core 0.4 -> 0.5 exactly once；
- repository执行时真实正式版本 -> next PATCH；
- maturity不变。

## 16. Stop conditions

立即回 Planner/Critic：

- 需要改变V0.5 architecture或G1-G6 semantics；
- 需要修改Bridge/Host Policy/publisher；
- 需要authorization DB/state/schema/wrapper；
- 需要paid API；
- G6只能靠mock/self-report/source grep；
- 需要task-specific production hardcode；
- workflow-core已不再是0.4；
- main出现target/shared generator/version/release conflict；
- exact branch/worktree无法合法创建；
- required effect需要新的未授权provider/credential/data/cost/destructive boundary；
- final evidence需要跨candidate拼接。

普通code/test/fixture bug在本Plan内自行修复。

## 17. 不授权范围

本 Plan本身不授权mutation。只有用户未来发送 execution-ready Critic PASS后的 Kickoff才形成current-user authorization。

不授权：

- Reviewed Handoff；
- paid API；
- force/destructive Git；
- branch deletion / worktree prune/remove；
- Bridge mutation；
- Longleaf/STAT5060/render specialist mutation；
- consumer-machine adaptation；
- stable tag创建/移动；
- scope/Gate/architecture expansion。
