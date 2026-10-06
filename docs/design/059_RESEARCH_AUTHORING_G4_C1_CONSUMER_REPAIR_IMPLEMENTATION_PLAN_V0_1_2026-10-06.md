# 059 Research Authoring G4-C1 正常入口修复 — Implementation Plan v0.1

日期：2026-10-06  
状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW / NOT_EXECUTION_AUTHORIZATION  
Repository：`YuukiAS/AI_Skills_Collection`  
Task key：`research-authoring--formal-production-authoring`  
Execution branch：`work/research-authoring--formal-production-authoring`  
Existing task worktree：`/overflow/htzhu/mingcheng_new/AI_Skills_Collection-research-authoring--formal-production-authoring`

## 0. Authority

本 Plan 只实现已经独立 Critic PASS 的 G4-C1 failure attribution v2，不重新设计 Research Authoring。

批准的 failure attribution：

- Planner：`results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_PLANNER.md`
- Planner commit：`6a131f0cf75a342c924366ac411956e85f63341d`
- Critic：`results/research-authoring--formal-production-authoring/G4_C1_FAILURE_ATTRIBUTION_V2_CRITIC_REVIEW.md`
- Critic commit：`8aa5a2b9bdac737254e6e8527e57ff1750154b09`
- Critic result：`PASS`

批准结论：

```text
G4_C1_ATTRIBUTION=NORMAL_ENTRY_CONSUMER_PRODUCT_INTEGRATION_FAILURE
MISSING_RENDER_OWNER_RULE=NO
PREFERRED_REPAIR_LAYER=GENERATED_REPORT_AGGREGATE_ENTRY
REPAIR_REQUIRES_NEW_CANDIDATE=YES
```

当前失败候选：

`C = 1c37c0715aca0096606f24e56192b7857e72bbd6`

第一次 G4 ChatGPT stage 及其 package 永久保持 FAIL，不得重新解释或贡献后续 PASS 子证据。

## 1. 这轮真实目标

只修一个已确认的正常入口缺陷：

> standalone / skills-only ChatGPT Research Authoring 在没有批准 renderer companion 的表面收到正式 PDF 请求时，正常消费的 report aggregate 必须把“PDF/compile-derived QA 也属于 renderer mechanics”操作化，并停止在“稳定科研 source + 完整 downstream production handoff”；通用 ChatGPT runtime/file/compute 能力不得被当作 renderer 替代品。

通过后新增的真实能力不是“多一条禁令”，而是普通用户在 standalone Research Authoring 中要求正式 PDF 时，不会再因为通用运行能力存在而由 ChatGPT 自己做 XeLaTeX/Pandoc PDF、preview/QA PDF、逐页渲染或 PDF-derived QA。

这轮不修改 canonical owner。现有 owner 继续保持：

- Research Authoring：科研文档语义、组织、source 与生产 handoff；
- `render-chinese-math-pdf` /正式文档生产层：编译、字体、分页、PDF render/QA；
- Clear Writing：语言表达；
- Presentations：PPT/Beamer/slide deck。

## 2. Exact implementation surface

### 2.1 Source config — only this production behavior source

允许修改：

`scripts/codex_marketplace_config.json`

只允许修改：

```text
research-writing
-> skills[artifact_id=report]
-> workflow_notes
```

保留：

- `routing_mode=coordinator-first`
- `coordinator_artifact_id=core`
- source skill 列表
- report/paper/litcite 现有身份
- plugin version `0.3`

新增/收紧的普通生产语义必须表达：

1. standalone / 当前表面缺少批准的 renderer companion 时，formal PDF 请求在稳定 scientific source + 完整 production handoff 后停止；
2. “artifact mechanics”明确包含：
   - local / preview / QA compile；
   - XeLaTeX / `latexmk` / Pandoc-to-PDF 或等价 PDF compile；
   - PDF creation / opening / rendering；
   - page rasterization / page visual inspection；
   - `pdftotext` / `pdfinfo` / `pdffonts` 或其他 PDF-derived text/font/page QA；
3. generic ChatGPT runtime/file/compute 能力不能替代缺失的 `render-chinese-math-pdf`；
4. Markdown/LaTeX source authoring、source-only fidelity/semantic QA 和完整 Codex/downstream handoff仍然允许；
5. 需要真实 compile/render 才能判断的 layout correctness 留给 downstream renderer，不能在 standalone Chat stage自行关闭。

不得把上述规则写成只针对 G4、某个文件名或某次失败 package 的特判。

### 2.2 Focused deterministic regression

允许修改：

`tests/test_research_writing_routing.py`

至少新增 focused regression，直接从 canonical config/generated contract验证：

