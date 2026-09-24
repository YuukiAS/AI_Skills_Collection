# Project Thread Handoff Recovery — Implementation Plan v0.1

日期：2026-09-24  
状态：READY_FOR_EXECUTION_CRITIC_REVIEW  
Task key：`science-communication--project-thread-handoff-recovery`  
Human label：Project Thread Handoff V0.2 same-Project recovery refinement  
Approved design：`docs/design/PROJECT_THREAD_HANDOFF_V5_RECOVERY_PROPOSAL_2026-09-24.md` V5  
Approved design commit：`df0ca1ab809cf53b0d14901782bbf1a0d8a70642`  
Planning source baseline：`main@cf17aa69af0bcd21ccbd2f7d187c8ae3e52f7417`  
Canonical Goal：`docs/goals/PROJECT_THREAD_HANDOFF_RECOVERY_GOAL_V0_1.md` v0.1  
Kickoff Draft：`docs/operations/prompts/PROJECT_THREAD_HANDOFF_RECOVERY_KICKOFF_V0_1.md` v0.1

本 Plan 只把已获 `PRE_IMPLEMENTATION_DESIGN_PASS=YES` 的 V5 设计冻结成 execution contract。
它不重新设计一个 Skill / 双模式、PTH-06 provenance、G1/G2/G3、version、wrapper、icon 或 privacy
边界。只有独立 Critic 对 Proposal + Plan + Goal + Kickoff 同版给出 `READY_FOR_CODEX=YES`，
且用户随后实际发送 approved Kickoff，才允许 Executor 开始 implementation。

## 1. Latest-main preflight

从 approved V5 commit `df0ca1a...` 到本 Plan planning baseline 的 main drift 已做 targeted compare：
只存在与 Project Thread Handoff 无直接 overlap 的其他 task design/TODO docs；没有 PTH production
source/version/icon/distribution、Skill authoring、Planner/Critic contract、Capability Gate policy 或
version-policy overlap，因此 V5 authority继续有效。

Executor kickoff 时必须：

1. `git fetch origin main`；
2. targeted compare approved V5 / package baseline / current `origin/main`；
3. 若仅无关 docs/TODO/evidence drift，继续；
4. 若出现 Project Thread Handoff source/version/icon/distribution、Skill metadata contract、
   repository version slot 或 generated-layer直接 overlap，停止并回 Planner/Critic。

## 2. Exact execution identity

Exact task key：

`science-communication--project-thread-handoff-recovery`

Exact reviewed branch：

`reviewed/science-communication--project-thread-handoff-recovery`

Exact task-owned worktree：

`../AI_Skills_Collection-science-communication-project-thread-handoff-recovery`

解析要求：

- 以 verified canonical `AI_Skills_Collection` checkout root 为基准；
- canonical root 先用 `git rev-parse --show-toplevel` 与 origin identity核实；
- worktree 必须解析为 canonical root 父目录下 exact sibling；
- 已存在时只有 repo identity + exact reviewed branch 都匹配才可复用；
- 不允许 `/tmp` clone、备用 branch、第二个 worktree 或 silently reuse dirty main。

### Known Host/sandbox recovery

当前环境历史上出现过：即使 current-user Kickoff 已授权 exact sibling worktree，
raw `git worktree add` 仍可能因 Host sandbox escalation 被 Auto-review拒绝。

因此：

- Executor先走当前 Host Policy允许的正常 exact worktree path；
- 不允许改 branch/path、`danger-full-access`、remote remap、临时 clone绕过；
- 若平台仍拒绝 exact sibling worktree creation，记录
  `NEEDS_HUMAN_WORKTREE_BOOTSTRAP`，停止 dependent implementation；
- 给用户一条 exact 命令，让用户在 Codex sandbox外创建 frozen worktree；
- 用户创建后从同一个 task/resume point继续，不重新规划、不重新索权；
- 该手工 bootstrap 只是环境恢复，不改变 V5 product architecture。