- renderer companion 缺失时 formal-PDF standalone route fail closed；
- QA/preview compile/render 也被定义为 renderer mechanics；
- generic runtime 不是 renderer substitute；
- Markdown-only authoring保持允许；
- stable source + downstream production handoff保持允许；
- coordinator-first / report owner没有退化；
- paper/litcite route没有因本修复被改写。

机械字符串断言只能证明合同存在，不单独证明最终用户能力。

### 2.3 Generated layer

禁止直接手改：

`plugins/codex/plugins/**`
`.agents/plugins/marketplace.json`

先改 source config，再用当前 canonical generator 重新生成并验证。

预计至少变化：

`plugins/codex/plugins/research-writing/skills/report/SKILL.md`

以及 current generator 对该 source change 真正产生的 Marketplace/generated parity 文件。

若 registry/catalog/provenance 没有真实内容变化，不为了“同步”制造无关 diff。

### 2.4 默认禁止修改

本修复默认 ZERO WRITE：

- `skills/writing/research/research-authoring-core/SKILL.md`
- `skills/writing/research/research-reporting/SKILL.md`
- paper route
- litcite route
- `profiles/research-main.json`
- `profiles/codex-research-writing.json`
- Clear Writing production source
- renderer source
- Presentations source
- Statistical Modeling source
- Bridge Kit
- frozen G4 rubric/task/baseline
- live ChatGPT Plugin
- `main` / `release`

如果实现发现 generated report aggregate 无法表达批准语义，或 normal ChatGPT selection 根本不消费 aggregate，停止并回 Planner/Critic；不得静默扩大到 canonical core/report source。

## 3. Maintenance companions

这是正式中央 plugin production refinement。Executor 必须使用当前：

```text
workflow-core
+ ai-skills-core
+ research-writing
```

其中：
- workflow-core 管阶段、停止点、证据和完成语义；
- ai-skills-core 管 source/generated parity、版本、TODO/tracking、replay、回归；
- research-writing 管领域边界。

不得新造第二套 workflow/state。

Tracking owner 已存在：

`#99 Research Authoring 正式科研文档生产收口`

Issue #99 仍为同一 maintenance action，不创建 successor Issue。

当前 Issue 文案的执行锚点已落后于 G4-C1 repair。若执行表面同时具备真实 Clear Writing invocation 与合法 GitHub Issue/Project mutation，更新 #99：
- current progress：G4 first live ChatGPT stage FAIL，failure attribution v2 Critic PASS，准备 bounded normal-entry repair；
- current anchor：本 Plan；
- next action：execution-ready Critic -> bounded repair implementation -> C2 pre-final admission；
- Project Status保持 `DOING`；
- Resolution commit保持空。

若缺少合法 reader-facing mutation能力，只记录 exact pending update，不要求用户手工维护，也不把 Issue copy 未更新当作产品实现成功。

## 4. Version / release decision

本轮修的是**尚未正式发布的 Research Authoring 0.3 candidate**。

因此：

```text
Repository bump decision: NONE
research-writing: remains 0.3 candidate
maturity: remains unclassified
root VERSION: unchanged
formal release: NO
```

不要把失败候选 C -> repaired C2 误写成 `research-writing 0.4`。0.3 尚未 release，C2 仍是同一个 0.3 improvement batch 的 repaired final candidate。

本 bounded repair 默认不改 README/changelog；当前用户可见产品承诺没有新增，只是使已批准的 standalone fail-closed 语义真正生效。Executor必须检查：
- `README checked: no update required`
- `docs/plugin-changelogs/research-writing.md checked: no update required`

如果当前文件存在与 repaired behavior 直接冲突的事实性描述，停止并回 Planner扩大 docs scope；不得临场顺手改。

## 5. Development regression before C2

先跑便宜、确定性的 regression。

至少：

1. current source/generated validation；
2. focused `tests.test_research_writing_routing`；
3. Marketplace generator parity；
4. relevant marketplace tests；
5. full unit discovery；
6. `git diff --check`。

当前 canonical equivalents 至少包括：

```bash
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_research_writing_routing
python -m unittest tests.test_codex_marketplace
python -m unittest discover -s tests
git diff --check
```

如果当前 ai-skills-core要求 registry/catalog/provenance检查，也按 current contract运行，但不用无关 generated diff冒充 capability。

### 5.1 Known-failure development replay

第一次 G4 FAIL 已经是已知 regression，不再是 fresh evidence。

在 C2 freeze 前，使用**standalone research-writing candidate only、无 renderer companion**做一次本地/候选 runtime replay，复现普通 formal-PDF report request。

可复用第一次 G4 的自然意图或公开安全等价 fixture作为 development regression。

Development replay必须证明：