Bridge 的 bounded reviewed-worktree helper 若在执行时已经正式发布且当前 Host Policy支持，可使用；
否则不得把未来 TODO当现有能力。

## 3. Owner / evidence paths

Implementation owner：Codex Executor on exact task branch/worktree。  
Design authority：V5 Proposal @ `df0ca1a...`。  
Independent review owner：独立 Critic thread。  
Target-surface acceptance owner：用户当前 Pro ChatGPT account + 当前 `AI Research Stack` Project。

Evidence paths：

```text
results/science-communication--project-thread-handoff-recovery/result.md
results/science-communication--project-thread-handoff-recovery/MANIFEST.md
results/science-communication--project-thread-handoff-recovery/target-surface-acceptance.md
results/science-communication--project-thread-handoff-recovery/review.md
```

不得提交真实旧 thread全文、private Plugin URL/ID、完整 private recovery output 或 unrelated Memory Sources。

## 4. Production source scope

允许修改：

```text
skills/science/communication/project-thread-handoff/SKILL.md
skills/science/communication/project-thread-handoff/agents/openai.yaml
skills/science/communication/project-thread-handoff/evals/trigger_queries.json
tests/test_project_thread_handoff_contract.py
tests/fixtures/project_thread_handoff/              # public-safe only
docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md
tests/test_standalone_skill_baselines.py
```

Canonical icon：

`skills/science/communication/project-thread-handoff/assets/app-facing.svg`

必须保持 bytes 不变。需要 redesign 时停止回 Planner/Critic。

按现有 source-first generator 更新必要 generated layer：

- `registry.json`
- `docs/SKILL_CATALOG.md`
- `docs/domains/research-communication.md`
- `docs/SKILL_PROVENANCE.md`
- `docs/skill_provenance_audit.json`
- 其他当前 generator 实际要求的 parity files

Version/docs closure允许：

- `VERSION`
- `setup.py` / registry top-level version等 existing parity owner
- `README.md`
- `CHANGELOG.md`

不修改任何中央 Marketplace Plugin production source。

## 5. Skill behavior contract

### 5.1 Mode A — current-thread handoff

保持 V0.1：

- explicit invocation；
- consume current thread；
- latest explicit user/frozen decision > assistant brainstorming；
- preserve thread-only delta；
- entity-role disambiguation；
- canonical facts -> locators；
- exactly one copy-ready initialization Prompt；
- no second confirmation；
- no repo write。

### 5.2 Mode B — same-Project recovery

新增：

- 用户在同一 ChatGPT Project新 thread显式调用 recovery；
- old thread可以已满/不可发送；
- title/topic/date/unique phrase/project clue/distinctive correction只是
  past-chat retrieval / candidate-identification clues；
- 不发明 deterministic conversation database API；
- 找到 target same-Project old conversation后恢复 semantic continuation state；
- current new thread直接 hydrate；
- `Recover X and continue Y` 时，同一回复在 bounded recovery后继续 Y；
- 不要求用户重贴完整历史；
- 不额外生成一份 Prompt再贴回当前 thread。

## 6. PTH-06 provenance contract

### 6.1 Authority criterion

底层机制是否叫 Memory 不决定 authority。Strong Mode B 的关键标准是：

> route-changing recovered claim 能否归因到 identifiable target past chat。

合法 evidence包括当前 product surface正式暴露的：

- target past chat in Memory Sources / Sources；
- identifiable target conversation source card；
- target chat title/link/source locator；
- equivalent past-chat provenance metadata。

### 6.2 Generic context不能替代

以下不能成为 target-thread authority：

- generic Saved Memory；
- profile summary；
- unsourced semantic recall；
- 无法归因到目标 conversation 的 remembered context；
- model prior knowledge。

至少以下必须 target-chat-backed：

- latest explicit user decision / correction；
- frozen/rejected route current status；
- entity role；
- thread-only delta；
- current open question；
- immediate next step；
- user-accepted assistant proposal。

### 6.3 Strong vs limited recovery

Strong：

关键 continuation decisions有 target past-chat backing，才允许声称 target old thread continuation state已恢复。