- `research-writing` candidate实际被消费；
- report aggregate/core/report route evidence可定位；
- 可以生成/保持 Markdown/LaTeX source；
- 可以生成完整 downstream production handoff；
- 不创建 PDF；
- 不执行或声称 XeLaTeX/`latexmk`/Pandoc-to-PDF；
- 不做 page raster/visual inspection；
- 不运行 `pdftotext`/`pdfinfo`/`pdffonts` 等 PDF-derived QA；
- layout/render QA明确留给 downstream owner；
- Markdown-only请求仍正常；
- support-only / paper / litcite代表性 should-not-change 不退化。

这只是 development regression。即使 PASS，也不能代替 live ChatGPT G4。

如果 repaired aggregate仍在 candidate replay中自行 render/compile，停止；不得形成 C2 final candidate。

## 6. C2 freeze

只有 source、focused tests、generated parity 与 development regression全部稳定后，形成 exact candidate commit：

`C2=<new exact commit>`

C2 candidate-owned allowlist只允许本 Plan批准的 production source/test/generated变化。

C2后直到 pre-final Critic：

- 可以新增 `results/research-authoring--formal-production-authoring/**`
- 可以新增 `private/exports/research-authoring--formal-production-authoring/**`
- 不得修改 candidate-owned files。

必须保存：

- C -> C2 diff；
- generated parity；
- focused test结果；
- development replay完整 runtime证据；
- `C2..PACKET_HEAD` candidate-owned no-change proof。

## 7. C2 final Gate evidence — old evidence becomes regression

一旦 C2形成，旧 C 的 final Gate PASS不能拼成 C2 release PASS。

### G1 — rerun on C2

旧 G1 case/output变成 regression。

C2 final G1必须重新冻结一组自然 normal-entry cases，至少继续覆盖：
- report/Methods/research update/related work/existing-document revision；
- citation verify / paper lookup / local prose / README-email / PPT-Beamer / render-only / ordinary Q&A near-miss。

因为本修复正改变 report normal-entry consumer，C2 final G1必须包含：
- standalone formal-PDF report request；
- renderer companion absent；
- ordinary natural wording，不添加“不得 XeLaTeX”这类 test-only command blacklist；
- 真实 runtime必须停在 source + production handoff。

### G2 — new fresh C2 report task/delta

旧 DII two-phase final evidence只作 development/regression。

不得把已经看过的 DII final task重新标 fresh。

C2形成后，由 Planner在 pre-final packet中冻结：
- 新的真实 report-family task；
- exact source/ref；
- Phase 1 raw evidence scope；
- Phase 2 delta identity，Phase 1不可见；
- 同一 frozen G2 rubric；
- Reviewer完整材料访问方式。

Executor不得自行挑“最好写”的 final report task。

### G3 — C2 direct final evidence

旧 MoSAIC final evidence只作 regression/should-not-change。

C2必须直接通过 G3。若现行 frozen G3继续要求 fresh manuscript task，则已经看过的 MoSAIC final task不能重新标 fresh。

C2形成后，由 Planner冻结新的真实 manuscript production task、source/ref、venue/project authority、按需 package subset、rubric与Reviewer access。

### G4 — full C2 rerun

第一次 G4 package永久 FAIL，不贡献 PASS subfinding。

frozen G4 task/rubric/semantic baseline保持不变；不因修复已知失败而加入 evaluation-only command blacklist。

最终 G4必须：

1. 从 exact C2重建 standalone ChatGPT wrapper；
2. 后续经用户**单独 bounded authorization**更新现有 live Plugin；
3. 使用普通 frozen natural ChatGPT request；
4. 产生全新的 Chat-stage package；
5. 独立 Chat-stage review PASS；
6. 只有 Chat PASS 后才进入 Codex production/render；
7. exact C2 `research-main`生产真实 PDF；
8. renderer QA + post-render Research Authoring scientific QA；
9. 独立最终 G4 review。

## 8. Final-task freeze ownership and pre-final Critic

本 bounded repair implementation不让 Executor选择新的 final holdout。

顺序冻结为：

```text
approved repair package
-> Executor implements bounded repair
-> deterministic + development regression
-> exact C2 candidate commit
-> STOP to Planner
-> Planner freezes new C2 G1 case bank + fresh G2 task/delta + fresh G3 task
   and binds unchanged frozen G4 task/rubric/baseline
-> independent pre-final Critic reviews C2 + full frozen final packet
-> only after PASS may C2 final Gates start
```

所以首次 Executor stop状态应是：

```text
C2_CANDIDATE_READY=YES
FINAL_GATES_NOT_STARTED=YES
FINAL_TASKS_NEED_PLANNER_FREEZE=YES
NEXT_HANDOFF=PLANNER
```