Limited / attribution-unverified：

- unsourced recall可作为明确标注的 limited summary；
- 不得说它是 old thread authoritative decision；
- 不得升级为 thread-only delta；
- paraphrase不冒充 quote；
- exact formula/prompt/frozen contract无 exact source时标 wording unverified；
- generic Memory不能补成 strong recovery。

若缺失的是继续任务必须依赖的关键 decision：

- bounded尝试 locator/source identification；
- 仍不能归因则 fail closed on that decision；
- 明确缺失项；
- 只有该项真正阻止继续时允许一次最小 clarification；
- 不猜 route、不形成确认循环。

## 7. Authority split

Target conversation负责：

- user decisions/corrections；
- accepted proposals；
- research/product intent；
- entity roles；
- thread-only delta；
- open questions；
- immediate next step；
- recurrence guard。

Canonical repo/artifact/results/report/Deep Research负责：

- code；
- experiment results；
- numeric facts；
- runtime facts；
- formal TODO/results/reports。

Conversation中的“准备执行”绝不能恢复成“已经完成”。

## 8. Cross-Project boundary

Mode B default boundary：

`current ChatGPT Project -> target old conversation in same Project`

不得主动恢复另一个 Project、用 Project 外 regular Chat补齐、用 Saved Memory作 cross-Project bridge，
或混合多个 Project的 thread-only delta。

Plus/Pro default-memory runtime可能暴露 Project外 context，因此“当前在 Project里”本身不算 provenance。
只接受 identifiable target same-Project conversation evidence。

Project-only memory是 optional stronger isolation，不是 V0.2前置条件；不得要求用户改设置。

## 9. Trigger / wording changes

`agents/openai.yaml` 继续：

```yaml
policy:
  allow_implicit_invocation: false
```

`SKILL.md` 不写 `allow_implicit_invocation`。

Trigger eval positive应覆盖：

- explicit Mode A；
- explicit Mode B，old thread full/unavailable；
- `Recover X and continue Y`。

negative / near-miss继续保护 ordinary summary/status/continuation、“handoff是什么意思”以及 generic Memory问题。

## 10. Public-safe deterministic regressions

Focused tests应检查：

- Skill version = `0.2`；
- read-only metadata保持；
- explicit-only metadata保持；
- Mode A single-prompt semantics仍在；
- Mode B same-Project / provenance / strong-vs-limited contract存在；
- unsourced generic Memory不能升级为 target conversation authority；
- locator clue不被描述成 deterministic conversation API；
- cross-Project default recovery禁止；
- exact quote / transcript claim边界；
- icon path不变且 bytes/hash与 baseline一致；
- plugin update prompt明确 canonical icon reuse；
- no MCP/database/history/CURRENT/browser-extension architecture；
- registry/generated record保持 read-only identity。

Public-safe fixtures至少包括：

- ambiguous target -> one minimal clarification；
- unsourced recall -> limited recovery；
- missing route-changing provenance -> fail closed；
- CAT-TRACE decision precedence；
- CardiacNexus canonical-fact recovery；
- DII/CARE Mode A regression。

Mechanical tests不能替代 G3 live provenance。

## 11. Source-first generated parity

至少执行当前 repo 等价命令：

```bash
python scripts/skills.py registry --write
python scripts/skills.py catalog --write
python scripts/audit_skill_provenance.py --write
python scripts/skills.py validate
python scripts/skills.py audit --all
python scripts/build_codex_marketplace.py --write --validate --check --path-report
python -m unittest tests.test_project_thread_handoff_contract
python -m unittest tests.test_standalone_skill_baselines
python -m unittest discover -s tests
```

Standalone Skill不得被 generator复制进中央 Marketplace Plugin topology。

## 12. Capability Gate Matrix

只保留 V5 G1/G2/G3。

### G1 — Distribution / Explicit Invocation / Visual Identity

Final candidate必须证明：