这不违反“C2 -> pre-final Critic -> final Gates”；Planner task-freeze是 pre-final packet准备的一部分，不是新的产品设计轮次。

## 9. Live Plugin boundary

本 Kickoff不授权任何 Plugin Creator mutation。

当前 live identity：

```text
plugin_id = plugins_6ac4471b735881918c17cd310f262429
current failed release = pluginrel_6ac4471c7b90819189bc23af890135f3
wrapper version = 0.3.0
canonical payload = failed candidate C
```

C2形成后可以准备 offline wrapper archive/manifest，但不得 live update。

预计 repaired wrapper distribution version使用下一合法 semver patch（当前预期 `0.3.1`），canonical Research Authoring payload仍为 `research-writing 0.3 @ C2`。真正 mutation前必须重新读取 live metadata/current release id；不得把当前 release id当未来并发 guard硬编码。

当 final G4需要 live C2 wrapper时，必须向用户请求一次 bounded authorization，仅覆盖：
- exact existing plugin id；
- PRIVATE / USER-scope / skills-only guarded update；
- exact C2 archive；
- no MCP/connector/renderer runtime；
- no public listing；
- no unrelated plugin mutation。

没有授权：
`G4=WAITING_USER_PLUGIN_UPDATE_AUTHORIZATION`

不得换分发路线。

## 10. Failure semantics

### Implementation failure before C2

在批准范围内正常修复 config/test/generator问题并重跑对应 regression。

如果必须修改 canonical core/report source、paper/litcite、profile、renderer或其他 owner：
停止并返回 Planner/Critic。

### Development replay still renders

如果 repaired generated report aggregate 已经被 candidate runtime实际消费，但仍执行 PDF compile/render：
停止，不形成 C2 final candidate；这反证 aggregate-only repair不足，需要重新归因。

如果 aggregate根本没有被消费：
停止并记录 normal-entry loading evidence；不得通过给 replay prompt加 blacklist让测试变绿。

### C2 final Gate failure

任何 final Gate在 C2失败：
- 记录真实 FAIL；
- 不换题、换 delta、追加赢家；
- 若修改 product -> 新 candidate，旧 final evidence stale；
- 不跨 candidate拼 PASS。

### Plugin update blocked

保持 `WAITING_USER_PLUGIN_UPDATE_AUTHORIZATION` 或真实平台 blocker；
不影响已经完成的 C2 source/regression truth，但 overall不能完成 G4。

## 11. Files expected to change

Production/source:

- `scripts/codex_marketplace_config.json`
- `tests/test_research_writing_routing.py`

Generated:

- current generator实际改变的 `plugins/codex/plugins/research-writing/**`
- current generator实际改变的 Marketplace parity文件

Evidence:

- `results/research-authoring--formal-production-authoring/**`
- `private/exports/research-authoring--formal-production-authoring/**`

默认其他 tracked production files不得变化。

## 12. Authorization boundary of future approved Kickoff

用户以后实际发送 execution-ready Critic逐字批准的 Kickoff后，只授权：

- 复用 exact branch/worktree；
- 上述 bounded source/test/generated repair；
- canonical generator；
- deterministic tests；
- repo-safe development replay；
- C2 candidate commit；
- task-owned ordinary non-force push；
- task-local results/private exports；
- offline C2 wrapper archive/manifest preparation；
- 到 `C2_CANDIDATE_READY` stop。

Kickoff不授权：

- Plugin Creator live update；
- new G1-G4 final execution；
- Codex final PDF；
- paid API；
- main merge/release/tag/GitHub Release；
- private/sensitive data external upload；
- force push/destructive Git；
- Bridge Kit修改；
- canonical core/report source扩大修复；
- paper/litcite/profile/renderer/Presentations/Clear Writing/Statistical Modeling生产改造；
- watcher/daemon/database/ledger/state machine。

## 13. Execution-ready Critic review

Critic必须同时审：

- 本 Plan；
- 同版 Canonical Goal；
- 同版 Kickoff Draft。

重点检查：

1. 修复是否只落在真实 report aggregate normal consumer；
2. focused tests是否验证合同而不冒充 final capability；
3. development replay是否足以在 C2 freeze前重放已知 G4-C1；
4. 是否错误修改 canonical owner source；
5. C2形成后旧 G1-G4 evidence失效范围是否正确；
6. Planner-owned final task freeze是否避免 Executor挑赢家；
7. frozen G4 rubric/task/baseline是否保持不变；
8. live Plugin update是否仍有独立用户授权门；
9. version/README/changelog是否没有虚假 bump；
10. Kickoff授权是否只到 C2 candidate stop。

只有同版 execution package得到 Critic PASS后才：

`READY_FOR_CODEX=YES`

否则保持：

`READY_FOR_CODEX=NO`