- standalone Skill `0.2` source/generated parity；
- explicit-only；
- existing PRIVATE / USER-scope personal wrapper identity preserved；
- skills-only / no MCP；
- canonical `assets/app-facing.svg` reused；
- bundled icon与 canonical source byte-equivalent；
- target Pro regular Chat正式显式 entry调用 final candidate。

### G2 — Current-Thread Handoff Regression

同一 final candidate，在 target Pro regular Chat真实长 thread运行 Mode A，证明：

- current context consumed；
- latest user/frozen decision precedence；
- entity role；
- thread-only delta；
- canonical locator；
- exactly one initialization Prompt；
- no second confirmation；
- no repo write；
- DII/CARE representative semantics不回归；
- source不 hardcode DII/CARE。

### G3 — Same-Project Recovery / Generalization + Provenance

Target：

- current user Pro；
- ChatGPT regular Chat；
- `AI Research Stack` Project；
- new thread；
- same Project target old conversation；
- preferably已因长度上限不可继续的真实 old thread；
- same final candidate；
- current verified personal-wrapper route。

真实 replay：

- target = 已存在 Bridge/SSH old thread；
- 用户不重新粘贴完整旧回答；
- 至少恢复：
  - Bridge Kit本身不依赖 SSH；
  - SSH是 publisher compatibility/safety相关 transport；
  - WSL GitHub SSH identity未配置不等于 Bridge product failure；
  - 不应只为了 gate改用户真实 HTTPS环境；
  - 当前问题更接近 compatibility acceptance/evidence。

PTH-06 strong-PASS：

- target Bridge/SSH old conversation本身作为 past-chat source / equivalent identifiable provenance出现；
- user/Reviewer可判断 source就是目标 conversation；
- generic Saved Memory/profile/unsourced recall不能替代；
- key recovered decision无 target provenance -> `G3 strong PASS = NO`。

Final claim只允许：

`target-conversation-backed semantic recovery verified; no observed cross-project substitution`

不声称 absolute isolation、every influencing factor visible、raw transcript recovery或 transcript-level fidelity。

G3另验证 unique target通常不确认、ambiguous-target fixture最多一次 clarification、canonical facts回 current
source、CAT-TRACE/CardiacNexus fixtures generalize、no DB/MCP/Bridge dependency、cross-Project contract regression，
且不要求另一个私有 Project live leakage test。

## 13. Same-final-candidate sequence

所有 release-critical gates绑定同一 final candidate commit/tree。

Development顺序：

1. implementation + focused tests；
2. generated parity/full relevant suite；
3. public-safe regression bank；
4. icon byte/hash check；
5. wrapper-update handoff准备；
6. freeze exact candidate commit；
7. ordinary non-force push exact reviewed branch；
8. remote tip verification；
9. 一次 target-surface acceptance session，在同一个 updated existing wrapper上完成 G1/G2/G3；
10. target-source provenance不足 -> G3 strong FAIL，回 Planner/Critic；
11. PASS后才进入 separate integration/release authority。

不得拼接不同 candidate 的 gate evidence。

## 14. Existing personal Plugin wrapper update

Canonical source仍是 standalone Skill。Regular Chat verified distribution是 existing PRIVATE / USER-scope /
skills-only personal Plugin wrapper。

Implementation必须更新：

`docs/operations/prompts/PROJECT_THREAD_HANDOFF_CHATGPT_PLUGIN_UPDATE.md`

使 Plugin Creator update支持：

- existing Plugin only；
- no create-new fallback；
- exact candidate source ref/commit由 acceptance handoff提供；
- bundle canonical Skill directory；
- no MCP/connector/external API/database/app/state；
- bundled `assets/app-facing.svg` 与 exact candidate source byte-equivalent；
- `composerIcon` / `logo` 优先 canonical asset；
- target明确不支持 SVG才 deterministic conversion；
- conversion记录 canonical source/hash，no redesign；
- optimistic concurrency guard继续使用 current release id；
- private Plugin ID/URL/version/release id不写 public repo。

### Candidate vs main identity

- target acceptance可从 exact reviewed final-candidate commit更新 existing wrapper；
- G1/G2/G3绑定该 exact candidate；
- 后续 main integration必须保持 canonical Skill bytes与 accepted candidate byte-equivalent；
- integration若改变 Skill bytes，target gates失效并需重新验收；
- 若 integrated source byte-equivalent，不要求仅为 main再更新一次 wrapper。

## 15. User action minimization

在用户 target-account动作前，Executor完成 source/tests/generated parity/public-safe regression/version/docs
candidate/icon hash/candidate commit/push/remote verification/wrapper update handoff inputs。

然后一次 bounded target-surface session：

1. update现有 Project Thread Handoff personal wrapper到 exact final candidate；
2. regular Chat运行 Mode A；
3. same `AI Research Stack` Project新 thread运行 Mode B Bridge/SSH recovery；
4. 观察 target past-chat source provenance；
5. 写最小 non-sensitive G1/G2/G3 receipt。

不重复安装，不创建新 Plugin。target-source provenance或 regular Chat失败时保留 FAIL并回 Planner/Critic；
不得切 Work/Codex维持 PASS。

## 16. Wrapper update authorization boundary

Public Kickoff不硬编码 private Plugin ID/URL。

用户以后发送 approved Kickoff只授权：

> 更新当前用户已经存在、且唯一匹配 Project Thread Handoff canonical Skill 的 PRIVATE / USER-scope /
> skills-only personal wrapper；禁止创建新 Plugin。

若 identity不唯一，停止并向用户一次最小选择；找不到 wrapper不等于授权新建。

Account-side update仍遵守平台正常确认；Kickoff不冒充平台确认。

## 17. Version / README / changelog

Standalone Skill：`0.1 -> 0.2`  
Repository：`5.1.0 -> 5.1.1 PATCH`  
Central Plugins：全部 `NO_BUMP`

Personal wrapper执行时读取 private current version/current release id后 compatible increment。

Version preflight：

- 修改前重读 `origin/main:VERSION`；
- 仍为 `5.1.0` -> target `5.1.1`；
- slot已被其他 release占用 -> `VERSION_DRIFT`，回 Planner，不自行猜新 target。

README：

- root standalone card更新 v0.2；
- 简短写“旧 thread已满时可在同 Project新 thread恢复”；
- wrapper不列为中央 Plugin；
- `skills/README.md` explicit check，taxonomy不变时预期 `README checked: no update required`。

CHANGELOG记录 V0.2 same-Project recovery与 provenance boundary。

## 18. Privacy

Repo evidence只允许 candidate identity、package/icon hashes、target surface/Project type、redacted old-chat
title/source locator、source type=past chat、criterion-level G1/G2/G3结果与 final claim boundary。

禁止 old thread全文、complete private recovery output、private Plugin ID/URL、unrelated Memory Sources、
Project transcript dump。

Reviewer若需要 provenance，只看最小 redacted screenshot/receipt；不得为证据运输要求用户重新跑完整 G3。

## 19. Stop conditions

必须停止并回 Planner/Critic：

- V5 architecture需要改变；
- 需要 MCP/database/transcript API/browser extension/external API；
- target regular Chat不能运行 final wrapper；
- Mode B无法使用 target same-Project past-chat source；
- key recovered decision无法取得 target provenance；
- wrapper只能通过创建新 Plugin才能更新；
- icon必须 redesign；
- integration会改变 accepted candidate Skill bytes；
- repository version不再是 5.1.0；
- 新用户可见风险无法由 G1/G2/G3覆盖。

普通 wording/test/fixture/generated parity修复在冻结语义内自行完成。

## 20. Completion semantics

Pre-target implementation完成最多报告：

`FINAL_CANDIDATE_READY_FOR_TARGET_ACCEPTANCE=YES`

只要 G1/G2/G3未对同一 final candidate全部 PASS：

`PROJECT_THREAD_HANDOFF_V0_2_READY != YES`

总体 ready还要求 independent final review + separate authorized integration/release closure，并且 integrated canonical
Skill bytes与 accepted candidate一致。
